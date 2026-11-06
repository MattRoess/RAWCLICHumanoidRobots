"""
04_stock_and_flow.py
====================

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

The stock and flow of the humanoid robots in the world and of the critical and strategic elements in them, quarter by
quarter from 2025 to 2039, reported by year, in the way RAWCLICDataCenters' 07 follows the world's data centres: the
robots in use at each 1 January as the article ai-2040.com Plan A states them; each robot one unit with its lifetime; its
joints and its battery packs replaced on their own; every robot made as 02's draw i of its robot type. Press Run. No
arguments; every setting is in `src/params_schema.py` (section `stock_and_flow`). Run `02_composition.py` first.

Matthias, 2026-11-06: "Get the article, which was already the bases for the work on the stock and flow modeling of the
datacenters. Read it and use the stock numbers for the humanoid robots", "Do exactly what has been done for the
datacenter", "I want the same figures as for the datacenters, but expand them all the essential critcial and statigic
elements. Also have real lifetimes not something fixed like this. I want to see uncerttainites", "Add also the limit in
stock and production like for the data centers", to the table of this stage "Yes, build it"; then "No look at the robots
as a unit with exception of the batteries", "Have at least so many battery packs ready for use as it is needed to have
them for 1 day to switch. So they can recharge slowly", "Yes, replace joints" (documentation/claude/EVIDENCE.md E39 to
E43).

WHAT IT READS
-------------
  - Its settings (`stock_and_flow`): the article's robots at 1 January, 2025 to 2040 (10 M to 70 × 10⁹); a robot's
    lifetime 5 / 7 / 10 years; the hours a day, 24 (the article: robots "can work 24/7"); a joint's life 7,000 /
    10,000 / 30,000 hours; a battery pack's charges until 80 % of its capacity, 500 / 800 / 1,000, and the capacity
    below which it is replaced, 75 / 80 / 85 % (one value a draw); the runtime in 2025 of robot types 1, 3 and 5; the
    share of research robots (type 1) among the robots built, in 2025 and in 2040 (one point of the two triangles a
    draw).
  - His workbook (`data.workbook`): the shares of robot types 2, 4, 5 and 6 among the robots shipped (sheet Market
    Units & Shares 2025-2040, its first table; type 1's share there is not used, type 3's is the remainder) and the
    runtime or the battery energy density of each type (sheet Material Trajectories 2025-2040).
  - 02's draws of each robot type: the kg of each element of interest in one robot, by kind of part
    (`output.parts_dir`, table 'elements', columns '<kind>: <element>'), its elements in the order of 02's table
    (`output.composition_dir`, 'elements.txt'). All six types with as many draws; draw i of each type is a robot of
    draw i.
  - The world's mine production in 2025 and reserves of each element, for the figures: RAWCLICDataCenters' sheet
    ElementReference (`data.data_center_scenarios`, the values 07 draws), and USGS's data file (`data.usgs_commodities`)
    for magnesium, titanium and indium, which that sheet does not hold; both read where they lie.

HOW IT COUNTS (every draw; quarter by quarter, as 07)
-------------
  1. The robots: in use at the end of each quarter, the article's 1 January values, the quarters between geometric
     (V(y)^(1 − k/4) × V(y + 1)^(k/4), as 07). Each quarter's robots arrive in its middle and leave by the share of
     them whose lifetime (the triangle 5 / 7 / 10 years, spread among them) is shorter than their age; a quarter's
     inflow is the target less what the earlier quarters' robots still hold, never below 0. The robots of 1 January
     2025 by their ages: built in the quarters before at the article's own growth (its 2026 over its 2025), as many as
     it takes to hold the 10 M with their survivals (an estimate, E42).
  2. The robot types: each quarter's robots built by type. The research robots (type 1): their share drawn once a draw,
     the same point of its triangle of 2025 and of 2040, a straight line between; types 2, 4, 5 and 6 the workbook's
     shares, a straight line between its years; type 3, the largest, the remainder (1 minus the others; nothing is
     normalised, and a remainder below 0 stops the run). The robots of 1 January 2025 by the shares of 2025.
  3. The joint sets: a robot's joints (the kinds 01 numbers 1 to 6: hip, knee, ankle, waist, arm and head joints) a
     stock of its own, as many as the robots in use of its type, each set leaving when it wears out (its life the
     triangle 7,000 / 10,000 / 30,000 hours at the hours a day, spread among the sets) and replaced by a new one, as
     07's units that follow the GPUs: a stock target with their own lifetimes.
  4. The battery packs: a robot holds as many as one day's work needs, the hours a day over a pack's runtime, rounded
     up (types 2, 4 and 6 their runtime in the workbook; types 1, 3 and 5 the setting's runtime of 2025 times their
     battery energy density over that of 2025; a straight line between the workbook's years, the last value held after
     it). Each pack is charged once a day and replaced when its capacity falls below the draw's share: its life in
     charges, its charges to 80 % (spread among the packs) times (1 − the share) / 0.2, a straight-line fade (an
     approximation). A stock target, as the joint sets: the robots in use times the packs a robot needs. Where that
     need falls (longer runtimes), the packs in use stay until they wear out and the stock lies above the need.
     07's approximation in both: the joint sets and the packs of a retired robot go on in a new robot until they wear
     out, which makes their inflow and outflow slightly low.
  5. The elements: every flow and stock of robots, joint sets and packs of a type times one robot's kg of each element
     in 02's draw i: a robot its body (every kind of part but the joints and the battery pack), a joint set the joint
     kinds, a pack the kind Battery pack (02 builds one pack a robot). Sums on the raw draws, before any statistic.
  6. The years: the flows added up over the four quarters of a year, the stocks at 1 January of 2025 to 2040.
Each chunk of draws is checked (`check`): in every quarter the stock before + inflow − outflow = the stock, the outflow
counted cohort by cohort apart from the stock; no flow below 0; the robots in use at each 1 January the article's; the
six types adding up to all robots; the joint sets as many as the robots; the packs never fewer than the need. A fault
stops the run.

WHAT IT WRITES
--------------
Into `output.stock_and_flow_dir` (`data/stock_and_flow/`; not in git), the draws of every level ("keep the distribution
on all levels"), float32 (about 7 significant digits): units_in.npy and units_out.npy (draw × year 2025 to 2039 × robots, joint sets, battery packs
× robot type 1 to 6), units_stock.npy (draw × 1 January 2025 to 2040 × the same), elements_in.npy, elements_out.npy
(draw × year × robots' bodies, joint sets, battery packs × element, kg) and elements_stock.npy (draw × 1 January × the
same); their axes in draws.txt; summary.csv, each quantity's mean and 2.5 % and 97.5 % percentiles over the draws above
0 and the share of the draws above 0, by year. The elements of one robot type are its units times 02's draw i.
Into `output.stock_and_flow_figures_dir` (`figures/stock_and_flow/`; not in git), as 07's, each an A4 landscape page:
overview.png (the robots in use; built and retired; in use by robot type; the joint sets; the battery packs in use;
built and worn out) and elements/<Element>.png (its stock beside the world's reserves; its inflow and outflow beside
the world's mine production in 2025). Each line the mean over the draws above 0, its band 95 % of them; logarithmic
axes. An element 0 in every draw has no page, and 04 says so.

Where it sits: after 03_comparison.py; it reads 02's draws and nothing of 03.
"""

