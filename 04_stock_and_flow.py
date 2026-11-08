"""
04_stock_and_flow.py
====================

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

The stock and flow of the humanoid robots in the world and of the critical and strategic elements in them, quarter by
quarter from 2025 Q1 to 2040 Q4, reported by calendar year with the stocks at the end of each year, exactly as
RAWCLICDataCenters' 07 follows the world's data centres, so that both can be combined (Matthias, 2026-11-08: "Both have
to be exactly the same, as we have to combine both data!!!", "Both have to be on the same x axis scale!!", "Yes!!"): the
robots in use as the article ai-2040.com Plan A states them, each value at the end of its year ("Follow the artcile!!
70 x 10E9"), 70 × 10⁹ at the end of 2040; each robot one unit with its lifetime; its
joints and its battery packs replaced on their own; every robot made as 02's draw i of its robot type. Press Run. No
arguments; every setting is in `src/params_schema.py` (section `stock_and_flow`). Run `02_composition.py` first.

Matthias, 2026-11-06: "Get the article, which was already the bases for the work on the stock and flow modeling of the
datacenters. Read it and use the stock numbers for the humanoid robots", "Do exactly what has been done for the
datacenter", "I want the same figures as for the datacenters, but expand them all the essential critcial and statigic
elements. Also have real lifetimes not something fixed like this. I want to see uncerttainites", "Add also the limit in
stock and production like for the data centers", to the table of this stage "Yes, build it"; then "No look at the robots
as a unit with exception of the batteries", "Have at least so many battery packs ready for use as it is needed to have
them for 1 day to switch. So they can recharge slowly", "Yes, replace joints"; 2026-11-07, on the robot types: "All have
a triangular distribution", "the last type is not just the rest to 100%", "Have them from 10% to 30%", "All types have
to have the same uncertainty!!!", "The summ of the total has to be correct", "Check all the privous code. You have do it
correct before!! It is an approximatoion", to RAWCLICRecoveryModel's conditioning "Conditioning", then "I want that you
developt an algorthym that has for all 6 types around 10% +- in 2025 and 30%+- in 2040", "NO type 3 is not
triangular!!" and to the rearrangement "Yes, build it"; on the lifetimes "I want that is is 30% short and 20% longer.
Also with the batteries" (documentation/claude/EVIDENCE.md E39 to E45).

WHAT IT READS
-------------
  - Its settings (`stock_and_flow`): the article's robots of 2025 to 2040 (10 M to 70 × 10⁹), each at the end of its year,
    and, before its first value, those of 1 January 2025, its 2025 less one year of its own growth (8.62 M); a robot's
    lifetime 5 / 7 / 10 years and the factor of a draw on it, on the joints' life and on the packs' charges, each its
    own, 0.7 / 1 / 1.2; the hours a day, 24 (the article: robots "can work 24/7"); a joint's life 7,000 /
    10,000 / 30,000 hours; a battery pack's charges until 80 % of its capacity, 500 / 800 / 1,000, and the capacity
    below which it is replaced, 75 / 80 / 85 % (one value a draw); the runtime in 2025 of robot types 1, 3 and 5; the
    mode of the share of research robots (type 1) among the robots built, 10 % in 2025 and 5 % in 2040; how far the
    share of each type lies from its mode in 95 % of the draws, 10 % of it in 2025 and 30 % in 2040.
  - His workbook (`data.workbook`): the shares of robot types 2 to 6 among the robots shipped (sheet Market Units &
    Shares 2025-2040, its first table; type 1's share there is not used) and the runtime or the battery energy density
    of each type (sheet Material Trajectories 2025-2040).
  - 02's draws of each robot type: the kg of each element of interest in one robot, by kind of part
    (`output.parts_dir`, table 'elements', columns '<kind>: <element>'), its elements in the order of 02's table
    (`output.composition_dir`, 'elements.txt'). All six types with as many draws; draw i of each type is a robot of
    draw i.
  - The world's mine production in 2025 and reserves of each element, for the figures: RAWCLICDataCenters' sheet
    ElementReference (`data.data_center_scenarios`, the values 07 draws), and USGS's data file (`data.usgs_commodities`)
    for magnesium, titanium and indium, which that sheet does not hold; both read where they lie.

HOW IT COUNTS (every draw; quarter by quarter, as 07)
-------------
  1. The robots: in use at the end of each quarter, the article's values at the end of their years, the quarters
     between geometric
     (V(y)^(1 − k/4) × V(y + 1)^(k/4), as 07). Each quarter's robots arrive in its middle and leave by the share of
     them whose lifetime (the triangle 5 / 7 / 10 years, spread among them, times the draw's factor from the triangle
     0.7 / 1 / 1.2: "30% short and 20% longer") is shorter than their age; a quarter's
     inflow is the target less what the earlier quarters' robots still hold, never below 0. The robots of 1 January
     2025 by their ages: built in the quarters before at the article's own growth (its 2026 over its 2025), as many as
     it takes to hold the 10 M with their survivals (an estimate, E42).
  2. The robot types (Matthias, 2026-11-07: "I want that you developt an algorthym that has for all 6 types around 10% +-
     in 2025 and 30%+- in 2040. All have to have close to this value!!", "NO type 3 is not triangular!!", to the
     rearrangement "Yes, build it"). Every type's share of the robots built has its own triangle, mode × (1 ∓ end), the
     end the spread over 0.7764, so that 95 % of its draws lie within ±10 % of its mode in 2025 widening to ±30 % in
     2040 (12.88 % and 38.64 % at the ends). Every type has its own draws of it, one random number a type and draw, the
     same draws in every year. Which draws of the six go together in one draw is then chosen so that the six add up to
     the article's robots: at 1 January 2025 and in every quarter, starting from the five other types linked by one
     correlation (0.353 in 2025, −0.212 in 2040) with type 3 1 minus them, each type's own draws put in that order,
     then the rearrangement algorithm (Puccetti & Rüschendorf 2012): each type's draws in turn put in the opposite order
     of the sum of the others, until the sum no longer improves. No draw changes, only which draws share a row; nothing
     is divided ("I do NOT want this [normalisation]"). Type 3, the largest, is 1 minus the other five, so that the sum
     is exact; it lies off its own draws by what the rearrangement leaves, which the run prints (0.14 % of its
     half-width at 200,000 draws; with few draws more: 0.43 % at 2,000, 23 % at 40). Measured at 200,000 draws: every
     type ±10.0 % in 2025 and ±29.9 to 30.1 % in the last quarter of 2040 (95 % of the draws); each type's draws as close to its
     triangle as random draws of a triangle are; a draw from one quarter to the next correlated at least 0.998. The
     modes: type 1 10 % in 2025 to 5 % in 2040; types 2 to 6 the workbook's shares, scaled together to what type 1
     leaves, so that the six modes add up to 1; a straight line between the years. Each type's robots built are the
     article's robots built times its share. The robots of 1 January 2025 by the shares of 2025. The workbook's
     years, the type shares' spread and type 1's mode at 1 January of their years, a straight line between.
  3. The joint sets: a robot's joints (the kinds 01 numbers 1 to 6: hip, knee, ankle, waist, arm and head joints) a
     stock of its own, as many as the robots in use of its type, each set leaving when it wears out (its life the
     triangle 7,000 / 10,000 / 30,000 hours at the hours a day, spread among the sets, times the draw's own factor from
     the triangle 0.7 / 1 / 1.2, as the robots' and the packs') and replaced by a new one, as
     07's units that follow the GPUs: a stock target with their own lifetimes.
  4. The battery packs: a robot holds as many as one day's work needs, the hours a day over a pack's runtime, rounded
     up (types 2, 4 and 6 their runtime in the workbook; types 1, 3 and 5 the setting's runtime of 2025 times their
     battery energy density over that of 2025; a straight line between the workbook's years, the last value held after
     it). Each pack is charged once a day and replaced when its capacity falls below the draw's share: its life in
     charges, its charges to 80 % (spread among the packs, times the draw's own factor from the triangle 0.7 / 1 /
     1.2: "Also with the batteries") times (1 − the share) / 0.2, a straight-line fade (an approximation). A stock target, as the joint sets: the robots in use times the packs a robot needs. Where that
     need falls (longer runtimes), the packs in use stay until they wear out and the stock lies above the need.
     07's approximation in both: the joint sets and the packs of a retired robot go on in a new robot until they wear
     out, which makes their inflow and outflow slightly low.
  5. The elements: every flow and stock of robots, joint sets and packs of a type times one robot's kg of each element
     in 02's draw i: a robot its body (every kind of part but the joints and the battery pack), a joint set the joint
     kinds, a pack the kind Battery pack (02 builds one pack a robot). Sums on the raw draws, before any statistic.
  6. The years, as 07's: the flows added up over the four quarters of each calendar year, 2025 to 2040; the stocks
     at the end of each year (the article's values: 10 M at the end of 2025, 70 × 10⁹ at the end of 2040).
Each chunk of draws is checked (`check`): in every quarter the stock before + inflow − outflow = the stock, the outflow
counted cohort by cohort apart from the stock; no flow below 0; the article's robots in use at the end of each year and 8.62 M at 1 January 2025; the joint
sets as many as the robots of their type; the packs never fewer than the need. A fault stops the run.

WHAT IT WRITES
--------------
Into `output.stock_and_flow_dir` (`data/stock_and_flow/`; not in git), the draws of every level ("keep the distribution
on all levels"), float32 (about 7 significant digits): units_in.npy and units_out.npy (draw × the calendar years 2025 to 2040 × robots, joint sets,
battery packs × robot type 1 to 6), units_stock.npy (draw × the end of 2025 to 2040 × the same), elements_in.npy,
elements_out.npy (draw × year × the 14 parts of how a robot is taken apart, 01's TAKEN_APART, × element, kg) and
elements_stock.npy (draw × year end × the same; Matthias, 2026-11-08, "Yes do it": about 4.2 GB each at 200,000 draws); article_in.npy, article_stock.npy, article_out.npy (draw × year: the article's robots built, in use and
retired, at the draw's lifetime); their axes in draws.txt; summary.csv, each quantity's mean and 2.5 % and 97.5 % percentiles over the draws above
0 and the share of the draws above 0, by year (as 07: a flow its calendar year, a stock the year's end), each element also by group
('Copper, Electronics') and by part ('Copper, Electronics: Small PCB'). The elements of one robot type are its units
times 02's draw i, each part with the unit that carries it (a joint's with the joint sets, the battery's with the packs,
every other with the robots).
Into `output.stock_and_flow_figures_dir` (`figures/stock_and_flow/`; not in git), as 07's, each an A4 landscape page:
overview.png (the robots in use; built and retired; in use by robot type; the share of the robots built by robot type;
the joint sets; the battery packs in use; built and worn out) and elements/<Element>.png (its stock beside the world's reserves; its inflow and outflow beside
the world's mine production in 2025). Each line the mean over the draws above 0, its band 95 % of them; logarithmic
axes. An element 0 in every draw has no page, and 04 says so. In distributions/ (Matthias, 2026-11-07: "I also want the
distributions"; 2026-11-08: "Exactkly the figures we have worked out for the data centers!!!", "Sorry end of goes away"):
robots_in_use.png (the robots in use of 2025, 2030, 2035 and 2040, a panel a year, the six types one above the other,
every draw on the axis, the robots in all in the title; followed by robots_in_use_numbers.png) and elements_<year>.png
for 2025, 2030, 2035 and 2040, each exactly as RAWCLICDataCenters' 05 draws the elements of one data centre: a panel per
element held in all robots in use, its draws' distribution, each bar split into the four groups of how a robot is taken
apart (joints, battery, electronics, body), the mean a line with its number, 95 % dashed, the groups' means written in the
panel; each followed by parts_<year>_<k>.png, every element in each of the 14 parts that holds it (2026-11-08, "I want a
detailed list of the component ... to know how to take it apart!!!").
Every figure a result of the run, never an input (GitHub/CLAUDE.md §5).

Where it sits: after 03_comparison.py; it reads 02's draws and nothing of 03.
"""

