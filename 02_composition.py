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
types are fully listed. For now it has to be just all for type 1."). Where the robots of the sheet Type 1 include one
taken apart (the Unitree G1, AgiBot X1 and Fourier N1), type 1 is drawn over the robots of that sheet from the robots
taken apart; for it 02 also reads the parts file (`data.parts_taken_apart`), the sibling projects' files where they
lie (RAWCLICVehicleElectronics' board metals and sensor elements, RAWCLICDataCenters' tantalum) and runs
RAWCLICVehicleTractionMotor's own code in its own environment for the elements of the magnets.

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

HOW IT DRAWS ROBOT TYPE 1 (Matthias, 2026-10-28: "Yes in 02 it is all type 1 in.!", "Yes, code it in 02")
-----------------------------------------------------------------------------------------------------
  - Each draw is one of the robots of the register's sheet Type 1, all equally often; those without a stated mass
    are not drawn (named on the notes page; the sheet says "not drawn"). Its mass: a triangle on its register mass
    (the stated mass +- 1 kg, or its range).
  - Its parts: those of the robot taken apart that it is, else those of one of the three, each as often. The factor
    its mass over that robot's own scales the joints whole, with all inside them, and the parts of the kinds "Frame
    and shell" and "Battery pack" (the pack's energy too); not the boards outside the joints, the sensors, the cables
    and connectors, the fans and heat sinks, the hands and grippers.
  - The joints: each component of the G1's joint (sheet JointParts) drawn once in each draw for each joint size and
    shared by all the joints of that size; the large joint's the small one's grams times its factor. The X1's and N1's
    joints: their module mass drawn for each joint kind, their inside the G1's of their size times the module mass over
    the G1 joint's mass at its modes, and the joint's structure (housing, end caps, output flange, small bearings) the
    explicit remainder, so that the joint weighs its drawn module mass.
  - A part of shares (sheet Shares): each share a triangle, the remainder 1 minus the others. Elements: aluminium and
    plastics by type 1's recipes, the NMC cells by theirs with the energy per kg drawn; copper is copper; the magnets
    by the grade class drawn for their joint's heat group (sheet MagnetGrades), one draw of heat deciding for every
    joint how hot the robot is built for; boards: copper their mass times the copper share, gold, silver, palladium,
    tin and nickel their area times the car board category's mg per cm2, tantalum their mass times the data centres'
    share; sensors: their car sensor elements. Steel, titanium and the mixed parts have no recipe yet.
  - The battery cells: the pack's voltage times its capacity over the cells' energy per kg; its housing the pack less
    its cells and its management board. The cables: their length times the four conductors' cross-sections times
    copper's density, and their insulation. The frame: the robot's mass less every other part; where it falls below
    zero it is reported, not cut.
  - Its part groups and body regions: its ten kinds of part placed whole (KIND_PART_GROUP, KIND_BODY_REGION).

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

