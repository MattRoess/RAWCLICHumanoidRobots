"""
Builder of data/researched/2_full_scale_general_purpose_ai_research/parts_taken_apart.xlsx: the robots of type 2 taken
apart so far, part by part.

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

Matthias, 2026-10-29: "commit and push and then to typ 2", then "Yes, as proposed" (A: every robot of type 2 its own
rows, in batches; C: a parts file and builder per type); 2026-10-30: "Yes, all three" (EVIDENCE.md E6.6), "Yes, agree
E6.8" (the proposal for batch 1, points 1 to 13), "Yes, build C".

WHAT IT DOES
------------
It writes the data file of the robots of type 2 taken apart so far, each part by part, as type 1's builder writes
type 1's (the same sheets, the same machinery in tools/parts_taken_apart.py): batch 1, the five robots whose makers
publish a model file, the Unitree H2, H2 Plus and H1-2 and the Fourier GR-2 and GR-1 (EVIDENCE.md E3, "Those with model
files"), the GR-1 in two versions (one or two depth cameras). Each block gives what the robot's own sources give
(E6.1 to E6.7) and, where they stop, what E6.8 agreed: each joint's mass from its torque by type 1's fit refit with
the M107 (point 1), its battery from its voltage and capacity (point 6), its boards and sensors by the template
(points 7 and 8), its cables scaled by its height (point 9), its shell and screws by its mass (points 10 and 11), its
frame the remainder (point 12). Each row names its own sources.

WHAT IT READS AND WRITES
------------------------
It reads nothing but 00's settings (src/params_schema.py, for where the file goes). It writes one file, the path of
`data.parts_taken_apart` with its folder (data/researched/2_full_scale_general_purpose_ai_research/
parts_taken_apart.xlsx, git-ignored; the folder is the one this file sits in), and replaces the file there. The values
are held here and in tools/parts_taken_apart.py: a change to them is made there, not in the .xlsx.

WHERE IT SITS
-------------
It is not a stage of the model: it writes one of the model's inputs, so it stands in tools/ and has no number.
01_schemas.py reads and checks the file; 02_composition.py draws robot type 2 part by part from it, each robot from
its own rows. Press Run: no arguments. Importing this file writes nothing; tests/test_make_parts_taken_apart.py checks
that what it writes passes 01's checks.
"""
import os
import sys

# The tools/ folder, so that the shared machinery (tools/parts_taken_apart.py) can be imported when this file is run.
TOOLS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TOOLS not in sys.path:
    sys.path.insert(0, TOOLS)
from parts_taken_apart import *  # noqa: E402,F401,F403  (every shared name: the sheets, the template, the functions)
from parts_taken_apart import (CABLE_ETHERNET, DRIVER_AREA, DRIVER_BOARD_AREA, SHARED_CONSTANTS_FIRST,  # noqa: E402
                               SHARED_CONSTANTS_LAST, SHARED_SOURCES, estimate, joint, robot_rows, sensor_elements,
                               sheets, spread, type_output_path, write_file)

# The robot type of this file, and its folder (the one this builder sits in, named as data/consolidated/'s).
ROBOT_TYPE = 2
FOLDER = os.path.basename(os.path.dirname(os.path.abspath(__file__)))

# --- About ----------------------------------------------------------------------------------------------------------
# The file's own description, one line per row of its first column (None leaves the row empty).
ABOUT = [
    'Robot type 2 part by part: the five of its robots taken apart so far (batch 1; the GR-1 in two versions), for '
    'where their critical materials sit',
    None,
    'The Unitree H2, H2 Plus and H1-2 and the Fourier GR-2 and GR-1, the robots of type 2 whose makers publish a model '
    'file, agreed by Matthias on 2026-10-30 (documentation/claude/EVIDENCE.md E6.1 to E6.8: "Yes, all three", "Yes, '
    'agree E6.8"), written as type 1\'s robots are (tools/parts_taken_apart.py). Written by Claude.',
    "Sheet Robots: each robot, its maker, its type, the maker's height and stated mass. Every sheet with a column "
    "Robot holds each robot's own rows; JointParts, Shares and SensorElements are one set for all (the G1's joint "
    'insides, scaled to each joint\'s module mass, as for type 1).',
    "Labels: W weighed; S from a source (named in Sources); E an estimate, with at least half to 1.5 times its mode.",
    'Every range is min / mode / max. A remainder takes what the other shares or parts leave; nothing is rescaled.',
    None,
    "Sheet Joints: each robot's joints, where they sit, their peak torque and module mass: the M107's stated 1.9 kg "
    "where Unitree names it (the H1-2's knees), else type 1's fit of mass on torque refit with the M107, 0.0689 kg × "
    'torque^0.566, half to 1.5 times (E6.8 point 1). The hands of the H2 Plus, GR-2 and GR-1 as small joints.',
    'Sheet Constants: each robot\'s own numbers, and the shared ones once (robot "all"), with the Ethernet line\'s '
    'conductors of the Fourier robots (E6.8 point 9).',
    'Sheet Sources: every source code used here, as in EVIDENCE.md E6.',
    None,
    'Read where they lie, not copied: as type 1\'s file (RAWCLICVehicleElectronics, RAWCLICDataCenters, '
    "RAWCLICVehicleTractionMotor); this project's element_recipes.xlsx (the cells, type 2's aluminium and plastics, "
    'the other grades).',
]

