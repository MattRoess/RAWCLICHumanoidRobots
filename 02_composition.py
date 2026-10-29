"""
02_composition.py
=================

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

What each robot type is made of, drawn at random (Monte Carlo): its materials, its elements, its part groups and its
body regions, kg per robot, written for stock-and-flow, each robot type on its own. Press Run. No arguments; every
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

The register (`data.register`): its sheet Robots, every known humanoid robot with its robot types, and its sheet
Type 1, every robot of type 1 with what this run does with it (Matthias, 2026-10-29: "I want the all the know type 1
robots are integrated and included in the run", "There has to be an excel sheet where all the robots of the different
types are fully listed. For now it has to be just all for type 1."). Where the robots of the sheet Type 1 have rows of
their own in the parts file (`data.parts_taken_apart`: all of them since 2026-10-29), type 1 is drawn over the robots
of that sheet, each from its own rows; for it 02 also reads the sibling projects' files where they lie
(RAWCLICVehicleElectronics' board metals and sensor elements, RAWCLICDataCenters' tantalum,
RAWCLICVehicleTractionMotor's steels) and runs RAWCLICVehicleTractionMotor's own code in its own environment for the
elements of the magnets.

WHAT IT CHECKS
--------------
Before drawing, every check of 01 (the list is `CHECKS_DONE` in 01_schemas.py) and its own, `check_composition`: an
item that follows a cell's energy sits only in the recipe of NMC cells. Any fault stops it before anything is written;
01's faults.png shows them. After drawing, in every draw (`draw_faults`): the materials and Not allocated add up to the
parts, and so do the part groups and the body regions; the elements add up to the materials that have recipes; the
cells and the rest add up to the battery row; nothing is below zero except Not allocated. A fault there stops it too.

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
  - Not allocated: the parts minus the materials, draw by draw. It is below zero where the drawn materials exceed the
    drawn parts (recommendation b); the summary gives the share of draws where it is.
  - Materials without a recipe yet: their kilograms are drawn, their elements are not, and the summary says so
    (point 9 and recommendation c). A recipe added later needs no change here.
Each robot type has random numbers of its own, from the seed and its number, so that it gives the same draws however
many robot types are drawn. Nothing is normalised.

HOW IT DRAWS ROBOT TYPE 1 (Matthias, 2026-10-28: "Yes in 02 it is all type 1 in.!"; 2026-10-29: "Yes, build it")
-----------------------------------------------------------------------------------------------------------
  - Each draw is one of the robots of the register's sheet Type 1, all equally often; those without a stated mass
    are not drawn (named on the notes page; the sheet says "not drawn"). A robot in several versions (the Booster K1,
    5 Ah and 2 Ah) is one of them, each as often (a discrete state). Its mass: a triangle on its own mass in the parts
    file (its sheet Constants); its parts: its own rows of the parts file, part by part, nothing scaled from another
    robot.
  - The joints: each component of the G1's joint (sheet JointParts) drawn once in each draw for each joint size and
    shared by all the joints of that size; the large joint's the small one's grams times its factor. A joint whose
    module mass is given: its module mass drawn, its inside the G1's of its size times the module mass over the G1
    joint's mass at its modes, and the joint's structure (housing, end caps, output flange, small bearings) the
    explicit remainder, so that the joint weighs its drawn module mass. A robot whose sources give no joint torques:
    its joint modules one share of its mass, drawn, split among its joints by their fixed shares (EVIDENCE.md E5.17
    point 1). The G1's and G1+'s joints: as weighed.
  - A part of shares (sheet Shares): each share a triangle, the remainder 1 minus the others. Elements: aluminium and
    plastics by type 1's recipes, the NMC cells by theirs with the energy per kg drawn; copper is copper; a part of
    steel, titanium or a copper alloy by its grade (a recipe of the element recipes, or a steel of
    RAWCLICVehicleTractionMotor's workbook read where it lies, each element a triangle, iron the remainder); a
    material or grade written 'A or B' is either, each as often, the same in every place of a draw; the magnets by
    the grade class drawn for their joint's heat group (sheet MagnetGrades), one draw of heat deciding for every joint
    how hot the robot is built for; boards: copper their mass times the copper share, gold, silver, palladium, tin and
    nickel their area times the car board category's mg per cm2, tantalum their mass times the data centres' share;
    sensors: their car sensor elements (a sensor without a mass from its sources: its elements only).
  - The battery: its energy its voltage times its capacity, or, where its sources give neither, its energy per kg of
    robot times its mass; its cells the energy over the cells' energy per kg; its housing the pack less its cells and
    its management board, the pack its stated mass or its energy over a pack's energy per kg (a pack lighter than its
    cells, the Asimov's: no housing). The shell, where no source weighs it: a share of the robot's mass. The cables:
    their length times the four conductors' cross-sections times copper's density, and their insulation. The frame:
    the robot's mass less every other part; where it falls below zero it is reported, not cut.
  - Its part groups and body regions: its ten kinds of part placed whole (KIND_PART_GROUP, KIND_BODY_REGION), kept so
    on his word (2026-10-29, "Yes, build them", point 5). A robot of two types is drawn in full in each (point 6).

WHAT IT WRITES
--------------
For each robot type, into `output.composition_dir`/<n>_<name>/ (`data/consolidated/`, the folder another repository
reads; not in git):

  materials.npy, elements.npy, part_groups.npy, body_regions.npy, total.npy
        the draws, kg per robot, float32, one row per draw (point 10, the format of RAWCLICVehicleTractionMotor:
        recommendation e). Each has its columns, one name per line, in the .txt of the same name. Row i is the same
        draw in every array, so that stock-and-flow can pair them.
  summary.xlsx, summary.csv
        per material and per element: the mean, the median and the 95 % interval (2.5 % and 97.5 %), the share of
        draws below zero, and how much of each material is in the elements (point 11).

For robot type 1 also, into `output.parts_dir` (`data/parts_taken_apart/`): robots.npy (the robot of the
parts file each draw is, its mass, the robot of the register drawn), parts.npy, materials.npy, grades.npy,
elements.npy and estimated.npy (every element in every kind of part, and its kg resting on masses labelled E), each
with its columns in the .txt of the same name; register.txt (the robots of the register drawn) and summary.csv.

Every robot type has the same columns of elements, all those any of them holds (0 where a robot type's materials hold
none so far). Pages only of the robot types `output.robot_types_with_pages` names (Matthias, 2026-10-29: "Type 1
only"); the draws of all six are written. Into `output.composition_figures_dir` (`figures/composition/`; not in git):
for robot type 1 its notes (<n>_<name>_notes_<k>.png), its elements nine a page (<n>_<name>_elements_<k>.png) and its
materials nine a page (<n>_<name>_materials_<k>.png: the steels by grade, the aluminium by alloy, the permanent magnets
in all and by grade class; Matthias, 2026-10-29: "how much Copper and especially permanent magnets. The different
steels and aluminum alyoys"), each as its total in one robot over the draws; for another robot type one page,
<n>_<name>.png: its kg by material and its kg by element, each bar the mean with a line over 95 % of the draws (point
14). Into `output.parts_figures_dir` (`figures/parts_taken_apart/`): robot type 1's two figures of where its critical
elements sit, kind of part by kind of part (robot_type_1_elements_<k>.png, robot_type_1_overview_<k>.png; the stage 04
until 2026-10-29, "Yes, into 02"), and sources/<material>.png, where copper, the magnets, each steel and each
aluminium alloy sit, as RAWCLICDataCenters' "where the copper comes from". The draws behind the material pages are
written with type 1's other tables: grades.npy, each material by grade, alloy or magnet class in every kind of part.

Where it sits: after 01_schemas.py. 03_comparison.py reads what it writes (after robot type 6).
"""

from __future__ import annotations

import csv
import importlib.util
import os
import subprocess
import sys
import tempfile
import textwrap
from dataclasses import dataclass

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
from matplotlib.transforms import blended_transform_factory  # noqa: E402

Fault = schemas.Fault
NOT_ALLOCATED, BATTERY, SPLIT = schemas.NOT_ALLOCATED, schemas.BATTERY, schemas.SPLIT
KEPT, BUILD, REST = schemas.KEPT, schemas.BUILD, schemas.REST

