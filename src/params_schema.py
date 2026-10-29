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
                       folder per robot type, for stock-and-flow; and a page per robot type.

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

    # Robot type 1 (the Unitree G1) taken apart: its 12 joint kinds and where they sit (sheet Joints), the joint
    # module part by part as China Post Securities weighed it (JointParts), every other part (Parts), the materials of
    # the parts that hold more than one (Shares), its circuit boards and sensors (Boards, Sensors, SensorElements), the
    # numbers used across the sheets (Constants) and the sources (Sources). Agreed by Matthias on 2026-10-27
    # (documentation/claude/EVIDENCE.md, E2.8 to E2.8c, and his decisions of step 1); written by Claude, to be
    # corrected by Matthias in Excel. 01_schemas.py checks it.
    # SAFE TO CHANGE: only if the file moves.
    parts_taken_apart: str = field(
        default=os.path.join('data', 'researched', 'parts_taken_apart.xlsx'),
        metadata={'doc': 'Robot type 1 taken apart: its joints, the joint module part by part, every other part, '
                         'their materials, boards and sensors, for where its critical materials sit.'})

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
    # 01_schemas.py checks it; 02_composition.py draws robot type 1 over its robots.
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

    # The elements left off the element pages of 02 and 03, by their symbols (Matthias, 2026-10-29: "Hydrogene and
    # Oxygen have to go you should know this. Same for F, and N"; as in RAWCLICStockAndFlow, whose figures leave out
    # nitrogen, fluorine and oxygen, and RAWCLICDataCenters, whose leave out oxygen). The draws keep them, so that the
    # elements still add up to the materials in every draw and stock-and-flow can read any of them. 02 stops when a
    # symbol is not an element.
    # SAFE TO CHANGE: only on Matthias's word.
    elements_not_shown: tuple = field(
        default=('H', 'N', 'O', 'F'),
        metadata={'doc': 'The elements left off the element pages of 02 and 03 (Matthias, 2026-10-29); the draws '
                         'keep them.'})


@dataclass
class PartsParams:
    """How the stage that draws robot type 1 taken apart draws it (Monte Carlo); step 5 of its plan."""

    # How many times robot type 1 taken apart is drawn: 200,000, as 02. The real run is Matthias's; the tests and the
    # sandbox runs use few draws.
    # SAFE TO CHANGE: yes, between 100 and 1,000,000 (`current()` enforces it).
    draws: int = field(
        default=200_000,
        metadata={'doc': 'How many Monte Carlo draws are made of robot type 1 taken apart.'})

    # The start of its random numbers, fixed so that a rerun gives the same draws.
    # SAFE TO CHANGE: yes; another seed gives other draws of the same distributions.
    seed: int = field(
        default=1,
        metadata={'doc': 'The seed of the random numbers of robot type 1 taken apart.'})


@dataclass
class OutputParams:
    """Where the stages write. Paths are relative to the project root."""

    # The pages of 01_schemas.py: overview.png, faults.png and categories/<n>_<name>.png.
    schemas_dir: str = field(
        default=os.path.join('figures', 'schemas'),
        metadata={'doc': 'Where 01_schemas.py draws the overview, one page per category and the '
                         'faults.'})

    # What 02_composition.py writes for stock-and-flow, one folder per robot type (<n>_<name>/): the draws and their
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

    # What 02_composition.py writes of robot type 1 taken apart, for 04's figures: its draws of every material and
    # element in every kind of part. The project's own outputs (data/), until Matthias decides whether stock-and-flow
    # reads them (open point F of its plan), which would move them to data/consolidated/. Outputs: not in git.
    parts_dir: str = field(
        default=os.path.join('data', 'parts_taken_apart'),
        metadata={'doc': 'Where the draws of robot type 1 taken apart are written.'})

    # The figure of robot type 1 taken apart, as Matthias approved it on 2026-10-27 ("Looks good to me").
    parts_figures_dir: str = field(
        default=os.path.join('figures', 'parts_taken_apart'),
        metadata={'doc': 'Where the figure of robot type 1 taken apart is drawn.'})

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
    parts: PartsParams = field(default_factory=PartsParams)
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
    # A tuple of element symbols, each once and none empty (whether each is an element, 02 checks against 01's list).
    hidden = composition.elements_not_shown
    if (not isinstance(hidden, tuple) or not all(isinstance(e, str) and e.strip() for e in hidden)
            or len(set(hidden)) < len(hidden)):
        raise ParameterError('composition.elements_not_shown must be a tuple of element symbols, each once, such as '
                             f"('H', 'N', 'O', 'F'), not {hidden!r}.")

    # The sibling projects' files: absolute, .xlsx where a file is named.
    for name in ('vehicle_pcb_composition', 'vehicle_sensor_composition', 'data_center_element_composition',
                 'traction_motor_magnets', 'traction_motor_dir'):
        value = getattr(data, name)
        if not os.path.isabs(value) or (name != 'traction_motor_dir' and not value.lower().endswith('.xlsx')):
            raise ParameterError(f'data.{name} must be an absolute path' + ('' if name == 'traction_motor_dir' else
                                 ' to an .xlsx workbook') + f', not {value!r}.')
    parts = params.parts
    if not 100 <= parts.draws <= 1_000_000:
        raise ParameterError(f'parts.draws must be between 100 and 1,000,000, not {parts.draws}.')
    if not isinstance(parts.seed, int) or parts.seed < 0:
        raise ParameterError(f'parts.seed must be a whole number from 0 up, not {parts.seed!r}.')

    for name in ('schemas_dir', 'composition_dir', 'composition_figures_dir', 'comparison_dir', 'parts_dir',
                 'parts_figures_dir'):
        if not str(getattr(params.output, name)).strip():
            raise ParameterError(f'output.{name} is empty.')
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
                        ('recipes', params.data.element_recipes),
                        ('taken apart', params.data.parts_taken_apart), ('sources', params.data.sources_dir)):
        state = 'present' if os.path.exists(absolute(path)) else 'MISSING'
        lines.append(f'{label:<13} {path}: {state}')
    return '\n  '.join(lines)