# --- Constants: the shared numbers, and type 2's own ----------------------------------------------------------------
# The Ethernet line of the Fourier GR-1 and GR-2 (their pages: "46V电源线和以太网线", a 46 V power line and an Ethernet
# line through every joint): eight conductors of 26 / 24 / 22 AWG, the gauges of Ethernet cables, the gauge not stated
# (E); the minimum widened from 26 AWG's 0.129 mm2 to half the mode (his rule for estimates; E6.8 point 9).
ETHERNET_CS = 'Ethernet conductor cross-section (8 conductors)'
TYPE_TWO_SHARED = [
    ('all', DRIVER_AREA, *DRIVER_BOARD_AREA, 'cm2', 'W, E',
     "the G1's weighed small joint's driver board (12.8 g, T1 slides 24, 43), its area at most the 60 mm joint (E2.8): "
     "the area every joint's driver board is scaled from, as in type 1"),
    ('all', ETHERNET_CS, 0.1, 0.205, 0.326, 'mm2', 'E',
     'the Fourier robots\' Ethernet line (GR1a, GR2a): 26 / 24 / 22 AWG, the gauge not stated; the minimum widened to '
     'half the mode (E6.8 point 9)'),
]

# --- Sources --------------------------------------------------------------------------------------------------------
# Every source code used in this file (EVIDENCE.md E6), read by Claude on 2026-10-28 (E3) and 2026-10-30; and those the
# shared rows cite.
SOURCES_ROWS = [
    ('H2p', 'Unitree, H2 product page (its parameter table)', 'https://www.unitree.com/h2',
     "Manufacturer's specification"),
    ('H2d', 'Unitree, H2 SDK development guide, About H2 (updated 2026-09-03)',
     'https://support.unitree.com/home/en/H2_developer/About_H2', "Manufacturer's documentation"),
    ('H2u', 'Unitree, H2.urdf (torque limits, link masses: 75.59 kg)',
     'https://github.com/unitreerobotics/unitree_ros/tree/master/robots/h2_description', "Manufacturer's model file"),
    ('H2Pu', 'Unitree, H2_Plus.urdf (31 joints and 44 of the hands, link masses: 77.24 kg)',
     'https://github.com/unitreerobotics/unitree_ros/tree/master/robots/h2_plus', "Manufacturer's model file"),
    ('H1p', 'Unitree, H1 and H1-2 product page (their parameter tables, the M107 table: "Weight 1.9kg", 360 N·m)',
     'https://www.unitree.com/h1', "Manufacturer's specification"),
    ('H1d', 'Unitree, H1 SDK development guide, About_H1-2 (updated 2026-03-12)',
     'https://support.unitree.com/home/en/H1_developer/About_H1-2', "Manufacturer's documentation"),
    ('H1u', 'Unitree, h1_2.urdf (67.37 kg with two hands) and h1_2_handless.urdf (66.98 kg)',
     'https://github.com/unitreerobotics/unitree_ros/tree/master/robots/h1_2_description',
     "Manufacturer's model files"),
    ('GR2a', 'Fourier, About GR-2 (its specification table)',
     'https://support-old.fftai.com/docs/GR-X-Humanoid-Robot/GR2/GR-2_Introduction/', "Manufacturer's documentation"),
    ('GR2u', 'Fourier, gr2v3_8_7.urdf (29 joints, 62.98 kg; with hands 63.92 kg) and GR2T2V2.urdf (62.73 kg)',
     'https://github.com/FFTAI/Wiki-GRx-Models', "Manufacturer's model files"),
    ('GR1a', 'Fourier, About GR-1 (its specification table, its components)',
     'https://support-old.fftai.com/docs/GR-X-Humanoid-Robot/GR1/GR-1_Introduction/', "Manufacturer's documentation"),
    ('GR1u', 'Fourier, GR1T2.urdf (fourier_lab: the legs, decided) and gr1t2.urdf (Wiki-GRx-Models: the arms, waist '
             'and head; 54.53 kg, with hands 55.47 kg)', 'https://github.com/FFTAI/fourier_lab',
     "Manufacturer's model files"),
    ('FH1', "Fourier, fourier_left_hand_6dof.urdf and fourier_right_hand_6dof.urdf (0.443 kg each)",
     'https://github.com/FFTAI/Wiki-GRx-Models', "Manufacturer's model files"),
    ('FSA', 'Fourier, Fourier Smart Actuator programming reference (seven actuator models, no masses)',
     'https://fftai.github.io/fsa/fsa/', "Manufacturer's documentation"),
    SHARED_SOURCES['L1'],
    SHARED_SOURCES['T1'],
    SHARED_SOURCES['T3'],
    SHARED_SOURCES['T3k'],
    SHARED_SOURCES['Bizzo 2014'],
    SHARED_SOURCES['Drexler 2025'],
]