from __future__ import annotations

import csv
import importlib.util
import math
import os
import sys
import textwrap
from typing import NamedTuple

# Run from anywhere, and put the project root on the path, so that `src` imports. Must come before any import of src.
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import numpy as np  # noqa: E402
import openpyxl  # noqa: E402

from src.params_schema import Params, ParameterError, absolute, current  # noqa: E402


def load_comparison():
    """03_comparison.py as a module, for its reader of 02's tables (read_table), and through it 02 (`composition`:
    folder_name, ELEMENT_NAMES, plt) and 01 (`schemas`: read_workbook, KINDS, MARKS, text, number, numbered): one copy
    of the code. Loaded once."""
    path = os.path.join(HERE, '03_comparison.py')
    loaded = sys.modules.get('comparison')
    if loaded is not None and os.path.samefile(getattr(loaded, '__file__', path), path):
        return loaded
    spec = importlib.util.spec_from_file_location('comparison', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules['comparison'] = module
    spec.loader.exec_module(module)
    return module


comparison = load_comparison()
composition = comparison.composition
schemas = composition.schemas
plt = composition.plt
from matplotlib import ticker  # noqa: E402  (after 01, which sets matplotlib to draw into files only)

# ------------------------------------------------------------------------------------------------------
# The time, the parts of a robot, what it writes
# ------------------------------------------------------------------------------------------------------

FIRST, LAST = 2025, 2040          # the article's first and last 1 January; flows from 2025 to 2039
QUARTERS = 4 * (LAST - FIRST)     # 60: 2025 Q1 to 2039 Q4
DAYS_A_YEAR = 365.25              # days in a year, for the charges and operating hours of a year
FADE_TO_80 = 0.2                  # the capacity a pack loses until 80 %: 1 − 0.8
TYPES = (1, 2, 3, 4, 5, 6)        # the robot types, the workbook's categories
RESEARCH_TYPE = 1                 # its share the setting's triangles, not the workbook's
REMAINDER_TYPE = 3                # the largest type takes 1 minus the others (never normalised)
# The joint kinds: those 01 numbers on its robot (1 to 6; the other kinds have letters). The battery: its kind.
JOINT_KINDS = tuple(kind for kind, mark in schemas.MARKS.items() if mark.isdigit())
BATTERY_KIND = 'battery'
UNITS = ('robots', 'joint sets', 'battery packs')     # the three stocks of every robot type
PARTS = ("robots' bodies", 'joint sets', 'battery packs')   # what of a robot each unit carries, in the element files
# The workbook's sheets and rows, as his workbook writes them.
SHARES_SHEET, SHARES_HEADING = 'Market Units & Shares 2025-2040', '2025 Share (%)'
TRAJECTORIES_SHEET = 'Material Trajectories 2025-2040'
RUNTIME_ROW, DENSITY_ROW = 'Runtime (hours)', 'Battery Energy Density (Wh/kg)'
WORKBOOK_YEARS = (2025, 2030, 2035, 2040)
# What it writes, by exact name.
UNIT_FILES = ('units_in', 'units_stock', 'units_out')
ELEMENT_FILES = ('elements_in', 'elements_stock', 'elements_out')
FLOWS = ('in', 'stock', 'out')
SUMMARY, AXES_FILE = 'summary.csv', 'draws.txt'
OVERVIEW, ELEMENTS_DIR = 'overview.png', 'elements'
CHUNK = 20000                     # draws counted at once (memory: 1.4 GB at most, measured 2026-11-06)
TOLERANCE = 1e-9                  # of the largest stock: a balance that misses by more is a fault (07's check_balance)

# The world's production and reserves of magnesium, titanium and indium, which RAWCLICDataCenters' sheet
# ElementReference does not hold, from USGS's data file: for each, its commodity, its statistic, the share of the
# element in what USGS counts and what the figure's foot says of it. Magnesium's reserves are magnesite (MgCO3, gross
# weight), its magnesium by the formula, 24.305 / 84.313; titanium's are ilmenite and rutile as titanium dioxide (TiO2
# content), its titanium by the formula, 47.867 / 79.866; both estimates (E). Magnesium's production is the smelters'
# metal, titanium's the sponge metal; indium's the refineries' (USGS gives no mine production and no reserves of it).
USGS_ROWS = {
    'Mg': {'production': ('Magnesium Metal', 'Smelter production: rounded', 1.0, 'magnesium metal from smelters'),
           'reserves': ('Magnesium Compounds', 'Reserves: rounded', 24.305 / 84.313,
                        'magnesite (gross weight) x 28.8 % magnesium by its formula, an estimate')},
    'Ti': {'production': ('Titanium Sponge Metal', 'Titanium sponge metal production: rounded', 1.0,
                          'titanium sponge metal'),
           'reserves': ('Titanium Mineral Concentrates', 'Reserves: ilmenite and rutile, rounded', 47.867 / 79.866,
                        'ilmenite and rutile (TiO2 content) x 59.9 % titanium by its formula, an estimate')},
    'In': {'production': ('Indium', 'Refinery production: rounded', 1.0, 'refined indium; USGS gives no reserves')},
}
USGS_UNITS = {'metric tons': 1e3, 'thousand metric tons': 1e6}      # kg in USGS's unit
USGS_PLAIN = 'USGS MCS 2026'      # a note of sheet ElementReference that adds nothing to the source named at the foot


# ------------------------------------------------------------------------------------------------------
# A triangle: the lifetimes spread among the units, a draw's point
# ------------------------------------------------------------------------------------------------------

def triangle_cdf(x, low: float, mode: float, high: float):
    """The share of a triangle (min, mode, max) below x: of the units of one quarter, the share whose lifetime is
    shorter than x (as 07's triangle_cdf)."""
    x = np.asarray(x, dtype=float)
    with np.errstate(divide='ignore', invalid='ignore'):
        rising = (x - low) ** 2 / ((high - low) * (mode - low)) if mode > low else np.ones_like(x)
        falling = 1 - (high - x) ** 2 / ((high - low) * (high - mode)) if high > mode else np.ones_like(x)
    return np.where(x <= low, 0.0, np.where(x >= high, 1.0, np.where(x <= mode, rising, falling)))


def survival(age, triangle: tuple):
    """The share of one quarter's units still in use at `age` (in the triangle's unit): 1 − triangle_cdf."""
    return 1.0 - triangle_cdf(age, *triangle)


def triangle_ppf(u, low: float, mode: float, high: float):
    """The value of a triangle (min, mode, max) at the share u of it: a draw's value from its one random number."""
    u = np.asarray(u, dtype=float)
    cut = (mode - low) / (high - low)
    return np.where(u < cut, low + np.sqrt(u * (high - low) * (mode - low)),
                    high - np.sqrt((1 - u) * (high - low) * (high - mode)))


def joint_survival(age, hours_a_day: float, life_hours: tuple):
    """The share of one quarter's joint sets still in use at `age` (years): their operating hours, the hours a day for
    every day of their age, against their life in hours spread among the sets (step 3)."""
    return survival(np.asarray(age, dtype=float) * hours_a_day * DAYS_A_YEAR, life_hours)


def pack_survival(age, threshold, cycles_to_80: tuple):
    """The share of one quarter's battery packs still in use at `age` (years), one row a draw of `threshold` (the
    capacity below which a pack is replaced): a pack charged once a day leaves when its charges reach its charges to
    80 % × (1 − threshold) / 0.2 (a straight-line fade), so it survives while its charges to 80 %, spread among the
    packs, exceed its charges × 0.2 / (1 − threshold) (step 4)."""
    age, threshold = np.asarray(age, dtype=float), np.atleast_1d(np.asarray(threshold, dtype=float))
    return survival(age[None, :] * DAYS_A_YEAR * FADE_TO_80 / (1 - threshold[:, None]), cycles_to_80)


# ------------------------------------------------------------------------------------------------------
# Step 1: the quarters, the cohorts
# ------------------------------------------------------------------------------------------------------

def targets(robots: dict) -> np.ndarray:
    """The robots in use at the end of each quarter, 2025 Q1 to 2039 Q4: the article's 1 January values, geometric
    between (as 07): V(y)^(1 − k/4) × V(y + 1)^(k/4) at the end of quarter k of year y; the end of Q4 is the article's
    next 1 January."""
    out = np.empty(QUARTERS)
    for q in range(QUARTERS):
        year, k = FIRST + q // 4, q % 4 + 1
        out[q] = robots[year] ** (1 - k / 4) * robots[year + 1] ** (k / 4)
    return out


def ages(span: int) -> np.ndarray:
    """The age, years, at the end of a quarter, of the units that arrived in the middle of the quarter k quarters
    before (k = 0 its own quarter): (k + 0.5) / 4, for k = 0 … span − 1."""
    return (np.arange(span) + 0.5) / 4


class Flows(NamedTuple):
    """One stock, quarter by quarter, in every draw of a chunk (n draws)."""
    past: np.ndarray     # n × the quarters before 2025: what arrived in each, oldest first
    start: np.ndarray    # n: in use at 1 January 2025
    built: np.ndarray    # n × QUARTERS: the inflow
    stock: np.ndarray    # n × QUARTERS: in use at the end of the quarter
    gone: np.ndarray     # n × QUARTERS: the outflow


def cohorts(survive: np.ndarray, start, growth: float, target=None, inflow=None, past=None) -> Flows:
    """One stock, quarter by quarter, as 07's follow_target. `survive` (one row for all draws, or n rows, one a draw):
    the share of a quarter's units still in use at the end of the quarter k quarters later (column k, ages()). Its
    units of 1 January 2025 (`start`, n or one number) arrived in the quarters before, as many as hold `start` with
    their survivals, the arrivals growing by `growth` a year (or `past`, given: n × the quarters before, oldest first).
    Either `target` (n × QUARTERS, the stock at the end of each quarter: the inflow its shortfall, never below 0) or
    `inflow` (n × QUARTERS) is given. The outflow is counted cohort by cohort (what each quarter's units lose in the
    quarter), apart from the stock, so that check() can compare them."""
    survive = np.atleast_2d(np.asarray(survive, dtype=float))
    rows, span = survive.shape
    before = span - QUARTERS
    n = (target if target is not None else inflow).shape[0]
    start = np.broadcast_to(np.asarray(start, dtype=float), (n,)).astype(float)
    if past is None:
        # The quarters before 2025 Q1, oldest first: p quarters before (p = before … 1), the arrivals ∝ growth^(their
        # time); at 1 January 2025 such a quarter's units are survive[:, p − 1] (k = p − 1 quarters after their own).
        p = np.arange(before, 0, -1)
        weights = growth ** (-(p - 0.5) / 4)
        per_unit = (weights * survive[:, p - 1]).sum(axis=1)
        past = start[:, None] * weights[None, :] / per_unit[:, None]
    past = np.broadcast_to(np.asarray(past, dtype=float), (n, before))
    history = np.concatenate([past, np.zeros((n, QUARTERS))], axis=1)     # every quarter's arrivals, oldest first
    built, stock, gone = (np.empty((n, QUARTERS)) for _ in range(3))
    own = survive[:, 0]                                                   # a quarter's units at its own end
    for q in range(QUARTERS):
        now = before + q
        k = now - np.arange(now)              # the earlier quarters 0 … now − 1, k quarters after their own
        if rows == 1:
            held = history[:, :now] @ survive[0, k]
            lost = history[:, :now] @ (survive[0, k - 1] - survive[0, k])
        else:
            held = (history[:, :now] * survive[:, k]).sum(axis=1)
            lost = (history[:, :now] * (survive[:, k - 1] - survive[:, k])).sum(axis=1)
        new = inflow[:, q] if target is None else np.maximum(0.0, (target[:, q] - held) / own)
        history[:, now] = new
        built[:, q] = new
        stock[:, q] = held + new * own
        gone[:, q] = lost + new * (1 - own)
    return Flows(np.array(past), start, built, stock, gone)


# ------------------------------------------------------------------------------------------------------
# Steps 2 and 4: his workbook, the robot types' shares, runtimes and packs
# ------------------------------------------------------------------------------------------------------

def workbook_rows(params: Params) -> tuple:
    """From his workbook: each robot type's shares of the robots shipped in WORKBOOK_YEARS (the first table of sheet
    SHARES_SHEET) and its row of runtime or of battery energy density (sheet TRAJECTORIES_SHEET):
    ({type: (share, …)}, {type: (row name, (value or None, …))}). Raises ValueError, naming what it misses."""
    book = openpyxl.load_workbook(absolute(params.data.workbook), read_only=True, data_only=True)
    rows = list(book[SHARES_SHEET].iter_rows(values_only=True))
    head = next((k for k, r in enumerate(rows) if any(schemas.text(c) == SHARES_HEADING for c in r)), None)
    shares = {}
    if head is not None:
        at = [schemas.text(c) for c in rows[head]].index(SHARES_HEADING)
        for row in rows[head + 1:]:
            found = schemas.numbered(row[0])
            if not found:
                break                         # the table's total row ends it
            shares[found[0]] = tuple(schemas.number(row[at + k]) for k in range(len(WORKBOOK_YEARS)))
    trajectories = {}
    for row in book[TRAJECTORIES_SHEET].iter_rows(values_only=True):
        found = schemas.numbered(row[0]) if row else None
        name = schemas.text(row[2]) if found and len(row) > 2 else ''
        if name in (RUNTIME_ROW, DENSITY_ROW):
            trajectories[found[0]] = (name, tuple(schemas.number(v) for v in row[3:3 + len(WORKBOOK_YEARS)]))
    book.close()
    missing = [t for t in TYPES if t not in shares or None in shares[t] or t not in trajectories
               or trajectories[t][1][0] is None]
    if missing:
        raise ValueError(f'{params.data.workbook}: robot type(s) {missing} have no share in each year of '
                         f'{WORKBOOK_YEARS} (sheet {SHARES_SHEET!r}) or no runtime or battery energy density of '
                         f'{FIRST} (sheet {TRAJECTORIES_SHEET!r}).')
    return shares, trajectories


def along(times: np.ndarray, values: tuple) -> np.ndarray:
    """A straight line through the workbook's years and values at `times`, held before its first year and after its
    last value (a value None, '—' in the workbook, is left out: the one before it held)."""
    known = [(y, v) for y, v in zip(WORKBOOK_YEARS, values) if v is not None]
    return np.interp(times, [y for y, _ in known], [v for _, v in known])


def mid_times() -> np.ndarray:
    """The middle of each quarter, 2025 Q1 to 2039 Q4, in years: when its robots arrive."""
    return FIRST + (np.arange(QUARTERS) + 0.5) / 4


def end_times() -> np.ndarray:
    """The end of each quarter, 2025 Q1 to 2039 Q4, in years: when its stock is counted."""
    return FIRST + (np.arange(QUARTERS) + 1.0) / 4


def type_shares(params: Params, shares: dict, u: np.ndarray, times: np.ndarray) -> np.ndarray:
    """Each robot type's share of the robots built at `times` in every draw (n × times × 6): type 1 the draw's point
    `u` of its triangles of 2025 and 2040, a straight line between; types 2, 4, 5 and 6 the workbook's; type 3 the
    remainder. Raises ValueError where the remainder falls below 0."""
    flow = params.stock_and_flow
    first = triangle_ppf(u, *flow.research_share_2025)
    last = triangle_ppf(u, *flow.research_share_2040)
    along_time = np.clip((times - FIRST) / (LAST - FIRST), 0, 1)
    out = np.zeros((u.size, times.size, len(TYPES)))
    out[:, :, TYPES.index(RESEARCH_TYPE)] = first[:, None] + (last - first)[:, None] * along_time[None, :]
    for k, t in enumerate(TYPES):
        if t not in (RESEARCH_TYPE, REMAINDER_TYPE):
            out[:, :, k] = along(times, shares[t])[None, :]
    rest = TYPES.index(REMAINDER_TYPE)
    out[:, :, rest] = 1 - out.sum(axis=2)
    if (out[:, :, rest] < 0).any():
        raise ValueError(f'robot type {REMAINDER_TYPE}, the remainder of the shares, falls below 0: the shares of the '
                         'other types add up to more than 1.')
    return out


def runtimes(params: Params, trajectories: dict, times: np.ndarray) -> np.ndarray:
    """A pack's runtime, hours, of each robot type at `times` (6 × times): the workbook's runtime where its row gives
    one (types 2, 4, 6); else the setting's runtime of 2025 times the workbook's energy density over its 2025's."""
    given = dict(params.stock_and_flow.runtime_2025_hours)
    out = np.empty((len(TYPES), times.size))
    for k, t in enumerate(TYPES):
        name, values = trajectories[t]
        out[k] = along(times, values) if name == RUNTIME_ROW else given[t] * along(times, values) / values[0]
    return out


def packs_per_robot(params: Params, trajectories: dict, times: np.ndarray) -> np.ndarray:
    """The packs a robot of each type holds at `times` (6 × times): one day's work over a pack's runtime, rounded up
    (Matthias: "at least so many battery packs ready for use as it is needed to have them for 1 day to switch")."""
    return np.ceil(params.stock_and_flow.hours_a_day / runtimes(params, trajectories, times) - 1e-9)


# ------------------------------------------------------------------------------------------------------
# Step 5: 02's draws, one robot of each type by its parts
# ------------------------------------------------------------------------------------------------------

def robot_parts(params: Params) -> tuple:
    """From 02's draws, for each robot type, one robot's kg of each element in each draw, by what each unit carries:
    ({type: n × PARTS × elements}, the elements, {type: its name}). Raises FileNotFoundError where 02 has not written a
    table; ValueError where the types' draws or elements differ or a column is no kind and element."""
    book = schemas.read_workbook(absolute(params.data.workbook), params)
    kinds = {name: kind for kind, (name, _) in schemas.KINDS.items()}
    out, names, elements, draws = {}, {}, None, None
    for category in book.categories:
        folder = composition.folder_name(category)
        with open(os.path.join(absolute(params.output.composition_dir), folder, 'elements.txt'),
                  encoding='utf-8') as handle:
            symbols = handle.read().splitlines()
        columns, values = comparison.read_table(os.path.join(absolute(params.output.parts_dir), folder), 'elements')
        if elements is None:
            elements, draws = symbols, values.shape[0]
        if symbols != elements or values.shape[0] != draws:
            raise ValueError(f'robot type {category.number}: its draws ({values.shape[0]}) or elements differ from '
                             f"robot type {book.categories[0].number}'s; run 02 for all six types.")
        carried = np.zeros((draws, len(PARTS), len(elements)))
        for c, column in enumerate(columns):
            name, _, symbol = column.rpartition(': ')
            kind = kinds.get(name)
            if kind is None or symbol not in elements:
                raise ValueError(f'robot type {category.number}: the column {column!r} of 02 is no kind and element.')
            part = 1 if kind in JOINT_KINDS else 2 if kind == BATTERY_KIND else 0
            carried[:, part, elements.index(symbol)] += values[:, c]
        out[category.number], names[category.number] = carried, category.name
    if sorted(out) != list(TYPES):
        raise ValueError(f'the workbook holds robot types {sorted(out)}, not {list(TYPES)}.')
    return out, elements, names


# ------------------------------------------------------------------------------------------------------
# Steps 1 to 4 in every draw of a chunk
# ------------------------------------------------------------------------------------------------------

def count(params: Params, shares: dict, trajectories: dict, u: np.ndarray, threshold: np.ndarray) -> tuple:
    """The robots, joint sets and packs of each type, quarter by quarter, in the draws of `u` (the research share's
    point) and `threshold` (the capacity below which a pack is replaced): ({(unit, type): Flows}, with all robots
    under ('robots', 0); {type: the packs needed, n × QUARTERS})."""
    flow = params.stock_and_flow
    robots = {year: float(v) for year, v in flow.robots}
    growth = robots[FIRST + 1] / robots[FIRST]
    n = u.size
    # The quarters before 2025 that can still hold a unit: the longest life of a robot, a joint set or a pack.
    longest = max(flow.robot_lifetime_years[2], flow.joint_life_hours[2] / (flow.hours_a_day * DAYS_A_YEAR),
                  flow.battery_cycles_to_80[2] * (1 - flow.battery_replaced_below[0]) / FADE_TO_80 / DAYS_A_YEAR)
    before = int(math.ceil(4 * longest)) + 1
    age = ages(before + QUARTERS)
    robot_survive = survival(age, flow.robot_lifetime_years)
    joint_survive = joint_survival(age, flow.hours_a_day, flow.joint_life_hours)
    pack_survive = pack_survival(age, threshold, flow.battery_cycles_to_80)          # one row a draw
    counted, needs = {}, {}
    total = cohorts(robot_survive, robots[FIRST], growth, target=np.broadcast_to(targets(robots), (n, QUARTERS)))
    counted[('robots', 0)] = total
    built_shares = type_shares(params, shares, u, mid_times())                       # n × QUARTERS × 6
    start_shares = type_shares(params, shares, u, np.array([float(FIRST)]))[:, 0, :]  # n × 6
    packs = packs_per_robot(params, trajectories, end_times())                        # 6 × QUARTERS
    first_packs = packs_per_robot(params, trajectories, np.array([float(FIRST)]))[:, 0]
    for k, t in enumerate(TYPES):
        start = robots[FIRST] * start_shares[:, k]
        robots_t = cohorts(robot_survive, start, growth, inflow=total.built * built_shares[:, :, k],
                           past=total.past * start_shares[:, k:k + 1])
        counted[('robots', t)] = robots_t
        counted[('joint sets', t)] = cohorts(joint_survive, start, growth, target=robots_t.stock)
        needs[t] = robots_t.stock * packs[k][None, :]
        counted[('battery packs', t)] = cohorts(pack_survive, start * first_packs[k], growth, target=needs[t])
    return counted, needs


def check(params: Params, counted: dict, needs: dict) -> list:
    """The faults of one chunk, in plain words ([] where none): a quarter whose stock before + inflow − outflow is not
    its stock (the outflow counted apart, cohort by cohort), a flow below 0, the robots in use at a 1 January not the
    article's, the types not adding up to all robots, joint sets not as many as the robots, packs fewer than needed.
    Each to TOLERANCE of the largest stock (07's check_balance)."""
    faults = []
    robots = {year: float(v) for year, v in params.stock_and_flow.robots}
    for (unit, t), f in counted.items():
        what = f'{unit} of robot type {t}' if t else 'all robots'
        scale = max(float(np.abs(f.stock).max()), 1.0)
        before = np.concatenate([f.start[:, None], f.stock[:, :-1]], axis=1)
        gap = np.abs(before + f.built - f.gone - f.stock).max()
        if gap > TOLERANCE * scale:
            faults.append(f'{what}: the stock before + inflow − outflow is not the stock (largest gap {gap:.3g} of a '
                          f'stock up to {scale:.3g}).')
        if (f.built < 0).any() or (f.gone < -TOLERANCE * scale).any():
            faults.append(f'{what}: a flow below 0.')
    total = counted[('robots', 0)]
    at_january = np.concatenate([total.start[:, None], total.stock[:, 3::4]], axis=1)
    for y, year in enumerate(range(FIRST, LAST + 1)):
        if np.abs(at_january[:, y] - robots[year]).max() > TOLERANCE * robots[year]:
            faults.append(f"the robots in use at 1 January {year} are not the article's {robots[year]:,.0f}.")
    scale = float(total.stock.max())
    if np.abs(sum(counted[('robots', t)].stock for t in TYPES) - total.stock).max() > TOLERANCE * scale:
        faults.append('the robots of the six types do not add up to all robots.')
    for t in TYPES:
        if np.abs(counted[('joint sets', t)].stock - counted[('robots', t)].stock).max() > TOLERANCE * scale:
            faults.append(f'robot type {t}: the joint sets in use are not as many as its robots in use.')
        if (counted[('battery packs', t)].stock < needs[t] - TOLERANCE * max(float(needs[t].max()), 1.0)).any():
            faults.append(f'robot type {t}: fewer battery packs in use than its robots need.')
    return faults


def years_of(f: Flows) -> tuple:
    """A stock by year: (inflow n × 15 years 2025 to 2039, stock n × 16 at 1 January 2025 to 2040, outflow n × 15),
    the order of FLOWS."""
    n = f.built.shape[0]
    return (f.built.reshape(n, -1, 4).sum(axis=2), np.concatenate([f.start[:, None], f.stock[:, 3::4]], axis=1),
            f.gone.reshape(n, -1, 4).sum(axis=2))


# ------------------------------------------------------------------------------------------------------
# The world's production and reserves (the figures' dashed lines)
# ------------------------------------------------------------------------------------------------------

def references(params: Params) -> tuple:
    """The world's production in 2025 (kg a year) and reserves (kg) of each element: ({element: {'production' |
    'reserves': (min, mode, max, at least)}}, {element: [what the foot says of it]}): RAWCLICDataCenters' sheet
    ElementReference as 07 reads it (t in the sheet; its note where it adds to the source), and USGS_ROWS from USGS's
    data file. A file not on disk gives nothing, and the pages say so."""
    values, notes = {}, {}
    if os.path.exists(params.data.data_center_scenarios):
        book = openpyxl.load_workbook(params.data.data_center_scenarios, read_only=True, data_only=True)
        rows = list(book['ElementReference'].iter_rows(values_only=True))
        book.close()
        head = [schemas.text(c) for c in rows[0]]
        for row in rows[1:]:
            cell = dict(zip(head, row))
            element, quantity = schemas.text(cell.get('Element')), schemas.text(cell.get('Quantity'))
            if not element or schemas.text(cell.get('Unit')) != 't':
                continue
            low, mode, high = (schemas.number(cell.get(k)) * 1e3 for k in ('Min', 'Mode', 'Max'))
            values.setdefault(element, {})[quantity] = (low, mode, high,
                                                        schemas.text(cell.get('AtLeast')).lower() == 'yes')
            note = schemas.text(cell.get('Note'))
            if note and note != USGS_PLAIN:
                notes.setdefault(element, []).append(f'{quantity}: {note}')
    if os.path.exists(params.data.usgs_commodities):
        with open(params.data.usgs_commodities, encoding='utf-8', errors='replace') as handle:
            rows = list(csv.reader(handle))
        for element, wanted in USGS_ROWS.items():
            for quantity, (commodity, detail, share, words) in wanted.items():
                for row in rows[1:]:
                    if (len(row) > 8 and row[2] == commodity and row[3] == 'World total' and row[5] == detail
                            and row[7] == str(FIRST) and row[6] in USGS_UNITS):
                        written = row[8].replace(',', '').strip()
                        kg = float(written.lstrip('>')) * USGS_UNITS[row[6]] * share
                        values.setdefault(element, {})[quantity] = (kg, kg, kg, written.startswith('>'))
                        notes.setdefault(element, []).append(f'{quantity}: {words}')
    return values, notes


# ------------------------------------------------------------------------------------------------------
# The summary: over the draws above 0 ("A 0 is not part of a distribution")
# ------------------------------------------------------------------------------------------------------

def stats_of(values: np.ndarray) -> dict:
    """Per column of `values` (draws × columns), over the draws above 0: the mean, the 2.5 % and 97.5 % percentiles,
    and the share of the draws above 0 ('held'); NaN where no draw is above 0."""
    out = {key: np.full(values.shape[1], np.nan) for key in ('mean', 'low', 'high')}
    out['held'] = np.zeros(values.shape[1])
    for c in range(values.shape[1]):
        above = values[:, c][values[:, c] > 0]
        if above.size:
            out['mean'][c] = above.mean()
            out['low'][c], out['high'][c] = np.percentile(above, (2.5, 97.5))
            out['held'][c] = above.size / values.shape[0]
    return out


def held_words(held: np.ndarray) -> str:
    """'' where a quantity is above 0 in every draw of every year it is held; else ', held in 56 % of the draws' (or
    '56 % to 100 %'), its share over the years it is held, rounded down so that 100 % means every draw."""
    shares = held[held > 0]
    if not shares.size or shares.min() >= 1:
        return ''
    low, high = math.floor(100 * shares.min()), math.floor(100 * shares.max())
    return f', held in {low} % of the draws' if low == high else f', held in {low} % to {high} % of the draws'


# ------------------------------------------------------------------------------------------------------
# The figures, as 07's
# ------------------------------------------------------------------------------------------------------

# Every figure one landscape A4 page with 07's print fonts (Matthias, 2026-10-22, for 07: "I want that the figures look
# great on a landscpae A4 page").
A4_LANDSCAPE = (297 / 25.4, 210 / 25.4)                    # inches
PRINT_STYLE = {'font.size': 9, 'axes.titlesize': 11, 'axes.labelsize': 9, 'xtick.labelsize': 9, 'ytick.labelsize': 9,
               'legend.fontsize': 8, 'legend.title_fontsize': 8, 'figure.titlesize': 13, 'lines.linewidth': 1.4}
# Paul Tol's bright scheme (as published): in use blue, built green, out red; the six robot types its six colours.
IN_USE, BUILT, GONE = '#4477AA', '#228833', '#EE6677'
TYPE_COLOURS = ('#4477AA', '#66CCEE', '#228833', '#CCBB44', '#EE6677', '#AA3377')
WORLD_SOURCE = 'U.S. Geological Survey, Mineral Commodity Summaries 2026 (ver. 1.3)'
NOTE_WIDTH = 160                  # characters a line of a page's foot (07's save_figure)
# Where a panel's legend goes: the upper left, as 07's; where a line of the panel runs under it there, or a value
# written in the panel ("above the scale"), the next of these corners where none does (found 2026-11-06: indium's
# world production ran under the legend).
LEGEND_PLACES = ('upper left', 'lower right', 'upper right', 'lower left')


def decade_label(value: float, _position=None) -> str:
    """A tick of a log axis of numbers: the decade as 10 to its power (07's decade_label)."""
    return f'$10^{{{int(round(np.log10(value)))}}}$'


def mass_label(value_kg: float, _position=None) -> str:
    """A tick of a log axis of kg: the power of ten in the unit that writes it as 1, 10 or 100 ('1 kt', '100 t'), as
    07 and RAWCLICDataCenters' 03 write them (kg, not Mg)."""
    power = int(round(np.log10(value_kg)))
    for base, unit in ((9, 'Mt'), (6, 'kt'), (3, 't'), (0, 'kg'), (-3, 'g')):
        if power >= base:
            return f'{10 ** (power - base):,} {unit}'
    return f'{10.0 ** (power + 3):g} g'


def mass_text(value_kg: float) -> str:
    """A mass written in a figure: three significant digits in the unit that writes it from 1 up ('980 Mt', '55 kt',
    '190 t'; Mt the largest; "4000 not 4k"), as 07's mass_text."""
    for factor, unit in ((1e9, 'Mt'), (1e6, 'kt'), (1e3, 't'), (1.0, 'kg'), (1e-3, 'g')):
        if value_kg >= factor or unit == 'g':
            v = float(f'{value_kg / factor:.3g}')
            return f'{v:,.0f} {unit}' if v >= 100 else f'{v:g} {unit}'
    return ''


def log_panel(axes, series: list, word: str, tick_label=decade_label) -> bool:
    """One panel on a log axis, as 07's log_panel: each of `series` (years, stats of stats_of, label, colour) its mean
    a line and 95 % of its draws above 0 a band, `word` the axis label; a year with no draw above 0 has no point. The
    label says the share of the draws that hold it where not all do. A panel with nothing above 0 is not drawn.
    Returns whether it was drawn."""
    values = np.concatenate([np.concatenate([s[1]['mean'], s[1]['low']]) for s in series])
    positive = values[np.isfinite(values) & (values > 0)]
    if not positive.size:
        axes.set_visible(False)
        return False
    foot = float(positive.min()) / 2.0
    for years, stats, label, colour in series:
        axes.plot(years, stats['mean'], '-', color=colour, label=label + held_words(stats['held']))
        axes.fill_between(years, stats['low'], stats['high'], where=np.isfinite(stats['mean']), alpha=0.2,
                          color=colour, linewidth=0)
    axes.set_xlim(FIRST, LAST)
    axes.set_xticks(range(FIRST, LAST + 1, 5))
    axes.set_yscale('log')
    axes.set_ylim(bottom=foot)
    axes.yaxis.set_major_locator(ticker.LogLocator(base=10))
    axes.yaxis.set_major_formatter(ticker.FuncFormatter(tick_label))
    axes.yaxis.set_minor_formatter(ticker.NullFormatter())
    axes.set_ylabel(word)
    return True


def held_in_label(axes) -> bool:
    """Whether a label of the panel says the share of the draws that hold it: then the panel has a legend, also with
    one line ("one colour, no legend" otherwise), so that the share is written beside it."""
    return any('held in' in label for label in axes.get_legend_handles_labels()[1])


def world_reference(axes, value: tuple | None, name: str, per_year: bool) -> None:
    """The world's production (kg a year) or reserves (kg) in a panel drawn by log_panel, as 07's world_reference:
    within the panel's scale a black dashed line (its min to max, where they differ, a grey band), the axis unchanged;
    outside it the value written in the panel, at its top where above the scale, at its foot where below."""
    if value is None or not axes.get_visible():
        return
    low, mode, high, at_least = value
    bottom, top = axes.get_ylim()
    text = mass_text(mode) if low == high else f'{mass_text(low)} to {mass_text(high)}'
    text = f"{name}: {'at least ' if at_least else ''}{text}{' per year' if per_year else ''}"
    if bottom <= mode <= top:
        left, right = axes.get_xlim()
        axes.plot([left, right], [mode, mode], 'k--', linewidth=1.2, label=name)
        if high > low:
            axes.fill_between([left, right], max(low, bottom), min(high, top), color='0.5', alpha=0.15, linewidth=0)
        axes.set_xlim(left, right)
        axes.set_ylim(bottom, top)
        return
    above = mode > top
    axes.text(0.98, 0.97 if above else 0.03, f"{text}, {'above' if above else 'below'} the scale",
              transform=axes.transAxes, ha='right', va='top' if above else 'bottom', fontsize=8, color='0.2')


def figure_note(draws: int) -> str:
    """The words at the foot of every page: what its lines and bands are, the axes, where the robots come from."""
    return (f'Lines: the mean of the draws above 0 of {draws:,} draws; bands: 95 % of them (2.5 % to 97.5 %); flows '
            'per year, stocks at 1 January; logarithmic axes. Robots in use at 1 January: ai-2040.com Plan A; each '
            "robot one of 02's draws of its robot type.")


def lines_under(axes, box, renderer=None) -> bool:
    """Whether a line of the panel (a mean or a dashed world value) runs under the box (in the page's pixels): its
    points and the points between them, 50 to a segment; with `renderer`, also whether a text written in the panel
    overlaps it."""
    if renderer is not None and any(text.get_visible() and text.get_window_extent(renderer).overlaps(box)
                                    for text in axes.texts):
        return True
    for line in axes.get_lines():
        xy = line.get_xydata()
        xy = xy[np.isfinite(xy).all(axis=1)]
        if len(xy) == 0:
            continue
        if len(xy) > 1:
            steps = np.linspace(0, 1, 50)[:, None, None]
            xy = (xy[:-1][None] * (1 - steps) + xy[1:][None] * steps).reshape(-1, 2)
        points = axes.transData.transform(xy)
        inside = ((points[:, 0] >= box.x0) & (points[:, 0] <= box.x1) & (points[:, 1] >= box.y0)
                  & (points[:, 1] <= box.y1))
        if inside.any():
            return True
    return False


def place_legends(figure) -> None:
    """Each panel's legend in the first of LEGEND_PLACES where no line runs under it (else matplotlib's 'best'), the
    page laid out as it is saved."""
    figure.canvas.draw()
    renderer = figure.canvas.get_renderer()
    for axes in figure.axes:
        if axes.get_legend() is None:
            continue
        for place in LEGEND_PLACES:
            legend = axes.legend(loc=place)
            if not lines_under(axes, legend.get_window_extent(renderer), renderer):
                break
        else:
            axes.legend(loc='best')


def save_figure(figure, path: str, note: str, dpi: int) -> str:
    """Write a page with its note at the foot, wrapped within the page's width, and close it (07's save_figure); each
    legend where no line runs under it (place_legends)."""
    lines = textwrap.wrap(note, NOTE_WIDTH)
    figure.text(0.5, 0.008, '\n'.join(lines), ha='center', va='bottom', fontsize=8)
    figure.tight_layout(rect=(0, 0.012 + 0.02 * len(lines), 1, 1))
    place_legends(figure)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    figure.savefig(path, dpi=dpi, facecolor='white')
    plt.close(figure)
    return path


def overview_page(summary: dict, names: dict, draws: int, path: str, dpi: int) -> str:
    """The overview: the robots in use; built and retired; in use by robot type; the joint sets; the battery packs in
    use; built and worn out."""
    flows, stocks = np.arange(FIRST, LAST), np.arange(FIRST, LAST + 1)

    def line(unit, t, flow, label, colour):
        return (stocks if flow == 'stock' else flows, summary[(unit, t, flow)], label, colour)

    panels = (
        ('Robots in use', [line('robots', 0, 'stock', 'in use', IN_USE)], 'robots'),
        ('Robots built and retired', [line('robots', 0, 'in', 'built', BUILT),
                                      line('robots', 0, 'out', 'retired', GONE)], 'robots per year'),
        ('Robots in use by robot type', [line('robots', t, 'stock', f'robot type {t}', TYPE_COLOURS[k])
                                         for k, t in enumerate(TYPES)], 'robots'),
        ('Joint sets', [line('joint sets', 0, 'stock', 'in use', IN_USE),
                        line('joint sets', 0, 'in', 'built per year', BUILT),
                        line('joint sets', 0, 'out', 'worn out per year', GONE)], 'joint sets'),
        ('Battery packs in use', [line('battery packs', 0, 'stock', 'in use', IN_USE)], 'battery packs'),
        ('Battery packs built and worn out', [line('battery packs', 0, 'in', 'built', BUILT),
                                              line('battery packs', 0, 'out', 'worn out', GONE)],
         'battery packs per year'))
    figure, grid = plt.subplots(2, 3, figsize=A4_LANDSCAPE)
    for axes, (title, series, word) in zip(grid.flat, panels):
        if log_panel(axes, series, word):
            axes.set_title(title)
            if len(series) > 1 or held_in_label(axes):
                axes.legend(loc='upper left')
    figure.suptitle('Humanoid robots in the world')
    types = '; '.join(f'{t} {names[t]}' for t in TYPES)
    note = (figure_note(draws) + ' A joint set: the hip, knee, ankle, waist, arm and head joints of one robot. '
            f'Robot types: {types}.')
    return save_figure(figure, path, note, dpi)


def element_page(symbol: str, summary: dict, world: dict, notes: list, draws: int, path: str, dpi: int) -> str:
    """One element: its stock beside the world's reserves; its inflow and outflow beside the world's mine production
    in 2025 (07's element figure, without "collected")."""
    flows, stocks = np.arange(FIRST, LAST), np.arange(FIRST, LAST + 1)
    figure, (left, right) = plt.subplots(1, 2, figsize=A4_LANDSCAPE)
    if log_panel(left, [(stocks, summary[('element', symbol, 'stock')], 'stock', IN_USE)], '', mass_label):
        left.set_title('Stock')
        world_reference(left, world.get('reserves'), 'World reserves', per_year=False)
        if any('World' in label for label in left.get_legend_handles_labels()[1]) or held_in_label(left):
            left.legend(loc='upper left')
    if log_panel(right, [(flows, summary[('element', symbol, 'in')], 'inflow', BUILT),
                         (flows, summary[('element', symbol, 'out')], 'outflow', GONE)], 'per year', mass_label):
        right.set_title('Inflow and outflow')
        world_reference(right, world.get('production'), 'World production 2025', per_year=True)
        right.legend(loc='upper left')
    figure.suptitle(composition.ELEMENT_NAMES.get(symbol, symbol))
    note = figure_note(draws) + " The robots' bodies, their joint sets and their battery packs."
    if world:
        note += (" Dashed: the world's mine production in 2025 (inflow) and reserves (stock), " + WORLD_SOURCE
                 + ('; ' + '; '.join(notes) if notes else '') + '; a value outside the scale is written in the panel.')
    else:
        note += ' No world production or reserves for it in the sources read.'
    return save_figure(figure, path, note, dpi)


def element_file(symbol: str) -> str:
    """The file name of an element's page: its name, as 07 writes it ('Copper.png')."""
    return f"{composition.ELEMENT_NAMES.get(symbol, symbol).replace(' ', '_')}.png"


# ------------------------------------------------------------------------------------------------------
# The run
# ------------------------------------------------------------------------------------------------------

def run(params: Params) -> int:
    """Count every draw, chunk by chunk, check it, write the draws, the summary and the pages. 0 when done; 1 when an
    input is missing or a check fails (then it stops, and says what is incomplete)."""
    flow = params.stock_and_flow
    try:
        parts, elements, names = robot_parts(params)
        shares, trajectories = workbook_rows(params)
    except (FileNotFoundError, ValueError, KeyError) as error:
        print(f'04 stopped: {error}')
        return 1
    draws = parts[TYPES[0]].shape[0]
    # One point of the research share's triangles and one capacity threshold a draw, the same in every rerun.
    rng = np.random.default_rng([params.composition.seed, 4])
    u = rng.random(draws)
    threshold = triangle_ppf(rng.random(draws), *flow.battery_replaced_below)
    folder = absolute(params.output.stock_and_flow_dir)
    os.makedirs(folder, exist_ok=True)
    years = {'in': LAST - FIRST, 'stock': LAST - FIRST + 1, 'out': LAST - FIRST}
    files = {}
    for unit_name, element_name, flow_name in zip(UNIT_FILES, ELEMENT_FILES, FLOWS):
        files[unit_name] = np.lib.format.open_memmap(os.path.join(folder, f'{unit_name}.npy'), mode='w+',
                                                     dtype=np.float32,
                                                     shape=(draws, years[flow_name], len(UNITS), len(TYPES)))
        files[element_name] = np.lib.format.open_memmap(os.path.join(folder, f'{element_name}.npy'), mode='w+',
                                                        dtype=np.float32,
                                                        shape=(draws, years[flow_name], len(PARTS), len(elements)))
    for first in range(0, draws, CHUNK):
        rows = slice(first, min(first + CHUNK, draws))
        try:
            counted, needs = count(params, shares, trajectories, u[rows], threshold[rows])
        except ValueError as error:
            print(f'04 stopped: {error}')
            return 1
        faults = check(params, counted, needs)
        if faults:
            print(f'04 stopped: the stock and flow of draws {first + 1:,} to {rows.stop:,} does not add up; the draws '
                  f'in {folder} are incomplete.')
            for fault in faults:
                print(f'  {fault}')
            return 1
        by_year = {(unit, t): years_of(counted[(unit, t)]) for unit in UNITS for t in TYPES}
        for j, unit in enumerate(UNITS):
            for i, (unit_name, element_name) in enumerate(zip(UNIT_FILES, ELEMENT_FILES)):
                kg = 0.0
                for k, t in enumerate(TYPES):
                    values = by_year[(unit, t)][i]
                    files[unit_name][rows, :, j, k] = values
                    # Step 5: this type's units times its robot's kg in draw i, added over the types.
                    kg = kg + values[:, :, None] * parts[t][rows, j][:, None, :]
                files[element_name][rows, :, j, :] = kg
        print(f'04: draws {first + 1:,} to {rows.stop:,} of {draws:,} counted and checked')
    for array in files.values():
        array.flush()
    with open(os.path.join(folder, AXES_FILE), 'w', encoding='utf-8') as handle:
        handle.write(f"{', '.join(UNIT_FILES)}: draw; year (in, out: {FIRST} to {LAST - 1}; stock: 1 January {FIRST} "
                     f"to {LAST}); unit ({', '.join(UNITS)}); robot type ({', '.join(map(str, TYPES))})\n")
        handle.write(f"{', '.join(ELEMENT_FILES)}: draw; year (the same); part ({', '.join(PARTS)}); element "
                     f"({', '.join(elements)}); kg\n")
    # The summary, over the draws above 0: every unit of all types and of each type; every element of all three parts.
    summary = {}
    for unit_name, flow_name in zip(UNIT_FILES, FLOWS):
        values = np.array(files[unit_name], dtype=np.float64)
        for j, unit in enumerate(UNITS):
            summary[(unit, 0, flow_name)] = stats_of(values[:, :, j, :].sum(axis=2))
            for k, t in enumerate(TYPES):
                summary[(unit, t, flow_name)] = stats_of(values[:, :, j, k])
    for element_name, flow_name in zip(ELEMENT_FILES, FLOWS):
        values = files[element_name].sum(axis=2, dtype=np.float64)              # draws × years × elements
        for e, symbol in enumerate(elements):
            summary[('element', symbol, flow_name)] = stats_of(values[:, :, e])
    with open(os.path.join(folder, SUMMARY), 'w', newline='', encoding='utf-8') as handle:
        writer = csv.writer(handle)
        writer.writerow(('quantity', 'robot type', 'flow', 'year', 'mean', '2.5 %', '97.5 %',
                         'held in % of the draws'))
        for (what, which, flow_name), stats in summary.items():
            quantity = composition.ELEMENT_NAMES.get(which, which) if what == 'element' else what
            robot_type = which if what != 'element' and which else 'all'
            for i in range(len(stats['mean'])):
                cells = [f'{stats[key][i]:.6g}' if np.isfinite(stats[key][i]) else '–'
                         for key in ('mean', 'low', 'high')]
                writer.writerow((quantity, robot_type, flow_name, FIRST + i, *cells, f"{100 * stats['held'][i]:.1f}"))
    # The pages.
    figures = absolute(params.output.stock_and_flow_figures_dir)
    world, notes = references(params)
    held = []
    with plt.rc_context(PRINT_STYLE):
        overview_page(summary, names, draws, os.path.join(figures, OVERVIEW), params.output.dpi)
        for symbol in elements:
            if not any(summary[('element', symbol, f)]['held'].max() > 0 for f in FLOWS):
                print(f'04: {composition.ELEMENT_NAMES.get(symbol, symbol)}: no numbers, 0 kg in every draw; no page.')
                continue
            held.append(symbol)
            element_page(symbol, summary, world.get(symbol, {}), notes.get(symbol, []), draws,
                         os.path.join(figures, ELEMENTS_DIR, element_file(symbol)), params.output.dpi)
    without = [composition.ELEMENT_NAMES.get(s, s) for s in held if s not in world]
    if without:
        print(f"04: no world production or reserves for {', '.join(without)}; their pages say so.")
    robots = [float(f'{v:.7g}') for v in summary[('robots', 0, 'stock')]['mean']]     # float32: 7 digits
    print(f'04 done: {draws:,} draws; robots in use 1 January {FIRST} {robots[0]:,.0f}, {LAST} {robots[-1]:,.0f}; '
          f'the overview and {len(held)} element pages in {figures}.')
    return 0


def main() -> int:
    """Press Run: the settings in force, then run()."""
    try:
        params = current()
    except ParameterError as error:
        print(error, file=sys.stderr)
        return 1
    return run(params)


if __name__ == '__main__':
    raise SystemExit(main())
