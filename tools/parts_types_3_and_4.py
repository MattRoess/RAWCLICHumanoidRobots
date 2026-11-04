"""
The robots of robot types 3 and 4 taken apart, part by part: their two templates and the blocks of their batches, one
copy for both types' builders.

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

Matthias, 2026-10-30: "Can we move to type 3 and 4 together?", "Yes, together", then for batch 1 "Yes, all four"
(EVIDENCE.md E11.2), "Yes, 64 kg" (E11.5), "Yes, agree E11.6" (the proposal) and "Yes, build it" (E11.7, its open
points A to C as recommended: A, this one module for both builders); for batch 2, 2026-11-01: "Yes, agree E12.2",
"A stated mass" (E12.4), "Yes, agree E13", "Yes, agree E12.5" and "Yes, build it" (E12.6, open points A to C as
recommended: B, the joint ratios computed here).

WHAT IT HOLDS
-------------
Types 3 and 4's own templates (E11.6 point 1): on legs, the joint modules 22.4 / 44.7 / 67.1 % of the robot's mass, the
median of the seven robots of types 3 or 4 with every joint (SEVEN: four of type 2's file, three of batch 1), split as
they are on average; on wheels 6.95 / 13.9 / 20.85 %, the median of the three of types 3 or 4 with every joint, split as
type 2's four (E9.6); the battery's energy per kg of robot where a maker gives none, 14.67 Wh/kg on legs and 10.84 on
wheels. Their shared values carry names of their own ("…, types 3 and 4"), so that no shared value has two numbers
under one name (E11.7 point 2). Then every robot of batch 1 (E11.6, 28 blocks with the X2 in two versions), each a block
of tools/parts_taken_apart.py's machinery, its numbers from its own sources (E11.1 to E11.5) and E11.6's method; the
joints of a robot from its one stated joint (from_stated_joint(), by the ratios between the joints of the robots with
every joint, E12.5 point 2; its module by type 2's fit or, for type 1's robots, type 1's rule); and every robot of
batch 2 (E12.5, 30 blocks: the CASBOT 02, the CYBORG RO1, the DR02 and the FF Master in two versions), from its sources
(E12.1 to E12.4). Since E14 (2026-11-01, "Yes, build it", E14.6 point 3) AgiBot's X2, X2 Ultra, A3 and A3 Ultra take
their joints from AgiBot's model files and the A2 from its page's knee. Since 2026-11-02 ("E15's entry", "Move on",
EVIDENCE.md E15.7) every robot of batch 3 (E15.3, 112 robots in 122 blocks: a robot of no stated form on legs and on
wheels, each as often), its numbers typed in from the record read first-hand (research_2026-11-01/), the 17 of one
stated joint by from_stated_joint(), the GR-3 and the Star1 by their makers' models, the Tau Humanoid by the Unitree
G1's rows of type 1's file.

WHAT IT READS AND WRITES
------------------------
It reads nothing and writes nothing. It imports the shared machinery (tools/parts_taken_apart.py) and type 2's builder
(its helpers and the four robots of type 2's file in the template on legs, one copy of them), and is imported by
tools/3_industrial_logistics_warehousing/make_parts_taken_apart.py and tools/4_service_healthcare_interaction/
make_parts_taken_apart.py, each of which writes the robots of its type (BLOCKS_3, BLOCKS_4): each robot in the file of
its first type among 3 and 4 (E11.7 point 1).

WHERE IT SITS
-------------
Not a stage: it holds the inputs of two builders. 01_schemas.py checks what they write; 02_composition.py draws types 3
and 4 over their robots in every file that holds one (E11.7 point 4).
"""
import importlib.util
import os
import re
import sys
from collections import defaultdict
from statistics import median

TOOLS = os.path.dirname(os.path.abspath(__file__))
if TOOLS not in sys.path:
    sys.path.insert(0, TOOLS)
from parts_taken_apart import *  # noqa: E402,F401,F403  (every shared name: the sheets, the template, the functions)
from parts_taken_apart import (DRIVER_AREA, DRIVER_BOARD_AREA, SHARED_CONSTANTS_FIRST,  # noqa: E402
                               SHARED_CONSTANTS_LAST, average_joints, block, estimate, joint, spread, template_block)


def _type_two():
    """Type 2's builder, imported once under its own name (its folder's name begins with a digit): its helpers and its
    robots, one copy."""
    name = 'make_parts_taken_apart_type_2'
    if name not in sys.modules:
        path = os.path.join(TOOLS, '2_full_scale_general_purpose_ai_research', 'make_parts_taken_apart.py')
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
    return sys.modules[name]


T2 = _type_two()
fitted, voltage_capacity, cables_by_height, screws = T2.fitted, T2.voltage_capacity, T2.cables_by_height, T2.screws
binocular, depth_camera, camera, lidar, imu = T2.binocular, T2.depth_camera, T2.camera, T2.lidar, T2.imu
microphones, speaker, base_lidar, base_depth_camera = T2.microphones, T2.speaker, T2.base_lidar, T2.base_depth_camera
thor, agx_orin, intel, orin_nx_boards, hands, grippers = T2.thor, T2.agx_orin, T2.intel, T2.orin_nx_boards, T2.hands, \
    T2.grippers
COMPUTER, POWER_BOARD, IMU_G, RK3588_BOARDS = T2.COMPUTER, T2.POWER_BOARD, T2.IMU_G, T2.RK3588_BOARDS
SIX_JOINT_HAND = T2.SIX_JOINT_HAND
FIT_KG, FIT_POWER = T2.FIT_KG, T2.FIT_POWER

# --- Texts of types 3 and 4 (E11.6) ---------------------------------------------------------------------------------
TEMPLATE_LABEL = "as types 3 and 4's seven robots with every joint on average"
TEMPLATE_SOURCES = ("no joint torques in its sources: its joint modules 22.4 / 44.7 / 67.1 % of its mass, split as "
                    "types 3 and 4's seven robots with every joint (H2, Kuavo 5, Luna, MagicBot Gen1, Adam Lite, Adam SP, "
                    'Atom) are on average, their hands left out (E11.6 point 1)')
WHEELED_LABEL = "as types 3 and 4's three robots on wheels, split as type 2's four"
WHEELED_SOURCES = ("its maker gives no joint's torque or mass: its joint modules 6.95 / 13.9 / 20.85 % of its mass "
                   "(types 3 and 4's three robots on wheels with every joint: AI Worker, RB-Y1, Vega), split as type "
                   "2's four on average, their hands, wheels, steering and lift left out (E11.6 point 1)")
COMPUTER_NOT_NAMED = 'Computer board (not named)'
COMPUTER_SOURCE = "its maker names none: one computer board, as the X1's and N1's (E11.6 point 7)"
CELLS_NOT_STATED = ('E', 'NMC cylindrical, E: no chemistry stated (E11.6 point 6)')
IMU_NOT_NAMED = ('Motion sensor (IMU)', 1, 'Boards', 'Torso', IMU_G, 'E',
                 "its maker names none: one, as every robot that walks or carries arms balances by one; as the G1's "
                 '(E11.6 point 8)', [('IMU', 1)])
SHELL_NOT_STATED = ('Shell: plastics', 'not stated; plastics, 11.5 % of the robot (E11.6 point 10)')
FRAME_NOT_STATED = ('Frame', 'Aluminium alloys', 'not stated; aluminium, the remainder (E11.6 point 10)')
# A robot whose maker gives energy but no voltage: 48 V (E), as type 2's Tlibot T1 and Tien Kung 3.0 (E8.3 point 6).
VOLTS_NOT_STATED = 48
# The share of its mass and the energy per kg of robot of a robot of a template, by these names (01 and 02 read them so:
# 01's template_quantity, "…, types 3 and 4").
JOINT_SHARE_34 = 'Joint modules, share of the robot mass, types 3 and 4'
ENERGY_PER_KG_34 = 'Battery energy per kg of robot, types 3 and 4'
ON_WHEELS = ', on wheels'

# --- The seven robots on legs and the three on wheels of types 3 and 4 with every joint (E11.6 point 1) ---------------
# Batch 1's Adam Lite and Adam SP: each joint its actuator's stated mass (the wiki's actuator pages, "Weight/kg"),
# ± 5 % (S); the shoulders' PND-50-14A, whose page gives no mass, E6.8's fit at its "Maximum torque" 60 N·m (E).
PND_SOURCES = ('PNDw: each joint its actuator (the Adam line\'s table) and the actuator\'s "Weight/kg" ± 5 % (S); the '
               'shoulders\' PND-50-14A no mass on its page: the fit at its 60 N·m, 0.0689 kg × torque^0.566, half to 1.5 '
               'times (E) (E11.6 point 2)')


def actuator(name: str, count: int, torque: float, kg: float, heat: str, region: str) -> tuple:
    """A joint of the Adam line: its actuator's stated maximum torque (N·m) and mass (kg), ± 5 % (S)."""
    return joint(name, count, torque, spread(kg), heat, region)


ADAM_LEGS_WAIST = [
    actuator('Hip pitch', 2, 340, 4.0, 'Hips', 'Legs'), actuator('Hip roll', 2, 180, 1.5, 'Hips', 'Legs'),
    actuator('Hip yaw', 2, 48, 1.0, 'Hips', 'Legs'), actuator('Knee', 2, 340, 4.0, 'Knees', 'Legs'),
    actuator('Ankle pitch', 2, 46, 0.7, 'Ankles', 'Legs'), actuator('Ankle roll', 2, 46, 0.7, 'Ankles', 'Legs'),
    actuator('Waist roll', 1, 89, 1.0, 'Waist', 'Torso'), actuator('Waist pitch', 1, 89, 1.0, 'Waist', 'Torso'),
    actuator('Waist yaw', 1, 89, 1.0, 'Waist', 'Torso')]
ADAM_ARMS = [
    fitted('Shoulder pitch', 2, 60, 'Shoulders', 'Arms'), fitted('Shoulder roll', 2, 60, 'Shoulders', 'Arms'),
    actuator('Shoulder yaw', 2, 17.5, 0.4, 'Shoulders', 'Arms'), actuator('Elbow', 2, 17.5, 0.4, 'Elbows and wrists',
                                                                          'Arms'),
    actuator('Wrist yaw', 2, 6.2, 0.3, 'Elbows and wrists', 'Arms')]
ADAM_WRISTS = [actuator('Wrist pitch', 2, 6.4, 0.2, 'Elbows and wrists', 'Arms'),
               actuator('Wrist roll', 2, 6.4, 0.2, 'Elbows and wrists', 'Arms')]
ADAM_BATTERY = voltage_capacity(39.6, 'PNDw "1172W·h capacity, 46.2V max voltage": 11 cells at 4.2 V, 3.6 V each nominal '
                                '(E11.6 point 6)', 1172 / 39.6, 'PNDw "1172W·h": 1172 / 39.6 V', label='S, E')
ADAM_CELLS = ('E', 'NMC cylindrical, E: no chemistry stated (E11.6 point 6)')


def adam(model: str, kg: float, model_kg: float, joints: list, more: dict) -> dict:
    """An Adam of PNDbotics (E11.1, E11.6 point 2): its wiki's mass the mode, its model file's the min, ± 1 kg above."""
    return block(
        f'PNDbotics Adam {model}', 'PNDbotics', 1.67, kg,
        f'PNDw (PNDbotics\' wiki: "1.67m", "{kg:g}kg"), PNDu (its model, {model_kg} kg); E11.1',
        ((model_kg, kg, kg + 1), 'S', f'PNDw "{kg:g}kg"; PNDu its model {model_kg} kg the min; 1 kg above (E11.2 point 1)'),
        joints, joint_sources=PND_SOURCES, **ADAM_BATTERY, **with_defaults(1.67, kg, dict(more, cells=ADAM_CELLS)))


def with_defaults(height: float, kg: float, more: dict) -> dict:
    """What a block of types 3 and 4 has unless `more` says otherwise (E11.6 points 6 to 10)."""
    defaults = dict(cells=CELLS_NOT_STATED, sensors=[IMU_NOT_NAMED], cables=cables_by_height(height),
                    screws=screws(kg), shell=SHELL_NOT_STATED, frame=FRAME_NOT_STATED,
                    boards=[(COMPUTER_NOT_NAMED, 1, 'Boards', 'Torso', COMPUTER, 'ITC', 'E', COMPUTER_SOURCE),
                            POWER_BOARD])
    defaults.update(more)
    return defaults


PNDBOTICS_ADAM_LITE = adam('Lite', 60, 58.48, ADAM_LEGS_WAIST + ADAM_ARMS, dict(
    boards=[intel('Intel i7', 'PNDw "NUC12WSKi7 for motion control" (12th Gen Intel Core i7-1260P)'), POWER_BOARD]))
PNDBOTICS_ADAM_SP = adam('SP', 62, 60.25, ADAM_LEGS_WAIST + ADAM_ARMS + ADAM_WRISTS + [SIX_JOINT_HAND], dict(
    boards=[intel('Intel i7', 'PNDw "NUC12WSKi7 for motion control"'),
            *orin_nx_boards('PNDw "NVIDIA Jetson Orin NX 16GB"'), POWER_BOARD],
    sensors=[depth_camera('PNDw "Intel Realsense D455"'), IMU_NOT_NAMED]))
# The Atom (DOBOT), register 45: by the same function as type 2's Atom Max block (E7.5; E11.7 point 3), DOBOT's same
# model: its joints (type 2's ATOM_JOINTS) and its mass as type 2's reading of those files. Named by its height, as
# 'DOBOT Atom' holds the Atom Max's rows since E7.3 and a name holds no brackets (the register's test).
DOBOT_ATOM = block(
    'DOBOT Atom 153 cm', 'DOBOT', 1.53, None,
    'DOBa (DOBOT: "28 upper-body degrees of freedom", "binocular RGB vision"), ATu (its model); E11.1',
    ((57.91, 58.91, 61.81), 'S, E', "ATu: its whole-body model 58.91 kg the mode, its legs model 61.81 kg the max, as "
                                    "type 2's Atom Max (E7.5 point 5; E11.7 point 3); DOBOT states none; the "
                                    "register's 62 kg reported"),
    T2.ATOM_JOINTS, joint_sources=T2.DOBOT_ATOM['joint_sources'],
    **with_defaults(1.53, 58.91, dict(sensors=[binocular('DOBa "binocular RGB vision"'),
                                                                     IMU_NOT_NAMED])))

SEVEN = [T2.UNITREE_H2, T2.LEJU_KUAVO_5, T2.LIMX_LUNA, T2.MAGICLAB_MAGICBOT, PNDBOTICS_ADAM_LITE, PNDBOTICS_ADAM_SP,
         DOBOT_ATOM]


def body(b: dict) -> list:
    """A block's body joints: its hands and grippers left out (E7.4)."""
    return [j for j in b['joints'] if not j[0].startswith(('Hand', 'Gripper'))]


def median_share(blocks: list) -> float:
    """The median over `blocks` of their body joints' modules' share of the robot's mass, at the modes (E11.6 point 1);
    the template's mode, checked by tests/test_make_parts_taken_apart.py."""
    return median(sum(j[1] * j[4][1] for j in body(b)) / b['mass'][0][1] for b in blocks)


AVERAGE_JOINTS = average_joints([dict(b, joints=body(b)) for b in SEVEN], TEMPLATE_LABEL)
# On wheels: E9.6's split of type 2's four (its rows), named as types 3 and 4's (what they stand for here).
WHEELED_JOINTS = [(row[0].replace(T2.WHEELED_TEMPLATE_LABEL, WHEELED_LABEL),) + tuple(row[1:])
                  for row in T2.WHEELED_AVERAGE_JOINTS]
# A robot whose maker names no degrees of freedom: the median of the seven's body joints, for its encoders and
# connectors only (E); on wheels type 2's (E9.6: 18).
JOINTS_MEDIAN = int(median(sum(j[1] for j in body(b)) for b in SEVEN))
WHEELED_JOINTS_MEDIAN = T2.WHEELED_JOINTS_MEDIAN

TYPES_34_SHARED = [
    # Types 3 and 4's own templates (E11.6 point 1, agreed 2026-10-30, "Yes, agree E11.6"); 01 and 02 read them by these
    # names (E11.7 point 2).
    ('all', JOINT_SHARE_34, 0.2235, 0.447, 0.6705, 'share', 'E',
     "types 3 and 4's seven robots on legs with every joint (H2 44.7, Kuavo 5 34.1, Luna 41.5, MagicBot Gen1 46.6, Adam "
     'Lite 53.0, Adam SP 52.6, Atom 38.0 %): median 44.7 %; half to 1.5 times (E11.6 point 1)'),
    ('all', JOINT_SHARE_34 + ON_WHEELS, 0.0695, 0.139, 0.2085, 'share', 'E',
     "types 3 and 4's three robots on wheels with every joint (AI Worker 14.3, RB-Y1 A 13.9, Vega 13.2 %): median "
     '13.9 %; half to 1.5 times (E11.6 point 1)'),
    ('all', ENERGY_PER_KG_34, 7.335, 14.67, 22.005, 'Wh/kg', 'E',
     "the 16 robots of types 3 or 4 on legs with a stated energy and mass: 10.14 to 28.07, median 14.67; half to 1.5 "
     'times (E11.6 point 1)'),
    ('all', ENERGY_PER_KG_34 + ON_WHEELS, 5.42, 10.84, 16.26, 'Wh/kg', 'E',
     "the 14 robots of types 3 or 4 on wheels with a stated energy and mass: 4.62 to 22.86, median 10.84; half to 1.5 "
     'times (E11.6 point 1)'),
    ('all', DRIVER_AREA, *DRIVER_BOARD_AREA, 'cm2', 'W, E',
     "the G1's weighed small joint's driver board, as in types 1 and 2 (E2.8)"),
    ('all', 'Lift column, share of the robot mass, on wheels', 0.0995, 0.199, 0.2985, 'share', 'E',
     "the AI Worker's lift link in its model, 17.9 of 90 kg; half to 1.5 times (E9.6 point 7; E11.6 point 11)"),
]


# --- The kinds of block of types 3 and 4 ----------------------------------------------------------------------------
def template(name: str, maker: str, height: float, stated: float | None, mass: tuple, joints_stated: int,
             computer: str = COMPUTER_NOT_NAMED, **more) -> dict:
    """A robot of types 3 and 4 whose maker gives no joint torques: the shared template_block() with types 3 and 4's
    texts and defaults (E11.6 point 3). `joints_stated` counts its body joints and its hands (one each) for its
    encoders and connectors."""
    joint_sources = more.pop('joint_sources', TEMPLATE_SOURCES)
    return template_block(name, maker, height, stated, mass, joints_stated, computer, computer_source=COMPUTER_SOURCE,
                          joint_sources=joint_sources, default_sources='HG (the register); E11.1, E11.6',
                          **with_defaults(height, mass[0][1], more))


def wheeled(name: str, maker: str, height: float, stated: float | None, mass: tuple, body_joints: int, *, sources: str,
            driven: int = 2, caster_count: int = 2, lift: bool = False, added: tuple = (), **more) -> dict:
    """A robot of types 3 and 4 on wheels whose maker gives no joint's torque or mass (E11.6 points 3 and 11): the
    template on wheels for its body joints, its hands or grippers (`added`), its drive wheels' hub motors by its mass
    per driven wheel (E9.6 point 4), two casters unless more is known, its lift column a share of its mass, its battery
    in its base. Its hands or grippers count one each for its encoders and connectors."""
    wheel, why = T2.hub_motors(driven, mass[0][1])
    joints = [wheel] + ([T2.lift_motor()] if lift else [])
    return template(name, maker, height, stated, mass, body_joints + sum(h[1] for h in added) + driven + int(lift),
                    sources=sources, averaged=WHEELED_JOINTS,
                    joint_sources=WHEELED_SOURCES + f'; its {driven} drive wheels each a hub motor as {why}, half to 1.5 '
                                                    'times (E9.6 point 4)' + ("; its lift motor as ROBOTIS's (E)"
                                                                              if lift else ''),
                    added_joints=list(added) + joints, battery_region='Base',
                    parts=([T2.casters(caster_count)] if caster_count else []) + more.pop('parts', []),
                    lift_column=T2.LIFT_BY_SHARE if lift else None, **more)


def catalogue(kg: float, why: str) -> tuple:
    """The register's (the catalogue's) mass ± 1 kg, labelled as the catalogue's, for a robot whose maker gives none
    (E11.2 point 2)."""
    return (kg - 1, kg, kg + 1), 'S', f'HG "{kg:g}" (the register, the catalogue\'s); ± 1 kg; {why} (E11.2 point 2)'


def makers(kg: float, source: str) -> tuple:
    """The maker's mass the mode, ± 1 kg (E11.2 point 1)."""
    return (kg - 1, kg, kg + 1), 'S', f'{source}; ± 1 kg (E11.2 point 1)'


def energy(wh: float, source: str) -> dict:
    """A battery whose maker states its energy but not its voltage: 48 V (E), its capacity the energy over it (S, E)."""
    return voltage_capacity(VOLTS_NOT_STATED, f'{source.split()[0]} states no voltage: 48 V, as type 2\'s Tlibot T1 '
                                              '(E11.6 point 6)', wh / VOLTS_NOT_STATED,
                            f'{source}: {wh:g} / 48 V', label='S, E')


SIX_HANDS = SIX_JOINT_HAND
AGILE_HAND = joint('Hand (Agile Hand)', 2, None, estimate(1.5), 'Elbows and wrists', 'Arms', size='small')
MAGNESIUM_FRAME_A3 = ('Frame', 'Magnesium alloys', 'AGA3p "magnesium alloy, titanium alloy, and TPU flexible materials": '
                                            'magnesium alloy; its titanium and TPU not drawn (no share stated); the '
                                            'remainder (E11.6 point 10, question 4)')
MAGNESIUM_FRAME_A3U = ('Frame', 'Magnesium alloys', 'AGA3Up "Magnesium alloy + carbon-fiber nylon": magnesium alloy; the '
                                             'remainder (E11.6 point 10)')

# --- Batch 1, robot by robot (E11.6), in the register's order --------------------------------------------------------
ONE_X_NEO = template(
    '1X NEO', '1X Technologies', 1.676, 29.9, makers(29.9, '1XN "66 lbs" (29.9 kg)'), 31 + 2,
    'Compute module, NVIDIA Jetson Thor', sources='1XN (1X: "5\'6”", "66 lbs", DoF hands "22x2", arms "7x2", neck "3", '
                                                  'spine "2", legs "6x2"); E11.1',
    added_joints=[hands(22)], **energy(842, '1XN "Capacity 842 Wh"'),
    boards=thor('1XN "1X NEO Cortex (Nvidia Jetson Thor)"') + [POWER_BOARD],
    sensors=[camera('Camera, fisheye', 2, 'Head', '1XN "Dual 8.85MP 90Hz Stereo Fisheye"'),
             microphones('1XN "4 beamforming microphones"'), speaker('1XN "3 stage speaker in pelvis and chest area"'),
             IMU_NOT_NAMED])
NEURA_4NE1_GEN_3 = template(
    'NEURA 4NE1 Gen 3', 'NEURA Robotics', 1.80, 80, makers(80, 'N4G3 "Weight 80 kg" (its datasheet, "4NE1 Gen 3")'),
    43 + 2, sources='N4G3 (NEURA: "55 Degrees of Freedom", "Hands (DoF) 12", "180 cm"), N4; E11.3',
    added_joints=[SIX_HANDS])
NEURA_4NE1_GEN_35 = template(
    'NEURA 4NE1 Gen 3.5', 'NEURA Robotics', 1.80, 80, makers(80, 'N4G35 "Weight 80 kg" (its datasheet)'), 43 + 2,
    'Compute module, NVIDIA Jetson Thor', sources='N4G35 (NEURA: "Own Hands (DoF) 12", "180 cm", "Thor T5000"); E11.3',
    added_joints=[SIX_HANDS], boards=thor('N4G35 "NVIDIA Thor T5000"') + [POWER_BOARD])
NEURA_4NE1_GEN_4 = template(
    'NEURA 4NE1 Gen 4', 'NEURA Robotics', 1.80, 64,
    ((63, 64, 65), 'S, E', 'N4 "20% lighter than the generation before": 80 kg less 20 %, 64 kg (arith.); its box\'s '
                           '"Weight (kg) 80" reported; ± 1 kg (E11.5, decided "Yes, 64 kg")'),
    43 + 2, sources='N4 (NEURA: "Height (cm) 180", "Advanced hands"), N4G35; E11.1, E11.5', added_joints=[SIX_HANDS])
AGIBOT_A2 = template(
    'AgiBot A2', 'AgiBot', 1.69, 69, makers(69, 'AGA2p "Weight 69 kg"'), 28 + 2,
    sources='AGA2p (AgiBot: "Weight 69 kg", "Height 169 cm", "Battery 700 wh"), AGA2U (its A2 Ultra: "6-DOF Dexterous '
            'Hand"); E11.4', added_joints=[SIX_HANDS], **energy(700, 'AGA2p "Battery 700 wh"'))
AGIBOT_A2_MAX = template(
    'AgiBot A2 Max', 'AgiBot', 1.78, 85, catalogue(85, 'AgiBot states none (E11.4)'), JOINTS_MEDIAN,
    sources='HG (the register); "AGIBOT A2-Max" only in AgiBot\'s inquiry form (E11.1, E11.4)')
AGIBOT_A3_ULTRA = template(
    'AgiBot A3 Ultra', 'AgiBot', 1.74, 60, makers(60, 'AGA3Um "Weight 60 KG"'), 31 + 2,
    'Computer board, RK3588', sources='AGA3Um (its user manual: neck 2, arms 7 × 2, waist 3, legs 6 × 2, hands "10 '
                                      '(optional, up to 20 DOF)"), AGA3Up; E11.3',
    added_joints=[hands(10)], **energy(1152, 'AGA3Um "Battery Capacity 1152 W·h"'),
    boards=[*RK3588_BOARDS, *RK3588_BOARDS, *thor('AGA3Um "NVIDIA Thor"'), POWER_BOARD],
    sensors=[lidar('AGA3Um "3D LiDAR"'), depth_camera('AGA3Um, AGA3Up RGB-D in chest, terrain and knee', 3),
             binocular('AGA3Um "RGB Binocular Camera"'), camera('Camera, fisheye', 3, 'Head', 'AGA3Up "3 wide-angle '
                                                                                            'fisheye cameras"'),
             microphones('AGA3Um "Front and Rear 8-Microphone Array"'), IMU_NOT_NAMED],
    frame=MAGNESIUM_FRAME_A3U)
ANDROMEDA_ABI = wheeled(
    'Andromeda Abi', 'Andromeda Robotics', 1.20, None, catalogue(50, 'Andromeda states none (E11.4)'),
    WHEELED_JOINTS_MEDIAN, sources='ABI (Andromeda: no figures), HG (the register: wheels); E11.1')
HEXAGON_AEON = template(
    'Hexagon AEON', 'Hexagon', 1.65, 60, makers(60, 'HEX "Weight: 60kg"'), 34,
    'Compute module, NVIDIA Jetson Thor', sources='HEX (Hexagon: "Height: 165cm", "Degrees of freedom: 34", "5 hours"), '
                                                  'HEXh (its NVIDIA Jetson Thor); E11.1',
    boards=thor('HEXh "We built a custom receiver to connect to NVIDIA Jetson Thor"') + [POWER_BOARD],
    sensors=[depth_camera('HEXh "cameras and depth sensors"'), camera('Camera', 1, 'Head', 'HEXh "cameras"'),
             imu('HEXh "inertial measurement units (IMUs)"')])
AGIBOT_A3 = template(
    'AgiBot A3', 'AgiBot', 1.73, 55, makers(55, 'AGA3m "Weight 55 KG"'), 31,
    'Computer board, RK3588', sources='AGA3m (its user manual: "Active Degrees of Freedom 31"), AGA3p; E11.3',
    **energy(1152, 'AGA3m "Battery Capacity 1152 W·h"'), boards=[*RK3588_BOARDS, *RK3588_BOARDS, POWER_BOARD],
    sensors=[binocular('AGA3m "RGB Binocular Camera"'), microphones('AGA3m "Front and Rear 8-Microphone Array"'),
             IMU_NOT_NAMED], frame=MAGNESIUM_FRAME_A3)


def agibot_x2(ultra: bool) -> dict:
    """The X2 in two versions, X2 and X2 Ultra, each as often (decided, E11.2 point 3)."""
    name, kg, dof = ('AgiBot X2 Ultra', 39, 30) if ultra else ('AgiBot X2', 35, 25)
    boards = [*RK3588_BOARDS, *RK3588_BOARDS] + (orin_nx_boards('AGX2 "Orin NX (157 TOPS)"') if ultra else [])
    sensors = ([lidar('AGX2 "3D LiDAR" (Ultra)'), depth_camera('AGX2 "RGB-D Camera" (Ultra)'),
                binocular('AGX2 "Front dual RGB" (Ultra)')] if ultra else []) + [
        camera('Camera, interactive', 1, 'Head', 'AGX2 "Interactive RGB camera"'),
        microphones('AGX2 "Microphone array"'), IMU_NOT_NAMED]
    return template(name, 'AgiBot', 1.31, kg, makers(kg, f'AGX2 "Approx.{kg}kg" ({name})'), dof, 'Computer board, RK3588',
                    sources=f'AGX2 (AgiBot: "Total Degrees of Freedom" {dof}, "Approx.500Wh", "RK3588 ×2"); E11.1',
                    **energy(500, 'AGX2 "Approx.500Wh"'), boards=boards + [POWER_BOARD], sensors=sensors)


