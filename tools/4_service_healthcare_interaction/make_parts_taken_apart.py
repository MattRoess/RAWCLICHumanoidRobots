"""
Builder of data/researched/4_service_healthcare_interaction/parts_taken_apart.xlsx: the robots of type 4
(Service / Healthcare / Interaction) taken apart so far, part by part.

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

Matthias, 2026-10-30: "Can we move to type 3 and 4 together?", "Yes, together", "Yes, all four" (EVIDENCE.md E11.2),
"Yes, 64 kg" (E11.5), "Yes, agree E11.6", "Yes, build it" (E11.7, its open points A to C as recommended).

WHAT IT DOES
------------
It writes the data file of type 4's robots taken apart so far, each part by part, as type 2's builder writes type 2's
(the same sheets, the same machinery in tools/parts_taken_apart.py): batch 1 of types 3 and 4, its robots whose first
type among 3 and 4 is 4, 8 (9 blocks, the X2 in two versions) (E11.7 point 1). Their blocks, and types 3 and 4's
templates (on legs and on wheels, under names of their own), are held in tools/parts_types_3_and_4.py, one copy for both
builders (E11.7 open point A). A robot of type 4 whose rows stand in another type's file (types 1 and 2, or the other of
3 and 4) is drawn by 02 from there (E11.7 point 4), not written here.

WHAT IT READS AND WRITES
------------------------
It reads nothing but 00's settings (src/params_schema.py, for where the file goes). It writes one file, the path of
`data.parts_taken_apart` with its folder (data/researched/4_service_healthcare_interaction/parts_taken_apart.xlsx,
git-ignored; the folder is the one this file sits in), and replaces the file there.

WHERE IT SITS
-------------
It is not a stage: it writes one of the model's inputs, so it stands in tools/ and has no number. 01_schemas.py reads
and checks the file; 02_composition.py draws robot type 4 part by part over its robots of every file. Press Run: no
arguments. Importing this file writes nothing; tests/test_make_parts_taken_apart.py checks what it writes.
"""
import os
import sys

# The tools/ folder, so that the shared machinery (tools/parts_taken_apart.py) and types 3 and 4's one copy of their
# robots (tools/parts_types_3_and_4.py) can be imported when this file is run.
TOOLS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TOOLS not in sys.path:
    sys.path.insert(0, TOOLS)
import parts_types_3_and_4 as SHARED  # noqa: E402  (types 3 and 4's templates and blocks)
from parts_taken_apart import (SHARED_CONSTANTS_FIRST, SHARED_CONSTANTS_LAST, robot_rows,  # noqa: E402
                               sensor_elements, sheets, type_output_path, write_file)

ROBOT_TYPE = 4
FOLDER = os.path.basename(os.path.dirname(os.path.abspath(__file__)))

# --- About ----------------------------------------------------------------------------------------------------------
# The file's own description, one line per row of its first column (None leaves the row empty).
ABOUT = [
    'Robot type 4 part by part: its robots of batch 1 of types 3 and 4 taken apart (each in the file of its first type '
    'among 3 and 4), for where their critical materials sit',
    None,
    'Agreed by Matthias on 2026-10-30 (documentation/claude/EVIDENCE.md E11.2, E11.5, E11.6: "Yes, all four", "Yes, 64 '
    'kg", "Yes, agree E11.6"; entered on "Yes, build it", E11.7), written as type 2\'s robots are '
    '(tools/parts_taken_apart.py), their blocks in tools/parts_types_3_and_4.py. Written by Claude.',
    "Sheet Robots: each robot, its maker, its type, the maker's height and stated mass. Every sheet with a column "
    "Robot holds each robot's own rows; JointParts, Shares and SensorElements are one set for all (the G1's joint "
    "insides, scaled to each joint's module mass, as for types 1 and 2).",
    "Labels: W weighed; S from a source (named in Sources); E an estimate, with at least half to 1.5 times its mode.",
    'Every range is min / mode / max. A remainder takes what the other shares or parts leave; nothing is rescaled.',
    None,
    "Types 3 and 4's own templates (E11.6 point 1), by names of their own: the joint modules 22.4 / 44.7 / 67.1 % of "
    "the robot's mass on legs (the median of the seven robots of types 3 or 4 with every joint), 6.95 / 13.9 / 20.85 % "
    'on wheels (of the three), split as they are on average; the battery 14.67 Wh per kg of robot on legs, 10.84 on '
    'wheels, where a maker gives no energy.',
    "A robot whose maker gives no mass: the register's (the catalogue's) ± 1 kg (E11.2 point 2); the 4NE1 Gen 4 64 kg "
    'from its "20% lighter than the generation before" (E11.5).',
    'Sheet Sources: every source code used here, as in EVIDENCE.md E11.',
]

# Every robot of type 4 of batch 1, in the register's order of numbers, the robots of a template with its rows.
GENERATED = [robot_rows(b, ROBOT_TYPE, SHARED.AVERAGE_JOINTS) for b in SHARED.BLOCKS_4]


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
CONSTANTS_ROWS = SHARED_CONSTANTS_FIRST + SHARED.TYPES_34_SHARED + SHARED_CONSTANTS_LAST + generated('Constants')
SOURCES_ROWS = SHARED.sources({'Robots': ROBOTS_ROWS, 'Joints': JOINTS_ROWS, 'Parts': PARTS_ROWS,
                               'Boards': BOARDS_ROWS, 'Sensors': SENSORS_ROWS, 'Constants': CONSTANTS_ROWS})

# Every sheet after About, in the order of the file (sheets(): the shared ones with type 4's rows).
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