For robot type 1 also, into `output.parts_dir` (`data/parts_taken_apart/`, for 04): robots.npy (the robot taken apart
whose parts each draw takes, its own mass, the draw's mass, the robot of the register drawn), parts.npy, materials.npy,
elements.npy and estimated.npy (every element in every kind of part, and its kg resting on masses labelled E), each
with its columns in the .txt of the same name; register.txt (the robots of the register drawn) and summary.csv.

Every robot type has the same columns of elements, all those any of them holds (0 where a robot type's materials hold
none so far). Into `output.composition_figures_dir` (`figures/composition/`; not in git): for robot type 1 a notes page
(<n>_<name>_notes.png) and its elements nine a page (<n>_<name>_elements_<k>.png), each element as its total in one
robot over the draws; for the other robot types one page each, <n>_<name>.png: its kg by material and its kg by
element, each bar the mean with a line over 95 % of the draws (point 14).

Where it sits: after 01_schemas.py. 03_comparison.py reads what it writes.
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

    def add(self, recipe: str, within: str, weight: np.ndarray, f: np.ndarray | None, out: dict) -> None:
        """Adds to `out` the elements of the items of `recipe` that sit within `within`, which make up `weight` of the
        recipe in every draw."""
        items = self.members[(recipe, within)]
        if items[0].probability is not None:
            # Alternatives: one is drawn in each draw, by its probability; it takes the group's whole weight.
            key = (recipe, within)
            if key not in self.states:
                self.states[key] = self.rng.choice(len(items), size=self.n, p=[i.probability for i in items])
            parts = [(i, (self.states[key] == k).astype(float)) for k, i in enumerate(items)]
        else:
            # Shares: each drawn, the remainder 1 minus the others, never below zero (01 checks the largest shares).
            parts = [(i, self.share(i, f)) for i in items if not i.remainder]
            rest = 1 - sum(share for _, share in parts) if parts else np.ones(self.n)
            if rest.min() < -SUM_TOLERANCE:
                raise ValueError(f"{recipe}, within '{within or 'the recipe itself'}': the remainder falls below zero "
                                 f'in {(rest < -SUM_TOLERANCE).sum()} draws.')
            parts += [(i, rest) for i in items if i.remainder]
        for i, share in parts:
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
# Robot type 1 over its robots: what is known of the robots taken apart
# ------------------------------------------------------------------------------------------------------

TYPE_ONE = 1   # the robot type of the workbook's Taxonomy whose robots the data file holds

# The ten kinds of part of both figures, in the order of their legend, each with its colour: Paul Tol's discrete
# rainbow for 10 colours, as published, with the frame's and the battery's colours swapped so that the frame stands
# apart from the hip joints in aluminium (Matthias, 2026-10-27: "not bad with expection of the aluminum"; V49).
KINDS = {
    'hips': ('Hip joints', '#882E72'),
    'knees': ('Knee joints', '#1965B0'),
    'ankles': ('Ankle joints', '#7BAFDE'),
    'waist': ('Waist joints', '#4EB265'),
    'arms': ('Arm joints and hands', '#CAE0AB'),
    'battery': ('Battery pack', '#72190E'),
    'boards': ('Torso boards and heat sink', '#F4A736'),
    'head': ('Head', '#E8601C'),
    'cables': ('Cables', '#DC050C'),
    'frame': ('Frame and shell', '#F7F056'),
}
# The kind of a joint, by the first word of its name in the sheet Joints.
JOINT_KIND = {'hip': 'hips', 'knee': 'knees', 'ankle': 'ankles', 'waist': 'waist', 'shoulder': 'arms',
              'elbow': 'arms', 'wrist': 'arms'}
# The kind of a part, board or sensor, by its column "Kind (the figure's row)".
KIND_OF = {'Hips': 'hips', 'Knees': 'knees', 'Waist': 'waist', 'Arms': 'arms', 'Battery pack': 'battery',
           'Torso boards': 'boards', 'Head': 'head', 'Cables': 'cables', 'Frame and shell': 'frame'}
# The values of that column that are the joints themselves, or sit in them (driver boards, encoders): drawn with the
# joints, joint kind by joint kind.
IN_THE_JOINTS = {'Ankles and arms', 'Hips, knees and waist', 'Hips, knees, waist and shoulders', 'In the joints'}
# What follows the varied mass besides the joints (answer B, "Joints whole, as listed"): the parts of these kinds.
SCALED_KINDS = {'Frame and shell', 'Battery pack'}

# How a part of the sheet Parts is computed, by the start of its column "Remainder of, or computed from".
FROM_JOINTS = ('the sum of JointParts', "the Joints' module masses")   # the joint modules: drawn with the joints
FROM_SENSORS = 'Sensors and SensorElements'                            # the encoders: their elements only
PACK = 'its cells, its management board'                               # the battery pack: its cells and housing
CELLS = 'from the energy'                                              # the battery cells
HOUSING = 'the battery pack, less'                                     # the battery housing: a remainder
CABLES = 'from Constants: length'                                      # the cables' conductors and insulation
FRAME = schemas.ROBOT_REMAINDER                                        # the frame: the robot's remainder
COMPUTED = FROM_JOINTS + (FROM_SENSORS, PACK, CELLS, HOUSING, CABLES, FRAME)

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
# The NdFeB grade classes for 150 °C and above (RAWCLICVehicleTractionMotor's sheet PermanentMagnetNdFeB): a joint
# whose heat group draws one of them in most draws is ringed red in the overview.
HOT_CLASSES = {'SH', 'UH', 'EH', 'AH'}

# The quantities of the sheet Constants this stage uses, as the sheet writes them.
ROBOT_MASS, VOLTAGE, CAPACITY, CABLE_LENGTH = ('Robot mass, with battery', 'Battery voltage', 'Battery capacity',
                                               'Cable length (four conductors)')
BOARD_G_PER_CM2, BOARD_COPPER = 'Board mass per cm2 (boards not weighed)', "Copper share of a board's mass"
POWER_CS, SIGNAL_CS = 'Power conductor cross-section (2 conductors)', 'Signal conductor cross-section (2 conductors)'
DENSITY, INSULATION = 'Copper density', 'Insulation and jackets, per mass of copper'

# The critical elements whose kilograms resting on estimates (E) are followed, for 04's overview (its hatching).
TRACKED = {'Cu', 'Al', 'Ag', 'Au', 'Pd', 'Ta', 'Nd', 'Pr', 'Dy', 'Ga', 'In'}

# What is written of robot type 1 taken apart, for 04, in this order: each a file <name>.npy with its columns in
# <name>.txt.
APART_TABLES = ('robots', 'parts', 'materials', 'elements', 'estimated')

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
    """Everything 02 reads for the robot types drawn from robots taken apart."""

    base: object          # Inputs: the workbook, the shared lists and the element recipes
    apart: object         # schemas.PartsTakenApart: the robots of type 1 taken apart
    pcb: dict             # car board category -> element -> (min, mode, max), mg per cm2 of board
    sensor_types: dict    # car sensor type -> element -> (min, mode, max), mg per unit
    tantalum: tuple       # kg of tantalum per kg of board: min, mode, max
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
    of_type = [r for r in register if TYPE_ONE in r.types]
    drawn = [r for r in of_type if None not in r.mass]
    return ApartInputs(base, apart, pcb, sensor_types, tantalum, drawn, [r for r in of_type if r not in drawn])


def base_robot(apart) -> str | None:
    """The robot whose joints follow the sheet JointParts directly (no module masses of their own): the G1, whose
    joint was weighed. The other robots' joints follow its inside."""
    found = [name for name in apart.robots
             if all(None in j.module_mass for j in apart.joints if j.robot == name)]
    return found[0] if len(found) == 1 else None


def check_parts(inputs: ApartInputs) -> list:
    """The checks 02 adds to 01's for robot type 1 taken apart: one robot whose joints follow JointParts; every
    joint, part, board and sensor goes to a kind of part; every part computed in a way 02 knows; every robot of type 1;
    the driver board a component of JointParts; the recipes it uses there; the tantalum row read."""
    apart, faults = inputs.apart, []
    on = 'parts_taken_apart.xlsx: '
    if base_robot(apart) is None:
        faults.append(Fault(on + 'Joints', 0, 'exactly one robot must have no module masses (its joints follow the '
                                               'sheet JointParts).'))
    for robot in apart.robots.values():
        if robot.type != TYPE_ONE:
            faults.append(Fault(on + 'Robots', robot.row, f'{robot.name} is of type {robot.type}; the robots taken '
                                                          f'apart are of type {TYPE_ONE} only.'))
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
    """The faults of robot type 1 taken apart: 01's checks of the parts file (18 to 20) and check_parts. (02's own and
    the register's are in all_faults.)"""
    base, apart = inputs.base, inputs.apart
    return (schemas.check_parts_taken_apart(apart, base.lists, params)
            + schemas.check_sibling_data(apart, params) + schemas.check_robot_types(apart, base.book.categories)
            + check_parts(inputs))


def grade_classes(inputs: ApartInputs) -> list:
    """The NdFeB grade classes a heat group can draw (sheet MagnetGrades), in the order of the heat they stand."""
    drawn = {g.klass for g in inputs.apart.grades if (g.probability or 0) > 0}
    return [k for k in schemas.MAGNET_CLASSES if k in drawn]


def group_classes(apart, group: str) -> list:
    """A heat group's grade classes and their probabilities, in the order of the heat they stand."""
    order = list(schemas.MAGNET_CLASSES)
    return sorted(((g.klass, g.probability) for g in apart.grades if g.group == group),
                  key=lambda c: order.index(c[0]))


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
    """Robot type 1 taken apart, drawn N times."""

    n: int
    robots: list          # the robots' names, in the order of the sheet Robots
    robot: np.ndarray     # the robot taken apart whose parts each draw takes, as its place in `robots`
    own: np.ndarray       # kg: that robot's own mass in each draw
    varied: np.ndarray    # kg: the mass of each draw's robot of the register
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
    register: list = None          # the register's robots drawn, '<number> <name>', in their order
    register_robot: np.ndarray = None   # the robot of the register of each draw, as its place in `register`


class Shared:
    """What is drawn once in each of the N draws and shared by every robot: the joint's components, the shares, the
    constants for all robots, the recipes, the sibling projects' metals and elements, the cells' energy per kg."""

    def __init__(self, inputs: ApartInputs, params: Params, magnets: dict, rng: np.random.Generator, n: int):
        apart = inputs.apart
        self.magnets = {k: (names, drawn) for k, (names, drawn) in magnets.items()}
        # The joint's components, kg, for each size: the small one's grams times its spread, the large one's grams
        # times its factor; and the joint at its modes, which the X1's and N1's module masses are measured against.
        self.joint: dict = {'small': {}, 'large': {}}
        self.at_mode = {'small': 0.0, 'large': 0.0}
        for c in apart.joint_parts:
            self.joint['small'][c.name] = c.grams / 1000 * triangle(rng, *c.spread, n)
            self.joint['large'][c.name] = c.grams / 1000 * triangle(rng, *c.factor, n)
            self.at_mode['small'] += c.grams / 1000 * c.spread[1]
            self.at_mode['large'] += c.grams / 1000 * c.factor[1]
        self.material = {c.name: c.material for c in apart.joint_parts}
        # The structure's components' shares of the structure, for each size: the G1's grams at their modes.
        structure = [c for c in apart.joint_parts if c.name in STRUCTURE]
        self.structure_share = {}
        for size, multiplier in (('small', lambda c: c.spread[1]), ('large', lambda c: c.factor[1])):
            total = sum(c.grams * multiplier(c) for c in structure)
            self.structure_share[size] = {c.name: c.grams * multiplier(c) / total for c in structure}
        # The shares of every component or part that has them: name -> [(material, share in each draw)].
        groups: dict = {}
        for s in apart.shares:
            groups.setdefault(s.item, []).append((s.material, s.share, s.remainder))
        self.shares = {item: shares_drawn(rng, group, n) for item, group in groups.items()}
        # The constants for all robots.
        self.constant = {q: triangle(rng, *values, n) for q, (_, values, _, _) in
                         apart.constants.get(schemas.ALL_ROBOTS, {}).items()}
        # The board metals per cm2 by car board category, the tantalum per kg of board, the sensor elements per unit.
        self.pcb = {(category, element): triangle(rng, *inputs.pcb[category][element], n)
                    for category in sorted({b.category for b in apart.boards})
                    for element in schemas.BOARD_METALS}
        self.tantalum = triangle(rng, *inputs.tantalum, n)
        self.sensor = {(car_type, element): triangle(rng, *values, n)
                       for car_type in sorted({e[2] for e in apart.elements})
                       for element, values in inputs.sensor_types[car_type].items()}
        # The recipes: type 1's aluminium and plastics; the NMC cells with their energy per kg drawn.
        settings = params.composition
        self.wh_per_kg = triangle(rng, settings.nmc_wh_per_kg_min, settings.nmc_wh_per_kg_mode,
                                  settings.nmc_wh_per_kg_max, n)
        recipes = RecipeDraws(inputs.base.recipes, rng, n)
        rows = {(r.robot, r.family, r.shared): r.recipe for r in inputs.base.recipes.rows or []}
        self.recipe = {shared: recipes.elements(rows[(TYPE_ONE, family, shared)])
                       for shared, family in RECIPE_FAMILY.items()}
        self.recipe[COPPER] = {'Cu': np.ones(n)}
        self.cells = recipes.elements(CELL_RECIPE, self.wh_per_kg / settings.nmc_wh_per_kg_mode)
        # The magnets by heat (sheet MagnetGrades): one draw of heat, from 0 to 1, decides how hot the robot is built
        # for; each heat group takes the grade class at that point of its cumulative probabilities (the classes tied
        # within a draw, so that the hot cases do not average out), and its magnets the element fractions of that class
        # in that draw (a discrete state, never blended).
        self.heat = rng.random(n)
        self.grade, self.magnet = {}, {}
        for group in dict.fromkeys(g.group for g in apart.grades):
            classes = group_classes(apart, group)
            at = np.minimum(np.searchsorted(np.cumsum([p for _, p in classes]), self.heat, side='right'),
                            len(classes) - 1)
            self.grade[group] = np.array([k for k, _ in classes])[at]
            names = magnets[classes[0][0]][0]
            fractions = np.zeros((n, len(names)))
            for k, (klass, _) in enumerate(classes):
                if magnets[klass][0] != names:
                    raise ValueError(f'the magnets of {klass} name other elements than those of {classes[0][0]}.')
                fractions[at == k] = magnets[klass][1][at == k]
            self.magnet[group] = (names, fractions)
        # The driver board of each joint size: its area (cm2) in the base robot (the G1): the small joint's from its
        # row of the sheet Boards, the large joint's the small one's times the same factor as its mass.
        base = base_robot(apart)
        small = next(b for b in apart.boards if b.robot == base and b.kind in IN_THE_JOINTS and None not in b.bounds)
        board = next(c for c in apart.joint_parts if c.name == DRIVER_BOARD)
        self.board_area = {'small': triangle(rng, *small.bounds, n)}
        self.board_area['large'] = self.board_area['small'] * self.joint['large'][DRIVER_BOARD] / (board.grams / 1000)


class Robot:
    """One robot's draws (its rows of the N draws), added up as they are drawn."""

    def __init__(self, name: str, rows: np.ndarray, shared: Shared, f: np.ndarray):
        self.name, self.rows, self.shared, self.f = name, rows, shared, f
        self.n = rows.size
        self.parts: dict = {}       # part column -> kg
        self.materials: dict = {}   # (kind, material) -> kg
        self.elements: dict = {}    # (kind, element) -> kg
        self.estimated: dict = {}   # (kind, element) -> kg resting on masses labelled E
        self.structures: dict = {}  # '<robot>: <joint> structure' -> kg of one joint's structure
        self.followed: dict = {}    # material -> kg of its elements drawn

    def of(self, values: np.ndarray) -> np.ndarray:
        """This robot's rows of draws shared by all robots."""
        return values[self.rows]

    def element(self, kind: str, element: str, kg: np.ndarray, estimate: bool, material: str) -> None:
        """kg of one element in a kind of part, held by `material` (02's "in the elements" of that material)."""
        self.elements[(kind, element)] = self.elements.get((kind, element), 0) + kg
        self.followed[material] = self.followed.get(material, 0) + kg
        if estimate and element in TRACKED:
            self.estimated[(kind, element)] = self.estimated.get((kind, element), 0) + kg

    def material(self, part: str, kind: str, material: str, kg: np.ndarray, estimate: bool,
                 heat_group: str = '') -> None:
        """kg of one material of a part in a kind, and the elements it holds: by its recipe, as copper, or as magnets
        of the grade class drawn for `heat_group`. Electronics are added by board() and sensor(); steel, titanium and
        mixed parts have none."""
        self.parts[part] = self.parts.get(part, 0) + kg
        self.materials[(kind, material)] = self.materials.get((kind, material), 0) + kg
        if material == MAGNETS:
            names, drawn = self.shared.magnet[heat_group]
            for k, element in enumerate(names):
                self.element(kind, element, kg * self.of(drawn[:, k]), estimate, material)
        elif material in self.shared.recipe:
            for element, share in self.shared.recipe[material].items():
                self.element(kind, element, kg * self.of(share), estimate, material)

    def piece(self, part: str, kind: str, item: str, material: str, kg: np.ndarray, estimate: bool,
              heat_group: str = '') -> None:
        """A part or component of one material, or of the shares of the sheet Shares."""
        if material:
            self.material(part, kind, material, kg, estimate, heat_group)
        else:
            for shared, share in self.shared.shares[item]:
                self.material(part, kind, shared, kg * self.of(share), estimate, heat_group)

    def board(self, kind: str, category: str, kg: np.ndarray, area: np.ndarray, estimate: bool) -> None:
        """The elements of boards of `kg` and `area` (cm2): copper their mass times the copper share, the metals of
        BOARD_METALS their area times the car category's mg per cm2, tantalum their mass times its share."""
        s = self.shared
        self.element(kind, 'Cu', kg * self.of(s.constant[BOARD_COPPER]), estimate, ELECTRONICS)
        for metal in schemas.BOARD_METALS:
            self.element(kind, metal, area * self.of(s.pcb[(category, metal)]) / 1e6, estimate, ELECTRONICS)
        self.element(kind, 'Ta', kg * self.of(s.tantalum), estimate, ELECTRONICS)

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
    "Do it for all the robots which are in type 1"); its mass a triangle on its register mass; its parts those of the
    robot taken apart that it is, else those of one of the robots taken apart, each as often; the joints, frame,
    shell and battery scaled by its mass over that robot's own, the electronics and sensors not."""
    apart, n = inputs.apart, params.composition.draws
    rng = np.random.default_rng([params.composition.seed, TYPE_ONE])
    names = list(apart.robots)                                    # the robots taken apart
    robots = inputs.robots
    which = rng.integers(len(robots), size=n)                     # each robot of the register as often
    itself = np.array([names.index(r.taken_apart) if r.taken_apart else -1 for r in robots])[which]
    template = np.where(itself >= 0, itself, rng.integers(len(names), size=n))
    low, mode, high = (np.array([r.mass[k] for r in robots])[which] for k in range(3))
    shared = Shared(inputs, params, magnets, rng, n)
    own, varied = np.zeros(n), np.zeros(n)
    done = []
    for k, name in enumerate(names):
        rows = np.flatnonzero(template == k)
        constants = apart.constants[name]
        own_kg = triangle(rng, *constants[ROBOT_MASS][1], rows.size)   # the robot taken apart, as the parts file has it
        robot_kg = np.where(itself[rows] == k, own_kg, triangles(rng, low[rows], mode[rows], high[rows]))
        own[rows], varied[rows] = own_kg, robot_kg
        r = Robot(name, rows, shared, robot_kg / own_kg)
        draw_robot(r, inputs, constants, rng)
        frame = next(p for p in apart.parts if p.robot == name and p.computed.startswith(FRAME))
        rest = robot_kg - sum(r.parts.values())
        r.piece(f'{name}: {frame.name}', KIND_OF[frame.kind], frame.name, frame.material, rest,
                frame.label.startswith('E'))
        done.append(r)
    d = assemble(n, names, template, own, varied, done, apart, shared)
    d.register, d.register_robot = [f'{r.number} {r.name}' for r in robots], which
    return d