AGIBOT_X2, AGIBOT_X2_ULTRA = agibot_x2(False), agibot_x2(True)
AGILE_ONE = template(
    'Agile Robots Agile One', 'Agile Robots', 1.74, None, catalogue(69, 'Agile Robots states none; heise 69 kg at its '
                                                                        'launch (E11.4)'), JOINTS_MEDIAN + 2,
    sources='AGR1 (Agile Robots: "modular fingers, 21 joints", "cameras, LiDARs"), AGRh (the Agile Hand), HG; E11.1',
    added_joints=[AGILE_HAND],
    sensors=[camera('Camera', 1, 'Head', 'AGR1 "intelligent cameras"'), lidar('AGR1 "LiDARs"'), IMU_NOT_NAMED])
AIDOL = template(
    'AIDOL Lab AIDOL', 'AIDOL Lab', 1.86, 95, makers(95, 'AID "95 кг"'), 67,
    'Compute module, GPU-based (as an AGX Orin)', sources='AID (AIDOL: "67" DoF, "186 см", "до 6 часов"); E11.1',
    boards=agx_orin('AID "вычислительному модулю на основе графического процессора" (a GPU-based module; E: as an AGX '
                    'Orin)', label='E') + [POWER_BOARD])
AEI_ALICE_M1 = wheeled(
    'AeiROBOT ALICE M1', 'AeiROBOT', 1.55, 97, makers(97, 'AEIM1 "130 - 180cm / 97kg"'), 19,
    sources='AEIM1 (AeiROBOT: "DoF 31 Waist(3), Arm(7*2), Head(2), Hand(6*2)", "Mobile platform"; its height the middle '
            'of 1.3 to 1.8 m, E); E11.1', added=(SIX_HANDS,),
    boards=agx_orin('AEIM1 "AFE-R360 | NVIDIA AGX Orin"') + [POWER_BOARD],
    sensors=[binocular('AEIM1 "Stereo Camera"'), lidar('AEIM1 "3D Lidar"'), imu('AEIM1 "IMU"')])
TEKNTRASH_ALPHA = template(
    'TeknTrash ALPHA', 'TeknTrash', 2.00, None, catalogue(90, "TeknTrash's site refused (E11.1, E11.4)"), JOINTS_MEDIAN,
    sources='HG (the register); on legs, as no source states wheels (E11.6 question 2)')


# AlphaBot 2: its maker's peaks by E6.8's fit (its folding legs' knee and ankle, its waist, its neck), its arms (7 each,
# not given) the wheeled template's arms' share of its mass split per joint (E: shoulders 38.3 %, elbows and wrists
# 33.6 % of 13.9 % of 135 kg, E11.6 question 3), two grippers, two drive wheels and two casters, 48 V × 30 Ah.
def alphabot_arm_joints() -> list:
    """The AlphaBot 2's 14 arm joints (E11.6 question 3): its mass at the mode times the template on wheels' share
    (13.9 %) and its arms' split (shoulders, elbows and wrists), per joint, half to 1.5 times (E)."""
    modules = 135 * 0.139
    shoulders = sum(r[7] for r in T2.WHEELED_AVERAGE_JOINTS if r[0].startswith('Shoulder')) * modules / 6
    elbows = sum(r[7] for r in T2.WHEELED_AVERAGE_JOINTS if r[0].startswith('Elbow')) * modules / 8
    return [joint('Shoulder', 6, None, estimate(round(shoulders, 3)), 'Shoulders', 'Arms', size='large'),
            joint('Elbow and wrist', 8, None, estimate(round(elbows, 3)), 'Elbows and wrists', 'Arms', size='small')]


AI2_ALPHABOT_2 = block(
    'AI² Robotics AlphaBot 2', 'AI² Robotics', 1.80, 135,
    'AI2 (AI² Robotics: "a wheeled dual-arm humanoid robot", "22 degrees of freedom (excluding end effectors)", its '
    'joints\' peak torques, "Battery 48V 30Ah"); E11.1',
    makers(135, 'AI2 "135kg (standard configuration)"'),
    [fitted('Neck pitch', 1, 3.3, 'Elbows and wrists', 'Head'), fitted('Neck yaw', 1, 3.3, 'Elbows and wrists', 'Head'),
     fitted('Waist yaw', 1, 66, 'Waist', 'Torso'), fitted('Waist pitch', 1, 207, 'Waist', 'Torso'),
     fitted('Knee', 1, 436, 'Knees', 'Legs'), fitted('Ankle', 1, 436, 'Ankles', 'Legs'), *alphabot_arm_joints(),
     grippers(), T2.hub_motors(2, 135)[0]],
    joint_sources='AI2 its peaks, the fit 0.0689 kg × torque^0.566, half to 1.5 times (E); its arms the template on '
                  "wheels' arms (E11.6 question 3); its two drive wheels hub motors (E9.6 point 4)",
    battery_region='Base', **voltage_capacity(48, 'AI2 "Battery 48V 30Ah"', 30, 'AI2 "48V 30Ah"'),
    parts=[T2.casters(2)],
    **with_defaults(1.80, 135, dict(
        boards=agx_orin('AI2 "NVIDIA Orin AGX 64G"') + [POWER_BOARD],
        sensors=[depth_camera('AI2 "Realsense D435" in head, chest and back', 3),
                 depth_camera('AI2 "Realsense D405" at the arms\' ends', 2),
                 base_depth_camera('AI2 "RGBD Camera 1" (chassis)', 1), base_lidar('AI2 "2D LiDAR"'),
                 microphones('AI2 "MIC array: linear MIC*4"'), IMU_NOT_NAMED])))
ANIGON = wheeled(
    'Anigon', 'Anigon Humanoid Robotics', 1.89, None, catalogue(120, 'Anigon states none (E11.4)'), 28,
    sources='ANI (Anigon: "Height 189 cm", "Full Body 28 DoF", "Mobile Base: Adaptive Lifting", "Dual Hot-Swap '
            'Batteries"), ANIt; E11.1', added=(SIX_HANDS,), lift=True)
APPTRONIK_APOLLO = template(
    'Apptronik Apollo', 'Apptronik', 1.73, None, catalogue(72, 'Apptronik states none; Engadget "160-lb" at its launch '
                                                               '(E11.4)'), JOINTS_MEDIAN,
    sources='APT (Apptronik: its page answered 404), HG (the register); E11.1')
APPTRONIK_APOLLO_2 = template(
    'Apptronik Apollo 2', 'Apptronik', 1.73, None, catalogue(75, 'Apptronik states none (E11.4)'), JOINTS_MEDIAN,
    sources='APT2 (Apptronik: "A bipedal configuration … while a wheeled base", "Swappable batteries"), HG; on legs '
            '(E11.6 question 2)')
BOSTON_DYNAMICS_ATLAS = template(
    'Boston Dynamics Atlas', 'Boston Dynamics', 1.90, 90, makers(90, 'BDA, BDAs "Weight 90 kg"'), 30 + 2,
    'Compute module, NVIDIA Jetson Thor',
    sources='BDA, BDAs (Boston Dynamics: "Height 1.9 m", "Degrees of Freedom 56", "Tactile fingers and palm", "Battery '
            'Life 4 hrs"), BDh (its hands: "13 degrees of freedom (DOF), directly actuated"; its body 56 less 2 × 13, '
            'arith.), BDn ("NVIDIA Jetson Thor"); E11.3, E16.2',
    # Since types 5 and 6's entry (E16.2, agreed 2026-11-01, "Yes, agree both"): its hands the GR3's 13 joints each,
    # its computer its maker's Jetson Thor, its cells NMC as an outlet names them (BTN, second-hand).
    added_joints=[hands(13)], boards=thor('BDn "NVIDIA Jetson Thor computing platform"') + [POWER_BOARD],
    cells=('S, E', 'NMC cylindrical: BTN "46-series ternary cells" (industry sources, second-hand)'))
VBOT_ATOM = template(
    'Vbot ATOM', 'Vbot', 1.60, None, catalogue(50, 'Vbot states none; Xinhua 1.6 m, 31 body DoF (E11.4)'), 31,
    sources='XHA (Xinhua at its launch: "160cm 身高", "31 个本体自由度"), VBOT (its site: a robot dog only), HG; E11.4')
NEUBILITY_BILLI = wheeled(
    'NEUBILITY Billi', 'NEUBILITY', 1.497, None, catalogue(110, 'NEUBILITY states none (E11.4)'),
    WHEELED_JOINTS_MEDIAN, sources='NEU (NEUBILITY: "Hybrid humanoid combining mobility and manipulation"), HG; E11.1')
BORG_01 = template(
    'Borg Robotics Borg 01', 'Borg Robotics', 1.73, None, catalogue(62, 'Borg states none ("IN DEVELOPMENT") (E11.4)'),
    JOINTS_MEDIAN, sources='BORG (Borg Robotics: "IN DEVELOPMENT"), HG; on legs (E11.6 question 2)')
WANDERCRAFT_CALVIN_40 = template(
    'Wandercraft CALVIN-40', 'Wandercraft', 1.70, None, catalogue(80, 'Wandercraft states none (E11.4)'),
    JOINTS_MEDIAN, sources='WAN (Wandercraft: "High-torque motors, high-strength structure", no figures), HG; E11.1')

# --- Joints from a stated joint (E12.5 point 2; Matthias, 2026-11-01: "Also the joints can be well estimated, based on
# the other joints", "Yes, agree E12.5") -------------------------------------------------------------------------------
# A robot whose maker states one joint's torque, or its largest, has every body joint from it: the stated torque is its
# largest joint's (on legs the knee, the largest in six of the seven robots with every joint; on wheels the waist, as in
# the Vega 1 Pro and the RB-Y1), every other joint's torque its kind's ratio to that joint in the robots with every
# joint (the median; their least and most bound its mass), each module E6.8's fit at its torque, half to 1.5 times (E).
# The ratios are computed here from those robots' blocks, one copy (E12.6 open point B): a change to their joints moves
# them. A kind's ratio is its largest joint's, so a kind's smaller joints (a shoulder's roll beside its pitch) come out
# heavier than they are: the joints overstated, the frame understated (an approximation, its direction stated).
LEG_KINDS = {'Hip pitch': ('Hips', 'Legs'), 'Hip roll': ('Hips', 'Legs'), 'Hip yaw': ('Hips', 'Legs'),
             'Knee': ('Knees', 'Legs'), 'Ankle pitch': ('Ankles', 'Legs'), 'Ankle roll': ('Ankles', 'Legs'),
             'Waist': ('Waist', 'Torso'), 'Shoulder': ('Shoulders', 'Arms'), 'Elbow': ('Elbows and wrists', 'Arms'),
             'Wrist': ('Elbows and wrists', 'Arms'), 'Head': ('Elbows and wrists', 'Head')}
WHEEL_KINDS = {'Waist': ('Waist', 'Torso'), 'Second waist': ('Waist', 'Torso'), 'Shoulder': ('Shoulders', 'Arms'),
               'Elbow': ('Elbows and wrists', 'Arms'), 'Wrist': ('Elbows and wrists', 'Arms'),
               'Head': ('Elbows and wrists', 'Head')}
# The joint names each kind of joint begins with in the blocks (a neck is the head's).
KIND_NAMES = (('hip pitch', 'Hip pitch'), ('hip roll', 'Hip roll'), ('hip yaw', 'Hip yaw'), ('knee', 'Knee'),
              ('ankle pitch', 'Ankle pitch'), ('ankle roll', 'Ankle roll'), ('waist', 'Waist'),
              ('shoulder', 'Shoulder'), ('elbow', 'Elbow'), ('wrist', 'Wrist'), ('head', 'Head'), ('neck', 'Head'))


def kind_of(name: str) -> str | None:
    """The kind of a body joint by its name ('Shoulder roll' -> 'Shoulder'); None for a wheel, steering or lift."""
    return next((kind for start, kind in KIND_NAMES if name.lower().startswith(start)), None)


def joint_ratios(blocks: list, on_wheels: bool) -> dict:
    """Over `blocks` (robots with every joint's torque), each kind's largest torque over the robot's reference joint
    (on legs its knee, on wheels its largest waist joint; on wheels also its second waist joint): kind -> (least,
    median, most)."""
    found = defaultdict(list)
    for b in blocks:
        torques = defaultdict(list)
        for j in body(b):
            if j[3] and kind_of(j[0]):
                torques[kind_of(j[0])] += [j[3]] * j[1]
        reference = max(torques['Waist'] if on_wheels else torques['Knee'])
        for kind, values in torques.items():
            found[kind].append(max(values) / reference)
        if on_wheels:
            found['Second waist'].append(sorted(torques['Waist'], reverse=True)[1] / reference)
    return {kind: (min(v), median(v), max(v)) for kind, v in found.items()}


LEG_RATIOS = joint_ratios(SEVEN, on_wheels=False)
WHEEL_RATIOS = joint_ratios([T2.DEXMATE_VEGA, T2.RAINBOW_RBY1_A], on_wheels=True)
JOINT_NAME = {'Second waist': 'Waist 2'}   # a second waist joint's name (02 knows a joint by its first word)


def from_stated_joint(torque: float, counts: dict, on_wheels: bool = False, fit=None) -> list:
    """Every body joint of a robot from its one stated joint (`torque`, N·m, its largest; E12.5 point 2), `counts`
    its joints per kind as its maker gives them: each kind's torque its median ratio times the stated one, its module
    half the fit at the least ratio, the fit at the median and 1.5 times the fit at the most (E). The fit E6.8's
    unless `fit` (one module's kg at a torque) gives its type's own: type 1's, the torque over 87.3 N·m/kg (E5.12
    point 4; E14.6 point 1)."""
    ratios, kinds = (WHEEL_RATIOS, WHEEL_KINDS) if on_wheels else (LEG_RATIOS, LEG_KINDS)
    fit = fit or (lambda t: FIT_KG * t ** FIT_POWER)   # E6.8: one module's kg at its torque
    rows = []
    for kind, count in counts.items():
        low, mid, high = ratios[kind]
        heat, region = kinds[kind]
        rows.append(joint(JOINT_NAME.get(kind, kind), count, round(torque * mid, 2),
                          (round(0.5 * fit(torque * low), 4), round(fit(torque * mid), 4),
                           round(1.5 * fit(torque * high), 4)), heat, region))
    return rows


def stated_joint_sources(code: str, words: str, torque: float, joint_name: str,
                         fit_words: str = 'the fit 0.0689 kg × torque^0.566') -> str:
    """The sources of a robot's joints from its one stated joint (E12.5 point 2); `fit_words` its type's fit."""
    return (f'{code} {words}: its {joint_name} {torque:g} N·m, every other joint by its kind\'s ratio in the robots '
            f'with every joint (E12.5 point 2), each module {fit_words} at the least, median and most ratio, half to '
            '1.5 times (E)')


LEGS_12 = {'Hip pitch': 2, 'Hip roll': 2, 'Hip yaw': 2, 'Knee': 2, 'Ankle pitch': 2, 'Ankle roll': 2}
CYBORG_HAND = joint('Hand (CYBORG, 16 joints)', 2, None, spread(0.75), 'Elbows and wrists', 'Arms', size='small')
CYBORG_HAND_SOURCE = 'CYBh "重量 750g", "16（主动6，欠驱动10）" (its hand page), ± 5 % (S)'


def lidars(source: str, count: int) -> tuple:
    """`count` LiDARs in the head, each as type 1's of no named model (E7.5 point 8)."""
    one = lidar(source)
    return (one[0], count) + one[2:]


def counted(sensor: tuple, count: int) -> tuple:
    """A sensor row (camera(), imu(), speaker() …) with `count` units."""
    return (sensor[0], count) + sensor[2:]


def named_board(what: str, source: str) -> tuple:
    """A computer board its maker names without a module (an eight-core or 16-core CPU board), as the X1's and N1's
    (E)."""
    return (f'Computer board, {what}', 1, 'Boards', 'Torso', COMPUTER, 'ITC', 'E',
            f"{source}; as the X1's and N1's computer board (E)")


# --- Batch 2, robot by robot (E12.5, agreed 2026-11-01, "Yes, agree E12.5"), in the register's order ------------------
def casbot_02(edu: bool) -> dict:
    """The CASBOT 02 and its EDU, each as often (E12.2 point 2): joints from its "最大关节扭矩150N.m" (E12.5 point 2),
    its battery 48 V × 10 Ah NMC, an AGX Orin and an RK3588."""
    name, kg = ('CASBOT 02 EDU', 52) if edu else ('CASBOT 02', 50)
    counts = {**LEGS_12, 'Waist': 1, 'Shoulder': 6, 'Elbow': 2, 'Wrist': 2, 'Head': 2}
    sensors = [depth_camera('CAS2 "RGB-D相机"' + (' (EDU 3)' if edu else ' 1'), 3 if edu else 1),
               binocular('CAS2 "双目相机 1"'), camera('Camera, fisheye', 2, 'Head', 'CAS2 "鱼眼 2"'),
               imu('CAS2 "IMU 1"'), microphones('CAS2 "麦克风阵列"'), speaker('CAS2 "扬声器"')]
    if edu:
        sensors.append(lidar('CAS2 "激光雷达 1" (EDU)'))
    return block(
        name, 'CASBOT', 1.63, kg, 'CAS2 (CASBOT: "身高约163cm", "整机重量 (带电池) 约50kg" / EDU "约52kg", legs 6 × 2, '
                                  'arms 5 × 2, waist 1, head 2, "灵巧手 11DoF (6支持)"); E12.1',
        makers(kg, f'CAS2 "约{kg}kg"'), from_stated_joint(150, counts) + [hands(6)],
        joint_sources=stated_joint_sources('CAS2', '"最大关节扭矩150N.m"', 150, 'knee'),
        **voltage_capacity(48, 'CAS2 "电池规格 48V 10Ah"', 10, 'CAS2 "48V 10Ah"'),
        **with_defaults(1.63, kg, dict(cells=('S, E', 'NMC cylindrical: CAS2 "三元锂电池" (ternary lithium, NMC)'),
                                       boards=agx_orin('CAS2 "RCU Orin AGX"') + RK3588_BOARDS + [POWER_BOARD],
                                       sensors=sensors)))


CASBOT_02, CASBOT_02_EDU = casbot_02(False), casbot_02(True)
CASIVISION_CASIVIBOT = wheeled(
    'CasiVision CASIVIBOT', 'CasiVision', 1.40, None, catalogue(55, 'CasiVision states none, its site shows inspection '
                                                                    'machines (E12.1, E12.4)'), 14,
    sources='CSV (CasiVision: no humanoid on its site), QBA (its launch: "工业具身质检机器人"), HG; E12.1, E12.4')
ELITE_CENTAUR_G1 = wheeled(
    'Elite Robots Centaur-G1', 'Elite Robots', 1.50, None,
    ((85, 260, 261), 'S', 'HG "260" (the catalogue) the mode, 1 kg above; OBC "WEIGHT 85 kg" (a database, Origin of '
                          'Bots) the min; Elite states none (E12.5 question 2)'), 20,
    sources='ELC (Elite: "全身自由度 20个", "全向移动底盘", "48V 40Ah", "单臂最大负载 5KG"), ELCr, OBC, HG; E12.1',
    driven=4, caster_count=0, **voltage_capacity(48, 'ELC "48V 40Ah 电池容量"', 40, 'ELC "48V 40Ah"'),
    sensors=[base_lidar('ELC "激光雷达"'), depth_camera('ELC "头部RGB-D相机"'),
             binocular('ELC "腕部双目微距相机", one at each wrist', 2), IMU_NOT_NAMED])
DONUT_CINNAMON_1 = template(
    'Donut Cinnamon 1', 'Donut Robotics', 1.70, 70, makers(70, 'DNT "Weight approx. 70kg"'), JOINTS_MEDIAN,
    sources='DNT (Donut Robotics: "Height approx. 170cm・Weight approx. 70kg", "bipedal"); E12.1')
LG_CLOID = wheeled(
    'LG CLOiD', 'LG Electronics', 1.43, None,
    ((60, 65, 70), 'S', 'HG "~60–70" (the catalogue\'s range); LG states none (E12.4)'), 14,
    sources='LGC (LG: arms "seven degrees of freedom each", "Five individually actuated fingers on each hand"), ENGc '
            '(a wheeled base; its torso 105 to 143 cm), HG; E12.1, E12.4', added=(hands(5),),
    sensors=[camera('Camera', 1, 'Head', 'LGC "a display, speaker, camera and an array of sensors"'),
             speaker('LGC "speaker"'), IMU_NOT_NAMED])
UBTECH_CRUZR_S2 = wheeled(
    'UBTECH Cruzr S2', 'UBTECH Robotics', 1.75, None, catalogue(150, 'UBTECH states none (E12.1, E12.4)'),
    WHEELED_JOINTS_MEDIAN, sources='UBS2 (UBTECH: its spec picture, "0-40cm lifting range", "gen-4 industrial '
                                   'dexterous hands"), HG; E12.1', added=(SIX_HANDS,), lift=True,
    sensors=[camera('Camera, fisheye', 2, 'Head', 'UBS2 "Fish-eye Camera*2"'),
             camera('Camera, RGB', 2, 'Head', 'UBS2 "RGB Camera*2"'), depth_camera('UBS2 "RGBD*1" (chest)'),
             base_depth_camera('UBS2 "RGBD*1" (base)'), base_lidar('UBS2 "Radar*1" front and back (E: as LiDAR)', 2),
             microphones('UBS2 "Microphone*1"'), counted(speaker('UBS2 "Speaker*2"'), 2), IMU_NOT_NAMED])
UBTECH_CRUZR_Y1 = wheeled(
    'UBTECH Cruzr Y1', 'UBTECH Robotics', 1.70, None, catalogue(90, 'UBTECH states none (E12.1, E12.4)'),
    WHEELED_JOINTS_MEDIAN, sources='UBY1 (UBTECH: its spec picture, "Lifting Module", "End Effectors × 2"), HG; E12.1',
    added=(grippers(),), lift=True,
    sensors=[depth_camera('UBY1 "Head RGBD", "Wrist RGBD × 2"', 3), base_lidar('UBY1 "LiDAR"'),
             base_depth_camera('UBY1 "Array TOF × 2" (E: as depth cameras)', 2),
             binocular('UBY1 "Binocular Cameras × 2"', 2), IMU_NOT_NAMED])


def cyborg_ro1(pro: bool) -> dict:
    """The CYBORG RO1, SE and PRO, each as often (E12.2 point 2): joints from its ">400N·m" (E12.5 point 2, its least),
    its hands as its maker weighs them, 48 V with its backup battery, an AGX Orin by its figures (E)."""
    name, kg, ah = ('CYBORG RO1 PRO', 80, 30) if pro else ('CYBORG RO1 SE', 75, 15)
    counts = {**LEGS_12, 'Waist': 2, 'Shoulder': 6, 'Elbow': 2, 'Wrist': 6, 'Head': 2}
    return block(
        name, 'Cyborg Robotics', 1.80, kg, 'CYBr (Cyborg: "1800*578*327mm", "体重 75kg（SE），80kg（PRO）", "总自由度 62": '
                                           'legs 6 × 2, waist 2, arms 7 × 2, hands 16; its head 2 the rest, arith.), '
                                           'CYBh; E12.1',
        makers(kg, f'CYBr "{kg}kg（{"PRO" if pro else "SE"}）"'), from_stated_joint(400, counts) + [CYBORG_HAND],
        joint_sources=stated_joint_sources('CYBr', '"最大关节扭矩 >400N·m"', 400, 'knee') + '; ' + CYBORG_HAND_SOURCE,
        **voltage_capacity(48, f'CYBr "48V{ah * 1000}mAH" and its backup "48V3500mAH"', ah + 3.5,
                           f'CYBr {ah} + 3.5 Ah (arith.)'),
        **with_defaults(1.80, kg, dict(
            boards=agx_orin('CYBr "感知算力 12核275TOPS" (E: the AGX Orin\'s figures)', label='E') + [POWER_BOARD],
            sensors=[camera('Camera, fisheye', 1, 'Head', 'CYBr "鱼眼相机 有" (its count not stated: one, E)'),
                     depth_camera('CYBr "RGBD深度相机 有" (one, E)'), lidar('CYBr "激光雷达 有"'),
                     imu('CYBr "IMU 有"'), microphones('CYBr "线性4麦"')])))


CYBORG_RO1_SE, CYBORG_RO1_PRO = cyborg_ro1(False), cyborg_ro1(True)
CYBORG_WO1 = block(
    'CYBORG WO1', 'Cyborg Robotics', 1.60, 170,
    'CYBw (Cyborg: "710*585*1600mm", "体重 170kg", "总自由度 53": chassis 3, waist 2, arms 7, hands 16; its head 2 the '
    'rest, arith.), CYBh; E12.1', makers(170, 'CYBw "体重 170kg"'),
    from_stated_joint(562, {'Waist': 1, 'Second waist': 1, 'Shoulder': 6, 'Elbow': 2, 'Wrist': 6, 'Head': 2},
                      on_wheels=True) + [CYBORG_HAND, T2.hub_motors(3, 170)[0]],
    joint_sources=stated_joint_sources('CYBw', '"最大关节扭矩 562N.m"', 562, 'waist') + '; ' + CYBORG_HAND_SOURCE +
    '; its base "底盘自由度 3": three drive wheels, hub motors by its mass per wheel (E9.6 point 4)',
    battery_region='Base',
    **with_defaults(1.60, 170, dict(
        boards=agx_orin('CYBw "感知算力 12核275TOPS" (E: the AGX Orin\'s figures)', label='E') + [POWER_BOARD],
        sensors=[camera('Camera', 1, 'Head', 'CYBw "单目相机 有"'), depth_camera('CYBw "RGBD深度相机 有" (one, E)'),
                 base_lidar('CYBw "激光雷达 有"'), imu('CYBw "IMU 有"'), microphones('CYBw "线性4麦"'),
                 speaker('CYBw "扬声器 有"')])))
SHARPA_D01 = wheeled(
    'Sharpa D01', 'Sharpa', 1.624, None,
    ((57.5, 75, 92.5), 'S, E', 'SHD "Weight (Without Chassis) ～40kg" and its chassis the DEUX\'s base, XYZ "35kg '
                               '(Base)", half to 1.5 times (E): 40 + 17.5 / 35 / 52.5 kg (E12.5 question 3)'), 22,
    sources='SHD (Sharpa: "1109-1624 mm (H)", "～40kg" without its chassis, "66 DoF" with its hands, "NVIDIA® Jetson '
            'Thor™"); E12.1', added=(hands(22),),
    boards=thor('SHD "NVIDIA® Jetson Thor™"') + [POWER_BOARD])
XYZ_DEUX = wheeled(
    'XYZ DEUX', 'XYZ', 1.55, 60, makers(60, 'XYZ "35kg (Base), 25kg (Robot), 60kg (Total)"'), 14,
    sources='XYZ (XYZ: "900mm (min) – 1550mm (max)", "7 DoF Arm × 2, 7 DoF Dexterous Hand × 2, 1 DoF Lift × 1, 3 DoF '
            'Mobile Base with Swerve Drive × 1", "24V, 60Ah (1,440Wh)"); E12.1, E12.4',
    caster_count=0, added=(hands(7), T2.steering(2)), lift=True,
    **voltage_capacity(24, 'XYZ "24V, 60Ah (1,440Wh)"', 60, 'XYZ "60Ah"'))
RICHTECH_DEX = wheeled(
    'Richtech Robotics Dex', 'Richtech Robotics', 1.37, None, catalogue(60, 'Richtech states none (E12.1, E12.4)'),
    WHEELED_JOINTS_MEDIAN, sources='RCH (Richtech: "4\'6\\" (mobile)", "NVIDIA Jetson Thor", "4 cameras (2 depth, 2 '
                                   'arm-mounted)", "LiDAR, RGB camera, depth camera, IMU"), RCHp, HG; E12.1',
    boards=thor('RCH "NVIDIA Jetson Thor"') + [POWER_BOARD],
    sensors=[depth_camera('RCH "4 cameras (2 depth, 2 arm-mounted)"', 2),
             camera('Camera, arm', 2, 'Arms', 'RCH "2 arm-mounted"'), base_lidar('RCH "LiDAR"'),
             camera('Camera, RGB', 1, 'Head', 'RCH "RGB camera"'), base_depth_camera('RCH "depth camera"'),
             imu('RCH "IMU"')])
BOSHIAC_DEXBOT = template(
    'BOSHIAC DexBot', 'BOSHIAC', 1.75, None,
    ((57, 58, 80), 'S', 'AIW "a weight of 58 kg" (the AI Wiki, its bipedal version) the mode, 1 kg below; HG "80" the '
                        'max; BOSHIAC\'s site not read (its certificate) (E12.5 question 2)'), 28,
    sources='AIW (the AI Wiki: "175 cm", "58 kg", "28 active joints"), HG; E12.4')
AGILITY_DIGIT = template(
    'Agility Digit', 'Agility Robotics', 1.75, None,
    ((62.5, 63.5, 76), 'S', 'ENGd "weighs around 140 lbs, including newly designed end effectors" (63.5 kg, arith.) '
                            'the mode, 1 kg below; HG "76" the max, its text\'s 65 kg between (E12.5 question 2)'), 28,
    sources='ENGd (Engadget at its launch, 2023-03-20: "5\'9\\"", "around 140 lbs"), AGL (Agility: no figures), HG; '
            'E12.4')
