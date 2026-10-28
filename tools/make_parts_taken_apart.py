"""
Builder of data/researched/parts_taken_apart.xlsx: the robots of type 1 taken apart, part by part.

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

Matthias, 2026-10-27: "Yes, put the builder in tools/make_parts_taken_apart.py as proposed, with its test and
documents"; 2026-10-28: "Yes, rewrite" (the first builder, in Claude's scratch folder, was lost with it).

WHAT IT DOES
------------
It writes the data file of the robots of type 1 taken apart: the Unitree G1, the AgiBot X1 and the Fourier N1, each
part by part, with the materials, boards and sensors of each, so that the model can show where in a robot its
critical materials sit (Matthias, 2026-10-27: "the slipt into parts is just to get a deeper look into the robot, so
that there is information on where the interesting materials are and the recycling can be optimized"). Every value
below was agreed by Matthias on 2026-10-27 and is documented, with its sources, in documentation/claude/EVIDENCE.md
E2.8 to E2.8e; each row of the file names its own sources.

WHAT IT READS AND WRITES
------------------------
It reads nothing but 00's settings (src/params_schema.py, for where the file goes). It writes one file, the path of
`data.parts_taken_apart` (data/researched/parts_taken_apart.xlsx, git-ignored), and replaces the file there. The
values are held here: a change to them is made in this file, not in the .xlsx, where it would be lost at the next run.

WHERE IT SITS
-------------
It is not a stage of the model: it writes one of the model's inputs, not a result, so it stands in tools/ and has no
number. 01_schemas.py reads and checks the file (METHODOLOGY.md checks 18 to 20); the stage that draws it is to come
(step 5 of the plan in documentation/claude/HANDOVER.md). Press Run: no arguments. Importing this file writes nothing;
tests/test_make_parts_taken_apart.py checks that what it writes passes 01's checks and equals the file on disk.
"""
import os
import sys

import openpyxl
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

# The project's root, so that its settings (src/params_schema.py) can be imported when this file is run from tools/.
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
from src.params_schema import Params, absolute  # noqa: E402

# The grey of every sheet's first row, so that the headings stand apart from the values.
HEADING_FILL = PatternFill('solid', fgColor='FFEEEEEE')
# The width of the About sheet's one column, in characters.
ABOUT_WIDTH = 150

# --- About ----------------------------------------------------------------------------------------------------------
# The file's own description, one line per row of its first column (None leaves the row empty).
ABOUT = [
    'Robot type 1 taken apart: the Unitree G1, the AgiBot X1 and the Fourier N1, part by '
    'part, for where their critical materials sit',
    None,
    'Agreed by Matthias on 2026-10-27: documentation/claude/EVIDENCE.md E2.8, E2.8b and '
    'E2.8c, with his decisions of step 1 (remainders, rotor NdFeB, values marked E, hot '
    'joints); the X1 and N1 from E2.8e (step 2b). Type 1 is "informed by the G1, X1 and '
    'N1" (the Booster T1, 1.18 m, out). Written by Claude.',
    "Sheet Robots: each robot, its maker, its type, the maker's height and stated mass. "
    "Every sheet with a column Robot holds each robot's own rows; JointParts, Shares and "
    "SensorElements are one set for all three (the G1's joint insides, scaled to each "
    'joint\'s module mass: "We can assume, they are similar within given ranges").',
    "Labels: W weighed (China Post Securities' teardown, T1); S from a source (named in "
    'Sources); E an estimate, with at least half to 1.5 times its mode ("Estimates should '
    'be larger than known numbers").',
    'Every range is min / mode / max. A remainder takes what the other shares or parts '
    'leave; nothing is rescaled.',
    None,
    'Sheet Joints: the 12 joint kinds of the basic G1 (23 joints), where they sit, torque, '
    'cooling, magnet grade.',
    'Sheet JointParts: the joint module part by part: the small joint as weighed (T1, '
    'slide 43), the 13 not weighed at 0.5 / 1 / 1.5 times; the large joint as the small '
    'one times a factor from size and torque.',
    'Sheet Parts: every other part, with its count, kind, body region and mass of one.',
    'Sheet Shares: the materials of the parts and components that hold more than one; the '
    'remainder is named.',
    'Sheet Boards: each circuit board, its area and the car board category whose gold, '
    'silver, palladium, tin and nickel per cm2 it takes (read where they lie).',
    'Sheets Sensors and SensorElements: each sensor, and the car sensor elements it is '
    'made of (read where they lie).',
    'Sheet Constants: each robot\'s own numbers, and the shared ones once (robot "all").',
    'Sheet Sources: every source code used here, as in EVIDENCE.md E2.1.',
    None,
    'Read where they lie, not copied: RAWCLICVehicleElectronics '
    'Data/04_VehiclePCBComposition.xlsx (board metals per cm2 by category) and '
    'Data/07_VehicleSensorComposition.xlsx (sensor elements); RAWCLICDataCenters '
    'data/researched/04_DataCenterElementComposition.xlsx, sheet BoardsAndComponents '
    '(tantalum per kg of board); RAWCLICVehicleTractionMotor '
    'data/raw/10_MaterialElementDefinitions.xlsx, sheet PermanentMagnetNdFeB (NdFeB grade '
    "classes); this project's element_recipes.xlsx, recipe NMC cylindrical (the cells).",
]


# --- Robots ---------------------------------------------------------------------------------------------------------
# The robots of type 1: each with its maker, its type, the maker's height and stated mass (EVIDENCE.md
# E2.8e). Matthias, 2026-10-27: "Type 1 is informed by the G1, X1 and N1"; 01 checks that each lies inside
# its type's height and mass in the workbook's sheet Taxonomy.
ROBOTS_HEADINGS = ['Robot', 'Maker', 'Type', 'Height (m)', 'Stated mass (kg)', 'Sources']
ROBOTS_ROWS = [
    ('Unitree G1', 'Unitree', 1, 1.32, 35, 'U1: "1320x450x200mm", "About 35kg"'),
    ('AgiBot X1', 'AgiBot', 1, 1.3, 33, 'X1e: "130 cm", "33kg", "31DoF"'),
    ('Fourier N1', 'Fourier', 1, 1.245, 39, 'N1a: "1245 mm × 441 mm × 202 mm", "≈39 kg"'),
]
ROBOTS_WIDTHS = [14, 10, 6, 10, 14, 60]

# --- Joints ---------------------------------------------------------------------------------------------------------
# Every joint kind of every robot: where it sits, its torque, which of the G1's two joint designs its inside
# follows (Module), its module mass (the X1's from AgiBot, the N1's from the joint-mass fit, none for the G1,
# whose JointParts give it), its magnet grade class. The G1: EVIDENCE.md E2.8 and E2.8c; the X1 and N1: E2.8e.
JOINTS_HEADINGS = ['Robot', 'Number', 'Joint', 'Joints in the robot', 'Module', 'Torque limit (N·m)',
                   'Module mass, min (kg)', 'mode (kg)', 'max (kg)', 'Cooling', 'Magnet grade class (base)',
                   'Magnet grade scenarios', 'Body region', 'Sources', 'Basis']