# ======================================================================================================================
# The robots of type 2 taken apart: one block each (EVIDENCE.md E6.8)
# ======================================================================================================================

# An actuator's mass where no source states it (E6.8 point 1): type 1's fit of mass on peak torque (E2.8e), refit on
# the 12 makers' actuators with a stated mass (AgiBot's 3, E5.11's 8, the M107; every one within 0.79 to 1.33 times
# it): kg = FIT_KG × torque^FIT_POWER, half to 1.5 times (E). Type 1's own robots keep type 1's (E5.12 point 4).
FIT_KG, FIT_POWER = 0.0689, 0.566
# Unitree's M107: "Weight 1.9kg", 360 N·m (H1p, its table), ± 5 % as a figure stated once (E5.12 point 3); the H1-2's
# knees ("uses the self-developed M107", H1d; knee "About 360N.m", H1p).
M107 = spread(1.9)
# The camera of a robot whose maker names it but gives no mass: as a D435 (75 g), a stereo camera too, half to 1.5
# times (E6.8 point 8); its elements two image sensors.
STEREO_CAMERA_G = estimate(75)
STEREO = [('CMOS image sensor', 2)]
# The cables of a robot of type 2 (E6.8 point 9): the X1's 11 m listed and the G1's "not longer than 10m", both at
# 1.3 m, scaled by the robot's height, half to 1.5 times (E).
CABLES_TALL = (7, 14, 21)      # m: 1.75 to 1.82 m (the H2, H2 Plus, H1-2, GR-2)
CABLES_GR1 = (6.5, 13, 19.5)   # m: 1.65 m (the GR-1)
CABLES_SOURCE = ("the X1's 11 m listed and the G1's \"not longer than 10m\" at 1.3 m, scaled by its height, half to "
                 '1.5 times (E6.8 point 9)')
# A robot's titanium where its maker names it but gives no share (the H2's "Titanium Alloy"): 0.6 / 1.2 / 1.8 % of its
# mass, as the X1's 0.4 kg of TC4 in 33 kg, the one robot of this project with titanium parts named (E6.8 point 12).
TITANIUM_SHARE = (0.006, 0.012, 0.018)


def from_torque(torque: float) -> tuple:
    """An actuator's mass, kg, from its peak torque (E6.8 point 1): the refit, half to 1.5 times."""
    return estimate(FIT_KG * torque ** FIT_POWER)


def screws(robot_kg: float) -> list:
    """A robot's screws (E6.8 point 11): the G1's 0.2 / 0.5 / 1 kg scaled by the robot's mass over the G1's 35 kg."""
    f = robot_kg / 35
    return [('Screws', 1, tuple(round(v * f, 4) for v in SCREWS_KG), '42CrMo4', 'E',
             f"the G1's 0.2 / 0.5 / 1 kg times {robot_kg:g} / 35 kg (E6.8 point 11); grade E5.18")]


def titanium(robot_kg: float, source: str) -> tuple:
    """A robot's titanium alloy parts, a share of its mass (TITANIUM_SHARE), Ti-6Al-4V (E6.8 point 12)."""
    return ('Titanium alloy parts', 1, 'Frame and shell', 'Whole body',
            tuple(round(s * robot_kg, 4) for s in TITANIUM_SHARE), 'Titanium', 'Ti-6Al-4V', 'E', source)


def fans(count: int, why: str) -> tuple:
    """The fans of a robot's computers, one each, as the G1's main board fan (E6.8 point 7)."""
    return ('Main board fan', count, 'Torso boards', 'Torso', FAN_KG, None, None, 'E',
            f"{why}, a fan each: as the G1's main board fan (E6.8 point 7)")


def x86_sinks(count: int) -> tuple:
    """The heat pipes and fins of `count` Intel computers, as the X1's and N1's (E5.22; E6.8 point 7)."""
    return (X86_SINK[0], count) + X86_SINK[2:]


# --- The joints -----------------------------------------------------------------------------------------------------
# Each joint: its name (its first word its kind), how many, its peak torque N·m, its module mass, heat group, region.
def fitted(name: str, count: int, torque: float, heat_group: str, region: str) -> tuple:
    """A joint whose actuator's mass no source states: the refit at its torque (E6.8 point 1)."""
    return joint(name, count, torque, from_torque(torque), heat_group, region)


