"""
Builder of data/researched/parts_taken_apart.xlsx: the robots of type 1, part by part.

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

Matthias, 2026-10-27: "Yes, put the builder in tools/make_parts_taken_apart.py as proposed, with its test and
documents"; 2026-10-28: "Yes, rewrite" (the first builder, in Claude's scratch folder, was lost with it).

WHAT IT DOES
------------
It writes the data file of the robots of type 1, each part by part, with the materials, boards and sensors of each,
so that the model can show where in a robot its critical materials sit (Matthias, 2026-10-27: "the slipt into parts is
just to get a deeper look into the robot, so that there is information on where the interesting materials are and the
recycling can be optimized"). First the Unitree G1, the AgiBot X1 and the Fourier N1, taken apart first (agreed on
2026-10-27, documentation/claude/EVIDENCE.md E2.8 to E2.8e); then every other robot of the register's sheet Type 1, one
block each (Matthias, 2026-10-29: "Yes, build it", the entry of type 1's research: E5.1 to E5.19, each agreed that
day), 32 robots in all, the Booster K1 in its two versions. Each row of the file names its own sources.

WHAT IT READS AND WRITES
------------------------
It reads nothing but 00's settings (src/params_schema.py, for where the file goes). It writes one file, the path of
`data.parts_taken_apart` (data/researched/parts_taken_apart.xlsx, git-ignored), and replaces the file there. The
values are held here: a change to them is made in this file, not in the .xlsx, where it would be lost at the next run.

WHERE IT SITS
-------------
It is not a stage of the model: it writes one of the model's inputs, not a result, so it stands in tools/ and has no
number. 01_schemas.py reads and checks the file (METHODOLOGY.md checks 18 and 19); 02_composition.py draws robot type 1
from it, each robot from its own rows. Press Run: no arguments. Importing this file writes nothing;
tests/test_make_parts_taken_apart.py checks that what it writes passes 01's checks and equals the file on disk.
"""
import math
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
    'Robot type 1 part by part: its 31 robots of the register (the Booster K1 in two versions), for where their '
    'critical materials sit',
    None,
    'The Unitree G1, the AgiBot X1 and the Fourier N1 agreed by Matthias on 2026-10-27 (documentation/claude/'
    'EVIDENCE.md E2.8 to E2.8e); every other robot of type 1 agreed on 2026-10-29 (E5.1 to E5.19: the actuators E5.12, '
    'the rest E5.14, batches 2 to 4 E5.17, the steels E5.18, the battery\'s rest E5.19), "Yes, build it". Written by '
    'Claude.',
    "Sheet Robots: each robot, its maker, its type, the maker's height and stated mass. Every sheet with a column "
    "Robot holds each robot's own rows; JointParts, Shares and SensorElements are one set for all (the G1's joint "
    'insides, scaled to each joint\'s module mass: "We can assume, they are similar within given ranges").',
    "Labels: W weighed (China Post Securities' teardown, T1); S from a source (named in Sources); E an estimate, with "
    'at least half to 1.5 times its mode ("Estimates should be larger than known numbers").',
    'Every range is min / mode / max. A remainder takes what the other shares or parts leave; nothing is rescaled.',
    None,
    "Sheet Joints: the joint kinds of each robot, where they sit, torque, module mass; for a robot whose sources give "
    "no joint torques, each joint group's share of its joint modules, a share of its mass (E5.17 point 1).",
    "Sheet MagnetGrades: each heat group a distribution over the magnets' grade classes (H, SH, UH, EH), drawn; "
    'estimates on the order of heat (EVIDENCE.md E2.11).',
    'Sheet JointParts: the joint module part by part: the small joint as weighed (T1, slide 43), the 13 not weighed at '
    '0.5 / 1 / 1.5 times; the large joint as the small one times a factor from size and torque; the steel grades.',
    'Sheet Parts: every other part, with its count, kind, body region, mass of one, material and grade.',
    'Sheet Shares: the materials of the parts and components that hold more than one; the remainder is named; the '
    'grade of each steel.',
    "Sheet Boards: each circuit board, its area and the car board category whose gold, silver, palladium, tin and "
    'nickel per cm2 it takes (read where they lie).',
    'Sheets Sensors and SensorElements: each sensor, and the car sensor elements it is made of (read where they lie).',
    'Sheet Constants: each robot\'s own numbers, and the shared ones once (robot "all").',
    'Sheet Sources: every source code used here, as in EVIDENCE.md E2.1 and E5.',
    None,
    'Read where they lie, not copied: RAWCLICVehicleElectronics Data/04_VehiclePCBComposition.xlsx (board metals per '
    'cm2 by category) and Data/07_VehicleSensorComposition.xlsx (sensor elements); RAWCLICDataCenters '
    'data/researched/04_DataCenterElementComposition.xlsx, sheet BoardsAndComponents (tantalum per kg of board); '
    'RAWCLICVehicleTractionMotor data/raw/10_MaterialElementDefinitions.xlsx, sheets PermanentMagnetNdFeB (NdFeB grade '
    "classes), ElectricalSteel (M19, M27) and CastFeSteel (Type 304); this project's element_recipes.xlsx (the cells, "
    'the other grades).',
]


# --- Robots ---------------------------------------------------------------------------------------------------------
# The three robots of type 1 taken apart first: each with its maker, its type, the maker's height and stated mass
# (EVIDENCE.md E2.8e; Matthias, 2026-10-27: "Type 1 is informed by the G1, X1 and N1"). The other robots of type 1
# follow from their blocks (ROBOT_BLOCKS below); the sheet Robots holds all of them (ROBOTS_ROWS at the end).
ROBOTS_HEADINGS = ['Robot', 'Maker', 'Type', 'Height (m)', 'Stated mass (kg)', 'Sources']
ROBOTS_G1_X1_N1 = [
    ('Unitree G1', 'Unitree', 1, 1.32, 35, 'U1: "1320x450x200mm", "About 35kg"'),
    ('AgiBot X1', 'AgiBot', 1, 1.3, 33, 'X1e: "130 cm", "33kg", "31DoF"'),
    ('Fourier N1', 'Fourier', 1, 1.245, 39, 'N1a: "1245 mm × 441 mm × 202 mm", "≈39 kg"'),
]
ROBOTS_WIDTHS = [14, 10, 6, 10, 14, 60]

# --- Joints ---------------------------------------------------------------------------------------------------------
# Every joint kind of the G1, X1 and N1: where it sits, its torque, which of the G1's two joint designs its inside
# follows (Module), its module mass (the X1's from AgiBot, the N1's from the joint-mass fit, none for the G1,
# whose JointParts give it), its heat group (sheet MagnetGrades). The G1: EVIDENCE.md E2.8 and E2.8c; the X1 and N1:
# E2.8e; the heat groups: E2.11.
# The column 'Share of the joint modules' is empty for them: it is for a robot whose joint torques and module masses
# no source gives, whose joint modules are a share of its mass (E5.17 point 1), split into its joints by this column.
JOINTS_HEADINGS = ['Robot', 'Number', 'Joint', 'Joints in the robot', 'Module', 'Torque limit (N·m)',
                   'Module mass, min (kg)', 'mode (kg)', 'max (kg)', 'Share of the joint modules', 'Cooling',
                   'Heat group', 'Body region', 'Sources', 'Basis']
JOINTS_G1_X1_N1 = [
    ('Unitree G1', 1, 'Hip pitch', 2, 'large', 88, None, None, None,
     'passive, with air from two centrifugal fans in the hip area', 'Hips', 'Legs', 'U3; T1 slides 11, 18, 41; T3',
     'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'),
    ('Unitree G1', 2, 'Hip roll', 2, 'large', 88, None, None, None,
     'passive, with air from two centrifugal fans in the hip area', 'Hips', 'Legs', 'U3; T1 slides 11, 18; T3',
     'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'),
    ('Unitree G1', 3, 'Hip yaw', 2, 'large', 88, None, None, None,
     'passive, with air from two centrifugal fans in the hip area', 'Hips', 'Legs', 'U3; T1 slides 11, 18; T3',
     'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'),
    ('Unitree G1', 4, 'Knee', 2, 'large', 139, None, None, None, 'copper vapour chamber into the frame', 'Knees',
     'Legs', 'U3; U1 90 (basic) and 120 N·m (EDU); T1 slides 18, 40, 42; T3k',
     'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'),
    ('Unitree G1', 5, 'Ankle pitch', 2, 'small', 35, None, None, None, 'passive', 'Ankles', 'Legs',
     'U3; T1 slides 11, 18, 20',
     'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'),
    ('Unitree G1', 6, 'Ankle roll', 2, 'small', 35, None, None, None, 'passive', 'Ankles', 'Legs',
     'U3; T1 slides 11, 18, 20',
     'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'),
    ('Unitree G1', 7, 'Waist yaw', 1, 'large', 88, None, None, None, 'centrifugal fan', 'Waist', 'Torso',
     'U3; T1 slides 11, 41',
     'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'),
    ('Unitree G1', 8, 'Shoulder pitch', 2, 'small', 25, None, None, None, 'passive', 'Shoulders', 'Arms',
     'U3; T1 slides 11, 18',
     'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'),
    ('Unitree G1', 9, 'Shoulder roll', 2, 'small', 25, None, None, None, 'passive', 'Shoulders', 'Arms',
     'U3; T1 slides 11, 18',
     'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'),
    ('Unitree G1', 10, 'Shoulder yaw', 2, 'small', 25, None, None, None, 'passive', 'Shoulders', 'Arms',
     'U3; T1 slides 11, 18',
     'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'),
    ('Unitree G1', 11, 'Elbow', 2, 'small', 25, None, None, None, 'passive', 'Elbows and wrists', 'Arms',
     'U3; T1 slides 11, 18',
     'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'),
    ('Unitree G1', 12, 'Wrist roll', 2, 'small', 25, None, None, None, 'passive', 'Elbows and wrists', 'Arms',
     'U3; T1 slide 11', 'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'),
    ('AgiBot X1', 1, 'Hip pitch', 2, 'large', 150, 1.22, 1.28, 1.34, 'not stated', 'Hips', 'Legs',
     'X1b R86-3 1.28 kg; X1c (150 N·m)',
     'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'),
    ('AgiBot X1', 2, 'Hip roll', 2, 'large', 150, 1.22, 1.28, 1.34, 'not stated', 'Hips', 'Legs',
     'X1b R86-3 1.28 kg; X1c (150 N·m)',
     'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'),
    ('AgiBot X1', 3, 'Hip yaw', 2, 'large', 50, 0.77, 0.81, 0.85, 'not stated', 'Hips', 'Legs',
     'X1b R86-2 0.81 kg; X1c (50 N·m)',
     'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'),
    ('AgiBot X1', 4, 'Knee', 2, 'large', 150, 1.22, 1.28, 1.34, 'not stated', 'Knees', 'Legs',
     'X1b R86-3 1.28 kg; X1c (150 N·m)',
     'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'),
    ('AgiBot X1', 5, 'Ankle pitch', 2, 'small', 80, 0.19, 0.2, 0.21, 'not stated', 'Ankles', 'Legs',
     'X1b L28 push rod 0.20 kg; X1c (80 N·m at the ankle)',
     'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'),
    ('AgiBot X1', 6, 'Ankle roll', 2, 'small', 80, 0.19, 0.2, 0.21, 'not stated', 'Ankles', 'Legs',
     'X1b L28 push rod 0.20 kg; X1c (80 N·m at the ankle)',
     'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'),
    ('AgiBot X1', 7, 'Waist', 3, 'large', 80, 0.77, 0.81, 0.85, 'not stated', 'Waist', 'Torso',
     'X1b R86-2 0.81 kg, 80 N·m peak; X1a "腰部连杆组件"; 9 R86-2 less 2 hips and 4 shoulders (E2.8e)',
     'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'),
    ('AgiBot X1', 8, 'Shoulder pitch', 2, 'large', 80, 0.77, 0.81, 0.85, 'not stated', 'Shoulders', 'Arms',
     'X1b R86-2 0.81 kg, 80 N·m peak (E2.8e)',
     'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'),
    ('AgiBot X1', 9, 'Shoulder roll', 2, 'large', 80, 0.77, 0.81, 0.85, 'not stated', 'Shoulders', 'Arms',
     'X1b R86-2 0.81 kg, 80 N·m peak (E2.8e)',
     'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'),
    ('AgiBot X1', 10, 'Shoulder yaw', 2, 'small', 19, 0.43, 0.45, 0.47, 'not stated', 'Shoulders', 'Arms',
     'X1b R52 0.45 kg, 19 N·m peak',
     'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'),
    ('AgiBot X1', 11, 'Elbow', 2, 'small', 19, 0.43, 0.45, 0.47, 'not stated', 'Elbows and wrists', 'Arms',
     'X1b R52 0.45 kg, 19 N·m peak',
     'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'),
    ('AgiBot X1', 12, 'Wrist (yaw, pitch, roll)', 6, 'small', 19, 0.43, 0.45, 0.47, 'not stated', 'Elbows and wrists',
     'Arms', 'X1b R52 0.45 kg, 19 N·m peak',
     'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'),
    ('AgiBot X1', 13, 'Gripper (OmniPicker)', 2, 'small', None, 0.41, 0.43, 0.45, 'not stated', 'Elbows and wrists',
     'Arms', 'X1d "Weight 0.43kg"; drawn as a small joint (E5.19 point 2: a motor, gears and a frame)',
     'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'),
    ('Fourier N1', 1, 'Hip pitch', 2, 'large', 90, 0.44, 0.88, 1.32, 'not stated', 'Hips', 'Legs',
     "N1a (90 N·m; N1b 95); the joint-mass fit on AgiBot's actuators, ± 50 % (E2.8e)",
     'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'),
    ('Fourier N1', 2, 'Hip roll', 2, 'large', 54, 0.35, 0.7, 1.05, 'not stated', 'Hips', 'Legs',
     "N1a (54 N·m); the joint-mass fit on AgiBot's actuators, ± 50 % (E2.8e)",
     'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'),
    ('Fourier N1', 3, 'Hip yaw', 2, 'large', 54, 0.35, 0.7, 1.05, 'not stated', 'Hips', 'Legs',
     "N1a (54 N·m); the joint-mass fit on AgiBot's actuators, ± 50 % (E2.8e)",
     'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'),
    ('Fourier N1', 4, 'Knee', 2, 'large', 90, 0.44, 0.88, 1.32, 'not stated', 'Knees', 'Legs',
     "N1a (90 N·m; N1b 95); the joint-mass fit on AgiBot's actuators, ± 50 % (E2.8e)",
     'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'),
    ('Fourier N1', 5, 'Ankle pitch', 2, 'small', 30, 0.27, 0.54, 0.81, 'not stated', 'Ankles', 'Legs',
     "N1a (30 N·m); the joint-mass fit on AgiBot's actuators, ± 50 % (E2.8e)",
     'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'),
    ('Fourier N1', 6, 'Ankle roll', 2, 'small', 30, 0.27, 0.54, 0.81, 'not stated', 'Ankles', 'Legs',
     "N1a (30 N·m); the joint-mass fit on AgiBot's actuators, ± 50 % (E2.8e)",
     'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'),
    ('Fourier N1', 7, 'Waist yaw', 1, 'large', 54, 0.35, 0.7, 1.05, 'not stated', 'Waist', 'Torso',
     "N1a (54 N·m); the joint-mass fit on AgiBot's actuators, ± 50 % (E2.8e)",
     'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'),
    ('Fourier N1', 8, 'Shoulder pitch', 2, 'large', 54, 0.35, 0.7, 1.05, 'not stated', 'Shoulders', 'Arms',
     "N1a (54 N·m); the joint-mass fit on AgiBot's actuators, ± 50 % (E2.8e)",
     'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'),
    ('Fourier N1', 9, 'Shoulder roll', 2, 'small', 30, 0.27, 0.54, 0.81, 'not stated', 'Shoulders', 'Arms',
     "N1a (30 N·m); the joint-mass fit on AgiBot's actuators, ± 50 % (E2.8e)",
     'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'),
    ('Fourier N1', 10, 'Shoulder yaw', 2, 'small', 30, 0.27, 0.54, 0.81, 'not stated', 'Shoulders', 'Arms',
     "N1a (30 N·m); the joint-mass fit on AgiBot's actuators, ± 50 % (E2.8e)",
     'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'),
    ('Fourier N1', 11, 'Elbow', 2, 'small', 30, 0.27, 0.54, 0.81, 'not stated', 'Elbows and wrists', 'Arms',
     "N1a (30 N·m); the joint-mass fit on AgiBot's actuators, ± 50 % (E2.8e)",
     'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'),
    ('Fourier N1', 12, 'Wrist yaw', 2, 'small', 30, 0.27, 0.54, 0.81, 'not stated', 'Elbows and wrists', 'Arms',
     "N1a (30 N·m); the joint-mass fit on AgiBot's actuators, ± 50 % (E2.8e)",
     'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'),
]
JOINTS_WIDTHS = [12, 8, 22, 10, 9, 10, 10, 9, 9, 12, 30, 18, 11, 50, 70]