AGILITY_DIGIT_5 = template(
    'Agility Digit 5', 'Agility Robotics', 1.80, 129, makers(129, 'AGLh "Making a 129 kg dynamically stable '
                                                                           'robot"'), 30 + 2,
    'Compute module, NVIDIA IGX Thor (as a Jetson Thor)',
    sources='AGLh (Agility\'s CTO, 2026-10-23: "129 kg", "NVIDIA IGX Thor"), AGL5 ("Payload* 23kg/50lbs", "swappable '
            'gripper"), HG; E12.1, E12.4', added_joints=[grippers()],
    boards=thor('AGLh "NVIDIA IGX Thor" (as a Jetson Thor, E)') + [POWER_BOARD])
NOETIX_DORA = template(
    'Noetix Dora', 'Noetix Robotics', 1.00, None, catalogue(20, 'Noetix shows no Dora (E12.1, E12.4)'), 20,
    sources='NOE (Noetix: no Dora on its site), HG; its 120 N·m (second-hand) not used (E12.5 point 2)')


def deep_dr02(pro: bool) -> dict:
    """The DR02 and DR02 Pro, each as often (E12.2 point 2): its sheet's mass, its battery "20Ah（1440Wh）", its eight-
    core board, the Pro also an AGX Orin, a LiDAR and three depth cameras."""
    name, kg, dof = ('DEEP Robotics DR02 Pro', 78, 31) if pro else ('DEEP Robotics DR02', 68, 21)
    sensors = [camera('Camera, wide-angle', 1, 'Head', 'DPRs "广角相机 ×1"'), microphones('DPRs "麦克风阵列与扬声器 ×1"'),
               speaker('DPRs "扬声器"'), IMU_NOT_NAMED]
    boards = [named_board('8-core industrial processor', 'DPRs "八核64位工业级处理器×1 (16GB+128GB)"')]
    if pro:
        sensors[1:1] = [depth_camera('DPRs "深度相机 ×3" (Pro)', 3), lidar('DPRs "激光雷达 ×1" (Pro)')]
        boards += agx_orin('DPRs "AI处理器 ×1": "NVIDIA AGX Orin(275Tops)"')
    return template(
        name, 'DEEP Robotics', 1.80, kg, makers(kg, f'DPRs "整机重量（含电池）{kg}kg"'), dof,
        sources=f'DPRs (its product sheet: "站立高度 180cm", "{kg}kg", "主动自由度（总） {dof}", "20Ah（1440Wh）"), DPR; '
                'E12.3', **voltage_capacity(72, 'DPRs "电源接口(72V)": 1440 Wh / 20 Ah (arith.)', 20,
                                           'DPRs "电池容量 20Ah（1440Wh）"', label='S, E'),
        boards=boards + [POWER_BOARD], sensors=sensors)


DEEP_DR02, DEEP_DR02_PRO = deep_dr02(False), deep_dr02(True)
DUATIC_ALPHA = wheeled(
    'Duatic Alpha', 'Duatic', 1.75, None,
    catalogue(90, 'Duatic states none; OBA "around 90kg total" (a database); its arms DUAa "Total Weight 9.2 kg" each, '
                  'a check (E12.5 point 2)'), 18,
    sources='DUA (Duatic: its DXTR page, titled "Alpha Half-Humanoid Robot", "Hot swappable batteries", "48V (DC)"), '
            'DUAa, OBA, HG; E12.1, E12.4')
SIASUN_DUCO = wheeled(
    'Siasun DUCO', 'Siasun', 1.55, None, ((90, 100, 110), 'S', 'HG "~90–110" (the catalogue\'s range); Siasun states '
                                                                  'none (E12.4)'), 20,
    sources='DUC (Siasun\'s DUCO humanoid series: "BR-MA73A轮式人形机器人", its column BR-DR73 "24自由度", "伸缩高度约'
            '600mm", "Orin AGX 200/275 TOPS"), HG; E12.5 question 4', driven=4, caster_count=0, lift=True,
    boards=agx_orin('DUC "Orin AGX 200/275 TOPS"') + [POWER_BOARD],
    sensors=[depth_camera('DUC "头部深度相机"'), camera('Camera, surround', 2, 'Head', 'DUC "胸部前后环视相机" (in the chest; as the cameras, kind Head)'),
             microphones('DUC "麦克风整列"'), IMU_NOT_NAMED])
ELIXIS_BOARDS = [intel('Intel i7', 'ADV "MAIN CONTROL UNIT i7 PROCESSOR"'),
                 *agx_orin('ADV "INTELLIGENCE UNIT NVIDIA JETSON ORIN" (which Orin not said: an AGX Orin, E)',
                           label='E'), POWER_BOARD]
ADDVERB_ELIXIS = template(
    'Addverb Elixis', 'Addverb Technologies', 1.75, 75, makers(75, 'ADV "GROSS WEIGHT 75 KG"'), 41 + 2,
    sources='ADV (Addverb: "STANDING HEIGHT 1750 MM", "GROSS WEIGHT 75 KG", "DEGREES OF FREEDOM 41", "FIVE-FINGER '
            'DEXTEROUS OR PARALLEL-JAW GRIPPER": the gripper); E12.1', added_joints=[grippers()], boards=ELIXIS_BOARDS,
    sensors=[depth_camera('ADV "4x STEREO DEPTH CAMERA"', 4), lidar('ADV "1x 3D LIDAR"'),
             counted(imu('ADV "2x 9-AXIS IMU"'), 2)])
ADDVERB_ELIXIS_W = wheeled(
    'Addverb Elixis-W', 'Addverb Technologies', 1.80, 210, makers(210, 'ADV "GROSS WEIGHT 210 KG" (ELIXIS-W)'), 33,
    sources='ADV (Addverb, its tab ELIXIS-W: "STANDING HEIGHT 1800 MM", "GROSS WEIGHT 210 KG", "DEGREES OF FREEDOM '
            '33", "WHEEL ACTUATOR PLANETARY SERVO DRIVE"); E12.1', added=(grippers(),), boards=ELIXIS_BOARDS,
    sensors=[binocular('ADV "6x STEREO CAMERA"', 6), lidars('ADV "3x 3D LIDAR"', 3), imu('ADV "9-AXIS IMU"')])
GENESIS_ENO = wheeled(
    'Genesis AI Eno', 'Genesis AI', 1.70, None, catalogue(120, 'Genesis AI states none (E12.1, E12.4)'),
    WHEELED_JOINTS_MEDIAN, sources='GEN (Genesis AI: a waitlist), TNW ("a wheeled robot with a foldable tower, '
                                   'dexterous hands"), HG; its tower "can adjust the robot\'s height" as a lift (E12.5 '
                                   'point 8)',
    added=(SIX_HANDS,), lift=True)
REALBOTIX_F_SERIES = wheeled(
    'Realbotix F-Series', 'Realbotix', 1.65, None,
    catalogue(50, 'Realbotix names no F-Series; its full-body Echo "88 lb" not used (E12.2 point 4)'), 31,
    sources='HGF (humanoid.guide: "At 165 cm tall and 50 kg", "44 total degrees of freedom include 13 in the hands", '
            '"a motorized wheeled base"; second-hand), RBX (Realbotix: no F-Series named); E12.4', added=(SIX_HANDS,),
    sensors=[camera('Camera', 2, 'Head', 'HGF "Tiny cameras inside the eyes" (second-hand; two, E)'), IMU_NOT_NAMED])
AVIC_FENGXING_001 = template(
    'AVIC Fengxing-001', 'AVIC', 1.80, None, ((79, 80, 81), 'S', 'GTF "weighing 80 kilograms" (Global Times at AVIC\'s '
                                                                   'stand, 2026-08-20); ± 1 kg'), JOINTS_MEDIAN,
    sources='GTF (Global Times: "about 1.8 meters tall", "80 kilograms", "electro-hydraulic hybrid-drive '
            'architecture"; second-hand), AVC (AVIC: no page names it); E12.4')
FF_FUTURIST = block(
    'FF Futurist', 'Faraday Future', 1.69, 69,
    'FFF (Faraday Future: "169 × 75 × 30 cm", "≈69 kg", "28 DOF + 6-DOF Dexterous Hand", neck 2, arms 7, legs 6, "Peak '
    'Knee Torque 270 N·m", "Battery 0.69 kWh", "16-core CPU + NVIDIA AGX Orin 64G"); E12.1',
    makers(69, 'FFF "≈69 kg"'),
    from_stated_joint(270, {**LEGS_12, 'Shoulder': 6, 'Elbow': 2, 'Wrist': 6, 'Head': 2}) + [SIX_HANDS],
    joint_sources=stated_joint_sources('FFF', '"Peak Knee Torque 270 N·m" (its "500 Nm Peak torque" not used)', 270,
                                       'knee'),
    **energy(690, 'FFF "Battery 0.69 kWh"'),
    **with_defaults(1.69, 69, dict(
        boards=agx_orin('FFF "NVIDIA AGX Orin 64G"') + [named_board('16-core CPU', 'FFF "16-core CPU"'), POWER_BOARD],
        sensors=[camera('Camera, interactive', 1, 'Head', 'FFF "Interactive"'),
                 camera('Camera, fisheye', 2, 'Head', 'FFF "2 Fisheye"'), depth_camera('FFF "2 RGB-D"', 2),
                 lidar('FFF "LiDAR"'), microphones('FFF "Mic"'), speaker('FFF "Speaker"'), IMU_NOT_NAMED])))


def ff_master(ultra: bool) -> dict:
    """The FF Master Classic, Edu and Ultra, each as often (E12.2 point 2): joints from its "Peak torque: 120 N·m"
    (E12.5 point 2), its joints per body part as the Unitree G1's 23 and 29 with a head of 2 and 1 (E), the Ultra an
    Orin NX by its "157 TOPS" (E)."""
    name, kg = ('FF Master Classic Ultra', 39) if ultra else ('FF Master Classic Edu', 35)
    counts = {**LEGS_12, 'Waist': 3 if ultra else 1, 'Shoulder': 6, 'Elbow': 2, 'Wrist': 6 if ultra else 2,
              'Head': 1 if ultra else 2}
    more = dict(sensors=[camera('Camera, RGB', 1, 'Head', 'FFM "RGB camera" (Edu)'), microphones('FFM "Microphone"'),
                         speaker('FFM "speaker"'), IMU_NOT_NAMED])
    if ultra:
        more = dict(boards=orin_nx_boards('FFM "NVIDIA Orin", "157 TOPS" (E: the Orin NX 16 GB\'s)') + [POWER_BOARD],
                    sensors=[lidar('FFM "LiDAR ×1"'), binocular('FFM "Stereo RGB camera"'),
                             camera('Camera, interaction', 1, 'Head', 'FFM "Interaction RGB camera ×1"'),
                             camera('Camera, rear-view', 1, 'Head', 'FFM "Rear-view RGB camera ×1"'),
                             depth_camera('FFM "RGB-D camera ×1"'), microphones('FFM "Microphone"'),
                             speaker('FFM "speaker"'), IMU_NOT_NAMED])
    return block(
        name, 'Faraday Future', 1.31, kg, f'FFM (Faraday Future: "Height: 131 cm", "Weight: {kg} kg", '
                                          f'"{30 if ultra else 25} DOF", "Peak torque: 120 N·m"; its joints per body '
                                          'part as the Unitree G1\'s, E); E12.1',
        makers(kg, f'FFM "Weight: {kg} kg"'), from_stated_joint(120, counts),
        joint_sources=stated_joint_sources('FFM', '"Peak torque: 120 N·m"', 120, 'knee') +
        "; its joints per body part not stated: as the Unitree G1's 23 and 29 with a head of 2 and 1 (E)",
        **with_defaults(1.31, kg, more))


FF_MASTER_EDU, FF_MASTER_ULTRA = ff_master(False), ff_master(True)

# --- E14.6 (2026-11-01, "Yes, build it"): AgiBot's robots of the template, their joints their maker's -----------------
# Each block above as entered; its body joints now AgiBot's model files (AGX2u, AGA3u, read first-hand: V123, V130),
# each module type 2's refit at its torque, half to 1.5 times (E6.8 point 1), or, for the A2, from its page's knee
# (E12.5 point 2). The X2 (25 DoF, arms of five): its legs and waist the X2 files' (the same in both), its arms the
# first five of their seven (E14.4 question 1, agreed; E). The A3 Ultra its body the A3's 31 (the same limits in its
# own file), its hands as entered.
AGIBOT_MODEL_SOURCES = "{code}: its joints' torque limits; mass the refit at its torque, 0.0689 kg × torque^0.566, " \
                       'half to 1.5 times (E6.8 point 1; E14.6 point 3)'
X2_LEGS_WAIST = [('Hip pitch', 2, 120), ('Hip roll', 2, 120), ('Hip yaw', 2, 120), ('Knee', 2, 120),
                 ('Ankle pitch', 2, 60), ('Ankle roll', 2, 36), ('Waist yaw', 1, 120), ('Waist pitch', 1, 36),
                 ('Waist roll', 1, 36)]
X2_ARM_FIVE = [('Shoulder pitch', 2, 60), ('Shoulder roll', 2, 60), ('Shoulder yaw', 2, 36), ('Elbow', 2, 36),
               ('Wrist yaw', 2, 36)]
AGIBOT_X2_ULTRA = with_own_joints(AGIBOT_X2_ULTRA, model_joints(
    X2_LEGS_WAIST + [('Head yaw', 1, 3.13), ('Head pitch', 1, 2)] + X2_ARM_FIVE +
    [('Wrist pitch', 2, 6), ('Wrist roll', 2, 6)], T2.from_torque),
    AGIBOT_MODEL_SOURCES.format(code='AGX2u (X2-Ultra.urdf, v1.4.0; its head 2, the page\'s neck 1)'))
AGIBOT_X2 = with_own_joints(AGIBOT_X2, model_joints(X2_LEGS_WAIST + X2_ARM_FIVE, T2.from_torque),
                            AGIBOT_MODEL_SOURCES.format(code="AGX2u (its legs and waist; its arms of five the first "
                                                             "five of the files' seven, E)"))
A3_BODY = model_joints(
    [('Waist yaw', 1, 220), ('Waist roll', 1, 46), ('Waist pitch', 1, 118), ('Head yaw', 1, 6), ('Head pitch', 1, 6),
     ('Shoulder pitch', 2, 60), ('Shoulder roll', 2, 60), ('Shoulder yaw', 2, 24), ('Elbow', 2, 24),
     ('Wrist roll', 2, 24), ('Wrist pitch', 2, 6), ('Wrist yaw', 2, 6), ('Hip pitch', 2, 220), ('Hip roll', 2, 220),
     ('Hip yaw', 2, 220), ('Knee', 2, 320), ('Ankle pitch', 2, 118.2), ('Ankle roll', 2, 54.75)], T2.from_torque)
AGIBOT_A3 = with_own_joints(AGIBOT_A3, A3_BODY, AGIBOT_MODEL_SOURCES.format(code='AGA3u (a3_t3d0, a3_t2d5)'))
AGIBOT_A3_ULTRA = with_own_joints(AGIBOT_A3_ULTRA, A3_BODY,
                                  AGIBOT_MODEL_SOURCES.format(code='AGA3u (a3_ultra_t3d0: its body)') +
                                  '; its hands as entered')
AGIBOT_A2 = with_own_joints(AGIBOT_A2, from_stated_joint(
    270, {**LEGS_12, 'Shoulder': 6, 'Elbow': 2, 'Wrist': 6, 'Head': 2}),
    stated_joint_sources('AGA2U', '"Peak Knee Torque 270N·m"', 270, 'knee') +
    '; its joints per body part its page\'s (neck 2, arms 7, legs 6)')

# Since types 5 and 6's entry (E16.2, E16.5 question 3, agreed 2026-11-01, "Yes, agree both"): every body joint from
# DEEP Robotics' model files (DPRu: DR02-std.urdf 67.575 kg, 21 joints; DR02-pro.urdf 78.085 kg, 31; read and added up
# by script, V135), y the pitch, x the roll, z the yaw; each module type 2's refit at its torque (E6.8 point 1).
DR02_MODEL_LEGS = [('Hip pitch', 2, 363), ('Hip roll', 2, 363), ('Hip yaw', 2, 137), ('Knee', 2, 363),
                   ('Ankle pitch', 2, 137), ('Ankle roll', 2, 50)]
DEEP_DR02 = with_own_joints(DEEP_DR02, model_joints(
    DR02_MODEL_LEGS + [('Waist yaw', 1, 137), ('Shoulder pitch', 2, 137), ('Shoulder roll', 2, 137),
                       ('Shoulder yaw', 2, 137), ('Elbow', 2, 137)], T2.from_torque),
    AGIBOT_MODEL_SOURCES.format(code='DPRu (DR02-std.urdf, its joints\' efforts)'))
DEEP_DR02_PRO = with_own_joints(DEEP_DR02_PRO, model_joints(
    DR02_MODEL_LEGS + [('Waist pitch', 1, 363), ('Waist yaw', 1, 137), ('Waist roll', 1, 137),
                       ('Shoulder pitch', 2, 137), ('Shoulder roll', 2, 137), ('Shoulder yaw', 2, 137), ('Elbow', 2, 137),
                       ('Wrist yaw', 2, 50), ('Wrist pitch', 2, 50), ('Wrist roll', 2, 50), ('Head yaw', 1, 50),
                       ('Head pitch', 1, 50)], T2.from_torque),
    AGIBOT_MODEL_SOURCES.format(code='DPRu (DR02-pro.urdf, its joints\' efforts)'))

# --- Types 5 and 6's entry (E16.6; Matthias, 2026-11-01, "Yes, agree both", "Find all the data for 5 and 6 and then fill
# in the data in the respective sheets"): batch 3's three robots of types 5 and 6 whose first type among 3 and 4 is 3,
# as E15.3 and E16.2 give them (read first-hand: V134, V135) ------------------------------------------------------------
KAWASAKI_KALEIDO_9 = template(
    'Kawasaki Kaleido 9', 'Kawasaki Robotics', 1.90, None,
    ((98, 99, 100), 'S', 'MYN "体重は99kg" (Mynavi at its showing; Kawasaki\'s pages state none); ± 1 kg (E15.2 point 1)'),
    30, sources='MYN (Mynavi, 2025-12-05: "身長は190cm", "全身に30軸(ハンドは別)の自由度", "頭部にステレオカメラ", "胸にはLIDAR'
                'センサー"), KAWb (Kawasaki: "maintaining torque", LiDAR), KAWj (Kawasaki on its 2019 Kaleido); E15, E16',
    sensors=[binocular('MYN "頭部にステレオカメラ"'), lidar('MYN "胸にはLIDARセンサー"'), IMU_NOT_NAMED],
    frame=('Frame', 'Magnesium alloys', 'KAWj "骨格部品に、アルミより軽量なマグネシウム合金を採用" (its 2019 Kaleido): magnesium '
                                 'alloy; the remainder (E16.2; as the A3\'s, E11.6 question 4)'))
NOBLE_MACHINES_MOBY = template(
    'Noble Machines Moby', 'Noble Machines', 1.70, 72, makers(72, 'NMb "Moby\'s 72 Kg body"'), 34 + 2,
    'Compute module, NVIDIA Jetson Thor',
    sources='NMb (its blog, 2025-03-18: "72 Kg", "200W", "five to six-hour shifts"), NMp (its page: "Payload 23KG/50LB", '
            '"Battery life 5 hours", "Modular end-effectors"), NVm (NVIDIA: "NVIDIA Jetson Thor"), ORBm (Orbbec: '
            '"Gemini 336L stereo 3D cameras"), MKm (170 cm, "a reported 34 degrees of freedom"); E15, E16',
    added_joints=[grippers()], boards=thor('NVm "NVIDIA Jetson Thor processes sensor data"') + [POWER_BOARD],
    sensors=[depth_camera('ORBm "Orbbec Gemini 336L stereo 3D cameras" (their count not stated: two, E)', 2),
             IMU_NOT_NAMED])


def phantom_mk1_joints() -> list:
    """The Phantom MK1's body joints (E15.3): from its "MAX PEAK TORQUE, 160Nm" at its knee by the seven robots' ratios
    (E12.5 point 2), its joints per body part as the Unitree G1's 29 (E: its "29º" not split), its shoulders' "119 Nm"
    and wrists' "20 Nm" as stated, each module type 2's refit at its torque."""
    rows = from_stated_joint(160, {**LEGS_12, 'Waist': 3, 'Shoulder': 6, 'Elbow': 2, 'Wrist': 6})
    stated = {'Shoulder': joint('Shoulder', 6, 119, T2.from_torque(119), 'Shoulders', 'Arms'),
              'Wrist': joint('Wrist', 6, 20, T2.from_torque(20), 'Elbows and wrists', 'Arms')}
    return [stated.get(r[0], r) for r in rows]


FOUNDATION_PHANTOM_MK1 = block(
    'Foundation Phantom MK1', 'Foundation', 1.80, 80,
    'FDp (Foundation: "5\'-11", (1.8m)", "176lbs, (80kg)", "29º", "MAX PEAK TORQUE, 160Nm", "LEGS TORQUE, >160", '
    '"SHOULDER TORQUE, 119", "WRIST TORQUE, 20", "9 RAD/S @ 48V"), TBS (the BBC via UNB: "lacks a battery"); E15, E16',
    makers(80, 'FDp "176lbs, (80kg)"'), phantom_mk1_joints(),
    joint_sources=stated_joint_sources('FDp', '"MAX PEAK TORQUE, 160Nm"', 160, 'knee') +
    '; its shoulders "119 Nm" and wrists "20 Nm" as stated, each the refit at its torque; its joints per body part as '
    "the Unitree G1's 29 (E)",
    # TBS: "Phantom MK-1 … lacks a battery" (E16.2): no battery rows; it draws its power by cable.
    battery=False, **with_defaults(1.80, 80, {}))

# --- Batch 3, robot by robot (EVIDENCE.md E15.3 and E15.6, agreed 2026-11-01, "Yes, agree both"; entered on "E15's
# entry" and "Move on", 2026-11-02, E15.7), in the register's order. Each figure as read first-hand (V134; the record in
# documentation/claude/research_2026-11-01/firsthand_batch3.md), typed in here, never read from a document at run time.
def internet(kg: float, source: str) -> tuple:
    """A mass from the internet (C), ± 1 kg (E15.2 point 1), its source named."""
    return (kg - 1, kg, kg + 1), 'S', f"{source} (the internet's); ± 1 kg (E15.2 point 1)"


def stated_hands(what: str, kg: float, label: str, source: str) -> tuple:
    """Two hands of a stated mass each (E15.2 point 3): ± 5 % where a source states it (S), half to 1.5 times where
    it is another hand's (E). `source` is said in the block's joint sources."""
    return joint(f'Hand ({what})', 2, None, (spread if label == 'S' else estimate)(kg), 'Elbows and wrists', 'Arms',
                 size='small')


def lfp(source: str) -> dict:
    """Cells of LiFePO4 where the maker says so (E15.2 point 4): the LFP cylindrical recipe, their format E."""
    return dict(cell_recipe='LFP cylindrical', cells=('S', f'LFP cylindrical: {source}; the cell format E (E9.6 point 8)'))


def orin_nx_read(source: str) -> list:
    """A Jetson Orin NX read from a computing figure (E15.2 point 5): its size half to 1.5 times (E), and its carrier."""
    module, carrier = orin_nx_boards(source)
    return [module[:4] + (estimate(T2.ORIN_NX[1]), module[5], 'E',
                          f'{source}; 69.6 × 45 mm (E5.13), half to 1.5 times (E)'), carrier]


def x86_and_arm(why: str) -> list:
    """The cooler of a robot with an Intel or AMD computer and an ARM module: two fans, a heat sink of each (as type 2's
    robots with both, E9.6 point 9)."""
    return [T2.fans(2, why), T2.x86_sinks(1), ARM_SINK]


def on_legs_and_wheels(name: str, maker: str, height: float, mass: tuple, body_joints: int, *, sources: str,
                       added: tuple = (), **more) -> tuple:
    """A robot of no stated form, on legs and on wheels, each as often (E15.6 question 2): the template on legs, and
    the template on wheels with two drive wheels and two casters."""
    legs = template(f'{name} on legs', maker, height, None, mass,
                    JOINTS_MEDIAN + sum(h[1] for h in added), sources=sources, added_joints=list(added), **more)
    wheels = wheeled(f'{name} on wheels', maker, height, None, mass, WHEELED_JOINTS_MEDIAN, sources=sources,
                     added=added, **more)
    return legs, wheels


NO_FORM = 'its form not stated: on legs and on wheels, each as often (E15.6 question 2)'
FIGURE_AI_FIGURE_02 = template(
    'Figure AI Figure 02', 'Figure AI', 1.68, None, catalogue(70, 'Figure states none (E15.1)'), JOINTS_MEDIAN + 2,
    sources='FIGr (New Atlas on its launch: "six RGB cameras", "16 degrees of freedom" in its hands, "a new 2.25-kWh", '
            '"onboard microphones and speakers"), HG; E15', added_joints=[hands(16)],
    **energy(2250, 'FIGr "a new 2.25-kWh"'),
    sensors=[camera('Camera, RGB', 6, 'Head', 'FIGr "six RGB cameras"'), microphones('FIGr "onboard microphones"'),
             speaker('FIGr "speakers"'), IMU_NOT_NAMED])
PUDU_FLASHBOT_ARM = wheeled(
    'Pudu FlashBot Arm', 'Pudu Robotics', 1.44, None, catalogue(70, 'Pudu states none (E15.1)'), 14,
    sources='PUDf (Pudu: "539*515*1440mm", "Arm: 7", "Hand: 6 Active + 5 Passive", "PUDU DH11 dexterous hands", '
            '"Independent Suspended Chassis", "RGBD cameras, LiDAR, panoramic cameras" with no counts), HG; E15',
    added=(hands(6),),
    sensors=[depth_camera('PUDf "RGBD cameras" (their count not stated: one, E)'), base_lidar('PUDf "LiDAR"'),
             camera('Camera, panoramic', 1, 'Head', 'PUDf "panoramic cameras" (one, E)'), IMU_NOT_NAMED])
HOLIDAY_ROBOTICS_FRIDAY = wheeled(
    'Holiday Robotics Friday', 'Holiday Robotics', 1.76, None,
    internet(115, 'HDF "176cm tall, weighing 115kg (with a heavy 66kg mobile base"'), WHEELED_JOINTS_MEDIAN,
    sources='HDF (Humanoids Daily, from the specifications Holiday Robotics released: "176cm tall, weighing 115kg", "A '
            '20-DoF ... hand that weighs only 500g", "differential drive wheeled base"), HG; E15',
    added=(stated_hands('Friday, 20 joints', 0.5, 'S', 'HDF "500g"'),),
    boards=agx_orin('HG "NVIDIA Jetson Orin" (the catalogue\'s; E: an AGX Orin)', label='E') + [POWER_BOARD])
FUTURING_2_ON_LEGS, FUTURING_2_ON_WHEELS = on_legs_and_wheels(
    'Futuring 2', 'Futuring Robot', 1.68, catalogue(70, 'Futuring states none (E15.1)'), 0,
    sources=f'HG (the catalogue: 70 kg, "2-finger gripping claws"; {NO_FORM}); E15', added=(grippers(),))
AGIBOT_G2_MAX = wheeled(
    'AgiBot G2 Max', 'AgiBot', 1.79, None,
    ((184, 185, 186), 'S', 'HG "185" (the register, the catalogue\'s), which is the base G2\'s (AGG2s "Weight 185kg"); ± 1 '
                           'kg (E15.3)'), WHEELED_JOINTS_MEDIAN,
    sources='HG; AGG2s (the base G2\'s specification as a seller carries it: "Weight 185kg"); E15', driven=4,
    caster_count=0, added=(T2.steering(4),))
GALBOT_G1 = wheeled(
    'Galbot G1', 'Galbot', 1.73, 92.5, makers(92.5, 'GALg1 "92.5 kg"'), 21,
    sources='GALg1 (Galbot: "92.5 kg", "1730 mm", "合计 21 颈部 2 · 手臂 7×2 · 腰部 3 · 腿部 2", "48 V 30 Ah", "NVIDIA AGX Orin '
            '64GB", "4 轮全向移动底盘"); E15', driven=4, caster_count=0, added=(grippers(),),
    **voltage_capacity(48, 'GALg1 "48 V 30 Ah"', 30, 'GALg1 "48 V 30 Ah"'),
    boards=agx_orin('GALg1 "NVIDIA AGX Orin 64GB"') + [POWER_BOARD],
    sensors=[binocular('GALg1 "头部 双目相机 ×1"'), camera('Camera, RGB', 4, 'Head', 'GALg1 "躯干 RGB 相机 ×4"'),
             depth_camera('GALg1 "腕部 深度相机 ×2"', 2), base_lidar('GALg1 "底盘 3D 激光雷达 ×1"'),
             counted(imu('GALg1 "IMU ×1" in its torso and in its chassis'), 2),
             counted(microphones('GALg1 "线性四麦克风阵列 ×2"'), 2), counted(speaker('GALg1 "喇叭 5 W ×2"'), 2)])
GALBOT_ET1 = template(
    'Galbot ET1', 'Galbot', 1.25, 32, makers(32, 'GALet1 "带电池重量 32 kg"'), 26,
    sources='GALet1 (Galbot: "1250 mm", "带电池重量 32 kg", "标准版：26", "RK3588 + RDK X5", "双目摄像头"); E15',
    boards=RK3588_BOARDS + [named_board('RDK X5', 'GALet1 "RK3588 + RDK X5"'), POWER_BOARD],
    sensors=[binocular('GALet1 "双目摄像头"'), IMU_NOT_NAMED])