# The H2 (H2u: every joint's torque limit; H2p: legs "360N.m", arms "120N.m" at most).
H2_JOINTS = [
    fitted('Hip pitch', 2, 360, 'Hips', 'Legs'), fitted('Hip roll', 2, 360, 'Hips', 'Legs'),
    fitted('Hip yaw', 2, 360, 'Hips', 'Legs'), fitted('Knee', 2, 360, 'Knees', 'Legs'),
    fitted('Ankle pitch', 2, 66.88, 'Ankles', 'Legs'), fitted('Ankle roll', 2, 19, 'Ankles', 'Legs'),
    fitted('Waist yaw', 1, 120, 'Waist', 'Torso'), fitted('Waist roll', 1, 180, 'Waist', 'Torso'),
    fitted('Waist pitch', 1, 180, 'Waist', 'Torso'),
    fitted('Head pitch', 1, 50, 'Elbows and wrists', 'Head'), fitted('Head yaw', 1, 50, 'Elbows and wrists', 'Head'),
    fitted('Shoulder pitch', 2, 130, 'Shoulders', 'Arms'), fitted('Shoulder roll', 2, 60, 'Shoulders', 'Arms'),
    fitted('Shoulder yaw', 2, 60, 'Shoulders', 'Arms'), fitted('Elbow', 2, 60, 'Elbows and wrists', 'Arms'),
    fitted('Wrist roll', 2, 60, 'Elbows and wrists', 'Arms'), fitted('Wrist pitch', 2, 10, 'Elbows and wrists', 'Arms'),
    fitted('Wrist yaw', 2, 10, 'Elbows and wrists', 'Arms')]
H2_JOINT_SOURCES = ("H2u: every joint's torque limit; mass the refit at its torque, 0.0689 kg × torque^0.566, half to "
                    '1.5 times (E6.8 point 1)')
# The H2 Plus's hands (H2Pu: 22 joints each, which of them driven not stated): their mass the models' difference,
# 77.24 − 75.59 = 1.65 kg for both, half to 1.5 times (decided 2026-10-30, "Yes, all three"); as small joints.
H2_PLUS_HAND = joint('Hand (five fingers)', 2, None, estimate(0.825), 'Elbows and wrists', 'Arms', size='small')
# The H1-2 (H1p's peak torques per joint; H1u's limits lower: 2026-10-30, E6.8 point 2), its knees the M107.
H1_2_JOINTS = [
    fitted('Hip yaw', 2, 220, 'Hips', 'Legs'), fitted('Hip pitch', 2, 220, 'Hips', 'Legs'),
    fitted('Hip roll', 2, 220, 'Hips', 'Legs'), joint('Knee', 2, 360, M107, 'Knees', 'Legs'),
    fitted('Ankle pitch', 2, 75, 'Ankles', 'Legs'), fitted('Ankle roll', 2, 75, 'Ankles', 'Legs'),
    fitted('Waist (torso)', 1, 220, 'Waist', 'Torso'),
    fitted('Shoulder pitch', 2, 120, 'Shoulders', 'Arms'), fitted('Shoulder roll', 2, 120, 'Shoulders', 'Arms'),
    fitted('Shoulder yaw', 2, 120, 'Shoulders', 'Arms'), fitted('Elbow', 2, 120, 'Elbows and wrists', 'Arms'),
    fitted('Wrist roll', 2, 30, 'Elbows and wrists', 'Arms'), fitted('Wrist pitch', 2, 30, 'Elbows and wrists', 'Arms'),
    fitted('Wrist yaw', 2, 30, 'Elbows and wrists', 'Arms')]
# A Fourier hand of six joints (GR1a: "该装置具有六个运动自由度"; the GR-2's "单手基础自由度 6"): Fourier's own model of it,
# 0.443 kg (FH1), a model's mass, not a datasheet's: half to 1.5 times (E6.8 point 4); as a small joint.
FOURIER_HAND = joint('Hand (Fourier, six joints)', 2, None, estimate(0.443), 'Elbows and wrists', 'Arms', size='small')
# The GR-2 (GR2u: every joint's torque limit, the same as GR2a's).
GR2_JOINTS = [
    fitted('Hip pitch', 2, 366.05, 'Hips', 'Legs'), fitted('Hip roll', 2, 95.472, 'Hips', 'Legs'),
    fitted('Hip yaw', 2, 54.33, 'Hips', 'Legs'), fitted('Knee', 2, 366.05, 'Knees', 'Legs'),
    fitted('Ankle pitch', 2, 54.33, 'Ankles', 'Legs'), fitted('Ankle roll', 2, 29.835, 'Ankles', 'Legs'),
    fitted('Waist yaw', 1, 74.45, 'Waist', 'Torso'),
    fitted('Head yaw', 1, 17.325, 'Elbows and wrists', 'Head'),
    fitted('Head pitch', 1, 17.325, 'Elbows and wrists', 'Head'),
    fitted('Shoulder pitch', 2, 74.45, 'Shoulders', 'Arms'), fitted('Shoulder roll', 2, 74.45, 'Shoulders', 'Arms'),
    fitted('Shoulder yaw', 2, 42.75, 'Shoulders', 'Arms'), fitted('Elbow', 2, 42.75, 'Elbows and wrists', 'Arms'),
    fitted('Wrist yaw', 2, 17.325, 'Elbows and wrists', 'Arms'),
    fitted('Wrist pitch', 2, 17.325, 'Elbows and wrists', 'Arms'),
    fitted('Wrist roll', 2, 17.325, 'Elbows and wrists', 'Arms'), FOURIER_HAND]