def draw_robot(r: Robot, inputs: ApartInputs, constants: dict, rng: np.random.Generator) -> None:
    """Every part of one robot but its frame: its joints with all inside them, its parts, boards and sensors."""
    apart, s, n, name = inputs.apart, r.shared, r.n, r.name
    label = {p.name: p.label for p in apart.parts if p.robot == name}
    joints = [j for j in apart.joints if j.robot == name]
    in_robot = sum(j.count for j in joints)

    # The joints, joint kind by joint kind: the components of the G1's joint of their size, times the X1's or N1's
    # module mass over the G1 joint's at its modes, the structure their remainder; times the joints of the kind and the
    # mass factor (joints whole).
    drivers = {('small' if 'small' in b.name else 'large'): b for b in apart.boards
               if b.robot == name and b.kind in IN_THE_JOINTS}
    encoders = [p for p in apart.sensors if p.robot == name and p.kind in IN_THE_JOINTS]
    for j in joints:
        kind = JOINT_KIND[j.name.split()[0].lower()]
        estimate = label.get(f'Joint module, {j.module}', 'E').startswith('E')
        stated = None if None in j.module_mass else triangle(rng, *j.module_mass, n)
        scale = np.ones(n) if stated is None else stated / s.at_mode[j.module]
        one = {component: r.of(kg) * scale for component, kg in s.joint[j.module].items()}   # one joint, kg
        if stated is not None:
            rest = stated - sum(kg for component, kg in one.items() if component not in STRUCTURE)
            one.update({component: rest * share for component, share in s.structure_share[j.module].items()})
            r.structures[f'{name}: {j.name} structure'] = rest
        times = j.count * r.f
        part = f'{name}: {j.name} ({j.count} joints)'
        for component, kg_one in one.items():
            kg_here = kg_one * times
            material = s.material[component]
            if component == DRIVER_BOARD:
                r.material(part, kind, ELECTRONICS, kg_here, estimate)
                area = r.of(s.board_area[j.module]) * scale * times
                r.board(kind, drivers[j.module].category, kg_here, area, estimate)
            else:
                r.piece(part, kind, component, material, kg_here, estimate, j.heat_group)
        for e in encoders:   # their elements only: their mass is inside the joint's components
            units = [(t, u) for _, sensor, t, u in apart.elements if sensor == e.name]
            r.sensor(kind, units, e.count / in_robot * j.count * r.f, e.label.startswith('E'))

    # The parts: of one material or of shares, the battery pack as cells and housing, the cables from their length;
    # those of SCALED_KINDS times the mass factor. The frame is added last, by draw().
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
        kg = p.count * triangle(rng, *p.bounds, n) * (r.f if p.kind in SCALED_KINDS else 1)
        r.piece(column, kind, p.name, p.material, kg, estimate)

    # The boards outside the joints: their area, their mass from it, their elements.
    for b in apart.boards:
        if b.robot != name or b.kind in IN_THE_JOINTS:
            continue
        area = b.count * triangle(rng, *b.bounds, n)
        kg = area * r.of(s.constant[BOARD_G_PER_CM2]) / 1000
        r.material(f'{name}: {b.name}', KIND_OF[b.kind], ELECTRONICS, kg, b.label.startswith('E'))
        r.board(KIND_OF[b.kind], b.category, kg, area, b.label.startswith('E'))

    # The sensors outside the joints: their mass (g), their car sensor elements.
    for e in apart.sensors:
        if e.robot != name or e.kind in IN_THE_JOINTS:
            continue
        kg = e.count * triangle(rng, *e.bounds, n) / 1000
        r.material(f'{name}: {e.name}', KIND_OF[e.kind], ELECTRONICS, kg, e.label.startswith('E'))
        units = [(t, u) for _, sensor, t, u in apart.elements if sensor == e.name]
        r.sensor(KIND_OF[e.kind], units, e.count, e.label.startswith('E'))

    # The battery: the pack (times the mass factor), its cells from its energy (times the mass factor too), its
    # housing the pack less its cells and its management board (the boards of the kind Battery pack).
    pack = next((p for p in apart.parts if p.robot == name and p.computed.startswith(PACK)), None)
    if pack is not None:
        pack_kg = pack.count * triangle(rng, *pack.bounds, n) * r.f
        wh = triangle(rng, *constants[VOLTAGE][1], n) * triangle(rng, *constants[CAPACITY][1], n) * r.f
        cells_kg = wh / r.of(s.wh_per_kg)
        cells = next(p for p in apart.parts if p.robot == name and p.computed.startswith(CELLS))
        column = f'{name}: {cells.name}'
        r.parts[column] = cells_kg
        r.materials[('battery', CELL_MATERIAL)] = r.materials.get(('battery', CELL_MATERIAL), 0) + cells_kg
        for element, share in s.cells.items():
            r.element('battery', element, cells_kg * r.of(share), cells.label.startswith('E'), CELL_MATERIAL)
        managed = sum((r.parts[f'{name}: {b.name}'] for b in apart.boards
                       if b.robot == name and b.kind == 'Battery pack'), np.zeros(n))
        housing = next(p for p in apart.parts if p.robot == name and p.computed.startswith(HOUSING))
        r.piece(f'{name}: {housing.name}', 'battery', housing.name, housing.material, pack_kg - cells_kg - managed,
                housing.label.startswith('E'))


