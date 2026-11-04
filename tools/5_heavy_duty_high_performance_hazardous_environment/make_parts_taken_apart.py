"""
Builder of data/researched/5_heavy_duty_high_performance_hazardous_environment/parts_taken_apart.xlsx: the robots of
type 5 (Heavy-Duty / High-Performance / Hazardous-Environment) whose first type is 5, taken apart part by part.

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

Matthias, 2026-11-01: "do now all the rest for type 5 and 6 research all data use the internet as much as possible and
read also .pdf", "Yes, agree both" (EVIDENCE.md E15 and E16), then "Find all the data for 5 and 6 and then fill in the
data in the respective sheets. So I can then have all dat for the run of 01 and 02" (E16.6).

WHAT IT DOES
------------
It writes the data file of type 5's own robots, each part by part, as types 3 and 4's builders write theirs (the same
sheets, the same machinery in tools/parts_taken_apart.py, types 3 and 4's templates in tools/parts_types_3_and_4.py,
which types 5 and 6 use, having none of their own): EngineAI's T800 in two versions, Dev and PRO, each joint its
stated motor (E16.2, E16.5 question 2), and Mirsee's MH3 on its wheels. A robot of type 5 whose rows stand in another
type's file (the Atlas, the CYBORG RO1 and WO1, the DR02, the Kaleido 9 and the Moby in type 3's; the H1 in type 2's) is
drawn by 02 from there (E11.7 point 4), not written here. Since 2026-11-04 (EVIDENCE.md E27.7, "Yes, build it") the
hydraulic Atlas (old) of 2016 to 2024, its actuators as Moog's ISA v2, or in its other version the v5 at its knees (E27.8),
each as often, its power unit, battery and oil; Neo1, also of type 5, stands in type 3's file. TITAN has no stated mass.

WHAT IT READS AND WRITES
------------------------
It reads nothing but 00's settings (src/params_schema.py, for where the file goes). It writes one file, the path of
`data.parts_taken_apart` with its folder (data/researched/5_heavy_duty_high_performance_hazardous_environment/
parts_taken_apart.xlsx, git-ignored; the folder is the one this file sits in), and replaces the file there.

WHERE IT SITS
-------------
It is not a stage: it writes one of the model's inputs, so it stands in tools/ and has no number. 01_schemas.py reads
and checks the file; 02_composition.py draws robot type 5 part by part over its robots of every file. Press Run: no
arguments. Importing this file writes nothing; tests/test_make_parts_taken_apart.py checks what it writes.
"""
import os
import re
import sys

# The tools/ folder, so that the shared machinery (tools/parts_taken_apart.py) and types 3 and 4's templates and
# helpers (tools/parts_types_3_and_4.py) can be imported when this file is run.
TOOLS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TOOLS not in sys.path:
    sys.path.insert(0, TOOLS)
import parts_types_3_and_4 as SHARED  # noqa: E402  (types 3 and 4's templates, used by types 5 and 6)
from parts_taken_apart import (HOUSING_ALUMINIUM, HYDRAULIC_CONSTANTS, HYDRAULICS, JOINT_PLACES,  # noqa: E402
                               SHARED_CONSTANTS_FIRST, SHARED_CONSTANTS_LAST, block, estimate, isa_actuators, joint,
                               robot_rows, sensor_elements, sheets, spread, type_output_path, write_file)

ROBOT_TYPE = 5
FOLDER = os.path.basename(os.path.dirname(os.path.abspath(__file__)))