# The draws written for each robot type, in this order: each is a file <name>.npy with its columns in <name>.txt.
TABLES = ('materials', 'elements', 'part_groups', 'body_regions', 'total')
# The columns of summary.csv and summary.xlsx.
SUMMARY_HEADINGS = ['Robot type', 'Kind', 'Name', 'Mean (kg)', 'Median (kg)', '2.5 % (kg)', '97.5 % (kg)',
                    'Draws below zero (%)', 'In the elements', 'In the elements, mean (kg)']
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
    tables: dict              # one of TABLES -> (its columns, its draws: N rows × one column each), kg
    in_elements: np.ndarray   # N rows × the columns of 'materials': the kilograms of each that follow a recipe
    battery: dict | None      # 'row', 'cells', 'rest': the battery row and its parts in every draw; None without one
    build: np.ndarray | None  # the build of the battery drawn in every draw, as its place among the robot type's
    #                           builds in the sheet Battery cells; None where the battery row is kept or not built

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
    recipe, where there is no cell to take the energy from. And every element left off the pages
    (`composition.elements_not_shown`) is an element of 01's atomic masses, so that a slip of the pen cannot leave one
    on the pages unnoticed."""
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
    for symbol in params.composition.elements_not_shown:
        if symbol not in schemas.ATOMIC_MASS:
            faults.append(Fault('src/params_schema.py: composition.elements_not_shown', 0,
                                f"'{symbol}' is not an element of 01's atomic masses."))
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
        self.members: dict = {}   # (recipe, the item they sit within, '' for the recipe itself) -> its items
        for i in recipes.items:
            self.members.setdefault((i.recipe, i.within), []).append(i)
        self.shares: dict = {}    # (recipe, item) -> the item's share in every draw
        self.states: dict = {}    # (recipe, group) -> the alternative drawn in every draw, as its place in the group
        self.done: dict = {}      # recipe -> its element shares, for a recipe drawn without a cell's energy

    def share(self, item, f: np.ndarray | None) -> np.ndarray:
        """One item's share of what it sits within, in every draw: its mode × f where it follows the energy, else a
        triangle drawn once."""
        if item.follows_energy:
            if f is None:   # check_composition prevents it
                raise ValueError(f'{item.recipe}, {item.item}: it follows the energy, but no cell is drawn here.')
            return item.share[1] * f
        key = (item.recipe, item.item)
        if key not in self.shares:
            self.shares[key] = triangle(self.rng, *item.share, self.n)
        return self.shares[key]

    def elements(self, recipe: str, f: np.ndarray | None = None) -> dict:
        """The mass share of each element in `recipe`, in every draw: element -> N shares, adding up to 1 in every draw
        (to the rounding of the compounds). `f`: a cell's energy per kg over the mode of the NMC cells, in every draw,
        for a cell recipe whose items follow the energy."""
        if f is None and recipe in self.done:
            return self.done[recipe]
        out: dict = {}
        self.add(recipe, '', np.ones(self.n), f, out)
        if f is None:
            self.done[recipe] = out
        return out

    def parts_of(self, recipe: str, within: str, f: np.ndarray | None) -> list:
        """The items of `recipe` that sit within `within`, each with its share of it in every draw: of alternatives
        the one drawn takes the whole; of shares each is drawn, the remainder 1 minus the others."""
        items = self.members[(recipe, within)]
        if items[0].probability is not None:
            # Alternatives: one is drawn in each draw, by its probability; it takes the group's whole weight.
            key = (recipe, within)
            if key not in self.states:
                self.states[key] = self.rng.choice(len(items), size=self.n, p=[i.probability for i in items])
            return [(i, (self.states[key] == k).astype(float)) for k, i in enumerate(items)]
        # Shares: each drawn, the remainder 1 minus the others, never below zero (01 checks the largest shares).
        parts = [(i, self.share(i, f)) for i in items if not i.remainder]
        rest = 1 - sum(share for _, share in parts) if parts else np.ones(self.n)
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
        weight = np.ones(self.n) if weight is None else weight
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

    def add(self, recipe: str, within: str, weight: np.ndarray, f: np.ndarray | None, out: dict) -> None:
        """Adds to `out` the elements of the items of `recipe` that sit within `within`, which make up `weight` of the
        recipe in every draw."""
        for i, share in self.parts_of(recipe, within, f):
            part = weight * share
            if i.compound in self.recipes.compounds:
                for element, mass_share in schemas.composition(self.recipes.compounds[i.compound][0]).items():
                    out[element] = out.get(element, 0) + part * mass_share
            elif i.compound:   # another recipe, drawn once for the robot type
                for element, mass_share in self.elements(i.compound).items():
                    out[element] = out.get(element, 0) + part * mass_share
            else:              # a group of items within this one
                self.add(recipe, i.item, part, f, out)


def element_names(recipes) -> list:
    """Every element the compounds of the recipes hold, in the order of the periodic table: the same columns for every
    robot type."""
    found = set()
    for written, _ in recipes.compounds.values():
        found |= set(schemas.composition(written))
    return [element for element in schemas.ATOMIC_MASS if element in found]


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

    # The elements (point 7) of every piece that has a recipe. A piece of Not allocated stays out: Not allocated is
    # the parts minus the materials (point 8).
    materials = lists.names[schemas.MATERIAL]
    kg_of = {name: np.zeros(n) for name in materials}
    with_recipe = {name: np.zeros(n) for name in materials}
    elements_found = element_names(recipes)
    elements = {name: np.zeros(n) for name in elements_found}
    draws = RecipeDraws(recipes, rng, n)
    for piece in pieces:
        if piece.shared == NOT_ALLOCATED:
            continue
        kg_of[piece.shared] += piece.kg
        if piece.recipe:
            with_recipe[piece.shared] += piece.kg
            for element, share in draws.elements(piece.recipe, piece.f).items():
                elements[element] += piece.kg * share
    kg_of[NOT_ALLOCATED] = total - sum(kg_of[name] for name in materials if name != NOT_ALLOCATED)

    tables = {'materials': (materials, stack(materials, kg_of, n)),
              'elements': (elements_found, stack(elements_found, elements, n)),
              'part_groups': (lists.names[schemas.PART_GROUP], stack(lists.names[schemas.PART_GROUP], groups, n)),
              'body_regions': (lists.names[schemas.BODY_REGION], stack(lists.names[schemas.BODY_REGION], regions, n)),
              'total': (['Total'], total[:, None])}
    return Composition(number, folder_name(category), category.name, tables, stack(materials, with_recipe, n),
                       battery, build)


# ------------------------------------------------------------------------------------------------------
# What is checked in every draw, and what is written
# ------------------------------------------------------------------------------------------------------

def draw_faults(c: Composition) -> list:
    """Point 12, in every draw: the materials and Not allocated add up to the parts, and so do the part groups and the
    body regions; the elements add up to the materials that have recipes; the cells and the rest add up to the battery
    row; nothing is below zero except Not allocated. Each fault says in how many draws."""
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
    followed = c.in_elements.sum(axis=1)
    count(np.abs(c.tables['elements'][1].sum(axis=1) - followed) > COMPOUND_TOLERANCE * followed,
          'the elements do not add up to the materials that have recipes')
    if c.battery is not None:
        row = c.battery['row']
        count(np.abs(c.battery['cells'] + c.battery['rest'] - row) > SUM_TOLERANCE * np.abs(row),
              'the cells and the rest do not add up to the battery row')
    for table in ('materials', 'elements', 'part_groups', 'body_regions'):
        columns, draws = c.tables[table]
        for i, name in enumerate(columns):
            if name != NOT_ALLOCATED:
                count(draws[:, i] < 0, f'{name} is below zero')
    return faults


def statistics_of(draws: np.ndarray) -> dict:
    """The mean, the median, the 95 % interval and the share of draws below zero of one quantity."""
    low, median, high = np.percentile(draws, [2.5, 50, 97.5])
    return {'Mean (kg)': float(draws.mean()), 'Median (kg)': float(median), '2.5 % (kg)': float(low),
            '97.5 % (kg)': float(high), 'Draws below zero (%)': float((draws < 0).mean() * 100)}


def summary(c: Composition) -> list:
    """Point 11: per material and per element of one robot type its statistics; for each material whether it is in
    the elements (Yes, Partly, No), and its kilograms that are, at the mean. One dict per row, keyed by
    SUMMARY_HEADINGS."""
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
                     'In the elements': status, 'In the elements, mean (kg)': float(followed.mean())})
    columns, draws = c.tables['elements']
    for i, name in enumerate(columns):
        rows.append({'Robot type': c.number, 'Kind': 'Element', 'Name': name, **statistics_of(draws[:, i]),
                     'In the elements': '', 'In the elements, mean (kg)': None})
    return rows


def write(c: Composition, folder: str) -> None:
    """Points 10 and 11: the draws of one robot type, float32, each table with its columns, and its summary."""
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
    for letter, width in zip('ABCDEFGHIJ', (11, 9, 24, 11, 11, 11, 11, 12, 22, 14)):
        sheet.column_dimensions[letter].width = width
    sheet.freeze_panes = 'A2'
    book.save(os.path.join(folder, 'summary.xlsx'))


# ------------------------------------------------------------------------------------------------------
# Robot type 1 over its robots, each part by part
# ------------------------------------------------------------------------------------------------------

TYPE_ONE = 1   # the robot type of the workbook's Taxonomy whose robots the data file holds

# The ten kinds of part of the figures with their names and colours, and the kind of a joint by the first word of its
# name: 01's (one copy, drawn by 01's page of robot type 1 too).
KINDS, JOINT_KIND = schemas.KINDS, schemas.JOINT_KIND
# The kind of a part, board or sensor, by its column "Kind (the figure's row)".
KIND_OF = {'Hips': 'hips', 'Knees': 'knees', 'Waist': 'waist', 'Arms': 'arms', 'Battery pack': 'battery',
           'Torso boards': 'boards', 'Head': 'head', 'Cables': 'cables', 'Frame and shell': 'frame'}
# The values of that column that are the joints themselves, or sit in them (driver boards, encoders): drawn with the
# joints, joint kind by joint kind.
IN_THE_JOINTS = {'Ankles and arms', 'Hips, knees and waist', 'Hips, knees, waist and shoulders', 'In the joints'}

# How a part of the sheet Parts is computed, by the start of its column "Remainder of, or computed from".
FROM_JOINTS = ('the sum of JointParts', "the Joints' module masses",   # the joint modules: drawn with the joints
               "the Joints' shares")
FROM_SENSORS = 'Sensors and SensorElements'                            # the encoders: their elements only
PACK = 'its cells, its management board'                               # the battery pack: its cells and housing
CELLS = 'from the energy'                                              # the battery cells
HOUSING = schemas.PACK_REMAINDER                                       # the battery housing: a remainder
CABLES = 'from Constants: length'                                      # the cables' conductors and insulation
SHELL = schemas.ROBOT_SHARE                                            # the shell: a share of the robot's mass
FRAME = schemas.ROBOT_REMAINDER                                        # the frame: the robot's remainder
COMPUTED = FROM_JOINTS + (FROM_SENSORS, PACK, CELLS, HOUSING, CABLES, SHELL, FRAME)

# The JointParts component whose material is the joint's driver board.
DRIVER_BOARD = 'Driver board'
# The joint's structure: the JointParts components that are the explicit remainder of a joint whose module mass is
# stated (the X1's, the N1's), split among them in the G1's weighed proportions at their modes. Aluminium and steel,
# no copper or magnets; the housing alone was too small (below zero in 5.8 % of the large joints' draws, V57).
STRUCTURE = ('Housing', 'Two end caps', 'Output flange', 'Two small bearings')
# The recipes of type 1's aluminium and plastics: those its workbook rows of these families follow (sheet Rows of the
# element recipes); and the recipe of the battery cells (the sheet Parts: "element_recipes.xlsx NMC cylindrical").
RECIPE_FAMILY = {'Aluminium': 'Aluminum alloys', 'Plastics': 'Engineering polymers'}
CELL_RECIPE = 'NMC cylindrical'
COPPER, MAGNETS, CELL_MATERIAL, ELECTRONICS = 'Copper', 'Magnets (NdFeB)', 'Battery materials', 'Electronics'
# The steel of the sibling's element workbook whose modes are a producer's typical values, the compound of the element
# recipes that holds them (EVIDENCE.md E5.18: "304 ... modes Outokumpu's typical C 0.04, Cr 18.1, Ni 8.1"); every other
# element of a sibling steel has the middle of its range as its mode (E), its remainder (iron) 1 minus the others.
SIBLING_MODES = {'Type 304': 'Stainless steel 304'}
# The materials of type 1 shown by their alloys on the material pages, through the recipes type 1's rows name (Matthias,
# 2026-10-29: "The different steels and aluminum alyoys"); plastics are shown whole.
ALLOYS = ('Aluminium',)

# The quantities of the sheet Constants this stage uses, as the sheet writes them.
ROBOT_MASS, CABLE_LENGTH = schemas.APART_ROBOT_CONSTANTS
VOLTAGE, CAPACITY = schemas.BATTERY_CONSTANTS
JOINT_SHARE, ENERGY_PER_KG = schemas.JOINT_SHARE, schemas.ENERGY_PER_KG
PACK_WH_PER_KG, SHELL_SHARE = schemas.PACK_WH_PER_KG, schemas.SHELL_SHARE
BOARD_G_PER_CM2, BOARD_COPPER = 'Board mass per cm2 (boards not weighed)', "Copper share of a board's mass"
POWER_CS, SIGNAL_CS = 'Power conductor cross-section (2 conductors)', 'Signal conductor cross-section (2 conductors)'
DENSITY, INSULATION = 'Copper density', 'Insulation and jackets, per mass of copper'
SENSOR_ALUMINIUM = 'Sensor housing, aluminium share'   # of a sensor module beyond its elements (point 3c)
BOARD_GLASS, BOARD_BROMINE = schemas.BOARD_GLASS, schemas.BOARD_BROMINE   # of a board's rest (point 3b)
GLASS_RECIPE, EPOXY_RECIPE = schemas.BOARD_REST_RECIPES

# The critical elements whose kilograms resting on estimates (E) are followed, for the overview figure (its hatching).
TRACKED = {'Cu', 'Al', 'Ag', 'Au', 'Pd', 'Ta', 'Nd', 'Pr', 'Dy', 'Ga', 'In'}

# What is written of robot type 1 part by part, in this order: each a file <name>.npy with its columns in
# <name>.txt.
APART_TABLES = ('robots', 'parts', 'materials', 'grades', 'elements', 'estimated')

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
    """Everything 02 reads for robot type 1, drawn part by part."""

    base: object          # Inputs: the workbook, the shared lists and the element recipes
    apart: object         # schemas.PartsTakenApart: the robots of type 1, part by part
    pcb: dict             # car board category -> element -> (min, mode, max), mg per cm2 of board
    sensor_types: dict    # car sensor type -> element -> (min, mode, max), mg per unit
    tantalum: tuple       # kg of tantalum per kg of board: min, mode, max
    steels: dict          # the sibling's steels: grade -> ({element: (min, max)}, its remainder element)
    robots: list          # the robots of the register's sheet Type 1 drawn (schemas.RegisterRobot), each with a mass
    left_out: list        # the robots of the sheet Type 1 not drawn: no mass stated


def read_apart_inputs(params: Params, base: Inputs, register: list) -> ApartInputs:
    """The parts file and the sibling projects' files, read with 01's functions, beside 02's inputs (`base`) and the
    robots of the register's sheet Type 1 (`register`); those with a stated mass are drawn. Raises
    schemas.WorkbookError when a file cannot be read."""
    apart = schemas.read_parts_taken_apart(absolute(params.data.parts_taken_apart))
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
    of_type = [r for r in register if TYPE_ONE in r.types]
    drawn = [r for r in of_type if None not in r.mass]
    return ApartInputs(base, apart, pcb, sensor_types, tantalum, steels, drawn, [r for r in of_type if r not in drawn])


def weighed_boards(apart) -> list:
    """The small joint's driver boards whose area the parts file gives (the G1's, weighed, and the G1+'s, the G1's
    own): the area every joint's driver board is scaled from."""
    return [b for b in apart.boards if b.kind in IN_THE_JOINTS and 'small' in b.name and None not in b.bounds]


def check_parts(inputs: ApartInputs) -> list:
    """The checks 02 adds to 01's for robot type 1: the small joint's driver board's area given, and the same wherever
    given; every joint, part, board and sensor goes to a kind of part; every part computed in a way 02 knows; every
    robot of type 1; the driver board a component of JointParts; the recipes it uses there; the tantalum row read."""
    apart, faults = inputs.apart, []
    on = 'parts_taken_apart.xlsx: '
    weighed = weighed_boards(apart)
    if not weighed or any(b.bounds != weighed[0].bounds for b in weighed):
        given = ', '.join(f'{b.robot} {b.bounds}' for b in weighed) or 'none'
        faults.append(Fault(on + 'Boards', 0, "the small joint's driver board needs its area, the same wherever it is "
                                              f'given: {given}.'))
    for robot in apart.robots.values():
        if robot.type != TYPE_ONE:
            faults.append(Fault(on + 'Robots', robot.row, f'{robot.name} is of type {robot.type}; the robots of the '
                                                          f'parts file are of type {TYPE_ONE} only.'))
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
    for shared, family in RECIPE_FAMILY.items():
        if (TYPE_ONE, family, shared) not in rows:
            faults.append(Fault('element_recipes.xlsx: Rows', 0, f"no recipe for type {TYPE_ONE}'s {shared} "
                                                                 f"('{family}')."))
    if None in inputs.tantalum:
        faults.append(Fault('data.data_center_element_composition', 0, 'no Ta row with min, mode and max.'))
    return faults


def apart_faults(inputs: ApartInputs, params: Params) -> list:
    """The faults of robot type 1 part by part: 01's checks of the parts file (18 and 19), of the sibling files, of the
    grades, and check_parts. (02's own and the register's are in all_faults.)"""
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

