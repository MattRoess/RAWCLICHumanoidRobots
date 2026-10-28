"""
01_schemas.py
=============

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

The schemas of this project: what the workbook defines for each category of humanoid robot, before
anything is drawn at random. Press Run. No arguments; every setting is in `src/params_schema.py`. Run
`00_parameters.py` first.

Matthias, 2026-10-26: "As far as I understand the new research there are four or five different type of
categrories for humanoid robots. Draw a repective schema and the we will go through and do separate code
for each of the different categories." The research has six categories; asked the same day, he chose to
draw all six.

WHAT IT READS
-------------
The workbook named by the setting `data.workbook` (`data/raw/humanoid_robots_2040_workbook.xlsx`), only
reading it:

  Taxonomy                  the definition of each category: what it is for, its height and mass, its
                            joints (degrees of freedom) and payload, its anchor robot (the robot whose
                            parts list stands for the category).
  Components & Materials    the parts list of each anchor robot: per part the quantity, the mass of one
                            unit and of all units (minimum, mode, maximum, in kg), the main material and
                            the evidence (Direct, Derived, Estimate); per category the sum of the parts,
                            the stated mass of the anchor robot and the difference between the two.
  Material Composition per Cat
                            the materials of each anchor robot: per material its grade, minimum, mode and
                            maximum in kg, its share of the category and its evidence; per category their sum
                            and the kilograms they leave unallocated against the parts list and against the
                            stated mass.

It also reads `data.shared_lists` (`data/researched/shared_lists.xlsx`): where every part and every material
name goes in the shared part groups, body regions and materials (decided by Matthias on 2026-10-26,
documentation/claude/SHARED_LISTS.md), and, in its sheet 'Battery cells', each robot type's battery row as cells
only. It reads `data.element_recipes` (`data/researched/element_recipes.xlsx`): the datasheets of the cells, the
compounds and the recipe of each cell down to its elements (documentation/claude/EVIDENCE.md, E1.7i to E1.7k). It
reads `data.parts_taken_apart` (`data/researched/parts_taken_apart.xlsx`): the robots of type 1, the Unitree G1, the
AgiBot X1 and the Fourier N1, part by part (EVIDENCE.md E2.8 to E2.8e, agreed by Matthias on 2026-10-27), checks that
each lies inside its type's height and mass in the sheet Taxonomy, and checks the file against the sibling projects'
files it
names (`data.vehicle_pcb_composition`, `data.vehicle_sensor_composition`, `data.data_center_element_composition`,
`data.traction_motor_magnets`), read where they lie. And it looks in `data.sources_dir`
(`documentation/sources/`) for the report of each category.

WHAT IT CHECKS
--------------
Before drawing, `check_workbook` tests that the workbook agrees with itself, `check_shared_lists` that every
part and material name is placed once, under its own name, on the shared lists, `check_element_recipes` that the
recipes hold together, `check_battery_cells` that every battery is kept or built from cells that fit its packs and
`check_parts_taken_apart` that the robots of type 1 taken apart hold together, `check_robot_types` that each lies
inside its type and `check_sibling_data` that the sibling projects' files hold what they name (the list is in
`CHECKS_DONE`):
every minimum, mode and maximum in order, every mass of all units equal to the number times the mass of one,
every sum row equal to the sum of its rows, every difference and unallocated row equal to what it should be, the
colour of every row matching its evidence, the same categories in every sheet. A fault does not stop the drawing:
it is drawn in red, listed on faults.png and counted on the overview.

WHAT IT DRAWS
-------------
Into `output.schemas_dir` (`figures/schemas/`):

  overview.png                 how the project models a humanoid robot: the stages, how every mass
                               carries its minimum, mode and maximum, the six categories with their anchor
                               robots and masses, the faults found, what is still open.
  categories/<n>_<name>.png    one page per category: its definition, the anchor robot, height and mass,
                               joints and payload, the sum of the parts against the stated mass, whether
                               it has a report; then the parts list, grouped by subsystem.
  categories/<n>_<name>_shared_lists.png
                               one page per robot type in the shared lists, for Matthias to verify the
                               placements: every part with its part group and body region, every material
                               with its shared material, bars of the kg at the mode by part group, body region
                               and material, and the number of motors. Matthias, 2026-10-26: "I need schema for
                               each of the six types of robots, so that I can verify them". Not drawn when
                               the shared lists are not on disk.
  categories/<n>_<name>_robot.png
                               the robot type in one view (Matthias, 2026-10-26: "I want theat one can
                               understand the robot and its compostion and parts in one vew"): the robot drawn
                               to its height, at the same scale on all six pages, with its parts where they sit,
                               its body regions and its motors; beside it, its materials as bars on the same kg
                               scale on all six pages. With the element recipes, the battery is drawn as cells
                               only (Matthias, 2026-10-26: "Battery materials should be the cells only in every
                               robot type"), counted from each pack's voltage and capacity, and the rest of its row
                               goes where the sheet Battery cells says. Not drawn when the shared lists are not on
                               disk.
  faults.png                   every fault found in the workbook and the shared lists, in red, or "No fault
                               found", with the list of what was checked and what was not.

The numbers are the workbook's minimum, mode and maximum, not draws. It needs no Monte Carlo run.

Where it sits: after 00_parameters.py. 02_composition.py follows it and reads the workbook, the shared lists and
the element recipes through the functions here (`read_workbook`, `read_shared_lists`, `read_element_recipes`, and
every check), so that what it draws is what these pages show.
"""

from __future__ import annotations

import math
import os
import re
import statistics
import sys
import textwrap
from dataclasses import dataclass, field

# Run from anywhere, and put the project root on the path, so that `src` imports. Must come before any
# import of src.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import matplotlib  # noqa: E402

matplotlib.use('Agg')  # draw into files only: no window opens, also in a terminal without a screen
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyArrowPatch, Rectangle  # noqa: E402
from openpyxl import load_workbook  # noqa: E402

from src.params_schema import ParameterError, Params, absolute, current  # noqa: E402

# ------------------------------------------------------------------------------------------------------
# What the overview says about the project
# ------------------------------------------------------------------------------------------------------

# The stages of the project, in the order they are run, as the overview page shows them. A test
# (tests/test_schemas.py) compares this list with the numbered files at the top of the project, so that a
# stage cannot be added without the overview saying what it does.
STAGES = [
    ('00_parameters.py', 'The settings: checks them and writes their register.'),
    ('01_schemas.py', 'What the workbook defines, before anything is drawn at random, and each robot type in '
                      'the shared lists: these pages.'),
    ('02_composition.py', 'What each robot type is made of, drawn at random (Monte Carlo): its materials, elements, '
                          'part groups and body regions, written for stock-and-flow, and a page per robot type.'),
    ('03_comparison.py', 'The robot types side by side, by material, element, part group and body region, from the '
                         'draws of 02.'),
    ('04_parts_taken_apart.py', "Robot type 1 taken apart: where its critical elements sit, kind of part by kind of "
                                "part, its two figures drawn from 02's draws of type 1 over its robots."),
]

# What check_workbook tests, in plain words, for faults.png and documentation/claude/VERIFICATION.md.
CHECKS_DONE = [
    'Every part has a number above zero and a minimum, mode and maximum for the mass of one unit and of '
    'all units.',
    'Every minimum is at most its mode, and every mode at most its maximum.',
    'For every part, the mass of all units is the number times the mass of one unit (minimum, mode and '
    'maximum).',
    "Every row's evidence is Direct, Derived or Estimate, and its colour is the one the workbook's colour "
    'key gives that evidence.',
    "For every category, the sum row equals the sum of the parts' masses and of their numbers.",
    "For every category, the difference row equals the sum's mode minus the stated mass of the anchor "
    'robot, in kg and as a share.',
    "The last row equals the sum of the categories' sum rows.",
    'The number of parts equals the number stated at the top of the sheet.',
    'The same categories, with the same numbers and names, are in all three sheets, and every category has its '
    'parts, its materials and their closing rows.',
    "Materials: every minimum is at most its mode and every mode at most its maximum; the sum row equals the sum "
    "of the materials; every share equals the material's mode over the sum's mode.",
    "Materials: the unallocated row equals the parts' sum minus the materials' sum at the mode, and the stated "
    "mass minus the materials' sum.",
    'Shared lists: every part of the workbook is placed exactly once, under its own name and robot type, in a '
    'part group and a body region of the sheet Lists; a split adds up to the units of the part; the number of '
    'motors is a whole number from 0 to the units.',
    'Shared lists: every material name of the workbook is placed exactly once, in a material of the sheet Lists.',
    "Shared lists: every material name marked 'Split' has its pieces in the sheet Splits: exactly one remainder, "
    'the shares of the others in order between 0 and 1 and their largest adding up to at most 1, each piece '
    "labelled E and in a material of the sheet Lists.",
    'Element recipes: every compound can be read and its mass shares add up to 1; every item of a recipe sits within '
    'an item of the same recipe and is a compound, another recipe or a group; no name is both a compound and a recipe, '
    'and no recipe contains itself; the items of a group are shares with exactly one remainder, in order and leaving '
    'it above zero, or alternatives whose probabilities add up to 1; every cell has its recipe, its mass and its '
    'energy.',
    "Battery cells: every robot type's battery row is kept or built from cells, not both; a kept row names the "
    "recipe its cells follow; each build's cell is in the sheet Cells, its cells in series within one cell's voltage "
    "of the pack's, its cells in parallel within 12 % of the pack's capacity, its cells at most 85 % of the packs' "
    'mass; the rest of the row has exactly one remainder, shares in order, materials of the sheet Lists, and never '
    'falls below zero where it goes to a material.',
    'Material recipes: every piece of a shared material that has recipes (so far aluminium, magnesium, plastics and '
    'fibre composites, the rest of a battery row included) has exactly one row in the sheet Rows, naming a recipe of '
    'the sheet Recipe, and every row names a piece that exists.',
    "Robot type 1 taken apart (the G1, X1 and N1): every robot named in the sheet Robots and with rows of its own on "
    'every sheet that is per robot; every min, mode and max in order, and every estimate (E) at least half to 1.5 '
    "times its mode, cut only at 100 % for a share and at 1 for a large joint's factor; every label W, S or E; every "
    'group of shares with exactly one remainder that never falls below zero; every material and body region on the '
    'shared lists; every part or component of one material, of shares, or computed; for each robot its joints adding '
    'up to its joint modules, each number once, its module masses all three or none and in order, exactly one part '
    "taking its remainder, and its own constants there; every joint in a heat group of the sheet MagnetGrades, each "
    'group a distribution over known grade classes, each class once, its probabilities adding up to 1, and used by a '
    'joint; every sensor element of a listed sensor; every shared constant there; the layout of one robot only and '
    'the old grade columns refused.',
    "Robot type 1 taken apart, against the sibling projects' files it reads where they lie: every car board category "
    'with its gold, silver, palladium, tin and nickel (RAWCLICVehicleElectronics, 04_), every car sensor type (07_), '
    "a tantalum row (RAWCLICDataCenters, 04_), every magnet grade class a heat group can draw "
    "(RAWCLICVehicleTractionMotor's element workbook).",
    "Robot type 1 taken apart, against the sheet Taxonomy: every robot's maker height and stated mass inside its "
    "type's defining limits (on this rule the Booster T1, 1.18 m, is out of type 1).",
    'The register of every known humanoid robot: every number once; a robot with types has one or two different '
    'robot types of the six, a robot without has an entry saying why (not assigned, or the same robot as an entry '
    'with types); every form known; every mass min, mode and max or none, in order; no robot of type 1 below its '
    'lowest mass (15 kg); the three robots taken apart in the parts file and of type 1.',
]

# What the checks cannot tell, said on faults.png so that "No fault found" is not read as more than it is.
NOT_CHECKED = ('The checks test whether the workbook agrees with itself, whether every part and material is '
               'placed on the shared lists, and whether the battery cells and the element recipes hold together. '
               'They do not test whether the numbers are right, which needs the sources, report by report '
               '(documentation/claude/EVIDENCE.md), nor whether a placement is right, which is Matthias\'s check of '
               'the shared-lists pages.')

# ------------------------------------------------------------------------------------------------------
# How the workbook is laid out
# ------------------------------------------------------------------------------------------------------

# The headings of the sheet 'Components & Materials' that the parse needs, by the start of their text (the
# workbook writes the unit after some of them, as in 'Per-Unit Min (kg)'). Each must start exactly one
# heading of the header row.
PART_COLUMNS = {
    'category': 'Category', 'anchor': 'BOM Anchor Robot', 'subsystem': 'Subsystem',
    'component': 'Component', 'location': 'Location', 'quantity': 'Qty',
    'unit_min': 'Per-Unit Min', 'unit_mode': 'Per-Unit Mode', 'unit_max': 'Per-Unit Max',
    'total_min': 'Total Min', 'total_mode': 'Total Mode', 'total_max': 'Total Max',
    'material': 'Primary Material', 'evidence': 'Evidence', 'sources': 'Source',
}

# The headings of the sheet 'Taxonomy' that the parse needs, by the start of their text.
TAXONOMY_COLUMNS = {
    'category': 'Category', 'definition': 'Dominant Requirement', 'height_and_mass': 'Working Boundary',
    'joints_and_payload': 'Articulation', 'anchor': 'BOM Anchor Robot',
}

# The labels in the column 'Subsystem' of the three rows that close each category's parts list, and the
# start of the label of the last row of the sheet, the sum over all categories.
SUM_ROW, STATED_MASS_ROW, DIFFERENCE_ROW = 'CATEGORY SUBTOTAL', 'REPORTED ANCHOR MASS', 'RECONCILIATION CHECK'
ALL_CATEGORIES_ROW = 'GRAND TOTAL'

# The headings of the sheet 'Material Composition per Cat' that the parse needs, by the start of their text, and
# the labels in its column 'Material Family' of the two rows that close each category's materials.
MATERIAL_COLUMNS = {
    'category': 'Category', 'family': 'Material Family', 'grade': 'Proposed Grade', 'min': 'Min',
    'mode': 'Mode', 'max': 'Max', 'share': 'Share', 'evidence': 'Evidence', 'sources': 'Source',
}
MATERIAL_SUM_ROW, UNALLOCATED_ROW = 'CATEGORY MATERIAL SUBTOTAL', 'UNALLOCATED MATERIAL RESIDUAL'

# The shared lists (data/researched/shared_lists.xlsx): its sheets and the headings of each, exactly as written.
# 'Lists' names the shared part groups, body regions and materials; 'Parts' places every part of the workbook;
# 'Materials' places every material name.
LISTS_SHEET, PARTS_SHEET, MATERIALS_SHEET = 'Lists', 'Parts', 'Materials'
LIST_HEADINGS = ['List', 'Name', 'What it holds']
PART_HEADINGS = ['Robot type', 'Row', 'Part', 'Part group', 'Body region', 'Split by units', 'Motors', 'Why']
MATERIAL_HEADINGS = ['Material name in the workbook', 'Shared material', 'Why']
PART_GROUP, BODY_REGION, MATERIAL = 'Part group', 'Body region', 'Material'
NOT_ALLOCATED = 'Not allocated'   # the shared material that holds the kilograms the materials leave out
# A material name the workbook gives for several materials together can be split by an estimate (point 9 of
# SHARED_LISTS.md): its row in 'Materials' says 'Split', and the sheet 'Splits' gives one row per piece, each a share
# of the name's kilograms (minimum, mode, maximum), one of them the remainder.
SPLITS_SHEET, SPLIT = 'Splits', 'Split'
SPLIT_HEADINGS = ['Robot type', 'Material name in the workbook', 'Shared material', 'Share min', 'Share mode',
                  'Share max', 'Remainder', 'Label', 'Basis', 'Decided']

# The battery as cells only (documentation/claude/EVIDENCE.md, E1.7d to E1.7k; decided by Matthias on 2026-10-26). The
# sheet 'Battery cells' of the shared lists says, for the battery row of each robot type, either that the workbook's
# row is kept ('Kept', naming the recipe its cells follow), or how its packs are built from cells ('Build': one row
# per way to build them, all equally likely) and where the rest of the row goes ('Rest': shares of shared materials,
# one of them the remainder; 'Not allocated' may take a rest below zero, when the cells weigh more than the row).
BATTERY_SHEET, KEPT, BUILD, REST = 'Battery cells', 'Kept', 'Build', 'Rest'
BATTERY_HEADINGS = ['Robot type', 'Battery row in the workbook', 'Kind', 'Cell or material', 'Cells in series',
                    'Cells in parallel', 'Packs', 'Pack voltage (V)', 'Pack capacity (Ah)', 'Pack energy (kWh)',
                    'Pack mass (kg)', 'Share min', 'Share mode', 'Share max', 'Remainder', 'Label', 'Basis', 'Decided']
BATTERY = 'Battery materials'   # the shared material of the workbook's battery rows
# A build's whole cells in parallel must reach the pack's stated capacity within this share (E1.7j: an estimate, E).
CAPACITY_TOLERANCE = 0.12
# A build's cells may weigh at most this share of the packs' mass, so that the BMS, wiring and enclosure still fit
# (E1.7k: the largest share of cells van de Ven et al. 2024 weighed in battery modules, laptops 85 %; an estimate, E).
CELL_SHARE_OF_PACK = 0.85

# The element recipes (data/researched/element_recipes.xlsx; EVIDENCE.md E1.7i, E1.8c, E1.9c, E1.1c to E1.1f and
# E1.2c to E1.2e, agreed by Matthias on 2026-10-26 and 2026-10-27). 'Cells' holds the datasheet of every cell a build
# uses; 'Compounds' the composition of every compound, as a formula ('LiFePO4') or as mass shares ('C 0.905; H
# 0.095'); 'Recipe' the parts of each recipe as a tree: each item
# sits within another ('' for the recipe itself) and is a compound, another recipe (named in the column 'Compound') or a
# group of items. The items of a group are either shares (minimum, mode, maximum of the group's mass, exactly one of
# them the remainder) or alternatives (each with its probability, adding up to 1), of which one is drawn. 'Rows' says
# which recipe each row of the workbook follows, for every shared material that has recipes (the battery's cells
# follow the sheet Battery cells instead).
CELLS_SHEET, COMPOUNDS_SHEET, RECIPE_SHEET, ROWS_SHEET = 'Cells', 'Compounds', 'Recipe', 'Rows'
CELL_HEADINGS = ['Cell', 'Chemistry', 'Format', 'Voltage (V)', 'Capacity (Ah)', 'Mass (g)', 'Energy (Wh)', 'Recipe',
                 'Source', 'Kind']
COMPOUND_HEADINGS = ['Compound', 'Composition', 'Basis']
RECIPE_HEADINGS = ['Recipe', 'Within', 'Item', 'Share min', 'Share mode', 'Share max', 'Remainder',
                   'Probability', 'Compound', 'Follows the energy', 'Label', 'Basis']
ROW_HEADINGS = ['Robot type', 'Material name in the workbook', 'Shared material', 'Recipe', 'Basis']
RECIPE_LABELS = {'S': 'from a source read', 'E': 'an estimate'}
# The standard atomic weight of every element the recipes name, g/mol: IUPAC, Commission on Isotopic Abundances and
# Atomic Weights, "Abridged Standard Atomic Weights 2024", https://www.ciaaw.org/abridged-atomic-weights.htm.
ATOMIC_MASS = {'H': 1.0080, 'Li': 6.94, 'B': 10.81, 'C': 12.011, 'N': 14.007, 'O': 15.999, 'F': 18.998,
               'Na': 22.990, 'Mg': 24.305, 'Al': 26.982, 'Si': 28.085, 'P': 30.974, 'S': 32.06, 'Ca': 40.078,
               'Ti': 47.867, 'Cr': 51.996, 'Mn': 54.938, 'Fe': 55.845, 'Co': 58.933, 'Ni': 58.693, 'Cu': 63.546,
               'Zn': 65.38, 'Sn': 118.71, 'Pb': 207.2}

# How the workbook marks the evidence of each row: the label in the column 'Evidence' and the fill colour
# of the row (its colour key, row 4 of 'Components & Materials': no fill, light yellow, light orange). The
# pages use the same colours, so a row looks the same in the workbook and on the page.
EVIDENCE_FILL = {'Direct': None, 'Derived': 'FFFFF2CC', 'Estimate': 'FFFCE4D6'}
EVIDENCE_COLOUR = {'Direct': '#FFFFFF', 'Derived': '#FFF2CC', 'Estimate': '#FCE4D6'}
EVIDENCE_MEANING = {
    'Direct': 'reported in a manufacturer or sensor datasheet',
    'Derived': 'calculated from other numbers (number × mass of one, a sum, or a derived input)',
    'Estimate': 'engineering reconstruction, teardown or scenario model',
}

# ------------------------------------------------------------------------------------------------------
# What is read from the workbook
# ------------------------------------------------------------------------------------------------------


class WorkbookError(Exception):
    """Raised when the workbook cannot be read at all: a sheet or a heading the parse needs is missing."""


@dataclass
class Fault:
    """One place where the workbook does not agree with itself, or a part or material is not placed right."""

    sheet: str        # the sheet of the workbook, or of the shared lists
    row: int          # the row in that sheet, as Excel numbers it; 0 when the fault is about the sheet as a whole
    text: str         # what is wrong, in plain words
    part_row: int = 0  # for a placement of the shared lists: the row of its part in 'Components & Materials'


@dataclass
class Category:
    """One category of humanoid robot, as the sheet 'Taxonomy' defines it."""

    number: int               # 1 to 6, the number the workbook gives the category
    name: str                 # the name without its number, e.g. 'Compact Research & Developer'
    definition: str           # what the category is for
    height_and_mass: str      # its working boundary, as the workbook writes it
    joints_and_payload: str   # its degrees of freedom and payload, as the workbook writes them
    anchor: str               # its anchor robot, as the workbook writes it
    row: int                  # its row in 'Taxonomy'


@dataclass
class Part:
    """One row of a parts list (sheet 'Components & Materials')."""

    row: int
    subsystem: str                      # the group of parts, e.g. 'Actuation & Power'
    component: str                      # the part, e.g. 'Knee actuator module (120 Nm class)'
    location: str                       # where in the robot, e.g. 'Knees (L/R pitch)'
    quantity: float | None              # how many of the part one robot has
    unit_kg: tuple                      # minimum, mode, maximum mass of one unit, kg (None where empty)
    total_kg: tuple                     # minimum, mode, maximum mass of all units, kg
    material: str                       # the main material, as the workbook writes it
    evidence: str                       # Direct, Derived or Estimate
    fill: str | None                    # the fill colour of the row in the workbook, None for no fill
    sources: str                        # the workbook's source references, e.g. '[S01, S12, S15]'