# --- MagnetGrades ---------------------------------------------------------------------------------------------------
# The magnets' grade classes by heat group: each group a distribution over grade classes, drawn in each draw, tied
# within a draw (Matthias, 2026-10-28: "Heat has to matter and so the distribution will be different depending on the
# joint", "Accept as proposed"). Every joint judged as passively cooled ("Fans is not a sustainable solution"). No
# maker states the grade of a joint motor: the probabilities are estimates on the order of heat the sources give
# (EVIDENCE.md E2.11).
MAGNETGRADES_HEADINGS = ['Heat group', 'Grade class', 'Probability', 'Label', 'Basis']
MAGNETGRADES_ROWS = [
    ('Knees', 'SH', 0.3, 'E',
     'E2.11: the largest load, passive, derating to protect the magnets (OFweek; T1 slide 42; T3)'),
    ('Knees', 'UH', 0.5, 'E',
     'E2.11: the largest load, passive, derating to protect the magnets (OFweek; T1 slide 42; T3)'),
    ('Knees', 'EH', 0.2, 'E',
     'E2.11: the largest load, passive, derating to protect the magnets (OFweek; T1 slide 42; T3)'),
    ('Hips', 'SH', 0.5, 'E', 'E2.11: carry the body; passive as judged (T3, OFweek)'),
    ('Hips', 'UH', 0.4, 'E', 'E2.11: carry the body; passive as judged (T3, OFweek)'),
    ('Hips', 'EH', 0.1, 'E', 'E2.11: carry the body; passive as judged (T3, OFweek)'),
    ('Waist', 'SH', 0.6, 'E', 'E2.11: moves often (OFweek); passive as judged'),
    ('Waist', 'UH', 0.4, 'E', 'E2.11: moves often (OFweek); passive as judged'),
    ('Ankles', 'SH', 0.6, 'E', 'E2.11: carry the robot; small joints (T1)'),
    ('Ankles', 'UH', 0.4, 'E', 'E2.11: carry the robot; small joints (T1)'),
    ('Shoulders', 'H', 0.5, 'E', 'E2.11: hold the arm; low load'),
    ('Shoulders', 'SH', 0.5, 'E', 'E2.11: hold the arm; low load'),
    ('Elbows and wrists', 'H', 0.7, 'E', 'E2.11: the lowest load'),
    ('Elbows and wrists', 'SH', 0.3, 'E', 'E2.11: the lowest load'),
]
MAGNETGRADES_WIDTHS = [18, 12, 12, 7, 90]

# --- JointParts -----------------------------------------------------------------------------------------------------
# The G1's small joint part by part as China Post Securities weighed it (slide 43), the small joints not
# weighed at 0.5 / 1 / 1.5 times, and the large joint as the small one times a factor (EVIDENCE.md E2.8).
# One set for all robots, scaled to each joint's module mass ("similar within given ranges"). The column Grade:
# the steel grade whose element recipe a steel component follows, each by its use (EVIDENCE.md E5.18, agreed
# 2026-10-29): the gears 20CrMnTi, the small bearings GCr15, the output flange 42CrMo4; a component of shares has its
# grades in the sheet Shares.
JOINTPARTS_HEADINGS = ['Component', 'Small joint, weighed (g)', 'Small joints not weighed: times min', 'times mode',
                       'times max', 'Material (one material only)', 'Grade', 'Large joint: factor min',
                       'factor mode', 'factor max', 'Why the factor', 'Label', 'Sources']
JOINTPARTS_ROWS = [
    ('Motor stator', 94.3, 0.5, 1, 1.5, None, None, 1, 1.78, 2.67, "the motor's cross-section, 80 against 60 mm across",
     'W; E for the spread and the factor',
     'T1 slide 43 (figure 37); factors EVIDENCE.md E2.8; Matthias, 2026-10-27, step 1: '
     '"Accept all" (EVIDENCE.md E2.8)'),
    ('Motor rotor', 42.9, 0.5, 1, 1.5, None, None, 1, 1.78, 2.67, "the motor's cross-section",
     'W; E for the spread and the factor',
     'T1 slide 43 (figure 37); factors EVIDENCE.md E2.8; Matthias, 2026-10-27, step 1: '
     '"Accept all" (EVIDENCE.md E2.8)'),
    ('Magnet carrier', 16.9, 0.5, 1, 1.5, None, None, 1, 1.78, 2.67, "the motor's cross-section",
     'W; E for the spread and the factor',
     'T1 slide 43 (figure 37); factors EVIDENCE.md E2.8; Matthias, 2026-10-27, step 1: '
     '"Accept all" (EVIDENCE.md E2.8)'),
    ('Gear stage 1, sun gear', 8, 0.5, 1, 1.5, 'Steel', '20CrMnTi', 1.17, 2.33, 3.56,
     'from the cross-section alone to growing with the torque (99.3 against 27.9 N·m); mode '
     '3.56^(2/3)', 'W; E for the spread and the factor',
     'T1 slide 43 (figure 37); factors EVIDENCE.md E2.8; Matthias, 2026-10-27, step 1: '
     '"Accept all" (EVIDENCE.md E2.8)'),
    ('Gear stage 1, planets and carrier with stage 2 sun gear', 25.3, 0.5, 1, 1.5, 'Steel', '20CrMnTi', 1.17, 2.33,
     3.56, 'as the sun gear', 'W; E for the spread and the factor',
     'T1 slide 43 (figure 37); factors EVIDENCE.md E2.8; Matthias, 2026-10-27, step 1: '
     '"Accept all" (EVIDENCE.md E2.8)'),
    ('Gear stage 1, ring gear', 24.1, 0.5, 1, 1.5, 'Steel', '20CrMnTi', 1.17, 2.33, 3.56, 'as the sun gear',
     'W; E for the spread and the factor',
     'T1 slide 43 (figure 37); factors EVIDENCE.md E2.8; Matthias, 2026-10-27, step 1: '
     '"Accept all" (EVIDENCE.md E2.8)'),
    ('Gear stage 2, planets, carrier and crossed roller bearing', 74, 0.5, 1, 1.5, None, None, 1.17, 2.33, 3.56,
     'as the sun gear', 'W; E for the spread and the factor',
     'T1 slide 43 (figure 37); factors EVIDENCE.md E2.8; Matthias, 2026-10-27, step 1: '
     '"Accept all" (EVIDENCE.md E2.8)'),
    ('Gear stage 2, ring gear', 23.8, 0.5, 1, 1.5, 'Steel', '20CrMnTi', 1.17, 2.33, 3.56, 'as the sun gear',
     'W; E for the spread and the factor',
     'T1 slide 43 (figure 37); factors EVIDENCE.md E2.8; Matthias, 2026-10-27, step 1: '
     '"Accept all" (EVIDENCE.md E2.8)'),
    ('Driver board', 12.8, 0.5, 1, 1.5, 'Electronics', None, 1.78, 3.56, 5.33,
     'one, two or three boards of the larger size (T3k: "a stack")', 'W; E for the spread and the factor',
     'T1 slide 43 (figure 37); factors EVIDENCE.md E2.8; Matthias, 2026-10-27, step 1: '
     '"Accept all" (EVIDENCE.md E2.8)'),
    ('Two small bearings', 11, 0.5, 1, 1.5, 'Steel', 'GCr15', 1, 1.78, 2.67, 'the area',
     'W; E for the spread and the factor',
     'T1 slide 43 (figure 37); factors EVIDENCE.md E2.8; Matthias, 2026-10-27, step 1: '
     '"Accept all" (EVIDENCE.md E2.8)'),
    ('Housing', 79.3, 0.5, 1, 1.5, 'Aluminium', None, 1, 1.39, 2.09, "the joint's surface",
     'W; E for the spread and the factor',
     'T1 slide 43 (figure 37); factors EVIDENCE.md E2.8; Matthias, 2026-10-27, step 1: '
     '"Accept all" (EVIDENCE.md E2.8)'),
    ('Two end caps', 23.7, 0.5, 1, 1.5, 'Aluminium', None, 1, 1.78, 2.67, 'the area',
     'W; E for the spread and the factor',
     'T1 slide 43 (figure 37); factors EVIDENCE.md E2.8; Matthias, 2026-10-27, step 1: '
     '"Accept all" (EVIDENCE.md E2.8)'),
    ('Output flange', 50.8, 0.5, 1, 1.5, 'Steel', '42CrMo4', 1, 1.78, 2.67, 'the area',
     'W; E for the spread and the factor',
     'T1 slide 43 (figure 37); factors EVIDENCE.md E2.8; Matthias, 2026-10-27, step 1: '
     '"Accept all" (EVIDENCE.md E2.8)'),
    ('Other', 38.1, 0.5, 1, 1.5, None, None, 1, 1.78, 2.67, 'the area', 'W; E for the spread and the factor',
     'T1 slide 43 (figure 37); factors EVIDENCE.md E2.8; Matthias, 2026-10-27, step 1: '
     '"Accept all" (EVIDENCE.md E2.8)'),
]
JOINTPARTS_WIDTHS = [44, 12, 12, 9, 9, 16, 12, 10, 9, 9, 60, 14, 60]

# --- Parts ----------------------------------------------------------------------------------------------------------
# Every other part of the G1, X1 and N1: its number, the figure's row it falls in, its body region, the mass of one
# and its one material, its shares (sheet Shares), or what it is computed from; one part per robot takes the
# robot's remainder (the frame). EVIDENCE.md E2.8, E2.8c, E2.8e. Their grades are in PART_GRADES below; the column
# Grade: the grade whose element recipe a part of steel, titanium or a copper alloy follows (E5.18, E5.19).
PARTS_HEADINGS = ['Robot', 'Part', 'Number in the robot', "Kind (the figure's row)", 'Body region',
                  'Mass of one, min (kg)', 'mode (kg)', 'max (kg)', 'Material (one material only)', 'Grade',
                  'Remainder of, or computed from', 'Label', 'Sources']