JOINTS_ROWS = [
    ('Unitree G1', 1, 'Hip pitch', 2, 'large', 88, None, None, None, 'two centrifugal fans per hip', 'SH', 'UH; EH',
     'Legs', 'U3; T1 slides 11, 18, 41; T3',
     'Hot, air-cooled: magnets for 150 °C, 180 and 200 °C as scenarios. Matthias, '
     '2026-10-27, step 1: "Accept all" (EVIDENCE.md E2.8)'),
    ('Unitree G1', 2, 'Hip roll', 2, 'large', 88, None, None, None, 'two centrifugal fans per hip', 'SH', 'UH; EH',
     'Legs', 'U3; T1 slides 11, 18; T3',
     'Hot, air-cooled: magnets for 150 °C, 180 and 200 °C as scenarios. Matthias, '
     '2026-10-27, step 1: "Accept all" (EVIDENCE.md E2.8)'),
    ('Unitree G1', 3, 'Hip yaw', 2, 'large', 88, None, None, None, 'two centrifugal fans per hip', 'SH', 'UH; EH',
     'Legs', 'U3; T1 slides 11, 18; T3',
     'Hot, air-cooled: magnets for 150 °C, 180 and 200 °C as scenarios. Matthias, '
     '2026-10-27, step 1: "Accept all" (EVIDENCE.md E2.8)'),
    ('Unitree G1', 4, 'Knee', 2, 'large', 139, None, None, None, 'copper vapour chamber into the frame', 'SH',
     'UH; EH', 'Legs', 'U3; U1 90 (basic) and 120 N·m (EDU); T1 slides 18, 40, 42; T3k',
     'Hot, air-cooled: magnets for 150 °C, 180 and 200 °C as scenarios. Matthias, '
     '2026-10-27, step 1: "Accept all" (EVIDENCE.md E2.8)'),
    ('Unitree G1', 5, 'Ankle pitch', 2, 'small', 35, None, None, None, 'passive', 'SH', 'UH; EH', 'Legs',
     'U3; T1 slides 11, 18, 20',
     'Hot, air-cooled: magnets for 150 °C, 180 and 200 °C as scenarios. Matthias, '
     '2026-10-27, step 1: "Accept all" (EVIDENCE.md E2.8)'),
    ('Unitree G1', 6, 'Ankle roll', 2, 'small', 35, None, None, None, 'passive', 'SH', 'UH; EH', 'Legs',
     'U3; T1 slides 11, 18, 20',
     'Hot, air-cooled: magnets for 150 °C, 180 and 200 °C as scenarios. Matthias, '
     '2026-10-27, step 1: "Accept all" (EVIDENCE.md E2.8)'),
    ('Unitree G1', 7, 'Waist yaw', 1, 'large', 88, None, None, None, 'centrifugal fan', 'SH', 'UH; EH', 'Torso',
     'U3; T1 slides 11, 41',
     'Hot, air-cooled: magnets for 150 °C, 180 and 200 °C as scenarios. Matthias, '
     '2026-10-27, step 1: "Accept all" (EVIDENCE.md E2.8)'),
    ('Unitree G1', 8, 'Shoulder pitch', 2, 'small', 25, None, None, None, 'passive', 'H', None, 'Arms',
     'U3; T1 slides 11, 18',
     'Arm joint, at most 2 kg payload: magnets for 120 °C. Matthias, 2026-10-27, step 1: '
     '"Accept all" (EVIDENCE.md E2.8)'),
    ('Unitree G1', 9, 'Shoulder roll', 2, 'small', 25, None, None, None, 'passive', 'H', None, 'Arms',
     'U3; T1 slides 11, 18',
     'Arm joint, at most 2 kg payload: magnets for 120 °C. Matthias, 2026-10-27, step 1: '
     '"Accept all" (EVIDENCE.md E2.8)'),
    ('Unitree G1', 10, 'Shoulder yaw', 2, 'small', 25, None, None, None, 'passive', 'H', None, 'Arms',
     'U3; T1 slides 11, 18',
     'Arm joint, at most 2 kg payload: magnets for 120 °C. Matthias, 2026-10-27, step 1: '
     '"Accept all" (EVIDENCE.md E2.8)'),
    ('Unitree G1', 11, 'Elbow', 2, 'small', 25, None, None, None, 'passive', 'H', None, 'Arms',
     'U3; T1 slides 11, 18',
     'Arm joint, at most 2 kg payload: magnets for 120 °C. Matthias, 2026-10-27, step 1: '
     '"Accept all" (EVIDENCE.md E2.8)'),
    ('Unitree G1', 12, 'Wrist roll', 2, 'small', 25, None, None, None, 'passive', 'H', None, 'Arms',
     'U3; T1 slide 11',
     'Arm joint, at most 2 kg payload: magnets for 120 °C. Matthias, 2026-10-27, step 1: '
     '"Accept all" (EVIDENCE.md E2.8)'),
    ('AgiBot X1', 1, 'Hip pitch', 2, 'large', 150, 1.22, 1.28, 1.34, 'not stated', 'SH', 'UH; EH', 'Legs',
     'X1b R86-3 1.28 kg; X1c (150 N·m)',
     'Hot, air-cooled (legs, waist): magnets for 150 °C, 180 and 200 °C as scenarios, as '
     'the G1 (E2.8e).'),
    ('AgiBot X1', 2, 'Hip roll', 2, 'large', 150, 1.22, 1.28, 1.34, 'not stated', 'SH', 'UH; EH', 'Legs',
     'X1b R86-3 1.28 kg; X1c (150 N·m)',
     'Hot, air-cooled (legs, waist): magnets for 150 °C, 180 and 200 °C as scenarios, as '
     'the G1 (E2.8e).'),
    ('AgiBot X1', 3, 'Hip yaw', 2, 'large', 50, 0.77, 0.81, 0.85, 'not stated', 'SH', 'UH; EH', 'Legs',
     'X1b R86-2 0.81 kg; X1c (50 N·m)',
     'Hot, air-cooled (legs, waist): magnets for 150 °C, 180 and 200 °C as scenarios, as '
     'the G1 (E2.8e).'),
    ('AgiBot X1', 4, 'Knee', 2, 'large', 150, 1.22, 1.28, 1.34, 'not stated', 'SH', 'UH; EH', 'Legs',
     'X1b R86-3 1.28 kg; X1c (150 N·m)',
     'Hot, air-cooled (legs, waist): magnets for 150 °C, 180 and 200 °C as scenarios, as '
     'the G1 (E2.8e).'),
    ('AgiBot X1', 5, 'Ankle pitch', 2, 'small', 80, 0.19, 0.2, 0.21, 'not stated', 'SH', 'UH; EH', 'Legs',
     'X1b L28 push rod 0.20 kg; X1c (80 N·m at the ankle)',
     'Hot, air-cooled (legs, waist): magnets for 150 °C, 180 and 200 °C as scenarios, as '
     'the G1 (E2.8e).'),
    ('AgiBot X1', 6, 'Ankle roll', 2, 'small', 80, 0.19, 0.2, 0.21, 'not stated', 'SH', 'UH; EH', 'Legs',
     'X1b L28 push rod 0.20 kg; X1c (80 N·m at the ankle)',
     'Hot, air-cooled (legs, waist): magnets for 150 °C, 180 and 200 °C as scenarios, as '
     'the G1 (E2.8e).'),
    ('AgiBot X1', 7, 'Waist', 3, 'large', 80, 0.77, 0.81, 0.85, 'not stated', 'SH', 'UH; EH', 'Torso',
     'X1b R86-2 0.81 kg, 80 N·m peak; X1a "腰部连杆组件"; 9 R86-2 less 2 hips and 4 shoulders '
     '(E2.8e)',
     'Hot, air-cooled (legs, waist): magnets for 150 °C, 180 and 200 °C as scenarios, as '
     'the G1 (E2.8e).'),
    ('AgiBot X1', 8, 'Shoulder pitch', 2, 'large', 80, 0.77, 0.81, 0.85, 'not stated', 'H', None, 'Arms',
     'X1b R86-2 0.81 kg, 80 N·m peak (E2.8e)', 'Arm joint: magnets for 120 °C, as the G1 (E2.8e).'),
    ('AgiBot X1', 9, 'Shoulder roll', 2, 'large', 80, 0.77, 0.81, 0.85, 'not stated', 'H', None, 'Arms',
     'X1b R86-2 0.81 kg, 80 N·m peak (E2.8e)', 'Arm joint: magnets for 120 °C, as the G1 (E2.8e).'),
    ('AgiBot X1', 10, 'Shoulder yaw', 2, 'small', 19, 0.43, 0.45, 0.47, 'not stated', 'H', None, 'Arms',
     'X1b R52 0.45 kg, 19 N·m peak', 'Arm joint: magnets for 120 °C, as the G1 (E2.8e).'),
    ('AgiBot X1', 11, 'Elbow', 2, 'small', 19, 0.43, 0.45, 0.47, 'not stated', 'H', None, 'Arms',
     'X1b R52 0.45 kg, 19 N·m peak', 'Arm joint: magnets for 120 °C, as the G1 (E2.8e).'),
    ('AgiBot X1', 12, 'Wrist (yaw, pitch, roll)', 6, 'small', 19, 0.43, 0.45, 0.47, 'not stated', 'H', None, 'Arms',
     'X1b R52 0.45 kg, 19 N·m peak', 'Arm joint: magnets for 120 °C, as the G1 (E2.8e).'),
    ('Fourier N1', 1, 'Hip pitch', 2, 'large', 90, 0.44, 0.88, 1.32, 'not stated', 'SH', 'UH; EH', 'Legs',
     "N1a (90 N·m; N1b 95); the joint-mass fit on AgiBot's actuators, ± 50 % (E2.8e)",
     'Hot, air-cooled (legs, waist): magnets for 150 °C, 180 and 200 °C as scenarios, as '
     'the G1 (E2.8e).'),
    ('Fourier N1', 2, 'Hip roll', 2, 'large', 54, 0.35, 0.7, 1.05, 'not stated', 'SH', 'UH; EH', 'Legs',
     "N1a (54 N·m); the joint-mass fit on AgiBot's actuators, ± 50 % (E2.8e)",
     'Hot, air-cooled (legs, waist): magnets for 150 °C, 180 and 200 °C as scenarios, as '
     'the G1 (E2.8e).'),
    ('Fourier N1', 3, 'Hip yaw', 2, 'large', 54, 0.35, 0.7, 1.05, 'not stated', 'SH', 'UH; EH', 'Legs',
     "N1a (54 N·m); the joint-mass fit on AgiBot's actuators, ± 50 % (E2.8e)",
     'Hot, air-cooled (legs, waist): magnets for 150 °C, 180 and 200 °C as scenarios, as '
     'the G1 (E2.8e).'),
    ('Fourier N1', 4, 'Knee', 2, 'large', 90, 0.44, 0.88, 1.32, 'not stated', 'SH', 'UH; EH', 'Legs',
     "N1a (90 N·m; N1b 95); the joint-mass fit on AgiBot's actuators, ± 50 % (E2.8e)",
     'Hot, air-cooled (legs, waist): magnets for 150 °C, 180 and 200 °C as scenarios, as '
     'the G1 (E2.8e).'),
    ('Fourier N1', 5, 'Ankle pitch', 2, 'small', 30, 0.27, 0.54, 0.81, 'not stated', 'SH', 'UH; EH', 'Legs',
     "N1a (30 N·m); the joint-mass fit on AgiBot's actuators, ± 50 % (E2.8e)",
     'Hot, air-cooled (legs, waist): magnets for 150 °C, 180 and 200 °C as scenarios, as '
     'the G1 (E2.8e).'),
    ('Fourier N1', 6, 'Ankle roll', 2, 'small', 30, 0.27, 0.54, 0.81, 'not stated', 'SH', 'UH; EH', 'Legs',
     "N1a (30 N·m); the joint-mass fit on AgiBot's actuators, ± 50 % (E2.8e)",
     'Hot, air-cooled (legs, waist): magnets for 150 °C, 180 and 200 °C as scenarios, as '
     'the G1 (E2.8e).'),
    ('Fourier N1', 7, 'Waist yaw', 1, 'large', 54, 0.35, 0.7, 1.05, 'not stated', 'SH', 'UH; EH', 'Torso',
     "N1a (54 N·m); the joint-mass fit on AgiBot's actuators, ± 50 % (E2.8e)",
     'Hot, air-cooled (legs, waist): magnets for 150 °C, 180 and 200 °C as scenarios, as '
     'the G1 (E2.8e).'),
    ('Fourier N1', 8, 'Shoulder pitch', 2, 'large', 54, 0.35, 0.7, 1.05, 'not stated', 'H', None, 'Arms',
     "N1a (54 N·m); the joint-mass fit on AgiBot's actuators, ± 50 % (E2.8e)",
     'Arm joint: magnets for 120 °C, as the G1 (E2.8e).'),
    ('Fourier N1', 9, 'Shoulder roll', 2, 'small', 30, 0.27, 0.54, 0.81, 'not stated', 'H', None, 'Arms',
     "N1a (30 N·m); the joint-mass fit on AgiBot's actuators, ± 50 % (E2.8e)",
     'Arm joint: magnets for 120 °C, as the G1 (E2.8e).'),
    ('Fourier N1', 10, 'Shoulder yaw', 2, 'small', 30, 0.27, 0.54, 0.81, 'not stated', 'H', None, 'Arms',
     "N1a (30 N·m); the joint-mass fit on AgiBot's actuators, ± 50 % (E2.8e)",
     'Arm joint: magnets for 120 °C, as the G1 (E2.8e).'),
    ('Fourier N1', 11, 'Elbow', 2, 'small', 30, 0.27, 0.54, 0.81, 'not stated', 'H', None, 'Arms',
     "N1a (30 N·m); the joint-mass fit on AgiBot's actuators, ± 50 % (E2.8e)",
     'Arm joint: magnets for 120 °C, as the G1 (E2.8e).'),
    ('Fourier N1', 12, 'Wrist yaw', 2, 'small', 30, 0.27, 0.54, 0.81, 'not stated', 'H', None, 'Arms',
     "N1a (30 N·m); the joint-mass fit on AgiBot's actuators, ± 50 % (E2.8e)",
     'Arm joint: magnets for 120 °C, as the G1 (E2.8e).'),
]
JOINTS_WIDTHS = [12, 8, 22, 10, 9, 10, 10, 9, 9, 30, 12, 12, 11, 50, 90]