# --- About ----------------------------------------------------------------------------------------------------------
ABOUT = [
    'Robot type 5 part by part: its own robots taken apart (each in the file of its first type), for where their '
    'critical materials sit',
    None,
    'Agreed by Matthias on 2026-11-01 (documentation/claude/EVIDENCE.md E16: "Yes, agree both"; entered on "Find all '
    'the data for 5 and 6 and then fill in the data in the respective sheets", E16.6), written as types 3 and 4\'s '
    'robots are (tools/parts_taken_apart.py), with types 3 and 4\'s templates (tools/parts_types_3_and_4.py). Written by '
    'Claude.',
    "Sheet Robots: each robot, its maker, its type, the maker's height and stated mass. Every sheet with a column "
    "Robot holds each robot's own rows; JointParts, Shares and SensorElements are one set for all (the G1's joint "
    "insides, scaled to each joint's module mass, as for types 1 to 4).",
    "Labels: W weighed; S from a source (named in Sources); E an estimate, with at least half to 1.5 times its mode.",
    'Every range is min / mode / max. A remainder takes what the other shares or parts leave; nothing is rescaled.',
    None,
    "The T800: each joint its motor as EngineAI's developer documents weigh it (Q25H 0.5 to Q300H-L 2.6 kg), matched "
    "to the joint by its model files' efforts, ± 5 %; its battery 61.2 V × 20 Ah, NMC, its pack 7.2 kg in aluminium. "
    "The MH3: types 3 and 4's template on wheels, its four mecanum wheels driven.",
    "The hydraulic Atlas (old) (EVIDENCE.md E27.7, 2026-11-04): its 28 hydraulic joints each an actuator as Moog's ISA "
    'v2, or in its other version the v5 at its knees (E27.8, "Yes, knees only"), each version as often; its valve, '
    'board and sensors, its titanium body the remainder; its power unit, manifold, battery and oil; no electric joint.',
    "Robots of type 5 in other files (types 2 and 3) are drawn by 02 from there; the sheet Type 5 of the register "
    'names every robot of type 5 and what the run does with it.',
    'Sheet Sources: every source code used here, as in EVIDENCE.md E16.',
]

# --- EngineAI T800 (E16.2; EngineAI's developer documents and model files, read first-hand: V135) -------------------
# Each joint its motor's stated mass ± 5 % (S), as the PNDbotics Adam's actuators (E11.6 point 2): the Q-series motor
# whose "最大力矩" is the joint's effort in its model file (415 the Q300H-L, 370 the Q300H, 222 the Q200H, 160 the Q50H,
# 52 the Q25H, its "峰值扭矩52 N·m"), each at its place in the body (JOINT_PLACES, by its name's first word).
T800_MOTOR_KG = {415: 2.6, 370: 2.1, 222: 1.65, 160: 0.95, 52: 0.5}


def motor(name: str, count: int, torque: float) -> tuple:
    """A joint of the T800: its effort (N·m) in EngineAI's model file and its Q-series motor's stated mass, ± 5 %."""
    return joint(name, count, torque, spread(T800_MOTOR_KG[torque]), *JOINT_PLACES[name.split()[0]])


T800_BODY = [motor('Hip pitch', 2, 415), motor('Hip roll', 2, 370), motor('Hip yaw', 2, 222), motor('Knee', 2, 415),
             motor('Ankle pitch', 2, 160), motor('Ankle roll', 2, 160), motor('Waist yaw', 1, 222),
             motor('Shoulder pitch', 2, 160), motor('Shoulder roll', 2, 160), motor('Shoulder yaw', 2, 160),
             motor('Elbow pitch', 2, 160), motor('Elbow yaw', 2, 52), motor('Head pitch', 1, 52),
             motor('Head yaw', 1, 52)]
# The PRO's wrists, its "L05直线关节" (linear joints) at 5 N·m in its model file, of no stated mass: type 2's refit at
# their torque, half to 1.5 times (E); its hands EngineAI's "单手 740g" with their seven F17 finger joints, ± 5 % (S).
T800_PRO_WRISTS = [joint('Wrist pitch', 2, 5, SHARED.T2.from_torque(5), 'Elbows and wrists', 'Arms'),
                   joint('Wrist roll', 2, 5, SHARED.T2.from_torque(5), 'Elbows and wrists', 'Arms')]
T800_HAND = joint('Hand (EngineAI, 7 joints)', 2, None, spread(0.74), 'Elbows and wrists', 'Arms', size='small')
T800_SOURCES = ('EAIm: each joint its Q-series motor, "最大力矩" and "质量" (Q25H 50 N·m 0.5 kg, Q50H 160 N·m 0.95 kg, '
                'Q200H 222 N·m 1.65 kg, Q300H 370 N·m 2.1 kg, Q300H-L 415 N·m 2.6 kg), matched by EAIu\'s efforts, '
                '± 5 % (S)')


