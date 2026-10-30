"""
The robots of robot types 3 and 4 taken apart, part by part: their two templates and the blocks of their batches, one
copy for both types' builders.

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

Matthias, 2026-10-30: "Can we move to type 3 and 4 together?", "Yes, together", then for batch 1 "Yes, all four"
(EVIDENCE.md E11.2), "Yes, 64 kg" (E11.5), "Yes, agree E11.6" (the proposal) and "Yes, build it" (E11.7, its open
points A to C as recommended: A, this one module for both builders).

WHAT IT HOLDS
-------------
Types 3 and 4's own templates (E11.6 point 1): on legs, the joint modules 22.4 / 44.7 / 67.1 % of the robot's mass, the
median of the seven robots of types 3 or 4 with every joint (SEVEN: four of type 2's file, three of batch 1), split as
they are on average; on wheels 6.95 / 13.9 / 20.85 %, the median of the three of types 3 or 4 with every joint, split as
type 2's four (E9.6); the battery's energy per kg of robot where a maker gives none, 14.67 Wh/kg on legs and 10.84 on
wheels. Their shared values carry names of their own ("…, types 3 and 4"), so that no shared value has two numbers
under one name (E11.7 point 2). Then every robot of batch 1 (E11.6, 28 blocks with the X2 in two versions), each a block
of tools/parts_taken_apart.py's machinery, its numbers from its own sources (E11.1 to E11.5) and E11.6's method.

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
FRAME_NOT_STATED = ('Frame', 'Aluminium', 'not stated; aluminium, the remainder (E11.6 point 10)')
# A robot whose maker gives energy but no voltage: 48 V (E), as type 2's TLIBOT T1 and Tien Kung 3.0 (E8.3 point 6).
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
    return voltage_capacity(VOLTS_NOT_STATED, f'{source.split()[0]} states no voltage: 48 V, as type 2\'s TLIBOT T1 '
                                              '(E11.6 point 6)', wh / VOLTS_NOT_STATED,
                            f'{source}: {wh:g} / 48 V', label='S, E')


SIX_HANDS = SIX_JOINT_HAND
AGILE_HAND = joint('Hand (Agile Hand)', 2, None, estimate(1.5), 'Elbows and wrists', 'Arms', size='small')
MAGNESIUM_FRAME_A3 = ('Frame', 'Magnesium', 'AGA3p "magnesium alloy, titanium alloy, and TPU flexible materials": '
                                            'magnesium alloy; its titanium and TPU not drawn (no share stated); the '
                                            'remainder (E11.6 point 10, question 4)')
MAGNESIUM_FRAME_A3U = ('Frame', 'Magnesium', 'AGA3Up "Magnesium alloy + carbon-fiber nylon": magnesium alloy; the '
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
    'Boston Dynamics Atlas', 'Boston Dynamics', 1.90, 90, makers(90, 'BDA, BDAs "Weight 90 kg"'), 56,
    sources='BDA, BDAs (Boston Dynamics: "Height 1.9 m", "Degrees of Freedom 56", "Tactile fingers and palm", "Battery '
            'Life 4 hrs"); E11.3', added_joints=[SIX_HANDS])
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

# Each robot in the file of its first type among 3 and 4 (E11.7 point 1), in the register's order of numbers.
BLOCKS_3 = [NEURA_4NE1_GEN_3, NEURA_4NE1_GEN_35, NEURA_4NE1_GEN_4, AGIBOT_A2_MAX, PNDBOTICS_ADAM_LITE,
            PNDBOTICS_ADAM_SP, HEXAGON_AEON, AGILE_ONE, AIDOL, AEI_ALICE_M1, TEKNTRASH_ALPHA, AI2_ALPHABOT_2, ANIGON,
            APPTRONIK_APOLLO, APPTRONIK_APOLLO_2, BOSTON_DYNAMICS_ATLAS, NEUBILITY_BILLI, BORG_01,
            WANDERCRAFT_CALVIN_40]
BLOCKS_4 = [ONE_X_NEO, AGIBOT_A2, AGIBOT_A3_ULTRA, ANDROMEDA_ABI, AGIBOT_A3, AGIBOT_X2, AGIBOT_X2_ULTRA, DOBOT_ATOM,
            VBOT_ATOM]

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
    ('AGA2U', 'AgiBot, A2 Ultra and A2 Lite page', 'https://www.agibot.com/products/A2_Ultra',
     "Manufacturer's specification"),
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
]


def sources(rows: dict) -> list:
    """The sheet Sources of a file: its own sources that its rows name, and type 2's file's sources its rows name (the
    shared rows' and the helpers' codes), each once."""
    text = ' '.join(str(cell) for sheet in rows.values() for row in sheet for cell in row)
    named = lambda code: re.search(r'(?<![\w])' + re.escape(code) + r'(?![\w])', text)  # noqa: E731
    own = [row for row in OWN_SOURCES if named(row[0])]
    mine = {row[0] for row in own}
    return own + [row for row in T2.SOURCES_ROWS if row[0] not in mine and named(row[0])]
