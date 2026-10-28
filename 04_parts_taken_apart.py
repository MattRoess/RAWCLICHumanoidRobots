"""
04_parts_taken_apart.py
=======================

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

Robot type 1 taken apart, drawn at random (Monte Carlo): where its critical elements sit, kind of part by kind of part,
and how sure we are. Press Run. No arguments; every setting is in `src/params_schema.py`. Run `00_parameters.py` and
`01_schemas.py` first.

Matthias, 2026-10-27: "the slipt into parts is just to get a deeper look into the robot, so that there is information
on where the interesting materials are and the recycling can be optimized", and "The different realisations of such a
type could vary on the compositon parts etc quite a bit. This has to be in the results." On 2026-10-28: "Yes, build
steps 5 and 6: stage 04 and its two approved figures, tests first, tried in a sandbox with few draws", with his answers
A to E (documentation/claude/HANDOVER.md, 2026-10-28; the method in documentation/claude/METHODOLOGY.md).

WHAT IT READS
-------------
  - `data.parts_taken_apart` (`data/researched/parts_taken_apart.xlsx`): the Unitree G1, AgiBot X1 and Fourier N1 part
    by part, through 01's `read_parts_taken_apart`;
  - the workbook, the shared lists and the element recipes, through 02's `read_inputs` (type 1's mass limits from the
    sheet Taxonomy; the recipes of type 1's aluminium and plastics, and of the NMC cells);
  - the sibling projects' files where they lie, never copied: RAWCLICVehicleElectronics' board metals per cm2 and
    sensor elements, RAWCLICDataCenters' tantalum per kg of board; and RAWCLICVehicleTractionMotor's own code, run in
    its own environment, for the elements of the magnets (answer C);
  - the settings `parts.draws`, `parts.seed`, the NMC cells' energy per kg (`composition.nmc_wh_per_kg_*`), the
    folders `output.parts_dir` and `output.parts_figures_dir`, and `output.dpi`.

WHAT IT CHECKS
--------------
Before drawing, every check 02 makes (01's checks of the workbook, the shared lists and the recipes, and its own), 01's
checks 18 to 20 of the data file, and its own (`check_parts`): every joint, part, board and sensor goes to a kind of
the figures, and every part is of one material, of shares, or computed in a way this stage knows. Any fault stops it
before anything is written. After drawing, it reports the share of draws where a remainder (a robot's frame, its
battery housing, a joint's structure) falls below zero; nothing is cut.

HOW IT DRAWS (N = `parts.draws` times; every triangle on the data file's min, mode and max; counts fixed)
-------------------------------------------------------------------------------------------------------
  - Each draw is one robot of type 1, the three equally likely ("Equal"), kept whole ("Real robot, varied").
  - Its own mass, a triangle on its range (sheet Constants); its varied mass, a triangle with type 1's limits as
    minimum and maximum and its own mass as mode (answer A). The factor varied over own scales what follows mass
    (answer B): the joints whole, with all inside them, and the parts of the kinds "Frame and shell" and "Battery pack"
    (the pack's energy too); not the boards outside the joints, the sensors, the cables and connectors, the fans and
    heat sinks, the hands and grippers.
  - The joints: each component of the G1's joint (sheet JointParts) drawn once in each draw for each joint size and
    shared by all the joints of that size (one design); the large joint's the small one's grams times its factor. The
    X1's and N1's joints: their module mass drawn for each joint kind, their inside the G1's of their size times the
    module mass over the G1 joint's mass at its modes (a fixed number, not the draw's own sum: nothing normalised),
    and the joint's structure (housing, end caps, output flange, small bearings) the explicit remainder, so that the
    joint weighs its drawn module mass (Matthias, 2026-10-28, "Yes, build it"; VERIFICATION.md V57).
  - A component or part of shares (sheet Shares): each share a triangle, the remainder 1 minus the others (02's
    `shares_drawn`). Elements: aluminium and plastics by type 1's recipes, the NMC cells by theirs with the energy per
    kg drawn (02's `RecipeDraws`); copper is copper; the magnets by the grade class drawn for their joint's heat group
    (sheet MagnetGrades: Matthias, 2026-10-28, "Heat has to matter", "Accept as proposed"), one draw of heat deciding
    for every joint how hot the robot is built for (the classes tied within a draw);
    boards: copper their mass times the copper share, gold, silver, palladium, tin and nickel their area times the car
    board category's mg per cm2, tantalum their mass times the data centres' share; sensors: their car sensor elements
    times their units. Steel, titanium and the mixed parts have no recipe: their kilograms are drawn, not their
    elements.
  - The battery cells: the pack's voltage times its capacity over the cells' energy per kg; its housing the pack less
    its cells and its management board. The cables: their length times the four conductors' cross-sections times
    copper's density, and their insulation. The frame: the varied mass less every other part.

WHAT IT WRITES
--------------
Into `output.parts_dir` (`data/parts_taken_apart/`, answer D; not in git), kg per draw, float32, row i the same draw in
every file, each with its columns, one name per line, in the .txt of the same name:

  robots.npy      the robot of each draw (its place in the sheet Robots), its own mass and its varied mass
  parts.npy       every joint kind, part, board and sensor of every robot (0 in the draws of the other robots)
  materials.npy   every material in every kind of part
  elements.npy    every element in every kind of part
  summary.csv     per element and per kind of part: mean, median, 2.5 % and 97.5 %; the remainders below zero;
                  the grade classes drawn for each heat group, as shares of the draws

And into `output.parts_figures_dir` (`figures/parts_taken_apart/`; not in git) the two figures Matthias approved, each
on pages of a screen's shape (16 × 9 inches, text 14 points and up): `robot_type_1_elements_1.png` and `_2.png` (one
histogram per critical element, each bar split by kind of part, three across) and `robot_type_1_overview_1.png` to
`_5.png` (the robot with its joints and parts, and two critical elements a page, one row per kind of part).

Where it sits: after 01_schemas.py; it uses 02_composition.py's drawing functions. Nothing reads what it writes yet.
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

Fault = schemas.Fault

# ------------------------------------------------------------------------------------------------------
# What the stage knows of the data file
# ------------------------------------------------------------------------------------------------------

TYPE = 1   # the robot type of the workbook's Taxonomy whose robots the data file holds

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

# The critical elements of the figures, in Matthias's order (V49): symbol (Nd+Pr: the two added) and name.
FIGURE_ELEMENTS = [('Cu', 'Copper'), ('Al', 'Aluminium'), ('Ag', 'Silver'), ('Au', 'Gold'), ('Pd', 'Palladium'),
                   ('Ta', 'Tantalum'), ('Nd+Pr', 'Neodymium and praseodymium'), ('Dy', 'Dysprosium'),
                   ('Ga', 'Gallium'), ('In', 'Indium')]
TRACKED = {'Cu', 'Al', 'Ag', 'Au', 'Pd', 'Ta', 'Nd', 'Pr', 'Dy', 'Ga', 'In'}   # for the overview's hatching

# What is written, in this order: each a file <name>.npy with its columns in <name>.txt.
TABLES = ('robots', 'parts', 'materials', 'elements')
HISTOGRAM_BINS = 70   # the bars of a distribution, as in RAWCLICDataCenters' figures
HELD_SHARE = 0.025    # a kind of part holding an element in fewer draws than this is not drawn (the 95 % rule)

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
class Inputs:
    """Everything 04 reads."""

    base: object          # 02's Inputs: the workbook, the shared lists and the element recipes
    apart: object         # schemas.PartsTakenApart: the robots of type 1 taken apart
    pcb: dict             # car board category -> element -> (min, mode, max), mg per cm2 of board
    sensor_types: dict    # car sensor type -> element -> (min, mode, max), mg per unit
    tantalum: tuple       # kg of tantalum per kg of board: min, mode, max
    mass_limits: tuple    # type 1's defining mass, kg: (lowest, highest)


def read_inputs(params: Params) -> Inputs:
    """The data file, the workbook, the shared lists, the recipes and the sibling projects' files, read with 01's and
    02's functions. Raises schemas.WorkbookError when a file cannot be read, or type 1's mass limits cannot."""
    base = composition.read_inputs(params)
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
    category = next((c for c in base.book.categories if c.number == TYPE), None)
    limits = schemas.type_limits(category) if category else None
    if limits is None:
        raise schemas.WorkbookError(f"type {TYPE}'s mass limits cannot be read from the workbook's sheet Taxonomy.")
    return Inputs(base, apart, pcb, sensor_types, tantalum, limits[1])


def base_robot(apart) -> str | None:
    """The robot whose joints follow the sheet JointParts directly (no module masses of their own): the G1, whose
    joint was weighed. The other robots' joints follow its inside."""
    found = [name for name in apart.robots
             if all(None in j.module_mass for j in apart.joints if j.robot == name)]
    return found[0] if len(found) == 1 else None