from __future__ import annotations

import csv
import importlib.util
import math
import os
import sys
import textwrap
import warnings
from typing import NamedTuple

# Run from anywhere, and put the project root on the path, so that `src` imports. Must come before any import of src.
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import numpy as np  # noqa: E402
import openpyxl  # noqa: E402
from scipy.special import ndtr, ndtri  # noqa: E402  (the normal distribution and its inverse)

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
from matplotlib.patches import Patch  # noqa: E402  (a part's colour in a page's legend)

# ------------------------------------------------------------------------------------------------------
# The time, the parts of a robot, what it writes
# ------------------------------------------------------------------------------------------------------

# The years as RAWCLICDataCenters' 07 counts them (Matthias, 2026-11-08: "Both have to be exactly the same, as we have
# to combine both data!!!", "Both have to be on the same x axis scale!!", "Yes!!"): quarters from 2025 Q1 to 2040 Q4,
# the flows of each calendar year, the stocks at the end of each year; the article's robots each at the end of its year
# ("Follow the artcile!! 70 x 10E9").
FIRST, LAST = 2025, 2040          # the first and the last year counted
QUARTERS = 4 * (LAST - FIRST + 1) # 64: 2025 Q1 to 2040 Q4
DAYS_A_YEAR = 365.25              # days in a year, for the charges and operating hours of a year
FADE_TO_80 = 0.2                  # the capacity a pack loses until 80 %: 1 − 0.8
TYPES = (1, 2, 3, 4, 5, 6)        # the robot types, the workbook's categories
RESEARCH_TYPE = 1                 # its mode the setting's, not the workbook's
BALANCING_TYPE = 3                # the largest: 1 − the other five, so that the six add up to 1 (step 2)
HALF95 = 1 - math.sqrt(0.05)      # 95 % of a symmetric triangle lies within 0.7764 of its half-width: (1 − 0.7764)² = 5 %
# The joint kinds: those 01 numbers on its robot (1 to 6; the other kinds have letters). The battery: its kind.
JOINT_KINDS = tuple(kind for kind, mark in schemas.MARKS.items() if mark.isdigit())
BATTERY_KIND = 'battery'
UNITS = ('robots', 'joint sets', 'battery packs')     # the three stocks of every robot type
# What the elements are counted in: the 14 parts of how a robot is taken apart, in 01's order, each in one of the four
# groups, joints, battery, electronics and body (01's TAKEN_APART; Matthias, 2026-11-08: "I want a detailed list of the
# component, so it is easy to understand and establish a recycling to know how to take it apart!!!", "Yes do it"). A
# part of a kind goes with the unit of its kind, and so with its lifetime: a joint's parts with the joint sets (its
# driver board and encoders too), the battery's with the packs (its management board too), every other with the robots.
PARTS = tuple(schemas.TAKEN_PARTS)
GROUPS = tuple(schemas.TAKEN_APART)
GROUP_OF = schemas.TAKEN_GROUP
# The workbook's sheets and rows, as his workbook writes them.
SHARES_SHEET, SHARES_HEADING = 'Market Units & Shares 2025-2040', '2025 Share (%)'
TRAJECTORIES_SHEET = 'Material Trajectories 2025-2040'
RUNTIME_ROW, DENSITY_ROW = 'Runtime (hours)', 'Battery Energy Density (Wh/kg)'
WORKBOOK_YEARS = (2025, 2030, 2035, 2040)
# What it writes, by exact name.
UNIT_FILES = ('units_in', 'units_stock', 'units_out')
ARTICLE_FILES = ('article_in', 'article_stock', 'article_out')   # the article's robots built, in use, retired
ELEMENT_FILES = ('elements_in', 'elements_stock', 'elements_out')
FLOWS = ('in', 'stock', 'out')
SUMMARY, AXES_FILE = 'summary.csv', 'draws.txt'
SHARE_QUANTITY = 'share of the robots built, %'   # each type's share of a year's robots built, in the summary
OVERVIEW, ELEMENTS_DIR = 'overview.png', 'elements'
DISTRIBUTIONS_DIR = 'distributions'   # the pages of the distributions of the draws, each followed by its numbers
DISTRIBUTION_YEARS = (2025, 2030, 2035, 2040)    # the year ends of the distribution pages of robots and elements
CHUNK = 10000                     # draws counted at once (memory measured in the sandbox: VERIFICATION.md V222)
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


def robot_survival(age, factor, lifetime: tuple):
    """The share of one quarter's robots still in use at `age` (years), one row a draw of `factor` (the draw's factor on
    the lifetime, Matthias's "30% short and 20% longer"): the lifetime triangle, spread among the robots, times the
    factor; so a robot of age a survives as one of age a / factor would with the triangle itself (step 1)."""
    age, factor = np.asarray(age, dtype=float), np.atleast_1d(np.asarray(factor, dtype=float))
    return survival(age[None, :] / factor[:, None], lifetime)


def joint_survival(age, hours_a_day: float, life_hours: tuple, factor=1.0):
    """The share of one quarter's joint sets still in use at `age` (years), one row a draw of `factor` (the draw's
    factor on the joints' life, as on the robots' and the packs'): their operating hours, the hours a day for every day
    of their age, against their life in hours spread among the sets times the factor (step 3)."""
    age, factor = np.asarray(age, dtype=float), np.atleast_1d(np.asarray(factor, dtype=float))
    return survival(age[None, :] * hours_a_day * DAYS_A_YEAR / factor[:, None], life_hours)


def pack_survival(age, threshold, cycles_to_80: tuple, factor=1.0):
    """The share of one quarter's battery packs still in use at `age` (years), one row a draw of `threshold` (the
    capacity below which a pack is replaced) and `factor` (the draw's factor on the charges, "Also with the
    batteries"): a pack charged once a day leaves when its charges reach its charges to 80 % × factor × (1 − threshold)
    / 0.2 (a straight-line fade), so it survives while its charges to 80 %, spread among the packs, exceed its charges ×
    0.2 / (1 − threshold) / factor (step 4)."""
    age, threshold = np.asarray(age, dtype=float), np.atleast_1d(np.asarray(threshold, dtype=float))
    factor = np.broadcast_to(np.asarray(factor, dtype=float), threshold.shape)
    return survival(age[None, :] * DAYS_A_YEAR * FADE_TO_80 / ((1 - threshold) * factor)[:, None], cycles_to_80)


# ------------------------------------------------------------------------------------------------------
# Step 1: the quarters, the cohorts
# ------------------------------------------------------------------------------------------------------

