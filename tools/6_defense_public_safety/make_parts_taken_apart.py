"""
Builder of data/researched/6_defense_public_safety/parts_taken_apart.xlsx: the robots of type 6 (Defense / Public
Safety) whose first type is 6, taken apart part by part.

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

Matthias, 2026-11-01: "do now all the rest for type 5 and 6 research all data use the internet as much as possible and
read also .pdf", "Yes, agree both" (EVIDENCE.md E15 and E16), then "Find all the data for 5 and 6 and then fill in the
data in the respective sheets. So I can then have all dat for the run of 01 and 02" (E16.6).

WHAT IT DOES
------------
It writes the data file of type 6's own robots, each part by part, as type 5's builder writes type 5's (the same
machinery, types 3 and 4's templates): IHMC's Alex, its arms as Nadia's cycloidal arm actuators (IHMC: "an iteration of
the actuators made for Nadia's arms", E16.5 question 1), the rest on the template; NORINCO's Fuxi, its form stated by
no source, in two versions, on legs and on wheels, each as often (E15.6 question 2). A robot of type 6 whose rows stand
in another type's file (the T800 in type 5's, the Phantom MK1 in type 3's) is drawn by 02 from there (E11.7 point 4).
The hydraulic Nadia waits for its research step (E16.5 question 4).

WHAT IT READS AND WRITES
------------------------
It reads nothing but 00's settings (src/params_schema.py, for where the file goes). It writes one file, the path of
`data.parts_taken_apart` with its folder (data/researched/6_defense_public_safety/parts_taken_apart.xlsx, git-ignored;
the folder is the one this file sits in), and replaces the file there.

WHERE IT SITS
-------------
It is not a stage: it writes one of the model's inputs, so it stands in tools/ and has no number. 01_schemas.py reads
and checks the file; 02_composition.py draws robot type 6 part by part over its robots of every file. Press Run: no
arguments. Importing this file writes nothing; tests/test_make_parts_taken_apart.py checks what it writes.
"""
import os
import re
import sys

# The tools/ folder, so that the shared machinery and types 3 and 4's templates and helpers can be imported.
TOOLS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TOOLS not in sys.path:
    sys.path.insert(0, TOOLS)
import parts_types_3_and_4 as SHARED  # noqa: E402  (types 3 and 4's templates, used by types 5 and 6)
from parts_taken_apart import (SHARED_CONSTANTS_FIRST, SHARED_CONSTANTS_LAST, joint, model_joints,  # noqa: E402
                               robot_rows, sensor_elements, sheets, spread, type_output_path, write_file)

ROBOT_TYPE = 6
FOLDER = os.path.basename(os.path.dirname(os.path.abspath(__file__)))

# --- About ----------------------------------------------------------------------------------------------------------
ABOUT = [
    'Robot type 6 part by part: its own robots taken apart (each in the file of its first type), for where their '
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
    "Alex: its arms as Nadia's cycloidal arm actuators (peak 158, 158, 79, 79, 19, 19, 19 N·m), each module type 2's "
    "refit at its torque (E); its legs, spine and neck on types 3 and 4's template; its PSYONIC hands 490 g each. Fuxi "
    'on legs and on wheels, each as often, its form stated by no source.',
    "Robots of type 6 in other files (types 3 and 5) are drawn by 02 from there; the sheet Type 6 of the register names "
    'every robot of type 6 and what the run does with it.',
    'Sheet Sources: every source code used here, as in EVIDENCE.md E16.',
]

# --- IHMC Alex (E16.2, E16.5 question 1; IHMC's pages and papers, read first-hand: V135) ---------------------------
# Its arms as Nadia's (IHn, arXiv 2409.04639 Fig. 4: shoulder J1 and J2 158, J3 79, elbow 79, wrist J1 to J3 19 N·m
# peak), each module type 2's refit at its torque, half to 1.5 times (E: IHd "an iteration of the actuators made for
# Nadia's arms"); its other joints on types 3 and 4's template (no torque stated).
ALEX_ARMS = model_joints([('Shoulder pitch', 2, 158), ('Shoulder roll', 2, 158), ('Shoulder yaw', 2, 79),
                          ('Elbow', 2, 79), ('Wrist yaw', 2, 19), ('Wrist pitch', 2, 19), ('Wrist roll', 2, 19)],
                         SHARED.T2.from_torque)
PSYONIC_HAND = joint('Hand (PSYONIC Ability Hand)', 2, None, spread(0.49), 'Elbows and wrists', 'Arms', size='small')
IHMC_ALEX = SHARED.template(
    'IHMC Alex', 'IHMC', 1.79, 85, SHARED.makers(85, 'IHa "85 kg"'), 29 + 2,
    sources='IHa (IHMC: "179 cm", "85 kg", "2+ hrs"), IHd ("an iteration of the actuators made for Nadia\'s arms", "29 '
            'joints"), IHx (arXiv 2609.01518: "PSYONIC Ability Hands … 6 degrees of freedom each", "ZED X Mini"), IHn '
            '(arXiv 2409.04639: Nadia\'s arms), PSY ("490 grams"); E16',
    stated_joints=ALEX_ARMS, added_joints=[PSYONIC_HAND],
    joint_sources=SHARED.TEMPLATE_SOURCES + "; its arms as Nadia's (IHn Fig. 4, peak N·m), each the refit at its "
                                            "torque (E: IHd \"an iteration\"); its hands PSY \"490 grams\", ± 5 % (S)",
    sensors=[SHARED.binocular('IHx "ZED X Mini, a stereo color camera pair"'), SHARED.IMU_NOT_NAMED])

