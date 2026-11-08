"""
03_comparison.py
================

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

The six robot types side by side, one item a page: the mass of one robot, each material, each element of interest,
the part groups, the body regions and copper, each type's draws in a panel of its own, split into what contributes to
them, in the form of 02's pages. Press Run. No arguments; every setting is in `src/params_schema.py`. Run
`02_composition.py` first.

Matthias, 2026-10-26: "I want that it is possible to compare on a material level between the 6 types of roboy", and on
the level of the parts, understandable "as 20 year old, not familiar with the topic"; 2026-11-04: "The figures should
look similar or the same as in 02", "I want how the different contributions to the overall is", "Yes, agree E29" and
"Yes, build 03" (documentation/claude/EVIDENCE.md E29: the form and the pages, questions 1 to 4 as recommended).

WHAT IT READS
-------------
The draws 02 wrote, as they are: it draws nothing at random itself. For each robot type,
`output.composition_dir`/<n>_<name>/ (`data/consolidated/`): total, materials, elements (of interest), part_groups,
body_regions and copper (02's TABLES); and `output.parts_dir`/<n>_<name>/ (`data/parts_taken_apart/`): materials (each
material in each kind of part, '<kind>: <material>') and by_material (each element of interest by the material it
comes from, '<element>: <material>', and the copper fixed in alloys, '<element>: <material> (fixed in alloys)'). Each is
<table>.npy with its columns in <table>.txt. The names of the robot types come from the workbook, through 01's
`read_workbook`. The register (`data.register`, 01's `read_register`), for the outliers of the setting
`composition.outliers`, not drawn by 02, which the notes page names (the Neo1: Matthias, 2026-11-04, "Mark it as
outlier"; EVIDENCE.md E30 point 4); and 02's register.txt of each type (the robots of the register drawn).

WHAT IT CHECKS
--------------
That the draws belong together (`problems`), before anything is drawn: every table of every robot type there, with
the same number of draws, as many columns as its list names, 02's tables with the columns of the first robot type; in
every draw its materials, part groups and body regions adding up to its total; its materials by kind of part to its
materials; its elements by material to its elements; its copper fixed in each alloy to its copper fixed in alloys, and
its copper recycled as copper and fixed in alloys to its inflow. All to the rounding of float32 (FLOAT32_TOLERANCE).
And that no type's draws hold a robot set as an outlier (`outliers_in_draws`, its register.txt; Matthias, 2026-11-05,
"Yes, all ten"): such draws are older than the setting. Any problem stops it: nothing is drawn.

WHAT IT DRAWS
-------------
Into `output.comparison_dir` (`figures/comparison/`; not in git), pages of 16 × 9 inches, text 14 points and up, as
02's: the notes once, on pages of their own (comparison_notes_<k>.png), then one item a page, its six robot types in
six panels, three across and two down:

  comparison_total_1.png             the mass of one robot, split by material
  comparison_materials_<k>.png       each material any type holds, split by the kind of part it sits in
  comparison_elements_<k>.png        each element of interest any type holds, split by the material it comes from, in
                                     alphabetical order of their names (1 Aluminium … 22 Titanium)
  comparison_part_groups_1.png       the mass of one robot, split by part group
  comparison_body_regions_1.png      the mass of one robot, split by body region
  comparison_copper_1.png            copper's inflow, split into recycled as copper and fixed in alloys

Each panel 02's (`stacked_bars`, `centre_lines`, `panel_axes`): the histogram of the type's draws, the height the share
of the draws, each bar split into its contributions, the smaller lower, each in its colour; the median a solid line,
the mean a dotted one, the 2.5th and 97.5th percentile dashed, the numbers on the page after its page (02's E34); each
panel on its own scale and unit (question 3); a panel whose draws spread over orders of magnitude, its median in the
first 5 % of its axis, on a logarithmic mass axis (02's LOG_BELOW, E36). A type that holds the item in fewer than 2.5 % of its draws has no panel
(02's rule; a 0 is not part of a distribution, CLAUDE.md §7): its place says so. One legend at the top of a page. A
numbered page of an earlier run beyond those drawn is removed by its exact name, and so are the four pages of 03's old
form (OLD_PAGES); nothing else in the folder is touched.

Where it sits: after 02_composition.py; 04_stock_and_flow.py comes after it and reads nothing of 03.
"""

from __future__ import annotations

import importlib.util
import math
import os
import sys
import textwrap
from dataclasses import dataclass

# Run from anywhere, and put the project root on the path, so that `src` imports. Must come before any import of src.
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import numpy as np  # noqa: E402
from matplotlib.patches import Patch  # noqa: E402

from src.params_schema import ParameterError, Params, absolute, current  # noqa: E402