@dataclass
class PartsList:
    """The parts list of one category, with the three rows that close it."""

    number: int                         # the category's number
    name: str                           # the category's name as this sheet writes it, without the number
    anchor: str                         # the anchor robot as this sheet writes it
    first_row: int                      # the first row of the category in the sheet
    parts: list = field(default_factory=list)
    sum_row: int = 0                    # 0 until the row is found
    sum_quantity: float | None = None
    sum_kg: tuple = (None, None, None)
    stated_row: int = 0
    stated_mass_kg: float | None = None
    stated_evidence: str = ''
    stated_fill: str | None = None
    difference_row: int = 0
    difference_kg: float | None = None      # the workbook's difference, sum's mode minus stated mass
    difference_share: float | None = None   # the same as a share of the stated mass
    rows_with_evidence: list = field(default_factory=list)   # (row, evidence, fill) of the closing rows


@dataclass
class Material:
    """One row of a category's materials (sheet 'Material Composition per Cat')."""

    row: int
    family: str            # the workbook's name of the material, e.g. 'Aluminum alloys'
    grade: str             # the grade the workbook gives, e.g. 'Al 6061-T6 / 7075-T6'
    kg: tuple              # minimum, mode, maximum, kg (None where empty)
    share: float | None    # the workbook's share of the category's materials at the mode, 0 to 1
    evidence: str
    fill: str | None


@dataclass
class MaterialsList:
    """The materials of one category, with the two rows that close them."""

    number: int
    name: str
    first_row: int
    materials: list = field(default_factory=list)
    sum_row: int = 0
    sum_kg: tuple = (None, None, None)
    unallocated_row: int = 0
    unallocated_parts_kg: float | None = None    # the parts' sum at the mode minus the materials' sum at the mode
    unallocated_stated_kg: float | None = None   # the stated mass minus the materials' sum at the mode
    rows_with_evidence: list = field(default_factory=list)


@dataclass
class Workbook:
    """Everything 01 reads from the workbook."""

    categories: list            # Category, in the order of 'Taxonomy'
    parts_lists: dict           # category number -> PartsList
    all_row: int                # the row of the sum over all categories, 0 if the sheet has none
    all_quantity: float | None
    all_kg: tuple
    stated_part_count: int | None   # the number of parts the top of the sheet states ('COVERAGE: 68 ...')
    faults: list                # Fault, found while reading
    materials_lists: dict = field(default_factory=dict)   # category number -> MaterialsList


@dataclass
class Placement:
    """Where one part of the workbook goes in the shared lists (sheet 'Parts' of shared_lists.xlsx)."""

    row: int               # the row in the sheet 'Parts'
    robot: int             # the robot type the shared lists give the part
    part_row: int          # the row of the part in 'Components & Materials'
    part: str              # the name of the part, as the shared lists write it
    group: str             # its part group
    region: str            # its body region, '' when it is split
    split: dict            # body region -> units, for a part split by the units its location names
    motors: float | None   # how many electric motors the part holds
    why: str               # why it sits there, with the point of SHARED_LISTS.md that decided it


@dataclass
class SplitPiece:
    """One piece of a material name split by an estimate (sheet 'Splits' of shared_lists.xlsx)."""

    row: int               # the row in the sheet 'Splits'
    robot: int             # the robot type the row gives
    shared: str            # the shared material of the piece
    share: tuple           # its share of the name's kilograms: minimum, mode, maximum (None for the remainder)
    remainder: bool        # True for the piece that takes 1 minus the shares of the others
    label: str             # 'E': an estimate
    basis: str             # how the shares were found


@dataclass
class BatteryRow:
    """One row of the sheet 'Battery cells' of shared_lists.xlsx: a robot type's battery row kept, one way to build
    its packs from cells, or one place the rest of the row goes."""

    row: int                 # the row in the sheet 'Battery cells'
    robot: int               # the robot type
    family: str              # the battery row's material name in the workbook, e.g. 'Battery constituents'
    kind: str                # 'Kept', 'Build' or 'Rest'
    name: str                # a build's cell (sheet Cells of element_recipes.xlsx), the recipe a kept row's cells
                             # follow (sheet Recipe), or the shared material of a rest
    series: float | None     # a build: cells in series in one pack
    parallel: float | None   # a build: cells in parallel in one pack
    packs: float | None      # a build: how many packs the robot carries
    volts: float | None      # a build: the pack's voltage, as the sources state it
    amp_hours: float | None  # a build: the pack's capacity, as the sources state it
    kwh: float | None        # a build without voltage and capacity: the energy of all packs, kWh
    pack_kg: float | None    # a build: the mass of all packs, kg, where the parts list gives it
    share: tuple             # a rest: its share of the rest, minimum, mode, maximum (None for the remainder)
    remainder: bool          # a rest: True for the piece that takes 1 minus the shares of the others
    label: str               # 'E': an estimate
    basis: str               # how it was found


@dataclass
class SharedLists:
    """Everything 01 reads from shared_lists.xlsx."""

    names: dict            # 'Part group', 'Body region', 'Material' -> the names of that list, in order
    parts: dict            # row of the part in 'Components & Materials' -> Placement
    materials: dict        # material name of the workbook -> (shared material, why, row in the sheet 'Materials')
    faults: list           # Fault, found while reading
    splits: dict = field(default_factory=dict)   # material name of the workbook -> [SplitPiece], from 'Splits'
    battery: list | None = None                  # BatteryRow, from 'Battery cells'; None when the sheet is not there


@dataclass
class Cell:
    """One cell's datasheet (sheet 'Cells' of element_recipes.xlsx)."""

    row: int
    name: str
    chemistry: str
    volts: float | None       # nominal voltage
    amp_hours: float | None   # capacity, as the datasheet states it
    grams: float | None       # mass of one cell
    energy_wh: float | None   # energy of one cell: voltage × capacity, or as given where those are not
    recipe: str               # the cell recipe of the sheet 'Recipe' that its elements follow


@dataclass
class RecipeItem:
    """One item of a cell recipe (sheet 'Recipe' of element_recipes.xlsx)."""

    row: int
    recipe: str               # the recipe, e.g. 'NMC cylindrical' or 'PA66-GF'
    within: str               # the item it is part of; '' for the cell itself
    item: str                 # its name, unique within the recipe
    share: tuple              # its share of what it is within: minimum, mode, maximum (None for a remainder)
    remainder: bool           # True for the item that takes 1 minus the shares of the others
    probability: float | None # for an alternative: how likely it is drawn
    compound: str             # the compound, or the other recipe, it is made of; '' for a group of items
    follows_energy: bool      # its share rises and falls with the cell's energy per kg (E1.7i)
    label: str                # 'S' from a source read, 'E' an estimate
    basis: str


@dataclass
class MaterialRow:
    """Which recipe one row of the workbook follows (sheet 'Rows' of element_recipes.xlsx)."""

    row: int                  # the row in the sheet 'Rows'
    robot: int                # the robot type
    family: str               # the material name in the workbook, e.g. 'Engineering polymers'
    shared: str               # its shared material, e.g. 'Plastics'
    recipe: str               # the recipe of the sheet 'Recipe' it follows
    basis: str


@dataclass
class ElementRecipes:
    """Everything 01 reads from element_recipes.xlsx."""

    cells: dict               # cell name -> Cell
    compounds: dict           # compound name -> (composition as written, row in the sheet 'Compounds')
    items: list               # RecipeItem, in the order of the sheet
    faults: list              # Fault, found while reading
    rows: list | None = None  # MaterialRow, from 'Rows'; None when the sheet is not there


def number(value) -> float | None:
    """A cell as a number, or None for an empty cell, a dash ('—' stands for 'not applicable') or text."""
    if value is None or isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    try:
        return float(str(value).strip())
    except ValueError:
        return None


def text(value) -> str:
    """A cell as text, without the spaces at its ends; '' for an empty cell."""
    return '' if value is None else str(value).strip()


def numbered(value) -> tuple[int, str] | None:
    """'3. Industrial Logistics & Warehousing' -> (3, 'Industrial Logistics & Warehousing'); else None."""
    match = re.match(r'^(\d+)\.\s*(.+)$', text(value), re.S)
    return (int(match.group(1)), match.group(2).strip()) if match else None


def fill_of(cell) -> str | None:
    """The fill colour of a cell as ARGB text ('FFFFF2CC'), None for no fill or a white fill."""
    if cell.fill is None or cell.fill.fill_type != 'solid':
        return None
    colour = cell.fill.fgColor.rgb
    return None if not isinstance(colour, str) or colour.upper() in ('FFFFFFFF', '00000000') else colour.upper()


def find_header(sheet, first: str, needed: dict) -> tuple[int, dict]:
    """The row of a table's header (its first cell is `first`) and the column of each needed heading."""
    for row in sheet.iter_rows():
        if text(row[0].value) != first:
            continue
        columns = {}
        for key, start in needed.items():
            matches = [cell.column for cell in row if text(cell.value).startswith(start)]
            if len(matches) != 1:
                raise WorkbookError(f"sheet '{sheet.title}', row {row[0].row}: {len(matches)} headings "
                                    f"start with '{start}', where the schema needs exactly one.")
            columns[key] = matches[0]
        return row[0].row, columns
    raise WorkbookError(f"sheet '{sheet.title}': no header row whose first cell is '{first}'.")


def read_taxonomy(sheet) -> list[Category]:
    """The categories of the sheet 'Taxonomy': one per row after the header, until the first empty row."""
    header, columns = find_header(sheet, 'Category', TAXONOMY_COLUMNS)
    categories = []
    for row in sheet.iter_rows(min_row=header + 1):
        cell = {key: row[column - 1].value for key, column in columns.items()}
        named = numbered(cell['category'])
        if named is None:
            break  # the first table ends here; the sheet's second table (emphasis by category) is not read
        categories.append(Category(number=named[0], name=named[1], definition=text(cell['definition']),
                                   height_and_mass=text(cell['height_and_mass']),
                                   joints_and_payload=text(cell['joints_and_payload']),
                                   anchor=text(cell['anchor']), row=row[0].row))
    return categories


def read_parts(sheet) -> tuple:
    """The parts lists of the sheet 'Components & Materials', the sum over all categories, the stated
    number of parts and the faults met while reading."""
    header, columns = find_header(sheet, 'Category', PART_COLUMNS)
    faults, lists = [], {}
    all_row, all_quantity, all_kg = 0, None, (None, None, None)

    # The top of the sheet states how many parts it lists: 'COVERAGE: 68 leaf component assemblies ...'.
    stated_part_count = None
    for row in sheet.iter_rows(max_row=header - 1):
        found = re.search(r'COVERAGE:\s*(\d+)', text(row[0].value))
        if found:
            stated_part_count = int(found.group(1))

    for row in sheet.iter_rows(min_row=header + 1):
        cell = {key: row[column - 1].value for key, column in columns.items()}
        if all(value is None for value in cell.values()):
            continue
        r = row[0].row
        label = text(cell['subsystem'])
        unit = (number(cell['unit_min']), number(cell['unit_mode']), number(cell['unit_max']))
        total = (number(cell['total_min']), number(cell['total_mode']), number(cell['total_max']))
        evidence = text(cell['evidence'])
        fill = fill_of(row[columns['component'] - 1])

        if label.upper().startswith(ALL_CATEGORIES_ROW):
            all_row, all_quantity, all_kg = r, number(cell['quantity']), total
            continue

        named = numbered(cell['category'])
        if named is None:
            faults.append(Fault(sheet.title, r, f"the category '{text(cell['category'])}' has no number "
                                                '("1." to "6.") in front of its name.'))
            continue
        parts_list = lists.setdefault(named[0], PartsList(number=named[0], name=named[1],
                                                          anchor=text(cell['anchor']), first_row=r))

        if label == SUM_ROW:
            parts_list.sum_row, parts_list.sum_quantity, parts_list.sum_kg = r, number(cell['quantity']), total
        elif label == STATED_MASS_ROW:
            parts_list.stated_row, parts_list.stated_mass_kg = r, total[1]
            parts_list.stated_evidence, parts_list.stated_fill = evidence, fill
        elif label == DIFFERENCE_ROW:
            # The difference row writes the difference in kg in the column 'Total Mode' and the share of
            # the stated mass in the column 'Total Max' (the workbook's note on the row says so).
            parts_list.difference_row, parts_list.difference_kg, parts_list.difference_share = r, total[1], total[2]
        else:
            parts_list.parts.append(Part(row=r, subsystem=label, component=text(cell['component']),
                                         location=text(cell['location']), quantity=number(cell['quantity']),
                                         unit_kg=unit, total_kg=total, material=text(cell['material']),
                                         evidence=evidence, fill=fill, sources=text(cell['sources'])))
            continue
        parts_list.rows_with_evidence.append((r, evidence, fill))
    return lists, all_row, all_quantity, all_kg, stated_part_count, faults


def read_materials(sheet) -> tuple[dict, list]:
    """The materials of each category (sheet 'Material Composition per Cat') and the faults met reading them."""
    header, columns = find_header(sheet, 'Category', MATERIAL_COLUMNS)
    lists, faults = {}, []
    for row in sheet.iter_rows(min_row=header + 1):
        cell = {key: row[column - 1].value for key, column in columns.items()}
        if all(value is None for value in cell.values()):
            continue
        r = row[0].row
        named = numbered(cell['category'])
        if named is None:
            faults.append(Fault(sheet.title, r, f"the category '{text(cell['category'])}' has no number "
                                                '("1." to "6.") in front of its name.'))
            continue
        materials = lists.setdefault(named[0], MaterialsList(number=named[0], name=named[1], first_row=r))
        family, evidence = text(cell['family']), text(cell['evidence'])
        kg_ = (number(cell['min']), number(cell['mode']), number(cell['max']))
        fill = fill_of(row[columns['family'] - 1])
        if family == MATERIAL_SUM_ROW:
            materials.sum_row, materials.sum_kg = r, kg_
        elif family == UNALLOCATED_ROW:
            # The unallocated row writes the gap to the parts list in the column 'Mode (kg)' and the gap to the
            # stated mass in the column 'Max (kg)' (the workbook's note on the row: "Col G = Gap vs BOM; Col H =
            # Gap vs Stated Mass").
            materials.unallocated_row = r
            materials.unallocated_parts_kg, materials.unallocated_stated_kg = kg_[1], kg_[2]
        else:
            materials.materials.append(Material(row=r, family=family, grade=text(cell['grade']), kg=kg_,
                                                share=number(cell['share']), evidence=evidence, fill=fill))
            continue
        materials.rows_with_evidence.append((r, evidence, fill))
    return lists, faults


def read_workbook(path: str, params: Params) -> Workbook:
    """Read the categories, the parts lists and the materials from the workbook; never writes to it."""
    if not os.path.exists(path):
        raise WorkbookError(f'{path}: the workbook is not there. 00_parameters.py says which input files '
                            'are on disk.')
    book = load_workbook(path, data_only=True)  # data_only: the values Excel computed, not the formulas
    for name in (params.data.taxonomy_sheet, params.data.components_sheet, params.data.materials_sheet):
        if name not in book.sheetnames:
            raise WorkbookError(f"{path}: no sheet '{name}'. Its sheets are: {', '.join(book.sheetnames)}.")
    categories = read_taxonomy(book[params.data.taxonomy_sheet])
    lists, all_row, all_quantity, all_kg, stated, faults = read_parts(book[params.data.components_sheet])
    materials, material_faults = read_materials(book[params.data.materials_sheet])
    return Workbook(categories, lists, all_row, all_quantity, all_kg, stated, faults + material_faults,
                    materials)


def read_shared_lists(path: str) -> SharedLists:
    """Read the shared lists (data/researched/shared_lists.xlsx); never writes to them."""
    if not os.path.exists(path):
        raise WorkbookError(f'{path}: the shared lists are not there.')
    book = load_workbook(path, data_only=True)
    sheets = {}
    for name, headings in ((LISTS_SHEET, LIST_HEADINGS), (PARTS_SHEET, PART_HEADINGS),
                           (MATERIALS_SHEET, MATERIAL_HEADINGS)):
        if name not in book.sheetnames:
            raise WorkbookError(f"{path}: no sheet '{name}'. Its sheets are: {', '.join(book.sheetnames)}.")
        found = [text(cell.value) for cell in book[name][1]][:len(headings)]
        if found != headings:
            raise WorkbookError(f"{path}, sheet '{name}': the first row must be {headings}, not {found}.")
        sheets[name] = [(row[0].row, [cell.value for cell in row]) for row in book[name].iter_rows(min_row=2)
                        if any(cell.value is not None for cell in row)]
    where = f'{os.path.basename(path)}: '
    faults, names = [], {PART_GROUP: [], BODY_REGION: [], MATERIAL: []}
    for r, (kind, name, _) in ((r, values[:3]) for r, values in sheets[LISTS_SHEET]):
        if text(kind) not in names:
            faults.append(Fault(where + LISTS_SHEET, r, f"'{text(kind)}' is not one of {', '.join(names)}."))
        else:
            names[text(kind)].append(text(name))

    parts = {}
    for r, values in sheets[PARTS_SHEET]:
        robot, part_row, part, group, region, split, motors, why = (values + [None] * 8)[:8]
        units = {}
        for item in filter(None, (piece.strip() for piece in text(split).split(';'))):
            found = re.match(r'^(.+?)\s+(\d+(?:\.\d+)?)$', item)
            if found:
                units[found.group(1).strip()] = float(found.group(2))
            else:
                faults.append(Fault(where + PARTS_SHEET, r, f"the split '{item}' is not a region and a number "
                                                            "of units, as in 'Legs 4'."))
        placement = Placement(row=r, robot=int(number(robot) or 0), part_row=int(number(part_row) or 0),
                              part=text(part), group=text(group), region=text(region), split=units,
                              motors=number(motors), why=text(why))
        if placement.part_row in parts:
            faults.append(Fault(where + PARTS_SHEET, r, f'the part of row {placement.part_row} is placed a second '
                                                        f'time (first in row {parts[placement.part_row].row}).',
                                placement.part_row))
            continue
        parts[placement.part_row] = placement

    materials = {}
    for r, values in sheets[MATERIALS_SHEET]:
        name, shared, why = (values + [None] * 3)[:3]
        if text(name) in materials:
            faults.append(Fault(where + MATERIALS_SHEET, r, f"the material name '{text(name)}' is placed a second "
                                                            f'time (first in row {materials[text(name)][2]}).'))
            continue
        materials[text(name)] = (text(shared), text(why), r)

    # The splits by estimate, when the sheet is there.
    splits = {}
    if SPLITS_SHEET in book.sheetnames:
        found = [text(cell.value) for cell in book[SPLITS_SHEET][1]][:len(SPLIT_HEADINGS)]
        if found != SPLIT_HEADINGS:
            raise WorkbookError(f"{path}, sheet '{SPLITS_SHEET}': the first row must be {SPLIT_HEADINGS}, not {found}.")
        for row in book[SPLITS_SHEET].iter_rows(min_row=2):
            values = [cell.value for cell in row]
            if all(value is None for value in values):
                continue
            robot, name, shared, low, mode, high, remainder, label, basis = (values + [None] * 9)[:9]
            splits.setdefault(text(name), []).append(SplitPiece(
                row=row[0].row, robot=int(number(robot) or 0), shared=text(shared),
                share=(number(low), number(mode), number(high)), remainder=text(remainder).lower() == 'yes',
                label=text(label), basis=text(basis)))

    # The battery as cells only, when the sheet is there.
    battery = None
    if BATTERY_SHEET in book.sheetnames:
        found = [text(cell.value) for cell in book[BATTERY_SHEET][1]][:len(BATTERY_HEADINGS)]
        if found != BATTERY_HEADINGS:
            raise WorkbookError(f"{path}, sheet '{BATTERY_SHEET}': the first row must be {BATTERY_HEADINGS}, not "
                                f'{found}.')
        battery = []
        for row in book[BATTERY_SHEET].iter_rows(min_row=2):
            values = [cell.value for cell in row]
            if all(value is None for value in values):
                continue
            (robot, family, kind, name, series, parallel, packs, volts, amp_hours, kwh, pack_kg, low, mode, high,
             remainder, label, basis) = (values + [None] * 17)[:17]
            battery.append(BatteryRow(
                row=row[0].row, robot=int(number(robot) or 0), family=text(family), kind=text(kind), name=text(name),
                series=number(series), parallel=number(parallel), packs=number(packs), volts=number(volts),
                amp_hours=number(amp_hours), kwh=number(kwh), pack_kg=number(pack_kg),
                share=(number(low), number(mode), number(high)), remainder=text(remainder).lower() == 'yes',
                label=text(label), basis=text(basis)))
    return SharedLists(names, parts, materials, faults, splits, battery)


def composition(value: str) -> dict:
    """The mass share of each element of a compound: from its formula, each element's atoms times its atomic mass
    over the whole ('LiFePO4', 'SiO0.64'), or from mass shares written out ('C 0.905; H 0.095'). Raises ValueError
    for text that is neither, or for an element without an atomic mass in ATOMIC_MASS."""
    written = text(value)
    if re.fullmatch(r'\s*[A-Z][a-z]?\s+\d*\.?\d+\s*(;\s*[A-Z][a-z]?\s+\d*\.?\d+\s*)*;?\s*', written):
        return {element: float(share) for element, share in re.findall(r'([A-Z][a-z]?)\s+(\d*\.?\d+)', written)}
    if not re.fullmatch(r'([A-Z][a-z]?(\d+(\.\d+)?)?)+', written):
        raise ValueError(f"'{written}' cannot be read as a formula ('LiFePO4') or as mass shares ('C 0.9; H 0.1').")
    atoms: dict = {}
    for element, count in re.findall(r'([A-Z][a-z]?)(\d+(?:\.\d+)?)?', written):
        if element not in ATOMIC_MASS:
            raise ValueError(f"'{written}': the element '{element}' has no atomic mass in ATOMIC_MASS.")
        atoms[element] = atoms.get(element, 0) + float(count or 1)
    whole = sum(n * ATOMIC_MASS[e] for e, n in atoms.items())
    return {e: n * ATOMIC_MASS[e] / whole for e, n in atoms.items()}


