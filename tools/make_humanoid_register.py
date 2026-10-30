"""
Builder of data/researched/humanoid_register.xlsx: every known humanoid robot, each with its one or two robot types.

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

Matthias, 2026-10-28: "I want that all know humanoid robots at the end can be assigned to types. It should be possible
also to assign themeven they are out of limts. Nothing is left behind as the field is fluid and changes fast"; then the
rules he set while the robots were read (documentation/claude/EVIDENCE.md E4 to E4.11): the use first, the size second;
wheels accepted, an upper body only not; one entry for one robot ("No double counting use just 1"), also when two
makers sell it under two names; a robot in at most two types ("Double assignment means 1 robot can be two types");
industry listed gives type 3; security alone type 6; "Below 15 kg not part of the type 1".

Then, 2026-10-29: "I want the all the know type 1 robots are integrated and included in the run" and "There has to be
an excel sheet where all the robots of the different types are fully listed. For now it has to be just all for type 1."

WHAT IT DOES
------------
It writes the register: one row per robot of the humanoid.guide catalogue (349, as read on 2026-10-28) and the five
robots the catalogue lacks (numbered 350 to 354), each with its types, its form, its mass as a minimum, mode and
maximum, and where in EVIDENCE.md it was decided. The decisions are held here, one line per robot (DECISIONS): a
change is made in this file, not in the .xlsx, where it would be lost at the next run.

Beside the sheet Robots (all robots), the sheet Type 1: every robot whose types include 1, as its leading or its
second type, with every cell of its row in Robots and one more, "In the run": what 02_composition.py does with it
(drawn with its own rows of the parts file, which every robot of type 1 has since 2026-10-29). 02 draws robot type 1
over the robots of this sheet; 01 checks that it lists exactly the robots of type 1 of the sheet Robots, as they
are there. The sheet Type 2 the same for robot type 2 (2026-10-29), none of its robots taken apart yet: 02 draws type
2 from the workbook, and the sheet says so of each.

WHAT IT READS AND WRITES
------------------------
It reads the catalogue (`data.humanoid_guide`, data/raw/humanoid_guide_2026-10-28.xlsx, sheet Catalogue) and writes one
file, the path of `data.register` (data/researched/humanoid_register.xlsx, git-ignored; sheets About, Robots, Type 1
and Type 2), replacing the file there.

WHERE IT SITS
-------------
It is not a stage of the model: it writes one of the model's inputs, so it stands in tools/ and has no number.
01_schemas.py reads and checks the register; 02_composition.py draws robot type 1 over its robots. Press Run: no
arguments. Importing this file writes nothing; tests/test_make_humanoid_register.py checks that what it writes passes
01's checks and equals the file on disk.
"""
import os
import re
import sys

import openpyxl
from openpyxl.styles import Alignment, Font, PatternFill

# The project's root, so that its settings (src/params_schema.py) can be imported when this file is run from tools/.
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
from src.params_schema import Params, absolute, current  # noqa: E402

HEADING_FILL = PatternFill('solid', fgColor='FFEEEEEE')   # the grey of every sheet's first row
ABOUT_WIDTH = 150                                          # the width of the About sheet's column, in characters

# --- About ----------------------------------------------------------------------------------------------------------
ABOUT = [
    'The register of every known humanoid robot, each with its one or two robot types',
    None,
    'Built by tools/make_humanoid_register.py from the humanoid.guide catalogue as read on 2026-10-28 '
    '(data/raw/humanoid_guide_2026-10-28.xlsx) and the decisions held in the builder. Every decision with its reason '
    'and Matthias\'s words: documentation/claude/EVIDENCE.md, the section named in the column "Decided in".',
    None,
    'Types: the robot types of the workbook\'s sheet Taxonomy, 1 to 6, at most two, the leading one first. Entry: '
    'empty for a robot with types; "not assigned: ..." for a robot left out, with why; "the same robot as n" for a '
    'second entry of one robot (counted once, as entry n).',
    'Mass: as the catalogue (or the source of an added robot) states it, second-hand; minimum, mode and maximum the '
    'stated mass +- 1 kg (as the X1\'s and N1\'s own masses, EVIDENCE.md E2.8e) or the stated range; empty where no '
    'mass is stated.',
    'Mass of the PrimeBOT Q1: no source states one; the estimate (E) agreed on 2026-10-29 (EVIDENCE.md E5.17).',
    'Taken apart as: the rows of its type\'s parts file (data/researched/<n>_<name>/parts_taken_apart.xlsx) that are '
    'this robot, for every robot of type 1 and the robots of type 2 taken apart so far; a robot in several versions '
    'names each, separated by "; ", each drawn as often (the Booster K1\'s two batteries, the GR-1\'s one or two '
    'cameras).',
    None,
    'Sheet Type 1: every robot of the sheet Robots whose types include 1 (leading or second), with every cell of its '
    'row there, and "In the run": what 02_composition.py does with it, "drawn: its own parts". 02 draws robot type 1 '
    'over the robots of this sheet, each as often.',
    'Sheet Type 2: every robot whose types include 2, as the sheet Type 1. Five taken apart so far (2026-10-30, "Yes, '
    'build C"), each "drawn: its own parts", part by part on its own; the others "not drawn: not yet taken apart" or '
    '"not drawn: no mass stated"; robot type 2 for stock-and-flow drawn from the workbook until every robot of it with '
    'a mass is taken apart.',
]

# --- The sheets of robot types --------------------------------------------------------------------------------------
# The robot types whose robots are listed in a sheet of their own, "Type n". Matthias, 2026-10-29: "For now it has to
# be just all for type 1"; then for type 2, "Yes, as proposed" (type 2 as type 1, step 5).
TYPES_LISTED = (1, 2)
TYPE_SHEET = 'Type {}'
# What a sheet Type n says of a robot in 02's run, by what 02 does with it (01_schemas.py checks the same four).
IN_RUN_OWN = 'drawn: its own parts'
IN_RUN_NOT = 'not drawn: no mass stated'   # no robot of type 1 since 2026-10-29: each has a mass and its own rows
IN_RUN_WORKBOOK = 'not drawn: its type drawn from the workbook, none of its robots taken apart yet'
# A robot with a mass of a type some of whose robots are taken apart, itself not yet (2026-10-30, "Yes, build C", Q4):
# its type drawn from the workbook for stock-and-flow until every robot of it with a mass is taken apart (Q2).
IN_RUN_LATER = 'not drawn: not yet taken apart'