@dataclass
class Draws:
    """Robot type 1, drawn N times, each draw one of its robots."""

    n: int
    robots: list          # the robots of the parts file, in the order of its sheet Robots (a version each)
    robot: np.ndarray     # the robot of the parts file each draw is, as its place in `robots`
    mass: np.ndarray      # kg: that robot's mass in each draw
    parts: tuple          # (columns '<robot>: <part>', N × columns): kg of all units of each row of each robot
    remainders: list      # the columns of `parts` that are remainders (frames, battery housings)
    structures: dict      # '<robot>: <joint> structure' -> kg of one joint's structure, a remainder (0 elsewhere)
    materials: tuple      # (columns (kind, material), N × columns): kg
    elements: dict        # (kind, element) -> kg in each draw
    estimated: dict       # (kind, element) -> the part of those kg resting on masses labelled E (TRACKED elements)
    hot: dict             # kind of joint -> True where its magnets are for 150 °C or more in most draws
    heat: np.ndarray      # the draw of heat, 0 to 1, that decides every heat group's grade class (tied)
    grades: dict          # heat group -> the grade class drawn in each draw
    followed: dict        # material -> kg of its elements drawn in each draw (02's "in the elements")
    details: dict = None  # (kind, material, grade, alloy or magnet class; '' for none) -> kg in each draw
    register: list = None          # the register's robots drawn, '<number> <name>', in their order
    register_robot: np.ndarray = None   # the robot of the register of each draw, as its place in `register`
    on_estimates: dict = None      # what rests on estimates (E) -> the robots it does, for the notes page


class Shared:
    """What is drawn once in each of the N draws and shared by every robot: the joint's components, the shares, the
    constants for all robots, the recipes and grades, the alternatives, the sibling projects' metals and elements, the
    cells' energy per kg."""

    def __init__(self, inputs: ApartInputs, params: Params, magnets: dict, rng: np.random.Generator, n: int):
        apart = inputs.apart
        self.rng, self.n = rng, n
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
                         apart.constants.get(schemas.ALL_ROBOTS, {}).items()}
        # The board metals per cm2 by car board category, the tantalum per kg of board, the sensor elements per unit.
        self.pcb = {(category, element): triangle(rng, *inputs.pcb[category][element], n)
                    for category in sorted({b.category for b in apart.boards})
                    for element in schemas.BOARD_METALS}
        self.tantalum = triangle(rng, *inputs.tantalum, n)
        self.sensor = {(car_type, element): triangle(rng, *values, n)
                       for car_type in sorted({e[2] for e in apart.elements})
                       for element, values in inputs.sensor_types[car_type].items()}
        # The recipes: type 1's aluminium and plastics; the NMC cells with their energy per kg drawn; the grades (a
        # recipe of the element recipes, or a steel of the sibling's workbook), each drawn once and used wherever it
        # sits.
        settings = params.composition
        self.wh_per_kg = triangle(rng, settings.nmc_wh_per_kg_min, settings.nmc_wh_per_kg_mode,
                                  settings.nmc_wh_per_kg_max, n)
        self.recipes = RecipeDraws(inputs.base.recipes, rng, n)
        rows = {(r.robot, r.family, r.shared): r.recipe for r in inputs.base.recipes.rows or []}
        self.recipe_name = {shared: rows[(TYPE_ONE, family, shared)] for shared, family in RECIPE_FAMILY.items()}
        self.recipe = {shared: self.recipes.elements(name) for shared, name in self.recipe_name.items()}
        self.recipe[COPPER] = {'Cu': np.ones(n)}
        self.cells = self.recipes.elements(CELL_RECIPE, self.wh_per_kg / settings.nmc_wh_per_kg_mode)
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
        small = weighed_boards(apart)[0]
        board = next(c for c in apart.joint_parts if c.name == DRIVER_BOARD)
        self.board_area = {'small': triangle(rng, *small.bounds, n)}
        self.board_area['large'] = self.board_area['small'] * self.joint['large'][DRIVER_BOARD] / (board.grams / 1000)

    def state(self, written: str) -> np.ndarray:
        """Which of 'A or B' each draw is, as its place: each as often, drawn once for the written cell and used
        wherever it is written (a discrete state, never blended: the electrical steel of the stator and the rotor is
        one grade in a draw)."""
        if written not in self.states:
            self.states[written] = self.rng.integers(len(schemas.alternatives(written)), size=self.n)
        return self.states[written]

    def grade_leaves(self, grade: str) -> dict:
        """What a grade or a recipe is made of, for the material pages: the recipes it holds and their share in every
        draw (RecipeDraws.leaves); a steel of the sibling's workbook is itself."""
        if grade not in self.split:
            self.split[grade] = {grade: np.ones(self.n)} if grade in self.steels else self.recipes.leaves(grade)
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
                out = {e: triangle(self.rng, low, typical.get(e, (low + high) / 2), high, self.n)
                       for e, (low, high) in elements.items() if high > 0}
                out[remainder] = 1 - sum(out.values())
                self.graded[grade] = out
        return self.graded[grade]


class Robot:
    """One robot's draws (its rows of the N draws), added up as they are drawn."""

    def __init__(self, name: str, rows: np.ndarray, shared: Shared, mass: np.ndarray):
        self.name, self.rows, self.shared, self.mass = name, rows, shared, mass
        self.n = rows.size
        self.parts: dict = {}       # part column -> kg
        self.materials: dict = {}   # (kind, material) -> kg
        self.elements: dict = {}    # (kind, element) -> kg
        self.estimated: dict = {}   # (kind, element) -> kg resting on masses labelled E
        self.structures: dict = {}  # '<robot>: <joint> structure' -> kg of one joint's structure
        self.followed: dict = {}    # material -> kg of its elements drawn
        self.details: dict = {}     # (kind, material, grade, alloy or magnet class; '' for none) -> kg

    def of(self, values: np.ndarray) -> np.ndarray:
        """This robot's rows of draws shared by all robots."""
        return values[self.rows]

    def element(self, kind: str, element: str, kg: np.ndarray, estimate: bool, material: str) -> None:
        """kg of one element in a kind of part, held by `material` (02's "in the elements" of that material)."""
        self.elements[(kind, element)] = self.elements.get((kind, element), 0) + kg
        self.followed[material] = self.followed.get(material, 0) + kg
        if estimate and element in TRACKED:
            self.estimated[(kind, element)] = self.estimated.get((kind, element), 0) + kg

    def material(self, part: str, kind: str, material: str, kg: np.ndarray, estimate: bool, heat_group: str = '',
                 grade: str = '') -> None:
        """kg of one material of a part in a kind, and the elements it holds: by its grade's recipe where it names one,
        else by type 1's recipe, as copper, or as magnets of the grade class drawn for `heat_group`. A material or grade
        written 'A or B' is either, drawn (Shared.state). A part of magnets outside the joints may name its grade
        class, a part of battery cells follows the cells' recipe as the main pack (2026-10-29, "Yes, build them",
        point 4). Electronics are added by board() and sensor()."""
        for written, call in ((material, lambda m, k: self.material(part, kind, m, k, estimate, heat_group, grade)),
                              (grade, lambda g, k: self.material(part, kind, material, k, estimate, heat_group, g))):
            if schemas.OR in written:
                drawn = self.of(self.shared.state(written))
                for place, one in enumerate(schemas.alternatives(written)):
                    call(one, kg * (drawn == place))
                return
        self.parts[part] = self.parts.get(part, 0) + kg
        self.materials[(kind, material)] = self.materials.get((kind, material), 0) + kg
        self.detail(kind, material, kg, heat_group, grade)
        if material == MAGNETS:
            names, drawn = self.shared.magnets[grade] if grade else self.shared.magnet[heat_group]
            for k, element in enumerate(names):
                self.element(kind, element, kg * self.of(drawn[:, k]), estimate, material)
        elif material == CELL_MATERIAL:
            for element, share in self.shared.cells.items():
                self.element(kind, element, kg * self.of(share), estimate, material)
        elif grade:
            for element, share in self.shared.grade_elements(grade).items():
                self.element(kind, element, kg * self.of(share), estimate, material)
        elif material in self.shared.recipe:
            for element, share in self.shared.recipe[material].items():
                self.element(kind, element, kg * self.of(share), estimate, material)

    def detail(self, kind: str, material: str, kg: np.ndarray, heat_group: str, grade: str) -> None:
        """The kg of a material by what it is, for the material pages (Matthias, 2026-10-29: "how much Copper and
        especially permanent magnets. The different steels and aluminum alyoys"): the magnets by the grade class drawn
        for their joint's heat; a material with a grade by the recipes the grade holds (the gear stage 2's steel as
        20CrMnTi and GCr15); type 1's aluminium by its alloys; every other material whole ('')."""
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
        elif material in ALLOYS:
            split = {leaf: self.of(share) for leaf, share in s.grade_leaves(s.recipe_name[material]).items()}
        else:
            split = {'': 1.0}
        for what, share in split.items():
            key = (kind, material, what)
            self.details[key] = self.details.get(key, 0) + kg * share

    def piece(self, part: str, kind: str, item: str, material: str, kg: np.ndarray, estimate: bool,
              heat_group: str = '', grade: str = '') -> None:
        """A part or component of one material (and its grade), or of the shares of the sheet Shares."""
        if material:
            self.material(part, kind, material, kg, estimate, heat_group, grade)
        else:
            for (shared, its_grade), share in self.shared.shares[item]:
                self.material(part, kind, shared, kg * self.of(share), estimate, heat_group, its_grade)

    def board(self, kind: str, category: str, kg: np.ndarray, area: np.ndarray, estimate: bool,
              inside: np.ndarray | float = 0.0) -> None:
        """The elements of boards of `kg` and `area` (cm2): copper their mass times the copper share, the metals of
        BOARD_METALS their area times the car category's mg per cm2, tantalum their mass times its share; their rest,
        less the elements `inside` them that are drawn as another's (a joint's encoders on its driver board), glass
        fibre and bromine each a share of it and epoxy the remainder, the glass and the epoxy by their recipes
        (2026-10-29, "Yes, enter them", point 3b; EVIDENCE.md E5.21)."""
        s = self.shared
        copper, tantalum = kg * self.of(s.constant[BOARD_COPPER]), kg * self.of(s.tantalum)
        metals = {metal: area * self.of(s.pcb[(category, metal)]) / 1e6 for metal in schemas.BOARD_METALS}
        self.element(kind, 'Cu', copper, estimate, ELECTRONICS)
        for metal, kg_metal in metals.items():
            self.element(kind, metal, kg_metal, estimate, ELECTRONICS)
        self.element(kind, 'Ta', tantalum, estimate, ELECTRONICS)
        rest = kg - copper - tantalum - sum(metals.values()) - inside
        glass, bromine = rest * self.of(s.constant[BOARD_GLASS]), rest * self.of(s.constant[BOARD_BROMINE])
        self.element(kind, 'Br', bromine, estimate, ELECTRONICS)
        for recipe, kg_of in ((GLASS_RECIPE, glass), (EPOXY_RECIPE, rest - glass - bromine)):
            for element, share in s.grade_elements(recipe).items():
                self.element(kind, element, kg_of * self.of(share), estimate, ELECTRONICS)

    def sensor_kg(self, units: list, count: np.ndarray | float) -> np.ndarray:
        """kg of the car sensor elements of `count` sensors, each made of `units` (car sensor type, units in one
        sensor): what sensor() adds as their elements."""
        return sum((count * per_sensor * self.of(mg) / 1e6 for car_type, per_sensor in units
                    for (t, _), mg in self.shared.sensor.items() if t == car_type), np.zeros(self.n))

    def sensor(self, kind: str, units: list, count: np.ndarray | float, estimate: bool) -> None:
        """The elements of `count` sensors, each made of `units` (car sensor type, units in one sensor)."""
        for car_type, per_sensor in units:
            for (t, element), mg in self.shared.sensor.items():
                if t == car_type:
                    self.element(kind, element, count * per_sensor * self.of(mg) / 1e6, estimate, ELECTRONICS)


def triangles(rng: np.random.Generator, low: np.ndarray, mode: np.ndarray, high: np.ndarray) -> np.ndarray:
    """One draw of a triangle for each entry of the arrays; the mode itself where minimum and maximum are equal."""
    out = np.array(mode, dtype=float)
    spread = high > low
    out[spread] = rng.triangular(low[spread], mode[spread], high[spread])
    return out


def draw_type_one(inputs: ApartInputs, params: Params, magnets: dict) -> Draws:
    """Robot type 1 over its robots of the register, drawn `composition.draws` times (HOW IT DRAWS ROBOT TYPE 1 in the
    docstring at the top): each draw one of the register's robots of type 1, all equally often (Matthias, 2026-10-28:
    "Do it for all the robots which are in type 1"); a robot in several versions (the Booster K1) one of them, each as
    often (2026-10-29, decision B); its mass a triangle on its own mass in the parts file, its parts its own rows, part
    by part (decision C: nothing scaled from another robot)."""
    apart, n = inputs.apart, params.composition.draws
    rng = np.random.default_rng([params.composition.seed, TYPE_ONE])
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
    shared = Shared(inputs, params, magnets, rng, n)
    mass = np.zeros(n)
    done = []
    for k, name in enumerate(names):
        rows = np.flatnonzero(robot == k)
        constants = apart.constants[name]
        robot_kg = triangle(rng, *constants[ROBOT_MASS][1], rows.size)
        mass[rows] = robot_kg
        r = Robot(name, rows, shared, robot_kg)
        draw_robot(r, inputs, constants, rng)
        frame = next(p for p in apart.parts if p.robot == name and p.computed.startswith(FRAME))
        rest = robot_kg - sum(r.parts.values())
        r.piece(f'{name}: {frame.name}', KIND_OF[frame.kind], frame.name, frame.material, rest,
                frame.label.startswith('E'), grade=frame.grade)
        done.append(r)
    d = assemble(n, names, robot, mass, done, apart, shared)
    d.register, d.register_robot = [f'{r.number} {r.name}' for r in robots], which
    d.on_estimates = on_estimates(apart, [v for r in robots for v in schemas.versions(r.taken_apart)])
    return d


