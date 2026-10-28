"""
04_parts_taken_apart.py
=======================

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

Robot type 1 taken apart: where its critical elements sit, kind of part by kind of part, and how sure we are; drawn
from the draws 02_composition.py makes of robot type 1 over its robots. Press Run. No arguments; every setting is in
`src/params_schema.py`. Run `00_parameters.py`, `01_schemas.py` and `02_composition.py` first.

Matthias, 2026-10-27: "the slipt into parts is just to get a deeper look into the robot, so that there is information
on where the interesting materials are and the recycling can be optimized". On 2026-10-28 the drawing moved to 02, so
that robot type 1 is drawn once, over all its robots of the register ("Why is it in 04", "Yes in 02 it is all type 1
in.!", "Yes, code it in 02"); this stage draws its two approved figures from what 02 writes (one copy of the code).

WHAT IT READS
-------------
  - What 02 writes of robot type 1 taken apart, in `output.parts_dir` (`data/parts_taken_apart/`): robots.npy (the
    robot taken apart whose parts each draw takes, and the robot of the register it is), elements.npy and
    estimated.npy (every element in every kind of part, and its kg resting on masses labelled E), register.txt (the
    robots of the register drawn);
  - the parts file (`data.parts_taken_apart`), through 01's `read_parts_taken_apart`: which joints' magnets are for
    150 °C or more in most draws (sheet MagnetGrades), for the overview's red rings;
  - the settings `output.parts_figures_dir` and `output.dpi`.

WHAT IT DRAWS
-------------
Into `output.parts_figures_dir` (`figures/parts_taken_apart/`; not in git) the two figures Matthias approved, each on
pages of a screen's shape (16 × 9 inches, text 14 points and up): `robot_type_1_elements_1.png` and `_2.png` (one
histogram per critical element, each bar split by kind of part, three across) and `robot_type_1_overview_1.png` to
`_5.png` (the robot with its joints and parts, and two critical elements a page, one row per kind of part).

Where it sits: after 02_composition.py, whose draws it reads and whose functions it uses.
"""

from __future__ import annotations

import importlib.util
import os
import sys
import textwrap
from dataclasses import dataclass

# Run from anywhere, and put the project root on the path, so that `src` imports. Must come before any import of src.
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import numpy as np  # noqa: E402

from src.params_schema import ParameterError, Params, absolute, current  # noqa: E402


def load_stage(name: str, file: str):
    """A stage of the project as a module, to use its functions (one copy of the code). Its name starts with a digit,
    so it is loaded from its path and registered under `name`; where the tests have loaded it already, that module is
    used."""
    path = os.path.join(HERE, file)
    loaded = sys.modules.get(name)
    if loaded is not None and os.path.samefile(getattr(loaded, '__file__', path), path):
        return loaded
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


composition = load_stage('composition', '02_composition.py')   # 02, which loads 01 as `schemas`
schemas = composition.schemas
import matplotlib.pyplot as plt  # noqa: E402  (after 01, which sets matplotlib to draw into files only)
from matplotlib.patches import Circle, Patch, Rectangle  # noqa: E402
from matplotlib.transforms import blended_transform_factory  # noqa: E402

# The ten kinds of part, each with its name and colour, and how a joint's kind is named: 02's, which draws them.
KINDS, JOINT_KIND, HOT_CLASSES = composition.KINDS, composition.JOINT_KIND, composition.HOT_CLASSES

# The critical elements of the figures, in Matthias's order (V49): symbol (Nd+Pr: the two added) and name.
FIGURE_ELEMENTS = [('Cu', 'Copper'), ('Al', 'Aluminium'), ('Ag', 'Silver'), ('Au', 'Gold'), ('Pd', 'Palladium'),
                   ('Ta', 'Tantalum'), ('Nd+Pr', 'Neodymium and praseodymium'), ('Dy', 'Dysprosium'),
                   ('Ga', 'Gallium'), ('In', 'Indium')]
HISTOGRAM_BINS = 70   # the bars of a distribution, as in RAWCLICDataCenters' figures
HELD_SHARE = 0.025    # a kind of part holding an element in fewer draws than this is not drawn (the 95 % rule)


# ------------------------------------------------------------------------------------------------------
# What is read: 02's draws of robot type 1 taken apart
# ------------------------------------------------------------------------------------------------------