# --- Robots ---------------------------------------------------------------------------------------------------------
HEADINGS = ['Number', 'Robot', 'Maker', 'Country', 'Status', 'Height (cm)', 'Mass (kg), stated', 'Mass min (kg)',
            'Mass mode (kg)', 'Mass max (kg)', 'Mass basis', 'Types', 'Form', 'Entry', 'Taken apart as',
            'Decided in', 'Source']
WIDTHS = [8, 26, 28, 12, 22, 12, 14, 10, 10, 10, 34, 8, 16, 34, 14, 16, 50]
IN_RUN_WIDTH = 80   # the width of the sheet Type 1's column "In the run", in characters

# The robots the catalogue lacks, read from their makers or from the workbook's sources (EVIDENCE.md E4.11):
# number -> (robot, maker, country, status, height in cm, mass in kg as stated, source).
ADDED = {
    350: ('N1', 'Fourier', 'China', 'In production', '130', '38',
          'https://support-old.fftai.com/en/docs/GR-X-Humanoid-Robot/Fouriern1/N1_Introduction/'),
    351: ('Fuxi', 'NORINCO', 'China', 'Prototype', '180', '90',
          'https://defensemirror.com/news/41857/China___s_NORINCO_Unveils____Fuxi____Humanoid_Battlefield_Robot'),
    352: ('H1', 'Unitree Robotics', 'China', 'In production', '180', '47', 'https://www.unitree.com/h1'),
    353: ('Walker S', 'UBTECH Robotics', 'China', 'In production', '170', '',
          'https://www.ubtrobot.com/en/humanoid/products/walker-s'),
    354: ('PR-OMNI', 'Perceptyne', 'India', 'Pre-order', '157', '120', 'https://www.perceptyne.com/product/omni'),
}

# The robots taken apart, robot type by robot type: number -> the name of its own rows in its type's parts file
# (data/researched/<n>_<name>/parts_taken_apart.xlsx). Type 1: every robot (Matthias, 2026-10-29, "Yes, build it",
# EVIDENCE.md E5.12 to E5.19); type 2: batch 1 (2026-10-30, "Yes, agree E6.8", "Yes, build C") and batch 2
# (2026-10-30, "Yes, agree E7.5", "Yes, build it"; the Alice as the ALICE 4, the Atom Max as DOBOT's Atom, the
# "Kepler" as the K1, E7.3 question 3) and batch 2b (2026-10-30, "Yes, agree E8.3", "Yes, build it"; the Omni kept in
# type 2, E8.2) and its 43 robots on wheels (2026-10-30, "Yes, agree E9.6", "Yes, build it"). A robot in several
# versions names each, separated by '; ', each drawn as often: the Booster K1 with
# its 5 Ah and its 2 Ah battery (E5.14, point 2), the GR-1 with one or two depth cameras (E6.8 point 8), the H2-X with
# an Intel Core i7 or an Orin NX as its second computer (E7.5 point 12), the Walker Tienkung "Voice & Vision" or
# "Embodied intelligence" (E8.2 question 4). No brackets or commas in a name: 04 reads the names from between brackets,
# by commas.
TAKEN_APART = {1: {
    16: 'AgiBot X1', 19: 'ROBOTIS AI Sapiens K1', 23: 'AKINROBOTICS AKINCI-5', 37: 'Menlo Asimov 1',
    38: 'Menlo Asimov 2', 54: 'Booster T1', 55: 'Booster T2', 57: 'Noetix Bumi', 85: 'Noetix E1', 102: 'Unitree G1',
    103: 'Unitree G1+', 143: 'JAKA π', 147: 'ROBOTIS K0', 148: 'Booster K1 5 Ah; Booster K1 2 Ah',
    168: 'Light Origins LightBot-0', 175: 'DOBOT LUMO', 212: 'Nori L3', 231: 'PHYBOT C1', 234: 'EngineAI PM01',
    236: 'PrimeBOT Q1', 246: 'AgiBot QUESTER1', 260: 'Leju Roban2', 268: 'RoboParty Roboto Origin',
    269: 'RoboParty RP1', 279: 'Fauna Sprout', 281: 'StarBot Astra', 308: 'WL Robotics Totan O1', 311: 'Unitree R1',
    332: 'TOPSTAR Xiao Tuo', 343: 'YMBOT E3', 350: 'Fourier N1',
}, 2: {
    25: 'AeiROBOT ALICE 4', 47: 'DOBOT Atom', 53: 'MirrorMe Bolt', 69: 'Xiaomi CyberOne', 80: 'Deep Robotics DR01',
    98: 'Figure AI Figure 03', 116: 'Fourier GR-1 one camera; Fourier GR-1 two cameras', 117: 'Fourier GR-2',
    119: 'Unitree H1-2', 120: 'Unitree H2', 121: 'Unitree H2 Plus',
    123: 'Unitree H2-X Core i7; Unitree H2-X Orin NX', 132: 'HONOR D1', 134: 'Simplexity I-Series',
    135: 'ROBROS IGRIS-C', 144: 'JCBOT JingChu', 151: 'KAIST Humanoid', 153: 'PAL Kangaroo', 157: 'Kepler K1',
    158: 'Kepler K2', 163: 'Leju Kuavo 5', 170: 'LimX CL', 171: 'LimX Oli', 176: 'LimX Luna', 177: 'Lumos LUS2',
    180: 'MagicLab MagicBot Gen1', 199: 'VinMotion Motion 2', 203: 'Zhejiang NAVAI-I3', 210: 'Digit Nezha P01',
    216: 'X-Humanoid Omni', 221: 'Tesla Optimus Gen 3', 222: 'Tesla Optimus Gen 2', 223: 'Tesla Optimus V2.5',
    224: 'Cyan Robotics Orca', 229: 'Sanctuary Phoenix', 232: 'PHYBOT M1', 244: 'OpenLoong Qinglong', 256: 'PAL REEM-C',
    265: 'Robotera L7', 271: 'EngineAI SE01', 272: 'Zeroth Sean', 276: 'Siasun Songxing', 285: 'Unitree Superman',
    290: 'PAL TALOS', 294: 'Westwood THEMIS', 297: 'X-Humanoid TianGong Ultra', 298: 'Tlibot Tianzhen Z1',
    299: 'X-Humanoid Tien Kung 2.0', 300: 'X-Humanoid Tien Kung 3.0', 302: 'Tlibot T1', 323: 'DroidUp Walker II',
    326: 'Walker Tienkung Vision; Walker Tienkung Embodied', 352: 'Unitree H1',
    # The robots on wheels (2026-10-30, "Yes, agree E9.6", "Yes, build it"; EVIDENCE.md E9.6, E9.7): the AICO 2, the
    # RB-Y1 and the R1-D in two versions each (E9.2 point 2), the H2-D as its Flagship and the G1-D as its Ultimate.
    13: 'AgiBot A2-W', 15: 'AgiBot G1', 20: 'ROBOTIS AI Worker', 21: 'Flexiv AICO 2-4; Flexiv AICO 2-10', 34: 'PAL ARI',
    35: 'KIT ARMAR-7', 40: 'Astribot S1', 41: 'Astribot T1', 42: 'ELU.AI AstroDroid AD-01', 49: 'Honda Avatar',
    60: 'CASBOT W1', 68: 'Toyota CUE7', 82: 'RealMan Dual-Arm Lift', 86: 'Tangible Robots Eggie',
    92: 'Feather Robotics Feather', 104: 'Unitree G1-D Ultimate', 105: 'AgiBot G2', 122: 'Unitree H2-D Flagship',
    179: 'MagicLab MagicBot D1', 184: 'Blue Worm Mantis Standard', 200: 'Spirit AI Moz1', 230: 'Sanctuary Phoenix Gen 8',
    247: 'Galaxea R1 Pro', 248: 'Unitree R1-A5-D; Unitree R1-A7-D',
    251: 'Rainbow Robotics RB-Y1 A; Rainbow Robotics RB-Y1 M', 252: 'Pollen Robotics Reachy 2',
    253: 'RealMan RealBot-01', 254: 'RealMan RealBot-L2', 255: 'RealMan RealBot-S2', 295: 'PAL TIAGo Pro',
    307: 'Tokyo Robotics Torobo', 312: 'Lanxin VB1-I', 313: 'Lanxin VB2', 314: 'Dexmate Vega 1 Pro',
    315: 'Lanxin VersaBot VB-1', 318: 'Yue Quan Bionics W-Bot', 335: 'Tlibot Y1', 336: 'Tlibot Y2-B', 337: 'Tlibot Y2-P',
    340: 'Yunmu YMBot D', 341: 'Yunmu YMBot D2', 342: 'Yunmu YMBot D4', 349: 'PsiBot ψ-SynRobot',
}}