def assemble(n: int, names: list, robot: np.ndarray, own: np.ndarray, varied: np.ndarray, done: list,
             apart, shared: Shared) -> Draws:
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
    hot = {}
    for j in apart.joints:
        kind = JOINT_KIND[j.name.split()[0].lower()]
        hot_share = sum(p for klass, p in group_classes(apart, j.heat_group) if klass in HOT_CLASSES)
        hot[kind] = hot.get(kind, False) or hot_share > 0.5
    followed = {m: sum((put(m, r.followed, r) for r in done if m in r.followed), np.zeros(n))
                for m in {m for r in done for m in r.followed}}
    return Draws(n, names, robot, own, varied, (part_columns, parts), remainders, structures,
                 (material_keys, materials), elements, estimated, hot, shared.heat, shared.grade, followed)


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
    """Robot type 1 taken apart, at every level, and its summary, into `folder`, for 04 (WHAT IT WRITES in the
    docstring at the top)."""
    os.makedirs(folder, exist_ok=True)
    names = ', '.join(f'{k} {name}' for k, name in enumerate(d.robots))
    element_keys = [(kind, e) for kind in KINDS for e in element_order({e for k, e in d.elements if k == kind})]
    tables = {
        'robots': ([f'Robot taken apart ({names})', 'Own mass (kg)', 'Mass (kg)', 'Robot of the register'],
                   np.column_stack([d.robot, d.own, d.varied, d.register_robot])),
        'parts': d.parts,
        'materials': ([f'{KINDS[k][0]}: {m}' for k, m in d.materials[0]], d.materials[1]),
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
    rows = [['Robot mass', 'All kinds', *statistics(d.varied)]]
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
# the columns of every other robot type (03 compares them): whole kinds, not part by part.
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
              'total': (['Total'], d.varied[:, None])}
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
                 'Sn': 'Tin', 'Pb': 'Lead'}


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
TYPE_ONE_NOTE_WIDTH = 120                       # characters in a line of the notes page
# The elements of robot type 1's other materials (boards, sensors, magnets) in plain words, beside those of the recipes.
ELEMENT_NAMES.update({'Ag': 'Silver', 'As': 'Arsenic', 'Au': 'Gold', 'Dy': 'Dysprosium', 'Ga': 'Gallium',
                      'In': 'Indium', 'Nb': 'Niobium', 'Nd': 'Neodymium', 'Pd': 'Palladium', 'Pr': 'Praseodymium',
                      'Ta': 'Tantalum', 'Tb': 'Terbium', 'W': 'Tungsten'})


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