def read_element_recipes(path: str) -> ElementRecipes:
    """Read the cells, the compounds and the cell recipes (data/researched/element_recipes.xlsx); never writes to
    them."""
    if not os.path.exists(path):
        raise WorkbookError(f'{path}: the element recipes are not there.')
    book = load_workbook(path, data_only=True)
    sheets = {}
    for name, headings in ((CELLS_SHEET, CELL_HEADINGS), (COMPOUNDS_SHEET, COMPOUND_HEADINGS),
                           (RECIPE_SHEET, RECIPE_HEADINGS)):
        if name not in book.sheetnames:
            raise WorkbookError(f"{path}: no sheet '{name}'. Its sheets are: {', '.join(book.sheetnames)}.")
        found = [text(cell.value) for cell in book[name][1]][:len(headings)]
        if found != headings:
            raise WorkbookError(f"{path}, sheet '{name}': the first row must be {headings}, not {found}.")
        sheets[name] = [(row[0].row, [cell.value for cell in row] + [None] * len(headings))
                        for row in book[name].iter_rows(min_row=2) if any(cell.value is not None for cell in row)]
    where = f'{os.path.basename(path)}: '
    faults, cells, compounds, items = [], {}, {}, []
    for r, values in sheets[CELLS_SHEET]:
        name, chemistry, _, volts, amp_hours, grams, energy, recipe = values[:8]
        volts, amp_hours, energy = number(volts), number(amp_hours), number(energy)
        if text(name) in cells:
            faults.append(Fault(where + CELLS_SHEET, r, f"the cell '{text(name)}' is listed a second time."))
            continue
        cells[text(name)] = Cell(row=r, name=text(name), chemistry=text(chemistry), volts=volts, amp_hours=amp_hours,
                                 grams=number(grams), recipe=text(recipe),
                                 energy_wh=volts * amp_hours if volts and amp_hours else energy)
    for r, values in sheets[COMPOUNDS_SHEET]:
        name, written = text(values[0]), text(values[1])
        if name in compounds:
            faults.append(Fault(where + COMPOUNDS_SHEET, r, f"the compound '{name}' is listed a second time."))
            continue
        compounds[name] = (written, r)
    for r, values in sheets[RECIPE_SHEET]:
        recipe, within, item, low, mode, high, remainder, probability, compound, follows, label, basis = values[:12]
        items.append(RecipeItem(row=r, recipe=text(recipe), within=text(within), item=text(item),
                                share=(number(low), number(mode), number(high)),
                                remainder=text(remainder).lower() == 'yes', probability=number(probability),
                                compound=text(compound), follows_energy=text(follows).lower() == 'yes',
                                label=text(label), basis=text(basis)))

    # Which recipe each row of the workbook follows, when the sheet is there.
    rows = None
    if ROWS_SHEET in book.sheetnames:
        found = [text(cell.value) for cell in book[ROWS_SHEET][1]][:len(ROW_HEADINGS)]
        if found != ROW_HEADINGS:
            raise WorkbookError(f"{path}, sheet '{ROWS_SHEET}': the first row must be {ROW_HEADINGS}, not {found}.")
        rows = []
        for row in book[ROWS_SHEET].iter_rows(min_row=2):
            values = [cell.value for cell in row] + [None] * 5
            if all(value is None for value in values):
                continue
            robot, family, shared, recipe, basis = values[:5]
            rows.append(MaterialRow(row=row[0].row, robot=int(number(robot) or 0), family=text(family),
                                    shared=text(shared), recipe=text(recipe), basis=text(basis)))
    return ElementRecipes(cells, compounds, items, faults, rows)


# ------------------------------------------------------------------------------------------------------
# Whether the workbook agrees with itself
# ------------------------------------------------------------------------------------------------------

WHICH = ('minimum', 'mode', 'maximum')


def kg(value: float | None) -> str:
    """A mass for a page or a fault: at most three decimals, without trailing zeros (0.409, 2.5, 35)."""
    if value is None:
        return '—'
    shown = f'{value:.3f}'.rstrip('0').rstrip('.')
    return '0' if shown in ('-0', '') else shown


def check_workbook(book: Workbook, params: Params) -> list[Fault]:
    """Every place where the workbook does not agree with itself (the checks of CHECKS_DONE)."""
    tolerance = params.checks.tolerance_kg
    sheet = params.data.components_sheet
    faults = list(book.faults)

    def close(a, b, allowed=tolerance):
        return a is not None and b is not None and abs(a - b) <= allowed

    def evidence_faults(row, evidence, fill, on=sheet):
        if evidence not in EVIDENCE_FILL:
            return [Fault(on, row, f"the evidence '{evidence}' is not one of Direct, Derived, Estimate.")]
        if fill != EVIDENCE_FILL[evidence]:
            return [Fault(on, row, f'the row is coloured {fill or "without fill"}, but its evidence, '
                                   f'{evidence}, is coloured {EVIDENCE_FILL[evidence] or "without fill"} '
                                   "in the workbook's colour key.")]
        return []

    for parts_list in book.parts_lists.values():
        n = parts_list.number
        for part in parts_list.parts:
            here = lambda what: Fault(sheet, part.row, f'{part.component}: {what}')  # noqa: E731
            if part.quantity is None or part.quantity <= 0:
                faults.append(here('the number of units is missing or not above zero.'))
            for masses, of in ((part.unit_kg, 'one unit'), (part.total_kg, 'all units')):
                if None in masses:
                    missing = ', '.join(w for w, m in zip(WHICH, masses) if m is None)
                    faults.append(here(f'the {missing} of the mass of {of} is missing.'))
                    continue
                low, mode, high = masses
                if not low <= mode <= high:
                    faults.append(here(f'the mass of {of} is not in order: minimum {kg(low)}, mode '
                                       f'{kg(mode)}, maximum {kg(high)} kg.'))
            if part.quantity is not None and None not in part.unit_kg and None not in part.total_kg:
                for which, unit, total in zip(WHICH, part.unit_kg, part.total_kg):
                    if not close(total, part.quantity * unit):
                        faults.append(here(f'the {which} mass of all units, {kg(total)} kg, is not the number '
                                           f'{kg(part.quantity)} times the mass of one, {kg(unit)} kg '
                                           f'(= {kg(part.quantity * unit)} kg).'))
            faults += evidence_faults(part.row, part.evidence, part.fill)

        for row, evidence, fill in parts_list.rows_with_evidence:
            faults += evidence_faults(row, evidence, fill)

        # The three closing rows: present, and in agreement with the parts and with each other.
        for row, label in ((parts_list.sum_row, 'sum'), (parts_list.stated_row, 'stated mass'),
                           (parts_list.difference_row, 'difference')):
            if not row:
                faults.append(Fault(sheet, parts_list.first_row, f'category {n} has no {label} row.'))
        if parts_list.sum_row:
            for i, which in enumerate(WHICH):
                parts_sum = sum(p.total_kg[i] for p in parts_list.parts if p.total_kg[i] is not None)
                if not close(parts_list.sum_kg[i], parts_sum):
                    faults.append(Fault(sheet, parts_list.sum_row,
                                        f'category {n}: the {which} of the parts adds up to {kg(parts_sum)} kg, '
                                        f'but the sum row says {kg(parts_list.sum_kg[i])} kg.'))
            units = sum(p.quantity for p in parts_list.parts if p.quantity is not None)
            if not close(parts_list.sum_quantity, units, 0):
                faults.append(Fault(sheet, parts_list.sum_row,
                                    f'category {n}: the parts add up to {kg(units)} units, but the sum row '
                                    f'says {kg(parts_list.sum_quantity)}.'))
        if parts_list.sum_row and parts_list.stated_row and parts_list.difference_row:
            stated, mode = parts_list.stated_mass_kg, parts_list.sum_kg[1]
            if stated is None or mode is None:
                faults.append(Fault(sheet, parts_list.difference_row,
                                    f'category {n}: the stated mass or the mode of the sum is missing.'))
            else:
                if not close(parts_list.difference_kg, mode - stated):
                    faults.append(Fault(sheet, parts_list.difference_row,
                                        f'category {n}: the difference row says {kg(parts_list.difference_kg)} '
                                        f'kg, but the mode of the sum minus the stated mass is '
                                        f'{kg(mode)} - {kg(stated)} = {kg(mode - stated)} kg.'))
                # The share may differ by the tolerance in kg, taken as a share of the stated mass.
                if not close(parts_list.difference_share, (mode - stated) / stated, tolerance / stated):
                    shown = ('—' if parts_list.difference_share is None
                             else f'{parts_list.difference_share:.2%}')
                    faults.append(Fault(sheet, parts_list.difference_row,
                                        f'category {n}: the difference row says {shown} of the stated mass, '
                                        f'but the difference is {(mode - stated) / stated:.2%} of it.'))

    # The last row against the six sum rows.
    if not book.all_row:
        faults.append(Fault(sheet, 0, 'the sheet has no last row with the sum over all categories.'))
    else:
        lists = book.parts_lists.values()
        for i, which in enumerate(WHICH):
            total = sum(pl.sum_kg[i] for pl in lists if pl.sum_kg[i] is not None)
            if not close(book.all_kg[i], total):
                faults.append(Fault(sheet, book.all_row,
                                    f'the {which} of the sum rows adds up to {kg(total)} kg, but the last row '
                                    f'says {kg(book.all_kg[i])} kg.'))
        units = sum(pl.sum_quantity for pl in lists if pl.sum_quantity is not None)
        if not close(book.all_quantity, units, 0):
            faults.append(Fault(sheet, book.all_row, f'the sum rows add up to {kg(units)} units, but the last '
                                                     f'row says {kg(book.all_quantity)}.'))

    # The number of parts against what the top of the sheet states.
    count = sum(len(pl.parts) for pl in book.parts_lists.values())
    if book.stated_part_count is not None and count != book.stated_part_count:
        faults.append(Fault(sheet, 0, f'the top of the sheet states {book.stated_part_count} parts, but the '
                                      f'sheet lists {count}.'))

    # The categories of the two sheets against each other.
    taxonomy = {c.number: c for c in book.categories}
    for number_, category in taxonomy.items():
        parts_list = book.parts_lists.get(number_)
        if parts_list is None:
            faults.append(Fault(params.data.taxonomy_sheet, category.row,
                                f'category {number_} is in this sheet but has no parts list in '
                                f"'{sheet}'."))
        elif parts_list.name != category.name:
            faults.append(Fault(sheet, parts_list.first_row,
                                f"category {number_} is called '{category.name}' in "
                                f"'{params.data.taxonomy_sheet}' but '{parts_list.name}' here."))
    for number_, parts_list in book.parts_lists.items():
        if number_ not in taxonomy:
            faults.append(Fault(sheet, parts_list.first_row, f"category {number_} has a parts list but is not "
                                                             f"in '{params.data.taxonomy_sheet}'."))

    # The materials of each category: in order, summed, shared out and closed as the workbook states.
    on = params.data.materials_sheet
    for materials in book.materials_lists.values():
        n = materials.number
        for m in materials.materials:
            if None in m.kg:
                faults.append(Fault(on, m.row, f'{m.family}: the minimum, mode or maximum is missing.'))
            elif not m.kg[0] <= m.kg[1] <= m.kg[2]:
                faults.append(Fault(on, m.row, f'{m.family}: not in order: minimum {kg(m.kg[0])}, mode '
                                               f'{kg(m.kg[1])}, maximum {kg(m.kg[2])} kg.'))
            faults += evidence_faults(m.row, m.evidence, m.fill, on)
        for row, evidence, fill in materials.rows_with_evidence:
            faults += evidence_faults(row, evidence, fill, on)

        if not materials.sum_row:
            faults.append(Fault(on, materials.first_row, f'category {n} has no sum row of its materials.'))
        else:
            for i, which in enumerate(WHICH):
                total = sum(m.kg[i] for m in materials.materials if m.kg[i] is not None)
                if not close(materials.sum_kg[i], total):
                    faults.append(Fault(on, materials.sum_row, f'category {n}: the {which} of the materials adds '
                                                               f'up to {kg(total)} kg, but the sum row says '
                                                               f'{kg(materials.sum_kg[i])} kg.'))
            mode = materials.sum_kg[1]
            for m in materials.materials if mode else []:
                # A share may differ by the tolerance in kg, taken as a share of the sum.
                if m.kg[1] is not None and not close(m.share, m.kg[1] / mode, tolerance / mode):
                    shown = '—' if m.share is None else f'{m.share:.2%}'
                    faults.append(Fault(on, m.row, f'{m.family}: the share says {shown}, but its mode is '
                                                   f'{m.kg[1] / mode:.2%} of the sum.'))

        parts_list = book.parts_lists.get(n)
        if not materials.unallocated_row:
            faults.append(Fault(on, materials.first_row, f'category {n} has no unallocated row.'))
        elif materials.sum_kg[1] is not None and parts_list and parts_list.sum_kg[1] is not None:
            mode = materials.sum_kg[1]
            for stated, against, against_kg in (
                    (materials.unallocated_parts_kg, "the parts' sum", parts_list.sum_kg[1]),
                    (materials.unallocated_stated_kg, 'the stated mass', parts_list.stated_mass_kg)):
                if against_kg is not None and not close(stated, against_kg - mode):
                    faults.append(Fault(on, materials.unallocated_row,
                                        f'category {n}: the unallocated row says {kg(stated)} kg against '
                                        f"{against}, but {against} minus the materials' sum is {kg(against_kg)} "
                                        f'- {kg(mode)} = {kg(against_kg - mode)} kg.'))

    for number_, category in taxonomy.items():
        materials = book.materials_lists.get(number_)
        if materials is None:
            faults.append(Fault(params.data.taxonomy_sheet, category.row,
                                f"category {number_} is in this sheet but has no materials in '{on}'."))
        elif materials.name != category.name:
            faults.append(Fault(on, materials.first_row, f"category {number_} is called '{category.name}' in "
                                                         f"'{params.data.taxonomy_sheet}' but '{materials.name}' "
                                                         'here.'))
    for number_, materials in book.materials_lists.items():
        if number_ not in taxonomy:
            faults.append(Fault(on, materials.first_row, f'category {number_} has materials but is not in '
                                                         f"'{params.data.taxonomy_sheet}'."))
    return faults


def check_shared_lists(book: Workbook, lists: SharedLists, params: Params) -> list[Fault]:
    """Every part and material name of the workbook placed exactly once, under its own name, in the shared lists
    (the last two checks of CHECKS_DONE)."""
    faults = list(lists.faults)
    where = os.path.basename(params.data.shared_lists) + ': '
    parts = {p.row: (n, p) for n, pl in book.parts_lists.items() for p in pl.parts}

    for part_row, (n, part) in parts.items():
        if part_row not in lists.parts:
            faults.append(Fault(where + PARTS_SHEET, 0, f"{part.component} (row {part_row} of "
                                                        f"'{params.data.components_sheet}'): not placed.", part_row))
    for part_row, place in lists.parts.items():
        here = lambda what: Fault(where + PARTS_SHEET, place.row, what, part_row)  # noqa: E731
        if part_row not in parts:
            faults.append(here(f'row {part_row} of the workbook is not a part.'))
            continue
        n, part = parts[part_row]
        if place.robot != n:
            faults.append(here(f'{part.component}: robot type {place.robot}, but the workbook has it in {n}.'))
        if place.part != part.component:
            faults.append(here(f"row {part_row} is '{part.component}' in the workbook, not '{place.part}'."))
        if place.group not in lists.names[PART_GROUP]:
            faults.append(here(f"{part.component}: the part group '{place.group}' is not in the sheet Lists."))
        if bool(place.region) == bool(place.split):
            faults.append(here(f'{part.component}: give either one body region or a split by units.'))
        for region in [place.region] if place.region else list(place.split):
            if region not in lists.names[BODY_REGION]:
                faults.append(here(f"{part.component}: the body region '{region}' is not in the sheet Lists."))
        if place.split and part.quantity is not None and sum(place.split.values()) != part.quantity:
            faults.append(here(f'{part.component}: the split adds up to {kg(sum(place.split.values()))} units, '
                               f'but the part has {kg(part.quantity)}.'))
        if (place.motors is None or place.motors != int(place.motors) or not
                0 <= place.motors <= (part.quantity or 0)):
            faults.append(here(f'{part.component}: the number of motors must be a whole number from 0 to its '
                               f'{kg(part.quantity)} units.'))

    names = {m.family for ml in book.materials_lists.values() for m in ml.materials}
    for name in sorted(names - set(lists.materials)):
        faults.append(Fault(where + MATERIALS_SHEET, 0, f"the material name '{name}' of "
                                                        f"'{params.data.materials_sheet}': not placed."))
    for name, (shared, _, row) in lists.materials.items():
        if name not in names:
            faults.append(Fault(where + MATERIALS_SHEET, row, f"'{name}' is not a material name of the workbook."))
        elif shared == SPLIT:
            if name not in lists.splits:
                faults.append(Fault(where + MATERIALS_SHEET, row, f"{name}: it says '{SPLIT}', but the sheet "
                                                                  f'{SPLITS_SHEET} has no rows for it.'))
        elif shared not in lists.names[MATERIAL] or shared == NOT_ALLOCATED:
            faults.append(Fault(where + MATERIALS_SHEET, row, f"{name}: the shared material '{shared}' is not a "
                                                              f'material of the sheet Lists (other than '
                                                              f"'{NOT_ALLOCATED}')."))

    # The splits by estimate: one remainder, shares in order between 0 and 1 that leave the remainder above zero,
    # each piece an estimate in a material of the sheet Lists, under the robot type of its material name.
    robot_of = {m.family: n for n, ml in book.materials_lists.items() for m in ml.materials}
    for name, pieces in lists.splits.items():
        on = where + SPLITS_SHEET
        if lists.materials.get(name, ('',))[0] != SPLIT:
            faults.append(Fault(on, pieces[0].row, f"{name}: split here, but its row in the sheet Materials does not "
                                                   f"say '{SPLIT}'."))
        remainders = [p for p in pieces if p.remainder]
        if len(remainders) != 1:
            faults.append(Fault(on, pieces[0].row, f'{name}: a split needs exactly one remainder, not '
                                                   f'{len(remainders)}.'))
        if len({p.shared for p in pieces}) != len(pieces):
            faults.append(Fault(on, pieces[0].row, f'{name}: a shared material appears twice in its split.'))
        for p in pieces:
            if p.robot != robot_of.get(name, p.robot):
                faults.append(Fault(on, p.row, f'{name}: robot type {p.robot}, but the workbook has it in '
                                               f'{robot_of[name]}.'))
            if p.shared not in lists.names[MATERIAL] or p.shared in (NOT_ALLOCATED, 'Mixed'):
                faults.append(Fault(on, p.row, f"{name}: the piece '{p.shared}' is not a material of the sheet Lists "
                                               f"(other than 'Mixed' and '{NOT_ALLOCATED}')."))
            if p.label != 'E':
                faults.append(Fault(on, p.row, f"{name}: a split is an estimate and is labelled 'E', not "
                                               f"'{p.label}'."))
            if not p.remainder and (None in p.share or not 0 <= p.share[0] <= p.share[1] <= p.share[2] <= 1):
                faults.append(Fault(on, p.row, f'{name}, {p.shared}: the shares must be in order between 0 and 1: '
                                               f"{', '.join(kg(s) for s in p.share)}."))
        largest = sum(p.share[2] for p in pieces if not p.remainder and p.share[2] is not None)
        if largest > 1:
            faults.append(Fault(on, pieces[0].row, f'{name}: the largest shares add up to {kg(largest)}, which leaves '
                                                   'the remainder below zero.'))
    return faults


def shares_faults(pieces: list, on: str, what: str) -> list[Fault]:
    """The faults of a group of shares (rows with .share, .remainder, .row): exactly one remainder; every other
    share in order between 0 and 1; their largest adding up to at most 1, so that the remainder never falls below 0."""
    remainders = [p for p in pieces if p.remainder]
    if len(remainders) != 1:
        return [Fault(on, pieces[0].row, f'{what}: a group of shares needs exactly one remainder, not '
                                         f'{len(remainders)}.')]
    faults = []
    for p in pieces:
        if not p.remainder and (None in p.share or not 0 <= p.share[0] <= p.share[1] <= p.share[2] <= 1):
            faults.append(Fault(on, p.row, f"{what}: the shares must be in order between 0 and 1: "
                                           f"{', '.join('—' if s is None else kg(s) for s in p.share)}."))
    largest = sum(p.share[2] for p in pieces if not p.remainder and p.share[2] is not None)
    if largest > 1 + 1e-9:
        faults.append(Fault(on, pieces[0].row, f'{what}: the largest shares add up to {kg(largest)}, which leaves the '
                                               'remainder below zero.'))
    return faults


def recipe_cycles(recipes: ElementRecipes) -> list[list[str]]:
    """The groups of recipes that contain themselves, directly or through others (each group once, sorted): a recipe
    may hold another recipe, but never one that holds it back."""
    holds: dict = {}
    names = {i.recipe for i in recipes.items}
    for i in recipes.items:
        if i.compound in names:
            holds.setdefault(i.recipe, set()).add(i.compound)

    def reach(start: str) -> set:
        seen, todo = set(), list(holds.get(start, ()))
        while todo:
            name = todo.pop()
            if name not in seen:
                seen.add(name)
                todo += list(holds.get(name, ()))
        return seen

    cycles = {frozenset(n for n in reach(name) if name in reach(n)) | {name} for name in names if name in reach(name)}
    return sorted(sorted(c) for c in cycles)