@dataclass
class Taken:
    """Robot type 1 taken apart, as 02 drew it N times."""

    n: int
    robots: list          # the robots taken apart, in the order of the parts file's sheet Robots
    register: list        # the robots of the register drawn, '<number> <name>'
    elements: dict        # (kind, element) -> kg in each draw
    estimated: dict       # (kind, element) -> the part of those kg resting on masses labelled E
    hot: dict             # kind of joint -> True where its magnets are for 150 °C or more in most draws


def read_table(folder: str, table: str) -> tuple:
    """One table 02 wrote: (its columns, its draws as float64)."""
    with open(os.path.join(folder, f'{table}.txt'), encoding='utf-8') as file:
        columns = file.read().splitlines()
    return columns, np.load(os.path.join(folder, f'{table}.npy')).astype(np.float64)


def by_kind_and_element(columns: list, draws: np.ndarray) -> dict:
    """'<kind's name>: <element>' columns as (kind, element) -> kg in each draw."""
    kind_of_name = {name: kind for kind, (name, _) in KINDS.items()}
    out = {}
    for k, column in enumerate(columns):
        name, element = column.rsplit(': ', 1)
        out[(kind_of_name[name], element)] = draws[:, k]
    return out


def hot_joints(apart) -> dict:
    """Kind of joint -> whether its heat group draws a grade class for 150 °C or more in most draws."""
    hot = {}
    for j in apart.joints:
        kind = JOINT_KIND[j.name.split()[0].lower()]
        share = sum(p for klass, p in composition.group_classes(apart, j.heat_group) if klass in HOT_CLASSES)
        hot[kind] = hot.get(kind, False) or share > 0.5
    return hot


def read_taken(params: Params) -> Taken:
    """02's draws of robot type 1 taken apart and the parts file. Raises FileNotFoundError where 02 has not written
    them, schemas.WorkbookError where the parts file cannot be read."""
    folder = absolute(params.output.parts_dir)
    robots_columns, robots = read_table(folder, 'robots')
    names = robots_columns[0][robots_columns[0].index('(') + 1:-1].split(', ')
    elements = by_kind_and_element(*read_table(folder, 'elements'))
    estimated = by_kind_and_element(*read_table(folder, 'estimated'))
    with open(os.path.join(folder, 'register.txt'), encoding='utf-8') as file:
        register = file.read().splitlines()
    apart = schemas.read_parts_taken_apart(absolute(params.data.parts_taken_apart))
    return Taken(robots.shape[0], [name.split(' ', 1)[1] for name in names], register, elements, estimated,
                 hot_joints(apart))


# ------------------------------------------------------------------------------------------------------
# The figures
# ------------------------------------------------------------------------------------------------------

INK = '#222222'        # lines and numbers
MUTED = '#555555'      # footnotes
SHELL, OUTLINE = '#E9ECEF', '#8A8A8A'   # the robot's body, as 01 draws it
HOT_RING = '#CC0000'   # the ring of a hot joint

# The pages (Matthias, 2026-10-28: "Have the overview on several pages. I can not read it. too smal, you should notice
# this before you sjhow me. Elements is an edge case. Also quite small"). Each page has a screen's shape, 16 × 9
# inches, and no text below TEXT points: fit to a 1920 × 1080 screen its smallest text is about 23 pixels tall
# (tests/test_parts_taken_apart.py requires 18 at least). A footnote is wrapped at NOTE_WIDTH characters, so that it
# stays within the page's width.
PAGE = (16, 9)
TEXT, LABEL, TITLE, HEADING = 14, 15, 16, 20   # points: the smallest text, axis labels, panel titles, page titles
NOTE_WIDTH = 145
TITLE_WIDTH = 30   # characters in a line of an element page's panel title; a longer one takes two lines
# The overview's panels: their width (share of the page), and where their two columns of numbers start, the median's
# and the mean's (share of the panel's width beyond its right edge), so that both stay within the page.
PANEL_WIDTH = 0.42
NUMBER_COLUMNS = (1.02, 1.20)
ELEMENT_PAGES = [FIGURE_ELEMENTS[:6], FIGURE_ELEMENTS[6:]]                                # three panels across
OVERVIEW_PAGES = [FIGURE_ELEMENTS[k:k + 2] for k in range(0, len(FIGURE_ELEMENTS), 2)]    # two elements a page
FIGURES = tuple([f'robot_type_1_elements_{k}.png' for k in range(1, len(ELEMENT_PAGES) + 1)]
                + [f'robot_type_1_overview_{k}.png' for k in range(1, len(OVERVIEW_PAGES) + 1)])