def on_estimates(apart, drawn: list) -> dict:
    """What of the robots drawn rests most on estimates (E), for the notes page (the entry, point 8), by 01's
    estimate_kinds: their joint modules a share of their mass, their joints' masses from their torques, their battery's
    energy a share of their mass, their mass itself."""
    # In plain words, without the sections of EVIDENCE.md (E5.17 points 1, 2 and 6; E5.12 point 4, E2.8e), which are
    # project words on a page (Matthias's figure rule; 2026-10-29, "Yes, build them", point 7).
    words = {'joint shares': "the joint modules a share of the robot's mass, split as batch 1's on average",
             'joint torques': "the joints' masses from their torques",
             'battery per kg': "the battery's energy a share of the robot's mass",
             'mass': 'the mass itself'}
    out = {what: [r for r in drawn if key in schemas.estimate_kinds(apart, r)] for key, what in words.items()}
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
    encoders = [p for p in apart.sensors if p.robot == name and p.kind in IN_THE_JOINTS]
    modules = r.mass * r.of(s.constant[JOINT_SHARE]) if any(j.share is not None for j in joints) else None
    for j in joints:
        kind = JOINT_KIND[j.name.split()[0].lower()]
        estimate = label.get(f'Joint module, {j.module}', 'E').startswith('E')
        if j.share is not None:
            stated = modules * j.share / j.count
        else:
            stated = None if None in j.module_mass else triangle(rng, *j.module_mass, n)
        scale = np.ones(n) if stated is None else stated / s.at_mode[j.module]
        one = {component: r.of(kg) * scale for component, kg in s.joint[j.module].items()}   # one joint, kg
        if stated is not None:
            rest = stated - sum(kg for component, kg in one.items() if component not in STRUCTURE)
            one.update({component: rest * share for component, share in s.structure_share[j.module].items()})
            r.structures[f'{name}: {j.name} structure'] = rest
        part = f'{name}: {j.name} ({j.count} joints)'
        for component, kg_one in one.items():
            kg_here = kg_one * j.count
            if component == DRIVER_BOARD:
                r.material(part, kind, ELECTRONICS, kg_here, estimate)
                area = r.of(s.board_area[j.module]) * scale * j.count
                # The joint's encoders sit on its driver board: their elements are in its mass (point 3b).
                inside = sum((r.sensor_kg([(t, u) for _, sensor, t, u in apart.elements if sensor == e.name],
                                          e.count / in_robot * j.count) for e in encoders), np.zeros(n))
                r.board(kind, drivers[j.module].category, kg_here, area, estimate, inside)
            else:
                r.piece(part, kind, component, s.material[component], kg_here, estimate, j.heat_group,
                        s.grade[component])
        for e in encoders:   # their elements only: their mass is inside the joint's components
            units = [(t, u) for _, sensor, t, u in apart.elements if sensor == e.name]
            r.sensor(kind, units, e.count / in_robot * j.count, e.label.startswith('E'))

    # The parts: of one material or of shares, the cables from their length, the shell a share of the robot's mass.
    # The battery follows below; the frame is added last, by draw_type_one().
    for p in apart.parts:
        if p.robot != name or p.kind in IN_THE_JOINTS or p.computed.startswith((PACK, CELLS, HOUSING, FRAME)):
            continue
        kind, estimate, column = KIND_OF[p.kind], p.label.startswith('E'), f'{name}: {p.name}'
        if p.computed.startswith(CABLES):
            # Four conductors, two for power and two for signals: m × mm2 × g/cm3 is g.
            mm2 = 2 * r.of(s.constant[POWER_CS]) + 2 * r.of(s.constant[SIGNAL_CS])
            copper = triangle(rng, *constants[CABLE_LENGTH][1], n) * mm2 * r.of(s.constant[DENSITY]) / 1000
            r.material(column, kind, COPPER, copper, estimate)
            r.material(column, kind, 'Plastics', copper * r.of(s.constant[INSULATION]), estimate)
            continue
        if p.computed.startswith(SHELL):
            kg = r.mass * r.of(s.constant[SHELL_SHARE])
        else:
            kg = p.count * triangle(rng, *p.bounds, n)
        r.piece(column, kind, p.name, p.material, kg, estimate, grade=p.grade)

    # The boards outside the joints: their area, their mass from it, their elements.
    for b in apart.boards:
        if b.robot != name or b.kind in IN_THE_JOINTS:
            continue
        area = b.count * triangle(rng, *b.bounds, n)
        kg = area * r.of(s.constant[BOARD_G_PER_CM2]) / 1000
        r.material(f'{name}: {b.name}', KIND_OF[b.kind], ELECTRONICS, kg, b.label.startswith('E'))
        r.board(KIND_OF[b.kind], b.category, kg, area, b.label.startswith('E'))

    # The sensors outside the joints: their mass (g) where a source gives it, their car sensor elements. A module is
    # its elements (electronics) and its housing, the rest of its mass: aluminium a share of it, plastics the remainder
    # (2026-10-29, "Yes, build them", point 3c; the car file holds the elements, "not the complete module housing").
    # A sensor whose mass no source states is its elements at least (point 3b: the electronics wholly in the elements);
    # its housing, not known, stays in the frame's remainder.
    for e in apart.sensors:
        if e.robot != name or e.kind in IN_THE_JOINTS:
            continue
        units = [(t, u) for _, sensor, t, u in apart.elements if sensor == e.name]
        estimate, column, kind = e.label.startswith('E'), f'{name}: {e.name}', KIND_OF[e.kind]
        inside = r.sensor_kg(units, e.count)
        r.material(column, kind, ELECTRONICS, inside, estimate)
        if None not in e.bounds:
            kg = e.count * triangle(rng, *e.bounds, n) / 1000
            aluminium = (kg - inside) * r.of(s.constant[SENSOR_ALUMINIUM])
            r.material(column, kind, 'Aluminium', aluminium, estimate)
            r.material(column, kind, 'Plastics', kg - inside - aluminium, estimate)
        r.sensor(kind, units, e.count, estimate)

    # The battery: its energy (its voltage times its capacity, or its energy per kg of robot times its mass), its cells
    # from it, its housing the pack less its cells and its management board (the boards of the kind Battery pack); the
    # pack its stated mass, or its energy over a pack's energy per kg. A pack with no housing is its cells and board.
    pack = next((p for p in apart.parts if p.robot == name and p.computed.startswith(PACK)), None)
    if pack is not None:
        if VOLTAGE in constants:
            wh = triangle(rng, *constants[VOLTAGE][1], n) * triangle(rng, *constants[CAPACITY][1], n)
        else:
            wh = r.mass * r.of(s.constant[ENERGY_PER_KG])
        cells_kg = wh / r.of(s.wh_per_kg)
        cells = next(p for p in apart.parts if p.robot == name and p.computed.startswith(CELLS))
        column = f'{name}: {cells.name}'
        r.parts[column] = cells_kg
        r.materials[('battery', CELL_MATERIAL)] = r.materials.get(('battery', CELL_MATERIAL), 0) + cells_kg
        # The cells by their chemistry, for the material pages (Matthias, 2026-10-29: "Give me NMC etc. for the
        # batteries as materiel"): the recipe they follow.
        key = ('battery', CELL_MATERIAL, CELL_RECIPE)
        r.details[key] = r.details.get(key, 0) + cells_kg
        for element, share in s.cells.items():
            r.element('battery', element, cells_kg * r.of(share), cells.label.startswith('E'), CELL_MATERIAL)
        housing = next((p for p in apart.parts if p.robot == name and p.computed.startswith(HOUSING)), None)
        if housing is not None:
            if None in pack.bounds:
                pack_kg = wh / r.of(s.constant[PACK_WH_PER_KG])
            else:
                pack_kg = pack.count * triangle(rng, *pack.bounds, n)
            managed = sum((r.parts[f'{name}: {b.name}'] for b in apart.boards
                           if b.robot == name and b.kind == 'Battery pack'), np.zeros(n))
            r.piece(f'{name}: {housing.name}', 'battery', housing.name, housing.material, pack_kg - cells_kg - managed,
                    housing.label.startswith('E'), grade=housing.grade)


def assemble(n: int, names: list, robot: np.ndarray, mass: np.ndarray, done: list, apart, shared: Shared) -> Draws:
    """The robots' draws put together into the N draws, in the order the data file names things."""
    def put(key, store, r):
        values = np.zeros(n)
        values[r.rows] = store[key]
        return values

    part_columns = [c for r in done for c in r.parts]
    parts = np.column_stack([put(c, r.parts, r) for r in done for c in r.parts])
    remainders = [f'{p.robot}: {p.name}' for p in apart.parts if p.computed.startswith((FRAME, HOUSING))]
    structures = {c: put(c, r.structures, r) for r in done for c in r.structures}
    material_keys = sorted({k for r in done for k in r.materials}, key=lambda k: (list(KINDS).index(k[0]), k[1]))
    materials = np.column_stack([sum((put(k, r.materials, r) for r in done if k in r.materials), np.zeros(n))
                                 for k in material_keys])
    elements = {k: sum((put(k, r.elements, r) for r in done if k in r.elements), np.zeros(n))
                for k in {k for r in done for k in r.elements}}
    estimated = {k: sum((put(k, r.estimated, r) for r in done if k in r.estimated), np.zeros(n))
                 for k in {k for r in done for k in r.estimated}}
    hot = schemas.hot_kinds(apart)
    followed = {m: sum((put(m, r.followed, r) for r in done if m in r.followed), np.zeros(n))
                for m in {m for r in done for m in r.followed}}
    details = {k: sum((put(k, r.details, r) for r in done if k in r.details), np.zeros(n))
               for k in {k for r in done for k in r.details}}
    return Draws(n, names, robot, mass, (part_columns, parts), remainders, structures, (material_keys, materials),
                 elements, estimated, hot, shared.heat, shared.heat_grade, followed, details)


def kind_kg(d: Draws, kind: str) -> np.ndarray:
    """The kg of one kind of part in each draw: all its materials."""
    columns, draws = d.materials
    return draws[:, [i for i, (k, _) in enumerate(columns) if k == kind]].sum(axis=1)


def below_zero(d: Draws) -> dict:
    """The share of each robot's draws where one of its remainders (a frame, a battery housing, a joint's structure)
    falls below zero: '<robot>: <part>' -> share."""
    columns, draws = d.parts
    out = {}
    for column in d.remainders:
        k = d.robots.index(column.split(': ')[0])
        out[column] = float((draws[d.robot == k, columns.index(column)] < 0).mean())
    for column, values in d.structures.items():
        k = d.robots.index(column.split(': ')[0])
        out[column] = float((values[d.robot == k] < 0).mean())
    return out


def element_order(elements) -> list:
    """Elements in the order of 01's table of atomic masses, the others after them by name."""
    known = list(schemas.ATOMIC_MASS)
    return sorted(elements, key=lambda e: (known.index(e) if e in known else len(known), e))


# ------------------------------------------------------------------------------------------------------
# What is written
# ------------------------------------------------------------------------------------------------------

def statistics(values: np.ndarray) -> list:
    """Mean, median, 2.5 % and 97.5 % of draws, kg."""
    return [float(values.mean()), float(np.median(values)), *map(float, np.percentile(values, [2.5, 97.5]))]


def write_taken_apart(d: Draws, folder: str) -> None:
    """Robot type 1 part by part, at every level, and its summary, into `folder` (WHAT IT WRITES in the
    docstring at the top)."""
    os.makedirs(folder, exist_ok=True)
    names = ', '.join(f'{k} {name}' for k, name in enumerate(d.robots))
    element_keys = [(kind, e) for kind in KINDS for e in element_order({e for k, e in d.elements if k == kind})]
    grade_keys = sorted(d.details, key=lambda key: (list(KINDS).index(key[0]), key[1], key[2]))
    tables = {
        'robots': ([f'Robot drawn ({names})', 'Mass (kg)', 'Robot of the register'],
                   np.column_stack([d.robot, d.mass, d.register_robot])),
        'parts': d.parts,
        'materials': ([f'{KINDS[k][0]}: {m}' for k, m in d.materials[0]], d.materials[1]),
        # Each material by its grade, alloy or magnet grade class ('<kind>: <material>: <grade>'; a material whole
        # without the third part): the draws behind the material pages.
        'grades': ([f'{KINDS[k][0]}: {m}' + (f': {x}' if x else '') for k, m, x in grade_keys],
                   np.column_stack([d.details[key] for key in grade_keys])),
        'elements': ([f'{KINDS[k][0]}: {e}' for k, e in element_keys],
                     np.column_stack([d.elements[k] for k in element_keys])),
        'estimated': ([f'{KINDS[k][0]}: {e}' for k, e in element_keys],
                      np.column_stack([d.estimated.get(k, np.zeros(d.n)) for k in element_keys])),
    }
    for table in APART_TABLES:
        columns, draws = tables[table]
        np.save(os.path.join(folder, f'{table}.npy'), np.asarray(draws, dtype=np.float32))
        with open(os.path.join(folder, f'{table}.txt'), 'w', encoding='utf-8') as file:
            file.write('\n'.join(columns) + '\n')
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
        out.writerow(['Element', 'Kind of part', 'Mean (kg)', 'Median (kg)', '2.5 % (kg)', '97.5 % (kg)'])
        out.writerows(rows)
        out.writerow([])
        out.writerow(['Remainder', 'Share of its robot\'s draws below zero'])
        out.writerows([[column, share] for column, share in below_zero(d).items()])
        out.writerow([])
        out.writerow(['Heat group', 'Grade class', 'Share of the draws'])
        out.writerows([[group, klass, float((drawn == klass).mean())] for group, drawn in d.grades.items()
                       for klass in dict.fromkeys(drawn)])