# A mass no source states, estimated (E) and agreed: number -> (min, mode, max) kg and the basis. The PrimeBOT Q1:
# the Booster K1's 19.5 kg, the robot nearest in height (0.95 against 0.88 m) with a mass from its maker, half to 1.5
# times (Matthias, 2026-10-29: "I agree with the proposal of E5.17 ...", point 6).
MASS_ESTIMATES = {236: (9.75, 19.5, 29.25, "E: the Booster K1's 19.5 kg, half to 1.5 times (EVIDENCE.md E5.17)")}

# The decisions, one per robot: (number, types, form, entry, decided in). Types: "4" or "3, 4", the leading one first,
# empty where the entry says why there are none. Form: how the robot moves, as read (EVIDENCE.md E4.1 to E4.10).
DECISIONS = [
    (1, '4', 'no wheels named', '', 'E4.1'),
    (2, '', 'no wheels named', 'the same robot as 3', 'E4.1'),
    (3, '3, 4', 'legs or wheels', '', 'E4.1, E4.6'),
    (4, '3', 'no wheels named', '', 'E4.1'),
    (5, '3, 4', 'legs or wheels', '', 'E4.1, E4.6'),
    (6, '4', 'no wheels named', '', 'E4.1'),
    (7, '3, 4', 'no wheels named', '', 'E4.1, E4.6'),
    (8, '4', 'no wheels named', '', 'E4.1'),
    (9, '4', 'wheels', '', 'E4.1'),
    (10, '3, 4', 'no wheels named', '', 'E4.1, E4.6'),
    (11, '3, 4', 'legs', '', 'E4.1, E4.6'),
    (12, '3', 'legs or wheels', '', 'E4.1'),
    (13, '3, 2', 'wheels', '', 'E4.1, E4.6'),
    (14, '4', 'legs', '', 'E4.1'),
    (15, '2, 3', 'wheels', '', 'E4.1, E4.6'),
    (16, '1', 'legs', '', 'E4.1'),
    (17, '4, 3', 'legs', '', 'E4.1, E4.6'),
    (18, '3', 'legs', '', 'E4.1'),
    (19, '1', 'legs', '', 'E4.1'),
    (20, '3, 2', 'wheels', '', 'E4.1, E4.6'),
    (21, '3, 2', 'wheels', '', 'E4.1, E4.6'),
    (22, '3, 4', 'legs', '', 'E4.1, E4.6'),
    (23, '3, 1', 'legs', '', 'E4.1, E4.6'),
    (24, '6', 'legs', '', 'E4.1'),
    (25, '2', 'no wheels named', '', 'E4.1'),
    (26, '3', 'wheels', '', 'E4.1'),
    (27, '', 'an upper body', 'not assigned: an upper body only', 'E4.1'),
    (28, '3', 'not stated', '', 'E4.1'),
    (29, '3, 4', 'wheels', '', 'E4.1, E4.6'),
    (30, '', 'two arms', 'not assigned: arms only', 'E4.1, E4.10'),
    (31, '3', 'wheels', '', 'E4.1'),
    (32, '3', 'no wheels named', '', 'E4.1'),
    (33, '3, 4', 'legs or wheels', '', 'E4.1, E4.6'),
    (34, '4, 2', 'wheels', '', 'E4.1, E4.6'),
    (35, '4, 2', 'wheels', '', 'E4.1, E4.6'),
    (36, '', 'no wheels named', 'the same robot as 37', 'E4.1'),
    (37, '1', 'no wheels named', '', 'E4.1'),
    (38, '1', 'no wheels named', '', 'E4.1'),
    (39, '', 'an upper body', 'not assigned: an upper body only', 'E4.1, E4.10'),
    (40, '2, 3', 'wheels', '', 'E4.1, E4.6, E7.3'),      # its maker's pictures: a wheeled base
    (41, '2, 3', 'wheels', '', 'E4.1, E4.6'),
    (42, '3, 2', 'wheels', '', 'E4.1, E4.6'),
    (43, '5, 3', 'legs', '', 'E4.1, E4.6'),
    (44, '5', 'legs', '', 'E4.1'),
    (45, '4, 3', 'legs', '', 'E4.1, E4.6'),
    (46, '4', 'legs', '', 'E4.1'),
    (47, '2', 'legs', '', 'E4.1'),
    (48, '3', 'not stated', '', 'E4.1'),
    (49, '2', 'wheels', '', 'E4.1'),
    (50, '', 'two arms', 'not assigned: arms only', 'E4.1'),
    (51, '3', 'wheels', '', 'E4.2'),
    (52, '', 'two arms and a torso', 'not assigned: an upper body only', 'E4.2, E4.10'),
    (53, '2', 'legs', '', 'E4.2'),
    (54, '1', 'no wheels named', '', 'E4.2'),
    (55, '1', 'no wheels named', '', 'E4.2'),
    (56, '3', 'legs or wheels', '', 'E4.2'),
    (57, '4, 1', 'no wheels named', '', 'E4.2, E4.6'),
    (58, '3', 'no wheels named', '', 'E4.2'),
    (59, '4', 'legs', '', 'E4.2'),
    (60, '3, 2', 'wheels', '', 'E4.2, E4.6'),
    (61, '4, 3', 'not stated', '', 'E4.2, E4.6'),
    (62, '3, 4', 'wheels', '', 'E4.2, E4.6'),
    (63, '3, 4', 'legs', '', 'E4.2, E4.6'),
    (64, '4', 'wheels', '', 'E4.2'),
    (65, '4', 'legs', '', 'E4.2'),
    (66, '3, 4', 'wheels', '', 'E4.2, E4.6'),
    (67, '3', 'wheels', '', 'E4.2'),
    (68, '2', 'wheels', '', 'E4.2, E7.3'),               # the press: "a wheeled base instead of legs"
    (69, '2', 'no wheels named', '', 'E4.2'),
    (70, '', 'no wheels named', 'the same robot as 69', 'E4.2'),
    (71, '3, 5', 'legs', '', 'E4.2, E4.6'),
    (72, '3, 5', 'wheels', '', 'E4.2, E4.6'),
    (73, '3, 4', 'not stated', '', 'E4.2, E4.6'),
    (74, '4', 'wheels', '', 'E4.2'),
    (75, '3', 'wheels', '', 'E4.2'),
    (76, '3', 'legs or wheels', '', 'E4.2'),
    (77, '3', 'legs', '', 'E4.2'),
    (78, '3', 'no wheels named', '', 'E4.2'),
    (79, '4', 'legs', '', 'E4.2'),
    (80, '2', 'no wheels named', '', 'E4.2'),
    (81, '5, 3', 'no wheels named', '', 'E4.2, E4.6'),
    (82, '2, 3', 'wheels', '', 'E4.2, E4.6'),
    (83, '3', 'wheels', '', 'E4.2'),
    (84, '3, 4', 'wheels', '', 'E4.2, E4.6'),
    (85, '1, 4', 'legs', '', 'E4.2, E4.6'),
    (86, '4, 2', 'wheels', '', 'E4.2, E4.6'),
    (87, '', 'an upper body', 'not assigned: an upper body only', 'E4.2'),
    (88, '3, 4', 'legs', '', 'E4.2, E4.6'),
    (89, '3', 'wheels', '', 'E4.2'),
    (90, '3, 4', 'wheels', '', 'E4.2, E4.6'),
    (91, '4', 'wheels', '', 'E4.2'),
    (92, '2, 3', 'wheels', '', 'E4.2, E4.6'),
    (93, '3', 'legs', '', 'E4.2'),
    (94, '4', 'not stated', '', 'E4.2'),
    (95, '4', 'not stated', '', 'E4.2'),
    (96, '', 'legs or wheels', 'not assigned: below 15 kg', 'E4.2, E4.11'),
    (97, '3', 'no wheels named', '', 'E4.2'),
    (98, '2, 3', 'no wheels named', '', 'E4.2, E4.6'),
    (99, '4', 'wheels', '', 'E4.2'),
    (100, '3', 'wheels', '', 'E4.2'),
    (101, '4', 'not stated', '', 'E4.3'),
    (102, '1, 3', 'legs', '', 'E4.3, E4.6'),
    (103, '1, 3', 'no wheels named', '', 'E4.3, E4.6'),
    (104, '2', 'wheels', '', 'E4.3'),
    (105, '3, 2', 'wheels', '', 'E4.3, E4.6'),
    (106, '3', 'wheels', '', 'E4.3'),
    (107, '3', 'wheels', '', 'E4.3'),
    (108, '3', 'legs', '', 'E4.3'),
    (109, '3', 'not stated', '', 'E4.3'),
    (110, '3', 'not stated', '', 'E4.3, E4.6'),
    (111, '3', 'not stated', '', 'E4.3'),
    (112, '3, 4', 'wheels', '', 'E4.3, E4.6'),
    (113, '3', 'wheels', '', 'E4.3'),
    (114, '3, 4', 'wheels', '', 'E4.3, E4.6'),
    (115, '3, 4', 'wheels', '', 'E4.3, E4.6'),
    (116, '2', 'legs', '', 'E4.3'),
    (117, '2', 'no wheels named', '', 'E4.3'),
    (118, '4', 'no wheels named', '', 'E4.3'),
    (119, '2', 'no wheels named', '', 'E4.3'),
    (120, '2, 3', 'legs', '', 'E4.3, E4.6'),
    (121, '2', 'legs', '', 'E4.3'),
    (122, '2', 'wheels', '', 'E4.3'),
    (123, '2', 'no wheels named', '', 'E4.3'),
    (124, '3', 'four arms, no legs', '', 'E4.3, E4.10'),
    (125, '4', 'wheels', '', 'E4.3'),
    (126, '', 'legs', 'the same robot as 127', 'E4.3'),
    (127, '3', 'legs', '', 'E4.3'),
    (128, '', 'an upper body', 'not assigned: an upper body only', 'E4.3, E4.10'),
    (129, '4', 'wheels', '', 'E4.3'),
    (130, '4', 'not stated', '', 'E4.3'),
    (131, '4', 'legs', '', 'E4.3'),
    (132, '2', 'legs', '', 'E4.3'),
    (133, '3', 'wheels', '', 'E4.3'),
    (134, '2, 3', 'legs', '', 'E4.3, E4.6'),
    (135, '2, 3', 'not stated', '', 'E4.3, E4.6'),
    (136, '4, 3', 'not stated', '', 'E4.3, E4.6'),
    (137, '3, 4', 'not stated', '', 'E4.3, E4.6'),
    (138, '', 'an upper body', 'not assigned: an upper body only', 'E4.3'),
    (139, '4', 'wheels', '', 'E4.3'),
    (140, '', 'legs', 'the same robot as 121', 'E4.3'),
    (141, '3, 4', 'not stated', '', 'E4.3, E4.6'),
    (142, '3', 'wheels', '', 'E4.3'),
    (143, '4, 1', 'no wheels named', '', 'E4.3, E4.6'),
    (144, '2, 4', 'legs', '', 'E4.3, E4.6'),
    (145, '4', 'wheels', '', 'E4.3'),
    (146, '3, 4', 'not stated', '', 'E4.3, E4.6'),
    (147, '1', 'not stated', '', 'E4.3'),
    (148, '1', 'no wheels named', '', 'E4.3'),
    (149, '', 'not stated', 'the same robot as 158', 'E4.3'),
    (150, '4, 3', 'not stated', '', 'E4.3, E4.6'),
    (151, '2', 'legs', '', 'E4.4'),
    (152, '3, 5', 'legs', '', 'E4.4, E4.6'),
    (153, '2', 'legs', '', 'E4.4'),
    (154, '3, 4', 'legs', '', 'E4.4, E4.6'),
    (155, '4, 3', 'not stated', '', 'E4.4, E4.6'),
    (156, '3, 4', 'legs', '', 'E4.4, E4.6'),
    (157, '2, 3', 'not stated', '', 'E4.4, E4.6'),
    (158, '3, 2', 'not stated', '', 'E4.4, E4.6'),
    (159, '', 'wheels', 'the same robot as 160', 'E4.4'),
    (160, '3', 'wheels', '', 'E4.4'),
    (161, '4', 'wheels', '', 'E4.4'),
    (162, '4, 3', 'wheels', '', 'E4.4, E4.6'),
    (163, '2, 3', 'legs or wheels', '', 'E4.4, E4.6'),
    (164, '4', 'not stated', '', 'E4.4'),
    (165, '3', 'wheels', '', 'E4.4'),
    (166, '4', 'legs', '', 'E4.4'),
    (167, '3', 'legs', '', 'E4.4'),
    (168, '1', 'legs', '', 'E4.4'),
    (169, '', 'legs', 'the same robot as 170', 'E4.4'),
    (170, '2, 3', 'legs', '', 'E4.4, E4.6'),
    (171, '2', 'not stated', '', 'E4.4'),
    (172, '', 'an arm', 'not assigned: arms only', 'E4.4'),
    (173, '4', 'not stated', '', 'E4.4'),
    (174, '4', 'not stated', '', 'E4.4'),
    (175, '4, 1', 'legs', '', 'E4.4, E4.6'),
    (176, '4, 2', 'not stated', '', 'E4.4, E4.6'),
    (177, '2', 'not stated', '', 'E4.4'),
    (178, '4', 'not stated', '', 'E4.4'),
    (179, '3, 2', 'wheels', '', 'E4.4, E4.6'),
    (180, '2, 3', 'legs', '', 'E4.4, E4.6'),
    (181, '3, 4', 'not stated', '', 'E4.4, E4.6'),
    (182, '4', 'not stated', '', 'E4.4'),
    (183, '4, 3', 'wheels', '', 'E4.4, E4.6'),
    (184, '2, 3', 'wheels', '', 'E4.4, E4.6'),
    (185, '4, 3', 'legs', '', 'E4.4, E4.6'),
    (186, '3', 'legs', '', 'E4.4'),
    (187, '3, 4', 'legs', '', 'E4.4, E4.6'),
    (188, '4', 'wheels', '', 'E4.4'),
    (189, '3, 4', 'not stated', '', 'E4.4, E4.6'),
    (190, '3', 'not stated', '', 'E4.4'),
    (191, '5', 'not stated', '', 'E4.4'),
    (192, '', 'two arms', 'not assigned: arms only', 'E4.4, E4.10'),
    (193, '3', 'wheels', '', 'E4.4'),
    (194, '4', 'a ball', '', 'E4.4'),
    (195, '3, 5', 'not stated', '', 'E4.4, E4.6'),
    (196, '', 'not stated', 'the same robot as 195', 'E4.4'),
    (197, '3', 'wheels', '', 'E4.4'),
    (198, '4', 'legs', '', 'E4.4'),
    (199, '2, 3', 'legs', '', 'E4.4, E4.6'),
    (200, '2, 4', 'wheels', '', 'E4.4, E4.6, E7.3'),     # its maker: "全向轮式底盘", an omnidirectional wheeled chassis
    (201, '4', 'legs', '', 'E4.5'),
    (202, '6', 'legs', '', 'E4.5'),
    (203, '2', 'legs', '', 'E4.5'),
    (204, '3', 'legs', '', 'E4.5'),
    (205, '4', 'not stated', '', 'E4.5'),
    (206, '4, 3', 'not stated', '', 'E4.5, E4.6'),
    (207, '4', 'not stated', '', 'E4.5'),
    (208, '5, 3', 'not stated', '', 'E4.5, E4.6'),
    (209, '3, 4', 'wheels', '', 'E4.5, E4.6'),
    (210, '2', 'legs', '', 'E4.5'),
    (211, '4', 'legs', '', 'E4.5'),
    (212, '1', 'wheels', '', 'E4.5'),
    (213, '3, 4', 'wheels', '', 'E4.5, E4.6'),
    (214, '3, 4', 'not stated', '', 'E4.5, E4.6'),
    (215, '3', 'wheels', '', 'E4.5'),
    (216, '2, 3', 'legs', '', 'E4.5, E4.6'),
    (217, '4', 'not stated', '', 'E4.5'),
    (218, '', 'two arms', 'not assigned: arms only', 'E4.5'),
    (219, '', 'an upper body', 'not assigned: an upper body only', 'E4.5'),
    (220, '', 'not stated', 'the same robot as 222', 'E4.5'),
    (221, '2, 3', 'no wheels named', '', 'E4.5, E4.6'),
    (222, '2', 'no wheels named', '', 'E4.5'),
    (223, '2, 3', 'legs', '', 'E4.5, E4.6'),
    (224, '2', 'legs', '', 'E4.5'),
    (225, '', 'an upper body', 'not assigned: an upper body only', 'E4.5'),
    (226, '3', 'not stated', '', 'E4.5'),
    (227, '3', 'wheels', '', 'E4.5'),
    (228, '6, 3', 'not stated', '', 'E4.5, E4.6'),
    (229, '2, 3', 'not stated', '', 'E4.5, E4.6'),
    (230, '2, 3', 'wheels', '', 'E4.5, E4.6'),
    (231, '1', 'not stated', '', 'E4.5'),
    (232, '2, 3', 'not stated', '', 'E4.5, E4.6'),
    (233, '', 'an upper body', 'not assigned: an upper body only', 'E4.5, E4.10'),
    (234, '1', 'legs', '', 'E4.5'),
    (235, '', 'not stated', 'not assigned: not found at its maker', 'E4.5, E4.10'),
    (236, '4, 1', 'not stated', '', 'E4.5, E4.6'),
    (237, '4', 'wheels', '', 'E4.5'),
    (238, '4', 'legs', '', 'E4.5'),
    (239, '3', 'not stated', '', 'E4.5'),
    (240, '4, 3', 'wheels', '', 'E4.5, E4.6'),
    (241, '3', 'legs', '', 'E4.5'),
    (242, '3, 4', 'legs', '', 'E4.5, E4.6'),
    (243, '', 'an upper body', 'not assigned: an upper body only', 'E4.5, E4.10'),
    (244, '2', 'legs', '', 'E4.5'),
    (245, '3, 4', 'wheels', '', 'E4.5, E4.6'),
    (246, '1', 'not stated', '', 'E4.5'),
    (247, '2, 3', 'wheels', '', 'E4.5, E4.6'),
    (248, '2', 'wheels', '', 'E4.5'),
    (249, '3', 'legs', '', 'E4.5'),
    (250, '3', 'legs', '', 'E4.5'),
    (251, '3, 2', 'wheels', '', 'E4.7'),
    (252, '2', 'wheels', '', 'E4.7, E4.10'),
    (253, '2, 3', 'wheels', '', 'E4.7'),
    (254, '4, 2', 'wheels', '', 'E4.7'),
    (255, '3, 2', 'wheels', '', 'E4.7'),
    (256, '2', 'legs', '', 'E4.7'),
    (257, '3', 'wheels', '', 'E4.7'),
    (258, '3, 4', 'wheels', '', 'E4.7'),
    (259, '4', 'not stated', '', 'E4.7'),
    (260, '1', 'not stated', '', 'E4.7'),
    (261, '4', 'wheels', '', 'E4.7'),
    (262, '3', 'not stated', '', 'E4.7'),
    (263, '3', 'wheels', '', 'E4.7'),
    (264, '3', 'not stated', '', 'E4.7'),
    (265, '3, 2', 'legs', '', 'E4.7'),
    (266, '', 'an upper body', 'not assigned: an upper body only', 'E4.7'),
    (267, '4', 'wheels', '', 'E4.7'),
    (268, '1', 'legs', '', 'E4.7'),
    (269, '1', 'legs', '', 'E4.7'),
    (270, '4', 'not stated', '', 'E4.7'),
    (271, '2', 'not stated', '', 'E4.7'),
    (272, '2, 4', 'not stated', '', 'E4.7'),
    (273, '3', 'wheels', '', 'E4.7'),
    (274, '3', 'legs', '', 'E4.7'),
    (275, '3, 4', 'not stated', '', 'E4.7'),
    (276, '3, 2', 'legs', '', 'E4.7'),
    (277, '4', 'wheels', '', 'E4.7'),
    (278, '3', 'wheels', '', 'E4.7'),
    (279, '1, 4', 'legs', '', 'E4.7'),
    (280, '3, 4', 'legs', '', 'E4.7'),
    (281, '1', 'legs', '', 'E4.7'),
    (282, '4', 'wheels', '', 'E4.7'),
    (283, '4', 'wheels', '', 'E4.7'),
    (284, '4', 'not stated', '', 'E4.7'),
    (285, '2', 'legs', '', 'E4.7'),
    (286, '4', 'legs', '', 'E4.7, E4.10'),
    (287, '3', 'not stated', '', 'E4.7'),
    (288, '5, 6', 'no wheels named', '', 'E4.7'),
    (289, '4, 3', 'wheels', '', 'E4.7'),
    (290, '2', 'legs', '', 'E4.7'),
    (291, '4, 3', 'not stated', '', 'E4.7'),
    (292, '3', 'not stated', '', 'E4.7'),
    (293, '4', 'not stated', '', 'E4.7'),
    (294, '2, 3', 'legs', '', 'E4.7'),
    (295, '2, 3', 'wheels', '', 'E4.7'),
    (296, '3, 4', 'not stated', '', 'E4.7'),
    (297, '2', 'legs', '', 'E4.7'),
    (298, '4, 2', 'not stated', '', 'E4.7'),
    (299, '2', 'legs', '', 'E4.7'),
    (300, '2', 'legs', '', 'E4.7'),
    (301, '3, 5', 'wheels', '', 'E4.8'),
    (302, '2', 'legs', '', 'E4.8'),
    (303, '3', 'wheels', '', 'E4.8'),
    (304, '4', 'not stated', '', 'E4.8'),
    (305, '3, 4', 'wheels', '', 'E4.8'),
    (306, '3, 4', 'not stated', '', 'E4.8'),
    (307, '3, 2', 'wheels', '', 'E4.8, E8.2'),           # its maker: "omni-directional mobile base"
    (308, '1', 'not stated', '', 'E4.8'),
    (309, '', 'legs or wheels', 'not assigned: no form with legs and arms', 'E4.8, E5.15, E5.17'),
    (310, '4', 'not stated', '', 'E4.8'),
    (311, '1', 'legs', '', 'E4.8'),
    (312, '2, 3', 'wheels', '', 'E4.8, E8.2'),           # its maker: "Dual-wheel differential motor"
    (313, '2, 3', 'wheels', '', 'E4.8, E8.2'),           # its maker: "Four-wheel omnidirectional wheel"
    (314, '3, 2', 'wheels', '', 'E4.8'),
    (315, '2', 'wheels', '', 'E4.8, E4.10'),
    (316, '3, 4', 'not stated', '', 'E4.8'),
    (317, '4', 'legs', '', 'E4.8'),
    (318, '2', 'wheels', '', 'E4.8'),
    (319, '3, 4', 'wheels', '', 'E4.8'),
    (320, '3', 'wheels', '', 'E4.8'),
    (321, '4, 3', 'not stated', '', 'E4.8'),
    (322, '4', 'not stated', '', 'E4.8'),
    (323, '4, 2', 'legs', '', 'E4.8'),
    (324, '4', 'not stated', '', 'E4.8'),
    (325, '3', 'legs', '', 'E4.8'),
    (326, '2', 'legs', '', 'E4.8'),
    (327, '3', 'legs', '', 'E4.8'),
    (328, '4, 3', 'legs', '', 'E4.8'),
    (329, '2', 'not stated', '', 'E4.8'),
    (330, '4, 3', 'legs', '', 'E4.8'),
    (331, '4', 'wheels', '', 'E4.8'),
    (332, '1, 3', 'not stated', '', 'E4.8'),
    (333, '4', 'not stated', '', 'E4.8'),
    (334, '4, 3', 'legs', '', 'E4.8'),
    (335, '3, 2', 'wheels', '', 'E4.8'),
    (336, '2, 4', 'wheels', '', 'E4.8'),
    (337, '3, 2', 'wheels', '', 'E4.8'),
    (338, '', 'an upper body', 'not assigned: an upper body only', 'E4.8'),
    (339, '4', 'legs', '', 'E4.8'),
    (340, '3, 2', 'wheels', '', 'E4.8'),
    (341, '3, 2', 'wheels', '', 'E4.8'),
    (342, '3, 2', 'wheels', '', 'E4.8'),
    (343, '1', 'legs', '', 'E4.8'),
    (344, '4', 'wheels', '', 'E4.8'),
    (345, '4', 'legs', '', 'E4.8'),
    (346, '4, 3', 'wheels', '', 'E4.8'),
    (347, '4, 3', 'legs', '', 'E4.8'),
    (348, '3', 'not stated', '', 'E4.8'),
    (349, '3, 2', 'wheels', '', 'E4.8'),
    (350, '1', 'legs', '', 'E4.11'),
    (351, '6', 'not stated', '', 'E4.11'),
    (352, '2, 5', 'legs', '', 'E4.11'),
    (353, '3', 'legs', '', 'E4.11'),
    (354, '3', 'wheels', '', 'E4.11'),
]