def element_panel(axes, kg: np.ndarray, symbol: str, first_in_row: bool) -> None:
    """One element in one robot over the draws: its histogram (the height the share of the draws), the median a solid
    line and the mean a dotted one, both written above the panel, right (Matthias, 2026-10-28: "Use the median or show
    boths"), the 2.5th and 97.5th percentile dashed; its own scale and unit."""
    per, unit = panel_unit(kg)
    values = kg / per
    axes.set_title(element_label(symbol), fontsize=TYPE_ONE_TITLE, fontweight='bold', loc='left')
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
    axes.set_title(f'median {panel_number(median)}\u00a0{unit}\nmean {panel_number(mean)}\u00a0{unit}', loc='right',
                   fontsize=TYPE_ONE_TEXT, color=TYPE_ONE_INK)
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
    taken = ', '.join(d.robots[:-1]) + ' or ' + d.robots[-1]
    notes = [
        'The bars: the draws of one element in one robot, the height the share of the draws. Solid line: the median; '
        'dotted line: the mean; both written above the panel, right. Dashed lines: the 2.5th and 97.5th percentile '
        '(95 % of the draws between them). Each panel on its own scale and unit (kg, g, mg).',
        f"The draws: {d.n:,}, each one robot of the register's sheet Type 1, each of its {len(d.register)} robots "
        'drawn equally often; its mass a triangle on its stated mass ± 1 kg or its stated range; its parts those of '
        'the robot taken apart that it is, else '
        f'those of the {taken} (each as often), the joints, frame, shell and battery scaled to its mass, the '
        'electronics and sensors not.',
        'The robots drawn: ' + '; '.join(d.register) + '.',
        'Not drawn: ' + ('; '.join(f'{r.number} {r.name} (no mass stated)' for r in left_out) or 'none') +
        '. A robot lighter than 15 kg is not of robot type 1.',
        'Not yet in the elements: ' + (', '.join(missing) or 'none') + '; their iron, chromium, nickel and the '
        'other elements of those materials are missing from the pages.' +
        (f" In part: {', '.join(partly)} (only the metals of the boards and the elements of the sensors)."
         if partly else ''),
        not_shown_note(params),
    ]
    return [note for note in notes if note]