def start_robots(robots: dict) -> float:
    """The robots in use at 1 January 2025, before the article's first value: its 2025 less one year of its own
    growth (its 2026 over its 2025), 10 M / 1.16 = 8.62 M (an estimate, by the growth with which the robots before
    2025 are built, E42)."""
    return robots[FIRST] / (robots[FIRST + 1] / robots[FIRST])


def targets(robots: dict) -> np.ndarray:
    """The robots in use at the end of each quarter, 2025 Q1 to 2040 Q4: each of the article's values at the end of
    its year (Matthias, 2026-11-08: "Follow the artcile!! 70 x 10E9"), geometric between (as 07): V(y − 1)^(1 − k/4) ×
    V(y)^(k/4) at the end of quarter k of year y, V(2024) the start (`start_robots`); the end of 2040 the article's
    70 × 10⁹."""
    out = np.empty(QUARTERS)
    for q in range(QUARTERS):
        year, k = FIRST + q // 4, q % 4 + 1
        before = robots[year - 1] if year - 1 in robots else start_robots(robots)
        out[q] = before ** (1 - k / 4) * robots[year] ** (k / 4)
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
        # The quarters before 2025 Q1, oldest first: p quarters before (p = before … 1), the arrivals ∝
        # growth^(their time); at 1 January 2025 such a quarter's units are survive[:, p − 1] (k = p − 1 quarters after their own).
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
    """A straight line through the workbook's years, each value at its 1 January, at `times`, held before its first
    year and after its last value (a value None, '—' in the workbook, is left out: the one before it held)."""
    known = [(y, v) for y, v in zip(WORKBOOK_YEARS, values) if v is not None]
    return np.interp(times, [y for y, _ in known], [v for _, v in known])


def mid_times() -> np.ndarray:
    """The middle of each quarter, 2025 Q1 to 2040 Q4, in years: when its robots arrive."""
    return FIRST + (np.arange(QUARTERS) + 0.5) / 4


def share_times() -> np.ndarray:
    """1 January 2025 and the middles of the quarters: where the robot types' shares are drawn (the robots of 1 January
    2025, then each quarter's robots built)."""
    return np.concatenate([[float(FIRST)], mid_times()])


SHARE_TIMES = share_times()       # 65: 1 January 2025, then the middle of each quarter


def end_times() -> np.ndarray:
    """The end of each quarter, 2025 Q1 to 2040 Q4, in years: when its stock is counted."""
    return FIRST + (np.arange(QUARTERS) + 1.0) / 4


def between(pairs: tuple, times: np.ndarray) -> np.ndarray:
    """A setting given for 2025 and 2040 ((2025, value), (2040, value)), each at its 1 January, at `times`: a straight
    line between, held outside."""
    (first_year, first), (last_year, last) = pairs
    return np.interp(times, [first_year, last_year], [first, last])


def type_modes(params: Params, shares: dict, times: np.ndarray) -> np.ndarray:
    """The mode of each robot type's share of the robots built at `times` (6 × times): type 1 the setting's (10 % to
    5 %); types 2 to 6 the workbook's shares, a straight line between its years, scaled together to what type 1 leaves,
    so that the six modes add up to 1 (in 2025 the workbook's type 1 is 25 %, the setting's 10 %: types 2 to 6 take
    the 15 points in proportion)."""
    out = np.empty((len(TYPES), times.size))
    research = TYPES.index(RESEARCH_TYPE)
    out[research] = between(params.stock_and_flow.research_share, times)
    others = [k for k, t in enumerate(TYPES) if t != RESEARCH_TYPE]
    for k in others:
        out[k] = along(times, shares[TYPES[k]])
    out[others] *= (1 - out[research]) / out[others].sum(axis=0)
    return out


def type_spread(params: Params, times: np.ndarray) -> np.ndarray:
    """How far each type's share, every type's alike, lies from its mode in 95 % of the draws at `times`, a share of the
    mode: 10 % in 2025 widening to 30 % in 2040 (Matthias: "Damit I told you 10% in 2025 and 30% in 2040", "I said +-10%
    and then +- 30% this is never the case", "all 6 types around 10% +- in 2025 and 30%+- in 2040")."""
    return between(params.stock_and_flow.type_share_spread, times)


def type_ends(params: Params, times: np.ndarray) -> np.ndarray:
    """The ends of each type's triangle at `times`, a share of the mode: the spread over HALF95, so that 95 % of the
    triangle lies within the spread (2025: 0.10 / 0.7764 = 12.88 %; 2040: 38.64 %)."""
    return type_spread(params, times) / HALF95


def type_shares(params: Params, shares: dict, points: np.ndarray, times: np.ndarray) -> np.ndarray:
    """Each robot type's share of the robots built at `times` in every draw (n × times × 6), from `points` (n × times ×
    5, the point of the unit triangle −1 / 0 / 1 of types 1, 2, 4, 5 and 6, from `type_points`): each of them mode × (1
    + point × end); type 3 1 minus them, so that the six add up to the article's robots in every draw (Matthias,
    2026-11-07: "The summ of the total has to be correct"). Nothing divided."""
    modes, ends = type_modes(params, shares, times), type_ends(params, times)        # 6 × times; times
    others = [k for k, t in enumerate(TYPES) if t != BALANCING_TYPE]
    rest = TYPES.index(BALANCING_TYPE)
    out = np.empty((points.shape[0], times.size, len(TYPES)))
    out[:, :, others] = modes[others].T[None] * (1 + ends[None, :, None] * points)
    out[:, :, rest] = 1 - out[:, :, others].sum(axis=2)
    return out


def unit_triangle(u):
    """The symmetric triangle −1 / 0 / 1 at the share u of it: a type's point in its own triangle from its random number."""
    u = np.asarray(u, dtype=float)
    return np.where(u < 0.5, -1 + np.sqrt(2 * u), 1 - np.sqrt(2 * (1 - u)))


def linked_scores(eps: np.ndarray, rho: np.ndarray) -> np.ndarray:
    """Five normal scores a draw at each time (n × times × 5), any two correlated by the time's `rho`, each with
    variance 1, from `eps` (n × 5, independent normal scores, the same for all times, so that a draw is one world):
    R^(1/2) eps with R = (1 − rho) I + rho J, that is √(1 − rho) × (eps − their mean) + √(1 + 4 rho) × their mean."""
    mean = eps.mean(axis=1, keepdims=True)
    return (np.sqrt(1 - rho)[None, :, None] * (eps - mean)[:, None, :]
            + np.sqrt(1 + 4 * rho)[None, :, None] * mean[:, None, :])


def link_correlation(modes: np.ndarray) -> np.ndarray:
    """The correlation of the five other types at each time (modes: 6 × times) that gives type 3, 1 minus them, the
    spread of a type of its own: its variance m3² × that of the unit triangle when (m3² − Σm²) / ((Σm)² − Σm²), the
    sums over the other five (2025: 0.353; 2040: −0.212). Only where the rearrangement starts from (`type_points`).
    Raises ValueError where it would have to lie outside −1/4 (the least five can share) to 1."""
    others = [k for k, t in enumerate(TYPES) if t != BALANCING_TYPE]
    rest = TYPES.index(BALANCING_TYPE)
    total, squares = modes[others].sum(axis=0), (modes[others] ** 2).sum(axis=0)
    rho = (modes[rest] ** 2 - squares) / (total ** 2 - squares)
    if (rho < -0.25).any() or (rho > 1).any():
        raise ValueError(f'robot type {BALANCING_TYPE} cannot have the spread of the other types: its share is too large '
                         'or too small against theirs.')
    return rho


def rearrange(h: np.ndarray, weights: np.ndarray, ordered: list, sweeps: int = 200) -> int:
    """The rearrangement algorithm (Puccetti & Rüschendorf 2012): the points `h` (n × types, each column one type's own
    draws) rearranged in place within each column, so that Σ weights × h is as near 0 in every row as it gets. Each
    column in turn is put in the opposite order of the sum of the others (its largest point beside their smallest sum),
    until a sweep over all columns no longer lowers the largest row sum by 0.1 %. `ordered`: each column's points from
    the largest to the smallest. No point changes, only which points share a row. Returns the sweeps it took."""
    total = h @ weights
    for sweep in range(1, sweeps + 1):
        before = np.abs(total).max()
        for k in range(h.shape[1]):
            rest = total - weights[k] * h[:, k]
            h[np.argsort(rest, kind='stable'), k] = ordered[k]
            total = rest + weights[k] * h[:, k]
        if np.abs(total).max() >= 0.999 * before:
            return sweep
    return sweeps