# Masses: a stated mass +- this many kg (as the X1's and N1's own masses, EVIDENCE.md E2.8e).
MASS_SPREAD_KG = 1.0


def mass_bounds(stated: str) -> tuple:
    """The minimum, mode and maximum of a stated mass, kg, and how they were made: a range as it is (its middle the
    mode), one mass +- MASS_SPREAD_KG; where two masses are given ("43, 73"), the larger (the smaller is another
    robot's, EVIDENCE.md E4.11); (None, None, None, '') where none is stated."""
    text = stated.replace('kg', '').replace('~', '').strip()
    if ',' in text:
        text = max(text.split(','), key=lambda v: float(re.match(r'\s*([\d.]+)', v).group(1))).strip()
        basis = 'the larger of the two masses stated, +- 1 kg'
    else:
        basis = 'the stated mass +- 1 kg'
    span = re.match(r'([\d.]+)\s*[\u2013-]\s*([\d.]+)', text)
    if span:
        low, high = float(span.group(1)), float(span.group(2))
        return low, (low + high) / 2, high, 'the stated range, its middle the mode'
    one = re.match(r'([\d.]+)', text)
    if one:
        mode = float(one.group(1))
        return round(max(mode - MASS_SPREAD_KG, 0.0), 3), mode, round(mode + MASS_SPREAD_KG, 3), basis
    return None, None, None, ''


