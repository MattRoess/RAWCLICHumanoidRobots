"""
src/params_schema.py
====================

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

**EVERY SETTING FOR THIS PROJECT IS IN THIS FILE.** Open it, change a value, press Run on
`00_parameters.py`, then on the stages in order. Nothing is passed on a command line: no stage takes an
argument, because a switch that only exists on a command line is a switch the person running this never
sees.

`params.xlsx` and `documentation/claude/PARAMETER_REFERENCE.md` are OUTPUTS of this file. Editing either
of them changes nothing.

WHAT THIS PROJECT IS
--------------------
What a humanoid robot is made of, by category of humanoid robot, through 2040. The research of 2026
(`documentation/sources/00_overview_categories_market_shares_2040.md` and the category reports) defines
six categories, each with one anchor robot whose parts list stands for the category. The stages:

  00_parameters.py     checks the settings in this file and writes the register of them.

  01_schemas.py        draws what the workbook defines, before anything is drawn at random: an
                       overview, per category its page, its page in the shared lists and its robot in one
                       view, and the faults found, into `figures/schemas/`.

  02_composition.py    draws what each robot type is made of, `composition.draws` times (Monte Carlo): its
                       materials, elements, part groups and body regions, into `data/consolidated/`, one
                       folder per robot type, the draws of each robot type; and a page per robot type.

  03_comparison.py     draws the robot types side by side, by material, element, part group and body
                       region, from the draws of 02, into `figures/comparison/`.

WHAT IS IN THIS FILE
--------------------
One small class per group of settings (`DataParams`, `CheckParams`, `CompositionParams`, `OutputParams`), gathered
in `Params`.
Each setting carries, in `metadata['doc']`, the one-line description that the register shows. `current()`
returns the settings in force after checking them; `flatten()` lists them for the register;
`source_status()` says which of the input files are on disk.
"""

from __future__ import annotations

import glob
import math
import os
from dataclasses import dataclass, field, fields

# The project root: the folder above src/. Every relative path below is read from here, whatever the
# working folder of the run happens to be.
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class ParameterError(ValueError):
    """Raised when a setting in this file cannot be used as written."""