def type_points(params: Params, shares: dict, z: np.ndarray, u_rest: np.ndarray) -> tuple:
    """Each type's point of its own triangle in every draw, at 1 January 2025 and in the middle of every quarter
    (SHARE_TIMES), put together so that the six shares add up to 1 (Matthias, 2026-11-07: "I want that you developt an
    algorthym that has for all 6 types around 10% +- in 2025 and 30%+- in 2040. All have to have close to this value!!",
    "NO type 3 is not triangular!!", to the rearrangement "Yes, build it"):
      - every type its own draws of its own triangle: types 1, 2, 4, 5 and 6 from `z` (n × 5), type 3 from `u_rest` (n),
        one random number a type and draw, the same draws in every year;
      - at each time the start: the five linked by one correlation (`link_correlation`, normal scores of `z`,
        `linked_scores`), type 3 1 minus them; each type's own draws put in the order of the start;
      - then the rearrangement (`rearrange`), weighted by the time's modes, so that the six add up to 1 in every draw.
    The point of the unit triangle −1 / 0 / 1 is the same at all times, its ends scaled by `type_ends`. Returns (the
    points of types 1, 2, 4, 5 and 6, n × SHARE_TIMES × 5, float32; the largest amount by which type 3, 1 minus them,
    lies off its own draws, a share of its triangle's half-width: what the rearrangement leaves)."""
    others = [k for k, t in enumerate(TYPES) if t != BALANCING_TYPE]
    rest = TYPES.index(BALANCING_TYPE)
    modes = type_modes(params, shares, SHARE_TIMES)
    rho = link_correlation(modes)
    own = np.empty((z.shape[0], len(TYPES)))                       # each type's own draws of the unit triangle
    own[:, others], own[:, rest] = unit_triangle(z), unit_triangle(u_rest)
    ascending = [np.sort(own[:, k]) for k in range(len(TYPES))]
    descending = [a[::-1] for a in ascending]
    eps = ndtri(np.clip(z, 1e-12, 1 - 1e-12))                      # the five's normal scores: the same ranks as z
    points = np.empty((z.shape[0], SHARE_TIMES.size, len(others)), dtype=np.float32)
    worst = 0.0
    for i in range(SHARE_TIMES.size):
        start = np.empty_like(own)
        start[:, others] = unit_triangle(ndtr(linked_scores(eps, rho[i:i + 1])[:, 0, :]))
        start[:, rest] = -(start[:, others] @ modes[others, i]) / modes[rest, i]
        h = np.empty_like(own)
        for k in range(len(TYPES)):                                 # own draws in the order of the start
            h[np.argsort(start[:, k], kind='stable'), k] = ascending[k]
        rearrange(h, modes[:, i], descending)
        points[:, i, :] = h[:, others]
        # What type 3, 1 minus the five as type_shares makes it, lies off its own draw, in its triangle's half-widths.
        forced = -(points[:, i, :].astype(np.float64) @ modes[others, i]) / modes[rest, i]
        worst = max(worst, float(np.abs(forced - h[:, rest]).max()))
    return points, worst


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

def unit_of(kind: str) -> int:
    """The unit that carries a kind of part, as its place in UNITS: a joint kind the joint sets, the battery the packs,
    every other kind the robots."""
    return 1 if kind in JOINT_KINDS else 2 if kind == BATTERY_KIND else 0


def robot_parts(params: Params) -> tuple:
    """From 02's draws (its table taken_apart: each element of interest by kind and part, '<kind>: <part>: <element>'),
    for each robot type, the places of its columns in one robot's units × PARTS × elements and its draws, read where
    they lie as they are needed (draw × column): ({type: (places, draws)}, the elements, {type: its name}). `places` is
    a matrix of 0 and 1 (columns × units·parts·elements), so that a chunk of draws times it is the chunk's kg in each
    unit, part and element; several kinds of a unit add up in it. Raises FileNotFoundError where 02 has not written a
    table; ValueError where the types' draws or elements differ or a column is no kind, part and element."""
    book = schemas.read_workbook(absolute(params.data.workbook), params)
    kinds = {name: kind for kind, (name, _) in schemas.KINDS.items()}
    out, names, elements, draws = {}, {}, None, None
    for category in book.categories:
        folder = composition.folder_name(category)
        with open(os.path.join(absolute(params.output.composition_dir), folder, 'elements.txt'),
                  encoding='utf-8') as handle:
            symbols = handle.read().splitlines()
        apart = os.path.join(absolute(params.output.parts_dir), folder)
        with open(os.path.join(apart, 'taken_apart.txt'), encoding='utf-8') as handle:
            columns = handle.read().splitlines()
        values = np.load(os.path.join(apart, 'taken_apart.npy'), mmap_mode='r')
        if elements is None:
            elements, draws = symbols, values.shape[0]
        if symbols != elements or values.shape[0] != draws:
            raise ValueError(f'robot type {category.number}: its draws ({values.shape[0]}) or elements differ from '
                             f"robot type {book.categories[0].number}'s; run 02 for all six types.")
        if values.shape[1] != len(columns):
            raise ValueError(f'robot type {category.number}: 02\'s table taken_apart has {values.shape[1]} columns, its '
                             f'list {len(columns)}; run 02 again.')
        places = np.zeros((len(columns), len(UNITS) * len(PARTS) * len(elements)))
        for c, column in enumerate(columns):
            words = column.split(': ')
            kind = kinds.get(words[0]) if len(words) == 3 else None
            if kind is None or words[1] not in PARTS or words[2] not in elements:
                raise ValueError(f'robot type {category.number}: the column {column!r} of 02 is no kind, part and '
                                 'element.')
            places[c, (unit_of(kind) * len(PARTS) + PARTS.index(words[1])) * len(elements)
                   + elements.index(words[2])] = 1.0
        out[category.number], names[category.number] = (places, values), category.name
    if sorted(out) != list(TYPES):
        raise ValueError(f'the workbook holds robot types {sorted(out)}, not {list(TYPES)}.')
    return out, elements, names


# ------------------------------------------------------------------------------------------------------
# Steps 1 to 4 in every draw of a chunk
# ------------------------------------------------------------------------------------------------------

def count(params: Params, shares: dict, trajectories: dict, points: np.ndarray, threshold: np.ndarray,
          robot_factor: np.ndarray, pack_factor: np.ndarray, joint_factor: np.ndarray) -> tuple:
    """The robots, joint sets and packs of each type, quarter by quarter, in the draws of `points` (n × SHARE_TIMES × 5,
    the points of types 1, 2, 4, 5 and 6 in their triangles from `type_points`), `threshold` (the capacity below which a pack is replaced), `robot_factor`, `pack_factor`
    and `joint_factor` (the draw's factors on the robots' lifetime, the packs' charges and the joints' life):
    ({(unit, type): Flows}, with all robots under ('robots', 0); {type: the packs needed, n × QUARTERS})."""
    flow = params.stock_and_flow
    robots = {year: float(v) for year, v in flow.robots}
    growth = robots[FIRST + 1] / robots[FIRST]
    n = points.shape[0]
    # The quarters before 2025 that can still hold a unit: the longest life of a robot, a joint set or a pack.
    longest = max(flow.robot_lifetime_years[2] * flow.lifetime_factor[2],
                  flow.joint_life_hours[2] * flow.lifetime_factor[2] / (flow.hours_a_day * DAYS_A_YEAR),
                  flow.battery_cycles_to_80[2] * flow.lifetime_factor[2] * (1 - flow.battery_replaced_below[0])
                  / FADE_TO_80 / DAYS_A_YEAR)
    before = int(math.ceil(4 * longest)) + 1
    age = ages(before + QUARTERS)
    robot_survive = robot_survival(age, robot_factor, flow.robot_lifetime_years)          # one row a draw
    joint_survive = joint_survival(age, flow.hours_a_day, flow.joint_life_hours, joint_factor)    # one row a draw
    pack_survive = pack_survival(age, threshold, flow.battery_cycles_to_80, pack_factor)   # one row a draw
    counted, needs = {}, {}
    # The article's robots in use, the frame: what has to be built in each quarter, at the draw's lifetime, to hold
    # them. Each type then builds its own share of it.
    first = start_robots(robots)                                   # 1 January 2025
    total = cohorts(robot_survive, first, growth, target=np.broadcast_to(targets(robots), (n, QUARTERS)))
    counted[('article', 0)] = total
    built_shares = type_shares(params, shares, points[:, 1:], SHARE_TIMES[1:])     # n × QUARTERS × 6
    start_shares = type_shares(params, shares, points[:, :1], SHARE_TIMES[:1])[:, 0]   # n × 6: 1 January 2025
    packs = packs_per_robot(params, trajectories, end_times())                        # 6 × QUARTERS
    first_packs = packs_per_robot(params, trajectories, np.array([float(FIRST)]))[:, 0]
    for k, t in enumerate(TYPES):
        start = first * start_shares[:, k]
        robots_t = cohorts(robot_survive, start, growth, inflow=total.built * built_shares[:, :, k],
                           past=total.past * start_shares[:, k:k + 1])
        counted[('robots', t)] = robots_t
        counted[('joint sets', t)] = cohorts(joint_survive, start, growth, target=robots_t.stock)
        needs[t] = robots_t.stock * packs[k][None, :]
        counted[('battery packs', t)] = cohorts(pack_survive, start * first_packs[k], growth, target=needs[t])
    return counted, needs