# --- JointParts -----------------------------------------------------------------------------------------------------
# The G1's small joint part by part as China Post Securities weighed it (slide 43), the small joints not
# weighed at 0.5 / 1 / 1.5 times, and the large joint as the small one times a factor (EVIDENCE.md E2.8).
# One set for all robots, scaled to each joint's module mass ("similar within given ranges").
JOINTPARTS_HEADINGS = ['Component', 'Small joint, weighed (g)', 'Small joints not weighed: times min', 'times mode',
                       'times max', 'Material (one material only)', 'Large joint: factor min', 'factor mode',
                       'factor max', 'Why the factor', 'Label', 'Sources']
JOINTPARTS_ROWS = [
    ('Motor stator', 94.3, 0.5, 1, 1.5, None, 1, 1.78, 2.67, "the motor's cross-section, 80 against 60 mm across",
     'W; E for the spread and the factor',
     'T1 slide 43 (figure 37); factors EVIDENCE.md E2.8; Matthias, 2026-10-27, step 1: '
     '"Accept all" (EVIDENCE.md E2.8)'),
    ('Motor rotor', 42.9, 0.5, 1, 1.5, None, 1, 1.78, 2.67, "the motor's cross-section",
     'W; E for the spread and the factor',
     'T1 slide 43 (figure 37); factors EVIDENCE.md E2.8; Matthias, 2026-10-27, step 1: '
     '"Accept all" (EVIDENCE.md E2.8)'),
    ('Magnet carrier', 16.9, 0.5, 1, 1.5, None, 1, 1.78, 2.67, "the motor's cross-section",
     'W; E for the spread and the factor',
     'T1 slide 43 (figure 37); factors EVIDENCE.md E2.8; Matthias, 2026-10-27, step 1: '
     '"Accept all" (EVIDENCE.md E2.8)'),
    ('Gear stage 1, sun gear', 8, 0.5, 1, 1.5, 'Steel', 1.17, 2.33, 3.56,
     'from the cross-section alone to growing with the torque (99.3 against 27.9 N·m); mode '
     '3.56^(2/3)', 'W; E for the spread and the factor',
     'T1 slide 43 (figure 37); factors EVIDENCE.md E2.8; Matthias, 2026-10-27, step 1: '
     '"Accept all" (EVIDENCE.md E2.8)'),
    ('Gear stage 1, planets and carrier with stage 2 sun gear', 25.3, 0.5, 1, 1.5, 'Steel', 1.17, 2.33, 3.56,
     'as the sun gear', 'W; E for the spread and the factor',
     'T1 slide 43 (figure 37); factors EVIDENCE.md E2.8; Matthias, 2026-10-27, step 1: '
     '"Accept all" (EVIDENCE.md E2.8)'),
    ('Gear stage 1, ring gear', 24.1, 0.5, 1, 1.5, 'Steel', 1.17, 2.33, 3.56, 'as the sun gear',
     'W; E for the spread and the factor',
     'T1 slide 43 (figure 37); factors EVIDENCE.md E2.8; Matthias, 2026-10-27, step 1: '
     '"Accept all" (EVIDENCE.md E2.8)'),
    ('Gear stage 2, planets, carrier and crossed roller bearing', 74, 0.5, 1, 1.5, None, 1.17, 2.33, 3.56,
     'as the sun gear', 'W; E for the spread and the factor',
     'T1 slide 43 (figure 37); factors EVIDENCE.md E2.8; Matthias, 2026-10-27, step 1: '
     '"Accept all" (EVIDENCE.md E2.8)'),
    ('Gear stage 2, ring gear', 23.8, 0.5, 1, 1.5, 'Steel', 1.17, 2.33, 3.56, 'as the sun gear',
     'W; E for the spread and the factor',
     'T1 slide 43 (figure 37); factors EVIDENCE.md E2.8; Matthias, 2026-10-27, step 1: '
     '"Accept all" (EVIDENCE.md E2.8)'),
    ('Driver board', 12.8, 0.5, 1, 1.5, 'Electronics', 1.78, 3.56, 5.33,
     'one, two or three boards of the larger size (T3k: "a stack")', 'W; E for the spread and the factor',
     'T1 slide 43 (figure 37); factors EVIDENCE.md E2.8; Matthias, 2026-10-27, step 1: '
     '"Accept all" (EVIDENCE.md E2.8)'),
    ('Two small bearings', 11, 0.5, 1, 1.5, 'Steel', 1, 1.78, 2.67, 'the area', 'W; E for the spread and the factor',
     'T1 slide 43 (figure 37); factors EVIDENCE.md E2.8; Matthias, 2026-10-27, step 1: '
     '"Accept all" (EVIDENCE.md E2.8)'),
    ('Housing', 79.3, 0.5, 1, 1.5, 'Aluminium', 1, 1.39, 2.09, "the joint's surface",
     'W; E for the spread and the factor',
     'T1 slide 43 (figure 37); factors EVIDENCE.md E2.8; Matthias, 2026-10-27, step 1: '
     '"Accept all" (EVIDENCE.md E2.8)'),
    ('Two end caps', 23.7, 0.5, 1, 1.5, 'Aluminium', 1, 1.78, 2.67, 'the area', 'W; E for the spread and the factor',
     'T1 slide 43 (figure 37); factors EVIDENCE.md E2.8; Matthias, 2026-10-27, step 1: '
     '"Accept all" (EVIDENCE.md E2.8)'),
    ('Output flange', 50.8, 0.5, 1, 1.5, 'Steel', 1, 1.78, 2.67, 'the area', 'W; E for the spread and the factor',
     'T1 slide 43 (figure 37); factors EVIDENCE.md E2.8; Matthias, 2026-10-27, step 1: '
     '"Accept all" (EVIDENCE.md E2.8)'),
    ('Other', 38.1, 0.5, 1, 1.5, None, 1, 1.78, 2.67, 'the area', 'W; E for the spread and the factor',
     'T1 slide 43 (figure 37); factors EVIDENCE.md E2.8; Matthias, 2026-10-27, step 1: '
     '"Accept all" (EVIDENCE.md E2.8)'),
]
JOINTPARTS_WIDTHS = [44, 12, 12, 9, 9, 16, 10, 9, 9, 60, 14, 60]