# ------------------------------------------------------------------------------------------------------
# Robot type 1 as 02 writes every robot type
# ------------------------------------------------------------------------------------------------------

# The kinds of part of robot type 1 placed in the shared lists' part groups and body regions, so that its tables have
# the columns of every other robot type (03 compares them): whole kinds, not part by part. Kept so (2026-10-29, "Yes,
# build them", point 5): no repository reads these tables yet; rough where a kind holds parts of another group (the
# head's joints in Sensors, the battery management board in Battery), as the notes page says.
KIND_PART_GROUP = {'hips': 'Joint drives', 'knees': 'Joint drives', 'ankles': 'Joint drives', 'waist': 'Joint drives',
                   'arms': 'Joint drives', 'battery': 'Battery', 'boards': 'Computer', 'head': 'Sensors',
                   'cables': 'Cables', 'frame': 'Frame'}
KIND_BODY_REGION = {'hips': 'Legs', 'knees': 'Legs', 'ankles': 'Legs', 'waist': 'Torso', 'arms': 'Arms',
                    'battery': 'Torso', 'boards': 'Torso', 'head': 'Head', 'cables': 'Whole body',
                    'frame': 'Whole body'}


def compose_type_one(category, d: Draws, lists) -> Composition:
    """Robot type 1 as 02 writes every robot type, from its draws over its robots: its materials (Not allocated 0, as
    the frame takes the rest), its elements, its part groups and body
    regions (its kinds placed by KIND_PART_GROUP and KIND_BODY_REGION), its total; and the kilograms of each material
    whose elements are drawn."""
    n, materials = d.n, lists.names[schemas.MATERIAL]
    columns, draws = d.materials
    kg_of = {name: np.zeros(n) for name in materials}
    for i, (_, material) in enumerate(columns):
        kg_of[material] += draws[:, i]
    # Not allocated: none, as the frame takes the rest of the robot's mass (the materials add up to it to the
    # rounding of the computer, which draw_faults checks).
    kg_of[NOT_ALLOCATED] = np.zeros(n)
    followed = {name: d.followed.get(name, np.zeros(n)) for name in materials}
    element_columns = element_order({e for _, e in d.elements})
    elements = {e: sum((v for (_, x), v in d.elements.items() if x == e), np.zeros(n)) for e in element_columns}
    group_names, region_names = lists.names[schemas.PART_GROUP], lists.names[schemas.BODY_REGION]
    groups, regions = {g: np.zeros(n) for g in group_names}, {r: np.zeros(n) for r in region_names}
    for kind in KINDS:
        kg = kind_kg(d, kind)
        groups[KIND_PART_GROUP[kind]] += kg
        regions[KIND_BODY_REGION[kind]] += kg
    tables = {'materials': (materials, stack(materials, kg_of, n)),
              'elements': (element_columns, stack(element_columns, elements, n)),
              'part_groups': (group_names, stack(group_names, groups, n)),
              'body_regions': (region_names, stack(region_names, regions, n)),
              'total': (['Total'], d.mass[:, None])}
    return Composition(TYPE_ONE, folder_name(category), category.name, tables, stack(materials, followed, n), None,
                       None)


def same_elements(drawn: list) -> None:
    """Every robot type's elements with the same columns, all the elements any of them holds, in the order of 01's
    table of atomic masses: 0 kg where a robot type's materials hold none of an element so far (its summary says which
    materials are in the elements). 03 compares robot types column by column."""
    columns = element_order(set().union(*(set(c.tables['elements'][0]) for c in drawn)))
    for c in drawn:
        own, draws = c.tables['elements']
        full = np.zeros((draws.shape[0], len(columns)))
        for k, name in enumerate(own):
            full[:, columns.index(name)] = draws[:, k]
        c.tables['elements'] = (columns, full)


# ------------------------------------------------------------------------------------------------------
# The page of each robot type (point 14)
# ------------------------------------------------------------------------------------------------------
# Laid out in inches from the top left, with 01's page functions (new_page, write, save), as 01's pages are.

ROW = 0.25                 # the height of one row of a chart, inches
LABEL = 1.9                # the names left of a chart, inches
CHART = 4.4                # the width of a chart, inches
NUMBERS = 2.2              # the numbers right of a chart, inches
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
    """An element in plain words: 'Carbon (C)'."""
    return f'{ELEMENT_NAMES[symbol]} ({symbol})' if symbol in ELEMENT_NAMES else symbol


def interval_bars(axes, rows: list, size: float = 9, grey: bool = False) -> None:
    """On `axes`, one row per (name, its draws): a bar of the mean from zero (grey for Mixed and Not allocated, or for
    every row with `grey`) and a line with end ticks over 95 % of the draws (2.5 % to 97.5 %); nothing where there is
    no mass in any draw. The kg scale is fitted to the lines, with the zero line and hairlines; the names stand on the
    left. 03_comparison.py draws its charts with it too."""
    stats = [(name, draws.any(), statistics_of(draws)) for name, draws in rows]
    lows = [s['2.5 % (kg)'] for _, present, s in stats if present]
    highs = [s['97.5 % (kg)'] for _, present, s in stats if present]
    low, high = min([0] + lows), max(highs + [1e-9])
    pad = 0.03 * (high - low)
    for i, (name, present, s) in enumerate(stats):
        if not present:
            continue
        lower, upper = s['2.5 % (kg)'], s['97.5 % (kg)']
        colour = GREY if grey or name in ('Mixed', NOT_ALLOCATED) else BAR
        axes.barh(i, s['Mean (kg)'], height=0.6, color=colour, zorder=2)
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
    """One chart of a page, under its title and a line saying what it covers: interval_bars, with the mean and the
    interval of each row written beside it, '–' for a row with no mass in any draw. (x, y): the chart's top left,
    inches. Returns the y below it."""
    schemas.write(page, x, y, [title], size=11, weight='bold')
    schemas.write(page, x, y + 0.27, [what], size=9, colour=MUTED)
    y += 0.6
    numbers = x + LABEL + CHART + 0.15
    schemas.write(page, numbers + 0.55, y, ['Mean'], size=8.5, colour=MUTED, align='right')
    schemas.write(page, numbers + 0.75, y, ['95 % of the draws'], size=8.5, colour=MUTED)
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
        page.text(numbers + 0.55, row_y, mass(s['Mean (kg)']), fontsize=9, ha='right', va='center')
        page.text(numbers + 0.75, row_y, f"{mass(s['2.5 % (kg)'])} to {mass(s['97.5 % (kg)'])}", fontsize=9,
                  va='center')
    return y + height + 0.55


def shown_elements(names: list, params: Params) -> list:
    """The elements a page shows: `names` less those of `composition.elements_not_shown` (Matthias, 2026-10-29:
    "Hydrogene and Oxygen have to go you should know this. Same for F, and N"). The draws keep them all."""
    return [name for name in names if name not in params.composition.elements_not_shown]


def not_shown_note(params: Params) -> str:
    """The note that says, in plain words, which elements the pages leave out: 'Hydrogen, nitrogen, oxygen and
    fluorine are not shown; they are in the draws.'"""
    words = [ELEMENT_NAMES.get(e, e).lower() for e in params.composition.elements_not_shown]
    if not words:
        return ''
    listed = words[0] if len(words) == 1 else ', '.join(words[:-1]) + ' and ' + words[-1]
    return f"{listed[0].upper()}{listed[1:]} {'is' if len(words) == 1 else 'are'} not shown; " \
           f"{'it is' if len(words) == 1 else 'they are'} in the draws."


def page_elements(c: Composition, params: Params) -> list:
    """The rows of a page's 'By element': (the element in plain words, its draws), those not shown left out."""
    return [(element_label(name), c.column('elements', name))
            for name in shown_elements(c.tables['elements'][0], params)]


def page_notes(c: Composition, params: Params) -> list:
    """What a reader needs to read the page of one robot type, in plain words."""
    rows = {r['Name']: r for r in summary(c) if r['Kind'] == 'Material'}
    below = rows[NOT_ALLOCATED]['Draws below zero (%)']
    notes = ["Not allocated: the parts' mass minus the materials' mass in each draw, both drawn from the workbook's "
             'minimum, mode and maximum. ' + (f'It is below zero in {below:.1f} % of the draws, where the drawn '
                                              'materials weigh more than the drawn parts.' if below else
                                              'It is above zero in every draw.')]
    if c.build is not None:
        notes.append('Battery materials: the cells only, one build of the sheet Battery cells drawn in each draw, all '
                     'builds equally likely; the rest of the battery row is in the materials it goes to.')
    elif c.battery is not None:
        notes.append("Battery materials: the workbook's row, already cells only.")
    covered = [n for n, r in rows.items() if r['In the elements'] == 'Yes']
    partly = [n for n, r in rows.items() if r['In the elements'] == 'Partly']
    missing = [n for n, r in rows.items() if r['In the elements'] == 'No' and n != NOT_ALLOCATED]
    notes.append(f'By element: the materials that have a recipe so far, {", ".join(covered) or "none"}'
                 f'{"; in part: " + ", ".join(partly) if partly else ""}. Not yet in the elements: '
                 f'{", ".join(missing) or "none"}; their kilograms are in the materials only. '
                 + not_shown_note(params))
    notes.append('–: none in this robot type.')
    return notes


def draw_page(c: Composition, draws: int, path: str, params: Params) -> None:
    """Point 14: the page of one robot type, its kg by material and its kg by element, each with its 95 % interval."""
    materials = [(name, c.column('materials', name)) for name in c.tables['materials'][0]]
    elements = page_elements(c, params)
    notes = [line for note in page_notes(c, params) for line in schemas.wrap('• ' + note, 200)]
    total = c.column('total', 'Total')
    materials_kg = (total - c.column('materials', NOT_ALLOCATED)).mean()
    followed = c.in_elements.sum(axis=1).mean()
    top = 1.15
    height = top + 0.85 + ROW * max(len(materials), len(elements)) + 0.55 + len(notes) * schemas.LINE + 0.4
    figure, page = schemas.new_page(PAGE_WIDTH, height)
    page.text(MARGIN, 0.35, f'Robot type {c.number}: {c.title}', fontsize=15, fontweight='bold', va='top')
    page.text(MARGIN, 0.75, f'What one robot is made of, from {draws:,} draws. Each bar is the mean; its line spans '
                            '95 % of the draws, from 2.5 % to 97.5 %.', fontsize=10, color=MUTED, va='top')
    below = interval_chart(figure, page, height, MARGIN, top, 'By material',
                           f"All of the robot's {mass(total.mean())} kg at the mean: its materials, and Not allocated",
                           materials)
    below = max(below, interval_chart(figure, page, height, MARGIN + LABEL + CHART + NUMBERS + GAP, top,
                                      'By element', f'Only the materials that have a recipe so far: {mass(followed)} '
                                                    f'of the {mass(materials_kg)} kg of materials at the mean',
                                      elements))
    schemas.write(page, MARGIN, below, notes, size=9)
    schemas.save(figure, path, params.output.dpi)


# ------------------------------------------------------------------------------------------------------
# The pages of robot type 1: each element as its total in one robot
# ------------------------------------------------------------------------------------------------------
# Matthias, 2026-10-28: "I want to see the overall information on the element as total. Show me the distributions",
# "Do it for all the robots which are in type 1. Do the code and the figure!!", on the preview "Yes, code it in 02",
# and "Do not repeat the comments on all slides have it on a separate one. It uses much to much space". Pages of a
# screen's shape, 16 × 9 inches, text 14 points and up (about 23 pixels fit to a 1920 × 1080 screen), as approved for
# 04's pages ("Pages right"): a page of notes first, then the elements, nine a page.

TYPE_ONE_PAGE = (16, 9)
TYPE_ONE_TEXT, TYPE_ONE_LABEL, TYPE_ONE_TITLE, TYPE_ONE_HEADING = 14, 15, 16, 20   # points
TYPE_ONE_ACROSS, TYPE_ONE_DOWN = 3, 3           # element panels on a page
TYPE_ONE_BINS = 70                              # the bars of a distribution, as in RAWCLICDataCenters' figures
TYPE_ONE_BAR = '#4477AA'                        # Paul Tol's bright blue, as published
TYPE_ONE_INK = '#222222'                        # lines and numbers
TYPE_ONE_NOTE_WIDTH = 140                       # characters in a line of a notes page
# The lines of a notes page, its blank lines counted: from the top of its text (0.83 of the page's height from the
# foot) to 0.35 inches above the foot, one line of 14-point text at a spacing of 1.3 taking 0.269 inches, as measured;
# tests/test_parts_taken_apart.py fails where a text runs off its page.
NOTES_LINES = 26
# The elements of robot type 1's other materials (boards, sensors, magnets) in plain words, beside those of the recipes.
ELEMENT_NAMES.update({'Ag': 'Silver', 'As': 'Arsenic', 'Au': 'Gold', 'Br': 'Bromine', 'Dy': 'Dysprosium',
                      'Ga': 'Gallium', 'In': 'Indium', 'Nb': 'Niobium', 'Nd': 'Neodymium', 'Pd': 'Palladium',
                      'Pr': 'Praseodymium', 'Ta': 'Tantalum', 'Tb': 'Terbium', 'W': 'Tungsten'})


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