def check(params: Params, counted: dict, needs: dict) -> list:
    """The faults of one chunk, in plain words ([] where none): a quarter whose stock before + inflow − outflow is not
    its stock (the outflow counted apart, cohort by cohort), a flow below 0, the article's frame not holding its robots
    in use at the end of a year (the article's value of the year) or at 1 January 2025 (`start_robots`), the six types not adding up to it, joint sets not as many as the robots, packs fewer than
    needed. Each to TOLERANCE of the largest stock (07's check_balance)."""
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
    article = counted[('article', 0)]
    year_ends = article.stock[:, 3::4]
    for y, year in enumerate(range(FIRST, LAST + 1)):
        if np.abs(year_ends[:, y] - robots[year]).max() > TOLERANCE * robots[year]:
            faults.append(f"the robots in use at the end of {year} are not the article's {robots[year]:,.0f}.")
    first = start_robots(robots)
    if np.abs(article.start - first).max() > TOLERANCE * first:
        faults.append(f'the robots in use at 1 January {FIRST} are not {first:,.0f}.')
    scale = float(article.stock.max())
    if np.abs(sum(counted[('robots', t)].stock for t in TYPES) - article.stock).max() > TOLERANCE * scale:
        faults.append("the robots of the six types do not add up to the article's.")
    for t in TYPES:
        if np.abs(counted[('joint sets', t)].stock - counted[('robots', t)].stock).max() > TOLERANCE * scale:
            faults.append(f'robot type {t}: the joint sets in use are not as many as its robots in use.')
        if (counted[('battery packs', t)].stock < needs[t] - TOLERANCE * max(float(needs[t].max()), 1.0)).any():
            faults.append(f'robot type {t}: fewer battery packs in use than its robots need.')
    return faults


def years_of(f: Flows) -> tuple:
    """A stock by year, as 07's to_years: (inflow n × 16, the calendar years 2025 to 2040; the stock at the end of each
    year, n × 16; outflow n × 16), the order of FLOWS."""
    n = f.built.shape[0]
    return f.built.reshape(n, -1, 4).sum(axis=2), f.stock[:, 3::4], f.gone.reshape(n, -1, 4).sum(axis=2)


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


def column_stats(values: np.ndarray) -> tuple:
    """stats_of() for every column of `values` (draws × columns) at once, over the draws above 0: (the mean, the 2.5 %
    and the 97.5 % percentile, the share of the draws above 0), NaN where no draw is above 0. The same numbers as
    stats_of (the same percentiles, numpy's default), for the elements of every part of a year in one go."""
    above = values > 0
    masked = np.where(above, values, np.nan)
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', RuntimeWarning)          # a column with no draw above 0: NaN, as stats_of
        mean = np.nanmean(masked, axis=0)
        low, high = np.nanpercentile(masked, (2.5, 97.5), axis=0)
    return mean, low, high, above.mean(axis=0)


def element_summary(files: dict, elements: list) -> dict:
    """Every element in all, by group and by part, each flow and year, over the draws above 0 (as stats_of): one year
    of an element file read at a time (draws × parts × elements), its groups the sums of their parts draw by draw, its
    total the sum of all parts. Keys ('element', symbol, flow), ('element group', (symbol, group), flow) and ('element
    part', (symbol, part), flow), each {'mean', 'low', 'high', 'held'} over the years."""
    years = LAST - FIRST + 1
    members = [[PARTS.index(p) for p in PARTS if GROUP_OF[p] == g] for g in GROUPS]
    out = {}
    for element_name, flow_name in zip(ELEMENT_FILES, FLOWS):
        keys = ([('element', e, flow_name) for e in elements]
                + [('element group', (e, g), flow_name) for g in GROUPS for e in elements]
                + [('element part', (e, p), flow_name) for p in PARTS for e in elements])
        for key in keys:
            out[key] = {name: np.full(years, np.nan) for name in ('mean', 'low', 'high')}
            out[key]['held'] = np.zeros(years)
        for y in range(years):
            block = np.asarray(files[element_name][:, y], dtype=np.float64)          # draws × parts × elements
            columns = np.concatenate([block.sum(axis=1)] + [block[:, idx].sum(axis=1) for idx in members]
                                     + [block[:, j] for j in range(len(PARTS))], axis=1)
            for key, *numbers in zip(keys, *column_stats(columns)):
                for name, value in zip(('mean', 'low', 'high', 'held'), numbers):
                    out[key][name][y] = value
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


def share_panel(axes, series: list, word: str) -> None:
    """One panel on a plain axis from 0, for shares in %: each of `series` (years, stats of stats_of, label, colour)
    its mean a line and 95 % of its draws a band (Matthias, 2026-11-07: each type's range "one has to see it")."""
    for years, stats, label, colour in series:
        axes.plot(years, stats['mean'], '-', color=colour, label=label)
        axes.fill_between(years, stats['low'], stats['high'], alpha=0.25, color=colour, linewidth=0)
    axes.set_xlim(FIRST, LAST)
    axes.set_xticks(range(FIRST, LAST + 1, 5))
    axes.set_ylim(bottom=0)
    axes.set_ylabel(word)


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
            "per calendar year, stocks at the end of the year, as RAWCLICDataCenters' 07; logarithmic axes. Robots in "
            "use: ai-2040.com Plan A, each value at the end of its year; each robot one of 02's draws of its robot "
            "type.")


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
    page laid out as it is saved. A place without a panel that only holds a legend (the overview's robot types) keeps
    its legend as it is."""
    figure.canvas.draw()
    renderer = figure.canvas.get_renderer()
    for axes in figure.axes:
        if axes.get_legend() is None or not axes.axison:
            continue
        for place in LEGEND_PLACES:
            legend = axes.legend(loc=place)
            if not lines_under(axes, legend.get_window_extent(renderer), renderer):
                break
        else:
            axes.legend(loc='best')


def save_figure(figure, path: str, note: str, dpi: int, top: float = 1.0) -> str:
    """Write a page with its note at the foot, wrapped within the page's width, and close it (07's save_figure); each
    legend where no line runs under it (place_legends); `top` below 1 leaves room above the panels for a page's
    legend."""
    lines = textwrap.wrap(note, NOTE_WIDTH)
    figure.text(0.5, 0.008, '\n'.join(lines), ha='center', va='bottom', fontsize=8)
    figure.tight_layout(rect=(0, 0.012 + 0.02 * len(lines), 1, top))
    place_legends(figure)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    figure.savefig(path, dpi=dpi, facecolor='white')
    plt.close(figure)
    return path


def overview_page(summary: dict, names: dict, draws: int, path: str, dpi: int) -> str:
    """The overview, two rows of four: the robots in use; built and retired; in use by robot type; beside it each type's
    share of the robots built (Matthias, 2026-11-07, "Add it beside"); the joint sets; the battery packs in use; built
    and worn out; the robot types' legend in the eighth place, for the two panels of the types."""
    flows = stocks = np.arange(FIRST, LAST + 1)                     # every year at its year, as 07

    def line(unit, t, flow, label, colour):
        return (stocks if flow == 'stock' else flows, summary[(unit, t, flow)], label, colour)

    figure, grid = plt.subplots(2, 4, figsize=A4_LANDSCAPE)
    panels = (
        (grid[0, 0], 'Robots in use', [line('robots', 0, 'stock', 'in use', IN_USE)], 'robots'),
        (grid[0, 1], 'Robots built\nand retired', [line('robots', 0, 'in', 'built', BUILT),
                                                 line('robots', 0, 'out', 'retired', GONE)], 'robots per year'),
        (grid[0, 2], 'Robots in use\nby robot type', [line('robots', t, 'stock', f'robot type {t}', TYPE_COLOURS[k])
                                                    for k, t in enumerate(TYPES)], 'robots'),
        (grid[1, 0], 'Joint sets', [line('joint sets', 0, 'stock', 'in use', IN_USE),
                                    line('joint sets', 0, 'in', 'built per year', BUILT),
                                    line('joint sets', 0, 'out', 'worn out per year', GONE)], 'joint sets'),
        (grid[1, 1], 'Battery packs\nin use', [line('battery packs', 0, 'stock', 'in use', IN_USE)], 'battery packs'),
        (grid[1, 2], 'Battery packs\nbuilt and worn out', [line('battery packs', 0, 'in', 'built', BUILT),
                                                         line('battery packs', 0, 'out', 'worn out', GONE)],
         'battery packs per year'))
    for axes, title, series, word in panels:
        if log_panel(axes, series, word):
            axes.set_title(title)
            types_panel = title.startswith('Robots in use\nby')
            if (len(series) > 1 and not types_panel) or held_in_label(axes):
                axes.legend(loc='upper left')
    share_panel(grid[0, 3], [line(SHARE_QUANTITY, t, 'in', f'robot type {t}', TYPE_COLOURS[k])
                             for k, t in enumerate(TYPES)], '% of the robots built')
    grid[0, 3].set_title('Share of the robots built\nby robot type')
    # The eighth place: the legend of the robot types, for the two panels of the types beside each other.
    grid[1, 3].axis('off')
    grid[1, 3].legend(*grid[0, 3].get_legend_handles_labels(), loc='center', title='Robot types')
    figure.suptitle('Humanoid robots in the world')
    types = '; '.join(f'{t} {names[t]}' for t in TYPES)
    note = (figure_note(draws).replace('logarithmic axes.', 'logarithmic axes, the shares a plain one.')
            + ' A joint set: the hip, knee, ankle, waist, arm and head joints of one robot. '
            f'Robot types: {types}.')
    return save_figure(figure, path, note, dpi)


