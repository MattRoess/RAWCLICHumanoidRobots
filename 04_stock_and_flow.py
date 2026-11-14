"""
04_stock_and_flow.py
====================

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

The stock and flow of the humanoid robots in the world and of the critical and strategic elements in them, quarter by
quarter from 2025 Q1 to 2040 Q4, reported by calendar year with the stocks at the end of each year, exactly as
RAWCLICDataCenters' 08 follows the world's data centres, so that both can be combined (Matthias, 2026-11-08: "Both have
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
    ElementReference (`data.data_center_scenarios`, the values 08 draws), and USGS's data file (`data.usgs_commodities`)
    for magnesium, titanium and indium, which that sheet does not hold; both read where they lie.

HOW IT COUNTS (every draw; quarter by quarter, as 08)
-------------
  1. The robots: in use at the end of each quarter, the article's values at the end of their years, the quarters
     between geometric
     (V(y)^(1 − k/4) × V(y + 1)^(k/4), as 08). Each quarter's robots arrive in its middle and leave by the share of
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
     08's units that follow the GPUs: a stock target with their own lifetimes.
  4. The battery packs: a robot holds as many as one day's work needs, the hours a day over a pack's runtime, rounded
     up (types 2, 4 and 6 their runtime in the workbook; types 1, 3 and 5 the setting's runtime of 2025 times their
     battery energy density over that of 2025; a straight line between the workbook's years, the last value held after
     it). Each pack is charged once a day and replaced when its capacity falls below the draw's share: its life in
     charges, its charges to 80 % (spread among the packs, times the draw's own factor from the triangle 0.7 / 1 /
     1.2: "Also with the batteries") times (1 − the share) / 0.2, a straight-line fade (an approximation). A stock target, as the joint sets: the robots in use times the packs a robot needs. Where that
     need falls (longer runtimes), the packs in use stay until they wear out and the stock lies above the need.
     08's approximation in both: the joint sets and the packs of a retired robot go on in a new robot until they wear
     out, which makes their inflow and outflow slightly low.
  5. The elements: every flow and stock of robots, joint sets and packs of a type times one robot's kg of each element
     in 02's draw i: a robot its body (every kind of part but the joints and the battery pack), a joint set the joint
     kinds, a pack the kind Battery pack (02 builds one pack a robot). Sums on the raw draws, before any statistic.
  6. The years, as 08's: the flows added up over the four quarters of each calendar year, 2025 to 2040; the stocks
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
retired, at the draw's lifetime); their axes in draws.txt; summary.csv, each quantity's median, 25 % and 75 % (the middle half) and 2.5 % and 97.5 % over
the draws above 0 and the share of the draws above 0, by year (as 08: a flow its calendar year, a stock the year's end), each element also by group
('Copper, Electronics') and by part ('Copper, Electronics: Small PCB'). The elements of one robot type are its units
times 02's draw i, each part with the unit that carries it (a joint's with the joint sets, the battery's with the packs,
every other with the robots).
Into `output.stock_and_flow_figures_dir` (`figures/stock_and_flow/`; not in git), as RAWCLICDataCenters' 08 draws its
own (FigureTests' rules 1 to 11; Matthias, 2026-11-13: "test all the figures", "Yes, 1 to 7"), each an A4 landscape page
at the dpi of the settings: overview.png (the robots in use; built and retired; in use by robot type; the share of the
robots built by robot type; the joint sets; the battery packs in use; built and worn out) and elements/<Element>.png
(what is in use beside the world's reserves; what is added and removed per year beside the world's mine production in
2025). Each line the median of the runs above 0, its middle half the darker band, where 95 of 100 runs lie the lighter;
logarithmic axes; one legend below the panels, the uncertainty as its grey samples; a foot of at most three sentences. An element 0 in every draw has no page, and 04 says so. In distributions/ (Matthias, 2026-11-07: "I also want the
distributions"; 2026-11-08: "Exactkly the figures we have worked out for the data centers!!!", "Sorry end of goes away"):
robots_in_use.png (the robots in use of 2025, 2030, 2035 and 2040, a panel a year, the six types one above the other,
every draw on the axis, the robots in all in the title; followed by robots_in_use_numbers.png) and elements_<year>.png
for 2025, 2030, 2035 and 2040, each exactly as RAWCLICDataCenters' 05 draws the elements of one data centre: a panel per
element held in all robots in use, its draws' distribution, each bar split into the four groups of how a robot is taken
apart (joints, battery, electronics, body), the median a line with its number, the 95 % interval dashed, each group's
median under the title; each followed by parts_<year>_<k>.png, every element in each of the 14 parts that holds it (2026-11-08, "I want a
detailed list of the component ... to know how to take it apart!!!").
Every figure a result of the run, never an input (GitHub/CLAUDE.md §5).

Where it sits: after 03_comparison.py; it reads 02's draws and nothing of 03.
"""

from __future__ import annotations

import csv
import gc
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