def check_element_recipes(recipes: ElementRecipes, params: Params) -> list[Fault]:
    """Every compound readable and adding up to 1; every recipe a tree of items whose shares are in order with one
    remainder, or whose alternatives add up to a probability of 1; every compound or recipe an item names listed, no
    name both a compound and a recipe, no recipe containing itself; every cell's recipe there."""
    faults = list(recipes.faults)
    where = os.path.basename(params.data.element_recipes) + ': '
    for name, (written, row) in recipes.compounds.items():
        try:
            total = sum(composition(written).values())
        except ValueError as error:
            faults.append(Fault(where + COMPOUNDS_SHEET, row, f'{name}: {error}'))
            continue
        if abs(total - 1) > 0.001:
            faults.append(Fault(where + COMPOUNDS_SHEET, row, f'{name}: its mass shares add up to {kg(total)}, not 1.'))

    on = where + RECIPE_SHEET
    names = {(i.recipe, i.item) for i in recipes.items}
    recipe_names = {i.recipe for i in recipes.items}
    for name in sorted(recipe_names & set(recipes.compounds)):
        faults.append(Fault(on, next(i.row for i in recipes.items if i.recipe == name),
                            f"'{name}' is both a compound and a recipe; give them different names."))
    for cycle in recipe_cycles(recipes):
        faults.append(Fault(on, 0, f"the recipes {', '.join(cycle)} contain themselves; a recipe may hold another "
                                   'recipe, but never one that holds it back.'))
    groups: dict = {}
    for i in recipes.items:
        groups.setdefault((i.recipe, i.within), []).append(i)
        if i.within and (i.recipe, i.within) not in names:
            faults.append(Fault(on, i.row, f"{i.recipe}, {i.item}: it sits within '{i.within}', which is not an item "
                                           'of this recipe.'))
        if i.compound and i.compound not in recipes.compounds and i.compound not in recipe_names:
            faults.append(Fault(on, i.row, f"{i.recipe}, {i.item}: the compound '{i.compound}' is not in the sheet "
                                           f'{COMPOUNDS_SHEET}, nor is it a recipe.'))
        if i.label not in RECIPE_LABELS:
            faults.append(Fault(on, i.row, f"{i.recipe}, {i.item}: the label must be one of "
                                           f"{', '.join(RECIPE_LABELS)}, not '{i.label}'."))
    for i in recipes.items:
        has_items = (i.recipe, i.item) in groups
        if bool(i.compound) == has_items:
            faults.append(Fault(on, i.row, f'{i.recipe}, {i.item}: give either a compound or items within it.'))
    for (recipe, within), members in groups.items():
        if within and (recipe, within) not in names:
            continue  # reported above, against the item that names it
        what = f"{recipe}, within '{within or 'the recipe itself'}'"
        alternatives = [m for m in members if m.probability is not None]
        if alternatives and len(alternatives) != len(members):
            faults.append(Fault(on, members[0].row, f'{what}: give every item a probability, or none.'))
        elif alternatives:
            total = sum(m.probability for m in alternatives)
            if abs(total - 1) > 0.001:
                faults.append(Fault(on, members[0].row, f'{what}: the probabilities add up to {kg(total)}, not 1.'))
        else:
            faults += shares_faults(members, on, what)
    for cell in recipes.cells.values():
        if cell.recipe not in {i.recipe for i in recipes.items}:
            faults.append(Fault(where + CELLS_SHEET, cell.row, f"{cell.name}: the recipe '{cell.recipe}' is not in the "
                                                               f'sheet {RECIPE_SHEET}.'))
        if not cell.grams or not cell.energy_wh:
            faults.append(Fault(where + CELLS_SHEET, cell.row, f'{cell.name}: give its mass and its voltage and '
                                                               'capacity, or its energy.'))
    return faults


def element_shares(recipes: ElementRecipes, recipe: str, choose: dict | None = None) -> dict:
    """The mass share of each element in `recipe`, with every share at its mode and each remainder 1 minus the modes of
    the others; an item that is another recipe adds that recipe's elements. Where the items of a group are
    alternatives, `choose` names the one taken (the group's name -> the item's name); without it, the first. The
    shares add up to 1. The recipes must not contain themselves (check_element_recipes)."""
    members: dict = {}
    for i in recipes.items:
        members.setdefault((i.recipe, i.within), []).append(i)

    def add(name: str, within: str, weight: float, out: dict) -> None:
        items = members.get((name, within), [])
        if items and items[0].probability is not None:
            wanted = (choose or {}).get(within, items[0].item)
            items = [next((i for i in items if i.item == wanted), items[0])]
            shares = {items[0].item: 1.0}
        else:
            others = sum(i.share[1] for i in items if not i.remainder)
            shares = {i.item: 1 - others if i.remainder else i.share[1] for i in items}
        for i in items:
            if i.compound in recipes.compounds:
                for element, share in composition(recipes.compounds[i.compound][0]).items():
                    out[element] = out.get(element, 0) + weight * shares[i.item] * share
            elif i.compound:
                add(i.compound, '', weight * shares[i.item], out)    # another recipe, from its top
            else:
                add(name, i.item, weight * shares[i.item], out)

    out: dict = {}
    add(recipe, '', 1.0, out)
    return out


def battery_row_of(materials: MaterialsList, lists: SharedLists) -> Material | None:
    """The row of a robot type's materials that the shared lists place in 'Battery materials', or None."""
    return next((m for m in materials.materials if lists.materials.get(m.family, ('',))[0] == BATTERY), None)


def cells_of(build: BatteryRow, cell: Cell) -> tuple[int, float]:
    """The number of cells of one build and their mass in kg: cells in series × in parallel × packs, or, for a build
    given by its energy, the whole cells that hold it (rounded up)."""
    if build.series:
        count = int(build.series * (build.parallel or 0) * (build.packs or 0))
    else:
        count = math.ceil(build.kwh * 1000 / cell.energy_wh - 1e-9) if build.kwh and cell.energy_wh else 0
    return count, count * (cell.grams or 0) / 1000


def battery_cells(materials: MaterialsList, lists: SharedLists, recipes: ElementRecipes) -> tuple | None:
    """The cells of one robot type in kg: the lightest build, the middle one (the median, which the pages show as the
    mode) and the heaviest. None where its battery row is kept as the workbook gives it, or has no builds."""
    builds = [b for b in (lists.battery or []) if b.robot == materials.number and b.kind == BUILD
              and b.name in recipes.cells]
    if not builds:
        return None
    masses = sorted(cells_of(b, recipes.cells[b.name])[1] for b in builds)
    return masses[0], statistics.median(masses), masses[-1]


def check_battery_cells(book: Workbook, lists: SharedLists, recipes: ElementRecipes, params: Params) -> list[Fault]:
    """Every robot type's battery row kept or built from cells (sheet 'Battery cells'): a kept row naming the recipe
    of the sheet Recipe that its cells follow (E1.7e: the NMC recipe for robot types 2 and 6); each build's cell in the
    sheet Cells, its cells in series within one cell's voltage of the pack's voltage, its cells in parallel within
    CAPACITY_TOLERANCE of the pack's capacity, its cells at most CELL_SHARE_OF_PACK of the packs' mass; the rest of the
    row split by shares with one remainder, and never below zero where it goes to a material."""
    if lists.battery is None:
        return []
    on = os.path.basename(params.data.shared_lists) + ': ' + BATTERY_SHEET
    faults = []
    rows_of: dict = {}
    for b in lists.battery:
        rows_of.setdefault(b.robot, []).append(b)
    for n, materials in book.materials_lists.items():
        battery = battery_row_of(materials, lists)
        rows = rows_of.pop(n, [])
        if battery is None:
            for b in rows:
                faults.append(Fault(on, b.row, f'robot type {n} has no material placed in {BATTERY}.'))
            continue
        if not rows:
            faults.append(Fault(on, 0, f"robot type {n}: its battery row '{battery.family}' has no row in the sheet "
                                       f"{BATTERY_SHEET}; give '{KEPT}', or its builds and where the rest goes."))
            continue
        for b in rows:
            if b.family != battery.family:
                faults.append(Fault(on, b.row, f"robot type {n}: the battery row is '{battery.family}' in the "
                                               f"workbook, not '{b.family}'."))
            if b.kind not in (KEPT, BUILD, REST):
                faults.append(Fault(on, b.row, f"robot type {n}: the kind must be {KEPT}, {BUILD} or {REST}, not "
                                               f"'{b.kind}'."))
            elif b.kind != KEPT and b.label != 'E':
                faults.append(Fault(on, b.row, f"robot type {n}, {b.name}: a build or a rest is an estimate and is "
                                               f"labelled 'E', not '{b.label}'."))
        builds = [b for b in rows if b.kind == BUILD]
        rest = [b for b in rows if b.kind == REST]
        if any(b.kind == KEPT for b in rows):
            if builds or rest:
                faults.append(Fault(on, rows[0].row, f"robot type {n}: '{battery.family}' is both kept and built."))
                continue
            for b in rows:
                if b.name not in {i.recipe for i in recipes.items}:
                    faults.append(Fault(on, b.row, f'robot type {n}: a kept battery row names the recipe its cells '
                                                   f"follow; '{b.name}' is not in the sheet {RECIPE_SHEET}."))
            continue
        if not builds or not rest:
            faults.append(Fault(on, rows[0].row, f"robot type {n}: give the builds of '{battery.family}' and where its "
                                                 'rest goes.'))
            continue
        for b in builds:
            cell = recipes.cells.get(b.name)
            if cell is None:
                faults.append(Fault(on, b.row, f"robot type {n}: the cell '{b.name}' is not in the sheet {CELLS_SHEET} "
                                               f'of {os.path.basename(params.data.element_recipes)}.'))
                continue
            if not (b.series and b.parallel and b.packs) and not (b.kwh and not b.series and not b.parallel):
                faults.append(Fault(on, b.row, f'robot type {n}, {b.name}: give the cells in series, in parallel and '
                                               'the packs, or only the pack energy.'))
                continue
            if b.series and b.volts and cell.volts and abs(b.series * cell.volts - b.volts) > cell.volts:
                faults.append(Fault(on, b.row, f'robot type {n}, {b.name}: {kg(b.series)} cells in series give '
                                               f'{kg(b.series * cell.volts)} V, more than one cell\'s voltage from the '
                                               f"pack's {kg(b.volts)} V."))
            if b.parallel and b.amp_hours and cell.amp_hours:
                off = b.parallel * cell.amp_hours / b.amp_hours - 1
                if abs(off) > CAPACITY_TOLERANCE + 1e-9:
                    faults.append(Fault(on, b.row, f'robot type {n}, {b.name}: {kg(b.parallel)} cells in parallel '
                                                   f'give {kg(b.parallel * cell.amp_hours)} Ah, which is '
                                                   f"{abs(off) * 100:.0f} % off the pack's {kg(b.amp_hours)} Ah (at "
                                                   f'most {CAPACITY_TOLERANCE * 100:.0f} %).'))
            count, mass = cells_of(b, cell)
            if b.pack_kg and mass > CELL_SHARE_OF_PACK * b.pack_kg + 1e-9:
                faults.append(Fault(on, b.row, f'robot type {n}, {b.name}: its {count} cells weigh {kg(mass)} kg, '
                                               f"more than {CELL_SHARE_OF_PACK * 100:.0f} % of the pack's "
                                               f'{kg(b.pack_kg)} kg.'))
        what = f"robot type {n}, the rest of '{battery.family}'"
        faults += shares_faults(rest, on, what)
        for b in rest:
            if b.name not in lists.names[MATERIAL] or b.name in ('Mixed', BATTERY):
                faults.append(Fault(on, b.row, f"{what}: '{b.name}' is not a material of the sheet Lists (other than "
                                               f"'Mixed' and '{BATTERY}')."))
        cells = battery_cells(materials, lists, recipes)
        if (cells and any(b.name != NOT_ALLOCATED for b in rest) and battery.kg[0] is not None
                and battery.kg[0] < cells[2] - params.checks.tolerance_kg):
            faults.append(Fault(on, rest[0].row, f'{what} can fall below zero: its minimum is {kg(battery.kg[0])} kg, '
                                                 f'its heaviest cells {kg(cells[2])} kg. Only {NOT_ALLOCATED} can take '
                                                 'a rest below zero.'))
    for n, rows in rows_of.items():
        faults.append(Fault(on, rows[0].row, f'robot type {n} is not in the workbook.'))
    return faults


def check_material_recipes(book: Workbook, lists: SharedLists, recipes: ElementRecipes,
                           params: Params) -> list[Fault]:
    """Every piece of a shared material that has recipes (a material named in the sheet Rows; so far Aluminium,
    Magnesium, Plastics and Fibre composites) has exactly one row there, naming a recipe of the sheet Recipe; and
    every row names a piece that exists. The pieces are those the robot pages draw: with the battery as cells only, so
    the rest of a battery row needs its recipe too."""
    if recipes.rows is None:
        return []
    on = os.path.basename(params.data.element_recipes) + ': ' + ROWS_SHEET
    faults = []
    covered = {r.shared for r in recipes.rows}
    pieces = {(n, family, shared) for n, ml in book.materials_lists.items()
              for shared, _, _, family in material_pieces(ml, lists, recipes) if shared in covered}
    seen: dict = {}
    for r in recipes.rows:
        key = (r.robot, r.family, r.shared)
        if key in seen:
            faults.append(Fault(on, r.row, f"robot type {r.robot}: '{r.family}' in {r.shared} has a second row "
                                           f'(first in row {seen[key]}).'))
            continue
        seen[key] = r.row
        if key not in pieces:
            faults.append(Fault(on, r.row, f"robot type {r.robot} has no piece '{r.family}' in {r.shared}."))
        if r.recipe not in {i.recipe for i in recipes.items}:
            faults.append(Fault(on, r.row, f"robot type {r.robot}, '{r.family}': the recipe '{r.recipe}' is not in the "
                                           f'sheet {RECIPE_SHEET}.'))
    for n, family, shared in sorted(pieces - set(seen)):
        faults.append(Fault(on, 0, f"robot type {n}: '{family}' in {shared} has no row in the sheet {ROWS_SHEET}."))
    return faults


# ------------------------------------------------------------------------------------------------------
# Robot type 1 taken apart (data/researched/parts_taken_apart.xlsx)
# ------------------------------------------------------------------------------------------------------
# Matthias, 2026-10-27: "the slipt into parts is just to get a deeper look into the robot, so that there is
# information on where the interesting materials are and the recycling can be optimized"; agreed in
# documentation/claude/EVIDENCE.md, E2.8 to E2.8c, and step by step from then on ("Yes. Show me the steps and then we
# move step by step through them"). Step 3: 01 reads the file and checks that it holds together. Step 2b ("Yes, build
# points 1 to 8 as specified, tests first", EVIDENCE.md E2.8e): the file holds every robot of the type, each in its
# own rows (column Robot), so that the spread between the robots of a type can be drawn ("You have just individual
# examples. The different realisations of such a type could vary on the compositon parts etc quite a bit."). Type 1 is
# the Unitree G1, the AgiBot X1 and the Fourier N1 ("No, the T1 is out of type 1 (1.18 m). Type 1 is informed by the
# G1, X1 and N1.").

# The sheets of the file and the first row of each, as written. A file without the column Robot (the layout before
# step 2b, one robot only) stops the reading: the old layout goes entirely.
APART_SHEETS = {
    'Robots': ['Robot', 'Maker', 'Type', 'Height (m)', 'Stated mass (kg)', 'Sources'],
    'Joints': ['Robot', 'Number', 'Joint', 'Joints in the robot', 'Module', 'Torque limit (N·m)',
               'Module mass, min (kg)', 'mode (kg)', 'max (kg)', 'Cooling', 'Heat group', 'Body region', 'Sources',
               'Basis'],
    # The magnets' grade classes by heat group: each group a distribution over grade classes, drawn (Matthias,
    # 2026-10-28: "Heat has to matter and so the distribution will be different depending on the joint"; "Accept as
    # proposed", EVIDENCE.md E2.11). It replaces the sheet Joints' base class and scenarios, whose headings now stop
    # the reading.
    'MagnetGrades': ['Heat group', 'Grade class', 'Probability', 'Label', 'Basis'],
    'JointParts': ['Component', 'Small joint, weighed (g)', 'Small joints not weighed: times min', 'times mode',
                   'times max', 'Material (one material only)', 'Large joint: factor min', 'factor mode', 'factor max',
                   'Why the factor', 'Label', 'Sources'],
    'Parts': ['Robot', 'Part', 'Number in the robot', "Kind (the figure's row)", 'Body region',
              'Mass of one, min (kg)', 'mode (kg)', 'max (kg)', 'Material (one material only)',
              'Remainder of, or computed from', 'Label', 'Sources'],
    'Shares': ['Part or component', 'Material', 'Grade', 'Share min', 'Share mode', 'Share max', 'Remainder', 'Label',
               'Basis'],
    'Boards': ['Robot', 'Board', 'Number in the robot', "Kind (the figure's row)", 'Body region',
               'Area of one, min (cm2)', 'mode (cm2)', 'max (cm2)', 'Mass from',
               'Car board category (RAWCLICVehicleElectronics 04_)', 'Label', 'Sources'],
    'Sensors': ['Robot', 'Sensor', 'Number in the robot', "Kind (the figure's row)", 'Body region',
                'Mass of one, min (g)', 'mode (g)', 'max (g)', 'Label', 'Sources'],
    'SensorElements': ['Sensor', 'Car sensor type (RAWCLICVehicleElectronics 07_, sheet Sensor Details)',
                       'Units in one sensor'],
    'Constants': ['Robot', 'Quantity', 'Min', 'Mode', 'Max', 'Unit', 'Label', 'Source'],
    'Sources': ['Code', 'Source', 'Link', 'What it is'],
}
# The sheets on which every robot has rows of its own. JointParts, Shares and SensorElements are one set for all
# robots: the insides of the G1's two joint designs, scaled to each joint's mass, and the elements of each sensor
# (Matthias: "We can assume, they are similar within given ranges").
APART_ROBOT_SHEETS = ('Joints', 'Parts', 'Boards', 'Sensors')
# What a label says: W weighed (China Post Securities' teardown), S from a source, E an estimate. A label may name
# more than one ('W, E': a weighed part, spread over the joints not weighed by an estimate).
APART_LABELS = {'W': 'weighed', 'S': 'from a source', 'E': 'an estimate'}
# The NdFeB grade classes of RAWCLICVehicleTractionMotor's element workbook
# (data/raw/10_MaterialElementDefinitions.xlsx, sheet PermanentMagnetNdFeB), from 80 °C (N) to 230 °C (AH), in the
# order of the heat they stand (04 draws a heat group's class along it). Whether that file holds them is checked with
# step 4.
# A heat group's probabilities may miss 1 by this much (they are written to two decimals; their sum in floating point).
PROBABILITY_TOLERANCE = 1e-9
MAGNET_CLASSES = ('N', 'M', 'H', 'SH', 'UH', 'EH', 'AH')
# The numbers the stage that draws the file needs from the sheet Constants: each robot's own, and those shared by all
# robots, given once under the robot ALL_ROBOTS.
APART_ROBOT_CONSTANTS = ('Robot mass, with battery', 'Battery voltage', 'Battery capacity',
                         'Cable length (four conductors)')
APART_SHARED_CONSTANTS = ('Board mass per cm2 (boards not weighed)', "Copper share of a board's mass",
                          'Power conductor cross-section (2 conductors)',
                          'Signal conductor cross-section (2 conductors)', 'Copper density',
                          'Insulation and jackets, per mass of copper')
ALL_ROBOTS = 'all'
# The words that mark the one part of each robot that takes its remainder (the frame), and a body region that follows
# the joints a part sits in (the encoders).
ROBOT_REMAINDER = 'the robot'
AS_THEIR_JOINTS = 'as their joints'
# An estimate (E) spans at least half to 1.5 times its mode (Matthias, 2026-10-27: "Estimates should be larger than
# known numbers"). The agreed values are written to two or three figures, so a bound may miss the exact half or 1.5
# times by this share of it before it counts as a fault (the gears' factor 1.17 against 2.33 / 2 = 1.165).
WIDTH_ROUNDING = 0.01
# A type's defining height and mass as the sheet Taxonomy writes them, e.g. 'Height: 1.20–1.45 m (defining)' and
# 'Mass: 30–50 kg (defining)'.
TYPE_HEIGHT = re.compile(r'Height:\s*~?\s*([\d.]+)\s*[–-]\s*([\d.]+)\s*m')
TYPE_MASS = re.compile(r'Mass:\s*~?\s*([\d.]+)\s*[–-]\s*([\d.]+)\s*kg')


@dataclass
class ApartRobot:
    """One robot of the sheet Robots: its maker's own height and stated mass decide its type."""

    row: int
    name: str
    maker: str
    type: int | None      # the category of the sheet Taxonomy
    height: float | None  # m, the maker's
    mass: float | None    # kg, the maker's stated mass
    sources: str


@dataclass
class Joint:
    """One joint kind of one robot (sheet Joints): the same joint on both sides of the robot, or the waist joints."""

    row: int
    robot: str
    number: int
    name: str
    count: int        # joints of this kind in the robot
    module: str       # 'small' or 'large': which of the G1's two joint designs its inside follows
    torque: float     # N·m, the torque limit of the maker's model file, or its stated peak
    module_mass: tuple    # kg of one joint, min, mode, max; (None, None, None) where JointParts give it (the G1)
    heat_group: str       # the heat group of the sheet MagnetGrades its magnets' grade class is drawn from
    region: str


@dataclass
class JointPart:
    """One component of the joint module (sheet JointParts)."""

    row: int
    name: str
    grams: float          # in the small joint China Post Securities weighed
    spread: tuple         # the small joints not weighed: times min, mode, max
    material: str         # '' when its materials are in the sheet Shares
    factor: tuple         # the large joint: the small one's grams times min, mode, max
    label: str
    sources: str


@dataclass
class ApartPart:
    """One part of the sheet Parts, a board of Boards or a sensor of Sensors, of one robot: what the checks need of
    each."""

    sheet: str
    row: int
    robot: str
    name: str
    count: float | None
    kind: str
    region: str
    bounds: tuple         # mass of one (kg), area of one (cm2) or mass of one (g): min, mode, max
    material: str         # one material, or '' (Parts only)
    computed: str         # what it is the remainder of, or computed from (Parts), or where its mass comes from (Boards)
    category: str         # the car board category (Boards only)
    label: str
    sources: str


@dataclass
class ShareRow:
    """One row of the sheet Shares; `share` and `remainder` as shares_faults reads them."""

    row: int
    item: str
    material: str
    grade: str
    share: tuple
    remainder: bool
    label: str


@dataclass
class MagnetGrade:
    """One row of the sheet MagnetGrades: a grade class of a heat group and its probability."""

    row: int
    group: str
    klass: str
    probability: float | None
    label: str


@dataclass
class PartsTakenApart:
    """Everything 01 reads from parts_taken_apart.xlsx."""

    robots: dict          # robot name -> ApartRobot
    joints: list          # Joint
    grades: list          # MagnetGrade
    joint_parts: list     # JointPart
    parts: list           # ApartPart, sheet Parts
    shares: list          # ShareRow
    boards: list          # ApartPart, sheet Boards
    sensors: list         # ApartPart, sheet Sensors
    elements: list        # (row, sensor, car sensor type, units), sheet SensorElements
    constants: dict       # robot name or ALL_ROBOTS -> {quantity -> (row, (min, mode, max), unit, label)}
    sources: dict         # code -> (row, source, link)
    faults: list          # Fault, found while reading