def element_page(symbol: str, summary: dict, world: dict, notes: list, draws: int, path: str, dpi: int) -> str:
    """One element: its stock beside the world's reserves; its inflow and outflow beside the world's mine production
    in 2025 (07's element figure, without "collected")."""
    flows = stocks = np.arange(FIRST, LAST + 1)                     # every year at its year, as 07
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
    note = figure_note(draws) + ' All of every robot: its joints, battery, electronics and body.'
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
# The distribution pages (Matthias, 2026-11-07: "I also want the distributions", to the table "Yes, as recommended"), in
# 02's form (its centre_lines, stacked_bars, mass_ticks, panel_rows: one copy of the code): bars of the share of the
# draws, the median a solid line, the mean a dotted one, 2.5 % and 97.5 % dashed, no number on a panel; each page
# followed by a page of its numbers (EVIDENCE.md E34). The elements split by the four groups of how a robot is taken
# apart as RAWCLICDataCenters' 05 splits its elements by 03 and 04, the smaller lower, in 01's colours (GROUP_COLOURS);
# their parts listed on the pages after.
# ------------------------------------------------------------------------------------------------------

PARTS_ROWS = 24                   # the rows of one list page of the elements part by part (parts_pages)
PARTS_COLUMNS = (0.02, 0.15, 0.27, 0.50, 0.61, 0.72, 0.83)   # where each column of a list page starts, across the page
PARTS_HEAD = ('Element', 'Group', 'Part', 'Held in', 'Median', 'Mean', '95 % of the draws')
NUMBER_COLUMNS = (0.02, 0.21, 0.31, 0.45, 0.59, 0.79)    # where each column of a page of numbers starts, across the page


def count_unit(values: np.ndarray) -> tuple:
    """The unit a panel of robots is written in, by the mean of its draws above 0, so that it reads from 1 up:
    (robots in one unit, its words), e.g. (1e6, 'million robots')."""
    positive = values[values > 0]
    typical = float(positive.mean()) if positive.size else 0.0
    for per, words in ((1e9, 'billion robots'), (1e6, 'million robots'), (1e3, 'thousand robots')):
        if typical >= per:
            return per, words
    return 1.0, 'robots'


def mass_unit(values_kg: np.ndarray) -> tuple:
    """The unit a panel of kg is written in, by the mean of its draws above 0, so that it reads from 1 up (kg, not Mg;
    Mt the largest, as mass_text): (kg in one unit, its symbol)."""
    positive = values_kg[values_kg > 0]
    typical = float(positive.mean()) if positive.size else 0.0
    for per, unit in ((1e9, 'Mt'), (1e6, 'kt'), (1e3, 't'), (1.0, 'kg'), (1e-3, 'g')):
        if typical >= per:
            return per, unit
    return 1e-6, 'mg'


def numbers_page(heading: str, rows: list, path: str, dpi: int) -> str:
    """The page of numbers that follows a page of panels (EVIDENCE.md E34), A4 landscape as 04's pages: a row per panel
    (02's panel_rows: its title, in what share of the draws it is held, the median, the mean, 95 % of the draws, the
    draws beyond its axis), each under 02's column names (NUMBERS_HEAD)."""
    page = plt.figure(figsize=A4_LANDSCAPE)
    page.suptitle(heading)
    for x, words in zip(NUMBER_COLUMNS, composition.NUMBERS_HEAD):
        page.text(x, 0.91, words, fontsize=9, fontweight='bold', va='top')
    step, y = min(0.034, 0.82 / max(len(rows), 1)), 0.87
    for row in rows:
        page.add_artist(plt.Line2D([0.02, 0.98], [y + 0.007, y + 0.007], color=composition.GRID, linewidth=0.8))
        for x, cell in zip(NUMBER_COLUMNS, row):
            page.text(x, y, cell, fontsize=8, va='top')
        y -= step
    os.makedirs(os.path.dirname(path), exist_ok=True)
    page.savefig(path, dpi=dpi, facecolor='white')
    plt.close(page)
    return path


RIDGE_BINS = 40                   # the bars of one type's row on the page of the robots in use, over its own draws


def robots_text(value: float) -> str:
    """A number of robots written out to four significant digits, as a title writes it: '11,600,000'."""
    return f'{float(f"{value:.4g}"):,.0f}'


def robots_in_use_page(files: dict, draws: int, folder: str, dpi: int) -> list:
    """The robots in use at the end of 2025, 2030, 2035 and 2040, the six types in one panel a year (Matthias, 2026-11-08:
    "can you not combine the 6 types to 1", "I want to see at the end how many robots there are", "not 39 I want 2040",
    "SHit it to 1st of July", "Yes"): each type a row, type 1 at the top, its robots in use over the draws, the bars of
    its own draws scaled to the row, its median (solid), mean (dotted) and 2.5 % and 97.5 % (dashed) within the row; one
    axis for the six, from the smallest to the largest draw of any type, so that no draw is cut ("why is the largest
    part of the triangal cut off?"); the robots in all, the article's, in the panel's title. The results of the run,
    nothing else (GitHub/CLAUDE.md §5). Followed by the page of each row's numbers."""
    figure, grid = plt.subplots(2, 2, figsize=A4_LANDSCAPE)
    numbers = []
    for axes, year in zip(grid.flat, DISTRIBUTION_YEARS):
        robots = np.asarray(files['units_stock'][:, year - FIRST, UNITS.index('robots'), :], dtype=np.float64)
        totals = np.asarray(files['article_stock'][:, year - FIRST], dtype=np.float64)   # all robots, each draw
        per, words = count_unit(robots.max(axis=1))
        axes.type_numbers = []
        for k, t in enumerate(TYPES):
            values = robots[:, k] / per
            base = len(TYPES) - 1 - k
            counts, edges = np.histogram(values, bins=RIDGE_BINS)                     # every draw of the type
            axes.bar(edges[:-1], 0.85 * counts / counts.max(), width=np.diff(edges), align='edge', bottom=base,
                     color=TYPE_COLOURS[k], edgecolor='none')
            median, mean = float(np.median(values)), float(values.mean())
            low, high = (float(b) for b in np.percentile(values, (2.5, 97.5)))
            for x, style, width in ((median, '-', 1.4), (mean, ':', 1.4), (low, '--', 0.9), (high, '--', 0.9)):
                axes.plot([x, x], [base, base + 0.9], color=composition.APART_INK, linestyle=style, linewidth=width)
            axes.type_numbers.append((f'Robot type {t}, {year}', median, mean, low, high, words))
            numbers.append([f'Robot type {t}, {year}', 'all draws',
                            f'{composition.panel_number(median)}\u00a0{words}',
                            f'{composition.panel_number(mean)}\u00a0{words}',
                            f'{composition.panel_number(low)} to {composition.panel_number(high)}\u00a0{words}', '–'])
        smallest, largest = robots.min() / per, robots.max() / per
        margin = 0.02 * (largest - smallest)
        axes.set_xlim(smallest - margin, largest + margin)
        axes.set_ylim(0, len(TYPES))
        axes.set_yticks(np.arange(len(TYPES)) + 0.4)
        axes.set_yticklabels([f'robot type {t}' for t in reversed(TYPES)])
        axes.xaxis.set_major_locator(plt.MaxNLocator(6))
        axes.xaxis.set_major_formatter(ticker.ScalarFormatter(useOffset=False))
        axes.ticklabel_format(axis='x', style='plain', useOffset=False)
        axes.tick_params(labelsize=8)
        axes.set_xlabel(f'robots in use ({words})', fontsize=8)
        axes.grid(axis='x', alpha=0.3)
        for side in ('top', 'right'):
            axes.spines[side].set_visible(False)
        # The robots in all: the article's, the same in every draw (written as a range, were it ever to vary).
        if totals.max() - totals.min() <= 1e-6 * totals.max():
            words_in_all = robots_text(totals[0])
        else:
            low_all, high_all = np.percentile(totals, (2.5, 97.5))
            words_in_all = f'{robots_text(low_all)} to {robots_text(high_all)}'
        axes.set_title(f'{year}: {words_in_all} robots', loc='left', fontsize=10, fontweight='bold')   # the year alone
    figure.suptitle('Humanoid robots in use by robot type: the distribution of the draws')
    note = ('Each row one robot type: its bars the draws of the run, the height scaled to the row; solid line: the '
            'median; dotted: the mean; dashed: 2.5 % and 97.5 % (95 % of the draws); every draw on the axis. The six '
            'types add up to the robots in use of ai-2040.com Plan A at the end of each year, the number in the '
            f'title, the same in every draw; {draws:,} draws; the numbers of every row on the next page.')
    path = os.path.join(folder, 'robots_in_use.png')
    heading = figure._suptitle.get_text() + ': its numbers'
    saved = save_figure(figure, path, note, dpi)
    return [saved, numbers_page(heading, numbers, path[:-len('.png')] + '_numbers.png', dpi)]