@dataclass
class DataParams:
    """The files the stages read. Paths are relative to the project root."""

    # The workbook of the 2026 research. Sheet 'Taxonomy' defines the six categories (what each is for, its
    # height, mass, joints and payload, its anchor robot); sheet 'Components & Materials' holds the parts
    # list of each anchor robot (per part the quantity, the mass of one unit and of all units as minimum,
    # mode and maximum in kg, the main material, the evidence). Matthias's workbook: read, never changed.
    # SAFE TO CHANGE: yes, when a newer workbook with the same sheets arrives under another name.
    workbook: str = field(
        default=os.path.join('data', 'raw', 'humanoid_robots_2040_workbook.xlsx'),
        metadata={'doc': 'The workbook of the 2026 research: the six categories and the parts list of '
                         'each anchor robot. Read, never changed.'})

    # The sheet of the workbook that defines the categories. Its first row is the header; one row per
    # category follows, numbered "1." to "6.".
    taxonomy_sheet: str = field(
        default='Taxonomy',
        metadata={'doc': 'The sheet that defines each category: what it is for, height, mass, joints, '
                         'payload, anchor robot.'})

    # The sheet of the workbook with the parts lists. Its header row starts with 'Category'; each
    # category's parts are closed by three rows: the sum of the parts, the stated mass of the anchor robot
    # and the difference between the two.
    components_sheet: str = field(
        default='Components & Materials',
        metadata={'doc': 'The sheet with the parts list of each anchor robot, closed per category by its '
                         'sum, the stated mass and their difference.'})

    # The sheet of the workbook with the materials of each anchor robot: per material its grade, minimum, mode and
    # maximum in kg, its share of the category and its evidence. Each category's materials are closed by their sum
    # and by the kilograms they leave unallocated against the parts list and against the stated mass.
    materials_sheet: str = field(
        default='Material Composition per Cat',
        metadata={'doc': 'The sheet with the materials of each anchor robot, closed per category by their sum '
                         'and the kilograms left unallocated.'})

    # Matthias's sources. 01_schemas.py looks here for the report of each category (a file whose name
    # starts with the category's number, as in 01_category_..., 02_category_...) and says on the category's
    # page whether there is one.
    # SAFE TO CHANGE: only if the sources move.
    sources_dir: str = field(
        default=os.path.join('documentation', 'sources'),
        metadata={'doc': "Matthias's sources; the schema looks here for each category's own report."})

    # Where every part and every material name of the workbook goes in the shared lists (part groups, body regions,
    # materials) that make the six robot types comparable. Decided by Matthias on 2026-10-26, point by point
    # (documentation/claude/SHARED_LISTS.md); written by Claude, to be corrected by Matthias in Excel.
    # 01_schemas.py checks every placement and draws one page per robot type from it.
    # SAFE TO CHANGE: only if the file moves.
    shared_lists: str = field(
        default=os.path.join('data', 'researched', 'shared_lists.xlsx'),
        metadata={'doc': 'Where every part and material name goes in the shared part groups, body regions and '
                         'materials.'})

    # The element recipes: the datasheets of the cells the battery builds use (sheet Cells), the compounds (sheet
    # Compounds), the parts of each recipe down to its elements (sheet Recipe: the cells, plastics, fibre composites,
    # aluminium and magnesium alloys) and which recipe each workbook row follows (sheet Rows). Agreed by Matthias on
    # 2026-10-26 and 2026-10-27 (documentation/claude/EVIDENCE.md, E1.1c-f, E1.2c-e, E1.7i-k, E1.8c, E1.9c); written
    # by Claude, to be corrected by Matthias in Excel. 01_schemas.py checks them and counts each robot type's cells from
    # them (sheet Battery cells of the shared lists). The recipes of the other materials will be added here.
    # SAFE TO CHANGE: only if the file moves.
    element_recipes: str = field(
        default=os.path.join('data', 'researched', 'element_recipes.xlsx'),
        metadata={'doc': 'The element recipes: the cells and their datasheets, the compounds, and the parts of each '
                         'cell down to its elements.'})

    # Each robot type's robots taken apart, one file per type in a folder of its own (Matthias, 2026-10-30: "Yes,
    # build C"; "separate by folder, not by prefix"): {folder} is the type's folder, named as data/consolidated/'s
    # ('1_compact_research_developer', '2_full_scale_general_purpose_ai_research'). Each file: the joints of every
    # robot and where they sit (sheet Joints), the joint module part by part as China Post Securities weighed the
    # G1's (JointParts), every other part (Parts), the materials of the parts that hold more than one (Shares), the
    # circuit boards and sensors (Boards, Sensors, SensorElements), the numbers used across the sheets (Constants) and
    # the sources (Sources). Written by its type's builder, tools/{folder}/make_parts_taken_apart.py, from the research
    # Matthias agreed (documentation/claude/EVIDENCE.md E2, E5, E6); 01_schemas.py checks it, 02 draws from it.
    # SAFE TO CHANGE: only if the files move; {folder} must stay in it.
    parts_taken_apart: str = field(
        default=os.path.join('data', 'researched', '{folder}', 'parts_taken_apart.xlsx'),
        metadata={'doc': "Each robot type's robots taken apart ({folder} its folder): joints, the joint module part "
                         'by part, every other part, their materials, boards and sensors.'})

    # The humanoid.guide catalogue as read on 2026-10-28 (https://humanoid.guide/humanoid-robots-database/, "349
    # humanoids"): each robot's attribute table, numbered in the order the robots were read (documentation/claude/
    # EVIDENCE.md E4). Second-hand: makers may edit their entries. Read, never changed; the register is built from it.
    # SAFE TO CHANGE: only if the file moves, or for a newer reading of the catalogue under another name.
    humanoid_guide: str = field(
        default=os.path.join('data', 'raw', 'humanoid_guide_2026-10-28.xlsx'),
        metadata={'doc': 'The humanoid.guide catalogue as read on 2026-10-28: every robot\'s attribute table.'})

    # The register of every known humanoid robot, each with its one or two robot types (Matthias, 2026-10-28: "I want
    # that all know humanoid robots at the end can be assigned to types"; his rules and decisions in EVIDENCE.md E4 to
    # E4.11). Built by tools/make_humanoid_register.py from the catalogue above and the decisions held there.
    # 01_schemas.py checks it; 02_composition.py draws each robot type taken apart over its robots.
    # SAFE TO CHANGE: only if the file moves.
    register: str = field(
        default=os.path.join('data', 'researched', 'humanoid_register.xlsx'),
        metadata={'doc': 'The register of every known humanoid robot with its one or two robot types.'})

    # THE SIBLING PROJECTS' FILES that robot type 1 taken apart reads where they lie, never copied (Matthias,
    # 2026-09-21: "Each project owns its data"; agreed for this file 2026-10-27, open point C of its plan). Absolute
    # paths, because those projects are sibling checkouts and neither may assume where the other sits (as in
    # RAWCLICStockAndFlow's `battery_composition_dir`). Nothing under them is ever written. 01_schemas.py checks that
    # each holds what the file names.
    # SAFE TO CHANGE: yes, when a sibling project moves.

    # RAWCLICVehicleElectronics' board metals, mg per cm2 of board by car board category (sheet PCPComposition): the
    # gold, silver, palladium, tin and nickel of each G1 board, by the category of the sheet Boards (EVIDENCE.md E2.8b).
    vehicle_pcb_composition: str = field(
        default=('/Users/rm/Library/Mobile Documents/com~apple~CloudDocs/Documents/GitHub/'
                 'RAWCLICVehicleElectronics/Data/04_VehiclePCBComposition.xlsx'),
        metadata={'doc': "RAWCLICVehicleElectronics' board metals per cm2 by car board category; read where it lies."})

    # RAWCLICVehicleElectronics' sensor elements, mg per sensor element by sensor type (sheet Sensor Details): the
    # elements of each G1 sensor, by the car sensor types of the sheet SensorElements (EVIDENCE.md E2.8b).
    vehicle_sensor_composition: str = field(
        default=('/Users/rm/Library/Mobile Documents/com~apple~CloudDocs/Documents/GitHub/'
                 'RAWCLICVehicleElectronics/Data/07_VehicleSensorComposition.xlsx'),
        metadata={'doc': "RAWCLICVehicleElectronics' elements per sensor element by sensor type; read where it "
                         'lies.'})

    # RAWCLICDataCenters' elements per kg of boards and components (sheet BoardsAndComponents): the tantalum of the
    # G1's boards (Matthias, 2026-10-27: "There is the tantalum for the PBC of the data center").
    data_center_element_composition: str = field(
        default=('/Users/rm/Library/Mobile Documents/com~apple~CloudDocs/Documents/GitHub/'
                 'RAWCLICDataCenters/data/researched/04_DataCenterElementComposition.xlsx'),
        metadata={'doc': "RAWCLICDataCenters' elements per kg of boards (tantalum); read where it lies."})

    # RAWCLICVehicleTractionMotor's NdFeB grades by temperature class (sheet PermanentMagnetNdFeB of its element
    # workbook), and the project itself, whose own code draws the magnets' elements of a grade class (Matthias,
    # 2026-10-27: "take the NdBFe composition from the car traction motors"; one copy of the code).
    traction_motor_magnets: str = field(
        default=('/Users/rm/Library/Mobile Documents/com~apple~CloudDocs/Documents/GitHub/'
                 'RAWCLICVehicleTractionMotor/data/raw/10_MaterialElementDefinitions.xlsx'),
        metadata={'doc': "RAWCLICVehicleTractionMotor's NdFeB grades by temperature class; read where it lies."})
    # RAWCLICVehicleTractionMotor's steels (sheets ElectricalSteel and CastFeSteel of the same element workbook): the
    # electrical steels M19 and M27 of type 1's motors and the stainless steel Type 304 of the RP1's pins and screws,
    # each a row of minima and of maxima, iron the balance (EVIDENCE.md E5.18; Matthias, 2026-10-29: "Yes, build it",
    # point 4: "M19, M27 and 304 read where they lie").
    traction_motor_steels: str = field(
        default=('/Users/rm/Library/Mobile Documents/com~apple~CloudDocs/Documents/GitHub/'
                 'RAWCLICVehicleTractionMotor/data/raw/10_MaterialElementDefinitions.xlsx'),
        metadata={'doc': "RAWCLICVehicleTractionMotor's electrical steels and stainless steel 304; read where they "
                         'lie.'})
    # The world's mine production in 2025 and reserves of each element, for 04's figures (Matthias, 2026-11-06: "Add
    # also the limit in stock and production like for the data centers"): RAWCLICDataCenters' sheet ElementReference
    # (U.S. Geological Survey, Mineral Commodity Summaries 2026, its EVIDENCE.md § 24), read where it lies; and for the
    # elements that sheet does not hold (magnesium, titanium, indium) the USGS data file in RAWCLICDataCenters' sources.
    # SAFE TO CHANGE: only if the files move.
    data_center_scenarios: str = field(
        default=('/Users/rm/Library/Mobile Documents/com~apple~CloudDocs/Documents/GitHub/'
                 'RAWCLICDataCenters/data/researched/05_DataCenterScenarios.xlsx'),
        metadata={'doc': "RAWCLICDataCenters' scenario workbook: its sheet ElementReference, the world's production "
                         'and reserves of each element; read where it lies.'})
    usgs_commodities: str = field(
        default=('/Users/rm/Library/Mobile Documents/com~apple~CloudDocs/Documents/GitHub/'
                 'RAWCLICDataCenters/documentation/sources/MCS2026_Commodities_Data.csv'),
        metadata={'doc': "USGS Mineral Commodity Summaries 2026, its data file, in RAWCLICDataCenters' sources: "
                         'magnesium, titanium and indium; read where it lies.'})
    traction_motor_dir: str = field(
        default='/Users/rm/Library/Mobile Documents/com~apple~CloudDocs/Documents/GitHub/RAWCLICVehicleTractionMotor',
        metadata={'doc': "RAWCLICVehicleTractionMotor, whose own code draws the NdFeB elements of a grade class."})