# --- Parts ----------------------------------------------------------------------------------------------------------
# Every other part of each robot: its number, the figure's row it falls in, its body region, the mass of one
# and its one material, its shares (sheet Shares), or what it is computed from; one part per robot takes the
# robot's remainder (the frame). EVIDENCE.md E2.8, E2.8c, E2.8e.
PARTS_HEADINGS = ['Robot', 'Part', 'Number in the robot', "Kind (the figure's row)", 'Body region',
                  'Mass of one, min (kg)', 'mode (kg)', 'max (kg)', 'Material (one material only)',
                  'Remainder of, or computed from', 'Label', 'Sources']
PARTS_ROWS = [
    ('Unitree G1', 'Joint module, small', 14, 'Ankles and arms', 'Legs 4, Arms 10', None, None, None, None,
     'the sum of JointParts', 'W, E', 'T1 slides 11, 43'),
    ('Unitree G1', 'Joint module, large', 9, 'Hips, knees and waist', 'Legs 8, Torso 1', None, None, None, None,
     'the sum of JointParts', 'E', 'T1 slide 11; T3k'),
    ('Unitree G1', 'Encoders (two per joint)', 46, 'In the joints', 'as their joints', None, None, None, None,
     'Sensors and SensorElements (Encoder)', 'S', 'U1, U2 "Dual encoder"; elements: SensorElements'),
    ('Unitree G1', 'Knee vapour chamber and copper strip', 2, 'Knees', 'Legs', 0.01, 0.02, 0.04, 'Copper', None, 'E',
     'T1 slide 40; T3'),
    ('Unitree G1', 'Hip fan', 2, 'Hips', 'Legs', 0.005, 0.01, 0.02, None, None, 'E',
     'T3 (two per hip joint pair); T1 slide 39'),
    ('Unitree G1', 'Waist fan', 1, 'Waist', 'Torso', 0.005, 0.01, 0.02, None, None, 'E', 'T1 slide 41'),
    ('Unitree G1', 'Main board fan', 1, 'Torso boards', 'Torso', 0.005, 0.01, 0.02, None, None, 'E', 'T1 slide 39'),
    ('Unitree G1', 'Main board heat sink', 1, 'Torso boards', 'Torso', 0.05, 0.1, 0.2, 'Aluminium', None, 'E',
     'T1 slide 39'),
    ('Unitree G1', 'Battery pack', 1, 'Battery pack', 'Torso', 2.25, 2.5, 2.75, None,
     'its cells, its management board (Boards) and its housing (the rows below)', 'S',
     'T1 slide 25 ("~2.5kg"); ± 10 % for the "~" (E2.8e, accepted)'),
    ('Unitree G1', 'Battery cells', 1, 'Battery pack', 'Torso', None, None, None, 'Battery materials',
     "from the energy: Constants voltage × capacity over the NMC cell's Wh/kg", 'S',
     'T1 slide 25; element_recipes.xlsx NMC cylindrical; composition.nmc_wh_per_kg_*'),
    ('Unitree G1', 'Battery housing, busbars and wires', 1, 'Battery pack', 'Torso', None, None, None, 'Mixed',
     'the battery pack, less its cells and its management board', 'E',
     'Matthias, 2026-10-27, step 1: "Accept all" (EVIDENCE.md E2.8)'),
    ('Unitree G1', 'Cable conductors and insulation', 1, 'Cables', 'Whole body', None, None, None, None,
     'from Constants: length, cross-sections, insulation', 'E', 'T1 slides 3, 35, 36; T3k'),
    ('Unitree G1', 'XT30 (2+2) connectors (two per joint)', 46, 'Cables', 'Whole body', 0.0015, 0.003, 0.0045, None,
     None, 'E', 'T3k ("XT30 2+2"); T1 slide 12'),
    ('Unitree G1', 'Fixed plastic hands', 2, 'Arms', 'Arms', 0.12, 0.17, 0.22, 'Plastics', None, 'S',
     'T1 slide 18; U3 (0.170 kg each, a design value)'),
    ('Unitree G1', 'Screws', 1, 'Frame and shell', 'Whole body', 0.2, 0.5, 1, 'Steel', None, 'E', 'no source'),
    ('Unitree G1', 'Shell and torso plastic parts, silicone, foam', 1, 'Frame and shell', 'Whole body', 2.25, 4.5,
     6.75, 'Plastics', None, 'E', 'T1 slides 26, 44'),
    ('Unitree G1', 'Lower-leg links', 1, 'Frame and shell', 'Legs', 0.3, 0.6, 1, 'Steel', None, 'E', 'T1 slide 45'),
    ('Unitree G1', 'Frame', 1, 'Frame and shell', 'Whole body', None, None, None, 'Aluminium',
     'the robot (Constants), less every other part', 'E',
     'T1 slides 18, 44, 45; Matthias, 2026-10-27, step 1: "Accept all" (EVIDENCE.md E2.8)'),
    ('AgiBot X1', 'Joint module, small', 14, 'Ankles and arms', 'Legs 4, Arms 10', None, None, None, None,
     "the Joints' module masses; inside as JointParts' joint of its size, scaled to its mass", 'S', 'X1b'),
    ('AgiBot X1', 'Joint module, large', 15, 'Hips, knees, waist and shoulders', 'Legs 8, Torso 3, Arms 4', None,
     None, None, None, "the Joints' module masses; inside as JointParts' joint of its size, scaled to its mass", 'S',
     'X1b'),
    ('AgiBot X1', 'Encoders (two per joint)', 58, 'In the joints', 'as their joints', None, None, None, None,
     'Sensors and SensorElements (Encoder)', 'E',
     'two per joint, as the G1 (U1, U2) and the N1 (N1a); X1a lists the actuators as bought-in units and names no '
     'encoders (E2.8e)'),
    ('AgiBot X1', 'Main board fan', 1, 'Torso boards', 'Torso', 0.005, 0.01, 0.02, None, None, 'E',
     "the mini PC's fan, as the G1's main board fan (E2.8e)"),
    ('AgiBot X1', 'Main board heat sink: heat pipes and fins', 1, 'Torso boards', 'Torso', 0.055, 0.12, 0.19,
     'Copper', None, 'E',
     "the mini PC's cooler; no source of a mini PC's cooler; context only: FW1 67.5 g, DY1 199 g, each with its fan "
     '(E2.8e)'),
    ('AgiBot X1', 'OmniPicker grippers', 2, 'Arms', 'Arms', 0.41, 0.43, 0.45, 'Mixed', None, 'S',
     'X1d "Weight 0.43kg"'),
    ('AgiBot X1', 'Battery pack', 1, 'Battery pack', 'Torso', 1.75, 2.2, 3.3, None,
     'its cells, its management board (Boards) and its housing (the rows below)', 'S, E',
     'X1a "48V8AH三元电池", stainless-steel case; mass: the G1\'s 168 Wh/kg; the lower cut where the pack holds '
     'its heaviest cells (232.5 Wh/kg) and management board in the lightest robot (E2.8e, 2026-10-28)'),
    ('AgiBot X1', 'Battery cells', 1, 'Battery pack', 'Torso', None, None, None, 'Battery materials',
     "from the energy: Constants voltage × capacity over the NMC cell's Wh/kg", 'S',
     'X1a "12S"; element_recipes.xlsx NMC cylindrical'),
    ('AgiBot X1', 'Battery housing, busbars and wires', 1, 'Battery pack', 'Torso', None, None, None, 'Mixed',
     'the battery pack, less its cells and its management board', 'E', 'X1a (stainless-steel case); as the G1'),
    ('AgiBot X1', 'Cable conductors and insulation', 1, 'Cables', 'Whole body', None, None, None, None,
     'from Constants: length, cross-sections, insulation', 'S', 'X1a: the lengths listed (11.0 m)'),
    ('AgiBot X1', 'XT30 (2+2) connectors (two per joint)', 58, 'Cables', 'Whole body', 0.0015, 0.003, 0.0045, None,
     None, 'S, E',
     "X1a: 58 cable plugs (19 cables with two, 12 with one, 6 terminating resistors, 2 to the L28); mass as the "
     "G1's (E)"),
    ('AgiBot X1', 'Titanium (TC4) links: waist (2), ankles (4)', 1, 'Frame and shell', 'Legs, Torso', 0.2, 0.4, 0.6,
     'Titanium', None, 'E', 'X1a "钛合金TC4"; masses not given'),
    ('AgiBot X1', 'Stainless 17-4PH shafts and crosses; steel pins (about 115)', 1, 'Frame and shell', 'Whole body',
     0.1, 0.3, 0.5, 'Steel', None, 'E', 'X1a "0Cr17Ni4Cu4Nb", "40Cr"'),
    ('AgiBot X1', 'Screws (about 980)', 1, 'Frame and shell', 'Whole body', 0.3, 0.6, 0.9, 'Steel', None, 'E',
     'X1a (M2 to M5)'),
    ('AgiBot X1', 'Bearings outside the actuators', 1, 'Frame and shell', 'Whole body', 0.4, 0.8, 1.2, 'Steel', None,
     'E', 'X1a: crossed roller × 10, four-point × 9, ball × 20, rod ends × 8, spherical × 12'),
    ('AgiBot X1', 'Shell: 3D-printed resin or ABS', 1, 'Frame and shell', 'Whole body', 1.5, 3, 4.5, 'Plastics', None,
     'E', 'X1a: "3D打印树脂" in the BOM list, "ABS" in the overall BOM'),
    ('AgiBot X1', 'Rubber feet and handle', 1, 'Frame and shell', 'Whole body', 0.1, 0.2, 0.3, 'Plastics', None, 'E',
     'X1a "橡胶"'),
    ('AgiBot X1', 'Frame', 1, 'Frame and shell', 'Whole body', None, None, None, 'Aluminium',
     'the robot (Constants), less every other part', 'E', 'X1a: 6061-T6 and 7075-T6 machined parts'),
    ('Fourier N1', 'Joint module, small', 12, 'Ankles and arms', 'Legs 4, Arms 8', None, None, None, None,
     "the Joints' module masses; inside as JointParts' joint of its size, scaled to its mass", 'E',
     "N1a; the joint-mass fit on AgiBot's actuators, ± 50 % (E2.8e)"),
    ('Fourier N1', 'Joint module, large', 11, 'Hips, knees, waist and shoulders', 'Legs 8, Torso 1, Arms 2', None,
     None, None, None, "the Joints' module masses; inside as JointParts' joint of its size, scaled to its mass", 'E',
     "N1a; the joint-mass fit on AgiBot's actuators, ± 50 % (E2.8e)"),
    ('Fourier N1', 'Encoders (two per joint)', 46, 'In the joints', 'as their joints', None, None, None, None,
     'Sensors and SensorElements (Encoder)', 'S', 'N1a "双编码器 16bit/14bit"; elements: SensorElements'),
    ('Fourier N1', 'Main board fan', 1, 'Torso boards', 'Torso', 0.005, 0.01, 0.02, None, None, 'E',
     "the computer's fan, as the G1's main board fan (E2.8e)"),
    ('Fourier N1', 'Main board heat sink: heat pipes and fins', 1, 'Torso boards', 'Torso', 0.055, 0.12, 0.19,
     'Copper', None, 'E',
     "the computer's cooler; no source of a mini PC's cooler; context only: FW1 67.5 g, DY1 199 g, each with its "
     'fan (E2.8e)'),
    ('Fourier N1', 'End pieces of the arms', 2, 'Arms', 'Arms', 0.05, 0.1, 0.15, 'Plastics', None, 'S, E',
     'N1b 0.099 kg each'),
    ('Fourier N1', 'Battery pack', 1, 'Battery pack', 'Torso', 2.26, 2.9, 3.2, None,
     'its cells, its management board (Boards) and its housing (the rows below)', 'S, E',
     'N1a "≤3.2kg" (the upper cut); the lower cut where the pack holds its heaviest cells (232.5 Wh/kg) and '
     'management board in the lightest robot (E2.8e, 2026-10-28)'),
    ('Fourier N1', 'Battery cells', 1, 'Battery pack', 'Torso', None, None, None, 'Battery materials',
     "from the energy: Constants voltage × capacity over the NMC cell's Wh/kg", 'S',
     'N1a "475WH", "39.6V"; NMC (E2.8e); element_recipes.xlsx NMC cylindrical'),
    ('Fourier N1', 'Battery housing, busbars and wires', 1, 'Battery pack', 'Torso', None, None, None, 'Mixed',
     'the battery pack, less its cells and its management board', 'E', 'as the G1'),
    ('Fourier N1', 'Cable conductors and insulation', 1, 'Cables', 'Whole body', None, None, None, None,
     'from Constants: length, cross-sections, insulation', 'E', 'E2.8e'),
    ('Fourier N1', 'XT30 (2+2) connectors (two per joint)', 46, 'Cables', 'Whole body', 0.0015, 0.003, 0.0045,
     None, None, 'E', "two per joint and their mass, as the G1's (T3k); N1a names no connector (E2.8e)"),
    ('Fourier N1', 'Screws', 1, 'Frame and shell', 'Whole body', 0.2, 0.5, 1, 'Steel', None, 'E',
     'as the G1 (E2.8e)'),
    ('Fourier N1', 'Shell (engineering plastics)', 1, 'Frame and shell', 'Whole body', 2.25, 4.5, 6.75, 'Plastics',
     None, 'E', 'N1a "工程塑料"; as the G1 (E2.8e)'),
    ('Fourier N1', 'Frame', 1, 'Frame and shell', 'Whole body', None, None, None, 'Aluminium',
     'the robot (Constants), less every other part', 'E', 'N1a "铝合金"'),
]
PARTS_WIDTHS = [12, 44, 10, 20, 16, 11, 9, 9, 18, 52, 7, 56]

