"""
03_comparison.py
================

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

The robot types side by side, by material, by element, by part group and by body region, each with its 95 % interval,
from the draws 02_composition.py wrote. Press Run. No arguments; every setting is in `src/params_schema.py`. Run
`02_composition.py` first.

Matthias, 2026-10-26: "I want that it is possible to compare on a material level between the 6 types of roboy", and
on the level of the parts; "So come up with a proposition, which I can understand as 20 year old, not familiar with
the topic". Point 15 of the specification he agreed (documentation/claude/HANDOVER.md): "03 reads the six robot
types' draws from 02, never re-deriving them, and draws them side by side: by material, by element, by part group and
body region, each with its 95 % interval."

WHAT IT READS
-------------
The draws 02 wrote, `output.composition_dir`/<n>_<name>/<table>.npy with their columns in <table>.txt, as they are: it
draws nothing at random itself. The names of the robot types come from the workbook, through 01's `read_workbook`.

WHAT IT CHECKS
--------------
That the draws belong together (`problems`): every robot type has every table, with the same number of draws, the
same columns in the same order as the first robot type, and, in every draw, its materials, part groups and body
regions add up to its total (to the rounding of float32). Any problem stops it before anything is drawn.

WHAT IT DRAWS
-------------
Into `output.comparison_dir` (`figures/comparison/`; not in git), one page per view (recommendation g):

  materials.png, elements.png, part_groups.png, body_regions.png
        one small chart per material (element, part group, body region), with one row per robot type: a bar of the
        mean and a line over 95 % of the draws (02's interval_bars), and the mean written beside it. Each chart has
        its own kg scale, so that a material of a few grams can be read as well as one of 25 kg.

Where it sits: after 02_composition.py, the last stage.
"""

from __future__ import annotations

import importlib.util
import os
import sys
from dataclasses import dataclass

# Run from anywhere, and put the project root on the path, so that `src` imports. Must come before any import of src.
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import numpy as np  # noqa: E402
from matplotlib.ticker import MaxNLocator  # noqa: E402

from src.params_schema import ParameterError, Params, absolute, current  # noqa: E402


def load_composition():
    """02_composition.py as a module, for the files it writes (TABLES, folder_name) and its drawing (interval_bars,
    mass); it loads 01 as `schemas`. Loaded from its path, registered as 'composition', and only once: where the tests
    have loaded it already, that module is used."""
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

# The pages, one per view: the table of 02's draws it shows -> its title.
VIEWS = {'materials': 'By material', 'elements': 'By element', 'part_groups': 'By part group',
         'body_regions': 'By body region'}
# The draws are written as float32, whose rounding is about 6e-8 of a value; a sum of a dozen columns may miss the
# total by some 1e-6 of it. A miss above this share of the total means the files do not belong together.
FLOAT32_TOLERANCE = 1e-4

COLUMNS = 4                 # charts side by side on a page
PANEL_LABEL = 1.05          # the robot types left of a chart, inches
PANEL_CHART = 2.35          # the width of a chart, inches
PANEL_NUMBER = 0.6          # the means right of a chart, inches
PANEL_GAP = 0.45            # between two charts, inches
PANEL_ROW = 0.21            # the height of one robot type's row, inches
PAGE_WIDTH = 2 * composition.MARGIN + COLUMNS * (PANEL_LABEL + PANEL_CHART + PANEL_NUMBER) + (COLUMNS - 1) * PANEL_GAP


@dataclass
class Robot:
    """One robot type, as 02 wrote it."""

    number: int               # the robot type, 1 to 6
    title: str                # its name, e.g. 'Compact Research & Developer'
    tables: dict              # one of 02's TABLES -> (its columns, its draws as written: N rows × one column each)

    def column(self, table: str, name: str) -> np.ndarray:
        """The draws of one column of one table, in float64 for the statistics."""
        columns, draws = self.tables[table]
        return draws[:, columns.index(name)].astype(np.float64)


