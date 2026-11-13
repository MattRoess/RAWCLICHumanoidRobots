"""
02_composition.py
=================

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

What each robot type is made of, drawn at random (Monte Carlo): its materials, its elements, its part groups and its
body regions, kg per robot, written as the draws of each robot type, each on its own. Press Run. No arguments; every
setting is in `src/params_schema.py`. Run `00_parameters.py` and `01_schemas.py` first.

Matthias, 2026-10-26: "The composition has the be for each of the type as there are different stock and flows for
them", and, choosing the answer offered: "One stage, 02_composition.py, with the same code for all six robot types,
writing each type's composition separately for stock-and-flow, and a comparison stage after it." The specification he
agreed ("I agree with the specification of 02_composition.py and 03_comparison.py and with the recommendations a to
g"), points 1 to 18, is in documentation/claude/HANDOVER.md.

WHAT IT READS
-------------
The workbook (`data.workbook`), the shared lists (`data.shared_lists`) and the element recipes
(`data.element_recipes`), through the reading functions of 01_schemas.py, so that what is drawn here is what the pages
of 01 show (one copy of the code). And the settings `composition.draws`, `composition.seed` and the energy per kg of
the NMC cells (`composition.nmc_wh_per_kg_min`, `_mode`, `_max`).

The register (`data.register`): its sheet Robots, every known humanoid robot with its robot types, and its sheets Type 1
to Type 4, every robot of the type with what this run does with it (Matthias, 2026-10-29: "I want the all the know type
1 robots are integrated and included in the run", "There has to be an excel sheet where all the robots of the different
types are fully listed."). Where robots of a sheet Type n have rows of their own in their type's parts file
(`data.parts_taken_apart` with the type's folder, data/researched/<n>_<name>/parts_taken_apart.xlsx: every robot of type
1 since 2026-10-29; of type 2 five since 2026-10-30, "Yes, build C", 96 of its 97 since the robots on wheels, "Yes,
build it", EVIDENCE.md E9.7; batch 1 of types 3 and 4 since 2026-10-30, "Yes, build it", E11.7), the type is drawn part
by part over them, each from its own rows; a type with robots in several files (types 3 and 4: their robots taken apart
in types 1 and 2 too) over its robots of every file, each robot with its own file's shared numbers; for it 02 also reads
the sibling projects' files where they lie (RAWCLICVehicleElectronics' board metals and sensor elements,
RAWCLICDataCenters' tantalum, RAWCLICVehicleTractionMotor's steels) and runs RAWCLICVehicleTractionMotor's own code in
its own environment for the elements of the magnets.

WHAT IT CHECKS
--------------
Before drawing, every check of 01 (the list is `CHECKS_DONE` in 01_schemas.py) and its own, `check_composition`: an
item that follows a cell's energy sits only in the recipe of NMC cells. Any fault stops it before anything is written;
01's faults.png shows them. After drawing, in every draw (`draw_faults`): the materials and Not allocated add up to the
parts, and so do the part groups and the body regions; the elements of the recipes add up to the materials that have
recipes; the elements of interest add up to the materials they come from, copper and nickel each its element whole
and no other material giving more than it weighs (the light alloys their metal, E24); the cells and the rest add up to the battery row;
nothing is below zero except Not allocated. A fault there stops it too, except below zero in a draw where a remainder
of the robot drawn (its frame, a weighed pack's housing, a joint's structure) is below zero: that is reported in the
run and on the type's notes page, its draws kept as they are (Matthias, 2026-11-02, "A, as recommended", EVIDENCE.md
E21; CLAUDE.md §7: a remainder below zero keeps its negative draws, which show a fault).

HOW IT DRAWS (the same code for all six robot types, N = `composition.draws` times)
-------------------------------------------------------------------------------
  - Each part: the mass of all its units, one triangle on the workbook's minimum, mode and maximum (recommendation a).
    Its part group takes it, and its body region; a part split by units gives each region its units' part.
  - Each material row: a triangle on its minimum, mode and maximum. A row split by the sheet Splits: each share a
    triangle, the remainder 1 minus the others.
  - The battery row as cells (E1.7j, E1.7k): one build drawn in each draw, every build equally likely; the cells are
    their number times the mass of one cell; the rest, the row minus the cells, split by the shares of the sheet
    Battery cells. A kept row (robot types 2 and 6) is cells as it is, following the recipe it names.
  - The elements: each material piece that has a recipe, times the recipe's element shares, drawn: every share a
    triangle, every remainder 1 minus the others, every group of alternatives a discrete state drawn by its
    probabilities (never blended). A recipe is drawn once in each draw and used wherever it sits in the robot type:
    the hard-segment share of TPU is one uncertain quantity, not one per row. The parts of the NMC cell that follow
    the energy (its coatings and foils, E1.7i) are their mode times f, the cell's energy per kg over the mode of the
    NMC cells: of the drawn build's cell, or, for a kept row, drawn from the NMC cells' triangle (recommendation f).
  - Of the elements, only those of interest are written (EVIDENCE.md E19 point 3; Matthias, 2026-11-02, "Yes, agree
    E19"), from what is recovered as elements, as RAWCLICDataCenters counts them (`INTEREST`, `declared`): copper,
    nickel their element whole (Cu, Ni), with a recipe or without; the aluminium, magnesium and titanium alloys the
    metal their recipe holds (Al, Mg, Ti; their whole mass stays the material's: Matthias, 2026-11-02, "I need both
    alloy mass and then also the Al mass", EVIDENCE.md E24), their alloying elements staying in the alloy, in no
    element; the magnets their Nd, Pr, Dy, Tb, Co, B, Nb and Ga; the
    battery cells their Li, Ni, Co and Mn and the Cu and Al of their foils and tabs (their items 'As metal'); the
    boards and the sensors their metals of interest, not the glass, epoxy and bromine of the laminate. Steel, stainless
    steel, electrical steel, brass, plastics, fibre composites, ceramics and other stay materials. Every element of the
    recipes is still drawn, and checked to add up, but not written.
  - The electronics, the material Boards and components, by their components (Matthias, 2026-11-05: "senors are par
    of the elctronics!!", "3 yes", "Yes, include them", "yes do it"; EVIDENCE.md E32): the circuit boards, the cameras,
    the other sensors, the cables and the connectors. The cables (conductors and insulation) and the connectors (XT30,
    XT60) are booked in it, no longer in copper, brass and plastics, each with the elements of what it is made of. An
    element of interest of the electronics is written by its component, '<element>: Boards and components:
    <component>' in the table by_material; the materials keep the electronics one material.
  - Not allocated: the parts minus the materials, draw by draw. It is below zero where the drawn materials exceed the
    drawn parts (recommendation b); the summary gives the share of draws where it is.
  - Materials without a recipe yet: their kilograms are drawn, their elements by a recipe are not, and the summary
    says so (point 9 and recommendation c); copper and nickel are their element whole all the same, and a light alloy
    with no recipe its metal whole.
    A recipe added later needs no change here.
Each robot type has random numbers of its own, from the seed and its number, so that it gives the same draws however
many robot types are drawn. Nothing is normalised.

HOW IT DRAWS A ROBOT TYPE TAKEN APART (type 1: Matthias, 2026-10-28, "Yes in 02 it is all type 1 in.!", 2026-10-29,
"Yes, build it"; type 2: 2026-10-30, "Yes, build C", the same code; types 3 and 4: 2026-10-30, "Yes, build it", E11.7)
-----------------------------------------------------------------------------------------------------------
  - A type whose robots stand in several parts files (types 3 and 4, some of whose robots are taken apart in types 1
    and 2's files) is drawn over its robots of every file; its shared numbers (the constants for all robots, the joint's
    parts, the shares, the magnets by heat, the driver board) drawn once per file, each robot with its own file's; its
    recipes the type's own. Types 1 and 2 stand in their own file only and are drawn as before.
  - Each draw is one of the robots of the register's sheet Type n taken apart, all equally often; those without a
    stated mass are not drawn (named on the notes page; the sheet says "not drawn"), nor an outlier of the setting
    `composition.outliers` (the Neo1, in types 3 and 5: Matthias, 2026-11-04, "Ok it is neo. It should be out. Mark it
    as outlier."; EVIDENCE.md E30), which stays in its parts file, is named on the notes pages of its types and is
    counted nowhere (the sheet says "not drawn: an outlier"). A robot in several versions (the
    Booster K1, 5 Ah and 2 Ah; the GR-1, one or two cameras) is one of them, each as often (a discrete state). Its
    mass: a triangle on its own mass in the parts file (its sheet Constants); its parts: its own rows of the parts
    file, part by part, nothing scaled from another robot. Each type has random numbers of its own, from the seed and
    its number.
  - Until every robot of a type with a mass is taken apart (type 2 until its robots on wheels were entered; its one
    robot left, the Xialan S0, has no mass), its draws (the draws of the robot type) come from the workbook, as for a
    type none of whose robots is taken apart, and its robots taken apart are drawn part by part on their own, with
    their pages (Q2); its sheet says "not drawn: not yet taken apart" of the others (Q4).
  - The joints: each component of the G1's joint (sheet JointParts) drawn once in each draw for each joint size and
    shared by all the joints of that size; the large joint's the small one's grams times its factor. A joint whose
    module mass is given: its module mass drawn, its inside the G1's of its size times the module mass over the G1
    joint's mass at its modes, and the joint's structure (housing, end caps, output flange, small bearings) the
    explicit remainder, so that the joint weighs its drawn module mass. A robot whose sources give no joint torques:
    its joint modules one share of its mass, drawn, split among its joints by their fixed shares (EVIDENCE.md E5.17
    point 1). The G1's and G1+'s joints: as weighed. A robot on wheels (a joint of its wheeled base): the template on
    wheels, its own shared numbers ("…, on wheels", EVIDENCE.md E9.6 point 3); its hub, steering and lift motors drawn
    as joints; a lift column with no mass from its maker a share of the robot's mass less its motor (LESS_ITS_MOTOR).
  - A part of shares (sheet Shares): each share a triangle, the remainder 1 minus the others. Elements: aluminium and
    plastics by the type's own recipes (RECIPE_FAMILY), the NMC cells by theirs with the energy per kg drawn; copper
    is copper; a part of steel, titanium or a copper alloy by its grade (a recipe of the element recipes, or a steel
    of RAWCLICVehicleTractionMotor's workbook read where it lies, each element a triangle, iron the remainder); a
    material or grade written 'A or B' is either, each as often, the same in every place of a draw; the magnets by
    the grade class drawn for their joint's heat group (sheet MagnetGrades), one draw of heat deciding for every joint
    how hot the robot is built for; boards: copper their mass times the copper share, gold, silver, palladium, tin and
    nickel their area times the car board category's mg per cm2, tantalum their mass times the data centres' share;
    sensors: their car sensor elements (a sensor without a mass from its sources: its elements only). Of all these,
    the elements of interest are written, as for a robot type of the workbook (E19 point 3, above).
  - The battery: its energy its voltage times its capacity, or, where its sources give neither, its energy per kg of
    robot times its mass; its cells the energy over the cells' energy per kg, by their own chemistry (the grade of its
    cells' row: none, NMC cylindrical; the CASBOT W1's LFP cylindrical, one LFP cell of the sheet Cells drawn,
    EVIDENCE.md E9.4 C); its housing the pack less its cells and its management board where a source weighs the pack
    (a pack lighter than its cells, the Asimov's: no housing), else a share of its cells, the pack then its cells, its
    housing and its board (EVIDENCE.md E20: never below zero). The shell, where no
    source weighs it: a share of the robot's mass. The cables: their length times their conductors' cross-sections (two
    for power and two for signals, or two for power and an Ethernet line of eight: the Fourier robots of type 2) times
    copper's density, and their insulation. The frame: the robot's mass less every other part; where it falls below zero
    it is reported, not cut.
  - Its part groups: the four groups of how a robot is taken apart (01's TAKEN_APART: joints, battery, electronics,
    body), each the mass of its parts, every kilogram of a robot booked to its part (since 2026-11-08, "Yes, add 1 to
    3"; until then the shared lists' seven part groups by whole kinds). Its body regions: its kinds of part (ten; twelve
    with a wheeled base and a lift column) placed whole (KIND_BODY_REGION), kept so on his word (2026-10-29, "Yes,
    build them", point 5). A robot of two types is drawn in full in each (point 6).

WHAT IT WRITES
--------------
For each robot type, into `output.composition_dir`/<n>_<name>/ (`data/consolidated/`, the folder another repository
reads; not in git):

  materials.npy, elements.npy, part_groups.npy, body_regions.npy, total.npy
        the draws, kg per robot, float32, one row per draw (point 10, the format of RAWCLICVehicleTractionMotor:
        recommendation e); the elements those of interest (E19 point 3). Each has its columns, one name per line, in the .txt of the same name. Row i is the same
        draw in every array, so that a later stage can pair them.
  summary.xlsx, summary.csv
        per material and per element: the mean, the median and the 95 % interval (2.5 % and 97.5 %) over the draws
        that hold it (those not 0: a 0 is not part of a distribution, CLAUDE.md §7), the share of the draws that hold
        it, the share of all the draws below zero, and how much of each material is in the elements of interest
        (point 11: Yes, its element whole; Partly, its elements of interest; No, it stays a material).

For each robot type taken apart also, into `output.parts_dir`/<n>_<name>/ (`data/parts_taken_apart/<n>_<name>/`):
robots.npy (the robot of the parts file each draw is, its mass, the robot of the register drawn), parts.npy,
materials.npy, grades.npy, elements.npy and estimated.npy (every element of interest in every kind of part, and its kg
resting on masses labelled E), by_material.npy (every element of interest by the material it comes from, as the element
pages split it, '<element>: <material>', and the copper fixed in an alloy, '<element>: <material> (fixed in alloys)';
03_comparison.py draws it: EVIDENCE.md E29), places.npy and places_estimated.npy (every element of interest by its place: each
kind of part, the electronics by their components wherever they sit, the sensors by their kind since 2026-11-06; the
pages of where the critical elements sit, since 2026-11-05), taken_apart.npy (every element of interest by its kind of
part and its part of how a robot is taken apart, '<kind>: <part>: <element>', the parts of 01's TAKEN_APART: the four
groups joints, battery, electronics and body; since 2026-11-08, "I want a detailed list of the component ... to know
how to take it apart!!!", "Yes do it"; its parts add up to elements.npy, draw by draw, or 02 stops), each with its
columns in the .txt of the same name; register.txt (the robots of the register
drawn) and summary.csv (each element in all and in each kind of part: its mean, median and 95 % interval over the
draws that hold it, and the share of the draws that hold it).

The draws keep their zeros (a robot without a part holds 0 kg in it), since sums are made on raw draws; only the
statistics, the tables and the pages leave them out.

MEMORY (Matthias, 2026-11-13, after his run of 02 held 43 GB on his 16 GB computer, swapped for 48 minutes and wrote
nothing: "This is very very bad designe!!!", "Fix it damit and this never ever happens again. We always do Monte
Carlo", "It must adopte, so if data are added, it still works!!!"; the rule in the GitHub folder's CLAUDE.md §4).
Before any type is drawn, a trial of MEMORY_TRIAL draws of each robot type taken apart gives the memory it will need
at `composition.draws` (memory_needed); a type that would need more than MEMORY_SHARE of the computer's memory stops
the run there, nothing drawn. One robot type is held at a time: drawn, checked, its tables part by part and its
figures written, and its draws part by part let go before the next. Each robot's parts and joints' structures are held
over its own draws only (PartBlocks), so the memory grows with the draws and the materials and elements, not with the
number of robots; parts.npy is written robot by robot straight into the file. Everything goes into staging folders
('<output folder>.writing') and is moved into the output folders only when every type has added up: a run stopped by a
fault writes nothing. The outputs are byte for byte those of the code before (VERIFICATION V236).

Every robot type has the same columns of elements, all the elements of interest any of them holds (0 where a robot
type's materials hold none so far). Pages only of the robot types `output.robot_types_with_pages` names (Matthias, 2026-10-29: "Type 1
only"; types 1 and 2 since 2026-10-30, types 1 to 4 since 2026-10-30, E11.7 open point B); the draws of all six are
written. Into `output.composition_figures_dir`
(`figures/composition/`; not in git): for a robot type taken apart its notes (<n>_<name>_notes_<k>.png); its elements
of interest six a page (<n>_<name>_elements_<k>.png), each split by the material it comes from, as RAWCLICDataCenters'
05 (EVIDENCE.md E19 point 7; the preview of type 5, "Yes, build them", 2026-11-02); its materials nine a page
(<n>_<name>_materials_<k>.png: each material of the one list, then its grades, alloys or magnet classes; Matthias,
2026-10-29: "how much Copper and especially permanent magnets. The different steels and aluminum alyoys"; since
2026-11-02, "the material is much too detailed", "Yes, build it": the steels and the aluminium alloys as their material
only, their grades on the pages of where each sits and in the alloys table), each as its
total in one robot over the draws; and its alloys and grades in a table (<n>_<name>_alloys_<k>.png: what each holds by
its recipe and its kg in one robot, E19 point 4: "So if elements are in alloys, then one has to know it"); for another
robot type one page,
<n>_<name>.png: its kg by material and its kg by element, each bar the mean with a line over 95 % of the draws (point
14). Into `output.parts_figures_dir`/<n>_<name>/ (`figures/parts_taken_apart/<n>_<name>/`): a type taken apart its
overview of where its critical elements sit, place by place (robot_type_<n>_overview_<k>.png; type 1's the stage 04
until 2026-10-29, "Yes, into 02"; its element pages robot_type_<n>_elements_<k>.png removed on 2026-11-13, "Yes,
all"), and sources/<material>.png,
where copper, the magnets, each steel and each aluminium alloy sit, as RAWCLICDataCenters' "where the copper comes
from". The draws behind the material pages are written with the type's other tables: grades.npy, each material by
grade, alloy or magnet class in every kind of part.

WHAT IT SAYS WHILE IT RUNS
--------------------------
Each step as it begins and its time when it ends (Matthias, 2026-10-30: "Information on the working of 02 is poor",
"Yes, build them"; `Steps`): reading the inputs; checking every input; each robot type as it is drawn, part by part
(every tenth robot of its parts file said as it is drawn) or from the workbook; checking that the draws add up;
each type's draws written and its pages drawn; at the end "02 done in …", or, where a fault stops it, "02 stopped
after …: nothing is written". Every line is flushed at once, so that the console shows it while the next step runs.

Where it sits: after 01_schemas.py. 03_comparison.py reads what it writes (after robot type 6).
"""

from __future__ import annotations

import csv
import importlib.util
import math
import gc
import os
import resource
import shutil
import weakref
import re
import subprocess
import sys
import tempfile
import textwrap
import time
from dataclasses import dataclass, fields, replace
from types import SimpleNamespace

# Run from anywhere, and put the project root on the path, so that `src` imports. Must come before any import of src.
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import numpy as np  # noqa: E402
from openpyxl import Workbook  # noqa: E402
from openpyxl.styles import Font  # noqa: E402

from src.params_schema import ParameterError, Params, absolute, current  # noqa: E402