def engineai_t800(pro: bool) -> dict:
    """The T800 Dev and PRO, each as often (E16.5 question 2): each its stated mass with battery, its motors, its
    battery, its two computers, its sensors; the PRO also its wrists and its hands."""
    name, kg = ('EngineAI T800 PRO', 85.3) if pro else ('EngineAI T800 Dev', 84.5)
    joints = T800_BODY + (T800_PRO_WRISTS + [T800_HAND] if pro else [])
    return block(
        name, 'EngineAI Robotics', 1.73, kg,
        f'EAIs (EngineAI: "带电重量 约{kg:g}kg", "总自由度 {"29+14(灵巧手)" if pro else "25"}", "173cm(H)"), EAIm, EAIb, '
        'EAIc, EAIn, EAIh, EAIu (its model files serial_t800.urdf 84.988 kg and serial_t800pro.urdf 85.227 kg), EAI; '
        'E16', SHARED.makers(kg, f'EAIs "带电重量 约{kg:g}kg"'), joints,
        joints_stated=sum(j[1] for j in joints if not j[0].startswith('Hand')) + (2 if pro else 0),
        # Its motors and hands weighed by their maker (S); the PRO's wrists of no stated mass among its small joints.
        joint_label={'small': 'S, E' if pro else 'S', 'large': 'S'},
        joint_sources=T800_SOURCES + ('; its wrists the refit at 5 N·m (E); its hands EAIh "单手 740g", ± 5 % (S)'
                                      if pro else ''),
        **SHARED.voltage_capacity(61.2, 'EAIb "标称电压 61.2V"', 20, 'EAIb "标称容量 20Ah", "电池能量 1.22kWh"'),
        pack=(spread(7.2), 'S', 'EAIb "系统总质量 ≈7.2KG", ± 5 %'), housing=HOUSING_ALUMINIUM,
        **SHARED.with_defaults(1.73, kg, dict(
            cells=('S', 'NMC cylindrical: EAIb "三元锂电池" (ternary lithium, NMC); its "PACK 外壳材质 铝合金" the housing'),
            boards=[SHARED.named_board('Nezha (Intel N97)', 'EAIc "Nezha", EAIs "NeZha N97"'),
                    *SHARED.agx_orin('EAIc "NVIDIA Jetson AGX Orin 64GB"'), SHARED.POWER_BOARD],
            sensors=[SHARED.binocular('EAIn "视觉感知 RGB 头部 1（双目）"'), SHARED.lidar('EAIn "激光雷达 头部 1"'),
                     SHARED.imu('EAIn "IMU 躯干中心 1"'), SHARED.microphones('EAIn "麦克风阵列 环麦 ×4"'),
                     SHARED.counted(SHARED.speaker('EAIn "高保真扬声器 2个"'), 2)],
            frame=('Frame', 'Aluminium alloys', 'EAI "Aviation Aluminum + Titanium": aluminium, its titanium not drawn (no '
                                         'share stated); the remainder (E15.6 question 6)'))))


ENGINEAI_T800_DEV, ENGINEAI_T800_PRO = engineai_t800(False), engineai_t800(True)

# --- Mirsee MH3 (E16.2): types 3 and 4's template on wheels, its four mecanum wheels driven ---------------------------
MIRSEE_MH3 = SHARED.wheeled(
    'Mirsee MH3', 'Mirsee Robotics', 1.80, None,
    ((124, 125, 126), 'S', 'AIWm "Weight (with battery) 125 kg" (aiwiki, citing Mirsee\'s site and Aparobot; the '
                           'catalogue the same); Mirsee states none; ± 1 kg (E15.2 point 1)'),
    31 - 12, sources='MIR (Mirsee: "31 degrees of freedom", "10 Hour Runtime", "Wireless Charging", "Power off brakes"), '
                     'AIWm ("Wheeled (Mecanum omnidirectional)", "DOF per hand 6", "Aluminum 6061"), IEm ("NVIDIA Jetson '
                     'processors", "Mecanum wheels"); its 31 less its two hands of 6; E16',
    driven=4, caster_count=0, added=(SHARED.hands(6),),
    boards=SHARED.agx_orin('IEm "NVIDIA Jetson processors" (E: as an AGX Orin)', label='E') + [SHARED.POWER_BOARD],
    sensors=[SHARED.binocular('IEm "Hadron Vision System … custom-designed stereo cameras"'), SHARED.IMU_NOT_NAMED])