def check_parts(inputs: Inputs) -> list:
    """The checks 04 adds to 01's: one robot whose joints follow JointParts; every joint, part, board and sensor goes
    to a kind of the figures; every part computed in a way this stage knows; every robot of type 1; the driver board a
    component of JointParts; the recipes it uses there; the tantalum row read."""
    apart, faults = inputs.apart, []
    on = 'parts_taken_apart.xlsx: '
    if base_robot(apart) is None:
        faults.append(Fault(on + 'Joints', 0, 'exactly one robot must have no module masses (its joints follow the '
                                               'sheet JointParts).'))
    for robot in apart.robots.values():
        if robot.type != TYPE:
            faults.append(Fault(on + 'Robots', robot.row, f'{robot.name} is of type {robot.type}; 04 draws type '
                                                          f'{TYPE} only.'))
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
            faults.append(Fault(on + 'Parts', p.row, f"{p.robot}, {p.name}: 04 does not know how to compute "
                                                     f"'{p.computed}'."))
    for needed in (DRIVER_BOARD, *STRUCTURE):
        if needed not in {c.name for c in apart.joint_parts}:
            faults.append(Fault(on + 'JointParts', 0, f"no component '{needed}'."))
    rows = {(r.robot, r.family, r.shared): r.recipe for r in inputs.base.recipes.rows or []}
    for shared, family in RECIPE_FAMILY.items():
        if (TYPE, family, shared) not in rows:
            faults.append(Fault('element_recipes.xlsx: Rows', 0, f"no recipe for type {TYPE}'s {shared} "
                                                                 f"('{family}')."))
    if None in inputs.tantalum:
        faults.append(Fault('data.data_center_element_composition', 0, 'no Ta row with min, mode and max.'))
    return faults