# --- Shares ---------------------------------------------------------------------------------------------------------
# The materials of the parts and components that hold more than one; each group has one named remainder and
# nothing is rescaled (no normalisation). EVIDENCE.md E2.8, E2.10.
SHARES_HEADINGS = ['Part or component', 'Material', 'Grade', 'Share min', 'Share mode', 'Share max', 'Remainder',
                   'Label', 'Basis']
SHARES_ROWS = [
    ('Motor stator', 'Copper', 'winding', 0.23, 0.36, 0.45, None, 'S',
     'measured car traction motors 23-29 % (Drexler et al. 2025), car auxiliary motors 27 / '
     '36 / 45 %; E2.10; Matthias: "Yes use this numberrs"'),
    ('Motor stator', 'Plastics', 'winding coating', 0.02, 0.05, 0.1, None, 'E', 'E2.8'),
    ('Motor stator', 'Steel', 'electrical steel', None, None, None, 'Yes', 'E',
     'Matthias, 2026-10-27, step 1: "Accept all" (EVIDENCE.md E2.8)'),
    ('Motor rotor', 'Magnets (NdFeB)', None, 0.45, 0.9, 1, None, 'E',
     'T1 calls it "磁钢"; Matthias, 2026-10-27, step 1: "Accept all" (EVIDENCE.md E2.8)'),
    ('Motor rotor', 'Steel', None, None, None, None, 'Yes', 'E',
     'Matthias, 2026-10-27, step 1: "Accept all" (EVIDENCE.md E2.8)'),
    ('Magnet carrier', 'Plastics', 'plastic bearing', 0.05, 0.15, 0.3, None, 'E', 'T1 "铝+塑料轴承"'),
    ('Magnet carrier', 'Aluminium', None, None, None, None, 'Yes', 'E',
     'Matthias, 2026-10-27, step 1: "Accept all" (EVIDENCE.md E2.8)'),
    ('Gear stage 2, planets, carrier and crossed roller bearing', 'Aluminium', 'carrier', 0.125, 0.25, 0.4, None, 'E',
     'T1 "保持架为铝，其余为钢"'),
    ('Gear stage 2, planets, carrier and crossed roller bearing', 'Steel', None, None, None, None, 'Yes', 'E',
     'Matthias, 2026-10-27, step 1: "Accept all" (EVIDENCE.md E2.8)'),
    ('Other', 'Copper', 'wires', 0.1, 0.25, 0.4, None, 'E', 'no basis'),
    ('Other', 'Steel', 'screws, encoder parts', 0.2, 0.4, 0.6, None, 'E', 'no basis'),
    ('Other', 'Plastics', None, None, None, None, 'Yes', 'E',
     'Matthias, 2026-10-27, step 1: "Accept all" (EVIDENCE.md E2.8)'),
    ('Hip fan', 'Copper', 'motor winding', 0.05, 0.1, 0.2, None, 'E', 'E2.8'),
    ('Hip fan', 'Plastics', None, None, None, None, 'Yes', 'E', 'E2.8'),
    ('Waist fan', 'Copper', 'motor winding', 0.05, 0.1, 0.2, None, 'E', 'E2.8'),
    ('Waist fan', 'Plastics', None, None, None, None, 'Yes', 'E', 'E2.8'),
    ('Main board fan', 'Copper', 'motor winding', 0.05, 0.1, 0.2, None, 'E', 'E2.8'),
    ('Main board fan', 'Plastics', None, None, None, None, 'Yes', 'E', 'E2.8'),
    ('XT30 (2+2) connectors (two per joint)', 'Copper', 'contacts', 0.175, 0.35, 0.525, None, 'E', 'E2.8'),
    ('XT30 (2+2) connectors (two per joint)', 'Plastics', 'housing', None, None, None, 'Yes', 'E', 'E2.8'),
]
SHARES_WIDTHS = [52, 18, 22, 10, 10, 10, 10, 7, 90]