def load_composition():
    """02_composition.py as a module, for the files it writes (TABLES, folder_name) and its pages' drawing
    (stacked_bars, centre_lines, notes_pages …: one copy of the code); it loads 01 as `schemas`. Loaded from its path,
    registered as 'composition', and only once: where the tests have loaded it already, that module is used."""
    path = os.path.join(HERE, '02_composition.py')
    loaded = sys.modules.get('composition')
    if loaded is not None and os.path.samefile(getattr(loaded, '__file__', path), path):
        return loaded
    spec = importlib.util.spec_from_file_location('composition', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules['composition'] = module
    spec.loader.exec_module(module)
    return module


composition = load_composition()
schemas = composition.schemas
plt = composition.plt

# ------------------------------------------------------------------------------------------------------
# What it reads and how it checks it
# ------------------------------------------------------------------------------------------------------

# The tables of each robot type part by part that 03 reads (02's APART_TABLES): each material by kind of part, each
# element by the material it comes from.
PARTS_TABLES = ('materials', 'by_material', 'taken_apart')   # taken_apart since 2026-11-08 ("Yes, add 1 to 3")
# The draws are written as float32, whose rounding is about 6e-8 of a value; a sum of a few dozen columns may miss its
# whole by some 1e-6 of it. A miss above this share of the whole means the files do not belong together.
FLOAT32_TOLERANCE = 1e-4
# Below this, a miss is no miss: a picogram, where an element is 0 kg in a draw and its parts add up to 0 kg.
FLOOR_KG = 1e-12


@dataclass
class Robot:
    """One robot type, as 02 wrote it."""

    number: int               # the robot type, 1 to 6
    title: str                # its name, e.g. 'Compact Research & Developer'
    tables: dict              # one of 02's TABLES -> (its columns, its draws as written: N rows × one column each)
    parts: dict               # one of PARTS_TABLES -> (its columns, its draws as written), of data/parts_taken_apart/

    def column(self, table: str, name: str) -> np.ndarray:
        """The draws of one column of one of 02's TABLES, in float64 for the sums and statistics."""
        columns, draws = self.tables[table]
        return draws[:, columns.index(name)].astype(np.float64)

    def split(self, table: str, head: str) -> dict:
        """The columns '<head>: <name>' of one of PARTS_TABLES, as {name: its draws in float64}, in the table's order:
        a material in each kind of part ('materials', head the kind), or an element from each material ('by_material',
        head the element; the copper fixed in an alloy '<material> (fixed in alloys)')."""
        columns, draws = self.parts[table]
        out = {}
        for k, column in enumerate(columns):
            first, _, rest = column.partition(': ')
            if first == head:
                out[rest] = draws[:, k].astype(np.float64)
        return out

    def taken(self, symbol: str, key) -> dict:
        """One element of interest in the parts of how a robot is taken apart (the parts table 'taken_apart',
        '<kind>: <part>: <element>'), added over the kinds, keyed by `key(part)` (the part itself, or its group), in
        the order of 01's parts: {key: its draws}."""
        columns, draws = self.parts['taken_apart']
        out = {}
        for part in schemas.TAKEN_PARTS:
            for k, column in enumerate(columns):
                kind, _, rest = column.partition(': ')
                if rest == f'{part}: {symbol}':
                    out[key(part)] = out.get(key(part), 0) + draws[:, k].astype(np.float64)
        return out

    def by_group(self, symbol: str) -> dict:
        """One element by the four groups of how a robot is taken apart, {group: its draws}, each the sum of its parts."""
        return self.taken(symbol, lambda part: schemas.TAKEN_GROUP[part])

    def by_part(self, symbol: str) -> dict:
        """One element by the parts of how a robot is taken apart, {part: its draws}, added over the kinds."""
        return self.taken(symbol, lambda part: part)

    def in_kinds(self, material: str) -> dict:
        """One material in each kind of part it sits in, {kind's name: its draws} (the parts table 'materials',
        '<kind>: <material>')."""
        columns, draws = self.parts['materials']
        return {column.rpartition(': ')[0]: draws[:, k].astype(np.float64) for k, column in enumerate(columns)
                if column.rpartition(': ')[2] == material}


def read_table(folder: str, table: str) -> tuple:
    """One table as 02 writes it: its columns (<table>.txt, one a line) and its draws (<table>.npy)."""
    with open(os.path.join(folder, f'{table}.txt'), encoding='utf-8') as file:
        columns = file.read().splitlines()
    return columns, np.load(os.path.join(folder, f'{table}.npy'))


def read_draws(params: Params) -> list:
    """The draws of every robot type of the workbook, as 02 wrote them. Raises FileNotFoundError where 02 has not
    written a table of a robot type."""
    book = schemas.read_workbook(absolute(params.data.workbook), params)
    robots = []
    for category in book.categories:
        name = composition.folder_name(category)
        consolidated = os.path.join(absolute(params.output.composition_dir), name)
        apart = os.path.join(absolute(params.output.parts_dir), name)
        robots.append(Robot(category.number, category.name,
                            {table: read_table(consolidated, table) for table in composition.TABLES},
                            {table: read_table(apart, table) for table in PARTS_TABLES}))
    return robots


def outliers_in_draws(params: Params, outliers: list) -> list:
    """Whether the draws on disk hold a robot set as an outlier (Matthias, 2026-11-05, "Yes, all ten", open item 5):
    02 draws no outlier (composition.outliers, E30), so draws that hold one are older than the setting, and the notes
    page would name as "not drawn" a robot they hold. A sentence for each, [] where none, from 02's register.txt of every
    robot type (the robots of the register drawn, '<number> <name>'). Raises FileNotFoundError where it is missing."""
    book = schemas.read_workbook(absolute(params.data.workbook), params)
    numbers = {r.number: r for r in outliers}
    found = []
    for category in book.categories:
        path = os.path.join(absolute(params.output.parts_dir), composition.folder_name(category), 'register.txt')
        with open(path, encoding='utf-8') as file:
            drawn = [line.split(' ', 1) for line in file.read().splitlines() if line.strip()]
        for number, name in drawn:
            if int(number) in numbers:
                found.append(f'robot type {category.number}: its draws hold {number} {name}, set as an outlier '
                             '(composition.outliers), which 02 does not draw: the draws are older than the setting.')
    return found


def misses(sum_of_parts: np.ndarray, whole: np.ndarray) -> int:
    """In how many draws the parts miss their whole by more than the rounding of float32."""
    return int((np.abs(sum_of_parts - whole) > FLOAT32_TOLERANCE * np.abs(whole) + FLOOR_KG).sum())


def problems(robots: list) -> list:
    """Whether the draws belong together (WHAT IT CHECKS in the docstring at the top): a sentence for each problem,
    [] where none."""
    found = []
    first = robots[0]
    n = len(first.tables['total'][1])
    for robot in robots:
        shapes_right = True
        for table, (columns, draws) in [*robot.tables.items(), *robot.parts.items()]:
            if draws.ndim != 2 or draws.shape[0] != n:
                found.append(f'robot type {robot.number}: {table} has {draws.shape[0]} draws, not {n}.')
                shapes_right = False
            elif draws.shape[1] != len(columns):
                found.append(f'robot type {robot.number}: {table} has {draws.shape[1]} columns, but its list names '
                             f'{len(columns)}.')
                shapes_right = False
        for table in composition.TABLES:
            if robot.tables[table][0] != first.tables[table][0]:
                found.append(f'robot type {robot.number}: the columns of {table} are not those of robot type '
                             f'{first.number}.')
                shapes_right = False
        if not shapes_right:
            continue
        total = robot.column('total', 'Total')
        for table, what in (('materials', 'the materials'), ('part_groups', 'the part groups'),
                            ('body_regions', 'the body regions')):
            off = misses(robot.tables[table][1].astype(np.float64).sum(axis=1), total)
            if off:
                found.append(f'robot type {robot.number}: {what} do not add up to the total in {off} draws.')
        off = [m for m in robot.tables['materials'][0]
               if misses(sum(robot.in_kinds(m).values(), np.zeros(n)), robot.column('materials', m))]
        if off:
            found.append(f'robot type {robot.number}: its materials by kind of part do not add up to its materials: '
                         f"{', '.join(off)}.")
        off = [e for e in robot.tables['elements'][0]
               if misses(sum(recovered_from(robot, e).values(), np.zeros(n)), robot.column('elements', e))]
        if off:
            found.append(f'robot type {robot.number}: its elements by material do not add up to its elements: '
                         f"{', '.join(off)}.")
        off = [e for e in robot.tables['elements'][0]
               if misses(sum(robot.by_part(e).values(), np.zeros(n)), robot.column('elements', e))]
        if off:
            found.append(f'robot type {robot.number}: its elements by part of how a robot is taken apart do not add up '
                         f"to its elements: {', '.join(off)}.")
        recycled, fixed, inflow = (robot.column('copper', c) for c in composition.COPPER_COLUMNS)
        in_alloys = sum((kg for symbol in robot.tables['elements'][0] for kg in fixed_in(robot, symbol).values()),
                        np.zeros(n))
        if (misses(in_alloys, fixed) or misses(recycled, robot.column('elements', 'Cu'))
                or misses(recycled + fixed, inflow)):
            found.append(f'robot type {robot.number}: its copper recycled as copper, fixed in alloys and its inflow '
                         'do not belong together.')
    return found


def recovered_from(robot: Robot, symbol: str) -> dict:
    """One element of interest by the material it is recovered from, {material: its draws}."""
    return {m: kg for m, kg in robot.split('by_material', symbol).items() if not m.endswith(composition.FIXED_MARK)}


def fixed_in(robot: Robot, symbol: str) -> dict:
    """One element fixed in alloys, by the alloy, {'<material> (fixed)': its draws}, as 02's element pages mark it."""
    mark = composition.FIXED_MARK
    return {f'{m[:-len(mark)]} (fixed)': kg for m, kg in robot.split('by_material', symbol).items()
            if m.endswith(mark)}


# ------------------------------------------------------------------------------------------------------
# The colours
# ------------------------------------------------------------------------------------------------------
# Paul Tol's discrete rainbow, as published (tol_colors.py, version 2022.10, https://sronpersonalpages.nl/~pault/, read
# on 2026-11-04): its 29 colours, and for a scheme of n colours (1 to 23) which of them, in this order. The kinds of
# part (01's KINDS) take their colours from it, and the materials, part groups and body regions of 03's pages each the
# scheme of their number. The element pages keep 02's colours of the materials an element comes from (Tol's muted
# scheme, MATERIAL_COLOURS), so that they look as 02's.
RAINBOW = ('#E8ECFB', '#D9CCE3', '#D1BBD7', '#CAACCB', '#BA8DB4', '#AE76A3', '#AA6F9E', '#994F88', '#882E72',
           '#1965B0', '#437DBF', '#5289C7', '#6195CF', '#7BAFDE', '#4EB265', '#90C987', '#CAE0AB', '#F7F056',
           '#F7CB45', '#F6C141', '#F4A736', '#F1932D', '#EE8026', '#E8601C', '#E65518', '#DC050C', '#A5170E',
           '#72190E', '#42150A')
RAINBOW_INDEXES = (
    (9,), (9, 25), (9, 17, 25), (9, 14, 17, 25), (9, 13, 14, 17, 25), (9, 13, 14, 16, 17, 25),
    (8, 9, 13, 14, 16, 17, 25), (8, 9, 13, 14, 16, 17, 22, 25), (8, 9, 13, 14, 16, 17, 22, 25, 27),
    (8, 9, 13, 14, 16, 17, 20, 23, 25, 27), (8, 9, 11, 13, 14, 16, 17, 20, 23, 25, 27),
    (2, 5, 8, 9, 11, 13, 14, 16, 17, 20, 23, 25), (2, 5, 8, 9, 11, 13, 14, 15, 16, 17, 20, 23, 25),
    (2, 5, 8, 9, 11, 13, 14, 15, 16, 17, 19, 21, 23, 25), (2, 5, 8, 9, 11, 13, 14, 15, 16, 17, 19, 21, 23, 25, 27),
    (2, 4, 6, 8, 9, 11, 13, 14, 15, 16, 17, 19, 21, 23, 25, 27),
    (2, 4, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 19, 21, 23, 25, 27),
    (2, 4, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 19, 21, 23, 25, 26, 27),
    (1, 3, 4, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 19, 21, 23, 25, 26, 27),
    (1, 3, 4, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 19, 21, 23, 25, 26, 27),
    (1, 3, 4, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 20, 22, 24, 25, 26, 27),
    (1, 3, 4, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 20, 22, 24, 25, 26, 27, 28),
    (0, 1, 3, 4, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 20, 22, 24, 25, 26, 27, 28))


def rainbow(names: list) -> dict:
    """Each of `names` its colour of Tol's discrete rainbow of as many colours, in their order."""
    if not 1 <= len(names) <= len(RAINBOW_INDEXES):
        raise ValueError(f'Paul Tol publishes his discrete rainbow for 1 to {len(RAINBOW_INDEXES)} colours, not '
                         f'{len(names)}.')
    return {name: RAINBOW[i] for name, i in zip(names, RAINBOW_INDEXES[len(names) - 1])}


# The kinds of part in 01's colours, by their names as 02 writes them ('Hip joints', …).
KIND_COLOURS = {name: colour for name, colour in schemas.KINDS.values()}
# Copper's inflow: the copper recycled as copper in 02's colour of copper, that fixed in alloys in its pale grey (E25).
RECYCLED = 'Copper recycled as copper'
COPPER_COLOURS = {RECYCLED: composition.MATERIAL_COLOURS[composition.COPPER],
                  composition.FIXED_PART: composition.MATERIAL_COLOURS[composition.FIXED_PART]}

# ------------------------------------------------------------------------------------------------------
# The pages
# ------------------------------------------------------------------------------------------------------

PREFIX = 'comparison'
# The numbered pages, one series each (comparison_<series>_<k>.png), in the order they are drawn.
SERIES = ('notes', 'total', 'materials', 'elements', 'groups', 'part_groups', 'body_regions', 'copper', 'numbers',
          'parts')
# The four pages of 03's old form (2026-10-26 to 2026-11-04: a bar of the mean and a line over 95 % per type), removed by
# their exact names where an earlier run left them (E29).
OLD_PAGES = ('materials.png', 'elements.png', 'part_groups.png', 'body_regions.png')
ACROSS, DOWN = 3, 2           # six panels a page, one per robot type
PANEL_TITLE_WIDTH = 34        # characters in a line of a panel's title, the type's number and name
# The legend of a page in as many rows as it needs: 02's legend_columns, LEGEND_ROW (one copy, since 2026-11-05).


def magnets_and_sensors(robots: list, symbol: str) -> bool:
    """Whether an element is shown on two pages, its magnets' and its sensors' (E38 point 5): the magnets and the sensors
    hold it in some robot type (02's magnets_split), and in no robot type does anything else hold it in at least 02's
    HELD_SHARE of the draws."""
    parts = [recovered_from(r, symbol) for r in robots]
    sensors = {composition.component_label(c) for c in (composition.CAMERAS, composition.OTHER_SENSORS)}
    others = any(composition.held(kg) for p in parts for m, kg in p.items()
                 if m != composition.MAGNETS and m not in sensors)
    return not others and any(composition.magnets_split(p) for p in parts)


def compare_page(heading: str, robots: list, parts_of, colours: dict, fixed_of=None, symbol: str = '',
                 legend: bool = True):
    """One page: each robot type a panel (three across, two down), the histogram of its draws of the item split into
    its contributions, `parts_of(robot)` ({contribution: its draws}), each in its colour of `colours`, as 02's panels;
    where `fixed_of` is given, the panel of 02's element pages (by_material_panel), the copper fixed in alloys
    (`fixed_of(robot)`, {'<alloy> (fixed)': its draws}) one pale grey part. A type holding the item in fewer than 2.5 %
    of its draws has no panel; its place says so. The first panel drawn in a row has the scale of the share of the
    draws, as the first of a row on 02's pages. One legend of the contributions drawn, at the top. The metal of a light
    alloy (`symbol` of 02's ALLOY_OF, E33): each panel the metal its alloys hold alone (02's alloy_split); a type without
    the alloy in 2.5 % of its draws its place naming the alloy (02's alloy_place). The place of a type without the item:
    02's not_drawn_words (one copy)."""
    figure, axes = plt.subplots(DOWN, ACROSS, figsize=composition.APART_PAGE, squeeze=False)
    panels, rows_labelled = [], set()
    for k, robot in enumerate(robots):
        here = axes[k // ACROSS, k % ACROSS]
        title = textwrap.fill(f'{robot.number} {robot.title}', PANEL_TITLE_WIDTH)
        parts = composition.alloy_split(symbol, parts_of(robot))
        fixed = fixed_of(robot) if fixed_of else {}
        total = sum([*parts.values(), *fixed.values()], np.zeros(len(robot.tables['total'][1])))
        if symbol in composition.ALLOY_OF and not composition.held(total):
            composition.alloy_place(here, symbol, parts, title)
            continue
        if not composition.held(total):
            here.axis('off')
            here.set_title(title, fontsize=composition.APART_TITLE, fontweight='bold', loc='left')
            here.text(0, 0.85, composition.not_drawn_words(total), transform=here.transAxes,
                      fontsize=composition.APART_TEXT, va='top', color=composition.APART_INK)
            continue
        first_in_row = k // ACROSS not in rows_labelled
        rows_labelled.add(k // ACROSS)
        if fixed_of:
            panels.append((here, composition.by_material_panel(here, {**parts, **fixed}, title, first_in_row,
                                                               tuple(fixed))))
            continue
        here.set_title(title, fontsize=composition.APART_TITLE, fontweight='bold', loc='left')
        bars = composition.stacked_bars(here, parts, colours)
        composition.centre_lines(here, bars.values, bars.held_in, bars.end, bars.unit, title)
        composition.panel_axes(here, bars.unit, first_in_row)
        panels.append((here, (bars.top, 0, bars.drawn)))
    for spare in axes.flatten()[len(robots):]:
        spare.axis('off')
    drawn = {m for _, (_, _, contributions) in panels for m in contributions}
    # No legend for a light alloy's metal (E33, relabelled) nor for the magnets' part of an element (E38 point 5, no
    # `legend`): one colour, its page's title naming what it is.
    shown = [m for m in colours if m in drawn] if legend and symbol not in composition.ALLOY_OF else []
    # On an element page (`symbol`) copper and nickel by what they are (02's element_page_name, E37); every page a
    # component of the electronics its component first, the electronics in brackets (02's shown_name, E38).
    names = {m: composition.element_page_name(m) if symbol else composition.shown_name(m) for m in shown}
    columns = composition.legend_columns(list(names.values())) if shown else 1
    rows = math.ceil(len(shown) / columns) if shown else 0
    figure.suptitle(heading, fontsize=composition.APART_HEADING, y=0.985)
    if shown:
        figure.legend(handles=[Patch(color=colours[m], label=names[m]) for m in shown], loc='upper center',
                      bbox_to_anchor=(0.5, 0.955), ncol=columns, frameon=False, fontsize=composition.APART_TEXT)
    figure.tight_layout(rect=(0, 0, 1, 0.95 - max(rows, 1) * composition.LEGEND_ROW), h_pad=0.4, w_pad=2.5)
    composition.make_room(figure, panels)
    return figure


def held_by_any(robots: list, table: str, name: str) -> bool:
    """Whether any robot type holds one column of 02's TABLES in at least 2.5 % of its draws (02's rule)."""
    return any(composition.held(r.column(table, name)) for r in robots)


def material_names(robots: list) -> list:
    """The materials of the pages: those of 02's materials table (the one list's) in 02's MATERIAL_ORDER, any other
    after them, Not allocated not (none, as each robot's frame takes the rest of its mass)."""
    columns = [m for m in robots[0].tables['materials'][0] if m != composition.NOT_ALLOCATED]
    order = list(composition.MATERIAL_ORDER)
    return sorted(columns, key=lambda m: (order.index(m) if m in order else len(order), m))


def notes(robots: list, outliers: list, params: Params) -> list:
    """The notes page's paragraphs, in plain words; `outliers` (01's outlier_robots) named, each with its robot types,
    in 02's words (EVIDENCE.md E30 point 4)."""
    n = len(robots[0].tables['total'][1])
    paragraphs = [
        'Each page one item, the six robot types side by side: the mass of one robot by material, each material by '
        'the kind of part it sits in, each element of interest by the material it comes from, the mass of one robot '
        'by part group and by body region, and copper, recycled as copper or fixed in alloys. One panel per robot type, '
        'in the form of the pages of each robot type (figures/composition/).',
        'A panel: the bars the draws of one robot of the type, the height the share of the draws, each bar split into '
        'the kg its draws hold in each contribution, the one with the smaller mean lower, each in its colour (one '
        'legend at the top of the page). Solid line: the median; dotted line: the mean. Dashed lines: the 2.5th and '
        '97.5th percentile (95 % of the draws between them). Each axis ends at the 99.5th percentile of its draws: the '
        "0.5 % beyond are not drawn. " + composition.LOG_WORDS + " Every panel's numbers (in what share of the draws "
        "it is held, its median, mean and "
        '95 %, the draws beyond its axis) are on the page after its page.',
        'Each panel on its own scale and unit (kg, g, mg): compare the numbers of the panels, not the widths of '
        'their bars. One scale shared by the six would be stretched by the type with the heaviest robots and press '
        'every other type into its first bars.',
        'A robot type that holds an item in some of its draws only (a robot or a version without it): its panel shows '
        'the draws that hold it and says in what share of all its draws it is held; one held in fewer than 2.5 % of '
        'its draws has no panel, and its place on the page says so (a 0 is not part of a distribution). An item no '
        'type holds has no page.',
        f'The draws: {n:,} for each robot type, as 02_composition.py wrote them (data/consolidated/ and '
        'data/parts_taken_apart/), each one robot of the type in the register, each of its robots drawn equally often '
        '(a robot in two versions, each as often), part by part from its parts file. 03 draws nothing at random; it '
        'checks that the draws add up before it draws a page.',
        composition.outlier_words(outliers, params, types=True),
        'The elements: only the elements of interest, from what is recovered as elements, as on the pages of each '
        'robot type: copper and nickel each its metal whole; the aluminium, magnesium and titanium alloys the metal '
        'they hold; the NdFeB magnets their rare earths, cobalt, boron, niobium and gallium; the battery cells their '
        'lithium, nickel, cobalt and manganese and the copper and aluminium of their foils and tabs; the boards and '
        'components their metals of interest. Copper: its inflow, the copper recycled as copper and, in pale grey, the '
        'copper fixed in alloys (brass, the aluminium and magnesium alloys, the steels, the magnets), which is not '
        'recovered as copper.',
        composition.LIGHT_ALLOY_NOTE,   # what the light alloys' panels leave out (E33)
        composition.MAGNETS_NOTE,   # the magnets' and the sensors' part of an element apart (E38 point 5)
        "The part groups and body regions: each robot type's kinds of part placed whole; rough where a kind holds parts "
        "of another group: the head's joints are counted as sensors, the battery management board as battery; a "
        "hydraulic robot's power unit, oil and hoses as joint drives, in the torso.",
        "The colours: Paul Tol's schemes, as published, colour-blind safe: the materials of the page of the mass by "
        'material, the part groups and the body regions each his discrete rainbow of their number; the kinds of part '
        'the colours of the pages of each robot type (the same rainbow); the materials an element comes from his muted '
        'scheme, as on the pages of each robot type.',
    ]
    return [p for p in paragraphs if p]   # no outlier: no paragraph


def pages(robots: list, params: Params, outliers: list = ()):
    """Every page, as (file name, figure), one at a time (each is saved and closed before the next is drawn); the
    `outliers` named on the notes page; each page of panels followed by the page of its numbers (02's numbers_page,
    E34), comparison_numbers_<k>.png; then the lists part by part, comparison_parts_<k>.png."""
    yield from composition.notes_pages(PREFIX, 'Comparing the six robot types: how to read the pages',
                                       notes(robots, list(outliers), params))
    for k, (name, figure) in enumerate(panel_pages(robots), 1):
        numbers = composition.numbers_page(f'{PREFIX}_numbers_{k}.png', figure)   # read before the page is closed
        yield name, figure
        yield numbers
    yield from parts_pages(robots)


def elements_shown(robots: list) -> list:
    """The elements of interest any robot type holds in at least 2.5 % of its draws, in alphabetical order of their
    names, as the element pages."""
    return sorted((e for e in robots[0].tables['elements'][0] if held_by_any(robots, 'elements', e)),
                  key=composition.element_label)


def parts_pages(robots: list):
    """For each element shown, the list of one robot of each robot type part by part of how a robot is taken apart
    (02's part_rows and part_list_pages, one copy): a row for each type and each part that holds it, 14 rows a page,
    comparison_parts_<k>.png counted on over the elements (Matthias, 2026-11-08: "I want a detailed list of the
    component ... to know how to take it apart!!!", "Yes, add 1 to 3")."""
    k = 0
    for symbol in elements_shown(robots):
        kg = {(f'{r.number} {r.title}', part): values for r in robots for part, values in r.by_part(symbol).items()}
        for _, page in composition.part_list_pages(
                'x', f'{composition.element_label(symbol)} in one robot of each robot type, part by part',
                composition.part_rows(kg), first_head='Robot type'):
            k += 1
            yield f'{PREFIX}_parts_{k}.png', page


def panel_pages(robots: list):
    """Every page of panels, as (file name, figure), one at a time: the total by material, each material by kind of
    part, each element by the material it comes from, the part groups, the body regions, copper three ways."""
    materials = material_names(robots)
    yield (f'{PREFIX}_total_1.png',
           compare_page('The mass of one robot of each robot type, by material', robots,
                        lambda r: {m: r.column('materials', m) for m in materials}, rainbow(materials)))
    shown = [m for m in materials if held_by_any(robots, 'materials', m)]
    for k, material in enumerate(shown, 1):
        yield (f'{PREFIX}_materials_{k}.png',
               compare_page(f'{material} in one robot of each robot type, by the kind of part it sits in', robots,
                            lambda r, m=material: r.in_kinds(m), KIND_COLOURS))
    # The elements in alphabetical order of their names, as each page's title begins ('Aluminium (Al)' … 'Titanium (Ti)';
    # Matthias, 2026-11-04: "Alphabtetic is easier to find", "Elements only"); the materials keep 02's order.
    elements = sorted((e for e in robots[0].tables['elements'][0]
                       if any(composition.held(r.column('elements', e) + sum(fixed_in(r, e).values(), 0))
                              for r in robots)), key=composition.element_label)
    k = 0
    for symbol in elements:
        # An element the magnets and the sensors hold alone (02's magnets_split, E38 point 5; Matthias, 2026-11-06:
        # "Gallium apart", "Yes do it like this. Nd etc. are then similar as Ga in elements in Magnets"): two pages,
        # the magnets' and the sensors', in place of the one by material.
        if magnets_and_sensors(robots, symbol):
            label = composition.element_label(symbol)
            k += 1
            yield (f'{PREFIX}_elements_{k}.png',
                   compare_page(f'{label} in the magnets of one robot of each robot type', robots,
                                lambda r, e=symbol: {m: kg for m, kg in recovered_from(r, e).items()
                                                     if m == composition.MAGNETS},
                                composition.MATERIAL_COLOURS, legend=False))
            k += 1
            yield (f'{PREFIX}_elements_{k}.png',
                   compare_page(f'{label} in the sensors of one robot of each robot type', robots,
                                lambda r, e=symbol: composition.sensors_split(e, recovered_from(r, e)),
                                composition.MATERIAL_COLOURS))
            continue
        inflow = ', inflow' if any(fixed_in(r, symbol) for r in robots) else ''
        # A light alloy's metal titled as what its panels draw, the metal its alloy holds (E33, "Yes, relabel").
        heading = (f'{composition.element_label(symbol)} held in the {composition.ALLOY_OF[symbol].lower()} of one '
                   'robot of each robot type' if symbol in composition.ALLOY_OF else
                   f'{composition.element_label(symbol)} in one robot of each robot type{inflow}, by the material it '
                   'comes from')
        k += 1
        yield (f'{PREFIX}_elements_{k}.png',
               compare_page(heading, robots, lambda r, e=symbol: recovered_from(r, e),
                            composition.MATERIAL_COLOURS, lambda r, e=symbol: fixed_in(r, e), symbol))
        # The titanium in the sensors beside its alloy, a page of its own, its cameras and other sensors (02's
        # SENSORS_OF; Matthias, 2026-11-05: "where the hell is titanium in the sensor", "Yes, add it").
        if symbol in composition.SENSORS_OF:
            k += 1
            yield (f'{PREFIX}_elements_{k}.png',
                   compare_page(f'{composition.element_label(symbol)} in the sensors of one robot of each robot type',
                                robots, lambda r, e=symbol: composition.sensors_split(e, recovered_from(r, e)),
                                composition.MATERIAL_COLOURS))
    # Each element by the four groups of how a robot is taken apart (Matthias, 2026-11-08: "Why I am not allowed to
    # know what the different components contribut already at this level", "Yes, add 1 to 3").
    for k, symbol in enumerate(elements_shown(robots), 1):
        yield (f'{PREFIX}_groups_{k}.png',
               compare_page(f'{composition.element_label(symbol)} in one robot of each robot type, by group', robots,
                            lambda r, e=symbol: r.by_group(e), schemas.GROUP_COLOURS))
    # The mass by part group (02's: the four groups, in their colours) and by body region.
    for table, words in (('part_groups', 'group'), ('body_regions', 'body region')):
        columns = robots[0].tables[table][0]
        colours = {**rainbow(columns), **{g: c for g, c in schemas.GROUP_COLOURS.items() if g in columns}}
        yield (f'{PREFIX}_{table}_1.png',
               compare_page(f'The mass of one robot of each robot type, by {words}', robots,
                            lambda r, t=table, c=columns: {name: r.column(t, name) for name in c}, colours))
    yield (f'{PREFIX}_copper_1.png',
           compare_page('Copper in one robot of each robot type: its inflow, recycled as copper or fixed in alloys',
                        robots, lambda r: {RECYCLED: r.column('copper', composition.COPPER_COLUMNS[0]),
                                           composition.FIXED_PART: r.column('copper', composition.COPPER_COLUMNS[1])},
                        COPPER_COLOURS))


def run(params: Params) -> int:
    """Reads 02's draws, checks that they belong together, and draws the pages. 0 when it has drawn them, 1 when
    something stopped it (nothing drawn)."""
    print(f'Reading the draws of 02 from {params.output.composition_dir}/ and {params.output.parts_dir}/ …', flush=True)
    try:
        robots = read_draws(params)
    except (FileNotFoundError, schemas.WorkbookError) as error:
        print(f'{error}\nThe draws of 02 are not all there: run 02_composition.py first.', file=sys.stderr)
        return 1
    # The outliers, not drawn by 02, for the notes page (E30 point 4): from the register.
    try:
        outliers = schemas.outlier_robots(schemas.read_register(absolute(params.data.register)), params)
    except schemas.WorkbookError as error:
        print(f'{error}\nThe register is needed for the outliers on the notes page: run '
              'tools/make_humanoid_register.py first.', file=sys.stderr)
        return 1
    # The draws belong together, and hold no robot set as an outlier (02's register.txt of each type, open item 5).
    try:
        found = problems(robots) + outliers_in_draws(params, outliers)
    except FileNotFoundError as error:
        print(f'{error}\nThe draws of 02 are not all there: run 02_composition.py first.', file=sys.stderr)
        return 1
    if found:
        print('The draws of 02 do not belong together; nothing is drawn. Run 02_composition.py again.',
              file=sys.stderr)
        for problem in found:
            print(f'  {problem}', file=sys.stderr)
        return 1
    print(f'{len(robots)} robot types, {len(robots[0].tables["total"][1]):,} draws each: they add up. Drawing the pages '
          '…', flush=True)
    out = absolute(params.output.comparison_dir)
    os.makedirs(out, exist_ok=True)
    written = []
    for name, figure in pages(robots, params, outliers):
        figure.savefig(os.path.join(out, name), dpi=params.output.dpi, facecolor='white')
        plt.close(figure)
        written.append(name)
        print(f'  {name}', flush=True)
    for name in OLD_PAGES:
        if os.path.exists(os.path.join(out, name)):
            os.remove(os.path.join(out, name))
            print(f'  {name} removed: a page of the old form of 03.', flush=True)
    for name in composition.remove_pages_not_drawn(out, PREFIX, SERIES, written):
        print(f'  {name} removed: a page of an earlier run no longer drawn.', flush=True)
    print(f'03 done: {len(written)} pages drawn into {params.output.comparison_dir}/.', flush=True)
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