@dataclass
class CheckParams:
    """How strictly the workbook is checked before it is drawn."""

    # Two numbers that should be equal (the mass of all units and the number times the mass of one; a sum
    # row and the sum of its parts) may differ by this much, in kg, before it counts as a fault. The
    # workbook stores some masses of one unit as long fractions (0.4090909... kg = 9 kg / 22), so a product
    # is exact only to about 0.00000001 kg. 0.001 kg (1 g) is far above that, and far below the lightest
    # part of the workbook (the depth camera of category 1, 0.08 kg at its minimum).
    # SAFE TO CHANGE: yes, within the limits that `current()` enforces (above 0, at most 0.01 kg).
    tolerance_kg: float = field(
        default=0.001,
        metadata={'doc': 'How far apart, in kg, two numbers that should be equal may be before the '
                         'schema reports a fault.'})


@dataclass
class CompositionParams:
    """How 02_composition.py draws what each robot type is made of (Monte Carlo)."""

    # How many times every robot type is drawn. 200,000, like RAWCLICVehicleTractionMotor and RAWCLICDataCenters:
    # Matthias agreed it on 2026-10-26 (recommendation d of the specification, documentation/claude/HANDOVER.md).
    # With float32 that is about 0.8 MB per column of the draw files, some 50 MB per robot type. The real run is
    # Matthias's; the tests use few draws.
    # SAFE TO CHANGE: yes, between 100 and 1,000,000 (`current()` enforces it); fewer draws give rougher intervals.
    draws: int = field(
        default=200_000,
        metadata={'doc': 'How many Monte Carlo draws 02_composition.py makes for every robot type.'})

    # The start of the random numbers, fixed so that a rerun gives the same draws.
    # SAFE TO CHANGE: yes; another seed gives other draws of the same distributions.
    seed: int = field(
        default=1,
        metadata={'doc': 'The seed of the random numbers, so that a rerun gives the same draws.'})

    # The energy per kg of cylindrical NMC cells, Wh/kg: minimum (Tesla 4680, measured), mode (the median of the four
    # NMC cells read) and maximum (Samsung 50E). documentation/claude/EVIDENCE.md, E1.7d, agreed 2026-10-26. The NMC
    # cell's coatings and foils move with it (E1.7i): with a counted cell, by that cell's Wh/kg over the mode; where a
    # robot type keeps its battery row (robot types 2 and 6), it is drawn from this triangle (recommendation f).
    # SAFE TO CHANGE: only with new sources, in order (minimum <= mode <= maximum).
    nmc_wh_per_kg_min: float = field(
        default=232.5,
        metadata={'doc': 'Energy per kg of cylindrical NMC cells, minimum (E1.7d), Wh/kg.'})
    nmc_wh_per_kg_mode: float = field(
        default=241.5,
        metadata={'doc': 'Energy per kg of cylindrical NMC cells, mode (E1.7d), Wh/kg; the reference of the NMC '
                         "cell's coatings and foils."})
    nmc_wh_per_kg_max: float = field(
        default=256.0,
        metadata={'doc': 'Energy per kg of cylindrical NMC cells, maximum (E1.7d), Wh/kg.'})

    # Robot type 1's lowest mass, kg: a robot of the register lighter than this is not part of type 1 (Matthias,
    # 2026-10-28: "Below 15 kg not part of the type 1"). 01 checks the register against it; 02 draws type 1 over the
    # register's robots of type 1, all at or above it.
    # SAFE TO CHANGE: only on Matthias's word.
    type_one_lowest_kg: float = field(
        default=15.0,
        metadata={'doc': "Robot type 1's lowest mass, kg (Matthias, 2026-10-28); lighter robots are not type 1."})

    # The robots of the register that are outliers: listed, not drawn. Each its number in the register and the reason,
    # in Matthias's words. Matthias, 2026-11-04, of the NeodraDynamics Neo1 (208, about 4 m and 1,200 kg, hydraulic):
    # "We might need to qualify Neo the huge robot as an outlyer, as it was just built as a few of them and never will
    # be build in large numbers", "Ok it is neo. It should be out. Mark it as outlier."; this setting on 2026-11-05,
    # "Yes, 3 to 5" (documentation/claude/EVIDENCE.md E30). The register builder writes "not drawn: an outlier" in the
    # sheets of its robot types, 01 checks it and marks it in its robots tables, 02 does not draw it and names it on its
    # notes pages, 03 on its notes page. It stays in the register and in its parts file.
    # SAFE TO CHANGE: only on Matthias's word; each a number of the register, once, with its reason.
    outliers: tuple = field(
        default=((208, 'built as a few, never in large numbers'),),
        metadata={'doc': 'The robots of the register not drawn, outliers: (its number, the reason), each once '
                         '(Matthias, 2026-11-04; EVIDENCE.md E30).'})