# The GR-1: its legs from GR1T2.urdf (225 N·m, fitting GR1a's "230N.m"), its waist, head and arms from gr1t2.urdf
# (decided 2026-10-30, "Yes, all three").
GR1_JOINTS = [
    fitted('Hip roll', 2, 48, 'Hips', 'Legs'), fitted('Hip yaw', 2, 66, 'Hips', 'Legs'),
    fitted('Hip pitch', 2, 225, 'Hips', 'Legs'), fitted('Knee', 2, 225, 'Knees', 'Legs'),
    fitted('Ankle pitch', 2, 15, 'Ankles', 'Legs'), fitted('Ankle roll', 2, 30, 'Ankles', 'Legs'),
    fitted('Waist yaw', 1, 65, 'Waist', 'Torso'), fitted('Waist pitch', 1, 65, 'Waist', 'Torso'),
    fitted('Waist roll', 1, 65, 'Waist', 'Torso'),
    fitted('Head roll', 1, 5.25, 'Elbows and wrists', 'Head'),
    fitted('Head pitch', 1, 5.25, 'Elbows and wrists', 'Head'),
    fitted('Head yaw', 1, 5.25, 'Elbows and wrists', 'Head'),
    fitted('Shoulder pitch', 2, 38.46, 'Shoulders', 'Arms'), fitted('Shoulder roll', 2, 38.46, 'Shoulders', 'Arms'),
    fitted('Shoulder yaw', 2, 30.3, 'Shoulders', 'Arms'), fitted('Elbow', 2, 30.3, 'Elbows and wrists', 'Arms'),
    fitted('Wrist yaw', 2, 13.17, 'Elbows and wrists', 'Arms'),
    fitted('Wrist roll', 2, 5.25, 'Elbows and wrists', 'Arms'),
    fitted('Wrist pitch', 2, 5.25, 'Elbows and wrists', 'Arms'), FOURIER_HAND]

# --- The parts every Unitree robot of batch 1 shares ----------------------------------------------------------------
UNITREE_CELLS = ('E', 'NMC cylindrical, E: "Premium Lithium Battery with Low Internal Resistance" (H2p), no chemistry '
                      'stated (E6.8 point 6)')
H2_BOARDS = [
    ('Computer board PC1, Intel Core i5 (motion control)', 1, 'Torso boards', 'Torso', COMPUTER, 'ITC', 'E',
     "H2d (10 cores, 8 GB); as the X1's and N1's computer boards (E6.8 point 7)"),
    ('Computer board PC2, Intel Core i7 (development)', 1, 'Torso boards', 'Torso', COMPUTER, 'ITC', 'E',
     "H2d (10 cores, 16 or 32 GB); as the X1's and N1's computer boards (E6.8 point 7)"),
    POWER_BOARD]
H2_MICROPHONES = ('Microphone array (4 microphones)', 1, 'Head', 'Head', MICROPHONES_G, 'E',
                  'H2p "Array Microphone"; as the G1\'s four (E6.8 point 8)', MICROPHONES)
H2_SPEAKER = ('Speaker, high-power', 1, 'Head', 'Head', SPEAKER_G, 'E', 'H2p "High-Power Speaker"; as the G1\'s (E6.8 '
                                                                         'point 8)', [])
H2_IMUS = ('Motion sensor (IMU), torso and pelvis', 2, 'Torso boards', 'Torso', IMU_G, 'E',
           "H2u (imu_in_torso, imu_in_pelvis); as the G1's (E6.8 point 8)", [('IMU', 1)])


def h2(name: str, stated: float | None, sources: str, mass: tuple, joints: list, joint_sources: str, boards: list,
       cooler: list, camera: tuple) -> dict:
    """The H2 or the H2 Plus (E6.1, E6.2, E6.8): the same body, battery, cables and shell; the H2 Plus with its hands,
    its Jetson Thor and its camera on it."""
    robot_kg = mass[0][1]
    return block(
        name, 'Unitree', 1.82, stated, sources, mass, joints, joint_sources=joint_sources,
        voltage=((64.8, 64.8, 64.8), 'S', 'H2p "15Ah(0.972KWh)": 972 / 15 = 64.8 V, 18 cells of 3.6 V ("Maximum '
                                          'Voltage: 75.6 V" = 18 × 4.2 V; E6.1)'),
        capacity=(spread(15), 'S', 'H2p "15Ah"; ± 5 % (E6.8 point 6)'), cells=UNITREE_CELLS,
        boards=boards, cooler=cooler,
        sensors=[camera, H2_MICROPHONES, H2_SPEAKER, H2_IMUS],
        cables=(CABLES_TALL, 'E', CABLES_SOURCE), screws=screws(robot_kg),
        parts=[titanium(robot_kg, f'H2p "Titanium Alloy", no share stated: 0.6 / 1.2 / 1.8 % of {robot_kg:g} kg, as '
                                  "the X1's 0.4 kg of TC4 in 33 kg (E6.8 point 12)")],
        shell=('Shell: high-strength engineering plastics',
               'H2p "High-Strength Engineering Plastics"; 11.5 % of the robot (E6.8 point 10)'),
        frame=('Frame', 'Aluminium', 'H2p "Aircraft-Grade Aluminum"; the remainder (E6.8 point 12)'))