# --- Boston Dynamics' hydraulic Atlas of 2016 to 2024, the register's Atlas (old) (EVIDENCE.md E27.7 point 4) ----------
# Its 28 hydraulic joints (FPW, IRG "Degrees of Freedom (DoF) 28") by place as the seven robots of types 3 and 4's
# template have theirs (point 9.9); each an actuator as Moog's ISA, none electric: in one version each the v2, in the
# other the v5 at its knees only and the v2 at its other places (Matthias, 2026-11-04, "Yes, knees only", E27.8: with
# the v5 at all 28 its frame fell below zero in 2.1 % of its draws, V161; HyQReal has its v5 at its knees, SEM19).
ATLAS_OLD_PLACES = SHARED.places_of(28)
V5_AT_THE_KNEES = {place: 'v5' if place == 'knees' else 'v2' for place in ATLAS_OLD_PLACES}


def atlas_hydraulic(version: str | dict) -> dict:
    """The hydraulic Atlas with its actuators as Moog's ISA of `version` (or V5_AT_THE_KNEES), each version as
    often: its mass Boston
    Dynamics' (point 4.1, its block's, not the register's 89 kg: point 9.1), its actuators, manifold and power unit, its
    battery from its energy, its three computers, its sensors, its oil; its hydraulic lines in its frame of titanium and
    aluminium (points 4.8, 4.10); its shell, cables, screws and cooler the template's (point 4.11)."""
    why = 'FPW "28 degrees of freedom", by the seven robots of types 3 and 4\'s template, their joints by place (E27.7 ' \
          'point 9.9)' + ('; the v5 at its knees only (SEM19 "These ISAs (v5) are mounted in the upper leg of the robot ' \
                          'to actuate the knee joints"; E27.8)' if isinstance(version, dict) else '')
    actuators = isa_actuators(ATLAS_OLD_PLACES, version, why)
    name = 'v5 at the knees' if isinstance(version, dict) else version
    return block(
        f'Boston Dynamics Atlas hydraulic ISA {name}', 'Boston Dynamics', 1.50, 80,
        'BDs (Boston Dynamics, 2016: "180 lbs"), FPW (Saunders: "about 1.5 meters tall and weighs 80 kg", "28 degrees '
        'of freedom", its power unit "approaching a Kilowatt per kg"), BDb ("190-pound frame"), IRG, HBR; E27',
        ((80, 81.6, 86.2), 'S', 'FPW "weighs 80 kg" the min, BDs "180 lbs" (81.6 kg) the mode, BDb "190-pound" (86.2 '
                                'kg) the max (E27.4 question 2); the register\'s 89 kg (the catalogue\'s) has no '
                                'first-hand origin (E27.7 point 9.1)'),
        [], **SHARED.energy(1400, 'HBR "1400 ватт*час"'),
        oil=((1, 2, 4), 'E', 'its actuators, lines and reservoir: no source states it; HyQ\'s "4-litre plastic oil tank" '
                             '(SEM11) the most (E27.7 point 4.9)'),
        **SHARED.with_defaults(1.50, 81.6, dict(
            boards=[(SHARED.COMPUTER_NOT_NAMED, 3, 'Boards', 'Torso', SHARED.COMPUTER, 'ITC', 'E',
                     'IRG "Three on-board computers inside torso": each as the template\'s computer board (E)'),
                    SHARED.POWER_BOARD] + actuators['boards'],
            sensors=[SHARED.lidar('BDs "LIDAR and stereo sensors in its head"'),
                     SHARED.binocular('BDs "LIDAR and stereo sensors in its head"'), SHARED.IMU_NOT_NAMED]
            + actuators['sensors'],
            parts=actuators['parts'] + [
                ('Hydraulic manifold', 1, HYDRAULICS, 'Torso', estimate(2.1), 'Titanium alloy or Aluminium alloys',
                 'Ti-6Al-4V', 'E', 'FPW "Atlas\' manifold has 18 valves, which service the upper body": as the ISA\'s '
                                   'smart manifold, FRO Table 2 "2,100 g", half to 1.5 times; IRG titanium and '
                                   'aluminium, either, each as often (E27.4 question 7); Ti-6Al-4V the titanium\'s '
                                   "grade (E), the aluminium the type's"),
                ('Hydraulic power unit', 1, HYDRAULICS, 'Torso', (2.5, 5, 12), None, None, 'S, E',
                 'HBR "массой всего 5 кг и мощностью 5 кВт" the mode (second-hand: a retelling of the maker\'s talk); '
                 'half of it the min (E); KHN MiniHyQ\'s pack "Weight 12 kg" at "5.5 kW" the max (E27.4 question 8); '
                 'its materials in the sheet Shares')],
            frame=('Frame: titanium and aluminium', None, 'IRG "Mixture of titanium and aluminum 3D-printed parts. '
                                                          'Actuators and hydraulic lines embedded in leg structures": '
                                                          'the remainder, its shares in the sheet Shares (E27.7 point '
                                                          '4.10)'))))