@dataclass
class StockFlowParams:
    """How 04_stock_and_flow.py counts the robots, their joint sets and battery packs, and the elements in them: the
    robots in use as ai-2040.com Plan A states them ("Use the numbers in the article"), each robot one unit with its
    lifetime, its joints and battery packs replaced on their own (Matthias, 2026-11-06: "Yes, build it", "Yes, replace
    joints"; documentation/claude/EVIDENCE.md E39 to E43)."""

    # The robots in the world at 1 January of each year, as the article states them: AI Futures Project, AI 2040: Plan
    # A (https://ai-2040.com/?choices=plan-a-root), its economics explorer (https://ai-2040.com/econ-explorer/), preset
    # "AI 2040 Plan A Scenario", Input Table, row "Robots", read on 2026-11-06 (EVIDENCE.md E40). The article's robots
    # are of every form, "some mixture of humanoid and other specialized form factors"; on Matthias's word they are the
    # humanoid robots of 04 ("Use the numbers in the article", "It gives 70x10E9"). Its model takes them as stocks at
    # 1 January (model/costSide.js: "scenario H100e / Q_robot are Jan-1 (start-of-year) stocks").
    # SAFE TO CHANGE: only with the article; one value a year, the years without a gap.
    robots: tuple = field(
        default=((2025, 10e6), (2026, 11.6e6), (2027, 13.3e6), (2028, 15.3e6), (2029, 18.2e6), (2030, 23e6),
                 (2031, 35.7e6), (2032, 72e6), (2033, 170e6), (2034, 423e6), (2035, 1.0e9), (2036, 2.26e9),
                 (2037, 5.28e9), (2038, 12.5e9), (2039, 29.7e9), (2040, 70e9)),
        metadata={'doc': "The robots in the world at 1 January, ai-2040.com Plan A (its economics explorer's row "
                         "Robots; EVIDENCE.md E40), as the humanoid robots of 04."})

    # A robot's lifetime, years, spread among the robots of each quarter as RAWCLICDataCenters' 07 spreads its GPUs'
    # (min, mode, max of a triangle; Matthias, 2026-11-06: "have real lifetimes not something fixed like this", to the
    # table of 04, "Yes, build it"): CRU's "average of seven years (five to ten-year) life expectancy for humanoid
    # robots", Agility's assumed 5-year useful life of Digit and the article's "5-year robot life" (EVIDENCE.md E39.3).
    # The robot as one unit, its joints and battery packs apart ("No look at the robots as a unit with exception of the
    # batteries", "Yes, replace joints").
    # SAFE TO CHANGE: only with new sources; in order, above 0.
    robot_lifetime_years: tuple = field(
        default=(5.0, 7.0, 10.0),
        metadata={'doc': "A robot's lifetime, years (min, mode, max), spread among the robots of each quarter "
                         '(EVIDENCE.md E39.3, E42).'})

    # The uncertainty of the lifetimes, a factor drawn once a draw (min, mode, max): Matthias, 2026-11-07, "Is the
    # lifetime also with uncertainties. I want that is is 30% short and 20% longer. Also with the batteries"
    # (EVIDENCE.md E45). One factor a draw scales the robots' lifetime (the triangle above, spread among the robots,
    # times it), another of its own the battery packs' charges to 80 %, a third the joints' life in hours, as
    # RAWCLICStockAndFlow draws its lifetimes once a draw around their mode.
    # SAFE TO CHANGE: only on Matthias's word; in order, above 0, the min below the max.
    lifetime_factor: tuple = field(
        default=(0.70, 1.0, 1.20),
        metadata={'doc': "The factor of a draw on the robots' lifetime and, each drawn on its own, on the battery "
                         "packs' charges and the joints' life (min, mode, max): Matthias's 30 % shorter, 20 % longer."})

    # The hours a day a robot works: the article's "AIs and robots can work 24/7" (its main page, read 2026-11-06).
    # SAFE TO CHANGE: only with the article; above 0, at most 24.
    hours_a_day: float = field(
        default=24.0,
        metadata={'doc': "The hours a day a robot works: ai-2040.com Plan A, robots 'can work 24/7'."})

    # A joint's life, operating hours, spread among the joints (min, mode, max): the rated life of the strain-wave
    # gears in humanoid joints, Nabtesco's "market standard of 7,000 hours" and Harmonic Drive's "L10 of 10,000 hours",
    # and planetary gearboxes "up to 30,000 hours" (Wittenstein; EVIDENCE.md E43). A robot's joints are replaced
    # whenever they wear out (Matthias, 2026-11-06: "Yes, replace joints"), the joint kinds 01 numbers 1 to 6.
    # SAFE TO CHANGE: only with new sources; in order, above 0.
    joint_life_hours: tuple = field(
        default=(7000.0, 10000.0, 30000.0),
        metadata={'doc': "A joint's life, operating hours (min, mode, max), spread among the joints (EVIDENCE.md "
                         'E43).'})

    # A battery pack's charges until it holds 80 % of its capacity (min, mode, max), spread among the packs: Fourier's
    # GR-3 "Cycle Life ≥500 (80%DOD)" and N1 "≥800 cycles, SOH 80%", a cell maker's "more than 80% after 1000 cycles"
    # (EVIDENCE.md E39.2). A pack is replaced when its capacity falls below `battery_replaced_below`; the charges to that
    # share by a straight-line fade from 100 % to 80 % (an approximation: real cells fade faster at first and near
    # their end). Each pack is charged once a day: a robot holds as many packs as a day's work needs (Matthias,
    # 2026-11-06: "Have at least so many battery packs ready for use as it is needed to have them for 1 day to switch.
    # So they can recharge slowly").
    # SAFE TO CHANGE: only with new sources; in order, above 0.
    battery_cycles_to_80: tuple = field(
        default=(500.0, 800.0, 1000.0),
        metadata={'doc': "A battery pack's charges until 80 % of its capacity (min, mode, max), spread among the packs "
                         '(EVIDENCE.md E39.2).'})

    # The capacity below which a pack is replaced (min, mode, max), one value a draw: Matthias, 2026-11-06, "battery
    # packs will be repalce as soon as the capacity go below 80% +-5%".
    # SAFE TO CHANGE: only on Matthias's word; in order, between 0 and 1.
    battery_replaced_below: tuple = field(
        default=(0.75, 0.80, 0.85),
        metadata={'doc': "The capacity below which a battery pack is replaced (min, mode, max): Matthias's 80 % ± 5 %."})

    # A pack's runtime in 2025, hours, for the robot types whose rows of the workbook give energy density, not runtime
    # (types 1, 3 and 5): each its anchor robot's maker, the Unitree G1 "About 2h", the Atlas "4 hours"; the Walker S2's
    # maker states none, 2 h walking as a press report relays it (E) (EVIDENCE.md E39.1). Later years rise with the
    # workbook's energy density of the type; types 2, 4 and 6 take the workbook's runtimes (sheet Material Trajectories
    # 2025-2040).
    # SAFE TO CHANGE: only with new sources; hours above 0, one per type 1, 3 and 5.
    runtime_2025_hours: tuple = field(
        default=((1, 2.0), (3, 2.0), (5, 4.0)),
        metadata={'doc': "A battery pack's runtime in 2025, hours, of robot types 1, 3 and 5, their anchor robots' "
                         '(EVIDENCE.md E39.1).'})

    # The mode of the share of research robots, robot type 1, among the robots built, in 2025 and in 2040, a straight line
    # between: Matthias, 2026-11-06, "I assume reseach wil be around 10% within -+5% and over time this will decrease";
    # to 2040 half of it (E, agreed in the table of 04, "Yes, build it"). Types 2 to 6 take the workbook's shares of the
    # robots shipped (sheet Market Units & Shares 2025-2040), scaled together to what type 1 leaves, so that the six
    # modes add up to 1 (Matthias, 2026-11-07, to the table of the type shares, "Yes, build it"; EVIDENCE.md E44).
    # SAFE TO CHANGE: only on Matthias's word; the years 2025 and 2040, each share above 0 and below 1.
    # Its uncertainty the same as every other type's (`type_share_spread`; Matthias, 2026-11-07: "robot type 1 has the
    # same unceratinties as all the other").
    research_share: tuple = field(
        default=((2025, 0.10), (2040, 0.05)),
        metadata={'doc': 'The mode of the share of robot type 1 among the robots built, in 2025 and 2040 (Matthias; '
                         '2040 half of 2025, E).'})

    # How far the share of each robot type lies from its mode in 95 % of the draws, a share of the mode, in 2025 and in
    # 2040, a straight line between (Matthias, 2026-11-07: "Damit I told you 10% in 2025 and 30% in 2040", "I said +-10%
    # and then +- 30% this is never the case", "all 6 types around 10% +- in 2025 and 30%+- in 2040. All have to have
    # close to this value!!"). 04 gives every type its own triangle, mode × (1 ∓ spread / 0.7764) (95 % of a triangle
    # lies within 0.7764 of its half-width), and puts the draws of the six together so that they add up to the article's
    # robots in every draw (the rearrangement algorithm; "Yes, build it"); nothing divided (E44).
    # SAFE TO CHANGE: only on Matthias's word; the years 2025 and 2040, each spread above 0 and below 0.7764.
    type_share_spread: tuple = field(
        default=((2025, 0.10), (2040, 0.30)),
        metadata={'doc': "How far the share of each robot type lies from its mode in 95 % of the draws, as a share of "
                         "the mode, in 2025 and 2040 (Matthias's 10 % and 30 %)."})