def load_schemas():
    """01_schemas.py as a module, to read and check the inputs with its functions. Its name starts with a digit, so it
    is loaded from its path, registered as 'schemas' (its dataclasses look their module up there while it loads), and
    only once: where the tests have loaded it already, that module is used."""
    path = os.path.join(HERE, '01_schemas.py')
    loaded = sys.modules.get('schemas')
    if loaded is not None and os.path.samefile(getattr(loaded, '__file__', path), path):
        return loaded
    spec = importlib.util.spec_from_file_location('schemas', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules['schemas'] = module
    spec.loader.exec_module(module)
    return module


schemas = load_schemas()
import matplotlib.pyplot as plt  # noqa: E402  (after 01, which sets matplotlib to draw into files only)
from matplotlib.patches import Patch  # noqa: E402
from matplotlib.textpath import TextPath  # noqa: E402
from matplotlib.transforms import blended_transform_factory, offset_copy  # noqa: E402

Fault = schemas.Fault
NOT_ALLOCATED, BATTERY, SPLIT = schemas.NOT_ALLOCATED, schemas.BATTERY, schemas.SPLIT
KEPT, BUILD, REST = schemas.KEPT, schemas.BUILD, schemas.REST

# The draws written for each robot type, in this order: each is a file <name>.npy with its columns in <name>.txt.
TABLES = ('materials', 'elements', 'part_groups', 'body_regions', 'total', 'copper')
# The columns of summary.csv and summary.xlsx.
# Its statistics are over the draws that hold the quantity, those not 0, with their share in 'Held in' (statistics_of).
SUMMARY_HEADINGS = ['Robot type', 'Kind', 'Name', 'Mean (kg)', 'Median (kg)', '2.5 % (kg)', '97.5 % (kg)',
                    'Held in (% of the draws)', 'Draws below zero (%)', 'In the elements', 'In the elements, mean (kg)']
# 01 lets the mass shares of a compound add up to 1 within this (check_element_recipes): the compounds written as mass
# shares are rounded to five decimals. The elements may miss the materials that have recipes by as much, and no more.
COMPOUND_TOLERANCE = 0.001
# The other sums of point 12 hold to the rounding of the computer; this is far above it and far below a gram.
SUM_TOLERANCE = 1e-9


# ------------------------------------------------------------------------------------------------------
# What is read, and what is drawn
# ------------------------------------------------------------------------------------------------------

@dataclass
class Inputs:
    """Everything 02 reads, through 01's reading functions."""

    book: object      # schemas.Workbook: the parts lists and the materials of every robot type
    lists: object     # schemas.SharedLists: where every part and material goes, the splits and the battery cells
    recipes: object   # schemas.ElementRecipes: the cells, the compounds, the recipes and which row follows which


@dataclass
class Piece:
    """A part of one robot type's materials in every draw: a material row, a share of a split row, the cells of a
    battery row or a share of its rest."""

    shared: str              # its shared material, e.g. 'Plastics'
    kg: np.ndarray           # its kilograms in every draw
    recipe: str | None       # the recipe of the sheet Recipe it follows; None where it has none yet
    f: np.ndarray | None     # cells: their energy per kg over the mode of the NMC cells, in every draw; else None


@dataclass
class Composition:
    """One robot type, drawn N times."""

    number: int               # the robot type, 1 to 6
    name: str                 # its folder: '1_compact_research_developer'
    title: str                # its name, e.g. 'Compact Research & Developer'
    tables: dict              # one of TABLES -> (its columns, its draws: N rows × one column each), kg, 'elements'
    #                           the elements of interest (E19 point 3); and, not written, 'recipe_elements': every
    #                           element by the recipes
    in_elements: np.ndarray   # N rows × the columns of 'materials': the kilograms of each that are elements of interest
    in_recipes: np.ndarray    # N rows × the columns of 'materials': the kilograms of each that follow a recipe
    battery: dict | None      # 'row', 'cells', 'rest': the battery row and its parts in every draw; None without one
    build: np.ndarray | None  # the build of the battery drawn in every draw, as its place among the robot type's
    #                           builds in the sheet Battery cells; None where the battery row is kept or not built
    remainder_below: np.ndarray | None = None   # N booleans: in the draw, a remainder of the robot drawn is below zero
    #                           (a type drawn part by part, E21); None for a type of the workbook

    def column(self, table: str, name: str) -> np.ndarray:
        """The draws of one column of one table, e.g. column('materials', 'Steel')."""
        columns, draws = self.tables[table]
        return draws[:, columns.index(name)]


def read_inputs(params: Params) -> Inputs:
    """The workbook, the shared lists and the element recipes, read with 01's functions. Raises schemas.WorkbookError
    when a file cannot be read at all."""
    return Inputs(schemas.read_workbook(absolute(params.data.workbook), params),
                  schemas.read_shared_lists(absolute(params.data.shared_lists)),
                  schemas.read_element_recipes(absolute(params.data.element_recipes)))


def check_composition(inputs: Inputs, params: Params) -> list:
    """The checks 02 adds to 01's. An item that follows the energy (E1.7i) is its mode times a cell's energy per kg
    over the mode of the NMC cells, so it can sit only in the recipe of NMC cells, used as the recipe of cells: by NMC
    cells of the sheet Cells, or named by a kept battery row; never named in the sheet Rows, nor held within another
    recipe, where there is no cell to take the energy from."""
    recipes = inputs.recipes
    where = os.path.basename(params.data.element_recipes) + ': '
    follows = {i.recipe for i in recipes.items if i.follows_energy}
    faults = []
    for cell in recipes.cells.values():
        if cell.recipe in follows and cell.chemistry != 'NMC':
            faults.append(Fault(where + schemas.CELLS_SHEET, cell.row,
                                f"{cell.name}: its recipe '{cell.recipe}' follows the energy per kg of NMC cells, but "
                                f'the cell is {cell.chemistry}.'))
    for r in recipes.rows or []:
        if r.recipe in follows:
            faults.append(Fault(where + schemas.ROWS_SHEET, r.row,
                                f"robot type {r.robot}, '{r.family}': the recipe '{r.recipe}' follows the energy of a "
                                'cell; it can only be the recipe of cells.'))
    for i in recipes.items:
        if i.compound in follows:
            faults.append(Fault(where + schemas.RECIPE_SHEET, i.row,
                                f"{i.recipe}, {i.item}: the recipe '{i.compound}' follows the energy of a cell; it can "
                                'only be the recipe of cells, not held within another recipe.'))
    return faults


def all_faults(inputs: Inputs, params: Params) -> list:
    """Every fault of the inputs: 01's checks (point 1 of the specification) and check_composition."""
    book, lists, recipes = inputs.book, inputs.lists, inputs.recipes
    return (schemas.check_workbook(book, params) + schemas.check_shared_lists(book, lists, params)
            + schemas.check_element_recipes(recipes, params) + schemas.check_battery_cells(book, lists, recipes, params)
            + schemas.check_material_recipes(book, lists, recipes, params) + check_composition(inputs, params))


def triangle(rng: np.random.Generator, low: float, mode: float, high: float, n: int) -> np.ndarray:
    """n draws of a triangle on its minimum, mode and maximum; the value itself where the minimum is the maximum."""
    if high == low:
        return np.full(n, float(mode))
    return rng.triangular(low, mode, high, n)


def whole_numbers(rng: np.random.Generator, low: float, mode: float, high: float, n: int) -> np.ndarray:
    """n draws of a count stated as a minimum, mode and maximum, each a whole number (EVIDENCE.md E31 point 3: the
    cameras no source counts, 1 / 3 / 12): the whole numbers from the minimum to the maximum, each k with the share of
    the triangle widened by half a unit on each side (minimum - 0.5, mode, maximum + 0.5) that lies between k - 0.5 and
    k + 0.5, so that the minimum and the maximum occur too and the mean stays the triangle's, (min + mode + max) / 3.
    The way RAWCLICDataCenters draws its counts (its `whole_number_probabilities`; Matthias, 2026-10-15: "there is no
    2.3 board, there is 1, 2 or 3"). One value where the minimum is the maximum. 01 has checked that the three are whole
    numbers from 1 up."""
    if high == low:
        return np.full(n, int(mode))
    values = np.arange(int(low), int(high) + 1)
    left, right = low - 0.5, high + 0.5

    def below(x: np.ndarray) -> np.ndarray:
        """The share of the widened triangle below x."""
        rising = (x - left) ** 2 / ((right - left) * (mode - left))
        falling = 1 - (right - x) ** 2 / ((right - left) * (right - mode))
        return np.clip(np.where(x <= mode, rising, falling), 0, 1)

    return rng.choice(values, size=n, p=below(values + 0.5) - below(values - 0.5))


def sensor_count(e, constants: dict, rng: np.random.Generator, n: int) -> np.ndarray | float:
    """The number in the robot of one sensor row `e` (01's ApartPart), in each of its n draws: the number its row
    gives; or one of the numbers it writes 'A or B' (EVIDENCE.md E38 point 2: an option of the robot, the Kuavo 5's
    touch hand, or a maker's reading that can mean either, the Walker S1's six tactile arrays a hand or the robot),
    each as often, a discrete state never blended; or, where it gives none, a whole number drawn from the robot's
    constant NUMBER_OF + its name (whole_numbers: E31 point 3's cameras; E38's joint temperature sensors, one or two a
    joint motor). 01 has checked each."""
    if e.count is not None:
        return e.count
    if e.either:
        return np.asarray(e.either, dtype=float)[rng.integers(len(e.either), size=n)]
    return whole_numbers(rng, *constants[schemas.NUMBER_OF + e.name][1], n).astype(float)


def shares_drawn(rng: np.random.Generator, pieces: list, n: int) -> list:
    """The shares of a group (a split row, or the rest of a battery row) in every draw, as (name, share): each piece
    given as (name, (minimum, mode, maximum), is the remainder); each share a triangle, the remainder 1 minus the
    others. 01 has checked that the largest shares leave the remainder at or above zero."""
    drawn = [(name, triangle(rng, *share, n)) for name, share, remainder in pieces if not remainder]
    rest = 1 - sum(share for _, share in drawn) if drawn else np.ones(n)
    return drawn + [(name, rest) for name, _, remainder in pieces if remainder]


class RecipeDraws:
    """The element shares of the recipes, drawn N times for one robot type. Each share of a recipe is drawn once and
    kept, and each group of alternatives draws its state once, so that a recipe gives the same draws wherever it sits
    in the robot type."""

    def __init__(self, recipes, rng: np.random.Generator, n: int):
        self.recipes, self.rng, self.n = recipes, rng, n
        # The draws kept (Shared.keep): None for all N; `size` their number. What is drawn later is drawn over all N
        # draws and then kept (kept), so that the random numbers are those drawn when every set held all N.
        self.rows, self.size = None, n
        self.members: dict = {}   # (recipe, the item they sit within, '' for the recipe itself) -> its items
        for i in recipes.items:
            self.members.setdefault((i.recipe, i.within), []).append(i)
        self.shares: dict = {}    # (recipe, item) -> the item's share in every draw
        self.states: dict = {}    # (recipe, group) -> the alternative drawn in every draw, as its place in the group
        self.done: dict = {}      # recipe -> its element shares and those as metal, for a recipe drawn without a
        #                           cell's energy

    def kept(self, values: np.ndarray) -> np.ndarray:
        """A draw over all N draws, as drawn (the same random numbers), kept over the draws this set keeps (`rows`,
        Shared.keep): all of them where it keeps all."""
        return values if self.rows is None else values[self.rows]

    def share(self, item, f: np.ndarray | None) -> np.ndarray:
        """One item's share of what it sits within, in every draw: its mode × f where it follows the energy, else a
        triangle drawn once."""
        if item.follows_energy:
            if f is None:   # check_composition prevents it
                raise ValueError(f'{item.recipe}, {item.item}: it follows the energy, but no cell is drawn here.')
            return item.share[1] * f
        key = (item.recipe, item.item)
        if key not in self.shares:
            self.shares[key] = self.kept(triangle(self.rng, *item.share, self.n))
        return self.shares[key]

    def elements(self, recipe: str, f: np.ndarray | None = None) -> dict:
        """The mass share of each element in `recipe`, in every draw: element -> N shares, adding up to 1 in every draw
        (to the rounding of the compounds). `f`: a cell's energy per kg over the mode of the NMC cells, in every draw,
        for a cell recipe whose items follow the energy."""
        return self.drawn(recipe, f)[0]

    def drawn(self, recipe: str, f: np.ndarray | None = None) -> tuple:
        """The element shares of `recipe` (elements()) and, of them, those of its items marked 'As metal', element -> N
        shares: the battery cells' foils and tabs, whose copper and aluminium are elements of interest (EVIDENCE.md E19
        point 3; Matthias, 2026-11-02, "The foils are recycled to the elements"); each drawn once."""
        if f is None and recipe in self.done:
            return self.done[recipe]
        out: dict = {}
        metal: dict = {}
        self.add(recipe, '', np.ones(self.size), f, out, metal, False)
        if f is None:
            self.done[recipe] = (out, metal)
        return out, metal

    def parts_of(self, recipe: str, within: str, f: np.ndarray | None) -> list:
        """The items of `recipe` that sit within `within`, each with its share of it in every draw: of alternatives
        the one drawn takes the whole; of shares each is drawn, the remainder 1 minus the others."""
        items = self.members[(recipe, within)]
        if items[0].probability is not None:
            # Alternatives: one is drawn in each draw, by its probability; it takes the group's whole weight.
            key = (recipe, within)
            if key not in self.states:
                self.states[key] = self.kept(self.rng.choice(len(items), size=self.n,
                                                             p=[i.probability for i in items]))
            return [(i, (self.states[key] == k).astype(float)) for k, i in enumerate(items)]
        # Shares: each drawn, the remainder 1 minus the others, never below zero (01 checks the largest shares).
        parts = [(i, self.share(i, f)) for i in items if not i.remainder]
        rest = 1 - sum(share for _, share in parts) if parts else np.ones(self.size)
        if rest.min() < -SUM_TOLERANCE:
            raise ValueError(f"{recipe}, within '{within or 'the recipe itself'}': the remainder falls below zero "
                             f'in {(rest < -SUM_TOLERANCE).sum()} draws.')
        return parts + [(i, rest) for i in items if i.remainder]

    def leaves(self, recipe: str, within: str = '', weight: np.ndarray | None = None) -> dict:
        """The recipes `recipe` is made of, each with its share of it in every draw, the shares its elements are drawn
        with: an item naming another recipe is followed down to the recipes made of compounds (type 1's aluminium: its
        die-cast alloy and its wrought 6061 and 7075; the gear stage 2's steel: its 20CrMnTi and GCr15); a recipe made
        of compounds is a leaf itself. The shares add up to 1 in every draw (Matthias, 2026-10-29: "The different
        steels and aluminum alyoys")."""
        weight = np.ones(self.size) if weight is None else weight
        out: dict = {}
        for i, share in self.parts_of(recipe, within, None):
            part = weight * share
            if i.compound in self.recipes.compounds:
                found = {recipe: part}
            elif i.compound:
                found = {leaf: part * s for leaf, s in self.leaves(i.compound).items()}
            else:
                found = self.leaves(recipe, i.item, part)
            for leaf, kg in found.items():
                out[leaf] = out.get(leaf, 0) + kg
        return out

    def add(self, recipe: str, within: str, weight: np.ndarray, f: np.ndarray | None, out: dict, metal: dict,
            as_metal: bool) -> None:
        """Adds to `out` the elements of the items of `recipe` that sit within `within`, which make up `weight` of the
        recipe in every draw, and to `metal` those of them that are parts of their own metal: an item marked 'As metal',
        or any item within one (`as_metal`)."""
        for i, share in self.parts_of(recipe, within, f):
            part = weight * share
            pure = as_metal or i.as_metal
            if i.compound in self.recipes.compounds:
                for element, mass_share in schemas.composition(self.recipes.compounds[i.compound][0]).items():
                    out[element] = out.get(element, 0) + part * mass_share
                    if pure:
                        metal[element] = metal.get(element, 0) + part * mass_share
            elif i.compound:   # another recipe, drawn once for the robot type
                inner, inner_metal = self.drawn(i.compound)
                for element, mass_share in inner.items():
                    out[element] = out.get(element, 0) + part * mass_share
                for element, mass_share in (inner if pure else inner_metal).items():
                    metal[element] = metal.get(element, 0) + part * mass_share
            else:              # a group of items within this one
                self.add(recipe, i.item, part, f, out, metal, pure)


def component_label(component: str) -> str:
    """The name an element of interest of the electronics is recovered from, by its component (E32): 'Boards and
    components: cameras'."""
    return f'{ELECTRONICS}: {component}'


# The metal of each light alloy (E24) on the element pages (Matthias, 2026-11-05: "the aluminum alloy figure is shit.
# It is just the al in the alloy", "Ok three separate collections and then just one total, but there I do not need an
# additional figure, as the alloys is so dominate. Work out a pragmatic solution", "Yes", then "A figure is a figure and
# not text"; EVIDENCE.md E33): its panel draws the metal its alloys hold alone, titled so (alloy_title), nothing written
# beside it; the battery cells' and the electronics' are on the means pages and named once on the notes pages. The
# draws keep the three collections and their total (the element) as they are. ALLOY_OF, the alloy of each metal,
# follows LIGHT_ALLOYS below.


def alloy_split(symbol: str, parts: dict) -> dict:
    """What an element's panel draws (E33): for the metal of a light alloy (ALLOY_OF: aluminium, magnesium, titanium),
    its alloy's draws alone; for every other element, `parts` as they are."""
    if symbol not in ALLOY_OF:
        return parts
    return {m: kg for m, kg in parts.items() if m == ALLOY_OF[symbol]}


def alloy_title(symbol: str) -> str:
    """The panel title of a light alloy's metal on 02's element pages (E33, relabelled): 'Aluminium (Al) in the
    alloys', 'Titanium (Ti) in the alloy'; every other element its label."""
    return (f'{element_label(symbol)} in the {ALLOY_OF[symbol].split()[-1]}' if symbol in ALLOY_OF
            else element_label(symbol))


# The light alloys' metals held in the sensors too, beside their alloy, shown by a panel of their own (Matthias,
# 2026-11-05: "where the hell is titanium in the sensor … I only see titanium alloy the heavy stuff. But not any
# information about the sensors", "Yes, add it"): titanium, its cameras' and other sensors' milligrams, its own scale,
# never in one panel with the alloy's kilograms (E33).
SENSORS_OF = ('Ti',)


def sensors_split(symbol: str, parts: dict) -> dict:
    """The sensors' part of an element ({the component's label: its draws}): its cameras' and other sensors' (the
    components CAMERAS and OTHER_SENSORS of the electronics, E32)."""
    labels = {component_label(c) for c in (CAMERAS, OTHER_SENSORS)}
    return {m: kg for m, kg in parts.items() if m in labels}


def sensors_title(symbol: str) -> str:
    """The panel title of an element's sensors: 'Titanium (Ti) in the sensors'."""
    return f'{element_label(symbol)} in the sensors'


# An element the NdFeB magnets and the sensors hold, and nothing else, in two panels: the magnets' and the sensors'
# (Matthias, 2026-11-06: "Gallium apart", to the proposal of its two panels, "Yes do it like this. Nd etc. are then
# similar as Ga in elements in Magnets"; EVIDENCE.md E38 point 5): in his run gallium (the magnets' from his
# traction-motor workbook, the sensors' from the LiDARs' and cameras' laser diodes and photodetectors), neodymium and
# dysprosium (the sensors' from the encoders' magnets) and boron. The magnets' grams never stack on the sensors'
# milligrams; on the element pages, the pages of where the critical elements sit and on 03.
def magnets_split(parts: dict) -> dict | None:
    """An element's draws by what it is recovered from (`parts`: {material or component: draws}) in two panels,
    {'magnets': {MAGNETS: draws}, 'sensors': {component: draws}}, where the NdFeB magnets and the sensors (the cameras
    and the other sensors, E32) each hold it in at least HELD_SHARE of the draws and nothing else does; else None (one
    panel, as before). A holder in fewer than HELD_SHARE of the draws is not drawn, as on every page."""
    sensors = sensors_split('', parts)
    magnets = parts.get(MAGNETS)
    if magnets is None or not held(magnets) or not sensors or not held(sum(sensors.values(), np.zeros_like(magnets))):
        return None
    if any(held(kg) for m, kg in parts.items() if m != MAGNETS and m not in sensors):
        return None
    return {'magnets': {MAGNETS: magnets}, 'sensors': sensors}


# What the notes pages of 02 and 03 say of it.
MAGNETS_NOTE = ("An element the NdFeB magnets and the sensors hold, and nothing else (such as gallium, neodymium and "
                "dysprosium), in two panels: in the magnets, and in the sensors (cameras and other sensors), so that "
                "the magnets' grams are never stacked on the sensors' milligrams.")


def magnets_title(symbol: str) -> str:
    """The panel title of an element's magnets: 'Gallium (Ga) in the magnets'."""
    return f'{element_label(symbol)} in the magnets'


# A page's legend in as many rows as it needs (Matthias, 2026-11-05: "1_elements_2 has text for the legend cut"; in 03
# until then, here since, one copy for 02's and 03's pages).
LEGEND_WIDTH = 15.0           # inches of the page's width a legend may take
LEGEND_ROW = 0.035            # the height of a legend's row, share of the page's height (14 points and its spacing)


def legend_columns(names: list) -> int:
    """How many entries of a page's legend go in a row, so that the legend stays within LEGEND_WIDTH: each entry as
    wide as the longest name at 14 points (about 0.6 of a point's width a character) and its colour's patch."""
    widest = max(len(name) for name in names) * APART_TEXT * 0.6 / 72 + 0.8
    return max(1, min(len(names), int(LEGEND_WIDTH // widest)))


def not_drawn_words(total: np.ndarray) -> str:
    """What a place on a page says where it has no panel: none, or held in fewer than 2.5 % of the runs (02's rule;
    03's too), its share written so that it is never '0 %' (share_text)."""
    if not total.any():
        return 'none in this robot type'
    return f'held in {share_text(float((total > 0).mean()))} of its runs:\nfewer than 2.5 %, no panel'


def sensor_component(units: list) -> str:
    """The component of the electronics a sensor is (E32), by its car sensor elements (`units`, (car sensor type,
    units in one sensor)): a camera where they hold an image sensor (IMAGE_SENSORS; a depth camera's infrared chips and
    laser diode with it), else another sensor."""
    return CAMERAS if any(car_type in IMAGE_SENSORS for car_type, _ in units) else OTHER_SENSORS


def sensor_kind(units: list) -> str | None:
    """The kind of a sensor (SENSOR_KINDS, E38 point 1) by its car sensor elements (`units`, (car sensor type, units in
    one sensor)), the first of these that holds: a laser diode array and a photodetector array, a LiDAR (a
    time-of-flight sensor too, made of the same: "time of flight and lidar are the same"); an image sensor, a camera
    (colour, stereo or depth, its infrared projector and chips with it: "combine all the cameras"); an angle sensor, a
    joint encoder; a position or pressure sensor, a hydraulic actuator's; MEMS microphones; an ultrasonic sensor; a
    motion sensor (IMU) alone; since E38 point 2 a temperature sensor (a joint motor's thermistor); a force sensor (the
    strain gauges of a six-axis force sensor or of a joint torque sensor); a pressure/force sensor or a capacitive
    sensor (the tactile sensors of the hands, head and torso); a capacitive touch sensor (a touch screen); a cellular
    modem (4G/5G); a GNSS receiver (satellite positioning).
    None for any other combination (02 stops on it, check_parts) and for a sensor of no car elements (a speaker: it
    holds no element of interest)."""
    held = {car_type for car_type, _ in units}
    if {'laser diode array', 'photodetector array'} <= held:
        return 'LiDARs'
    if held & set(IMAGE_SENSORS):
        return CAMERAS
    if 'angle sensor' in held:
        return 'joint encoders'
    if held & {'position sensor', 'pressure sensor'}:
        return "hydraulic actuators' sensors"
    if 'MEMS microphone array' in held:
        return 'microphones'
    if 'ultrasonic sensor' in held:
        return 'ultrasonic sensors'
    if held == {'IMU'}:
        return 'motion sensors'
    if 'temperature sensor' in held:
        return 'temperature sensors'
    if 'force sensor' in held:
        return 'force and torque sensors'
    if held & {'pressure/force sensor', 'capacitive sensor'}:
        return 'tactile sensors'
    if 'capacitive touch sensor' in held:
        return 'touch screens'
    if 'cellular modem' in held:
        return '4G/5G modems'
    if 'GNSS receiver' in held:
        return 'satellite receivers'
    return None


def sensor_place(kind: str, region: str) -> str:
    """Where a sensor sits (E38 point 7): '<electronics>: <kind>, <region>' ('Boards and components: cameras, head'), or
    its kind alone where it sits in every joint (IN_EVERY_JOINT) or its row names no region of REGION_WORDS."""
    if kind in IN_EVERY_JOINT or region not in REGION_WORDS:
        return component_label(kind)
    return component_label(f'{kind}, {REGION_WORDS[region]}')


def sensor_of_place(place: str) -> str | None:
    """The sensor kind of a place ('Boards and components: cameras, head' -> 'cameras'), None for a place that is no
    sensor's."""
    head = f'{ELECTRONICS}: '
    if not place.startswith(head):
        return None
    kind = place[len(head):].split(', ')[0]
    return kind if kind in SENSOR_KINDS else None


def merge_regions(places: dict) -> dict:
    """The places of the element pages (E38 point 7): a sensor's places in every region together under its kind
    ('Boards and components: cameras'), every other place as it is."""
    out = {}
    for place, kg in places.items():
        kind = sensor_of_place(place)
        key = component_label(kind) if kind else place
        out[key] = out.get(key, 0) + kg
    return out


def declared(material: str, shares: dict, metal: dict) -> dict:
    """The elements of interest one material is recovered as (E19 point 3), each as its share of the material's mass:
    copper and nickel their element whole (WHOLE, the share 1); the light alloys the metal their recipe holds, from
    `shares`, or, with no recipe (none so far), their metal whole (LIGHT_ALLOYS, E24); the magnets their MAGNET_ELEMENTS
    and the battery cells their CELL_ELEMENTS, from `shares`, their element shares by their recipe or fractions, and
    the CELL_METALS of their foils and tabs, from `metal`, those of the shares as metal; every other material none. The
    boards and the sensors are declared where they are drawn (Robot.board, Robot.sensor)."""
    if material in WHOLE:
        return {WHOLE[material]: 1.0}
    if material in LIGHT_ALLOYS:
        metal = LIGHT_ALLOYS[material]
        return {metal: shares.get(metal, 0.0)} if shares else {metal: 1.0}
    if material == MAGNETS:
        return {e: share for e, share in shares.items() if e in MAGNET_ELEMENTS}
    if material == CELL_MATERIAL:
        return {**{e: share for e, share in shares.items() if e in CELL_ELEMENTS},
                **{e: share for e, share in metal.items() if e in CELL_METALS}}
    return {}


def element_names(recipes) -> list:
    """Every element the compounds of the recipes hold, in the order of the periodic table: the same columns for every
    robot type."""
    found = set()
    for written, _ in recipes.compounds.values():
        found |= set(schemas.composition(written))
    return [element for element in schemas.ATOMIC_MASS if element in found]


def shown_name(name: str) -> str:
    """A name as the pages write it: a component of the electronics (component_label, '<electronics>: <component>') its
    component first and the electronics in brackets, 'LiDARs (boards and components)' (Matthias, 2026-11-06: "Have
    LIDAR etc. first and then just in brackets boards and components"; E38); every other name as it is. The draws'
    columns keep component_label."""
    head = f'{ELECTRONICS}: '
    if not name.startswith(head):
        return name
    component = name[len(head):]
    return f'{component[0].upper()}{component[1:]} ({ELECTRONICS.lower()})'


def element_page_name(material: str) -> str:
    """A material's name on the element pages and their means pages (ELEMENT_PAGE_NAMES, E37): a metal recovered whole
    as its own element by what it is ('Copper metal: windings, busbars, heat pipes'), a component of the electronics
    its component first (shown_name, E38), every other material by its name."""
    return ELEMENT_PAGE_NAMES.get(material) or shown_name(material)


def folder_name(category) -> str:
    """The folder of a robot type: '1_compact_research_developer', the name of its pages in 01."""
    return schemas.file_name(category)[:-len('.png')]


def battery_pieces(rng: np.random.Generator, n: int, number: int, family: str, row_kg: np.ndarray, inputs: Inputs,
                   row_recipe: dict, params: Params) -> tuple:
    """A battery row in every draw, as cells only (points 6 and 7): (its parts, as a dict of the row, the cells and the
    rest; the build drawn, or None where the row is kept; its pieces)."""
    rows = [b for b in inputs.lists.battery if b.robot == number]
    settings = params.composition
    kept = [b for b in rows if b.kind == KEPT]
    if kept:
        # Kept (robot types 2 and 6): the row is cells already, following the recipe the row names. Their energy per
        # kg is drawn from the NMC cells' triangle (recommendation f).
        f = triangle(rng, settings.nmc_wh_per_kg_min, settings.nmc_wh_per_kg_mode, settings.nmc_wh_per_kg_max,
                     n) / settings.nmc_wh_per_kg_mode
        parts = {'row': row_kg, 'cells': row_kg, 'rest': np.zeros(n)}
        return parts, None, [Piece(BATTERY, row_kg, kept[0].name, f)]

    # Built: one build in each draw, all equally likely; its cells are a fixed number of cells of a fixed mass.
    builds = [b for b in rows if b.kind == BUILD]
    cells = [inputs.recipes.cells[b.name] for b in builds]
    build = rng.integers(len(builds), size=n)
    cells_kg = np.array([schemas.cells_of(b, cell)[1] for b, cell in zip(builds, cells)])[build]
    f = np.array([cell.energy_wh / cell.grams * 1000 for cell in cells])[build] / settings.nmc_wh_per_kg_mode
    rest = row_kg - cells_kg
    pieces = []
    for recipe in dict.fromkeys(cell.recipe for cell in cells):   # one piece per recipe, in the order of the builds
        follows = np.array([cell.recipe == recipe for cell in cells])[build]
        pieces.append(Piece(BATTERY, cells_kg * follows, recipe, f))
    # The rest, split by the shares of the sheet Battery cells; a share to Not allocated stays there.
    group = [(b.name, b.share, b.remainder) for b in rows if b.kind == REST]
    for shared, share in shares_drawn(rng, group, n):
        pieces.append(Piece(shared, rest * share, row_recipe.get((number, family, shared)), None))
    return {'row': row_kg, 'cells': cells_kg, 'rest': rest}, build, pieces


def stack(columns: list, values: dict, n: int) -> np.ndarray:
    """The draws of `columns` side by side, N rows × one column each."""
    return np.column_stack([values[name] for name in columns]) if columns else np.zeros((n, 0))


def compose(category, inputs: Inputs, params: Params) -> Composition:
    """One robot type drawn N times: its parts, its materials, its battery as cells and its elements."""
    book, lists, recipes = inputs.book, inputs.lists, inputs.recipes
    n, number = params.composition.draws, category.number
    rng = np.random.default_rng([params.composition.seed, number])

    # The parts (point 3): the mass of all units of each part, one triangle; by part group and by body region.
    groups = {name: np.zeros(n) for name in lists.names[schemas.PART_GROUP]}
    regions = {name: np.zeros(n) for name in lists.names[schemas.BODY_REGION]}
    total = np.zeros(n)
    for part in book.parts_lists[number].parts:
        place = lists.parts[part.row]
        kg = triangle(rng, *part.total_kg, n)
        total += kg
        groups[place.group] += kg
        if place.split:
            for region, units in place.split.items():   # 01 checks that the units add up to the part's
                regions[region] += kg * units / part.quantity
        else:
            regions[place.region] += kg

    # The materials (points 4 to 6), as pieces of shared materials, each with the recipe it follows.
    row_recipe = {(r.robot, r.family, r.shared): r.recipe for r in recipes.rows or []}
    pieces, battery, build = [], None, None
    built = lists.battery is not None and any(b.robot == number for b in lists.battery)
    for m in book.materials_lists[number].materials:
        shared = lists.materials[m.family][0]
        kg = triangle(rng, *m.kg, n)
        if shared == SPLIT:
            group = [(p.shared, p.share, p.remainder) for p in lists.splits[m.family]]
            for piece, share in shares_drawn(rng, group, n):
                pieces.append(Piece(piece, kg * share, row_recipe.get((number, m.family, piece)), None))
        elif shared == BATTERY and built:
            battery, build, more = battery_pieces(rng, n, number, m.family, kg, inputs, row_recipe, params)
            pieces += more
        else:
            pieces.append(Piece(shared, kg, row_recipe.get((number, m.family, shared)), None))

    # The elements (point 7) of every piece that has a recipe, and of them the elements of interest each material is
    # recovered as (E19 point 3, declared: copper and nickel whole, the light alloys their recipe's metal, E24). A
    # piece of Not allocated stays out: Not allocated is the parts minus the materials (point 8).
    materials = lists.names[schemas.MATERIAL]
    kg_of = {name: np.zeros(n) for name in materials}
    with_recipe = {name: np.zeros(n) for name in materials}
    of_interest = {name: np.zeros(n) for name in materials}
    elements_found = element_names(recipes)
    recipe_elements = {name: np.zeros(n) for name in elements_found}
    elements: dict = {}                                       # element of interest -> kg
    fixed_cu = np.zeros(n)                                    # copper fixed in alloys (E25)
    draws = RecipeDraws(recipes, rng, n)
    for piece in pieces:
        if piece.shared == NOT_ALLOCATED:
            continue
        kg_of[piece.shared] += piece.kg
        shares, metal_shares = draws.drawn(piece.recipe, piece.f) if piece.recipe else ({}, {})
        if piece.recipe:
            with_recipe[piece.shared] += piece.kg
            for element, share in shares.items():
                recipe_elements[element] += piece.kg * share
        for element, share in declared(piece.shared, shares, metal_shares).items():
            elements[element] = elements.get(element, 0) + piece.kg * share
            of_interest[piece.shared] += piece.kg * share
        if piece.shared in FIXED_IN_ALLOYS['Cu'] and 'Cu' in shares:
            fixed_cu = fixed_cu + piece.kg * shares['Cu']
    kg_of[NOT_ALLOCATED] = total - sum(kg_of[name] for name in materials if name != NOT_ALLOCATED)

    element_columns = element_order(elements)
    tables = {'materials': (materials, stack(materials, kg_of, n)),
              'elements': (element_columns, stack(element_columns, elements, n)),
              'recipe_elements': (elements_found, stack(elements_found, recipe_elements, n)),
              'part_groups': (lists.names[schemas.PART_GROUP], stack(lists.names[schemas.PART_GROUP], groups, n)),
              'body_regions': (lists.names[schemas.BODY_REGION], stack(lists.names[schemas.BODY_REGION], regions, n)),
              'total': (['Total'], total[:, None]),
              'copper': copper_table(elements.get('Cu', np.zeros(n)), fixed_cu)}
    return Composition(number, folder_name(category), category.name, tables, stack(materials, of_interest, n),
                       stack(materials, with_recipe, n), battery, build)


# ------------------------------------------------------------------------------------------------------
# What is checked in every draw, and what is written
# ------------------------------------------------------------------------------------------------------

def draw_faults(c: Composition) -> list:
    """Point 12, in every draw: the materials and Not allocated add up to the parts, and so do the part groups and the
    body regions; the elements of the recipes add up to the materials that have recipes; the elements of interest add
    up to the kilograms of the materials they come from, copper and nickel being their element whole and no other
    material giving more than it is (E19 point 3; the light alloys their metal, E24); the cells and the rest add up to the battery row;
    nothing is below zero except Not allocated. Each fault says in how many draws."""
    faults = []

    def count(wrong: np.ndarray, what: str) -> None:
        if wrong.any():
            k = int(wrong.sum())
            faults.append(f"robot type {c.number}: {what} in {k} draw{'s' if k != 1 else ''}.")

    total = c.column('total', 'Total')
    for table, what in (('materials', 'the materials and Not allocated do not add up to the parts'),
                        ('part_groups', 'the part groups do not add up to the parts'),
                        ('body_regions', 'the body regions do not add up to the parts')):
        count(np.abs(c.tables[table][1].sum(axis=1) - total) > SUM_TOLERANCE * np.abs(total), what)
    followed = c.in_recipes.sum(axis=1)
    count(np.abs(c.tables['recipe_elements'][1].sum(axis=1) - followed) > COMPOUND_TOLERANCE * followed,
          'the elements do not add up to the materials that have recipes')
    # The elements of interest (E19 point 3): their sum the kilograms declared of the materials; copper and nickel each
    # its element whole; no other material, the light alloys included (E24), more than it is.
    declared_kg = c.in_elements.sum(axis=1)
    count(np.abs(c.tables['elements'][1].sum(axis=1) - declared_kg) > SUM_TOLERANCE * np.abs(declared_kg),
          'the elements of interest do not add up to the materials they come from')
    columns, kg = c.tables['materials']
    for i, name in enumerate(columns):
        if name in WHOLE:
            count(np.abs(c.in_elements[:, i] - kg[:, i]) > SUM_TOLERANCE * np.abs(kg[:, i]),
                  f'{name} is not its element {WHOLE[name]} whole')
        elif name != NOT_ALLOCATED:
            # A material below zero where a remainder is (E21) holds its elements below zero too: reported, not here.
            count((c.in_elements[:, i] - kg[:, i] > COMPOUND_TOLERANCE * np.abs(kg[:, i]))
                  & ~((kg[:, i] < 0) & excused(c)), f'the elements of interest of {name} are more than it')
    if c.battery is not None:
        row = c.battery['row']
        count(np.abs(c.battery['cells'] + c.battery['rest'] - row) > SUM_TOLERANCE * np.abs(row),
              'the cells and the rest do not add up to the battery row')
    # The copper (E25): recycled as copper the element Cu; it and the copper fixed in alloys the inflow.
    copper = c.tables['copper'][1]
    cu = c.column('elements', 'Cu') if 'Cu' in c.tables['elements'][0] else np.zeros(len(copper))
    count(np.abs(copper[:, 0] - cu) > SUM_TOLERANCE * np.abs(cu), 'the copper recycled as copper is not the element Cu')
    count(np.abs(copper[:, 0] + copper[:, 1] - copper[:, 2]) > SUM_TOLERANCE * np.abs(copper[:, 2]),
          'the copper recycled and fixed in alloys do not add up to the inflow')
    # Below zero: a fault, except in a draw where a remainder of the robot drawn is below zero (E21): reported by
    # remainder_reports(), not stopped.
    for table in BELOW_ZERO_TABLES:
        columns, draws = c.tables[table]
        for i, name in enumerate(columns):
            if name != NOT_ALLOCATED:
                count((draws[:, i] < 0) & ~excused(c), f'{name} is below zero')
    return faults


# The tables checked for draws below zero, each with the words that name one of its columns in a report (E21).
BELOW_ZERO_TABLES = {'materials': 'the material', 'elements': 'the element of interest',
                     'recipe_elements': 'the element (by the recipes)', 'part_groups': 'the part group',
                     'body_regions': 'the body region'}


def excused(c: Composition) -> np.ndarray:
    """The draws in which a remainder of the robot drawn is below zero (E21): there a quantity below zero is reported,
    not a fault; none for a type of the workbook."""
    n = len(c.column('total', 'Total'))
    return c.remainder_below if c.remainder_below is not None else np.zeros(n, dtype=bool)


def remainder_reports(c: Composition) -> list:
    """What is below zero in the draws where a remainder of the robot drawn is below zero (Matthias, 2026-11-02, "A,
    as recommended", EVIDENCE.md E21): each quantity, in how many draws and in what share of all of them. Reported in
    the run and on the type's notes page, the draws kept as they are (CLAUDE.md §7)."""
    reports, mask = [], excused(c)
    for table, words in BELOW_ZERO_TABLES.items():
        columns, draws = c.tables[table]
        for i, name in enumerate(columns):
            k = int(((draws[:, i] < 0) & mask).sum()) if name != NOT_ALLOCATED else 0
            if k:
                reports.append(f"{words} {name} is below zero in {k} draw{'s' if k != 1 else ''} "
                               f"({100 * k / len(mask):.2g} % of the draws), where a remainder of the robot drawn is "
                               'below zero')
    return reports


def statistics_of(draws: np.ndarray) -> dict:
    """The mean, the median and the 95 % interval of one quantity over the draws that hold it, those not 0, with the
    share of the draws they are ('Held in (% of the draws)'), and the share of all the draws below zero. A 0 is not
    part of a distribution (Matthias, 2026-11-01: "If a value is 0 then it is NOT part of the distribution", "There
    needs to be a rule"; CLAUDE.md §7): a robot without a part holds 0 kg in it, which is no mass of that part. A
    remainder below zero keeps its negative draws, which show a fault. A quantity 0 in every draw has no statistics
    (None: an empty cell in a table, '–' on a page). Every statistic of 02 and 03 is made here."""
    draws = np.asarray(draws, dtype=float)
    held = draws[draws != 0]
    out = {'Held in (% of the draws)': float(100 * held.size / draws.size) if draws.size else 0.0,
           'Draws below zero (%)': float((draws < 0).mean() * 100) if draws.size else 0.0}
    if not held.size:
        return {'Mean (kg)': None, 'Median (kg)': None, '2.5 % (kg)': None, '97.5 % (kg)': None, **out}
    low, median, high = np.percentile(held, [2.5, 50, 97.5])
    return {'Mean (kg)': float(held.mean()), 'Median (kg)': float(median), '2.5 % (kg)': float(low),
            '97.5 % (kg)': float(high), **out}


def summary(c: Composition) -> list:
    """Point 11: per material and per element of interest of one robot type its statistics (statistics_of: over the
    draws that hold it); for each material whether it is in the elements of interest (E19 point 3: Yes, its element
    whole; Partly, its elements of interest; No, it stays a material), and its kilograms that are, at the mean over the
    same draws. One dict per row, keyed by SUMMARY_HEADINGS."""
    rows = []
    columns, draws = c.tables['materials']
    for i, name in enumerate(columns):
        kg, followed = draws[:, i], c.in_elements[:, i]
        if name != NOT_ALLOCATED and not kg.any():
            status = 'Not in this robot type'
        elif name == NOT_ALLOCATED or not followed.any():
            status = 'No'
        elif np.allclose(followed, kg, rtol=COMPOUND_TOLERANCE, atol=0):
            status = 'Yes'   # its elements add up to it, to the rounding of the compounds
        else:
            status = 'Partly'
        rows.append({'Robot type': c.number, 'Kind': 'Material', 'Name': name, **statistics_of(kg),
                     'In the elements': status,
                     'In the elements, mean (kg)': float(followed[kg != 0].mean()) if kg.any() else None})
    columns, draws = c.tables['elements']
    for i, name in enumerate(columns):
        rows.append({'Robot type': c.number, 'Kind': 'Element', 'Name': name, **statistics_of(draws[:, i]),
                     'In the elements': '', 'In the elements, mean (kg)': None})
    columns, draws = c.tables['copper']   # recycled as copper, fixed in alloys, the inflow (E25)
    for i, name in enumerate(columns):
        rows.append({'Robot type': c.number, 'Kind': 'Copper', 'Name': name, **statistics_of(draws[:, i]),
                     'In the elements': '', 'In the elements, mean (kg)': None})
    return rows


def copper_table(recycled: np.ndarray, fixed: np.ndarray) -> tuple:
    """The table 'copper' of a robot type (E25): its copper recycled as copper (the element Cu), fixed in alloys, and
    the inflow, their sum, draw by draw."""
    return list(COPPER_COLUMNS), np.column_stack([recycled, fixed, recycled + fixed])


def write(c: Composition, folder: str) -> None:
    """Points 10 and 11: the draws of one robot type, float32, each table with its columns (the elements those of
    interest, E19 point 3), and its summary."""
    os.makedirs(folder, exist_ok=True)
    for table in TABLES:
        columns, draws = c.tables[table]
        np.save(os.path.join(folder, f'{table}.npy'), draws.astype(np.float32))
        with open(os.path.join(folder, f'{table}.txt'), 'w', encoding='utf-8') as file:
            file.write(''.join(f'{name}\n' for name in columns))
    rows = summary(c)
    with open(os.path.join(folder, 'summary.csv'), 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=SUMMARY_HEADINGS)
        writer.writeheader()
        writer.writerows(rows)
    book = Workbook()
    sheet = book.active
    sheet.title = 'Summary'
    sheet.append(SUMMARY_HEADINGS)
    for cell in sheet[1]:
        cell.font = Font(bold=True)
    for row in rows:
        sheet.append([row[heading] for heading in SUMMARY_HEADINGS])
    for letter, width in zip('ABCDEFGHIJK', (11, 9, 24, 11, 11, 11, 11, 12, 12, 22, 14)):
        sheet.column_dimensions[letter].width = width
    sheet.freeze_panes = 'A2'
    book.save(os.path.join(folder, 'summary.xlsx'))


# ------------------------------------------------------------------------------------------------------
# A robot type over its robots, each part by part (type 1 since 2026-10-28, type 2 since 2026-10-30)
# ------------------------------------------------------------------------------------------------------

TYPE_ONE = 1   # robot type 1: its lowest mass (composition.type_one_lowest_kg) holds for it alone

# The twelve kinds of part of the figures (ten on legs, two more on wheels) with their names and colours, and the kind
# of a joint by the first word of its name: 01's (one copy, drawn by 01's page of robot type 1 too).
KINDS, JOINT_KIND = schemas.KINDS, schemas.JOINT_KIND
# The kind of a part, board or sensor, by its column "Kind (the figure's row)": 01's (one copy; since 2026-10-30
# "Boards" for the boards, and the wheeled base and the lift column of a robot on wheels, EVIDENCE.md E9.7 point 1).
KIND_OF = schemas.PART_KIND
# The values of that column that are the joints themselves, or sit in them (driver boards, encoders): drawn with the
# joints, joint kind by joint kind.
IN_THE_JOINTS = {'Ankles and arms', 'Hips, knees and waist', 'Hips, knees, waist and shoulders', 'In the joints'}

# How a part of the sheet Parts is computed, by the start of its column "Remainder of, or computed from".
FROM_JOINTS = schemas.FROM_JOINTS                                       # the joint modules: drawn with the joints
FROM_SENSORS = schemas.FROM_SENSORS                                     # the encoders: their elements only
PACK = schemas.PACK_WHOLE                               # the battery pack: its cells and housing
CELLS = 'from the energy'                                              # the battery cells
HOUSING = schemas.PACK_REMAINDER                                       # the battery housing: a remainder
HOUSING_OF_CELLS = schemas.CELLS_SHARE                                 # of a pack not weighed: a share of its cells
CABLES = 'from Constants: length'                                      # the cables' conductors and insulation
SHELL = schemas.ROBOT_SHARE                                            # the shell: a share of the robot's mass
FRAME = schemas.ROBOT_REMAINDER                                        # the frame: the robot's remainder
# A hydraulic robot's (EVIDENCE.md E27.7): a place's actuators (their valves, boards, sensors and bodies), their bodies
# (the remainder), the oil (its volume times its density).
ACTUATORS, ACTUATOR_REST, OIL = schemas.ACTUATORS_WHOLE, schemas.ACTUATOR_REST, schemas.OIL_FROM
COMPUTED = FROM_JOINTS + (FROM_SENSORS, PACK, CELLS, HOUSING, HOUSING_OF_CELLS, CABLES, SHELL, FRAME, ACTUATORS,
                          ACTUATOR_REST, OIL)

# The JointParts component whose material is the joint's driver board.
DRIVER_BOARD = 'Driver board'
# The joint's structure: the JointParts components that are the explicit remainder of a joint whose module mass is
# stated (the X1's, the N1's), split among them in the G1's weighed proportions at their modes. Aluminium and steel,
# no copper or magnets; the housing alone was too small (below zero in 5.8 % of the large joints' draws, V57).
STRUCTURE = ('Housing', 'Two end caps', 'Output flange', 'Two small bearings')
# The materials 02 names (EVIDENCE.md E19, agreed 2026-11-02, "Yes, agree E19": one fixed list, each name what it is;
# before, 'Magnets (NdFeB)', 'Battery materials', 'Electronics', 'Aluminium', 'Magnesium', 'Mixed').
COPPER, MAGNETS, CELL_MATERIAL, ELECTRONICS = 'Copper', 'NdFeB magnets', 'Battery cells', 'Boards and components'
ALUMINIUM, MAGNESIUM, OTHER = 'Aluminium alloys', 'Magnesium alloys', 'Other'
# The electronics by their components (Matthias, 2026-11-05: "senors are par of the elctronics!!", "3 yes", the cables,
# connectors and antennas "Yes, include them", "yes do it"; EVIDENCE.md E32): the circuit boards (board(): a board's
# area and mass), the cameras (a sensor whose elements hold an image sensor, a depth camera's infrared chips and laser
# diode with it), the other sensors (joint encoders, motion sensors, LiDARs and time-of-flight sensors, microphones,
# ultrasonic sensors, the hydraulic actuators' position and pressure sensors, and since 2026-11-06 (E38 point 2) the
# joints' temperature sensors, force and torque sensors, tactile sensors, touch screens, 4G/5G modems and satellite
# receivers where the makers state them: sensor_component), the cables (their conductors and insulation) and the
# connectors (XT30, XT60). The cables and connectors are booked in the electronics, no longer in copper, brass and
# plastics, each with the elements of what it is made of (a cable's copper whole, a connector's brass its copper fixed
# in the alloy, E25). An element of interest of the electronics is recovered from its component, '<electronics>:
# <component>' (component_label): the element pages show it so; the materials pages and tables keep the electronics one
# material.
ELECTRONICS_COMPONENTS = ('circuit boards', 'cameras', 'other sensors', 'cables', 'connectors', 'capacitors')
CIRCUIT_BOARDS, CAMERAS, OTHER_SENSORS, CABLE_PARTS, CONNECTORS, CAPACITOR_PARTS = ELECTRONICS_COMPONENTS
# The car sensor types (RAWCLICVehicleElectronics' 07_, sheet Sensor Details) that are an image sensor: a sensor of the
# parts file whose elements hold one is a camera.
IMAGE_SENSORS = ('CMOS image sensor', 'IR camera sensor')
# The sensors by their kind on the pages of where the critical elements sit, and in places.npy (Matthias, 2026-11-06:
# "What I miss at the moment are the sensors. Temperature LIDAR, Cameras etc.", "Theses sensors are the location for
# cirticial raw materials such as indium galium etc.", "I would like to continue with the sensor work. This has to be
# resolved now"; EVIDENCE.md E38 point 1). A sensor's kind comes from its car sensor elements (sensor_kind), never from
# its name; the element pages by material keep the cameras and the other sensors (E32). All cameras one kind, colour,
# stereo and depth cameras, and the time-of-flight sensors with the LiDARs (Matthias, 2026-11-06: "combine all the
# cameras and time of flight and lidar are the same"). Each kind's colour on those pages is from Paul Tol's published
# schemes (muted, vibrant, light, dark), chosen by colour difference (CIE Lab) to stand apart from the kinds of part, the
# circuit boards, cables and connectors and from each other (V193), the cameras keeping their purple of E32.
# Where a sensor sits, on the overview pages: its kind and the body region its row names, "Cameras, head" (Matthias,
# 2026-11-06: "show me where they are located", to the proposal of kind and place together "Yes do it"; E38 point 7);
# the element pages stack the sensors by kind alone (merge_regions), their colours the kinds'. The joint encoders and
# the hydraulic actuators' sensors sit in every joint: one place each, no region.
REGION_WORDS = {'Head': 'head', 'Torso': 'torso', 'Arms': 'arms', 'Legs': 'legs', 'Base': 'wheeled base'}
IN_EVERY_JOINT = ('joint encoders', "hydraulic actuators' sensors", 'temperature sensors')
# The kinds the makers' statements added (Matthias, 2026-11-06, "Yes, all three"; EVIDENCE.md E38 point 2), each by
# the car sensor elements of its rows: the joints' temperature sensors (every joint motor's), the six-axis force sensors
# and the joint torque sensors, the tactile sensors of the hands, head and torso, the touch screens, the 4G/5G modems
# and the satellite receivers; their colours of Paul Tol's schemes as before (CIE Lab difference to the nearest other
# colour of those pages: 30.4, 23.7, 24.9, 24.0, 30.4, 20.5; the joint encoders' since 23.7, to the force sensors').
SENSOR_KINDS = {'LiDARs': '#332288', 'cameras': '#AA4499', 'joint encoders': '#666633',
                "hydraulic actuators' sensors": '#222255', 'microphones': '#BBBBBB', 'ultrasonic sensors': '#EE8866',
                'motion sensors': '#009988', 'temperature sensors': '#EE3377', 'force and torque sensors': '#225522',
                'tactile sensors': '#FFAABB', 'touch screens': '#EECC66', '4G/5G modems': '#BB5566',
                'satellite receivers': '#997700'}
# The notes page's words on the cameras no source counts (EVIDENCE.md E31 point 3; Matthias, 2026-11-05, "Yes, all
# ten", open item 6): their number drawn from the robot's constant NUMBER_OF, 1 / 3 / 12 (whole_numbers).
ESTIMATED_CAMERAS_WORDS = ("where no source counts a robot's cameras, 1 to 12 colour image sensors, most often 3, a "
                           'whole number in every run, an estimate')
CABLE_KIND = 'Cables'   # the sheets' kind of the cables and connectors (Kind (the figure's row))
# The elements of interest, and what each material gives of them (EVIDENCE.md E19 point 3 and questions 2 to 4;
# Matthias, 2026-11-02, "Yes, agree E19"): only what is recovered as elements, as RAWCLICDataCenters counts them, its
# twenty and this project's magnesium, titanium and indium. Copper and nickel are their metal whole (WHOLE); the
# aluminium, magnesium and titanium alloys keep their whole mass as materials (the total weight) and give the metal
# their recipe holds as their element (LIGHT_ALLOYS; Matthias, 2026-11-02: "I need both alloy mass and then also the Al
# mass. The first for the total weight and the last for the inflow needs", "Yes do it as writen in A"; EVIDENCE.md
# E24), their alloying elements staying in the alloy, in no element; the magnets give their rare
# earths, cobalt, boron, niobium and gallium; the battery cells their lithium, nickel, cobalt and manganese, and the
# copper and aluminium of their foils and tabs (their items 'As metal': "The foils are recycled to the elements"); the
# boards and the sensors their metals of interest, not the glass, epoxy and bromine of the laminate (Robot.board). Steel,
# stainless steel, electrical steel, brass, plastics, fibre composites, ceramics and other stay materials: no element.
INTEREST = ('Li', 'B', 'Mg', 'Al', 'Ti', 'Mn', 'Co', 'Ni', 'Cu', 'Ga', 'Sr', 'Nb', 'Pd', 'Ag', 'In', 'Sn', 'Ta', 'Au',
            'Pb', 'Nd', 'Pr', 'Dy', 'Tb')
WHOLE = {COPPER: 'Cu', 'Nickel': 'Ni'}
# Each of them on the element pages and their means pages by what it is, not by its element's name (Matthias,
# 2026-11-05: "Compariosn. We had this befor copper in copper does not make any sense", to the proposal "Yes,
# relabel"; 2026-11-06: "Relabel and page check"; EVIDENCE.md E37): the material Copper is the windings of the joints
# and wheel drives (84 to 93 % of it in his run of 2026-11-05), the battery's busbars and wires (6 to 11 %), the head's
# and the boards' heat pipes, vapour chambers and copper strips; the material Nickel the battery's nickel strips. The materials pages keep the material's name; colours and data as they are.
ELEMENT_PAGE_NAMES = {COPPER: 'Copper metal: windings, busbars, heat pipes',
                      'Nickel': "Nickel metal: the battery's nickel strips"}
LIGHT_ALLOYS = {ALUMINIUM: 'Al', MAGNESIUM: 'Mg', 'Titanium alloy': 'Ti'}
ALLOY_OF = {metal: alloy for alloy, metal in LIGHT_ALLOYS.items()}   # the alloy of each light alloy's metal (E33)
# The one sentence of the notes pages (02's and 03's) on what the light alloys' panels leave out (E33).
LIGHT_ALLOY_NOTE = ("Aluminium, magnesium and titanium: their panels show the metal held in the alloys alone; the "
                    "battery cells' and the electronics' aluminium, small beside it, are in the model's runs and on "
                    "the pages of the medians; the sensors' titanium has a panel of its own, titanium in the sensors.")
# The copper of a robot, three ways (Matthias, 2026-11-02: "So we have to add it to the inflow cupper, but we have to
# destiguish, what is fixed in alloys like Al aalloysa nd brass", "and what can be recycled as elemental Cu", "Yes,
# build it"; EVIDENCE.md E25): recycled as copper, the element Cu; fixed in alloys, the copper the materials of
# FIXED_IN_ALLOYS hold by their recipes or fractions, which goes where the alloy goes; and the inflow, both. Written as
# the table 'copper', one column each, draw by draw.
FIXED_IN_ALLOYS = {'Cu': (ALUMINIUM, 'Brass', 'Steel', 'Stainless steel', 'Electrical steel', 'NdFeB magnets',
                          MAGNESIUM)}
COPPER_COLUMNS = ('Cu recycled as copper', 'Cu fixed in alloys', 'Cu inflow')
MAGNET_ELEMENTS = ('Nd', 'Pr', 'Dy', 'Tb', 'Co', 'B', 'Nb', 'Ga')
CELL_ELEMENTS, CELL_METALS = ('Li', 'Ni', 'Co', 'Mn'), ('Cu', 'Al')   # of the whole cell; of its items 'As metal'
# The recipes of a robot type's aluminium and plastics: those its workbook rows of these families follow (sheet Rows
# of the element recipes): type 1's, and type 2's own (2026-10-30, "Yes, build C", Q3); and the recipe of the battery
# cells (the sheet Parts: "element_recipes.xlsx NMC cylindrical").
RECIPE_FAMILY = {1: {ALUMINIUM: 'Aluminum alloys', 'Plastics': 'Engineering polymers'},
                 2: {ALUMINIUM: 'Aluminum alloys', 'Plastics': 'Engineering plastics'},
                 # Types 3 and 4 since 2026-10-30 (EVIDENCE.md E11.7 point 7): the workbook's, and type 4's magnesium
                 # (the AgiBot A3's and A3 Ultra's frames, both of type 4 only).
                 3: {ALUMINIUM: 'Aluminum alloys', 'Plastics': 'Engineering plastics',
                     # Since types 5 and 6's entry (E16.6): the Kaleido 9's magnesium-alloy frame, its type's AZ91D.
                     MAGNESIUM: 'Magnesium alloys'},
                 4: {ALUMINIUM: 'Aluminum alloys', 'Plastics': 'Polymers & elastomers',
                     MAGNESIUM: 'Magnesium alloys'},
                 # Types 5 and 6 since 2026-11-01 (E16.6, "Find all the data for 5 and 6 and then fill in the data in
                 # the respective sheets"): the workbook's, its first plastics of each (the shell: type 5's "Composites &
                 # polymers", type 6's "Reinforced polymers"); type 5 has no magnesium recipe, so the Kaleido 9's frame,
                 # drawn in type 5, takes its own file's, type 3's AZ91D (E): a (type, family) pair names another type's.
                 5: {ALUMINIUM: 'Aluminum alloys', 'Plastics': 'Composites & polymers',
                     MAGNESIUM: (3, 'Magnesium alloys')},
                 6: {ALUMINIUM: 'Aluminum alloys', 'Plastics': 'Reinforced polymers'}}


def recipe_key(robot_type: int, shared: str, family) -> tuple:
    """The key of a recipe in the sheet Rows of the element recipes, (robot type, family, shared material): `family`
    the drawing type's own, or a (type, family) pair naming another type's (RECIPE_FAMILY)."""
    return (*family, shared) if isinstance(family, tuple) else (robot_type, family, shared)
CELL_RECIPE = 'NMC cylindrical'
# The recipe of the material Copper in the element recipes: copper metal, Cu, its one item 'As metal' (EVIDENCE.md E17;
# before, "copper is copper" was written here as {'Cu': 1}).
COPPER_RECIPE = 'Copper metal'
# The steel of the sibling's element workbook whose modes are a producer's typical values, the compound of the element
# recipes that holds them (EVIDENCE.md E5.18: "304 ... modes Outokumpu's typical C 0.04, Cr 18.1, Ni 8.1"); every other
# element of a sibling steel has the middle of its range as its mode (E), its remainder (iron) 1 minus the others.
SIBLING_MODES = {'Type 304': 'Stainless steel 304'}
# The materials shown by their alloys on the material pages, through the recipes the type's rows name (Matthias,
# 2026-10-29: "The different steels and aluminum alyoys"); plastics are shown whole. The magnesium alloys since E19
# (point 4, "Yes, build them", 2026-11-02): type 4's recipe is AM magnesium (AM50A or AM60B) and AZ91D, each an alloy of
# the alloys table.
ALLOYS = (ALUMINIUM, MAGNESIUM)

# The quantities of the sheet Constants this stage uses, as the sheet writes them.
ROBOT_MASS, = schemas.APART_ROBOT_CONSTANTS
# The ceramic capacitors of a joint's driver board (Matthias, 2026-11-06, "Yes, all three"; EVIDENCE.md E38 point 4):
# their number in a board of the G1's small joint (8 / 16 / 24, E: Ben Katz's Cheetah driver 8, mjbots' moteus 16, TI's
# humanoid joint drive TIDA-010979 17), a whole number in every draw, and one capacitor's barium titanate (the case
# sizes 0805 / 1206 / 1210 of KEMET/YAGEO's material declaration, mg).
CAPACITORS, CAPACITOR_TITANATE = schemas.CAPACITORS, schemas.CAPACITOR_TITANATE
# Barium titanate, BaTiO3, by its formula: the standard atomic weights of barium (137.327), titanium (47.867) and three
# of oxygen (15.999 each), so barium 58.9 %, titanium 20.5 % and oxygen 20.6 % of its mass.
TITANATE_ATOMS = {'Ba': 137.327, 'Ti': 47.867, 'O': 3 * 15.999}
# A large capacitor's organic rest (E51), the remainder of its shares: its paper, electrolyte, seal rubber and sleeve, by
# their elements, from FROLYT's declared masses of one radial capacitor (mg; RoHS_Umbrella_radial.pdf) and each one's
# formula: paper as cellulose C6H10O5 24.91; the electrolyte 83.66, its γ-butyrolactone C4H6O2 75 % with its 15 % of
# additives counted as it (E) and its ethylene glycol C2H6O2 10 %; the rubber as butyl (C4H8)n 76.61; the PET sleeve
# C10H8O4 20.68. The same for both kinds (E: the hybrid's rest is of the same materials, TDK). Shares of the rest.
ATOMS = {'C': 12.011, 'H': 1.008, 'O': 15.999, 'Al': 26.982, 'Si': 28.085}
ORGANIC_MIX = [(24.91, {'C': 6, 'H': 10, 'O': 5}), (83.66 * 0.90, {'C': 4, 'H': 6, 'O': 2}),
               (83.66 * 0.10, {'C': 2, 'H': 6, 'O': 2}), (76.61, {'C': 4, 'H': 8}), (20.68, {'C': 10, 'H': 8, 'O': 4})]


def formula_shares(atoms: dict) -> dict:
    """Each element's share of the mass of a formula ({'C': 6, 'H': 10, 'O': 5} -> {'C': 0.444, ...})."""
    total = sum(ATOMS[e] * k for e, k in atoms.items())
    return {e: ATOMS[e] * k / total for e, k in atoms.items()}


CAPACITOR_ORGANICS = {e: sum(mg * formula_shares(f).get(e, 0.0) for mg, f in ORGANIC_MIX) / sum(mg for mg, _ in ORGANIC_MIX)
                      for e in ('C', 'H', 'O')}
# The kaolinite of a liquid capacitor's seal (TDK, E51), Al2Si2O5(OH)4: its aluminium bound in the mineral, not an
# element of interest.
KAOLINITE = formula_shares({'Al': 2, 'Si': 2, 'O': 9, 'H': 4})
# The metals of a large capacitor's shares by their element; aluminium, copper and tin are elements of interest.
CAPACITOR_METALS = {'aluminium': 'Al', 'iron': 'Fe', 'chromium': 'Cr', 'copper': 'Cu', 'tin': 'Sn'}
LARGE_CAPACITOR_ITEM = 'Large capacitors'   # a joint's large capacitors among its components (draw_robot)
TITANATE = {element: weight / sum(TITANATE_ATOMS.values()) for element, weight in TITANATE_ATOMS.items()}
# A robot's cables, by the conductors they hold: four (two for power, two for signals), or two for power and an Ethernet
# line of eight (the Fourier robots of type 2, EVIDENCE.md E6.8 point 9).
CABLE_FOUR, CABLE_ETHERNET, ETHERNET_CS = schemas.CABLE_FOUR, schemas.CABLE_ETHERNET, schemas.ETHERNET_CS
VOLTAGE, CAPACITY = schemas.BATTERY_CONSTANTS
JOINT_SHARE, ENERGY_PER_KG = schemas.JOINT_SHARE, schemas.ENERGY_PER_KG
# A part that is a share of the robot's mass names its shared number (the shell's, a lift column's), a lift column
# "less its motor" (E9.7 point 3).
LESS_ITS_MOTOR = schemas.LESS_ITS_MOTOR
SHELL_SHARE = schemas.SHELL_SHARE
BOARD_G_PER_CM2, BOARD_COPPER = 'Board mass per cm2 (boards not weighed)', "Copper share of a board's mass"
POWER_CS, SIGNAL_CS = 'Power conductor cross-section (2 conductors)', 'Signal conductor cross-section (2 conductors)'
DENSITY, INSULATION = 'Copper density', 'Insulation and jackets, per mass of copper'
SENSOR_ALUMINIUM = 'Sensor housing, aluminium share'   # of a sensor module beyond its elements (point 3c)
BOARD_GLASS, BOARD_BROMINE = schemas.BOARD_GLASS, schemas.BOARD_BROMINE   # of a board's rest (point 3b)
GLASS_RECIPE, EPOXY_RECIPE = schemas.BOARD_REST_RECIPES

# The critical elements whose kilograms resting on estimates (E) are followed, for the overview figure (its hatching).
TRACKED = {'Cu', 'Al', 'Ag', 'Au', 'Pd', 'Ta', 'Nd', 'Pr', 'Dy', 'Ga', 'In'}

# What is written of a robot type part by part, in this order: each a file <name>.npy with its columns in
# <name>.txt.
APART_TABLES = ('robots', 'parts', 'materials', 'grades', 'elements', 'estimated', 'by_material', 'places',
                'places_estimated', 'taken_apart', 'taken_apart_mass')
# The table by_material's columns of an element fixed in an alloy, '<element>: <material> (fixed in alloys)' (E25): its
# copper not recovered as copper, beside the columns of each element of interest by the material it comes from
# (Matthias, 2026-11-04: "Yes, agree E29", question 2, "Yes, build 03").
FIXED_MARK = ' (fixed in alloys)'

# The elements of the magnets come from RAWCLICVehicleTractionMotor's own `magnet_element_draws`, run in that project's
# own environment (its pinned numpy), where it lies; it writes each grade class's fractions into a temporary folder.
MAGNET_SCRIPT = '\n'.join([
    'import os, sys',
    'import numpy as np',
    'sys.path.insert(0, os.getcwd())',
    'from src.params_schema import Params',
    'from src.composition import magnet_element_draws',
    'folder, n = sys.argv[1], int(sys.argv[2])',
    'for klass in sys.argv[3:]:',
    '    names, drawn = magnet_element_draws(Params(), "", n, klass)',
    '    np.save(os.path.join(folder, klass + ".npy"), drawn)',
    '    with open(os.path.join(folder, klass + ".txt"), "w", encoding="utf-8") as file:',
    '        file.write("\\n".join(names))',
])


# ------------------------------------------------------------------------------------------------------
# What is read and checked
# ------------------------------------------------------------------------------------------------------

@dataclass
class ApartInputs:
    """Everything 02 reads for one robot type, drawn part by part."""

    base: object          # Inputs: the workbook, the shared lists and the element recipes
    apart: object         # schemas.PartsTakenApart: the robots of the type, part by part
    pcb: dict             # car board category -> element -> (min, mode, max), mg per cm2 of board
    sensor_types: dict    # car sensor type -> element -> (min, mode, max), mg per unit
    tantalum: tuple       # kg of tantalum per kg of board: min, mode, max
    steels: dict          # the sibling's steels: grade -> ({element: (min, max)}, its remainder element)
    robots: list          # the robots of the register's sheet Type n drawn (schemas.RegisterRobot): taken apart, a mass
    left_out: list        # the robots of the sheet not drawn: no mass stated
    robot_type: int = 1   # the robot type of the workbook's Taxonomy
    later: list = None    # the robots of the sheet with a mass, not yet taken apart (its type then from the workbook)
    listed: int = 0       # the robots of the sheet Type n with a mass (one without is not in the evaluation, E10.1)
    files: dict = None    # robot type -> the parts file its robots' rows are read from (E11.7 point 4): one for types
                          # 1 and 2, several for types 3 and 4; each robot drawn with its own file's shared numbers
    outliers: list = None  # the robots of the sheet not drawn, outliers (composition.outliers; E30), counted nowhere


def read_parts_files(params: Params, base: Inputs) -> dict:
    """Every robot type's parts file that is on disk, read with 01's reader: robot type -> its file (E11.7 point 4: a
    type is drawn over its robots of every file). Raises schemas.WorkbookError when a file cannot be read."""
    return {c.number: schemas.read_parts_taken_apart(schemas.parts_path(params, c)) for c in base.book.categories
            if os.path.exists(schemas.parts_path(params, c))}


def read_apart_inputs(params: Params, base: Inputs, register: list, category, files: dict | None = None
                      ) -> ApartInputs:
    """The robots of the robot type of `category` part by part and the sibling projects' files, read with 01's
    functions, beside 02's inputs (`base`) and the robots of the register's sheet of that type (`register`); those
    taken apart with a stated mass are drawn. `files` are the parts files read (robot type -> file; only the type's own
    where not given): the type's robots are taken from every one that holds one (01's type_parts, E11.7 point 4), each
    with its own rows. An outlier of composition.outliers (01's outlier_robots) is not drawn and not counted: its rows
    left out of what is drawn (01's without_robots), kept in its file (Matthias, 2026-11-04, "Ok it is neo. It should be
    out. Mark it as outlier."; EVIDENCE.md E30 point 1). Raises schemas.WorkbookError when a file cannot be read."""
    if files is None:
        files = {category.number: schemas.read_parts_taken_apart(schemas.parts_path(params, category))}
    apart = schemas.type_parts(files, register, category.number)
    if apart is None:
        raise schemas.WorkbookError(f'{schemas.parts_path(params, category)}: no parts file holds a robot of type '
                                    f'{category.number}.')
    of_type = [r for r in register if category.number in r.types]
    outliers = schemas.outlier_robots(of_type, params)
    apart = schemas.without_robots(apart, schemas.outlier_names(outliers, params))
    used = {t: f for t, f in files.items() if f is apart or set(f.robots) & set(apart.robots)}
    triple = lambda row, keys: tuple(schemas.number(row.get(k)) for k in keys)  # noqa: E731
    pcb: dict = {}
    for row in schemas.sibling_rows(params.data.vehicle_pcb_composition, schemas.SIBLING_SHEETS[
            'vehicle_pcb_composition']):
        pcb.setdefault(schemas.text(row.get('PCBCategory')), {})[schemas.text(row.get('Element'))] = triple(
            row, ('mg_cm2_min', 'mg_cm2_mode', 'mg_cm2_max'))
    sensor_types: dict = {}
    for row in schemas.sibling_rows(params.data.vehicle_sensor_composition, schemas.SIBLING_SHEETS[
            'vehicle_sensor_composition']):
        elements = {}
        for heading in row:
            # Each element has three columns, e.g. Au_min_mg, Au_mode_mg, Au_max_mg; Overall_Weight is the unit's mass.
            if heading.endswith('_min_mg') and not heading.startswith('Overall'):
                element = heading[:-len('_min_mg')]
                values = triple(row, (f'{element}_min_mg', f'{element}_mode_mg', f'{element}_max_mg'))
                if None not in values and values[2] > 0:
                    elements[element] = values
        sensor_types[schemas.text(row.get('SensorType'))] = elements
    tantalum_rows = [r for r in schemas.sibling_rows(params.data.data_center_element_composition,
                                                      schemas.SIBLING_SHEETS['data_center_element_composition'])
                     if schemas.text(r.get('Element')) == 'Ta']
    tantalum = triple(tantalum_rows[0], ('Min', 'Mode', 'Max')) if tantalum_rows else (None, None, None)
    steels = schemas.sibling_steels(params.data.traction_motor_steels)
    counted = [r for r in of_type if r not in outliers]
    taken = [r for r in counted if r.taken_apart and all(v in apart.robots for v in schemas.versions(r.taken_apart))]
    drawn = [r for r in taken if None not in r.mass]
    return ApartInputs(base, apart, pcb, sensor_types, tantalum, steels, drawn,
                       [r for r in counted if None in r.mass], category.number,
                       [r for r in counted if r not in taken and None not in r.mass],
                       sum(None not in r.mass for r in counted), used, outliers)


def file_inputs(inputs: ApartInputs, robot_type: int, file) -> ApartInputs:
    """One parts file as inputs of its own robot type (for its checks, and for its shared numbers in a type drawn over
    several files): `inputs` with that file and type."""
    return replace(inputs, apart=file, robot_type=robot_type, files={robot_type: file})


def weighed_boards(apart) -> list:
    """The small joint's driver boards whose area the parts file gives (the G1's, weighed, and the G1+'s, the G1's
    own): the area every joint's driver board is scaled from."""
    return [b for b in apart.boards if b.kind in IN_THE_JOINTS and 'small' in b.name and None not in b.bounds]


def driver_area(apart) -> tuple | None:
    """The small joint's driver board's area, cm2 (min, mode, max): its weighed row of the sheet Boards where the
    file holds the G1 (type 1's), else the shared number schemas.DRIVER_AREA (a file without the G1, type 2's); None
    where neither is given."""
    weighed = weighed_boards(apart)
    if weighed:
        return weighed[0].bounds
    given = apart.constants.get(schemas.ALL_ROBOTS, {}).get(schemas.DRIVER_AREA)
    return given[1] if given else None


def check_parts(inputs: ApartInputs) -> list:
    """The checks 02 adds to 01's for a robot type taken apart: the small joint's driver board's area given, and the
    same wherever given; every joint, part, board and sensor goes to a kind of part; every part computed in a way 02
    knows; every robot of the file's type; the driver board a component of JointParts; the recipes it uses there; the
    tantalum row read."""
    apart, faults, robot_type = inputs.apart, [], inputs.robot_type
    on = apart.source + ': '
    weighed = weighed_boards(apart)
    if (not weighed and driver_area(apart) is None) or any(b.bounds != weighed[0].bounds for b in weighed):
        given = ', '.join(f'{b.robot} {b.bounds}' for b in weighed) or 'none'
        faults.append(Fault(on + 'Boards', 0, "the small joint's driver board needs its area, the same wherever it is "
                                              f"given (or '{schemas.DRIVER_AREA}' for all): {given}."))
    for robot in apart.robots.values():
        if robot.type != robot_type:
            faults.append(Fault(on + 'Robots', robot.row, f'{robot.name} is of type {robot.type}; the robots of the '
                                                          f'parts file are of type {robot_type} only.'))
    for j in apart.joints:
        if j.name.split()[0].lower() not in JOINT_KIND:
            faults.append(Fault(on + 'Joints', j.row, f"{j.robot}, {j.name}: no kind of the figures for a joint named "
                                                      f"so (it must start with {', '.join(JOINT_KIND)})."))
    for p in apart.parts + apart.boards + apart.sensors:
        if p.kind not in KIND_OF and p.kind not in IN_THE_JOINTS:
            faults.append(Fault(on + p.sheet, p.row, f"{p.robot}, {p.name}: the kind '{p.kind}' is not one of the "
                                                     'figures.'))
    for p in apart.parts:
        if p.computed and not p.computed.startswith(COMPUTED):
            faults.append(Fault(on + 'Parts', p.row, f"{p.robot}, {p.name}: 02 does not know how to compute "
                                                     f"'{p.computed}'."))
    for needed in (DRIVER_BOARD, *STRUCTURE):
        if needed not in {c.name for c in apart.joint_parts}:
            faults.append(Fault(on + 'JointParts', 0, f"no component '{needed}'."))
    rows = {(r.robot, r.family, r.shared): r.recipe for r in inputs.base.recipes.rows or []}
    if robot_type not in RECIPE_FAMILY:
        faults.append(Fault('element_recipes.xlsx: Rows', 0, f"02 names no recipes of type {robot_type}'s aluminium "
                                                             'and plastics (RECIPE_FAMILY).'))
    for shared, family in RECIPE_FAMILY.get(robot_type, {}).items():
        if recipe_key(robot_type, shared, family) not in rows:
            faults.append(Fault('element_recipes.xlsx: Rows', 0, f"no recipe for type {robot_type}'s {shared} "
                                                                 f"('{family}')."))
    if None in inputs.tantalum:
        faults.append(Fault('data.data_center_element_composition', 0, 'no Ta row with min, mode and max.'))
    # Every sensor of car sensor elements a kind (sensor_kind, E38 point 1): a new combination stops 02 here, loudly,
    # until its kind is named, rather than falling into a kind it is not.
    for p in apart.sensors:
        units = [(t, u) for _, sensor, t, u in apart.elements if sensor == p.name]
        if units and sensor_kind(units) is None:
            faults.append(Fault(on + 'Sensors', p.row, f"{p.robot}, {p.name}: its car sensor elements "
                                                       f"({', '.join(sorted({t for t, _ in units}))}) are no kind of "
                                                       'sensor 02 names (SENSOR_KINDS).'))
        elif (units and p.kind not in IN_THE_JOINTS and sensor_kind(units) not in IN_EVERY_JOINT
              and p.region not in REGION_WORDS):
            faults.append(Fault(on + 'Sensors', p.row, f"{p.robot}, {p.name}: its region '{p.region}' is none 02 "
                                                       f"names ({', '.join(REGION_WORDS)}; E38 point 7)."))
    return faults


def apart_faults(inputs: ApartInputs, params: Params) -> list:
    """The faults of a robot type part by part: 01's checks of its parts file (18 and 19), of the sibling files, of
    the grades, and check_parts. (02's own and the register's are in all_faults.)"""
    base, apart = inputs.base, inputs.apart
    return (schemas.check_parts_taken_apart(apart, base.lists, params) + schemas.check_sibling_data(apart, params)
            + schemas.check_grades(apart, base.recipes, params) + check_parts(inputs))


def grade_classes(inputs: ApartInputs) -> list:
    """The NdFeB grade classes a heat group can draw (sheet MagnetGrades) or a part of magnets names (sheet Parts,
    since 2026-10-29, point 4), in the order of the heat they stand."""
    drawn = {g.klass for g in inputs.apart.grades if (g.probability or 0) > 0} | schemas.stated_magnet_classes(
        inputs.apart)
    return [k for k in schemas.MAGNET_CLASSES if k in drawn]


group_classes = schemas.group_classes   # a heat group's grade classes and their probabilities (01's)


def magnet_fractions(params: Params, classes: list, n: int) -> dict:
    """The magnets' element fractions of each grade class in n draws, from RAWCLICVehicleTractionMotor's own
    `magnet_element_draws`, run in its own environment where it lies (answer C): class -> (element names, n × names).
    The fractions add up to 1 in every draw, iron their remainder (its docstring: "iron takes 1 minus their sum"); its
    seed is its own. Writes into a temporary folder only."""
    folder = params.data.traction_motor_dir
    python = os.path.join(folder, '.venv', 'bin', 'python')
    with tempfile.TemporaryDirectory() as out:
        done = subprocess.run([python, '-I', '-c', MAGNET_SCRIPT, out, str(n), *classes], cwd=folder,
                              capture_output=True, text=True, timeout=1800)
        if done.returncode != 0:
            raise RuntimeError(f'RAWCLICVehicleTractionMotor could not draw the magnets:\n{done.stderr}')
        fractions = {}
        for klass in classes:
            with open(os.path.join(out, f'{klass}.txt'), encoding='utf-8') as file:
                names = file.read().split('\n')
            fractions[klass] = (names, np.load(os.path.join(out, f'{klass}.npy')))
    return fractions


# ------------------------------------------------------------------------------------------------------
# The draws
# ------------------------------------------------------------------------------------------------------

class DiskArrays:
    """Arrays of the N draws kept on the disk, memory-mapped, in a temporary folder of their own, removed with the
    draws that hold them: the system keeps in memory only what is in use and writes the rest to the disk, never to its
    swap, whatever the draws and the data (the rule of the GitHub folder's CLAUDE.md §4: "a large matrix lives on disk,
    memory-mapped"; Matthias, 2026-11-13: "so if it is not reliable the go for a safe solution"). The values are the
    arrays' own, the same as in memory."""

    def __init__(self):
        self.folder = tempfile.mkdtemp(prefix='humanoid_02_draws_')
        self.files = 0
        weakref.finalize(self, shutil.rmtree, self.folder, True)   # the folder removed when the draws are let go

    def matrix(self, values: np.ndarray) -> np.ndarray:
        """`values` written to a file of the folder and read back memory-mapped."""
        path = os.path.join(self.folder, f'{self.files}.npy')
        self.files += 1
        kept = np.lib.format.open_memmap(path, mode='w+', dtype=values.dtype, shape=values.shape)
        kept[...] = values
        return kept

    def table(self, arrays: dict) -> dict:
        """Every array of `arrays` (key -> the N draws) a row of one file, memory-mapped: key -> its row."""
        if not arrays:
            return arrays
        keys = list(arrays)
        kept = self.matrix(np.stack([arrays[k] for k in keys]))
        return {k: kept[j] for j, k in enumerate(keys)}


# The draws written at a time into parts.npy (PartBlocks.save): 5,000 draws × every robot's columns in float32, some
# 50 MB for robot type 3.
SAVE_ROWS = 5000


@dataclass
class PartBlocks:
    """The kg of all units of each row of each robot (its columns '<robot>: <part>'), kept robot by robot: a draw is one
    robot, so a robot's columns are 0 in every other robot's draws, and only its own draws are held. `blocks`: for each
    robot, (its draws, the place of its first column in `columns`, its kg: its draws × its columns). Its memory grows
    with the draws and the rows of one robot, never with the number of robots. Until 2026-11-13 a matrix of every draw ×
    every robot's columns: 7.4 GB for robot type 3 at 200,000 draws, all six types 43 GB on a 16 GB computer (Matthias:
    "This is very very bad designe!!!", "Fix it damit and this never ever happens again", "It must adopte, so if data
    are added, it still works!!!")."""

    n: int
    columns: list
    blocks: list

    def column(self, name: str) -> np.ndarray:
        """One column over the N draws, 0 where another robot is drawn."""
        k = self.columns.index(name)
        values = np.zeros(self.n)
        for rows, first, kg in self.blocks:
            if first <= k < first + kg.shape[1]:
                values[rows] = kg[:, k - first]
        return values

    def robot_column(self, name: str) -> np.ndarray:
        """One column over the draws of its own robot only, in the order of those draws."""
        k = self.columns.index(name)
        return next(kg[:, k - first] for rows, first, kg in self.blocks if first <= k < first + kg.shape[1])

    def dense(self) -> np.ndarray:
        """Every column over every draw, the matrix parts.npy holds: for the tests at few draws, never at a run's size
        (N × every robot's columns)."""
        out = np.zeros((self.n, len(self.columns)))
        for rows, first, kg in self.blocks:
            out[rows, first:first + kg.shape[1]] = kg
        return out

    def save(self, path: str) -> None:
        """parts.npy exactly as np.save writes the matrix in float32 (its header, its bytes), written block after block
        of SAVE_ROWS draws, each block filled from the robots' draws in it, so that at most one block is in memory
        whatever the draws and the robots (a matrix of 3.7 GB for robot type 3 at 200,000 draws)."""
        header = {'descr': np.lib.format.dtype_to_descr(np.dtype(np.float32)), 'fortran_order': False,
                  'shape': (self.n, len(self.columns))}
        with open(path, 'wb') as file:
            np.lib.format.write_array_header_1_0(file, header)
            for start in range(0, self.n, SAVE_ROWS):
                stop = min(start + SAVE_ROWS, self.n)
                block = np.zeros((stop - start, len(self.columns)), dtype=np.float32)
                for rows, first, kg in self.blocks:          # a robot's draws in order: those in this block
                    a, b = np.searchsorted(rows, start), np.searchsorted(rows, stop)
                    block[rows[a:b] - start, first:first + kg.shape[1]] = kg[a:b]
                file.write(block.tobytes())


@dataclass
class Draws:
    """A robot type taken apart, drawn N times, each draw one of its robots."""

    n: int
    robots: list          # the robots of the parts file, in the order of its sheet Robots (a version each)
    robot: np.ndarray     # the robot of the parts file each draw is, as its place in `robots`
    mass: np.ndarray      # kg: that robot's mass in each draw
    part_blocks: PartBlocks   # kg of all units of each row of each robot, robot by robot (PartBlocks)
    remainders: list      # the columns of the parts that are remainders (frames, battery housings)
    # '<robot>: <joint> structure' -> (its robot's draws, kg of one joint's structure in them), a remainder; 0 in every
    # other robot's draws, which are not held (as PartBlocks)
    structure_blocks: dict
    materials: tuple      # (columns (kind, material), N × columns): kg
    elements: dict        # (kind, element of interest) -> kg in each draw (E19 point 3)
    estimated: dict       # (kind, element) -> the part of those kg resting on masses labelled E (TRACKED elements)
    hot: dict             # kind of joint -> True where its magnets are for 150 °C or more in most draws
    heat: np.ndarray      # the draw of heat, 0 to 1, that decides every heat group's grade class (tied)
    grades: dict          # heat group -> the grade class drawn in each draw
    followed: dict        # material -> kg of its elements of interest in each draw (02's "in the elements")
    details: dict = None  # (kind, material, grade, alloy or magnet class; '' for none) -> kg in each draw
    recipe_elements: dict = None   # (kind, element) -> kg of every element by the recipes, fractions and sibling files
    in_recipes: dict = None        # material -> kg of it whose elements are drawn, in each draw (where its mass is booked)
    by_material: dict = None       # (material, element of interest) -> kg in each draw: where each comes from (E19)
    holds: dict = None             # (material, grade, alloy or magnet class) -> what it holds by its recipe, in words
    fixed: dict = None             # (material, element) -> kg of the element fixed in that alloy, each draw (E25)
    register: list = None          # the register's robots drawn, '<number> <name>', in their order
    register_robot: np.ndarray = None   # the robot of the register of each draw, as its place in `register`
    on_estimates: dict = None      # what rests on estimates (E) -> the robots it does, for the notes page
    robot_type: int = 1            # the robot type drawn
    listed: int = 0                # the robots of its sheet Type n with a mass (drawn, or not yet taken apart)
    aluminium: str = ''            # its aluminium recipe in words, for the notes page
    templates: str = ''            # how many of its robots rest on templates, in 01's words (E13 rules 2 and 4)
    # (place, element of interest) -> kg in each draw, and the kg resting on masses labelled E: a place a kind of part,
    # or the component of the electronics (E32) whatever kind it sits in (Matthias, 2026-11-05: "parts_taken element
    # indum is head. it is sensors. Cameras.", "Yes, fix all three"): the pages of where the critical elements sit.
    places: dict = None
    places_estimated: dict = None
    # (kind, part of how a robot is taken apart, element of interest) -> kg in each draw (01's TAKEN_APART; Matthias,
    # 2026-11-08, "Yes do it"): the elements of each kind split by part, adding up to `elements` (check_taken).
    taken: dict = None
    taken_kg: dict = None   # (kind, part of how a robot is taken apart) -> kg of all its materials, in each draw
    # kind -> (draws of its boards with copper above what all their layers can hold, draws of its boards): E51 row 8
    layer_check: dict = None
    elements_of: dict = None       # material -> kg of the elements booked under it, in each draw (check_recipes)
    disk: object = None            # its DiskArrays: the folder of its draws on the disk, removed with the record

    @property
    def parts(self) -> tuple:
        """(columns, N × columns): every robot's parts over every draw, built from part_blocks: for the tests at few
        draws, never at a run's size (PartBlocks.dense)."""
        return self.part_blocks.columns, self.part_blocks.dense()

    @property
    def structures(self) -> dict:
        """'<robot>: <joint> structure' -> kg over every draw, 0 in another robot's: for the tests at few draws."""
        out = {}
        for column, (rows, kg) in self.structure_blocks.items():
            out[column] = np.zeros(self.n)
            out[column][rows] = kg
        return out


class Shared:
    """What is drawn once in each of the N draws and shared by every robot: the joint's components, the shares, the
    constants for all robots, the recipes and grades, the alternatives, the sibling projects' metals and elements, the
    cells' energy per kg."""

    def __init__(self, inputs: ApartInputs, params: Params, magnets: dict, rng: np.random.Generator, n: int):
        apart = inputs.apart
        self.rng, self.n = rng, n
        self.rows, self.size = None, n   # the draws kept (keep): None for all N; `size` their number
        self.magnets = {k: (names, drawn) for k, (names, drawn) in magnets.items()}
        # The joint's components, kg, for each size: the small one's grams times its spread, the large one's grams
        # times its factor; and the joint at its modes, which a module mass given is measured against.
        self.joint: dict = {'small': {}, 'large': {}}
        self.at_mode = {'small': 0.0, 'large': 0.0}
        for c in apart.joint_parts:
            self.joint['small'][c.name] = c.grams / 1000 * triangle(rng, *c.spread, n)
            self.joint['large'][c.name] = c.grams / 1000 * triangle(rng, *c.factor, n)
            self.at_mode['small'] += c.grams / 1000 * c.spread[1]
            self.at_mode['large'] += c.grams / 1000 * c.factor[1]
        self.material = {c.name: c.material for c in apart.joint_parts}
        self.grade = {c.name: c.grade for c in apart.joint_parts}
        # The structure's components' shares of the structure, for each size: the G1's grams at their modes.
        structure = [c for c in apart.joint_parts if c.name in STRUCTURE]
        self.structure_share = {}
        for size, multiplier in (('small', lambda c: c.spread[1]), ('large', lambda c: c.factor[1])):
            total = sum(c.grams * multiplier(c) for c in structure)
            self.structure_share[size] = {c.name: c.grams * multiplier(c) / total for c in structure}
        # The shares of every component or part that has them: name -> [((material, grade), share in each draw)].
        groups: dict = {}
        for s in apart.shares:
            groups.setdefault(s.item, []).append(((s.material, s.grade), s.share, s.remainder))
        self.shares = {item: shares_drawn(rng, group, n) for item, group in groups.items()}
        # The constants for all robots.
        self.constant = {q: triangle(rng, *values, n) for q, (_, values, _, _, _) in
                         apart.constants.get(schemas.ALL_ROBOTS, {}).items()
                         if q not in (CAPACITORS, schemas.LARGE_CAPACITORS, schemas.BOARD_CAPACITORS)}
        # The board metals per cm2 by car board category, the tantalum per kg of board, the sensor elements per unit.
        self.pcb = {(category, element): triangle(rng, *inputs.pcb[category][element], n)
                    for category in sorted({b.category for b in apart.boards})
                    for element in schemas.BOARD_METALS}
        self.tantalum = triangle(rng, *inputs.tantalum, n)
        self.sensor = {(car_type, element): triangle(rng, *values, n)
                       for car_type in sorted({e[2] for e in apart.elements})
                       for element, values in inputs.sensor_types[car_type].items()}
        # The recipes: the type's aluminium and plastics; the NMC cells with their energy per kg drawn; the grades (a
        # recipe of the element recipes, or a steel of the sibling's workbook), each drawn once and used wherever it
        # sits.
        settings = params.composition
        self.wh_per_kg = triangle(rng, settings.nmc_wh_per_kg_min, settings.nmc_wh_per_kg_mode,
                                  settings.nmc_wh_per_kg_max, n)
        self.recipes = RecipeDraws(inputs.base.recipes, rng, n)
        rows = {(r.robot, r.family, r.shared): r.recipe for r in inputs.base.recipes.rows or []}
        self.recipe_name = {shared: rows[recipe_key(inputs.robot_type, shared, family)]
                            for shared, family in RECIPE_FAMILY[inputs.robot_type].items()}
        # The material Copper by its recipe (copper metal, Cu: "copper is copper"); each recipe's elements.
        self.recipe_name[COPPER] = COPPER_RECIPE
        self.recipe = {shared: self.recipes.elements(name) for shared, name in self.recipe_name.items()}
        self.cells, self.cells_metal = self.recipes.drawn(CELL_RECIPE, self.wh_per_kg / settings.nmc_wh_per_kg_mode)
        self.cell_sheet, self.nmc_mode, self.other_cells = inputs.base.recipes.cells, settings.nmc_wh_per_kg_mode, {}
        self.steels, self.compounds = inputs.steels, inputs.base.recipes.compounds
        self.graded: dict = {}   # grade -> element -> share in each draw
        self.split: dict = {}    # grade or recipe -> the recipes it is made of -> share in each draw
        self.states: dict = {}   # 'A or B' -> the one drawn in each draw, as its place
        # The magnets by heat (sheet MagnetGrades): one draw of heat, from 0 to 1, decides how hot the robot is built
        # for; each heat group takes the grade class at that point of its cumulative probabilities (the classes tied
        # within a draw, so that the hot cases do not average out), and its magnets the element fractions of that class
        # in that draw (a discrete state, never blended).
        self.heat = rng.random(n)
        self.heat_grade, self.magnet = {}, {}
        for group in dict.fromkeys(g.group for g in apart.grades):
            classes = group_classes(apart, group)
            at = np.minimum(np.searchsorted(np.cumsum([p for _, p in classes]), self.heat, side='right'),
                            len(classes) - 1)
            self.heat_grade[group] = np.array([k for k, _ in classes])[at]
            names = magnets[classes[0][0]][0]
            fractions = np.zeros((n, len(names)))
            for k, (klass, _) in enumerate(classes):
                if magnets[klass][0] != names:
                    raise ValueError(f'the magnets of {klass} name other elements than those of {classes[0][0]}.')
                fractions[at == k] = magnets[klass][1][at == k]
            self.magnet[group] = (names, fractions)
        # The driver board of each joint size: its area (cm2), the small joint's from the weighed row of the sheet
        # Boards, the large joint's the small one's times the same factor as its mass.
        board = next(c for c in apart.joint_parts if c.name == DRIVER_BOARD)
        self.board_area = {'small': triangle(rng, *driver_area(apart), n)}
        self.board_area['large'] = self.board_area['small'] * self.joint['large'][DRIVER_BOARD] / (board.grams / 1000)
        # The ceramic capacitors of a joint's driver board (E38 point 4): a whole number of them in the G1's small
        # joint's board, each of the barium titanate drawn, over that board's weighed mass; every driver board, of any
        # joint and robot, the same share of its mass in that draw.
        capacitors = apart.constants[schemas.ALL_ROBOTS][CAPACITORS][1]
        self.titanate_share = (whole_numbers(rng, *capacitors, n) * self.constant[CAPACITOR_TITANATE] / 1e6
                               / (board.grams / 1000))
        # The large capacitors (Matthias, 2026-11-08, "Yes, enter 1 to 8"; EVIDENCE.md E51): their number on a joint's
        # driver board, a whole number the same on every joint of the robot (one design of driver a robot), and on a
        # capacitor board, each a whole number in every draw; their kind, liquid electrolytic or hybrid polymer, one or
        # the other in each draw, each as often (a discrete state, never blended). Drawn last, so that every draw
        # before them stays as it was.
        shared = apart.constants[schemas.ALL_ROBOTS]
        self.large_capacitors = whole_numbers(rng, *shared[schemas.LARGE_CAPACITORS][1], n)
        self.board_capacitors = whole_numbers(rng, *shared[schemas.BOARD_CAPACITORS][1], n)
        self.capacitor_kind = self.state(schemas.CAPACITOR_KINDS)

    def kept(self, values: np.ndarray) -> np.ndarray:
        """A draw over all N draws, as drawn (the same random numbers), kept over the draws this set keeps (`rows`,
        Shared.keep): all of them where it keeps all."""
        return values if self.rows is None else values[self.rows]

    def keep(self, rows: np.ndarray) -> 'Shared':
        """This set kept over the draws `rows` only (those of the robots of its file, draw_taken_apart): every draw it
        holds cut to them (keep_rows), and what it draws later kept so (kept). Returns itself."""
        keep_rows(self, rows, self.n)
        self.rows, self.size = rows, rows.size
        self.recipes.rows, self.recipes.size = rows, rows.size
        return self

    def cell_draws(self, recipe: str) -> tuple:
        """The cells of `recipe` in every draw: their energy per kg (Wh/kg), their element shares and those of them as
        metal (their foils and tabs, whose copper and aluminium are elements of interest, E19 point 3). NMC as
        before (00's triangle, E1.7d); another recipe (LFP, the CASBOT W1's, E9.7 point 5) one of its cells of the sheet
        Cells in each draw, each as often (as a battery built from counted cells), its energy per kg its own, its items
        that follow the energy by it over the NMC mode. Drawn once, when first asked: a type without such cells draws
        as before."""
        if recipe == CELL_RECIPE:
            return self.wh_per_kg, self.cells, self.cells_metal
        if recipe not in self.other_cells:
            cells = [c for c in self.cell_sheet.values() if c.recipe == recipe]
            if not cells:
                raise ValueError(f"no cell of the sheet Cells follows the recipe '{recipe}'.")
            chosen = self.kept(self.rng.integers(len(cells), size=self.n))
            wh_per_kg = np.array([c.energy_wh / c.grams * 1000 for c in cells])[chosen]
            self.other_cells[recipe] = (wh_per_kg, *self.recipes.drawn(recipe, wh_per_kg / self.nmc_mode))
        return self.other_cells[recipe]

    def state(self, written: str) -> np.ndarray:
        """Which of 'A or B' each draw is, as its place: each as often, drawn once for the written cell and used
        wherever it is written (a discrete state, never blended: the electrical steel of the stator and the rotor is
        one grade in a draw)."""
        if written not in self.states:
            self.states[written] = self.kept(self.rng.integers(len(schemas.alternatives(written)), size=self.n))
        return self.states[written]

    def grade_leaves(self, grade: str) -> dict:
        """What a grade or a recipe is made of, for the material pages: the recipes it holds and their share in every
        draw (RecipeDraws.leaves); a steel of the sibling's workbook is itself."""
        if grade not in self.split:
            self.split[grade] = {grade: np.ones(self.size)} if grade in self.steels else self.recipes.leaves(grade)
        return self.split[grade]

    def grade_elements(self, grade: str) -> dict:
        """The element shares of one grade in every draw: a recipe of the element recipes, or a steel of the sibling's
        workbook, each element a triangle on its minimum, its mode (the middle of its range, or the typical value of
        SIBLING_MODES) and its maximum, its remainder 1 minus the others."""
        if grade not in self.graded:
            if grade not in self.steels:
                self.graded[grade] = self.recipes.elements(grade)
            else:
                elements, remainder = self.steels[grade]
                typical = (schemas.composition(self.compounds[SIBLING_MODES[grade]][0]) if grade in SIBLING_MODES
                           else {})
                out = {e: self.kept(triangle(self.rng, low, typical.get(e, (low + high) / 2), high, self.n))
                       for e, (low, high) in elements.items() if high > 0}
                out[remainder] = 1 - sum(out.values())
                self.graded[grade] = out
        return self.graded[grade]


class Robot:
    """One robot's draws (its rows of the N draws), added up as they are drawn."""

    def __init__(self, name: str, rows: np.ndarray, shared: Shared, mass: np.ndarray):
        self.name, self.rows, self.shared, self.mass = name, rows, shared, mass
        self.n = rows.size
        # Its draws within its shared draws: the same rows where these hold every draw; their places among the draws
        # kept where they hold only the draws of the robots of one file (keep_rows; a type over several files).
        kept = getattr(shared, 'rows', None)
        self.local = rows if kept is None else np.searchsorted(kept, rows)
        self.parts: dict = {}       # part column -> kg
        self.materials: dict = {}   # (kind, material) -> kg
        self.elements: dict = {}    # (kind, element of interest) -> kg (E19 point 3)
        self.recipe_elements: dict = {}   # (kind, element) -> kg, every element by the recipes and fractions
        self.estimated: dict = {}   # (kind, element of interest) -> kg resting on masses labelled E
        self.places: dict = {}      # (place: a kind of part, or the electronics' component, element) -> kg (PLACES)
        self.places_estimated: dict = {}   # the same, the kg resting on masses labelled E
        # (kind, part of how a robot is taken apart, element of interest) -> kg (01's TAKEN_APART; Matthias,
        # 2026-11-08, "I want a detailed list of the component ... to know how to take it apart!!!", "Yes do it")
        self.taken: dict = {}
        self.taken_kg: dict = {}    # (kind, part of how a robot is taken apart) -> kg of all its materials
        # kind -> (the draws of its boards whose copper is above what all their layers can hold, the draws of its
        # boards): the check of a board's copper against its layers (E51 row 8), reported, not cut.
        self.layer_check: dict = {}
        self.structures: dict = {}  # '<robot>: <joint> structure' -> kg of one joint's structure
        self.followed: dict = {}    # material -> kg of its elements of interest
        self.by_material: dict = {}   # (material, element of interest) -> kg
        self.fixed: dict = {}       # (material, element) -> kg of the element fixed in that alloy (E25)
        # Each material's kilograms whose elements are drawn, counted where its mass is booked (a recipe or grade, the
        # magnets, the cells; a board less what sits on it; a sensor's elements; the capacitors; the titanate), and the
        # kilograms of the elements booked under it, counted where each element is booked: two counts that must agree
        # (check_recipes; Matthias, 2026-11-08, "Yes, fix it": until then one count, of the elements, compared with
        # itself).
        self.in_recipes: dict = {}  # material -> kg of it whose elements are drawn
        self.elements_of: dict = {}  # material -> kg of the elements booked under it (recipe_elements)
        self.details: dict = {}     # (kind, material, grade, alloy or magnet class; '' for none) -> kg

    def of(self, values: np.ndarray) -> np.ndarray:
        """This robot's rows of draws shared by all robots."""
        return values[self.local]

    def drawn(self, material: str, kg) -> None:
        """`kg` of `material` whose elements are drawn, wherever they are booked (check_recipes)."""
        self.in_recipes[material] = self.in_recipes.get(material, 0) + kg

    def element(self, kind: str, element: str, kg: np.ndarray, estimate: bool, material: str,
                of_interest: bool = False, component: str = '', place: str = '', taken: str = '') -> None:
        """kg of one element in a kind of part, held by `material`, by its recipe, fractions or sibling file
        (recipe_elements, which add up to the material); where `of_interest`, also an element of interest it is
        recovered as (declare()). A `component` of the electronics (E32) books it in the electronics, whatever it is
        made of; the copper of a connector's brass stays fixed in the alloy (FIXED_IN_ALLOYS by what it is made of). A
        `place` (a sensor's kind, E38) is where the pages of where the critical elements sit show it; `taken` its part
        of how a robot is taken apart (declare())."""
        self.recipe_elements[(kind, element)] = self.recipe_elements.get((kind, element), 0) + kg
        booked = ELECTRONICS if component else material
        self.elements_of[booked] = self.elements_of.get(booked, 0) + kg
        if material in FIXED_IN_ALLOYS.get(element, ()):
            self.fixed[(material, element)] = self.fixed.get((material, element), 0) + kg
        if of_interest:
            self.declare(kind, element, kg, estimate, material, component, place, taken)

    def declare(self, kind: str, element: str, kg: np.ndarray, estimate: bool, material: str,
                component: str = '', place: str = '', taken: str = '') -> None:
        """kg of one element of interest in a kind of part, recovered from `material` (E19 point 3; 02's "in the
        elements" of that material), or from the `component` of the electronics it sits in (E32: '<electronics>:
        <component>', the electronics' own "in the elements"); and in its part of how a robot is taken apart: `taken`,
        or that of its component of the electronics (01's taken_part). Raises ValueError where it has neither, so that
        no element is booked to no part."""
        part = taken or (schemas.taken_part(kind, component=component) if component else '')
        if not part:
            raise ValueError(f'{element} in {KINDS[kind][0]} ({material}): booked to no part of how a robot is taken '
                             'apart.')
        self.taken[(kind, part, element)] = self.taken.get((kind, part, element), 0) + kg
        self.elements[(kind, element)] = self.elements.get((kind, element), 0) + kg
        booked = ELECTRONICS if component else material
        self.followed[booked] = self.followed.get(booked, 0) + kg
        source = component_label(component) if component else material
        self.by_material[(source, element)] = self.by_material.get((source, element), 0) + kg
        # Its place: a sensor's kind (E38), else the electronics' component wherever it sits, every other part its
        # kind of part.
        place = place or (component_label(component) if component else kind)
        self.places[(place, element)] = self.places.get((place, element), 0) + kg
        if estimate and element in TRACKED:
            self.estimated[(kind, element)] = self.estimated.get((kind, element), 0) + kg
            self.places_estimated[(place, element)] = self.places_estimated.get((place, element), 0) + kg

    def declare_all(self, kind: str, material: str, shares: dict, metal: dict, kg: np.ndarray, estimate: bool,
                    component: str = '', taken: str = '') -> None:
        """The elements of interest of `kg` of `material` (declared(): its element whole, or those of its element
        shares and of its shares as metal), each shared by all robots or, for a whole element, 1; of a `component` of
        the electronics, recovered from it (E32); each in its part `taken` of how a robot is taken apart."""
        for element, share in declared(material, shares, metal).items():
            self.declare(kind, element, kg * (self.of(share) if np.ndim(share) else share), estimate, material,
                         component, taken=taken)

    def material(self, part: str, kind: str, material: str, kg: np.ndarray, estimate: bool, heat_group: str = '',
                 grade: str = '', component: str = '', item: str = '', taken: str = '') -> None:
        """kg of one material of a part in a kind, and the elements it holds: by its grade's recipe where it names one,
        else by the type's recipe, as copper, or as magnets of the grade class drawn for `heat_group`; and the elements
        of interest it is recovered as (declare_all(), E19 point 3: copper and nickel whole, the light alloys the
        metal of their recipe (E24); the battery cells' foils and tabs by their items 'As metal'). A material or
        grade written 'A or B' is either, drawn (Shared.state). A part of magnets outside the joints may name its grade
        class, a part of battery cells follows the cells' recipe as the main pack (2026-10-29, "Yes, build them", point
        4). The grade of a material written 'A or B' goes to the alternative it is a grade of only, the other following
        its type's recipe (a hydraulic manifold of titanium alloy, Ti-6Al-4V, or of aluminium alloys: EVIDENCE.md
        E27.7). Electronics are added by board() and sensor(). A `component` of the electronics (E32: the cables and
        connectors) books the kilograms in the electronics, its detail whole (one material on the material pages), its
        elements those of what it is made of (`material`, `grade`), recovered from the component. Its elements of
        interest go to its part of how a robot is taken apart: `taken` where the caller knows it (a sensor's housing, a
        driver board, a board), else by its kind, the name of its row (`item`), its material and its component (01's
        taken_part, which stops at a row it cannot place)."""
        for written, call in ((material, lambda m, k: self.material(part, kind, m, k, estimate, heat_group,
                                                                    grade if m in schemas.GRADED else '', component,
                                                                    item, taken)),
                              (grade, lambda g, k: self.material(part, kind, material, k, estimate, heat_group, g,
                                                                 component, item, taken))):
            if schemas.OR in written:
                drawn = self.of(self.shared.state(written))
                for place, one in enumerate(schemas.alternatives(written)):
                    call(one, kg * (drawn == place))
                return
        self.parts[part] = self.parts.get(part, 0) + kg
        booked = ELECTRONICS if component else material
        self.materials[(kind, booked)] = self.materials.get((kind, booked), 0) + kg
        taken = taken or schemas.taken_part(kind, item, material, component)
        self.taken_kg[(kind, taken)] = self.taken_kg.get((kind, taken), 0) + kg
        if component:
            self.detail(kind, ELECTRONICS, kg, '', '')
        else:
            self.detail(kind, material, kg, heat_group, grade)
        metal = {}   # of the shares, those of the items 'As metal': the battery cells' foils and tabs
        if material == MAGNETS:
            names, drawn = self.shared.magnets[grade] if grade else self.shared.magnet[heat_group]
            shares = {element: drawn[:, k] for k, element in enumerate(names)}
        elif material == CELL_MATERIAL:
            shares, metal = self.shared.cells, self.shared.cells_metal
        elif grade:
            shares = self.shared.grade_elements(grade)
        elif material in self.shared.recipe:
            shares = self.shared.recipe[material]
        else:
            shares = {}
        if shares:   # its kilograms follow its recipe, grade, magnets' or cells' fractions: their elements drawn
            self.drawn(booked, kg)
        for element, share in shares.items():
            self.element(kind, element, kg * self.of(share), estimate, material, component=component, taken=taken)
        self.declare_all(kind, material, shares, metal, kg, estimate, component, taken)

    def detail(self, kind: str, material: str, kg: np.ndarray, heat_group: str, grade: str) -> None:
        """The kg of a material by what it is, for the material pages (Matthias, 2026-10-29: "how much Copper and
        especially permanent magnets. The different steels and aluminum alyoys"): the magnets by the grade class drawn
        for their joint's heat; a material with a grade by the recipes the grade holds (the gear stage 2's steel as
        20CrMnTi and GCr15); the type's aluminium by its alloys; every other material whole ('')."""
        s = self.shared
        if material == MAGNETS and grade:
            split = {grade: 1.0}
        elif material == MAGNETS:
            classes = self.of(s.heat_grade[heat_group])
            split = {klass: (classes == klass).astype(float) for klass in np.unique(classes)}
        elif material == CELL_MATERIAL:
            split = {CELL_RECIPE: 1.0}
        elif grade:
            split = {leaf: self.of(share) for leaf, share in s.grade_leaves(grade).items()}
        elif material in ALLOYS and material in s.recipe_name:
            split = {leaf: self.of(share) for leaf, share in s.grade_leaves(s.recipe_name[material]).items()}
        else:
            split = {'': 1.0}
        for what, share in split.items():
            key = (kind, material, what)
            self.details[key] = self.details.get(key, 0) + kg * share

    def piece(self, part: str, kind: str, item: str, material: str, kg: np.ndarray, estimate: bool,
              heat_group: str = '', grade: str = '', component: str = '') -> None:
        """A part or component of one material (and its grade), or of the shares of the sheet Shares; a `component`
        of the electronics booked there (E32: the connectors)."""
        if material:
            self.material(part, kind, material, kg, estimate, heat_group, grade, component, item)
        else:
            for (shared, its_grade), share in self.shared.shares[item]:
                self.material(part, kind, shared, kg * self.of(share), estimate, heat_group, its_grade, component,
                              item)

    def board(self, kind: str, category: str, kg: np.ndarray, area: np.ndarray, estimate: bool,
              inside: np.ndarray | float = 0.0) -> None:
        """The elements of boards of `kg` and `area` (cm2): copper their mass times the copper share, the metals of
        BOARD_METALS their area times the car category's mg per cm2, tantalum their mass times its share; their rest,
        less the elements `inside` them that are drawn as another's (a joint's encoders on its driver board), glass
        fibre and bromine each a share of it and epoxy the remainder, the glass and the epoxy by their recipes
        (2026-10-29, "Yes, enter them", point 3b; EVIDENCE.md E5.21). Its elements of interest (E19 point 3): its
        copper, tantalum and those of its metals of interest; not the laminate's glass, epoxy and bromine."""
        s, on = self.shared, CIRCUIT_BOARDS   # its elements of interest recovered from the circuit boards (E32)
        copper, tantalum = kg * self.of(s.constant[BOARD_COPPER]), kg * self.of(s.tantalum)
        metals = {metal: area * self.of(s.pcb[(category, metal)]) / 1e6 for metal in schemas.BOARD_METALS}
        self.element(kind, 'Cu', copper, estimate, ELECTRONICS, True, on)
        # The check of its copper against its layers (E51 row 8): its copper per cm2, a share of its mass (Bizzo),
        # against the most copper all the layers its group of boards has at most can hold (01's board_layers,
        # layers_copper_mg); counted, reported, not cut.
        held = np.asarray(area) > 0
        bound = schemas.layers_copper_mg(schemas.board_layers(kind)[2])
        above = int((np.asarray(copper)[held] / np.asarray(area)[held] * 1e6 > bound).sum())
        before = self.layer_check.get(kind, (0, 0))
        self.layer_check[kind] = (before[0] + above, before[1] + int(held.sum()))
        for metal, kg_metal in metals.items():
            self.element(kind, metal, kg_metal, estimate, ELECTRONICS, metal in INTEREST, on)
        self.element(kind, 'Ta', tantalum, estimate, ELECTRONICS, True, on)
        rest = kg - copper - tantalum - sum(metals.values()) - inside
        self.drawn(ELECTRONICS, kg - inside)   # its elements: all its mass but what sits on it, drawn as another's
        glass, bromine = rest * self.of(s.constant[BOARD_GLASS]), rest * self.of(s.constant[BOARD_BROMINE])
        self.element(kind, 'Br', bromine, estimate, ELECTRONICS, component=on)
        for recipe, kg_of in ((GLASS_RECIPE, glass), (EPOXY_RECIPE, rest - glass - bromine)):
            for element, share in s.grade_elements(recipe).items():
                self.element(kind, element, kg_of * self.of(share), estimate, ELECTRONICS, component=on)

    def sensor_kg(self, units: list, count: np.ndarray | float) -> np.ndarray:
        """kg of the car sensor elements of `count` sensors, each made of `units` (car sensor type, units in one
        sensor): what sensor() adds as their elements."""
        return sum((count * per_sensor * self.of(mg) / 1e6 for car_type, per_sensor in units
                    for (t, _), mg in self.shared.sensor.items() if t == car_type), np.zeros(self.n))

    def capacitors(self, part: str, kind: str, kg: np.ndarray, estimate: bool) -> None:
        """`kg` of large capacitors in a kind of part (EVIDENCE.md E51; Matthias, 2026-11-08: "There are also quite large
        capacitors close to each joint motor ... So have them correct!!", "Yes, enter 1 to 8"): booked in the electronics
        as their component the capacitors (the part Small PCB, the board they sit on), their elements by their kind in
        each draw, liquid electrolytic or hybrid polymer (Shared.capacitor_kind), its shares drawn (aluminium, iron,
        copper, tin; the liquid's seal kaolinite, the hybrid's chromium and glass fibre), the organic rest their
        remainder (CAPACITOR_ORGANICS), never normalised. Aluminium, copper and tin are elements of interest; the
        kaolinite's and the glass's aluminium are bound, not."""
        s, on = self.shared, CAPACITOR_PARTS
        taken = schemas.taken_part(kind, component=on)
        self.material(part, kind, ELECTRONICS, kg, estimate, component=on, taken=taken)
        self.drawn(ELECTRONICS, kg)            # every kilogram of them in their elements
        hybrid = self.of(s.capacitor_kind) == 1
        for name, rows in ((schemas.LIQUID_CAPACITOR, ~hybrid), (schemas.HYBRID_CAPACITOR, hybrid)):
            mass = kg * rows
            shares = {what: self.of(s.constant[schemas.capacitor_share(name, what)])
                      for what in schemas.CAPACITOR_SHARES[name]}
            for what, share in shares.items():
                if what in CAPACITOR_METALS:
                    symbol = CAPACITOR_METALS[what]
                    self.element(kind, symbol, mass * share, estimate, ELECTRONICS, symbol in INTEREST, on,
                                 taken=taken)
                elif what == 'kaolinite':
                    for element, f in KAOLINITE.items():
                        self.element(kind, element, mass * share * f, estimate, ELECTRONICS, component=on, taken=taken)
                elif what == 'glass fibre':
                    for element, f in s.grade_elements(GLASS_RECIPE).items():
                        self.element(kind, element, mass * share * self.of(f), estimate, ELECTRONICS, component=on,
                                     taken=taken)
            rest = mass * (1 - sum(shares.values()))
            for element, f in CAPACITOR_ORGANICS.items():
                self.element(kind, element, rest * f, estimate, ELECTRONICS, component=on, taken=taken)

    def sensor(self, kind: str, units: list, count: np.ndarray | float, estimate: bool, region: str = '') -> None:
        """The elements of `count` sensors, each made of `units` (car sensor type, units in one sensor); those of
        interest declared (E19 point 3), recovered from the cameras or the other sensors (sensor_component, E32), and
        placed by the sensor's kind on the pages of where the critical elements sit (sensor_kind, E38), with the body
        region of its row (`region`, REGION_WORDS) unless it sits in every joint (IN_EVERY_JOINT)."""
        on, kind_of_sensor = sensor_component(units), sensor_kind(units)
        place = sensor_place(kind_of_sensor, region) if kind_of_sensor else ''
        self.drawn(ELECTRONICS, self.sensor_kg(units, count))   # its elements, the car sensor elements' kilograms
        for car_type, per_sensor in units:
            for (t, element), mg in self.shared.sensor.items():
                if t == car_type:
                    self.element(kind, element, count * per_sensor * self.of(mg) / 1e6, estimate, ELECTRONICS,
                                 element in INTEREST, on, place, taken='Sensors')


def keep_rows(value, rows: np.ndarray, n: int):
    """`value` with every array whose first axis is the N draws cut to the draws `rows`, walking through its dicts and
    lists (changed in place), its tuples (made anew) and the objects of this file (Shared, RecipeDraws); everything else
    as it is. Used to keep of a file's shared draws only the draws of its robots (draw_taken_apart)."""
    if isinstance(value, np.ndarray):
        return value[rows] if value.ndim and value.shape[0] == n else value
    if isinstance(value, dict):
        for key in value:
            value[key] = keep_rows(value[key], rows, n)
        return value
    if isinstance(value, list):
        value[:] = [keep_rows(v, rows, n) for v in value]
        return value
    if isinstance(value, tuple):
        items = [keep_rows(v, rows, n) for v in value]
        return type(value)(*items) if hasattr(value, '_fields') else tuple(items)
    if type(value).__module__ == __name__ and hasattr(value, '__dict__'):
        for key, v in vars(value).items():
            setattr(value, key, keep_rows(v, rows, n))
        return value
    return value


def draw_taken_apart(inputs: ApartInputs, params: Params, magnets: dict, say=None) -> Draws:
    """A robot type over its robots of the register taken apart, drawn `composition.draws` times (HOW IT DRAWS A
    ROBOT TYPE TAKEN APART in the docstring at the top): each draw one of the register's robots of the type taken
    apart, all equally often (Matthias, 2026-10-28: "Do it for all the robots which are in type 1"); a robot in several
    versions (the Booster K1, the GR-1) one of them, each as often (2026-10-29, decision B); its mass a triangle on its
    own mass in the parts file, its parts its own rows, part by part (decision C: nothing scaled from another robot).
    Its random numbers its own, from the seed and its type (type 1's as they were before type 2 came). `say`, where
    given, is told every tenth robot drawn (its number, the robots of the parts file, its name: "Yes, build them",
    2026-10-30, point 4); it changes no draw."""
    apart, n = inputs.apart, params.composition.draws
    rng = np.random.default_rng([params.composition.seed, inputs.robot_type])
    names = list(apart.robots)                                    # the robots of the parts file, a version each
    robots = inputs.robots
    which = rng.integers(len(robots), size=n)                     # each robot of the register as often
    pick = rng.random(n)                                          # and each of its versions as often
    robot = np.zeros(n, dtype=int)
    for k, r in enumerate(robots):
        versions = schemas.versions(r.taken_apart)
        rows = which == k
        robot[rows] = np.array([names.index(v) for v in versions])[np.minimum((pick[rows] * len(versions)).astype(int),
                                                                               len(versions) - 1)]
    # The shared numbers (constants, joint parts, shares, magnet grades): one set for a type of one file (types 1 and
    # 2, as before); for a type over several files one set per file, each robot drawn with its own file's (E11.7
    # point 4), in the order of the files' types.
    files = inputs.files or {inputs.robot_type: apart}
    if len(files) == 1:
        shared = Shared(inputs, params, magnets, rng, n)
        shared_of = {name: shared for name in names}
    else:
        # Each file's set as of the type drawing it (its recipes are the type's): only its rows replaced. Each set
        # drawn over all N draws, in the order of the files as before (the same random numbers), then cut to the draws
        # of its own file's robots, the only ones that read it (keep_rows; until 2026-11-13 every set over all N draws:
        # four sets of 1 GB for robot type 3 at 200,000 draws).
        file_of = {name: t for t, f in files.items() for name in f.robots if name in apart.robots}
        per_file = {}
        for t, f in sorted(files.items()):
            mine = np.flatnonzero(np.isin(robot, [k for k, name in enumerate(names) if file_of.get(name) == t]))
            per_file[t] = Shared(replace(inputs, apart=f), params, magnets, rng, n).keep(mine)
        shared = per_file[min(per_file)]
        shared_of = {name: per_file[t] for name, t in file_of.items()}
    mass = np.zeros(n)
    done = []
    for k, name in enumerate(names):
        rows = np.flatnonzero(robot == k)
        constants = apart.constants[name]
        robot_kg = triangle(rng, *constants[ROBOT_MASS][1], rows.size)
        mass[rows] = robot_kg
        r = Robot(name, rows, shared_of[name], robot_kg)
        draw_robot(r, inputs, constants, rng)
        frame = next(p for p in apart.parts if p.robot == name and p.computed.startswith(FRAME))
        rest = robot_kg - sum(r.parts.values())
        r.piece(f'{name}: {frame.name}', KIND_OF[frame.kind], frame.name, frame.material, rest,
                frame.label.startswith('E'), grade=frame.grade)
        done.append(r)
        if say is not None and (k + 1) % 10 == 0:
            say(k + 1, len(names), name)
    # What assemble takes of the shared draws (their heat), and the aluminium's recipe for the notes page; then the
    # shared draws let go, before the robots' draws are put together (assemble).
    heat = (SimpleNamespace(heat=shared.heat, heat_grade=shared.heat_grade) if len(files) == 1
            else heat_of(done, shared_of, n))
    aluminium = shared.recipe_name[ALUMINIUM]
    for r in done:
        r.shared = None
    shared = shared_of = per_file = None
    d = assemble(n, names, robot, mass, done, apart, heat)
    done = None
    check_taken(d)   # every element of each kind in its parts of how a robot is taken apart, adding up to the kind
    check_recipes(d)   # every material's elements adding up to its kilograms whose elements are drawn
    d.register, d.register_robot = [f'{r.number} {r.name}' for r in robots], which
    d.on_estimates = on_estimates(apart, [v for r in robots for v in schemas.versions(r.taken_apart)])
    d.robot_type, d.listed = inputs.robot_type, inputs.listed or len(robots)
    d.aluminium = alloy_words(inputs.base.recipes, aluminium)
    d.templates = schemas.template_words(apart)   # E13 rules 2 and 4, for its notes page
    d.holds = holds_words(d, inputs, magnets)     # the alloys table (E19 point 4)
    return d


def heat_of(done: list, shared_of: dict, n: int) -> SimpleNamespace:
    """The heat a type over several files is built for, draw by draw (E11.7 point 4): each robot's draws its own
    file's heat and grade classes by heat group (Shared.heat, Shared.heat_grade), put together as assemble() takes
    them."""
    heat, grade = np.zeros(n), {}
    for r in done:
        s = shared_of[r.name]
        heat[r.rows] = r.of(s.heat)
        for group, classes in s.heat_grade.items():
            grade.setdefault(group, np.full(n, '', dtype=classes.dtype))[r.rows] = r.of(classes)
    return SimpleNamespace(heat=heat, heat_grade=grade)


def alloy_words(recipes, name: str) -> str:
    """A recipe of alloys in words, for the notes page: 'die-cast 0 to 40 %, of the wrought rest 7075 0 to 64 % and
    6061' (type 1's aluminium): each item's share as its minimum to maximum, a remainder named last."""
    items = [i for i in recipes.items if i.recipe == name]
    share = lambda i: f'{100 * i.share[0]:g} to {100 * i.share[2]:g} %'   # noqa: E731
    words = []
    for top in (i for i in items if not i.within):
        if not top.remainder:
            words.append(f"{top.item.lower().replace(' ', '-')} {share(top)}")
            continue
        inner = [i for i in items if i.within == top.item]
        rest = [i.item for i in inner if i.remainder]
        words.append(f'of the {top.item.lower()} rest ' + ', '.join(f'{i.item} {share(i)}' for i in inner
                                                                   if not i.remainder)
                     + (f' and {rest[0]}' if rest else ''))
    return ', '.join(words)


def share_words(low: float, high: float) -> str:
    """A share of a mass from its least to its most, in % to two significant digits: '1.2–2', '58–65'; one number
    where they are the same; below 0.005 % it is 0 at this precision (a magnet's least drawn niobium, 0.00024 %)."""
    def pct(x: float) -> str:
        return '0' if 100 * x < 0.005 else f'{100 * x:.2g}'
    return pct(low) if pct(low) == pct(high) else f'{pct(low)}–{pct(high)}'


def recipe_words(recipes, name: str) -> str:
    """What a recipe of single elements holds, for the alloys table: 'Zn 5.1–6.1, Mg 2.1–2.9, …; Al the rest', each
    item's least to most share, the largest first, its remainder last ('Ni 100' where the remainder is all)."""
    items = [i for i in recipes.items if i.recipe == name and not i.within]
    if not items:
        raise ValueError(f"the alloys table: no recipe '{name}' in the element recipes.")
    shown, rest = [], ''
    for i in items:
        symbols = list(schemas.composition(recipes.compounds[i.compound][0])) if i.compound in recipes.compounds else []
        symbol = symbols[0] if len(symbols) == 1 else i.compound
        if i.remainder:
            rest = symbol
        elif share_words(i.share[2], i.share[2]) != '0':   # below the precision shown, 0.005 %, left out
            shown.append((i.share[2], f'{symbol} {share_words(i.share[0], i.share[2])}'))
    words = ', '.join(text for _, text in sorted(shown, key=lambda x: -x[0]))
    return f'{words}; {rest} the rest' if words else f'{rest} 100'


def steel_words(found: dict, rest: str) -> str:
    """What a steel of RAWCLICVehicleTractionMotor's workbook holds, for the alloys table: each element's range, the
    largest first, its remainder (iron) last."""
    words = ', '.join(f'{e} {share_words(low, high)}' for e, (low, high) in sorted(found.items(), key=lambda x: -x[1][1])
                      if share_words(high, high) != '0')
    return f'{words}; {rest} the rest'


def magnet_words(names: list, drawn: np.ndarray) -> str:
    """What a grade class of NdFeB magnets holds, for the alloys table: each element's least to most over its drawn
    fractions (RAWCLICVehicleTractionMotor's, no recipe here), the largest first, iron the rest."""
    shown = [(float(drawn[:, k].max()), f'{e} {share_words(float(drawn[:, k].min()), float(drawn[:, k].max()))}')
             for k, e in enumerate(names) if e != 'Fe' and share_words(drawn[:, k].max(), drawn[:, k].max()) != '0']
    return ', '.join(text for _, text in sorted(shown, key=lambda x: -x[0])) + '; Fe the rest'


def holds_words(d: Draws, inputs: ApartInputs, magnets: dict) -> dict:
    """What each alloy, grade and magnet class of a robot type holds, for its alloys table (EVIDENCE.md E19 point 4;
    Matthias, 2026-11-02, "So if elements are in alloys, then one has to know it", and his yes to the preview of type
    5): (material, grade) -> words, for the materials of TABLE_MATERIALS: a recipe's items, a sibling steel's ranges, a
    magnet class's drawn fractions."""
    out = {}
    for material, grade in {(m, x) for _, m, x in d.details if m in TABLE_MATERIALS}:
        if material == MAGNETS:
            out[(material, grade)] = magnet_words(*magnets[grade])
        elif not grade:   # a part of an alloy with neither a grade nor a recipe of its type
            out[(material, grade)] = 'no recipe in this robot type'
        elif grade in inputs.steels:
            out[(material, grade)] = steel_words(*inputs.steels[grade])
        else:
            out[(material, grade)] = recipe_words(inputs.base.recipes, grade)
    return out


def on_estimates(apart, drawn: list) -> dict:
    """What of the robots drawn rests most on estimates (E), for the notes page (the entry, point 8), by 01's
    estimate_kinds: their joint modules a share of their mass, their joints' masses from their torques, their battery's
    energy a share of their mass, their mass itself."""
    # In plain words, without the sections of EVIDENCE.md (E5.17 points 1, 2 and 6; E5.12 point 4, E2.8e), which are
    # project words on a page (Matthias's figure rule; 2026-10-29, "Yes, build them", point 7). What a template of
    # joint shares averages in the words of its own rows, which name it in brackets (type 1: "as batch 1 on average";
    # type 2: its seven robots with every joint's torque; 2026-10-30, "Yes, build it", open point B).
    # Type 2 has two templates (on legs, E7.4; on wheels, E9.6): each robot of a template under its own words.
    def averaged(robot: str) -> str:
        return next((schemas.template_of(j) for j in apart.joints if j.robot == robot and j.share is not None
                     and j.name.endswith(')')), '') or 'on average'

    words = {'joint torques': "the joints' masses from their torques",
             'joint estimates': "the joints' masses estimated, no torque stated",
             'battery per kg': "the battery's energy a share of the robot's mass",
             'mass': 'the mass itself'}
    out: dict = {}
    for r in drawn:
        if 'joint shares' in schemas.estimate_kinds(apart, r):
            out.setdefault(f"the joint modules a share of the robot's mass, split {averaged(r)}", []).append(r)
    for key, what in words.items():
        out[what] = [r for r in drawn if key in schemas.estimate_kinds(apart, r)]
    return {what: robots for what, robots in out.items() if robots}


def draw_robot(r: Robot, inputs: ApartInputs, constants: dict, rng: np.random.Generator) -> None:
    """Every part of one robot but its frame: its joints with all inside them, its parts, boards and sensors, its
    battery."""
    apart, s, n, name = inputs.apart, r.shared, r.n, r.name
    label = {p.name: p.label for p in apart.parts if p.robot == name}
    joints = [j for j in apart.joints if j.robot == name]
    in_robot = sum(j.count for j in joints)

    # The joints, joint kind by joint kind: the components of the G1's joint of their size, times the joint's module
    # mass over the G1 joint's at its modes, the structure their remainder; times the joints of the kind. A module
    # mass is drawn where the parts file gives it; where the robot's joint modules are a share of its mass, one share
    # is drawn for the robot and split by each joint's share (nothing rescaled); else the G1's joint as weighed.
    drivers = {('small' if 'small' in b.name else 'large'): b for b in apart.boards
               if b.robot == name and b.kind in IN_THE_JOINTS}
    # The sensors in the joints (the encoders; since E38 point 2 the temperature sensors): their number in the robot,
    # drawn where their row gives none, spread over the joints by each joint kind's share of the joints.
    encoders = [p for p in apart.sensors if p.robot == name and p.kind in IN_THE_JOINTS]
    in_joints = {e.name: sensor_count(e, constants, rng, n) for e in encoders}
    # The share of the template the robot takes: on legs or, for a robot on wheels, on wheels (E9.7 point 3).
    modules = (r.mass * r.of(s.constant[schemas.template_quantity(apart, name, JOINT_SHARE)])
               if any(j.share is not None for j in joints) else None)
    for j in joints:
        kind = JOINT_KIND[j.name.split()[0].lower()]
        estimate = label.get(f'Joint module, {j.module}', 'E').startswith('E')
        if j.share is not None:
            stated = modules * j.share / j.count
        else:
            stated = None if None in j.module_mass else triangle(rng, *j.module_mass, n)
        scale = np.ones(n) if stated is None else stated / s.at_mode[j.module]
        one = {component: r.of(kg) * scale for component, kg in s.joint[j.module].items()}   # one joint, kg
        # The large capacitors of its driver board (E51): the robot's number of them, each of the drawn mass; inside its
        # joint module, so that a module whose mass its maker states keeps that mass, its structure the less.
        one[LARGE_CAPACITOR_ITEM] = r.of(s.large_capacitors) * r.of(s.constant[schemas.LARGE_CAPACITOR_G]) / 1000
        if stated is not None:
            rest = stated - sum(kg for component, kg in one.items() if component not in STRUCTURE)
            one.update({component: rest * share for component, share in s.structure_share[j.module].items()})
            r.structures[f'{name}: {j.name} structure'] = rest
        part = f'{name}: {j.name} ({j.count} joints)'
        for component, kg_one in one.items():
            kg_here = kg_one * j.count
            if component == DRIVER_BOARD:
                r.material(part, kind, ELECTRONICS, kg_here, estimate, taken=schemas.taken_part(kind,
                                                                                               component=CIRCUIT_BOARDS))
                area = r.of(s.board_area[j.module]) * scale * j.count
                # The joint's encoders and temperature sensors sit on its driver board: their elements are in its
                # mass (point 3b).
                inside = sum((r.sensor_kg([(t, u) for _, sensor, t, u in apart.elements if sensor == e.name],
                                          in_joints[e.name] / in_robot * j.count) for e in encoders), np.zeros(n))
                # Its ceramic capacitors (E38 point 4): their barium titanate a share of the board's mass, its
                # elements by the formula, the circuit boards'; taken out of the board's glass and epoxy, its mass
                # unchanged. Their nickel electrodes, copper and tin are in the board's metals per cm2 (the car's
                # populated boards), so not added again.
                titanate = kg_here * r.of(s.titanate_share)
                r.drawn(ELECTRONICS, titanate)             # the capacitors' barium titanate, its elements by formula
                for element, share in TITANATE.items():
                    r.element(kind, element, titanate * share, estimate, ELECTRONICS, element in INTEREST,
                              CIRCUIT_BOARDS)
                r.board(kind, drivers[j.module].category, kg_here, area, estimate, inside + titanate)
            elif component == LARGE_CAPACITOR_ITEM:
                r.capacitors(part, kind, kg_here, True)        # their number an estimate (E51)
            else:
                r.piece(part, kind, component, s.material[component], kg_here, estimate, j.heat_group,
                        s.grade[component])
        for e in encoders:   # their elements only: their mass is inside the joint's components
            units = [(t, u) for _, sensor, t, u in apart.elements if sensor == e.name]
            r.sensor(kind, units, in_joints[e.name] / in_robot * j.count, e.label.startswith('E'))

    # The parts: of one material or of shares, the cables from their length, the shell a share of the robot's mass, a
    # hydraulic robot's oil its volume times its density. The bodies of hydraulic actuators and the battery follow
    # below; the frame is added last, by draw_taken_apart().
    for p in apart.parts:
        if p.robot != name or p.kind in IN_THE_JOINTS or p.computed.startswith((PACK, CELLS, HOUSING, HOUSING_OF_CELLS,
                                                                                FRAME, ACTUATORS, ACTUATOR_REST)):
            continue
        kind, estimate, column = KIND_OF[p.kind], p.label.startswith('E'), f'{name}: {p.name}'
        if p.computed.startswith(CABLES):
            # Two conductors for power, and two for signals or an Ethernet line of eight (the robot's cable length says
            # which): m × mm2 × g/cm3 is g.
            if CABLE_ETHERNET in constants:
                length, signals = constants[CABLE_ETHERNET][1], 8 * r.of(s.constant[ETHERNET_CS])
            else:
                length, signals = constants[CABLE_FOUR][1], 2 * r.of(s.constant[SIGNAL_CS])
            mm2 = 2 * r.of(s.constant[POWER_CS]) + signals
            copper = triangle(rng, *length, n) * mm2 * r.of(s.constant[DENSITY]) / 1000
            # In the electronics, as their component the cables (E32): copper and insulation as they are made.
            r.material(column, kind, COPPER, copper, estimate, component=CABLE_PARTS)
            r.material(column, kind, 'Plastics', copper * r.of(s.constant[INSULATION]), estimate, component=CABLE_PARTS)
            continue
        if p.computed.startswith(OIL):
            kg = triangle(rng, *constants[schemas.OIL_VOLUME][1], n) * r.of(s.constant[schemas.OIL_DENSITY])
        elif p.computed.startswith(SHELL):
            # A share of the robot's mass by the shared number it names (the shell's; a lift column's, less its motor,
            # a joint drawn above: E9.7 point 3).
            kg = r.mass * r.of(s.constant[schemas.share_quantity(p.computed) or SHELL_SHARE])
            if LESS_ITS_MOTOR in p.computed:
                kg = kg - sum((v for c, v in r.parts.items() if c.startswith(f'{name}: Lift')), np.zeros(n))
        else:
            kg = p.count * triangle(rng, *p.bounds, n)
        # A part of the cables beyond their conductors is a connector: in the electronics, as their component (E32).
        r.piece(column, kind, p.name, p.material, kg, estimate, grade=p.grade,
                component=CONNECTORS if p.kind == CABLE_KIND else '')

    # The boards outside the joints: their area, their mass from it, their elements.
    for b in apart.boards:
        if b.robot != name or b.kind in IN_THE_JOINTS:
            continue
        area = b.count * triangle(rng, *b.bounds, n)
        kg = area * r.of(s.constant[BOARD_G_PER_CM2]) / 1000
        r.material(f'{name}: {b.name}', KIND_OF[b.kind], ELECTRONICS, kg, b.label.startswith('E'),
                   taken=schemas.taken_part(KIND_OF[b.kind], component=CIRCUIT_BOARDS))
        r.board(KIND_OF[b.kind], b.category, kg, area, b.label.startswith('E'))
        # A capacitor board's capacitors (E51): their number its maker's where its parts list counts them (the RP1's
        # motor-capacitor board, 'Capacitors on: <board>'), else the shared number, a whole number in every draw; each
        # of the drawn mass.
        if schemas.is_capacitor_board(b.name):
            own = constants.get(schemas.CAPACITORS_ON + b.name)
            on_board = whole_numbers(rng, *own[1], n) if own else r.of(s.board_capacitors)
            caps = b.count * on_board * r.of(s.constant[schemas.BOARD_CAPACITOR_G]) / 1000
            r.capacitors(f'{name}: {b.name}', KIND_OF[b.kind], caps, b.label.startswith('E') or own is None)

    # The sensors outside the joints: their mass (g) where a source gives it, their car sensor elements. A module is
    # its elements (electronics) and its housing, the rest of its mass: aluminium a share of it, plastics the remainder
    # (2026-10-29, "Yes, build them", point 3c; the car file holds the elements, "not the complete module housing").
    # A sensor whose mass no source states is its elements at least (point 3b: the electronics wholly in the elements);
    # its housing, not known, stays in the frame's remainder. A sensor whose number no source states (E31 point 3: the
    # cameras of a robot whose sources count none) has its number drawn, a whole number in every draw, from the
    # robot's own constant NUMBER_OF + its name (whole_numbers); one whose number is written 'A or B' (E38 point 2: an
    # option) one of them, each as often (sensor_count).
    for e in apart.sensors:
        if e.robot != name or e.kind in IN_THE_JOINTS:
            continue
        units = [(t, u) for _, sensor, t, u in apart.elements if sensor == e.name]
        estimate, column, kind = e.label.startswith('E'), f'{name}: {e.name}', KIND_OF[e.kind]
        count = sensor_count(e, constants, rng, n)
        inside = r.sensor_kg(units, count)
        sensors = schemas.taken_part(kind, sensor=True)   # a sensor and its housing: the sensors, wherever it sits
        r.material(column, kind, ELECTRONICS, inside, estimate, taken=sensors)
        if None not in e.bounds:
            kg = count * triangle(rng, *e.bounds, n) / 1000
            aluminium = (kg - inside) * r.of(s.constant[SENSOR_ALUMINIUM])
            r.material(column, kind, ALUMINIUM, aluminium, estimate, taken=sensors)
            r.material(column, kind, 'Plastics', kg - inside - aluminium, estimate, taken=sensors)
        r.sensor(kind, units, count, estimate, e.region)

    # The hydraulic actuators (EVIDENCE.md E27.7 point 2): each place's actuators as weighed; their valves, boards and
    # sensors drawn above (the rows whose names end with the place); their bodies, rods and seals the remainder, as a
    # weighed pack's housing is (01 checks that it never falls below zero).
    for body in (p for p in apart.parts if p.robot == name and p.computed.startswith(ACTUATOR_REST)):
        place = schemas.place_of(body.name)
        whole = next(p for p in apart.parts if p.robot == name and p.computed.startswith(ACTUATORS)
                     and schemas.place_of(p.name) == place)
        inside = sum((kg for column, kg in r.parts.items() if column.startswith(f'{name}: ')
                      and schemas.place_of(column) == place), np.zeros(n))
        kg = whole.count * triangle(rng, *whole.bounds, n) - inside
        r.piece(f'{name}: {body.name}', KIND_OF[body.kind], body.name, body.material, kg, body.label.startswith('E'),
                grade=body.grade)

    # The battery: its energy (its voltage times its capacity, or its energy per kg of robot times its mass), its cells
    # from it, its housing the pack's stated mass less its cells and its management board (the boards of the kind
    # Battery pack), or, where no source weighs the pack, a share of its cells (Matthias, 2026-11-02, "A, as
    # recommended", EVIDENCE.md E20: the pack then its cells, its housing and its board, the housing never below zero).
    # A pack with no housing is its cells and board.
    pack = next((p for p in apart.parts if p.robot == name and p.computed.startswith(PACK)), None)
    if pack is not None:
        if VOLTAGE in constants:
            wh = triangle(rng, *constants[VOLTAGE][1], n) * triangle(rng, *constants[CAPACITY][1], n)
        else:
            wh = r.mass * r.of(s.constant[schemas.template_quantity(apart, name, ENERGY_PER_KG)])
        cells = next(p for p in apart.parts if p.robot == name and p.computed.startswith(CELLS))
        # The cells' recipe: the one their row names (the CASBOT W1's LFP, E9.7 point 5), else the NMC cells'.
        recipe = cells.grade or CELL_RECIPE
        wh_per_kg, elements, metal = s.cell_draws(recipe)
        cells_kg = wh / r.of(wh_per_kg)
        column = f'{name}: {cells.name}'
        r.parts[column] = cells_kg
        r.materials[('battery', CELL_MATERIAL)] = r.materials.get(('battery', CELL_MATERIAL), 0) + cells_kg
        in_cells = ('battery', schemas.taken_part('battery', cells.name, CELL_MATERIAL))
        r.taken_kg[in_cells] = r.taken_kg.get(in_cells, 0) + cells_kg
        # The cells by their chemistry, for the material pages (Matthias, 2026-10-29: "Give me NMC etc. for the
        # batteries as materiel"): the recipe they follow.
        key = ('battery', CELL_MATERIAL, recipe)
        r.details[key] = r.details.get(key, 0) + cells_kg
        r.drawn(CELL_MATERIAL, cells_kg)                   # the cells' elements by their recipe
        for element, share in elements.items():
            r.element('battery', element, cells_kg * r.of(share), cells.label.startswith('E'), CELL_MATERIAL)
        r.declare_all('battery', CELL_MATERIAL, elements, metal, cells_kg, cells.label.startswith('E'),
                      taken=schemas.taken_part('battery', cells.name, CELL_MATERIAL))
        housing = next((p for p in apart.parts if p.robot == name
                        and p.computed.startswith((HOUSING, HOUSING_OF_CELLS))), None)
        if housing is not None:
            if housing.computed.startswith(HOUSING_OF_CELLS):
                # A pack no source weighs (E20): its housing the share its row names of its cells, in each draw; the
                # CASBOT W1's LFP cells so too, as an NMC pack's housing in proportion to its cells (E9.8).
                kg = cells_kg * r.of(s.constant[schemas.share_quantity(housing.computed)])
            else:
                managed = sum((r.parts[f'{name}: {b.name}'] for b in apart.boards
                               if b.robot == name and b.kind == 'Battery pack'), np.zeros(n))
                kg = pack.count * triangle(rng, *pack.bounds, n) - cells_kg - managed
            r.piece(f'{name}: {housing.name}', 'battery', housing.name, housing.material, kg,
                    housing.label.startswith('E'), grade=housing.grade)


def assemble(n: int, names: list, robot: np.ndarray, mass: np.ndarray, done: list, apart, shared: Shared) -> Draws:
    """The robots' draws put together into the N draws, in the order the data file names things. Each quantity's
    draws of the robots let go once it is put together (let_go), so that the robots' draws and the draws put together
    are not held whole at the same time (2026-11-13: the peak of drawing robot type 3 was both)."""
    def put(key, store, r):
        values = np.zeros(n)
        values[r.rows] = store[key]
        return values

    def let_go(name: str) -> None:
        for r in done:
            setattr(r, name, None)

    disk = DiskArrays()   # the draws put together kept on the disk, memory-mapped (DiskArrays)

    # The parts and the joints' structures robot by robot (PartBlocks): only each robot's own draws are held.
    part_columns, blocks = [], []
    for r in done:
        blocks.append((r.rows, len(part_columns), np.column_stack([r.parts[c] * np.ones(r.n) for c in r.parts])
                       if r.parts else np.zeros((r.n, 0))))
        part_columns += list(r.parts)
    part_blocks = PartBlocks(n, part_columns, blocks)
    let_go('parts')
    remainders = [f'{p.robot}: {p.name}' for p in apart.parts if p.computed.startswith((FRAME, HOUSING, ACTUATOR_REST))]
    structure_blocks = {c: (r.rows, r.structures[c] * np.ones(r.n)) for r in done for c in r.structures}
    let_go('structures')
    material_keys = sorted({k for r in done for k in r.materials}, key=lambda k: (list(KINDS).index(k[0]), k[1]))
    materials = np.column_stack([sum((put(k, r.materials, r) for r in done if k in r.materials), np.zeros(n))
                                 for k in material_keys])
    materials = disk.matrix(materials)
    let_go('materials')
    elements = {k: sum((put(k, r.elements, r) for r in done if k in r.elements), np.zeros(n))
                for k in {k for r in done for k in r.elements}}
    elements = disk.table(elements)
    let_go('elements')
    estimated = {k: sum((put(k, r.estimated, r) for r in done if k in r.estimated), np.zeros(n))
                 for k in {k for r in done for k in r.estimated}}
    estimated = disk.table(estimated)
    let_go('estimated')
    hot = schemas.hot_kinds(apart)
    followed = {m: sum((put(m, r.followed, r) for r in done if m in r.followed), np.zeros(n))
                for m in {m for r in done for m in r.followed}}
    followed = disk.table(followed)
    let_go('followed')
    details = {k: sum((put(k, r.details, r) for r in done if k in r.details), np.zeros(n))
               for k in {k for r in done for k in r.details}}
    details = disk.table(details)
    let_go('details')
    recipe_elements = {k: sum((put(k, r.recipe_elements, r) for r in done if k in r.recipe_elements), np.zeros(n))
                       for k in {k for r in done for k in r.recipe_elements}}
    recipe_elements = disk.table(recipe_elements)
    let_go('recipe_elements')
    in_recipes = {m: sum((put(m, r.in_recipes, r) for r in done if m in r.in_recipes), np.zeros(n))
                  for m in {m for r in done for m in r.in_recipes}}
    in_recipes = disk.table(in_recipes)
    let_go('in_recipes')
    elements_of = {m: sum((put(m, r.elements_of, r) for r in done if m in r.elements_of), np.zeros(n))
                   for m in {m for r in done for m in r.elements_of}}
    elements_of = disk.table(elements_of)
    let_go('elements_of')
    by_material = {k: sum((put(k, r.by_material, r) for r in done if k in r.by_material), np.zeros(n))
                   for k in {k for r in done for k in r.by_material}}
    by_material = disk.table(by_material)
    let_go('by_material')
    fixed = {k: sum((put(k, r.fixed, r) for r in done if k in r.fixed), np.zeros(n))
             for k in {k for r in done for k in r.fixed}}
    fixed = disk.table(fixed)
    let_go('fixed')
    places = {k: sum((put(k, r.places, r) for r in done if k in r.places), np.zeros(n))
              for k in {k for r in done for k in r.places}}
    places = disk.table(places)
    let_go('places')
    places_estimated = {k: sum((put(k, r.places_estimated, r) for r in done if k in r.places_estimated), np.zeros(n))
                        for k in {k for r in done for k in r.places_estimated}}
    places_estimated = disk.table(places_estimated)
    let_go('places_estimated')
    taken = {k: sum((put(k, r.taken, r) for r in done if k in r.taken), np.zeros(n))
             for k in {k for r in done for k in r.taken}}
    taken = disk.table(taken)
    let_go('taken')
    taken_kg = {k: sum((put(k, r.taken_kg, r) for r in done if k in r.taken_kg), np.zeros(n))
                for k in {k for r in done for k in r.taken_kg}}
    taken_kg = disk.table(taken_kg)
    let_go('taken_kg')
    layer_check = {k: tuple(sum(r.layer_check[k][i] for r in done if k in r.layer_check) for i in (0, 1))
                   for k in {k for r in done for k in r.layer_check}}

    let_go('layer_check')
    drawn = Draws(n, names, robot, mass, part_blocks, remainders, structure_blocks, (material_keys, materials),
                 elements, estimated, hot, shared.heat, shared.heat_grade, followed, details, recipe_elements,
                 in_recipes, by_material, fixed=fixed, places=places, places_estimated=places_estimated, taken=taken,
                 taken_kg=taken_kg, layer_check=layer_check, elements_of=elements_of)
    drawn.disk = disk   # its folder on the disk lives as long as the record
    return drawn


def check_recipes(d: Draws) -> None:
    """Whether each material's elements add up to its kilograms whose elements are drawn, in every draw, within
    COMPOUND_TOLERANCE (the element recipes' compounds written to five decimals), and no material holds elements without
    such kilograms or such kilograms without elements (Matthias, 2026-11-08, "Yes, fix it": until then 02 compared the
    elements with themselves). Raises ValueError, in plain words, where not: 02 then writes nothing."""
    for material in sorted(set(d.elements_of or {}) | set(d.in_recipes or {})):
        kg = d.in_recipes.get(material, np.zeros(d.n))
        elements = d.elements_of.get(material, np.zeros(d.n))
        off = np.abs(elements - kg) > COMPOUND_TOLERANCE * np.abs(kg) + 1e-12
        if off.any():
            k = int(off.sum())
            raise ValueError(f'{material}: its elements miss its kilograms whose elements are drawn in {k} draw'
                             f"{'s' if k != 1 else ''} (by up to {float(np.abs(elements - kg).max()):.3g} kg).")


def check_taken(d: Draws) -> None:
    """Whether the elements and the mass of each kind split by part of how a robot is taken apart add up to the
    kind's elements and its mass (all its materials), draw by draw (to a billionth of the kind's largest draw: the same
    kilograms added in another order), and every part is one of 01's TAKEN_PARTS. Raises ValueError, in plain words,
    where not: 02 then writes nothing."""
    for kind, part in d.taken_kg:
        if part not in schemas.TAKEN_PARTS:
            raise ValueError(f'{KINDS[kind][0]}: its mass booked to "{part}", not a part of how a robot is taken apart.')
    for kind in {k for k, _ in d.materials[0]} | {k for k, _ in d.taken_kg}:
        whole = kind_kg(d, kind)
        split = sum((v for (k, _), v in d.taken_kg.items() if k == kind), np.zeros(d.n))
        off = float(np.abs(split - whole).max())
        if off > 1e-9 * max(float(np.abs(whole).max()), 1e-12):
            raise ValueError(f'{KINDS[kind][0]}: the mass of its parts of how a robot is taken apart adds up to '
                             f'{off:.3g} kg more or less than the kind in some draw.')
    for kind, part, element in d.taken:
        if part not in schemas.TAKEN_PARTS:
            raise ValueError(f'{element} in {KINDS[kind][0]}: booked to "{part}", not a part of how a robot is taken '
                             'apart.')
    for (kind, element), kg in d.elements.items():
        split = sum((v for (k, _, e), v in d.taken.items() if k == kind and e == element), np.zeros(d.n))
        off = float(np.abs(split - kg).max())
        if off > 1e-9 * max(float(np.abs(kg).max()), 1e-12):
            raise ValueError(f'{element} in {KINDS[kind][0]}: its parts of how a robot is taken apart add up to '
                             f'{off:.3g} kg more or less than the kind in some draw.')
    for kind, _, element in d.taken:
        if (kind, element) not in d.elements:
            raise ValueError(f'{element} in {KINDS[kind][0]}: in a part of how a robot is taken apart, not in its kind.')


def kind_kg(d: Draws, kind: str) -> np.ndarray:
    """The kg of one kind of part in each draw: all its materials."""
    columns, draws = d.materials
    return draws[:, [i for i, (k, _) in enumerate(columns) if k == kind]].sum(axis=1)


def remainders_below(d: Draws) -> np.ndarray:
    """In every draw, whether a remainder of the robot drawn (its frame, a weighed pack's housing, a joint's structure)
    is below zero (E21)."""
    below = np.zeros(d.n, dtype=bool)
    for column in d.remainders:
        below |= d.part_blocks.column(column) < 0
    for rows, values in d.structure_blocks.values():
        below[rows] |= values < 0
    return below


def below_zero(d: Draws) -> dict:
    """The share of each robot's draws where one of its remainders (a frame, a battery housing, a joint's structure)
    falls below zero: '<robot>: <part>' -> share."""
    out = {}
    for column in d.remainders:
        out[column] = float((d.part_blocks.robot_column(column) < 0).mean())   # over its robot's draws
    for column, (rows, values) in d.structure_blocks.items():
        out[column] = float((values < 0).mean())
    return out


def element_order(elements) -> list:
    """Elements in the order of 01's table of atomic masses, the others after them by name."""
    known = list(schemas.ATOMIC_MASS)
    return sorted(elements, key=lambda e: (known.index(e) if e in known else len(known), e))


# ------------------------------------------------------------------------------------------------------
# What is written
# ------------------------------------------------------------------------------------------------------

def statistics(values: np.ndarray) -> list:
    """Mean, median, 2.5 % and 97.5 % of the draws that hold it (kg), and the share of the draws they are (%), with
    statistics_of: a 0 is not part of a distribution (CLAUDE.md §7); empty where it is 0 in every draw."""
    s = statistics_of(values)
    return [s['Mean (kg)'], s['Median (kg)'], s['2.5 % (kg)'], s['97.5 % (kg)'], s['Held in (% of the draws)']]


def by_material_table(d: Draws) -> tuple:
    """The table 'by_material' of a robot type (EVIDENCE.md E29 question 2): each element of interest by the material
    it comes from (Draws.by_material, as its element pages split it), '<element>: <material>', its columns adding up to
    the element in every draw; after each element's, the element fixed in each alloy that holds it (Draws.fixed, E25:
    only copper so far), '<element>: <material> (fixed in alloys)', adding up to the copper fixed in alloys. The
    elements in the order of 01's table of atomic masses, the materials in MATERIAL_ORDER, any other after them by
    name."""
    def material_key(material: str) -> tuple:
        known, parts = list(MATERIAL_ORDER), list(map(component_label, ELECTRONICS_COMPONENTS))
        if material in parts:   # a component of the electronics (E32) at the electronics' place, in their order
            return known.index(ELECTRONICS), parts.index(material), material
        return (known.index(material) if material in known else len(known), -1, material)

    recovered, fixed = d.by_material or {}, d.fixed or {}
    columns, draws = [], []
    for element in element_order({e for _, e in recovered} | {e for _, e in fixed}):
        for material in sorted((m for m, e in recovered if e == element), key=material_key):
            columns.append(f'{element}: {material}')
            draws.append(recovered[(material, element)])
        for material in sorted((m for m, e in fixed if e == element), key=material_key):
            columns.append(f'{element}: {material}{FIXED_MARK}')
            draws.append(fixed[(material, element)])
    return columns, np.column_stack(draws) if draws else np.zeros((d.n, 0))


def taken_keys(d: Draws) -> list:
    """The keys of `d.taken` (kind, part, element) in the order of the kinds, of 01's TAKEN_PARTS and of the
    elements (element_order)."""
    order = element_order({e for _, _, e in d.taken})
    return sorted(d.taken, key=lambda key: (list(KINDS).index(key[0]), schemas.TAKEN_PARTS.index(key[1]),
                                            order.index(key[2])))


def taken_mass_keys(d: Draws) -> list:
    """The keys of `d.taken_kg` (kind, part) in the order of the kinds and of 01's TAKEN_PARTS."""
    return sorted(d.taken_kg, key=lambda key: (list(KINDS).index(key[0]), schemas.TAKEN_PARTS.index(key[1])))


def layer_rows(d: Draws) -> list:
    """The check of the boards' copper against their layers (E51 row 8), a row for each kind of part with boards: its
    name, its boards' layers (min, mode, max), the most copper the most of them can hold (mg per cm2), the share of its
    boards' draws whose copper is above it."""
    rows = []
    for kind in KINDS:
        if kind in (d.layer_check or {}):
            above, total = d.layer_check[kind]
            layers = schemas.board_layers(kind)
            rows.append([KINDS[kind][0], ' / '.join(map(str, layers)), schemas.layers_copper_mg(layers[2]),
                         above / total if total else 0.0])
    return rows


def layer_words(d: Draws) -> list:
    """layer_rows in words, for 02's report of a robot type: '<kind> (<layers> layers) <share> %'."""
    return [f'{name} ({layers} layers, at most {bound:.0f} mg/cm2) {100 * share:.1f} %'
            for name, layers, bound, share in layer_rows(d)] or ['no boards']


def write_taken_apart(d: Draws, folder: str) -> None:
    """A robot type part by part, at every level, and its summary, into `folder` (WHAT IT WRITES in the docstring at
    the top)."""
    os.makedirs(folder, exist_ok=True)
    names = ', '.join(f'{k} {name}' for k, name in enumerate(d.robots))
    element_keys = [(kind, e) for kind in KINDS for e in element_order({e for k, e in d.elements if k == kind})]
    grade_keys = sorted(d.details, key=lambda key: (list(KINDS).index(key[0]), key[1], key[2]))
    # Each table built only when it is written and let go after (until 2026-11-13 all built first: a second copy of
    # the type's draws held while writing, 3 GB for robot type 3 at 200,000 draws).
    tables = {
        'robots': lambda: ([f'Robot drawn ({names})', 'Mass (kg)', 'Robot of the register'],
                   np.column_stack([d.robot, d.mass, d.register_robot])),
        'parts': lambda: (d.part_blocks.columns, d.part_blocks),   # written robot by robot (PartBlocks.save)
        'materials': lambda: ([f'{KINDS[k][0]}: {m}' for k, m in d.materials[0]], d.materials[1]),
        # Each material by its grade, alloy or magnet grade class ('<kind>: <material>: <grade>'; a material whole
        # without the third part): the draws behind the material pages.
        'grades': lambda: ([f'{KINDS[k][0]}: {m}' + (f': {x}' if x else '') for k, m, x in grade_keys],
                   np.column_stack([d.details[key] for key in grade_keys])),
        'elements': lambda: ([f'{KINDS[k][0]}: {e}' for k, e in element_keys],
                     np.column_stack([d.elements[k] for k in element_keys])),
        'estimated': lambda: ([f'{KINDS[k][0]}: {e}' for k, e in element_keys],
                      np.column_stack([d.estimated.get(k, np.zeros(d.n)) for k in element_keys])),
        'by_material': lambda: by_material_table(d),
        # Each element of interest by its place (PLACES): a kind of part, or the electronics' component, '<place>: <e>'.
        'places': lambda: ([f'{place_label(p)}: {e}' for p, e in place_keys(d)],
                   np.column_stack([d.places[k] for k in place_keys(d)])),
        'places_estimated': lambda: ([f'{place_label(p)}: {e}' for p, e in place_keys(d)],
                             np.column_stack([d.places_estimated.get(k, np.zeros(d.n)) for k in place_keys(d)])),
        # Each element of interest by its kind and its part of how a robot is taken apart ('<kind>: <part>: <e>'), in
        # the order of the kinds, of 01's TAKEN_PARTS and of the elements: what 04 counts the elements in use by.
        'taken_apart': lambda: ([f'{KINDS[k][0]}: {part}: {e}' for k, part, e in taken_keys(d)],
                        np.column_stack([d.taken[k] for k in taken_keys(d)])),
        # The mass of each kind by its part of how a robot is taken apart ('<kind>: <part>'), all its materials.
        'taken_apart_mass': lambda: ([f'{KINDS[k][0]}: {part}' for k, part in taken_mass_keys(d)],
                             np.column_stack([d.taken_kg[k] for k in taken_mass_keys(d)])),
    }
    for table in APART_TABLES:
        columns, draws = tables[table]()
        if isinstance(draws, PartBlocks):
            draws.save(os.path.join(folder, f'{table}.npy'))
        else:
            np.save(os.path.join(folder, f'{table}.npy'), np.asarray(draws, dtype=np.float32))
        with open(os.path.join(folder, f'{table}.txt'), 'w', encoding='utf-8') as file:
            file.write('\n'.join(columns) + '\n')
        columns = draws = None   # let go before the next table is built
    # The robots of the register drawn, '<number> <name>', in the order of the column 'Robot of the register'.
    with open(os.path.join(folder, 'register.txt'), 'w', encoding='utf-8') as file:
        file.write('\n'.join(d.register) + '\n')
    rows = [['Robot mass', 'All kinds', *statistics(d.mass)]]
    for element in element_order({e for _, e in d.elements}):
        total = sum(v for (_, e), v in d.elements.items() if e == element)
        rows.append([element, 'All kinds', *statistics(total)])
        for kind in KINDS:
            if (kind, element) in d.elements:
                rows.append([element, KINDS[kind][0], *statistics(d.elements[(kind, element)])])
    with open(os.path.join(folder, 'summary.csv'), 'w', encoding='utf-8', newline='') as file:
        out = csv.writer(file)
        out.writerow(['Element', 'Kind of part', 'Mean (kg)', 'Median (kg)', '2.5 % (kg)', '97.5 % (kg)',
                      'Held in (% of the draws)'])
        out.writerows(rows)
        out.writerow([])
        out.writerow(['Remainder', 'Share of its robot\'s draws below zero'])
        out.writerows([[column, share] for column, share in below_zero(d).items()])
        out.writerow([])
        # The check of the boards' copper against their layers (E51 row 8), reported, not cut.
        out.writerow(['Boards of the kind of part', 'Layers (min / mode / max)', 'Copper all layers can hold at most '
                      '(mg/cm2)', "Share of its boards' draws with more copper"])
        out.writerows(layer_rows(d))
        out.writerow([])
        out.writerow(['Heat group', 'Grade class', 'Share of the draws'])
        out.writerows([[group, klass, float((drawn == klass).mean())] for group, drawn in d.grades.items()
                       for klass in dict.fromkeys(drawn)])


# ------------------------------------------------------------------------------------------------------
# A robot type taken apart as 02 writes every robot type
# ------------------------------------------------------------------------------------------------------

# The kinds of part of a robot type taken apart placed in the shared lists' body regions, so that its tables have the
# columns of every other robot type (03 compares them): whole kinds, not part by part (2026-10-29, "Yes, build them",
# point 5). Its part groups are the four groups of how a robot is taken apart, each the mass of its parts (01's
# TAKEN_APART; Matthias, 2026-11-08: "I want a detailed list of the component", "Yes, add 1 to 3": one grouping in the
# project; until then the shared lists' seven part groups, Joint drives to Wheels and wheel drives, by whole kinds).
# The wheeled base in the body region Base, the lift column in the torso (2026-10-30, "Yes, agree E9.4", point 3).
KIND_BODY_REGION = {'hips': 'Legs', 'knees': 'Legs', 'ankles': 'Legs', 'waist': 'Torso', 'arms': 'Arms',
                    'headjoints': 'Head',
                    'battery': 'Torso', 'boards': 'Torso', 'head': 'Head', 'cables': 'Whole body',
                    'frame': 'Whole body', 'base': 'Base', 'lift': 'Torso',
                    'hydraulics': 'Torso'}   # a hydraulic robot's: where its power unit sits (EVIDENCE.md E27.7)


def compose_taken_apart(category, d: Draws, lists) -> Composition:
    """A robot type taken apart as 02 writes every robot type, from its draws over its robots: its materials (Not
    allocated 0, as the frame takes the rest), its elements, its part groups (the four groups of how a robot is taken
    apart, each the mass of its parts: 01's TAKEN_APART) and body regions (its kinds placed by KIND_BODY_REGION), its
    total; and the kilograms of each material whose elements are drawn."""
    n, materials = d.n, lists.names[schemas.MATERIAL]
    columns, draws = d.materials
    kg_of = {name: np.zeros(n) for name in materials}
    for i, (_, material) in enumerate(columns):
        kg_of[material] += draws[:, i]
    # Not allocated: none, as the frame takes the rest of the robot's mass (the materials add up to it to the
    # rounding of the computer, which draw_faults checks).
    kg_of[NOT_ALLOCATED] = np.zeros(n)
    followed = {name: d.followed.get(name, np.zeros(n)) for name in materials}
    in_recipes = {name: d.in_recipes.get(name, np.zeros(n)) for name in materials}
    element_columns = element_order({e for _, e in d.elements})
    elements = {e: sum((v for (_, x), v in d.elements.items() if x == e), np.zeros(n)) for e in element_columns}
    recipe_columns = element_order({e for _, e in d.recipe_elements})
    recipe_elements = {e: sum((v for (_, x), v in d.recipe_elements.items() if x == e), np.zeros(n))
                       for e in recipe_columns}
    group_names, region_names = list(schemas.TAKEN_APART), lists.names[schemas.BODY_REGION]
    groups = {g: sum((kg for (_, part), kg in d.taken_kg.items() if schemas.TAKEN_GROUP[part] == g), np.zeros(n))
              for g in group_names}
    regions = {r: np.zeros(n) for r in region_names}
    for kind in KINDS:
        regions[KIND_BODY_REGION[kind]] += kind_kg(d, kind)
    tables = {'materials': (materials, stack(materials, kg_of, n)),
              'elements': (element_columns, stack(element_columns, elements, n)),
              'recipe_elements': (recipe_columns, stack(recipe_columns, recipe_elements, n)),
              'part_groups': (group_names, stack(group_names, groups, n)),
              'body_regions': (region_names, stack(region_names, regions, n)),
              'total': (['Total'], d.mass[:, None]),
              'copper': copper_table(elements.get('Cu', np.zeros(n)),
                                     sum((kg for (_, e), kg in (d.fixed or {}).items() if e == 'Cu'), np.zeros(n)))}
    return Composition(category.number, folder_name(category), category.name, tables, stack(materials, followed, n),
                       stack(materials, in_recipes, n), None, None, remainders_below(d))


def same_elements(drawn: list) -> None:
    """Every robot type's elements with the same columns, all the elements any of them holds, in the order of 01's
    table of atomic masses: 0 kg where a robot type's materials hold none of an element so far (its summary says which
    materials are in the elements). 03 compares robot types column by column. The elements of interest so, and the
    elements by the recipes."""
    for table in ('elements', 'recipe_elements'):
        columns = element_order(set().union(*(set(c.tables[table][0]) for c in drawn)))
        for c in drawn:
            own, draws = c.tables[table]
            full = np.zeros((draws.shape[0], len(columns)))
            for k, name in enumerate(own):
                full[:, columns.index(name)] = draws[:, k]
            c.tables[table] = (columns, full)


# ------------------------------------------------------------------------------------------------------
# The page of each robot type (point 14)
# ------------------------------------------------------------------------------------------------------
# Laid out in inches from the top left, with 01's page functions (new_page, write, save), as 01's pages are.

ROW = 0.25                 # the height of one row of a chart, inches
LABEL = 1.9                # the names left of a chart, inches
CHART = 4.4                # the width of a chart, inches
NUMBERS = 2.75             # the numbers right of a chart (the mean, the 95 %, the share held), inches
MARGIN = 0.4               # the margin of the page, inches
GAP = 0.6                  # between the two charts, inches
PAGE_WIDTH = 2 * MARGIN + 2 * (LABEL + CHART + NUMBERS) + GAP
BAR, GREY = schemas.BAR, schemas.GREY   # the bars of 01's pages; grey for Mixed and Not allocated
INTERVAL = '#33332F'       # the line over 95 % of the draws
GRID = '#E1E0D9'           # the hairlines of the kg scale
MUTED = '#52514E'          # secondary text
# The elements in plain words, by their symbols in the recipes.
ELEMENT_NAMES = {'H': 'Hydrogen', 'Li': 'Lithium', 'B': 'Boron', 'C': 'Carbon', 'N': 'Nitrogen', 'O': 'Oxygen',
                 'F': 'Fluorine', 'Na': 'Sodium', 'Mg': 'Magnesium', 'Al': 'Aluminium', 'Si': 'Silicon',
                 'P': 'Phosphorus', 'S': 'Sulfur', 'Ca': 'Calcium', 'Ti': 'Titanium', 'Cr': 'Chromium',
                 'Mn': 'Manganese', 'Fe': 'Iron', 'Co': 'Cobalt', 'Ni': 'Nickel', 'Cu': 'Copper', 'Zn': 'Zinc',
                 'Sn': 'Tin', 'Pb': 'Lead', 'V': 'Vanadium', 'Mo': 'Molybdenum'}


def mass(value: float) -> str:
    """A mass for a page, kg, with three significant figures at least, so that a few grams are not printed as 0:
    104, 12.0, 6.11, 0.0479, 0.0140, 0.000474."""
    size = abs(value)
    if size >= 100:
        return f'{value:.0f}'
    if size >= 10:
        return f'{value:.1f}'
    if size >= 1:
        return f'{value:.2f}'
    if size == 0:
        return '0'
    if size >= 1e-4:
        return f'{value:#.3g}'   # '#' keeps the trailing zeros: 0.150, not 0.15
    return np.format_float_positional(value, precision=3, unique=False, fractional=False)   # not 4.74e-05


def element_label(symbol: str) -> str:
    """An element in plain words: 'Copper (Cu)'."""
    return f'{ELEMENT_NAMES[symbol]} ({symbol})' if symbol in ELEMENT_NAMES else symbol


def interval_bars(axes, rows: list, size: float = 9, grey: bool = False) -> None:
    """On `axes`, one row per (name, its draws): a bar of the median from zero (grey for Mixed and Not allocated, or for
    every row with `grey`; Matthias, 2026-11-10: "Not mean, but median") and a line with end ticks over 95 % of the
    draws (2.5 % to 97.5 %), both of the draws that hold it (statistics_of: a 0 is not part of a distribution); nothing where there is no mass in any draw. The kg
    scale is fitted to the lines, with the zero line and hairlines; the names stand on the left. 03_comparison.py draws
    its charts with it too."""
    stats = [(name, draws.any(), statistics_of(draws)) for name, draws in rows]
    lows = [s['2.5 % (kg)'] for _, present, s in stats if present]
    highs = [s['97.5 % (kg)'] for _, present, s in stats if present]
    low, high = min([0] + lows), max(highs + [1e-9])
    pad = 0.03 * (high - low)
    for i, (name, present, s) in enumerate(stats):
        if not present:
            continue
        lower, upper = s['2.5 % (kg)'], s['97.5 % (kg)']
        colour = GREY if grey or name in ('Mixed', OTHER, NOT_ALLOCATED) else BAR
        axes.barh(i, s['Median (kg)'], height=0.6, color=colour, zorder=2)
        axes.plot([lower, upper, np.nan, lower, lower, np.nan, upper, upper],
                  [i, i, np.nan, i - 0.17, i + 0.17, np.nan, i - 0.17, i + 0.17], color=INTERVAL, linewidth=1.1,
                  zorder=3)
    axes.set_ylim(len(rows) - 0.5, -0.5)
    axes.set_yticks(range(len(rows)), [name for name, _ in rows], fontsize=size)
    axes.tick_params(axis='y', length=0)
    axes.set_xlim(low - pad if low < 0 else 0, high + pad)
    axes.tick_params(axis='x', labelsize=size - 1, colors=MUTED, length=0)
    axes.grid(axis='x', color=GRID, linewidth=0.8)
    axes.set_axisbelow(True)
    axes.axvline(0, color='#C3C2B7', linewidth=0.9, zorder=1)
    for side in ('top', 'right', 'left', 'bottom'):
        axes.spines[side].set_visible(False)


def interval_chart(figure, page, page_height: float, x: float, y: float, title: str, what: str,
                   rows: list) -> float:
    """One chart of a page, under its title and a line saying what it covers: interval_bars, with the median and the
    95 % interval of each row written beside it, both of the draws that hold it, and the share of the draws that hold it
    where it is not all (Matthias, 2026-11-01: "If a value is 0 then it is NOT part of the distribution"); '–' for a
    row with no mass in any draw. (x, y): the chart's top left, inches. Returns the y below it."""
    schemas.write(page, x, y, [title], size=11, weight='normal')
    schemas.write(page, x, y + 0.27, [what], size=9, colour=MUTED)
    y += 0.6
    numbers = x + LABEL + CHART + 0.15
    schemas.write(page, numbers + 0.55, y, ['Median'], size=8.5, colour=MUTED, align='right')
    schemas.write(page, numbers + 0.75, y, ['95 % interval'], size=8.5, colour=MUTED)
    schemas.write(page, numbers + 2.15, y, ['Held in'], size=8.5, colour=MUTED)
    y += 0.25
    height = ROW * len(rows)
    axes = figure.add_axes([(x + LABEL) / PAGE_WIDTH, 1 - (y + height) / page_height, CHART / PAGE_WIDTH,
                            height / page_height])
    interval_bars(axes, rows)
    axes.set_xlabel('kg per robot', fontsize=8.5, color=MUTED)
    for i, (name, draws) in enumerate(rows):
        row_y = y + (i + 0.5) * ROW
        if not draws.any():
            page.text(numbers + 0.55, row_y, '–', fontsize=9, ha='right', va='center')
            continue
        s = statistics_of(draws)
        page.text(numbers + 0.55, row_y, mass(s['Median (kg)']), fontsize=9, ha='right', va='center')
        page.text(numbers + 0.75, row_y, f"{mass(s['2.5 % (kg)'])} to {mass(s['97.5 % (kg)'])}", fontsize=9,
                  va='center')
        if s['Held in (% of the draws)'] < 99.5:   # held in some runs only: their share, never '0 %'
            page.text(numbers + 2.15, row_y, share_text(s['Held in (% of the draws)'] / 100), fontsize=9,
                      va='center')
    return y + height + 0.55


def page_elements(c: Composition) -> list:
    """The rows of a page's 'By element': (the element in plain words, its draws), every element of interest."""
    return [(element_label(name), c.column('elements', name)) for name in c.tables['elements'][0]]


def page_notes(c: Composition) -> list:
    """What a reader needs to read the page of one robot type, in plain words."""
    rows = {r['Name']: r for r in summary(c) if r['Kind'] == 'Material'}
    below = rows[NOT_ALLOCATED]['Draws below zero (%)']
    notes = ["Not allocated: the parts' mass minus the materials' mass in each run, both drawn from the workbook's "
             'minimum, mode and maximum. ' + (f'It is below zero in {below:.1f} % of the runs, where the drawn '
                                              'materials weigh more than the drawn parts.' if below else
                                              'It is above zero in every run.')]
    if c.build is not None:
        notes.append('Battery cells: the cells only, one build of the sheet Battery cells drawn in each run, all '
                     'builds equally likely; the rest of the battery row is in the materials it goes to.')
    elif c.battery is not None:
        notes.append("Battery cells: the workbook's row, already cells only.")
    covered = [n for n, r in rows.items() if r['In the elements'] == 'Yes']
    partly = [n for n, r in rows.items() if r['In the elements'] == 'Partly']
    missing = [n for n, r in rows.items() if r['In the elements'] == 'No' and n != NOT_ALLOCATED]
    notes.append('By element: only the elements of interest, from what is recovered as elements (copper and nickel '
                 'each its metal whole; the aluminium, magnesium and titanium alloys the metal they hold, their whole '
                 'mass in the materials; of the battery cells their lithium, nickel, cobalt and manganese '
                 f'and the copper and aluminium of their foils and tabs). Whole: {", ".join(covered) or "none"}'
                 f'{"; in part: " + ", ".join(partly) if partly else ""}. Not in the elements: '
                 f'{", ".join(missing) or "none"}; their kilograms are in the materials only.')
    notes.append('–: none in this robot type.')
    return notes


def draw_page(c: Composition, draws: int, path: str, params: Params) -> None:
    """Point 14: the page of one robot type, its kg by material and its kg by element, each with its 95 % interval."""
    materials = [(name, c.column('materials', name)) for name in c.tables['materials'][0]]
    elements = page_elements(c)
    notes = [line for note in page_notes(c) for line in schemas.wrap('• ' + note, 200)]
    total = c.column('total', 'Total')
    materials_kg = float(np.median(total - c.column('materials', NOT_ALLOCATED)))
    followed = float(np.median(c.in_elements.sum(axis=1)))
    top = 1.15
    height = top + 0.85 + ROW * max(len(materials), len(elements)) + 0.55 + len(notes) * schemas.LINE + 0.4
    figure, page = schemas.new_page(PAGE_WIDTH, height)
    page.text(MARGIN, 0.35, f'Robot type {c.number}: {c.title}', fontsize=15, va='top')   # regular since 2026-11-13
    page.text(MARGIN, 0.75, f'What one robot is made of, from {draws:,} model runs. Each bar is the median of the runs '
                            'that hold it, with its 95 % interval; Held in: the share of the runs that hold it, where '
                            'not all.', fontsize=10, color=MUTED, va='top')
    below = interval_chart(figure, page, height, MARGIN, top, 'By material',
                           f"All of the robot's {mass(float(np.median(total)))} kg at the median: its materials, and "
                           'Not allocated',
                           materials)
    below = max(below, interval_chart(figure, page, height, MARGIN + LABEL + CHART + NUMBERS + GAP, top,
                                      'By element', f'The elements of interest: {mass(followed)} kg '
                                                    f'of the {mass(materials_kg)} kg of materials at the median',
                                      elements))
    schemas.write(page, MARGIN, below, notes, size=9)
    schemas.save(figure, path, params.output.dpi)


# ------------------------------------------------------------------------------------------------------
# The pages of a robot type taken apart (type 1's since 2026-10-29, type 2's since 2026-10-30): each element as its
# total in one robot
# ------------------------------------------------------------------------------------------------------
# Matthias, 2026-10-28: "I want to see the overall information on the element as total. Show me the distributions",
# "Do it for all the robots which are in type 1. Do the code and the figure!!", on the preview "Yes, code it in 02",
# and "Do not repeat the comments on all slides have it on a separate one. It uses much to much space". Pages of a
# screen's shape, 16 × 9 inches, text 14 points and up (about 23 pixels fit to a 1920 × 1080 screen), as approved for
# 04's pages ("Pages right"): a page of notes first, then the elements, nine a page.

APART_PAGE = (16, 9)
APART_TEXT, APART_LABEL, APART_TITLE, APART_HEADING = 14, 15, 16, 20   # points
APART_ACROSS, APART_DOWN = 3, 3           # element panels on a page
APART_BINS = 70                              # the bars of a distribution, as in RAWCLICDataCenters' figures
# Where a distribution panel's axis ends: this percentile of its draws (Matthias, 2026-11-01: "The distribution figures
# show the distribution pressed to the left side. You give away have of the x axis", then "Yes, build it"; V124: up to
# the largest draw, type 2's 97.5th percentile sat at a third of the axis, at the 99.5th it sits at two thirds). The
# draws beyond are not drawn; the panel says how many and the largest (beyond_words).
AXIS_END = 99.5
# Where a panel's mass axis is logarithmic: where the median of its draws would lie in the first LOG_BELOW (5 %) of its
# linear axis, from its smallest draw to its end, the draws spread over orders of magnitude (Matthias, 2026-11-05:
# "Titanium in sensors the x axis is not good, You know this", then "Yes, build it"; EVIDENCE.md E36, V186: type 2's
# sensors' titanium, 96 % of its draws 0.1 to 10 mg from the cameras, 4 % 50 to 470 mg from the PZT of ultrasonic
# sensors, its median at 0.3 % of a linear axis). In the 2,000-draw run of V186 four panels of 412: the sensors'
# titanium of types 2 and 3, on 02's pages and on 03's; the next median sat at 7 % of its axis.
LOG_BELOW = 0.05
# What the notes pages of 02 and 03 say of it.
LOG_WORDS = (f"Where a panel's median would lie in the first {100 * LOG_BELOW:g} % of its axis, its runs spread over "
             "orders of magnitude, its mass axis is logarithmic (0.1, 0.3, 1, 3 …), its bars evenly spaced on it.")
APART_BAR = '#4477AA'                        # Paul Tol's bright blue, as published
APART_INK = '#222222'                        # lines and numbers
APART_NOTE_WIDTH = 140                       # characters in a line of a notes page
# The lines of a notes page, its blank lines counted: from the top of its text (0.83 of the page's height from the
# foot) to 0.35 inches above the foot, one line of 14-point text at a spacing of 1.3 taking 0.269 inches, as measured;
# tests/test_parts_taken_apart.py fails where a text runs off its page.
NOTES_LINES = 26
# The elements of the other materials (boards, sensors, magnets) in plain words, beside those of the recipes.
ELEMENT_NAMES.update({'Ag': 'Silver', 'As': 'Arsenic', 'Au': 'Gold', 'Br': 'Bromine', 'Dy': 'Dysprosium',
                      'Ga': 'Gallium', 'In': 'Indium', 'Nb': 'Niobium', 'Nd': 'Neodymium', 'Pd': 'Palladium',
                      'Pr': 'Praseodymium', 'Ta': 'Tantalum', 'Tb': 'Terbium', 'W': 'Tungsten',
                      # An element of interest no robot holds so far, but the data centres do (05, 2026-11-08).
                      'Sr': 'Strontium'})


def axis_end(values: np.ndarray) -> float:
    """Where a distribution panel's axis ends: the AXIS_END-th percentile of its draws, or its largest draw where that
    percentile is its smallest (draws that are nearly all the same)."""
    end = float(np.percentile(values, AXIS_END))
    return end if end > float(values.min()) else float(values.max())


def logarithmic(values: np.ndarray, end: float) -> bool:
    """Whether a distribution panel's mass axis is logarithmic (LOG_BELOW, E36): where the median of its draws would
    lie in the first LOG_BELOW of its linear axis, from its smallest draw to its axis's `end`, the draws spread over
    orders of magnitude, most of them pressed into its first bars. Only draws above 0 (a logarithmic axis has no place
    for 0; a panel's draws are those that hold it)."""
    low = float(values.min())
    if low <= 0 or end <= low:
        return False
    return (float(np.median(values)) - low) / (end - low) < LOG_BELOW


def mass_ticks(axes, count: int) -> None:
    """The ticks of a panel's mass axis in plain numbers (panel_number): about `count` on a linear axis; on a
    logarithmic one (logarithmic) at 1 and 3 of each power of ten (0.1, 0.3, 1, 3, 10 …), no powers of ten written."""
    if axes.get_xscale() == 'log':
        # 1 and 3 of each power of ten; over more than three powers of ten the powers alone, whose numbers would else
        # lie on one another ('0.003' on '0.01', FigureTests' rule overlap, 2026-11-13)
        low, high = axes.get_xlim()
        wide = low > 0 and high / low > 1e3
        axes.xaxis.set_major_locator(plt.LogLocator(base=10, subs=(1.0,) if wide else (1.0, 3.0)))
        axes.xaxis.set_minor_locator(plt.NullLocator())
    else:
        # one tick fewer than asked: at 14 points '2.5' lay on '0' on a narrow panel (overlap, 2026-11-13)
        axes.xaxis.set_major_locator(plt.MaxNLocator(max(count - 1, 3)))
    axes.xaxis.set_major_formatter(plt.FuncFormatter(panel_number))


def beyond_words(values: np.ndarray, end: float, unit: str) -> str:
    """What a panel says of the draws beyond its axis's end, in the panel's unit: '0.5 % beyond the axis, up to 13 kg';
    '' where none lies beyond. Their share is of all the panel's draws."""
    over = values > end
    if not over.any():
        return ''
    return f'{panel_number(100 * over.mean())} % beyond the axis, up to {panel_number(float(values.max()))}\u00a0{unit}'


def text_width(text: str) -> float:
    """The width of `text` written at APART_TEXT points, in points, from the outlines of the page's font (matplotlib's
    TextPath): to set columns of numbers apart by what they hold (ridge_panel, E38)."""
    return float(TextPath((0, 0), text, size=APART_TEXT).get_extents().width)


def panel_unit(values_kg: np.ndarray) -> tuple:
    """The unit a panel is drawn in, by the mean of its draws: kg from 1 kg, g from 1 g, mg below. Returns the kg in
    one unit and its symbol."""
    typical = float(np.mean(np.abs(values_kg))) if values_kg.size else 0.0
    if typical >= 1.0:
        return 1.0, 'kg'
    if typical >= 1e-3:
        return 1e-3, 'g'
    return 1e-6, 'mg'


def panel_number(x: float, _pos=None) -> str:
    """A number as the figures write it (RAWCLICDataCenters' rule): whole from 10, one decimal from 1, two significant
    digits below 1, written out (4000, never 4k; 0.000095, never 9.5e-05). (`_pos` lets matplotlib use it as a tick
    formatter.)"""
    if abs(x) >= 10:
        return f'{x:.0f}'
    if abs(x) >= 1:
        return f'{x:.1f}'.rstrip('0').rstrip('.')
    return np.format_float_positional(float(f'{x:.2g}'), trim='-')


# ------------------------------------------------------------------------------------------------------------------------
# The words and marks every figure of 02 to 05 shares, as the data-centre pages (FigureTests' rules 1 to 11; Matthias,
# 2026-11-12: "yes, 1 to 11"; 2026-11-13: "test all the figures", "Yes, 1 to 7", the choices as recommended): the model's
# draws are "runs"; the statistic is the median, never the mean ("Not mean, but median", 2026-11-10); every mark has its
# sample in one legend; the foot at most three sentences. One copy: 03, 04 and 05 call these.
# ------------------------------------------------------------------------------------------------------------------------

MEDIAN_MARK = {'color': APART_INK, 'linewidth': 1.8}                        # the median of a distribution: solid
BOUND_MARK = {'color': APART_INK, 'linewidth': 1.2, 'linestyle': '--'}      # its 95 % interval: dashed (as the data centres')


def share_text(share: float) -> str:
    """A share of the runs as the figures write it: whole per cent, below 1 % with one decimal ('0.6 %'), so that what
    some runs hold is never written '0 %' (the choice of 2026-11-13: "held in 0.6 %"; the data centres' share_text)."""
    percent = 100.0 * share
    return f'{percent:.1f} %' if percent < 1 else f'{percent:.0f} %'


def held_words(share: float, short: bool = False) -> str:
    """'' where every run holds it (99.5 % and more); else ' (in 56 % of the runs)', or ' (56 %)' short."""
    if share >= 0.995:
        return ''
    return f' ({share_text(share)})' if short else f' (in {share_text(share)} of the runs)'


def held_share(share: float) -> str:
    """The column 'Held in' of a list or a page of numbers: 'all runs', or the share ('56 %', '0.6 %')."""
    return 'all runs' if share >= 0.995 else share_text(share)


def distribution_handles(runs: int) -> list:
    """The legend samples of a distribution's marks: its median (solid) and its 95 % interval (dashed), named in plain
    words, as the data centres' distribution_handles."""
    return [plt.Line2D([], [], label=f'Median of {runs:,} model runs', **MEDIAN_MARK),
            plt.Line2D([], [], label='95 % interval', **BOUND_MARK)]


def readable(colour, background='white', ratio: float = 4.5) -> str:
    """A colour for a text that belongs to a line of `colour`: the colour itself where it stands out from `background`
    by at least `ratio` (WCAG AA, FigureTests' rule text_contrast), else the same hue darkened in steps of 5 % towards
    black until it does (a share written beside a light red line stood out 3.1 : 1, 2026-11-13). Returns a hex colour."""
    from matplotlib.colors import to_hex, to_rgb
    def luminance(rgb):
        lin = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in rgb]
        return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]
    back = luminance(to_rgb(background))
    rgb = to_rgb(colour)
    for step in range(21):
        shade = tuple(x * (1 - 0.05 * step) for x in rgb)
        y = luminance(shade)
        if (max(y, back) + 0.05) / (min(y, back) + 0.05) >= ratio:
            return to_hex(shade)
    return '#000000'


def foot_text(sentences: list, width: int) -> str:
    """The text at the foot of a figure (rule 6: at most three sentences, no lists): the sentences given that are not
    empty, each ending with a full stop, wrapped to `width` characters a line (the data centres' foot_text)."""
    parts = [x.strip() for x in sentences if x and x.strip()]
    text = ' '.join(x if x.endswith(('.', '!', '?')) else x + '.' for x in parts)
    return '\n'.join(textwrap.wrap(text, width))


def element_panel(axes, kg: np.ndarray, title: str, first_in_row: bool) -> None:
    """One element (or, on the material pages, one material) in one robot over the runs, under `title`: its
    histogram (the height the share of the runs), the median a solid line and the 95 % interval dashed (centre_lines;
    Matthias, 2026-11-10: "Not mean, but median"; the samples in the page's legend); its own scale and unit. Where it is
    0 in some runs (a robot or a version without it), the panel shows the runs that hold it, their median and 95 %
    interval, and its numbers say in what share of all the runs it is held (Matthias, 2026-10-29, on the materials: "If
    it is just a bit and a large 0 then show me the distribution"; on the elements: "I told you I want to see the
    distribution not just the 0 value for vanadium and lead")."""
    share = float((kg > 0).mean())
    held_in = share if share < 0.995 else 1.0
    if share < 1:                                     # only the runs that hold it ("A 0 is not part of a distribution")
        kg = kg[kg > 0]
    per, unit = panel_unit(kg)
    values = kg / per
    axes.set_title(title, fontsize=APART_TITLE, loc='left')
    # Its 70 bars from the smallest draw to the axis's end (AXIS_END), each the share of all the panel's draws; the
    # draws beyond the end not drawn, said above the panel. Its draws spread over orders of magnitude (LOG_BELOW): the
    # bars even on a logarithmic axis.
    end = axis_end(values)
    if logarithmic(values, end):
        axes.set_xscale('log')
        edges = np.geomspace(float(values.min()), end, APART_BINS + 1)
    else:
        edges = np.histogram_bin_edges(values[values <= end], bins=APART_BINS, range=(float(values.min()), end))
    counts, edges = np.histogram(values[values <= end], bins=edges)
    axes.bar(edges[:-1], counts / values.size, width=np.diff(edges), align='edge', color=APART_BAR,
             edgecolor='none')
    # The bars up to about nine tenths of the panel (Matthias, 2026-10-28: "can you better adust the hight. we loose
    # quite a bit of space. Not full but much better").
    axes.set_ylim(0, (counts / values.size).max() * 1.1)
    centre_lines(axes, values, held_in, end, unit, title)
    panel_axes(axes, unit, first_in_row)


def centre_lines(axes, values: np.ndarray, held_in: float, end: float, unit: str, title: str) -> None:
    """A panel's median (a solid line, MEDIAN_MARK) and the range where 95 of 100 of its runs lie (two dashed lines,
    BOUND_MARK) of `values` (in its unit), their samples in the page's legend (distribution_handles; Matthias,
    2026-11-10: "Not mean, but median"; the rules of 2026-11-12). Its numbers are kept for the page of numbers that
    follows its page (Matthias, 2026-11-05: "Do we really need all this text in the figure. It might be better to have it
    separate", "Yes"; EVIDENCE.md E34), none written on the panel: its title, the share of the runs that hold it
    (`held_in`, 1 where all do), the median, the middle half (25 % to 75 %), the 95 % interval and what lies beyond the
    axis's `end` (panel_rows)."""
    median = float(np.median(values))
    p25, p75, low, high = (float(b) for b in np.percentile(values, [25, 75, 2.5, 97.5]))
    axes.axvline(median, **MEDIAN_MARK)
    for bound in (low, high):
        axes.axvline(bound, **BOUND_MARK)
    axes.panel_numbers = (title.replace('\n', ' '), held_in, median, p25, p75, low, high, unit,
                          beyond_words(values, end, unit))


def panel_rows(figure) -> list:
    """The rows of a page's numbers (E34), one per panel that has them, in the order of its panels: its title, the
    share of the runs that hold it ('all runs' where all do), the median, the middle half of the runs (50 %), where 95
    of 100 lie, and the runs beyond the axis ('–' where none), each with its unit."""
    rows = []
    for axes in figure.axes:
        numbers = getattr(axes, 'panel_numbers', None)
        if numbers is None:
            continue
        title, held_in, median, p25, p75, low, high, unit, beyond = numbers
        rows.append([title, held_share(held_in), f'{panel_number(median)}\u00a0{unit}',
                     f'{panel_number(p25)} to {panel_number(p75)}\u00a0{unit}',
                     f'{panel_number(low)} to {panel_number(high)}\u00a0{unit}',
                     beyond.replace(' beyond the axis', '') if beyond else '–'])
    return rows


# The page of numbers (E34): its columns, their places across the page and their widths before a cell wraps.
NUMBERS_HEAD = ('Panel', 'Held in', 'Median', '50 % interval', '95 % interval', 'Beyond the axis')
NUMBERS_X, NUMBERS_WRAP = (0.03, 0.36, 0.47, 0.58, 0.69, 0.84), (34, 12, 12, 12, 16, 22)


# Between a panel's axis title and the title of the panel below it, in matplotlib's units of the font size (10 points):
# 14 points, one line of the pages' text (FigureTests' rule text_gap; 0.4, 4 points, until 2026-11-13, when Matthias found
# the texts "much to close").
PANEL_GAP = 1.4


def numbers_page(name: str, figure) -> tuple:
    """The page of the numbers of a page of panels (E34), as (file name `name`, figure): its title the panels' page's
    with ': its numbers', a row per panel (panel_rows), each cell wrapped in its column."""
    heading = (figure._suptitle.get_text() if figure._suptitle else '') + ': its numbers'
    page = plt.figure(figsize=APART_PAGE)
    page.suptitle(textwrap.fill(heading, 110), fontsize=APART_HEADING, y=0.985)
    for x, words in zip(NUMBERS_X, NUMBERS_HEAD):
        page.text(x, 0.875, words, fontsize=APART_TEXT, va='top')   # 0.90 until 2026-11-13 (text_gap)
    y = TABLE_TOP
    for row in panel_rows(figure):
        cells = [textwrap.fill(cell, width) for cell, width in zip(row, NUMBERS_WRAP)]
        page.add_artist(plt.Line2D([0.03, 0.97], [y + 0.012, y + 0.012], color=GRID, linewidth=1))
        for x, cell in zip(NUMBERS_X, cells):
            page.text(x, y, cell, fontsize=APART_TEXT, va='top', linespacing=1.25)
        y -= ROW_GAP + max(cell.count('\n') + 1 for cell in cells) * LINE_HEIGHT
    return name, page


def with_numbers(pages: list, prefix: str, first: int = 1) -> list:
    """Each page of panels (`pages`: (file name, figure)) followed by the page of its numbers (E34),
    '<prefix>_numbers_<k>.png', k counted from `first`."""
    out = []
    for k, (name, figure) in enumerate(pages, first):
        out += [(name, figure), numbers_page(f'{prefix}_numbers_{k}.png', figure)]
    return out


# Points: below the mass axis to its numbers, above the panel to its title; more than half the height of a 14-point
# number (about 8 points), so that the share axis's first and last numbers stand clear of them (matplotlib's 3.5 and 6).
# SHARE_PAD: left of the share axis to its numbers (matplotlib's 3.5 until 2026-11-13: at 2,000 runs the top number,
# '0.06', fell on the panel's top and stood 7 points from the left-aligned title above; half a line is 8).
TICK_PAD, TITLE_PAD, SHARE_PAD = 13.0, 10.0, 6.0   # TICK_PAD 9 until Luciole (2026-11-13), whose taller lines needed 13


def panel_axes(axes, unit: str, first_in_row: bool) -> None:
    """The axes of a panel of the element and material pages: mass in one robot in its unit, the share of the draws
    on the first of a row, plain numbers (mass_ticks, also on a logarithmic mass axis), hairlines on the mass. The mass
    axis's numbers TICK_PAD below the axis, the share axis's SHARE_PAD left of it and the panel's title TITLE_PAD above
    it, so that neither stands beside the share axis's first or last number (FigureTests' text_gap, 2026-11-13: the "0"
    of the shares beside the first mass, "0.8", 2 to 7 points apart; at 2,000 runs the top share, "0.06", 7 points from
    a two-line title)."""
    mass_ticks(axes, 5)
    axes.yaxis.set_major_locator(plt.MaxNLocator(3))
    axes.yaxis.set_major_formatter(plt.FuncFormatter(panel_number))
    axes.tick_params(labelsize=APART_TEXT)
    axes.tick_params(axis='x', pad=TICK_PAD)
    axes.tick_params(axis='y', pad=SHARE_PAD)
    axes.set_title('', pad=TITLE_PAD)              # the offset of every title of the panel, its left one too
    axes.set_xlabel(f'mass in one robot ({unit})', fontsize=APART_LABEL)
    if first_in_row:
        axes.set_ylabel('share of the runs', fontsize=APART_LABEL)
    axes.grid(axis='x', alpha=0.3)
    for side in ('top', 'right'):
        axes.spines[side].set_visible(False)


def by_material_panel(axes, parts: dict, title: str, first_in_row: bool, fixed: tuple = ()) -> tuple:
    """One element of the element pages, split by the material it comes from (EVIDENCE.md E19 point 7, as
    RAWCLICDataCenters 05; the preview of type 5, "Yes, build them", 2026-11-02): the histogram of its total in one
    robot (stacked_bars, the material with the smaller mean lower, MATERIAL_COLOURS), its median, mean and 95 % as on
    the element panel (centre_lines); where more than one material gives it, each material's mean over the draws that
    hold the element written in the panel, top right, the largest first, a material of `fixed` marked '(fixed)': its
    share of the element fixed in the alloy (E25). Returns (the top of its bars, the lines of those means, the materials
    drawn), for make_room and the page's legend."""
    axes.set_title(title, fontsize=APART_TITLE, loc='left')
    # The materials `fixed` (E25) as one part of the bars, FIXED_PART; each of them in the means, marked.
    whole = {m: kg for m, kg in parts.items() if m not in fixed}
    if fixed:
        whole[FIXED_PART] = sum(parts[m] for m in fixed)
    bars = stacked_bars(axes, whole, MATERIAL_COLOURS)
    centre_lines(axes, bars.values, bars.held_in, bars.end, bars.unit, title)
    panel_axes(axes, bars.unit, first_in_row)
    return bars.top, 0, bars.drawn


def group_panel(axes, groups: dict, title: str, first_in_row: bool) -> tuple:
    """One element in one robot split by the four groups of how a robot is taken apart (Matthias, 2026-11-08: "Why I
    am not allowed to know what the different components contribut already at this level", "Yes, add 1 to 3"): the
    histogram of its total over the draws (stacked_bars, the group with the smaller mean lower, 01's GROUP_COLOURS), its
    median, mean and 95 % (centre_lines), as the element pages' panels. Returns (the top of its bars, 0, the groups
    drawn), as by_material_panel."""
    axes.set_title(title, fontsize=APART_TITLE, loc='left')
    bars = stacked_bars(axes, groups, schemas.GROUP_COLOURS)
    centre_lines(axes, bars.values, bars.held_in, bars.end, bars.unit, title)
    panel_axes(axes, bars.unit, first_in_row)
    return bars.top, 0, bars.drawn


def part_rows(kg: dict, unit=None) -> list:
    """The rows of a list part by part of how a robot is taken apart (Matthias, 2026-11-08: "I want a detailed list of
    the component, so it is easy to understand and establish a recycling to know how to take it apart!!!"): `kg`
    {(what the row is of, part): its draws}, in the order given; a row for each that holds it in a draw at least: what it
    is of, its group, its part, the share of the runs that hold it (share_text: never '0 %' for what some runs hold),
    its median, the middle half (25 % to 75 %) and where 95 of 100 lie, over those runs ("A 0 is not part of a
    distribution"), in its own unit (`unit`: a function of the runs, panel_unit where none). One copy: 02's, 03's and
    04's lists."""
    unit = unit or panel_unit
    rows = []
    for (what, part), values in kg.items():
        values = np.asarray(values, dtype=np.float64)
        above = values[values > 0]
        if not above.size:
            continue
        per, symbol = unit(above)
        low, p25, median, p75, high = np.percentile(above / per, (2.5, 25, 50, 75, 97.5))
        rows.append([what, schemas.TAKEN_GROUP[part], part, held_share(above.size / values.size),
                     f'{panel_number(median)}\u00a0{symbol}',
                     f'{panel_number(p25)} to {panel_number(p75)}\u00a0{symbol}',
                     f'{panel_number(low)} to {panel_number(high)}\u00a0{symbol}'])
    return rows


# A list page part by part (part_list_pages): its columns, where each starts across the page and how wide each wraps;
# its rows fill a page down to TABLE_BOTTOM, the next on a page of its own.
PART_LIST_HEAD = ('Element', 'Group', 'Part', 'Held in', 'Median', '50 % interval', '95 % interval')
PART_LIST_X, PART_LIST_WRAP = (0.03, 0.20, 0.33, 0.53, 0.64, 0.75, 0.86), (20, 14, 22, 11, 11, 11, 16)


def part_list_pages(name: str, heading: str, rows: list, first_head: str = 'Element') -> list:
    """The list part by part (part_rows) on pages of 02's form, as [(file name, figure)]: '<name>_<k>.png', each page
    filled with rows down to TABLE_BOTTOM (a row as tall as its most wrapped cell), the heading with '(k of n)' where
    more than one; the first column headed `first_head`."""
    wrapped = [[textwrap.fill(cell, width) for cell, width in zip(row, PART_LIST_WRAP)] for row in rows]
    pages, page, used = [], [], 0.0
    for cells in wrapped:
        tall = ROW_GAP + max(cell.count('\n') + 1 for cell in cells) * LINE_HEIGHT
        if page and used + tall > TABLE_TOP - TABLE_BOTTOM:
            pages.append(page)
            page, used = [], 0.0
        page.append((cells, tall))
        used += tall
    pages.append(page)
    out = []
    for k, page_rows in enumerate(pages, 1):
        figure = plt.figure(figsize=APART_PAGE)
        title = heading + (f' ({k} of {len(pages)})' if len(pages) > 1 else '')
        figure.suptitle(textwrap.fill(title, 110), fontsize=APART_HEADING, y=0.985)
        for x, words in zip(PART_LIST_X, (first_head,) + PART_LIST_HEAD[1:]):
            figure.text(x, 0.90, words, fontsize=APART_TEXT, va='top')
        y = TABLE_TOP
        for cells, tall in page_rows:
            figure.add_artist(plt.Line2D([0.03, 0.97], [y + 0.012, y + 0.012], color=GRID, linewidth=1))
            for x, cell in zip(PART_LIST_X, cells):
                figure.text(x, y, cell, fontsize=APART_TEXT, va='top', linespacing=1.25)
            y -= tall
        out.append((f'{name}_{k}.png', figure))
    return out


def group_pages(c: Composition, d: Draws) -> list:
    """A robot type's elements in one robot, each split by the four groups of how a robot is taken apart (group_panel),
    six a page, one legend of the groups drawn, each page followed by the page of its numbers; then the list of every
    element in each part that holds it (part_rows, part_list_pages): '<name>_groups_<k>.png', '<name>_parts_<k>.png'."""
    shown = [e for e in c.tables['elements'][0] if held(c.column('elements', e))]
    per_page = APART_ACROSS * ELEMENT_DOWN
    pages = [shown[k:k + per_page] for k in range(0, len(shown), per_page)]
    out = []
    for p, page in enumerate(pages, 1):
        figure, axes = plt.subplots(ELEMENT_DOWN, APART_ACROSS, figsize=APART_PAGE, squeeze=False)
        panels = []
        for k, symbol in enumerate(page):
            here = axes[k // APART_ACROSS, k % APART_ACROSS]
            groups = {g: sum((kg for (_, part, e), kg in d.taken.items()
                              if e == symbol and schemas.TAKEN_GROUP[part] == g), np.zeros(d.n))
                      for g in schemas.TAKEN_APART}
            panels.append((here, group_panel(here, groups, element_label(symbol), k % APART_ACROSS == 0)))
        for spare in axes.flatten()[len(page):]:
            spare.axis('off')
        drawn = {g for _, (_, _, groups) in panels for g in groups}
        shown_groups = [g for g in schemas.TAKEN_APART if g in drawn]
        figure.suptitle(f'{lead(d)}: each element in one robot, by group ({p} of {len(pages)})',
                        fontsize=APART_HEADING, y=0.985)
        # one legend: the groups drawn, the median and the 95 % interval (rule 3 of 2026-11-12: every mark its sample)
        handles = [Patch(color=schemas.GROUP_COLOURS[g], label=g) for g in shown_groups] + distribution_handles(d.n)
        figure.legend(handles=handles, loc='upper center', bbox_to_anchor=(0.5, 0.955), ncol=len(handles),
                      frameon=False, fontsize=APART_TEXT)
        figure.tight_layout(rect=(0, 0, 1, 0.95 - LEGEND_ROW), h_pad=PANEL_GAP, w_pad=2.5)
        make_room(figure, panels)
        out.append((f'{c.name}_groups_{p}.png', figure))
    by_part = {(element_label(e), part): sum((kg for (_, x, y), kg in d.taken.items() if x == part and y == e),
                                             np.zeros(d.n))
               for e in shown for part in schemas.TAKEN_PARTS}
    lists = part_list_pages(f'{c.name}_parts', f'{lead(d)}: each element in one robot, part by part',
                            part_rows(by_part))
    return out, lists


def alloy_place(axes, symbol: str, drawn: dict, title: str) -> None:
    """The place of a light alloy's metal with no panel (E33): its alloy held in fewer than 2.5 % of the draws or not
    at all (type 4's titanium: its sensors' only), the place naming the alloy."""
    total = sum(drawn.values(), 0)
    axes.set_xticks([])   # no tick labels left on an empty place (they would count as text of the page)
    axes.set_yticks([])
    axes.axis('off')
    axes.set_title(title, fontsize=APART_TITLE, loc='left')
    words = f'{ALLOY_OF[symbol]}: ' + not_drawn_words(np.asarray(total) if np.ndim(total) else np.zeros(1))
    axes.text(0, 0.85, words, transform=axes.transAxes, fontsize=APART_TEXT, va='top', color=APART_INK)


def material_medians(d: Draws, symbol: str) -> list:
    """One element's median in one robot by the material it comes from, over the runs that hold the element, the
    largest first, a material whose copper is fixed in it marked '(fixed)' (E25): [(material, kg, the share of the
    runs in which it holds the element)]. The median, not the mean (Matthias, 2026-11-10: "Not mean, but median";
    until 2026-11-13 the mean), over the runs in which the material holds it."""
    parts = {**materials_of(d, symbol), **{f'{m} (fixed)': kg for (m, e), kg in (d.fixed or {}).items()
                                           if e == symbol and kg.any()}}
    # Each material over the runs in which it holds the element, with the share of all runs that do ("A 0 is not part
    # of a distribution": over the runs that hold the element, a material in fewer than half of them had a median of
    # 0, written "0 mg", found 2026-11-13)
    return sorted(((m, float(np.median(kg[kg > 0])), float((kg > 0).mean())) for m, kg in parts.items() if held(kg)),
                  key=lambda x: -x[1])


def medians_pages(c: Composition, d: Draws) -> list:
    """The medians of the element pages, on pages of their own (Matthias, 2026-11-02: "The figure is first and not the
    text Tex can go to other places"): each element shown, the materials it comes from with its median from each."""
    shown = [e for e in c.tables['elements'][0] if held(c.column('elements', e))]
    rows = [(element_label(e) + (', in all' if any(x == e for _, x in (d.fixed or {})) else ''), median_words(d, e))
            for e in shown]
    cells_of = [[textwrap.fill(text, width) for text, width in zip(row, MEANS_WRAP)] for row in rows]
    pages, page, y = [], [], TABLE_TOP
    for cells in cells_of:
        height = ROW_GAP + max(cell.count('\n') + 1 for cell in cells) * LINE_HEIGHT
        if page and y - height < TABLE_BOTTOM:
            pages.append(page)
            page, y = [], TABLE_TOP
        page.append(cells)
        y -= height
    if page:
        pages.append(page)
    out = []
    for p, page in enumerate(pages, 1):
        figure = plt.figure(figsize=APART_PAGE)
        figure.suptitle(f'{lead(d)}: each element in one robot, its median by the material it comes from ({p} of '
                        f'{len(pages)})', fontsize=APART_HEADING, y=0.985)
        for x, words in zip(MEANS_X, MEANS_HEAD):
            figure.text(x, 0.90, words, fontsize=APART_TEXT, va='top')
        y = TABLE_TOP
        for cells in page:
            figure.add_artist(plt.Line2D([0.03, 0.97], [y + 0.012, y + 0.012], color=GRID, linewidth=1))
            for x, cell in zip(MEANS_X, cells):
                figure.text(x, y, cell, fontsize=APART_TEXT, va='top', linespacing=1.25)
            y -= ROW_GAP + max(cell.count('\n') + 1 for cell in cells) * LINE_HEIGHT
        out.append((f'{c.name}_medians_{p}.png', figure))
    return out


def median_words(d: Draws, symbol: str) -> str:
    """One element's medians by the material it comes from, '<material> <median>' each, '; ' between; the components of
    the electronics (E32) together, ', ' between them, the electronics' name once after them in brackets ('Circuit
    boards 65 mg, cameras 1 mg (boards and components)', E38), at the place of the first."""
    words, parts, at = [], [], None
    for m, kg, share in material_medians(d, symbol):
        held_in = held_words(share, short=True)                       # its share where not every run holds it
        if m.startswith(ELECTRONICS + ': '):
            at = len(words) if at is None else at
            parts.append(f'{m[len(ELECTRONICS) + 2:]} {mass_in_unit(kg)}{held_in}')
        else:
            words.append(f'{element_page_name(m)} {mass_in_unit(kg)}{held_in}')   # copper and nickel by what they are
    if parts:
        listed = ', '.join(parts)
        words.insert(at, f'{listed[0].upper()}{listed[1:]} ({ELECTRONICS.lower()})')
    return '; '.join(words)


# The second column wrapped at 100 characters since 2026-11-13 (110 before: a row of copper's materials ran past the
# page's right edge at the 300 dpi the pages are saved with; 100 characters of 14-point text are about 10 of the 10.7
# inches the column has).
MEANS_X, MEANS_WRAP = (0.03, 0.30), (30, 100)
MEANS_HEAD = ('Element', 'By the material it comes from: its median in one robot, over the runs that hold the '
                         'element')


def texts_over_data(figure) -> list:
    """The rule of every chart (Matthias, 2026-11-02: "Text over the figures. Build a rule, which prevents this. The
    figure is first and not the text Tex can go to other places"): no text inside a chart (an axes whose axis is drawn)
    lies over its data, its bars and its lines. Returns the texts that do, as '<title>: <text>'; [] where none."""
    figure.canvas.draw()
    renderer = figure.canvas.get_renderer()
    found = []
    for axes in figure.axes:
        if not axes.axison:
            continue
        data = [p.get_window_extent(renderer) for p in axes.patches if p.get_visible()]
        data += [line.get_window_extent(renderer) for line in axes.lines if line.get_visible()]
        data = [b for b in data if b.width > 0.5 or b.height > 0.5]
        for text in axes.texts:
            if not text.get_visible() or not text.get_text().strip():
                continue
            box = text.get_window_extent(renderer)
            if any(min(box.x1, b.x1) - max(box.x0, b.x0) > 1 and min(box.y1, b.y1) - max(box.y0, b.y0) > 1
                   for b in data):
                found.append(f"{axes.get_title(loc='left')}: {text.get_text().splitlines()[0]}")
    return found


def mass_in_unit(kg: float) -> str:
    """One mass in its own plain unit: '3.1 kg', '453 g', '125 mg'."""
    per, unit = panel_unit(np.array([kg]))
    return f'{panel_number(kg / per)}\u00a0{unit}'


def make_room(figure, panels: list) -> None:
    """After a page's layout, each panel's bars below its materials' means (`panels`: (axes, (top of its bars, lines
    of means, …))): the bars end below the means' lines, at 1.15 times the text each, or at 0.95 of the panel."""
    height = figure.get_size_inches()[1] * 72   # points
    for axes, (top, lines, _) in panels:
        room = (lines * APART_TEXT * 1.15 * 1.2 + 6) / (axes.get_position().height * height) if lines else 0.05
        axes.set_ylim(0, top / max(1 - room, 0.3))


def lead(d: Draws) -> str:
    """The first words of a page's title: 'Robot type 1, all its 31 robots', or, while not all of a type's robots
    with a mass are taken apart, 'Robot type 2, 5 of its 96 robots' (a robot without a mass is not in the evaluation
    and not counted, since 2026-10-30: E10.1 point 4)."""
    drawn, listed = len(d.register), max(d.listed, len(d.register))
    return f'Robot type {d.robot_type}, ' + (f'all its {drawn} robots' if drawn >= listed else
                                             f'{drawn} of its {listed} robots')


def outlier_words(outliers: list, params: Params, types: bool = False) -> str:
    """The sentence of the notes pages naming the robots not drawn as outliers (`outliers`: 01's outlier_robots), each
    its number, its name as taken apart, its mass at the mode and the reason of the setting composition.outliers, and
    with `types` its robot types (03's notes); '' where there is none. Matthias, 2026-11-04: "So kick it out of the
    statistics and just hae it mentioned or in as the outlier"; 2026-11-05, "Yes, 3 to 5" (EVIDENCE.md E30 point 4: on
    the notes pages of 02 and 03, not a page of its own)."""
    reasons = dict(params.composition.outliers)
    said = []
    for r in outliers:
        name = r.taken_apart if r.taken_apart and len(schemas.versions(r.taken_apart)) == 1 else r.name
        kinds = sorted(r.types)
        said.append(f'{r.number} {name}' + (f', {r.mass[1]:,g} kg' if r.mass[1] is not None else '')
                    + f', {reasons[r.number]}'
                    + (f" (robot type{'s' if len(kinds) > 1 else ''} "
                       f"{', '.join(map(str, kinds[:-1])) + ' and ' if len(kinds) > 1 else ''}{kinds[-1]})"
                       if types else ''))
    if not said:
        return ''
    return ('Not drawn, an outlier: ' if len(said) == 1 else 'Not drawn, outliers: ') + '; '.join(said) + '.'


def taken_apart_notes(c: Composition, d: Draws, left_out: list, params: Params, later: list | None = None,
                      outliers: list | None = None) -> list:
    """The notes page's paragraphs: how to read the element, material and alloys pages, what is drawn, which
    elements are counted and which materials stay materials (EVIDENCE.md E19); `later` the robots of the type not yet
    taken apart (the type's draws then from the workbook); `outliers` its robots not drawn, outliers (E30 point 4)."""
    rows = {r['Name']: r for r in summary(c) if r['Kind'] == 'Material'}
    # Each with its median over the runs that hold it, and their share where not all (CLAUDE.md §7).
    missing = [f"{name} (median {panel_number(rows[name]['Median (kg)'])} kg"
               + (f", held in {share_text(rows[name]['Held in (% of the draws)'] / 100)} of the runs"
                  if rows[name]['Held in (% of the draws)'] < 99.5 else '') + ')' for name in rows
               if rows[name]['In the elements'] == 'No' and name != NOT_ALLOCATED]
    partly = [name for name in rows if rows[name]['In the elements'] == 'Partly']
    estimates = [f"{what}: {', '.join(robots)}" for what, robots in (d.on_estimates or {}).items()]
    notes = [
        'The element pages: the bars show how often each mass of one element in one robot came out in the model '
        'runs, the height the share of the runs, each bar split into the kg its runs hold from each material, the '
        "material with the smaller median lower, each in its colour (Paul Tol's muted scheme); each material's median "
        'over the runs that hold the element is on the pages of medians after them. The material pages: the bars of '
        'one material in one robot. The median and the 95 % interval (where 95 of 100 runs lie) are named in the '
        'legend of each page. Each panel on its own scale and unit (kg, g, mg). The numbers of every panel are on the '
        'page after its page: in what share of the runs it is held, its median, its 50 % and 95 % intervals, and the '
        'runs beyond its axis. An element or material 0 in some runs: its panel shows the runs that hold it; one held '
        'in fewer than 2.5 % of the runs has no panel. Each axis ends where 99.5 % of its runs lie: the 0.5 % beyond '
        'are not drawn. ' + LOG_WORDS,
        f"The model runs: {d.n:,}, each one robot of type {d.robot_type} in the register, each of its "
        f'{len(d.register)} robots taken apart drawn equally often (a robot in two versions, each as often); its mass '
        'a triangle on its own mass, its parts its own, part by part (the parts file, from its sources).',
        (f'Not yet taken apart: {len(later)} of its {d.listed} robots of the register with a mass; until all are, '
         f'the runs of robot type {d.robot_type} come from the workbook, and these pages show the '
         f'{len(d.register)} taken apart.') if later else '',
        'The robots drawn: ' + '; '.join(d.register) + '. A robot of two robot types is drawn in full in each of them.',
        d.templates,   # how many rest on templates, their parts estimated from their mass (E13 rules 2 and 4)
        ('Resting most on estimates: ' + '; '.join(estimates) + '.') if estimates else '',
        ('Below zero where a remainder is (reported, not cut: a remainder below zero keeps its negative runs, which '
         'show a fault; EVIDENCE.md E21): ' + '; '.join(remainder_reports(c)) + '.') if remainder_reports(c) else '',
        'Not drawn: ' + ('; '.join(f'{r.number} {r.name} (no mass stated)' for r in left_out) or 'none') + '.' +
        (f' A robot lighter than {params.composition.type_one_lowest_kg:g} kg is not of robot type 1.'
         if d.robot_type == TYPE_ONE else ''),
        outlier_words(outliers or [], params),
        'The elements: only the elements of interest, from what is recovered as elements: copper and nickel each its '
        'metal whole; the aluminium, magnesium and titanium alloys the metal they hold, their whole mass in the '
        'materials (their other elements stay in the alloy: the alloys table); '
        'the NdFeB magnets their neodymium, praseodymium, dysprosium, terbium, cobalt, boron, niobium and gallium; the '
        'battery cells their lithium, nickel, cobalt and manganese and the copper and aluminium of their foils and '
        'tabs; the boards and components (the electronics) their metals of interest, not the glass, epoxy and bromine '
        'of the board, each element by the component it comes from: the circuit boards, the cameras (their image '
        f"chips, a depth camera's infrared chips and laser diode; {ESTIMATED_CAMERAS_WORDS}), the other sensors "
        "(joint encoders, motion sensors, LiDARs and time-of-flight sensors, "
        "microphones, ultrasonic sensors, the hydraulic actuators' position and pressure sensors; the joints' "
        'temperature sensors, one or two a joint motor; the force and torque sensors, tactile sensors, touch screens, '
        '4G/5G modems and satellite receivers where their makers state them, an option in half the runs), the cables '
        "(their conductors and insulation) and the connectors (whose brass keeps its copper fixed in the alloy). "
        "Each joint's driver board holds its ceramic capacitors, their barium titanate a share of its mass in place "
        "of glass and epoxy (8 to 24 capacitors in a board of the size of the G1's small joint). "
        + LIGHT_ALLOY_NOTE + ' ' + MAGNETS_NOTE + ' '
        + (f"In part: {', '.join(partly)}. " if partly else '')
        + 'These stay materials: ' + (', '.join(missing) + '.' if missing else 'none.'),
        'The groups (joints with the wheels, the lift column and the hydraulics; battery; electronics; body): every '
        'kilogram of a robot in one of their parts, wherever the part sits (a driver board in a joint a small PCB of '
        'the electronics, a sensor a sensor); each element by group on the pages of groups, every element in each part '
        'on the list pages after them. The table by body region: the kinds of part, each placed whole.',
        'The material pages: each material in one robot; the steels and the aluminium alloys as their material only '
        f"(their grades on the pages of where each sits and in the alloys table; the aluminium by the type's recipe: "
        f"{d.aluminium}); the NdFeB magnets then by the grade class each joint's heat calls for, the other materials by "
        "their grades or alloys where they have several. Copper is the metal of windings, "
        'wires, busbars, contacts and heat pipes; the copper of the boards and of the cables is in the boards and '
        'components (the electronics), as are the connectors. '
        'The alloys and grades: every one the robot type holds, also one held in fewer than 2.5 % of the runs (which '
        'has no panel); what each holds by its recipe, each element from its least to its most share of its '
        "mass, the largest first, one below 0.005 % left out, its base metal the rest (a magnets' grade class by the "
        "least and most of its drawn "
        "fractions, the traction motors' own); and its kg in one robot, the median and the 95 % interval of the runs "
        'that hold it. Where copper, the magnets, each steel and each aluminium alloy sit: one row per kind of part, '
        'how often each mass came out in the runs in which it holds the material, on a logarithmic axis, with its '
        'median and its 95 % interval named in the legend; at the right the median and in what share of the runs the '
        'kind of part holds it. A logarithmic axis has no place for a value below zero: a remainder that falls below '
        'zero in some runs (a fault, reported in the run log and the summary) is drawn there over its runs above 0.',
    ]
    return [note for note in notes if note]


def notes_pages(prefix: str, title: str, paragraphs: list) -> list:
    """The notes, as (file name, figure): `<prefix>_notes_<k>.png`, its title and its paragraphs, each wrapped at
    APART_NOTE_WIDTH characters, as many to a page as fit within NOTES_LINES lines, a paragraph never split unless it
    alone is longer than a page (types 3 and 4's robots resting on estimates, since batch 3: then on over the next
    pages, at its lines), on as many pages as they need, '(k of n)' where more than one (Matthias's rule: the notes
    once, on pages of their own).
    A type's element and material pages have their notes, its figures of where the critical elements sit theirs."""
    pages, page, lines = [], [], 0
    wrapped = [textwrap.fill(p, APART_NOTE_WIDTH).split('\n') for p in paragraphs]
    for paragraph in ('\n'.join(lines[k:k + NOTES_LINES]) for lines in wrapped
                      for k in range(0, len(lines), NOTES_LINES)):
        tall = paragraph.count('\n') + 1 + (1 if page else 0)   # its lines, and the blank line before it
        if page and lines + tall > NOTES_LINES:
            pages.append(page)
            page, lines, tall = [], 0, tall - 1
        page.append(paragraph)
        lines += tall
    pages.append(page)
    out = []
    for k, page in enumerate(pages, 1):
        figure = plt.figure(figsize=APART_PAGE)
        figure.text(0.04, 0.93, title + (f' ({k} of {len(pages)})' if len(pages) > 1 else ''),
                    fontsize=APART_HEADING, va='top')
        figure.text(0.04, 0.83, '\n\n'.join(page), fontsize=APART_TEXT, va='top', color=APART_INK,
                    linespacing=1.3)
        out.append((f'{prefix}_notes_{k}.png', figure))
    return out


def taken_apart_pages(c: Composition, d: Draws, left_out: list, params: Params, later: list | None = None,
                      outliers: list | None = None) -> list:
    """A robot type's pages, as (file name, figure): the notes pages (`outliers` named there, E30 point 4); its
    elements six a page, each split by the material it comes from (by_material_panel), one legend of the page's
    materials at the top; its materials nine a page (material_page_panels); its alloys and grades in a table
    (EVIDENCE.md E19 points 4 and 7; the preview of type 5, "Yes, build them", 2026-11-02)."""
    # Each element of interest held in at least HELD_SHARE of the draws, as a material; the titanium also its sensors'
    # (SENSORS_OF), a panel of its own after its alloy's, where the sensors hold it in HELD_SHARE of the draws; an
    # element of the magnets and the sensors alone (magnets_split, E38 point 5) in two panels, the magnets' and the
    # sensors'. Each entry (element, its view: 'all', 'magnets' or 'sensors').
    shown = [e for e in c.tables['elements'][0] if held(c.column('elements', e))]
    entries = []
    for e in shown:
        if magnets_split(materials_of(d, e)):
            entries += [(e, 'magnets'), (e, 'sensors')]
            continue
        entries.append((e, 'all'))
        if e in SENSORS_OF and held(sum(sensors_split(e, materials_of(d, e)).values(), np.zeros(d.n))):
            entries.append((e, 'sensors'))
    per_page = APART_ACROSS * ELEMENT_DOWN
    pages = [entries[k:k + per_page] for k in range(0, len(entries), per_page)]
    notes = notes_pages(c.name, f'Robot type {d.robot_type}, {c.title}: how to read its pages',
                        taken_apart_notes(c, d, left_out, params, later, outliers))
    out = []
    for p, page in enumerate(pages, 1):
        figure, axes = plt.subplots(ELEMENT_DOWN, APART_ACROSS, figsize=APART_PAGE, squeeze=False)
        panels = []
        for k, (symbol, view) in enumerate(page):
            here = axes[k // APART_ACROSS, k % APART_ACROSS]
            if view == 'sensors':   # the sensors' part, a panel of its own (SENSORS_OF, magnets_split)
                panels.append((here, by_material_panel(here, sensors_split(symbol, materials_of(d, symbol)),
                                                       sensors_title(symbol), k % APART_ACROSS == 0, ())))
                continue
            if view == 'magnets':   # the magnets' part, a panel of its own (magnets_split, E38 point 5)
                panels.append((here, by_material_panel(here, {MAGNETS: materials_of(d, symbol)[MAGNETS]},
                                                       magnets_title(symbol), k % APART_ACROSS == 0, ())))
                continue
            # Copper in all: its copper recycled as copper and, marked (fixed), that fixed in alloys (E25).
            fixed = {m: kg for (m, e), kg in (d.fixed or {}).items() if e == symbol and kg.any()}
            title = alloy_title(symbol) + (', in all' if fixed else '')
            # A light alloy's metal: the metal its alloys hold, alone (E33).
            drawn = alloy_split(symbol, materials_of(d, symbol))
            if symbol in ALLOY_OF and not held(sum(drawn.values(), np.zeros(d.n))):
                alloy_place(here, symbol, drawn, title)
                continue
            panels.append((here, by_material_panel(here, {**drawn, **fixed}, title, k % APART_ACROSS == 0,
                                                   tuple(fixed))))
        for spare in axes.flatten()[len(page):]:
            spare.axis('off')
        # The legend: every material the page draws, the light alloys too (Matthias, 2026-11-05: "There are also
        # legend colors missing"; from E33's relabelling until then without them), in as many rows as it needs.
        drawn = {m for _, (_, _, materials) in panels for m in materials}
        shown = [m for m in MATERIAL_COLOURS if m in drawn]
        # one legend: the materials drawn (by their names, E37), the median and the 95 % interval (rule 3)
        handles = ([Patch(color=MATERIAL_COLOURS[m], label=element_page_name(m)) for m in shown]
                   + distribution_handles(d.n))
        columns = legend_columns([h.get_label() for h in handles])
        rows = math.ceil(len(handles) / columns)
        figure.suptitle(f'{lead(d)}: each element in one robot, by the material it comes from ({p} of {len(pages)})',
                        fontsize=APART_HEADING, y=0.985)
        figure.legend(handles=handles, loc='upper center', bbox_to_anchor=(0.5, 0.955), ncol=columns, frameon=False,
                      fontsize=APART_TEXT)
        figure.tight_layout(rect=(0, 0, 1, 0.95 - max(rows, 1) * LEGEND_ROW), h_pad=PANEL_GAP, w_pad=2.5)
        make_room(figure, panels)
        out.append((f'{c.name}_elements_{p}.png', figure))
    # Each page of panels followed by the page of its numbers (E34), the element pages', then the material pages'.
    materials = material_pages(c, d)
    # Each element by the four groups of how a robot is taken apart, and the list part by part (Matthias, 2026-11-08,
    # "Yes, add 1 to 3"), after the alloys.
    groups, lists = group_pages(c, d)
    return (notes + with_numbers(out, c.name) + medians_pages(c, d) + with_numbers(materials, c.name, len(out) + 1)
            + alloys_pages(c, d) + with_numbers(groups, c.name, len(out) + len(materials) + 1) + lists)


def materials_of(d: Draws, symbol: str) -> dict:
    """material -> kg of one element of interest it gives, in each draw (Draws.by_material)."""
    return {m: kg for (m, e), kg in d.by_material.items() if e == symbol}


# The numbered pages of a robot type, one series each (<prefix>_<series>_<k>.png): a page of a series beyond those a run
# writes is removed by its exact name (Matthias, 2026-11-02, "02 removes them itself": a type's material pages went
# from four to two, and its third and fourth of the run before would have stayed in the folder).
COMPOSITION_SERIES = ('notes', 'elements', 'medians', 'materials', 'alloys', 'groups', 'parts', 'numbers')   # figures/composition/<n>_<name>_<series>_<k>.png
PARTS_SERIES = ('notes', 'overview')   # figures/parts_taken_apart/<n>_<name>/robot_type_<n>_<series>_<k>.png


def remove_pages_not_drawn(folder: str, prefix: str, series: tuple, written: list) -> list:
    """In `folder`, the pages <prefix>_<series>_<k>.png of each of `series` numbered beyond the last one just `written`
    (all of a series none of whose pages was written), each removed by its exact name; returns their names. Nothing
    else in the folder is touched."""
    removed = []
    for kind in series:
        page = re.compile(re.escape(f'{prefix}_{kind}_') + r'(\d+)\.png')
        last = max((int(m.group(1)) for name in written if (m := page.fullmatch(name))), default=0)
        for name in sorted(os.listdir(folder)):
            if (m := page.fullmatch(name)) and int(m.group(1)) > last:
                os.remove(os.path.join(folder, name))
                removed.append(name)
    return removed


def draw_taken_apart_pages(c: Composition, d: Draws, left_out: list, folder: str, params: Params,
                           later: list | None = None, outliers: list | None = None) -> list:
    """A robot type's pages into `folder` (its `outliers` named on its notes pages), and its pages of an earlier run
    beyond them removed (said as removed); returns their file names."""
    os.makedirs(folder, exist_ok=True)
    written = save_pages(taken_apart_pages(c, d, left_out, params, later, outliers), folder, params.output.dpi)
    for name in remove_pages_not_drawn(folder, c.name, COMPOSITION_SERIES, written):
        print(f'  {name} removed: a page of an earlier run no longer drawn.', flush=True)
    return written


# ------------------------------------------------------------------------------------------------------
# A robot type's two figures of where its critical elements sit (type 1's until 2026-10-29 the stage 04)
# ------------------------------------------------------------------------------------------------------
# Matthias, 2026-10-27, on the element figure: "Yes, the element figure is right now" (V49), and on the overview: "Looks
# good to me"; 2026-10-29: "Yes, into 02" (04's two figures drawn by 02 from the draws it holds, 04 removed). The code
# as 04 had it, its names given the forms of 02's.

# The critical elements of the figures, in Matthias's order (V49): symbol (Nd+Pr: the two added) and name.
FIGURE_ELEMENTS = [('Cu', 'Copper'), ('Al', 'Aluminium'), ('Ag', 'Silver'), ('Au', 'Gold'), ('Pd', 'Palladium'),
                   ('Ta', 'Tantalum'), ('Nd+Pr', 'Neodymium and praseodymium'), ('Dy', 'Dysprosium'),
                   ('Ga', 'Gallium'), ('In', 'Indium')]
HELD_SHARE = 0.025    # a kind of part holding an element in fewer draws than this is not drawn (the 95 % rule)

# The pages (Matthias, 2026-10-28: "Have the overview on several pages. I can not read it. too smal, you should notice
# this before you sjhow me. Elements is an edge case. Also quite small"): APART_PAGE, no text below APART_TEXT
# points; fit to a 1920 × 1080 screen the smallest text is about 23 pixels tall (tests/test_parts_taken_apart.py
# requires 18 at least). No footnote under a page: the notes are once, on a page of their own, the first of the folder
# (Matthias, 2026-10-29: "parts taken apart show each a long legend, you know, what I think about this").
FIGURE_TITLE_WIDTH = 30   # characters in a line of an element page's panel title; a longer one takes two lines
# The overview's panels: their width (share of the page), and where their three columns of numbers start, the
# median's, the mean's and in what share of the draws the kind of part holds the element (share of the panel's width
# beyond its right edge), so that all three stay within the page and a number of eight characters (0.000022) clears
# the next (2026-10-29, "Yes, do it": the third column, the panels 0.42 of the page before). The figures of where a
# material sits likewise, the same three columns since 2026-11-01 ("If a value is 0 then it is NOT part of the
# distribution"), their axes SOURCES_WIDTH of the page (0.6 before, with two).
PANEL_WIDTH = 0.38
OVERVIEW_COLUMNS = (1.01, 1.18, 1.35)
COLUMN_GAP = 10.0   # points between a column's widest number and the next column (E38)
SOURCES_WIDTH = 0.52
NUMBER_COLUMNS = (1.02, 1.21, 1.40)
# The overview's pages (Matthias, 2026-11-13, on its rows' labels 5 to 9 points apart: "These two figures look ugly.
# The different text are much to close. It looks overloaded", then "Yes, all"): every row OVERVIEW_ROW inches tall, so
# that one text height stands between two row labels (a 14-point label is about 16 points tall; 30 points a row); the
# panels from the top of the page down, OVERVIEW_TOP below the page's top (its title, then the panel's title with its
# column headings), OVERVIEW_GAP between two (the upper's axis numbers and axis title, the lower's title), and below
# the last its axis numbers and title, then the legend, within OVERVIEW_BOTTOM of the page's foot. An element whose
# rows a page cannot hold is drawn in as few panels as hold them, its rows split evenly, each on the same scale
# (overview_panels); two panels a page where both fit, else one (overview_pages). Until 2026-11-13 the rows shared the
# page's height, up to 24 on a page, 18 points a row.
OVERVIEW_ROW, OVERVIEW_TOP, OVERVIEW_GAP, OVERVIEW_BOTTOM = 0.42, 1.05, 1.15, 1.35


def overview_room(panels: int) -> int:
    """How many rows `panels` panels on one overview page hold together (APART_PAGE's height, OVERVIEW_TOP, OVERVIEW_GAP
    between two, OVERVIEW_BOTTOM)."""
    return int((APART_PAGE[1] - OVERVIEW_TOP - OVERVIEW_BOTTOM - OVERVIEW_GAP * (panels - 1)) / OVERVIEW_ROW)


def overview_panels(d: 'Draws') -> list:
    """The overview's panels of a robot type, the figure elements in their order (FIGURE_ELEMENTS), as (symbol, name,
    its rows on this panel, this panel's number, the element's panels): its rows the places holding it (a row per place
    holding it in at least HELD_SHARE of the runs, in the order of places_order), in as few panels as a page holds
    (overview_room(1)), split evenly; an element no place holds one panel without rows."""
    out = []
    for symbol, name in FIGURE_ELEMENTS:
        places = by_place(d, symbol)
        rows = [p for p in places_order() if p in places and held(places[p])]
        parts = max(1, math.ceil(len(rows) / overview_room(1)))
        size = math.ceil(len(rows) / parts) if rows else 0
        out += [(symbol, name, rows[k * size:(k + 1) * size], k + 1, parts) for k in range(parts)]
    return out


def overview_pages(d: 'Draws') -> list:
    """The overview's pages of a robot type: its panels (overview_panels) in their order, two a page where their rows
    together fit (overview_room(2)), else one."""
    panels, pages, k = overview_panels(d), [], 0
    while k < len(panels):
        two = panels[k:k + 2]
        if len(two) == 2 and sum(max(len(rows), 1) for _, _, rows, _, _ in two) <= overview_room(2):
            pages.append(two)
        else:
            pages.append(two[:1])
        k += len(pages[-1])
    return pages


def parts_figures(robot_type: int, overviews: int) -> tuple:
    """The file names of a robot type's overview pages, robot_type_<n>_overview_<k>.png (overview_pages); until
    2026-11-13 after its element pages robot_type_<n>_elements_<k>.png, each followed by the page of its numbers
    (removed on Matthias's "Yes, all": split by the four groups they repeated 02's pages by group, split kind by kind
    their colours could not all be told apart; the overview shows each element place by place)."""
    return tuple(f'robot_type_{robot_type}_overview_{k}.png' for k in range(1, overviews + 1))

# Where each kind sits on the robot, its mark and the kinds whose colour takes white text: 01's (one copy).
MARKS = schemas.MARKS


def save_figure(figure, path: str, dpi: int) -> None:
    """Write a page and close it."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    figure.savefig(path, dpi=dpi, facecolor='white')
    plt.close(figure)


def save_pages(pages: list, folder: str, dpi: int) -> list:
    """Each page of `pages` ((file name below `folder`, figure)) written, closed and let go before the next is written,
    the image matplotlib drew it into freed with it; `pages` emptied; returns the file names. Each page at 300 dpi is
    drawn into an image of 52 MB, which matplotlib keeps with the figure: all of a robot type's pages kept until the
    last was written held some 2.5 GB beyond what Python counts (measured 2026-11-13, the rule that every stage fits in
    half the computer's memory, the GitHub folder's CLAUDE.md §4)."""
    names = []
    while pages:
        name, figure = pages.pop(0)
        save_figure(figure, os.path.join(folder, name), dpi)
        del figure
        gc.collect()   # a figure refers to itself through its parts: only the collector frees it and its image
        names.append(name)
    return names


def places_order() -> list:
    """The places of the pages of where the critical elements sit, in their order: the kinds of part, then the
    electronics' components (E32), the sensors by their kind in place of the cameras and the other sensors (E38),
    each by its label."""
    return (list(KINDS) + [component_label(CIRCUIT_BOARDS), component_label(CAPACITOR_PARTS)]
            + [p for k in SENSOR_KINDS for p in [component_label(k)] + [component_label(f'{k}, {w}')
                                                                       for w in REGION_WORDS.values()]]
            + [component_label(c) for c in (CABLE_PARTS, CONNECTORS)])


def place_label(place: str) -> str:
    """A place's name on the pages: a kind of part's, or the component's, its component first ('Cameras (boards and
    components)', shown_name, E38)."""
    return KINDS[place][0] if place in KINDS else shown_name(place)


def place_group(place: str) -> str:
    """The group of how a robot is taken apart a place belongs to (01's TAKEN_APART): a kind of part's (01's
    KIND_GROUP); a component of the electronics or a kind of sensor, wherever it sits, the electronics (01's taken_part:
    a sensor, a board, a cable or a connector goes to the electronics wherever it sits)."""
    return schemas.KIND_GROUP[place] if place in KINDS else schemas.GROUP_ELECTRONICS


def place_keys(d: Draws) -> list:
    """(place, element) of Draws.places, in the order of places_order, the elements in element_order."""
    return [(p, e) for p in places_order() for e in element_order({e for q, e in d.places if q == p})]


def by_place(d: Draws, symbol: str) -> dict:
    """place -> kg of one figure element in each draw ('Nd+Pr' the two added): each kind of part, and the electronics
    by their components wherever they sit (Matthias, 2026-11-05, "Yes, fix all three": indium the cameras', not the
    head's)."""
    wanted = symbol.split('+')
    out = {}
    for place in places_order():
        found = [d.places[(place, e)] for e in wanted if (place, e) in d.places]
        if found:
            out[place] = sum(found)
    return out


def by_kind(d: Draws, symbol: str) -> dict:
    """kind -> kg of one figure element in each draw; 'Nd+Pr' is the two added."""
    wanted = symbol.split('+')
    out = {}
    for kind in KINDS:
        found = [d.elements[(kind, e)] for e in wanted if (kind, e) in d.elements]
        if found:
            out[kind] = sum(found)
    return out


def held(values: np.ndarray) -> bool:
    """Whether a kind of part holds an element in the figures' sense: in at least HELD_SHARE of the draws."""
    return bool((values > 0).mean() >= HELD_SHARE)


def robots_note(d: Draws) -> str:
    """What every draw is, for the notes page of the figures of where the critical elements sit."""
    return (f'{d.n:,} model runs, each one of the {len(d.register)} robots of type {d.robot_type} in the register taken '
            'apart, each as often (a robot in two versions, each as often); each robot from its own parts, part by '
            'part.')


def stacked_bars(axes, parts: dict, colours: dict) -> SimpleNamespace:
    """The bars of a stacked panel, the form Matthias set for RAWCLICDataCenters' 05: the histogram of the total of
    `parts` (each kg in each draw) over the draws, the height the share of the draws, each bar split into the kg its
    draws hold in each part, the part with the smaller median lower, in its colour; the parts held in fewer than
    HELD_SHARE of the draws not drawn. Where the total is 0 in some draws, over the draws that hold it. Its 70 bars from
    the smallest draw to the axis's end (AXIS_END), the draws beyond not drawn; where its draws spread over orders of
    magnitude (logarithmic, LOG_BELOW), even on a logarithmic axis. Returns its values (in its unit), unit,
    end, the share of the runs that hold it (1 where all do), the parts drawn, the parts over those draws, the top of
    its bars."""
    total = sum(parts.values())
    drawn = [k for k in parts if held(parts[k])]   # the parts holding it in at least HELD_SHARE of all the draws
    inside = total > 0
    held_in = float(inside.mean()) if not inside.all() else 1.0
    if not inside.all():
        parts = {k: v[inside] for k, v in parts.items()}
        total = total[inside]
    per, unit = panel_unit(total)
    values = total / per
    end = axis_end(values)
    on_axis = values <= end
    if logarithmic(values, end):   # spread over orders of magnitude (LOG_BELOW): its bars even on a logarithmic axis
        axes.set_xscale('log')
        edges = np.geomspace(float(values.min()), end, APART_BINS + 1)
    else:
        edges = (np.linspace(float(values.min()), end, APART_BINS + 1) if end > values.min()
                 else np.histogram_bin_edges(values, bins=APART_BINS))
    index = np.clip(np.digitize(values, edges[1:-1]), 0, len(edges) - 2)[on_axis]   # the bar each draw falls into
    share_of_draws = np.bincount(index, minlength=len(edges) - 1) / values.size
    kg_all = np.bincount(index, weights=total[on_axis], minlength=len(edges) - 1)
    bottom = np.zeros(len(edges) - 1)
    for part in sorted(drawn, key=lambda k: float(np.median(parts[k]))):          # the smaller median lower
        kg = np.bincount(index, weights=parts[part][on_axis], minlength=len(edges) - 1)
        height = share_of_draws * np.divide(kg, kg_all, out=np.zeros_like(kg), where=kg_all > 0)
        axes.bar(edges[:-1], height, width=np.diff(edges), align='edge', bottom=bottom, color=colours[part],
                 edgecolor='none')
        bottom += height
    return SimpleNamespace(values=values, unit=unit, end=end, held_in=held_in, drawn=drawn, parts=parts,
                           top=float(bottom.max()))


def ridge_panel(axes, kinds: dict, estimated: dict, title: str, rows: list | None = None) -> None:
    """One panel of the overview: one row per kind of part holding the element, labelled with its mark on the robot,
    in the colour of its group (place_group; since 2026-11-13, "Yes, both": a colour per kind of part, up to 20 in a
    panel, could not all be told apart), each the histogram of its kg over the draws that hold it scaled to the row,
    hatched where more than half its median
    rests on masses labelled E; the median a solid line and the 95 % interval dashed (MEDIAN_MARK, BOUND_MARK; their
    samples in the page's legend), all of the draws that hold it; at the right three columns: the median, the 95 %
    interval and in what share of the runs the kind of part holds the element (since 2026-11-13 two columns, the
    median and the share: a column of the 95 % interval ran off the page; its marks are drawn in the row) (Matthias, 2026-10-29, "Yes, do it", to the
    overview's rows as the element panels: a kind of part holding it in only some draws showed a median of 0); one
    scale and unit for the panel, its axis ending at the largest of the rows' AXIS_END-th percentiles, the draws beyond
    not drawn and said on its label. `rows`: the rows this panel draws, where an element's rows take more than one panel
    (overview_panels); the scale, the unit, the axis's end and the runs beyond it are those of all its rows, so that its
    panels can be read together."""
    every = [k for k in places_order() if k in kinds and held(kinds[k])]   # kinds of part, then components
    shown = every if rows is None else [k for k in every if k in rows]
    axes.set_title(title, fontsize=APART_TITLE, loc='left')
    if not shown:
        axes.text(0.5, 0.5, 'none in these robots', transform=axes.transAxes, ha='center', va='center',
                  fontsize=APART_TEXT)
        axes.axis('off')
        return
    per, unit = panel_unit(sum(kinds[k] for k in every))
    holding = {k: kinds[k][kinds[k] > 0] for k in every}   # the draws in which the kind of part holds the element
    # The axis ends at the largest of the rows' AXIS_END-th percentiles, of all the element's rows; the draws beyond are
    # not drawn (until 2026-11-01 piled into the last bar) and are said on the axis's label (beyond_words).
    top = max(axis_end(holding[k]) for k in every) / per
    edges = np.linspace(0, top if top > 0 else 1, 51)
    right = blended_transform_factory(axes.transAxes, axes.transData)
    cells = []   # (row, its median, 95 % interval and share held, as written)
    for row, kind in enumerate(reversed(shown)):
        values = holding[kind] / per
        counts, _ = np.histogram(values[values <= edges[-1]], bins=edges)
        heights = 0.8 * counts / max(counts.max(), 1)
        hatched = float(np.median(estimated[kind])) > 0.5 * float(np.median(kinds[kind]))
        axes.bar(edges[:-1], heights, width=np.diff(edges), align='edge', bottom=row + 0.05,
                 color=schemas.GROUP_COLOURS[place_group(kind)],
                 edgecolor=APART_INK if hatched else 'none', linewidth=0, hatch='///' if hatched else None)
        median = float(np.median(values))
        low, high = (float(b) for b in np.percentile(values, [2.5, 97.5]))
        axes.plot([median, median], [row + 0.05, row + 0.9], **MEDIAN_MARK)
        for bound in (low, high):
            axes.plot([bound, bound], [row + 0.05, row + 0.9], **BOUND_MARK)
        share = holding[kind].size / kinds[kind].size
        cells.append((row, (panel_number(median), held_share(share))))
    # The three columns of numbers, each at its place of OVERVIEW_COLUMNS, or further right where the widest number of
    # the column before would reach it (since 2026-11-06, E38: a sensor's milligrams in a panel in kg are numbers of up
    # to ten characters, such as 0.0000066); measured in points from the font's outlines (text_width), the panel's width
    # fixed on the page.
    heads = ('median', 'held in')
    panel_points = axes.get_position().width * axes.figure.get_figwidth() * 72
    columns = [OVERVIEW_COLUMNS[0]]
    for k in range(1, len(OVERVIEW_COLUMNS)):
        widest = max(text_width(t) for t in [heads[k - 1]] + [numbers[k - 1] for _, numbers in cells])
        columns.append(max(OVERVIEW_COLUMNS[k], columns[-1] + (widest + COLUMN_GAP) / panel_points))
    for row, numbers in cells:
        for column, number in zip(columns, numbers):
            axes.text(column, row + 0.45, number, transform=right, ha='left', va='center', fontsize=APART_TEXT,
                      color=APART_INK)
    # The headings 2 points above the panel, whatever its rows' height (since 2026-11-06: a page of one short panel,
    # indium's two rows, had them a tenth of a tall row up, above the panel's title; E38).
    above = offset_copy(axes.transAxes, fig=axes.figure, y=2, units='points')
    for column, what in zip(columns, heads):
        axes.text(column, 1.0, what, transform=above, ha='left', va='bottom', fontsize=APART_TEXT, color=APART_INK)
    axes.set_title(f'{title}, in {unit}', fontsize=APART_TITLE, loc='left')
    axes.set_ylim(0, len(shown))
    axes.set_yticks([row + 0.45 for row in range(len(shown))])
    # A kind of part with its mark on the robot; a component of the electronics by its name (it has no one place).
    axes.set_yticklabels([f'{MARKS[k]}  {KINDS[k][0]}' if k in KINDS else k.replace(f'{ELECTRONICS}: ', '')
                          for k in reversed(shown)], fontsize=APART_TEXT)
    axes.tick_params(axis='y', length=0)
    axes.set_xlim(0, edges[-1])
    axes.xaxis.set_major_locator(plt.MaxNLocator(6))
    axes.xaxis.set_major_formatter(plt.FuncFormatter(panel_number))
    axes.tick_params(axis='x', labelsize=APART_TEXT)
    # The draws beyond the axis's end, of all its rows, on its label: above the panel stand its title and the columns.
    beyond = beyond_words(np.concatenate([holding[k] for k in every]) / per, edges[-1], unit)
    axes.set_xlabel(f'mass ({unit})' + (f'; {beyond} (of its rows’ runs)' if beyond else ''),
                    fontsize=APART_LABEL)
    axes.grid(axis='x', alpha=0.3)
    for side in ('top', 'right'):
        axes.spines[side].set_visible(False)


def draw_schema(axes, d: Draws) -> None:
    """The robot of the overview: 01's robot with its kinds of part (draw_kinds), the joints whose magnets are for
    150 °C or more in most draws ringed red."""
    schemas.draw_kinds(axes, d.hot, APART_TEXT, {k for k, _ in d.materials[0]})


def overview_page(d: Draws, page: list, number: int, of: int):
    """One page of the overview Matthias approved ("Looks good to me", 2026-10-27), for three robots (answer E,
    "Groups, histograms"): left the robot with its joint groups numbered and its other kinds lettered; right one or two
    panels of overview_panels, one above the other from the top, each row OVERVIEW_ROW inches tall; the legend below the
    last panel, as on the data centres' pages (since 2026-11-13, "Yes, all": above the panels it stood 4 points from the
    panel's title); page `number` of `of`."""
    figure = plt.figure(figsize=APART_PAGE)
    figure.add_axes((0.01, 0.04, 0.21, 0.85))   # 0.22 wide until 2026-11-13: the base's mark 'F' 6.8 points from a row label
    draw_schema(figure.axes[0], d)
    height = APART_PAGE[1]
    top = height - OVERVIEW_TOP                    # inches from the page's foot to the top of the next panel
    groups = set()
    for symbol, name, rows, part, parts in page:
        places = by_place(d, symbol)
        tall = max(len(rows), 1) * OVERVIEW_ROW
        estimated = {place: sum((d.places_estimated[(place, e)] for e in symbol.split('+')
                                 if (place, e) in d.places_estimated), np.zeros(d.n)) for place in places}
        title = f'{name} ({symbol})' + (f', part {part} of {parts}' if parts > 1 else '')
        ridge_panel(figure.add_axes((0.43, (top - tall) / height, PANEL_WIDTH, tall / height)), places, estimated,
                    title, rows)
        groups |= {place_group(p) for p in rows}
        top -= tall + OVERVIEW_GAP
    figure.suptitle(f'Robot type {d.robot_type} taken apart: where the critical materials sit, and how sure we are '
                    f'({number} of {of})', fontsize=APART_HEADING, y=0.975)
    # the colours of the rows and of the robot's marks (the groups of the places drawn and of every kind on the robot,
    # draw_schema), the median and the 95 % interval, in one legend below the last panel's axis title (rule 3: every
    # colour and mark its sample; until 2026-11-13 the groups of the rows alone, so the body's yellow mark on the robot
    # had no sample on a page without a row of the body)
    groups |= {schemas.KIND_GROUP[k] for k, _ in d.materials[0]}
    handles = ([Patch(color=schemas.GROUP_COLOURS[g], label=g) for g in schemas.TAKEN_APART if g in groups]
               + distribution_handles(d.n))
    # In one row where it fits between the robot (its drawing ends at 0.22 of the page's width) and the page's right
    # edge, measured as drawn in the page's font; else in fewer columns, as many rows as it needs (2026-11-13: in one
    # row of six it ran 2 pixels beyond the page, Luciole's letters being wider than the former font's; the real run's
    # "Median of 200,000 model runs" is longer still than the tests' 200).
    renderer = figure.canvas.get_renderer()
    for columns in range(len(handles), 0, -1):
        legend = figure.legend(handles=handles, loc='upper center', ncol=columns, frameon=False, fontsize=APART_TEXT,
                               bbox_to_anchor=(0.62, (top + OVERVIEW_GAP - 0.85) / height))
        box = legend.get_window_extent(renderer).transformed(figure.transFigure.inverted())
        if (box.x0 >= 0.23 and box.x1 <= 0.99) or columns == 1:
            break
        legend.remove()
    # its rows even (six entries in two rows three and three, not five and one)
    even = math.ceil(len(handles) / math.ceil(len(handles) / columns))
    if even < columns:
        legend.remove()
        figure.legend(handles=handles, loc='upper center', ncol=even, frameon=False, fontsize=APART_TEXT,
                      bbox_to_anchor=(0.62, (top + OVERVIEW_GAP - 0.85) / height))
    return figure


def parts_notes(d: Draws) -> list:
    """The paragraphs of the notes page of the overview, once for all its pages (until 2026-10-29 a footnote under
    every page; the element pages' paragraph until 2026-11-13, when they were removed, "Yes, all")."""
    return [
        "The overview pages: each row the element's weight in one kind of part, in one component of the electronics "
        "or in one kind of sensor, in the colour of its group (a component or a sensor the electronics, wherever it "
        "sits), over the runs that hold it; two elements a page where their rows fit, else one, and an element with "
        "more rows than a page holds on two pages, its rows split, on the same scale. The height of a row the share "
        f"of those runs scaled to the row; the median and the 95 % interval (where 95 of 100 runs lie) named in the "
        "legend; at the right the median and 'held in': in what share of all the runs the kind of part holds the "
        'element. Hatched: more than half of the median rests on parts whose mass is an estimate. Each axis ends where '
        "99.5 % of the runs of its widest row lie; the runs beyond are not drawn, and its label says how many.",
        'A kind of part holding the element in fewer than 2.5 % of the runs is not drawn. Each element by the four '
        "groups of how a robot is taken apart, and each in one robot in all, is on the type's pages of its composition.",
        robots_note(d),
        "The joints with their driver boards and encoders; the magnets' grade class (with it their dysprosium) drawn "
        "by each joint's heat, the knees hottest, the arms coolest, one choice a run for every joint; the NdFeB "
        'magnets shown by their neodymium and praseodymium; the battery metals and silicon not shown.',
    ]


def parts_figure_pages(d: Draws) -> list:
    """Every page of the overview, as (file name, figure): its notes pages first, then its pages in the order of
    parts_figures() (the element pages before them until 2026-11-13, "Yes, all")."""
    prefix = f'robot_type_{d.robot_type}'
    layout = overview_pages(d)   # two panels a page where their rows fit, else one
    pages = [(f'{prefix}_overview_{k + 1}.png', overview_page(d, page, k + 1, len(layout)))
             for k, page in enumerate(layout)]
    assert [name for name, _ in pages] == list(parts_figures(d.robot_type, len(layout)))
    return notes_pages(prefix, f'{lead(d)}: how to read the pages of where its critical elements sit',
                       parts_notes(d)) + pages


def draw_parts_figures(d: Draws, params: Params, folder: str) -> None:
    """Every page of the overview, and the figures of where each material sits (sources_pages), into `folder` (the
    type's folder in `output.parts_figures_dir`); its numbered pages of an earlier run beyond them removed (said as
    removed)."""
    written = save_pages(parts_figure_pages(d) + sources_pages(d), folder, params.output.dpi)
    for name in remove_pages_not_drawn(folder, f'robot_type_{d.robot_type}', PARTS_SERIES, written):
        print(f'  {name} removed: a page of an earlier run no longer drawn.', flush=True)


# ------------------------------------------------------------------------------------------------------
# A robot type's material pages, as RAWCLICDataCenters draws its materials
# ------------------------------------------------------------------------------------------------------
# Matthias, 2026-10-29: "There are only figures on the element level I want to see, how much Copper and especially
# permanent magnets. The different steels and aluminum alyoys. We had this differently in datacenters", then "Yes, 1 to
# 5": the materials of one robot, one panel each (as the data centres' "materials of one data center"), the steels by
# their grade, the aluminium by its alloys, the permanent magnets in all and by their grade class; and for copper, the
# magnets, each steel and each aluminium alloy, where it sits, kind of part by kind of part (as the data centres' "where
# the copper comes from").

# The materials of the pages in this order; any other material follows them.
MATERIAL_ORDER = (COPPER, 'Brass', 'Nickel', ALUMINIUM, MAGNESIUM, 'Titanium alloy', 'Steel', 'Stainless steel',
                  'Electrical steel', MAGNETS, CELL_MATERIAL, ELECTRONICS, 'Plastics', 'Fibre composites', 'Ceramics',
                  OTHER)   # the one list's order (E19 point 2), as the shared lists write it
# Each grade, alloy or recipe whose name is a code, in plain words on its own, for the "where it comes from"
# figures (the others keep their recipe's name, e.g. 'Aluminium 6061').
GRADE_TITLES = {'20CrMnTi': 'Gear steel 20CrMnTi', 'GCr15': 'Bearing steel GCr15', '42CrMo4': 'Alloy steel 42CrMo4',
                'C45': 'Carbon steel C45', 'P20': 'Tool steel P20', '17-4PH': 'Stainless steel 17-4PH',
                'Type 304': 'Stainless steel 304', '440C': 'Stainless steel 440C', 'M19': 'Electrical steel M19',
                'M27': 'Electrical steel M27',
                'Ti-6Al-4V': 'Titanium Ti-6Al-4V', 'Brass': 'Brass', 'Nickel strip': 'Nickel strips, battery',
                'NMC cylindrical': 'Battery cells, NMC (cylindrical)', 'LFP cylindrical': 'Battery cells, LFP '
                                                                                           '(cylindrical)'}
# Each grade, alloy or magnet class in plain words under its material on the material pages ('Steel: gear steel
# 20CrMnTi'; EVIDENCE.md E19 point 2, the preview of type 5, "Yes, build them", 2026-11-02); '' where it is its material
# (brass); another keeps its recipe's name.
GRADE_WORDS = {'20CrMnTi': 'gear steel 20CrMnTi', 'GCr15': 'bearing steel GCr15', '42CrMo4': 'alloy steel 42CrMo4',
               'C45': 'carbon steel C45', 'P20': 'tool steel P20', '17-4PH': '17-4PH', 'Type 304': '304',
               '440C': '440C', 'M19': 'M19', 'M27': 'M27', 'Ti-6Al-4V': 'Ti-6Al-4V', 'Brass': '',
               'Nickel strip': 'strips of the battery', 'NMC cylindrical': 'NMC (cylindrical)',
               'LFP cylindrical': 'LFP (cylindrical)', 'Aluminium 6061': '6061 (wrought)',
               'Aluminium 7075': '7075 (wrought)', 'Aluminium A380': 'A380 (die-cast)',
               'Aluminium ADC12': 'ADC12 (die-cast)', 'Magnesium AZ91D': 'AZ91D', 'Magnesium AM50A': 'AM50A',
               'Magnesium AM60B': 'AM60B'}
# The materials of the alloys table (E19 point 4): those whose elements stay in their alloy or grade, the nickel and the
# magnets; not copper (copper metal), the battery cells, the boards and components, plastics, composites and the rest.
TABLE_MATERIALS = ('Brass', 'Nickel', ALUMINIUM, MAGNESIUM, 'Titanium alloy', 'Steel', 'Stainless steel',
                   'Electrical steel', MAGNETS)
# The colour of each material an element of interest comes from, on the element pages: Paul Tol's muted qualitative
# scheme, as published (https://sronpersonalpages.nl/~pault/, "colour-blind safe"), in its order, the materials in the
# one list's order (E19; the preview of type 5 approved, 2026-11-02).
MATERIAL_COLOURS = {COPPER: '#CC6677', 'Nickel': '#332288', ALUMINIUM: '#DDCC77', MAGNESIUM: '#117733',
                    'Titanium alloy': '#88CCEE', MAGNETS: '#882255', CELL_MATERIAL: '#44AA99', ELECTRONICS: '#999933'}
# The electronics by their components (E32), after the electronics: the circuit boards in the electronics' olive, the
# cameras in Paul Tol's vibrant blue (since 2026-11-13, "Yes, all": the muted scheme's purple, #AA4499, stood 20.1 from
# copper's rose in CAM02-UCS, under the 21 of FigureTests' rule colour_normal; the blue stands at least 25.2 from every
# other colour here, 22.9 for a colour-blind reader), the other sensors, the cables and the connectors in Paul Tol's
# published companions of the scheme's olive, his dark yellow, pale yellow and dark grey.
MATERIAL_COLOURS.update({component_label(CIRCUIT_BOARDS): '#999933', component_label(CAMERAS): '#0077BB',
                         component_label(OTHER_SENSORS): '#666633', component_label(CABLE_PARTS): '#EEEEBB',
                         component_label(CONNECTORS): '#555555',
                         # The large capacitors (E51) in Paul Tol's dark cyan of his "dark" scheme, not used before.
                         component_label(CAPACITOR_PARTS): '#225555'})
# The copper fixed in alloys (E25), one part of the copper's bars in the scheme's own pale grey, the scheme having no
# colour left for brass and the three steels; each alloy's share written in the panel, marked '(fixed)'.
FIXED_PART = 'Copper fixed in alloys'
MATERIAL_COLOURS[FIXED_PART] = '#DDDDDD'
# The element pages: six panels a page, three across, so that each material's mean has room above the bars (the
# preview of type 5; nine a page before, the means over the bars).
ELEMENT_DOWN = 2
# The alloys table's columns: where each starts (share of the page's width), its characters in a line of 14 points; a
# row's gap and one line's height (share of the page's height); where the rows start and where a page ends.
TABLE_X, TABLE_WRAP = (0.03, 0.22, 0.38, 0.79), (22, 18, 64, 30)
TABLE_HEAD = ('Alloy or grade', 'Material', 'What it holds, by its recipe (% of its mass)',
              'In one robot: median\n(95 % interval)')
ROW_GAP, LINE_HEIGHT, TABLE_TOP, TABLE_BOTTOM = 0.02, 0.036, 0.815, 0.03
# The materials whose "where it comes from" figure is drawn, each grade and alloy of them: copper, the magnets (in
# all), the steels and the aluminium (point 3 of his yes).
# Each steel: since E19 step 1 the stainless and electrical steels are materials of their own.
SOURCES_OF = (COPPER, MAGNETS, 'Steel', 'Stainless steel', 'Electrical steel', ALUMINIUM)
SOURCES_FOLDER = 'sources'   # within `output.parts_figures_dir`
VIOLIN = '#4477AA'           # Paul Tol's bright blue, as published (the bars of the pages)


def grade_words(material: str, grade) -> str:
    """A grade, alloy or magnet class in plain words under its material: 'gear steel 20CrMnTi', '6061 (wrought)',
    'grade class H' (GRADE_WORDS); '' for none, or for a grade that is its material (brass)."""
    if material == MAGNETS:
        return f'grade class {grade}' if grade else ''
    return GRADE_WORDS.get(grade, grade)


def material_panels(d: Draws) -> list:
    """The panels of the material pages, in their order (EVIDENCE.md E19 point 7; the preview of type 5, "Yes, build
    them", 2026-11-02): (title, the material, its grade, alloy or class (None for the material whole where it has
    several), kind -> kg in each draw). Each material of the one list in its order, then its grades, alloys or magnet
    classes, each under its material ('Steel: gear steel 20CrMnTi'); a material of one grade that grade in its title
    ('Titanium alloy: Ti-6Al-4V'). Those held in at least HELD_SHARE of the draws (the 95 % rule of the panels)."""
    return [p for p in every_material_panel(d) if held(sum(p[3].values()))]


# The materials the material pages show whole, their grades not under them (Matthias, 2026-11-02: "There are far to
# many different types of steels. Can we have this in separate plots and in the overview just steel", "It is the same
# with aluminum alloys", "We have the parts for each alloy. This is good. But the material is much too detailed", then
# "Yes, build it"): their grades stay on the pages of where each sits (sources_pages) and in the alloys table.
MATERIAL_ONLY = ('Steel', 'Stainless steel', 'Electrical steel', ALUMINIUM)


def material_page_panels(d: Draws) -> list:
    """The panels of the material pages: material_panels, the steels and the aluminium alloys (MATERIAL_ONLY) each as
    its material only, the sum of its grades in each draw, in its place; the other materials as material_panels gives
    them."""
    panels, whole = [], set()
    for title, material, detail, kinds in material_panels(d):
        if material not in MATERIAL_ONLY:
            panels.append((title, material, detail, kinds))
        elif material not in whole:
            whole.add(material)
            panels.append((material, material, None,
                           {kind: sum(kg for (k, m, _), kg in d.details.items() if k == kind and m == material)
                            for kind in KINDS if any(k == kind and m == material for k, m, _ in d.details)}))
    return panels


def every_material_panel(d: Draws) -> list:
    """material_panels, also those held in fewer than HELD_SHARE of the draws (the alloys table lists every alloy)."""
    materials = [m for m in MATERIAL_ORDER if any(k[1] == m for k in d.details)]
    materials += sorted({k[1] for k in d.details} - set(materials))
    order = list(schemas.MAGNET_CLASSES)
    panels = []
    for material in materials:
        details = sorted({k[2] for k in d.details if k[1] == material},
                         key=lambda x: (order.index(x) if material == MAGNETS and x in order else 0, x != '', x))
        if len(details) > 1:
            kinds = {kind: sum(kg for (k, m, _), kg in d.details.items() if k == kind and m == material)
                     for kind in KINDS if any(k == kind and m == material for k, m, _ in d.details)}
            panels.append((material, material, None, kinds))
        for detail in details:
            kinds = {k: kg for (k, m, x), kg in d.details.items() if m == material and x == detail}
            words = grade_words(material, detail)
            panels.append((f'{material}: {words}' if words else material, material, detail, kinds))
    return panels


def material_panel(axes, kg: np.ndarray, title: str, first_in_row: bool) -> None:
    """One material in one robot over the draws, drawn as an element of the element pages (element_panel, also
    where the material is 0 in some draws), its title wrapped between words ("die-cast" whole)."""
    element_panel(axes, kg, textwrap.fill(title, FIGURE_TITLE_WIDTH, break_on_hyphens=False), first_in_row)


def material_pages(c: Composition, d: Draws) -> list:
    """A robot type's material pages, as (file name, figure): its materials nine a page, each the histogram of its kg
    in one robot over the draws, the steels and the aluminium alloys whole, the others then their grades
    (material_page_panels)."""
    panels = material_page_panels(d)
    per_page = APART_ACROSS * APART_DOWN
    pages = [panels[k:k + per_page] for k in range(0, len(panels), per_page)]
    out = []
    for p, page in enumerate(pages, 1):
        figure, axes = plt.subplots(APART_DOWN, APART_ACROSS, figsize=APART_PAGE, squeeze=False)
        for k, (title, _, _, kinds) in enumerate(page):
            material_panel(axes[k // APART_ACROSS, k % APART_ACROSS], sum(kinds.values()), title,
                           k % APART_ACROSS == 0)
        for spare in axes.flatten()[len(page):]:
            spare.axis('off')
        figure.suptitle(f'{lead(d)}: each material in one robot, then its grades ({p} of {len(pages)})',
                        fontsize=APART_HEADING, y=0.985)
        # the median and the 95 % interval in a legend under the title (rule 3 of 2026-11-12)
        figure.legend(handles=distribution_handles(d.n), loc='upper center', bbox_to_anchor=(0.5, 0.955), ncol=2,
                      frameon=False, fontsize=APART_TEXT)
        figure.tight_layout(rect=(0, 0, 1, 0.95 - LEGEND_ROW), h_pad=PANEL_GAP, w_pad=2.5)
        out.append((f'{c.name}_materials_{p}.png', figure))
    return out


def alloy_rows(d: Draws) -> list:
    """The rows of a robot type's alloys table (EVIDENCE.md E19 point 4), in the order of the material pages, every
    alloy the type holds in any draw: (the alloy, grade or magnet class in plain words, its material, what it holds by
    its recipe (Draws.holds), its kg in one robot: its median and 95 % interval over the draws that hold it, and in what
    share of the draws where not all (CLAUDE.md §7))."""
    rows = []
    for _, material, detail, kinds in every_material_panel(d):
        kg = sum(kinds.values())
        if material not in TABLE_MATERIALS or detail is None or not kg.any():
            continue
        stats = statistics_of(kg)
        per, unit = panel_unit(kg[kg != 0])
        words = (f"{panel_number(stats['Median (kg)'] / per)} {unit} ({panel_number(stats['2.5 % (kg)'] / per)} to "
                 f"{panel_number(stats['97.5 % (kg)'] / per)})")
        if stats['Held in (% of the draws)'] < 99.5:                   # never '0 %' for what some runs hold
            words += f" in {share_text(stats['Held in (% of the draws)'] / 100)} of the runs"
        label = grade_words(material, detail) or str(detail)
        rows.append((label[0].upper() + label[1:], material, d.holds[(material, detail)], words))
    return rows


def alloys_pages(c: Composition, d: Draws) -> list:
    """A robot type's alloys table, as (file name, figure): its rows (alloy_rows) wrapped in their columns, a row on
    the next page where it would pass the page's foot."""
    cells_of = [[textwrap.fill(text, width) for text, width in zip(row, TABLE_WRAP)] for row in alloy_rows(d)]
    pages, page, y = [], [], TABLE_TOP
    for cells in cells_of:
        height = ROW_GAP + max(cell.count('\n') + 1 for cell in cells) * LINE_HEIGHT
        if page and y - height < TABLE_BOTTOM:
            pages.append(page)
            page, y = [], TABLE_TOP
        page.append(cells)
        y -= height
    if page:
        pages.append(page)
    out = []
    for p, page in enumerate(pages, 1):
        figure = plt.figure(figsize=APART_PAGE)
        figure.suptitle(f'{lead(d)}: its alloys and grades, what each holds ({p} of {len(pages)})',
                        fontsize=APART_HEADING, y=0.985)
        for x, words in zip(TABLE_X, TABLE_HEAD):
            figure.text(x, 0.90, words, fontsize=APART_TEXT, va='top')
        y = TABLE_TOP
        for cells in page:
            figure.add_artist(plt.Line2D([0.03, 0.97], [y + 0.012, y + 0.012], color=GRID, linewidth=1))
            for x, cell in zip(TABLE_X, cells):
                figure.text(x, y, cell, fontsize=APART_TEXT, va='top', linespacing=1.25)
            y -= ROW_GAP + max(cell.count('\n') + 1 for cell in cells) * LINE_HEIGHT
        out.append((f'{c.name}_alloys_{p}.png', figure))
    return out


def source_words(material: str, detail) -> str:
    """The words of a "where it comes from" figure: a grade or alloy on its own ('Gear steel 20CrMnTi', 'Aluminium
    7075', GRADE_TITLES), else its material ('Copper', 'NdFeB magnets')."""
    return GRADE_TITLES.get(detail, detail) if detail else material


def source_file(material: str, detail) -> str:
    """Its file within the parts figures' folder: sources/Gear_steel_20CrMnTi.png."""
    name = '_'.join(''.join(ch if ch.isalnum() else ' ' for ch in source_words(material, detail)).split())
    return os.path.join(SOURCES_FOLDER, f'{name}.png')


def log_mass(log_kg: float, _pos=None) -> str:
    """A tick of a logarithmic mass axis, its power of ten of kg in plain units: '1 mg', '10 g', '1 kg'."""
    kg = 10 ** log_kg
    per, unit = panel_unit(np.array([kg]))
    return f'{panel_number(kg / per)} {unit}'


def sources_figure(title: str, kinds: dict, d: Draws):
    """Where one material sits in a robot type, as RAWCLICDataCenters' "where the copper comes from": one row per kind
    of part holding it (in at least 2.5 % of the draws), the largest median on top; each over the draws in which the
    kind of part holds it, those above 0 (Matthias, 2026-11-01: "It can not be that median is 0. If a value is 0 then it
    is NOT part of the distribution"; CLAUDE.md §7; a draw below zero has no place on a logarithmic axis): the violin
    of its kg on a logarithmic axis, the median a filled dot, the 95 % interval a line (their samples in the page's
    legend; no mean since 2026-11-13: "Not mean, but median"), and at the right the median and in what share of the
    runs the kind of part holds it, as the overview's rows (ridge_panel)."""
    # The draws that hold it, those above 0: a logarithmic axis has no place for a draw below zero (a remainder below
    # zero, a fault the run log and the summary report: type 1's frame aluminium in 72 of 200,000 draws stopped his run
    # of 2026-11-01 when these pages took the draws not 0); the notes page says so.
    holding = {k: kinds[k][kinds[k] > 0] for k in kinds if held(kinds[k])}
    shown = sorted(holding, key=lambda k: float(np.median(holding[k])))
    figure = plt.figure(figsize=APART_PAGE)
    axes = figure.add_axes((0.22, 0.12, SOURCES_WIDTH, 0.76))
    lows = [np.log10(holding[k]).min() for k in shown]
    highs = [np.log10(holding[k]).max() for k in shown]
    left, right = np.floor(min(lows)), np.ceil(max(highs))
    numbers = blended_transform_factory(axes.transAxes, axes.transData)
    for row, kind in enumerate(shown):
        values = holding[kind]
        logs = np.log10(values)
        if logs.max() > logs.min():
            body = axes.violinplot([logs], positions=[row], orientation='horizontal', widths=0.8,
                                  showextrema=False)['bodies'][0]
            body.set_facecolor(VIOLIN)
            body.set_edgecolor('none')
            body.set_alpha(0.6)
        low, high = np.percentile(values, [2.5, 97.5])
        median = float(np.median(values))
        axes.plot([np.log10(low), np.log10(high)], [row, row], color=APART_INK, linewidth=1.6)
        axes.plot(np.log10(median), row, 'o', color=APART_INK, markersize=8)
        per, unit = panel_unit(np.array([median]))
        axes.text(NUMBER_COLUMNS[0], row, f'{panel_number(median / per)} {unit}', transform=numbers, ha='left',
                  va='center', fontsize=APART_TEXT, color=APART_INK)
        axes.text(NUMBER_COLUMNS[1], row, held_share(values.size / kinds[kind].size), transform=numbers, ha='left',
                  va='center', fontsize=APART_TEXT, color=APART_INK)
    for column, what in zip(NUMBER_COLUMNS, ('median', 'held in')):
        axes.text(column, len(shown) - 0.4, what, transform=numbers, ha='left', va='bottom', fontsize=APART_TEXT,
                  color=APART_INK)
    axes.set_yticks(range(len(shown)))
    axes.set_yticklabels([KINDS[k][0] for k in shown], fontsize=APART_TEXT)
    axes.set_ylim(-0.6, len(shown) - 0.4)
    axes.set_xlim(left, right)
    axes.xaxis.set_major_locator(plt.MultipleLocator(1))
    axes.xaxis.set_major_formatter(plt.FuncFormatter(log_mass))
    axes.tick_params(axis='x', labelsize=APART_TEXT)
    axes.tick_params(axis='y', length=0)
    axes.set_xlabel('mass in one robot (logarithmic axis)', fontsize=APART_LABEL)
    axes.grid(axis='x', alpha=0.3)
    for side in ('top', 'right'):
        axes.spines[side].set_visible(False)
    # Its first letter small, but in a name such as NdFeB.
    words = title[0].lower() + title[1:] if title.split()[0][1:].islower() else title
    figure.suptitle(f"{lead(d)}: where its {words} {'sit' if words.endswith('magnets') else 'sits'}",
                    fontsize=APART_HEADING, y=0.96)
    # Its marks in one legend between the title and the panel (rule 3 of 2026-11-12: every mark its sample)
    figure.legend(handles=[plt.Line2D([], [], marker='o', color=APART_INK, linestyle='None', markersize=8,
                                      label=f'Median of {d.n:,} model runs'),
                           plt.Line2D([], [], color=APART_INK, linewidth=1.6, label='95 % interval')],
                  loc='upper center', bbox_to_anchor=(0.5, 0.925), ncol=2, frameon=False, fontsize=APART_TEXT)
    return figure


def sources_pages(d: Draws) -> list:
    """Every "where it comes from" figure, as (file name, figure): copper, the magnets in all, each steel and each
    aluminium alloy (SOURCES_OF), in the order of the material pages: the magnets whole (or their one class), every
    other by its grades or alloys (or whole, where it has one)."""
    panels = material_panels(d)
    single = {m for m in SOURCES_OF if sum(p[1] == m for p in panels) == 1}
    out = []
    for _, material, detail, kinds in panels:
        if material in SOURCES_OF and (material in single or (detail is None) == (material == MAGNETS)):
            out.append((source_file(material, detail), sources_figure(source_words(material, detail), kinds, d)))
    return out


def duration(seconds: float) -> str:
    """A time in plain words, for the lines 02 says while it runs: '0.4 s', '12 s', '3 min 40 s', '1 h 2 min'."""
    if seconds < 10:
        return f'{seconds:.1f} s'
    whole = round(seconds)
    if whole < 60:
        return f'{whole} s'
    if whole < 3600:
        return f'{whole // 60} min {whole % 60} s'
    return f'{whole // 3600} h {whole % 3600 // 60} min'


class Steps:
    """What 02 is doing, said while it runs (Matthias, 2026-10-30: "Information on the working of 02 is poor", "Yes,
    build them"): a line when a step begins, its time when it ends, and the whole run's time last. Every line is
    flushed at once, so that the console shows it while the next step runs (a 200,000-draw run takes minutes)."""

    def __init__(self):
        self.started = self.step = time.perf_counter()

    def begin(self, words: str) -> None:
        """A step begins: its words, and its clock started."""
        self.step = time.perf_counter()
        print(f'{words} …', flush=True)

    def end(self, words: str) -> None:
        """A step ends: `words`, with '{}' where its time goes (e.g. '  read in {}')."""
        print(words.format(duration(time.perf_counter() - self.step)), flush=True)

    def stopped(self) -> int:
        """A fault stopped the run: when, and that nothing is written (02 writes only after every check). Returns 1."""
        print(f'02 stopped after {duration(time.perf_counter() - self.started)}: nothing is written.', file=sys.stderr,
              flush=True)
        return 1

    def done(self) -> int:
        """The run's end: its whole time. Returns 0."""
        print(f'02 done in {duration(time.perf_counter() - self.started)}.', flush=True)
        return 0


# The memory check before a run (Step 3), on the safe side: the trial's draws; its estimate counts the draws kept on the
# disk (DiskArrays) as if all were in memory, and PEAK_FACTOR (what drawing a type holds at its peak, as a multiple of
# what it holds when done: measured 1.2 on robot type 3, set at 2), and the pages' PAGES_MEMORY, so that it is never
# below what the run holds (measured 2026-11-13: 2.4 GB at 50,000 draws against its 3.2); the run stops before any type
# is drawn where that estimate passes MEMORY_SHARE of the computer's memory, the line where it would begin to swap
# (VERIFICATION V236).
MEMORY_TRIAL, MEMORY_SHARE, PEAK_FACTOR = 2000, 0.75, 2.0
# What drawing the pages holds beyond the draws (matplotlib, its images), measured 2026-11-13: about 1 GB at 20,000 to
# 50,000 draws; added to the check so that it never says less than the run holds (VERIFICATION V236).
PAGES_MEMORY = 1.0e9


def held_bytes(value) -> int:
    """The bytes the arrays in `value` hold: an array, a dict, tuple or list of them, a PartBlocks or a record of them."""
    if isinstance(value, np.ndarray):
        return value.nbytes         # its draws on the disk too (DiskArrays), as if all were in memory: the safe side
    if isinstance(value, dict):
        return sum(held_bytes(v) for v in value.values())
    if isinstance(value, (tuple, list)):
        return sum(held_bytes(v) for v in value)
    if isinstance(value, (PartBlocks, Draws)):
        return sum(held_bytes(getattr(value, f.name)) for f in fields(value))
    return 0


def memory_needed(a, category, lists, params: Params) -> tuple:
    """(the bytes drawing robot type `a` will hold at its peak, the bytes of its Composition kept until every type is
    drawn), at params.composition.draws: `a` its ApartInputs, `category` its category of the workbook, `lists` the
    shared lists; from a trial of MEMORY_TRIAL draws, scaled to the draws, the peak times PEAK_FACTOR. Grows with the
    draws and the materials and elements, not with the number of robots (PartBlocks, Shared.keep)."""
    trial = replace(params, composition=replace(params.composition, draws=MEMORY_TRIAL))
    d = draw_taken_apart(a, trial, magnet_fractions(trial, grade_classes(a), MEMORY_TRIAL))
    scale = params.composition.draws / MEMORY_TRIAL
    kept = held_bytes(vars(compose_taken_apart(category, d, lists))) * scale
    return (held_bytes(d) * scale + kept) * PEAK_FACTOR, kept


def memory_in_use() -> float:
    """The bytes this process has held at most so far, as the system counts them (its peak resident memory)."""
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return float(peak if sys.platform == 'darwin' else peak * 1024)   # bytes on macOS, kilobytes elsewhere


def staging_folders(params: Params) -> dict:
    """The staging folder of each output folder 02 writes ('<folder>.writing', beside it), emptied of what a stopped
    run left there and made anew: what 02 writes goes there first and reaches the output folders only when every
    robot type has added up (move_staged). The staging folders hold only 02's own files of this run."""
    staged = {}
    for name in ('composition_dir', 'composition_figures_dir', 'parts_dir', 'parts_figures_dir'):
        folder = absolute(getattr(params.output, name)).rstrip(os.sep) + '.writing'
        if os.path.isdir(folder):
            shutil.rmtree(folder)
        os.makedirs(folder)
        staged[name] = folder
    return staged


def clear_staging(staged: dict) -> None:
    """The staging folders removed, with what this run wrote into them (a run stopped by a fault writes nothing)."""
    for folder in staged.values():
        if os.path.isdir(folder):
            shutil.rmtree(folder)


def move_staged(staged: dict) -> None:
    """Every file of the staging folders moved into its output folder (the folder's name without '.writing'), at the
    same place below it; a file there of the same name replaced, every other file there left as it is; then the
    staging folders, empty, removed."""
    for folder in staged.values():
        target = folder[:-len('.writing')]
        for here, _, names in os.walk(folder):
            into = os.path.join(target, os.path.relpath(here, folder))
            os.makedirs(into, exist_ok=True)
            for name in names:
                os.replace(os.path.join(here, name), os.path.join(into, name))
        shutil.rmtree(folder)


def write_part_by_part(category, d: Draws, a, c, inputs: Inputs, params: Params, staged: dict, with_pages: tuple,
                       steps) -> None:
    """A robot type drawn part by part: its tables part by part, its pages of its robots part by part and its two
    figures with where each material sits (where the settings name its pages), into the staging folders, with the
    reports of its draws."""
    folder = folder_name(category)
    if d.robot_type in with_pages:
        steps.begin(f'Robot type {d.robot_type}: drawing its pages')
        shown = c if not a.later else compose_taken_apart(category, d, inputs.lists)
        draw_taken_apart_pages(shown, d, a.left_out, staged['composition_figures_dir'], params, a.later, a.outliers)
        steps.end('  drawn in {}.')
    steps.begin(f'Robot type {d.robot_type} part by part: writing its draws')
    write_taken_apart(d, os.path.join(staged['parts_dir'], folder))
    steps.end('  written in {}.')
    # The check of the boards' copper against their layers (E51 row 8), reported, not cut.
    print(f'  Robot type {d.robot_type}: its boards\' copper (a share of their mass) above what all their layers can '
          'hold: ' + '; '.join(layer_words(d)), flush=True)
    print(f"  Robot type {d.robot_type} drawn part by part over {len(d.register)} robots of the register's sheet "
          f"Type {d.robot_type}; not drawn (no mass stated): "
          f"{', '.join(f'{r.number} {r.name}' for r in a.left_out) or 'none'}"
          + (f"; not drawn, an outlier: {', '.join(f'{r.number} {r.name}' for r in a.outliers)}"
             if a.outliers else '')
          + (f'; not yet taken apart: {len(a.later)}, so its draws are from the workbook.'
             if a.later else '.'))
    for column, share in below_zero(d).items():
        if share > 0:
            print(f'  {column} is below zero in {100 * share:.1f} % of its draws (reported, not cut).')
    print(f'  Robot type {d.robot_type} part by part written into {params.output.parts_dir}/{folder}/.')
    if d.robot_type in with_pages:
        steps.begin(f'Robot type {d.robot_type} part by part: drawing its two figures and where each material sits')
        draw_parts_figures(d, params, os.path.join(staged['parts_figures_dir'], folder))
        steps.end('  drawn in {}.')
        for symbol, name in FIGURE_ELEMENTS:
            total = sum(by_kind(d, symbol).values())
            per, unit = panel_unit(total)
            mean, median, low, high, held_in = statistics(total / per)   # over the draws that hold it
            if mean is None:
                print(f'  {name} in one robot: in none of the draws')
                continue
            print(f'  {name} in one robot: median {panel_number(median)} {unit}, mean {panel_number(mean)} {unit} '
                  f'(95 %: {panel_number(low)} to {panel_number(high)})'
                  + (f', held in {panel_number(held_in)} % of the draws' if held_in < 100 else ''))
        print(f'  Its two figures and where each material sits drawn into {params.output.parts_figures_dir}/'
              f'{folder}/.')


def run(params: Params) -> int:
    """Reads and checks the inputs, checks the memory each robot type will need, then draws, checks and writes one
    robot type after another into staging folders, and moves everything into the output folders only when every type
    has added up (MEMORY in the docstring at the top). 0 when it has written, 1 when a fault stopped it (nothing
    written). Each step is said as it begins and its time when it ends (Steps)."""
    steps = Steps()
    # Step 1: the inputs.
    steps.begin("Reading the inputs: the workbook, the shared lists, the element recipes, the register, the parts "
                "files of the robot types taken apart and the sibling projects' files")
    try:
        inputs = read_inputs(params)
        path = absolute(params.data.register)
        register = schemas.read_register(path)
        # Each robot type of the register's sheets "Type n": its robots, checked below against its sheet Robots; a
        # type some of whose robots are drawn with their own parts is drawn part by part from its own parts file, each
        # robot from its own rows (Matthias, 2026-10-30, "Yes, build C"); a robot taken apart in another of its types
        # does not make its type one (01's drawn_part_by_part, E10.1 point 2: types 3 and 4 from the workbook).
        sheets = {n: schemas.read_type_sheet(path, n) for n in schemas.type_sheet_numbers(path)}
        files = read_parts_files(params, inputs)
        aparts = {c.number: read_apart_inputs(params, inputs, sheets[c.number], c, files)
                  for c in inputs.book.categories
                  if c.number in sheets and schemas.drawn_part_by_part(sheets[c.number])}
    except schemas.WorkbookError as error:
        print(error, file=sys.stderr)
        return steps.stopped()
    steps.end('  read in {}' + (f" (the parts files of robot types {' and '.join(str(n) for n in aparts)})"
                                if aparts else '') + '.')

    # Step 2: every check of the inputs, 01's and 02's own.
    steps.begin("Checking every input (01's checks and 02's own)")
    named = {n: list(f.robots) for n, f in files.items()}
    faults = (all_faults(inputs, params) + schemas.check_register(register, params, named)
              + schemas.check_type_sheets(path, register, params, named))
    # Each parts file checked once, as its own type's (E11.7 point 6), whichever types draw its robots.
    some = next(iter(aparts.values()), None)
    for t, file in files.items():
        if some is not None:
            faults += apart_faults(file_inputs(some, t, file), params)
    if faults:
        print(f'{len(faults)} fault(s) in the inputs; nothing is drawn. 01_schemas.py shows them on faults.png.',
              file=sys.stderr)
        for fault in faults:
            print(f"  sheet '{fault.sheet}', row {fault.row}: {fault.text}", file=sys.stderr)
        return steps.stopped()
    steps.end('  no fault, in {}.')

    # Step 3: the memory each robot type taken apart will need, from a trial of MEMORY_TRIAL draws, before any is
    # drawn: a type that would hold more than MEMORY_SHARE of this computer's memory stops the run here, nothing drawn
    # (Matthias, 2026-11-13, after 02 held 43 GB on his 16 GB computer: "It must adopte, so if data are added, it still
    # works!!!").
    draws = params.composition.draws
    steps.begin(f'Checking the memory each robot type taken apart needs at {draws:,} draws (a trial of '
                f'{MEMORY_TRIAL:,} draws each)')
    # What the run will hold at most: what this process holds already (the inputs read), the summaries of every type
    # kept until all are drawn, and the largest peak of drawing one type.
    budget = MEMORY_SHARE * os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')
    needs = {n: memory_needed(a, next(c for c in inputs.book.categories if c.number == n), inputs.lists, params)
             for n, a in aparts.items()}
    for n, (peak, kept) in needs.items():
        print(f'  robot type {n}: about {peak / 1e9:.1f} GB at its peak', flush=True)
    total = (memory_in_use() + sum(kept for _, kept in needs.values())
             + max((peak for peak, _ in needs.values()), default=0.0) + PAGES_MEMORY)
    print(f'  the run at most about {total / 1e9:.1f} GB, of {budget / 1e9:.1f} GB ({MEMORY_SHARE:.0%} of this '
          'computer\'s memory)', flush=True)
    if total > budget:
        print(f'The run would need about {total / 1e9:.1f} GB, more than {budget / 1e9:.1f} GB, {MEMORY_SHARE:.0%} of '
              'this computer\'s memory; nothing is drawn.', file=sys.stderr)
        return steps.stopped()
    steps.end('  it fits, in {}.')

    # Step 4: one robot type after another, drawn (part by part where its robots are taken apart, every tenth robot
    # said as it is drawn; from the workbook until all its robots with a mass are taken apart, Q2), its draws checked,
    # its tables part by part and its figures written into the staging folders (staged), and its draws part by part let
    # go before the next type is drawn, so that one type at a time is held (until 2026-11-13 all six at once). What is
    # kept of each type is its draws of the materials and elements (Composition), whose element columns are made the
    # same for all types once all are drawn (same_elements); nothing reaches the output folders unless every type adds
    # up (Step 6).
    staged = staging_folders(params)
    print(f'{draws:,} draws per robot type, seed {params.composition.seed}.', flush=True)
    drawn, taken = [], set()
    with_pages = params.output.robot_types_with_pages   # Matthias, 2026-10-29: "Type 1 only"; type 2 since 2026-10-30
    for category in inputs.book.categories:
        a = aparts.get(category.number)
        d = None
        if a is not None:
            versions = len(a.apart.robots)
            steps.begin(f'Robot type {category.number}: drawing part by part over its {len(a.robots)} robots'
                        + (f' ({versions} with their versions)' if versions != len(a.robots) else '')
                        + f', {draws:,} draws')
            magnets = magnet_fractions(params, grade_classes(a), draws)
            d = draw_taken_apart(a, params, magnets,
                                 say=lambda done, of, name: print(f'  robot {done} of {of} drawn: {name}', flush=True))
            taken.add(category.number)
            c = compose_taken_apart(category, d, inputs.lists) if not a.later else None
            steps.end('  done in {}.')
        if a is None or a.later:
            steps.begin(f'Robot type {category.number}: drawing from the workbook, {draws:,} draws'
                        + (' (its draws until all its robots with a mass are taken apart)'
                           if a is not None else ''))
            c = compose(category, inputs, params)
            steps.end('  done in {}.')
        # Its draws checked; nothing is written unless all add up.
        steps.begin(f'Robot type {category.number}: checking that its draws add up')
        problems = draw_faults(c)
        if problems:
            print('The draws do not add up; nothing is written.', file=sys.stderr)
            for problem in problems:
                print(f'  {problem}', file=sys.stderr)
            clear_staging(staged)
            return steps.stopped()
        for report in remainder_reports(c):
            print(f'  robot type {c.number}: {report} (reported, not cut).', flush=True)
        steps.end('  they add up, in {}.')
        if d is not None:
            write_part_by_part(category, d, a, c, inputs, params, staged, with_pages, steps)
            del d   # its draws part by part let go: one robot type at a time in memory
            gc.collect()
        drawn.append(c)

    # Step 5: every robot type's draws of the materials and elements, their element columns the same for all
    # (same_elements), written with their pages into the staging folders.
    same_elements(drawn)
    for c in drawn:
        steps.begin(f'Robot type {c.number}: writing its draws')
        write(c, os.path.join(staged['composition_dir'], c.name))
        steps.end('  written in {}.')
        if c.number in with_pages and c.number not in taken:
            steps.begin(f'Robot type {c.number}: drawing its page')
            draw_page(c, params.composition.draws, os.path.join(staged['composition_figures_dir'], c.name + '.png'),
                      params)
            steps.end('  drawn in {}.')
        rows = {r['Name']: r for r in summary(c) if r['Kind'] == 'Material'}
        stats = statistics_of(c.column('total', 'Total'))
        partly = [name for name, r in rows.items() if r['In the elements'] == 'Partly']
        kept = [name for name, r in rows.items() if r['In the elements'] == 'No' and name != NOT_ALLOCATED]
        print(f"  {c.number} {c.title}: {stats['Mean (kg)']:.1f} kg at the mean (95 %: {stats['2.5 % (kg)']:.1f} to "
              f"{stats['97.5 % (kg)']:.1f}); Not allocated below zero in "
              f"{rows[NOT_ALLOCATED]['Draws below zero (%)']:.1f} % of the draws; elements of interest in part: "
              f"{', '.join(partly) or 'none'}; staying materials: {', '.join(kept) or 'none'}.")

    # Step 6: every type has added up: everything staged moved into the output folders, a file there of the same name
    # replaced, every other file there left as it is.
    steps.begin('Moving what is written into the output folders')
    move_staged(staged)
    steps.end('  moved in {}.')
    print(f'Written into {params.output.composition_dir}/, one folder per robot type, and the pages into '
          f'{params.output.composition_figures_dir}/.')
    # Step 7: the whole run's time.
    return steps.done()


def main() -> int:
    """Press Run: the settings of src/params_schema.py, checked, then run()."""
    try:
        params = current()
    except ParameterError as error:
        print(error, file=sys.stderr)
        return 1
    return run(params)


if __name__ == '__main__':
    raise SystemExit(main())