# --- Boards ---------------------------------------------------------------------------------------------------------
# Every circuit board of each robot: its area and the car board category whose gold, silver, palladium, tin
# and nickel per cm2 it takes (RAWCLICVehicleElectronics, read where it lies). EVIDENCE.md E2.8b, E2.8e.
BOARDS_HEADINGS = ['Robot', 'Board', 'Number in the robot', "Kind (the figure's row)", 'Body region',
                   'Area of one, min (cm2)', 'mode (cm2)', 'max (cm2)', 'Mass from',
                   'Car board category (RAWCLICVehicleElectronics 04_)', 'Label', 'Sources']
BOARDS_ROWS = [
    ('Unitree G1', 'Driver board, small joint', 14, 'Ankles and arms', 'Legs 4, Arms 10', 11.5, 22.9, 28.3,
     'JointParts, driver board (weighed 12.8 g)', 'PE_HVS', 'W, E', 'T1 slides 24, 43; area at most the 60 mm joint'),
    ('Unitree G1', 'Driver board, large joint', 9, 'Hips, knees and waist', 'Legs 8, Torso 1', None, None, None,
     "JointParts, driver board times its factor; area: the small one's times the same factor", 'PE_HVS', 'E',
     'T1 slide 24; T3k'),
    ('Unitree G1', 'Main control board (RK3588S, core board on base board)', 1, 'Torso boards', 'Torso', 50, 100, 150,
     'area times Constants board mass per cm2', 'ITC', 'E', 'T1 slides 26, 27; C1; RK3588S whole boards 48-54 cm2'),
    ('Unitree G1', 'Power distribution unit and DC-DC converter', 1, 'Torso boards', 'Torso', 30, 60, 100,
     'area times Constants board mass per cm2', 'PE_HVS', 'E', 'T1 slide 12'),
    ('Unitree G1', 'Battery management board', 1, 'Battery pack', 'Torso', 30, 60, 96,
     'area times Constants board mass per cm2', 'BMS', 'E', 'T1 slide 42; B1 (pack 120 x 80 mm)'),
    ('Unitree G1', 'Head control board', 1, 'Head', 'Head', 5, 15, 30, 'area times Constants board mass per cm2',
     'VCC', 'E', 'T1 slide 37'),
    ('Unitree G1', 'Capacitor buffer board', 4, 'Cables', 'Legs 2, Arms 2', 2, 5, 10,
     'area times Constants board mass per cm2', 'PE_HVS', 'E', 'T1 slide 38; T3'),
    ('AgiBot X1', 'Driver board, small joint', 14, 'Ankles and arms', 'Legs 4, Arms 10', None, None, None,
     "JointParts' driver board of its size, scaled to its joint's module mass; area likewise", 'PE_HVS', 'E',
     'as the G1 (E2.8e)'),
    ('AgiBot X1', 'Driver board, large joint', 15, 'Hips, knees, waist and shoulders', 'Legs 8, Torso 3, Arms 4',
     None, None, None, "JointParts' driver board of its size, scaled to its joint's module mass; area likewise",
     'PE_HVS', 'E', 'as the G1 (E2.8e)'),
    ('AgiBot X1', 'Mini PC board, Intel i7-13620H', 1, 'Torso boards', 'Torso', 60, 120, 180,
     'area times Constants board mass per cm2', 'ITC', 'E', 'X1a; a 4 × 4 inch board is 104 cm2'),
    ('AgiBot X1', 'Xyber-DCU control board', 2, 'Torso boards', 'Torso', 30, 60, 90,
     'area times Constants board mass per cm2', 'ITC', 'E', 'X1a'),
    ('AgiBot X1', 'Router board, GL.iNet MT2500A', 1, 'Torso boards', 'Torso', 30, 60, 90,
     'area times Constants board mass per cm2', 'ITC', 'E', 'X1a'),
    ('AgiBot X1', 'Power boards: 48-to-24 V (2), 5 V module, 95 W supply, soft start (2)', 6, 'Torso boards', 'Torso',
     10, 20, 30, 'area times Constants board mass per cm2', 'PE_HVS', 'E', 'X1a'),
    ('AgiBot X1', 'Battery management board', 1, 'Battery pack', 'Torso', 30, 60, 96,
     'area times Constants board mass per cm2', 'BMS', 'E', 'as the G1 (E2.8e)'),
    ('AgiBot X1', 'Phone board (the phone in the head)', 1, 'Head', 'Head', 20, 50, 100,
     'area times Constants board mass per cm2', 'ITC', 'E',
     'X1a overall BOM "手机"; no measured area of a phone\'s main board found (E2.8e)'),
    ('Fourier N1', 'Driver board, small joint', 12, 'Ankles and arms', 'Legs 4, Arms 8', None, None, None,
     "JointParts' driver board of its size, scaled to its joint's module mass; area likewise", 'PE_HVS', 'E',
     'as the G1 (E2.8e)'),
    ('Fourier N1', 'Driver board, large joint', 11, 'Hips, knees, waist and shoulders', 'Legs 8, Torso 1, Arms 2',
     None, None, None, "JointParts' driver board of its size, scaled to its joint's module mass; area likewise",
     'PE_HVS', 'E', 'as the G1 (E2.8e)'),
    ('Fourier N1', 'Computer board, Intel Core i7-13700H', 1, 'Torso boards', 'Torso', 60, 120, 180,
     'area times Constants board mass per cm2', 'ITC', 'E', 'N1a'),
    ('Fourier N1', 'Power distribution unit and DC-DC converter', 1, 'Torso boards', 'Torso', 30, 60, 100,
     'area times Constants board mass per cm2', 'PE_HVS', 'E', 'as the G1 (E2.8e)'),
    ('Fourier N1', 'Battery management board', 1, 'Battery pack', 'Torso', 30, 60, 96,
     'area times Constants board mass per cm2', 'BMS', 'E', 'as the G1 (E2.8e)'),
]
BOARDS_WIDTHS = [12, 50, 10, 20, 16, 11, 9, 9, 52, 18, 7, 46]