def read_catalogue(path: str) -> dict:
    """The catalogue's robots: number -> (robot, maker, country, status, height, mass as stated, source)."""
    sheet = openpyxl.load_workbook(path, read_only=True, data_only=True)['Catalogue']
    rows = list(sheet.iter_rows(values_only=True))
    at = {name: k for k, name in enumerate(rows[0])}
    text = lambda v: '' if v is None else str(v).strip()   # noqa: E731
    return {int(r[at['Number']]): (text(r[at['Robot']]), text(r[at['Maker']]), text(r[at['Country']]),
                                   text(r[at['Status']]), text(r[at['Height (cm)']]), text(r[at['Mass (kg)']]),
                                   text(r[at['Page']]))
            for r in rows[1:] if r[at['Number']] is not None}


def taken_apart_as(number: int) -> str:
    """The name (or names) of a robot's own rows in its type's parts file, '' where it is not taken apart. One robot
    taken apart in two types' files is not foreseen: it stops the building."""
    names = [by_number[number] for by_number in TAKEN_APART.values() if number in by_number]
    if len(names) > 1:
        raise ValueError(f'robot {number} is taken apart in more than one robot type: {names}.')
    return names[0] if names else ''


def register_rows(catalogue: dict) -> list:
    """One row per robot, in the order of HEADINGS."""
    robots = {**catalogue, **ADDED}
    out = []
    for number, types, form, entry, decided in DECISIONS:
        robot, maker, country, status, height, mass, source = robots[number]
        low, mode, high, basis = mass_bounds(mass)
        if number in MASS_ESTIMATES:      # no mass stated anywhere: the agreed estimate (E)
            low, mode, high, basis = MASS_ESTIMATES[number]
        out.append([number, robot, maker, country, status, height, mass, low, mode, high, basis, types, form, entry,
                    taken_apart_as(number), decided, source])
    return out