@dataclass
class OutputParams:
    """Where the stages write. Paths are relative to the project root."""

    # The pages of 01_schemas.py: overview.png, faults.png and categories/<n>_<name>.png.
    schemas_dir: str = field(
        default=os.path.join('figures', 'schemas'),
        metadata={'doc': 'Where 01_schemas.py draws the overview, one page per category and the '
                         'faults.'})

    # The draws of each robot type, as 02_composition.py writes them, one folder per robot type (<n>_<name>/): the draws and their
    # summary. data/consolidated/ is the one folder another repository reads (the house layout of the RAWCLIC
    # projects). Outputs: not in git.
    composition_dir: str = field(
        default=os.path.join('data', 'consolidated'),
        metadata={'doc': 'Where 02_composition.py writes the draws and the summary of each robot type, one folder '
                         'per type.'})

    # The pages of 02_composition.py, one per robot type.
    composition_figures_dir: str = field(
        default=os.path.join('figures', 'composition'),
        metadata={'doc': 'Where 02_composition.py draws one page per robot type.'})

    # The pages of 03_comparison.py: the six robot types side by side.
    comparison_dir: str = field(
        default=os.path.join('figures', 'comparison'),
        metadata={'doc': 'Where 03_comparison.py draws the six robot types side by side.'})

    # What 02_composition.py writes of each robot type taken apart: its draws of every material and element in every
    # kind of part, into a folder of its own below this one (<n>_<name>/, as data/consolidated/'s; 2026-10-30, "Yes,
    # build C"). The project's own outputs (data/), until Matthias decides whether a later stage reads them
    # (open point F of its plan), which would move them to data/consolidated/. Outputs: not in git.
    parts_dir: str = field(
        default=os.path.join('data', 'parts_taken_apart'),
        metadata={'doc': 'Where the draws of each robot type taken apart are written, a folder per type.'})

    # The figures of each robot type taken apart (type 1's approved on 2026-10-27, "Looks good to me"), a folder per
    # type below this one (<n>_<name>/).
    parts_figures_dir: str = field(
        default=os.path.join('figures', 'parts_taken_apart'),
        metadata={'doc': 'Where the figures of each robot type taken apart are drawn, a folder per type.'})

    # The robot types whose pages 01 and 02 draw (Matthias, 2026-10-29: "Why the hell are ther all thes figure for robot
    # types 2 to 6?", then "Type 1 only"; "I will only focus on 1", 2026-10-28). The same code draws every robot type's
    # pages; a type comes back here when its steps begin: type 2 on 2026-10-30 ("Yes, build C", point 6), types 3 and 4
    # the same day ("Yes, build it", EVIDENCE.md E11.7 open point B), types 5 and 6 on 2026-11-01 ("Find all the data
    # for 5 and 6 and then fill in the data in the respective sheets. So I can then have all dat for the run of 01 and
    # 02", E16.6). 02 writes the draws of all six types whatever is set here.
    # SAFE TO CHANGE: yes, any of the robot types 1 to 6, each once.
    robot_types_with_pages: tuple = field(
        default=(1, 2, 3, 4, 5, 6),
        metadata={'doc': 'The robot types whose pages 01 and 02 draw; 02 writes the draws of all six.'})

    # What 04_stock_and_flow.py writes: the draws of the robots, joint sets and battery packs of each type and of the
    # elements in them, year by year, and their summary. Outputs: not in git.
    stock_and_flow_dir: str = field(
        default=os.path.join('data', 'stock_and_flow'),
        metadata={'doc': 'Where 04_stock_and_flow.py writes the draws of the robots, joint sets, battery packs and '
                         'elements, year by year, and their summary.'})

    # The pages of 04_stock_and_flow.py: overview.png and elements/<Element>.png.
    stock_and_flow_figures_dir: str = field(
        default=os.path.join('figures', 'stock_and_flow'),
        metadata={'doc': 'Where 04_stock_and_flow.py draws its overview and its page of each element.'})

    # The resolution of every figure, in dots per inch. 150 keeps the text of a page sharp on a screen
    # and a page small enough to open quickly.
    dpi: int = field(
        default=150,
        metadata={'doc': 'Resolution of the figures in dots per inch.'})