UNITREE_H2 = h2(
    'Unitree H2', 70, 'H2p (Unitree), H2d, H2u (its model, 75.59 kg); E6.1',
    ((69, 70, 75.59), 'S, E', 'H2p "About 70kg"; H2u its model 75.59 kg the max; 1 kg below the min (E6.8 point 5)'),
    H2_JOINTS, H2_JOINT_SOURCES, H2_BOARDS, [fans(2, 'its two Intel computers'), x86_sinks(2)],
    ('Binocular camera, 2 RGB sensors (2064 × 1552)', 1, 'Head', 'Head', STEREO_CAMERA_G, 'E',
     'H2d ("H2/H2 edu", on PC1); its mass not stated: as a D435, a stereo camera too (E6.8 point 8)', STEREO))
UNITREE_H2_PLUS = h2(
    'Unitree H2 Plus', None, 'H2p, H2d (Unitree; the H2 Plus\'s mass not stated), H2Pu (its model, 77.24 kg); E6.2',
    ((70.65, 71.65, 77.24), 'S, E', 'the H2\'s "About 70kg" and its two hands, 77.24 − 75.59 = 1.65 kg (E, decided '
                                    '2026-10-30); H2Pu its model 77.24 kg the max; 1 kg below the min (E6.8 point 5)'),
    H2_JOINTS + [H2_PLUS_HAND], H2_JOINT_SOURCES + "; its hands 1.65 kg for both, the models' difference (E)",
    H2_BOARDS + [
        ('Compute module PC3, NVIDIA Jetson Thor T5000', 1, 'Torso boards', 'Torso', estimate(87), 'ITC', 'E',
         "H2d (its camera on PC3, GMSL2); as the AGX Orin's 100 × 87 mm, the Thor's size not read (E6.8 point 7)"),
        ('Carrier board of the Jetson Thor', 1, 'Torso boards', 'Torso', (50, 100, 150), 'ITC', 'E',
         "as the Booster T1's carrier board (E6.8 point 7)")],
    [fans(3, 'its two Intel computers and its Jetson Thor'), x86_sinks(2), ARM_SINK],
    ('Binocular camera, 2 sensors (2560 × 1984)', 1, 'Head', 'Head', STEREO_CAMERA_G, 'E',
     'H2d ("H2plus", on PC3 over GMSL2); its mass not stated: as a D435, a stereo camera too (E6.8 point 8)', STEREO))
UNITREE_H1_2 = block(
    'Unitree H1-2', 'Unitree', 1.78, 70, 'H1p (Unitree), H1d, H1u (its models, 67.37 kg, without hands 66.98 kg); E6.3',
    ((66.98, 70, 71), 'S, E', 'H1p "About 70kg"; H1u its model without hands 66.98 kg the min; 1 kg above the max '
                              '(E6.8 point 5)'),
    # Its joint modules labelled E: 25 of its 27 joints' masses come from their torques; the knees' M107 is stated
    # (its rows in the sheet Joints say so), as the sources below (2026-10-30: the table of 01 grouped it as stated).
    H1_2_JOINTS, joint_label={'small': 'E', 'large': 'E'},
    joint_sources=('H1p: the peak torque of each joint ("Knee Torque About 360N.m, Hip Joint Torque About 220N.m, '
                   'Waist Joint About 220N.m, Ankle Joint About 75x2N.m"; shoulder and elbow 120, wrist 30 N·m); the '
                   'knees the M107, 1.9 kg (H1p, H1d), ± 5 %; the others the refit at their torque, half to 1.5 times '
                   '(E6.8 points 1 and 2)'),
    voltage=((57.6, 57.6, 57.6), 'S', 'H1p "15Ah(0.864KWh)": 864 / 15 = 57.6 V, 16 cells of 3.6 V ("Max Voltage '
                                      '67.2V" = 16 × 4.2 V; E6.3)'),
    capacity=(spread(15), 'S', 'H1p "15Ah"; ± 5 % (E6.8 point 6)'),
    cells=('E', 'NMC cylindrical, E: no chemistry stated (E6.8 point 6)'),
    boards=[('Computer board PC1, Intel i5-1235U (motion control)', 1, 'Torso boards', 'Torso', COMPUTER, 'ITC', 'E',
             "H1d; as the X1's and N1's computer boards (E6.8 point 7)"),
            ('Computer board PC4, Intel i7-1255U or i7-1265U (development)', 1, 'Torso boards', 'Torso', COMPUTER,
             'ITC', 'E', "H1d; as the X1's and N1's computer boards (E6.8 point 7)"),
            POWER_BOARD],
    cooler=[fans(2, 'its two Intel computers'), x86_sinks(2)],
    sensors=[('LiDAR, Livox Mid-360', 1, 'Head', 'Head', (265, 265, 265), 'S', 'H1d "MID-360 Lidar"; L1 (265 g)',
              LIDAR),
             ('Depth camera, Intel RealSense D435', 1, 'Head', 'Head', D435_G, 'S',
              'H1d "D435 depth camera"; Intel D400 datasheet, D435 75 g (second-hand), as the G1', DEPTH_CAMERA),
             ('Motion sensor (IMU)', 1, 'Torso boards', 'Torso', IMU_G, 'E', "H1u imu_link; as the G1's (E6.8 point "
                                                                             '8)', [('IMU', 1)])],
    encoders=('E', 'two per joint, as type 1; the M107 "Dual Encoder" (H1p)'),
    cables=(CABLES_TALL, 'E', CABLES_SOURCE), screws=screws(70),
    shell=('Shell: plastics', 'not stated; plastics as type 1, 11.5 % of the robot (E6.8 point 10)'),
    frame=('Frame', 'Aluminium', 'not stated; aluminium as type 1, the remainder (E6.8 point 12)'))
