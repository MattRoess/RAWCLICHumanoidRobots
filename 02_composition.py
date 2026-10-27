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

And one page per robot type into `output.composition_figures_dir`/<n>_<name>.png (`figures/composition/`; not in
git): its kg by material and its kg by element, each bar the mean with a line over 95 % of the draws (point 14).

Where it sits: after 01_schemas.py. 03_comparison.py reads what it writes.
"""

from __future__ import annotations

import csv
import importlib.util
import os
import sys
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
    """The check 02 adds to 01's. An item that follows the energy (E1.7i) is its mode times a cell's energy per kg over
    the mode of the NMC cells, so it can sit only in the recipe of NMC cells, used as the recipe of cells: by NMC cells
    of the sheet Cells, or named by a kept battery row; never named in the sheet Rows, nor held within another recipe,
    where there is no cell to take the energy from."""
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
        elif np.allclose(followed, kg, rtol=SUM_TOLERANCE, atol=0):
            status = 'Yes'
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


def page_notes(c: Composition) -> list:
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
                 f'{", ".join(missing) or "none"}; their kilograms are in the materials only.')
    notes.append('–: none in this robot type.')
    return notes


def draw_page(c: Composition, draws: int, path: str, params: Params) -> None:
    """Point 14: the page of one robot type, its kg by material and its kg by element, each with its 95 % interval."""
    materials = [(name, c.column('materials', name)) for name in c.tables['materials'][0]]
    elements = [(element_label(name), c.column('elements', name)) for name in c.tables['elements'][0]]
    notes = [line for note in page_notes(c) for line in schemas.wrap('• ' + note, 200)]
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


def run(params: Params) -> int:
    """Reads and checks the inputs, draws every robot type, checks every draw, and only then writes. 0 when it has
    written, 1 when a fault stopped it (nothing written)."""
    try:
        inputs = read_inputs(params)
    except schemas.WorkbookError as error:
        print(error, file=sys.stderr)
        return 1
    faults = all_faults(inputs, params)
    if faults:
        print(f'{len(faults)} fault(s) in the inputs; nothing is drawn. 01_schemas.py shows them on faults.png.',
              file=sys.stderr)
        for fault in faults:
            print(f"  sheet '{fault.sheet}', row {fault.row}: {fault.text}", file=sys.stderr)
        return 1

    drawn = [compose(category, inputs, params) for category in inputs.book.categories]
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
        draw_page(c, params.composition.draws, os.path.join(pages, c.name + '.png'), params)
        rows = {r['Name']: r for r in summary(c) if r['Kind'] == 'Material'}
        stats = statistics_of(c.column('total', 'Total'))
        missing = [name for name, r in rows.items()
                   if r['In the elements'] in ('No', 'Partly') and name != NOT_ALLOCATED]
        print(f"  {c.number} {c.title}: {stats['Mean (kg)']:.1f} kg at the mean (95 %: {stats['2.5 % (kg)']:.1f} to "
              f"{stats['97.5 % (kg)']:.1f}); Not allocated below zero in "
              f"{rows[NOT_ALLOCATED]['Draws below zero (%)']:.1f} % of the draws; not yet in the elements: "
              f"{', '.join(missing) or 'none'}.")
    print(f'Written into {params.output.composition_dir}/, one folder per robot type, and a page per robot type '
          f'into {params.output.composition_figures_dir}/.')
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