ATLAS_HYDRAULIC_V2, ATLAS_HYDRAULIC_V5_KNEES = atlas_hydraulic('v2'), atlas_hydraulic(V5_AT_THE_KNEES)

# Every robot of type 5 written here, in the register's order of numbers.
BLOCKS_5 = [ATLAS_HYDRAULIC_V2, ATLAS_HYDRAULIC_V5_KNEES, MIRSEE_MH3, ENGINEAI_T800_DEV, ENGINEAI_T800_PRO]
GENERATED = [robot_rows(b, ROBOT_TYPE, SHARED.AVERAGE_JOINTS) for b in BLOCKS_5]

# --- Sources --------------------------------------------------------------------------------------------------------
# Every source of this file read first-hand on 2026-11-01 (EVIDENCE.md E16, VERIFICATION.md V135).
OWN_SOURCES = [
    ('EAI', 'EngineAI, T800 page ("Varies by Configuratoin: 75kg~85kg", "Aviation Aluminum + Titanium")',
     'https://en.engineai.com.cn/product-t800', "Manufacturer's specification"),
    ('EAIs', 'EngineAI, T800 developer documents 2, robot specification ("带电重量", "总自由度", "NeZha N97")',
     'https://engineai.com.cn/open/docs/t800/05/02', "Manufacturer's documentation"),
    ('EAIc', 'EngineAI, T800 developer documents 3, onboard computers ("Nezha", "NVIDIA Jetson AGX Orin 64GB")',
     'https://engineai.com.cn/open/docs/t800/05/03', "Manufacturer's documentation"),
    ('EAIn', 'EngineAI, T800 developer documents 4, sensors', 'https://engineai.com.cn/open/docs/t800/05/04',
     "Manufacturer's documentation"),
    ('EAIm', 'EngineAI, T800 developer documents 5, joint motors (Q25H to Q300H-L: "最大力矩", "质量")',
     'https://engineai.com.cn/open/docs/t800/05/05', "Manufacturer's documentation"),
    ('EAIh', 'EngineAI, T800 developer documents 6, dexterous hand ("单手 740g", "灵巧手自由度7个")',
     'https://engineai.com.cn/open/docs/t800/05/06', "Manufacturer's documentation"),
    ('EAIb', 'EngineAI, T800 developer documents, battery ("三元锂电池", "20Ah", "61.2V", "1.22kWh", "≈7.2KG")',
     'https://engineai.com.cn/open/docs/t800/05/08', "Manufacturer's documentation"),
    ('EAIu', 'EngineAI, engineai_robotics_description: serial_t800.urdf, serial_t800pro.urdf (their efforts)',
     'https://github.com/engineai-robotics/engineai_robotics_description', "Manufacturer's model file"),
    ('MIR', 'Mirsee Robotics, its site (MH3: "31 degrees of freedom", "10 Hour Runtime")', 'https://www.mirsee.com/',
     "Manufacturer's page"),
    ('AIWm', 'The AI Wiki, Mirsee Robotics MH3 ("Weight (with battery) 125 kg (276 lb)")',
     'https://aiwiki.ai/wiki/mirsee_robotics_mh3', 'Second-hand: a wiki citing its maker'),
    ('IEm', 'Interesting Engineering, Mirsee MH3, 2026-07-03 ("NVIDIA Jetson processors", "Mecanum wheels")',
     'https://interestingengineering.com/ai-robotics/canada-firms-humanoid-robot-hazardous',
     'Second-hand: a press report'),
    # The hydraulic Atlas (old) (EVIDENCE.md E27), read first-hand on 2026-11-01 and 2026-11-04 (V135, V157, V158).
    ('BDs', 'IEEE Spectrum, 2016-02-23, quoting Boston Dynamics\' video ("about 5\' 9" tall … and weighs 180 lbs", '
            '"LIDAR and stereo sensors in its head")',
     'https://spectrum.ieee.org/next-generation-of-boston-dynamics-atlas-robot', "Second-hand: the maker's video quoted"),
    ('FPW', 'Fluid Power World, 2018-03-23, Boston Dynamics\' Aaron Saunders ("weighs 80 kg", "28 degrees of freedom", '
            '"Atlas\' manifold has 18 valves")', 'https://www.fluidpowerworld.com/?p=131942',
     "Second-hand: the maker's engineer reported"),
    ('BDb', 'Boston Dynamics, blog "Build it, break it, fix it" ("its 190-pound frame")',
     'https://bostondynamics.com/blog/build-it-break-it-fix-it/', "Manufacturer's blog"),
    ('HBR', 'habr.com, 2021-01-26, how Atlas works, after Raibert\'s and Kuindersma\'s talk ("гидравлический силовой '
            'агрегат массой всего 5 кг и мощностью 5 кВт", "1400 ватт*час")', 'https://habr.com/ru/articles/539290/',
     "Second-hand: a blog retelling the maker's talk"),
    ('SEM11', 'Semini et al. (IIT), Design of HyQ, IMechE Part I 225 (2011) ("a 4-litre plastic oil tank", "70kg '
              '(external hydraulic system), 91kg (onboard hydraulic system)")',
     'https://iit-dlslab.github.io/papers/semini11jsce.pdf', 'Peer-reviewed'),
]