def all_faults(inputs: Inputs, params: Params) -> list:
    """Every fault of the inputs: 02's (01's checks of the workbook, the lists and the recipes), 01's checks of the
    data file (18 to 20), and check_parts."""
    base, apart = inputs.base, inputs.apart
    return (composition.all_faults(base, params) + schemas.check_parts_taken_apart(apart, base.lists, params)
            + schemas.check_sibling_data(apart, params) + schemas.check_robot_types(apart, base.book.categories)
            + check_parts(inputs))


def grade_classes(inputs: Inputs) -> list:
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
    robot: np.ndarray     # the robot of each draw, as its place in `robots`
    own: np.ndarray       # kg: each draw's robot's own mass
    varied: np.ndarray    # kg: its mass varied within type 1's limits
    parts: tuple          # (columns '<robot>: <part>', N × columns): kg of all units of each row of each robot
    remainders: list      # the columns of `parts` that are remainders (frames, battery housings)
    structures: dict      # '<robot>: <joint> structure' -> kg of one joint's structure, a remainder (0 elsewhere)
    materials: tuple      # (columns (kind, material), N × columns): kg
    elements: dict        # (kind, element) -> kg in each draw
    estimated: dict       # (kind, element) -> the part of those kg resting on masses labelled E (TRACKED elements)
    hot: dict             # kind of joint -> True where its magnets are for 150 °C or more in most draws
    heat: np.ndarray      # the draw of heat, 0 to 1, that decides every heat group's grade class (tied)
    grades: dict          # heat group -> the grade class drawn in each draw