GALBOT_S1 = wheeled(
    'Galbot S1', 'Galbot', 1.79, 320, makers(320, 'GALs1 "整机重量 320 kg"'), 16,
    sources='GALs1 (Galbot: "320 kg", "1793 mm", "升降行程 750 mm", "颈部 2 · 双臂 7×2 · 升降 1", "四轮转向全向底盘", "48 V 30 Ah × 2", '
            '"NVIDIA AGX Orin 64GB"); E15', driven=4, caster_count=0, added=(grippers(), T2.steering(4)), lift=True,
    **voltage_capacity(48, 'GALs1 "48 V 30 Ah × 2"', 60, 'GALs1 "30 Ah × 2" (arith.)'),
    boards=agx_orin('GALs1 "NVIDIA AGX Orin 64GB"') + [POWER_BOARD],
    sensors=[binocular('GALs1 "头部 双目相机 ×1"'), lidar('GALs1 "头部 3D 激光雷达 ×1"'),
             depth_camera('GALs1 "胸部 深度相机 ×2"', 2), base_lidar('GALs1 "底盘 3D 激光雷达 ×2"', 2),
             counted(speaker('GALs1 "喇叭 5 W × 2"'), 2), IMU_NOT_NAMED])
PERSONA_AI_GEN_1 = template(
    'Persona AI Gen 1', 'Persona AI', 1.75, None,
    ((69, 70, 85), 'S', 'HG "70" (the catalogue\'s) the mode, 1 kg below; OBP "WEIGHT 85 kg" (a database) the max (E15.2 '
                        'point 1)'), JOINTS_MEDIAN + 2,
    sources='PRSn (Persona: its page gives no figures), OBP, HG (hands 20); E15', added_joints=[hands(10)])
GENERATIVE_BIONICS_GENE_01 = template(
    'Generative Bionics GENE.01', 'Generative Bionics', 1.70, None,
    ((60, 79.7, 80.7), 'S', 'GBm its model\'s links 79.668 kg (added by script, V134) the mode, 1 kg above; the '
                            'internet\'s "approximately 60 kilograms" (Origin of Bots, not reread) the min (E15.2 '
                            'point 1)'), 31 + 2,
    sources='GBm (its model file gene01_0/model.urdf: 79.668 kg, 31 body joints, 42 hand joints, every effort "1e+09", '
            'six camera frames, "chest_imu"), HG; E15', added_joints=[hands(21)],
    sensors=[camera('Camera', 6, 'Head', 'GBm six camera frames'), imu('GBm "chest_imu"')])
GENTO_LUNA = wheeled(
    'Gento Luna', 'Gento Robotics', 1.70, None, catalogue(90, 'Gento states none (E15.1)'), 26,
    sources='GENl (Gento: "26 DoF (excluding dexterous hands)", "48 V 34.4 Ah LiFePO battery pack", "NVIDIA Jetson Orin '
            'AGX 64GB", "3D LiDAR and ultrasonic radar", "omnidirectional mobile chassis"), HG; E15', driven=4,
    caster_count=0, added=(grippers(),),
    **voltage_capacity(48, 'GENl "48 V 34.4 Ah"', 34.4, 'GENl "34.4 Ah"'), **lfp('GENl "LiFePO battery pack"'),
    boards=agx_orin('GENl "NVIDIA Jetson Orin AGX 64GB"') + [POWER_BOARD],
    sensors=[base_lidar('GENl "3D LiDAR"'), IMU_NOT_NAMED])
GEEK_PLUS_GINO_1 = wheeled(
    'Geek+ Gino 1', 'Geek+', 1.68, None, catalogue(63, 'Geek+ states none (E15.1)'), 14,
    sources='CLSg (财联社 on its launch: "机器人双臂14个自由度", "7主动自由度三指灵巧手", "50Ah的大容量电池" without its voltage: on '
            'the template, E15.2 point 4, "Nvidia Thor", "三目主视觉和前后鱼眼相机", "前后半球形3D激光雷达", "手心双目相机"), HG; E15',
    driven=4, caster_count=0, added=(hands(7),),
    boards=thor('CLSg "Nvidia Thor机器人计算机"') + [POWER_BOARD],
    sensors=[camera('Camera, trinocular', 1, 'Head', 'CLSg "三目主视觉"'),
             camera('Camera, fisheye', 2, 'Head', 'CLSg "前后鱼眼相机"'),
             base_lidar('CLSg "前后半球形3D激光雷达"', 2), binocular('CLSg "手心双目相机", one in each palm', 2),
             IMU_NOT_NAMED])
GAC_GOMATE = wheeled(
    'GAC GoMate', 'GAC', 1.74, None, catalogue(45, 'GAC states none (E15.1)'), 28,
    sources='HSG (heise: "174 cm", "38 degrees of freedom", "hands with five movable fingers"; its wheel-legs four '
            'driven, E15.3), HG; E15', driven=4, caster_count=0, added=(hands(5),))
GAC_GOMATE_MINI = wheeled(
    'GAC GoMate Mini', 'GAC', 1.70, None, catalogue(60, 'GAC states none (E15.1)'), WHEELED_JOINTS_MEDIAN,
    sources='HG (the catalogue: 60 kg, wheel-legs); E15', driven=4, caster_count=0)
GR3_JOINTS = [('Hip pitch', 2, 366), ('Hip roll', 2, 140.4), ('Hip yaw', 2, 140.4), ('Knee', 2, 366),
              ('Ankle pitch', 2, 59.4), ('Ankle roll', 2, 59.4), ('Waist yaw', 1, 140.4), ('Waist roll', 1, 108.6),
              ('Waist pitch', 1, 108.6), ('Head yaw', 1, 17.4), ('Head pitch', 1, 17.4), ('Shoulder pitch', 2, 74.4),
              ('Shoulder roll', 2, 74.4), ('Shoulder yaw', 2, 42.9), ('Elbow', 2, 42.9), ('Wrist yaw', 2, 42.9),
              ('Wrist pitch', 2, 17.4), ('Wrist roll', 2, 17.4)]
FOURIER_GR_3 = block(
    'Fourier GR-3', 'Fourier', 1.65, 71,
    'FFgr3 (Fourier: "Net Weight ≈71 kg", 1642 × 552 × 292 mm, its joint table, head 2, leg 6, waist 3, arm 7, hand 6, '
    '"702Wh + 234Wh", "46.8V", "AMD Ryzen 7 8845HS", "Aluminum Alloy + Engineering Plastic + Soft Cover Material"), '
    'FFgr3u (its model file gr3v2_1_1.urdf: the same torques); E15', makers(71, 'FFgr3 "Net Weight ≈71 kg"'),
    model_joints(GR3_JOINTS, T2.from_torque) + [hands(6)],
    joint_sources="FFgr3 its joint table's \"Torque Upper Limit (Nm)\", the same as its model file's (FFgr3u); each "
                  'module the refit at its torque, 0.0689 kg × torque^0.566, half to 1.5 times (E14.1); its hands '
                  "Fourier's six-joint hand per joint (E7.5 point 4)",
    **voltage_capacity(46.8, 'FFgr3 "46.8V"', 20, 'FFgr3 "702Wh + 234Wh" over 46.8 V (arith.)'),
    **with_defaults(1.65, 71, dict(
        boards=[intel('AMD Ryzen 7 8845HS', 'FFgr3 "AMD Ryzen 7 8845HS"'), POWER_BOARD], cooler=X86_COOLER,
        sensors=[camera('Camera, monocular', 1, 'Head', 'FFgr3 "Monocular camera"'), imu('FFgr3 IMU "6-axis"'),
                 microphones('FFgr3 microphone "360-degree"'), speaker('FFgr3 speaker 15 W')],
        frame=('Frame', 'Aluminium alloys', 'FFgr3 "Aluminum Alloy + Engineering Plastic + Soft Cover Material": '
                                            'aluminium; the remainder (E15.6 question 6)'))))
HAIER_HIVA_HAIWA = wheeled(
    'Haier HIVA Haiwa', 'Haier', 1.65, None, catalogue(70, 'Haier states none (E15.1)'), WHEELED_JOINTS_MEDIAN,
    sources='HG (the catalogue: 70 kg, hands 12, on a base); E15', added=(hands(6),))
HUMANOID_HMND_01_ALPHA_BIPEDAL = template(
    'Humanoid HMND 01 Bipedal', 'Humanoid', 1.79, 90, makers(90, 'HMNp "WEIGHT 90 kg"'), 29 + 2,
    sources='HMNp (Humanoid: "WEIGHT 90 kg", "HEIGHT 179 cm", "DEGREES OF FREEDOM 29", "12-DOF 5-finger hand or 1-DOF '
            'parallel gripper", "Wrist RGB cameras", "6-mic array, speakers"), HMNr (its release: "six RGB cameras, two '
            'depth sensors, and a six-microphone array", "Nvidia Jetson Orin AGX and Intel i9 processors", "1-degree-of-'
            'freedom parallel grippers"); E15', added_joints=[grippers()],
    boards=agx_orin('HMNr "Nvidia Jetson Orin AGX"') + [intel('Intel i9', 'HMNr "Intel i9 processors"'), POWER_BOARD],
    cooler=x86_and_arm('its Intel computer and its AGX Orin'),
    sensors=[camera('Camera, RGB', 6, 'Head', 'HMNr "six RGB cameras"'), depth_camera('HMNr "two depth sensors"', 2),
             camera('Camera, wrist', 2, 'Arms', 'HMNp "Wrist RGB cameras"'),
             microphones('HMNr "a six-microphone array"'), speaker('HMNp "speakers"'), IMU_NOT_NAMED])
NOETIX_HOBBS_W1 = wheeled(
    'Noetix Hobbs W1', 'Noetix', 1.70, None, internet(75, 'AIWh "75 kg" (aiwiki, citing Noetix\'s page)'),
    WHEELED_JOINTS_MEDIAN,
    sources='NTXh (Noetix: "Wheeled Full-Body Form", "54 Active DoF", "LiDAR, ultrasonic sensors, and depth cameras"), '
            'AIWh (aiwiki, citing Noetix\'s page: "75 kg", "32 Ah (21V to 29.4V)", "Rockchip RK3588", "Intel J1900", '
            '"3 ToF sensors on chassis", "2x RGB cameras", "1x RGB camera", "Linear four-microphone array"); E15',
    added=(hands(6),),
    **voltage_capacity(25.9, 'AIWh "21V to 29.4V": seven cells in series, 3.7 V each nominal (arith., E)', 32,
                       'AIWh "32 Ah"', label='S, E'),
    boards=RK3588_BOARDS + [intel('Intel J1900', 'AIWh "Intel J1900"'), POWER_BOARD],
    cooler=x86_and_arm('its Intel computer and its RK3588'),
    sensors=[base_depth_camera('AIWh "3 ToF sensors on chassis"', 3),
             camera('Camera, RGB', 3, 'Head', 'AIWh "2x RGB cameras" (its eyes), "1x RGB camera" (its chest)'),
             microphones('AIWh "Linear four-microphone array"'), base_lidar('NTXh "LiDAR"'), IMU_NOT_NAMED])
HONOR = template(
    'HONOR', 'HONOR', 1.60, None, catalogue(80, 'HONOR states none; which of its robots this is is not said (E15.1)'),
    JOINTS_MEDIAN, sources='HONr (HONOR: its robots named, no figures), HG ("forehead-mounted camera"); E15',
    sensors=[camera('Camera', 1, 'Head', 'HG "forehead-mounted camera"'), IMU_NOT_NAMED])
HONOR_A1 = template(
    'HONOR A1', 'HONOR', 1.37, None, catalogue(40, 'HONOR states none (E15.1)'), JOINTS_MEDIAN,
    sources='HONr (HONOR: "HONOR Robotics A1", no figures), HG; E15')
HUASHU_HSR_ER_HR705 = wheeled(
    'Huashu HSR-ER-HR705', 'Huashu Robotics', 1.70, 200, makers(200, 'HSRp "机器人重量 200kg"'), 20,
    sources='HSRp (Huashu: "机器人重量 200kg", "机器人高度 1700mm", "23（机械臂7×2+头部2+腰部1+腿部3+底盘3）", "深度相机×2、鱼眼相机×1", '
            '"SLAM激光导航", "全向移动"; three driven wheels, E15.2 point 6); E15', driven=3, caster_count=0,
    added=(grippers(),),
    sensors=[depth_camera('HSRp "深度相机×2"', 2), camera('Camera, fisheye', 1, 'Head', 'HSRp "鱼眼相机×1"'),
             base_lidar('HSRp "SLAM激光导航" (one, E)'), IMU_NOT_NAMED])
XPENG_IRON_2024 = template(
    'XPENG IRON 2024', 'XPENG', 1.78, None, catalogue(70, 'XPENG states none (E15.1)'), JOINTS_MEDIAN + 2,
    sources='QVI (Qviro on its launch: "Each hand features 15 degrees of freedom"), HG; E15', added_joints=[hands(15)],
    boards=[named_board('XPENG Turing', 'its Turing chip (the internet\'s, E15.3) as one board'), POWER_BOARD])
XPENG_IRON_2025 = template(
    'XPENG IRON 2025', 'XPENG', 1.78, None,
    ((69, 70, 90), 'S', 'K36i "体重达到 70kg" the mode, 1 kg below; HG "90" (the register\'s, no source) the max (E15.2 '
                        'point 1)'), JOINTS_MEDIAN + 2,
    sources='K36i (36Kr on its launch: "IRON 身高约 1.78 米 ... 体重达到 70kg", "双手 ... 22 个自由度", "三颗图灵 AI 芯片"), HG; E15',
    added_joints=[hands(22)],
    boards=[counted(named_board('XPENG Turing', 'K36i "三颗图灵 AI 芯片": three boards (E)'), 3), POWER_BOARD])

WEAVE_ISAAC_1 = wheeled(
    'Weave Isaac 1', 'Weave Robotics', 1.75, None,
    ((39, 40, 45), 'S', 'HG "40" (the catalogue\'s) the mode, 1 kg below; OBI "WEIGHT 45 kg" (a database) the max (E15.2 '
                        'point 1)'), 16,
    sources='WVi (Weave: "3\' – 5\'9"", Neck "2", Arms "2 × 6", Hands "2 × 1", Torso "2", Base "3", "collapsible torso"; '
            'three driven wheels, E15.2 point 6), OBI, HG; E15', driven=3, caster_count=0, added=(grippers(),),
    lift=True)
JAKA_K1 = template('JAKA K1', 'JAKA', 1.80, None, catalogue(40, 'JAKA states none (E15.1)'), JOINTS_MEDIAN,
                   sources='HG; E15')
JAKA_KARGO = wheeled(
    'JAKA Kargo', 'JAKA', 1.57, None,
    ((179, 180, 200), 'S', 'HG "180" (the catalogue\'s table) the mode, 1 kg below; its text "about 200 kilograms with '
                           'everything" the max (E15.2 point 1)'), WHEELED_JOINTS_MEDIAN,
    sources='HG (the catalogue: 180 kg, "about 200 kilograms with everything", a lift, an Intel i5); E15', lift=True,
    boards=[intel('Intel i5', 'HG "Intel i5" (the catalogue\'s)'), POWER_BOARD], cooler=X86_COOLER)
JINGCHU_ELF = wheeled(
    'Jingchu Elf', 'Hubei Jingchu', 1.65, None,
    ((69, 70, 80), 'S', 'JNGe "体重约70kg" the mode, 1 kg below; the same page\'s wheeled block "体重：80kg" the max (E15.2 '
                        'point 1)'), 16,
    sources='JNGe (Jingchu: "荆楚精灵身高165cm，体重约70kg。具备16个自由度（不含手），拥有高精度智能移动底盘", "轮式机器人 ... 体重：80kg 2轮驱动", '
            '"1024核NVIDIA Ampere架构GPU，约117TOPS", "激光雷达和深度相机"); E15',
    boards=orin_nx_read('JNGe "1024核NVIDIA Ampere架构GPU，约117TOPS" (E: an Orin NX)') + [POWER_BOARD],
    sensors=[base_lidar('JNGe "激光雷达"'), depth_camera('JNGe "深度相机" (one, E)'), IMU_NOT_NAMED])
ZEROTH_JUPITER = template(
    'Zeroth Jupiter', 'Zeroth', 1.65, None,
    ((57, 58, 60), 'S', 'IFAz "Weight: 58 kg" (its IFA exhibitor listing) the mode, 1 kg below; HG "60" the max (E15.2 '
                        'point 1)'), 25 + 2,
    sources='IFAz (IFA, Zeroth\'s exhibitor listing: Jupiter "Height: 165 cm Weight: 58 kg", "25 joints", "Hands: 22 '
            'points of articulation (10 per hand)"), HG; E15', added_joints=[hands(10)])
KAI_HAND = stated_hands('KaiHand, 20 active joints', 0.75, 'E', 'KXh "750 g"')
KINETIXAI_KAI_ON_LEGS, KINETIXAI_KAI_ON_WHEELS = on_legs_and_wheels(
    'KinetixAI KAI', 'KinetixAI', 1.73, internet(70, 'IEK "70 kilograms"'), 0,
    sources=f'IEK (Interesting Engineering: "173 centimeters", "70 kilograms", "1.7-kilowatt-hour (kWh) semi-solid-state '
            f'battery", "72 DoF in its hands"), KXh (its KaiHand: "750 g", "20 active"; which robot it belongs to not '
            f'said: E), HG; {NO_FORM}; E15', added=(KAI_HAND,),
    **energy(1700, 'IEK "1.7-kilowatt-hour (kWh) semi-solid-state battery"'))
LG_KAPEX = template(
    'LG KAPEX', 'LG Electronics', 1.70, None,
    ((60, 65, 70), 'S', 'HKK "체중 60㎏대" (Hankyung: in the sixties) its range, 65 the middle (E15.2 point 1)'),
    JOINTS_MEDIAN, sources='HKK (Hankyung, 2025-11-13: "키 170㎝, 체중 60㎏대"), HG; E15')
KEENON_XMAN_R1 = wheeled(
    'Keenon XMAN-R1', 'Keenon Robotics', 1.72, None, catalogue(110, 'Keenon states none (E15.1)'),
    WHEELED_JOINTS_MEDIAN, sources='HG; E15')
GALAXEA_KENGO = block(
    'Galaxea Kengo', 'Galaxea Dynamics', 1.40, None,
    'OBK (Origin of Bots: "The reported 140 x 44 x 22.5 cm footprint and 40 kg weight"), ITHk (IT之家: "单关节扭矩超 '
    '130N·m", "星海图官方暂未公布 Kengo 机器人的具体参数"), HG ("Degrees of freedom, hands 12": six a hand); E15',
    ((39, 40, 65), 'S', 'OBK "40 kg weight" the mode, 1 kg below (its 1.4 m in two outlets fits it); HG "65" the max '
                        '(E15.2 point 1)'),
    from_stated_joint(130, {**LEGS_12, 'Waist': 1, 'Shoulder': 6, 'Elbow': 2, 'Wrist': 6, 'Head': 2}) + [hands(6)],
    joint_sources=stated_joint_sources('ITHk', '"单关节扭矩超 130N·m" (the internet\'s, E15.6 question 1)', 130, 'knee') +
    '; its hands HG "hands 12", six joints each, as Fourier\'s six-joint hand (E7.5 point 4)',
    **with_defaults(1.40, 40, {}))
KINISI_KR1 = wheeled(
    'Kinisi KR1', 'Kinisi', 1.62, None, catalogue(100, 'Kinisi states none (E15.1)'), WHEELED_JOINTS_MEDIAN,
    sources='KNS (Bear Robotics: "Wheeled humanoid mobile manipulator"), IEKR (Interesting Engineering: "stereo depth '
            'cameras, a 180° LiDAR array", "an onboard NVIDIA Jetson module", "hot-swappable 48 V lith[ium]" without its '
            'capacity), HG; E15', driven=4, caster_count=0, added=(grippers(),),
    boards=agx_orin('IEKR "an onboard NVIDIA Jetson module" (E: an AGX Orin)', label='E') + [POWER_BOARD],
    sensors=[depth_camera('IEKR "stereo depth cameras" (two, E)', 2), base_lidar('IEKR "a 180° LiDAR array"'),
             IMU_NOT_NAMED])
KNOWIN_X1 = wheeled(
    'Knowin-X1', 'Knowin', 1.30, None, catalogue(50, 'Knowin states none (E15.1)'), 23,
    sources='KNWx (Knowin: "130 cm" extended, "7 DoF" an arm, "Total Degrees of Freedom 23 DoF", "Wheeled chassis", '
            '"Vision · Depth · LiDAR"), HG; E15',
    sensors=[depth_camera('KNWx "Depth" (one, E)'), base_lidar('KNWx "LiDAR"'), IMU_NOT_NAMED])
LEJU_KUAVO_5_W = wheeled(
    'Leju KUAVO 5-W', 'Leju Robotics', 2.00, None, catalogue(156, 'Leju states none (E15.1)'), WHEELED_JOINTS_MEDIAN,
    sources='HG (the catalogue: 156 kg, "Degrees of freedom, hands 12", "(4 depth cameras)", "depth cameras and '
            'LiDAR"); E15', driven=4, caster_count=0, added=(hands(6),),
    sensors=[depth_camera('HG "(4 depth cameras)"', 4), base_lidar('HG "LiDAR"'), IMU_NOT_NAMED])
LEJU_KUAVO_MY = template('Leju Kuavo-my', 'Leju Robotics', 1.45, None, catalogue(45, 'Leju states none (E15.1)'),
                         JOINTS_MEDIAN, sources='HG; E15')
MOON_DYNAMICS_L1 = wheeled(
    'Moon Dynamics L1', 'Moon Dynamics', 1.65, None, catalogue(60, 'Moon Dynamics has no site (E15.1)'),
    WHEELED_JOINTS_MEDIAN, sources='HG (the catalogue: 60 kg, on two wheels); E15', caster_count=0,
    added=(grippers(),))
GLROAD_LABORER_C1 = block(
    'Glroad Laborer C1', 'Glroad', 1.37, 38,
    'GLc1 (Glroad: 身高 "137.1CM", 重量 "38KG", 电池容量 "10AH" without its voltage: on the template, E15.2 point 4, 全身自由度 '
    '"21", 单腿 "6", 腰部 "1", 单臂 "4(可扩展)", 最大峰值扭矩 "150N.M", "Nvidia Orin NX 100T/157T", "6轴IMU", "深度相机 激光雷达", '
    '"阵列麦克风+5W扬声器"); E15', makers(38, 'GLc1 "重量 38KG"'),
    from_stated_joint(150, {**LEGS_12, 'Waist': 1, 'Shoulder': 6, 'Elbow': 2}),
    joint_sources=stated_joint_sources('GLc1', '最大峰值扭矩 "150N.M"', 150, 'knee'),
    **with_defaults(1.37, 38, dict(
        boards=orin_nx_boards('GLc1 "Nvidia Orin NX 100T/157T"') + [POWER_BOARD],
        sensors=[depth_camera('GLc1 "深度相机"'), lidar('GLc1 "激光雷达"'), imu('GLc1 "6轴IMU"'),
                 microphones('GLc1 "阵列麦克风"'), speaker('GLc1 "5W扬声器"')])))
GLROAD_LABORER_M1 = block(
    'Glroad Laborer M1', 'Glroad', 1.87, 86,
    'GLm1 (Glroad: 身高 "187CM", 重量 "86KG", 电池容量 "22AH" without its voltage: on the template, 全身自由度 "27", 单腿 "6", 头部 '
    '"1", 最大峰值扭矩 "430N.M"; its arms seven joints each by arithmetic, E); E15', makers(86, 'GLm1 "重量 86KG"'),
    from_stated_joint(430, {**LEGS_12, 'Head': 1, 'Shoulder': 6, 'Elbow': 2, 'Wrist': 6}),
    joint_sources=stated_joint_sources('GLm1', '最大峰值扭矩 "430N.M"', 430, 'knee'), **with_defaults(1.87, 86, {}))
HECBOT_LUMEN_H1 = block(
    'HECbot Lumen H1', 'HECbot', 1.69, 69,
    'HECh (HECbot: "身高169cm，净重≈69kg", 电池 "700 Wh", "40个（双臂7x2、双腿6x2、头部2、灵巧手6x2）", "自研一体化关节峰值扭矩512Nm", "激光雷达 + '
    'RGBD相机"); E15', makers(69, 'HECh "净重≈69kg"'),
    from_stated_joint(512, {**LEGS_12, 'Head': 2, 'Shoulder': 6, 'Elbow': 2, 'Wrist': 6}) + [hands(6)],
    joint_sources=stated_joint_sources('HECh', '"峰值扭矩512Nm"', 512, 'knee') + "; its hands Fourier's six-joint "
                                                                                'hand per joint (E7.5 point 4)',
    **energy(700, 'HECh "电池 700 Wh"'),
    **with_defaults(1.69, 69, dict(sensors=[lidar('HECh "激光雷达"'), depth_camera('HECh "RGBD相机"'),
                                            IMU_NOT_NAMED])))
HECBOT_LUMEN_S1_ON_LEGS, HECBOT_LUMEN_S1_ON_WHEELS = on_legs_and_wheels(
    'HECbot Lumen S1', 'HECbot', 1.30, catalogue(35, 'HECbot states none (E15.1)'), 0,
    sources=f'HG (the catalogue: 35 kg, "Orin NX", an RGB-D, a stereo and two RGB cameras, a LiDAR; {NO_FORM}); E15',
    boards=orin_nx_boards('HG "Orin NX" (the catalogue\'s)') + [POWER_BOARD],
    sensors=[depth_camera('HG "RGB-D"'), binocular('HG "stereo"'), camera('Camera, RGB', 2, 'Head', 'HG "RGB" two'),
             lidar('HG "LiDAR"'), IMU_NOT_NAMED])
MAGICLAB_MAGICBOT = block(
    'MagicLab MagicBot', 'MagicLab', 1.74, 70,
    'MLg1 (MagicLab, its Gen1: "1740*580*280 mm", "Approcimately 70kg", "Main Structure: Aluminum Alloy", "≥ 350 N·m", '
    '"42 (Active Degrees of Freedom)": neck 2, arm 7, hand "11 (6 Active DOF, 5 Passive DOF)", waist 2, leg 6, "8-Core '
    'CPU + 100 TOPS AI Processor", "3D LiDAR + Depth Cameras ×2 + Fisheye Cameras ×3", "25 Ah (1.35 kWh)"; the '
    'register\'s MagicBot is its Gen1, E15.6 question 4), HG; E15',
    ((54, 70, 71), 'S', 'MLg1 "Approcimately 70kg" the mode, 1 kg above; HG "54" (the catalogue\'s prototype) the min '
                        '(E15.2 point 1)'),
    from_stated_joint(350, {**LEGS_12, 'Head': 2, 'Waist': 2, 'Shoulder': 6, 'Elbow': 2, 'Wrist': 6}) + [hands(6)],
    joint_sources=stated_joint_sources('MLg1', 'Maximum Joint Torque "≥ 350 N·m"', 350, 'knee') +
    "; its hands Fourier's six-joint hand per joint (E7.5 point 4)",
    **voltage_capacity(54, 'MLg1 "25 Ah (1.35 kWh)": 54 V (arith.)', 25, 'MLg1 "25 Ah"', label='S, E'),
    **with_defaults(1.74, 70, dict(
        boards=[named_board('8-core CPU', 'MLg1 "8-Core CPU"')]
        + orin_nx_read('MLg1 "100 TOPS AI Processor" (E: an Orin NX)') + [POWER_BOARD],
        sensors=[lidar('MLg1 "3D LiDAR"'), depth_camera('MLg1 "Depth Cameras ×2"', 2),
                 camera('Camera, fisheye', 3, 'Head', 'MLg1 "Fisheye Cameras ×3"'),
                 microphones('MLg1 "Omnidirectional Microphone Array"'), speaker('MLg1 "Speakers"'), IMU_NOT_NAMED],
        frame=('Frame', 'Aluminium alloys', 'MLg1 "Main Structure: Aluminum Alloy": aluminium; the remainder (E15.6 '
                                            'question 6)'))))
MAGICLAB_MAGICBOT_X1 = block(
    'MagicLab MagicBot X1', 'MagicLab', 1.80, 70,
    'MLx1 (MagicLab: "180×55.4×28" cm, "Total Weight 70kg", "Total Active DoF 31": head 2, arm 7, waist 3, leg 6, "a peak '
    'knee torque of ≥350N·m", "Aerospace-grade Lightweight Aluminum Alloy", "Titanium Alloy", "18Ah" without its '
    'voltage: on the template, "8-Core High-Performance CPU", "Orin NX", "Stereo Camera Module", "Head RGB-D Camera", '
    '"Waist RGB-D Camera"); E15', makers(70, 'MLx1 "Total Weight 70kg"'),
    from_stated_joint(350, {**LEGS_12, 'Head': 2, 'Waist': 3, 'Shoulder': 6, 'Elbow': 2, 'Wrist': 6}),
    joint_sources=stated_joint_sources('MLx1', '"a peak knee torque of ≥350N·m"', 350, 'knee'),
    **with_defaults(1.80, 70, dict(
        boards=[named_board('8-core CPU', 'MLx1 "8-Core High-Performance CPU"')]
        + orin_nx_boards('MLx1 "Orin NX"') + [POWER_BOARD],
        sensors=[binocular('MLx1 "Stereo Camera Module"'),
                 depth_camera('MLx1 "Head RGB-D Camera", "Waist RGB-D Camera"', 2), IMU_NOT_NAMED],
        frame=('Frame', 'Aluminium alloys', 'MLx1 "Aerospace-grade Lightweight Aluminum Alloy" (and "Titanium Alloy"): '
                                            'aluminium; the remainder (E15.6 question 6)'))))