# --- Sensors --------------------------------------------------------------------------------------------------------
# Every sensor of each robot and the mass of one (EVIDENCE.md E2.8b, E2.8e).
SENSORS_HEADINGS = ['Robot', 'Sensor', 'Number in the robot', "Kind (the figure's row)", 'Body region',
                    'Mass of one, min (g)', 'mode (g)', 'max (g)', 'Label', 'Sources']
SENSORS_ROWS = [
    ('Unitree G1', 'LiDAR, Livox Mid-360', 1, 'Head', 'Head', 265, 265, 265, 'S', 'L1 (265 g); U2'),
    ('Unitree G1', 'Depth camera, Intel RealSense D435i', 1, 'Head', 'Head', 72, 75, 80, 'S',
     'Intel D400 datasheet, D435 75 g (second-hand); U2; T1'),
    ('Unitree G1', 'Microphone array (4 microphones)', 1, 'Head', 'Head', 5, 10, 20, 'E', 'T1 slide 33'),
    ('Unitree G1', 'Speaker, 5 W', 1, 'Head', 'Head', 17.5, 35, 60, 'E', 'T1 slide 33; U1'),
    ('Unitree G1', 'Motion sensor (IMU), torso and pelvis', 2, 'Torso boards', 'Torso', 1, 2, 5, 'E',
     'U3 (imu_in_torso, imu_in_pelvis)'),
    ('Unitree G1', 'Encoder', 46, 'In the joints', 'as their joints', None, None, None, 'S', 'U1, U2; elements only'),
    ('AgiBot X1', 'Depth camera, Intel RealSense D435', 1, 'Head', 'Head', 72, 75, 80, 'S',
     'X1a; Intel D400 datasheet, D435 75 g (second-hand), as the G1'),
    ('AgiBot X1', 'Motion sensor, YIS320', 2, 'Torso boards', 'Torso', 1, 2, 5, 'E', "X1a; as the G1's IMU"),
    ('AgiBot X1', 'Encoder', 58, 'In the joints', 'as their joints', None, None, None, 'E',
     'two per joint (E2.8e); elements only'),
    ('Fourier N1', 'Motion sensor (IMU), 6-axis', 1, 'Torso boards', 'Torso', 1, 2, 5, 'E', 'N1a "6轴"; N1b imu_link'),
    ('Fourier N1', 'Encoder', 46, 'In the joints', 'as their joints', None, None, None, 'S',
     'N1a "双编码器"; elements only'),
]
SENSORS_WIDTHS = [12, 40, 10, 20, 16, 11, 9, 9, 7, 52]

# --- SensorElements -------------------------------------------------------------------------------------------------
# The car sensor elements each sensor is made of (RAWCLICVehicleElectronics 07_, read where it lies);
# one set for all robots, by the sensor's name.
SENSORELEMENTS_HEADINGS = ['Sensor', 'Car sensor type (RAWCLICVehicleElectronics 07_, sheet Sensor Details)',
                           'Units in one sensor']
SENSORELEMENTS_ROWS = [
    ('LiDAR, Livox Mid-360', 'laser diode array', 1),
    ('LiDAR, Livox Mid-360', 'photodetector array', 1),
    ('LiDAR, Livox Mid-360', 'IMU', 1),
    ('Depth camera, Intel RealSense D435i', 'laser diode array', 1),
    ('Depth camera, Intel RealSense D435i', 'IR camera sensor', 2),
    ('Depth camera, Intel RealSense D435i', 'CMOS image sensor', 1),
    ('Depth camera, Intel RealSense D435i', 'IMU', 1),
    ('Microphone array (4 microphones)', 'MEMS microphone array', 4),
    ('Motion sensor (IMU), torso and pelvis', 'IMU', 1),
    ('Encoder', 'angle sensor', 1),
    ('Depth camera, Intel RealSense D435', 'laser diode array', 1),
    ('Depth camera, Intel RealSense D435', 'IR camera sensor', 2),
    ('Depth camera, Intel RealSense D435', 'CMOS image sensor', 1),
    ('Motion sensor, YIS320', 'IMU', 1),
    ('Motion sensor (IMU), 6-axis', 'IMU', 1),
]
SENSORELEMENTS_WIDTHS = [40, 50, 12]

# --- Constants ------------------------------------------------------------------------------------------------------
# Each robot's own numbers (mass, battery, cable length) and the shared ones once, under the robot "all"
# (EVIDENCE.md E2.8, E2.8b, E2.8e).
CONSTANTS_HEADINGS = ['Robot', 'Quantity', 'Min', 'Mode', 'Max', 'Unit', 'Label', 'Source']
CONSTANTS_ROWS = [
    ('all', 'Board mass per cm2 (boards not weighed)', 0.28, 0.56, 0.84, 'g/cm2', 'E',
     'the weighed small driver board, 12.8 g on 22.9 cm2, ± 50 %; E2.8'),
    ('all', "Copper share of a board's mass", 0.125, 0.2, 0.287, 'share', 'S',
     'Bizzo et al. 2014, Table 3: 14 analyses combined (min / mean / max); E2.8b'),
    ('all', 'Power conductor cross-section (2 conductors)', 0.52, 0.82, 1.31, 'mm2', 'S',
     "20 / 18 / 16 AWG, the XT30's wire range (TME, second-hand)"),
    ('all', 'Signal conductor cross-section (2 conductors)', 0.065, 0.13, 0.2, 'mm2', 'E', 'E2.8'),
    ('all', 'Copper density', 8.96, 8.96, 8.96, 'g/cm3', 'S', 'copper'),
    ('all', 'Insulation and jackets, per mass of copper', 0.5, 1, 1.5, 'times', 'E', 'E2.8'),
    ('Unitree G1', 'Robot mass, with battery', 34, 35, 36, 'kg', 'S', 'U1 "About 35kg"; U3 adds up to 35.115 kg'),
    ('Unitree G1', 'Battery voltage', 46.8, 46.8, 46.8, 'V', 'S', 'T1 slide 25 (13 cells in series)'),
    ('Unitree G1', 'Battery capacity', 8.55, 9, 9.45, 'Ah', 'S',
     'T1 slide 25; U1; ± 5 % production tolerance (E2.8e, accepted)'),
    ('Unitree G1', 'Cable length (four conductors)', 3, 6, 10, 'm', 'E',
     'T1 slide 3: "not over 10 m"; the body\'s routes'),
    ('AgiBot X1', 'Robot mass, with battery', 32, 33, 35.3, 'kg', 'S, E',
     'X1e "33kg"; the max from X1c, whose links add up to 35.32 kg; the min 1 kg below, as the G1\'s (E)'),
    ('AgiBot X1', 'Battery voltage', 43.2, 44.4, 48, 'V', 'S',
     'X1a "48V", "12S": 12 × 3.6 V, 12 × 3.7 V, the label\'s 48 V'),
    ('AgiBot X1', 'Battery capacity', 8, 8, 8, 'Ah', 'S', 'X1a "8AH"'),
    ('AgiBot X1', 'Cable length (four conductors)', 10, 11, 12, 'm', 'S', 'X1a: the lengths listed add up to 11.0 m'),
    ('Fourier N1', 'Robot mass, with battery', 38, 39, 40, 'kg', 'S',
     'N1a "≈39 kg" (38 kg in its text, 39.7 kg in N1b)'),
    ('Fourier N1', 'Battery voltage', 39.6, 39.6, 39.6, 'V', 'S', 'N1a "39.6V" (11 cells)'),
    ('Fourier N1', 'Battery capacity', 11.39, 11.99, 12.6, 'Ah', 'S',
     'N1a "475WH" at 39.6 V; 451 / 475 / 499 Wh, ± 5 % production tolerance (E2.8e, accepted)'),
    ('Fourier N1', 'Cable length (four conductors)', 5, 10, 15, 'm', 'E',
     "between the G1's 6 m and the X1's 11 m, wider (E2.8e)"),
]
CONSTANTS_WIDTHS = [12, 48, 9, 9, 9, 8, 7, 70]