def element_panel(axes, groups: dict, title: str, share_label: bool, colours: dict | None = None) -> list:
    """One element in all robots in use in one year, exactly as RAWCLICDataCenters' 05 draws an element of a data centre
    (its `_stacked_panel`; Matthias, 2026-11-08: "Exactkly the figures we have worked out for the data centers!!!"):
    the bars the distribution of the element's kg over the draws (the height the share of the draws, 70 bars over every
    draw), each bar split into the kg its draws hold in each group of how a robot is taken apart (`groups`: joints,
    battery, electronics, body), the group with the smaller mean at the bottom; the mean a solid line with its number,
    the 2.5 % and 97.5 % dashed; the groups' means written top right. Over the draws that hold the element ("A 0 is not
    part of a distribution"), their share written where it is not all of them. Returns the groups drawn (held in at
    least 2.5 % of the draws). `colours` the colour of each split, 01's GROUP_COLOURS where none (05 splits by the data
    centres and the humanoid robots)."""
    colours = colours or schemas.GROUP_COLOURS
    total = sum(groups.values())
    inside = total > 0
    per, unit = mass_unit(total)
    values = total[inside] / per
    kept = {group: kg[inside] / per for group, kg in groups.items()}
    mean = float(values.mean())
    edges = np.histogram_bin_edges(values, bins=composition.APART_BINS)
    index = np.clip(np.digitize(values, edges[1:-1]), 0, len(edges) - 2)          # the bar each draw falls into
    share_of_draws = np.bincount(index, minlength=len(edges) - 1) / values.size
    kg_all = np.bincount(index, weights=values, minlength=len(edges) - 1)
    drawn = [group for group in groups if composition.held(groups[group])]
    bottom = np.zeros(len(edges) - 1)
    for group in sorted(drawn, key=lambda g: kept[g].mean()):                        # the smaller at the bottom
        kg = np.bincount(index, weights=kept[group], minlength=len(edges) - 1)
        height = share_of_draws * np.divide(kg, kg_all, out=np.zeros_like(kg), where=kg_all > 0)
        axes.bar(edges[:-1], height, width=np.diff(edges), align='edge', bottom=bottom,
                 color=colours[group], edgecolor='none')
        bottom += height
    low, high = (float(b) for b in np.percentile(values, [2.5, 97.5]))
    axes.axvline(mean, color='#222222', linewidth=1.8)
    for bound in (low, high):
        axes.axvline(bound, color='#222222', linewidth=1.2, linestyle='--')
    axes.text(mean, 0.97, f' {composition.panel_number(mean)} {unit}', transform=axes.get_xaxis_transform(), ha='left',
              va='top', fontsize=12, color='#222222', bbox=dict(facecolor='white', edgecolor='none', alpha=0.8, pad=1))
    words = [f'{group}: {mass_text(float(kept[group].mean()) * per)}' for group in drawn]
    if not inside.all():
        words.append(f'held in {math.floor(100 * inside.mean())} % of the draws')
    axes.text(0.98, 0.80, '\n'.join(words), transform=axes.transAxes, ha='right', va='top', fontsize=10.5,
              color='#222222', bbox=dict(facecolor='white', edgecolor='none', alpha=0.8, pad=1))
    axes.xaxis.set_major_locator(plt.MaxNLocator(5))
    axes.xaxis.set_major_formatter(plt.FuncFormatter(composition.panel_number))
    axes.yaxis.set_major_locator(plt.MaxNLocator(4))
    axes.yaxis.set_major_formatter(plt.FuncFormatter(composition.panel_number))
    axes.tick_params(labelsize=11)
    axes.set_xlabel(f'mass ({unit})', fontsize=12)
    if share_label:
        axes.set_ylabel('share of the draws', fontsize=12)
    axes.grid(axis='x', alpha=0.3)
    axes.set_title(title, fontsize=13, fontweight='bold', loc='left')
    axes.element_numbers = (title, mean, low, high, unit)
    return drawn