MAGICLAB_MAGICBOT_Z1 = block(
    'MagicLab MagicBot Z1', 'MagicLab', 1.37, 40,
    'MLz1 (MagicLab: "1369*422*200mm", "Weight with Battery Approximately 40kg", "24" joints: leg 6, head 1, waist 1, '
    'arm 5, "Maximum Knee Torque* 100N.m", "15-cell battery", "Smart Battery (Quick Release) 10000mAh", charger "62V 5A", '
    '"8-core high-performance CPU", "3D LiDAR + Depth Camera + Binocular Fisheye Camera", microphone array, "5W '
    'Speaker"); E15', makers(40, 'MLz1 "Weight with Battery Approximately 40kg"'),
    from_stated_joint(100, {**LEGS_12, 'Head': 1, 'Waist': 1, 'Shoulder': 6, 'Elbow': 2, 'Wrist': 2}),
    joint_sources=stated_joint_sources('MLz1', '"Maximum Knee Torque* 100N.m"', 100, 'knee'),
    **voltage_capacity(55.5, 'MLz1 "15-cell battery": 15 cells at 3.7 V nominal (arith., E)', 10,
                       'MLz1 "10000mAh"', label='S, E'),
    **with_defaults(1.37, 40, dict(
        boards=[named_board('8-core CPU', 'MLz1 "8-core high-performance CPU"'), POWER_BOARD],
        sensors=[lidar('MLz1 "3D LiDAR"'), depth_camera('MLz1 "Depth Camera"'),
                 binocular('MLz1 "Binocular Fisheye Camera"'), microphones('MLz1 microphone array'),
                 speaker('MLz1 "5W Speaker"'), IMU_NOT_NAMED])))
GIGAAI_MAKER_H01 = wheeled(
    'GigaAI Maker H01', 'GigaAI', 1.60, None, catalogue(64, 'GigaAI states none (E15.1)'), WHEELED_JOINTS_MEDIAN,
    sources='HG (the catalogue: 64 kg, hands 14, "dual 7-DOF arms", a LiDAR); E15', added=(hands(7),),
    sensors=[base_lidar('HG "LiDAR"'), IMU_NOT_NAMED])
UNIX_MARTIAN = block(
    'UniX Martian', 'UniX AI', 1.48, 40,
    'UNXm (UniX: "148 cm Height", "40 kg Weight", "150 N.m Motor Max Torque", "9 Ah Battery Capacity", "48 V Rated '
    'Voltage", "6 DoF per leg", "7 DoF per arm", "3 DoF at the waist", "2 DoF at the head", "A 11-DoF industrial-grade '
    'dexterous hand", "40T Computing Power Platform 32GB Ram", "Depth Camera + RGB*2 + IMU"); E15',
    makers(40, 'UNXm "40 kg Weight"'),
    from_stated_joint(150, {**LEGS_12, 'Head': 2, 'Waist': 3, 'Shoulder': 6, 'Elbow': 2, 'Wrist': 6}) + [hands(11)],
    joint_sources=stated_joint_sources('UNXm', '"150 N.m Motor Max Torque"', 150, 'knee') +
    "; its hands Fourier's six-joint hand per joint (E7.5 point 4)",
    **voltage_capacity(48, 'UNXm "48 V Rated Voltage"', 9, 'UNXm "9 Ah Battery Capacity"'),
    **with_defaults(1.48, 40, dict(
        boards=orin_nx_read('UNXm "40T Computing Power Platform 32GB Ram" (E: an Orin NX)') + [POWER_BOARD],
        sensors=[depth_camera('UNXm "Depth Camera"'), camera('Camera, RGB', 2, 'Head', 'UNXm "RGB*2"'),
                 imu('UNXm "IMU"')])))
MATRIX_ROBOTICS_MATRIX_1 = template(
    'Matrix Robotics Matrix-1', 'Matrix Robotics', 1.80, 67, makers(67, 'MTXr "67 kg"'), JOINTS_MEDIAN + 2,
    sources='MTXr (Matrix Robotics: "180 cm", "67 kg", "2.28 KWh custom battery pack", "8 onboard RGB cameras", '
            'microphones and speakers, hand "22 degrees of freedom"); E15', added_joints=[hands(22)],
    **energy(2280, 'MTXr "2.28 KWh custom battery pack"'),
    sensors=[camera('Camera, RGB', 8, 'Head', 'MTXr "8 onboard RGB cameras"'), microphones('MTXr "microphones"'),
             speaker('MTXr "speakers"'), IMU_NOT_NAMED])

SUNDAY_MEMO = wheeled(
    'Sunday MEMO', 'Sunday Robotics', 1.70, 77.1, makers(77.1, 'SUNm "170 pounds" (77.1 kg)'), 19,
    sources='SUNm (Sunday: Height "1.7 meters", Weight "170 pounds", Arms "2×7", Hands "2×4", Torso "1", Lower Body "4", '
            'Materials "A blend of rigid and elastic polymers"); E15', added=(hands(4),), lift=True)
MENTEE_MENTEEBOT_2024 = template(
    'Mentee MenteeBot 2024', 'Mentee Robotics', 1.75, None, catalogue(70, 'Mentee states none for its 2024 robot; its '
                                                                          "form the V3's (E15.6 question 4)"),
    JOINTS_MEDIAN, sources='HG; E15')
MENTEE_MENTEEBOT_V3 = template(
    'Mentee MenteeBot V3', 'Mentee Robotics', 1.75, 70,
    ((65, 70, 71), 'S', 'MNTb "70kg" (its page, the V3\'s) the mode, 1 kg above; HG "65" the min (E15.2 point 1)'), 40,
    sources='MNTb (Mentee: "175cm", "70kg", DoF "40"; the page the V3\'s, E15.6 question 4), TRMB (Trend Hunter: '
            '"powered by two Jetson Orin AGX computing units"), HG; E15',
    boards=agx_orin('TRMB "two Jetson Orin AGX computing units"', count=2) + [POWER_BOARD])
MIROKAI_NX = [counted(row, 2) for row in orin_nx_read('RGM "2 NVIDIA Jetson NX" (E: two Orin NX)')]
ENCHANTED_TOOLS_MIROKAI = wheeled(
    'Enchanted Tools Mirokaï', 'Enchanted Tools', 1.23, None,
    ((26, 29, 30), 'S', 'RGM "WEIGHT 29 kg" (Robots Guide) the mode, 1 kg above; OBM "WEIGHT 26 kg" (a database) the '
                        'min (E15.2 point 1)'), WHEELED_JOINTS_MEDIAN,
    sources='RGM (Robots Guide: "WEIGHT 29 kg", "2 RGBD cameras, 2 infrared cameras, and 9 time-of-flight cameras", "4 '
            'microphones", "3 inertial measurement units", "2 NVIDIA Jetson NX", "Hand: 2 DoF x 2", "Ball mobile base: 3 '
            'DoF"; three driven, E15.2 point 6), OBM; E15', driven=3, caster_count=0, added=(hands(2),),
    boards=MIROKAI_NX + [POWER_BOARD],
    sensors=[depth_camera('RGM "2 RGBD cameras"', 2), camera('Camera, infrared', 2, 'Head', 'RGM "2 infrared cameras"'),
             camera('Camera, time-of-flight', 9, 'Head', 'RGM "9 time-of-flight cameras"'),
             microphones('RGM "4 microphones"'), counted(imu('RGM "3 inertial measurement units"'), 3)])
O_ID_MODULAR = wheeled(
    'O-ID Modular', 'O-ID', 1.72, 70, makers(70, 'OIDm "70 kg" WEIGHT'), 30,
    sources='OIDm (O-ID: "172 cm" HEIGHT, "70 kg" WEIGHT, "30 DoF" AXES, "9" MODULES; four driven, E15.3); E15', driven=4,
    caster_count=0, added=(grippers(),))
AIMOGA_MORNINE = template(
    'AiMOGA Mornine', 'AiMOGA', 1.67, None,
    ((65, 70, 71), 'S', 'CNCm "weighs 70kg" (CarNewsChina) the mode, 1 kg above; ITHm "65kg" (IT之家) the min (E15.2 '
                        'point 1)'), JOINTS_MEDIAN + 2,
    sources='ITHm (IT之家: "167cm、65kg，拥有 41 个自由度，单手 12 自由度", "电池容量为 0.7kwh", "3D 激光雷达、2 个深度相机、1 个全景相机、4 颗超声雷达、1 颗 6 '
            '麦克风阵列"), CNCm (CarNewsChina: "weighs 70kg", "0.7 kWh battery"); E15', added_joints=[hands(12)],
    **energy(700, 'CNCm "0.7 kWh battery"'),
    sensors=[camera('Camera, panoramic', 1, 'Head', 'ITHm "1 个全景相机"'), depth_camera('ITHm "2 个深度相机"', 2),
             lidar('ITHm "3D 激光雷达"'), microphones('ITHm "1 颗 6 麦克风阵列"'), IMU_NOT_NAMED])
NOETIX_N2 = block(
    'Noetix N2', 'Noetix', 1.18, None,
    'RBTXn (RBTX, a seller: "118 cm tall and weighing 30 kg", "peak torque of 150 Nm", "48V quick-swap lithium battery" '
    'without its capacity), HG (RK3588, Orin NX, a depth camera); E15', internet(30, 'RBTXn "weighing 30 kg"'),
    from_stated_joint(150, {'Hip pitch': 2, 'Hip roll': 2, 'Hip yaw': 2, 'Knee': 2, 'Ankle pitch': 2, 'Shoulder': 6,
                            'Elbow': 2}),
    joint_sources=stated_joint_sources('RBTXn', '"peak torque of 150 Nm" (the internet\'s, E15.6 question 1)', 150,
                                       'knee'),
    **with_defaults(1.18, 30, dict(
        boards=RK3588_BOARDS + orin_nx_boards('HG "Orin NX" (the catalogue\'s)') + [POWER_BOARD],
        sensors=[depth_camera('HG "depth camera"'), IMU_NOT_NAMED])))
ZHEJIANG_NAVIGATOR_2 = template(
    'Zhejiang Navigator 2', 'Zhejiang Humanoid Robot Innovation Center', 1.65, None, internet(60, 'AIWn "60 kg"'),
    JOINTS_MEDIAN + 2,
    sources='AIWn (aiwiki: "60 kg", "Single hand weight | 600 g", "275 TOPS", "15 per hand" joints, "6 per hand" '
            'active); E15', added_joints=[stated_hands('Navigator 2, 600 g', 0.6, 'S', 'AIWn "600 g"')],
    boards=agx_orin('AIWn "275 TOPS" (E: an AGX Orin)', label='E') + [POWER_BOARD])
GENISOM_NE01 = template('GENISOM NE01', 'GENISOM', 1.45, None, catalogue(40, 'GENISOM states none (E15.1)'),
                        JOINTS_MEDIAN, sources='GNSn (GENISOM: its page gives no figures), HG; E15')
ONE_X_NEO_BETA = template('1X NEO Beta', '1X Technologies', 1.65, None, catalogue(30, '1X states none (E15.1)'),
                          JOINTS_MEDIAN, sources='HG; E15')
ONE_X_NEO_GAMMA = template(
    '1X NEO Gamma', '1X Technologies', 1.65, None, catalogue(35, '1X states none (E15.1)'), JOINTS_MEDIAN,
    sources='1XNg (1X: "four microphones (front, back, left, and right)", a "three-speaker system", the suit "3D printed '
            'from durable and soft nylon"), HG; E15',
    sensors=[microphones('1XNg "four microphones"'), counted(speaker('1XNg "three-speaker system"'), 3), IMU_NOT_NAMED])
GALAXEA_NEXO = wheeled(
    'Galaxea NEXO', 'Galaxea Dynamics', 1.68, None,
    ((78, 85, 86), 'S', 'HG "85" (the catalogue\'s) the mode, 1 kg above; OBN "WEIGHT 78 kg" (a database) the min (E15.2 '
                        'point 1)'), 30,
    sources='GXNx (Galaxea\'s release: "wheeled dual‑arm robot with 30 degrees of freedom"), OBN, HG (an AGX Orin); E15',
    driven=4, caster_count=0, boards=agx_orin('HG "AGX Orin" (the catalogue\'s)') + [POWER_BOARD])
LUMOS_NIX = template(
    'Lumos NIX', 'Lumos Robotics', 0.89, None,
    ((18, 25.41, 26.41), 'S', 'LMSn "25.41 kg (total, incl. battery)" the mode, 1 kg above; NIXd "Weight: 18 kg" (its '
                              'Nix1) the min (E15.2 point 1)'), 21,
    sources='LMSn (Lumos: "25.41 kg (total, incl. battery)", "89 cm", "21 DOF", "RGB camera", "4-mic array / speaker", '
            '"282 Wh", "RK3588"; its model files\' joints not used, E15.1), NIXd (Lumos: "Nix1 ... Weight: 18 kg"); E15',
    **energy(282, 'LMSn "282 Wh"'),
    boards=RK3588_BOARDS + [POWER_BOARD],
    sensors=[camera('Camera, RGB', 1, 'Head', 'LMSn "RGB camera"'), microphones('LMSn "4-mic array"'),
             speaker('LMSn "speaker"'), IMU_NOT_NAMED])
SHARPA_NORTH = wheeled(
    'Sharpa North', 'Sharpa', 1.60, None,
    ((59, 60, 90), 'S', 'RCN "60 kg Net weight" (a seller) the mode, 1 kg below; HG "90" the max (E15.2 point 1)'),
    WHEELED_JOINTS_MEDIAN, sources='RCN (Robotics Center, a seller: "60 kg Net weight"), HG (hands 22 a hand, a Jetson '
                                   'Thor); E15', added=(hands(22),),
    boards=thor('HG "Jetson Thor" (the catalogue\'s)') + [POWER_BOARD])
UGO_NOVA = wheeled(
    'ugo Nova', 'ugo', 1.62, 100, makers(100, 'UGOn "約 100 kg"'), 20,
    sources='UGOn (ugo: "(h)126〜162cm", "約 100 kg", 頭部 "2軸", 腕部 "7軸＋ハンド1軸2指（双腕）", 腰部 "4軸", 車体部 "4軸（メカナム4輪）", カメラ '
            '"ヘッド x1（ステレオカメラ）", "ハンド x2（RGBカメラ）", "NVIDIA Jetson Thor", "LiFePO4 | 50.6V | 22Ah"); E15', driven=4,
    caster_count=0, added=(grippers(),),
    **voltage_capacity(50.6, 'UGOn "50.6V"', 22, 'UGOn "22Ah"'), **lfp('UGOn "LiFePO4"'),
    boards=thor('UGOn "NVIDIA Jetson Thor"') + [POWER_BOARD],
    sensors=[binocular('UGOn "ヘッド x1（ステレオカメラ）"'), camera('Camera, RGB', 2, 'Arms', 'UGOn "ハンド x2（RGBカメラ）"'),
             IMU_NOT_NAMED])
SWITCHBOT_ONERO_H1 = wheeled(
    'SwitchBot Onero H1', 'SwitchBot', 1.74, None,
    ((35, 68, 69), 'S', 'HPO "Weight: 68 kg" (humanoid.press, its "prototype spec") the mode, 1 kg above; HG "~35" the '
                        'min (E15.2 point 1)'), WHEELED_JOINTS_MEDIAN,
    sources='HPO (humanoid.press: "Height: 174 cm (prototype spec) - Weight: 68 kg", "Wheeled humanoid base"), HG (four '
            'RealSense cameras); E15',
    sensors=[depth_camera('HG "RealSense" in its head, arms, hands and abdomen (four, E)', 4), IMU_NOT_NAMED])
PINK_ROBOTICS_P0 = template(
    'Pink Robotics P0', 'Pink Robotics', 1.75, 82, makers(82, 'PNKp "Weight 82kg"'), 32 + 2,
    sources='PNKp (Pink Robotics: Height "1,75m", Weight "82kg", "Motion System 32 DoF", Payload "8kg"); E15',
    added_joints=[grippers()])
PRIMEBOT_T1 = wheeled(
    'PrimeBOT T1', 'PrimeBOT', 0.60, None,
    ((8, 8.5, 9), 'S', 'HG "8.5" (the register, the catalogue\'s); ± 0.5 kg (E15.3)'), WHEELED_JOINTS_MEDIAN,
    sources='HG; E15', caster_count=0)
PL_UNIVERSE_PROWHITE = wheeled(
    'PL-Universe ProWhite', 'PL-Universe', 2.04, 400, makers(400, 'PLpw "Weight 400 kg"'), 12,
    sources='PLpw (PL-Universe: "1051mm(L)*800(W)*2035mm(H)", Weight "400 kg", arm DoF "6", "Four-wheel '
            'omnidirectional", "Liftable torso", "modular end effectors", Battery Capacity "40 v 100 Ah"); E15', driven=4,
    caster_count=0, added=(grippers(),), lift=True,
    **voltage_capacity(40, 'PLpw "40 v 100 Ah"', 100, 'PLpw "100 Ah"'))
PSIBOT_PSI_V1 = wheeled(
    'PsiBot Psi V1', 'PsiBot', 1.80, None, catalogue(150, 'PsiBot states none (E15.1)'), WHEELED_JOINTS_MEDIAN,
    sources='PSIv (PsiBot: "Standing Height ：<180cm", "Sensor：RGBD*4；Fisheye Camera*3", "Computing Platform：Thor", '
            '"Waist：2-DOF", "Neck：2-DOF"), HG; E15',
    boards=thor('PSIv "Computing Platform：Thor"') + [POWER_BOARD],
    sensors=[depth_camera('PSIv "RGBD*4"', 4), camera('Camera, fisheye', 3, 'Head', 'PSIv "Fisheye Camera*3"'),
             IMU_NOT_NAMED])

PUDU_D7_2024 = wheeled(
    'Pudu D7 2024', 'Pudu Robotics', 1.65, 45, makers(45, 'PD7r "weighs 45 kilograms"'), WHEELED_JOINTS_MEDIAN,
    sources='PD7r (Pudu\'s release of 2024-09-19: "stands 165 cm tall and weighs 45 kilograms", "a battery exceeding 1 '
            'kWh", "360-degree omnidirectional movement"; each version as often, E15.2 point 7); E15', driven=4,
    caster_count=0, **energy(1000, 'PD7r "a battery exceeding 1 kWh" (its least)'))
PUDU_D7_2026 = wheeled(
    'Pudu D7 2026', 'Pudu Robotics', 1.75, 140, makers(140, 'PUDd7 "308.6 lbs（140 kg）"'), 23,
    sources='PUDd7 (Pudu: Height "68.9 in（175 cm）", Weight "308.6 lbs（140 kg）", DoF "*excluding end effectors 23", "NVIDIA '
            'Jetson Orin + RK 3588 dual-chip platform", "275 TOPS (Optional Chip Upgrade)", "Dual-LiDAR Omni Chassis", '
            '"Front and rear LiDAR"); E15', driven=4, caster_count=0,
    boards=agx_orin('PUDd7 "NVIDIA Jetson Orin", "275 TOPS" (E: an AGX Orin)', label='E') + RK3588_BOARDS
    + [POWER_BOARD],
    sensors=[base_lidar('PUDd7 "Front and rear LiDAR"', 2), IMU_NOT_NAMED])
PUDU_D9 = block(
    'Pudu D9', 'Pudu Robotics', 1.70, 65,
    'PUDd9 (Pudu: "170 cm", "65 kg", "Total DOF 42", "Single-leg DOF 6", "Single-arm DOF 7", DH11 "Active DOF 6" and '
    '"500 g", "Maximum Joint Torque 352 N·m", "275 TOPS", RGB, RGBD, IMU, Battery "15 Ah (0.72 kWh)", speaker '
    '"Stereo"); E15', makers(65, 'PUDd9 "65 kg"'),
    from_stated_joint(352, {**LEGS_12, 'Waist': 2, 'Head': 2, 'Shoulder': 6, 'Elbow': 2, 'Wrist': 6})
    + [stated_hands('DH11', 0.5, 'S', 'PUDd9 "500 g"')],
    joint_sources=stated_joint_sources('PUDd9', '"Maximum Joint Torque 352 N·m"', 352, 'knee') +
    '; its hands PUDd9 DH11 "500 g", ± 5 % (E15.2 point 3)',
    **voltage_capacity(48, 'PUDd9 "15 Ah (0.72 kWh)": 48 V (arith.)', 15, 'PUDd9 "15 Ah"', label='S, E'),
    **with_defaults(1.70, 65, dict(
        boards=agx_orin('PUDd9 "275 TOPS" (E: an AGX Orin)', label='E') + [POWER_BOARD],
        sensors=[camera('Camera, RGB', 1, 'Head', 'PUDd9 "RGB"'), depth_camera('PUDd9 "RGBD"'), imu('PUDd9 "IMU"'),
                 speaker('PUDd9 speaker "Stereo"')])))
XPENG_PX5 = template(
    'XPENG PX5', 'XPENG', 1.50, None, catalogue(109, 'XPENG states none (E15.1)'), JOINTS_MEDIAN + 2,
    sources='HG (the catalogue: 109 kg, 150 cm, hands 11 DoF, "hand unit … weighs only 430g"); E15',
    added_joints=[stated_hands('PX5, 430 g', 0.43, 'S', 'HG "430g"')])
X_SQUARE_QUANTA_X2 = wheeled(
    'X Square QUANTA X2', 'X Square Robot', 1.64, None, catalogue(95, 'X Square states none (E15.1)'),
    WHEELED_JOINTS_MEDIAN,
    sources='X2Rq (X Square: "62 （Dexterous Hand）", "164cm", torso "6", dexterous hand "20", chassis "2", 2D LiDAR "1", '
            'RGB-D "3", BEV camera "3"), HG; E15', added=(hands(20),),
    sensors=[base_lidar('X2Rq 2D LiDAR "1"'), depth_camera('X2Rq RGB-D "3"', 3),
             camera('Camera, BEV', 3, 'Head', 'X2Rq BEV camera "3"'), IMU_NOT_NAMED])
AGIBOT_RAISE_A1 = block(
    'AgiBot RAISE A1', 'AgiBot', 1.75, 55,
    'AGA1 (AgiBot: Height "175 cm", Weight "55 kg", "200 TOPS", microphone array, Lidar, RGB-D camera, Skill-hand "Active '
    'DoF 12", PowerFlow "Peak Torque 350N·m"); E15', makers(55, 'AGA1 "Weight 55 kg"'),
    from_stated_joint(350, {**LEGS_12, 'Waist': 1, 'Shoulder': 6, 'Elbow': 2, 'Wrist': 2, 'Head': 2}) + [hands(12)],
    joint_sources=stated_joint_sources('AGA1', 'PowerFlow "Peak Torque 350N·m"', 350, 'knee') +
    "; its hands Fourier's six-joint hand per joint (E7.5 point 4)",
    **with_defaults(1.75, 55, dict(
        boards=agx_orin('AGA1 "200 TOPS" (E: an AGX Orin)', label='E') + [POWER_BOARD],
        sensors=[microphones('AGA1 "microphone array"'), lidar('AGA1 "Lidar"'), depth_camera('AGA1 "RGB-D camera"'),
                 IMU_NOT_NAMED])))
NINERAY_RAYNEX_G3 = template(
    'NineRay RayNex G3', 'NineRay', 1.73, 60, makers(60, 'NRY "60 kg"'), 32 + 2,
    sources='NRY (NineRay: "173 cm", "60 kg", "32 DoF (Body)", "Linear & Harmonic Rotary Joints"), HG (hands 12); E15',
    added_joints=[hands(6)])
ROBOSCIENCE_REX_G1 = wheeled(
    'RoboScience REX G1', 'RoboScience', 1.70, None, catalogue(80, 'RoboScience states none (E15.1)'), 18,
    sources='RSCx (RoboScience: "22个自由度（2头颈、7×2臂、2腰部、1升降以及3底盘）", "高度覆盖1100–1700mm", "2070 TFLOPS 端侧算力"; three driven, '
            'E15.2 point 6), HG; E15', driven=3, caster_count=0, lift=True,
    boards=thor('RSCx "2070 TFLOPS 端侧算力" (E: an AGX Thor)') + [POWER_BOARD])
ROBOT_COM_RNOID = wheeled(
    'Robot.com RNoid', 'Robot.com', 1.70, 90, makers(90, 'RNDs "90 kg Total weight"'), 20,
    sources='RNDs (Robot.com\'s specification sheet: "1.7 m Height", "90 kg Total weight", "Dual 7-DOF Arm DOF", "4-DOF '
            'Torso", "2-DOF Neck", "Modular End effector", "AMD Ryzen 5 7640HS Base computing", "NVIDIA Jetson AGX Orin '
            'AI module", "RGB-D camera … Head and chest", "2x RGB-D camera Wrists cameras", "360° front + rear mapping '
            'LiDAR", "Mic and speaker", "smooth omnidirectional movement"); E15', driven=4, caster_count=0,
    added=(grippers(),),
    boards=[intel('AMD Ryzen 5 7640HS', 'RNDs "AMD Ryzen 5 7640HS Base computing"')]
    + agx_orin('RNDs "NVIDIA Jetson AGX Orin AI module"') + [POWER_BOARD],
    cooler=x86_and_arm('its AMD computer and its AGX Orin'),
    sensors=[depth_camera('RNDs "RGB-D camera … Head and chest" (two) and "2x RGB-D camera Wrists cameras"', 4),
             base_lidar('RNDs "360° front + rear mapping LiDAR"', 2), microphones('RNDs "Mic"'),
             speaker('RNDs "speaker"'), IMU_NOT_NAMED])
ROBBYANT_R1 = wheeled(
    'Robbyant R1', 'Robbyant', 1.60, None, catalogue(110, 'Robbyant states none (E15.1)'), WHEELED_JOINTS_MEDIAN,
    sources='HG (the catalogue: 110 kg; its joint modules by Ti5, its chassis by Galaxea, as Bloomberg reports, not '
            'reread); E15')
OVERSONIC_ROBEE = wheeled(
    'Oversonic RoBee', 'Oversonic Robotics', 1.99, None,
    ((179, 180, 293), 'S', 'HG "180" (the catalogue\'s) the mode, 1 kg below; OVRr "Up to 293 kg" (its brochure, Series R) '
                           'the max (E15.2 point 1; the register\'s RoBee its Series R, E15.6 question 4)'),
    WHEELED_JOINTS_MEDIAN,
    sources='OVRr (Oversonic, RoBee Series R brochure 10/2026: "165 — 199 cm", "Up to 293 kg", depth cameras in its head, '
            'chest, waist and base, "Laser 3D", "Laser scanner safety", a thermal camera, "Omnidirectional drive", '
            '"Batteries included 2", "Mechanical gripper"), HG; E15', driven=4, caster_count=0, added=(grippers(),),
    lift=True,
    sensors=[depth_camera('OVRr depth cameras in its head, chest and waist', 3),
             base_depth_camera('OVRr a depth camera in its base'), lidar('OVRr "Laser 3D"'),
             base_lidar('OVRr "Laser scanner safety"'), camera('Camera, thermal', 1, 'Head', 'OVRr a thermal camera'),
             IMU_NOT_NAMED])
ROBOLIGENT_ROBIN = wheeled(
    'Roboligent Robin', 'Roboligent', 1.80, 105, makers(105, 'RBLr "105 kg Total weight"'), 14,
    sources='RBLr (Roboligent: "Two 7-DOF arms on an omni-directional base, with a motorized lifting column", "105 kg '
            'Total weight", "Parallel gripper, 120 mm stroke"); E15', driven=4, caster_count=0, added=(grippers(),),
    lift=True)
ROBO_ROBOTICS_ROBO_T1 = wheeled(
    'Robo Robotics ROBO-T1', 'Robo Robotics', 1.30, None,
    ((45, 50, 60), 'S', 'OBR "WEIGHT Approx. 45–60 kg" (a database) its range, HG "50" the mode (E15.2 point 1)'), 12,
    sources='RBOi (Robo: "two 6-DOF robot arms with grippers"), OBR, HG; E15', added=(grippers(),))
ROBOTERA_Q5 = wheeled(
    'ROBOTERA Q5', 'ROBOTERA', 1.65, 70, makers(70, 'RTq5 Weight "70 Kg"'), 20,
    sources='RTq5 (ROBOTERA\'s Q5 brochure: "582*519*1650 mm", Weight "70 Kg", "Neck: 2 DoF", "Waist: 1 DoF", "Arms: 7 DoF '
            'X 2", "Hands: 11 DoF X 2", "Legs: 3 DoF", "Drive Wheels X2", "Omni Wheels X4", "3D LIDAR", "Binocular '
            'Camera", Supply Voltage "60 V" without its capacity: on the template); E15', caster_count=4,
    added=(hands(11),),
    sensors=[lidar('RTq5 "3D LIDAR"'), binocular('RTq5 "Binocular Camera"'), IMU_NOT_NAMED])
ENGINEAI_SA02_ON_LEGS, ENGINEAI_SA02_ON_WHEELS = on_legs_and_wheels(
    'EngineAI SA02', 'EngineAI', 1.25, catalogue(25, 'EngineAI states none (E15.1)'), 0,
    sources=f'TNS (TechNode: "1.25-meter-tall, 25-kilogram", "dual high-definition cameras"), HG; {NO_FORM}; E15',
    sensors=[camera('Camera', 2, 'Head', 'TNS "dual high-definition cameras"'), IMU_NOT_NAMED])