# --- Sources --------------------------------------------------------------------------------------------------------
# Every source code used in this file, with its link and what it is (EVIDENCE.md E2.1, E2.8e).
SOURCES_HEADINGS = ['Code', 'Source', 'Link', 'What it is']
SOURCES_ROWS = [
    ('U1', 'Unitree, G1 product page', 'https://www.unitree.com/g1/', "Manufacturer's specification"),
    ('U2', 'Unitree, G1 developer documentation, About G1',
     'https://support.unitree.com/home/en/G1_developer/about_G1', "Manufacturer's documentation"),
    ('U3', 'Unitree, g1_29dof.urdf (torque limits, link masses)',
     'https://raw.githubusercontent.com/unitreerobotics/unitree_ros/master/robots/g1_description/g1_29dof.urdf',
     "Manufacturer's model file"),
    ('L1', 'Livox, Mid-360 specifications', 'https://www.livoxtech.com/mid-360/specs', "Manufacturer's datasheet"),
    ('T1',
     'China Post Securities (Su, Sheng, Yang), Unitree G1 Humanoid Robot Teardown Report, '
     '2026-03-30', 'https://pdf.dfcfw.com/pdf/H3_AP202603311820899944_1.pdf',
     "A securities firm's own teardown, parts weighed"),
    ('T3', 'Munro & Associates, Munro Live, Unitree G1 teardown, 2026, through Humanoid.guide',
     'https://humanoid.guide/unitree-g1-teardown-reveals-actuator-and-cooling-tradeoffs/', 'Second-hand'),
    ('T3k', "Munro's knee-actuator report (Grant), through SMZDM", 'https://post.smzdm.com/p/awwo7o5g/',
     'Second-hand'),
    ('C1', "Lenz's law, G1 main control teardown", 'https://jishuzhan.net/article/1981300479431868417',
     'A private teardown'),
    ('B1', 'Maverick Drone, G1 battery', 'https://www.maverickdrone.com/collections/all/products/g1-battery',
     "Dealer's page"),
    ('Bizzo 2014', 'Bizzo, Figueiredo, de Andrade, Materials 7 (2014) 4555-4566',
     'https://pmc.ncbi.nlm.nih.gov/articles/PMC5455934/', 'University analyses, 14 combined'),
    ('Drexler 2025', 'Drexler, Kampker, Born et al., Elektrotech. Inftech. 142 (2025) 312-345',
     'doi:10.1007/s00502-025-01331-3', 'Measured traction motors, through RAWCLICVehicleTractionMotor'),
    ('X1a', 'AgiBot, X1 BOM list (智元灵犀X1_BOM清单_20241024.xlsx) and overall BOM (智元灵犀X1总BOM.xlsx)',
     'https://github.com/AGIBOTTech/AGIBOT_x1_hardware', "Manufacturer's design lists; quantities and materials"),
    ('X1b', 'AgiBot, X1 product page (actuator masses and peak torques)', 'https://agibot.com/products/X1',
     "Manufacturer's specification"),
    ('X1c', 'AgiBot, x1.urdf (legs only: joints, limits)',
     'https://github.com/AgibotTech/agibot_x1_train/blob/main/resources/robots/x1/urdf/x1.urdf',
     "Manufacturer's model file"),
    ('X1d', 'AgiBot, OmniPicker product manual',
     'https://cdn.robotshop.com/media/A/Agb/RB-Agb-14/pdf/omnigripper-manual.pdf', "Manufacturer's manual"),
    ('X1e', 'AgiBot, 灵犀X1 product page (Chinese)', 'http://www.agibot.com.cn/products/X1',
     "Manufacturer's specification"),
    ('N1a', 'Fourier, About Fourier N1 (specification table)',
     'https://support-old.fftai.com/docs/GR-X-Humanoid-Robot/Fouriern1/N1_Introduction/',
     "Manufacturer's documentation"),
    ('N1b', 'Fourier, FOURIERN1.urdf (joints, limits, link masses)', 'https://github.com/FFTAI/fourier_lab',
     "Manufacturer's model file"),
    ('N1c', 'A teardown article on Zhihu (actuators FSA80-29E, FSA60-43E, FSA45-30E)',
     'https://zhuanlan.zhihu.com/p/1899242762072749284', 'Second-hand, through a search summary (login)'),
    ('FW1', 'Framework, Laptop 13 Heatsink and Fan Kit ("Weight: 67.5g"; 28 W continuous, 60 W turbo)',
     'https://frame.work/products/heatsink-and-fan-kit',
     "Manufacturer's specification; a laptop's cooler, not a mini PC's: context only"),
    ('DY1', 'Dynatron, I2 CPU cooler ("199g ±5g", "Copper 1100 Skiving Fins"; Intel socket PGA988, 1U)',
     'https://www.dynatron.co/product-page/i2',
     "Manufacturer's specification; a server cooler for mobile Intel processors, not a mini PC's: context only"),
]
SOURCES_WIDTHS = [12, 70, 90, 50]

# Every sheet after About, in the order of the file: its name, first row, rows and column widths.
SHEETS = [
    ('Robots', ROBOTS_HEADINGS, ROBOTS_ROWS, ROBOTS_WIDTHS),
    ('Joints', JOINTS_HEADINGS, JOINTS_ROWS, JOINTS_WIDTHS),
    ('JointParts', JOINTPARTS_HEADINGS, JOINTPARTS_ROWS, JOINTPARTS_WIDTHS),
    ('Parts', PARTS_HEADINGS, PARTS_ROWS, PARTS_WIDTHS),
    ('Shares', SHARES_HEADINGS, SHARES_ROWS, SHARES_WIDTHS),
    ('Boards', BOARDS_HEADINGS, BOARDS_ROWS, BOARDS_WIDTHS),
    ('Sensors', SENSORS_HEADINGS, SENSORS_ROWS, SENSORS_WIDTHS),
    ('SensorElements', SENSORELEMENTS_HEADINGS, SENSORELEMENTS_ROWS, SENSORELEMENTS_WIDTHS),
    ('Constants', CONSTANTS_HEADINGS, CONSTANTS_ROWS, CONSTANTS_WIDTHS),
    ('Sources', SOURCES_HEADINGS, SOURCES_ROWS, SOURCES_WIDTHS),
]


def output_path() -> str:
    """Where the file goes: 00's setting `data.parts_taken_apart`, as an absolute path."""
    return absolute(Params().data.parts_taken_apart)


def write_sheet(book: openpyxl.Workbook, name: str, headings: list, rows: list, widths: list) -> None:
    """One sheet: its first row in bold on grey, then its rows, its column widths, the first row kept in view."""
    sheet = book.create_sheet(name)
    sheet.append(headings)
    for cell in sheet[1]:
        cell.font = Font(bold=True)
        cell.fill = HEADING_FILL
        cell.alignment = Alignment(wrap_text=True, vertical='top')
    for row in rows:
        sheet.append(list(row))
    for i, width in enumerate(widths):
        sheet.column_dimensions[get_column_letter(i + 1)].width = width
    sheet.freeze_panes = 'A2'


def build(path: str) -> None:
    """Write the whole file to `path`: the About sheet first, then every sheet of SHEETS in its order."""
    book = openpyxl.Workbook()
    about = book.active
    about.title = 'About'
    for row, line in enumerate(ABOUT, start=1):
        if line is not None:
            about.cell(row=row, column=1, value=line)
    about['A1'].font = Font(bold=True)
    about.column_dimensions['A'].width = ABOUT_WIDTH
    for name, headings, rows, widths in SHEETS:
        write_sheet(book, name, headings, rows, widths)
    book.save(path)


def main() -> None:
    """Pressing Run: write the file where 00 says, and say where."""
    path = output_path()
    build(path)
    print(f'Written: {path}')


if __name__ == '__main__':
    main()