# Where each kind sits on the robot of the overview, in 01's body units (across, up), and its mark: a number for the
# joints, a letter for the other kinds, the same in the rows of the panels. The joints on both sides of the robot.
SPOTS = {'hips': [(-0.06, 0.475), (0.06, 0.475)], 'knees': [(-0.065, 0.27), (0.065, 0.27)],
         'ankles': [(-0.065, 0.06), (0.065, 0.06)], 'waist': [(0.0, 0.565)],
         'arms': [(-0.16, 0.81), (-0.175, 0.64), (-0.185, 0.475), (0.16, 0.81), (0.175, 0.64), (0.185, 0.475)],
         'battery': [(-0.07, 0.62)], 'boards': [(0.07, 0.75)], 'head': [(0.0, 0.925)],
         'cables': [(0.075, 0.62)], 'frame': [(-0.07, 0.75)]}
MARKS = {'hips': '1', 'knees': '2', 'ankles': '3', 'waist': '4', 'arms': '5', 'battery': 'A', 'boards': 'B',
         'head': 'C', 'cables': 'D', 'frame': 'E'}
DARK = {'hips', 'knees', 'battery', 'cables', 'head'}   # the kinds whose colour takes white text


def save(figure, path: str, dpi: int) -> None:
    """Write a page and close it."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    figure.savefig(path, dpi=dpi, facecolor='white')
    plt.close(figure)


def note(*paragraphs: str) -> str:
    """A footnote: its paragraphs, each wrapped at NOTE_WIDTH characters (a number and its unit kept together by a
    non-breaking space)."""
    return '\n'.join(textwrap.fill(p, NOTE_WIDTH) for p in paragraphs)


def figure_unit(values_kg: np.ndarray) -> tuple:
    """The unit a panel is drawn in, by the mean of its draws: kg from 1 kg, g from 1 g, mg below. Returns the kg in
    one unit and its symbol."""
    typical = float(np.mean(np.abs(values_kg))) if values_kg.size else 0.0
    if typical >= 1.0:
        return 1.0, 'kg'
    if typical >= 1e-3:
        return 1e-3, 'g'
    return 1e-6, 'mg'


def figure_number(x: float, _pos=None) -> str:
    """A number as the figures write it (RAWCLICDataCenters' rule): whole from 10, one decimal from 1, two significant
    digits below 1, written out (4000, never 4k; 0.000095, never 9.5e-05). (`_pos` lets matplotlib use it as a tick
    formatter.)"""
    if abs(x) >= 10:
        return f'{x:.0f}'
    if abs(x) >= 1:
        return f'{x:.1f}'.rstrip('0').rstrip('.')
    return np.format_float_positional(float(f'{x:.2g}'), trim='-')


def by_kind(d: Taken, symbol: str) -> dict:
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


def robots_note(d: Taken) -> str:
    """What every draw is, for the footnotes."""
    names = ', '.join(d.robots[:-1]) + ' or ' + d.robots[-1]
    return (f'{d.n:,} draws, each one of the {len(d.register)} robots of type 1 in the register, each as often; its '
            f'parts those of the {names} taken apart (itself where it is one of them), its joints, frame, shell and '
            'battery scaled to its mass.')


def stacked_panel(axes, kinds: dict, title: str, share_label: bool) -> None:
    """One panel of the element pages, the form Matthias set for RAWCLICDataCenters' 05: the histogram of the robot's
    total of one element over the draws (the height the share of the draws), each bar split into the kg its draws hold
    in each kind of part, the kind with the smaller mean lower; the median a solid line and the mean a dotted one, each
    with its number (Matthias, 2026-10-28: "Showing the mean is wrong. It is not a good measure. Use the median or show
    boths"; his answer "Both, median first"); the 2.5th and 97.5th percentile dashed; its own scale and unit."""
    axes.set_title(title, fontsize=TITLE, fontweight='bold', loc='left')
    if not kinds:
        axes.text(0.5, 0.5, 'none in robot type 1', transform=axes.transAxes, ha='center', va='center', fontsize=TEXT)
        axes.set_xticks([])
        axes.set_yticks([])
        return
    total = sum(kinds.values())
    per, unit = figure_unit(total)
    values = total / per
    edges = np.histogram_bin_edges(values, bins=HISTOGRAM_BINS)
    index = np.clip(np.digitize(values, edges[1:-1]), 0, len(edges) - 2)   # the bar each draw falls into
    share_of_draws = np.bincount(index, minlength=len(edges) - 1) / values.size
    kg_all = np.bincount(index, weights=total, minlength=len(edges) - 1)
    bottom = np.zeros(len(edges) - 1)
    for kind in sorted((k for k in kinds if held(kinds[k])), key=lambda k: kinds[k].mean()):
        kg = np.bincount(index, weights=kinds[kind], minlength=len(edges) - 1)
        height = share_of_draws * np.divide(kg, kg_all, out=np.zeros_like(kg), where=kg_all > 0)
        axes.bar(edges[:-1], height, width=np.diff(edges), align='edge', bottom=bottom, color=KINDS[kind][1],
                 edgecolor='none')
        bottom += height
    median, mean = float(np.median(values)), float(values.mean())
    axes.axvline(median, color=INK, linewidth=1.8)
    axes.axvline(mean, color=INK, linewidth=1.8, linestyle=':')
    for bound in np.percentile(values, [2.5, 97.5]):
        axes.axvline(bound, color=INK, linewidth=1.2, linestyle='--')
    for x, y, what in ((median, 0.97, 'median'), (mean, 0.82, 'mean')):
        axes.text(x, y, f' {what} {figure_number(x)} {unit}', transform=axes.get_xaxis_transform(), ha='left',
                  va='top', fontsize=TEXT, color=INK, bbox=dict(facecolor='white', edgecolor='none', alpha=0.8, pad=1))
    axes.xaxis.set_major_locator(plt.MaxNLocator(4))
    axes.xaxis.set_major_formatter(plt.FuncFormatter(figure_number))
    axes.yaxis.set_major_locator(plt.MaxNLocator(4))
    axes.yaxis.set_major_formatter(plt.FuncFormatter(figure_number))
    axes.tick_params(labelsize=TEXT)
    axes.set_xlabel(f'mass ({unit})', fontsize=LABEL)
    if share_label:
        axes.set_ylabel('share of the draws', fontsize=LABEL)
    axes.grid(axis='x', alpha=0.3)


def element_page(d: Taken, page: list, number: int):
    """One page of the element figure Matthias approved (V49), for the three robots: its elements three across, each
    the stacked distribution of the robot's total; the legend of the kinds of part at the top; the footnote below."""
    columns = 3
    figure, axes = plt.subplots(2, columns, figsize=PAGE, squeeze=False)
    for k, (symbol, name) in enumerate(page):
        stacked_panel(axes[k // columns, k % columns], by_kind(d, symbol),
                      textwrap.fill(f'{name} ({symbol})', TITLE_WIDTH), k % columns == 0)
    for spare in axes.flatten()[len(page):]:
        spare.axis('off')
    figure.suptitle(f'Robot type 1, all its {len(d.register)} robots: critical elements in one robot ({number} of '
                    f'{len(ELEMENT_PAGES)})', fontsize=HEADING, y=0.985)
    handles = [Patch(color=colour, label=label) for label, colour in KINDS.values()]
    figure.legend(handles=handles, loc='upper center', bbox_to_anchor=(0.5, 0.94), ncol=5, frameon=False,
                  fontsize=TEXT)
    figure.tight_layout(rect=(0, 0.2, 1, 0.86))
    figure.text(0.5, 0.01, note(
        'Bars: the draws, the height the share of the draws; solid line: the median; dotted line: the mean; dashed '
        'lines: 2.5th and 97.5th percentile (the 95% interval); each panel on its own scale and unit; each bar split '
        'into the weight its draws hold in each kind of part, the smaller lower; a kind of part holding the element '
        'in fewer than 2.5% of the draws is not drawn.', robots_note(d),
        'The joints with their driver boards and encoders; the magnets\' grade class (with it their dysprosium) drawn '
        'by each joint\'s heat, the knees hottest, the arms coolest, one draw deciding for every joint; the NdFeB '
        'magnets shown by their neodymium and praseodymium; the battery metals and silicon not shown.'), ha='center',
        va='bottom', fontsize=TEXT, color=MUTED)
    return figure


def ridge_panel(axes, kinds: dict, estimated: dict, title: str) -> None:
    """One panel of the overview: one row per kind of part holding the element, labelled with its mark on the robot,
    each the histogram of its kg over the draws scaled to the row, hatched where more than half its mean rests on
    masses labelled E; the median a solid line and the mean a dotted one, their numbers in two columns at the right
    (answer "Both, median first"); the 2.5th and 97.5th percentile dashed; one scale and unit for the panel."""
    shown = [k for k in KINDS if k in kinds and held(kinds[k])]
    axes.set_title(title, fontsize=TITLE, fontweight='bold', loc='left')
    if not shown:
        axes.text(0.5, 0.5, 'none in robot type 1', transform=axes.transAxes, ha='center', va='center', fontsize=TEXT)
        axes.axis('off')
        return
    per, unit = figure_unit(sum(kinds[k] for k in shown))
    top = max(np.percentile(kinds[k], 99.9) for k in shown) / per
    edges = np.linspace(0, top if top > 0 else 1, 51)
    right = blended_transform_factory(axes.transAxes, axes.transData)
    for row, kind in enumerate(reversed(shown)):
        values = kinds[kind] / per
        counts, _ = np.histogram(np.clip(values, 0, edges[-1]), bins=edges)
        heights = 0.8 * counts / max(counts.max(), 1)
        hatched = float(estimated[kind].mean()) > 0.5 * float(kinds[kind].mean())
        axes.bar(edges[:-1], heights, width=np.diff(edges), align='edge', bottom=row + 0.05, color=KINDS[kind][1],
                 edgecolor=INK if hatched else 'none', linewidth=0, hatch='///' if hatched else None)
        median, mean = float(np.median(values)), float(values.mean())
        axes.plot([median, median], [row + 0.05, row + 0.9], color=INK, linewidth=1.8)
        axes.plot([mean, mean], [row + 0.05, row + 0.9], color=INK, linewidth=1.8, linestyle=':')
        for bound in np.percentile(values, [2.5, 97.5]):
            axes.plot([bound, bound], [row + 0.05, row + 0.9], color=INK, linewidth=1.2, linestyle='--')
        for column, x in zip(NUMBER_COLUMNS, (median, mean)):
            axes.text(column, row + 0.45, figure_number(x), transform=right, ha='left', va='center', fontsize=TEXT,
                      color=INK)
    for column, what in zip(NUMBER_COLUMNS, ('median', 'mean')):
        axes.text(column, len(shown) + 0.1, what, transform=right, ha='left', va='bottom', fontsize=TEXT, color=INK)
    axes.set_title(f'{title}, in {unit}', fontsize=TITLE, fontweight='bold', loc='left')
    axes.set_ylim(0, len(shown))
    axes.set_yticks([row + 0.45 for row in range(len(shown))])
    axes.set_yticklabels([f'{MARKS[k]}  {KINDS[k][0]}' for k in reversed(shown)], fontsize=TEXT)
    axes.tick_params(axis='y', length=0)
    axes.set_xlim(0, edges[-1])
    axes.xaxis.set_major_locator(plt.MaxNLocator(6))
    axes.xaxis.set_major_formatter(plt.FuncFormatter(figure_number))
    axes.tick_params(axis='x', labelsize=TEXT)
    axes.set_xlabel(f'mass ({unit})', fontsize=LABEL)
    axes.grid(axis='x', alpha=0.3)
    for side in ('top', 'right'):
        axes.spines[side].set_visible(False)


def draw_schema(axes, d: Taken) -> None:
    """The robot of the overview: 01's schematic body, each joint group numbered where it sits on both sides (a red
    ring where its magnets are for 150 °C or more in most draws), the other kinds lettered, a short key below; the
    marks are those of the panels' rows."""
    schemas.body_shapes(axes, 0.0, 0.0, 1.0, facecolor=SHELL, edgecolor=OUTLINE, linewidth=1.0)
    for kind, spots in SPOTS.items():
        colour = KINDS[kind][1]
        for u, v in spots:
            at = (u, -v)
            if MARKS[kind].isdigit():
                axes.add_patch(Circle(at, 0.031, facecolor=colour, edgecolor=HOT_RING if d.hot.get(kind) else INK,
                                      linewidth=3.0 if d.hot.get(kind) else 0.8, zorder=3))
            else:
                axes.add_patch(Rectangle((u - 0.027, -v - 0.027), 0.054, 0.054, facecolor=colour, edgecolor=INK,
                                         linewidth=0.8, zorder=3))
            axes.text(*at, MARKS[kind], ha='center', va='center', fontsize=TEXT, fontweight='bold', zorder=4,
                      color='white' if kind in DARK else INK)
    axes.text(-0.31, 0.09, 'Numbers: joints; letters: the\nother parts, as in the rows.\nRed ring: magnets for '
              '150 °C\nor more in most draws.', ha='left', va='top', fontsize=TEXT, color=INK, linespacing=1.3)
    axes.set_xlim(-0.32, 0.32)
    axes.set_ylim(0.36, -1.02)
    axes.set_aspect('equal')
    axes.axis('off')


def overview_page(d: Taken, page: list, number: int):
    """One page of the overview Matthias approved ("Looks good to me", 2026-10-27), for three robots (answer E,
    "Groups, histograms"): left the robot with its joint groups numbered and its other kinds lettered; right two
    critical elements, one above the other, one row per kind of part holding them; the footnote below."""
    figure = plt.figure(figsize=PAGE)
    figure.add_axes((0.01, 0.17, 0.22, 0.72))
    draw_schema(figure.axes[0], d)
    panels = [(symbol, name, by_kind(d, symbol)) for symbol, name in page]
    rows = [sum(held(v) for v in kinds.values()) + 1 for _, _, kinds in panels]
    bottom, top, gap = 0.235, 0.875, 0.11
    height = top - bottom - gap * (len(panels) - 1)
    for k, (symbol, name, kinds) in enumerate(panels):
        tall = height * rows[k] / sum(rows)
        y = top - tall - sum(height * rows[i] / sum(rows) + gap for i in range(k))
        estimated = {kind: sum((d.estimated[(kind, e)] for e in symbol.split('+') if (kind, e) in d.estimated),
                               np.zeros(d.n)) for kind in kinds}
        ridge_panel(figure.add_axes((0.43, y, PANEL_WIDTH, tall)), kinds, estimated, f'{name} ({symbol})')
    figure.suptitle('Robot type 1 taken apart: where the critical materials sit, and how sure we are '
                    f'({number} of {len(OVERVIEW_PAGES)})', fontsize=HEADING, y=0.975)
    figure.text(0.5, 0.01, note(
        "Each row: the element's weight in that kind of part over the draws, the height the share of the draws scaled "
        'to the row; solid line: the median; dotted line: the mean; dashed lines: 2.5th and 97.5th percentile (the 95% '
        'interval); '
        'hatched: more than half of the mean rests on parts whose mass is an estimate (E); a kind of part holding the '
        'element in fewer than 2.5% of the draws has no row; each panel on its own scale and unit.',
        robots_note(d)), ha='center', va='bottom', fontsize=TEXT, color=MUTED)
    return figure


def figure_pages(d: Taken) -> list:
    """Every page of both figures, as (file name, figure), in the order of FIGURES."""
    pages = [element_page(d, page, k + 1) for k, page in enumerate(ELEMENT_PAGES)]
    pages += [overview_page(d, page, k + 1) for k, page in enumerate(OVERVIEW_PAGES)]
    return list(zip(FIGURES, pages))


def draw_figures(d: Taken, params: Params) -> None:
    """Every page of both figures into `output.parts_figures_dir`."""
    folder = absolute(params.output.parts_figures_dir)
    for name, figure in figure_pages(d):
        save(figure, os.path.join(folder, name), params.output.dpi)



# ------------------------------------------------------------------------------------------------------
# The run
# ------------------------------------------------------------------------------------------------------

def run(params: Params) -> int:
    """Read 02's draws, draw the figures, and report in plain words."""
    try:
        d = read_taken(params)
    except FileNotFoundError as error:
        print(f'{error}\nRobot type 1 taken apart has not been drawn: run 02_composition.py first.', file=sys.stderr)
        return 1
    except schemas.WorkbookError as error:
        print(error, file=sys.stderr)
        return 1
    draw_figures(d, params)
    for symbol, name in FIGURE_ELEMENTS:
        total = sum(by_kind(d, symbol).values())
        per, unit = figure_unit(total)
        mean, median, low, high = composition.statistics(total / per)
        print(f'{name} in one robot: median {figure_number(median)} {unit}, mean {figure_number(mean)} {unit} (95 %: '
              f'{figure_number(low)} to {figure_number(high)})')
    print(f'The two figures drawn into {params.output.parts_figures_dir}/, from {d.n:,} draws of 02 over '
          f'{len(d.register)} robots of type 1.')
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