def element_panel(axes, kg: np.ndarray, title: str, first_in_row: bool) -> None:
    """One element (or, on the material pages, one material) in one robot over the draws, under `title`: its
    histogram (the height the share of the draws), the median a solid line and the mean a dotted one, both written
    above the panel, right (Matthias, 2026-10-28: "Use the median or show boths"), the 2.5th and 97.5th percentile
    dashed; its own scale and unit. Where it is 0 in some draws (a robot or a version without it), the panel shows the
    draws that hold it, their median, mean and 95 % interval, and above them in what share of all the draws it is held
    (Matthias, 2026-10-29, on the materials: "If it is just a bit and a large 0 then show me the distribution"; on the
    elements: "I told you I want to see the distribution not just the 0 value for vanadium and lead")."""
    share = float((kg > 0).mean())
    held_in = f'in {panel_number(100 * share)} % of the draws' if share < 1 else ''
    if held_in:
        kg = kg[kg > 0]
    per, unit = panel_unit(kg)
    values = kg / per
    axes.set_title(title, fontsize=TYPE_ONE_TITLE, fontweight='bold', loc='left')
    counts, edges = np.histogram(values, bins=TYPE_ONE_BINS)
    axes.bar(edges[:-1], counts / values.size, width=np.diff(edges), align='edge', color=TYPE_ONE_BAR,
             edgecolor='none')
    median, mean = float(np.median(values)), float(values.mean())
    axes.axvline(median, color=TYPE_ONE_INK, linewidth=1.8)
    axes.axvline(mean, color=TYPE_ONE_INK, linewidth=1.8, linestyle=':')
    for bound in np.percentile(values, [2.5, 97.5]):
        axes.axvline(bound, color=TYPE_ONE_INK, linewidth=1.2, linestyle='--')
    # The bars up to about nine tenths of the panel (Matthias, 2026-10-28: "can you better adust the hight. we loose
    # quite a bit of space. Not full but much better"); the two numbers in the title line, right.
    axes.set_ylim(0, (counts / values.size).max() * 1.1)
    numbers = f'median {panel_number(median)}\u00a0{unit}\nmean {panel_number(mean)}\u00a0{unit}'
    axes.set_title(f'{held_in}\n{numbers}' if held_in else numbers, loc='right', fontsize=TYPE_ONE_TEXT,
                   color=TYPE_ONE_INK)
    axes.xaxis.set_major_locator(plt.MaxNLocator(5))
    axes.xaxis.set_major_formatter(plt.FuncFormatter(panel_number))
    axes.yaxis.set_major_locator(plt.MaxNLocator(3))
    axes.yaxis.set_major_formatter(plt.FuncFormatter(panel_number))
    axes.tick_params(labelsize=TYPE_ONE_TEXT)
    axes.set_xlabel(f'mass in one robot ({unit})', fontsize=TYPE_ONE_LABEL)
    if first_in_row:
        axes.set_ylabel('share of draws', fontsize=TYPE_ONE_LABEL)
    axes.grid(axis='x', alpha=0.3)
    for side in ('top', 'right'):
        axes.spines[side].set_visible(False)


def type_one_notes(c: Composition, d: Draws, left_out: list, params: Params) -> list:
    """The notes page's paragraphs: how to read the element pages, what is drawn, what is not yet, what is not
    shown."""
    rows = {r['Name']: r for r in summary(c) if r['Kind'] == 'Material'}
    missing = [f"{name} (median {panel_number(rows[name]['Median (kg)'])} kg, mean "
               f"{panel_number(rows[name]['Mean (kg)'])} kg)" for name in rows
               if rows[name]['In the elements'] == 'No' and name != NOT_ALLOCATED]
    partly = [name for name in rows if rows[name]['In the elements'] == 'Partly']
    estimates = [f"{what}: {', '.join(robots)}" for what, robots in (d.on_estimates or {}).items()]
    notes = [
        'The bars: the draws of one element in one robot, the height the share of the draws. Solid line: the median; '
        'dotted line: the mean; both written above the panel, right. Dashed lines: the 2.5th and 97.5th percentile '
        '(95 % of the draws between them). Each panel on its own scale and unit (kg, g, mg). An element or material '
        '0 in some draws: its panel shows the draws that hold it and says in what share of all the draws it is held; '
        'one held in fewer than 2.5 % of the draws has no panel.',
        f"The draws: {d.n:,}, each one robot of type 1 in the register, each of its {len(d.register)} robots "
        'drawn equally often (a robot in two versions, each as often); its mass a triangle on its own mass, its '
        'parts its own, part by part (the parts file, from its sources).',
        'The robots drawn: ' + '; '.join(d.register) + '. A robot of two robot types is drawn in full in each of them.',
        ('Resting most on estimates: ' + '; '.join(estimates) + '.') if estimates else '',
        'Not drawn: ' + ('; '.join(f'{r.number} {r.name} (no mass stated)' for r in left_out) or 'none') +
        '. A robot lighter than 15 kg is not of robot type 1.',
        'Not yet in the elements: ' + (', '.join(missing) + '; their elements are missing from the pages.'
                                       if missing else 'none.') +
        (f" In part: {', '.join(partly)} (its elements less than its mass)." if partly else ''),
        not_shown_note(params),
        "The tables by part group and by body region (for stock-and-flow): type 1's ten kinds of part, each placed "
        "whole; rough where a kind holds parts of another group: the head's joints are counted as sensors, the battery "
        'management board as battery.',
        'The material pages: each material in one robot, drawn as the elements; the steels by their grade, the '
        "aluminium by its alloys (type 1's recipe: die-cast 0 to 40 %, of the wrought rest 7075 0 to 64 % and 6061), "
        "the permanent magnets in all and by the grade class each joint's heat draws. Copper is the metal of windings, "
        'wires, cables, busbars, contacts and heat pipes; the copper of the boards is in the electronics. Where '
        'copper, the magnets, each steel and each aluminium alloy sit: one row per kind of part, its draws as a violin '
        'on a logarithmic axis, the median a filled dot, the mean an open one, the line the 95 % interval.',
    ]
    return [note for note in notes if note]


def notes_pages(prefix: str, title: str, paragraphs: list) -> list:
    """The notes, as (file name, figure): `<prefix>_notes_<k>.png`, its title and its paragraphs, each wrapped at
    TYPE_ONE_NOTE_WIDTH characters, as many to a page as fit within NOTES_LINES lines, a paragraph never split, on as
    many pages as they need, '(k of n)' where more than one (Matthias's rule: the notes once, on pages of their own).
    Type 1's element and material pages have their notes, its figures of where the critical elements sit theirs."""
    pages, page, lines = [], [], 0
    for paragraph in (textwrap.fill(p, TYPE_ONE_NOTE_WIDTH) for p in paragraphs):
        tall = paragraph.count('\n') + 1 + (1 if page else 0)   # its lines, and the blank line before it
        if page and lines + tall > NOTES_LINES:
            pages.append(page)
            page, lines, tall = [], 0, tall - 1
        page.append(paragraph)
        lines += tall
    pages.append(page)
    out = []
    for k, page in enumerate(pages, 1):
        figure = plt.figure(figsize=TYPE_ONE_PAGE)
        figure.text(0.04, 0.93, title + (f' ({k} of {len(pages)})' if len(pages) > 1 else ''),
                    fontsize=TYPE_ONE_HEADING, va='top')
        figure.text(0.04, 0.83, '\n\n'.join(page), fontsize=TYPE_ONE_TEXT, va='top', color=TYPE_ONE_INK,
                    linespacing=1.3)
        out.append((f'{prefix}_notes_{k}.png', figure))
    return out