PARTS_G1_X1_N1 = [
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
    ('Unitree G1', 'Battery housing, busbars and wires', 1, 'Battery pack', 'Torso', None, None, None, None,
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
    ('AgiBot X1', 'Joint module, small', 16, 'Ankles and arms', 'Legs 4, Arms 12', None, None, None, None,
     "the Joints' module masses; inside as JointParts' joint of its size, scaled to its mass", 'S',
     'X1b; X1d (the two grippers, E5.19 point 2)'),
    ('AgiBot X1', 'Joint module, large', 15, 'Hips, knees, waist and shoulders', 'Legs 8, Torso 3, Arms 4', None,
     None, None, None, "the Joints' module masses; inside as JointParts' joint of its size, scaled to its mass", 'S',
     'X1b'),
    ('AgiBot X1', 'Encoders (two per joint)', 62, 'In the joints', 'as their joints', None, None, None, None,
     'Sensors and SensorElements (Encoder)', 'E',
     'two per joint, as the G1 (U1, U2) and the N1 (N1a); X1a lists the actuators as bought-in units and names no '
     'encoders (E2.8e); the two grippers joints since 2026-10-29 (E5.19 point 2)'),
    ('AgiBot X1', 'Main board fan', 1, 'Torso boards', 'Torso', 0.005, 0.01, 0.02, None, None, 'E',
     "the mini PC's fan, as the G1's main board fan (E2.8e)"),
    ('AgiBot X1', 'Main board heat sink: heat pipes and fins', 1, 'Torso boards', 'Torso', 0.055, 0.12, 0.19,
     'Copper', None, 'E',
     "the mini PC's cooler; no source of a mini PC's cooler; context only: FW1 67.5 g, DY1 199 g, each with its fan "
     '(E2.8e)'),
    ('AgiBot X1', 'Battery pack', 1, 'Battery pack', 'Torso', 1.75, 2.2, 3.3, None,
     'its cells, its management board (Boards) and its housing (the rows below)', 'S, E',
     'X1a "48V8AH三元电池", stainless-steel case; mass: the G1\'s 168 Wh/kg; the lower cut where the pack holds '
     'its heaviest cells (232.5 Wh/kg) and management board in the lightest robot (E2.8e, 2026-10-28)'),
    ('AgiBot X1', 'Battery cells', 1, 'Battery pack', 'Torso', None, None, None, 'Battery materials',
     "from the energy: Constants voltage × capacity over the NMC cell's Wh/kg", 'S',
     'X1a "12S"; element_recipes.xlsx NMC cylindrical'),
    ('AgiBot X1', 'Battery housing, busbars and wires', 1, 'Battery pack', 'Torso', None, None, None, None,
     'the battery pack, less its cells and its management board', 'E', 'X1a (stainless-steel case); as the G1'),
    ('AgiBot X1', 'Cable conductors and insulation', 1, 'Cables', 'Whole body', None, None, None, None,
     'from Constants: length, cross-sections, insulation', 'S', 'X1a: the lengths listed (11.0 m)'),
    ('AgiBot X1', 'XT30 (2+2) connectors (two per joint)', 62, 'Cables', 'Whole body', 0.0015, 0.003, 0.0045, None,
     None, 'S, E',
     "X1a: 58 cable plugs (19 cables with two, 12 with one, 6 terminating resistors, 2 to the L28); mass as the "
     "G1's (E); 4 more, two per joint, for the two grippers (E5.19 point 2)"),
    ('AgiBot X1', 'Titanium (TC4) links: waist (2), ankles (4)', 1, 'Frame and shell', 'Legs, Torso', 0.2, 0.4, 0.6,
     'Titanium', None, 'E', 'X1a "钛合金TC4"; masses not given'),
    ('AgiBot X1', 'Stainless 17-4PH shafts and crosses; steel pins (about 115)', 1, 'Frame and shell', 'Whole body',
     0.1, 0.3, 0.5, None, None, 'E', 'X1a "0Cr17Ni4Cu4Nb", "40Cr"; its two steels in the sheet Shares'),
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
    ('Fourier N1', 'Battery housing, busbars and wires', 1, 'Battery pack', 'Torso', None, None, None, None,
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
PARTS_WIDTHS = [12, 44, 10, 20, 16, 11, 9, 9, 18, 14, 52, 7, 56]

# --- Shares ---------------------------------------------------------------------------------------------------------
# The materials of the parts and components that hold more than one; each group has one named remainder and
# nothing is rescaled (no normalisation). EVIDENCE.md E2.8, E2.10. The column Grade: the grade whose element recipe the
# material follows, as for a part (E5.18, E5.19): 'A or B' is either, each as often (a discrete state, drawn); empty
# for aluminium and plastics (type 1's recipes) and for magnets (their heat group). What the share is of the part
# opens its Basis. A material written 'A or B' is either material, each as often (the battery housing, E5.19 point 1).
SHARES_HEADINGS = ['Part or component', 'Material', 'Grade', 'Share min', 'Share mode', 'Share max', 'Remainder',
                   'Label', 'Basis']
SHARES_ROWS = [
    ('Motor stator', 'Copper', None, 0.23, 0.36, 0.45, None, 'S',
     'The winding: measured car traction motors 23-29 % (Drexler et al. 2025), car auxiliary motors 27 / 36 / 45 %; '
     'E2.10; Matthias: "Yes use this numberrs"'),
    ('Motor stator', 'Plastics', None, 0.02, 0.05, 0.1, None, 'E', "The winding's coating: E2.8"),
    ('Motor stator', 'Steel', 'M19 or M27', None, None, None, 'Yes', 'E',
     'The electrical steel: Matthias, 2026-10-27, step 1: "Accept all" (EVIDENCE.md E2.8); its grade E5.18'),
    ('Motor rotor', 'Magnets (NdFeB)', None, 0.45, 0.9, 1, None, 'E',
     'T1 calls it "磁钢"; Matthias, 2026-10-27, step 1: "Accept all" (EVIDENCE.md E2.8)'),
    ('Motor rotor', 'Steel', 'M19 or M27', None, None, None, 'Yes', 'E',
     'Matthias, 2026-10-27, step 1: "Accept all" (EVIDENCE.md E2.8); its grade E5.18'),
    ('Magnet carrier', 'Plastics', None, 0.05, 0.15, 0.3, None, 'E', 'The plastic bearing: T1 "铝+塑料轴承"'),
    ('Magnet carrier', 'Aluminium', None, None, None, None, 'Yes', 'E',
     'Matthias, 2026-10-27, step 1: "Accept all" (EVIDENCE.md E2.8)'),
    ('Gear stage 2, planets, carrier and crossed roller bearing', 'Aluminium', None, 0.125, 0.25, 0.4, None, 'E',
     'The carrier: T1 "保持架为铝，其余为钢"'),
    ('Gear stage 2, planets, carrier and crossed roller bearing', 'Steel', 'Gear stage 2 steel: 20CrMnTi and GCr15',
     None, None, None, 'Yes', 'E',
     'The planets and the bearing: Matthias, 2026-10-27, step 1: "Accept all" (EVIDENCE.md E2.8); 20CrMnTi 30 / 50 / '
     '70 % of the steel, GCr15 the remainder (E5.18)'),
    ('Other', 'Copper', None, 0.1, 0.25, 0.4, None, 'E', 'Wires: no basis'),
    ('Other', 'Steel', '42CrMo4', 0.2, 0.4, 0.6, None, 'E',
     'Screws, encoder parts: no basis; the grade of class 12.9 screws (E5.18)'),
    ('Other', 'Plastics', None, None, None, None, 'Yes', 'E',
     'Matthias, 2026-10-27, step 1: "Accept all" (EVIDENCE.md E2.8)'),
    ('Hip fan', 'Copper', None, 0.05, 0.1, 0.2, None, 'E', 'The motor winding: E2.8'),
    ('Hip fan', 'Plastics', None, None, None, None, 'Yes', 'E', 'E2.8'),
    ('Waist fan', 'Copper', None, 0.05, 0.1, 0.2, None, 'E', 'The motor winding: E2.8'),
    ('Waist fan', 'Plastics', None, None, None, None, 'Yes', 'E', 'E2.8'),
    ('Main board fan', 'Copper', None, 0.05, 0.1, 0.2, None, 'E', 'The motor winding: E2.8'),
    ('Main board fan', 'Plastics', None, None, None, None, 'Yes', 'E', 'E2.8'),
    ('XT30 (2+2) connectors (two per joint)', 'Copper', None, 0.175, 0.35, 0.525, None, 'E', 'The contacts: E2.8'),
    ('XT30 (2+2) connectors (two per joint)', 'Plastics', None, None, None, None, 'Yes', 'E', 'The housing: E2.8'),
    ('Battery housing, busbars and wires', 'Copper', 'Nickel strip', 0.01, 0.03, 0.06, None, 'E',
     'The nickel strips between the cells, 0.2 mm thick (sevarg.net, measured), counted with the copper (Matthias, '
     '2026-10-29: "With Copper"); E5.19 point 1'),
    ('Battery housing, busbars and wires', 'Copper', None, 0.05, 0.1, 0.15, None, 'E',
     'The copper wires and busbars: E5.19 point 1'),
    ('Battery housing, busbars and wires', 'Plastics', None, 0.05, 0.1, 0.2, None, 'E',
     'The cell holders, insulation and tape: E5.19 point 1'),
    ('Battery housing, busbars and wires', 'Aluminium or Plastics', None, None, None, None, 'Yes', 'E',
     'The housing: "aluminum or high-impact plastics" (teswaybike.com, a claim), each as often (E5.19 point 1)'),
    ('Battery housing (aluminium), busbars and wires', 'Copper', 'Nickel strip', 0.01, 0.03, 0.06, None, 'E',
     'The nickel strips between the cells, counted with the copper (Matthias, 2026-10-29: "With Copper"); E5.19 '
     'point 1'),
    ('Battery housing (aluminium), busbars and wires', 'Copper', None, 0.05, 0.1, 0.15, None, 'E',
     'The copper wires and busbars: E5.19 point 1'),
    ('Battery housing (aluminium), busbars and wires', 'Plastics', None, 0.05, 0.1, 0.2, None, 'E',
     'The cell holders, insulation and tape: E5.19 point 1'),
    ('Battery housing (aluminium), busbars and wires', 'Aluminium', None, None, None, None, 'Yes', 'E',
     'The housing: "Aluminum Alloy" (EngineAI, the PM01; E5.6, E5.19 point 1)'),
    ('Stainless 17-4PH shafts and crosses; steel pins (about 115)', 'Steel', '17-4PH', 0.25, 0.5, 0.75, None, 'E',
     'The shafts and crosses: X1a "0Cr17Ni4Cu4Nb"; their share of the part not given (E: half, half to 1.5 times)'),
    ('Stainless 17-4PH shafts and crosses; steel pins (about 115)', 'Steel', 'C45', None, None, None, 'Yes', 'E',
     'The pins (E5.18: "the X1\'s steel pins C45")'),
    ('Frame: aluminium, with steel 45 and P20 parts', 'Steel', 'RP1 frame steel: C45 and P20', 0.1, 0.2, 0.3, None,
     'E', 'The steel parts: 28 of its 112 CNC parts are steel, 24 of steel 45 or AISI 1045 and 4 of P20 (RP1a), by '
     'count only (E5.14 point 9, E5.18)'),
    ('Frame: aluminium, with steel 45 and P20 parts', 'Aluminium', None, None, None, None, 'Yes', 'E',
     'The aluminium parts: AL6061-T6, AL7075, AL5052 (RP1a); E5.14 point 9'),
]
SHARES_WIDTHS = [52, 18, 22, 10, 10, 10, 10, 7, 90]

# --- Boards ---------------------------------------------------------------------------------------------------------
# Every circuit board of the G1, X1 and N1: its area and the car board category whose gold, silver, palladium, tin
# and nickel per cm2 it takes (RAWCLICVehicleElectronics, read where it lies). EVIDENCE.md E2.8b, E2.8e.
BOARDS_HEADINGS = ['Robot', 'Board', 'Number in the robot', "Kind (the figure's row)", 'Body region',
                   'Area of one, min (cm2)', 'mode (cm2)', 'max (cm2)', 'Mass from',
                   'Car board category (RAWCLICVehicleElectronics 04_)', 'Label', 'Sources']
BOARDS_G1_X1_N1 = [
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
    ('AgiBot X1', 'Driver board, small joint', 16, 'Ankles and arms', 'Legs 4, Arms 12', None, None, None,
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
# Every sensor of the G1, X1 and N1 and the mass of one (EVIDENCE.md E2.8b, E2.8e).
SENSORS_HEADINGS = ['Robot', 'Sensor', 'Number in the robot', "Kind (the figure's row)", 'Body region',
                    'Mass of one, min (g)', 'mode (g)', 'max (g)', 'Label', 'Sources']
SENSORS_G1_X1_N1 = [
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
    ('AgiBot X1', 'Encoder', 62, 'In the joints', 'as their joints', None, None, None, 'E',
     'two per joint (E2.8e), the grippers with them; elements only'),
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
SENSORELEMENTS_G1_X1_N1 = [
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
# The shared numbers once, under the robot "all", and the G1's, X1's and N1's own (mass, battery, cable length)
# (EVIDENCE.md E2.8, E2.8b, E2.8e). The last four shared ones are for the robots of the blocks below where their
# own sources stop (E5.14, E5.17, agreed 2026-10-29).
CONSTANTS_HEADINGS = ['Robot', 'Quantity', 'Min', 'Mode', 'Max', 'Unit', 'Label', 'Source']
CONSTANTS_G1_X1_N1 = [
    ('all', 'Board mass per cm2 (boards not weighed)', 0.28, 0.56, 0.84, 'g/cm2', 'E',
     'the weighed small driver board, 12.8 g on 22.9 cm2, ± 50 %; E2.8'),
    ('all', "Copper share of a board's mass", 0.125, 0.2, 0.287, 'share', 'S',
     'Bizzo et al. 2014, Table 3: 14 analyses combined (min / mean / max); E2.8b'),
    ('all', 'Power conductor cross-section (2 conductors)', 0.52, 0.82, 1.31, 'mm2', 'S',
     "20 / 18 / 16 AWG, the XT30's wire range (TME, second-hand)"),
    ('all', 'Signal conductor cross-section (2 conductors)', 0.065, 0.13, 0.2, 'mm2', 'E', 'E2.8'),
    ('all', 'Copper density', 8.96, 8.96, 8.96, 'g/cm3', 'S', 'copper'),
    ('all', 'Insulation and jackets, per mass of copper', 0.5, 1, 1.5, 'times', 'E', 'E2.8'),
    ('all', 'Joint modules, share of the robot mass', 0.245, 0.49, 0.735, 'share', 'E',
     'batch 1 and the G1: 36 to 53 %, median 49 %; half to 1.5 times (E5.17 point 1)'),
    ('all', 'Battery energy per kg of robot', 6, 12, 18, 'Wh/kg', 'E',
     'batch 1 and the G1, X1, N1: 6.8 to 21, median 12; half to 1.5 times (E5.17 point 2)'),
    ('all', 'Battery pack, Wh per kg (packs not weighed)', 109.3, 164, 232.5, 'Wh/kg', 'S, E',
     "the median of the G1's, X1's, N1's and PM01's packs (159 to 168); the pack at most 1.5 times its mode's mass, "
     "at least its cells at the NMC cells' lowest energy per kg (E5.14 point 3)"),
    ('all', 'Shell, share of the robot mass', 0.0575, 0.115, 0.1725, 'share', 'E',
     "the median of the G1's 12.9, the N1's 11.5 and the X1's 9.1 %; half to 1.5 times (E5.14 point 6)"),
    ('all', 'Sensor housing, aluminium share', 0.25, 0.5, 0.75, 'share', 'E',
     'a sensor module beyond its car sensor elements (the car file: "not the complete module housing"): its housing, '
     "aluminium as the LiDAR's and the depth camera's, plastics the remainder; half to 1.5 times (2026-10-29, point "
     '3c, its 30 / 50 / 70 % widened by the rule for estimates)'),
    ('all', 'Board rest, glass fibre share', 0.4, 0.55, 0.7, 'share', 'S, E',
     "the rest of a board beyond its metals: Isola's FR-4 laminates 35 to 60 % glass by weight, the populated boards' "
     'non-metals 46 to 72 %; the mode between a 1.6 mm board of 7628 cores and a dense board of thin plies '
     '(EVIDENCE.md E5.21; 2026-10-29, "Yes, enter them", point 3b)'),
    ('all', 'Board rest, bromine share', 0.044, 0.088, 0.132, 'share', 'E',
     'about 15 % TBBPA in an FR-4 laminate (Danish EPA 1999), 58.8 % of it bromine; half to 1.5 times (EVIDENCE.md '
     'E5.21; point 3b)'),
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
    # The sources of the robots of the blocks below (EVIDENCE.md E5.1 to E5.16), read on 2026-10-29.
    ('RO1', 'RoboParty, Roboto Origin parts list (Internal Roboto D-BOM, 20260105)',
     'https://github.com/Roboparty/roboto_origin/blob/main/assets/BOM_EN.md', "Manufacturer's parts list"),
    ('RO2', 'RoboParty, rpo.urdf (link masses, effort limits)', 'https://github.com/Roboparty/rpo_description',
     "Manufacturer's model file"),
    ('DM1', 'DAMIAO, 2025 product selection handbook (达妙科技 2025年产品选型手册), pp. 13 and 20',
     'worldrobotconference.com', "The actuators' maker's datasheet"),
    ('AS1', 'Menlo, Asimov 1 mechanical system tour (the actuator at each joint, its peak torque)',
     'https://docs.menlo.ai/asimov/1/overview/system-tour/mechanical',
     "Manufacturer's documentation; it marks these tables as possibly outdated"),
    ('AS2', 'Menlo, Asimov 1 electrical system tour', 'https://docs.menlo.ai/asimov/1/overview/system-tour/electrical',
     "Manufacturer's documentation"),
    ('AS3', 'Menlo, asimov_1_25dof.urdf', 'https://github.com/menloresearch/asimov-1', "Manufacturer's model file"),
    ('RP1a', 'RoboParty, RP1.3.4 BOM with 5-DOF arms (sheet 总BOM)', 'https://github.com/Roboparty/RP1_hardware',
     "Manufacturer's parts list; its unit weights empty"),
    ('RP1b', 'RoboParty, ROMOMO hardware introduction V261013', 'https://github.com/Roboparty/ROMOMO',
     "Manufacturer's specification"),
    ('RP1c', 'RoboParty, RMM6562-2E and RMM10062-2E test reports (1013); RMM drawings V1.0',
     'https://github.com/Roboparty/ROMOMO', "Manufacturer's laboratory tests and drawings"),
    ('RP1d', 'CNX Software, the RP1', 'https://www.cnx-software.com/?p=178402', 'Third party'),
    ('RP1e', 'RoboParty, rp1_24dof.urdf', 'https://github.com/Roboparty/RP1_description', "Manufacturer's model file"),
    ('BT1', 'Booster Robotics, T1 specifications',
     'https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/',
     "Manufacturer's documentation"),
    ('BT1b', 'chipsilicon and Generation Robots, the Booster T1 battery (10.5 Ah)', 'https://www.generationrobots.com',
     'Resellers'),
    ('BT1u', 'Booster Robotics, T1_23dof.urdf', 'https://github.com/BoosterRobotics/booster_assets',
     "Manufacturer's model file"),
    ('BK1', 'Booster Robotics, K1 specifications',
     'https://docs.booster.tech/docs/product-manual/k1/getting-started/specifications/',
     "Manufacturer's documentation"),
    ('BK1d', 'Generation Robots, Booster K1 datasheet (48 V, 5 Ah)',
     'https://static.generation-robots.com/media/datasheet-booster-k1.pdf',
     "A reseller's datasheet of Booster's figures"),
    ('BK1u', 'Booster Robotics, K1_22dof.urdf', 'https://github.com/BoosterRobotics/booster_assets',
     "Manufacturer's model file"),
    ('BT2', 'Booster Robotics, T2 specifications and overview; booster.tech/booster-t2', 'https://docs.booster.tech',
     "Manufacturer's documentation"),
    ('PM1', 'EngineAI, PM01 development guide (joint system, peripheral devices, hardware, sensors)',
     'https://en.engineai.com.cn/open/docs/pm01/01/joint-system', "Manufacturer's documentation"),
    ('PM1m', 'EngineAI, PM01 user manual V1.0', 'https://en.engineai.com.cn/product-support-pm01.html',
     "Manufacturer's manual"),
    ('PM1u', 'EngineAI, serial_pm01_edu.urdf', 'https://github.com/engineai-robotics/engineai_robotics_description',
     "Manufacturer's model file"),
    ('UR1', 'Unitree, R1 product page', 'https://www.unitree.com/R1', "Manufacturer's specification"),
    ('UR1b', "Resellers' R1 battery listings (maverickdrone, globaldronehq), through search results", '',
     'Third party, not read first-hand'),
    ('UR1u', 'Unitree, R1.urdf', 'https://github.com/unitreerobotics/unitree_ros', "Manufacturer's model file"),
    ('G1p', 'Unitree, G1+ product page', 'https://www.unitree.com/G1pl', "Manufacturer's specification"),
    ('AK1', 'ROBOTIS, AI Sapiens K1 hardware and electrical specifications',
     'https://docs.robotis.com/docs/systems/aisapiens/specifications/hardware',
     "Manufacturer's documentation; it may change before the launch"),
    ('AK2', 'ROBOTIS, DYNAMIXEL-Q product page', 'https://www.robotis.com/en/product/dynamixel-q.php',
     "Manufacturer's specification, preliminary"),
    ('K0a', 'ROBOTIS, K0 - AI Sapiens', 'https://ai.robotis.com/ai_sapiens/introduction_ai_sapiens.html',
     "Manufacturer's documentation, subject to change"),
    ('HG', 'humanoid.guide, the catalogue of humanoid robots, read 2026-10-28 and 2026-10-29', 'https://humanoid.guide',
     'A third-party catalogue; most entries marked "Not Verified" there'),
    ('SP1', "Fauna Robotics, Sprout, the maker's page as read on 2026-10-29", '',
     "Manufacturer's specification; its address is not recorded in EVIDENCE.md E5.16"),
    ('SA1', "StarBot USA, Astra, the maker's page as read on 2026-10-29", '',
     "Manufacturer's specification; its address is not recorded in EVIDENCE.md E5.16"),
]
SOURCES_WIDTHS = [12, 70, 90, 50]

# ======================================================================================================================
# The other robots of type 1: one block each
# ======================================================================================================================
# Matthias, 2026-10-29: "I want to complete all work with type 1 and see the results!", then "Yes, build it" (the entry
# of type 1's research, documentation/claude/HANDOVER.md, points 1 to 10, with decisions A to D). Every robot of the
# register's sheet Type 1 has rows of its own, as the G1, X1 and N1 have; decision A: held here, one block per robot.
# A block gives what the robot's own sources give (EVIDENCE.md E5.1 to E5.16) and, where they stop, what the agreed
# method fills in: the actuators E5.12, the rest of the robot E5.14, batches 2 to 4 E5.17, the steels E5.18, the
# battery's rest E5.19. robot_rows() writes from a block the rows every robot has in the same form: its joints and
# their modules, driver boards, encoders and connectors (two per joint), its battery pack, cells and housing, its
# battery management board, cables, screws, shell and frame. The G1+ and the Asimov 2 are written from the G1's and the
# Asimov 1's rows (E5.17 points 5 and 7). Nothing here is fitted or rescaled: each number is the source's or the
# agreed estimate's.

# An actuator's mass where no source states it: its peak torque over the median peak torque density of the nine
# actuators read, N·m per kg (65.7 / 87.3 / 133.7: RMM6562-2E, DM-J10010L, RMM10062-2E), widened to half to 1.5 times
# (E5.12 point 4).
TORQUE_DENSITY = 87.3
# A figure a maker states once: ± 5 %, the spread between units (E5.12 point 3; the N1's accepted production
# tolerance of its battery, E5.14 point 2).
STATED_SPREAD = 0.05
# A joint's class: small below this peak torque, N·m, large from it (E5.12 point 1: the geometric middle of the G1's
# small joint, 35 N·m, and its large one, 88 N·m). Each block's joints are written with the class this gives.
LARGE_FROM_NM = 55

# The template's sizes and masses where a robot's sources name a board or sensor but give no size or mass (E5.14
# points 4 and 8, as the G1's, X1's and N1's).
COMPUTER = (60, 120, 180)        # cm2: a computer board, or the carrier of a compute module (as the X1's and N1's)
POWER = (30, 60, 100)            # cm2: a power distribution board (as the G1's)
BATTERY_BOARD = (30, 60, 96)     # cm2: a battery management board (as the G1's)
SMALL_BOARD = (5, 15, 30)        # cm2: a head, IMU or other small board (as the G1's head control board)
AGX_ORIN = (82.65, 87, 91.35)    # cm2: NVIDIA Jetson AGX Orin, 100 × 87 mm (search results, E5.13), ± 5 %
ORIN_NX = (29.74, 31.3, 32.87)   # cm2: NVIDIA Jetson Orin NX, 69.6 × 45 mm (search results, E5.13), ± 5 %
RADXA_CM5 = (20.9, 22, 23.1)     # cm2: Radxa CM5, 55 × 40 mm (search results, E5.13), ± 5 %
IMU_G = (1, 2, 5)                # g: a motion sensor (as the G1's)
MICROPHONES_G = (5, 10, 20)      # g: a microphone array (as the G1's)
SPEAKER_G = (17.5, 35, 60)       # g: a speaker (as the G1's)
D435_G = (72, 75, 80)            # g: an Intel RealSense D435 or D435i (Intel's datasheet, second-hand; as the G1's)
CONNECTOR_KG = (0.0015, 0.003, 0.0045)   # kg: one XT30 (2+2) connector (as the G1's)
# The computer's cooler of a robot whose sources do not weigh it (Matthias, 2026-10-29, "Yes, build them", point 4;
# EVIDENCE.md E5.20, "Not entered": until then in its frame's remainder): a fan as the G1's main board fan (its copper
# winding by the sheet Shares), and for an ARM board (a Jetson, Rockchip, Radxa, Qualcomm or RDK, or a board not named)
# the G1's aluminium heat sink, for an Intel or AMD laptop-class processor the X1's and N1's copper heat pipes and fins
# (E2.8e). Each an entry of a block's `cooler`, as one of its `parts`.
FAN_KG = (0.005, 0.01, 0.02)
COOLER_FAN = ('Main board fan', 1, 'Torso boards', 'Torso', FAN_KG, None, None, 'E',
              "as the G1's main board fan (E2.8e; 2026-10-29, point 4)")
ARM_SINK = ('Main board heat sink', 1, 'Torso boards', 'Torso', (0.05, 0.1, 0.2), 'Aluminium', None, 'E',
            "an ARM board's: as the G1's (E2.8e; 2026-10-29, point 4)")
X86_SINK = ('Main board heat sink: heat pipes and fins', 1, 'Torso boards', 'Torso', (0.055, 0.12, 0.19), 'Copper',
            None, 'E', "an Intel or AMD laptop-class processor's: as the X1's and N1's (E2.8e; 2026-10-29, point 4)")
ARM_COOLER = [COOLER_FAN, ARM_SINK]
X86_COOLER = [COOLER_FAN, X86_SINK]
NDFEB_G_PER_MM3 = 0.0075   # g per mm3: sintered NdFeB, about 7.5 g/cm3


def disc_kg(diameter_mm: float, height_mm: float) -> float:
    """The mass of one NdFeB disc magnet, kg: its volume times NDFEB_G_PER_MM3."""
    return math.pi * (diameter_mm / 2) ** 2 * height_mm * NDFEB_G_PER_MM3 / 1000


# The RP1's 80 N52 magnets in its covers (RP1a: 4 × 4 and 4 × 2 mm, how many of each not stated): one magnet from all
# of the small size to all of the large, the mode between them (S, E).
COVER_MAGNET = (round(disc_kg(4, 2), 6), round((disc_kg(4, 2) + disc_kg(4, 4)) / 2, 6), round(disc_kg(4, 4), 6))
SCREWS_KG = (0.2, 0.5, 1)        # kg: a robot's screws (as the G1's; E5.14 point 7)
CABLES_M = (5, 10, 15)           # m of four conductors where no length is listed (as the N1's; E5.14 point 5)
# The car sensor elements of a sensor whose maker names its kind but not its model (E5.14 point 8, as type 1's).
DEPTH_CAMERA = [('laser diode array', 1), ('IR camera sensor', 2), ('CMOS image sensor', 1)]   # as the D435's
LIDAR = [('laser diode array', 1), ('photodetector array', 1), ('IMU', 1)]                      # as the Mid-360's
CAMERA = [('CMOS image sensor', 1)]
MICROPHONES = [('MEMS microphone array', 4)]   # as the G1's four (T1 slide 33)
# A power distribution board where a robot's sources name none (as the G1's; E5.14 point 4).
POWER_BOARD = ('Power distribution board', 1, 'Torso boards', 'Torso', POWER, 'PE_HVS', 'E',
               'as the G1 (E5.14 point 4)')

# The texts of the sheets that 02 reads as what a row is computed from (its column "Remainder of, or computed from"),
# and the basis every joint's magnets share.
JOINT_MASSES = "the Joints' module masses; inside as JointParts' joint of its size, scaled to its mass"
JOINT_SHARES = ("the Joints' shares of the joint modules, a share of the robot's mass (Constants); inside as "
                "JointParts' joint of its size, scaled to its mass")
DRIVER_FROM = "JointParts' driver board of its size, scaled to its joint's module mass; area likewise"
PACK_STATED = 'its cells, its management board (Boards) and its housing (the rows below)'
PACK_FROM_ENERGY = ('its cells, its management board (Boards) and its housing (the rows below); its mass the energy '
                    "over Constants' Battery pack, Wh per kg")
PACK_CELLS_ONLY = ("its cells, its management board (Boards) and no housing: the maker's pack is lighter than its "
                   'cells (E5.14 point 3)')
CELLS_FROM_CHARGE = "from the energy: Constants voltage × capacity over the NMC cell's Wh/kg"
CELLS_FROM_MASS = ("from the energy: Constants' Battery energy per kg of robot times the robot's mass, over the NMC "
                   "cell's Wh/kg")
HOUSING = 'the battery pack, less its cells and its management board'
SHELL = "a share of the robot's mass: Constants' Shell, share of the robot mass"
FRAME = 'the robot (Constants), less every other part'
MAGNETS_BASIS = 'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'
# The housing of a battery pack: its shares in the sheet Shares, the housing aluminium or plastics (each as often), or
# aluminium where the maker says so (the PM01).
HOUSING_MIXED = 'Battery housing, busbars and wires'
HOUSING_ALUMINIUM = 'Battery housing (aluminium), busbars and wires'
# The joints of a robot whose sources give no joint torques (E5.17 point 1): AVERAGE in its block.
AVERAGE = 'as batch 1 on average'


def spread(mode: float, low: float = 1 - STATED_SPREAD, high: float = 1 + STATED_SPREAD) -> tuple:
    """Min, mode and max: `low` and `high` times the mode, rounded to four decimals. By default ± 5 %, a figure stated
    once."""
    return round(low * mode, 4), round(mode, 4), round(high * mode, 4)


def estimate(mode: float) -> tuple:
    """An estimate (E): half to 1.5 times its mode (Matthias, 2026-10-27: "Estimates should be larger than known
    numbers")."""
    return spread(mode, 0.5, 1.5)


def from_torque(torque: float) -> tuple:
    """An actuator's mass, kg, from its peak torque where no source states its mass (E5.12 point 4)."""
    return estimate(torque / TORQUE_DENSITY)


def size_of(torque: float) -> str:
    """A joint's class by its actuator's peak torque (E5.12 point 1)."""
    return 'large' if torque >= LARGE_FROM_NM else 'small'


def joint(name: str, count: int, torque: float | None, masses: tuple, heat_group: str, region: str,
          size: str | None = None) -> tuple:
    """One joint kind of a block: its name, joints, class (by its torque, or `size` where no torque is stated), torque
    (N·m), module mass (kg), heat group and body region."""
    return name, count, size or size_of(torque), torque, masses, heat_group, region


# The actuators whose masses their makers state (E5.11), and the class of each.
DM_J10010L = spread(1.375)        # DAMIAO DM-J10010L-2EC, 1375 g, 120 N·m (DM1 p. 20)
DM_J4340P = spread(0.375)         # DAMIAO DM-J4340P-2EC, 375 g, 27 N·m (DM1 p. 13)
RMM10062 = (1.197, 1.197, 1.26)   # RoboParty RMM10062-2E: 1197 g measured, < 1260 g on its drawing (RP1c), 160 N·m
RMM8463 = (0.35, 0.7, 0.8)        # RoboParty RMM8463-2E: "< 800 g" (its drawing), E at least half (E5.12 point 3), 87
RMM6562 = (0.53, 0.5331, 0.5331)  # RoboParty RMM6562-2E: 533.1 g measured, ≤ 530 g on its drawing (RP1c), 35 N·m
Q90H = spread(1.1)                # EngineAI Q90H, 1.1 kg, 145 N·m (PM1)
Q25H = spread(0.5)                # EngineAI Q25H, 0.5 kg, 50 N·m (PM1)
Q25H_L = estimate(0.5)            # EngineAI Q25H-L: no data; as the Q25H, half to 1.5 times (E5.12 point 4)
QC080 = (0.845, 0.845, 0.865)     # ROBOTIS QC080-240-R020-RE: 845 g (AK1), 865 g (AK2), 72.6 N·m
QC060 = (0.435, 0.435, 0.455)     # ROBOTIS QC060-200-R020-RE: 435 g (AK1), 455 g (AK2), 30 N·m
QM080 = spread(0.85)              # ROBOTIS QM-080, 850 g (K0a); no torque stated
QM060 = spread(0.45)              # ROBOTIS QM-060, 450 g (K0a); no torque stated


def block(name: str, maker: str, height: float, stated: float | None, sources: str, mass: tuple, joints,
          **more) -> dict:
    """One robot's block: what its sheet Robots row says (`maker`, `height` m, `stated` mass kg, `sources`), its mass
    for the sheet Constants (`mass`: (min, mode, max), label, source), its joints (joint() each, or AVERAGE), and in
    `more` what differs from the template (E5.14): voltage and capacity ((min, mode, max), label, source; none: the
    energy per kg of robot), pack ((min, mode, max), label, source; None: from its energy; PACK_CELLS_ONLY), housing,
    boards, sensors, cables, screws, parts, cooler (ARM_COOLER unless its computer is an Intel or AMD processor's),
    shell, frame, and the labels and sources of its joints, connectors, encoders and cells."""
    b = dict(name=name, maker=maker, height=height, stated=stated, sources=sources, mass=mass, joints=joints,
             joints_stated=None, joint_label={'small': 'E', 'large': 'E'}, joint_sources='', voltage=None,
             capacity=None, pack=None, pack_source='', housing=HOUSING_MIXED,
             cells=('E', 'NMC cylindrical, E (E5.14 point 2)'),
             boards=[], sensors=[], cables=(CABLES_M, 'E', 'as the N1 (E5.14 point 5)'),
             connectors=('E', 'two per joint, as type 1 (E5.14 point 5)'),
             encoders=('E', 'two per joint, as type 1 (E5.14)'),
             screws=[('Screws', 1, SCREWS_KG, '42CrMo4', 'E', 'as the G1 (E5.14 point 7); grade E5.18')],
             parts=[], cooler=ARM_COOLER, shell=('Shell: plastics', 'not stated; plastics as type 1 (E5.14 point 6)'),
             frame=('Frame', 'Aluminium', 'not stated; aluminium as type 1 (E5.14 point 9)'))
    b.update(more)
    return b


def catalogue_block(name: str, maker: str, height: float, stated: float | None, mass: tuple, joints_stated: int,
                    computer: str, **more) -> dict:
    """A robot of batches 2 to 4 that gives no joint torques (E5.17): its joints a share of its mass, split as batch
    1's are on average (point 1); its battery 12 Wh per kg of robot unless a voltage or capacity is given (point 2); a
    computer board as the template's (point 3), named as its sources name it; the rest as E5.14 (point 4)."""
    defaults = dict(joints_stated=joints_stated,
                    boards=[(computer, 1, 'Torso boards', 'Torso', COMPUTER, 'ITC', 'E',
                             'HG; as the X1\'s and N1\'s computer boards (E5.17 point 3)'),
                            ('Power distribution board', 1, 'Torso boards', 'Torso', POWER, 'PE_HVS', 'E',
                             'as the G1 (E5.14 point 4)')],
                    joint_sources=("no joint torques in its sources: its joint modules 24.5 / 49 / 73.5 % of its mass, "
                                   "split as batch 1's on average (E5.17 point 1)"))
    defaults.update(more)
    return block(name, maker, height, stated, defaults.pop('sources', 'HG (E5.15, E5.16)'), mass, AVERAGE, **defaults)


# --- Batch 1: the eight robots with the most published hardware (E5.1 to E5.14) ---------------------------------------
ROBOTO_ORIGIN = block(
    'RoboParty Roboto Origin', 'RoboParty', 1.25, 34, 'RO1 (its BOM), RO2 (its model, 33.757 kg); E5.1, E5.10',
    ((32.8, 33.8, 34.8), 'S, E', 'RO2: its model adds up to 33.757 kg; ± 1 kg, as the G1 (E5.14 point 1)'),
    [joint('Hip yaw', 2, 120, DM_J10010L, 'Hips', 'Legs'), joint('Hip roll', 2, 120, DM_J10010L, 'Hips', 'Legs'),
     joint('Hip pitch', 2, 120, DM_J10010L, 'Hips', 'Legs'), joint('Knee', 2, 120, DM_J10010L, 'Knees', 'Legs'),
     joint('Ankle pitch', 2, 27, DM_J4340P, 'Ankles', 'Legs'), joint('Ankle roll', 2, 27, DM_J4340P, 'Ankles', 'Legs'),
     joint('Waist (torso)', 1, 120, DM_J10010L, 'Waist', 'Torso'),
     joint('Shoulder pitch', 2, 27, DM_J4340P, 'Shoulders', 'Arms'),
     joint('Shoulder roll', 2, 27, DM_J4340P, 'Shoulders', 'Arms'),
     joint('Shoulder yaw', 2, 27, DM_J4340P, 'Shoulders', 'Arms'),
     joint('Elbow pitch', 2, 27, DM_J4340P, 'Elbows and wrists', 'Arms'),
     joint('Elbow yaw', 2, 27, DM_J4340P, 'Elbows and wrists', 'Arms')],
    joint_label={'small': 'S, E', 'large': 'S, E'},
    joint_sources=('RO1: 9 × DM 10010L, 14 × DM 4340P; RO2: their torque limits; DM1: 1375 and 375 g, ± 5 % (E5.12 '
                   'point 3)'),
    voltage=((48, 48, 48), 'S', 'RO1 "48V 15Ah Li-ion pack"'),
    capacity=(spread(15), 'S', 'RO1 "15Ah"; ± 5 % (E5.14 point 2)'),
    boards=[('Compute board, D-Robotics RDK X5 8 GB', 1, 'Torso boards', 'Torso', COMPUTER, 'ITC', 'E',
             "RO1; its size not found (E5.13): as the X1's and N1's computer boards"),
            ('USB hub board', 1, 'Torso boards', 'Torso', SMALL_BOARD, 'ITC', 'E', 'RO1'),
            ('USB-to-CAN boards', 4, 'Torso boards', 'Torso', SMALL_BOARD, 'ITC', 'E', 'RO1'),
            ('CAN adapter boards', 4, 'Torso boards', 'Torso', SMALL_BOARD, 'ITC', 'E', 'RO1'),
            ('DC-DC converter, 48 V to 5 V', 1, 'Torso boards', 'Torso', SMALL_BOARD, 'PE_HVS', 'E', 'RO1'),
            ('Power distribution board', 1, 'Torso boards', 'Torso', POWER, 'PE_HVS', 'E', 'RO1')],
    sensors=[('Motion sensor (IMU), Chaohe HI13', 1, 'Torso boards', 'Torso', IMU_G, 'E', 'RO1', [('IMU', 1)])],
    cables=((10, 10.5, 12), 'S, E', 'RO1: its motor cables listed add up to 10.0 m; up to 12 m for any not listed '
                                    '(E5.13, E5.14 point 5)'),
    shell=('Shell: 3D-printed parts and rubber soles', 'RO1; 11.5 % of the robot (E5.14 point 6)'),
    frame=('Frame', 'Aluminium', 'RO1: CNC parts with "black anodizing", aluminium\'s treatment; the metal not named '
                                 '(E5.14 point 9)'))

ASIMOV_ONE = block(
    'Menlo Asimov 1', 'Menlo', 1.2, 35, 'AS1, AS2 (Menlo); AS3 (its model, 35.552 kg); E5.2',
    ((34, 35, 36), 'S, E', 'AS1 "35 kg"; ± 1 kg, as the G1 (E5.14 point 1)'),
    [joint('Hip pitch', 2, 120, from_torque(120), 'Hips', 'Legs'),
     joint('Hip roll', 2, 90, from_torque(90), 'Hips', 'Legs'),
     joint('Hip yaw', 2, 60, from_torque(60), 'Hips', 'Legs'),
     joint('Knee', 2, 75, from_torque(75), 'Knees', 'Legs'),
     joint('Ankle actuator A (parallel ankle)', 2, 36, from_torque(36), 'Ankles', 'Legs'),
     joint('Ankle actuator B (parallel ankle)', 2, 36, from_torque(36), 'Ankles', 'Legs'),
     joint('Waist yaw', 1, 120, from_torque(120), 'Waist', 'Torso'),
     joint('Neck yaw', 1, 36, from_torque(36), 'Elbows and wrists', 'Head'),
     joint('Neck pitch', 1, 36, from_torque(36), 'Elbows and wrists', 'Head'),
     joint('Shoulder pitch', 2, 90, from_torque(90), 'Shoulders', 'Arms'),
     joint('Shoulder roll', 2, 75, from_torque(75), 'Shoulders', 'Arms'),
     joint('Shoulder yaw', 2, 60, from_torque(60), 'Shoulders', 'Arms'),
     joint('Elbow', 2, 36, from_torque(36), 'Elbows and wrists', 'Arms'),
     joint('Wrist yaw', 2, 36, from_torque(36), 'Elbows and wrists', 'Arms')],
    joint_sources=('AS1: the actuator at each joint and its peak torque (EC-A6416 120, EC-A5013 90, EC-A4315 75, '
                   'EC-A3814 60, EC-A4310 36 N·m); mass the torque over 87.3 N·m/kg, half to 1.5 times (E5.12 point '
                   '4)'),
    voltage=((46.8, 46.8, 46.8), 'S', 'AS2 "13S4P", 46.8 V'),
    capacity=(spread(10.5), 'S', 'AS2 10.5 Ah; ± 5 % (E5.14 point 2)'),
    pack=PACK_CELLS_ONLY, housing=None,
    pack_source=('AS2 "Approximately 2 kg", less than its 52 cells (E5.13): its cells kept, its housing none (E5.14 '
                 'point 3)'),
    boards=[('Compute module, Radxa CM5', 1, 'Torso boards', 'Torso', RADXA_CM5, 'ITC', 'S',
             'AS2; 55 × 40 mm (search results, E5.13), ± 5 %'),
            ('Carrier board of the Radxa CM5 (motion control)', 1, 'Torso boards', 'Torso', COMPUTER, 'ITC', 'E',
             "AS2; as the X1's and N1's computer boards (E5.14 point 4)"),
            ('Raspberry Pi 5', 1, 'Torso boards', 'Torso', COMPUTER, 'ITC', 'E', 'AS2; its size not found (E5.13)'),
            ('Media HAT of the Raspberry Pi 5', 1, 'Torso boards', 'Torso', SMALL_BOARD, 'ITC', 'E', 'AS2'),
            ('Head board', 1, 'Head', 'Head', SMALL_BOARD, 'VCC', 'E', "AS2; as the G1's head control board"),
            ('Power distribution board', 1, 'Torso boards', 'Torso', POWER, 'PE_HVS', 'E', 'AS2')],
    sensors=[('Motion sensor (IMU), 6-axis', 1, 'Torso boards', 'Torso', IMU_G, 'E', 'AS2', [('IMU', 1)]),
             ('Camera, 2 MP', 1, 'Head', 'Head', None, 'S', 'AS2; its mass not stated: its elements only', CAMERA),
             ('Microphone array (4 microphones)', 1, 'Head', 'Head', MICROPHONES_G, 'E',
              "AS2 \"microphones\", their number not stated: as the G1's four", MICROPHONES),
             ('Speaker, 10 W', 1, 'Head', 'Head', SPEAKER_G, 'E', "AS2; as the G1's 5 W speaker", [])],
    connectors=('S, E', 'AS1: XT30 (2+2) at every actuator (E5.13); their mass as the G1\'s (E)'),
    shell=('Shell: MJF PA12 nylon', 'AS1 "7075 aluminum and MJF PA12 nylon"; 11.5 % of the robot (E5.14 point 6)'),
    frame=('Frame', 'Aluminium', 'AS1 "7075 aluminum"'))

RP1 = block(
    'RoboParty RP1', 'RoboParty', 1.35, 39, 'RP1a (its BOM), RP1b, RP1c (its actuators), RP1d, RP1e (its model, '
                                            '39.109 kg); E5.3, E5.10, E5.11',
    ((38.1, 39.1, 40.1), 'S, E', 'RP1e: its model adds up to 39.109 kg; ± 1 kg (E5.14 point 1); RP1d "about 39 kg"'),
    [joint('Hip pitch', 2, 160, RMM10062, 'Hips', 'Legs'), joint('Hip roll', 2, 160, RMM10062, 'Hips', 'Legs'),
     joint('Hip yaw', 2, 160, RMM10062, 'Hips', 'Legs'), joint('Knee', 2, 160, RMM10062, 'Knees', 'Legs'),
     joint('Ankle pitch', 2, 35, RMM6562, 'Ankles', 'Legs'), joint('Ankle roll', 2, 35, RMM6562, 'Ankles', 'Legs'),
     joint('Waist roll', 1, 87, RMM8463, 'Waist', 'Torso'), joint('Waist yaw', 1, 87, RMM8463, 'Waist', 'Torso'),
     joint('Shoulder pitch', 2, 87, RMM8463, 'Shoulders', 'Arms'),
     joint('Shoulder roll', 2, 35, RMM6562, 'Shoulders', 'Arms'),
     joint('Shoulder yaw', 2, 35, RMM6562, 'Shoulders', 'Arms'),
     joint('Elbow', 2, 35, RMM6562, 'Elbows and wrists', 'Arms'),
     joint('Wrist', 2, 35, RMM6562, 'Elbows and wrists', 'Arms')],
    joint_label={'small': 'S', 'large': 'S, E'},
    joint_sources=('RP1a: 12 × RMM6562-2E, 8 × RMM10062-2E, 4 × RMM8463-2E; RP1b: which where (RMM10062 thighs, '
                   'knees, hips; RMM8463 shoulders, waist; RMM6562 arms, wrists, ankles); RP1c: their masses (E5.12 '
                   'point 3)'),
    voltage=((48, 48, 48), 'S', 'RP1d "48V main lithium battery" (third party)'),
    capacity=(spread(10), 'S', 'RP1d "10Ah" (third party), ± 5 %; its 30 V auxiliary battery a part of its own since '
                               '2026-10-29 (point 4)'),
    boards=[('Main board RBE-MAIN-RK3588S, with an Orange Pi CM5', 1, 'Torso boards', 'Torso', COMPUTER, 'ITC', 'E',
             "RP1a; as the X1's and N1's computer boards (E5.14 point 4)"),
            ('Main control wiring board', 1, 'Torso boards', 'Torso', SMALL_BOARD, 'ITC', 'E', 'RP1a'),
            ('IMU board RBE-SENS-IMU', 1, 'Torso boards', 'Torso', SMALL_BOARD, 'ITC', 'E', 'RP1a'),
            ('Fan power board RBE-PWR-FAN', 1, 'Torso boards', 'Torso', SMALL_BOARD, 'PE_HVS', 'E', 'RP1a'),
            ('Battery adapter board RBE-PWR-MINGMEI-BC', 1, 'Torso boards', 'Torso', SMALL_BOARD, 'PE_HVS', 'E',
             'RP1a'),
            ('Small-battery protection board RBE-PWR-HOTSWAP', 1, 'Torso boards', 'Torso', SMALL_BOARD, 'BMS', 'E',
             'RP1a'),
            ('Back interface board', 1, 'Torso boards', 'Torso', SMALL_BOARD, 'ITC', 'E', 'RP1a'),
            ('Flexible board (FPC)', 1, 'Torso boards', 'Torso', SMALL_BOARD, 'ITC', 'E', 'RP1a'),
            ('LED board', 1, 'Torso boards', 'Torso', SMALL_BOARD, 'ITC', 'E', 'RP1a'),
            ('Leg board YCL.E000057', 2, 'Cables', 'Legs', SMALL_BOARD, 'ITC', 'E',
             'RP1a (named "4"), one in each leg'),
            ('Capacitor board RBE-PWR-CAP', 2, 'Cables', 'Legs', (2, 5, 10), 'PE_HVS', 'E',
             "RP1a, one in each leg; as the G1's capacitor buffer boards")],
    sensors=[('Motion sensor (IMU), RBE-SENS-IMU', 1, 'Torso boards', 'Torso', IMU_G, 'E', 'RP1a', [('IMU', 1)])],
    cables=(CABLES_M, 'E', 'as the N1 (E5.14 point 5); its harness list (RP1_hardware, 03_Harness) not downloaded'),
    encoders=('S', 'RP1b: dual magnetic encoders inside each module'),
    screws=[('Screws, grade 12.9 (753)', 1, (0.241, 0.481, 0.722), '42CrMo4', 'E',
             'RP1a "12.9级"; E5.14 point 7: 0.26 / 0.52 / 0.78 kg for its about 850 screws, split by their number'),
            ('Pins and screws, 304 stainless (61)', 1, (0.0195, 0.039, 0.0585), 'Type 304', 'E',
             'RP1a "304"; E5.14 point 7, split by their number; grade E5.18')],
    parts=[('Brass parts (8)', 8, 'Frame and shell', 'Whole body', (0.005, 0.01, 0.02), 'Copper', 'Brass', 'E',
            'RP1a (8 brass parts); 5 / 10 / 20 g each (E5.19 point 3)'),
           ('Auxiliary battery cells (30 V)', 1, 'Battery pack', 'Torso', (0.12, 0.25, 0.5), 'Battery materials', None,
            'E', 'RP1a: two "小电池" (small batteries), no data; RP1d "30V auxiliary battery" (third party): 30 V × 1 '
                 "/ 2 / 4 Ah over the NMC cells' 241.5 Wh/kg, NMC as its main pack (2026-10-29, point 4)"),
           ('Bearings outside the actuators (9)', 9, 'Frame and shell', 'Whole body', estimate(round(0.8 / 21, 4)),
            'Steel', 'GCr15', 'E', "RP1a: 9 parts of bearing steel; each as the X1's on average, 0.8 kg over 21 "
                                   '(2026-10-29, point 4)'),
           ('Magnets in the covers, N52 (80)', 80, 'Frame and shell', 'Whole body', COVER_MAGNET, 'Magnets (NdFeB)',
            'N', 'S, E', 'RP1a: 80 × N52 NdFeB, 4 × 4 and 4 × 2 mm, how many of each not stated: each between the two, '
                         'about 7.5 g/cm3; its grade class N (2026-10-29, point 4)')],
    cooler=[(*COOLER_FAN[:8], 'RP1a (a main-board fan); as the G1\'s main board fan (E2.8e; 2026-10-29, point 4)'),
            ('Waist fan', 2, 'Waist', 'Torso', FAN_KG, None, None, 'E',
             "RP1a (two waist fans); as the G1's waist fan (E2.8e; 2026-10-29, point 4)"),
            ARM_SINK],
    shell=('Shell: ABS, PLA, PC, resin; PU, TPU, EPDM, EPP and EVA', 'RP1a; 11.5 % of the robot (E5.14 point 6)'),
    frame=('Frame: aluminium, with steel 45 and P20 parts', None,
           'RP1a: AL6061-T6 (76 CNC parts), AL7075, AL5052; steel 45 or AISI 1045 (24), P20 (4); its shares in the '
           'sheet Shares (E5.14 point 9)'))

BOOSTER_T1 = block(
    'Booster T1', 'Booster Robotics', 1.18, 30, 'BT1 (Booster), BT1u (its model, 31.738 kg); E5.4, E5.10',
    ((29, 30, 31.7), 'S, E', 'BT1 "About 30kg"; BT1u its model 31.738 kg the max; 1 kg below the min (E5.14 point 1)'),
    [joint('Head yaw', 1, 7, from_torque(7), 'Elbows and wrists', 'Head'),
     joint('Head pitch', 1, 7, from_torque(7), 'Elbows and wrists', 'Head'),
     joint('Shoulder pitch', 2, 38.3, from_torque(38.3), 'Shoulders', 'Arms'),
     joint('Shoulder roll', 2, 38.3, from_torque(38.3), 'Shoulders', 'Arms'),
     joint('Elbow pitch', 2, 38.3, from_torque(38.3), 'Elbows and wrists', 'Arms'),
     joint('Elbow yaw', 2, 38.3, from_torque(38.3), 'Elbows and wrists', 'Arms'),
     joint('Waist yaw', 1, 68, from_torque(68), 'Waist', 'Torso'),
     joint('Hip pitch', 2, 98.8, from_torque(98.8), 'Hips', 'Legs'),
     joint('Hip roll', 2, 68, from_torque(68), 'Hips', 'Legs'),
     joint('Hip yaw', 2, 68, from_torque(68), 'Hips', 'Legs'),
     joint('Knee', 2, 130.5, from_torque(130.5), 'Knees', 'Legs'),
     joint('Ankle pitch', 2, 73.1, from_torque(73.1), 'Ankles', 'Legs'),
     joint('Ankle roll', 2, 17.2, from_torque(17.2), 'Ankles', 'Legs')],
    joint_sources=('BT1: 23 joints; BT1u: their torque limits; mass the torque over 87.3 N·m/kg, half to 1.5 times '
                   '(E5.12 point 4)'),
    voltage=((24, 48, 72), 'E', 'not stated: as its sibling the K1 (BK1d "48V"), half to 1.5 times (E5.14 point 2)'),
    capacity=(spread(10.5), 'S', 'BT1b 10.5 Ah (third party); ± 5 %'),
    boards=[('Compute module, NVIDIA Jetson AGX Orin 32 GB', 1, 'Torso boards', 'Torso', AGX_ORIN, 'ITC', 'S',
             'BT1; 100 × 87 mm (search results, E5.13), ± 5 %'),
            ('Carrier board of the Jetson AGX Orin', 1, 'Torso boards', 'Torso', COMPUTER, 'ITC', 'E',
             "as the X1's and N1's computer boards (E5.14 point 4)"),
            ('Motion control board, Express-i7', 1, 'Torso boards', 'Torso', COMPUTER, 'ITC', 'E',
             'BT1; its size not found'),
            POWER_BOARD],
    cooler=[('Main board fan', 2, 'Torso boards', 'Torso', FAN_KG, None, None, 'E',
             "its two computers, a fan each: as the G1's main board fan (E2.8e; 2026-10-29, point 4)"),
            ARM_SINK, X86_SINK],
    sensors=[('Depth camera (not named)', 1, 'Head', 'Head', None, 'S',
              "BT1; its elements as the Intel RealSense D435's, its mass not stated: its elements only", DEPTH_CAMERA),
             ('Microphone array (4 microphones)', 1, 'Head', 'Head', MICROPHONES_G, 'E',
              'BT1 "microphone array"; as the G1\'s', MICROPHONES)],
    encoders=('S', 'BT1 "dual encoders"'))


def booster_k1(capacity_ah: float, version: str, computer: list) -> dict:
    """The Booster K1 in one of its two versions (E5.14 point 2; decision B: each drawn as often): its battery's
    capacity, its computer."""
    return block(
        f'Booster K1 {capacity_ah:g} Ah', 'Booster Robotics', 0.95, 19.5,
        f'BK1 (Booster; the {version}), BK1d, BK1u (its model, 19.666 kg); E5.5, E5.10',
        ((18.5, 19.5, 20.5), 'S, E', 'BK1 "About 19.5kg"; BK1u 19.666 kg; ± 1 kg (E5.14 point 1)'),
        [joint('Head yaw', 1, 6, from_torque(6), 'Elbows and wrists', 'Head'),
         joint('Head pitch', 1, 6, from_torque(6), 'Elbows and wrists', 'Head'),
         joint('Shoulder pitch', 2, 14, from_torque(14), 'Shoulders', 'Arms'),
         joint('Shoulder roll', 2, 14, from_torque(14), 'Shoulders', 'Arms'),
         joint('Elbow pitch', 2, 14, from_torque(14), 'Elbows and wrists', 'Arms'),
         joint('Elbow yaw', 2, 14, from_torque(14), 'Elbows and wrists', 'Arms'),
         joint('Hip pitch', 2, 68, from_torque(68), 'Hips', 'Legs'),
         joint('Hip roll', 2, 43, from_torque(43), 'Hips', 'Legs'),
         joint('Hip yaw', 2, 38.3, from_torque(38.3), 'Hips', 'Legs'),
         joint('Knee', 2, 112, from_torque(112), 'Knees', 'Legs'),
         joint('Ankle pitch', 2, 38.3, from_torque(38.3), 'Ankles', 'Legs'),
         joint('Ankle roll', 2, 38.3, from_torque(38.3), 'Ankles', 'Legs')],
        joint_sources=('BK1: 22 joints; BK1u: their torque limits; mass the torque over 87.3 N·m/kg, half to 1.5 '
                       'times (E5.12 point 4)'),
        voltage=((48, 48, 48), 'S', 'BK1d "48V" (a reseller\'s datasheet)'),
        capacity=(spread(capacity_ah), 'S', f'BK1: {capacity_ah:g} Ah, the {version}; ± 5 %'),
        boards=computer + [('Power distribution board', 1, 'Torso boards', 'Torso', POWER, 'PE_HVS', 'E',
                            'as the G1 (E5.14 point 4)')],
        sensors=[('Depth camera (not named)', 1, 'Head', 'Head', None, 'S',
                  "BK1 \"binocular depth camera\"; its elements as the Intel RealSense D435's, its mass not stated",
                  DEPTH_CAMERA),
                 ('Motion sensor (IMU), 9-axis', 1, 'Torso boards', 'Torso', IMU_G, 'E', 'BK1', [('IMU', 1)]),
                 ('Microphone array (4 microphones)', 1, 'Head', 'Head', MICROPHONES_G, 'E',
                  'BK1 "microphones"; as the G1\'s', MICROPHONES),
                 ('Speaker', 1, 'Head', 'Head', SPEAKER_G, 'E', "BK1; as the G1's", [])],
        cables=((3, 6, 10), 'E', 'as the G1, a smaller robot (E5.14 point 5)'),
        encoders=('S', 'BK1 "dual encoders"'))


BOOSTER_K1_5AH = booster_k1(5, 'Education and Professional versions', [
    ('Compute module, NVIDIA Jetson Orin NX 8 GB', 1, 'Torso boards', 'Torso', ORIN_NX, 'ITC', 'S',
     "BK1, the Education version's (the Professional's AGX Orin not drawn); 69.6 × 45 mm (search results, E5.13), "
     '± 5 %'),
    ('Carrier board of the Jetson Orin NX', 1, 'Torso boards', 'Torso', COMPUTER, 'ITC', 'E',
     "as the X1's and N1's computer boards (E5.14 point 4)")])
BOOSTER_K1_2AH = booster_k1(2, 'Geek version', [
    ('Computer board, Qualcomm QCS8550', 1, 'Torso boards', 'Torso', COMPUTER, 'ITC', 'E',
     "BK1 (an ARM processor); the QCS8550 by a reseller (E5.5); its size not found: as the X1's and N1's computer "
     'boards')])

PM01 = block(
    'EngineAI PM01', 'EngineAI', 1.388, 43, 'PM1 (its development guide), PM1m (its manual), PM1u (its model, 40.921 '
                                            'kg); E5.6, E5.10, E5.11',
    ((40, 43, 44.5), 'S',
     'PM1m "约43kg" with battery (its text "约 40kg"); its editions up to 44.5 kg (E5.14 point 1)'),
    [joint('Hip pitch', 2, 145, Q90H, 'Hips', 'Legs'), joint('Hip roll', 2, 145, Q90H, 'Hips', 'Legs'),
     joint('Hip yaw', 2, 50, Q25H_L, 'Hips', 'Legs'), joint('Knee', 2, 145, Q90H, 'Knees', 'Legs'),
     joint('Ankle pitch', 2, 50, Q25H, 'Ankles', 'Legs'), joint('Ankle roll', 2, 50, Q25H, 'Ankles', 'Legs'),
     joint('Waist yaw', 1, 50, Q25H_L, 'Waist', 'Torso'),
     joint('Shoulder pitch', 2, 50, Q25H, 'Shoulders', 'Arms'),
     joint('Shoulder roll', 2, 50, Q25H, 'Shoulders', 'Arms'),
     joint('Shoulder yaw', 2, 50, Q25H, 'Shoulders', 'Arms'),
     joint('Elbow pitch', 2, 50, Q25H, 'Elbows and wrists', 'Arms'),
     joint('Elbow yaw', 2, 50, Q25H, 'Elbows and wrists', 'Arms'),
     joint('Head yaw', 1, 50, Q25H, 'Elbows and wrists', 'Head')],
    joint_label={'small': 'S, E', 'large': 'S, E'},
    joint_sources=('PM1: Q90H 1.1 kg and 145 N·m, Q25H 0.5 kg and 50 N·m, ± 5 %; the Q25H-L (hip yaw, waist) as the '
                   'Q25H, half to 1.5 times (E5.12 points 3, 4)'),
    voltage=((46.8, 46.8, 46.8), 'S', 'PM1 "13S", 46.8 V'),
    capacity=(spread(10), 'S', 'PM1 "10Ah" nominal; ± 5 % (E5.14 point 2)'),
    cells=('S', 'PM1 "Ternary Lithium System" cylindrical cells; NMC cylindrical (E5.14 point 2)'),
    pack=((2.655, 2.95, 3.245), 'S', 'PM1 "Total System Mass ≈2.95kg"; ± 10 % for the "≈", as the G1\'s "~"'),
    housing=HOUSING_ALUMINIUM,
    boards=[('Compute module, NVIDIA Jetson Orin NX 16 GB', 1, 'Torso boards', 'Torso', ORIN_NX, 'ITC', 'S',
             'PM1; 69.6 × 45 mm (search results, E5.13), ± 5 %'),
            ('Carrier board of the Jetson Orin NX', 1, 'Torso boards', 'Torso', COMPUTER, 'ITC', 'E',
             "as the X1's and N1's computer boards (E5.14 point 4)"),
            ('Motion control unit "Nezha"', 1, 'Torso boards', 'Torso', COMPUTER, 'ITC', 'E',
             'PM1; its size not found'),
            POWER_BOARD],
    sensors=[('Depth camera, Intel RealSense D435i', 1, 'Head', 'Head', D435_G, 'S',
              'PM1; Intel D400 datasheet, D435 75 g (second-hand), as the G1', None),
             ('Camera in the waist', 1, 'Torso boards', 'Torso', None, 'S', 'PM1; its mass not stated: its elements '
                                                                            'only', CAMERA),
             ('Motion sensor, YIS320', 1, 'Torso boards', 'Torso', spread(7.7), 'S', 'PM1 (7.7 g); ± 5 %', None)],
    shell=('Shell: rubber and plastics', 'PM1m "航空铝合金和橡胶"; 11.5 % of the robot (E5.14 point 6)'),
    frame=('Frame', 'Aluminium', 'PM1 "Structural Material Aviation Aluminum"'))

UNITREE_R1 = block(
    'Unitree R1', 'Unitree', 1.23, 29, 'UR1 (Unitree), UR1u (its model, 29.138 kg), UR1b (its battery); E5.7, E5.10',
    ((28, 29, 30), 'S, E', 'UR1 "About 29kg" with battery; UR1u 29.138 kg; ± 1 kg (E5.14 point 1)'),
    [joint('Hip pitch', 2, 60, from_torque(60), 'Hips', 'Legs'),
     joint('Hip roll', 2, 60, from_torque(60), 'Hips', 'Legs'),
     joint('Hip yaw', 2, 60, from_torque(60), 'Hips', 'Legs'),
     joint('Knee', 2, 60, from_torque(60), 'Knees', 'Legs'),
     joint('Ankle pitch', 2, 50, from_torque(50), 'Ankles', 'Legs'),
     joint('Ankle roll', 2, 50, from_torque(50), 'Ankles', 'Legs'),
     joint('Waist roll', 1, 60, from_torque(60), 'Waist', 'Torso'),
     joint('Waist yaw', 1, 60, from_torque(60), 'Waist', 'Torso'),
     joint('Shoulder pitch', 2, 60, from_torque(60), 'Shoulders', 'Arms'),
     joint('Shoulder roll', 2, 60, from_torque(60), 'Shoulders', 'Arms'),
     joint('Shoulder yaw', 2, 33, from_torque(33), 'Shoulders', 'Arms'),
     joint('Elbow', 2, 33, from_torque(33), 'Elbows and wrists', 'Arms'),
     joint('Wrist roll', 2, 33, from_torque(33), 'Elbows and wrists', 'Arms'),
     joint('Head pitch', 1, 33, from_torque(33), 'Elbows and wrists', 'Head'),
     joint('Head yaw', 1, 0.86, from_torque(0.86), 'Elbows and wrists', 'Head')],
    joint_sources=('UR1: 26 joints, inner-rotor motors; UR1u: their torque limits; mass the torque over 87.3 N·m/kg, '
                   'half to 1.5 times (E5.12 point 4)'),
    voltage=((32.4, 33.12, 33.12), 'S', 'UR1b: 33.12 V ("according to Unitree") or 32.4 V (third party)'),
    capacity=(spread(6), 'S', 'UR1b 6000 mAh (third party); ± 5 %'),
    boards=[('Computer board, 8-core processor', 1, 'Torso boards', 'Torso', COMPUTER, 'ITC', 'E',
             'UR1 "8-Core High-Performance Processor"; its size not found'),
            POWER_BOARD],
    sensors=[('Camera, binocular (two image sensors)', 1, 'Head', 'Head', None, 'S',
              'UR1; its mass not stated: its elements only', [('CMOS image sensor', 2)]),
             ('Microphone array (4 microphones)', 1, 'Head', 'Head', MICROPHONES_G, 'E',
              'UR1 "4 microphones"; their mass as the G1\'s', MICROPHONES),
             ('Speaker', 1, 'Head', 'Head', SPEAKER_G, 'E', "UR1; as the G1's", [])])

AI_SAPIENS_K1 = block(
    'ROBOTIS AI Sapiens K1', 'ROBOTIS', 1.355, 35, 'AK1, AK2 (ROBOTIS); E5.8, E5.11',
    ((34, 35, 36), 'S, E', 'AK1 "Weight 35 kg"; the K0\'s 34 kg; ± 1 kg (E5.14 point 1)'),
    [joint('Hip pitch', 2, 72.6, QC080, 'Hips', 'Legs'), joint('Hip roll', 2, 72.6, QC080, 'Hips', 'Legs'),
     joint('Hip yaw', 2, 72.6, QC080, 'Hips', 'Legs'), joint('Knee', 2, 72.6, QC080, 'Knees', 'Legs'),
     joint('Ankle pitch', 2, 72.6, QC080, 'Ankles', 'Legs'), joint('Ankle roll', 2, 30, QC060, 'Ankles', 'Legs'),
     joint('Waist yaw', 1, 72.6, QC080, 'Waist', 'Torso'),
     joint('Shoulder pitch', 2, 30, QC060, 'Shoulders', 'Arms'),
     joint('Shoulder roll', 2, 30, QC060, 'Shoulders', 'Arms'),
     joint('Shoulder yaw', 2, 30, QC060, 'Shoulders', 'Arms'),
     joint('Elbow', 2, 30, QC060, 'Elbows and wrists', 'Arms'),
     joint('Wrist', 2, 30, QC060, 'Elbows and wrists', 'Arms')],
    joint_label={'small': 'S, E', 'large': 'S, E'},
    joint_sources=('AK1: 11 × QC080 (845 g; AK2 865 g), 12 × QC060 (435 g; AK2 455 g); legs 6, arms 5, waist 1; '
                   'which actuator at which joint not stated: the 11 larger at the hips, knees, waist and ankle pitch '
                   '(E, the joints of the larger loads, as in the Booster T1\'s model)'),
    voltage=((48, 48, 48), 'S', 'AK1 "48 V", 13S2P (its "460.8 Wh" does not add up, E5.8)'),
    capacity=(spread(10), 'S', 'AK1 "10 Ah"; ± 5 % (E5.14 point 2)'),
    cells=('S', 'AK1: LG Energy Solution M50LT, NCM; NMC cylindrical (E5.14 point 2)'),
    boards=[('Compute module, NVIDIA Jetson Orin NX 16 GB', 1, 'Torso boards', 'Torso', ORIN_NX, 'ITC', 'S',
             'AK1; 69.6 × 45 mm (search results, E5.13), ± 5 %'),
            ('Carrier board of the Jetson Orin NX', 1, 'Torso boards', 'Torso', COMPUTER, 'ITC', 'E',
             "as the X1's and N1's computer boards (E5.14 point 4)"),
            ('HAT board (two STM32)', 1, 'Torso boards', 'Torso', SMALL_BOARD, 'ITC', 'E', 'AK1'),
            ('IMU board', 1, 'Torso boards', 'Torso', SMALL_BOARD, 'ITC', 'E', 'AK1'),
            POWER_BOARD],
    sensors=[('Motion sensor (IMU), ICM-42688-P or BNO085', 1, 'Torso boards', 'Torso', IMU_G, 'E', 'AK1',
              [('IMU', 1)])],
    connectors=('S, E', 'ROBOTIS: XT30 (2+2) at every actuator (E5.13); their mass as the G1\'s (E)'),
    shell=('Shell: polymer covers', 'AK1 (covers 3D-printable); 11.5 % of the robot (E5.14 point 6)'),
    frame=('Frame', 'Aluminium', 'HG "Aluminium alloy frame" (third party)'))

# --- Batches 2 to 4: the other robots of type 1 (E5.15 to E5.17) ------------------------------------------------------
BOOSTER_T2 = catalogue_block(
    'Booster T2', 'Booster Robotics', 1.4, 42,
    ((41, 42, 44), 'S, E', 'BT2 "~42 kg" (Education, Pro), "~43 kg" (with grippers or hands); ± 1 kg (E5.14 point 1)'),
    31, 'Computer board (Education: an ARM board; Pro: NVIDIA Jetson Thor T5000)',
    sources='BT2 (Booster); E5.15',
    voltage=((48, 48, 48), 'S', 'BT2 "48V"'), capacity=(spread(10), 'S', 'BT2 "10Ah"; ± 5 %'),
    sensors=[('Depth camera (not named)', 2, 'Head', 'Head', None, 'S',
              "BT2: RGB-D cameras in the head and the waist; elements as the Intel RealSense D435's, mass not stated",
              DEPTH_CAMERA),
             ('Camera in the wrist (not named)', 2, 'Arms', 'Arms', None, 'S', 'BT2; its mass not stated: its elements '
                                                                            'only', CAMERA)])

MENLO_ASIMOV_2 = 'Menlo Asimov 2'      # written from the Asimov 1's rows, scaled to its mass (asimov_two_rows())
ASIMOV_TWO_MASS = ((37, 38, 39), 'S, E', 'HG: 38 kg, the catalogue\'s "educated estimate" (Menlo: "In progress"); ± '
                                         '1 kg (E5.17 point 7)')

NOETIX_E1 = catalogue_block(
    'Noetix E1', 'Noetix Robotics', 1.36, 40, ((39, 40, 41), 'S', 'HG "40 kg" ("Not Verified"); ± 1 kg'),
    26, 'Computer board, NVIDIA Jetson Orin Nano Super (development)',
    joint_sources=("HG: 23 to 28 joints, 26 for the encoders and connectors (E, the middle); no joint torques: its "
                   "joint modules 24.5 / 49 / 73.5 % of its mass, split as batch 1's on average (E5.17 point 1)"))
NOETIX_BUMI = catalogue_block(
    'Noetix Bumi', 'Noetix Robotics', 0.98, 17, ((16, 17, 18), 'S', 'HG "17 kg" ("Not Verified"); ± 1 kg'),
    21, 'Computer board, Rockchip RK3576',
    shell=('Shell: composite materials', 'HG "Composite materials", its kind not named: plastics as type 1; 11.5 % of '
                                         'the robot (E5.14 point 6)'))
AKINCI_5 = catalogue_block(
    'AKINROBOTICS AKINCI-5', 'AKINROBOTICS', 1.29, 42, ((41, 42, 43), 'S', 'HG "42 kg" ("Not Verified"); ± 1 kg'),
    19, 'Computer board, AMD Ryzen 9 PRO 6950H', cooler=X86_COOLER,
    shell=('Shell: composites',
           'HG "Aluminum alloy + composites", the composites\' kind not named: plastics as type 1; 11.5 % of the robot '
           '(E5.14 point 6)'),
    frame=('Frame', 'Aluminium', 'HG "Aluminum alloy"'))
JAKA_PI = catalogue_block(
    'JAKA π', 'JAKA Robotics', 1.22, 42, ((41, 42, 43), 'S', 'HG "42 kg" ("Not Verified"); ± 1 kg'),
    27, 'Computer board, Intel Core Ultra 7 255H', cooler=X86_COOLER,
    voltage=((48, 48, 48), 'S', 'HG "48-volt pack"'),
    capacity=(estimate(10.5), 'E', '12 Wh per kg of robot at 42 kg, over 48 V (E5.17 point 2)'),
    shell=('Shell: soft-touch polymer covers', 'HG; 11.5 % of the robot (E5.14 point 6)'),
    frame=('Frame', 'Aluminium', 'HG "Aluminum frame"'))
ROBOTIS_K0 = block(
    'ROBOTIS K0', 'ROBOTIS', 1.3, 34, 'K0a (ROBOTIS); E5.15',
    ((33, 34, 35), 'S, E', 'K0a "34 kg"; ± 1 kg (E5.14 point 1)'),
    [joint('Hip pitch', 2, None, QM080, 'Hips', 'Legs', 'large'),
     joint('Hip roll', 2, None, QM080, 'Hips', 'Legs', 'large'),
     joint('Hip yaw', 2, None, QM080, 'Hips', 'Legs', 'large'), joint('Knee', 2, None, QM080, 'Knees', 'Legs', 'large'),
     joint('Waist', 1, None, QM080, 'Waist', 'Torso', 'large'),
     joint('Ankle pitch', 2, None, QM060, 'Ankles', 'Legs', 'small'),
     joint('Ankle roll', 2, None, QM060, 'Ankles', 'Legs', 'small'),
     joint('Shoulder pitch', 2, None, QM060, 'Shoulders', 'Arms', 'small'),
     joint('Shoulder roll', 2, None, QM060, 'Shoulders', 'Arms', 'small'),
     joint('Shoulder yaw', 2, None, QM060, 'Shoulders', 'Arms', 'small'),
     joint('Elbow', 2, None, QM060, 'Elbows and wrists', 'Arms', 'small'),
     joint('Wrist', 2, None, QM060, 'Elbows and wrists', 'Arms', 'small')],
    joint_label={'small': 'S, E', 'large': 'S, E'},
    joint_sources=('K0a: 9 × QM-080 (850 g), 14 × QM-060 (450 g), ± 5 %, no torques (their class by their size, as '
                   'the QC080 and QC060); which actuator at which joint not stated: the 9 larger at the hips, knees '
                   'and waist (E, the layout of the G1\'s and the Roboto Origin\'s 9 large and 14 small joints)'),
    voltage=((46.8, 46.8, 46.8), 'S', 'K0a "46.8V"'), capacity=(spread(9), 'S', 'K0a "9Ah"; ± 5 %'),
    boards=[('Compute module, NVIDIA Jetson Orin NX 16 GB', 1, 'Torso boards', 'Torso', ORIN_NX, 'ITC', 'S',
             'K0a; 69.6 × 45 mm (search results, E5.13), ± 5 %'),
            ('Carrier board of the Jetson Orin NX', 1, 'Torso boards', 'Torso', COMPUTER, 'ITC', 'E',
             "as the X1's and N1's computer boards (E5.14 point 4)"),
            POWER_BOARD])
LIGHTBOT_0 = catalogue_block(
    'Light Origins LightBot-0', 'Light Origins', 0.9, 35, ((34, 35, 36), 'S', 'HG "35 kg" ("Not Verified"); ± 1 kg'),
    24, 'Computer board (not named)',
    joint_sources=("no joint count in its sources: 24 for the encoders and connectors (E, the median of type 1's "
                   "stated counts); no joint torques: its joint modules 24.5 / 49 / 73.5 % of its mass, split as batch "
                   "1's on average (E5.17 point 1)"),
    sensors=[('Depth camera (not named)', 1, 'Head', 'Head', None, 'S',
              "HG; its elements as the Intel RealSense D435's, its mass not stated", DEPTH_CAMERA)])
DOBOT_LUMO = catalogue_block(
    'DOBOT LUMO', 'DOBOT Robotics', 1.3, 35, ((34, 35, 36), 'S', 'HG "35 kg" ("Not Verified"); ± 1 kg'),
    24, 'Computer board (not named)',
    joint_sources=("no joint count in its sources: 24 for the encoders and connectors (E, the median of type 1's "
                   "stated counts); no joint torques: its joint modules 24.5 / 49 / 73.5 % of its mass, split as batch "
                   "1's on average (E5.17 point 1)"),
    shell=('Shell: plastic', 'HG "Aluminum alloy and plastic"; 11.5 % of the robot (E5.14 point 6)'),
    frame=('Frame', 'Aluminium', 'HG "Aluminum alloy"'))
NORI_L3 = catalogue_block(
    'Nori L3', 'Nori Robotics', 1.45, 40, ((39, 40, 41), 'S', 'HG "40 kg" ("Not Verified"); ± 1 kg'),
    20, 'Computer board (not named)',
    sensors=[('Camera, 720p (not named)', 4, 'Head', 'Head', None, 'S', 'HG: four 720p cameras; their mass not '
                                                                        'stated: their elements only', CAMERA)],
    shell=('Shell: engineering plastics', 'HG "Aluminum alloy with engineering plastics"; 11.5 % of the robot'),
    frame=('Frame', 'Aluminium', 'HG "Aluminum alloy"'))
PHYBOT_C1 = catalogue_block(
    'PHYBOT C1', 'PHYBOT', 1.25, 25, ((24, 25, 26), 'S', 'HG "25 kg" ("Not Verified"); ± 1 kg'),
    28, 'Computer board (not named)',
    sensors=[('Camera (not named)', 1, 'Head', 'Head', None, 'S', 'HG "RGB"; its mass not stated: its elements only',
              CAMERA),
             ('Depth camera (not named)', 1, 'Head', 'Head', None, 'S',
              "HG; its elements as the Intel RealSense D435's, its mass not stated", DEPTH_CAMERA)],
    shell=('Shell: composite polymer', 'HG "Composite polymer + aluminum frame"; 11.5 % of the robot'),
    frame=('Frame', 'Aluminium', 'HG "aluminum frame"'))
PRIMEBOT_Q1 = catalogue_block(
    'PrimeBOT Q1', 'PrimeBOT', 0.88, None, ((9.75, 19.5, 29.25), 'E',
                                             'no mass in any source: the Booster K1\'s 19.5 kg (0.95 m, the robot '
                                             'nearest in height with a mass from its maker), half to 1.5 times (E5.17 '
                                             'point 6)'),
    22, 'Computer board (not named)')
QUESTER1 = catalogue_block(
    'AgiBot QUESTER1', 'AgiBot', 0.79, 25, ((20, 25, 30), 'S', 'HG "~20–30 kg" ("Not Verified")'),
    28, 'Computer board (not named)',
    joint_sources=("HG: about 24 to 32 joints, 28 for the encoders and connectors (E, the middle); no joint torques: "
                   "its joint modules 24.5 / 49 / 73.5 % of its mass, split as batch 1's on average (E5.17 point 1)"),
    shell=('Shell: plastic composites', 'HG "Aluminum + plastic composites"; 11.5 % of the robot'),
    frame=('Frame', 'Aluminium', 'HG "Aluminum"'))
LEJU_ROBAN2 = catalogue_block(
    'Leju Roban2', 'Leju Robot', 1.45, 40, ((39, 40, 41), 'S', 'HG "40 kg" ("Not verified"); ± 1 kg'),
    40, 'Computer board (not named)',
    shell=('Shell: ABS composite', 'HG "Aluminum alloy + ABS composite shells"; 11.5 % of the robot'),
    frame=('Frame', 'Aluminium', 'HG "Aluminum alloy"'))
FAUNA_SPROUT = catalogue_block(
    'Fauna Sprout', 'Fauna Robotics', 1.07, 22.7, ((21.7, 22.7, 23.7), 'S', 'SP1 "22.7 kg"; ± 1 kg'),
    29, 'Carrier board of the Jetson AGX Orin',
    sources='SP1 (Fauna Robotics); E5.16',
    joint_sources=("SP1: 29 joints (neck 2, arms 6, grippers 1, legs 5 each); no joint torques: its joint modules "
                   "24.5 / 49 / 73.5 % of its mass, split as batch 1's on average (E5.17 point 1)"),
    boards=[('Compute module, NVIDIA Jetson AGX Orin 64 GB', 1, 'Torso boards', 'Torso', AGX_ORIN, 'ITC', 'S',
             'SP1; 100 × 87 mm (search results, E5.13), ± 5 %'),
            ('Carrier board of the Jetson AGX Orin', 1, 'Torso boards', 'Torso', COMPUTER, 'ITC', 'E',
             "as the X1's and N1's computer boards (E5.17 point 3)"),
            POWER_BOARD],
    sensors=[('Stereo camera, ZED 2i (two image sensors)', 1, 'Head', 'Head', None, 'S',
              'SP1; its mass not read: its elements only', [('CMOS image sensor', 2)]),
             ('Motion sensor (IMU), not named', 1, 'Torso boards', 'Torso', IMU_G, 'E', 'SP1', [('IMU', 1)]),
             ('Microphone array (4 microphones)', 1, 'Head', 'Head', MICROPHONES_G, 'E', 'SP1 "microphones"; as the '
                                                                                        "G1's", MICROPHONES),
             ('Time-of-flight sensor', 4, 'Head', 'Head', (5, 10, 20), 'E',
              'SP1 "4 time-of-flight sensors"; no such type in the car sensor file: the elements of the LiDAR\'s laser '
              'diode array and photodetector array; 5 / 10 / 20 g each (2026-10-29, point 4)',
              [('laser diode array', 1), ('photodetector array', 1)])],
    shell=('Shell: soft exterior', 'SP1 "soft exterior"; plastics as type 1; 11.5 % of the robot (E5.14 point 6)'),
    frame=('Frame', 'Aluminium', 'HG (aluminium, third party)'))
STARBOT_ASTRA = catalogue_block(
    'StarBot Astra', 'StarBot USA', 1.52, 34, ((33, 34, 35), 'S', 'SA1 "75 lb"; ± 1 kg'),
    23, 'Computer board, NVIDIA Jetson Orin class',
    sources='SA1 (StarBot), HG; E5.16',
    joint_sources=("SA1: 23 joints; no joint torques: its joint modules 24.5 / 49 / 73.5 % of its mass, split as "
                   "batch 1's on average (E5.17 point 1)"),
    voltage=((48, 48, 48), 'S', 'SA1 "48 V"'),
    capacity=(estimate(8.5), 'E', '12 Wh per kg of robot at 34 kg, over 48 V (E5.17 point 2)'))
TOTAN_O1 = catalogue_block(
    'WL Robotics Totan O1', 'WL Robotics', 1.34, 34, ((33, 34, 35), 'S', 'HG "34 kg" ("Not Verified"); ± 1 kg'),
    30, 'Computer board (not named)',
    shell=('Shell: composite panels', 'HG "Aluminum alloy frame with composite panels", their kind not named: plastics '
                                      'as type 1; 11.5 % of the robot'),
    frame=('Frame', 'Aluminium', 'HG "Aluminum alloy frame"'))
XIAO_TUO = catalogue_block(
    'TOPSTAR Xiao Tuo', 'TOPSTAR Group', 1.2, 40, ((39, 40, 41), 'S', 'HG "40 kg" ("Not Verified"); ± 1 kg'),
    30, 'Computer board (not named)',
    sensors=[('Camera (not named)', 1, 'Head', 'Head', None, 'S', 'HG "RGB"; its mass not stated: its elements only',
              CAMERA),
             ('LiDAR, 3D (not named)', 1, 'Head', 'Head', None, 'S',
              "HG; its elements as the Livox Mid-360's, its mass not stated", LIDAR)],
    shell=('Shell: plastic composites', 'HG "Aluminum + plastic composites"; 11.5 % of the robot'),
    frame=('Frame', 'Aluminium', 'HG "Aluminum"'))
YMBOT_E3 = catalogue_block(
    'YMBOT E3', 'Yunmu', 1.4, 35, ((34, 35, 36), 'S', 'HG "35 kg" ("Not Verified"); ± 1 kg'),
    24, 'Computer board, Intel 12th-generation Core i9 class', cooler=X86_COOLER,
    joint_sources=("no joint count in its sources: 24 for the encoders and connectors (E, the median of type 1's "
                   "stated counts); no joint torques: its joint modules 24.5 / 49 / 73.5 % of its mass, split as batch "
                   "1's on average (E5.17 point 1)"))

# Batch 1, whose joints give the split of the others' (E5.17 point 1): the K1 once, its two versions having the same
# joints.
BATCH_ONE = [ROBOTO_ORIGIN, ASIMOV_ONE, RP1, BOOSTER_T1, BOOSTER_K1_5AH, PM01, UNITREE_R1, AI_SAPIENS_K1]


def joint_group(j: tuple) -> tuple:
    """The group of a joint for the average split: its name in the sheet Joints, heat group and body region."""
    if j[6] == 'Head':
        return 'Head joints', 'Elbows and wrists', 'Head'
    return {'Hips': ('Hip joints', 'Hips', 'Legs'), 'Knees': ('Knee joints', 'Knees', 'Legs'),
            'Ankles': ('Ankle joints', 'Ankles', 'Legs'), 'Waist': ('Waist joints', 'Waist', 'Torso'),
            'Shoulders': ('Shoulder joints', 'Shoulders', 'Arms'),
            'Elbows and wrists': ('Elbow and wrist joints', 'Elbows and wrists', 'Arms')}[j[5]]


def average_joints(blocks: list) -> list:
    """The joints of a robot whose sources give no joint torques (E5.17 point 1: "split into small and large joints as
    batch 1's are on average"): for each group of joints (hips, knees, ankles, waist, shoulders, elbows and wrists,
    head) and class, its share of the joint modules' mass at the modes, averaged over the robots of batch 1; one row
    each, the joints of the group and class together. The shares add up to 1, as each robot's do; nothing is
    rescaled."""
    shares: dict = {}
    for b in blocks:
        total = sum(j[1] * j[4][1] for j in b['joints'])
        for j in b['joints']:
            key = joint_group(j) + (j[2],)
            shares[key] = shares.get(key, 0) + j[1] * j[4][1] / total / len(blocks)
    order = ['Hip joints', 'Knee joints', 'Ankle joints', 'Waist joints', 'Shoulder joints', 'Elbow and wrist joints',
             'Head joints']
    return [(f'{name}, {size} ({AVERAGE})', 1, size, None, None, heat, region, share)
            for (name, heat, region, size), share in sorted(shares.items(), key=lambda kv: (order.index(kv[0][0]),
                                                                                          kv[0][3] == 'large'))]


AVERAGE_JOINTS = average_joints(BATCH_ONE)


def regions(joints: list) -> str:
    """The body regions of joints with their numbers, as the sheet Parts writes them ('Legs 12, Torso 1, Arms 10')."""
    counts: dict = {}
    for j in joints:
        counts[j[6]] = counts.get(j[6], 0) + j[1]
    return ', '.join(f'{region} {n}' for region, n in counts.items())


def robot_rows(b: dict) -> dict:
    """Every row of one robot's block on the sheets Robots, Joints, Parts, Boards, Sensors and Constants, and the car
    sensor elements of its sensors (sheet SensorElements, by the sensor's name)."""
    name = b['name']
    out = {sheet: [] for sheet in ('Robots', 'Joints', 'Parts', 'Boards', 'Sensors', 'Constants', 'SensorElements')}
    out['Robots'].append((name, b['maker'], 1, b['height'], b['stated'], b['sources']))

    # Its joints, their modules and driver boards, and two encoders and two connectors per joint.
    averaged = b['joints'] == AVERAGE
    joints = AVERAGE_JOINTS if averaged else b['joints']
    for number, (joint_name, count, size, torque, masses, heat, region, *share) in enumerate(joints, start=1):
        low, mode, high = masses or (None, None, None)
        out['Joints'].append((name, number, joint_name, count, size, torque, low, mode, high,
                              share[0] if share else None, 'not stated', heat, region, b['joint_sources'],
                              MAGNETS_BASIS))
    in_robot = b['joints_stated'] or sum(j[1] for j in joints)
    for size in ('small', 'large'):
        mine = [j for j in joints if j[2] == size]
        if mine:
            count, where = sum(j[1] for j in mine), regions(mine)
            out['Parts'].append((name, f'Joint module, {size}', count, 'In the joints', where, None, None, None, None,
                                 None, JOINT_SHARES if averaged else JOINT_MASSES, b['joint_label'][size],
                                 b['joint_sources']))
            out['Boards'].append((name, f'Driver board, {size} joint', count, 'In the joints', where, None, None, None,
                                  DRIVER_FROM, 'PE_HVS', 'E', 'as the G1 (E5.12 point 2)'))
    label, source = b['encoders']
    out['Parts'].append((name, 'Encoders (two per joint)', 2 * in_robot, 'In the joints', 'as their joints', None,
                         None, None, None, None, 'Sensors and SensorElements (Encoder)', label, source))
    out['Sensors'].append((name, 'Encoder', 2 * in_robot, 'In the joints', 'as their joints', None, None, None, label,
                           f'{source}; elements only'))

    # Its battery: the pack, its cells from their energy, its housing the pack's remainder, its management board.
    if b['pack'] == PACK_CELLS_ONLY:
        out['Parts'].append((name, 'Battery pack', 1, 'Battery pack', 'Torso', None, None, None, None, None,
                             PACK_CELLS_ONLY, 'S', b['pack_source']))
    elif b['pack'] is None:
        out['Parts'].append((name, 'Battery pack', 1, 'Battery pack', 'Torso', None, None, None, None, None,
                             PACK_FROM_ENERGY, 'S, E', 'its mass not stated (E5.14 point 3)'))
    else:
        (low, mode, high), label, source = b['pack']
        out['Parts'].append((name, 'Battery pack', 1, 'Battery pack', 'Torso', low, mode, high, None, None,
                             PACK_STATED, label, source))
    label, source = b['cells']
    out['Parts'].append((name, 'Battery cells', 1, 'Battery pack', 'Torso', None, None, None, 'Battery materials', None,
                         CELLS_FROM_CHARGE if b['voltage'] else CELLS_FROM_MASS, label, source))
    if b['housing']:
        out['Parts'].append((name, b['housing'], 1, 'Battery pack', 'Torso', None, None, None, None, None, HOUSING,
                             'E', 'E5.19 point 1'))
    out['Boards'].append((name, 'Battery management board', 1, 'Battery pack', 'Torso', *BATTERY_BOARD,
                          'area times Constants board mass per cm2', 'BMS', 'E', 'as the G1 (E5.14 point 4)'))

    # Its other boards and its sensors, as its sources name them.
    for board, count, kind, region, area, category, label, source in b['boards']:
        out['Boards'].append((name, board, count, kind, region, *area, 'area times Constants board mass per cm2',
                              category, label, source))
    for sensor, count, kind, region, grams, label, source, units in b['sensors']:
        out['Sensors'].append((name, sensor, count, kind, region, *(grams or (None, None, None)), label, source))
        for car_type, per_sensor in units or []:
            out['SensorElements'].append((sensor, car_type, per_sensor))

    # Its cables and connectors, screws and other parts, shell and frame.
    out['Parts'].append((name, 'Cable conductors and insulation', 1, 'Cables', 'Whole body', None, None, None, None,
                         None, 'from Constants: length, cross-sections, insulation', b['cables'][1], b['cables'][2]))
    label, source = b['connectors']
    out['Parts'].append((name, 'XT30 (2+2) connectors (two per joint)', 2 * in_robot, 'Cables', 'Whole body',
                         *CONNECTOR_KG, None, None, None, label, source))
    for part, count, kg, grade, label, source in b['screws']:
        out['Parts'].append((name, part, count, 'Frame and shell', 'Whole body', *kg, 'Steel', grade, None, label,
                             source))
    for part, count, kind, region, kg, material, grade, label, source in b['cooler'] + b['parts']:
        out['Parts'].append((name, part, count, kind, region, *kg, material, grade, None, label, source))
    shell, source = b['shell']
    out['Parts'].append((name, shell, 1, 'Frame and shell', 'Whole body', None, None, None, 'Plastics', None, SHELL,
                         'E', source))
    frame, material, source = b['frame']
    out['Parts'].append((name, frame, 1, 'Frame and shell', 'Whole body', None, None, None, material, None, FRAME, 'E',
                         source))

    # Its own constants: its mass, its battery's voltage and capacity (or none: its energy per kg of robot), its cables.
    values, label, source = b['mass']
    out['Constants'].append((name, 'Robot mass, with battery', *values, 'kg', label, source))
    if b['voltage']:
        for quantity, unit, (values, label, source) in (('Battery voltage', 'V', b['voltage']),
                                                         ('Battery capacity', 'Ah', b['capacity'])):
            out['Constants'].append((name, quantity, *values, unit, label, source))
    values, label, source = b['cables']
    out['Constants'].append((name, 'Cable length (four conductors)', *values, 'm', label, source))
    return out


# --- The G1+ and the Asimov 2, from the rows of the robot each is ---------------------------------------------------
# The grades of the G1's, X1's and N1's parts of steel and titanium, each by its use (E5.18).
PART_GRADES = {('Unitree G1', 'Screws'): '42CrMo4', ('Unitree G1', 'Lower-leg links'): '42CrMo4',
               ('AgiBot X1', 'Titanium (TC4) links: waist (2), ankles (4)'): 'Ti-6Al-4V',
               ('AgiBot X1', 'Screws (about 980)'): '42CrMo4', ('AgiBot X1', 'Bearings outside the actuators'): 'GCr15',
               ('Fourier N1', 'Screws'): '42CrMo4'}
# The G1's, X1's and N1's rows with the columns added on 2026-10-29: the share of the joint modules (empty), the grade.
JOINTS_THREE = [r[:9] + (None,) + r[9:] for r in JOINTS_G1_X1_N1]
PARTS_THREE = [r[:9] + (PART_GRADES.get((r[0], r[1])),) + r[9:] for r in PARTS_G1_X1_N1]


def g1_plus_rows() -> dict:
    """The G1+ (E5.17 point 5): the G1's own rows as taken apart, its mass 35 kg ("Approx. 35kg"), and its two head
    joints as two small joints of the G1 (E), with their driver boards, encoders and connectors, two per joint; its
    "stronger motors" (+110 % peak torque at the shoulders and waist) are not in the G1's parts, and said so."""
    g1, plus, head = 'Unitree G1', 'Unitree G1+', 2
    note = "; the G1+: as the G1's (E5.17 point 5)"
    copy = lambda rows: [(plus,) + tuple(r[1:]) for r in rows if r[0] == g1]   # noqa: E731
    out = {'Robots': [(plus, 'Unitree', 1, 1.34, 35,
                       'G1p: the G1 with six upgrades, 25 joints, "Approx. 35kg", 1.34 m; its parts the G1\'s, its '
                       '"stronger motors" not (E5.17 point 5)')],
           'Joints': copy(JOINTS_THREE), 'Parts': [], 'Boards': [], 'Sensors': [], 'SensorElements': [],
           'Constants': copy(CONSTANTS_G1_X1_N1)}
    out['Joints'].append((plus, len(out['Joints']) + 1, 'Head (yaw and pitch)', head, 'small', None, None, None, None,
                          None, 'not stated', 'Elbows and wrists', 'Head',
                          'G1p: "2 head joints"; inside as the G1\'s small joint (E5.17 point 5)', MAGNETS_BASIS))
    for r in copy(PARTS_THREE):
        if r[1] == 'Joint module, small':
            r = r[:2] + (r[2] + head, r[3], f'{r[4]}, Head {head}') + r[5:12] + (r[12] + note,)
        elif r[1] in ('Encoders (two per joint)', 'XT30 (2+2) connectors (two per joint)'):
            r = r[:2] + (r[2] + 2 * head,) + r[3:12] + (r[12] + note,)
        out['Parts'].append(r)
    for r in copy(BOARDS_G1_X1_N1):
        if r[1] == 'Driver board, small joint':
            r = r[:2] + (r[2] + head, r[3], f'{r[4]}, Head {head}') + r[5:11] + (r[11] + note,)
        out['Boards'].append(r)
    for r in copy(SENSORS_G1_X1_N1):
        if r[1] == 'Encoder':
            r = r[:2] + (r[2] + 2 * head,) + r[3:9] + (r[9] + note,)
        out['Sensors'].append(r)
    return out


def scaled(values: tuple, factor: float) -> tuple:
    """Min, mode and max times a factor, rounded to four decimals; empty cells stay empty."""
    return tuple(None if v is None else round(v * factor, 4) for v in values)


def with_estimate(label: str) -> str:
    """A label with E added, for a value scaled by an estimate."""
    return label if 'E' in label else f'{label}, E'


def asimov_two_rows(asimov_one: dict) -> dict:
    """The Asimov 2 (E5.17 point 7: "The Asimov 1's composition ... scaled to the catalogue's 38 kg (E)"): every mass,
    area and energy of the Asimov 1's rows times 38 / 35, its labels with E; its mass the catalogue's."""
    one, two = ASIMOV_ONE['name'], MENLO_ASIMOV_2
    (_, mode_one, _), (_, mode_two, _) = ASIMOV_ONE['mass'][0], ASIMOV_TWO_MASS[0]
    f = mode_two / mode_one
    note = f"the Asimov 1's, times {mode_two:g} / {mode_one:g} (E5.17 point 7): "
    out = {'Robots': [(two, 'Menlo', 1, 1.2, 38, 'HG (an "educated estimate"; Menlo: "In progress"); the Asimov 1 '
                                                 'scaled to 38 kg (E5.17 point 7)')],
           'SensorElements': []}
    out['Joints'] = [(two,) + r[1:6] + scaled(r[6:9], f) + r[9:13] + (note + r[13], r[14])
                     for r in asimov_one['Joints']]
    out['Parts'] = [(two,) + r[1:5] + scaled(r[5:8], f) + r[8:11] + (with_estimate(r[11]), note + r[12])
                    for r in asimov_one['Parts']]
    out['Boards'] = [(two,) + r[1:5] + scaled(r[5:8], f) + r[8:10] + (with_estimate(r[10]), note + r[11])
                     for r in asimov_one['Boards']]
    out['Sensors'] = [(two,) + r[1:5] + scaled(r[5:8], f) + (with_estimate(r[8]), note + r[9])
                      for r in asimov_one['Sensors']]
    out['Constants'] = [(two, 'Robot mass, with battery', *ASIMOV_TWO_MASS[0], 'kg', *ASIMOV_TWO_MASS[1:])]
    for r in asimov_one['Constants']:
        if r[1] in ('Battery capacity', 'Cable length (four conductors)'):
            out['Constants'].append((two, r[1]) + scaled(r[2:5], f) + (r[5], with_estimate(r[6]), note + r[7]))
        elif r[1] == 'Battery voltage':
            out['Constants'].append((two,) + r[1:])
    return out


# Every robot of the register's sheet Type 1 beyond the G1, X1 and N1, in the register's order (its numbers).
ASIMOV_ONE_ROWS = robot_rows(ASIMOV_ONE)
GENERATED = [robot_rows(AI_SAPIENS_K1), robot_rows(AKINCI_5), ASIMOV_ONE_ROWS, asimov_two_rows(ASIMOV_ONE_ROWS),
             robot_rows(BOOSTER_T1), robot_rows(BOOSTER_T2), robot_rows(NOETIX_BUMI), robot_rows(NOETIX_E1),
             g1_plus_rows(), robot_rows(JAKA_PI), robot_rows(ROBOTIS_K0), robot_rows(BOOSTER_K1_5AH),
             robot_rows(BOOSTER_K1_2AH), robot_rows(LIGHTBOT_0), robot_rows(DOBOT_LUMO), robot_rows(NORI_L3),
             robot_rows(PHYBOT_C1), robot_rows(PM01), robot_rows(PRIMEBOT_Q1), robot_rows(QUESTER1),
             robot_rows(LEJU_ROBAN2), robot_rows(ROBOTO_ORIGIN), robot_rows(RP1), robot_rows(FAUNA_SPROUT),
             robot_rows(STARBOT_ASTRA), robot_rows(TOTAN_O1), robot_rows(UNITREE_R1), robot_rows(XIAO_TUO),
             robot_rows(YMBOT_E3)]


def generated(sheet: str) -> list:
    """The rows of every generated robot on one sheet, in the order of GENERATED."""
    return [row for rows in GENERATED for row in rows[sheet]]


def sensor_elements() -> list:
    """The car sensor elements of the generated robots' sensors, each sensor once; a sensor named twice must be made of
    the same elements."""
    known = {r[0]: [] for r in SENSORELEMENTS_G1_X1_N1}
    for r in SENSORELEMENTS_G1_X1_N1:
        known[r[0]].append(r[1:])
    new: dict = {}
    for sensor, car_type, units in generated('SensorElements'):
        new.setdefault(sensor, [])
        if (car_type, units) not in new[sensor]:
            new[sensor].append((car_type, units))
    for sensor, units in new.items():
        if sensor in known and sorted(known[sensor]) != sorted(units):
            raise ValueError(f'{sensor}: named with other elements than in SENSORELEMENTS_G1_X1_N1.')
    return list(SENSORELEMENTS_G1_X1_N1) + [(sensor, *u) for sensor, units in new.items() if sensor not in known
                                            for u in units]


# The sheets' rows: the G1's, X1's and N1's first, then every other robot of type 1.
ROBOTS_ROWS = ROBOTS_G1_X1_N1 + generated('Robots')
JOINTS_ROWS = JOINTS_THREE + generated('Joints')
PARTS_ROWS = PARTS_THREE + generated('Parts')
BOARDS_ROWS = BOARDS_G1_X1_N1 + generated('Boards')
SENSORS_ROWS = SENSORS_G1_X1_N1 + generated('Sensors')
SENSORELEMENTS_ROWS = sensor_elements()
CONSTANTS_ROWS = CONSTANTS_G1_X1_N1 + generated('Constants')


# Every sheet after About, in the order of the file: its name, first row, rows and column widths.
SHEETS = [
    ('Robots', ROBOTS_HEADINGS, ROBOTS_ROWS, ROBOTS_WIDTHS),
    ('Joints', JOINTS_HEADINGS, JOINTS_ROWS, JOINTS_WIDTHS),
    ('MagnetGrades', MAGNETGRADES_HEADINGS, MAGNETGRADES_ROWS, MAGNETGRADES_WIDTHS),
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