def type_one_pages(c: Composition, d: Draws, left_out: list, params: Params) -> list:
    """Robot type 1's pages, as (file name, figure): the notes page, then the elements nine a page, each element it
    holds but those not shown (`composition.elements_not_shown`)."""
    names = shown_elements(c.tables['elements'][0], params)
    held = [e for e in names if c.column('elements', e).any()]
    per_page = TYPE_ONE_ACROSS * TYPE_ONE_DOWN
    pages = [held[k:k + per_page] for k in range(0, len(held), per_page)]
    out = []
    figure = plt.figure(figsize=TYPE_ONE_PAGE)
    figure.text(0.04, 0.93, f'Robot type 1, {c.title}: how to read its element pages', fontsize=TYPE_ONE_HEADING,
                va='top')
    text = '\n\n'.join(textwrap.fill(p, TYPE_ONE_NOTE_WIDTH) for p in type_one_notes(c, d, left_out, params))
    figure.text(0.04, 0.83, text, fontsize=TYPE_ONE_TEXT, va='top', color=TYPE_ONE_INK, linespacing=1.3)
    out.append((f'{c.name}_notes.png', figure))
    for p, page in enumerate(pages, 1):
        figure, axes = plt.subplots(TYPE_ONE_DOWN, TYPE_ONE_ACROSS, figsize=TYPE_ONE_PAGE, squeeze=False)
        for k, symbol in enumerate(page):
            element_panel(axes[k // TYPE_ONE_ACROSS, k % TYPE_ONE_ACROSS], c.column('elements', symbol), symbol,
                          k % TYPE_ONE_ACROSS == 0)
        for spare in axes.flatten()[len(page):]:
            spare.axis('off')
        figure.suptitle(f'Robot type 1, all its {len(d.register)} robots: each element in one robot ({p} of '
                        f'{len(pages)})', fontsize=TYPE_ONE_HEADING, y=0.985)
        figure.tight_layout(rect=(0, 0, 1, 0.955), h_pad=0.4, w_pad=2.5)
        out.append((f'{c.name}_elements_{p}.png', figure))
    return out


def draw_type_one_pages(c: Composition, d: Draws, left_out: list, folder: str, params: Params) -> list:
    """Robot type 1's pages into `folder`; returns their file names."""
    os.makedirs(folder, exist_ok=True)
    written = []
    for name, figure in type_one_pages(c, d, left_out, params):
        figure.savefig(os.path.join(folder, name), dpi=params.output.dpi, facecolor='white')
        plt.close(figure)
        written.append(name)
    return written


def run(params: Params) -> int:
    """Reads and checks the inputs, draws every robot type, checks every draw, and only then writes. 0 when it has
    written, 1 when a fault stopped it (nothing written)."""
    try:
        inputs = read_inputs(params)
        register = schemas.read_register(absolute(params.data.register))
        # Robot type 1's robots: those of the register's sheet Type 1, checked below against its sheet Robots. Type 1 is
        # drawn from the robots taken apart where its robots include one.
        type_one = schemas.read_type_sheet(absolute(params.data.register), TYPE_ONE)
        apart = read_apart_inputs(params, inputs, type_one) if any(r.taken_apart for r in type_one) else None
    except schemas.WorkbookError as error:
        print(error, file=sys.stderr)
        return 1
    faults = (all_faults(inputs, params)
              + schemas.check_register(register, params, list(apart.apart.robots) if apart else [])
              + schemas.check_type_one(register, type_one, params))
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
    for c in drawn:
        write(c, os.path.join(out, c.name))
        if taken is not None and c.number == TYPE_ONE:
            draw_type_one_pages(c, taken, apart.left_out, pages, params)
        else:
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
        print(f'  Robot type 1 taken apart written into {params.output.parts_dir}/ for 04.')
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
