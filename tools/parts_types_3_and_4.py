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
their joints from AgiBot's model files and the A2 from its page's knee.

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

# Each robot in the file of its first type among 3 and 4 (E11.7 point 1), in the register's order of numbers.
BLOCKS_3 = [NEURA_4NE1_GEN_3, NEURA_4NE1_GEN_35, NEURA_4NE1_GEN_4, AGIBOT_A2_MAX, PNDBOTICS_ADAM_LITE,
            PNDBOTICS_ADAM_SP, HEXAGON_AEON, AGILE_ONE, AIDOL, AEI_ALICE_M1, TEKNTRASH_ALPHA, AI2_ALPHABOT_2, ANIGON,
            APPTRONIK_APOLLO, APPTRONIK_APOLLO_2, BOSTON_DYNAMICS_ATLAS, NEUBILITY_BILLI, BORG_01,
            WANDERCRAFT_CALVIN_40,
            # Batch 2 (E12.5, E12.6): 18 robots, the CYBORG RO1 and the DR02 in two versions.
            ELITE_CENTAUR_G1, DONUT_CINNAMON_1, UBTECH_CRUZR_S2, UBTECH_CRUZR_Y1, CYBORG_RO1_SE, CYBORG_RO1_PRO,
            CYBORG_WO1, SHARPA_D01, RICHTECH_DEX, BOSHIAC_DEXBOT, AGILITY_DIGIT, AGILITY_DIGIT_5, DEEP_DR02,
            DEEP_DR02_PRO, DUATIC_ALPHA, SIASUN_DUCO, ADDVERB_ELIXIS, ADDVERB_ELIXIS_W, GENESIS_ENO, AVIC_FENGXING_001]
BLOCKS_4 = [ONE_X_NEO, AGIBOT_A2, AGIBOT_A3_ULTRA, ANDROMEDA_ABI, AGIBOT_A3, AGIBOT_X2, AGIBOT_X2_ULTRA, DOBOT_ATOM,
            VBOT_ATOM,
            # Batch 2 (E12.5, E12.6): 8 robots, the CASBOT 02 and the FF Master in two versions.
            CASBOT_02, CASBOT_02_EDU, CASIVISION_CASIVIBOT, LG_CLOID, XYZ_DEUX, NOETIX_DORA, REALBOTIX_F_SERIES,
            FF_FUTURIST, FF_MASTER_EDU, FF_MASTER_ULTRA]

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
]


def sources(rows: dict) -> list:
    """The sheet Sources of a file: its own sources that its rows name, and type 2's file's sources its rows name (the
    shared rows' and the helpers' codes), each once."""
    text = ' '.join(str(cell) for sheet in rows.values() for row in sheet for cell in row)
    named = lambda code: re.search(r'(?<![\w])' + re.escape(code) + r'(?![\w])', text)  # noqa: E731
    own = [row for row in OWN_SOURCES if named(row[0])]
    mine = {row[0] for row in own}
    return own + [row for row in T2.SOURCES_ROWS if row[0] not in mine and named(row[0])]