# The years as RAWCLICDataCenters' 08 counts them (Matthias, 2026-11-08: "Both have to be exactly the same, as we have
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
# Draws counted at once: the memory of the counting grows with it, not with the draws (each chunk's kg of every part
# and element over the years, some 0.8 GB at 5,000; 10,000 until 2026-11-14, which the rule's measurements at 5,000
# and 20,000 draws read as growing with the draws: VERIFICATION.md V222, V237). The results the same.
CHUNK = 5000
TOLERANCE = 1e-9                  # of the largest stock: a balance that misses by more is a fault (08's check_balance)

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
    shorter than x (as 08's triangle_cdf)."""
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
    its year (Matthias, 2026-11-08: "Follow the artcile!! 70 x 10E9"), geometric between (as 08): V(y − 1)^(1 − k/4) ×
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
    """One stock, quarter by quarter, as 08's follow_target. `survive` (one row for all draws, or n rows, one a draw):
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
    needed. Each to TOLERANCE of the largest stock (08's check_balance)."""
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
    """A stock by year, as 08's to_years: (inflow n × 16, the calendar years 2025 to 2040; the stock at the end of each
    year, n × 16; outflow n × 16), the order of FLOWS."""
    n = f.built.shape[0]
    return f.built.reshape(n, -1, 4).sum(axis=2), f.stock[:, 3::4], f.gone.reshape(n, -1, 4).sum(axis=2)


# ------------------------------------------------------------------------------------------------------
# The world's production and reserves (the figures' dashed lines)
# ------------------------------------------------------------------------------------------------------

def references(params: Params) -> tuple:
    """The world's production in 2025 (kg a year) and reserves (kg) of each element: ({element: {'production' |
    'reserves': (min, mode, max, at least)}}, {element: [what the foot says of it]}): RAWCLICDataCenters' sheet
    ElementReference as 08 reads it (t in the sheet; its note where it adds to the source), and USGS_ROWS from USGS's
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
# The summary: over the runs above 0 ("A 0 is not part of a distribution")
# ------------------------------------------------------------------------------------------------------

STATISTICS = ('median', 'p25', 'p75', 'low', 'high')    # the median, the middle half and where 95 of 100 runs lie


def stats_of(values: np.ndarray) -> dict:
    """Per column of `values` (runs × columns), over the runs above 0: the median, the 25 % and 75 % (the middle half of
    the runs), the 2.5 % and 97.5 % (where 95 of 100 lie), and the share of the runs above 0 ('held'); NaN where no run
    is above 0. The median, not the mean (Matthias, 2026-11-10: "Not mean, but median"; RAWCLICDataCenters' 08)."""
    median, p25, p75, low, high, held = column_stats(values)
    return {'median': median, 'p25': p25, 'p75': p75, 'low': low, 'high': high, 'held': held}


def column_stats(values: np.ndarray) -> tuple:
    """For every column of `values` (runs × columns) at once, over the runs above 0: (the median, the 25 %, 75 %, 2.5 %
    and 97.5 % percentiles, the share of the runs above 0), NaN where no run is above 0 (numpy's percentiles)."""
    above = values > 0
    masked = np.where(above, values, np.nan)
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', RuntimeWarning)          # a column with no run above 0: NaN
        median, p25, p75, low, high = np.nanpercentile(masked, (50, 25, 75, 2.5, 97.5), axis=0)
    return median, p25, p75, low, high, above.mean(axis=0)


# The elements of an element file read at a time by element_summary (2 at least, so that the parts are added up as
# when all were read): its memory grows with them and the draws, some 0.3 GB at 200,000 draws (VERIFICATION V237).
SUMMARY_ELEMENTS = 2


def element_summary(files: dict, elements: list) -> dict:
    """Every element in all, by group and by part, each flow and year, over the runs above 0 (as stats_of): one year
    and SUMMARY_ELEMENTS elements of an element file read at a time (runs × parts × those elements; until 2026-11-14 a
    year with all elements, some 3 GB at 200,000 draws with the statistics), its groups the sums of their parts run by
    run, its total the sum of all parts. Keys ('element', symbol, flow), ('element group', (symbol, group), flow) and
    ('element part', (symbol, part), flow), each {'median', 'p25', 'p75', 'low', 'high', 'held'} over the years."""
    years = LAST - FIRST + 1
    members = [[PARTS.index(p) for p in PARTS if GROUP_OF[p] == g] for g in GROUPS]
    out = {}
    for element_name, flow_name in zip(ELEMENT_FILES, FLOWS):
        keys = ([('element', e, flow_name) for e in elements]
                + [('element group', (e, g), flow_name) for g in GROUPS for e in elements]
                + [('element part', (e, p), flow_name) for p in PARTS for e in elements])
        for key in keys:
            out[key] = {name: np.full(years, np.nan) for name in STATISTICS}
            out[key]['held'] = np.zeros(years)
        for y in range(years):
            # the elements in groups of SUMMARY_ELEMENTS, a last one left alone joining the group before it
            starts = list(range(0, len(elements), SUMMARY_ELEMENTS))
            if len(starts) > 1 and len(elements) - starts[-1] < 2:
                starts.pop()
            for first, stop in zip(starts, starts[1:] + [len(elements)]):
                these = elements[first:stop]
                block = np.array(files[element_name][:, y, :, first:first + len(these)], dtype=np.float64)
                columns = np.concatenate([block.sum(axis=1)] + [block[:, idx].sum(axis=1) for idx in members]
                                         + [block[:, j] for j in range(len(PARTS))], axis=1)   # runs × parts × these
                its_keys = ([('element', e, flow_name) for e in these]
                            + [('element group', (e, g), flow_name) for g in GROUPS for e in these]
                            + [('element part', (e, p), flow_name) for p in PARTS for e in these])
                for key, *numbers in zip(its_keys, *column_stats(columns)):
                    for name, value in zip(STATISTICS + ('held',), numbers):
                        out[key][name][y] = value
                del block, columns
    return out


# ------------------------------------------------------------------------------------------------------
# The figures, as RAWCLICDataCenters' 08 draws its own (Matthias, 2026-11-13: "test all the figures", "Yes, 1 to 7";
# FigureTests' rules 1 to 11 of 2026-11-12 and his rule "Robots exactly as the data centres")
# ------------------------------------------------------------------------------------------------------

# Every figure one landscape A4 page with 08's print fonts (Matthias, 2026-10-22, for the data centres: "I want that the
# figures look great on a landscpae A4 page"): titles 11 pt, axes and legends 9 pt (rule 9 of 2026-11-12).
A4_LANDSCAPE = (297 / 25.4, 210 / 25.4)                    # inches
PRINT_STYLE = {'font.size': 9, 'axes.titlesize': 11, 'axes.labelsize': 9, 'xtick.labelsize': 9, 'ytick.labelsize': 9,
               'legend.fontsize': 9, 'legend.title_fontsize': 9, 'figure.titlesize': 13, 'lines.linewidth': 1.4,
               # the years 7 points below the axis, clear of the lowest number of the mass axis beside them (matplotlib's
               # 3.5 until 2026-11-13: in Luciole '2025' stood 1.4 to 4 points from '100 kg'; FigureTests' text_gap)
               'xtick.major.pad': 7.0}
# The colours of the three quantities and of the six robot types, from published schemes (Paul Tol's bright, vibrant and
# muted, and Okabe & Ito's), chosen 2026-11-13 by FigureTests' colour rules (Matthias: "B", "Yes, build the three rules
# as proposed"): every two of the three, and every two of the six, told apart by red-green colour-blind readers (at
# least 10.5 in CAM02-UCS, the weakest pair 21.5) and by readers with normal vision (at least 21); every type at least 21
# from every quantity, so that no colour means two things on the overview; each at least 2 : 1 against the white page.
# In use Tol's muted indigo, built or added Tol's bright green, retired, worn out or removed Okabe-Ito's reddish purple;
# the types Okabe-Ito's blue, Tol's vibrant cyan, Tol's muted teal, Okabe-Ito's orange, Tol's vibrant red and Tol's
# muted wine. Until 2026-11-13: in use '#4477AA', retired '#EE6677', the types Tol's muted indigo to purple, two of them
# too close for normal vision (wine and purple, 17.3).
IN_USE, BUILT, GONE = '#332288', '#228833', '#CC79A7'
TYPE_COLOURS = ('#0072B2', '#33BBEE', '#44AA99', '#E69F00', '#CC3311', '#882255')
UNCERTAINTY = '0.35'                     # the grey of the samples of the uncertainty: median, 50 % and 95 % intervals
PRODUCTION_STYLE, RESERVES_STYLE = '--', ':'               # the world's mine production dashed, its reserves dotted
# The world's source as the data centres' figures name it (its version, 1.3, in EVIDENCE.md: "ver. 1.3" would end a
# sentence of the foot for the rule of three sentences)
WORLD_SOURCE = 'U.S. Geological Survey, Mineral Commodity Summaries 2026'
FOOT_WIDTH = 170                         # characters a line of a page's foot (08's save_figure)
TOGETHER = 0.10                          # two lines less than this share apart lie on one another (FigureTests)
UNDER_WORDS = ('Where a line is not visible, it lies under the line drawn after it: the two do not differ there.')
# The sentences at the foot (rule 6: at most three)
AMOUNTS = ('Amounts added or removed are per year, amounts in use at the end of the year; each step of a scale is ten '
           'times the one below.')                                                    # the element pages, 04's and 05's
ROBOT_AMOUNTS = ('Amounts built, retired or worn out are per year, amounts in use at the end of the year; each step of a '
                 'scale is ten times the one below.')                                  # the overview
ROBOTS_FROM = ('The robots in use are the ai-2040 article\'s at the end of each year; each robot of the six types is one '
               'model run of its type, with its joints, battery, electronics and body.')


def decade_label(value: float, _position=None) -> str:
    """A tick of a log axis of numbers: the decade as 10 to its power ('$10^{6}$', drawn 10⁶), a few characters wide,
    as 08's decade_label (Matthias, 2026-11-13, on the numbers written out in full that morning, '100,000,000,000': "the
    y axis scales are shit they use all the space")."""
    return f'$10^{{{int(round(np.log10(value)))}}}$'


def mass_label(value_kg: float, _position=None) -> str:
    """A tick of a log axis of kg: the power of ten in the unit that writes it as 1, 10 or 100 ('1 kt', '100 t'), as
    the data centres write them (kg, not Mg)."""
    power = int(round(np.log10(value_kg)))
    for base, unit in ((9, 'Mt'), (6, 'kt'), (3, 't'), (0, 'kg'), (-3, 'g')):
        if power >= base:
            return f'{10 ** (power - base):,} {unit}'
    return f'{10.0 ** (power + 3):g} g'


def mass_text(value_kg: float) -> str:
    """A mass written in a figure: three significant digits in the unit that writes it from 1 up ('980 Mt', '55 kt',
    '190 t'; Mt the largest; "4000 not 4k"), as the data centres' mass_text."""
    for factor, unit in ((1e9, 'Mt'), (1e6, 'kt'), (1e3, 't'), (1.0, 'kg'), (1e-3, 'g')):
        if value_kg >= factor or unit == 'g':
            v = float(f'{value_kg / factor:.3g}')
            return f'{v:,.0f} {unit}' if v >= 100 else f'{v:g} {unit}'
    return ''


def log_panel(axes, series: list, word: str, tick_label=decade_label) -> bool:
    """One panel on a log axis, as 08's log_panel: each of `series` (years, stats of stats_of, colour, line style) as its
    median, its middle half (the darker band) and where 95 of 100 runs lie (the lighter band), `word` the axis label.
    The statistics are over the runs above 0: a year in which not every run holds it has an open circle on the line, and
    each share is written once, beside the first circle that has it ('56 %'), not at every point; a year in which no run holds it has no point. A log axis has no 0: a band that reaches
    0 runs to the foot of the panel, half the smallest value above 0. A panel with nothing above 0 is not drawn ("0 is
    0"). Returns whether it was drawn."""
    values = np.concatenate([np.concatenate([s[1]['median'], s[1]['low']]) for s in series])
    positive = values[np.isfinite(values) & (values > 0)]
    if not positive.size:
        axes.set_visible(False)
        return False
    foot = float(positive.min()) / 2.0
    for years, stats, colour, style in series:
        shown = np.isfinite(stats['median']) & (stats['median'] > 0)
        axes.plot(years, np.where(shown, stats['median'], np.nan), style, color=colour)
        band = lambda a: np.where(np.isfinite(a) & (a > 0), a, foot)                          # noqa: E731
        axes.fill_between(years, band(stats['low']), band(stats['high']), where=shown, alpha=0.12, color=colour,
                          linewidth=0)
        axes.fill_between(years, band(stats['p25']), band(stats['p75']), where=shown, alpha=0.3, color=colour,
                          linewidth=0)
        part = shown & (stats['held'] < 0.995)               # held in some runs only: an open circle and the share
        if part.any():
            xs, ys, shares = np.asarray(years)[part], stats['median'][part], stats['held'][part]
            axes.plot(xs, ys, 'o', mfc='white', mec=colour, ms=4, mew=1, linestyle='None')
            # Each share written once on its line, at the first circle that has it (Matthias, 2026-11-13: "I do not need
            # so much numbers for each point espeially if they are the same. Do not label every point!!!"; FigureTests'
            # rule repeated_label); beside its circle, where exactly found when the page is laid out (place_labels, in
            # save_figure).
            written = set()
            for x, y, h in zip(xs, ys, shares):
                text = composition.share_text(h)
                if text not in written:
                    axes.annotate(text, (x, y), xytext=(3, 3), textcoords='offset points', fontsize=8,
                                  color=composition.readable(colour), gid='beside')     # its line's hue, readable
                    written.add(text)
    axes.set_xlim(FIRST, LAST)
    axes.xaxis.set_major_locator(ticker.MultipleLocator(5))   # whole years, every fifth (rule 10 of 2026-11-12)
    axes.set_yscale('log')
    axes.set_ylim(bottom=foot)
    axes.yaxis.set_major_locator(ticker.LogLocator(base=10))
    axes.yaxis.set_major_formatter(ticker.FuncFormatter(tick_label))
    axes.yaxis.set_minor_formatter(ticker.NullFormatter())
    axes.set_ylabel(word)
    return True


def share_panel(axes, series: list, word: str) -> None:
    """One panel on a plain axis from 0, for shares in %: each of `series` (years, stats of stats_of, colour, line style)
    its median a line, its middle half the darker band and where 95 of 100 runs lie the lighter one (Matthias,
    2026-11-07: each type's range "one has to see it")."""
    for years, stats, colour, style in series:
        axes.plot(years, stats['median'], style, color=colour)
        axes.fill_between(years, stats['low'], stats['high'], alpha=0.12, color=colour, linewidth=0)
        axes.fill_between(years, stats['p25'], stats['p75'], alpha=0.3, color=colour, linewidth=0)
    axes.set_xlim(FIRST, LAST)
    axes.xaxis.set_major_locator(ticker.MultipleLocator(5))
    axes.set_ylim(bottom=0)
    axes.set_ylabel(word)


def world_reference(axes, value: tuple | None, name: str, per_year: bool) -> None:
    """The world's production (kg a year, dashed) or reserves (kg, dotted) in a panel drawn by log_panel, as 08's
    world_reference: within the panel's scale a black line, the width of the panel's lines (its min to max, where they
    differ, a grey band), the axis unchanged; outside it the value written in the panel, at its top where above the
    scale, at its foot where below."""
    if value is None or not axes.get_visible():
        return
    low, mode, high, at_least = value
    bottom, top = axes.get_ylim()
    text = mass_text(mode) if low == high else f'{mass_text(low)} to {mass_text(high)}'
    text = f"{name}: {'at least ' if at_least else ''}{text}{' per year' if per_year else ''}"
    if bottom <= mode <= top:
        left, right = axes.get_xlim()
        axes.plot([left, right], [mode, mode], PRODUCTION_STYLE if per_year else RESERVES_STYLE, color='black')
        if high > low:
            axes.fill_between([left, right], max(low, bottom), min(high, top), color='0.5', alpha=0.15, linewidth=0)
        axes.set_xlim(left, right)
        axes.set_ylim(bottom, top)
        return
    above = mode > top
    axes.text(0.98, 0.97 if above else 0.03, f"{text}, {'above' if above else 'below'} the scale",
              transform=axes.transAxes, ha='right', va='top' if above else 'bottom', fontsize=8, color='0.2')


def line_handle(label: str, colour, style: str = '-'):
    """The legend sample of a line: its colour and style, named in words."""
    return plt.Line2D([], [], color=colour, linestyle=style, label=label)


def uncertainty_handles(draws: int, figure=None) -> list:
    """The samples of the uncertainty (rule 4), as 08's: the median of the runs, the 50 % and the 95 % interval, and,
    when `figure` draws an open circle, what it means."""
    handles = [plt.Line2D([], [], color=UNCERTAINTY, label=f'Median of {draws:,} model runs'),
               Patch(color=UNCERTAINTY, alpha=0.3, label='50 % interval'),
               Patch(color=UNCERTAINTY, alpha=0.12, label='95 % interval')]
    circles = [line for axes in (figure.axes if figure is not None else []) for line in axes.lines
               if line.get_marker() == 'o' and str(line.get_markerfacecolor()).lower() in ('white', '#ffffff', 'w')]
    if circles:
        handles.append(plt.Line2D([], [], marker='o', markerfacecolor='white', color=circles[-1].get_markeredgecolor(),
                                  linestyle='None', label='Not every run has it that year (number: share of runs with it)'))
    return handles


def world_handles(figure) -> list:
    """The samples of the world's lines a figure draws: its mine production of 2025 dashed, its reserves dotted."""
    drawn = {line.get_linestyle() for axes in figure.axes for line in axes.lines
             if plt.matplotlib.colors.to_hex(line.get_color()) == '#000000'}
    out = []
    if PRODUCTION_STYLE in drawn:
        out.append(line_handle('World mine production of 2025', 'black', PRODUCTION_STYLE))
    if RESERVES_STYLE in drawn:
        out.append(line_handle('World reserves', 'black', RESERVES_STYLE))
    return out


def lies_under(line, later: list) -> bool:
    """Whether `line` lies under a line drawn after it (another colour or style, less than TOGETHER apart at the same
    years) at three or more years in a row, or at every year: one cannot see it there, so the page says so in a sentence
    (UNDER_WORDS; Matthias, 2026-11-11, for the data centres: "where the hell are the green and blue dashed lines")."""
    x, y = (np.asarray(v, dtype=float) for v in (line.get_xdata(), line.get_ydata()))
    hidden = np.zeros(len(x), dtype=bool)
    for other in later:
        if (other.get_color(), other.get_linestyle()) == (line.get_color(), line.get_linestyle()):
            continue
        ox, oy = (np.asarray(v, dtype=float) for v in (other.get_xdata(), other.get_ydata()))
        _, i, j = np.intersect1d(x, ox, return_indices=True)
        a, b = y[i], oy[j]
        close = np.isfinite(a) & np.isfinite(b) & (np.abs(a - b) <= TOGETHER * np.maximum(np.abs(a), np.abs(b)))
        hidden[i[close]] = True
    finite = np.isfinite(y)
    run = longest = 0
    for h in hidden:
        run = run + 1 if h else 0
        longest = max(longest, run)
    return bool(finite.any() and hidden[finite].all()) or longest >= 3


def under_words(figure) -> str:
    """UNDER_WORDS where a line of a panel lies under a later one (lies_under), else ''."""
    for axes in figure.axes:
        # the lines drawn as lines: not the open circles of log_panel (markers on the median, the same values) nor a
        # vertical mark
        lines = [line for line in axes.lines if line.get_linestyle() not in ('None', '', ' ')
                 and len(np.unique(np.asarray(line.get_xdata(), dtype=float))) > 1]
        if any(lies_under(line, lines[k + 1:]) for k, line in enumerate(lines)):
            return UNDER_WORDS
    return ''


def save_figure(figure, path: str, note: str, dpi: int, handles: list | None = None, ncol: int = 3) -> str:
    """Write a page and close it, by the rules for science presentations (Matthias, 2026-11-12, "yes, 1 to 11"), as 08's
    save_figure: the one legend of the page (`handles`) below the panels, outside them; under it the foot, at most three
    sentences: the sentence on lines lying under others when there are any (under_words) and `note`. The foot and the
    legend are measured: the legend has `ncol` columns, or fewer where it would run out of the page, and the panels
    start above its measured top."""
    lines = textwrap.wrap(' '.join(x for x in (under_words(figure), note.strip()) if x), FOOT_WIDTH)
    foot = figure.text(0.5, 0.008, '\n'.join(lines), ha='center', va='bottom', fontsize=8.5)
    renderer = figure.canvas.get_renderer()
    to_figure = figure.transFigure.inverted()
    bottom = foot.get_window_extent(renderer).transformed(to_figure).y1 + 0.008
    if handles:
        for columns in range(ncol, 0, -1):
            legend = figure.legend(handles=handles, loc='lower center', bbox_to_anchor=(0.5, bottom), ncol=columns,
                                   frameon=False, fontsize=9)
            box = legend.get_window_extent(renderer).transformed(to_figure)
            if (box.x0 >= 0.005 and box.x1 <= 0.995) or columns == 1:
                break
            legend.remove()                                    # too wide for the page: one column fewer
        bottom = box.y1 + 0.012
    figure.tight_layout(rect=(0, bottom, 1, 0.97 if figure._suptitle is not None else 1))
    place_labels(figure)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    figure.savefig(path, dpi=dpi, facecolor='white')
    plt.close(figure)
    gc.collect()   # the pages closed before: a figure refers to itself through its parts, so only the
    #                collector frees it and its image of 52 MB (VERIFICATION V237)
    return path


# Where a share beside an open circle may stand, in points for 6-point text (scaled to its size): 08's SHARE_PLACES, and
# four further from the point for a point at the panel's left edge, where every place of 08's was on the line or outside
# (indium's first year on 05's pages, 2026-11-13)
SHARE_PLACES = ((3, 3), (3, -9), (-3, 3), (-3, -9), (3, 11), (3, -17), (-3, 11), (-3, -17), (9, -3), (-9, -3),
                (3, 19), (3, -25), (12, 11), (12, -17))


def place_labels(figure) -> None:
    """Move every label beside a point (an annotation with gid 'beside') to the first of SHARE_PLACES, scaled to its
    font, where it lies on no line of its panel, on no other text and inside the panel; a label that says the same as one
    already at its point is not written twice (08's place_labels: one design for both projects)."""
    figure.canvas.draw()
    renderer = figure.canvas.get_renderer()
    for axes in figure.axes:
        labels = [t for t in axes.texts if t.get_gid() == 'beside']
        if not labels:
            continue
        points = []
        for line in axes.lines:
            xy = np.asarray(line.get_xydata(), dtype=float)
            xy = xy[np.all(np.isfinite(xy), axis=1)]
            if line.get_linestyle() in ('None', '', ' ') or len(xy) < 2:
                continue
            pts = axes.transData.transform(xy)
            steps = np.maximum(1, (np.hypot(*np.diff(pts, axis=0).T) / 3).astype(int))
            points.append(np.vstack([np.linspace(pts[i], pts[i + 1], steps[i], endpoint=False)
                                     for i in range(len(pts) - 1)] + [pts[-1:]]))
        points = np.vstack(points) if points else np.zeros((0, 2))
        frame = axes.get_window_extent(renderer)
        taken = [t.get_window_extent(renderer) for t in axes.texts if t.get_gid() != 'beside' and t.get_text().strip()]
        # and the numbers of every axis of the page (a share stood on an axis number of 05's page, 2026-11-13)
        taken += [t.get_window_extent(renderer) for other in figure.axes for axis in (other.xaxis, other.yaxis)
                  for t in axis.get_ticklabels() if t.get_visible() and t.get_text().strip()]
        written = set()
        for label in labels[::-1]:            # the label of the line drawn last first: the line one sees (rule 3)
            key = (label.xy, label.get_text())
            if key in written:
                label.set_visible(False)
                continue
            written.add(key)
            grow = label.get_fontsize() / 6.0                  # the places are for 6 pt; a larger label stands further
            fallback = None                     # the first place inside the panel on no text, should every place be
            for dx, dy in SHARE_PLACES:         # on a line (a point at the panel's edge: found 2026-11-13)
                label.set_position((dx * grow, dy * grow))
                label.set_ha('left' if dx >= 0 else 'right')
                box = label.get_window_extent(renderer)
                inside = frame.x0 <= box.x0 and box.x1 <= frame.x1 and frame.y0 <= box.y0 and box.y1 <= frame.y1
                on_line = ((points[:, 0] > box.x0) & (points[:, 0] < box.x1)
                           & (points[:, 1] > box.y0) & (points[:, 1] < box.y1)).any()
                on_text = any(box.overlaps(b) for b in taken)
                if inside and not on_text and fallback is None:
                    fallback = (dx, dy)
                if inside and not on_line and not on_text:
                    break
            else:
                if fallback is not None:
                    label.set_position((fallback[0] * grow, fallback[1] * grow))
                    label.set_ha('left' if fallback[0] >= 0 else 'right')
            taken.append(label.get_window_extent(renderer))


def overview_page(summary: dict, names: dict, draws: int, path: str, dpi: int) -> str:
    """The overview, two rows of four: the robots in use; built and retired; in use by robot type; beside it each type's
    share of the robots built (Matthias, 2026-11-07, "Add it beside"); the joint sets; the battery packs in use; built
    and worn out. Every line the median of the runs with its 50 % and 95 % intervals; one legend below the panels, the
    robot types named in it (rule 2)."""
    years = np.arange(FIRST, LAST + 1)                     # every year at its year, as 08

    def line(unit, t, flow, colour):
        return years, summary[(unit, t, flow)], colour, '-'

    figure, grid = plt.subplots(2, 4, figsize=A4_LANDSCAPE)
    panels = (
        (grid[0, 0], 'Robots in use', [line('robots', 0, 'stock', IN_USE)], 'robots'),
        (grid[0, 1], 'Robots built and retired', [line('robots', 0, 'in', BUILT), line('robots', 0, 'out', GONE)],
         'robots per year'),
        (grid[0, 2], 'Robots in use by robot type', [line('robots', t, 'stock', TYPE_COLOURS[k])
                                                     for k, t in enumerate(TYPES)], 'robots'),
        (grid[1, 0], 'Joint sets', [line('joint sets', 0, 'stock', IN_USE), line('joint sets', 0, 'in', BUILT),
                                    line('joint sets', 0, 'out', GONE)], 'joint sets, or joint sets per year'),
        (grid[1, 1], 'Battery packs in use', [line('battery packs', 0, 'stock', IN_USE)], 'battery packs'),
        (grid[1, 2], 'Battery packs built and worn out', [line('battery packs', 0, 'in', BUILT),
                                                          line('battery packs', 0, 'out', GONE)],
         'battery packs per year'))
    for axes, title, series, word in panels:
        if log_panel(axes, series, word):
            axes.set_title(title)
    share_panel(grid[0, 3], [line(SHARE_QUANTITY, t, 'in', TYPE_COLOURS[k]) for k, t in enumerate(TYPES)],
                '% of the robots built')
    grid[0, 3].set_title('Share by robot type')                  # its axis: % of the robots built
    grid[1, 3].axis('off')
    handles = [line_handle('In use (at the end of the year)', IN_USE), line_handle('Built per year', BUILT),
               line_handle('Retired or worn out per year', GONE)]
    handles += [line_handle(f'Robot type {t}: {names[t]}', TYPE_COLOURS[k]) for k, t in enumerate(TYPES)]
    figure.suptitle('Humanoid robots in the world')
    note = (ROBOT_AMOUNTS + ' ' + ROBOTS_FROM[:-1] + '; a joint set is the hip, knee, ankle, waist, arm and head joints '
            'of one robot.')
    return save_figure(figure, path, note, dpi, handles + uncertainty_handles(draws, figure), ncol=3)


def element_page(symbol: str, summary: dict, world: dict, notes: list, draws: int, path: str, dpi: int) -> str:
    """One element, as 08's element figure: what is in use beside the world's reserves; what is added and removed per
    year beside the world's mine production in 2025 (no "collected": the robots have none yet). One legend below."""
    years = np.arange(FIRST, LAST + 1)                     # every year at its year, as 08
    figure, (left, right) = plt.subplots(1, 2, figsize=A4_LANDSCAPE)
    if log_panel(left, [(years, summary[('element', symbol, 'stock')], IN_USE, '-')], '', mass_label):
        left.set_title('In use')
        world_reference(left, world.get('reserves'), 'World reserves', per_year=False)
    if log_panel(right, [(years, summary[('element', symbol, 'in')], BUILT, '-'),
                         (years, summary[('element', symbol, 'out')], GONE, '-')], 'per year', mass_label):
        right.set_title('Added and removed per year')
        world_reference(right, world.get('production'), 'World production 2025', per_year=True)
    name = composition.ELEMENT_NAMES.get(symbol, symbol)
    figure.suptitle(f"{name} in the world's humanoid robots")
    handles = [line_handle('In use (at the end of the year)', IN_USE), line_handle('Added per year', BUILT),
               line_handle('Removed per year', GONE)] + world_handles(figure)
    note = AMOUNTS + ' ' + world_note(world, notes)
    return save_figure(figure, path, note, dpi, handles + uncertainty_handles(draws, figure), ncol=4)


def world_note(world: dict, notes: list) -> str:
    """The one sentence of the foot on the world's lines: their source and its notes, or that the sources read give
    none."""
    if not world:
        return 'No world production or reserves for it in the sources read.'
    return ("The world's mine production of 2025 and its reserves: " + WORLD_SOURCE
            + ('; ' + '; '.join(notes) if notes else '') + '; a value too large or too small for the scale is written '
            'in the panel.')


def element_file(symbol: str) -> str:
    """The file name of an element's page: its name, as 08 writes it ('Copper.png')."""
    return f"{composition.ELEMENT_NAMES.get(symbol, symbol).replace(' ', '_')}.png"


# ------------------------------------------------------------------------------------------------------
# The distribution pages (Matthias, 2026-11-07: "I also want the distributions", to the table "Yes, as recommended"), in
# 02's form (its centre_lines, stacked_bars, mass_ticks, panel_rows: one copy of the code): bars of the share of the
# runs, the median a solid line, the 95 % interval dashed, their samples in the page's legend; each page followed by a
# page of its numbers (EVIDENCE.md E34). The elements split by the four groups of how a robot is taken apart as
# RAWCLICDataCenters' 05 splits its elements by 03 and 04, the smaller lower, in 01's colours (GROUP_COLOURS); their
# parts listed on the pages after.
# ------------------------------------------------------------------------------------------------------

PARTS_ROWS = 24                   # the rows of one list page of the elements part by part (parts_pages)
PARTS_COLUMNS = (0.02, 0.15, 0.27, 0.48, 0.58, 0.70, 0.84)   # where each column of a list page starts, across the page
PARTS_HEAD = composition.PART_LIST_HEAD                       # 02's columns: one copy
NUMBER_COLUMNS = (0.02, 0.21, 0.31, 0.45, 0.62, 0.80)    # where each column of a page of numbers starts, across the page


def count_unit(values: np.ndarray) -> tuple:
    """The unit a panel of robots is written in, by the median of its runs above 0, so that it reads from 1 up:
    (robots in one unit, its words), e.g. (1e6, 'million robots')."""
    positive = values[values > 0]
    typical = float(np.median(positive)) if positive.size else 0.0
    for per, words in ((1e9, 'billion robots'), (1e6, 'million robots'), (1e3, 'thousand robots')):
        if typical >= per:
            return per, words
    return 1.0, 'robots'


def mass_unit(values_kg: np.ndarray) -> tuple:
    """The unit a panel of kg is written in, by the median of its runs above 0, so that it reads from 1 up (kg, not
    Mg; Mt the largest, as mass_text): (kg in one unit, its symbol)."""
    positive = values_kg[values_kg > 0]
    typical = float(np.median(positive)) if positive.size else 0.0
    for per, unit in ((1e9, 'Mt'), (1e6, 'kt'), (1e3, 't'), (1.0, 'kg'), (1e-3, 'g')):
        if typical >= per:
            return per, unit
    return 1e-6, 'mg'


def numbers_page(heading: str, rows: list, path: str, dpi: int) -> str:
    """The page of numbers that follows a page of panels (EVIDENCE.md E34), A4 landscape as 04's pages: a row per panel
    (its title, in what share of the runs it is held, the median, the middle half, where 95 of 100 runs lie, the runs
    beyond its axis), each under 02's column names (NUMBERS_HEAD)."""
    page = plt.figure(figsize=A4_LANDSCAPE)
    page.suptitle(heading)
    for x, words in zip(NUMBER_COLUMNS, composition.NUMBERS_HEAD):
        page.text(x, 0.91, words, fontsize=9, va='top')
    step, y = min(0.034, 0.82 / max(len(rows), 1)), 0.87
    for row in rows:
        page.add_artist(plt.Line2D([0.02, 0.98], [y + 0.007, y + 0.007], color=composition.GRID, linewidth=0.8))
        for x, cell in zip(NUMBER_COLUMNS, row):
            page.text(x, y, cell, fontsize=9, va='top')
        y -= step
    os.makedirs(os.path.dirname(path), exist_ok=True)
    page.savefig(path, dpi=dpi, facecolor='white')
    plt.close(page)
    gc.collect()   # the pages closed before: a figure refers to itself through its parts, so only the
    #                collector frees it and its image of 52 MB (VERIFICATION V237)
    return path


RIDGE_BINS = 40                   # the bars of one type's row on the page of the robots in use, over its own runs


def robots_text(value: float) -> str:
    """A number of robots written out to four significant digits, as a title writes it: '11,600,000'."""
    return f'{float(f"{value:.4g}"):,.0f}'


def robots_in_use_page(files: dict, draws: int, folder: str, dpi: int) -> list:
    """The robots in use at the end of 2025, 2030, 2035 and 2040, the six types in one panel a year (Matthias, 2026-11-08:
    "can you not combine the 6 types to 1", "I want to see at the end how many robots there are", "not 39 I want 2040",
    "SHit it to 1st of July", "Yes"): each type a row, type 1 at the top, its robots in use over the runs, the bars of
    its own runs scaled to the row, its median (solid) and where 95 of 100 runs lie (dashed) within the row, their
    samples in the page's legend; one axis for the six, from the smallest to the largest run of any type, so that no run
    is cut ("why is the largest part of the triangal cut off?"); the robots in all, the article's, in the panel's title.
    The results of the run, nothing else (GitHub/CLAUDE.md §5). Followed by the page of each row's numbers."""
    figure, grid = plt.subplots(2, 2, figsize=A4_LANDSCAPE)
    numbers = []
    for axes, year in zip(grid.flat, DISTRIBUTION_YEARS):
        robots = np.asarray(files['units_stock'][:, year - FIRST, UNITS.index('robots'), :], dtype=np.float64)
        totals = np.asarray(files['article_stock'][:, year - FIRST], dtype=np.float64)   # all robots, each run
        per, words = count_unit(robots.max(axis=1))
        axes.type_numbers = []
        for k, t in enumerate(TYPES):
            values = robots[:, k] / per
            base = len(TYPES) - 1 - k
            counts, edges = np.histogram(values, bins=RIDGE_BINS)                     # every run of the type
            axes.bar(edges[:-1], 0.85 * counts / counts.max(), width=np.diff(edges), align='edge', bottom=base,
                     color=TYPE_COLOURS[k], edgecolor='none')
            median = float(np.median(values))
            p25, p75, low, high = (float(b) for b in np.percentile(values, (25, 75, 2.5, 97.5)))
            axes.plot([median, median], [base, base + 0.9], **composition.MEDIAN_MARK)
            for x in (low, high):
                axes.plot([x, x], [base, base + 0.9], **composition.BOUND_MARK)
            axes.type_numbers.append((f'Robot type {t}, {year}', median, low, high, words))
            numbers.append([f'Robot type {t}, {year}', 'all runs', f'{composition.panel_number(median)} {words}',
                            f'{composition.panel_number(p25)} to {composition.panel_number(p75)} {words}',
                            f'{composition.panel_number(low)} to {composition.panel_number(high)} {words}', '–'])
        smallest, largest = robots.min() / per, robots.max() / per
        margin = 0.02 * (largest - smallest)
        axes.set_xlim(smallest - margin, largest + margin)
        axes.set_ylim(0, len(TYPES))
        axes.set_yticks(np.arange(len(TYPES)) + 0.4)
        axes.set_yticklabels([f'robot type {t}' for t in reversed(TYPES)])
        axes.xaxis.set_major_locator(plt.MaxNLocator(6))
        axes.xaxis.set_major_formatter(plt.FuncFormatter(composition.panel_number))
        axes.set_xlabel(f'robots in use ({words})')
        axes.grid(axis='x', alpha=0.3)
        for side in ('top', 'right'):
            axes.spines[side].set_visible(False)
        # The robots in all: the article's, the same in every run (written as a range, were it ever to vary).
        if totals.max() - totals.min() <= 1e-6 * totals.max():
            words_in_all = robots_text(totals[0])
        else:
            low_all, high_all = np.percentile(totals, (2.5, 97.5))
            words_in_all = f'{robots_text(low_all)} to {robots_text(high_all)}'
        axes.set_title(f'{year}: {words_in_all} robots', loc='left', fontsize=11)   # the year alone
    figure.suptitle('Humanoid robots in use by robot type')
    note = (f'Each row one robot type: how often each number of its robots came out in {draws:,} model runs, the height '
            'scaled to the row, every run on the axis. The six types add up to the robots in use of the ai-2040 '
            'article at the end of each year, the number in the title, the same in every run. The numbers of every row '
            'are on the next page.')
    path = os.path.join(folder, 'robots_in_use.png')
    heading = figure._suptitle.get_text() + ': its numbers'
    saved = save_figure(figure, path, note, dpi, composition.distribution_handles(draws), ncol=2)
    return [saved, numbers_page(heading, numbers, path[:-len('.png')] + '_numbers.png', dpi)]


def part_words(name: str, kg: np.ndarray) -> str | None:
    """A part of an element on a distribution panel: '<name>: <median>' over the runs in which the part holds it, with
    their share in brackets when not all ('Joints: 25 kg (60 %)'); None when it holds none in any run (a 0 is not part
    of a distribution: its 0 is not written), as the data centres' part_text."""
    held = kg[kg > 0]
    if not held.size:
        return None
    return f'{name}: {mass_text(float(np.median(held)))}{composition.held_words(held.size / kg.size, short=True)}'


# The panel's title this many points above the panel, above the line of each part's median (17 until 2026-11-13: in
# Luciole, a taller font, the two stood 0.7 points apart; FigureTests' text_gap); PART_LINE points more for each further
# line of medians (wrap_part_words).
PART_TITLE_PAD, PART_LINE = 26, 12


def element_panel(axes, groups: dict, title: str, share_label: bool, colours: dict | None = None) -> list:
    """One element in all robots in use in one year, exactly as RAWCLICDataCenters' 05 draws an element of a data centre
    (its `_stacked_panel`; Matthias, 2026-11-08: "Exactkly the figures we have worked out for the data centers!!!"):
    the bars the distribution of the element's kg over the runs (the height the share of the runs, 70 bars over every
    run), each bar split into the kg its runs hold in each part (`groups`: joints, battery, electronics, body; or the AI
    data centres and the humanoid robots), the part with the smaller median at the bottom; the median a solid line with
    its number, where 95 of 100 runs lie dashed (the samples in the page's legend); the median of each part that holds
    it on a line under the title (part_words). Over the runs that hold the element ("A 0 is not part of a
    distribution"), their share in the title where not all. Returns the parts drawn (held in at least 2.5 % of the
    runs). `colours` the colour of each part, 01's GROUP_COLOURS where none."""
    colours = colours or schemas.GROUP_COLOURS
    total = sum(groups.values())
    inside = total > 0
    per, unit = mass_unit(total)
    values = total[inside] / per
    kept = {group: kg[inside] / per for group, kg in groups.items()}
    median = float(np.median(values))
    edges = np.histogram_bin_edges(values, bins=composition.APART_BINS)
    index = np.clip(np.digitize(values, edges[1:-1]), 0, len(edges) - 2)          # the bar each run falls into
    share_of_draws = np.bincount(index, minlength=len(edges) - 1) / values.size
    kg_all = np.bincount(index, weights=values, minlength=len(edges) - 1)
    drawn = [group for group in groups if composition.held(groups[group])]
    bottom = np.zeros(len(edges) - 1)
    for group in sorted(drawn, key=lambda g: float(np.median(kept[g]))):            # the smaller at the bottom
        kg = np.bincount(index, weights=kept[group], minlength=len(edges) - 1)
        height = share_of_draws * np.divide(kg, kg_all, out=np.zeros_like(kg), where=kg_all > 0)
        axes.bar(edges[:-1], height, width=np.diff(edges), align='edge', bottom=bottom,
                 color=colours[group], edgecolor='none')
        bottom += height
    low, high = (float(b) for b in np.percentile(values, [2.5, 97.5]))
    axes.axvline(median, **composition.MEDIAN_MARK)
    for bound in (low, high):
        axes.axvline(bound, **composition.BOUND_MARK)
    # the median's number just inside the top of the panel, 0.94 of its height (0.97 until 2026-11-13: in Luciole it stood
    # 6 points from the line of medians above the panel; FigureTests' text_gap)
    axes.text(median, 0.94, f' {composition.panel_number(median)} {unit}', transform=axes.get_xaxis_transform(),
              ha='left', va='top', fontsize=12, color='#222222', bbox=dict(facecolor='white', edgecolor='none',
                                                                          alpha=0.8, pad=1))
    # each part's median on a line under the title, above the panel, on no line (the design of 2026-11-12)
    parts = [w for w in (part_words(g, np.asarray(groups[g], dtype=np.float64)[inside] * 1.0) for g in drawn) if w]
    line = axes.text(0.0, 1.015, '   '.join(parts), transform=axes.transAxes, ha='left', va='bottom', fontsize=10,
                     color='#222222')
    axes.part_words = (line, parts)    # wrapped to the panel's width once the page is laid out (wrap_part_words)
    # four mass numbers at most (five until 2026-11-13: in Luciole's wider figures '100000' lay on '150000')
    axes.xaxis.set_major_locator(plt.MaxNLocator(4))
    axes.xaxis.set_major_formatter(plt.FuncFormatter(composition.panel_number))
    axes.yaxis.set_major_locator(plt.MaxNLocator(4))
    axes.yaxis.set_major_formatter(plt.FuncFormatter(composition.panel_number))
    # the mass numbers 02's TICK_PAD below the axis (3.5 points until 2026-11-13: in Luciole the first, '10000', stood
    # 0.2 points from the share axis's '0'; FigureTests' text_gap), one copy with 02's panels
    axes.tick_params(labelsize=11)
    axes.tick_params(axis='x', pad=composition.TICK_PAD)
    axes.set_xlabel(f'mass ({unit})', fontsize=12)
    if share_label:
        axes.set_ylabel('share of the runs', fontsize=12)
    axes.grid(axis='x', alpha=0.3)
    # the title PART_TITLE_PAD points above the panel, above the line of each part's median
    axes.set_title(title + composition.held_words(float(inside.mean()), short=True), fontsize=13,
                   loc='left', pad=PART_TITLE_PAD)
    axes.element_numbers = (title, median, low, high, unit)
    return drawn


def wrap_part_words(axes, renderer) -> bool:
    """The line of each part's median above a panel (element_panel) in as many lines as the panel's width needs, broken
    between two parts, and the panel's title raised PART_LINE points for each line added; measured as drawn, once the
    page is laid out. Until 2026-11-13 one line, which in Luciole ran into the next panel's on the page of 2040 (the
    joints' and the electronics' medians; FigureTests' text_gap). True where it wrapped."""
    line, parts = axes.part_words
    room = axes.get_window_extent(renderer).width
    if not parts or line.get_window_extent(renderer).width <= room:
        return False
    lines = [parts[0]]
    for words in parts[1:]:
        line.set_text(f'{lines[-1]}   {words}')
        if line.get_window_extent(renderer).width <= room:
            lines[-1] = f'{lines[-1]}   {words}'
        else:
            lines.append(words)
    line.set_text('\n'.join(lines))
    axes.set_title(axes.get_title(loc='left'), fontsize=13, loc='left',
                   pad=PART_TITLE_PAD + (len(lines) - 1) * PART_LINE)
    return True


def split_elements_page(title: str, splits: dict, colours: dict, elements: list, note: str, path: str,
                        dpi: int) -> str:
    """One page of elements exactly as RAWCLICDataCenters' 05 draws the elements of one data centre: a panel per element
    held in at least 2.5 % of the runs, in the order of `elements`, four across, each bar split into the kg of each of
    `splits` ({name: runs × elements}, in the legend's order) in its `colours` (`element_panel`); one legend above the
    panels: the parts drawn, the median and the 95 % interval; `note` at the foot (at most three sentences). 04's pages
    (split by the four groups) and 05's (by the data centres and the humanoid robots) are drawn by it: one copy."""
    total = sum(np.asarray(v, dtype=np.float64) for v in splits.values())
    held = [e for e in range(len(elements)) if composition.held(total[:, e])]
    ncols = 4
    nrows = max(1, math.ceil(len(held) / ncols))
    drawn = set()
    runs = total.shape[0]
    with plt.style.context(['default', schemas.FONT_STYLE]):   # the default style in the pages' font (01's FONT_STYLE)
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
        handles += composition.distribution_handles(runs)
        figure.legend(handles=handles, loc='upper center', bbox_to_anchor=(0.5, 0.965), ncol=len(handles),
                      frameon=False, fontsize=12)
        figure.text(0.5, -0.005, composition.foot_text(note.split('\n'), 150), ha='center', va='top', fontsize=11,
                    color='#555555')
        figure.tight_layout(rect=(0, 0, 1, 0.93))
        # each panel's line of medians within its panel's width, then the page laid out again for the raised titles
        renderer = figure.canvas.get_renderer()
        if any([wrap_part_words(axes, renderer) for axes in grid.flat[:len(held)]]):
            figure.tight_layout(rect=(0, 0, 1, 0.93))
        os.makedirs(os.path.dirname(path), exist_ok=True)
        figure.savefig(path, dpi=dpi, facecolor='white', bbox_inches='tight')
        plt.close(figure)
        gc.collect()   # the pages closed before: a figure refers to itself through its parts, so only the
        #                collector frees it and its image of 52 MB (VERIFICATION V237)
    return path


def elements_page(year: int, kg, elements: list, draws: int, path: str, dpi: int) -> str:
    """The elements in all robots in use at `year` (`kg`: runs × PARTS × elements), one page, exactly as
    RAWCLICDataCenters' 05 draws the elements of one data centre (split_elements_page): each bar split by the four
    groups of how a robot is taken apart, the sums of their parts run by run, in their order."""
    splits = {g: np.asarray(kg[:, [PARTS.index(p) for p in PARTS if GROUP_OF[p] == g]], dtype=np.float64).sum(axis=1)
              for g in GROUPS}
    note = (f'How often each mass came out in {draws:,} model runs, each panel on its own scale and unit; each bar split '
            'into the joints, the battery, the electronics and the body, the median of each under the title; an '
            'element in fewer than 2.5 % of the runs is not drawn\n'
            'A number in brackets: the share of the runs that have it, over which its bars are drawn\n'
            'Its parts are listed on the pages after')
    return split_elements_page(f'{year}: elements in all humanoid robots in use', splits, schemas.GROUP_COLOURS,
                               elements, note, path, dpi)


def parts_rows(kg, elements: list) -> list:
    """The rows of the list of the elements part by part at one year (`kg`: runs × PARTS × elements): for each
    element (02's order) each part that holds it in a run at least, in the order of 01's parts, its group, the share of
    the runs that hold it, its median, middle half and 95 % interval over those runs, in its own unit (mass_unit): 02's
    part_rows, one copy ("A 0 is not part of a distribution")."""
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
            page.text(x, 0.91, words, fontsize=9, va='top')
        y = 0.87
        for row in page_rows:
            page.add_artist(plt.Line2D([0.02, 0.98], [y + 0.007, y + 0.007], color=composition.GRID, linewidth=0.8))
            for x, cell in zip(PARTS_COLUMNS, row):
                page.text(x, y, cell, fontsize=9, va='top')
            y -= 0.034
        page.text(0.5, 0.02, 'Each row: one element in one part of how a robot is taken apart, in all humanoid robots '
                  'in use at the end of the year, over the runs that hold it; each row in its own unit.',
                  ha='center', va='bottom', fontsize=8.5, color='#555555')
        path = os.path.join(folder, f'parts_{year}_{k}.png')
        os.makedirs(folder, exist_ok=True)
        page.savefig(path, dpi=dpi, facecolor='white')
        plt.close(page)
        gc.collect()   # the pages closed before: a figure refers to itself through its parts, so only the
        #                collector frees it and its image of 52 MB (VERIFICATION V237)
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
    years = {flow_name: LAST - FIRST + 1 for flow_name in FLOWS}     # 2025 to 2040, as 08
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
        handle.write(f"{', '.join(UNIT_FILES)}: draw; year {FIRST} to {LAST}, as RAWCLICDataCenters' 08 (in, out: the "
                     f"calendar year; stock: its end); unit ({', '.join(UNITS)}); robot type "
                     f"({', '.join(map(str, TYPES))})\n")
        handle.write(f"{', '.join(ARTICLE_FILES)}: draw; year (the same); the article's robots built, in use, retired "
                     "(each type its own share of the robots built)\n")
        handle.write(f"{', '.join(ELEMENT_FILES)}: draw; year (the same); part of how a robot is taken apart "
                     f"({', '.join(f'{p} ({GROUP_OF[p]})' for p in PARTS)}); element ({', '.join(elements)}); kg\n")
    # The summary, over the draws above 0: every unit of all types and of each type; every element of all three parts.
    # One unit of a file read at a time (draws × years × types), so that the memory does not grow with the draws as a
    # whole file would (VERIFICATION V237).
    summary = {}
    for unit_name, flow_name in zip(UNIT_FILES, FLOWS):
        for j, unit in enumerate(UNITS):
            values = np.array(files[unit_name][:, :, j, :], dtype=np.float64)
            # All robots: the article's (each type its own share of them, not their sum); joint sets and packs: the
            # types' added up.
            total = (np.array(files[ARTICLE_FILES[FLOWS.index(flow_name)]], dtype=np.float64) if unit == 'robots'
                     else values.sum(axis=2))
            summary[(unit, 0, flow_name)] = stats_of(total)
            for k, t in enumerate(TYPES):
                summary[(unit, t, flow_name)] = stats_of(values[:, :, k])
            del values, total
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
        writer.writerow(('quantity', 'robot type', 'flow', 'year', 'median', '25 %', '75 %', '2.5 %', '97.5 %',
                         'held in % of the runs'))
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
            for i in range(len(stats['median'])):
                cells = [f'{stats[key][i]:.6g}' if np.isfinite(stats[key][i]) else '–' for key in STATISTICS]
                # The year as 08: a flow its calendar year, a stock the end of the year.
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
    robots = [float(f'{v:.7g}') for v in summary[('robots', 0, 'stock')]['median']]     # float32: 7 digits
    print(f'04 done: {draws:,} runs; robots in use at the end of {FIRST} {robots[0]:,.0f}, of {LAST} {robots[-1]:,.0f} (median); '
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