ATI_SHERPA_MECHA = wheeled(
    'Ati Sherpa Mecha', 'Ati Motors', 2.00, None, catalogue(180, 'Ati states none (E15.1)'), 19,
    sources='ATIs (Ati: "Dual-arm mobile manipulator on autonomous wheeled base", "Dual arms with 19 degrees of freedom", '
            '"1,100 mm – 2,000 mm — extending torso", "Carbon-fibre" arms, "3D LiDAR and Camera", Battery "55 Ah × 2" '
            'without its voltage: on the template), HG; E15', lift=True,
    sensors=[lidar('ATIs "3D LiDAR"'), camera('Camera', 1, 'Head', 'ATIs "Camera"'), IMU_NOT_NAMED])
EIR_SKYWALKER_2_ON_LEGS, EIR_SKYWALKER_2_ON_WHEELS = on_legs_and_wheels(
    'EIR SkyWalker 2', 'EIR', 1.65, catalogue(55, 'EIR states none (E15.1)'), 0,
    sources=f'HG (the catalogue: 55 kg, hands 12; {NO_FORM}); E15', added=(hands(6),))


def shoulder_stated(torque: float, counts: dict) -> list:
    """Every body joint of a robot on wheels whose maker states its arm's torque only (the Spaceo M1's "160 kg cm"): its
    waist's torque the stated one over the shoulder's median ratio, so that its shoulder is the stated torque, every
    other joint by its kind's ratio (E12.5 point 2)."""
    return from_stated_joint(torque / WHEEL_RATIOS['Shoulder'][1], counts, on_wheels=True)


MUKS_SPACEO_M1 = block(
    'Muks Spaceo M1', 'Muks Robotics', 1.63, 45,
    'MUKm1 (Muks: "1625x420x390 mm", "Weight (With Battery) ~45 kg", "12 dof": arm 5, base 2, "Maximum Torque of Arm Joint '
    'About 160 kg cm", "Aluminium body with polymer covers", microphone array, RGB camera, "2D LiDAR", "Intel RealSense '
    'Depth Camera", "RYZEN 7, 16GB RAM", "Orin AGX (~275 TOPS)", "25.6V, 45Ah LiFePO4 Battery"); E15',
    makers(45, 'MUKm1 "~45 kg"'),
    shoulder_stated(15.7, {'Shoulder': 6, 'Elbow': 2, 'Wrist': 2}) + [grippers(), T2.hub_motors(2, 45)[0]],
    joint_sources=stated_joint_sources('MUKm1', '"Maximum Torque of Arm Joint About 160 kg cm" (15.7 N·m)', 15.7,
                                       'shoulder') +
    '; its two drive wheels hub motors by its mass per driven wheel (E9.6 point 4)',
    battery_region='Base', **voltage_capacity(25.6, 'MUKm1 "25.6V, 45Ah"', 45, 'MUKm1 "45Ah"'),
    **with_defaults(1.63, 45, dict(
        **lfp('MUKm1 "LiFePO4 Battery"'), parts=[T2.casters(2)],
        boards=[intel('AMD Ryzen 7', 'MUKm1 "RYZEN 7, 16GB RAM"')] + agx_orin('MUKm1 "Orin AGX (~275 TOPS)"')
        + [POWER_BOARD], cooler=x86_and_arm('its AMD computer and its AGX Orin'),
        sensors=[camera('Camera, RGB', 1, 'Head', 'MUKm1 "RGB camera"'),
                 depth_camera('MUKm1 "Intel RealSense Depth Camera"'), base_lidar('MUKm1 "2D LiDAR"'),
                 microphones('MUKm1 "microphone array"'), IMU_NOT_NAMED],
        frame=('Frame', 'Aluminium alloys', 'MUKm1 "Aluminium body with polymer covers": aluminium; the remainder '
                                            '(E15.6 question 6)'))))
SPACEO_PRO_JOINTS = [joint('Shoulder', 6, 66, T2.from_torque(66), 'Shoulders', 'Arms') if j[0] == 'Shoulder' else j
                     for j in from_stated_joint(90, {'Waist': 1, 'Shoulder': 6, 'Elbow': 2, 'Wrist': 4, 'Head': 2},
                                                on_wheels=True)]
MUKS_SPACEO_PRO = block(
    'Muks Spaceo Pro', 'Muks Robotics', 1.63, 60,
    'MUKpr (Muks: "(1625-2100)x450x450 mm", "60 kg", "20 (Waist and Gripper (optional))": arm 6, base 2, waist 1, arm '
    'joint "66 Nm", waist "90 Nm", "Aluminium body with polymer covers", RealSense, "RGB Camera*3", "RYZEN 7", "Jetson '
    'Orin AGX (~275 TOPS)", "25.6V, 45Ah LiFePO4 Battery"); E15', makers(60, 'MUKpr "60 kg"'),
    SPACEO_PRO_JOINTS + [grippers(), T2.hub_motors(2, 60)[0], T2.lift_motor()],
    joint_sources=stated_joint_sources('MUKpr', 'waist "90 Nm"', 90, 'waist') + '; its shoulders "66 Nm" as stated, '
    'the refit at it; its two drive wheels hub motors by its mass per driven wheel (E9.6 point 4); its lift motor as '
    "ROBOTIS's (E)",
    battery_region='Base', lift_column=T2.LIFT_BY_SHARE,
    **voltage_capacity(25.6, 'MUKpr "25.6V, 45Ah"', 45, 'MUKpr "45Ah"'),
    **with_defaults(1.63, 60, dict(
        **lfp('MUKpr "LiFePO4 Battery"'), parts=[T2.casters(2)],
        boards=[intel('AMD Ryzen 7', 'MUKpr "RYZEN 7"')] + agx_orin('MUKpr "Jetson Orin AGX (~275 TOPS)"')
        + [POWER_BOARD], cooler=x86_and_arm('its AMD computer and its AGX Orin'),
        sensors=[depth_camera('MUKpr "RealSense"'), camera('Camera, RGB', 3, 'Head', 'MUKpr "RGB Camera*3"'),
                 microphones('MUKpr microphone array'), IMU_NOT_NAMED],
        frame=('Frame', 'Aluminium alloys', 'MUKpr "Aluminium body with polymer covers": aluminium; the remainder '
                                            '(E15.6 question 6)'))))
STAR1_JOINTS = [('Head yaw', 1, 35), ('Head pitch', 1, 35), ('Shoulder pitch', 2, 110), ('Shoulder roll', 2, 110),
                ('Shoulder yaw', 2, 110), ('Elbow pitch', 2, 110), ('Elbow yaw', 2, 35), ('Wrist pitch', 2, 35),
                ('Wrist roll', 2, 35), ('Waist pitch', 1, 220), ('Waist roll', 1, 220), ('Waist yaw', 1, 110),
                ('Hip roll', 2, 255), ('Hip yaw', 2, 100), ('Hip pitch', 2, 400), ('Knee', 2, 400),
                ('Ankle pitch', 2, 100), ('Ankle roll', 2, 100)]
ROBOTERA_STAR1 = block(
    'Robotera Star1', 'ROBOTERA', 1.71, None,
    'RTXm (ROBOTERA\'s model file star1/urdf/l3_with_hand_fixedpin_xml.urdf: 31 body joints and their effort limits, '
    '24 hand joints, links 64.001 kg), HG; E15', catalogue(63, 'ROBOTERA states none (E15.1)'),
    model_joints(STAR1_JOINTS, T2.from_torque) + [hands(12)],
    joint_sources="RTXm its joints' effort limits; each module the refit at its torque, 0.0689 kg × torque^0.566, half "
                  "to 1.5 times (E14.1); its hands Fourier's six-joint hand per joint (E7.5 point 4)",
    **with_defaults(1.71, 63, {}))
STARBOT_NOVA = wheeled(
    'StarBot Nova', 'StarBot', 1.52, 31.8, makers(31.8, 'STBn "70 lb" (31.8 kg)'), 14,
    sources='STBn (StarBot: Nova "5 ft", "70 lb", "two 7-DOF arms", "Wheeled base, differential drive", "Depth cameras '
            '(Intel RealSense class), RGB camera, IMU"); E15',
    sensors=[depth_camera('STBn "Depth cameras (Intel RealSense class)" (one, E)'),
             camera('Camera, RGB', 1, 'Head', 'STBn "RGB camera"'), imu('STBn "IMU"')])
SULU_BE_STEVE_ON_LEGS, SULU_BE_STEVE_ON_WHEELS = on_legs_and_wheels(
    'Sulu.be Steve', 'Sulu.be', 2.00,
    ((99, 100, 140), 'S', 'GEs "Steve, who weighs 100 kilograms" the mode, 1 kg below; HG "140" the max (E15.2 point 1)'),
    0, sources=f'GEs (GE Reports, 2015: "Steve, who weighs 100 kilograms and stands two meters tall"), HG; {NO_FORM}; '
               f'E15')
SYNTHEVA_SYNTHIA = template(
    'Syntheva Synthia', 'Syntheva', 1.75, None,
    ((9.8, 10.9, 12.0), 'S', 'SYNt "9.8 - 12.0 kg" its range, the middle the mode (E15.2 point 1)'), 23,
    sources='SYNt (Syntheva: "165 - 190 cm", "9.8 - 12.0 kg", "BCM2712 CPU (base model)", "dual cameras", "microphone", '
            '"23 powerful and precise servos"); E15',
    boards=[named_board('BCM2712', 'SYNt "BCM2712 CPU (base model)"'), POWER_BOARD],
    sensors=[camera('Camera', 2, 'Head', 'SYNt "dual cameras"'), microphones('SYNt "microphone"'), IMU_NOT_NAMED])
WORKFAR_SYNTRO = wheeled(
    'WorkFar Syntro', 'WorkFar', 1.70, 108, makers(108, 'WKFs "240 lbs (108kg)"'), 18,
    sources='WKFs (WorkFar: "5′ 8″ (1.7m)", "240 lbs (108kg)", "Head: 2 / Arms: 4 (x2) / Wrist: 3 (x2) / Hands: 12 (x2) / '
            'Waist: 2 / Wheels: 3", "2D LiDAR / Camera(s) / Computer Vision / Microphone(s)", "Intel Multi Core I5", '
            '"Swappable Batteries 1.2 kWh", "3 All-directional Omni Wheels", "Aluminum / Stainless Steel / Carbon Steel / '
            'Brass / Acetal / Carbon-fiber Filament"); E15', driven=3, caster_count=0, added=(hands(12),),
    **energy(1200, 'WKFs "Swappable Batteries 1.2 kWh"'),
    boards=[intel('Intel i5', 'WKFs "Intel Multi Core I5"'), POWER_BOARD], cooler=X86_COOLER,
    sensors=[base_lidar('WKFs "2D LiDAR"'), camera('Camera', 1, 'Head', 'WKFs "Camera(s)" (one, E)'),
             microphones('WKFs "Microphone(s)"'), IMU_NOT_NAMED],
    frame=('Frame', 'Aluminium alloys', 'WKFs "Aluminum / Stainless Steel / Carbon Steel / Brass / Acetal / Carbon-fiber '
                                        'Filament": aluminium; the remainder (E15.6 question 6)'))
IHUB_TARA_GEN1 = wheeled('iHub TARA GEN1', 'iHub', 1.63, None, catalogue(75, 'iHub states none (E15.1)'),
                         WHEELED_JOINTS_MEDIAN, sources='HG; E15')

def _type_one():
    """Type 1's builder, imported once under its own name: the Unitree G1's rows, which the Tau Humanoid takes (one
    copy of them)."""
    name = 'make_parts_taken_apart_type_1'
    if name not in sys.modules:
        path = os.path.join(TOOLS, '1_compact_research_developer', 'make_parts_taken_apart.py')
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
    return sys.modules[name]


# The Unitree G1's joints as type 1's file has them (its every joint's torque, its module as weighed by China Post
# Securities, scaled by no factor: E2.8): for the Tau Humanoid, a modified G1 (E15.3).
G1_JOINTS = [joint(r[2], r[3], r[5], (None, None, None), r[10], r[11], size=r[4])
             for r in _type_one().JOINTS_G1_X1_N1 if r[0] == 'Unitree G1']
TAU_ROBOTICS_TAU_HUMANOID = block(
    'Tau Robotics Tau Humanoid', 'Tau Robotics', 1.32, None,
    'HGT (humanoid.guide on MarketWatch: "modified Unitree G1 robots", "pincer hands"), TAUh (Tau: its page gives no '
    'figures), HG; its joints and battery the Unitree G1\'s of type 1\'s file (E15.3), E; E15',
    catalogue(35, 'Tau states none; a modified Unitree G1 (E15.3)'), G1_JOINTS + [grippers()],
    joint_sources="the Unitree G1's joints (type 1's file: its torques, its modules as weighed, E2.8), as the Tau is a "
                  'modified G1 (HGT), E; its grippers ("pincer hands") as the RH-P12-RN (E)',
    # The G1's stated numbers carried over by an estimate (a modified G1): S, E, as an arithmetic voltage is.
    voltage=((46.8, 46.8, 46.8), 'S, E', "the G1's (type 1's: T1 slide 25, 13 cells in series), the Tau a modified G1"),
    capacity=((8.55, 9, 9.45), 'S, E', "the G1's (type 1's: T1 slide 25, U1, ± 5 %), the Tau a modified G1"),
    pack=((2.25, 2.5, 2.75), 'S, E', "the G1's (type 1's: T1 slide 25, \"~2.5kg\", ± 10 %), the Tau a modified G1"),
    **with_defaults(1.32, 35, {}))


def tora_doubleone(x: bool) -> dict:
    """The Tora DoubleOne, P and X, each as often (E15.2 point 7): joints from its "Peak Joint Torque (full body) 207
    Nm" at its waist (E12.5 point 2, on wheels), its hands 18 joints each, 47 Ah (1214.01 Wh), an AGX Orin; the P on a
    steered omnidirectional base, the X on a four-wheel drive one; each with its lift."""
    name, mass = ('PaXini Tora DoubleOne X', internet(73, 'RBTXx "Weight 73 kg"')) if x else \
        ('PaXini Tora DoubleOne P', catalogue(70, 'PaXini states none for the P (E15.1)'))
    counts = {'Waist': 2, 'Second waist': 2, 'Shoulder': 6, 'Elbow': 2, 'Wrist': 6, 'Head': 2}
    base = [T2.hub_motors(4, mass[0][1])[0]] + ([] if x else [T2.steering(4)]) + [T2.lift_motor()]
    return block(
        name, 'PaXini', 1.69 if x else 1.64, 73 if x else None,
        'PXNt (PaXini\'s parameter image: P "671 mm × 548 mm × 1276~1638 mm", X "767 mm × 486 mm × 1330~1692 mm", "Total '
        'Joint Motors (excluding dexterous hands & drive wheels)" P "20", X "22", P "4WD&4WS omnidirectional chassis", X '
        '"4-wheel drive active obstacle-surmounting chassis", "Nvidia Jetson AGX Orin Dev. Kit 64G", "RGB Camera: 1 '
        '(head). RGBD Camera: 2 (head, abdomen). 3D LIDAR: 1 (head)", "IMU: 2 (head, chassis)", "Front and rear '
        '8-Microphone Array", "10 W Speaker", "47 Ah (1214.01 Wh)", "Peak Joint Torque (full body) 207 Nm"; no mass), '
        + ('RBTXx (RBTX, a seller: "Weight 73 kg Height 1,687 mm", "18‑DOF hands")' if x else 'HG') + '; E15', mass,
        from_stated_joint(207, counts, on_wheels=True) + [hands(18)] + base,
        joint_sources=stated_joint_sources('PXNt', '"Peak Joint Torque (full body) 207 Nm"', 207, 'waist') +
        "; its hands Fourier's six-joint hand per joint (E7.5 point 4); its four drive wheels hub motors by its mass "
        'per driven wheel (E9.6 point 4)' + ('' if x else ", its steering motors as ROBOTIS's (E)") +
        "; its lift motor as ROBOTIS's (E)",
        battery_region='Base', lift_column=T2.LIFT_BY_SHARE,
        **voltage_capacity(round(1214.01 / 47, 4), 'PXNt "47 Ah (1214.01 Wh)": 25.83 V (arith.)', 47, 'PXNt "47 Ah"',
                           label='S, E'),
        **with_defaults(1.69 if x else 1.64, mass[0][1], dict(
            boards=agx_orin('PXNt "Nvidia Jetson AGX Orin Dev. Kit 64G"') + [POWER_BOARD],
            sensors=[camera('Camera, RGB', 1, 'Head', 'PXNt "RGB Camera: 1 (head)"'),
                     depth_camera('PXNt "RGBD Camera: 2 (head, abdomen)"', 2), lidar('PXNt "3D LIDAR: 1 (head)"'),
                     counted(imu('PXNt "IMU: 2 (head, chassis)"'), 2),
                     counted(microphones('PXNt "Front and rear 8-Microphone Array"'), 2),
                     speaker('PXNt "10 W Speaker"')])))


PAXINI_TORA_DOUBLEONE_P, PAXINI_TORA_DOUBLEONE_X = tora_doubleone(False), tora_doubleone(True)
UBTECH_U1_PRO_MALE = template(
    'UBTECH U1 Pro male', 'UBTECH Robotics', 1.83, None,
    internet(42, 'AIWu "the male stands 183 cm and weighs 42 kg"'), JOINTS_MEDIAN,
    sources='AIWu (aiwiki: "the male stands 183 cm and weighs 42 kg, and the female stands 168 cm and weighs 35.2 kg"; '
            'each version as often, E15.2 point 7); E15')
UBTECH_U1_PRO_FEMALE = template(
    'UBTECH U1 Pro female', 'UBTECH Robotics', 1.68, None,
    internet(35.2, 'AIWu "the female stands 168 cm and weighs 35.2 kg"'), JOINTS_MEDIAN,
    sources='AIWu (aiwiki: "the female stands 168 cm and weighs 35.2 kg"); E15')
TUESDAY_LABS_VOXEL = template(
    'Tuesday Labs Voxel', 'Tuesday Labs', 1.50, None, catalogue(45, 'Tuesday Labs states none (E15.1)'),
    JOINTS_MEDIAN + 2,
    sources='TSDv (Tuesday Labs: "7-DOF Arms with Fully Actuated Wrists", "1-DOF Grippers", "Z-Shaped Legs with '
            'Impact-Aware Feet", "Stereo RGB + Wide-Field Vision"), HG; E15', added_joints=[grippers()],
    sensors=[binocular('TSDv "Stereo RGB"'), IMU_NOT_NAMED])
DEXFORCE_W1_PRO = wheeled(
    'DexForce W1 Pro', 'DexForce', 1.64, 110, makers(110, 'DXFw1 Weight "110kg"'), 20,
    sources='DXFw1 (DexForce: Weight "110kg", "682mm*550mm*1636mm", "34 DOF … differential", Neck 2, Waist 2, Leg 2, arm "7 '
            'DOF", "Dexterous Hand", "6 Active DOF", "6cm Baseline Humanoid Binocular Vision", navigation LiDAR "2 pcs", '
            'navigation cameras "2 pcs", Battery Capacity "40 Ah" without its voltage or chemistry: on the template, '
            '"Dual-PC Architecture (≥300 TOPS)"); E15', added=(hands(6),),
    boards=[counted((COMPUTER_NOT_NAMED, 1, 'Boards', 'Torso', COMPUTER, 'ITC', 'E',
                     'DXFw1 "Dual-PC Architecture (≥300 TOPS)": two computer boards, as the X1\'s and N1\'s (E)'), 2),
            POWER_BOARD],
    sensors=[binocular('DXFw1 "6cm Baseline Humanoid Binocular Vision"'),
             base_lidar('DXFw1 navigation LiDAR "2 pcs"', 2),
             camera('Camera, navigation', 2, 'Head', 'DXFw1 navigation cameras "2 pcs"'), IMU_NOT_NAMED])
WALDEN_ROBOTICS_WALDEN = wheeled(
    'Walden Robotics Walden', 'Walden Robotics', 1.65, None, catalogue(90, 'Walden states none (E15.1)'),
    WHEELED_JOINTS_MEDIAN, sources='HG (the catalogue: 90 kg, a wheeled base, two-finger grippers); E15',
    added=(grippers(),))
UBTECH_WALKER_C = template(
    'UBTECH Walker C', 'UBTECH Robotics', 1.63, 43, makers(43, 'UBwc Weight "43kg"'), 20,
    sources='UBwc (UBTECH: Height "163cm", Battery "Lithium Battery 48V 15Ah", Weight "43kg", Degrees of Freedom "20", '
            'Camera "RGBD*2, All-Scenario Binocular Structured Light3D Camera*2"); E15',
    **voltage_capacity(48, 'UBwc "48V 15Ah"', 15, 'UBwc "15Ah"'),
    sensors=[depth_camera('UBwc "RGBD*2"', 2), binocular('UBwc "Binocular Structured Light3D Camera*2"', 2),
             IMU_NOT_NAMED])
UBTECH_WALKER_C1 = template(
    'UBTECH Walker C1', 'UBTECH Robotics', 1.64, 55, makers(55, 'UBwc1 "Weight 55kg"'), 53,
    sources='UBwc1 (UBTECH, its images: "53 of DOF", "Height 164cm", "Weight 55kg", "NVIDIA® Jetson Thor™ 2070 TFLOPS '
            '(FP4)", "Fish-eye Camera*2", "Binocular Camera*1", "Monocular Camera*1", "Speaker*2", "Automotive-grade '
            'Battery" without its capacity); E15',
    boards=thor('UBwc1 "NVIDIA® Jetson Thor™"') + [POWER_BOARD],
    sensors=[camera('Camera, fisheye', 2, 'Head', 'UBwc1 "Fish-eye Camera*2"'), binocular('UBwc1 "Binocular Camera*1"'),
             camera('Camera, monocular', 1, 'Head', 'UBwc1 "Monocular Camera*1"'),
             counted(speaker('UBwc1 "Speaker*2"'), 2), IMU_NOT_NAMED])
UBTECH_WALKER_S1 = block(
    'UBTECH Walker S1', 'UBTECH Robotics', 1.72, 76,
    'UBws1 (UBTECH, its images: "Height 172cm", "Weight 76kg", "Self-developed Integrated Joints … Peak Torques 250N.m", '
    '"Dexterous Hands", "RGBD*1" in its head and in its torso, "Stereo RGB Camera*2", "Speaker*2", "IMU"; its joints per '
    'body part as the CYBORG RO1\'s, E15.2 point 2); E15', makers(76, 'UBws1 "Weight 76kg"'),
    from_stated_joint(250, {**LEGS_12, 'Waist': 3, 'Shoulder': 6, 'Elbow': 2, 'Wrist': 6, 'Head': 2}) + [hands(6)],
    joint_sources=stated_joint_sources('UBws1', '"Peak Torques 250N.m"', 250, 'knee') +
    "; its hands Fourier's six-joint hand per joint (E7.5 point 4)",
    **with_defaults(1.72, 76, dict(
        sensors=[depth_camera('UBws1 "RGBD*1" in its head and in its torso', 2),
                 binocular('UBws1 "Stereo RGB Camera*2"', 2), counted(speaker('UBws1 "Speaker*2"'), 2),
                 imu('UBws1 "IMU"')])))
UBTECH_WALKER_S2 = template(
    'UBTECH Walker S2', 'UBTECH Robotics', 1.76, 70, makers(70, 'UBws2 "Weight 70kg"'), 30 + 2,
    sources='UBws2 (UBTECH, its images: "Height 176cm", "Weight 70kg", "52 of DOF", "Gen-4 Industrial Dexterous Hands 11 '
            'of DOF", "4 Array Microphones", "2 Speakers", "Aerospace-grade Aluminum Alloy", "Fish-eye Camera*2", "RGB '
            'Camera*2", "RGBD Camera*1" front and back), BDNw (Battery Design: "Total energy = 2.3 kWh Nominal voltage = '
            '48 V"); E15', added_joints=[hands(11)],
    **voltage_capacity(48, 'BDNw "Nominal voltage = 48 V"', round(2300 / 48, 4),
                       'BDNw "Total energy = 2.3 kWh" over 48 V (arith.)'),
    sensors=[camera('Camera, fisheye', 2, 'Head', 'UBws2 "Fish-eye Camera*2"'),
             camera('Camera, RGB', 2, 'Head', 'UBws2 "RGB Camera*2"'),
             depth_camera('UBws2 "RGBD Camera*1" front and back', 2), microphones('UBws2 "4 Array Microphones"'),
             counted(speaker('UBws2 "2 Speakers"'), 2), IMU_NOT_NAMED],
    frame=('Frame', 'Aluminium alloys', 'UBws2 "Aerospace-grade Aluminum Alloy": aluminium; the remainder (E15.6 '
                                        'question 6)'))
YUE_QUAN_X_BOT = template(
    'Yue Quan X-Bot', 'Yue Quan Bionics', 1.67, None, catalogue(60, 'Yue Quan states none (E15.1)'), JOINTS_MEDIAN,
    sources='HG (the catalogue: 60 kg, an Orin NX and an Intel NUC, a depth camera and a LiDAR); E15',
    boards=orin_nx_boards('HG "Orin NX" (the catalogue\'s)') + [intel('Intel NUC', 'HG "Intel NUC" (the catalogue\'s)'),
                                                                 POWER_BOARD],
    cooler=x86_and_arm('its Intel computer and its Orin NX'),
    sensors=[depth_camera('HG "depth camera"'), lidar('HG "LiDAR"'), IMU_NOT_NAMED])
BYD_XIAO_DI = template('BYD Xiao Di', 'BYD', 1.61, None, catalogue(58.5, 'BYD states none (E15.1)'), JOINTS_MEDIAN,
                       sources='HG; E15')
TENCENT_XIAO_LIU_ON_LEGS, TENCENT_XIAO_LIU_ON_WHEELS = on_legs_and_wheels(
    'Tencent Xiao Liu', 'Tencent Robotics X', 1.65,
    ((55, 70, 71), 'S', 'HG "70" (the catalogue\'s) the mode, 1 kg above; HPX "Weight: ~55–60 kg" (humanoid.press) the '
                        'min (E15.2 point 1)'), 0,
    sources=f'HPX (humanoid.press: "Bipedal", "Weight: ~55–60 kg"), HG; {NO_FORM}; E15')
DIGIT_XIAQI = template(
    'Digit XiaQi', 'Digit', 1.69, 69,
    ((68, 69, 69), 'S', 'DGTx "≤ 69kg" (its most) the mode and the max, 1 kg below (E15.2 point 1)'), JOINTS_MEDIAN,
    sources='DGTx (Digit, its image: "169cm", "≤ 69kg", "700woh" (700 Wh), "≥2h"); E15',
    **energy(700, 'DGTx "700woh" (700 Wh)'))
LEJU_XTRON_KUAVO_MY = template(
    'Leju XTRON KUAVO-MY', 'Leju Robotics', 1.66, None,
    ((50, 55, 56), 'S', 'HG "55" (the catalogue\'s) the mode, 1 kg above; 50 the min (E15.3: the internet\'s 45 to 55 kg, '
                        'not reread)'), JOINTS_MEDIAN,
    sources='HG (the catalogue: 55 kg, 166 cm, a stereo depth camera, a 6-microphone array, a LiDAR); E15',
    sensors=[depth_camera('HG "stereo depth"'), microphones('HG "6-microphone array"'), lidar('HG "LiDAR"'),
             IMU_NOT_NAMED])
YUNMU_YMBOT_C = template('Yunmu YMBot C', 'Jiangsu Yunmu', 1.74, None, catalogue(75, 'Yunmu states none (E15.1)'),
                         JOINTS_MEDIAN, sources='HG; E15')
YUNMU_YMBOT_H = wheeled('Yunmu YMBot H', 'Jiangsu Yunmu', 1.70, None, catalogue(75, 'Yunmu states none (E15.1)'),
                        WHEELED_JOINTS_MEDIAN, sources='HG; E15')
ZERITH_H1 = wheeled(
    'Zerith H1', 'Zerith', 1.80, None, catalogue(55, 'Zerith states none (E15.1)'), 23,
    sources='ZRTh (Zerith: "轮臂人形机器人", "7 轴" arms, "23总 自由度"), HG (a 3D LiDAR, a depth camera); E15',
    sensors=[lidar('HG "3D LiDAR"'), depth_camera('HG "depth camera"'), IMU_NOT_NAMED])
ZERITH_Z1 = block(
    'Zerith Z1', 'Zerith', 1.45, None,
    'RBTXz (RBTX, a seller: "21 degrees of freedom", "up to 150 Nm peak joint torque", "Weight 33 kg Height 1,450 mm"), '
    'HG (an RGB and a depth camera, a LiDAR, an IMU); E15', internet(33, 'RBTXz "Weight 33 kg"'),
    from_stated_joint(150, {**LEGS_12, 'Waist': 1, 'Shoulder': 6, 'Elbow': 2}),
    joint_sources=stated_joint_sources('RBTXz', '"up to 150 Nm peak joint torque" (the internet\'s, E15.6 question 1)',
                                       150, 'knee'),
    **with_defaults(1.45, 33, dict(sensors=[camera('Camera, RGB', 1, 'Head', 'HG "RGB"'),
                                            depth_camera('HG "depth camera"'), lidar('HG "LiDAR"'), imu('HG "IMU"')])))
PL_UNIVERSE_ZEUS_1 = wheeled(
    'PL-Universe Zeus 1', 'PL-Universe', 1.95, None, internet(300, 'CHZ "300Kg的整机重量"'), WHEELED_JOINTS_MEDIAN,
    sources='CHZ (中华网: "300Kg的整机重量", "四轮全向行走", "48V、40Ah电池"), AIWz (aiwiki: "weighing about 300 kg", Zeus 1 the 大白 named); '
            'E15', driven=4, caster_count=0, lift=True,
    **voltage_capacity(48, 'CHZ "48V、40Ah电池"', 40, 'CHZ "40Ah"'))