class Shared:
    """What is drawn once in each of the N draws and shared by every robot: the joint's components, the shares, the
    constants for all robots, the recipes, the sibling projects' metals and elements, the cells' energy per kg."""

    def __init__(self, inputs: Inputs, params: Params, magnets: dict, rng: np.random.Generator, n: int):
        apart, triangle = inputs.apart, composition.triangle
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
        self.shares = {item: composition.shares_drawn(rng, group, n) for item, group in groups.items()}
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
        recipes = composition.RecipeDraws(inputs.base.recipes, rng, n)
        rows = {(r.robot, r.family, r.shared): r.recipe for r in inputs.base.recipes.rows or []}
        self.recipe = {shared: recipes.elements(rows[(TYPE, family, shared)])
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

    def of(self, values: np.ndarray) -> np.ndarray:
        """This robot's rows of draws shared by all robots."""
        return values[self.rows]

    def element(self, kind: str, element: str, kg: np.ndarray, estimate: bool) -> None:
        self.elements[(kind, element)] = self.elements.get((kind, element), 0) + kg
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
                self.element(kind, element, kg * self.of(drawn[:, k]), estimate)
        elif material in self.shared.recipe:
            for element, share in self.shared.recipe[material].items():
                self.element(kind, element, kg * self.of(share), estimate)

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
        self.element(kind, 'Cu', kg * self.of(s.constant[BOARD_COPPER]), estimate)
        for metal in schemas.BOARD_METALS:
            self.element(kind, metal, area * self.of(s.pcb[(category, metal)]) / 1e6, estimate)
        self.element(kind, 'Ta', kg * self.of(s.tantalum), estimate)

    def sensor(self, kind: str, units: list, count: np.ndarray | float, estimate: bool) -> None:
        """The elements of `count` sensors, each made of `units` (car sensor type, units in one sensor)."""
        for car_type, per_sensor in units:
            for (t, element), mg in self.shared.sensor.items():
                if t == car_type:
                    self.element(kind, element, count * per_sensor * self.of(mg) / 1e6, estimate)


def draw(inputs: Inputs, params: Params, magnets: dict) -> Draws:
    """Robot type 1 taken apart, drawn `parts.draws` times (HOW IT DRAWS in the docstring at the top)."""
    apart, triangle = inputs.apart, composition.triangle
    n = params.parts.draws
    rng = np.random.default_rng(params.parts.seed)
    names = list(apart.robots)
    robot = rng.integers(len(names), size=n)            # answer "Equal": each robot as likely as the others
    shared = Shared(inputs, params, magnets, rng, n)
    low, high = inputs.mass_limits
    own, varied = np.zeros(n), np.zeros(n)
    done = []
    for k, name in enumerate(names):
        rows = np.flatnonzero(robot == k)
        constants = apart.constants[name]
        own_kg = triangle(rng, *constants[ROBOT_MASS][1], rows.size)
        varied_kg = triangle(rng, low, own_kg, high, rows.size)   # answer A: type 1's limits, its own mass the mode
        own[rows], varied[rows] = own_kg, varied_kg
        r = Robot(name, rows, shared, varied_kg / own_kg)
        draw_robot(r, inputs, constants, rng)
        frame = next(p for p in apart.parts if p.robot == name and p.computed.startswith(FRAME))
        rest = varied_kg - sum(r.parts.values())
        r.piece(f'{name}: {frame.name}', KIND_OF[frame.kind], frame.name, frame.material, rest,
                frame.label.startswith('E'))
        done.append(r)
    return assemble(n, names, robot, own, varied, done, apart, shared)


def draw_robot(r: Robot, inputs: Inputs, constants: dict, rng: np.random.Generator) -> None:
    """Every part of one robot but its frame: its joints with all inside them, its parts, boards and sensors."""
    apart, s, triangle, n, name = inputs.apart, r.shared, composition.triangle, r.n, r.name
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
            r.element('battery', element, cells_kg * r.of(share), cells.label.startswith('E'))
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
    return Draws(n, names, robot, own, varied, (part_columns, parts), remainders, structures,
                 (material_keys, materials), elements, estimated, hot, shared.heat, shared.grade)


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


def write(d: Draws, folder: str) -> None:
    """The draws at every level and their summary, into `folder` (WHAT IT WRITES in the docstring at the top)."""
    os.makedirs(folder, exist_ok=True)
    names = ', '.join(f'{k} {name}' for k, name in enumerate(d.robots))
    element_keys = [(kind, e) for kind in KINDS for e in element_order({e for k, e in d.elements if k == kind})]
    tables = {
        'robots': ([f'Robot ({names})', 'Own mass (kg)', 'Varied mass (kg)'],
                   np.column_stack([d.robot, d.own, d.varied])),
        'parts': d.parts,
        'materials': ([f'{KINDS[k][0]}: {m}' for k, m in d.materials[0]], d.materials[1]),
        'elements': ([f'{KINDS[k][0]}: {e}' for k, e in element_keys],
                     np.column_stack([d.elements[k] for k in element_keys])),
    }
    for table in TABLES:
        columns, draws = tables[table]
        np.save(os.path.join(folder, f'{table}.npy'), np.asarray(draws, dtype=np.float32))
        with open(os.path.join(folder, f'{table}.txt'), 'w', encoding='utf-8') as file:
            file.write('\n'.join(columns) + '\n')
    rows = [['Robot mass, varied', 'All kinds', *statistics(d.varied)]]
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


def by_kind(d: Draws, symbol: str) -> dict:
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


def robots_note(d: Draws, low: float, high: float) -> str:
    """What every draw is, for the footnotes."""
    names = ', '.join(d.robots[:-1]) + ' or ' + d.robots[-1]
    return (f'{d.n:,} draws, each one robot of type 1, the {names} (a third each), kept whole; its mass varied between '
            f'{low:.0f} and {high:.0f}\u00a0kg around its own, its joints, frame, shell and battery with it.')


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


def element_page(d: Draws, page: list, number: int, limits: tuple):
    """One page of the element figure Matthias approved (V49), for the three robots: its elements three across, each
    the stacked distribution of the robot's total; the legend of the kinds of part at the top; the footnote below."""
    columns = 3
    figure, axes = plt.subplots(2, columns, figsize=PAGE, squeeze=False)
    for k, (symbol, name) in enumerate(page):
        stacked_panel(axes[k // columns, k % columns], by_kind(d, symbol),
                      textwrap.fill(f'{name} ({symbol})', TITLE_WIDTH), k % columns == 0)
    for spare in axes.flatten()[len(page):]:
        spare.axis('off')
    figure.suptitle(f"Robot type 1 ({', '.join(d.robots)}): critical elements in one robot ({number} of "
                    f'{len(ELEMENT_PAGES)})', fontsize=HEADING, y=0.985)
    handles = [Patch(color=colour, label=label) for label, colour in KINDS.values()]
    figure.legend(handles=handles, loc='upper center', bbox_to_anchor=(0.5, 0.94), ncol=5, frameon=False,
                  fontsize=TEXT)
    figure.tight_layout(rect=(0, 0.2, 1, 0.86))
    figure.text(0.5, 0.01, note(
        'Bars: the draws, the height the share of the draws; solid line: the median; dotted line: the mean; dashed '
        'lines: 2.5th and 97.5th percentile (the 95% interval); each panel on its own scale and unit; each bar split '
        'into the weight its draws hold in each kind of part, the smaller lower; a kind of part holding the element '
        'in fewer than 2.5% of the draws is not drawn.', robots_note(d, *limits),
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


def draw_schema(axes, d: Draws) -> None:
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


def overview_page(d: Draws, page: list, number: int, limits: tuple):
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
        robots_note(d, *limits)), ha='center', va='bottom', fontsize=TEXT, color=MUTED)
    return figure


def figure_pages(d: Draws, limits: tuple) -> list:
    """Every page of both figures, as (file name, figure), in the order of FIGURES."""
    pages = [element_page(d, page, k + 1, limits) for k, page in enumerate(ELEMENT_PAGES)]
    pages += [overview_page(d, page, k + 1, limits) for k, page in enumerate(OVERVIEW_PAGES)]
    return list(zip(FIGURES, pages))


def draw_figures(d: Draws, params: Params, limits: tuple = (30, 50)) -> None:
    """Every page of both figures into `output.parts_figures_dir`."""
    folder = absolute(params.output.parts_figures_dir)
    for name, figure in figure_pages(d, limits):
        save(figure, os.path.join(folder, name), params.output.dpi)


# ------------------------------------------------------------------------------------------------------
# The run
# ------------------------------------------------------------------------------------------------------

def run(params: Params) -> int:
    """Read, check, draw, write, draw the figures, and report in plain words."""
    try:
        inputs = read_inputs(params)
    except schemas.WorkbookError as error:
        print(error, file=sys.stderr)
        return 1
    faults = all_faults(inputs, params)
    if faults:
        print(f'{len(faults)} fault(s) in the inputs; nothing drawn (01_schemas.py draws them into faults.png):',
              file=sys.stderr)
        for fault in faults:
            print(f'  {fault.sheet}, row {fault.row}: {fault.text}', file=sys.stderr)
        return 1
    magnets = magnet_fractions(params, grade_classes(inputs), params.parts.draws)
    d = draw(inputs, params, magnets)
    write(d, absolute(params.output.parts_dir))
    draw_figures(d, params, inputs.mass_limits)
    for symbol, name in FIGURE_ELEMENTS:
        total = sum(by_kind(d, symbol).values())
        per, unit = figure_unit(total)
        mean, median, low, high = statistics(total / per)
        print(f'{name} in one robot: median {figure_number(median)} {unit}, mean {figure_number(mean)} {unit} (95 %: '
              f'{figure_number(low)} to {figure_number(high)})')
    for column, share in below_zero(d).items():
        if share > 0:
            print(f'{column} is below zero in {100 * share:.1f} % of its draws (reported, not cut).')
    print(f'Written into {params.output.parts_dir}/, and the two figures into {params.output.parts_figures_dir}/.')
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