def read_draws(params: Params) -> list:
    """The draws of every robot type of the workbook, as 02 wrote them. Raises FileNotFoundError where 02 has not
    written a robot type."""
    book = schemas.read_workbook(absolute(params.data.workbook), params)
    out = absolute(params.output.composition_dir)
    robots = []
    for category in book.categories:
        folder = os.path.join(out, composition.folder_name(category))
        tables = {}
        for table in composition.TABLES:
            with open(os.path.join(folder, f'{table}.txt'), encoding='utf-8') as file:
                columns = file.read().splitlines()
            tables[table] = (columns, np.load(os.path.join(folder, f'{table}.npy')))
        robots.append(Robot(category.number, category.name, tables))
    return robots


def problems(robots: list) -> list:
    """Whether the draws belong together: every table of every robot type with the number of draws and the columns
    of the first robot type, and its materials, part groups and body regions adding up to its total in every draw."""
    found = []
    first = robots[0]
    n = len(first.tables['total'][1])
    for robot in robots:
        shapes_right = True
        for table in composition.TABLES:
            columns, draws = robot.tables[table]
            if draws.ndim != 2 or draws.shape[0] != n:
                found.append(f'robot type {robot.number}: {table} has {draws.shape[0]} draws, not {n}.')
                shapes_right = False
            elif draws.shape[1] != len(columns):
                found.append(f'robot type {robot.number}: {table} has {draws.shape[1]} columns, but its list names '
                             f'{len(columns)}.')
                shapes_right = False
            elif columns != first.tables[table][0]:
                found.append(f'robot type {robot.number}: the columns of {table} are not those of robot type '
                             f'{first.number}.')
        if not shapes_right:
            continue
        total = robot.column('total', 'Total')
        for table, what in (('materials', 'the materials'), ('part_groups', 'the part groups'),
                            ('body_regions', 'the body regions')):
            off = np.abs(robot.tables[table][1].astype(np.float64).sum(axis=1) - total) > FLOAT32_TOLERANCE * total
            if off.any():
                found.append(f'robot type {robot.number}: {what} do not add up to the total in {off.sum()} draws.')
    return found


def statistics(draws: np.ndarray) -> tuple:
    """(any mass in any draw, the mean, 2.5 %, 97.5 %) of one quantity, with 02's statistics_of."""
    s = composition.statistics_of(draws)
    return bool(draws.any()), s['Mean (kg)'], s['2.5 % (kg)'], s['97.5 % (kg)']


def label(table: str, name: str) -> str:
    """A column in plain words: an element by its name, 'Carbon (C)'; anything else as 02 names it."""
    return composition.element_label(name) if table == 'elements' else name


def view_columns(robots: list, table: str, params: Params) -> list:
    """The columns a view shows: all of the table's, but for the elements those not shown left out
    (`composition.elements_not_shown`, with 02's own function; the draws keep them)."""
    names = robots[0].tables[table][0]
    return composition.shown_elements(names, params) if table == 'elements' else names