PERCEPTYNE_PR_OMNI = wheeled(
    'Perceptyne PR-OMNI', 'Perceptyne', 1.57, 120, makers(120, 'PRCo Weight "120 kg"'), 16,
    sources='PRCo (Perceptyne: Height "5\'2"", Weight "120 kg", Body Material "Aluminium", "Dual arms, 7 DOF each", Head "2 '
            'DOF", "4 Wheel holonomic drive", "Indoor SLAM with dual LiDARs", "3 RGBD cameras (2 wrists + 1 head)", '
            'Vertical Gantry Range "800 mm", "3 kWh (2 × 1.5 kWh, swappable)", "Nvidia Jetson Orin + Intel NUC 5th '
            'Gen"); E15', driven=4, caster_count=0, added=(grippers(),), lift=True,
    **energy(3000, 'PRCo "3 kWh (2 × 1.5 kWh, swappable)"'),
    boards=agx_orin('PRCo "Nvidia Jetson Orin" (E: an AGX Orin)', label='E')
    + [intel('Intel NUC', 'PRCo "Intel NUC 5th Gen"'), POWER_BOARD],
    cooler=x86_and_arm('its Intel computer and its AGX Orin'),
    sensors=[depth_camera('PRCo "3 RGBD cameras (2 wrists + 1 head)"', 3), base_lidar('PRCo "dual LiDARs"', 2),
             IMU_NOT_NAMED],
    frame=('Frame', 'Aluminium alloys', 'PRCo Body Material "Aluminium": aluminium; the remainder (E15.6 question 6)'))

# --- The hydraulic robots (EVIDENCE.md E27.7; Matthias, 2026-11-04, "Yes, agree E27.7", "Yes, build it") --------------
# The place of a joint by the first word of its name, for the seven template robots' joints by place.
PLACE_OF_JOINT = {'Hip': 'hips', 'Knee': 'knees', 'Ankle': 'ankles', 'Waist': 'waist', 'Shoulder': 'arms',
                  'Elbow': 'arms', 'Wrist': 'arms', 'Head': 'head', 'Neck': 'head'}


def places_of(count: int) -> dict:
    """A robot's `count` hydraulic joints by place where no source splits them (E27.7 point 9.9): as the seven robots of
    types 3 and 4's template on legs have their body joints by place (SEVEN: hips 42, knees 14, ankles 28, waist 16,
    head 10, arms 90 of 200), each place its share of `count`, rounded down, the joints left to the largest remainders.
    Atlas (old)'s 28: hips 6, knees 2, ankles 4, waist 2, head 1, arms 13."""
    counts: dict = {}
    for b in SEVEN:
        for j in body(b):
            place = PLACE_OF_JOINT[j[0].split()[0]]
            counts[place] = counts.get(place, 0) + j[1]
    total = sum(counts.values())
    exact = {place: count * n / total for place, n in counts.items()}
    out = {place: int(v) for place, v in exact.items()}
    for place in sorted(exact, key=lambda k: exact[k] - out[k], reverse=True)[:count - sum(out.values())]:
        out[place] += 1
    return out


def template_joint(name: str, count: int, group: str, robot_kg: float) -> tuple:
    """`count` electric joints of no stated torque or mass of a robot of `robot_kg` on the template's rows (E27.7 point
    3.3, Nadia's pelvis): each the template's share of the joint modules of its group (AVERAGE_JOINTS, 'Hip joints' or
    'Waist joints', both sizes) over the joints the seven robots have in the group on average, times the template's
    joint modules' share of the robot's mass at its mode (TYPES_34_SHARED, 44.7 %) and the robot's mass: its module
    mass at the mode, half to 1.5 times, the template's own spread (E); a large joint, as the group's large rows hold
    most of it. A module mass, not a share: 01 lets a robot's joints be shares only as the template's whole groups."""
    share = sum(a[7] for a in AVERAGE_JOINTS if a[0].startswith(group + ','))
    place = {'Hip joints': 'hips', 'Waist joints': 'waist'}[group]
    per_robot = sum(j[1] for b in SEVEN for j in body(b) if PLACE_OF_JOINT[j[0].split()[0]] == place) / len(SEVEN)
    modules = next(r[3] for r in TYPES_34_SHARED if r[1] == JOINT_SHARE_34)
    return joint(name, count, None, estimate(round(share / per_robot * modules * robot_kg, 3)),
                 *JOINT_PLACES[name.split()[0]], size='large')


def digital_actuators(place: str, count: int) -> tuple:
    """Neo1's `count` digital hydraulic actuators at one place (PLACES; E27.7 point 5.2): each 1.0 / 1.1 / 1.65 kg, its
    insides its shares in the sheet Shares (point 5.3)."""
    kind, region = PLACES[place]
    return (f'Digital hydraulic actuators, {place}', count, kind, region, (1.0, 1.1, 1.65), None, None, 'S, E',
            'NAT "each actuator weighs about 1 kg" the min, NEW "自重1.1公斤" ("最小的直线驱动单元之一", one of its '
            'smallest) the mode, 1.5 times it the max (E27.4 question 9)')


# Neo1 (208): its 41 joints by place as 上海证券报's reporter counts them (SSB: "双臂14个、双手10个、双腿及脚部12个、腰部3个、
# 头部2个"), its two forearm rotary joints electric, the 39 others digital hydraulic actuators; the hands' 10 with the
# arms (the row "Arm joints and hands"); its legs' 12 as two legs of 6 (E).
NEO1_PLACES = {'arms': 14 - 2 + 10, 'hips': 6, 'knees': 2, 'ankles': 4, 'waist': 3, 'head': 2}
NEODRA_NEO1 = block(
    'NeodraDynamics Neo1', 'NeodraDynamics', 4.0, 1200,
    'NAT (New Atlas, 2026-11-01: "1.2 metric tons", "a cable supplies its power. A battery will come once it moves"), '
    'SSB (上海证券报: its 41 joints), NEW (its founder: "钛合金外壳", "小功率电机", "PLC"); E27',
    makers(1200, 'NAT "a weight of 1.2 metric tons"'),
    [joint('Elbow yaw (forearm rotation)', 2, None, estimate(2.6), 'Elbows and wrists', 'Arms', size='large')],
    joint_sources='SSB "双前臂两处旋关节采用电驱": no torque or mass stated; the heaviest module the files weigh, the '
                  "T800's Q300H-L 2.6 kg, half to 1.5 times (E27.7 point 9.5)",
    battery=False, oil=((1, 2, 3), 'E', 'its 39 actuators and their hoses: no source states it (E27.7 point 5.9)'),
    **with_defaults(4.0, 1200, dict(
        boards=[named_board('PLC', 'NEW "一台廉价的可编程逻辑控制器（PLC）"'), POWER_BOARD], sensors=[],
        parts=[digital_actuators(place, count) for place, count in NEO1_PLACES.items()]
        + [hoses((4, 8, 12), 'two lines to each of its 39 actuators: no source states them (E27.7 point 9.10)')],
        frame=('Frame', 'Steel', 'not stated: steel, its founder\'s "液压件是一堆铁" (E27.4 question 10); the remainder; '
                                 'C45 the grade (E)', 'C45'))))

# Each robot in the file of its first type among 3 and 4 (E11.7 point 1), in the register's order of numbers.
BLOCKS_3 = [NEURA_4NE1_GEN_3, NEURA_4NE1_GEN_35, NEURA_4NE1_GEN_4, AGIBOT_A2_MAX, PNDBOTICS_ADAM_LITE,
            PNDBOTICS_ADAM_SP, HEXAGON_AEON, AGILE_ONE, AIDOL, AEI_ALICE_M1, TEKNTRASH_ALPHA, AI2_ALPHABOT_2, ANIGON,
            APPTRONIK_APOLLO, APPTRONIK_APOLLO_2, BOSTON_DYNAMICS_ATLAS, NEUBILITY_BILLI, BORG_01,
            WANDERCRAFT_CALVIN_40,
            # Batch 2 (E12.5, E12.6): 18 robots, the CYBORG RO1 and the DR02 in two versions.
            ELITE_CENTAUR_G1, DONUT_CINNAMON_1, UBTECH_CRUZR_S2, UBTECH_CRUZR_Y1, CYBORG_RO1_SE, CYBORG_RO1_PRO,
            CYBORG_WO1, SHARPA_D01, RICHTECH_DEX, BOSHIAC_DEXBOT, AGILITY_DIGIT, AGILITY_DIGIT_5, DEEP_DR02,
            DEEP_DR02_PRO, DUATIC_ALPHA, SIASUN_DUCO, ADDVERB_ELIXIS, ADDVERB_ELIXIS_W, GENESIS_ENO, AVIC_FENGXING_001,
            # Batch 3 (E15.7), 56 blocks, with types 5 and 6's entry in their places (E16.6: the Kaleido 9, the Moby
            # and the Phantom MK1), in the register's order; the SkyWalker 2 on legs and on wheels, the Tora DoubleOne
            # P and X; the hydraulic Neo1 since E27.7 (2026-11-04).
            FIGURE_AI_FIGURE_02, HOLIDAY_ROBOTICS_FRIDAY, AGIBOT_G2_MAX, GALBOT_G1, GALBOT_ET1, GALBOT_S1,
            PERSONA_AI_GEN_1, GENERATIVE_BIONICS_GENE_01, GENTO_LUNA, GEEK_PLUS_GINO_1, GAC_GOMATE, GAC_GOMATE_MINI,
            HUMANOID_HMND_01_ALPHA_BIPEDAL, HUASHU_HSR_ER_HR705, XPENG_IRON_2025, JAKA_K1, JAKA_KARGO, ZEROTH_JUPITER,
            KAWASAKI_KALEIDO_9, LG_KAPEX, GALAXEA_KENGO, KINISI_KR1, MOON_DYNAMICS_L1, GLROAD_LABORER_M1,
            MAGICLAB_MAGICBOT_X1, MATRIX_ROBOTICS_MATRIX_1, MENTEE_MENTEEBOT_2024, MENTEE_MENTEEBOT_V3,
            NOBLE_MACHINES_MOBY, O_ID_MODULAR, ZHEJIANG_NAVIGATOR_2, NEODRA_NEO1, GALAXEA_NEXO, SHARPA_NORTH,
            UGO_NOVA, PINK_ROBOTICS_P0, FOUNDATION_PHANTOM_MK1, PSIBOT_PSI_V1, PUDU_D9, XPENG_PX5, X_SQUARE_QUANTA_X2,
            AGIBOT_RAISE_A1, NINERAY_RAYNEX_G3, ROBOSCIENCE_REX_G1, OVERSONIC_ROBEE, ROBOLIGENT_ROBIN,
            ROBO_ROBOTICS_ROBO_T1, ATI_SHERPA_MECHA, EIR_SKYWALKER_2_ON_LEGS, EIR_SKYWALKER_2_ON_WHEELS,
            MUKS_SPACEO_PRO, ROBOTERA_STAR1, WORKFAR_SYNTRO, PAXINI_TORA_DOUBLEONE_P, PAXINI_TORA_DOUBLEONE_X,
            DEXFORCE_W1_PRO, WALDEN_ROBOTICS_WALDEN, UBTECH_WALKER_S2, PL_UNIVERSE_ZEUS_1, PERCEPTYNE_PR_OMNI]
BLOCKS_4 = [ONE_X_NEO, AGIBOT_A2, AGIBOT_A3_ULTRA, ANDROMEDA_ABI, AGIBOT_A3, AGIBOT_X2, AGIBOT_X2_ULTRA, DOBOT_ATOM,
            VBOT_ATOM,
            # Batch 2 (E12.5, E12.6): 8 robots, the CASBOT 02 and the FF Master in two versions.
            CASBOT_02, CASBOT_02_EDU, CASIVISION_CASIVIBOT, LG_CLOID, XYZ_DEUX, NOETIX_DORA, REALBOTIX_F_SERIES,
            FF_FUTURIST, FF_MASTER_EDU, FF_MASTER_ULTRA,
            # Batch 3 (E15.7), 66 blocks, in the register's order: the Futuring 2, the KAI, the Lumen S1, the SA02, the
            # Steve and the Xiao Liu on legs and on wheels; the Pudu D7 2024 and 2026; the U1 Pro male and female.
            PUDU_FLASHBOT_ARM, FUTURING_2_ON_LEGS, FUTURING_2_ON_WHEELS, FOURIER_GR_3, HAIER_HIVA_HAIWA, NOETIX_HOBBS_W1,
            HONOR, HONOR_A1, XPENG_IRON_2024, WEAVE_ISAAC_1, JINGCHU_ELF, KINETIXAI_KAI_ON_LEGS, KINETIXAI_KAI_ON_WHEELS,
            KEENON_XMAN_R1, KNOWIN_X1, LEJU_KUAVO_5_W, LEJU_KUAVO_MY, GLROAD_LABORER_C1, HECBOT_LUMEN_H1,
            HECBOT_LUMEN_S1_ON_LEGS, HECBOT_LUMEN_S1_ON_WHEELS, MAGICLAB_MAGICBOT, MAGICLAB_MAGICBOT_Z1,
            GIGAAI_MAKER_H01, UNIX_MARTIAN, SUNDAY_MEMO, ENCHANTED_TOOLS_MIROKAI, AIMOGA_MORNINE, NOETIX_N2, GENISOM_NE01,
            ONE_X_NEO_BETA, ONE_X_NEO_GAMMA, LUMOS_NIX, SWITCHBOT_ONERO_H1, PRIMEBOT_T1, PL_UNIVERSE_PROWHITE,
            PUDU_D7_2024, PUDU_D7_2026, ROBOT_COM_RNOID, ROBBYANT_R1, ROBOTERA_Q5, ENGINEAI_SA02_ON_LEGS,
            ENGINEAI_SA02_ON_WHEELS, MUKS_SPACEO_M1, STARBOT_NOVA, SULU_BE_STEVE_ON_LEGS, SULU_BE_STEVE_ON_WHEELS,
            SYNTHEVA_SYNTHIA, IHUB_TARA_GEN1, TAU_ROBOTICS_TAU_HUMANOID, UBTECH_U1_PRO_MALE, UBTECH_U1_PRO_FEMALE,
            TUESDAY_LABS_VOXEL, UBTECH_WALKER_C, UBTECH_WALKER_C1, UBTECH_WALKER_S1, YUE_QUAN_X_BOT, BYD_XIAO_DI,
            TENCENT_XIAO_LIU_ON_LEGS, TENCENT_XIAO_LIU_ON_WHEELS, DIGIT_XIAQI, LEJU_XTRON_KUAVO_MY, YUNMU_YMBOT_C,
            YUNMU_YMBOT_H, ZERITH_H1, ZERITH_Z1]