FOURIER_SHELL = ('Shell: engineering plastics', 'GR1a, GR2a "铝合金+工程塑料"; 11.5 % of the robot (E6.8 point 10)')
FOURIER_FRAME = ('Frame', 'Aluminium', 'GR1a, GR2a "铝合金+工程塑料": aluminium alloy; the remainder (E6.8 point 12)')
FOURIER_MICROPHONES = ('Microphone', 1, 'Head', 'Head', MICROPHONES_G, 'E', "GR2a; as the G1's microphone array (E6.8 "
                                                                            'point 8)', MICROPHONES)
FOURIER_SPEAKER = ('Speaker', 1, 'Head', 'Head', SPEAKER_G, 'E', "GR2a; as the G1's (E6.8 point 8)", [])
FOURIER_JOINT_SOURCES = ("its joints' torque limits; mass the refit at the torque, 0.0689 kg × torque^0.566, half to "
                         "1.5 times (E6.8 point 1; Fourier's FSA masses not stated, FSA); its two hands Fourier's "
                         "model, 0.443 kg each, half to 1.5 times (FH1; E6.8 point 4)")
FOURIER_GR2 = block(
    'Fourier GR-2', 'Fourier', 1.75, 63, 'GR2a (Fourier), GR2u (its models, 62.98 kg; with hands 63.92 kg); E6.4',
    ((62, 63, 64), 'S', 'GR2a "≈63 kg", ± 1 kg; its models 62.98 and 63.92 kg within (E6.8 point 5)'),
    GR2_JOINTS, joint_sources='GR2u: ' + FOURIER_JOINT_SOURCES,
    voltage=((39.6, 39.6, 39.6), 'S', 'GR2a "电池标称电压 39.6 V"'),
    capacity=(spread(round(950 / 39.6, 4)), 'S', 'GR2a "≈950 Wh" at 39.6 V; ± 5 % (E6.8 point 6)'),
    pack=((4.33, 5.79, 9), 'S, E', 'GR2a "总重量 ≤9 kg" the upper cut; the mode 950 Wh over 164 Wh/kg; the lower cut '
                                   'its heaviest cells (997.5 Wh at 232.5 Wh/kg) and its management board (E6.8 point '
                                   '6)'),
    cells=('E', 'NMC cylindrical, E: GR2a "锂离子电池", no chemistry stated (E6.8 point 6)'),
    boards=[('Computer board, Intel Core i7 (14 cores)', 1, 'Torso boards', 'Torso', COMPUTER, 'ITC', 'E',
             "GR2a \"14核高性能CPU\"; as the X1's and N1's computer boards (E6.8 point 7)"),
            ('Perception board, 8-core ARM', 1, 'Torso boards', 'Torso', COMPUTER, 'ITC', 'E',
             "GR2a (E3); as the X1's and N1's computer boards (E6.8 point 7)"),
            POWER_BOARD],
    cooler=[fans(2, 'its Intel computer and its ARM board'), x86_sinks(1), ARM_SINK],
    sensors=[('Binocular camera', 1, 'Head', 'Head', STEREO_CAMERA_G, 'E',
              'GR2a "双目摄像头"; its mass not stated: as a D435, a stereo camera too (E6.8 point 8)', STEREO),
             ('Motion sensor (IMU), 6-axis', 1, 'Torso boards', 'Torso', IMU_G, 'E', 'GR2a "IMU 6轴"; as the G1\'s',
              [('IMU', 1)]),
             FOURIER_MICROPHONES, FOURIER_SPEAKER],
    encoders=('S', 'GR2a: dual encoders (E3)'),
    cables=(CABLES_TALL, 'E', CABLES_SOURCE), cable_quantity=CABLE_ETHERNET, screws=screws(63),
    shell=FOURIER_SHELL, frame=FOURIER_FRAME)