def generated(sheet: str) -> list:
    """The rows of every robot on one sheet, in the order of GENERATED."""
    return [row for rows in GENERATED for row in rows[sheet]]


def sources(rows: dict) -> list:
    """The sheet Sources of this file: its own sources that its rows name, then types 3 and 4's and type 2's that its
    rows name (the shared rows' and the helpers' codes), each once."""
    text = ' '.join(str(cell) for sheet in rows.values() for row in sheet for cell in row)
    named = lambda code: re.search(r'(?<![\w])' + re.escape(code) + r'(?![\w])', text)  # noqa: E731
    own = [row for row in OWN_SOURCES if named(row[0])]
    mine = {row[0] for row in own}
    return own + [row for row in SHARED.sources(rows) if row[0] not in mine]


# The sheets' rows.
ROBOTS_ROWS = generated('Robots')
JOINTS_ROWS = generated('Joints')
PARTS_ROWS = generated('Parts')
BOARDS_ROWS = generated('Boards')
SENSORS_ROWS = generated('Sensors')
SENSORELEMENTS_ROWS = sensor_elements([], generated('SensorElements'))
CONSTANTS_ROWS = (SHARED_CONSTANTS_FIRST + SHARED.TYPES_34_SHARED + SHARED_CONSTANTS_LAST + HYDRAULIC_CONSTANTS
                  + generated('Constants'))
SOURCES_ROWS = sources({'Robots': ROBOTS_ROWS, 'Joints': JOINTS_ROWS, 'Parts': PARTS_ROWS, 'Boards': BOARDS_ROWS,
                        'Sensors': SENSORS_ROWS, 'Constants': CONSTANTS_ROWS})

# Every sheet after About, in the order of the file (sheets(): the shared ones with type 5's rows).
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