def types_of(row: list) -> list:
    """The robot types of one row of the register, as numbers ('3, 1' -> [3, 1]; empty for a robot without)."""
    return [int(t) for t in (piece.strip() for piece in row[HEADINGS.index('Types')].split(',')) if t]


def in_the_run(row: list, robot_type: int, any_apart: bool) -> str:
    """What 02_composition.py does with a robot of `robot_type` (its row of the register), `any_apart` whether any
    robot of the type is taken apart: drawn with its own rows of the type's parts file, where it has them (every robot
    of type 1 since 2026-10-29); while none of its type is taken apart, its type drawn from the workbook; else not drawn
    where no mass is stated, and not drawn where it is not yet taken apart (2026-10-30, Q4)."""
    if row[0] in TAKEN_APART.get(robot_type, {}):
        return IN_RUN_OWN
    if not any_apart:
        return IN_RUN_WORKBOOK
    return IN_RUN_NOT if row[HEADINGS.index('Mass mode (kg)')] in (None, '') else IN_RUN_LATER


def type_rows(rows: list, robot_type: int) -> list:
    """The rows of the sheet of `robot_type`: every robot of the register whose types include it, in the register's
    order, each its row of the sheet Robots and what the run does with it."""
    of_type = [row for row in rows if robot_type in types_of(row)]
    any_apart = any(row[0] in TAKEN_APART.get(robot_type, {}) for row in of_type)
    return [row + [in_the_run(row, robot_type, any_apart)] for row in of_type]