def fourier_gr1(cameras: int) -> dict:
    """The GR-1 in one of its two versions (E6.8 point 8; a discrete state, each drawn as often): one or two depth
    cameras, its page saying both ("双深度相机" and "一个深度相机")."""
    return block(
        f"Fourier GR-1 {'one camera' if cameras == 1 else 'two cameras'}", 'Fourier', 1.65, 52,
        'GR1a (Fourier), GR1u (its models, 54.53 kg; with hands 55.47 kg); E6.5',
        ((51, 52, 55.47), 'S, E', 'GR1a "≈52kg"; GR1u its model with hands 55.47 kg the max; 1 kg below the min (E6.8 '
                                  'point 5)'),
        GR1_JOINTS, joint_sources='GR1u: ' + FOURIER_JOINT_SOURCES,
        voltage=((40, 40, 40), 'S', 'GR1a "电池标称电压 40V"'),
        capacity=(spread(483 / 40), 'S', 'GR1a "483Wh" at 40 V; ± 5 %; its "额定容量 5.2Ah 112.3Wh" unexplained, not '
                                         'used (E6.8 point 6)'),
        cells=('E', 'NMC cylindrical, E: GR1a "锂离子电池", no chemistry stated (E6.8 point 6)'),
        boards=[('Computer board, Intel Core i7-13700H (ASUS PN64 mini PC)', 1, 'Torso boards', 'Torso', COMPUTER,
                 'ITC', 'E', "GR1a; as the X1's and N1's computer boards (E6.8 point 7)"),
                ('Switch board (8 Ethernet ports)', 1, 'Torso boards', 'Torso', (30, 60, 90), 'ITC', 'E',
                 'GR1a "交换模块配有8个标准千兆以太网接口"; as the N1\'s network switch board (E6.8 point 7)'),
                ('Motion control unit', 1, 'Torso boards', 'Torso', (30, 60, 90), 'ITC', 'E',
                 "GR1a \"主运动控制单元\"; as the X1's control boards (E6.8 point 7)"),
                ('Power management module', 1, 'Torso boards', 'Torso', POWER, 'PE_HVS', 'E',
                 'GR1a "电源管理模块"; as the G1\'s power distribution board (E6.8 point 7)')],
        cooler=X86_COOLER,
        sensors=[('Depth camera, Intel RealSense (its model not named)', cameras, 'Head', 'Head', estimate(75), 'E',
                  'GR1a "Realsense"; as a D435, 75 g, half to 1.5 times; one or two, each as often (E6.8 point 8)',
                  DEPTH_CAMERA),
                 ('Motion sensor (IMU)', 1, 'Torso boards', 'Torso', IMU_G, 'E', "GR1a \"IMU 有\"; as the G1's",
                  [('IMU', 1)])],
        encoders=('S, E', 'GR1a: an absolute encoder at every active leg joint beside its motor\'s; two per joint, as '
                          'type 1'),
        cables=(CABLES_GR1, 'E', CABLES_SOURCE), cable_quantity=CABLE_ETHERNET, screws=screws(52),
        shell=FOURIER_SHELL, frame=FOURIER_FRAME)


FOURIER_GR1_ONE, FOURIER_GR1_TWO = fourier_gr1(1), fourier_gr1(2)

# Every robot of type 2 taken apart, in the register's order (its numbers: 116 GR-1, 117 GR-2, 119 H1-2, 120 H2,
# 121 H2 Plus).
GENERATED = [robot_rows(b, ROBOT_TYPE) for b in (FOURIER_GR1_ONE, FOURIER_GR1_TWO, FOURIER_GR2, UNITREE_H1_2,
                                                 UNITREE_H2, UNITREE_H2_PLUS)]


def generated(sheet: str) -> list:
    """The rows of every robot on one sheet, in the order of GENERATED."""
    return [row for rows in GENERATED for row in rows[sheet]]


# The sheets' rows.
ROBOTS_ROWS = generated('Robots')
JOINTS_ROWS = generated('Joints')
PARTS_ROWS = generated('Parts')
BOARDS_ROWS = generated('Boards')
SENSORS_ROWS = generated('Sensors')
SENSORELEMENTS_ROWS = sensor_elements([], generated('SensorElements'))
CONSTANTS_ROWS = SHARED_CONSTANTS_FIRST + TYPE_TWO_SHARED + SHARED_CONSTANTS_LAST + generated('Constants')

# Every sheet after About, in the order of the file (sheets(): the shared ones with type 2's rows).
SHEETS = sheets(ROBOTS_ROWS, JOINTS_ROWS, PARTS_ROWS, BOARDS_ROWS, SENSORS_ROWS, SENSORELEMENTS_ROWS, CONSTANTS_ROWS,
                SOURCES_ROWS)


def output_path() -> str:
    """Where the file goes: 00's setting `data.parts_taken_apart` with this type's folder, as an absolute path."""
    return type_output_path(FOLDER)


def build(path: str) -> None:
    """Write the whole file to `path`: the About sheet first, then every sheet of SHEETS in its order."""
    write_file(path, ABOUT, SHEETS)


def main() -> None:
    """Pressing Run: write the file where 00 says, in this type's folder, and say where."""
    path = output_path()
    build(path)
    print(f'Written: {path}')


if __name__ == '__main__':
    main()