def read_parts_taken_apart(path: str) -> PartsTakenApart:
    """Read the file of the robots of type 1 taken apart; never writes to it. A missing file, sheet or heading stops
    the reading (WorkbookError), as with the other files 01 reads."""
    if not os.path.exists(path):
        raise WorkbookError(f'{path}: robot type 1 taken apart is not there.')
    book = load_workbook(path, data_only=True)
    rows = {}
    for name, headings in APART_SHEETS.items():
        if name not in book.sheetnames:
            raise WorkbookError(f"{path}: no sheet '{name}'. Its sheets are: {', '.join(book.sheetnames)}.")
        found = [text(cell.value) for cell in book[name][1]][:len(headings)]
        if found != headings:
            raise WorkbookError(f"{path}, sheet '{name}': the first row must be {headings}, not {found}.")
        rows[name] = [(row[0].row, [cell.value for cell in row] + [None] * len(headings))
                      for row in book[name].iter_rows(min_row=2) if any(cell.value is not None for cell in row)]
    triple_of = lambda values: tuple(number(v) for v in values)  # noqa: E731
    robots = {text(v[0]): ApartRobot(row=r, name=text(v[0]), maker=text(v[1]),
                                     type=None if number(v[2]) is None else int(number(v[2])), height=number(v[3]),
                                     mass=number(v[4]), sources=text(v[5])) for r, v in rows['Robots']}
    joints = [Joint(row=r, robot=text(v[0]), number=int(number(v[1]) or 0), name=text(v[2]),
                    count=int(number(v[3]) or 0), module=text(v[4]), torque=number(v[5]),
                    module_mass=triple_of(v[6:9]), heat_group=text(v[10]), region=text(v[11]))
              for r, v in rows['Joints']]
    grades = [MagnetGrade(row=r, group=text(v[0]), klass=text(v[1]), probability=number(v[2]), label=text(v[3]))
              for r, v in rows['MagnetGrades']]
    joint_parts = [JointPart(row=r, name=text(v[0]), grams=number(v[1]), spread=triple_of(v[2:5]),
                             material=text(v[5]), factor=triple_of(v[6:9]), label=text(v[10]), sources=text(v[11]))
                   for r, v in rows['JointParts']]
    parts = [ApartPart('Parts', r, text(v[0]), text(v[1]), number(v[2]), text(v[3]), text(v[4]), triple_of(v[5:8]),
                       text(v[8]), text(v[9]), '', text(v[10]), text(v[11])) for r, v in rows['Parts']]
    boards = [ApartPart('Boards', r, text(v[0]), text(v[1]), number(v[2]), text(v[3]), text(v[4]), triple_of(v[5:8]),
                        '', text(v[8]), text(v[9]), text(v[10]), text(v[11])) for r, v in rows['Boards']]
    sensors = [ApartPart('Sensors', r, text(v[0]), text(v[1]), number(v[2]), text(v[3]), text(v[4]),
                         triple_of(v[5:8]), '', '', '', text(v[8]), text(v[9])) for r, v in rows['Sensors']]
    shares = [ShareRow(row=r, item=text(v[0]), material=text(v[1]), grade=text(v[2]), share=triple_of(v[3:6]),
                       remainder=text(v[6]).lower() == 'yes', label=text(v[7])) for r, v in rows['Shares']]
    elements = [(r, text(v[0]), text(v[1]), number(v[2])) for r, v in rows['SensorElements']]
    constants: dict = {}
    for r, v in rows['Constants']:
        constants.setdefault(text(v[0]), {})[text(v[1])] = (r, triple_of(v[2:5]), text(v[5]), text(v[6]))
    sources = {text(v[0]): (r, text(v[1]), text(v[2])) for r, v in rows['Sources']}
    return PartsTakenApart(robots, joints, grades, joint_parts, parts, shares, boards, sensors, elements, constants,
                           sources, [])


def label_faults(on: str, row: int, what: str, label: str) -> list[Fault]:
    """A label must start with W, S or E (APART_LABELS)."""
    if re.match(r'^(W|S|E)\b', label):
        return []
    return [Fault(on, row, f"{what}: the label must start with {', '.join(APART_LABELS)}, not '{label}'.")]


def bounds_faults(on: str, row: int, what: str, bounds: tuple, estimate: bool, floor: float | None = None,
                  ceiling: float | None = None) -> list[Fault]:
    """Min, mode and max present and in order; for an estimate, at least half to 1.5 times the mode, a bound cut
    only at a stated limit (`floor`, `ceiling`)."""
    if None in bounds:
        return [Fault(on, row, f'{what}: give its min, mode and max.')]
    low, mode, high = bounds
    if not 0 <= low <= mode <= high:
        return [Fault(on, row, f'{what}: min, mode and max must be in order from 0 up: {low}, {mode}, {high}.')]
    if not estimate:
        return []
    want_low = 0.5 * mode if floor is None else max(floor, 0.5 * mode)
    want_high = 1.5 * mode if ceiling is None else min(ceiling, 1.5 * mode)
    if low > want_low * (1 + WIDTH_ROUNDING) or high < want_high * (1 - WIDTH_ROUNDING):
        return [Fault(on, row, f'{what}: an estimate must span at least half to 1.5 times its mode ({mode}), not '
                               f'{low} to {high}.')]
    return []


def region_faults(on: str, row: int, what: str, region: str, lists: SharedLists) -> list[Fault]:
    """Every body region named ('Legs 4, Arms 10' names two) is one of the shared lists, or the part follows its
    joints."""
    if region == AS_THEIR_JOINTS:
        return []
    known = set(lists.names.get('Body region', []))
    names = [re.sub(r'\s*\d+\s*$', '', piece.strip()) for piece in region.split(',') if piece.strip()]
    return [Fault(on, row, f"{what}: the body region '{n}' is not in the shared lists.") for n in names or ['']
            if n not in known]


def check_parts_taken_apart(apart: PartsTakenApart, lists: SharedLists, params: Params) -> list[Fault]:
    """Whether the robots of type 1 taken apart hold together: every robot named in the sheet Robots and with rows of
    its own on every sheet that is per robot; ranges in order and estimates wide enough, labels known, shares with one
    remainder that never falls below zero, every material and body region on the shared lists, every part either of
    one material, of shares, or computed; for each robot its joints matching its joint modules, each joint number once,
    its module masses all three given or none, one part taking its remainder, and its own constants there; every joint
    in a heat group whose grade classes are known, each once, their probabilities adding up to 1, every group used;
    every sensor element of a listed sensor, every shared constant there."""
    faults = list(apart.faults)
    where = os.path.basename(params.data.parts_taken_apart) + ': '
    materials = set(lists.names.get('Material', [])) - {NOT_ALLOCATED}

    def material_fault(on, row, what, material):
        return [] if material in materials else [Fault(on, row, f"{what}: the material '{material}' is not in the "
                                                                'shared lists.')]

    # The robots: every row names a robot of the sheet Robots, and every robot has rows of its own on every sheet that
    # is per robot (step 2b, point 6).
    on_sheet = {'Joints': apart.joints, 'Parts': apart.parts, 'Boards': apart.boards, 'Sensors': apart.sensors}
    for sheet, items in on_sheet.items():
        for item in items:
            if item.robot not in apart.robots:
                faults.append(Fault(where + sheet, item.row, f"'{item.robot}' is not in the sheet Robots."))
    for robot in apart.robots:
        for sheet in APART_ROBOT_SHEETS:
            if not any(item.robot == robot for item in on_sheet[sheet]):
                faults.append(Fault(where + sheet, 0, f'{robot} has no rows in the sheet {sheet}.'))
    for robot in apart.constants:
        if robot != ALL_ROBOTS and robot not in apart.robots:
            faults.append(Fault(where + 'Constants', 0, f"'{robot}' is not in the sheet Robots."))

    # Joints: each number once in its robot, modules and grade classes known, regions on the lists, module masses all
    # three or none and in order, each robot's counts those of its joint modules.
    on = where + 'Joints'
    seen = set()
    for j in apart.joints:
        what = f'{j.robot}, {j.number} {j.name}'
        if (j.robot, j.number) in seen:
            faults.append(Fault(on, j.row, f'{what}: the number {j.number} is given twice.'))
        seen.add((j.robot, j.number))
        if j.module not in ('small', 'large') or j.count < 1:
            faults.append(Fault(on, j.row, f"{what}: the module must be 'small' or 'large' and the joints at least 1."))
        if any(m is not None for m in j.module_mass):
            if None in j.module_mass:
                faults.append(Fault(on, j.row, f'{what}: give its module mass min, mode and max, or none (then its '
                                               'joint parts give it).'))
            elif not 0 < j.module_mass[0] <= j.module_mass[1] <= j.module_mass[2]:
                faults.append(Fault(on, j.row, f'{what}: the module mass min, mode and max must be in order from 0 up: '
                                               f'{j.module_mass}.'))
        if j.heat_group not in {g.group for g in apart.grades}:
            faults.append(Fault(on, j.row, f"{what}: its heat group '{j.heat_group}' is not in the sheet "
                                           'MagnetGrades.'))
        faults += region_faults(on, j.row, what, j.region, lists)
    for robot in apart.robots:
        modules = {p.name: p for p in apart.parts if p.robot == robot and p.name.startswith('Joint module, ')}
        for size in ('small', 'large'):
            module = modules.get(f'Joint module, {size}')
            joints = sum(j.count for j in apart.joints if j.robot == robot and j.module == size)
            if (module is None and joints) or (module is not None and module.count != joints):
                faults.append(Fault(on, 0, f'{robot}: {joints} {size} joints in the sheet Joints, but '
                                           f"{'no' if module is None else int(module.count)} {size} joint modules in "
                                           'the sheet Parts.'))

    # The magnets' grade classes by heat group: known classes, each once in its group, probabilities from 0 to 1 adding
    # up to 1, labels known, every group used by a joint.
    on = where + 'MagnetGrades'
    by_group: dict = {}
    for g in apart.grades:
        faults += label_faults(on, g.row, f'{g.group}, {g.klass}', g.label)
        if g.klass not in MAGNET_CLASSES:
            faults.append(Fault(on, g.row, f"{g.group}: the magnet grade class '{g.klass}' is not one of "
                                           f"{', '.join(MAGNET_CLASSES)}."))
        if g.klass in {x.klass for x in by_group.get(g.group, [])}:
            faults.append(Fault(on, g.row, f"{g.group}: the grade class '{g.klass}' is given twice."))
        if g.probability is None or not 0 <= g.probability <= 1:
            faults.append(Fault(on, g.row, f'{g.group}, {g.klass}: the probability must be from 0 to 1, not '
                                           f'{g.probability}.'))
        by_group.setdefault(g.group, []).append(g)
    used = {j.heat_group for j in apart.joints}
    for group, members in by_group.items():
        total = sum(g.probability for g in members if g.probability is not None)
        if abs(total - 1) > PROBABILITY_TOLERANCE:
            faults.append(Fault(on, members[0].row, f'{group}: its probabilities add up to {total:g}, not to 1.'))
        if group not in used:
            faults.append(Fault(on, members[0].row, f"the heat group '{group}' is the heat group of no joint."))

    # The joint module part by part.
    on = where + 'JointParts'
    items_with_shares = {s.item for s in apart.shares}
    for c in apart.joint_parts:
        faults += label_faults(on, c.row, c.name, c.label)
        if c.grams is None or c.grams <= 0:
            faults.append(Fault(on, c.row, f'{c.name}: give its weighed grams.'))
        faults += bounds_faults(on, c.row, f'{c.name}, the joints not weighed', c.spread, 'E' in c.label)
        if c.factor[0] is not None and c.factor[0] < 1:
            faults.append(Fault(on, c.row, f"{c.name}: the large joint's factor may not fall below 1, as a large "
                                           f"joint's part is not lighter than the small one's: {c.factor[0]}."))
        else:
            faults += bounds_faults(on, c.row, f"{c.name}, the large joint's factor", c.factor, 'E' in c.label,
                                    floor=1.0)
        if c.material:
            faults += material_fault(on, c.row, c.name, c.material)
        elif c.name not in items_with_shares:
            faults.append(Fault(on, c.row, f"'{c.name}': give its one material, or its shares in the sheet Shares."))

    # The other parts, the boards and the sensors.
    remainders: dict = {}
    for p in apart.parts + apart.boards + apart.sensors:
        on = where + p.sheet
        what = f'{p.robot}, {p.name}'
        faults += label_faults(on, p.row, what, p.label)
        faults += region_faults(on, p.row, what, p.region, lists)
        if p.count is None or p.count < 1 or p.count != int(p.count):
            faults.append(Fault(on, p.row, f'{what}: the number in the robot must be a whole number from 1 up.'))
        if p.computed.startswith(ROBOT_REMAINDER):
            remainders.setdefault(p.robot, []).append(p)
        if None in p.bounds and (p.computed or p.sheet == 'Sensors' and p.name in {e[1] for e in apart.elements}):
            pass   # computed, a remainder, or a sensor known by its elements only (the encoders)
        else:
            faults += bounds_faults(on, p.row, what, p.bounds, p.label == 'E')
        if p.sheet == 'Parts':
            if p.material:
                faults += material_fault(on, p.row, what, p.material)
            elif not p.computed and p.name not in items_with_shares:
                faults.append(Fault(on, p.row, f"'{what}': give its one material, its shares in the sheet Shares, or "
                                               'what it is computed from.'))
        if p.sheet == 'Boards' and not p.category:
            faults.append(Fault(on, p.row, f'{what}: name the car board category its metals come from.'))
    for robot in apart.robots:
        found = remainders.get(robot, [])
        if len(found) != 1:
            faults.append(Fault(where + 'Parts', 0, f'{robot}: exactly one part takes the remainder of the robot, not '
                                                    f"{len(found)}: {', '.join(p.name for p in found)}."))

    # The shares: one remainder per part, in order, never below zero, an estimate wide enough; every part named
    # exists; every material on the lists.
    on = where + 'Shares'
    names = {c.name for c in apart.joint_parts} | {p.name for p in apart.parts}
    groups: dict = {}
    for s in apart.shares:
        groups.setdefault(s.item, []).append(s)
        faults += label_faults(on, s.row, s.item, s.label)
        faults += material_fault(on, s.row, f'{s.item}, {s.material}', s.material)
    for item, members in groups.items():
        if item not in names:
            faults.append(Fault(on, members[0].row, f"'{item}' is not a component of JointParts nor a part of Parts."))
            continue
        found = shares_faults(members, on, item)
        faults += found
        if not found:
            for s in members:
                if not s.remainder:
                    faults += bounds_faults(on, s.row, f'{item}, {s.material}', s.share, s.label == 'E', ceiling=1.0)

    # The sensor elements; the constants, the shared ones once for all robots and each robot's own.
    on = where + 'SensorElements'
    sensors = {p.name for p in apart.sensors}
    for row, sensor, car_type, units in apart.elements:
        if sensor not in sensors:
            faults.append(Fault(on, row, f"'{sensor}' is not a sensor of the sheet Sensors."))
        if not car_type or units is None or units < 1 or units != int(units):
            faults.append(Fault(on, row, f'{sensor}: name the car sensor type and its units, a whole number from 1.'))
    on = where + 'Constants'
    shared = apart.constants.get(ALL_ROBOTS, {})
    for quantity in APART_SHARED_CONSTANTS:
        if quantity not in shared:
            faults.append(Fault(on, 0, f"'{quantity}' is missing (for {ALL_ROBOTS}); the stage that draws the file "
                                       'needs it.'))
    for robot in apart.robots:
        for quantity in APART_ROBOT_CONSTANTS:
            if quantity not in apart.constants.get(robot, {}):
                faults.append(Fault(on, 0, f"{robot}: '{quantity}' is missing; the stage that draws the file needs "
                                           'it.'))
    for robot, given in apart.constants.items():
        for quantity, (row, values, _, label) in given.items():
            faults += label_faults(on, row, f'{robot}, {quantity}', label)
            faults += bounds_faults(on, row, f'{robot}, {quantity}', values, label == 'E')
    return faults


def type_limits(category: Category) -> tuple | None:
    """A type's defining height (m) and mass (kg) as (low, high) pairs, read from what the sheet Taxonomy writes; None
    where they cannot be read."""
    height = TYPE_HEIGHT.search(category.height_and_mass)
    mass = TYPE_MASS.search(category.height_and_mass)
    if height is None or mass is None:
        return None
    return (float(height.group(1)), float(height.group(2))), (float(mass.group(1)), float(mass.group(2)))


def check_robot_types(apart: PartsTakenApart, categories: list) -> list[Fault]:
    """Whether every robot of the file lies inside its type: its maker's own height and stated mass inside the type's
    defining limits of the sheet Taxonomy (Matthias, 2026-10-27: "We have to see, that there is not a mixup between
    the different types"; on this rule the Booster T1, 1.18 m, was taken out of type 1)."""
    faults = []
    by_number = {c.number: c for c in categories}
    unreadable = set()
    for robot in apart.robots.values():
        on = 'Robots'
        category = by_number.get(robot.type)
        if category is None:
            faults.append(Fault(on, robot.row, f'{robot.name}: type {robot.type} is not in the sheet Taxonomy.'))
            continue
        limits = type_limits(category)
        if limits is None:
            if robot.type not in unreadable:
                first = category.height_and_mass.splitlines()[0] if category.height_and_mass else ''
                faults.append(Fault(on, robot.row, f'type {robot.type}: its height and mass limits cannot be read from '
                                                   f"the sheet Taxonomy ('{first}')."))
                unreadable.add(robot.type)
            continue
        (h_low, h_high), (m_low, m_high) = limits
        if robot.height is None or not h_low <= robot.height <= h_high:
            faults.append(Fault(on, robot.row, f'{robot.name}: {robot.height} m lies outside type {robot.type}, '
                                               f'{h_low} to {h_high} m.'))
        if robot.mass is None or not m_low <= robot.mass <= m_high:
            faults.append(Fault(on, robot.row, f'{robot.name}: {robot.mass} kg lies outside type {robot.type}, '
                                               f'{m_low} to {m_high} kg.'))
    return faults


# The sheets of the sibling projects' files and the columns read from them (step 4 of the plan): each read where it
# lies, never written. The metals a car board category must hold for the G1's boards.
SIBLING_SHEETS = {'vehicle_pcb_composition': 'PCPComposition', 'vehicle_sensor_composition': 'Sensor Details',
                  'data_center_element_composition': 'BoardsAndComponents',
                  'traction_motor_magnets': 'PermanentMagnetNdFeB'}
BOARD_METALS = ('Au', 'Ag', 'Pd', 'Sn', 'Ni')


def sibling_rows(path: str, sheet: str) -> list[dict]:
    """The rows of a sibling project's sheet as dicts by heading; read only."""
    book = load_workbook(path, read_only=True, data_only=True)
    rows = list(book[sheet].iter_rows(values_only=True))
    book.close()
    header = [text(h) for h in rows[0]]
    return [dict(zip(header, r)) for r in rows[1:] if any(v is not None for v in r)]


def check_sibling_data(apart: PartsTakenApart, params: Params) -> list[Fault]:
    """Whether the sibling projects' files hold what the robots of type 1 taken apart name: every car board category
    with the metals of BOARD_METALS (RAWCLICVehicleElectronics, 04_), every car sensor type (07_), a tantalum row
    (RAWCLICDataCenters, 04_), every magnet grade class a heat group can draw (RAWCLICVehicleTractionMotor's element
    workbook)."""
    faults, rows = [], {}
    for key, sheet in SIBLING_SHEETS.items():
        path = getattr(params.data, key)
        on = f'data.{key}'
        if not os.path.exists(path):
            faults.append(Fault(on, 0, f'data.{key} names {path}, which is not there.'))
            continue
        try:
            rows[key] = sibling_rows(path, sheet)
        except KeyError:
            faults.append(Fault(on, 0, f"data.{key}: {os.path.basename(path)} has no sheet '{sheet}'."))
    if 'vehicle_pcb_composition' in rows:
        held = {}
        for r in rows['vehicle_pcb_composition']:
            held.setdefault(text(r.get('PCBCategory')), set()).add(text(r.get('Element')))
        for b in apart.boards:
            if b.category not in held:
                pcb = os.path.basename(params.data.vehicle_pcb_composition)
                faults.append(Fault('Boards', b.row, f"{b.robot}, {b.name}: the car board category '{b.category}' is "
                                                     f'not in {pcb}.'))
            elif set(BOARD_METALS) - held[b.category]:
                lacking = ', '.join(sorted(set(BOARD_METALS) - held[b.category]))
                faults.append(Fault('Boards', b.row, f"{b.robot}, {b.name}: the car board category '{b.category}' "
                                                     f'has no {lacking}.'))
    if 'vehicle_sensor_composition' in rows:
        types = {text(r.get('SensorType')) for r in rows['vehicle_sensor_composition']}
        for row, sensor, car_type, _ in apart.elements:
            if car_type not in types:
                where = os.path.basename(params.data.vehicle_sensor_composition)
                faults.append(Fault('SensorElements', row, f"{sensor}: the car sensor type '{car_type}' is not in "
                                                           f'{where}.'))
    if 'data_center_element_composition' in rows:
        tantalum = [r for r in rows['data_center_element_composition'] if text(r.get('Element')) == 'Ta']
        values = tuple(number(tantalum[0].get(k)) for k in ('Min', 'Mode', 'Max')) if tantalum else None
        if values is None or None in values or not 0 <= values[0] <= values[1] <= values[2]:
            faults.append(Fault('data.data_center_element_composition', 0, 'no Ta row with min, mode and max in order '
                                                                            'in its sheet BoardsAndComponents.'))
    if 'traction_motor_magnets' in rows:
        # One fault per grade class a heat group can draw that is missing, naming the groups (a class is shared).
        classes = {text(r.get('TempClass')) for r in rows['traction_motor_magnets']}
        missing: dict = {}
        for g in apart.grades:
            if g.klass not in classes and (g.probability or 0) > 0:
                missing.setdefault(g.klass, []).append(g)
        where = os.path.basename(params.data.traction_motor_magnets)
        for klass, grades in missing.items():
            used_by = ', '.join(g.group for g in grades)
            faults.append(Fault('MagnetGrades', grades[0].row, f"the magnet grade class '{klass}' is not in {where}; "
                                                               f'drawn by {used_by}.'))
    return faults


# ------------------------------------------------------------------------------------------------------
# The register of every known humanoid robot (data/researched/humanoid_register.xlsx)
# ------------------------------------------------------------------------------------------------------
# Built by tools/make_humanoid_register.py from the humanoid.guide catalogue and Matthias's decisions of 2026-10-28
# (documentation/claude/EVIDENCE.md E4 to E4.11): every robot once, with at most two robot types.

REGISTER_SHEET = 'Robots'
REGISTER_HEADINGS = ['Number', 'Robot', 'Maker', 'Country', 'Status', 'Height (cm)', 'Mass (kg), stated',
                     'Mass min (kg)', 'Mass mode (kg)', 'Mass max (kg)', 'Mass basis', 'Types', 'Form', 'Entry',
                     'Taken apart as', 'Decided in', 'Source']
# How a robot moves, as read (EVIDENCE.md E4.1 to E4.10); the last six are the forms of robots not assigned, or one
# moving by its arms (HELIOS) or a ball (Mirokaï).
REGISTER_FORMS = ('legs', 'wheels', 'legs or wheels', 'no wheels named', 'not stated', 'an upper body', 'two arms',
                  'two arms and a torso', 'an arm', 'four arms, no legs', 'a ball')