@dataclass
class Params:
    """All settings of the project, one group per stage concern."""

    data: DataParams = field(default_factory=DataParams)
    checks: CheckParams = field(default_factory=CheckParams)
    composition: CompositionParams = field(default_factory=CompositionParams)
    stock_and_flow: StockFlowParams = field(default_factory=StockFlowParams)
    output: OutputParams = field(default_factory=OutputParams)


def absolute(path: str) -> str:
    """A path of this file, relative to the project root, as an absolute path."""
    return os.path.join(ROOT, path)


def validate(params: Params) -> None:
    """Stop with a ParameterError, in plain words, when a setting cannot be used as written."""
    data = params.data
    for name in ('workbook', 'shared_lists', 'element_recipes', 'parts_taken_apart'):
        if not getattr(data, name).lower().endswith('.xlsx'):
            raise ParameterError(f'data.{name} must be an .xlsx workbook, not {getattr(data, name)!r}.')
    # One parts file per robot type, each in its type's folder: the path must name the folder.
    if '{folder}' not in data.parts_taken_apart:
        raise ParameterError("data.parts_taken_apart must name the robot type's folder as {folder}, such as "
                             f"'data/researched/{{folder}}/parts_taken_apart.xlsx', not {data.parts_taken_apart!r}.")
    for name in ('taxonomy_sheet', 'components_sheet', 'materials_sheet', 'sources_dir'):
        if not str(getattr(data, name)).strip():
            raise ParameterError(f'data.{name} is empty.')

    # Above 0, or every rounding difference would count as a fault; at most 0.01 kg, an eighth of the
    # lightest part (0.08 kg), so that a tolerance can never hide a whole part.
    tolerance = params.checks.tolerance_kg
    if not 0 < tolerance <= 0.01:
        raise ParameterError(f'checks.tolerance_kg must be above 0 and at most 0.01 kg, not {tolerance}.')

    # At least 100 draws, or no interval means anything; at most 1,000,000, or the files of six robot types reach
    # gigabytes for nothing a figure can show.
    composition = params.composition
    if not 100 <= composition.draws <= 1_000_000:
        raise ParameterError(f'composition.draws must be between 100 and 1,000,000, not {composition.draws}.')
    if not isinstance(composition.seed, int) or composition.seed < 0:
        raise ParameterError(f'composition.seed must be a whole number from 0 up, not {composition.seed!r}.')
    if not 0 < composition.nmc_wh_per_kg_min <= composition.nmc_wh_per_kg_mode <= composition.nmc_wh_per_kg_max:
        raise ParameterError('composition.nmc_wh_per_kg_min, _mode and _max must be above 0 and in order, not '
                             f'{composition.nmc_wh_per_kg_min}, {composition.nmc_wh_per_kg_mode}, '
                             f'{composition.nmc_wh_per_kg_max}.')
    # The outliers: pairs of a register number (a whole number from 1) and a reason in words, each number once; none
    # is allowed. 01 checks that each number is a robot of the register.
    outliers = composition.outliers
    if (not isinstance(outliers, tuple)
            or not all(isinstance(o, tuple) and len(o) == 2 and isinstance(o[0], int) and not isinstance(o[0], bool)
                       and o[0] >= 1 and isinstance(o[1], str) and o[1].strip() for o in outliers)
            or len({o[0] for o in outliers}) < len(outliers)):
        raise ParameterError('composition.outliers must be a tuple of (register number, reason) pairs, each number '
                             f"once, such as ((208, 'built as a few, never in large numbers'),), not {outliers!r}.")

    # The sibling projects' files: absolute, .xlsx where a file is named.
    for name in ('vehicle_pcb_composition', 'vehicle_sensor_composition', 'data_center_element_composition',
                 'traction_motor_magnets', 'traction_motor_steels', 'traction_motor_dir', 'data_center_scenarios'):
        value = getattr(data, name)
        if not os.path.isabs(value) or (name != 'traction_motor_dir' and not value.lower().endswith('.xlsx')):
            raise ParameterError(f'data.{name} must be an absolute path' + ('' if name == 'traction_motor_dir' else
                                 ' to an .xlsx workbook') + f', not {value!r}.')

    # 04's robots: one value a year from 0 up, the years without a gap, two at least (a year's flow needs the next 1
    # January). Its triangles in order, their min below their max (a triangle, never a single number); the capacity
    # below 1; the research share and the types' spread given for 2025 and 2040, each above 0 and below 1; the hours a
    # day at most 24; a runtime of 2025 for each of robot types 1, 3 and 5.
    robots = params.stock_and_flow.robots
    years = [y for y, _ in robots] if isinstance(robots, tuple) else []
    if (len(years) < 2 or years != list(range(years[0], years[0] + len(years)))
            or not all(isinstance(v, (int, float)) and v > 0 for _, v in robots)):
        raise ParameterError('stock_and_flow.robots must be (year, robots) pairs, one a year without a gap, two at '
                             f'least, each above 0, not {robots!r}.')
    flow = params.stock_and_flow
    for name in ('robot_lifetime_years', 'joint_life_hours', 'battery_cycles_to_80', 'battery_replaced_below',
                 'lifetime_factor'):
        low, mode, high = getattr(flow, name)
        if not (0 < low <= mode <= high and low < high):
            raise ParameterError(f'stock_and_flow.{name} must be a min, mode and max above 0, in order, the min below '
                                 f'the max, not {getattr(flow, name)!r}.')
    if flow.battery_replaced_below[2] >= 1:
        raise ParameterError(f'stock_and_flow.battery_replaced_below must stay below 1, not '
                             f'{flow.battery_replaced_below!r}.')
    for name in ('research_share', 'type_share_spread'):
        value = getattr(flow, name)
        if (not isinstance(value, tuple) or [y for y, _ in value] != [2025, 2040]
                or not all(0 < v < 1 for _, v in value)):
            raise ParameterError(f'stock_and_flow.{name} must be ((2025, value), (2040, value)), each value above 0 '
                                 f'and below 1, not {value!r}.')
    # 95 % of a triangle lies within 1 − √0.05 = 0.7764 of its half-width: a spread beyond it puts the triangle's foot
    # below 0 (04's type_ends).
    if not all(v < 1 - math.sqrt(0.05) for _, v in flow.type_share_spread):
        raise ParameterError(f'stock_and_flow.type_share_spread {flow.type_share_spread!r}: a spread of 0.7764 or more '
                             "puts a robot type's triangle below 0.")
    if not 0 < flow.hours_a_day <= 24:
        raise ParameterError(f'stock_and_flow.hours_a_day must be above 0 and at most 24, not {flow.hours_a_day}.')
    if sorted(t for t, _ in flow.runtime_2025_hours) != [1, 3, 5] or any(h <= 0 for _, h in flow.runtime_2025_hours):
        raise ParameterError('stock_and_flow.runtime_2025_hours must give hours above 0 for robot types 1, 3 and 5, '
                             f'not {flow.runtime_2025_hours!r}.')

    if not os.path.isabs(data.usgs_commodities) or not data.usgs_commodities.lower().endswith('.csv'):
        raise ParameterError(f'data.usgs_commodities must be an absolute path to a .csv file, not '
                             f'{data.usgs_commodities!r}.')

    for name in ('schemas_dir', 'composition_dir', 'composition_figures_dir', 'comparison_dir', 'parts_dir',
                 'parts_figures_dir', 'stock_and_flow_dir', 'stock_and_flow_figures_dir'):
        if not str(getattr(params.output, name)).strip():
            raise ParameterError(f'output.{name} is empty.')
    # The robot types whose pages are drawn: whole numbers from 1 to 6, each once, at least one.
    types = params.output.robot_types_with_pages
    if (not isinstance(types, tuple) or not types or len(set(types)) < len(types)
            or not all(isinstance(t, int) and 1 <= t <= 6 for t in types)):
        raise ParameterError('output.robot_types_with_pages must be a tuple of robot types from 1 to 6, each once, '
                             f'such as (1,), not {types!r}.')
    # Below 50 dpi the small print of a page cannot be read; above 600 a page takes megabytes and
    # seconds to open, for nothing a screen can show.
    if not 50 <= params.output.dpi <= 600:
        raise ParameterError(f'output.dpi must be between 50 and 600, not {params.output.dpi}.')