def write_sheet(sheet, headings: list, rows: list, widths: list) -> None:
    """One sheet of robots: its headings in bold on grey, its rows, its column widths, the first two columns frozen."""
    sheet.append(headings)
    for cell in sheet[1]:
        cell.font = Font(bold=True)
        cell.fill = HEADING_FILL
    for row in rows:
        sheet.append(row)
    for k, width in enumerate(widths, 1):
        sheet.column_dimensions[openpyxl.utils.get_column_letter(k)].width = width
    sheet.freeze_panes = 'C2'


def build(path: str, params: Params) -> dict:
    """Write the register to `path`: the sheets About, Robots (every robot) and a sheet Type n for each type of
    TYPES_LISTED (every robot of that type). Returns the number of robots of each listed type."""
    book = openpyxl.Workbook()
    about = book.active
    about.title = 'About'
    for line in ABOUT:
        about.append([line])
        about.cell(about.max_row, 1).alignment = Alignment(wrap_text=True, vertical='top')
    about['A1'].font = Font(bold=True, size=13)
    about.column_dimensions['A'].width = ABOUT_WIDTH
    rows = register_rows(read_catalogue(absolute(params.data.humanoid_guide)))
    write_sheet(book.create_sheet('Robots'), HEADINGS, rows, WIDTHS)
    # The same robots' rows again, those of each listed type, with what the run does with each: one list of decisions.
    counts = {}
    for robot_type in TYPES_LISTED:
        listed = type_rows(rows, robot_type)
        write_sheet(book.create_sheet(TYPE_SHEET.format(robot_type)), HEADINGS + ['In the run'], listed,
                    WIDTHS + [IN_RUN_WIDTH])
        counts[robot_type] = len(listed)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    book.save(path)
    return counts


def output_path(params: Params) -> str:
    """Where the register goes: 00's setting `data.register`."""
    return absolute(params.data.register)


def main() -> int:
    """Press Run: build the register from 00's settings."""
    params = current()
    path = output_path(params)
    counts = build(path, params)
    listed = '; '.join(f'{n} of robot type {t} also in the sheet {TYPE_SHEET.format(t)}' for t, n in counts.items())
    print(f'{len(DECISIONS)} robots written to {params.data.register}, sheet Robots; {listed}.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