def split_elements_page(title: str, splits: dict, colours: dict, elements: list, note: str, path: str,
                        dpi: int) -> str:
    """One page of elements exactly as RAWCLICDataCenters' 05 draws the elements of one data centre: a panel per element
    held in at least 2.5 % of the draws, in the order of `elements`, four across, each bar split into the kg of each of
    `splits` ({name: draws × elements}, in the legend's order) in its `colours` (`element_panel`); one legend of the
    splits drawn; `note` at the foot, its lines wrapped within the page's width. 04's pages (split by the four groups) and 05's (by the data centres and the
    humanoid robots) are drawn by it: one copy."""
    total = sum(np.asarray(v, dtype=np.float64) for v in splits.values())
    held = [e for e in range(len(elements)) if composition.held(total[:, e])]
    ncols = 4
    nrows = max(1, math.ceil(len(held) / ncols))
    drawn = set()
    with plt.style.context('default'):
        figure, grid = plt.subplots(nrows, ncols, figsize=(4.8 * ncols, 3.1 * nrows + 1.3), squeeze=False)
        for k, e in enumerate(held):
            parts = {name: np.asarray(v[:, e], dtype=np.float64) for name, v in splits.items()}
            name = composition.ELEMENT_NAMES.get(elements[e], elements[e])
            drawn |= set(element_panel(grid[k // ncols, k % ncols], parts, f'{name} ({elements[e]})', k % ncols == 0,
                                       colours))
        for axes in grid.flat[len(held):]:
            axes.axis('off')
        figure.suptitle(title, fontsize=18)
        handles = [Patch(color=colours[name], label=name) for name in splits if name in drawn]
        figure.legend(handles=handles, loc='upper center', bbox_to_anchor=(0.5, 0.965), ncol=max(len(handles), 1),
                      frameon=False, fontsize=12)
        # The note at the foot, each of its lines wrapped within the page's width: as many characters a line as 07's
        # note holds (NOTE_WIDTH at 8 pt on an A4 page), scaled to this page's width and to the note's 11 pt; the
        # panels end above its lines (about 0.2 inch a line). Until 2026-11-08 the note was one line, run off 05's
        # page (VERIFICATION.md V226).
        width = round(NOTE_WIDTH * (8 / 11) * figure.get_figwidth() / A4_LANDSCAPE[0])
        lines = [line for paragraph in note.split('\n') for line in textwrap.wrap(paragraph, width)]
        figure.text(0.5, 0.005, '\n'.join(lines), ha='center', va='bottom', fontsize=11, color='#555555')
        figure.tight_layout(rect=(0, (0.15 + 0.2 * len(lines)) / figure.get_figheight(), 1, 0.93))
        os.makedirs(os.path.dirname(path), exist_ok=True)
        figure.savefig(path, dpi=dpi, facecolor='white')
        plt.close(figure)
    return path


def elements_page(year: int, kg, elements: list, draws: int, path: str, dpi: int) -> str:
    """The elements in all robots in use at `year` (`kg`: draws × PARTS × elements), one page, exactly as
    RAWCLICDataCenters' 05 draws the elements of one data centre (split_elements_page): each bar split by the four
    groups of how a robot is taken apart, the sums of their parts draw by draw, in their order."""
    splits = {g: np.asarray(kg[:, [PARTS.index(p) for p in PARTS if GROUP_OF[p] == g]], dtype=np.float64).sum(axis=1)
              for g in GROUPS}
    note = (f'bars: the draws ({draws:,}), the height the share of the draws; solid line and number: the mean; dashed '
            'lines: 2.5th and 97.5th percentile (the 95% interval);\neach panel on its own scale and unit; each bar split '
            'into the kg of its draws in the joints, the battery, the electronics and the body; an element held in fewer '
            'than 2.5% of the draws is not drawn; its parts on the pages after')
    return split_elements_page(f'{year}: elements in all humanoid robots in use', splits, schemas.GROUP_COLOURS,
                               elements, note, path, dpi)


def parts_rows(kg, elements: list) -> list:
    """The rows of the list of the elements part by part at one year (`kg`: draws × PARTS × elements): for each
    element (02's order) each part that holds it in a draw at least, in the order of 01's parts, its group, the share of
    the draws that hold it, its median, mean and 95 % over those draws, in its own unit (mass_unit): 02's part_rows, one
    copy ("A 0 is not part of a distribution")."""
    return composition.part_rows({(composition.ELEMENT_NAMES.get(symbol, symbol), part): kg[:, j, e]
                                  for e, symbol in enumerate(elements) for j, part in enumerate(PARTS)}, unit=mass_unit)


def parts_pages(year: int, kg, elements: list, folder: str, dpi: int) -> list:
    """The list of the elements in all robots in use at `year`, part by part of how a robot is taken apart (Matthias,
    2026-11-08: "I want a detailed list of the component, so it is easy to understand and establish a recycling to know
    how to take it apart!!!"): a row for each element in each part that holds it (parts_rows), PARTS_ROWS a page, A4
    landscape as 04's pages, parts_<year>_<k>.png. Returns the pages written."""
    rows = parts_rows(kg, elements)
    pages = [rows[k:k + PARTS_ROWS] for k in range(0, len(rows), PARTS_ROWS)] or [[]]
    written = []
    for k, page_rows in enumerate(pages, 1):
        page = plt.figure(figsize=A4_LANDSCAPE)
        page.suptitle(f'{year}: elements in all humanoid robots in use, part by part'
                      + (f' ({k} of {len(pages)})' if len(pages) > 1 else ''))
        for x, words in zip(PARTS_COLUMNS, PARTS_HEAD):
            page.text(x, 0.91, words, fontsize=9, fontweight='bold', va='top')
        y = 0.87
        for row in page_rows:
            page.add_artist(plt.Line2D([0.02, 0.98], [y + 0.007, y + 0.007], color=composition.GRID, linewidth=0.8))
            for x, cell in zip(PARTS_COLUMNS, row):
                page.text(x, y, cell, fontsize=8, va='top')
            y -= 0.034
        page.text(0.5, 0.02, 'Each row: one element in one part of how a robot is taken apart, in all humanoid robots '
                  'in use at the end of the year; over the draws that hold it; each row in its own unit.',
                  ha='center', va='bottom', fontsize=8, color='#555555')
        path = os.path.join(folder, f'parts_{year}_{k}.png')
        os.makedirs(folder, exist_ok=True)
        page.savefig(path, dpi=dpi, facecolor='white')
        plt.close(page)
        written.append(path)
    return written


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
    draws = parts[TYPES[0]][1].shape[0]               # 02's draws of robot type 1 (all types the same)
    # Each type's point of its share's triangle, one capacity threshold and the three lifetime factors a draw (the
    # robots', the packs' and the joints', each its own random number), the same in every rerun.
    rng = np.random.default_rng([params.composition.seed, 4])
    z = rng.random((draws, len(TYPES) - 1))                 # types 1, 2, 4, 5 and 6: each its own random number
    threshold = triangle_ppf(rng.random(draws), *flow.battery_replaced_below)
    robot_factor = triangle_ppf(rng.random(draws), *flow.lifetime_factor)
    pack_factor = triangle_ppf(rng.random(draws), *flow.lifetime_factor)
    joint_factor = triangle_ppf(rng.random(draws), *flow.lifetime_factor)
    u_rest = rng.random(draws)                              # type 3's own random number, drawn last: the others stay
    # Step 2: every type its own triangle, the draws of the six put together so that they add up to 1.
    print(f'04: the robot types: each its own triangle, the six put together to add up to 1 (rearrangement) …')
    try:
        points, off = type_points(params, shares, z, u_rest)
    except ValueError as error:
        print(f'04 stopped: {error}')
        return 1
    print(f'04: the robot types put together; type {BALANCING_TYPE} off its own draws by at most {100 * off:.3f} % of its '
          'half-width')
    folder = absolute(params.output.stock_and_flow_dir)
    os.makedirs(folder, exist_ok=True)
    years = {flow_name: LAST - FIRST + 1 for flow_name in FLOWS}     # 2025 to 2040, as 07
    files = {}
    for unit_name, element_name, flow_name in zip(UNIT_FILES, ELEMENT_FILES, FLOWS):
        files[unit_name] = np.lib.format.open_memmap(os.path.join(folder, f'{unit_name}.npy'), mode='w+',
                                                     dtype=np.float32,
                                                     shape=(draws, years[flow_name], len(UNITS), len(TYPES)))
        files[element_name] = np.lib.format.open_memmap(os.path.join(folder, f'{element_name}.npy'), mode='w+',
                                                        dtype=np.float32,
                                                        shape=(draws, years[flow_name], len(PARTS), len(elements)))
    for article_name, flow_name in zip(ARTICLE_FILES, FLOWS):
        files[article_name] = np.lib.format.open_memmap(os.path.join(folder, f'{article_name}.npy'), mode='w+',
                                                        dtype=np.float32, shape=(draws, years[flow_name]))
    for first in range(0, draws, CHUNK):
        rows = slice(first, min(first + CHUNK, draws))
        counted, needs = count(params, shares, trajectories, points[rows], threshold[rows], robot_factor[rows],
                               pack_factor[rows], joint_factor[rows])
        faults = check(params, counted, needs)
        if faults:
            print(f'04 stopped: the stock and flow of draws {first + 1:,} to {rows.stop:,} does not add up; the draws '
                  f'in {folder} are incomplete.')
            for fault in faults:
                print(f'  {fault}')
            return 1
        by_year = {(unit, t): years_of(counted[(unit, t)]) for unit in UNITS for t in TYPES}
        for article_name, values in zip(ARTICLE_FILES, years_of(counted[('article', 0)])):
            files[article_name][rows] = values
        # One robot of each type in draw i: its kg in each unit, part and element (02's draw i, read for this chunk).
        n, size = rows.stop - rows.start, len(PARTS) * len(elements)
        one = {t: (np.asarray(parts[t][1][rows], dtype=np.float64) @ parts[t][0]).reshape(n, len(UNITS), size)
               for t in TYPES}
        for i, (unit_name, element_name) in enumerate(zip(UNIT_FILES, ELEMENT_FILES)):
            kg, product = np.zeros((n, years[FLOWS[i]], size)), np.empty((n, years[FLOWS[i]], size))
            for j, unit in enumerate(UNITS):
                for k, t in enumerate(TYPES):
                    values = by_year[(unit, t)][i]
                    files[unit_name][rows, :, j, k] = values
                    # Step 5: this type's units times the kg of each part they carry in draw i, added over the units
                    # and the types: a part of the joints with the joint sets, of the battery with the packs.
                    np.multiply(values[:, :, None], one[t][:, None, j, :], out=product)
                    kg += product
            files[element_name][rows] = kg.reshape(n, years[FLOWS[i]], len(PARTS), len(elements))
        print(f'04: draws {first + 1:,} to {rows.stop:,} of {draws:,} counted and checked')
    for array in files.values():
        array.flush()
    with open(os.path.join(folder, AXES_FILE), 'w', encoding='utf-8') as handle:
        handle.write(f"{', '.join(UNIT_FILES)}: draw; year {FIRST} to {LAST}, as RAWCLICDataCenters' 07 (in, out: the "
                     f"calendar year; stock: its end); unit ({', '.join(UNITS)}); robot type "
                     f"({', '.join(map(str, TYPES))})\n")
        handle.write(f"{', '.join(ARTICLE_FILES)}: draw; year (the same); the article's robots built, in use, retired "
                     "(each type its own share of the robots built)\n")
        handle.write(f"{', '.join(ELEMENT_FILES)}: draw; year (the same); part of how a robot is taken apart "
                     f"({', '.join(f'{p} ({GROUP_OF[p]})' for p in PARTS)}); element ({', '.join(elements)}); kg\n")
    # The summary, over the draws above 0: every unit of all types and of each type; every element of all three parts.
    summary = {}
    for unit_name, flow_name in zip(UNIT_FILES, FLOWS):
        values = np.array(files[unit_name], dtype=np.float64)
        for j, unit in enumerate(UNITS):
            # All robots: the article's (each type its own share of them, not their sum); joint sets and packs: the
            # types' added up.
            total = (np.array(files[ARTICLE_FILES[FLOWS.index(flow_name)]], dtype=np.float64) if unit == 'robots'
                     else values[:, :, j, :].sum(axis=2))
            summary[(unit, 0, flow_name)] = stats_of(total)
            for k, t in enumerate(TYPES):
                summary[(unit, t, flow_name)] = stats_of(values[:, :, j, k])
    # Each type's share of the robots built in a year, %, draw by draw (Matthias, 2026-11-07, the panel "Add it
    # beside" the robots in use by type): its robots built over the article's robots built, its own drawn share.
    built = np.array(files['units_in'][:, :, UNITS.index('robots'), :], dtype=np.float64)
    article_built = np.array(files['article_in'], dtype=np.float64)
    for k, t in enumerate(TYPES):
        summary[(SHARE_QUANTITY, t, 'in')] = stats_of(100 * built[:, :, k] / article_built)
    # Every element in all, by group and by part of how a robot is taken apart, each over its draws above 0.
    summary.update(element_summary(files, elements))
    with open(os.path.join(folder, SUMMARY), 'w', newline='', encoding='utf-8') as handle:
        writer = csv.writer(handle)
        writer.writerow(('quantity', 'robot type', 'flow', 'year', 'mean', '2.5 %', '97.5 %',
                         'held in % of the draws'))
        for (what, which, flow_name), stats in summary.items():
            if what == 'element':
                quantity, robot_type = composition.ELEMENT_NAMES.get(which, which), 'all'
            elif what == 'element group':                                        # 'Copper, Electronics'
                quantity, robot_type = f'{composition.ELEMENT_NAMES.get(which[0], which[0])}, {which[1]}', 'all'
            elif what == 'element part':                                         # 'Copper, Electronics: Small PCB'
                quantity = f'{composition.ELEMENT_NAMES.get(which[0], which[0])}, {GROUP_OF[which[1]]}: {which[1]}'
                robot_type = 'all'
            else:
                quantity, robot_type = what, which if which else 'all'
            for i in range(len(stats['mean'])):
                cells = [f'{stats[key][i]:.6g}' if np.isfinite(stats[key][i]) else '–'
                         for key in ('mean', 'low', 'high')]
                # The year as 07: a flow its calendar year, a stock the end of the year.
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
        # The distribution pages, each followed by its numbers.
        distributions = os.path.join(figures, DISTRIBUTIONS_DIR)
        written = robots_in_use_page(files, draws, distributions, params.output.dpi)
        for year in DISTRIBUTION_YEARS:                             # the elements, a page a year, as 05's
            stock = np.asarray(files['elements_stock'][:, year - FIRST], dtype=np.float64)   # draws × parts × elements
            written.append(elements_page(year, stock, elements, draws,
                                         os.path.join(distributions, f'elements_{year}.png'), params.output.dpi))
            # Then the list of its elements part by part (Matthias, 2026-11-08, "Yes do it").
            written += parts_pages(year, stock, elements, distributions, params.output.dpi)
    print(f'04: {len(written)} distribution pages and their numbers in {distributions}.')
    without = [composition.ELEMENT_NAMES.get(s, s) for s in held if s not in world]
    if without:
        print(f"04: no world production or reserves for {', '.join(without)}; their pages say so.")
    robots = [float(f'{v:.7g}') for v in summary[('robots', 0, 'stock')]['mean']]     # float32: 7 digits
    print(f'04 done: {draws:,} draws; robots in use at the end of {FIRST} {robots[0]:,.0f}, of {LAST} {robots[-1]:,.0f} (mean); '
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