def current() -> Params:
    """The settings in force: the values written in this file, checked."""
    params = Params()
    validate(params)
    return params


def flatten(params: Params) -> list[tuple[str, str, str, object]]:
    """Every setting as (name, description, key, value), in the order of this file, for the register."""
    rows = []
    for section in fields(params):
        group = getattr(params, section.name)
        for item in fields(group):
            rows.append((item.name, item.metadata.get('doc', ''), f'{section.name}.{item.name}',
                         getattr(group, item.name)))
    return rows


def source_status(params: Params) -> str:
    """Which of the input files and folders are on disk, one line each."""
    lines = []
    for label, path in (('workbook', params.data.workbook), ('shared lists', params.data.shared_lists),
                        ('recipes', params.data.element_recipes), ('sources', params.data.sources_dir)):
        state = 'present' if os.path.exists(absolute(path)) else 'MISSING'
        lines.append(f'{label:<13} {path}: {state}')
    # The parts files: one per robot type taken apart, each in its folder.
    found = sorted(glob.glob(absolute(params.data.parts_taken_apart.format(folder='*'))))
    lines.append(f"{'taken apart':<13} {params.data.parts_taken_apart}: "
                 + (', '.join(os.path.basename(os.path.dirname(f)) for f in found) or 'none'))
    return '\n  '.join(lines)