def draw_view(robots: list, table: str, path: str, params: Params) -> None:
    """The page of one view: one chart per column of the table, with one row per robot type."""
    names = view_columns(robots, table, params)
    draws = len(robots[0].tables['total'][1])
    rows_of_charts = -(-len(names) // COLUMNS)
    chart_height = PANEL_ROW * len(robots)
    block = 0.3 + chart_height + 0.55          # a chart's title, its rows and its kg scale
    key = schemas.wrap('; '.join(f'Robot type {r.number}: {r.title}' for r in robots) + '.', 210)
    notes = view_notes(table, params)
    top = 1.05 + len(key) * schemas.LINE + 0.25
    height = top + rows_of_charts * block + 0.2 + len(notes) * schemas.LINE + 0.4
    figure, page = schemas.new_page(PAGE_WIDTH, height)
    page.text(composition.MARGIN, 0.35, f'{VIEWS[table]}: the robot types side by side', fontsize=15,
              fontweight='bold', va='top')
    page.text(composition.MARGIN, 0.75, f'kg per robot, from {draws:,} draws of each robot type. Each bar is the '
                                         'mean, written beside it; its line spans 95 % of the draws, from 2.5 % to '
                                         '97.5 %. Each chart has its own kg scale.', fontsize=10,
              color=composition.MUTED, va='top')
    schemas.write(page, composition.MARGIN, 1.05, key, size=9, colour=composition.MUTED)
    for k, name in enumerate(names):
        x = composition.MARGIN + (k % COLUMNS) * (PANEL_LABEL + PANEL_CHART + PANEL_NUMBER + PANEL_GAP)
        y = top + (k // COLUMNS) * block
        schemas.write(page, x, y, [label(table, name)], size=10, weight='bold')
        y += 0.3
        axes = figure.add_axes([(x + PANEL_LABEL) / PAGE_WIDTH, 1 - (y + chart_height) / height,
                                PANEL_CHART / PAGE_WIDTH, chart_height / height])
        rows = [(f'Robot type {r.number}', r.column(table, name)) for r in robots]
        composition.interval_bars(axes, rows, size=8.5, grey=name in ('Mixed', composition.NOT_ALLOCATED))
        axes.xaxis.set_major_locator(MaxNLocator(4))   # a narrow chart: few kg marks, so that they never touch
        for i, (_, values) in enumerate(rows):
            present, mean, _, _ = statistics(values)
            page.text(x + PANEL_LABEL + PANEL_CHART + PANEL_NUMBER, y + (i + 0.5) * PANEL_ROW,
                      composition.mass(mean) if present else '–', fontsize=8.5, ha='right', va='center')
    below = top + rows_of_charts * block + 0.2
    schemas.write(page, composition.MARGIN, below, notes, size=9)
    schemas.save(figure, path, params.output.dpi)


def view_notes(table: str, params: Params) -> list:
    """What a reader needs to read the page of one view, in plain words."""
    notes = ['–: none in this robot type.']
    if table == 'materials':
        notes.insert(0, "Not allocated: the parts' mass minus the materials' mass in each draw; below zero where the "
                        'drawn materials weigh more than the drawn parts. Battery materials: the cells only.')
    elif table == 'elements':
        notes.insert(0, 'Only the materials that have a recipe so far are in the elements; which ones, for each robot '
                        'type, is on its page in figures/composition/. ' + composition.not_shown_note(params))
    elif table == 'part_groups':
        notes.insert(0, 'Battery: the battery packs as the parts list gives them; their cells alone are Battery '
                        'materials on the page by material.')
    elif table == 'body_regions':
        notes.insert(0, 'Whole body: the parts spread over the body (frame, shell, cables), and the parts the workbook '
                        'places in several regions without saying how many sit where (the sheet Lists of the shared '
                        'lists).')
    return [line for note in notes for line in schemas.wrap('• ' + note, 210)]


def run(params: Params) -> int:
    """Reads 02's draws, checks that they belong together, and draws the four pages. 0 when it has drawn them, 1 when
    something stopped it (nothing drawn)."""
    try:
        robots = read_draws(params)
    except (FileNotFoundError, schemas.WorkbookError) as error:
        print(f'{error}\nThe draws of 02 are not all there: run 02_composition.py first.', file=sys.stderr)
        return 1
    found = problems(robots)
    if found:
        print('The draws of 02 do not belong together; nothing is drawn. Run 02_composition.py again.',
              file=sys.stderr)
        for problem in found:
            print(f'  {problem}', file=sys.stderr)
        return 1
    out = absolute(params.output.comparison_dir)
    for table in VIEWS:
        draw_view(robots, table, os.path.join(out, f'{table}.png'), params)
    print(f'{len(robots)} robot types, {len(robots[0].tables["total"][1]):,} draws each, read from '
          f'{params.output.composition_dir}/; drawn into {params.output.comparison_dir}/: '
          f"{', '.join(f'{t}.png' for t in VIEWS)}.")
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