# --- NORINCO Fuxi (E16.2): its mass Global Times' reporter's, its form no source's: two versions, each as often -----
FUXI_MASS = ((84, 85, 86), 'S', 'GTf "伏羲机器人整机高180厘米，重85公斤" (Global Times\' reporter at NORINCO\'s institute; '
                                'NORINCO\'s release: robots "weighing around 90 kilograms", a class); ± 1 kg (E15.2 point 1)')
FUXI_SOURCES = ('GTf (Global Times via 163.com, 2025-11-06: "180厘米", "85公斤", "伏羲的6自由度灵巧手"), GTt (Global Times, '
                '2026-08-18: its teleoperation for robots "weighing around 90 kilograms"); its form stated by no source: '
                'on legs and on wheels, each as often (E15.6 question 2); E16')
NORINCO_FUXI_LEGS = SHARED.template(
    'NORINCO Fuxi on legs', 'NORINCO', 1.80, None, FUXI_MASS, SHARED.JOINTS_MEDIAN + 2, sources=FUXI_SOURCES,
    added_joints=[SHARED.hands(6)])
NORINCO_FUXI_WHEELS = SHARED.wheeled(
    'NORINCO Fuxi on wheels', 'NORINCO', 1.80, None, FUXI_MASS, SHARED.WHEELED_JOINTS_MEDIAN, sources=FUXI_SOURCES,
    added=(SHARED.hands(6),))

# Every robot of type 6 written here, in the register's order of numbers.
BLOCKS_6 = [IHMC_ALEX, NORINCO_FUXI_LEGS, NORINCO_FUXI_WHEELS]
GENERATED = [robot_rows(b, ROBOT_TYPE, SHARED.AVERAGE_JOINTS) for b in BLOCKS_6]

# --- Sources --------------------------------------------------------------------------------------------------------
# Every source of this file read first-hand on 2026-11-01 (EVIDENCE.md E16, VERIFICATION.md V135).
OWN_SOURCES = [
    ('IHa', 'IHMC Robotics, Alex humanoid ("179 cm", "85 kg", "2+ hrs")', 'https://robots.ihmc.us/alex-humanoid',
     "Manufacturer's specification"),
    ('IHd', 'IHMC Robotics, humanoid robot design ("an iteration of the actuators made for Nadia\'s arms")',
     'https://robots.ihmc.us/humanoid-design', "Manufacturer's page"),
    ('IHx', 'Calvert et al. (IHMC), arXiv 2609.01518, 2026: Alex, "PSYONIC Ability Hands", "ZED X Mini"',
     'https://arxiv.org/abs/2609.01518', "Manufacturer's paper"),
    ('IHn', "Bertrand et al. (IHMC), arXiv 2409.04639, 2024, Fig. 4: Nadia's cycloidal arm actuators",
     'https://arxiv.org/abs/2409.04639', "Manufacturer's paper"),
    ('PSY', 'PSYONIC, Ability Hand ("weighs in at 490 grams")', 'https://www.psyonic.io/ability-hand',
     "Manufacturer's specification"),
    ('GTf', 'Global Times via 163.com, NORINCO\'s institute at its show, 2025-11-06 ("180厘米", "85公斤")',
     'https://www.163.com/dy/article/KDLOLOCA0514R9OJ.html', 'Second-hand: a press report'),
    ('GTt', "Global Times, NORINCO's teleoperation system, 2026-08-18", 'https://www.globaltimes.cn/page/202608/'
                                                                       '1368491.shtml', 'Second-hand: a press report'),
]


def generated(sheet: str) -> list:
    """The rows of every robot on one sheet, in the order of GENERATED."""
    return [row for rows in GENERATED for row in rows[sheet]]


def sources(rows: dict) -> list:
    """The sheet Sources of this file: its own sources that its rows name, then types 3 and 4's and type 2's that its
    rows name, each once."""
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
CONSTANTS_ROWS = SHARED_CONSTANTS_FIRST + SHARED.TYPES_34_SHARED + SHARED_CONSTANTS_LAST + generated('Constants')
SOURCES_ROWS = sources({'Robots': ROBOTS_ROWS, 'Joints': JOINTS_ROWS, 'Parts': PARTS_ROWS, 'Boards': BOARDS_ROWS,
                        'Sensors': SENSORS_ROWS, 'Constants': CONSTANTS_ROWS})

# Every sheet after About, in the order of the file.
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