# The entry of a robot without types says why: left out ("not assigned: an upper body only"), or a second entry of
# one robot ("the same robot as 3", counted once as entry 3: "No double counting use just 1").
NOT_ASSIGNED = 'not assigned: '
SAME_ROBOT = 'the same robot as '
MOST_TYPES = 2   # "Double assignment means 1 robot can be two types" (Matthias, 2026-10-28)


@dataclass
class RegisterRobot:
    """One robot of the register."""

    row: int                 # its row in the sheet Robots
    number: int              # its number: the catalogue's order of reading, 350 on for the robots added
    name: str
    maker: str
    mass: tuple              # (min, mode, max) kg, or (None, None, None) where no mass is stated
    types: tuple             # its robot types, the leading one first; () where the entry says why there are none
    types_text: str          # the cell as written, for the faults
    form: str
    entry: str
    taken_apart: str         # its name in parts_taken_apart.xlsx, for the three robots of type 1 taken apart


def read_register(path: str) -> list[RegisterRobot]:
    """Read the register; never writes to it. A missing file, sheet or heading stops the reading (WorkbookError), as
    with the other files 01 reads."""
    if not os.path.exists(path):
        raise WorkbookError(f'{path}: the register is not there.')
    book = load_workbook(path, data_only=True)
    if REGISTER_SHEET not in book.sheetnames:
        raise WorkbookError(f"{path}: no sheet '{REGISTER_SHEET}'. Its sheets are: {', '.join(book.sheetnames)}.")
    sheet = book[REGISTER_SHEET]
    found = [text(cell.value) for cell in sheet[1]][:len(REGISTER_HEADINGS)]
    if found != REGISTER_HEADINGS:
        raise WorkbookError(f"{path}, sheet '{REGISTER_SHEET}': the first row must be {REGISTER_HEADINGS}, not "
                            f'{found}.')
    at = {name: k for k, name in enumerate(REGISTER_HEADINGS)}
    robots = []
    for cells in sheet.iter_rows(min_row=2):
        v = [cell.value for cell in cells] + [None] * len(REGISTER_HEADINGS)
        if all(x is None for x in v[:len(REGISTER_HEADINGS)]):
            continue
        written = text(v[at['Types']])
        types = tuple(int(t) if t.isdigit() else t for t in (piece.strip() for piece in written.split(',')) if t)
        mass = tuple(number(v[at[h]]) for h in ('Mass min (kg)', 'Mass mode (kg)', 'Mass max (kg)'))
        robots.append(RegisterRobot(row=cells[0].row, number=int(number(v[at['Number']]) or 0),
                                    name=text(v[at['Robot']]), maker=text(v[at['Maker']]), mass=mass, types=types,
                                    types_text=written, form=text(v[at['Form']]), entry=text(v[at['Entry']]),
                                    taken_apart=text(v[at['Taken apart as']])))
    return robots


def check_register(register: list, params: Params, taken_apart: list) -> list[Fault]:
    """Whether the register holds together (EVIDENCE.md E4 to E4.11): every number once; a robot with types has one or
    two different robot types of the six and no entry, a robot without has an entry saying why (not assigned, or the
    same robot as an entry with types); every form known; every mass all three or none, in order from 0; no robot of
    type 1 below its lowest mass; every robot taken apart in the parts file (`taken_apart`, its robot names) and of
    type 1."""
    where = os.path.basename(params.data.register) + ': ' + REGISTER_SHEET
    lowest = params.composition.type_one_lowest_kg
    faults = []
    numbers = [r.number for r in register]
    by_number = {r.number: r for r in register}
    for r in register:
        what = f'{r.number} {r.name}'
        if numbers.count(r.number) > 1:
            faults.append(Fault(where, r.row, f'{what}: the number {r.number} is given to more than one robot.'))
        unknown = [t for t in r.types if not isinstance(t, int) or not 1 <= t <= 6]
        for t in unknown:
            faults.append(Fault(where, r.row, f"{what}: the robot type '{t}' is not one of the six."))
        if len(r.types) > MOST_TYPES:
            faults.append(Fault(where, r.row, f"{what}: at most two robot types, not '{r.types_text}'."))
        if len(set(r.types)) < len(r.types):
            faults.append(Fault(where, r.row, f"{what}: a robot type is given twice ('{r.types_text}')."))
        if r.entry == '' and not r.types:
            faults.append(Fault(where, r.row, f'{what}: no type, and no entry saying why.'))
        elif r.entry.startswith(NOT_ASSIGNED):
            if r.types:
                faults.append(Fault(where, r.row, f'{what}: a robot not assigned has no types.'))
        elif r.entry.startswith(SAME_ROBOT):
            if r.types:
                faults.append(Fault(where, r.row, f'{what}: a second entry of a robot has no types.'))
            other = r.entry[len(SAME_ROBOT):].strip()
            target = by_number.get(int(other)) if other.isdigit() else None
            if target is None:
                faults.append(Fault(where, r.row, f"{what}: '{r.entry}': there is no robot {other}."))
            elif target.entry:
                faults.append(Fault(where, r.row, f"{what}: '{r.entry}': robot {other} is itself a second entry or "
                                                  'not assigned; name the entry with the types.'))
        elif r.entry:
            faults.append(Fault(where, r.row, f"{what}: the entry '{r.entry}' is not known; it is empty, starts with "
                                              f"'{NOT_ASSIGNED}' or '{SAME_ROBOT}'."))
        if r.form not in REGISTER_FORMS:
            faults.append(Fault(where, r.row, f"{what}: the form '{r.form}' is not one of "
                                              f"{', '.join(REGISTER_FORMS)}."))
        if any(m is not None for m in r.mass):
            if None in r.mass:
                faults.append(Fault(where, r.row, f'{what}: give its mass as min, mode and max, or none.'))
            elif not 0 <= r.mass[0] <= r.mass[1] <= r.mass[2]:
                faults.append(Fault(where, r.row, f'{what}: its mass min, mode and max must be in order from 0 up: '
                                                  f'{r.mass}.'))
            elif 1 in r.types and r.mass[1] < lowest:
                faults.append(Fault(where, r.row, f'{what}: {r.mass[1]:g} kg is below robot type 1\'s lowest mass, '
                                                  f'{lowest:g} kg ("Below 15 kg not part of the type 1").'))
        if r.taken_apart:
            if r.taken_apart not in taken_apart:
                faults.append(Fault(where, r.row, f"{what}: '{r.taken_apart}' is not a robot of "
                                                  f'{os.path.basename(params.data.parts_taken_apart)}.'))
            if 1 not in r.types:
                faults.append(Fault(where, r.row, f'{what}: a robot taken apart is a robot of type 1.'))
    return faults


def battery_pieces(materials: MaterialsList, battery: Material, lists: SharedLists, recipes: ElementRecipes) -> list:
    """The battery row of one robot type as cells only: its cells, and the rest of the row (the row minus the cells)
    split by the shares of the sheet Battery cells, the remainder 1 minus the others. Each piece is (shared material,
    (minimum, mode, maximum) kg, estimated, workbook name); a piece to Not allocated carries only its mode, which the
    pages add to the kilograms not allocated."""
    cells = battery_cells(materials, lists, recipes)
    rest_kg = tuple(None if k is None else k - c for k, c in zip(battery.kg, (cells[2], cells[1], cells[0])))
    rows = [b for b in lists.battery if b.robot == materials.number and b.kind == REST]
    others = [b for b in rows if not b.remainder and None not in b.share]
    pieces = [(BATTERY, cells, True, battery.family)]
    for b in rows:
        if b.remainder:
            share = tuple(1 - sum(o.share[i] for o in others) for i in (2, 1, 0))
        elif None in b.share:
            continue
        else:
            share = b.share
        kg_ = tuple(None if k is None else k * s for k, s in zip(rest_kg, share))
        pieces.append((b.name, (None, kg_[1], None) if b.name == NOT_ALLOCATED else kg_, True, battery.family))
    return pieces


def material_pieces(materials: MaterialsList, lists: SharedLists, recipes: ElementRecipes | None = None) -> list:
    """Every material of one robot as (shared material, (minimum, mode, maximum) kg, estimated, workbook name). A
    name split by the sheet Splits gives one piece per shared material, each its share of the name's kilograms:
    the minimum at the smallest share, the maximum at the largest, and the remainder 1 minus the others, so that the
    pieces add up to the name's kilograms at the mode. With the element recipes, the battery row is cells only
    (battery_pieces). Estimated pieces are marked."""
    pieces = []
    built = recipes is not None and lists.battery is not None and battery_cells(materials, lists, recipes) is not None
    for m in materials.materials:
        shared = lists.materials.get(m.family, ('',))[0]
        if built and shared == BATTERY:
            pieces += battery_pieces(materials, m, lists, recipes)
        elif shared == SPLIT and m.family in lists.splits:
            split = lists.splits[m.family]
            others = [p for p in split if not p.remainder and None not in p.share]
            for p in split:
                if p.remainder:
                    share = tuple(1 - sum(o.share[i] for o in others) for i in (2, 1, 0))
                elif None in p.share:
                    continue
                else:
                    share = p.share
                kg_ = tuple(None if k is None else k * s for k, s in zip(m.kg, share))
                pieces.append((p.shared, kg_, True, m.family))
        elif shared and shared != SPLIT:
            pieces.append((shared, m.kg, False, m.family))
    return pieces


def by_view(parts_list: PartsList, lists: SharedLists, view: str) -> dict:
    """The kg at the mode of one robot by part group (view 'group') or body region (view 'region'). A part split by
    units counts the mass of one unit for each unit in a region."""
    totals: dict = {}
    for part in parts_list.parts:
        place = lists.parts.get(part.row)
        if place is None or part.total_kg[1] is None:
            continue
        if view == 'group':
            totals[place.group] = totals.get(place.group, 0) + part.total_kg[1]
        elif place.split:
            for region, units in place.split.items():
                totals[region] = totals.get(region, 0) + units * (part.unit_kg[1] or 0)
        else:
            totals[place.region] = totals.get(place.region, 0) + part.total_kg[1]
    return totals


def by_material(materials: MaterialsList, lists: SharedLists, recipes: ElementRecipes | None = None) -> dict:
    """The kg at the mode of one robot by shared material, with the kilograms its materials leave out of its
    parts list as 'Not allocated'. With the element recipes, the battery is cells only, and the rest of its row that
    goes to Not allocated is added there (below zero where the cells weigh more than the row)."""
    totals: dict = {}
    for shared, kg_, _, _ in material_pieces(materials, lists, recipes):
        if kg_[1] is not None:
            totals[shared] = totals.get(shared, 0) + kg_[1]
    unallocated = totals.pop(NOT_ALLOCATED, 0) + (materials.unallocated_parts_kg or 0)
    if unallocated:
        totals[NOT_ALLOCATED] = unallocated
    return totals


def motors_of(parts_list: PartsList, lists: SharedLists) -> float:
    """How many electric motors the shared lists count in one robot (outside the hands)."""
    return sum(lists.parts[p.row].motors or 0 for p in parts_list.parts if p.row in lists.parts)


def category_report(number_: int, sources_dir: str) -> str | None:
    """The file name of the category's own report in the sources (e.g. '01_category_....md'), or None."""
    if not os.path.isdir(sources_dir):
        return None
    reports = sorted(name for name in os.listdir(sources_dir)
                     if name.startswith(f'{number_:02d}_category_') and name.endswith('.md'))
    return reports[0] if reports else None


def is_notional(anchor: str) -> bool:
    """Whether the workbook calls the anchor robot notional: a configuration, not a robot that exists."""
    return 'notional' in anchor.lower()


# ------------------------------------------------------------------------------------------------------
# Drawing
# ------------------------------------------------------------------------------------------------------
# Every page is laid out in inches, from the top left: an axes covers the whole figure with x from 0 to the
# width and y from 0 (top) down to the height, so a position on the page is a position in inches.

LINE = 0.19            # height of one line of 9-point text, inches
SMALL = 9              # the size of the text of tables and boxes, points
RED = '#C00000'        # faults
SUBSYSTEM = '#DCE3EE'  # the band that opens each group of parts
EDGE = '#8A8A8A'       # the edges of boxes and rows


def wrap(value: str, width: int) -> list[str]:
    """Text broken into lines of at most `width` characters; the workbook's own line breaks are kept."""
    lines = []
    for paragraph in str(value or '').split('\n'):
        lines += textwrap.wrap(paragraph.strip(), width) or ['']
    while len(lines) > 1 and not lines[-1]:
        lines.pop()
    return lines


def wrap_name(label: str, name: str, width: int) -> list[str]:
    """A label and a long file name, broken after underscores so that no line is longer than `width`
    characters and no word is cut in two ('01_category_compact_' / 'research_developer_...')."""
    lines, line = [], label
    for piece in re.findall(r'[^_]+_?', name):
        if line.strip() and len(line) + len(piece) > width:
            lines.append(line.rstrip())
            line = ''
        line += piece
    return lines + [line]


def triple(values: tuple) -> str:
    """Minimum, mode and maximum as '1.15 / 1.25 / 1.35'."""
    return ' / '.join(kg(v) for v in values)


def signed(value: float, unit: str) -> str:
    """A difference with its sign: '+2.4 kg', '-1 kg'; a share in % with one decimal, as the workbook
    writes it: '+14.9 %'."""
    shown = f'{abs(value):.1f}' if unit == '%' else kg(abs(value))
    return f"{'+' if value >= 0 else '-'}{shown} {unit}"


def by_subsystem(parts: list[Part]) -> list[tuple[str, list[Part]]]:
    """The parts grouped by subsystem, the groups in the order in which each first appears. The workbook
    does not always keep a subsystem's rows together (category 5 has 'Structure & Protection' in rows 71
    and 75 to 76); a page shows each subsystem once, with all its parts in their order in the sheet."""
    groups: dict[str, list[Part]] = {}
    for part in parts:
        groups.setdefault(part.subsystem, []).append(part)
    return list(groups.items())


def new_page(width: float, height: float):
    """A figure of the given size in inches, with one axes in which positions are inches from the top
    left."""
    figure = plt.figure(figsize=(width, height))
    axes = figure.add_axes([0, 0, 1, 1])
    axes.set_xlim(0, width)
    axes.set_ylim(height, 0)
    axes.axis('off')
    return figure, axes


def box(axes, x, y, width, height, colour='white', edge=EDGE):
    """A rectangle with its top left corner at (x, y), in inches."""
    axes.add_patch(Rectangle((x, y), width, height, facecolor=colour, edgecolor=edge, linewidth=0.8))


def write(axes, x, y, lines, size=SMALL, colour='black', weight='normal', align='left'):
    """Lines of text from (x, y) downwards; returns the y below the last line."""
    step = LINE * size / SMALL
    for line in lines:
        axes.text(x, y, line, fontsize=size, color=colour, fontweight=weight, ha=align, va='top')
        y += step
    return y