def type_one_pages(c: Composition, d: Draws, left_out: list, params: Params) -> list:
    """Robot type 1's pages, as (file name, figure): the notes pages, then the elements nine a page, each element it
    holds but those not shown (`composition.elements_not_shown`), then its materials nine a page."""
    names = shown_elements(c.tables['elements'][0], params)
    shown = [e for e in names if held(c.column('elements', e))]   # in at least HELD_SHARE of the draws, as a material
    per_page = TYPE_ONE_ACROSS * TYPE_ONE_DOWN
    pages = [shown[k:k + per_page] for k in range(0, len(shown), per_page)]
    out = notes_pages(c.name, f'Robot type 1, {c.title}: how to read its element and material pages',
                      type_one_notes(c, d, left_out, params))
    for p, page in enumerate(pages, 1):
        figure, axes = plt.subplots(TYPE_ONE_DOWN, TYPE_ONE_ACROSS, figsize=TYPE_ONE_PAGE, squeeze=False)
        for k, symbol in enumerate(page):
            element_panel(axes[k // TYPE_ONE_ACROSS, k % TYPE_ONE_ACROSS], c.column('elements', symbol),
                          element_label(symbol),
                          k % TYPE_ONE_ACROSS == 0)
        for spare in axes.flatten()[len(page):]:
            spare.axis('off')
        figure.suptitle(f'Robot type 1, all its {len(d.register)} robots: each element in one robot ({p} of '
                        f'{len(pages)})', fontsize=TYPE_ONE_HEADING, y=0.985)
        figure.tight_layout(rect=(0, 0, 1, 0.955), h_pad=0.4, w_pad=2.5)
        out.append((f'{c.name}_elements_{p}.png', figure))
    return out + material_pages(c, d)


def draw_type_one_pages(c: Composition, d: Draws, left_out: list, folder: str, params: Params) -> list:
    """Robot type 1's pages into `folder`; returns their file names."""
    os.makedirs(folder, exist_ok=True)
    written = []
    for name, figure in type_one_pages(c, d, left_out, params):
        figure.savefig(os.path.join(folder, name), dpi=params.output.dpi, facecolor='white')
        plt.close(figure)
        written.append(name)
    return written


# ------------------------------------------------------------------------------------------------------
# Robot type 1's two figures of where its critical elements sit (until 2026-10-29 the stage 04)
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
# this before you sjhow me. Elements is an edge case. Also quite small"): TYPE_ONE_PAGE, no text below TYPE_ONE_TEXT
# points; fit to a 1920 × 1080 screen the smallest text is about 23 pixels tall (tests/test_parts_taken_apart.py
# requires 18 at least). No footnote under a page: the notes are once, on a page of their own, the first of the folder
# (Matthias, 2026-10-29: "parts taken apart show each a long legend, you know, what I think about this").
FIGURE_TITLE_WIDTH = 30   # characters in a line of an element page's panel title; a longer one takes two lines
# The overview's panels: their width (share of the page), and where their three columns of numbers start, the
# median's, the mean's and in what share of the draws the kind of part holds the element (share of the panel's width
# beyond its right edge), so that all three stay within the page and a number of eight characters (0.000022) clears
# the next (2026-10-29, "Yes, do it": the third column, the panels 0.42 of the page before). The figures of where a
# material sits keep their two columns, NUMBER_COLUMNS.
PANEL_WIDTH = 0.38
OVERVIEW_COLUMNS = (1.01, 1.18, 1.35)
NUMBER_COLUMNS = (1.02, 1.20)
ELEMENT_PAGES = [FIGURE_ELEMENTS[:6], FIGURE_ELEMENTS[6:]]                                # three panels across
OVERVIEW_PAGES = [FIGURE_ELEMENTS[k:k + 2] for k in range(0, len(FIGURE_ELEMENTS), 2)]    # two elements a page
PARTS_FIGURES = tuple([f'robot_type_1_elements_{k}.png' for k in range(1, len(ELEMENT_PAGES) + 1)]
                + [f'robot_type_1_overview_{k}.png' for k in range(1, len(OVERVIEW_PAGES) + 1)])

# Where each kind sits on the robot, its mark and the kinds whose colour takes white text: 01's (one copy).
MARKS, DARK = schemas.MARKS, schemas.DARK


def save_figure(figure, path: str, dpi: int) -> None:
    """Write a page and close it."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    figure.savefig(path, dpi=dpi, facecolor='white')
    plt.close(figure)


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
    return (f'{d.n:,} draws, each one of the {len(d.register)} robots of type 1 in the register, each as often (a '
            'robot in two versions, each as often); each robot from its own parts, part by part.')


def stacked_panel(axes, kinds: dict, title: str, share_label: bool) -> None:
    """One panel of the element pages, the form Matthias set for RAWCLICDataCenters' 05: the histogram of the robot's
    total of one element over the draws (the height the share of the draws), each bar split into the kg its draws hold
    in each kind of part, the kind with the smaller mean lower; the median a solid line and the mean a dotted one, each
    with its number (Matthias, 2026-10-28: "Showing the mean is wrong. It is not a good measure. Use the median or show
    boths"; his answer "Both, median first"); the 2.5th and 97.5th percentile dashed; its own scale and unit. Where the
    element is 0 in some draws (a robot or a version without it), the draws that hold it, and in what share of all the
    draws it is held, right of the title, as on the element pages (element_panel)."""
    axes.set_title(title, fontsize=TYPE_ONE_TITLE, fontweight='bold', loc='left')
    if not kinds:
        axes.text(0.5, 0.5, 'none in robot type 1', transform=axes.transAxes, ha='center', va='center',
                  fontsize=TYPE_ONE_TEXT)
        axes.set_xticks([])
        axes.set_yticks([])
        return
    total = sum(kinds.values())
    drawn = [k for k in kinds if held(kinds[k])]   # the kinds holding it in at least HELD_SHARE of all the draws
    inside = total > 0
    if not inside.all():
        axes.set_title(f'in {panel_number(100 * inside.mean())} % of the draws', loc='right', fontsize=TYPE_ONE_TEXT,
                       color=TYPE_ONE_INK)
        kinds = {k: v[inside] for k, v in kinds.items()}
        total = total[inside]
    per, unit = panel_unit(total)
    values = total / per
    edges = np.histogram_bin_edges(values, bins=TYPE_ONE_BINS)
    index = np.clip(np.digitize(values, edges[1:-1]), 0, len(edges) - 2)   # the bar each draw falls into
    share_of_draws = np.bincount(index, minlength=len(edges) - 1) / values.size
    kg_all = np.bincount(index, weights=total, minlength=len(edges) - 1)
    bottom = np.zeros(len(edges) - 1)
    for kind in sorted(drawn, key=lambda k: kinds[k].mean()):
        kg = np.bincount(index, weights=kinds[kind], minlength=len(edges) - 1)
        height = share_of_draws * np.divide(kg, kg_all, out=np.zeros_like(kg), where=kg_all > 0)
        axes.bar(edges[:-1], height, width=np.diff(edges), align='edge', bottom=bottom, color=KINDS[kind][1],
                 edgecolor='none')
        bottom += height
    median, mean = float(np.median(values)), float(values.mean())
    axes.axvline(median, color=TYPE_ONE_INK, linewidth=1.8)
    axes.axvline(mean, color=TYPE_ONE_INK, linewidth=1.8, linestyle=':')
    for bound in np.percentile(values, [2.5, 97.5]):
        axes.axvline(bound, color=TYPE_ONE_INK, linewidth=1.2, linestyle='--')
    for x, y, what in ((median, 0.97, 'median'), (mean, 0.82, 'mean')):
        axes.text(x, y, f' {what} {panel_number(x)} {unit}', transform=axes.get_xaxis_transform(), ha='left',
                  va='top', fontsize=TYPE_ONE_TEXT, color=TYPE_ONE_INK,
                  bbox=dict(facecolor='white', edgecolor='none', alpha=0.8, pad=1))
    axes.xaxis.set_major_locator(plt.MaxNLocator(4))
    axes.xaxis.set_major_formatter(plt.FuncFormatter(panel_number))
    axes.yaxis.set_major_locator(plt.MaxNLocator(4))
    axes.yaxis.set_major_formatter(plt.FuncFormatter(panel_number))
    axes.tick_params(labelsize=TYPE_ONE_TEXT)
    axes.set_xlabel(f'mass ({unit})', fontsize=TYPE_ONE_LABEL)
    if share_label:
        axes.set_ylabel('share of the draws', fontsize=TYPE_ONE_LABEL)
    axes.grid(axis='x', alpha=0.3)


def element_page(d: Draws, page: list, number: int):
    """One page of the element figure Matthias approved (V49), for the three robots: its elements three across, each
    the stacked distribution of the robot's total; the legend of the kinds of part at the top."""
    columns = 3
    figure, axes = plt.subplots(2, columns, figsize=TYPE_ONE_PAGE, squeeze=False)
    for k, (symbol, name) in enumerate(page):
        stacked_panel(axes[k // columns, k % columns], by_kind(d, symbol),
                      textwrap.fill(f'{name} ({symbol})', FIGURE_TITLE_WIDTH), k % columns == 0)
    for spare in axes.flatten()[len(page):]:
        spare.axis('off')
    figure.suptitle(f'Robot type 1, all its {len(d.register)} robots: critical elements in one robot ({number} of '
                    f'{len(ELEMENT_PAGES)})', fontsize=TYPE_ONE_HEADING, y=0.985)
    handles = [Patch(color=colour, label=label) for label, colour in KINDS.values()]
    figure.legend(handles=handles, loc='upper center', bbox_to_anchor=(0.5, 0.94), ncol=5, frameon=False,
                  fontsize=TYPE_ONE_TEXT)
    figure.tight_layout(rect=(0, 0.01, 1, 0.86))
    return figure


def ridge_panel(axes, kinds: dict, estimated: dict, title: str) -> None:
    """One panel of the overview: one row per kind of part holding the element, labelled with its mark on the robot,
    each the histogram of its kg over the draws that hold it scaled to the row, hatched where more than half its mean
    rests on masses labelled E; the median a solid line and the mean a dotted one (answer "Both, median first"), the
    2.5th and 97.5th percentile dashed, all of the draws that hold it; at the right three columns: the median, the mean
    and in what share of the draws the kind of part holds the element (Matthias, 2026-10-29, "Yes, do it", to the
    overview's rows as the element panels: a kind of part holding it in only some draws showed a median of 0); one
    scale and unit for the panel."""
    shown = [k for k in KINDS if k in kinds and held(kinds[k])]
    axes.set_title(title, fontsize=TYPE_ONE_TITLE, fontweight='bold', loc='left')
    if not shown:
        axes.text(0.5, 0.5, 'none in robot type 1', transform=axes.transAxes, ha='center', va='center',
                  fontsize=TYPE_ONE_TEXT)
        axes.axis('off')
        return
    per, unit = panel_unit(sum(kinds[k] for k in shown))
    holding = {k: kinds[k][kinds[k] > 0] for k in shown}   # the draws in which the kind of part holds the element
    top = max(np.percentile(holding[k], 99.9) for k in shown) / per
    edges = np.linspace(0, top if top > 0 else 1, 51)
    right = blended_transform_factory(axes.transAxes, axes.transData)
    for row, kind in enumerate(reversed(shown)):
        values = holding[kind] / per
        counts, _ = np.histogram(np.clip(values, 0, edges[-1]), bins=edges)
        heights = 0.8 * counts / max(counts.max(), 1)
        hatched = float(estimated[kind].mean()) > 0.5 * float(kinds[kind].mean())
        axes.bar(edges[:-1], heights, width=np.diff(edges), align='edge', bottom=row + 0.05, color=KINDS[kind][1],
                 edgecolor=TYPE_ONE_INK if hatched else 'none', linewidth=0, hatch='///' if hatched else None)
        median, mean = float(np.median(values)), float(values.mean())
        axes.plot([median, median], [row + 0.05, row + 0.9], color=TYPE_ONE_INK, linewidth=1.8)
        axes.plot([mean, mean], [row + 0.05, row + 0.9], color=TYPE_ONE_INK, linewidth=1.8, linestyle=':')
        for bound in np.percentile(values, [2.5, 97.5]):
            axes.plot([bound, bound], [row + 0.05, row + 0.9], color=TYPE_ONE_INK, linewidth=1.2, linestyle='--')
        share = holding[kind].size / kinds[kind].size
        for column, number in zip(OVERVIEW_COLUMNS, (panel_number(median), panel_number(mean),
                                                     f'{panel_number(100 * share)} %')):
            axes.text(column, row + 0.45, number, transform=right, ha='left', va='center', fontsize=TYPE_ONE_TEXT,
                      color=TYPE_ONE_INK)
    for column, what in zip(OVERVIEW_COLUMNS, ('median', 'mean', 'held in')):
        axes.text(column, len(shown) + 0.1, what, transform=right, ha='left', va='bottom', fontsize=TYPE_ONE_TEXT,
                  color=TYPE_ONE_INK)
    axes.set_title(f'{title}, in {unit}', fontsize=TYPE_ONE_TITLE, fontweight='bold', loc='left')
    axes.set_ylim(0, len(shown))
    axes.set_yticks([row + 0.45 for row in range(len(shown))])
    axes.set_yticklabels([f'{MARKS[k]}  {KINDS[k][0]}' for k in reversed(shown)], fontsize=TYPE_ONE_TEXT)
    axes.tick_params(axis='y', length=0)
    axes.set_xlim(0, edges[-1])
    axes.xaxis.set_major_locator(plt.MaxNLocator(6))
    axes.xaxis.set_major_formatter(plt.FuncFormatter(panel_number))
    axes.tick_params(axis='x', labelsize=TYPE_ONE_TEXT)
    axes.set_xlabel(f'mass ({unit})', fontsize=TYPE_ONE_LABEL)
    axes.grid(axis='x', alpha=0.3)
    for side in ('top', 'right'):
        axes.spines[side].set_visible(False)


def draw_schema(axes, d: Draws) -> None:
    """The robot of the overview: 01's robot with its kinds of part (draw_kinds), the joints whose magnets are for
    150 °C or more in most draws ringed red."""
    schemas.draw_kinds(axes, d.hot, TYPE_ONE_TEXT)


def overview_page(d: Draws, page: list, number: int):
    """One page of the overview Matthias approved ("Looks good to me", 2026-10-27), for three robots (answer E,
    "Groups, histograms"): left the robot with its joint groups numbered and its other kinds lettered; right two
    critical elements, one above the other, one row per kind of part holding them."""
    figure = plt.figure(figsize=TYPE_ONE_PAGE)
    figure.add_axes((0.01, 0.04, 0.22, 0.85))
    draw_schema(figure.axes[0], d)
    panels = [(symbol, name, by_kind(d, symbol)) for symbol, name in page]
    rows = [sum(held(v) for v in kinds.values()) + 1 for _, _, kinds in panels]
    bottom, top, gap = 0.09, 0.875, 0.11
    height = top - bottom - gap * (len(panels) - 1)
    for k, (symbol, name, kinds) in enumerate(panels):
        tall = height * rows[k] / sum(rows)
        y = top - tall - sum(height * rows[i] / sum(rows) + gap for i in range(k))
        estimated = {kind: sum((d.estimated[(kind, e)] for e in symbol.split('+') if (kind, e) in d.estimated),
                               np.zeros(d.n)) for kind in kinds}
        ridge_panel(figure.add_axes((0.43, y, PANEL_WIDTH, tall)), kinds, estimated, f'{name} ({symbol})')
    figure.suptitle('Robot type 1 taken apart: where the critical materials sit, and how sure we are '
                    f'({number} of {len(OVERVIEW_PAGES)})', fontsize=TYPE_ONE_HEADING, y=0.975)
    return figure


def parts_notes(d: Draws) -> list:
    """The paragraphs of the notes page of both figures, once for all their pages (until 2026-10-29 a footnote under
    every page)."""
    return [
        'The element pages: one panel per critical element, its bars the draws of the element in one robot, the '
        'height the share of the draws, each bar split into the weight its draws hold in each kind of part, the '
        'smaller lower. Solid line: the median; dotted line: the mean; dashed lines: the 2.5th and 97.5th percentile '
        '(95 % of the draws between them). Each panel on its own scale and unit. An element that is 0 in some draws: '
        'its panel shows the draws that hold it and says in what share of all the draws it is held.',
        "The overview pages: each row the element's weight in one kind of part over the draws that hold it, the "
        'height the share of those draws scaled to the row, the lines as on the element pages, of those draws; at the '
        "right their median and mean, and 'held in': in what share of all the draws the kind of part holds the "
        'element. Hatched: more than half of the mean rests on parts whose mass is an estimate.',
        'On both: a kind of part holding the element in fewer than 2.5 % of the draws is not drawn.',
        robots_note(d),
        "The joints with their driver boards and encoders; the magnets' grade class (with it their dysprosium) drawn "
        "by each joint's heat, the knees hottest, the arms coolest, one draw deciding for every joint; the NdFeB "
        'magnets shown by their neodymium and praseodymium; the battery metals and silicon not shown.',
    ]


def parts_figure_pages(d: Draws) -> list:
    """Every page of both figures, as (file name, figure): their notes pages first, then the figures in the order of
    PARTS_FIGURES."""
    pages = [element_page(d, page, k + 1) for k, page in enumerate(ELEMENT_PAGES)]
    pages += [overview_page(d, page, k + 1) for k, page in enumerate(OVERVIEW_PAGES)]
    return notes_pages('robot_type_1', f'Robot type 1, all its {len(d.register)} robots: how to read the pages of '
                       'where its critical elements sit', parts_notes(d)) + list(zip(PARTS_FIGURES, pages))


def draw_parts_figures(d: Draws, params: Params) -> None:
    """Every page of both figures, and the figures of where each material sits (sources_pages), into
    `output.parts_figures_dir`."""
    folder = absolute(params.output.parts_figures_dir)
    for name, figure in parts_figure_pages(d) + sources_pages(d):
        save_figure(figure, os.path.join(folder, name), params.output.dpi)


# ------------------------------------------------------------------------------------------------------
# Robot type 1's material pages, as RAWCLICDataCenters draws its materials
# ------------------------------------------------------------------------------------------------------
# Matthias, 2026-10-29: "There are only figures on the element level I want to see, how much Copper and especially
# permanent magnets. The different steels and aluminum alyoys. We had this differently in datacenters", then "Yes, 1 to
# 5": the materials of one robot, one panel each (as the data centres' "materials of one data center"), the steels by
# their grade, the aluminium by its alloys, the permanent magnets in all and by their grade class; and for copper, the
# magnets, each steel and each aluminium alloy, where it sits, kind of part by kind of part (as the data centres' "where
# the copper comes from").

# The materials of the pages in this order; any other material follows them.
MATERIAL_ORDER = (COPPER, MAGNETS, 'Steel', 'Aluminium', 'Titanium', 'Plastics', CELL_MATERIAL, ELECTRONICS, 'Mixed',
                  'Ceramics', 'Fibre composites', 'Magnesium')
# Each material in plain words, and each grade, alloy or recipe whose name is a code (the others keep their recipe's
# name, e.g. 'Aluminium 6061').
MATERIAL_TITLES = {COPPER: 'Copper', MAGNETS: 'Permanent magnets', CELL_MATERIAL: 'Battery cells',
                   ELECTRONICS: 'Electronics'}
GRADE_TITLES = {'20CrMnTi': 'Gear steel 20CrMnTi', 'GCr15': 'Bearing steel GCr15', '42CrMo4': 'Alloy steel 42CrMo4',
                'C45': 'Carbon steel C45', 'P20': 'Tool steel P20', '17-4PH': 'Stainless steel 17-4PH',
                'Type 304': 'Stainless steel 304', '440C': 'Stainless steel 440C', 'M19': 'Electrical steel M19',
                'M27': 'Electrical steel M27',
                'Ti-6Al-4V': 'Titanium Ti-6Al-4V', 'Brass': 'Brass', 'Nickel strip': 'Nickel strips, battery',
                'NMC cylindrical': 'Battery cells, NMC (cylindrical)', 'LFP cylindrical': 'Battery cells, LFP '
                                                                                           '(cylindrical)'}
# The materials whose "where it comes from" figure is drawn, each grade and alloy of them: copper, the magnets (in
# all), the steels and the aluminium (point 3 of his yes).
SOURCES_OF = (COPPER, MAGNETS, 'Steel', 'Aluminium')
SOURCES_FOLDER = 'sources'   # within `output.parts_figures_dir`
VIOLIN = '#4477AA'           # Paul Tol's bright blue, as published (the bars of the pages)


def material_panels(d: Draws) -> list:
    """The panels of the material pages, in their order: (title, the material, its grade, alloy or class ('' for the
    material whole, None for the magnets in all), kind -> kg in each draw). The magnets come in all and then by grade
    class; a material with grades or alloys by each of them."""
    materials = [m for m in MATERIAL_ORDER if any(k[1] == m for k in d.details)]
    materials += sorted({k[1] for k in d.details} - set(materials))
    order = list(schemas.MAGNET_CLASSES)
    panels = []
    for material in materials:
        details = sorted({k[2] for k in d.details if k[1] == material},
                         key=lambda x: (order.index(x) if material == MAGNETS and x in order else 0, x != '', x))
        if material == MAGNETS:
            kinds = {kind: sum(kg for (k, m, _), kg in d.details.items() if k == kind and m == material)
                     for kind in KINDS if any(k == kind and m == material for k, m, _ in d.details)}
            panels.append((MATERIAL_TITLES[MAGNETS], material, None, kinds))
        for detail in details:
            kinds = {k: kg for (k, m, x), kg in d.details.items() if m == material and x == detail}
            if material == MAGNETS:
                title = f'Magnets, grade class {detail}'
            elif detail:
                title = GRADE_TITLES.get(detail, detail)
            else:
                title = MATERIAL_TITLES.get(material, material)
            panels.append((title, material, detail, kinds))
    return [p for p in panels if held(sum(p[3].values()))]


def material_panel(axes, kg: np.ndarray, title: str, first_in_row: bool) -> None:
    """One material in one robot over the draws, drawn as an element of type 1's element pages (element_panel, also
    where the material is 0 in some draws), its title wrapped."""
    element_panel(axes, kg, textwrap.fill(title, FIGURE_TITLE_WIDTH), first_in_row)


def material_pages(c: Composition, d: Draws) -> list:
    """Type 1's material pages, as (file name, figure): its materials nine a page, each the histogram of its kg in one
    robot over the draws."""
    panels = material_panels(d)
    per_page = TYPE_ONE_ACROSS * TYPE_ONE_DOWN
    pages = [panels[k:k + per_page] for k in range(0, len(panels), per_page)]
    out = []
    for p, page in enumerate(pages, 1):
        figure, axes = plt.subplots(TYPE_ONE_DOWN, TYPE_ONE_ACROSS, figsize=TYPE_ONE_PAGE, squeeze=False)
        for k, (title, _, _, kinds) in enumerate(page):
            material_panel(axes[k // TYPE_ONE_ACROSS, k % TYPE_ONE_ACROSS], sum(kinds.values()), title,
                           k % TYPE_ONE_ACROSS == 0)
        for spare in axes.flatten()[len(page):]:
            spare.axis('off')
        figure.suptitle(f'Robot type 1, all its {len(d.register)} robots: each material in one robot ({p} of '
                        f'{len(pages)})', fontsize=TYPE_ONE_HEADING, y=0.985)
        figure.tight_layout(rect=(0, 0, 1, 0.955), h_pad=0.4, w_pad=2.5)
        out.append((f'{c.name}_materials_{p}.png', figure))
    return out


def log_mass(log_kg: float, _pos=None) -> str:
    """A tick of a logarithmic mass axis, its power of ten of kg in plain units: '1 mg', '10 g', '1 kg'."""
    kg = 10 ** log_kg
    per, unit = panel_unit(np.array([kg]))
    return f'{panel_number(kg / per)} {unit}'


def sources_figure(title: str, kinds: dict, d: Draws):
    """Where one material sits in robot type 1, as RAWCLICDataCenters' "where the copper comes from": one row per kind
    of part holding it (in at least 2.5 % of the draws), the largest median on top; each the violin of its kg over the
    draws above 0 on a logarithmic axis, the median a filled dot and the mean an open one, the 95 % interval a line
    (from the left edge where it starts at 0), the median and the mean written at the right."""
    shown = sorted((k for k in kinds if held(kinds[k])), key=lambda k: float(np.median(kinds[k])))
    figure = plt.figure(figsize=TYPE_ONE_PAGE)
    axes = figure.add_axes((0.22, 0.12, 0.6, 0.76))
    lows = [np.log10(kinds[k][kinds[k] > 0]).min() for k in shown]
    highs = [np.log10(kinds[k][kinds[k] > 0]).max() for k in shown]
    left, right = np.floor(min(lows)), np.ceil(max(highs))
    numbers = blended_transform_factory(axes.transAxes, axes.transData)
    for row, kind in enumerate(shown):
        values = kinds[kind]
        logs = np.log10(values[values > 0])
        if logs.max() > logs.min():
            body = axes.violinplot([logs], positions=[row], orientation='horizontal', widths=0.8,
                                  showextrema=False)['bodies'][0]
            body.set_facecolor(VIOLIN)
            body.set_edgecolor('none')
            body.set_alpha(0.6)
        low, high = np.percentile(values, [2.5, 97.5])
        median, mean = float(np.median(values)), float(values.mean())
        axes.plot([np.log10(low) if low > 0 else left, np.log10(high)], [row, row], color=TYPE_ONE_INK, linewidth=1.6)
        if median > 0:
            axes.plot(np.log10(median), row, 'o', color=TYPE_ONE_INK, markersize=8)
        axes.plot(np.log10(mean), row, 'o', markerfacecolor='white', markeredgecolor=TYPE_ONE_INK, markersize=8)
        for column, x in zip(NUMBER_COLUMNS, (median, mean)):
            per, unit = panel_unit(np.array([x]))
            axes.text(column, row, f'{panel_number(x / per)} {unit}', transform=numbers, ha='left', va='center',
                      fontsize=TYPE_ONE_TEXT, color=TYPE_ONE_INK)
    for column, what in zip(NUMBER_COLUMNS, ('median', 'mean')):
        axes.text(column, len(shown) - 0.4, what, transform=numbers, ha='left', va='bottom', fontsize=TYPE_ONE_TEXT,
                  color=TYPE_ONE_INK)
    axes.set_yticks(range(len(shown)))
    axes.set_yticklabels([KINDS[k][0] for k in shown], fontsize=TYPE_ONE_TEXT)
    axes.set_ylim(-0.6, len(shown) - 0.4)
    axes.set_xlim(left, right)
    axes.xaxis.set_major_locator(plt.MultipleLocator(1))
    axes.xaxis.set_major_formatter(plt.FuncFormatter(log_mass))
    axes.tick_params(axis='x', labelsize=TYPE_ONE_TEXT)
    axes.tick_params(axis='y', length=0)
    axes.set_xlabel('mass in one robot (logarithmic axis)', fontsize=TYPE_ONE_LABEL)
    axes.grid(axis='x', alpha=0.3)
    for side in ('top', 'right'):
        axes.spines[side].set_visible(False)
    figure.suptitle(f'Robot type 1, all its {len(d.register)} robots: where its {title[0].lower()}{title[1:]} sits',
                    fontsize=TYPE_ONE_HEADING, y=0.96)
    return figure


def sources_pages(d: Draws) -> list:
    """Every "where it comes from" figure, as (file name, figure): copper, the magnets in all, each steel and each
    aluminium alloy (SOURCES_OF), in the order of the material pages."""
    out = []
    for title, material, detail, kinds in material_panels(d):
        if material in SOURCES_OF and not (material == MAGNETS and detail is not None):
            name = '_'.join(''.join(ch if ch.isalnum() else ' ' for ch in title).split())
            out.append((os.path.join(SOURCES_FOLDER, f'{name}.png'), sources_figure(title, kinds, d)))
    return out


def run(params: Params) -> int:
    """Reads and checks the inputs, draws every robot type, checks every draw, and only then writes. 0 when it has
    written, 1 when a fault stopped it (nothing written)."""
    try:
        inputs = read_inputs(params)
        register = schemas.read_register(absolute(params.data.register))
        # Robot type 1's robots: those of the register's sheet Type 1, checked below against its sheet Robots. Type 1 is
        # drawn part by part where its robots have rows in the parts file.
        type_one = schemas.read_type_sheet(absolute(params.data.register), TYPE_ONE)
        apart = read_apart_inputs(params, inputs, type_one) if any(r.taken_apart for r in type_one) else None
    except schemas.WorkbookError as error:
        print(error, file=sys.stderr)
        return 1
    faults = (all_faults(inputs, params)
              + schemas.check_register(register, params, list(apart.apart.robots) if apart else [])
              + schemas.check_type_sheet(register, type_one, TYPE_ONE, params))
    if apart is not None:
        faults += apart_faults(apart, params)
    if faults:
        print(f'{len(faults)} fault(s) in the inputs; nothing is drawn. 01_schemas.py shows them on faults.png.',
              file=sys.stderr)
        for fault in faults:
            print(f"  sheet '{fault.sheet}', row {fault.row}: {fault.text}", file=sys.stderr)
        return 1

    drawn, taken = [], None
    for category in inputs.book.categories:
        if apart is not None and category.number == TYPE_ONE:
            magnets = magnet_fractions(params, grade_classes(apart), params.composition.draws)
            taken = draw_type_one(apart, params, magnets)
            drawn.append(compose_type_one(category, taken, inputs.lists))
        else:
            drawn.append(compose(category, inputs, params))
    same_elements(drawn)
    problems = [problem for c in drawn for problem in draw_faults(c)]
    if problems:
        print('The draws do not add up; nothing is written.', file=sys.stderr)
        for problem in problems:
            print(f'  {problem}', file=sys.stderr)
        return 1

    out, pages = absolute(params.output.composition_dir), absolute(params.output.composition_figures_dir)
    print(f'{params.composition.draws:,} draws per robot type, seed {params.composition.seed}.')
    with_pages = params.output.robot_types_with_pages   # Matthias, 2026-10-29: "Type 1 only"
    for c in drawn:
        write(c, os.path.join(out, c.name))
        # Its draws are written for every robot type; its pages only where the setting names it.
        if c.number in with_pages and taken is not None and c.number == TYPE_ONE:
            draw_type_one_pages(c, taken, apart.left_out, pages, params)
        elif c.number in with_pages:
            draw_page(c, params.composition.draws, os.path.join(pages, c.name + '.png'), params)
        rows = {r['Name']: r for r in summary(c) if r['Kind'] == 'Material'}
        stats = statistics_of(c.column('total', 'Total'))
        missing = [name for name, r in rows.items()
                   if r['In the elements'] in ('No', 'Partly') and name != NOT_ALLOCATED]
        print(f"  {c.number} {c.title}: {stats['Mean (kg)']:.1f} kg at the mean (95 %: {stats['2.5 % (kg)']:.1f} to "
              f"{stats['97.5 % (kg)']:.1f}); Not allocated below zero in "
              f"{rows[NOT_ALLOCATED]['Draws below zero (%)']:.1f} % of the draws; not yet in the elements: "
              f"{', '.join(missing) or 'none'}.")
    if taken is not None:
        write_taken_apart(taken, absolute(params.output.parts_dir))
        print(f"  Robot type 1 drawn over {len(taken.register)} robots of the register's sheet Type 1; not drawn (no "
              f'mass stated): '
              f"{', '.join(f'{r.number} {r.name}' for r in apart.left_out) or 'none'}.")
        for column, share in below_zero(taken).items():
            if share > 0:
                print(f'  {column} is below zero in {100 * share:.1f} % of its draws (reported, not cut).')
        print(f'  Robot type 1 part by part written into {params.output.parts_dir}/.')
        if TYPE_ONE in with_pages:
            draw_parts_figures(taken, params)
            for symbol, name in FIGURE_ELEMENTS:
                total = sum(by_kind(taken, symbol).values())
                per, unit = panel_unit(total)
                mean, median, low, high = statistics(total / per)
                print(f'  {name} in one robot: median {panel_number(median)} {unit}, mean {panel_number(mean)} {unit} '
                      f'(95 %: {panel_number(low)} to {panel_number(high)})')
            print(f'  Its two figures and where each material sits drawn into {params.output.parts_figures_dir}/.')
    print(f'Written into {params.output.composition_dir}/, one folder per robot type, and the pages into '
          f'{params.output.composition_figures_dir}/.')
    return 0


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