# --- Sources --------------------------------------------------------------------------------------------------------
# Every source of batch 1 read first-hand on 2026-10-30 (E11.1 to E11.4), and those of type 2's file the shared rows
# and the helpers cite (sources(): by the codes the rows name).
OWN_SOURCES = [
    ('1XN', '1X Technologies, NEO page ("5\'6”", "66 lbs", "842 Wh", "1X NEO Cortex (Nvidia Jetson Thor)")',
     'https://www.1x.tech/neo', "Manufacturer's specification"),
    ('N4', 'NEURA Robotics, 4NE1 page (headed "Meet 4NE1 Gen 4": "Weight (kg) 80", "20% lighter than the generation '
           'before")', 'https://neura-robotics.com/products/4ne1/', "Manufacturer's specification"),
    ('N4G3', 'NEURA Robotics, 4NE1 datasheet V7 / 05.06.2026 ("4NE1 Gen 3": "Weight 80 kg", "55 Degrees of Freedom")',
     'https://neurarobotics.px.media/plk/cE/NEURA_Robotics_4NE1_Datasheet_Web.pdf', "Manufacturer's datasheet"),
    ('N4G35', 'NEURA Robotics, 4NE1 Gen 3.5 datasheet V6 / 02.01.2026 ("Weight 80 kg", "Thor T5000")',
     'https://neurarobotics.px.media/plk/Qc/4NE1Gen3.5Datasheet.pdf', "Manufacturer's datasheet"),
    ('AGA2p', 'AgiBot, A2 page ("Weight 69 kg", "Height 169 cm", "Battery 700 wh")', 'https://www.agibot.com/products/A2',
     "Manufacturer's specification"),
    ('AGA2U', 'AgiBot, A2 Ultra and A2 Lite page ("Peak Knee Torque 270N·m", "14.4Ah")',
     'https://www.agibot.com/products/A2_Ultra', "Manufacturer's specification"),
    ('AGX2u', 'AgiBot, agibot_x2_urdf X2_URDF-v1.4.0: X2-Ultra.urdf, X2-EDU.urdf (their joints\' torque limits)',
     'https://github.com/AgibotTech/agibot_x2_urdf', "Manufacturer's model file"),
    ('AGA3u', 'AgiBot, A3-A3U-robot-model: a3_t3d0, a3_t2d5, a3_ultra_t3d0 (their joints\' torque limits)',
     'https://github.com/AgibotTech/A3-A3U-robot-model', "Manufacturer's model file"),
    ('AGA3Up', 'AgiBot, A3 Ultra store page', 'https://store.agibot.com/products/a3u', "Manufacturer's specification"),
    ('AGA3Um', 'AgiBot, A3 Ultra user manual, 2.5 Robot Specifications', 'https://www.agibot.com/filepage/319.html',
     "Manufacturer's documentation"),
    ('AGA3p', 'AgiBot, A3 page ("magnesium alloy, titanium alloy, and TPU flexible materials")',
     'https://www.agibot.com/products/A3', "Manufacturer's specification"),
    ('AGA3m', 'AgiBot, A3 series user manual, 2.5 Robot Specifications', 'https://www.agibot.com/filepage/290.html',
     "Manufacturer's documentation"),
    ('AGX2', 'AgiBot, X2 page (X2 and X2 Ultra)', 'https://www.agibot.com/products/X2', "Manufacturer's specification"),
    ('ABI', 'Andromeda Robotics, Abi page (no hardware figures)', 'https://andromedarobotics.ai/product',
     "Manufacturer's page"),
    ('PNDw', 'PNDbotics wiki, Adam humanoid introduction and its actuators\' pages',
     'https://wiki.pndbotics.com/en/robot/humanoid_robot/', "Manufacturer's documentation"),
    ('PNDu', 'PNDbotics, pnd_models (adam_lite.urdf 58.48 kg, adam_sp.urdf 60.25 kg)',
     'https://github.com/pndbotics/pnd_models', "Manufacturer's model file"),
    ('HEX', 'Hexagon Robotics, AEON product page', 'https://robotics.hexagon.com/product/', "Manufacturer's specification"),
    ('HEXh', 'Hexagon Robotics, AEON perception with NVIDIA Holoscan', 'https://robotics.hexagon.com/aeon-perception-'
                                                                       'capabilities-nvidia-holoscan/',
     "Manufacturer's article"),
    ('AGR1', 'Agile Robots, Agile ONE page', 'https://www.agile-robots.com/en/products/humanoid-robots/agile-one/',
     "Manufacturer's specification"),
    ('AGRh', 'Agile Robots, Agile Hand flyer ("Weight 1.5kg", "Joints 21")', 'https://www.agile-robots.com/media/files/'
                                                                             'New_website/Products/Agile_Hand/AR-AgileHan'
                                                                             'd-Productflyer-SCREEN-en.pdf',
     "Manufacturer's datasheet"),
    ('AID', 'AIDOL, walking version page ("67", "186 см", "95 кг")', 'https://aidoltech.ru/walking',
     "Manufacturer's specification"),
    ('AEIM1', 'AeiROBOT, ALICE M1 page ("130 - 180cm / 97kg", "DoF 31")', 'https://eng.arobot4all.com/2069803258',
     "Manufacturer's specification"),
    ('AI2', 'AI² Robotics, AlphaBot 2 hardware architecture', 'https://docs.ai2robotics.com/en/alphabot2/hardware/'
                                                              'architecture', "Manufacturer's documentation"),
    ('ANI', 'Anigon, robot platform (reference specification)', 'https://anigon.ch/robot-platform/',
     "Manufacturer's specification"),
    ('ANIt', 'Anigon, technical overview ("ANIGON FA-L Series", "28 DoF")',
     'https://anigon.ch/documents/anigon-technical-overview.txt', "Manufacturer's documentation"),
    ('APT', 'Apptronik, home page (its Apollo page answered 404)', 'https://apptronik.com/', "Manufacturer's page"),
    ('APT2', 'Apptronik, Apollo 2 page', 'https://apptronik.com/apollo/apollo-2', "Manufacturer's page"),
    ('BDA', 'Boston Dynamics, Atlas page', 'https://bostondynamics.com/atlas', "Manufacturer's specification"),
    ('BDAs', 'Boston Dynamics, Atlas spec sheet, Rev: 10/15/2026', 'https://bostondynamics.com/wp-content/uploads/2026/01/'
                                                                   'atlas-spec-sheet.pdf', "Manufacturer's datasheet"),
    ('DOBa', 'DOBOT, Atom page ("28 upper-body degrees of freedom")',
     'https://www.dobot-robots.com/products/humanoid-robots/atom.html', "Manufacturer's specification"),
    ('XHA', 'Xinhua, on the Vbot ATOM at WRC, 2026-08-22', 'https://www.xinhuanet.com/auto/20260822/'
                                                           '552eab20bbfb45aab48880b1878f7938/c.html',
     'Second-hand: a press report at its launch'),
    ('VBOT', 'Vbot, its site (a robot dog only)', 'https://www.vbot.cn/', "Manufacturer's page"),
    ('NEU', 'NEUBILITY, its site ("Hybrid humanoid combining mobility and manipulation")', 'https://www.neubility.ai/en',
     "Manufacturer's page"),
    ('BORG', 'Borg Robotics, its site ("IN DEVELOPMENT")', 'https://www.borgrobotic.com/', "Manufacturer's page"),
    ('WAN', 'Wandercraft, Calvin-40 page (no figures)', 'https://en.wandercraft.eu/calvin-40', "Manufacturer's page"),
    # Batch 2, read first-hand on 2026-11-01 (E12.1, E12.3, E12.4).
    ('CAS2', 'CASBOT, CASBOT 02 product page (its parameter table)', 'https://casbot.tech/product/02',
     "Manufacturer's specification"),
    ('CSV', 'CasiVision, its site (inspection machines, no humanoid)', 'https://en.zhongkehuiyuan.com/',
     "Manufacturer's page"),
    ('QBA', 'QbitAI, on the launch of CASIVIBOT, 2025-08-20', 'https://www.qbitai.com/2025/08/324159.html',
     'Second-hand: a press report at its launch'),
    ('ELC', 'Elite Robots, Centaur-G1 page', 'https://www.elibot.com/product/wheeled', "Manufacturer's specification"),
    ('ELCr', 'Elite Robots, Centaur-G1 press release, 2026-05-25',
     'https://www.elibot.com/about/news/centaur-g1-wheeled-humanoid-robot', "Manufacturer's press release"),
    ('OBC', 'Origin of Bots, Centaur G1 ("WEIGHT 85 kg"; values "compiled from public sources")',
     'https://www.originofbots.com/robot/centaur-g1-by-elite-robots-details-specifications-rating',
     'Second-hand: a database'),
    ('DNT', 'Donut Robotics, products page ("Height approx. 170cm・Weight approx. 70kg")',
     'https://www.donutrobotics.com/en/blank-2', "Manufacturer's page"),
    ('LGC', 'LG Electronics, press release on CLOiD, 2025-12-31',
     'https://www.lg.com/us/press-release/lg-to-unveil-home-robot-at-ces-2026-sharing-vision-for-the-zero-labor-home',
     "Manufacturer's press release"),
    ('ENGc', 'Engadget, LG CLOiD at CES 2026, 2026-01-04', 'https://www.engadget.com/home/smart-home/lg-reveals-its-'
                                                           'laundry-folding-robot-at-ces-2026-215121021.html',
     'Second-hand: a press report'),
    ('UBS2', 'UBTECH, Cruzr S2 page and its specification picture', 'https://www.ubtrobot.com/en/humanoid/products/'
                                                                    'cruzr-s2/', "Manufacturer's specification"),
    ('UBY1', 'UBTECH, Cruzr Y1 page and its specification picture', 'https://www.ubtrobot.com/en/humanoid/products/'
                                                                    'cruzr-y1', "Manufacturer's specification"),
    ('CYBr', 'Cyborg Robotics, full-size biped page (CYBORG-R01: its technical parameters)',
     'https://www.cyb-org.cn/index.php?id=6', "Manufacturer's specification"),
    ('CYBw', 'Cyborg Robotics, wheeled humanoid page (CYBORG-W01: its technical parameters)',
     'https://www.cyb-org.cn/index.php?id=4', "Manufacturer's specification"),
    ('CYBh', 'Cyborg Robotics, dexterous hand page ("重量 750g")', 'https://www.cyb-org.cn/index.php?id=5',
     "Manufacturer's specification"),
    ('SHD', 'Sharpa, D01 page and its specification sheet', 'https://www.sharpa.com/pages/d01',
     "Manufacturer's specification"),
    ('XYZ', 'XYZ, DEUX page and its robot spec', 'https://xyzcorp.imweb.me/DEUX', "Manufacturer's specification"),
    ('RCH', 'Richtech Robotics, Dex page and its technical specifications',
     'https://www.richtechrobotics.com/solutions/dex', "Manufacturer's specification"),
    ('RCHp', 'Richtech Robotics, press release on Dex, 2025-10-28',
     'https://richtechrobotics.com/resources/dex-at-gtc-dc', "Manufacturer's press release"),
    ('AIW', 'The AI Wiki, DexBot ("a height of 175 cm, a weight of 58 kg, and 28 active joints")',
     'https://aiwiki.ai/wiki/boshiac_dexbot', 'Second-hand: a wiki'),
    ('ENGd', 'Engadget, the next Digit, 2023-03-20 ("5\'9\"", "around 140 lbs")',
     'https://www.engadget.com/the-next-gen-digits-robot-gets-a-head-and-hands-120001329.html',
     'Second-hand: a press report at its launch'),
    ('AGL', 'Agility Robotics, its site (no figures of the Digit)', 'https://www.agilityrobotics.com/',
     "Manufacturer's page"),
    ('AGL5', 'Agility Robotics, Digit 5 page', 'https://www.agilityrobotics.com/solutions/digit-5',
     "Manufacturer's specification"),
    ('AGLh', "Agility Robotics, its CTO's answers on Digit 5, 2026-10-23", 'https://www.agilityrobotics.com/content/'
                                                                          'jonathan-hurst-answers-your-questions-about-'
                                                                          'building-digit-5', "Manufacturer's article"),
    ('NOE', 'Noetix Robotics, its site (no Dora)', 'http://www.noetixrobotics.com/', "Manufacturer's page"),
    ('DPR', 'DEEP Robotics, DR02 page', 'https://www.deeprobotics.cn/products/detail/5.html',
     "Manufacturer's specification"),
    ('DPRs', 'DEEP Robotics, DR02 product sheet (产品手册)', 'https://www.deeprobotics.cn/bocupload/2026/09/21/'
                                                         '17899830514556fs00t.pdf', "Manufacturer's datasheet"),
    ('DUA', 'Duatic, DXTR page (titled "Alpha Half-Humanoid Robot")', 'https://www.duatic.com/dxtr',
     "Manufacturer's specification"),
    ('DUAa', 'Duatic, DynaArm page ("Total Weight 9.2 kg")', 'https://www.duatic.com/dynaarm',
     "Manufacturer's specification"),
    ('OBA', 'Origin of Bots, Duatic Alpha, 2026-01-26 ("around 90kg total")', 'https://www.originofbots.com/news/'
                                                                              'duatic-unveils-alpha-half-humanoid-'
                                                                              'powerhouse', 'Second-hand: a database'),
    ('DUC', "Siasun's DUCO, humanoid robot series", 'https://www.ducorobots.cn/prodetail/48.html',
     "Manufacturer's specification"),
    ('ADV', 'Addverb, Elixis page and its tabs ELIXIS and ELIXIS-W', 'https://addverb.ai/humanoid-robot-elixis',
     "Manufacturer's specification"),
    ('GEN', 'Genesis AI, its site (a waitlist)', 'https://www.genesis.ai/', "Manufacturer's page"),
    ('TNW', 'The Next Web, Genesis AI and Eno, 2026-06-16',
     'https://thenextweb.com/news/genesis-ai-thinks-the-humanoid-hype-is-wrong-'
     'its-wheeled-robot-is-the-counterargument',
     'Second-hand: a press report at its launch'),
    ('HGF', 'humanoid.guide, on the F-Series, 2026-09-30', 'https://humanoid.guide/welcome-f-series/',
     'Second-hand: a catalogue'),
    ('RBX', 'Realbotix, Echo page (no F-Series named)', 'https://realbotix.com/echo', "Manufacturer's page"),
    ('GTF', 'Global Times, robots at WRC 2026, 2026-08-20 (the Fengxing-001 at AVIC\'s stand)',
     'https://www.globaltimes.cn/page/202608/1368652.shtml', 'Second-hand: a press report'),
    ('AVC', 'AVIC, its site (no page names the Fengxing-001)', 'https://www.avic.com/', "Manufacturer's page"),
    ('FFF', 'Faraday Future, FF Futurist page and its table', 'https://robotics.ff.com/us/ff-futurist/',
     "Manufacturer's specification"),
    ('FFM', 'Faraday Future, FF Master page and its specs', 'https://robotics.ff.com/us/ff-master/',
     "Manufacturer's specification"),
    # Types 5 and 6's entry (E16.6), read first-hand on 2026-11-01 (V134, V135).
    ('BDh', 'Boston Dynamics, robot hands for modern AI and real work ("13 degrees of freedom (DOF), directly actuated")',
     'https://bostondynamics.com/blog/robot-hands-for-modern-ai-and-real-work/', "Manufacturer's article"),
    ('BDn', 'Boston Dynamics, collaboration with NVIDIA ("NVIDIA Jetson Thor computing platform")',
     'https://bostondynamics.com/news/boston-dynamics-expands-collaboration-with-nvidia/', "Manufacturer's press release"),
    ('BTN', 'Battery-Tech Network, LG Energy Solution and Atlas, 2026-02-12 ("46-series ternary cells")',
     'https://battery-tech.net/battery-markets-news/lg-energy-solutions-batteries-power-atlas-humanoid-robot/',
     'Second-hand: a trade report citing industry sources'),
    ('DPRu', 'DEEP Robotics, deep_robotics_model: DR02-std.urdf (67.575 kg), DR02-pro.urdf (78.085 kg)',
     'https://github.com/DeepRoboticsLab/deep_robotics_model', "Manufacturer's model file"),
    ('MYN', 'Mynavi TECH+, Kawasaki Kaleido 9, 2025-12-05 ("身長は190cm", "体重は99kg")',
     'https://news.mynavi.jp/techplus/article/20251205-3764371/', 'Second-hand: a press report at its showing'),
    ('KAWb', 'Kawasaki Robotics, blog on Kaleido 9, 2026-03 ("maintaining torque", LiDAR, the Kaleido Station)',
     'https://kawasakirobotics.com/in/blog/20260316_kaleido9/', "Manufacturer's article"),
    ('KAWj', 'Kawasaki Robotics, Japanese blog on the Kaleido (its 2019 one: "マグネシウム合金")',
     'https://kawasakirobotics.com/jp/blog/202511_kaleido/', "Manufacturer's article"),
    ('NMb', "Noble Machines (Under Control Robotics), blog, 2025-03-18 (\"Moby's 72 Kg body\")",
     'https://undercontrolrobotics.substack.com/p/real-world-world-building-ucr-develops', "Manufacturer's article"),
    ('NMp', 'Noble Machines, its page ("Payload 23KG/50LB", "Battery life 5 hours")', 'https://www.noblemachines.ai/',
     "Manufacturer's specification"),
    ('NVm', 'NVIDIA, case study on Noble Machines ("NVIDIA Jetson Thor")',
     'https://www.nvidia.com/en-us/case-studies/noble-machines/', 'Second-hand: a supplier\'s case study'),
    ('ORBm', 'Orbbec, case study on Moby ("Orbbec Gemini 336L stereo 3D cameras")', 'https://www.orbbec.com/?p=45035',
     "Second-hand: a supplier's case study"),
    ('MKm', 'Mike Kalil, on Moby ("Standing 170 cm", "a reported 34 degrees of freedom")',
     'https://mikekalil.com/blog/noble-machines-moby/', 'Second-hand: a blog'),
    ('FDp', 'Foundation, Phantom page', 'https://www.foundation.bot/phantom', "Manufacturer's specification"),
    ('TBS', 'The Business Standard (UNB, after the BBC), 2026-06-09 ("Phantom MK-1 … lacks a battery")',
     'https://www.tbsnews.net/node/1457841', 'Second-hand: a press report'),
    # Batch 3 (E15.7): every source its blocks cite, read first-hand on 2026-11-01 and 2026-11-02 (V134; the records in
    # documentation/claude/research_2026-11-01/), but where a row says it was not reread.
    ('FIGr', 'New Atlas on the Figure 02\'s launch ("six RGB cameras", "16 degrees of freedom", "a new 2.25-kWh")',
     'https://newatlas.com/robotics/figure-02-humanoid-robot-launch', 'Second-hand: a press report'),
    ('PUDf', 'Pudu Robotics, FlashBot Arm page', 'https://pudurobotics.com/products/flashbot-arm',
     "Manufacturer's specification"),
    ('HDF', 'Humanoids Daily on Holiday Robotics\' Friday ("176cm tall, weighing 115kg", "500g" a hand)',
     'https://www.humanoidsdaily.com/news/holiday-robotics-unveils-friday-a-wheeled-humanoid-that-prioritizes-hands-'
     'over-legs', 'Second-hand: a press report of the maker\'s figures'),
    ('AGG2s', 'AgiBot, G2 specification sheet as a seller carries it ("Weight 185kg", the base G2\'s; read by the '
              'research agent, not reread)', 'https://cdn.robotshop.com/media/A/Agb/RB-Agb-09/pdf/AgiBot-G2-'
                                              'Specification.pdf', "Manufacturer's specification, via a seller"),
    ('GALg1', 'Galbot, G1 page ("92.5 kg", "48 V 30 Ah", "NVIDIA AGX Orin 64GB")', 'https://www.galbot.com/g1/',
     "Manufacturer's specification"),
    ('GALet1', 'Galbot, ET1 page ("带电池重量 32 kg", "RK3588 + RDK X5")', 'https://www.galbot.com/et1/',
     "Manufacturer's specification"),
    ('GALs1', 'Galbot, S1 page ("整机重量 320 kg", "48 V 30 Ah × 2")', 'https://www.galbot.com/s1/',
     "Manufacturer's specification"),
    ('PRSn', 'Persona AI, its humanoid page (no figures)', 'https://persona.ai/humanoid/', "Manufacturer's page"),
    ('OBP', 'Origin of Bots, Persona humanoid ("WEIGHT 85 kg")',
     'https://www.originofbots.com/robot/persona-humanoid-by-persona-ai-details-specifications-rating',
     'Second-hand: a database'),
    ('GBm', 'Generative Bionics, gb-robot-models gene01_0/model.urdf (its links 79.668 kg, added by script)',
     'https://raw.githubusercontent.com/gbionics/gb-robot-models/main/share/gb_robot_models/robots/gene01_0/model.urdf',
     "Manufacturer's model file"),
    ('GENl', 'Gento Robotics, Gento Luna page ("48 V 34.4 Ah LiFePO battery pack")',
     'https://www.gentorobotics.ai/products/gento-luna/', "Manufacturer's specification"),
    ('CLSg', '财联社 on Geek+\'s Gino 1, 2026-02-10 ("双臂14个自由度", "50Ah", "Nvidia Thor")',
     'https://www.cls.cn/detail/2285549', 'Second-hand: a press report'),
    ('HSG', 'heise on GAC\'s GoMate ("174 cm", "38 degrees of freedom", "hands with five movable fingers")',
     'https://www.heise.de/en/news/Humanoid-robot-GoMate-to-work-in-Chinese-automotive-company-10224291.html',
     'Second-hand: a press report'),
    ('FFgr3', 'Fourier, GR-3 introduction ("Net Weight ≈71 kg", its joint table, "702Wh + 234Wh", "46.8V")',
     'https://support-old.fftai.com/en/docs/GR-X-Humanoid-Robot/GR3/GR-3_Introduction/', "Manufacturer's documentation"),
    ('FFgr3u', 'Fourier, Wiki-GRx-Models gr3v2_1_1.urdf (its joints\' effort limits)',
     'https://raw.githubusercontent.com/FFTAI/Wiki-GRx-Models/master/GRX/GR3/gr3v2_1_1/basic_urdf/gr3v2_1_1.urdf',
     "Manufacturer's model file"),
    ('HMNp', 'Humanoid, HMND 01 Alpha Bipedal page ("WEIGHT 90 kg", "DEGREES OF FREEDOM 29")',
     'https://thehumanoid.ai/hmnd-01-alpha-bipedal/', "Manufacturer's specification"),
    ('HMNr', 'Humanoid, release of 2025-12-02 ("six RGB cameras", "Nvidia Jetson Orin AGX and Intel i9")',
     'https://thehumanoid.ai/humanoid-unveils-record-breaking-bipedal-robot-walking-48-hours-after-assembly/',
     "Manufacturer's release"),
    ('NTXh', 'Noetix, Hobbs W1 page ("Wheeled Full-Body Form", "54 Active DoF")',
     'https://www.noetixrobotics.com/en/mobile/detail/W1', "Manufacturer's page"),
    ('AIWh', 'AI Wiki, Noetix Hobbs W1 ("75 kg", "32 Ah (21V to 29.4V)"; citing Noetix\'s page)',
     'https://aiwiki.ai/wiki/noetix_hobbs_w1', 'Second-hand: a wiki'),
    ('HONr', 'HONOR, its robots\' page (HONOR Robotics D1 and A1, no figures)',
     'https://www.honor.com/global/events/honor-robot/', "Manufacturer's page"),
    ('HSRp', 'Huashu Robotics, HSR-ER-HR705 page ("机器人重量 200kg")', 'https://www.hsrobotics.cn/products_xq/119.html',
     "Manufacturer's specification"),
    ('QVI', 'Qviro on XPENG\'s IRON ("Each hand features 15 degrees of freedom")',
     'https://qviro.com/blog/xpeng-launches-iron-advanced-humanoid-robot/', 'Second-hand: a blog'),
    ('K36i', '36Kr on XPENG\'s new IRON ("体重达到 70kg", "三颗图灵 AI 芯片")', 'https://eu.36kr.com/zh/p/3541045140353153',
     'Second-hand: a press report'),
    ('WVi', 'Weave Robotics, Isaac 1 page (its degrees of freedom, "collapsible torso")',
     'https://weaverobotics.com/isaac-1', "Manufacturer's specification"),
    ('OBI', 'Origin of Bots, Isaac 1 ("WEIGHT 45 kg")',
     'https://www.originofbots.com/robot/isssac-1-by-weave-robotics-details-specifications-rating',
     'Second-hand: a database'),
    ('JNGe', 'Hubei Jingchu, Jingchu Elf page ("体重约70kg", "体重：80kg")', 'https://www.jingchurobot.cn/product_detail/3.html',
     "Manufacturer's specification"),
    ('IFAz', 'IFA Berlin, Zeroth\'s exhibitor listing (Jupiter "Weight: 58 kg")',
     'https://www.ifa-berlin.com/exhibitors/zeroth', "Second-hand: a trade fair's listing"),
    ('IEK', 'Interesting Engineering on KinetixAI\'s KAI ("70 kilograms", "1.7-kilowatt-hour")',
     'https://interestingengineering.com/ai-robotics/chinas-humanoid-robot-with-115-degrees-of-freedom',
     'Second-hand: a press report'),
    ('KXh', 'KinetixAI, KaiHand page ("750 g", "20 active")', 'https://kinetixai.tech/en/kaihand',
     "Manufacturer's specification"),
    ('HKK', 'Hankyung on LG\'s KAPEX, 2025-11-13 ("키 170㎝, 체중 60㎏대")', 'https://www.hankyung.com/article/2025111324581',
     'Second-hand: a press report'),
    ('OBK', 'Origin of Bots on Galaxea\'s Kengo ("40 kg weight")',
     'https://www.originofbots.com/news/galaxea-dynamics-kengo-brings-bipedal-humanoid-teleoperation-into-sharper-focus',
     'Second-hand: a news site'),
    ('ITHk', 'IT之家 on Galaxea\'s Kengo, 2026-06-02 ("单关节扭矩超 130N·m")', 'https://www.ithome.com/0/958/651.htm',
     'Second-hand: a press report'),
    ('KNS', 'Bear Robotics, Kinisi page ("Wheeled humanoid mobile manipulator")', 'https://www.bearrobotics.ai/kinisi',
     "Manufacturer's page"),
    ('IEKR', 'Interesting Engineering on the Kinisi KR1 ("an onboard NVIDIA Jetson module")',
     'https://interestingengineering.com/innovation/humanoid-robot-kr1-kinisi', 'Second-hand: a press report'),
    ('KNWx', 'Knowin, its product page ("Total Degrees of Freedom 23 DoF")', 'https://knowinai.com/en/product.html',
     "Manufacturer's specification"),
    ('GLc1', 'Glroad, Laborer C1 page ("重量 38KG", "最大峰值扭矩 150N.M")',
     'https://www.glroad.com/ListIntroduction/info.aspx?itemid=549', "Manufacturer's specification"),
    ('GLm1', 'Glroad, Laborer M1 page ("重量 86KG", "最大峰值扭矩 430N.M")',
     'https://www.glroad.com/ListIntroduction/info.aspx?itemid=548', "Manufacturer's specification"),
    ('HECh', 'HECbot, Lumen H1 page ("净重≈69kg", "峰值扭矩512Nm", "700 Wh")', 'https://www.hecbot.cn/product.html?type=22',
     "Manufacturer's specification"),
    ('MLg1', 'MagicLab, MagicBot Gen1 page ("Approcimately 70kg", "≥ 350 N·m", "25 Ah (1.35 kWh)")',
     'https://www.magiclab.top/en/human', "Manufacturer's specification"),
    ('MLx1', 'MagicLab, MagicBot X1 page ("Total Weight 70kg", "≥350N·m")', 'https://www.magiclab.top/en/x1',
     "Manufacturer's specification"),
    ('MLz1', 'MagicLab, MagicBot Z1 page ("Approximately 40kg", "Maximum Knee Torque* 100N.m")',
     'https://www.magiclab.top/en/z1', "Manufacturer's specification"),
    ('UNXm', 'UniX AI, Martian page ("40 kg Weight", "150 N.m Motor Max Torque", "9 Ah", "48 V")',
     'https://unix-group.ai/martian/', "Manufacturer's specification"),
    ('MTXr', 'Matrix Robotics, Matrix-1 page ("67 kg", "2.28 KWh")', 'https://matrixrobotics.ai/matrix-1',
     "Manufacturer's specification"),
    ('SUNm', 'Sunday Robotics, technology page (MEMO: "170 pounds", its degrees of freedom)',
     'https://www.sunday.ai/technology', "Manufacturer's specification"),
    ('MNTb', 'Mentee Robotics, its bot page ("175cm", "70kg", "40"; the V3\'s)', 'https://www.menteebot.com/bot/',
     "Manufacturer's specification"),
    ('TRMB', 'Trend Hunter on the MenteeBot V3, 2025-02-25 ("powered by two Jetson Orin AGX computing units")',
     'https://www.trendhunter.com/trends/menteebot-v30', 'Second-hand: a blog'),
    ('RGM', 'Robots Guide (IEEE), Mirokaï ("WEIGHT 29 kg", its cameras, "2 NVIDIA Jetson NX")',
     'https://robotsguide.com/robots/mirokai', 'Second-hand: a database'),
    ('OBM', 'Origin of Bots, Mirokaï ("WEIGHT 26 kg")',
     'https://www.originofbots.com/robot/miroka-by-enchanted-tools-details-specifications-rating',
     'Second-hand: a database'),
    ('OIDm', 'O-ID, its page (Modular: "172 cm", "70 kg", "30 DoF")', 'https://o-id.net/',
     "Manufacturer's specification"),
    ('ITHm', 'IT之家 on AiMOGA\'s Mornine, 2025-03-19 ("167cm、65kg", "0.7kwh")', 'https://www.ithome.com/0/838/943.htm',
     'Second-hand: a press report'),
    ('CNCm', 'CarNewsChina on the Mornine, 2026-04-13 ("weighs 70kg", "0.7 kWh battery")',
     'https://carnewschina.com/2026/04/13/chery-begins-online-sales-of-humanoid-robot-with-a-0-7-kwh-battery-at-41400-usd/',
     'Second-hand: a press report'),
    ('RBTXn', 'RBTX, Noetix N2 ("weighing 30 kg", "peak torque of 150 Nm")',
     'https://rbtx.de/en-GB/components/humanoid/noetix-robotics-n2', "Second-hand: a seller's listing"),
    ('AIWn', 'AI Wiki, Zhejiang Navigator 2 ("60 kg", "Single hand weight | 600 g")',
     'https://aiwiki.ai/wiki/zhejiang_humanoid_navigator_2', 'Second-hand: a wiki'),
    ('GNSn', 'GENISOM, NE01 page (no figures)', 'https://www.genisomai.com/en/product-robot/ne01', "Manufacturer's page"),
    ('1XNg', '1X Technologies, "Introducing NEO Gamma" ("four microphones", "a three-speaker system")',
     'https://www.1x.tech/discover/introducing-neo-gamma', "Manufacturer's article"),
    ('GXNx', 'Galaxea AI, release on NEXO ("30 degrees of freedom")', 'https://kyodonewsprwire.jp/release/202608244591',
     "Manufacturer's release"),
    ('OBN', 'Origin of Bots, NEXO ("WEIGHT 78 kg")',
     'https://www.originofbots.com/robot/nexo-by-galaxea-dynamics-details-specifications-rating',
     'Second-hand: a database'),
    ('LMSn', 'Lumos Robotics, NIX page ("25.41 kg (total, incl. battery)", "282 Wh", "RK3588")',
     'https://lumosbot.tech/products/luxiaoming', "Manufacturer's specification"),
    ('NIXd', 'Lumos Robotics, its models page ("Nix1 ... Weight: 18 kg")',
     'https://lumosrobot.github.io/lumosrobotics.github.io/contents/models.html', "Manufacturer's page"),
    ('RCN', 'Robotics Center, Sharpa North ("60 kg Net weight")',
     'https://www.roboticscenter.ai/store/product/sharpa-sharpa-north', "Second-hand: a seller's listing"),
    ('UGOn', 'ugo, ugo Nova page ("約 100 kg", "LiFePO4 | 50.6V | 22Ah")', 'https://ugo.plus/ai/ugo-nova/',
     "Manufacturer's specification"),
    ('HPO', 'humanoid.press, Onero H1 ("Weight: 68 kg", "prototype spec")',
     'https://humanoid.press/database/humanoid-press-database-onero-h1/', 'Second-hand: a database'),
    ('PNKp', 'Pink Robotics, its page (P0: "82kg", "32 DoF")', 'https://www.pink-robotics.com/',
     "Manufacturer's specification"),
    ('PLpw', 'PL-Universe, ProWhite page ("Weight 400 kg", "40 v 100 Ah")',
     'https://en.pl-universe.com/Products/ProWhiteRobot', "Manufacturer's specification"),
    ('PSIv', 'PsiBot, Psi V1 page ("RGBD*4", "Computing Platform：Thor")',
     'https://www.psibot.ai/en/products/product_psibot-v1/', "Manufacturer's specification"),
    ('PD7r', 'Pudu Robotics, release of 2024-09-19 on its D7 ("weighs 45 kilograms", "a battery exceeding 1 kWh")',
     'https://www.aap.com.au/aapreleases/cision20240919ae10581/', "Manufacturer's release"),
    ('PUDd7', 'Pudu Robotics, D7 page (the 2026 one: "308.6 lbs（140 kg）")', 'https://www.pudurobotics.com/products/d7',
     "Manufacturer's specification"),
    ('PUDd9', 'Pudu Robotics, D9 page ("65 kg", "Maximum Joint Torque 352 N·m", "15 Ah (0.72 kWh)")',
     'https://www.pudurobotics.com/products/d9', "Manufacturer's specification"),
    ('X2Rq', 'X Square Robot, QUANTA X2 page (its degrees of freedom and sensors)',
     'https://x2robot.com/en/product/quantum2', "Manufacturer's specification"),
    ('AGA1', 'AgiBot, RAISE A1 page ("Weight 55 kg", "Peak Torque 350N·m")', 'https://www.agibot.com/products/A1',
     "Manufacturer's specification"),
    ('NRY', 'NineRay, humanoid page (RayNex G3: "60 kg", "32 DoF (Body)")', 'https://www.nineraygroup.com/en/humanoid.html',
     "Manufacturer's specification"),
    ('RSCx', 'RoboScience, REX G1 page ("22个自由度", "2070 TFLOPS")', 'https://www.robosci.com/rex-g1/',
     "Manufacturer's specification"),
    ('RNDs', 'Robot.com, RNoid specification sheet, revision 003, 2026-05-14 ("90 kg Total weight")',
     'https://lp.robot.com/rnoid/specs.pdf', "Manufacturer's datasheet"),
    ('OVRr', 'Oversonic Robotics, RoBee Series R brochure 10/2026, Oversonic_Robee-R-2026-eng.pdf ("Up to 293 kg")',
     'https://oversonicrobotics.com/download/', "Manufacturer's brochure"),
    ('RBLr', 'Roboligent, Robin page ("105 kg Total weight")', 'https://www.roboligent.com/robin/',
     "Manufacturer's specification"),
    ('RBOi', 'Robo, its page (ROBO-T1: "two 6-DOF robot arms with grippers")', 'https://robo.inc/',
     "Manufacturer's page"),
    ('OBR', 'Origin of Bots, ROBO-T1 ("WEIGHT Approx. 45–60 kg")',
     'https://www.originofbots.com/robot/robo-t1-robo-robotics', 'Second-hand: a database'),
    ('RTq5', 'ROBOTERA, Q5 brochure (Weight "70 Kg", its degrees of freedom; its digits read by OCR)',
     'https://a.storyblok.com/f/298593/x/5695abe67b/q5-brochure-en-robotera.pdf', "Manufacturer's brochure"),
    ('TNS', 'TechNode on EngineAI\'s SA02, 2025-08-11 ("1.25-meter-tall, 25-kilogram")',
     'https://technode.com/2025/08/11/engineai-to-launch-sa02-a-5500-humanoid-robot-aimed-at-young-people/',
     'Second-hand: a press report'),
    ('ATIs', 'Ati Motors, Sherpa Mecha page ("Dual arms with 19 degrees of freedom", "55 Ah × 2")',
     'https://www.atirobotics.ai/products/humanoid/sherpa-mecha/', "Manufacturer's specification"),
    ('MUKm1', 'Muks Robotics, Spaceo M1 page ("~45 kg", "About 160 kg cm", "25.6V, 45Ah LiFePO4")',
     'https://muksrobotics.com/spaceo-m1', "Manufacturer's specification"),
    ('MUKpr', 'Muks Robotics, Spaceo Pro page ("60 kg", arm "66 Nm", waist "90 Nm", "25.6V, 45Ah LiFePO4")',
     'https://muksrobotics.com/spaceo-pro', "Manufacturer's specification"),
    ('RTXm', 'ROBOTERA, models: star1/urdf/l3_with_hand_fixedpin_xml.urdf (its joints\' effort limits)',
     'https://github.com/roboterax/models', "Manufacturer's model file"),
    ('STBn', 'StarBot, its page (Nova: "70 lb", "two 7-DOF arms")', 'https://www.starbotusa.com/',
     "Manufacturer's specification"),
    ('GEs', 'GE Reports, "The Robot Soul", 2015-01-26 ("Steve, who weighs 100 kilograms")',
     'https://www.ge.com/news/reports/the-robot-soul', 'Second-hand: a press report'),
    ('SYNt', 'Syntheva, Synthia page ("9.8 - 12.0 kg", "BCM2712 CPU (base model)")',
     'https://robotics.syntheva.no/products/synthia', "Manufacturer's specification"),
    ('WKFs', 'WorkFar, Syntro page ("240 lbs (108kg)", "Swappable Batteries 1.2 kWh")',
     'https://www.workfar.com/product/syntro', "Manufacturer's specification"),
    ('HGT', 'humanoid.guide on Tau Robotics (MarketWatch: "modified Unitree G1 robots", "pincer hands")',
     'https://humanoid.guide/tau-robotics-humanoids-clean-homes-for-30-an-hour-with-help/', 'Second-hand: a news site'),
    ('TAUh', 'Tau Robotics, its page (no figures)', 'https://www.tau-robotics.com/', "Manufacturer's page"),
    ('PXNt', 'PaXini, Tora DoubleOne parameter image ("*Data from Paxini AI Lab"; read by OCR)',
     'https://paxini.com/images/en/tora-double-parameter.png', "Manufacturer's specification"),
    ('RBTXx', 'RBTX, PaXini Tora DoubleOne Model X ("Weight 73 kg")',
     'https://rbtx.de/en-GB/components/humanoid/paxini-tora-double-one-model-x-humanoid-robot-56-dof',
     "Second-hand: a seller's listing"),
    ('AIWu', 'AI Wiki, UWorld U1 Pro ("weighs 42 kg", "weighs 35.2 kg")', 'https://aiwiki.ai/wiki/uworld_u1_pro',
     'Second-hand: a wiki'),
    ('TSDv', 'Tuesday Labs, its robot page (Voxel)', 'https://tuesdaylabs.com/robot', "Manufacturer's page"),
    ('DXFw1', 'DexForce, W1 Pro page (Weight "110kg", "Dual-PC Architecture")', 'https://en.dexforce.com/w1pro.html',
     "Manufacturer's specification"),
    ('UBwc', 'UBTECH, Walker C page ("43kg", "48V 15Ah")', 'https://www.ubtrobot.com/en/humanoid/products/WalkerC',
     "Manufacturer's specification"),
    ('UBwc1', 'UBTECH, Walker C1 page and its images ("Weight 55kg", "NVIDIA® Jetson Thor™")',
     'https://www.ubtrobot.com/en/humanoid/products/walker-c1', "Manufacturer's specification"),
    ('UBws1', 'UBTECH, Walker S1 page and its images ("Weight 76kg", "Peak Torques 250N.m")',
     'https://www.ubtrobot.com/en/humanoid/products/walker-s1', "Manufacturer's specification"),
    ('UBws2', 'UBTECH, Walker S2 page and its images ("Weight 70kg", "52 of DOF")',
     'https://www.ubtrobot.com/en/humanoid/products/walker-s2', "Manufacturer's specification"),
    ('BDNw', 'Battery Design, "Robot battery swap", 2025-12-09 (the Walker S2: "Total energy = 2.3 kWh Nominal voltage '
             '= 48 V")', 'https://www.batterydesign.net/robot-battery-swap/', 'Second-hand: a technical blog'),
    ('HPX', 'humanoid.press, Xiao Liu ("Bipedal", "Weight: ~55–60 kg")', 'https://humanoid.press/database/database-xiao-liu/',
     'Second-hand: a database'),
    ('DGTx', 'Digit, XiaQi page and its image ("≤ 69kg", "700woh"; read by OCR)',
     'https://www.digit.com.cn/ProductsDetail/93.html', "Manufacturer's specification"),
    ('ZRTh', 'Zerith, H1 page ("轮臂人形机器人", "23总 自由度")', 'https://www.zerith.com/product/ZerithH1/',
     "Manufacturer's specification"),
    ('RBTXz', 'RBTX, Zerith Z1 ("up to 150 Nm peak joint torque", "Weight 33 kg")',
     'https://rbtx.de/en-GB/components/humanoid/zerith-z1-humanoid-robot-21-dof', "Second-hand: a seller's listing"),
    ('CHZ', '中华网 on PL-Universe\'s 大白, 2025-08-08 ("300Kg的整机重量", "48V、40Ah电池")',
     'https://m.tech.china.com/redian/2025/0808/082025_1712259.html', 'Second-hand: a press report'),
    ('AIWz', 'AI Wiki, PL-Universe Zeus 1 ("weighing about 300 kg"; Zeus 1 is the 大白)',
     'https://aiwiki.ai/wiki/pl_universe_zeus_1', 'Second-hand: a wiki'),
    ('PRCo', 'Perceptyne, PR-OMNI page ("120 kg", "3 kWh (2 × 1.5 kWh, swappable)")',
     'https://www.perceptyne.com/product/omni', "Manufacturer's specification"),
    # The hydraulic Neo1 (E27.7), read first-hand on 2026-11-04 (VERIFICATION.md V157, V159); and the hydraulic rows'
    # sources, shared with types 5 and 6 (tools/parts_taken_apart.py).
    ('NAT', 'New Atlas, Kardoudi, 2026-11-01: NeodraDynamics\' Neo1 ("1.2 metric tons", "a cable supplies its power. A '
            'battery will come once it moves")',
     'https://newatlas.com/robotics/neodradynamics-neo1-giant-hydraulic-humanoid-robot/',
     'Second-hand: a press report with the maker interviewed'),
    ('SSB', '上海证券报 via 新浪财经, 2026-08-19: Neo1\'s 41 joints ("双臂14个、双手10个、双腿及脚部12个、腰部3个、头部2个")',
     'https://finance.sina.com.cn/roll/2026-08-19/doc-ininwpnf6934528.shtml',
     "Second-hand: a press report at the maker's show"),
    *HYDRAULIC_SOURCES,
]


def sources(rows: dict) -> list:
    """The sheet Sources of a file: its own sources that its rows name, and type 2's file's sources its rows name (the
    shared rows' and the helpers' codes), each once. A robot's name is no citation: the names, some of which hold a
    source's code ("Moon Dynamics L1", "Robo Robotics ROBO-T1"), are left out of the text searched (E15.7)."""
    text = ' '.join(str(cell) for sheet in rows.values() for row in sheet for cell in row)
    # The robots' names of this file and of type 2's, whose helpers' texts name its robots ("type 2's Tlibot T1").
    names = {str(row[0]) for row in rows.get('Robots', []) if row} | {str(row[0]) for row in T2.ROBOTS_ROWS if row}
    for name in sorted(names, key=len, reverse=True):
        text = text.replace(name, ' ')
    named = lambda code: re.search(r'(?<![\w])' + re.escape(code) + r'(?![\w])', text)  # noqa: E731
    own = [row for row in OWN_SOURCES if named(row[0])]
    mine = {row[0] for row in own}
    return own + [row for row in T2.SOURCES_ROWS if row[0] not in mine and named(row[0])]