def save(figure, path: str, dpi: int) -> None:
    """Write the page and close it."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    figure.savefig(path, dpi=dpi, facecolor='white')
    plt.close(figure)


def evidence_key(axes, x, y) -> float:
    """The colour key of the evidence, as in the workbook; returns the y below it."""
    write(axes, x, y, ['Evidence, coloured as in the workbook:'], weight='bold')
    y += LINE * 1.2
    for evidence, colour in EVIDENCE_COLOUR.items():
        box(axes, x, y, 0.3, LINE * 0.8, colour)
        write(axes, x + 0.4, y, [f'{evidence}: {EVIDENCE_MEANING[evidence]}'])
        y += LINE * 1.15
    return y


# The columns of a parts list on a category page: (heading, x of the column in inches, characters per line
# before the text wraps, alignment). 'Number' is right-aligned at its x.
PART_TABLE = [
    (['Part'], 0.3, 46, 'left'),
    (['Where in the robot'], 3.7, 42, 'left'),
    (['Number'], 7.25, 0, 'right'),
    (['Mass of one, kg', 'min / mode / max'], 7.5, 0, 'left'),
    (['Mass of all, kg', 'min / mode / max'], 9.1, 0, 'left'),
    (['Main material'], 10.8, 58, 'left'),
    (['Evidence'], 15.0, 0, 'left'),
    (['Sources in the workbook'], 16.0, 30, 'left'),
]
PAGE_WIDTH = 19.0


def part_cells(part: Part) -> list[list[str]]:
    """The text of one part in the columns of PART_TABLE, already wrapped."""
    return [wrap(part.component, 46), wrap(part.location, 42), [kg(part.quantity)],
            [triple(part.unit_kg)], [triple(part.total_kg)], wrap(part.material, 58), [part.evidence],
            wrap(part.sources, 30)]


def draw_category(category: Category, parts_list: PartsList | None, report: str | None,
                  faults: list[Fault], path: str, params: Params) -> None:
    """One page per category: its definition and anchor robot, then its parts list by subsystem."""
    faulty_rows = {f.row for f in faults if f.sheet == params.data.components_sheet}
    parts = parts_list.parts if parts_list else []

    # The four boxes under the title: what the workbook writes, as it writes it.
    if parts_list and parts_list.stated_mass_kg is not None and parts_list.sum_kg[1] is not None:
        difference = parts_list.sum_kg[1] - parts_list.stated_mass_kg
        share = difference / parts_list.stated_mass_kg * 100
        mass_lines = [f'Sum of the parts: {triple(parts_list.sum_kg)} kg (min / mode / max)',
                      f'Stated mass of the anchor robot: {kg(parts_list.stated_mass_kg)} kg '
                      f'({parts_list.stated_evidence})',
                      f'Mode of the sum minus the stated mass: {signed(difference, "kg")} '
                      f'({signed(share, "%")})']
    else:
        mass_lines = ['The workbook has no sum or no stated mass for this category.']
    mass_lines += [''] + (wrap_name('Report of its own: ', report, 56) if report
                          else ['No report of its own in documentation/sources/.'])
    anchor_lines = wrap(category.anchor, 56)
    if is_notional(category.anchor):
        anchor_lines += [''] + wrap('The anchor robot is notional: a configuration the research assumes, '
                                    'not a robot that exists.', 56)
    boxes = [('Anchor robot', anchor_lines), ('Height and mass', wrap(category.height_and_mass, 56)),
             ('Joints and payload', wrap(category.joints_and_payload, 56)),
             ('Mass of the anchor robot', mass_lines)]

    # The height of the page: title, definition, boxes, the table rows, the key at the foot.
    definition = wrap(category.definition, 175)
    box_lines = max(len(lines) for _, lines in boxes) + 1
    rows = []
    for subsystem, members in by_subsystem(parts):
        rows.append(('subsystem', subsystem, 1))
        rows += [('part', part, max(len(c) for c in part_cells(part))) for part in members]
    table_height = sum(LINE * lines + 0.12 for _, _, lines in rows)
    height = 0.55 + len(definition) * LINE * 1.2 + 0.3 + box_lines * LINE + 0.5 + 2 * LINE + 0.25 \
        + table_height + 1.9
    figure, axes = new_page(PAGE_WIDTH, height)

    axes.text(0.3, 0.3, f'Category {category.number}: {category.name}', fontsize=16, fontweight='bold',
              va='top')
    y = write(axes, 0.3, 0.75, definition, size=11)

    # The four boxes.
    y += 0.25
    box_width = (PAGE_WIDTH - 0.6 - 3 * 0.2) / 4
    box_height = box_lines * LINE + 0.2
    for i, (title, lines) in enumerate(boxes):
        x = 0.3 + i * (box_width + 0.2)
        box(axes, x, y, box_width, box_height)
        write(axes, x + 0.12, y + 0.1, [title], weight='bold')
        write(axes, x + 0.12, y + 0.1 + LINE * 1.2, lines)
    y += box_height + 0.35

    # The parts list: a heading row, then a band per subsystem and a row per part, coloured by evidence.
    headings = max(len(h) for h, _, _, _ in PART_TABLE)
    box(axes, 0.2, y, PAGE_WIDTH - 0.4, headings * LINE + 0.12, '#EEEEEE')
    for heading, x, _, align in PART_TABLE:
        write(axes, x, y + 0.06, heading, weight='bold', align=align)
    y += headings * LINE + 0.12
    for kind, item, lines in rows:
        row_height = LINE * lines + 0.12
        if kind == 'subsystem':
            box(axes, 0.2, y, PAGE_WIDTH - 0.4, row_height, SUBSYSTEM)
            write(axes, 0.3, y + 0.06, [item], weight='bold')
        else:
            box(axes, 0.2, y, PAGE_WIDTH - 0.4, row_height, EVIDENCE_COLOUR.get(item.evidence, '#DDDDDD'))
            colour = RED if item.row in faulty_rows else 'black'
            for (_, x, _, align), cell in zip(PART_TABLE, part_cells(item)):
                write(axes, x, y + 0.06, cell, colour=colour, align=align)
        y += row_height

    # The foot of the page.
    y += 0.25
    own = [f for f in faults if f.sheet == params.data.components_sheet and f.row and parts_list
           and parts_list.first_row <= f.row
           <= max([parts_list.difference_row, parts_list.stated_row, parts_list.sum_row]
                  + [p.row for p in parts])]
    if own:
        y = write(axes, 0.3, y, [f'{len(own)} fault(s) in the rows of this category, drawn in red: see '
                                 'faults.png.'], colour=RED, weight='bold')
    else:
        y = write(axes, 0.3, y, ['No fault found in the rows of this category.'])
    y = evidence_key(axes, 0.3, y + 0.1)
    first = parts_list.first_row if parts_list else 0
    last = parts_list.difference_row if parts_list else 0
    write(axes, 0.3, y + 0.1, [f'Masses rounded to three decimals. Source: {params.data.workbook}, sheet '
                               f"'{params.data.taxonomy_sheet}' row {category.row} and sheet "
                               f"'{params.data.components_sheet}' rows {first} to {last}."])
    save(figure, path, params.output.dpi)


# The two tables of a shared-lists page: (heading, x of the column in inches, characters per line before the text
# wraps, alignment). The tables end at TABLE_RIGHT; the bars sit to the right of them, their names to the left of
# CHART_X.
SHARED_PART_TABLE = [
    (['Part'], 0.3, 44, 'left'),
    (['Where in the robot (workbook)'], 3.55, 38, 'left'),
    (['Units'], 6.75, 0, 'right'),
    (['kg, min / mode / max'], 6.95, 0, 'left'),
    (['Part group'], 8.55, 20, 'left'),
    (['Body region'], 10.15, 22, 'left'),
    (['Motors'], 12.6, 0, 'right'),
]
SHARED_MATERIAL_TABLE = [
    (['Material in the workbook'], 0.3, 34, 'left'),
    (['Grade'], 2.95, 38, 'left'),
    (['kg, min / mode / max'], 5.75, 0, 'left'),
    (['Evidence'], 7.5, 0, 'left'),
    (['Shared material'], 8.35, 20, 'left'),
    (['Why'], 9.85, 40, 'left'),
]
TABLE_RIGHT = 12.75
CHART_X, CHART_WIDTH = 14.75, 3.6
BAR_STEP = 0.24        # the height of one bar's row, inches
BAR = '#5B7DB1'        # the bars
GREY = '#A6A6A6'       # 'Mixed' and 'Not allocated', which are not one part group or material
PLAIN_WHY = 'The name says the material.'   # the reason of an obvious placement, not repeated on the page


def bars(figure, page, page_height: float, x: float, y: float, title: str, names: list, values: dict) -> float:
    """Horizontal bars of kg at the mode, one per name of the shared list, with the value at the end of each bar;
    a name the robot has none of shows '–'. Returns the y below the chart."""
    write(page, x - 1.6, y, [title], weight='bold')
    height = BAR_STEP * len(names)
    axes = figure.add_axes([x / PAGE_WIDTH, 1 - (y + 0.3 + height) / page_height, CHART_WIDTH / PAGE_WIDTH,
                            height / page_height])
    shown = [values.get(name, 0) for name in names]
    top = max(shown + [1])
    axes.barh(range(len(names)), shown, height=0.65,
              color=[GREY if name in ('Mixed', NOT_ALLOCATED) else BAR for name in names])
    axes.set_ylim(len(names) - 0.5, -0.5)
    axes.set_yticks(range(len(names)), names, fontsize=8.5)
    axes.set_xlim(0, top * 1.3)
    axes.set_xticks([])
    for side in ('top', 'right', 'bottom'):
        axes.spines[side].set_visible(False)
    for i, value in enumerate(shown):
        axes.text(value + top * 0.02, i, kg(value) if value else '–', va='center', fontsize=8.5)
    return y + 0.3 + height


def shared_part_cells(part: Part, place: Placement | None) -> list[list[str]]:
    """The text of one part in the columns of SHARED_PART_TABLE, already wrapped."""
    if place is None:
        group, region, motors = ['not placed'], ['not placed'], ['—']
    else:
        group = wrap(place.group, 20)
        region = wrap(', '.join(f'{r} {kg(u)}' for r, u in place.split.items()) if place.split else place.region, 22)
        motors = [kg(place.motors)]
    return [wrap(part.component, 44), wrap(part.location, 38), [kg(part.quantity)], [triple(part.total_kg)],
            group, region, motors]


def shared_material_cells(material: Material, lists: SharedLists) -> list[list[str]]:
    """The text of one material in the columns of SHARED_MATERIAL_TABLE, already wrapped."""
    shared, why, _ = lists.materials.get(material.family, ('not placed', '', 0))
    return [wrap(material.family, 34), wrap(material.grade, 38), [triple(material.kg)], [material.evidence],
            wrap(shared, 20), wrap('' if why == PLAIN_WHY else why, 40)]


def table(page, y: float, columns: list, rows: list, colours: list) -> float:
    """A table with a grey heading row and one row per entry of `rows` (its cells, already wrapped), each drawn in
    its colour of `colours`. Returns the y below it."""
    headings = max(len(h) for h, _, _, _ in columns)
    box(page, 0.2, y, TABLE_RIGHT - 0.2, headings * LINE + 0.12, '#EEEEEE')
    for heading, x, _, align in columns:
        write(page, x, y + 0.06, heading, weight='bold', align=align)
    y += headings * LINE + 0.12
    for cells, colour in zip(rows, colours):
        height = max(len(c) for c in cells) * LINE + 0.12
        box(page, 0.2, y, TABLE_RIGHT - 0.2, height)
        for (_, x, _, align), cell in zip(columns, cells):
            write(page, x, y + 0.06, cell, colour=colour, align=align)
        y += height
    return y


def draw_shared_lists(category: Category, parts_list: PartsList, materials: MaterialsList | None,
                      lists: SharedLists, faults: list[Fault], path: str, params: Params) -> None:
    """One page per robot type in the shared lists, for Matthias to verify every placement: the parts with their
    part group and body region, the materials with their shared material, and the kg at the mode by part group,
    body region and material, with the number of motors."""
    parts = parts_list.parts
    material_rows = materials.materials if materials else []
    part_rows = {p.row for p in parts}
    first = materials.first_row if materials else 0
    last = max([m.row for m in material_rows] + [materials.unallocated_row if materials else 0, first])
    own = [f for f in faults if f.part_row in part_rows
           or (f.sheet == params.data.materials_sheet and first <= f.row <= last)
           or (f.sheet.endswith(MATERIALS_SHEET) and any(f"'{m.family}'" in f.text or f.text.startswith(m.family)
                                                         for m in material_rows))]
    red_parts = {f.part_row for f in own if f.part_row}
    red_materials = {f.row for f in own if f.sheet == params.data.materials_sheet}

    part_cells = [shared_part_cells(p, lists.parts.get(p.row)) for p in parts]
    # Each material, and below a split one its pieces, each an estimate (E) with its share and its basis.
    pieces = [piece for piece in (material_pieces(materials, lists) if materials else []) if piece[2]]
    material_cells, material_colours = [], []
    for m in material_rows:
        material_cells.append(shared_material_cells(m, lists))
        material_colours.append(RED if m.row in red_materials else 'black')
        for shared, kg_, _, family in pieces:
            if family != m.family:
                continue
            piece = next(p for p in lists.splits[family] if p.shared == shared)
            share = ('the remainder: 1 minus the shares above' if piece.remainder else
                     f'{piece.share[0]:.1%} to {piece.share[2]:.1%} of it, most likely {piece.share[1]:.1%}')
            material_cells.append([[f'   → {shared}'], wrap(share, 38), [triple(kg_)], ['E'], wrap(shared, 20),
                                   wrap(piece.basis, 40)])
            material_colours.append('black')
    unallocated = materials.unallocated_parts_kg if materials else None
    if unallocated:
        material_cells.append([[NOT_ALLOCATED], wrap("The workbook's materials leave this out of the parts list",
                                                     38),
                               [f'— / {kg(unallocated)} / —'], ['Derived'], [NOT_ALLOCATED],
                               wrap('Point 10: shown as its own bar; nothing is rescaled.', 40)])

    # The notes at the foot: hands, the placements a point decided, faults.
    groups = by_view(parts_list, lists, 'group')
    notes = []
    if not groups.get('Hands'):
        notes.append('No hands of their own in the parts list: this robot type is not comparable for hands '
                     '(point 2 of SHARED_LISTS.md).')
    for p in parts:
        place = lists.parts.get(p.row)
        if place and place.why.startswith('Point'):
            notes.append(f'{p.component}: {place.why}')
    note_lines = [line for note in notes for line in wrap('• ' + note, 170)]

    rows_height = lambda cells: sum(max(len(c) for c in row) * LINE + 0.12 for row in cells)  # noqa: E731
    charts_top = BAR_STEP * (len(lists.names[PART_GROUP]) + len(lists.names[BODY_REGION])) + 0.3 * 2 + 0.35
    parts_height = max(2 * LINE + 0.12 + rows_height(part_cells), charts_top)
    materials_height = max(2 * LINE + 0.12 + rows_height(material_cells), BAR_STEP * len(lists.names[MATERIAL]) + 0.3)
    height = 1.45 + 0.35 + parts_height + 0.5 + 0.35 + materials_height + 0.5 + (len(note_lines) + 6) * LINE + 0.5
    figure, page = new_page(PAGE_WIDTH, height)

    page.text(0.3, 0.3, f'Robot type {category.number} in the shared lists: {category.name}', fontsize=16,
              fontweight='bold', va='top')
    anchor = category.anchor.splitlines()[0] if category.anchor else '—'
    y = write(page, 0.3, 0.75, [f'Anchor robot: {anchor}. Electric motors outside the hands: '
                                f'{kg(motors_of(parts_list, lists))}.',
                                'The bars are kg at the mode: the sum of the workbook\'s modes. Ranges come with the '
                                'Monte Carlo of this robot type\'s stage.'], size=11)

    # The parts, with the bars by part group and by body region beside them.
    y += 0.3
    write(page, 0.3, y, ['Parts'], size=11, weight='bold')
    y += 0.35
    bottom = table(page, y, SHARED_PART_TABLE, part_cells, [RED if p.row in red_parts else 'black' for p in parts])
    below = bars(figure, page, height, CHART_X, y, 'By part group', lists.names[PART_GROUP], groups)
    below = bars(figure, page, height, CHART_X, below + 0.3, 'By body region', lists.names[BODY_REGION],
                 by_view(parts_list, lists, 'region'))
    y = max(bottom, below) + 0.5

    # The materials, with the bars by material beside them.
    write(page, 0.3, y, ['Materials'], size=11, weight='bold')
    y += 0.35
    colours = material_colours + ['black'] * bool(unallocated)
    bottom = below = table(page, y, SHARED_MATERIAL_TABLE, material_cells, colours)
    if materials:
        below = bars(figure, page, height, CHART_X, y, 'By material', lists.names[MATERIAL],
                     by_material(materials, lists))
    y = max(bottom, below) + 0.5

    # The foot of the page.
    if own:
        y = write(page, 0.3, y, [f'{len(own)} fault(s) in the rows or placements of this robot type, drawn in red: '
                                 'see faults.png.'], colour=RED, weight='bold')
    else:
        y = write(page, 0.3, y, ['No fault found in the rows or placements of this robot type.'])
    if note_lines:
        y = write(page, 0.3, y + 0.1, ['Notes'], weight='bold')
        y = write(page, 0.3, y, note_lines)
    write(page, 0.3, y + 0.15, wrap(f'Source: {params.data.workbook}, sheets \'{params.data.components_sheet}\' rows '
                                    f'{parts_list.first_row} to {parts_list.difference_row} and '
                                    f"'{params.data.materials_sheet}' rows {first} to {last}; the placements: "
                                    f'{params.data.shared_lists}. Masses rounded to three decimals.', 190))
    save(figure, path, params.output.dpi)


# ------------------------------------------------------------------------------------------------------
# The one-view schema of a robot type
# ------------------------------------------------------------------------------------------------------
# Matthias, 2026-10-26: "I want theat one can understand the robot and its compostion and parts in one vew", "No I
# want to see it as a robot. Be more inovbative and visual", and on seeing it: "It looks better as robot, but the
# material compsotion as bar plat". On the left the robot, drawn to the anchor robot's height at the same scale on
# every page, with its parts where they sit; on the right its materials as bars, on the same kg scale on every page.

ROBOT_SCALE = 4.2      # inches of page per metre of robot height, the same on all six pages (1.85 m = 7.8 inches)
TALLEST = 1.85         # metres: the tallest robot of the research (categories 2, 5 and 6), which sets the page
PARTS_X = 6.5                      # the middle of the parts robot, inches
CHART_LEFT, CHART_RIGHT = 12.9, 17.6   # the bars of the materials, inches; their names sit to the left

# The body of the schema, in units of the robot's height: across (u, 0 in the middle, negative to the robot's
# right, which is the left of the page) and up (v, 0 at the soles, 1 at the top of the head). A schema, not the
# robot's real shape. Every shape is drawn for the left side and mirrored.
HEAD = ((0.0, 0.925), 0.065)
BLOCKS = {'neck': (-0.025, 0.025, 0.835, 0.87), 'torso': (-0.13, 0.13, 0.55, 0.84),
          'pelvis': (-0.105, 0.105, 0.465, 0.56), 'foot': (-0.115, -0.025, 0.0, 0.045)}
LIMBS = {'upper arm': ((-0.16, 0.82), (-0.175, 0.64), 0.055), 'forearm': ((-0.175, 0.64), (-0.185, 0.475), 0.048),
         'thigh': ((-0.06, 0.48), (-0.065, 0.27), 0.075), 'shin': ((-0.065, 0.27), (-0.065, 0.045), 0.062)}
HAND, HAND_RADIUS = (-0.188, 0.44), 0.032
JOINTS = {'Head': [(0.0, 0.852)], 'Torso': [(0.0, 0.56)],
          'Arms': [(-0.16, 0.81), (-0.175, 0.64), (-0.185, 0.475)],
          'Legs': [(-0.06, 0.475), (-0.065, 0.27), (-0.065, 0.05)]}
MIRRORED = {'Arms', 'Legs'}

# Where each part group is drawn inside the body, and where its label points.
PART_SPOTS = {'Joint drives': (-0.065, 0.27), 'Hands': HAND, 'Battery': (-0.08, 0.615), 'Computer': (-0.055, 0.75),
              'Sensors': (-0.04, 0.955), 'Frame': (-0.0625, 0.38), 'Shell and armour': (-0.19, 0.73),
              'Cables': (-0.105, 0.60), 'Cooling': (-0.1, 0.79), 'Screws and bearings': (-0.06, 0.475),
              'Mixed': (0.02, 0.69)}
# Where the label of each body region points: on the robot's left side, which faces the middle of the page.
REGION_SPOTS = {'Head': (0.065, 0.925), 'Arms': (0.18, 0.70), 'Hands': (0.22, 0.44), 'Torso': (0.13, 0.62),
                'Legs': (0.095, 0.20)}

# The colours of the parts robot.
SHELL, SKELETON, MOTOR = '#E9ECEF', '#495057', '#3B5BA5'
PART_COLOUR = {'Battery': '#E8B84A', 'Computer': '#2E8B57', 'Sensors': '#212529', 'Cables': '#C8742B',
               'Cooling': '#4FA3D1', 'Mixed': '#BDBDBD', 'Hands': '#9AA5B1'}
# The colour of every shared material, the same on all six pages, chosen to look like the material.
MATERIAL_COLOUR = {'Aluminium': '#B8C4CE', 'Magnesium': '#D6E2BE', 'Titanium': '#9A93B8', 'Steel': '#5F6B73',
                   'Copper': '#C8742B', 'Magnets (NdFeB)': '#8E3B46', 'Battery materials': '#E8B84A',
                   'Plastics': '#EFE3C8', 'Fibre composites': '#2F2F2F', 'Electronics': '#2E8B57',
                   'Ceramics': '#F7F7F2', 'Mixed': '#BDBDBD', NOT_ALLOCATED: '#FFFFFF'}


def robot_height(category: Category) -> tuple[float, str]:
    """The height the robot is drawn at, in metres, and how it was found: the anchor robot's height where the
    workbook gives one ('1.32 m | 35.0 kg'), else the middle of the category's height range ('1.73–1.85 m')."""
    found = re.search(r'(\d\.\d+)\s*m\b', category.anchor)
    if found:
        return float(found.group(1)), ''
    found = re.search(r'(\d\.\d+)\s*[–-]\s*(\d\.\d+)\s*m', category.height_and_mass)
    if found:
        low, high = float(found.group(1)), float(found.group(2))
        middle = (low + high) / 2
        return middle, (f'The workbook gives no height for the anchor robot: drawn at the middle of the '
                        f"category's height range, {kg(low)}–{kg(high)} m, so {kg(middle)} m.")
    return TALLEST, f'The workbook gives no height for this robot type: drawn at {kg(TALLEST)} m.'


def motors_by_region(parts_list: PartsList, lists: SharedLists) -> dict:
    """How many motors sit in each body region; a part split by units shares its motors like its units."""
    totals: dict = {}
    for part in parts_list.parts:
        place = lists.parts.get(part.row)
        if not place or not place.motors:
            continue
        if place.split:
            per_unit = place.motors / sum(place.split.values())
            for region, units in place.split.items():
                totals[region] = totals.get(region, 0) + units * per_unit
        else:
            totals[place.region] = totals.get(place.region, 0) + place.motors
    return totals


def bounds(rows: list) -> tuple[float, float]:
    """The sum of the minimums and the sum of the maximums of (minimum, mode, maximum) triples: the bounds of
    their total, if every one were at its minimum or every one at its maximum. Not a likely range."""
    return (sum(r[0] for r in rows if r[0] is not None), sum(r[2] for r in rows if r[2] is not None))


def spread(wanted: list, gap: float, top: float, bottom: float) -> list:
    """Positions for labels as near as possible to the `wanted` ones, at least `gap` apart and between `top` and
    `bottom`, in the order of the wanted positions."""
    order = sorted(range(len(wanted)), key=lambda i: wanted[i])
    placed = list(wanted)
    previous = top - gap
    for i in order:                                   # downwards: push each below the one above it
        placed[i] = previous = max(wanted[i], previous + gap)
    following = bottom + gap
    for i in reversed(order):                         # upwards: pull back what ran off the bottom
        placed[i] = following = min(placed[i], following - gap)
    return placed


def body_shapes(axes, cx: float, ground: float, size: float, **style) -> list:
    """The shapes of the schematic body, with its middle at `cx` and its soles at `ground` (inches), `size` inches
    tall; added to `axes` with `style`, and returned."""
    from matplotlib.patches import Circle, Polygon
    point = lambda u, v: (cx + u * size, ground - v * size)  # noqa: E731
    shapes = [Circle(point(*HEAD[0]), HEAD[1] * size, **style)]
    for name, (u0, u1, v0, v1) in BLOCKS.items():
        sides = [(u0, u1), (-u1, -u0)] if name == 'foot' else [(u0, u1)]
        for a, b in sides:
            shapes.append(Polygon([point(a, v0), point(b, v0), point(b, v1), point(a, v1)], closed=True, **style))
    for (u0, v0), (u1, v1), width in LIMBS.values():
        for sign in (1, -1):
            half = width / 2
            shapes.append(Polygon([point(sign * u0 - half, v0), point(sign * u0 + half, v0),
                                   point(sign * u1 + half, v1), point(sign * u1 - half, v1)], closed=True, **style))
    for sign in (1, -1):
        shapes.append(Circle(point(sign * HAND[0], HAND[1]), HAND_RADIUS * size, **style))
    for shape in shapes:
        axes.add_patch(shape)
    return shapes


def material_rows(materials: MaterialsList, lists: SharedLists, recipes: ElementRecipes | None = None) -> dict:
    """The (minimum, mode, maximum) of each material of one robot, gathered by shared material, with the pieces of
    a split name and, with the element recipes, of the battery as cells only. Not allocated has no bounds and is left
    out."""
    rows: dict = {}
    for shared, kg_, _, _ in material_pieces(materials, lists, recipes):
        if shared != NOT_ALLOCATED:
            rows.setdefault(shared, []).append(kg_)
    return rows


def battery_note(materials: MaterialsList, lists: SharedLists, recipes: ElementRecipes) -> str:
    """What a robot page says about its battery as cells only: how its cells were counted, and where the rest of the
    workbook's battery row goes."""
    battery = battery_row_of(materials, lists)
    builds = [b for b in lists.battery if b.robot == materials.number and b.kind == BUILD and b.name in recipes.cells]
    cells = battery_cells(materials, lists, recipes)
    names = sorted({b.name for b in builds})
    how = ("counted from the packs' voltage and capacity" if all(b.series for b in builds) else
           "counted from the packs' energy (no voltage or capacity found)")
    rest = battery.kg[1] - cells[1]
    places = [b.name for b in lists.battery if b.robot == materials.number and b.kind == REST]
    where = places[0] if len(places) == 1 else ', '.join(places[:-1]) + ' and ' + places[-1]
    rest_text = (f"The rest of the workbook's '{battery.family}' ({kg(battery.kg[1])} kg), {kg(rest)} kg at the mode, "
                 f'goes to {where}.' if rest >= 0 else
                 f"The workbook's '{battery.family}' ({kg(battery.kg[1])} kg) is {kg(-rest)} kg less than the cells at "
                 f"the mode; the difference comes out of {where}.")
    ways = f"{len(builds)} way{'s' * (len(builds) != 1)}"
    return (f"{BATTERY} (dotted): cells only, an estimate (E), {how}: {ways} to build the packs, from "
            f"{'; '.join(names)} (the bar is the middle one, the line the lightest to the heaviest; EVIDENCE.md E1.7j "
            f'and E1.7k). {rest_text}')


def draw_robot(category: Category, parts_list: PartsList, materials: MaterialsList | None, lists: SharedLists,
               path: str, params: Params, scale_kg: float | None = None, recipes: ElementRecipes | None = None) -> None:
    """The one-view schema of a robot type: its parts where they sit, as a robot, and what it is made of, as bars.
    `scale_kg` is the end of the kg axis, the same for all six robots; without it the robot's own largest bound. With
    the element recipes, the battery is drawn as cells only (sheet Battery cells of the shared lists)."""
    from matplotlib.patches import Circle, Rectangle as Box
    height_m, height_note = robot_height(category)
    size = height_m * ROBOT_SCALE
    groups = by_view(parts_list, lists, 'group')
    regions = by_view(parts_list, lists, 'region')
    motors = motors_by_region(parts_list, lists)
    made_of = by_material(materials, lists, recipes) if materials else {}
    total = parts_list.sum_kg[1] or 0
    built = bool(materials and recipes and lists.battery is not None and battery_cells(materials, lists, recipes))

    notes = [f'kg at the mode. Bounds: every part, or every material, at its minimum or at its maximum; the likely '
             f'range comes with the Monte Carlo of this robot type\'s stage.',
             'The bars show how much of each material the robot holds, not where it sits: the workbook does not link '
             'its parts to its materials. All six pages use the same kg scale.',
             'A schema: the shapes are not the robot\'s real shape. Its height is drawn to scale, the same on all six '
             'pages.']
    if height_note:
        notes.append(height_note)
    if not groups.get('Hands'):
        notes.append('No hands of their own in the parts list: not comparable for hands (point 2 of '
                     'SHARED_LISTS.md).')
    if is_notional(category.anchor):
        notes.append('The anchor robot is notional: a configuration the research assumes, not a robot that exists.')
    estimated = {piece[0]: piece[3] for piece in (material_pieces(materials, lists) if materials else []) if piece[2]}
    if estimated:
        notes.append(f"{', '.join(estimated)} (dotted): an estimate (E), the workbook's "
                     f"'{', '.join(sorted(set(estimated.values())))}' split by the shares of the sheet Splits (point 9 "
                     'of SHARED_LISTS.md).')
    if built:
        notes.append(battery_note(materials, lists, recipes))
    elif recipes and materials and any(b.robot == materials.number and b.kind == KEPT for b in lists.battery or []):
        notes.append(f"{BATTERY}: the workbook's row, already cells only; kept as it is (EVIDENCE.md E1.7d).")
    # Which bars hold an estimate: wholly (every piece of the bar) or in part (the rest of a battery row added to a
    # material the workbook also gives).
    pieces = material_pieces(materials, lists, recipes) if materials else []
    flags = {}
    for shared, _, guessed, _ in pieces:
        flags.setdefault(shared, set()).add(guessed)
    dotted = {name: (', estimate (E)' if marks == {True} else ', partly an estimate (E)')
              for name, marks in flags.items() if True in marks and name != NOT_ALLOCATED}
    note_lines = [line for note in notes for line in wrap('• ' + note, 190)]

    top = 1.75
    ground = top + TALLEST * ROBOT_SCALE + 0.15
    height = ground + 0.75 + (len(note_lines) + 2) * LINE + 0.5
    figure, page = new_page(PAGE_WIDTH, height)
    point = lambda cx, u, v: (cx + u * size, ground - v * size)  # noqa: E731

    # The heading: the robot, its mass and its motors.
    page.text(0.3, 0.3, f'How robot type {category.number} is built: {category.name}', fontsize=16,
              fontweight='bold', va='top')
    anchor = category.anchor.splitlines()[0] if category.anchor else '—'
    low, high = bounds([p.total_kg for p in parts_list.parts])
    stated = (f'Stated mass {kg(parts_list.stated_mass_kg)} kg ({parts_list.stated_evidence}). '
              if parts_list.stated_mass_kg is not None else '')
    write(page, 0.3, 0.75, [f'Anchor robot: {anchor}, {kg(height_m)} m tall. {stated}Its parts add up to '
                            f'{kg(total)} kg (bounds {kg(low)}–{kg(high)} kg).',
                            f'Electric motors outside the hands: {kg(sum(motors.values()))}.'], size=11)
    write(page, PARTS_X, top - 0.5, ['Its parts, where they sit'], size=12, weight='bold', align='center')
    write(page, (CHART_LEFT + CHART_RIGHT) / 2, top - 0.5, ['What it is made of'], size=12, weight='bold',
          align='center')

    # The parts robot: its outline is the shell, the dark lines its frame, and the parts drawn where they sit.
    body_shapes(page, PARTS_X, ground, size, facecolor=SHELL, edgecolor='#6C757D', linewidth=1.2)
    at = lambda u, v: point(PARTS_X, u, v)  # noqa: E731
    skeleton = [((0, 0.47), (0, 0.84)), ((-0.16, 0.82), (0.16, 0.82)), ((-0.06, 0.48), (0.06, 0.48))]
    for (u0, v0), (u1, v1), _ in LIMBS.values():
        skeleton += [((u0, v0), (u1, v1)), ((-u0, v0), (-u1, v1))]
    if groups.get('Frame'):
        for (u0, v0), (u1, v1) in skeleton:
            page.plot(*zip(at(u0, v0), at(u1, v1)), color=SKELETON, linewidth=2.2, solid_capstyle='round')
    if groups.get('Cables'):
        route = [(-0.055, 0.73), (-0.105, 0.70), (-0.105, 0.52), (-0.075, 0.47), (-0.08, 0.28)]
        page.plot(*zip(*[at(u, v) for u, v in route]), color=PART_COLOUR['Cables'], linewidth=1.6)
    for group, (u0, u1, v0, v1) in (('Battery', (-0.08, 0.08, 0.58, 0.65)), ('Computer', (-0.055, 0.055, 0.725, 0.775)),
                                    ('Mixed', (0.0, 0.05, 0.67, 0.71))):
        if groups.get(group):
            (x0, y1), (x1, y0) = at(u0, v0), at(u1, v1)
            page.add_patch(Box((x0, y0), x1 - x0, y1 - y0, facecolor=PART_COLOUR[group], edgecolor='black',
                               linewidth=0.6))
    if groups.get('Sensors'):
        (x0, y1), (x1, y0) = at(-0.045, 0.945), at(0.045, 0.965)
        page.add_patch(Box((x0, y0), x1 - x0, y1 - y0, facecolor=PART_COLOUR['Sensors']))
        for sign in (1, -1):
            page.add_patch(Circle(at(sign * 0.025, 0.915), 0.009 * size, facecolor=PART_COLOUR['Sensors']))
    if groups.get('Cooling'):
        page.add_patch(Circle(at(-0.1, 0.79), 0.017 * size, facecolor=PART_COLOUR['Cooling'], edgecolor='black',
                              linewidth=0.6))
    if groups.get('Hands'):
        for sign in (1, -1):
            page.add_patch(Circle(at(sign * HAND[0], HAND[1]), HAND_RADIUS * size, facecolor=PART_COLOUR['Hands'],
                                  edgecolor='black', linewidth=0.8))
    # Motors: a dot on each joint of a region the workbook places motors in, a ring on the other joints where the
    # workbook places motors in several regions without saying how many sit where.
    spread_motors = motors.get('Whole body', 0)
    for region, joints in JOINTS.items():
        for u, v in joints + ([(-u, v) for u, v in joints] if region in MIRRORED else []):
            if motors.get(region):
                page.add_patch(Circle(at(u, v), 0.016 * size, facecolor=MOTOR, edgecolor='white', linewidth=0.8))
            elif spread_motors:
                page.add_patch(Circle(at(u, v), 0.016 * size, facecolor='white', edgecolor=MOTOR, linewidth=1.4))

    # The labels of the part groups, to the left, each pointing at where its parts sit.
    shown = [g for g in lists.names[PART_GROUP] if groups.get(g)]
    wanted = [at(*PART_SPOTS.get(g, (0, 0.5)))[1] - 0.2 for g in shown]
    ys = spread(wanted, 0.62, top + 0.1, ground - 0.5)
    for group, y in zip(shown, ys):
        members = [p for p in parts_list.parts if lists.parts.get(p.row) and lists.parts[p.row].group == group]
        low, high = bounds([p.total_kg for p in members])
        detail = f'{len(members)} part{"s" * (len(members) > 1)}'
        if group == 'Joint drives':
            detail += f', {kg(sum(motors.values()))} motors'
        colour = PART_COLOUR.get(group, SKELETON if group == 'Frame' else MOTOR if group == 'Joint drives'
                                 else '#6C757D')
        page.add_patch(Box((0.3, y), 0.12, 0.38, facecolor=colour, edgecolor='none'))
        write(page, 0.5, y, [f'{group}: {kg(groups[group])} kg'], weight='bold')
        write(page, 0.5, y + LINE, [f'{detail}; bounds {kg(low)}–{kg(high)} kg'])
        target = at(*PART_SPOTS.get(group, (0, 0.5)))
        page.plot([3.75, target[0]], [y + 0.18, target[1]], color='#8A8A8A', linewidth=0.6, linestyle='--')

    # The labels of the body regions, in the middle, pointing at the robot's left side, above the box of what is
    # spread over the whole body.
    label_x = PARTS_X + 0.25 * TALLEST * ROBOT_SCALE
    whole_lines = []
    if regions.get('Whole body'):
        # What this robot places over the whole body, in the order of the part groups.
        spread_out = {lists.parts[p.row].group for p in parts_list.parts if p.row in lists.parts
                      and 'Whole body' in ([lists.parts[p.row].region] + list(lists.parts[p.row].split))}
        what = [g.lower() for g in lists.names[PART_GROUP] if g in spread_out and g != 'Joint drives']
        if any(lists.parts[p.row].group == 'Joint drives' and not lists.parts[p.row].motors
               and lists.parts[p.row].region == 'Whole body' for p in parts_list.parts if p.row in lists.parts):
            what.append('gearboxes')
        if spread_motors:
            what.append(f'{kg(spread_motors)} motors the workbook places in several regions without saying how many '
                        'sit where (rings)')
        listed = what[0] if len(what) == 1 else ', '.join(what[:-1]) + ', and ' + what[-1] if what else ''
        whole_lines = [f'Spread over the whole body: {kg(regions["Whole body"])} kg'] + wrap(listed, 34)
    whole_y = ground - 0.35 - len(whole_lines) * LINE
    shown = [r for r in ('Head', 'Arms', 'Hands', 'Torso', 'Legs') if regions.get(r)]
    wanted = [at(*REGION_SPOTS[r])[1] - 0.2 for r in shown]
    ys = spread(wanted, 0.55, top + 0.1, whole_y - 0.6)
    for region, y in zip(shown, ys):
        count = motors.get(region, 0)
        motor_line = (f'{kg(count)} motor{"s" * (count != 1)}' if count else
                      'its motors are inside, not counted' if region == 'Hands' else 'no motors')
        write(page, label_x, y, [f'{region}: {kg(regions[region])} kg'], weight='bold')
        write(page, label_x, y + LINE, [motor_line])
        target = at(*REGION_SPOTS[region])
        page.plot([label_x - 0.08, target[0]], [y + 0.18, target[1]], color='#8A8A8A', linewidth=0.6,
                  linestyle='--')
    if whole_lines:
        write(page, label_x, whole_y, whole_lines[:1], weight='bold')
        write(page, label_x, whole_y + LINE, whole_lines[1:])

    # What it is made of: one bar per shared material, in the order of the sheet Lists and on the same kg scale on
    # all six pages (Matthias, 2026-10-26: "the material compsotion as bar plat"); the line on a bar runs from the
    # sum of its minimums to the sum of its maximums; 'Not allocated' hatched.
    names = lists.names[MATERIAL]
    rows = material_rows(materials, lists, recipes) if materials else {}
    whole = sum(made_of.values()) or 1
    chart_top, chart_bottom = top + 0.15, ground - 0.55
    axes = figure.add_axes([CHART_LEFT / PAGE_WIDTH, 1 - chart_bottom / height,
                            (CHART_RIGHT - CHART_LEFT) / PAGE_WIDTH, (chart_bottom - chart_top) / height])
    values = [made_of.get(name, 0) for name in names]
    drawn = axes.barh(range(len(names)), values, height=0.62, linewidth=0.5, edgecolor='#6C757D',
                      color=[MATERIAL_COLOUR.get(name, '#BDBDBD') for name in names])
    scale = scale_kg or max([bounds(r)[1] for r in rows.values()] + values + [1])
    for i, name in enumerate(names):
        if name == NOT_ALLOCATED:
            drawn[i].set_hatch('///')
        elif name in dotted:
            drawn[i].set_hatch('..')
        end = values[i]
        if rows.get(name):
            low, high = bounds(rows[name])
            axes.plot([low, high], [i, i], color='black', linewidth=1)
            for at_kg in (low, high):
                axes.plot([at_kg, at_kg], [i - 0.15, i + 0.15], color='black', linewidth=1)
            end = max(end, high)
        shown = f'{kg(values[i])} kg ({values[i] / whole:.0%})' + dotted.get(name, '')
        axes.text(end + scale * 0.02, i, shown if values[i] else '–', va='center', fontsize=9)
    axes.set_ylim(len(names) - 0.5, -0.5)
    axes.set_yticks(range(len(names)), names, fontsize=9.5)
    axes.set_xlim(0, scale * 1.3)
    axes.tick_params(axis='x', labelsize=9)
    axes.set_xlabel('kg at the mode; the line: from all minimums to all maximums (bounds)', fontsize=9)
    for side in ('top', 'right'):
        axes.spines[side].set_visible(False)
    write(page, (CHART_LEFT + CHART_RIGHT) / 2, ground + 0.12,
          [f'In all: {kg(whole)} kg, its materials and what they leave out of its parts list.'], align='center')

    # The ground, the height of the tallest robot type (so that the scale shows), the notes.
    page.plot([PARTS_X - 0.3 * size, PARTS_X + 0.3 * size], [ground, ground], color='black', linewidth=1)
    tallest = ground - TALLEST * ROBOT_SCALE
    page.plot([PARTS_X - 2.2, PARTS_X + 2.2], [tallest, tallest], color='#B0B0B0', linewidth=0.8, linestyle=':')
    write(page, PARTS_X, tallest - 0.24, [f'{kg(TALLEST)} m: the tallest robot type, drawn at the same scale'],
          colour='#8A8A8A', align='center')
    write(page, PARTS_X, ground + 0.12, [f'{kg(height_m)} m'], align='center')
    y = write(page, 0.3, ground + 0.55, note_lines)
    recipes_source = f'; the cells in {params.data.element_recipes}' if built else ''
    write(page, 0.3, y + 0.1, [f'Source: {params.data.workbook} and the placements in {params.data.shared_lists}'
                               f'{recipes_source}.'])
    save(figure, path, params.output.dpi)


def draw_overview(book: Workbook, faults: list[Fault], reports: dict, path: str, params: Params) -> None:
    """The first page: the stages, how a mass is given, the six categories, the faults, what is open."""
    width = PAGE_WIDTH
    columns = 3
    box_width = (width - 0.6 - (columns - 1) * 0.3) / columns

    # The text of each category's box, to size the page before drawing it.
    category_boxes = []
    for category in book.categories:
        parts_list = book.parts_lists.get(category.number)
        lines = wrap(f'Anchor robot: {category.anchor.splitlines()[0] if category.anchor else "—"}', 70)
        if is_notional(category.anchor):
            lines += ['(notional: a configuration, not a robot that exists)']
        if parts_list:
            lines += [f'Parts list: {len(parts_list.parts)} parts, {kg(parts_list.sum_quantity)} units',
                      f'Sum of the parts: {triple(parts_list.sum_kg)} kg (min / mode / max)',
                      f'Stated mass of the anchor robot: {kg(parts_list.stated_mass_kg)} kg']
        else:
            lines += ['No parts list in the workbook.']
        report = reports.get(category.number)
        lines += wrap_name('Report of its own: ', report, 80) if report else ['No report of its own']
        category_boxes.append((f'{category.number}  {category.name}', lines))
    box_lines = max([len(lines) for _, lines in category_boxes] + [1]) + 1
    box_rows = -(-len(category_boxes) // columns)

    without_report = [str(c.number) for c in book.categories if not reports.get(c.number)]
    notional = [str(c.number) for c in book.categories if is_notional(c.anchor)]
    open_items = []
    if without_report:
        open_items.append(f"Categories without a report of their own in documentation/sources/: "
                          f"{', '.join(without_report)}. The workbook's last row names reports 00 to 06.")
    if notional:
        open_items.append(f"Categories whose anchor robot is notional: {', '.join(notional)}.")
    open_lines = [line for item in open_items for line in wrap('• ' + item, 175)]

    # The stages' boxes, as high as the longest text needs.
    stage_width = (width - 0.6 - (len(STAGES) - 1) * 0.5) / len(STAGES)
    stage_texts = [wrap(what, int(stage_width / 0.07)) for _, what in STAGES]
    stage_height = 0.1 + LINE * 1.2 + max(len(lines) for lines in stage_texts) * LINE + 0.1
    height = 0.6 + 0.45 + stage_height + 0.25 + 0.6 + 4 * LINE + 0.45 + box_rows * (box_lines * LINE + 0.45) + 0.6 \
        + LINE * 2 + 0.4 + len(open_lines) * LINE + 0.5
    figure, axes = new_page(width, height)
    axes.text(0.3, 0.3, 'Overview: how we model a humanoid robot', fontsize=16, fontweight='bold', va='top')

    # The stages, as boxes joined by arrows.
    y = 0.95
    write(axes, 0.3, y, ['The stages, run in this order by pressing Run'], size=11, weight='bold')
    y += 0.35
    for i, ((name, _), lines) in enumerate(zip(STAGES, stage_texts)):
        x = 0.3 + i * (stage_width + 0.5)
        box(axes, x, y, stage_width, stage_height)
        write(axes, x + 0.12, y + 0.1, [name], weight='bold')
        write(axes, x + 0.12, y + 0.1 + LINE * 1.2, lines)
        if i:
            axes.add_patch(FancyArrowPatch((x - 0.45, y + stage_height / 2), (x - 0.05, y + stage_height / 2),
                                           arrowstyle='-|>', mutation_scale=14, color='black'))
    y += stage_height + 0.4

    # How a mass is given.
    write(axes, 0.3, y, ['How every mass is given'], size=11, weight='bold')
    y = write(axes, 0.3, y + 0.3, wrap(
        'Every mass in a parts list has a minimum, a mode and a maximum, in kg: for one unit of a part and for '
        'all units of it in one robot. These pages show the three numbers as the workbook states them; '
        '02_composition.py then draws each mass at random from a triangle on them (Monte Carlo). Each category is '
        'represented by one anchor robot, whose parts list stands for the category.', 175))
    y += 0.3

    # The categories, three to a row.
    write(axes, 0.3, y, [f'The {len(category_boxes)} categories of the 2026 research'], size=11, weight='bold')
    y += 0.35
    box_height = box_lines * LINE + 0.2
    for i, (title, lines) in enumerate(category_boxes):
        x = 0.3 + (i % columns) * (box_width + 0.3)
        top = y + (i // columns) * (box_height + 0.25)
        box(axes, x, top, box_width, box_height)
        write(axes, x + 0.12, top + 0.1, [title], weight='bold')
        write(axes, x + 0.12, top + 0.1 + LINE * 1.2, lines)
    y += box_rows * (box_height + 0.25) + 0.2

    # The faults and what is open.
    if faults:
        y = write(axes, 0.3, y, [f'{len(faults)} fault(s) found in the workbook: see faults.png.'], size=11,
                  colour=RED, weight='bold')
    else:
        y = write(axes, 0.3, y, ['No fault found in the workbook (what was checked: faults.png).'], size=11)
    y += 0.25
    write(axes, 0.3, y, ['Open'], size=11, weight='bold')
    y = write(axes, 0.3, y + 0.3, open_lines)
    write(axes, 0.3, y + 0.2, [f'Source: {params.data.workbook}.'])
    save(figure, path, params.output.dpi)


def draw_faults(faults: list[Fault], path: str, params: Params) -> None:
    """Every fault in red, or 'No fault found'; then what was checked and what was not."""
    width = 15.0
    fault_lines = []
    for fault in faults:
        where = f"Sheet '{fault.sheet}'" + (f', row {fault.row}' if fault.row else '')
        fault_lines += wrap(f'{where}: {fault.text}', 150) + ['']
    checked = [line for item in CHECKS_DONE for line in wrap('• ' + item, 150)]
    height = 0.6 + 0.4 + max(len(fault_lines), 1) * LINE + 0.5 + 0.35 + len(checked) * LINE + 0.5 \
        + 3 * LINE + 0.5
    figure, axes = new_page(width, height)
    axes.text(0.3, 0.3, 'Faults in the workbook', fontsize=16, fontweight='bold', va='top')
    y = 0.85
    if faults:
        y = write(axes, 0.3, y, fault_lines, colour=RED)
    else:
        y = write(axes, 0.3, y, ['No fault found.'], size=12, weight='bold')
    y += 0.3
    write(axes, 0.3, y, ['What was checked'], size=11, weight='bold')
    y = write(axes, 0.3, y + 0.3, checked)
    y += 0.2
    write(axes, 0.3, y, ['What was not checked'], size=11, weight='bold')
    y = write(axes, 0.3, y + 0.3, wrap(NOT_CHECKED, 150))
    write(axes, 0.3, y + 0.2, [f'Source: {params.data.workbook}.'])
    save(figure, path, params.output.dpi)


def file_name(category: Category) -> str:
    """The page of a category: '1_compact_research_developer.png'."""
    return f"{category.number}_{re.sub(r'[^a-z0-9]+', '_', category.name.lower()).strip('_')}.png"


def main() -> int:
    """Read and check the workbook, then draw the overview, one page per category and the faults."""
    try:
        params = current()
        book = read_workbook(absolute(params.data.workbook), params)
    except (ParameterError, WorkbookError) as error:
        print(error, file=sys.stderr)
        return 1

    faults = check_workbook(book, params)
    try:
        lists = read_shared_lists(absolute(params.data.shared_lists))
        faults += check_shared_lists(book, lists, params)
    except WorkbookError as error:
        lists = None
        print(f'{error} The shared-lists pages are not drawn.')
    # The element recipes, and the battery as cells only that the robot pages draw from them.
    recipes = None
    if lists is not None:
        try:
            recipes = read_element_recipes(absolute(params.data.element_recipes))
            faults += (check_element_recipes(recipes, params) + check_battery_cells(book, lists, recipes, params)
                       + check_material_recipes(book, lists, recipes, params))
        except WorkbookError as error:
            print(f'{error} The robot pages show the battery rows as the workbook gives them.')
    # Robot type 1 taken apart: read and checked here; drawn by the stage that follows it (step 5 of its plan).
    apart = None
    if lists is not None:
        try:
            apart = read_parts_taken_apart(absolute(params.data.parts_taken_apart))
            faults += (check_parts_taken_apart(apart, lists, params) + check_sibling_data(apart, params)
                       + check_robot_types(apart, book.categories))
        except WorkbookError as error:
            print(f'{error} Robot type 1 taken apart is not checked.')
    # The register of every known humanoid robot, against the robots taken apart.
    try:
        register = read_register(absolute(params.data.register))
        faults += check_register(register, params, list(apart.robots) if apart is not None else [])
    except WorkbookError as error:
        print(f'{error} The register is not checked.')
    sources = absolute(params.data.sources_dir)
    reports = {c.number: category_report(c.number, sources) for c in book.categories}
    out = absolute(params.output.schemas_dir)
    # One kg scale for the materials of all six robots: the largest bound, or the largest kilograms not allocated.
    scale_kg = None
    if lists is not None:
        scale_kg = max([bounds(rows)[1] for ml in book.materials_lists.values()
                        for rows in material_rows(ml, lists, recipes).values()]
                       + [by_material(ml, lists, recipes).get(NOT_ALLOCATED, 0)
                          for ml in book.materials_lists.values()] + [1])

    draw_overview(book, faults, reports, os.path.join(out, 'overview.png'), params)
    for category in book.categories:
        parts_list = book.parts_lists.get(category.number)
        path = os.path.join(out, 'categories', file_name(category))
        draw_category(category, parts_list, reports[category.number], faults, path, params)
        if lists is not None and parts_list is not None:
            draw_shared_lists(category, parts_list, book.materials_lists.get(category.number), lists, faults,
                              path.replace('.png', '_shared_lists.png'), params)
            draw_robot(category, parts_list, book.materials_lists.get(category.number), lists,
                       path.replace('.png', '_robot.png'), params, scale_kg, recipes)
    draw_faults(faults, os.path.join(out, 'faults.png'), params)

    print(f'{len(book.categories)} categories, '
          f'{sum(len(pl.parts) for pl in book.parts_lists.values())} parts and '
          f'{sum(len(ml.materials) for ml in book.materials_lists.values())} materials read from '
          f'{params.data.workbook}.')
    if lists is not None:
        print(f'{len(lists.parts)} parts and {len(lists.materials)} material names placed in '
              f'{params.data.shared_lists}.')
    print(f'{len(faults)} fault(s) found.' if faults else 'No fault found.')
    for fault in faults:
        print(f"  sheet '{fault.sheet}', row {fault.row}: {fault.text}")
    pages = len(book.categories) * (3 if lists is not None else 1)
    print(f'Drawn into {params.output.schemas_dir}/: overview.png, faults.png and {pages} pages in categories/.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
