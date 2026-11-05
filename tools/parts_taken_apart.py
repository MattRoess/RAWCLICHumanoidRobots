"""
The shared part of the builders of the parts files: what every robot type taken apart is written with.

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

Matthias, 2026-10-30: "Yes, build C" (documentation/claude/HANDOVER.md, C: "a parts file and builder per type, 02
drawing each type the same way"; Q1: each type in a folder of its own, the shared machinery here; "One copy of the
code").

WHAT IT HOLDS
-------------
The one copy of what the builders of every robot type share: the sheets' first rows and column widths; the sheets
that are one set for all robots (MagnetGrades, the magnets' grade classes by heat; JointParts, the G1's joint
weighed part by part, which every joint is scaled from; Shares, the materials of the parts and components that hold
more than one); the shared numbers of the sheet Constants and the sources they cite; the template's sizes and
masses where a source names a board or sensor but gives none (EVIDENCE.md E5.14); and the functions that write a
robot's block into its rows and the rows into a file. Each robot type's builder, tools/<n>_<name>/
make_parts_taken_apart.py, holds its own robots and calls these.

WHAT IT READS AND WRITES
------------------------
It reads nothing but 00's settings (src/params_schema.py, for where a file goes). It writes a file only when a
type's builder calls build(): `data.parts_taken_apart` with that type's folder (data/researched/<n>_<name>/
parts_taken_apart.xlsx, git-ignored).

WHERE IT SITS
-------------
Not a stage and not run by itself: the builders in tools/<n>_<name>/ import it. Importing it writes nothing.
"""
import os
import re
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


# --- The sheets' first rows and column widths --------------------------------------------------------------------
# The first row of every sheet and its columns' widths, the same in every robot type's file (01_schemas.py reads
# them by these headings, APART_SHEETS).
ROBOTS_HEADINGS = ['Robot', 'Maker', 'Type', 'Height (m)', 'Stated mass (kg)', 'Sources']
ROBOTS_WIDTHS = [14, 10, 6, 10, 14, 60]
JOINTS_HEADINGS = ['Robot', 'Number', 'Joint', 'Joints in the robot', 'Module', 'Torque limit (N·m)',
                   'Module mass, min (kg)', 'mode (kg)', 'max (kg)', 'Share of the joint modules', 'Cooling',
                   'Heat group', 'Body region', 'Sources', 'Basis']
JOINTS_WIDTHS = [12, 8, 22, 10, 9, 10, 10, 9, 9, 12, 30, 18, 11, 50, 70]
PARTS_HEADINGS = ['Robot', 'Part', 'Number in the robot', "Kind (the figure's row)", 'Body region',
                  'Mass of one, min (kg)', 'mode (kg)', 'max (kg)', 'Material (one material only)', 'Grade',
                  'Remainder of, or computed from', 'Label', 'Sources']
PARTS_WIDTHS = [12, 44, 10, 20, 16, 11, 9, 9, 18, 14, 52, 7, 56]
BOARDS_HEADINGS = ['Robot', 'Board', 'Number in the robot', "Kind (the figure's row)", 'Body region',
                   'Area of one, min (cm2)', 'mode (cm2)', 'max (cm2)', 'Mass from',
                   'Car board category (RAWCLICVehicleElectronics 04_)', 'Label', 'Sources']
BOARDS_WIDTHS = [12, 50, 10, 20, 16, 11, 9, 9, 52, 18, 7, 46]
SENSORS_HEADINGS = ['Robot', 'Sensor', 'Number in the robot', "Kind (the figure's row)", 'Body region',
                    'Mass of one, min (g)', 'mode (g)', 'max (g)', 'Label', 'Sources']
SENSORS_WIDTHS = [12, 40, 10, 20, 16, 11, 9, 9, 7, 52]
SENSORELEMENTS_HEADINGS = ['Sensor', 'Car sensor type (RAWCLICVehicleElectronics 07_, sheet Sensor Details)',
                           'Units in one sensor']
SENSORELEMENTS_WIDTHS = [40, 50, 12]
CONSTANTS_HEADINGS = ['Robot', 'Quantity', 'Min', 'Mode', 'Max', 'Unit', 'Label', 'Source']
CONSTANTS_WIDTHS = [12, 48, 9, 9, 9, 8, 7, 70]
SOURCES_HEADINGS = ['Code', 'Source', 'Link', 'What it is']
SOURCES_WIDTHS = [12, 70, 90, 50]
MAGNETGRADES_WIDTHS = [18, 12, 12, 7, 90]
JOINTPARTS_WIDTHS = [44, 12, 12, 9, 9, 16, 12, 10, 9, 9, 60, 14, 60]
SHARES_WIDTHS = [52, 18, 22, 10, 10, 10, 10, 7, 90]

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
    ('Driver board', 12.8, 0.5, 1, 1.5, 'Boards and components', None, 1.78, 3.56, 5.33,
     'one, two or three boards of the larger size (T3k: "a stack")', 'W; E for the spread and the factor',
     'T1 slide 43 (figure 37); factors EVIDENCE.md E2.8; Matthias, 2026-10-27, step 1: '
     '"Accept all" (EVIDENCE.md E2.8)'),
    ('Two small bearings', 11, 0.5, 1, 1.5, 'Steel', 'GCr15', 1, 1.78, 2.67, 'the area',
     'W; E for the spread and the factor',
     'T1 slide 43 (figure 37); factors EVIDENCE.md E2.8; Matthias, 2026-10-27, step 1: '
     '"Accept all" (EVIDENCE.md E2.8)'),
    ('Housing', 79.3, 0.5, 1, 1.5, 'Aluminium alloys', None, 1, 1.39, 2.09, "the joint's surface",
     'W; E for the spread and the factor',
     'T1 slide 43 (figure 37); factors EVIDENCE.md E2.8; Matthias, 2026-10-27, step 1: '
     '"Accept all" (EVIDENCE.md E2.8)'),
    ('Two end caps', 23.7, 0.5, 1, 1.5, 'Aluminium alloys', None, 1, 1.78, 2.67, 'the area',
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
     'The winding: measured car traction motors 23-29 % (Drexler 2025), car auxiliary motors 27 / 36 / 45 %; '
     'E2.10; Matthias: "Yes use this numberrs"'),
    ('Motor stator', 'Plastics', None, 0.02, 0.05, 0.1, None, 'E', "The winding's coating: E2.8"),
    ('Motor stator', 'Electrical steel', 'M19 or M27', None, None, None, 'Yes', 'E',
     'The electrical steel: Matthias, 2026-10-27, step 1: "Accept all" (EVIDENCE.md E2.8); its grade E5.18'),
    ('Motor rotor', 'NdFeB magnets', None, 0.45, 0.9, 1, None, 'E',
     'T1 calls it "磁钢"; Matthias, 2026-10-27, step 1: "Accept all" (EVIDENCE.md E2.8)'),
    ('Motor rotor', 'Electrical steel', 'M19 or M27', None, None, None, 'Yes', 'E',
     'Matthias, 2026-10-27, step 1: "Accept all" (EVIDENCE.md E2.8); its grade E5.18'),
    ('Magnet carrier', 'Plastics', None, 0.05, 0.15, 0.3, None, 'E', 'The plastic bearing: T1 "铝+塑料轴承"'),
    ('Magnet carrier', 'Aluminium alloys', None, None, None, None, 'Yes', 'E',
     'Matthias, 2026-10-27, step 1: "Accept all" (EVIDENCE.md E2.8)'),
    ('Gear stage 2, planets, carrier and crossed roller bearing', 'Aluminium alloys', None, 0.125, 0.25, 0.4, None, 'E',
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
    ('XT30 (2+2) connectors (two per joint)', 'Brass', 'Brass', 0.175, 0.35, 0.525, None, 'E',
     'The contacts: E2.8; brass, gold-plated (Amass, through LCSC; E5.22)'),
    ('XT30 (2+2) connectors (two per joint)', 'Plastics', None, None, None, None, 'Yes', 'E', 'The housing: E2.8'),
    ('XT60 connector, mated pair', 'Brass', 'Brass', 0.175, 0.35, 0.525, None, 'E',
     "The contacts, brass, as the XT30's (E5.22)"),
    ('XT60 connector, mated pair', 'Plastics', None, None, None, None, 'Yes', 'E', "The housing, as the XT30's"),
    ('Battery housing, busbars and wires', 'Nickel', 'Nickel strip', 0.01, 0.03, 0.06, None, 'E',
     'The nickel strips between the cells, 0.2 mm thick (sevarg.net, measured), counted with the copper (Matthias, '
     '2026-10-29: "With Copper"); E5.19 point 1'),
    ('Battery housing, busbars and wires', 'Copper', None, 0.05, 0.1, 0.15, None, 'E',
     'The copper wires and busbars: E5.19 point 1'),
    ('Battery housing, busbars and wires', 'Plastics', None, 0.05, 0.1, 0.2, None, 'E',
     'The cell holders, insulation and tape: E5.19 point 1'),
    ('Battery housing, busbars and wires', 'Aluminium alloys or Plastics', None, None, None, None, 'Yes', 'E',
     'The housing: "aluminum or high-impact plastics" (teswaybike.com, a claim), each as often (E5.19 point 1)'),
    ('Battery housing (aluminium), busbars and wires', 'Nickel', 'Nickel strip', 0.01, 0.03, 0.06, None, 'E',
     'The nickel strips between the cells, counted with the copper (Matthias, 2026-10-29: "With Copper"); E5.19 '
     'point 1'),
    ('Battery housing (aluminium), busbars and wires', 'Copper', None, 0.05, 0.1, 0.15, None, 'E',
     'The copper wires and busbars: E5.19 point 1'),
    ('Battery housing (aluminium), busbars and wires', 'Plastics', None, 0.05, 0.1, 0.2, None, 'E',
     'The cell holders, insulation and tape: E5.19 point 1'),
    ('Battery housing (aluminium), busbars and wires', 'Aluminium alloys', None, None, None, None, 'Yes', 'E',
     'The housing: "Aluminum Alloy" (EngineAI, the PM01; E5.6, E5.19 point 1)'),
    ('Frame: aluminium, with steel 45 and P20 parts', 'Steel', 'RP1 frame steel: C45 and P20', 0.1, 0.2, 0.3, None,
     'E', 'The steel parts: 28 of its 112 CNC parts are steel, 24 of steel 45 or AISI 1045 and 4 of P20 (RP1a), by '
     'count only (E5.14 point 9, E5.18)'),
    ('Frame: aluminium, with steel 45 and P20 parts', 'Aluminium alloys', None, None, None, None, 'Yes', 'E',
     'The aluminium parts: AL6061-T6, AL7075, AL5052 (RP1a); E5.14 point 9'),
    # The casters and the lift column of a robot on wheels (EVIDENCE.md E9.6 points 6 and 7, agreed 2026-10-30): no
    # source weighs their parts; the steel's grade the nearest the recipes hold (E).
    ('Casters', 'Steel', 'C45', 0.25, 0.5, 0.75, None, 'E',
     "The housing and fork: Tente's \"light steel sheet\" (1470PAO075P40); half to 1.5 times; C45 the nearest "
     'plain carbon steel of the recipes (E9.6 point 6)'),
    ('Casters', 'Plastics', None, None, None, None, 'Yes', 'E',
     "The wheel's body and tread: polypropylene or polyamide, injected polyurethane (Tente; E9.6 point 6)"),
    ('Lift column: aluminium profile, steel screw and guides', 'Steel', '42CrMo4', 0.15, 0.3, 0.45, None, 'E',
     'Its screw and guides (Oriental Motor\'s EL columns: "Ball Screw", ball splines); E9.6 point 7\'s 20 / 30 / 40 % '
     'widened to half to 1.5 times by the rule for estimates (the entry, E9.8); 42CrMo4 a ball screw\'s steel'),
    ('Lift column: aluminium profile, steel screw and guides', 'Aluminium alloys', None, None, None, None, 'Yes', 'E',
     'Its profile, the remainder (E9.6 point 7)'),
]

# --- The hydraulic robots -------------------------------------------------------------------------------------------
# The hydraulic Atlas (old), Nadia and Neo1 (EVIDENCE.md E27.7; Matthias, 2026-11-04, "Yes, agree E27.7", "Yes, build
# it"): each hydraulic joint an actuator in the row of its place (PLACES, the joints' kinds of the figures); Moog's ISA
# as its servo valve, its board, its sensors and its body, rod and seals, the remainder (point 2); Neo1's digital
# hydraulic actuator by its shares (point 5.3); the power unit, its manifold, the oil and the hoses a kind of their own,
# HYDRAULICS (point 9.7). No source weighs the parts inside an actuator, a valve or a power unit: their materials are
# the sources', their shares estimates, half to 1.5 times the mode.
HYDRAULICS = 'Hydraulics'
# A hydraulic actuator's place: its kind (the figure's row) and its body region.
PLACES = {'hips': ('Hips', 'Legs'), 'knees': ('Knees', 'Legs'), 'ankles': ('Ankles', 'Legs'),
          'waist': ('Waist', 'Torso'), 'arms': ('Arms', 'Arms'), 'head': ('Head', 'Head')}
# Moog's ISA dry, kg, by its version (FRO, Barasuol et al. 2018, Table 2: "Dry weight 920 g 1,600 g"), and its servo
# valve, kg (MOO, Moog's E024 datasheet: "Mass: 95 g (3.35 oz)").
ISA_KG = {'v2': 0.92, 'v5': 1.6}
VALVE_KG = 0.095
# The texts of what a hydraulic row is computed from (its column "Remainder of, or computed from"); 01 and 02 read
# their starts (ACTUATORS_WHOLE, ACTUATOR_REST, OIL_FROM). The actuators of a place are its servo valves, boards,
# sensors and bodies, the bodies their remainder, as a battery pack is its cells, board and housing.
ACTUATORS_STATED = 'its servo valves, boards and sensors, and its bodies, rods and seals (the rows of its place)'
ACTUATOR_BODY = 'the hydraulic actuators, less their servo valves, boards and sensors (the rows of its place)'
OIL_VOLUME = 'Hydraulic oil volume'
OIL_DENSITY = 'Hydraulic oil density'
OIL = f"its volume (Constants' {OIL_VOLUME}) times the oil's density (Constants' {OIL_DENSITY})"
# The share of a motor that is copper, electrical steel and magnets: the G1's weighed small joint (JointParts: the
# stator 94.3 g, 36 % of it copper and 5 % plastics; the rotor 42.9 g, 90 % of it magnets; the magnet carrier 16.9 g),
# 22, 39 and 25 % of its 154.1 g (Claude's arithmetic, E27.7 point 4.4).
MOTOR_SHARES = (('Copper', None, 0.22), ('Electrical steel', 'M19 or M27', 0.39), ('NdFeB magnets', None, 0.25))


def motor_share_rows(item: str, motor: float, magnets: str, why: str) -> list:
    """The copper, electrical steel and magnets of a motor that is `motor` of `item` (a share), each its share of the
    G1's weighed motor times `motor`, half to 1.5 times (E); its magnets of the grade class `magnets` (a part outside
    the joints names its own, 'A or B' each as often)."""
    return [(item, material, magnets if material == 'NdFeB magnets' else grade,
             *(round(f * motor * share, 6) for f in (0.5, 1, 1.5)), None, 'E',
             f"{why}; {share:.0%} of it {material.lower()}, as the G1's weighed motor (JointParts, arith.)")
            for material, grade, share in MOTOR_SHARES]


def hydraulic_share_rows(place: str) -> list:
    """The shares of a place's hydraulic parts (PLACES): Moog's servo valve and the ISA's body, rod and seals, and Neo1's
    digital hydraulic actuator; one set of rows each, by its name with its place."""
    return [
        # The servo valve (E27.7 point 2.2): the materials of the Type 30 it descends from (M30, MOO), no mass of any.
        (f'Servo valves, {place}', 'Copper', None, 0.05, 0.1, 0.15, None, 'E',
         'its torque motor\'s coils (MOO "coils in parallel"; M30 "Motor coils have resilient potting"): no mass '
         'stated (E27.7 point 2.2)'),
        (f'Servo valves, {place}', 'Other', None, 0.1, 0.2, 0.3, None, 'E',
         'its "Polepieces and armature Nickel-iron steel", "Magnets Alnico alloy", "Flexure sleeve Beryllium copper" '
         '(M30): none of the 17 materials (E27.4 question 14)'),
        (f'Servo valves, {place}', 'Aluminium alloys', None, 0.025, 0.05, 0.075, None, 'E',
         'its "Torque motor cover Anodized aluminum alloy" (M30)'),
        (f'Servo valves, {place}', 'Stainless steel', '17-4PH', None, None, None, 'Yes', 'E',
         'its "Body* Stainless steel", end caps, spool and bushing, filter and feedback spring (M30), the remainder; '
         '17-4PH the grade (E)'),
        # The body, rod and seals of Moog's ISA (point 2.5): the remainder of the actuator (ACTUATOR_BODY).
        (f'Actuator bodies, rods and seals, {place}', 'Steel', 'C45', 0.06, 0.12, 0.18, None, 'E',
         'its rod and piston: FRO Table 2\'s 12 mm rod at 120 to 140 mm of steel, 0.12 of 0.825 kg and 0.15 of 1.505 kg '
         '(arith.); C45 the grade (E)'),
        (f'Actuator bodies, rods and seals, {place}', 'Plastics', None, 0.005, 0.01, 0.015, None, 'E',
         'its seals: no source'),
        (f'Actuator bodies, rods and seals, {place}', 'Titanium alloy', 'Ti-6Al-4V', None, None, None, 'Yes', 'S, E',
         'its body: SEM19 "3D-printed Titanium body", the remainder; Ti-6Al-4V the grade (E)'),
        # Neo1's digital hydraulic actuator (point 5.3): its small motor 20 % of it (E), its steel, its seals, its
        # titanium-alloy housing the remainder; no board ("数字液压内部不需要需电子器件检测").
        *motor_share_rows(f'Digital hydraulic actuators, {place}', 0.2, 'H or SH',
                          'its small motor (NEW "小功率电机，伺服或步进电机都行"), 20 % of the actuator (E); H or SH, each '
                          'as often, as the elbows and wrists, the lowest load (E)'),
        (f'Digital hydraulic actuators, {place}', 'Steel', 'C45', 0.15, 0.3, 0.45, None, 'E',
         'its rod, piston and mechanical servo: NEW "液压件是一堆铁" (hydraulic parts are "a pile of iron"); C45 the '
         'grade (E)'),
        (f'Digital hydraulic actuators, {place}', 'Plastics', None, 0.005, 0.01, 0.015, None, 'E',
         'its seals: no source'),
        (f'Digital hydraulic actuators, {place}', 'Titanium alloy', 'Ti-6Al-4V', None, None, None, 'Yes', 'S, E',
         'its housing: NEW "钛合金外壳", the remainder; Ti-6Al-4V the grade (E)'),
    ]


SHARES_ROWS += [row for place in PLACES for row in hydraulic_share_rows(place)]
SHARES_ROWS += [
    # The power unit of Atlas (old) (point 4.4): as MiniHyQ's weighed pack (KHN), its pump and gearbox, its motor; the
    # rest of its printed parts, titanium or aluminium.
    ('Hydraulic power unit', 'Steel', '42CrMo4', 0.1, 0.2, 0.3, None, 'E',
     'its pump and gearbox: KHN\'s MiniHyQ pack, "weight 1.94 kg" and "0.43kg" of "12 kg", 20 % (arith.); 42CrMo4 the '
     'grade (E)'),
    *motor_share_rows('Hydraulic power unit', 0.11, 'SH',
                      'its motor: KHN "weight 1.36kg" of "12 kg", 11 % (arith.); SH, the class a joint that moves often '
                      'draws most (the waist, E)'),
    ('Hydraulic power unit', 'Titanium alloy or Aluminium alloys', 'Ti-6Al-4V', None, None, None, 'Yes', 'E',
     'its manifold, reservoir, accumulator, filter and cooler, the remainder: IRG "Mixture of titanium and aluminum '
     '3D-printed parts", either, each as often (E27.4 question 8); Ti-6Al-4V the titanium\'s grade (E), the aluminium '
     "the type's"),
    # The frame of Atlas (old) (point 4.10).
    ('Frame: titanium and aluminium', 'Titanium alloy', 'Ti-6Al-4V', 0.25, 0.5, 0.75, None, 'E',
     'IRG "Mixture of titanium and aluminum 3D-printed parts": no share stated; Ti-6Al-4V the grade (E)'),
    ('Frame: titanium and aluminium', 'Aluminium alloys', None, None, None, None, 'Yes', 'S, E',
     'IRG "Mixture of titanium and aluminum 3D-printed parts": its aluminium, the remainder'),
]
# The oil's density (point 6), in the files of the hydraulic robots only (types 3, 5 and 6).
HYDRAULIC_CONSTANTS = [
    ('all', OIL_DENSITY, 0.86, 0.87, 0.88, 'kg/l', 'S, E',
     'ENE "Density (15°C) g/cm3 0.869", CHV "Density at 15°C, kg/l 0.87": the mode; about 1 % either side (E); '
     'EVIDENCE.md E27.7 point 6'),
]
# The sources the hydraulic rows cite, read first-hand on 2026-11-04 (EVIDENCE.md E27, VERIFICATION.md V157 to V160);
# each builder of a hydraulic robot places them among its own.
HYDRAULIC_SOURCES = [
    ('FRO', 'Barasuol et al. (IIT with Moog), Frontiers in Robotics and AI 5:51, 2018: the ISA ("Dry weight 920 g 1,600 '
            'g", "additively manufactured (AM) in a titanium alloy")',
     'https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2018.00051/full',
     'Peer-reviewed; design and datasheet values'),
    ('MOO', 'Moog, E024 Series datasheet ("Mass: 95 g (3.35 oz)")',
     'https://www.moog.com/content/dam/moog/literature/products/servovalves/E024_Series_Datasheet.pdf',
     "Manufacturer's datasheet"),
    ('M30', 'Moog, Type 30 servo valve catalogue ("Materials used in Standard Type 30 Servo valves")',
     'https://www.moog.com/content/dam/moog/literature/sdg/defense/Moog-Type30-Servo-Valve-Catalog.pdf',
     "Manufacturer's catalogue of the valve the E024 descends from"),
    ('SEM19', 'Semini et al. (IIT with Moog), Brief introduction to the quadruped robot HyQReal, I-RIM 2019 (the ISA '
              'v2 cut open)', 'https://iit-dlslab.github.io/papers/semini19irim.pdf', 'Conference paper'),
    ('KHN', "Khan et al. (IIT), MiniHyQ's on-board power pack, SICFP 2015 (\"Weight 12 kg\", \"Max Power Consumption "
            '5.5 kW")', 'https://iit-dlslab.github.io/papers/khan15sicfp.pdf', 'Conference paper, its parts weighed'),
    ('IRG', 'IEEE Robots Guide, Atlas (hydraulic, 2016 to 2024: "Mixture of titanium and aluminum 3D-printed parts")',
     'https://robotsguide.com/robots/atlas2016', 'Second-hand: a guide'),
    ('ENE', 'ENEOS, Hydraulic Oil 5606J ("Density (15°C) g/cm3 0.869")',
     'https://www.eneos.co.jp/english/products/lubricants/pdf/ind-4032-2306e.pdf', "Manufacturer's datasheet"),
    ('CHV', 'Chevron, Hydraulic Oil 5606 ("Density at 15°C, kg/l 0.87", "autopilots and robotics")',
     'https://www.chevronmarineproducts.com/content/dam/chevron-marine/pds-2020/'
     'Chevron_PDS_HydraulicOil_HydraulicOil5606_v0720_1.pdf', "Manufacturer's datasheet"),
    ('NEW', "Neo1's founder Yang Tao, interviewed by 着陆TouchBase, 2026-10-15 (\"钛合金外壳，自重1.1公斤\", "
            '"小功率电机", "液压件是一堆铁")', 'https://www.163.com/dy/article/L9AAAKRI0553D9NB.html',
     "Second-hand: the maker's founder interviewed"),
]

# --- Constants: the shared numbers ----------------------------------------------------------------------------
# The numbers every robot of a file uses, once under the robot "all" (EVIDENCE.md E2.8, E2.8b, E5.14, E5.21, E5.22):
# the first six before a robot type's own shared numbers (type 1's for the robots whose sources stop, E5.17), the
# last five after them, in the order the files have always had.
SHARED_CONSTANTS_FIRST = [
    ('all', 'Board mass per cm2 (boards not weighed)', 0.28, 0.56, 0.84, 'g/cm2', 'E',
     'the weighed small driver board, 12.8 g on 22.9 cm2, ± 50 %; E2.8'),
    ('all', "Copper share of a board's mass", 0.125, 0.2, 0.287, 'share', 'S',
     'Bizzo 2014, Table 3: 14 analyses combined (min / mean / max); E2.8b'),
    ('all', 'Power conductor cross-section (2 conductors)', 0.52, 0.82, 1.31, 'mm2', 'S',
     "20 / 18 / 16 AWG, the XT30's wire range (TME, second-hand)"),
    ('all', 'Signal conductor cross-section (2 conductors)', 0.065, 0.13, 0.2, 'mm2', 'E', 'E2.8'),
    ('all', 'Copper density', 8.96, 8.96, 8.96, 'g/cm3', 'S', 'copper'),
    ('all', 'Insulation and jackets, per mass of copper', 0.5, 1, 1.5, 'times', 'E', 'E2.8'),
]
SHARED_CONSTANTS_LAST = [
    # A pack no source weighs (Matthias, 2026-11-02, "A, as recommended", EVIDENCE.md E20): its housing, busbars and
    # wires a share of its cells, from the packs their makers weigh with their energy, each its pack less its cells (at
    # the NMC cell's 241.5 Wh/kg) and its management board (33.6 g), over its cells.
    ('all', 'Battery housing, share of its cells (packs not weighed)', 0.207, 0.414, 0.859, 'share', 'S, E',
     "the median of the packs weighed with their energy, the Unitree G1's 0.414, the EngineAI PM01's 0.505 and "
     "T800's 0.414; the least half of it; the most the Reachy 2's 0.859 (its 2021 base's pack, E), above 1.5 times "
     "(E20)"),
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
]

# --- Sources: those the shared rows cite ---------------------------------------------------------------------
# Each a row of the sheet Sources, by its code (EVIDENCE.md E2.1); a robot type's builder places them among its own.
SHARED_SOURCES = {
    'L1': ('L1', 'Livox, Mid-360 specifications', 'https://www.livoxtech.com/mid-360/specs',
           "Manufacturer's datasheet"),
    'T1': ('T1',
           'China Post Securities (Su, Sheng, Yang), Unitree G1 Humanoid Robot Teardown Report, '
           '2026-03-30', 'https://pdf.dfcfw.com/pdf/H3_AP202603311820899944_1.pdf',
           "A securities firm's own teardown, parts weighed"),
    'T3': ('T3', 'Munro & Associates, Munro Live, Unitree G1 teardown, 2026, through Humanoid.guide',
           'https://humanoid.guide/unitree-g1-teardown-reveals-actuator-and-cooling-tradeoffs/', 'Second-hand'),
    'T3k': ('T3k', "Munro's knee-actuator report (Grant), through SMZDM", 'https://post.smzdm.com/p/awwo7o5g/',
           'Second-hand'),
    'Bizzo 2014': ('Bizzo 2014', 'Bizzo, Figueiredo, de Andrade, Materials 7 (2014) 4555-4566',
           'https://pmc.ncbi.nlm.nih.gov/articles/PMC5455934/', 'University analyses, 14 combined'),
    'Drexler 2025': ('Drexler 2025', 'Drexler, Kampker, Born et al., Elektrotech. Inftech. 142 (2025) 312-345',
           'doi:10.1007/s00502-025-01331-3', 'Measured traction motors, through RAWCLICVehicleTractionMotor'),
}


# --- The template where a source stops ---------------------------------------------------------------------
# A figure a maker states once: ± 5 %, the spread between units (E5.12 point 3; the N1's accepted production
# tolerance of its battery, E5.14 point 2).
STATED_SPREAD = 0.05
# A joint's class: small below this peak torque, N·m, large from it (E5.12 point 1: the geometric middle of the G1's
# small joint, 35 N·m, and its large one, 88 N·m). Each block's joints are written with the class this gives.
LARGE_FROM_NM = 55

# The template's sizes and masses where a robot's sources name a board or sensor but give no size or mass (E5.14
# points 4 and 8, as the G1's, X1's and N1's).
# cm2: the G1's small joint's driver board, weighed at 12.8 g (T1 slides 24, 43), its area at most the 60 mm joint
# (E2.8): the area every joint's driver board is scaled from, in every robot type (a G1's row of type 1's sheet Boards;
# in another type's file the shared number DRIVER_AREA).
DRIVER_BOARD_AREA = (11.5, 22.9, 28.3)
DRIVER_AREA = "Driver board area, small joint (the G1's, weighed)"
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
# kg: one XT30 (2+2) connector, a mated pair: Amass's cable female XT30(2+2)-F.G.B 1.1224 g and board male
# XT30PB(2+2)-M 1 g (LCSC, gross), ± 10 % (2026-10-29, "Yes, enter all"; EVIDENCE.md E5.22; 3 g before).
CONNECTOR_KG = (0.0019, 0.00212, 0.0023)
# The computer's cooler of a robot whose sources do not weigh it (Matthias, 2026-10-29, "Yes, build them", point 4;
# EVIDENCE.md E5.20, "Not entered": until then in its frame's remainder): a fan as the G1's main board fan (its copper
# winding by the sheet Shares), and for an ARM board (a Jetson, Rockchip, Radxa, Qualcomm or RDK, or a board not named)
# the G1's aluminium heat sink, for an Intel or AMD laptop-class processor the X1's and N1's copper heat pipes and fins
# (E2.8e). Each an entry of a block's `cooler`, as one of its `parts`.
FAN_KG = (0.005, 0.01, 0.02)
COOLER_FAN = ('Main board fan', 1, 'Boards', 'Torso', FAN_KG, None, None, 'E',
              "as the G1's main board fan (E2.8e; 2026-10-29, point 4)")
ARM_SINK = ('Main board heat sink', 1, 'Boards', 'Torso', (0.05, 0.1, 0.2), 'Aluminium alloys', None, 'E',
            "an ARM board's: as the G1's (E2.8e; 2026-10-29, point 4)")
X86_SINK = ('Main board heat sink: heat pipes and fins', 1, 'Boards', 'Torso', (0.055, 0.12, 0.19), 'Copper',
            None, 'E', "an Intel or AMD laptop-class processor's: as the X1's and N1's (E2.8e; 2026-10-29, point 4)")
ARM_COOLER = [COOLER_FAN, ARM_SINK]
X86_COOLER = [COOLER_FAN, X86_SINK]
SCREWS_KG = (0.2, 0.5, 1)        # kg: a robot's screws (as the G1's; E5.14 point 7)
CABLES_M = (5, 10, 15)           # m of four conductors where no length is listed (as the N1's; E5.14 point 5)
# A robot's cables in the sheet Constants: four conductors (two for power, two for signals: type 1's, E2.8), or two
# for power and an Ethernet line of eight (the Fourier GR-1's and GR-2's "46V电源线和以太网线", EVIDENCE.md
# E6.8 point 9). 01 reads the same two names (CABLE_LENGTHS).
CABLE_FOUR = 'Cable length (four conductors)'
CABLE_ETHERNET = 'Cable length (two power conductors and an Ethernet line)'
# The car sensor elements of a sensor whose maker names its kind but not its model (E5.14 point 8, as type 1's).
DEPTH_CAMERA = [('laser diode array', 1), ('IR camera sensor', 2), ('CMOS image sensor', 1)]   # as the D435's
LIDAR = [('laser diode array', 1), ('photodetector array', 1), ('IMU', 1)]                      # as the Mid-360's
CAMERA = [('CMOS image sensor', 1)]
MICROPHONES = [('MEMS microphone array', 4)]   # as the G1's four (T1 slide 33)
ENCODER = [('angle sensor', 1)]                # a joint's encoder: the car's angle sensor (as the G1's, E2.8b)
# A power distribution board where a robot's sources name none (as the G1's; E5.14 point 4).
POWER_BOARD = ('Power distribution board', 1, 'Boards', 'Torso', POWER, 'PE_HVS', 'E',
               'as the G1 (E5.14 point 4)')

# The texts of the sheets that 02 reads as what a row is computed from (its column "Remainder of, or computed from"),
# and the basis every joint's magnets share.
JOINT_MASSES = "the Joints' module masses; inside as JointParts' joint of its size, scaled to its mass"
JOINT_SHARES = ("the Joints' shares of the joint modules, a share of the robot's mass (Constants); inside as "
                "JointParts' joint of its size, scaled to its mass")
# A size of joint whose rows are partly shares, partly stated masses: a template robot's hands or grippers (outside the
# template, which counts body joints only: EVIDENCE.md E7.4), or its stated joints in place of a group of the template
# (the JingChu's knees, E7.5 point 2).
JOINT_MIXED = ("the Joints' module masses where given, else their shares of the joint modules, a share of the robot's "
               "mass (Constants); inside as JointParts' joint of its size, scaled to its mass")
DRIVER_FROM = "JointParts' driver board of its size, scaled to its joint's module mass; area likewise"
PACK_STATED = 'its cells, its management board (Boards) and its housing (the rows below)'
# A pack no source weighs (Matthias, 2026-11-02, "A, as recommended", EVIDENCE.md E20): its cells from its energy, its
# housing a share of its cells (HOUSING_OF_CELLS), its mass their sum with its management board.
PACK_FROM_ENERGY = ('its cells, its management board (Boards) and its housing (the rows below), their sum; its housing '
                    'a share of its cells (E20)')
PACK_CELLS_ONLY = ("its cells, its management board (Boards) and no housing: the maker's pack is lighter than its "
                   'cells (E5.14 point 3)')
# The cells from their energy, over the Wh/kg of their own cells: the NMC cell's, or for cells of another recipe (the
# grade of their row) one cell of that recipe in the sheet Cells, drawn.
CELLS_FROM_CHARGE = 'from the energy: Constants voltage × capacity over {}'
CELLS_FROM_MASS = "from the energy: Constants' Battery energy per kg of robot times the robot's mass, over {}"
NMC_CELL = "the NMC cell's Wh/kg"
CELL_OF_RECIPE = "the Wh/kg of a cell of its recipe (its grade) in the sheet Cells"
HOUSING = 'the battery pack, less its cells and its management board'
HOUSING_OF_CELLS = "a share of its cells: Constants' Battery housing, share of its cells (packs not weighed)"
SHELL = "a share of the robot's mass: Constants' Shell, share of the robot mass"
# A lift column whose maker gives it no mass: a share of the robot's mass less its motor, a joint of the sheet Joints
# (EVIDENCE.md E9.6 point 7; 01 and 02 read the shared number it names).
LIFT_SHARE = 'Lift column, share of the robot mass, on wheels'
LIFT = f"a share of the robot's mass: Constants' {LIFT_SHARE}; less its motor"
LIFT_PART = 'Lift column: aluminium profile, steel screw and guides'
FRAME = 'the robot (Constants), less every other part'
MAGNETS_BASIS = 'Its magnets: the grade classes of its heat group, sheet MagnetGrades (EVIDENCE.md E2.11)'
# The housing of a battery pack: its shares in the sheet Shares, the housing aluminium or plastics (each as often), or
# aluminium where the maker says so (the PM01).
HOUSING_MIXED = 'Battery housing, busbars and wires'
HOUSING_ALUMINIUM = 'Battery housing (aluminium), busbars and wires'
# The joints of a robot whose sources give no joint torques (E5.17 point 1): AVERAGE in its block. The text is also
# type 1's name of what its template's rows average; another type names its own (average_joints()).
AVERAGE = 'as batch 1 on average'


# The steels by their grade (EVIDENCE.md E19 point 2, agreed 2026-11-02, "Yes, agree E19"): a stainless steel and an
# electrical steel each a material of its own; every other grade is the material Steel.
STAINLESS_GRADES = ('17-4PH', '440C', 'Type 304')
ELECTRICAL_GRADES = ('M19', 'M27', 'M19 or M27')


def steel_of(grade: str | None) -> str:
    """The material of a part of steel by its grade: Stainless steel, Electrical steel, or Steel."""
    return ('Stainless steel' if grade in STAINLESS_GRADES else 'Electrical steel' if grade in ELECTRICAL_GRADES
            else 'Steel')


def spread(mode: float, low: float = 1 - STATED_SPREAD, high: float = 1 + STATED_SPREAD) -> tuple:
    """Min, mode and max: `low` and `high` times the mode, rounded to four decimals. By default ± 5 %, a figure stated
    once."""
    return round(low * mode, 4), round(mode, 4), round(high * mode, 4)


def estimate(mode: float) -> tuple:
    """An estimate (E): half to 1.5 times its mode (Matthias, 2026-10-27: "Estimates should be larger than known
    numbers")."""
    return spread(mode, 0.5, 1.5)


# --- Sensors whose makers name their kind but not their model (E7.5 point 8) ------------------------------------
# A binocular or depth camera as a D435, 75 g, half to 1.5 times (STEREO_CAMERA_G); a camera of one sensor and a LiDAR
# as type 1's of no named model (their kind's elements, no mass of their own). Each a row of a block's `sensors`:
# (sensor, number in the robot, kind of part, body region, grams min / mode / max or None, label, sources, its car
# sensor elements). In type 2's builder until 2026-11-05, here since, as every type uses them (EVIDENCE.md E31).
# The camera of a robot whose maker names it but gives no mass: as a D435 (75 g), a stereo camera too, half to 1.5
# times (E6.8 point 8); its elements two image sensors.
STEREO_CAMERA_G = estimate(75)
STEREO = [('CMOS image sensor', 2)]


def binocular(source: str, count: int = 1, name: str = 'Binocular camera') -> tuple:
    """`count` binocular (stereo) cameras in the head: two image sensors each, a D435's mass."""
    return (name, count, 'Head', 'Head', STEREO_CAMERA_G, 'E', f'{source}; its mass not stated: as a D435 (E7.5 point '
                                                               '8)', STEREO)


def depth_camera(source: str, count: int = 1) -> tuple:
    """`count` depth cameras in the head, as a D435: its laser diode array, two infrared and one colour image sensor."""
    return ('Depth camera (not named)', count, 'Head', 'Head', STEREO_CAMERA_G, 'E',
            f'{source}; its mass not stated: as a D435 (E7.5 point 8)', DEPTH_CAMERA)


def camera(name: str, count: int, kind: str, source: str) -> tuple:
    """`count` cameras of one colour image sensor in the kind of part `kind` (its body region of the same name), their
    elements only."""
    return (name, count, kind, kind, None, 'S', f'{source}; as type 1\'s cameras of no named model (E7.5 point 8)',
            CAMERA)


def lidar(source: str) -> tuple:
    """A 3D LiDAR in the head, as type 1's of no named model (the Mid-360's elements)."""
    return ('LiDAR, 3D (not named)', 1, 'Head', 'Head', None, 'S',
            f"{source}; as type 1's LiDAR of no named model (E7.5 point 8)", LIDAR)


def imu(source: str, name: str = 'Motion sensor (IMU)') -> tuple:
    """A motion sensor in the torso, as the G1's."""
    return (name, 1, 'Boards', 'Torso', IMU_G, 'E', f"{source}; as the G1's (E7.5 point 8)", [('IMU', 1)])


def microphones(source: str, name: str = 'Microphone array') -> tuple:
    """A microphone array in the head, as the G1's four microphones."""
    return (name, 1, 'Head', 'Head', MICROPHONES_G, 'E', f"{source}; as the G1's four (E7.5 point 8)", MICROPHONES)


def speaker(source: str) -> tuple:
    """A speaker in the head, as the G1's."""
    return ('Speaker', 1, 'Head', 'Head', SPEAKER_G, 'E', f"{source}; as the G1's (E7.5 point 8)", [])


# --- The cameras of the robots whose parts named none (EVIDENCE.md E31) -------------------------------------------
# Matthias, 2026-11-05: "Yes, build 1 to 5", "Yes, those first", "Yes, A to H". 144 robots of the six parts files listed
# no camera and no microphone. Their makers' pages and, where those say nothing, third parties were searched twice
# (E31), and every source below read first-hand before it was entered (VERIFICATION.md V181). Each robot its own rows,
# added by robot_rows() to its block's sensors, whatever its type:
#   point 1 and 2 (CAMERAS_STATED): the robots whose source states their cameras, as it states them; the microphones
#     the same source names (E31 point A: no LiDAR, the research was of cameras and microphones);
#   point 3 (CAMERAS_ESTIMATED): the robots whose cameras no source counts, ESTIMATED_CAMERAS, a row without a number,
#     and its number drawn by 02 in every draw, a whole number from the robot's constant NUMBER_OF + ESTIMATED_CAMERAS,
#     1 / 3 / 12 image sensors (E: the 172 robots and versions of the parts files that list cameras hold 1 to 20, most
#     often 3, median 4; colour image sensors, E31 point C); and a microphone array, four as the G1's, where a source
#     names a microphone or speech (listening, dialogue, voice; not "natural language interaction" alone, not a voice
#     module sold as an option or of another variant, E31 point G);
#   point 4: the makers who sell the camera only as an option (the RB-Y1, the Torobo, the N1, the Roboto Origin, the
#     Roban2, the RP1, the Adam Lite): none, so no row here.
# A camera outside the head where the source places it: in the arms (wrists, grippers) or the torso (kind Boards, as
# the motion sensors), each place a sensor of its own name.
NUMBER_OF = 'Number: '   # 01_schemas.py reads the same prefix (NUMBER_OF)
ESTIMATED_CAMERAS = 'Cameras (number not stated)'
CAMERAS_NUMBER = (1, 3, 12)
CAMERAS_NUMBER_SOURCE = ("E31 point 3: no source counts its cameras; the 172 robots and versions of the parts files "
                         'that list cameras hold 1 to 20 image sensors, most often 3, median 4 (E)')
MICROPHONES_6 = [('MEMS microphone array', 6)]
MICROPHONES_7 = [('MEMS microphone array', 7)]
# The sources E31's rows cite, each a row of the sheet Sources of every file whose rows cite it (sheets()).
E31_SOURCES = {
    'E31-BBC': ('E31-BBC', "BBC News, 8 June 2026, its reporter at Foundation's facility (\"Phantom MK-1, which I am "
                           "shown, doesn't have a battery\")", 'https://www.bbc.com/news/articles/cedpxwe26l1o',
                'First-hand: a journalist\'s own look'),
    'E31-NWK': ('E31-NWK', 'Newsweek on the Phantom, its photo caption ("Phantom MK1 has eight cameras in its head.")',
                'https://www.newsweek.com/could-this-humanoid-robot-become-the-armys-ultimate-warrior-11063424',
                'Second-hand: a press report'),
    'E31-PALt': ('E31-PALt', 'PAL Robotics, TALOS data sheet (TALOS-DataSheet-1.pdf: "RGB 1280x720 at 30 fps", "Depth '
                             '640x480 at 30 fps, 0.4-8m range")',
                 'https://pal-robotics.com/wp-content/uploads/2025/09/TALOS-DataSheet-1.pdf', "Manufacturer's datasheet"),
    'E31-PALr': ('E31-PALr', 'PAL Robotics, "Unplug and play with REEM-C humanoid robot!", 21 Nov 2013',
                 'https://pal-robotics.com/blog/unplug-play-reem-c/', "Manufacturer's blog"),
    'E31-AGA': ('E31-AGA', 'AgiBot, A2 page ("six high-definition cameras", "sound source localization")',
                'https://agibot.com/products/A2', "Manufacturer's specification"),
    'E31-DBA': ('E31-DBA', 'DOBOT, ATOM series page (the ATOM Max: "a 60FPS Full HD vision system, and Intel '
                           'RealSense D455 depth sensing")',
                'https://www.dobot-robots.com/products/humanoid-robots/atom.html', "Manufacturer's specification"),
    'E31-KNX': ('E31-KNX', 'KEENON, XMAN-R1 page ("Depth Vision Cameras *4", "HD Wide-Angle Cameras *4", "High-'
                           'definition omnidirectional microphones")', 'https://www.keenon.com/en/product/XMAN-R1',
                "Manufacturer's specification"),
    'E31-UBU': ('E31-UBU', 'UBTECH, U1 Pro page, its table ("6-microphone array built into the head", "2 RGB cameras '
                           'built into the eyes")', 'https://www.ubtrobot.com/en/humanoid/products/u1-pro',
                "Manufacturer's specification"),
    'E31-YMD': ('E31-YMD', 'Yunmu, YMBOT D page (the site\'s script index-DGa4y2sb.js: "Active binocular structured '
                           'light depth camera", "Color camera resolution: 1280 x 800"; its data feed api/products/4: '
                           '"耳部收声/喇叭")', 'https://www.ymbot.com/product/detail/4', "Manufacturer's specification"),
    'E31-TRR': ('E31-TRR', 'The Robot Report, 24 Jun 2025, after NEURA ("With the patented Omnisensor and seven '
                           'cameras", "speakers, and microphones")',
                'https://www.therobotreport.com/neura-robotics-launches-latest-cognitive-robots-neuraverse-ecosystem/',
                'Second-hand: trade press after the maker'),
    'E31-3DN': ('E31-3DN', '3DNews, 11 Nov 2025, on the AIDOL ("две стереокамеры", "семь микрофонов")',
                'https://3dnews.ru/1132222', 'Second-hand: a press report'),
    'E31-YNT': ('E31-YNT', 'Ynet on the MenteeBot V3 ("Its head is equipped with five cameras", "can follow voice '
                           'commands")', 'https://www.ynetnews.com/tech-and-digital/article/hkwyqhezbg',
                'Second-hand: a press report'),
    'E31-CNN': ('E31-CNN', 'CNN (A. Strickland), 23 Aug 2023, on the Apollo ("Apollo\'s head contains a perception '
                           'camera")', 'https://kioncentralcoast.com/?p=931628', 'Second-hand: a press report'),
    'E31-IET': ('E31-IET', 'Interesting Engineering on the PrimeBOT T1 ("a flip camera", "a multi-microphone array")',
                'https://interestingengineering.com/ai-robotics/china-qiyuan-t1-robot-humanoid-quadruped-modes',
                'Second-hand: a press report'),
    'E31-RSD': ('E31-RSD', 'RealSense, its case study of Agility\'s Digit ("Embedded in the neck of the robot, '
                           'RealSense Depth Camera D455")', 'https://www.realsenseai.com/?p=25482',
                "Second-hand: the camera maker's case study"),
    'E31-AST': ('E31-AST', 'Astribot, S1 data sheet (astribot-s1_eng.pdf, hosted by igus/RBTX: "Head camera RGB-D '
                           'camera * 1 Stereo vision camera*1", "Gripper camera RGB-D camera*2", "Chest camera RGB-D '
                           'camera*1")', 'https://a.storyblok.com/f/298593/x/d5cf3ddd99/astribot-s1_eng.pdf',
                "Manufacturer's datasheet"),
    'E31-NTX': ('E31-NTX', 'Noetix, Dora page, archived 28 Oct 2025 ("深度相机 3 斜向下 2 向前 1", "结构光深度相机", '
                           '"阵列麦克风 6")',
                'https://web.archive.org/web/20251028183926/https://www.noetixrobotics.com/products-137.html',
                "Manufacturer's specification (archived)"),
    'E31-JKK': ('E31-JKK', 'JAKA, JAKA Kargo page ("Vision camera 2")',
                'https://www.jaka.com/en/productDetails/JAKA_Kargo', "Manufacturer's specification"),
    'E31-JKP': ('E31-JKP', 'JAKA, news of 26 Jun 2026 on the JAKA π ("Using a camera on its head", "It can talk with '
                           'you, listen to commands")', 'https://www.jaka.com/en/newsDetail/1493',
                "Manufacturer's news"),
    'E31-SPM': ('E31-SPM', 'Spirit AI, Moz1 manual, mechanics ("头部相机（Intel D455） 1", "腕部相机（Intel D405） 2")',
                'https://docs.spirit-ai.com/zh/moz1/mechanics.html', "Manufacturer's manual"),
    'E31-XHB': ('E31-XHB', 'X-Humanoid, company brochure, WRC July 2025, p. 4, 具身天工2.0 ("全场景双目结构光3D相机*3")',
                'https://www.worldrobotconference.com/profile/robot/download/2025/07/11/'
                '18公司介绍手册印刷版_20250711192526A076.pdf', "Manufacturer's brochure"),
    'E31-TLY': ('E31-TLY', 'Tlibot, Y1 manual ("头部深度相机*1、7自由度带 视觉机械臂*2", "Y1机器人视觉系统采用realsense '
                           'D435相机", "讯飞语音节点已启动")', 'https://www.tlibot.com/arm/127.html',
                "Manufacturer's manual"),
    'E31-YM4': ('E31-YM4', 'Yunmu, YMBot D4 page, its data feed api/products/7 ("双目相机/激光雷达/六维力传感器 RGBD相机/'
                           '鱼眼相机", "阵列麦克风/扬声器/多彩灯带")', 'https://www.ymbot.com/product/detail/7',
                "Manufacturer's specification"),
    'E31-TNM': ('E31-TNM', '東京報道新聞, 17 Apr 2026, on the CUE7 ("頭部のステレオカメラ")',
                'https://tokyonewsmedia.com/archives/21230', 'Second-hand: a press report'),
    'E31-NKK': ('E31-NKK', '日刊工業新聞 (newswitch), April 2026, on the CUE7 ("ドリブル用のカメラセンサーをＣＵＥ７の腰に'
                           '配置した。")', 'https://newswitch.jp/p/49050', 'Second-hand: trade press after the maker'),
}


def placed(sensor: tuple, kind: str, region: str, name: str = '') -> tuple:
    """A sensor row of the helpers above in another kind of part and body region (a camera in the wrists or the
    torso), under `name` where given."""
    return (name or sensor[0], sensor[1], kind, region, *sensor[4:])


def several_microphones(units: list, source: str) -> tuple:
    """A microphone array of the number of microphones its source states (`units`, MICROPHONES_6 or _7)."""
    return (f'Microphone array, {units[0][1]} microphones', 1, 'Head', 'Head', MICROPHONES_G, 'E',
            f"{source}; its mass as the G1's (E31)", units)


# Points 1 and 2: each robot's cameras and microphones as its source states them (the source's code first, its words).
CAMERAS_STATED = {
    'Foundation Phantom MK1': [camera('Camera', 8, 'Head', 'E31-NWK, its photo caption: "Phantom MK1 has eight '
                                                           'cameras in its head." (E31 point 1)')],
    'PAL TALOS': [depth_camera('E31-PALt, its head camera: "RGB 1280x720 at 30 fps", "Depth 640x480 at 30 fps"')],
    'PAL REEM-C': [binocular('E31-PALr "Stereo camera as eyes (15 Hz, 656×492, software sync)"'),
                   placed(camera('Camera, back', 1, 'Boards', 'E31-PALr, its torso: "Back camera (15Hz, 752×480)"'),
                          'Boards', 'Torso'),
                   microphones('E31-PALr "4 omnidirectional microphones in an asymmetric linear array"')],
    'AgiBot A2': [camera('Camera, high-definition', 6, 'Head', 'E31-AGA "360° Lidar and six high-definition cameras"'),
                  microphones('E31-AGA "accurate sound source localization", "voice commands"')],
    'DOBOT Atom': [depth_camera('E31-DBA, the ATOM Max: "Intel RealSense D455 depth sensing"'),
                   camera('Camera, Full HD vision system', 1, 'Head',
                          'E31-DBA, the ATOM Max: "a 60FPS Full HD vision system"; its image sensors not stated: one')],
    'Keenon XMAN-R1': [depth_camera('E31-KNX "Depth Vision Cameras *4"', 4),
                       camera('Camera, HD wide-angle', 4, 'Head', 'E31-KNX "HD Wide-Angle Cameras *4"'),
                       microphones('E31-KNX "High-definition omnidirectional microphones", their number not stated')],
    'UBTECH U1 Pro male': [camera('Camera, RGB', 2, 'Head', 'E31-UBU "2 RGB cameras built into the eyes"'),
                           several_microphones(MICROPHONES_6, 'E31-UBU "6-microphone array built into the head"')],
    'UBTECH U1 Pro female': [camera('Camera, RGB', 2, 'Head', 'E31-UBU "2 RGB cameras built into the eyes"'),
                             several_microphones(MICROPHONES_6, 'E31-UBU "6-microphone array built into the head"')],
    'Yunmu YMBot D': [depth_camera('E31-YMD "Active binocular structured light depth camera", "Color camera '
                                   'resolution: 1280 x 800"'),
                      microphones('E31-YMD "耳部收声/喇叭" (sound pick-up and speaker at the ears), their number not '
                                  'stated')],
    'NEURA 4NE1 Gen 3': [camera('Camera', 7, 'Head', 'E31-TRR, after NEURA: "With the patented Omnisensor and seven '
                                                     'cameras"'),
                         microphones('E31-TRR "Its conversational AI, speakers, and microphones", their number not '
                                     'stated')],
    'AIDOL Lab AIDOL': [binocular('E31-3DN "две стереокамеры" (two stereo cameras)', 2),
                        several_microphones(MICROPHONES_7, 'E31-3DN "семь микрофонов" (seven microphones)')],
    'Mentee MenteeBot V3': [camera('Camera', 5, 'Head', 'E31-YNT "Its head is equipped with five cameras that provide '
                                                        '360-degree vision"'),
                            microphones('E31-YNT "The robot can follow voice commands"')],
    'Apptronik Apollo': [camera('Camera, perception', 1, 'Head', 'E31-CNN "Apollo\'s head contains a perception '
                                                                 'camera"')],
    'PrimeBOT T1': [camera('Camera, flip', 1, 'Head', 'E31-IET "a flip camera"'),
                    microphones('E31-IET "a multi-microphone array", its number not stated')],
    'Agility Digit': [depth_camera('E31-RSD "Embedded in the neck of the robot, RealSense Depth Camera D455"')],
    'Astribot S1': [depth_camera('E31-AST "Head camera RGB-D camera * 1"'),
                    binocular('E31-AST "Stereo vision camera*1" (its head)'),
                    placed(depth_camera('E31-AST "Gripper camera RGB-D camera*2"', 2), 'Arms', 'Arms',
                           'Depth camera, grippers (RGB-D)'),
                    placed(depth_camera('E31-AST "Chest camera RGB-D camera*1"'), 'Boards', 'Torso',
                           'Depth camera, chest (RGB-D)')],
    'Noetix Dora': [depth_camera('E31-NTX "深度相机 3 斜向下 2 向前 1" (depth cameras 3, 2 tilted down, 1 forward), '
                                 '"结构光深度相机" (structured light)', 3),
                    several_microphones(MICROPHONES_6, 'E31-NTX "阵列麦克风 6" (array microphones 6)')],
    'JAKA Kargo': [camera('Camera, vision', 2, 'Head', 'E31-JKK "Vision camera 2" (E31 point H)')],
    'JAKA π': [camera('Camera', 1, 'Head', 'E31-JKP "Using a camera on its head"'),
               microphones('E31-JKP "It can talk with you, listen to commands"')],
    'Spirit AI Moz1': [depth_camera('E31-SPM "头部相机（Intel D455） 1" (head camera)'),
                       placed(depth_camera('E31-SPM "腕部相机（Intel D405） 2" (wrist cameras)', 2), 'Arms', 'Arms',
                              'Depth camera, wrists (Intel D405)')],
    'X-Humanoid Tien Kung 2.0': [depth_camera('E31-XHB "全场景双目结构光3D相机*3" (binocular structured-light 3D '
                                              'cameras ×3)', 3)],
    'Tlibot Y1': [depth_camera('E31-TLY "头部深度相机*1" (head depth camera), "realsense D435相机"'),
                  camera('Camera, arm', 2, 'Arms', 'E31-TLY "7自由度带 视觉机械臂*2" (7-DoF arm with vision ×2): a camera '
                                                   'on each arm (E31 point F)'),
                  microphones('E31-TLY "讯飞语音节点已启动" (its iFlytek voice node), its microphones not stated')],
    'Yunmu YMBot D4': [binocular('E31-YM4 "双目相机" (binocular camera)'),
                       depth_camera('E31-YM4 "RGBD相机" (RGB-D camera)'),
                       camera('Camera, fisheye', 1, 'Head', 'E31-YM4 "鱼眼相机" (fisheye camera)'),
                       microphones('E31-YM4 "阵列麦克风" (microphone array), its number not stated')],
    'Toyota CUE7': [binocular('E31-TNM "頭部のステレオカメラ" (the stereo camera of its head)'),
                    placed(camera('Camera, waist', 1, 'Boards', 'E31-NKK "ドリブル用のカメラセンサーをＣＵＥ７の腰に配置'
                                                                'した。" (a camera sensor for dribbling at its waist)'),
                           'Boards', 'Torso')],
}

# Point 3: each robot (by its name in its parts file; the register's number beside it) whose cameras no source counts,
# with the words of its sources that name a microphone or speech ('' where none do): its cameras drawn, 1 / 3 / 12,
# and, where named, a microphone array of four.
CAMERAS_ESTIMATED = {
    'NEURA 4NE1 Gen 3.5': 'a microphone array (aiwiki), microphones (Origin of Bots)',   # 4
    'NEURA 4NE1 Gen 4': '"hears", "AI Voice" (4NE1 Gen 4)',   # 5
    'AgiBot A2 Max': '',   # 7
    'Andromeda Abi': 'microphone arrays',   # 9
    'AgiBot A2-W': '',   # 13
    'ROBOTIS AI Sapiens K1': '',   # 19
    'Flexiv AICO 2-4': '',   # 21
    'Flexiv AICO 2-10': '',   # 21
    'AKINROBOTICS AKINCI-5': '',   # 23
    'TeknTrash ALPHA': '',   # 28
    'Anigon': '',   # 31
    'Apptronik Apollo 2': '"listening capabilities"',   # 33
    'Astribot T1': '',   # 41
    'ELU.AI AstroDroid AD-01': '',   # 42
    'Boston Dynamics Atlas': '',   # 43
    'Vbot ATOM': '',   # 46
    'NEUBILITY Billi': '',   # 51
    'MirrorMe Bolt': '',   # 53
    'Borg Robotics Borg 01': '',   # 56
    'Noetix Bumi': 'a "voice module"',   # 57
    'Wandercraft CALVIN-40': '',   # 58
    'CasiVision CASIVIBOT': '',   # 61
    'Donut Cinnamon 1': '',   # 63
    'Sharpa D01': '',   # 73
    'XYZ DEUX': 'a voice-interaction model (Venture Square)',   # 74
    'BOSHIAC DexBot': 'speech (a catalogue)',   # 76
    'Agility Digit 5': '',   # 78
    'Deep Robotics DR01': '',   # 80
    'Duatic Alpha': '',   # 83
    'Noetix E1': 'a circular microphone',   # 85
    'Tangible Robots Eggie': '',   # 86
    'Genesis AI Eno': '',   # 90
    'AVIC Fengxing-001': '',   # 93
    'Holiday Robotics Friday': '',   # 100
    'Futuring 2 on legs': 'microphones',   # 101
    'Futuring 2 on wheels': 'microphones',   # 101
    'AgiBot G2 Max': '',   # 106
    'Persona AI Gen 1': '',   # 110
    'Gento Luna': '',   # 112
    'GAC GoMate': 'responds to voice commands',   # 114
    'GAC GoMate Mini': '',   # 115
    'Haier HIVA Haiwa': '',   # 125
    'HONOR A1': '"intelligent voice interaction"',   # 131
    'HONOR D1': '"voice interaction"',   # 132
    'Simplexity I-Series': '',   # 134
    'XPENG IRON 2024': 'a "speech interaction system"',   # 136
    'XPENG IRON 2025': 'a "microphone array" at the ears',   # 137
    'Weave Isaac 1': '',   # 139
    'JAKA K1': '',   # 141
    'Zeroth Jupiter': '',   # 146
    'ROBOTIS K0': '',   # 147
    'KinetixAI KAI on legs': 'talks with visitors (10jqka)',   # 150
    'KinetixAI KAI on wheels': 'talks with visitors (10jqka)',   # 150
    'KAIST Humanoid': '',   # 151
    'LG KAPEX': '',   # 154
    'Galaxea Kengo': '',   # 156
    'Leju Kuavo-my': '',   # 164
    'Moon Dynamics L1': '',   # 165
    'Glroad Laborer M1': '',   # 167
    'LimX CL': '',   # 170
    'DOBOT LUMO': '"voice"',   # 175
    'GigaAI Maker H01': '',   # 183
    'Blue Worm Mantis Standard': '',   # 184
    'Sunday MEMO': 'microphones',   # 188
    'Mentee MenteeBot 2024': 'a verbal command',   # 189
    'O-ID Modular': '',   # 197
    'VinMotion Motion 2': '',   # 199
    'Zhejiang NAVAI-I3': '',   # 203
    'Zhejiang Navigator 2': '',   # 204
    'GENISOM NE01': '',   # 205
    '1X NEO Beta': '',   # 206
    'Galaxea NEXO': '',   # 209
    'Digit Nezha P01': '',   # 210
    'Sharpa North': '',   # 213
    'Tesla Optimus Gen 3': '',   # 221
    'Tesla Optimus Gen 2': '',   # 222
    'Tesla Optimus V2.5': 'responds to voice input (heise)',   # 223
    'Cyan Robotics Orca': 'a 6-microphone ring array',   # 224
    'Pink Robotics P0': '',   # 226
    'Sanctuary Phoenix': '',   # 229
    'Sanctuary Phoenix Gen 8': '',   # 230
    'PHYBOT M1': '',   # 232
    'PL-Universe ProWhite': '',   # 238
    'Pudu D7 2024': '"auditory sensing"',   # 240
    'Pudu D7 2026': '"auditory sensing"',   # 240
    'XPENG PX5': '',   # 242
    'OpenLoong Qinglong': 'a "hearing" module',   # 244
    'AgiBot QUESTER1': '',   # 246
    'NineRay RayNex G3': 'responds to voice commands (Xinhua)',   # 250
    'RoboScience REX G1': '',   # 258
    'Robbyant R1': 'spoken explanations (aiwiki)',   # 261
    'Roboligent Robin': '',   # 263
    'Robo Robotics ROBO-T1': '',   # 264
    'Zeroth Sean': '',   # 272
    'EIR SkyWalker 2 on legs': 'its perception for dialogue',   # 275
    'EIR SkyWalker 2 on wheels': 'its perception for dialogue',   # 275
    'Siasun Songxing': '',   # 276
    'Robotera Star1': '',   # 280
    'StarBot Astra': '',   # 281
    'Sulu.be Steve on legs': '',   # 284
    'Sulu.be Steve on wheels': '',   # 284
    'Unitree Superman': '',   # 285
    'iHub TARA GEN1': '"natural conversations"',   # 291
    'Tau Robotics Tau Humanoid': 'microphones, fitted and disabled',   # 293
    'X-Humanoid TianGong Ultra': '',   # 297
    'Tlibot Tianzhen Z1': '',   # 298
    'Tlibot T1': '',   # 302
    'WL Robotics Totan O1': '',   # 308
    'Walden Robotics Walden': '',   # 320
    'BYD Xiao Di': 'speaks six dialects and six languages',   # 330
    'Tencent Xiao Liu on legs': '',   # 331
    'Tencent Xiao Liu on wheels': '',   # 331
    'Digit XiaQi': 'voice dialogue, sound-source localisation',   # 333
    'Tlibot Y2-B': '',   # 336
    'Tlibot Y2-P': '',   # 337
    'Yunmu YMBot C': 'voice input and output',   # 339
    'Yunmu YMBot D2': '',   # 341
    'YMBOT E3': '',   # 343
    'Yunmu YMBot H': '"语音交互" (voice interaction)',   # 344
    'PL-Universe Zeus 1': '',   # 348
    'NORINCO Fuxi on legs': '',   # 351
    'NORINCO Fuxi on wheels': '',   # 351
}


def size_of(torque: float) -> str:
    """A joint's class by its actuator's peak torque (E5.12 point 1)."""
    return 'large' if torque >= LARGE_FROM_NM else 'small'


def joint(name: str, count: int, torque: float | None, masses: tuple, heat_group: str, region: str,
          size: str | None = None) -> tuple:
    """One joint kind of a block: its name, joints, class (by its torque, or `size` where no torque is stated), torque
    (N·m), module mass (kg), heat group and body region."""
    return name, count, size or size_of(torque), torque, masses, heat_group, region


def block(name: str, maker: str, height: float, stated: float | None, sources: str, mass: tuple, joints,
          **more) -> dict:
    """One robot's block: what its sheet Robots row says (`maker`, `height` m, `stated` mass kg, `sources`), its mass
    for the sheet Constants (`mass`: (min, mode, max), label, source), its joints (joint() each, or AVERAGE), and in
    `more` what differs from the template (E5.14): battery (False for a robot that carries none, the Phantom MK1's
    "lacks a battery", EVIDENCE.md E16.2: no pack, cells, housing or management board), voltage and capacity ((min,
    mode, max), label, source; none: the energy per kg of robot), pack ((min, mode, max), label, source; None: from its
    energy; PACK_CELLS_ONLY), housing, boards, sensors, cables (and cable_quantity, CABLE_FOUR or CABLE_ETHERNET), screws,
    parts (each (part, count, kind, region, kg, material, grade, label, source), and what it is computed from where it
    is), cooler (ARM_COOLER unless its computer is an Intel or AMD processor's), shell (None: none, its frame its shell,
    Nadia's carbon fibre, EVIDENCE.md E27.7 point 9.8), frame ((name, material, source), its grade a fourth item where
    given), oil (a hydraulic robot's volume of oil, ((min, mode, max) litres, label, source), E27.7 point 6), and the
    labels and sources of its joints, connectors, encoders and cells. A block whose joints are AVERAGE may also have
    `stated_joints` (joint() each), which take the place of their groups' rows of the template, and `added_joints` (its
    hands or grippers), which the template leaves out (it counts body joints only: EVIDENCE.md E7.4, E7.5 points 2 and
    4)."""
    b = dict(name=name, maker=maker, height=height, stated=stated, sources=sources, mass=mass, joints=joints,
             stated_joints=[], added_joints=[],
             joints_stated=None, joint_label={'small': 'E', 'large': 'E'}, joint_sources='', battery=True,
             voltage=None, capacity=None, pack=None, pack_source='', housing=HOUSING_MIXED,
             cells=('E', 'NMC cylindrical, E (E5.14 point 2)'),
             boards=[], sensors=[], cables=(CABLES_M, 'E', 'as the N1 (E5.14 point 5)'), cable_quantity=CABLE_FOUR,
             connectors=('S, E', 'two per joint, as type 1 (E5.14 point 5); the mass of a mated pair, Amass '
                                 'through LCSC (E5.22)'),
             encoders=('E', 'two per joint, as type 1 (E5.14)'),
             screws=[('Screws', 1, SCREWS_KG, '42CrMo4', 'E', 'as the G1 (E5.14 point 7); grade E5.18')],
             parts=[], cooler=ARM_COOLER, shell=('Shell: plastics', 'not stated; plastics as type 1 (E5.14 point 6)'),
             frame=('Frame', 'Aluminium alloys', 'not stated; aluminium as type 1 (E5.14 point 9)'),
             # A robot on wheels (EVIDENCE.md E9.7 point 3): its battery in its base, its cells' recipe where not NMC
             # (the CASBOT W1's LFP), its template's rows where not its type's (the template on wheels), its lift
             # column ((min, mode, max) kg, label, source; its kg None: a share of its mass, LIFT).
             battery_region='Torso', cell_recipe=None, averaged=None, lift_column=None, oil=None)
    b.update(more)
    return b


def joint_group(j: tuple) -> tuple:
    """The group of a joint for the average split: its name in the sheet Joints, heat group and body region."""
    if j[6] == 'Head':
        return 'Head joints', 'Elbows and wrists', 'Head'
    return {'Hips': ('Hip joints', 'Hips', 'Legs'), 'Knees': ('Knee joints', 'Knees', 'Legs'),
            'Ankles': ('Ankle joints', 'Ankles', 'Legs'), 'Waist': ('Waist joints', 'Waist', 'Torso'),
            'Shoulders': ('Shoulder joints', 'Shoulders', 'Arms'),
            'Elbows and wrists': ('Elbow and wrist joints', 'Elbows and wrists', 'Arms')}[j[5]]


def average_joints(blocks: list, label: str = AVERAGE) -> list:
    """The joints of a robot whose sources give no joint torques (E5.17 point 1: "split into small and large joints as
    batch 1's are on average"): for each group of joints (hips, knees, ankles, waist, shoulders, elbows and wrists,
    head) and class, its share of the joint modules' mass at the modes, averaged over `blocks` (type 1: its batch 1;
    type 2: its seven robots with every joint's torque, without their hands, E7.4); one row each, the joints of the
    group and class together, named with `label`, what they average. The shares add up to 1, as each robot's do;
    nothing is rescaled."""
    shares: dict = {}
    for b in blocks:
        total = sum(j[1] * j[4][1] for j in b['joints'])
        for j in b['joints']:
            key = joint_group(j) + (j[2],)
            shares[key] = shares.get(key, 0) + j[1] * j[4][1] / total / len(blocks)
    order = ['Hip joints', 'Knee joints', 'Ankle joints', 'Waist joints', 'Shoulder joints', 'Elbow and wrist joints',
             'Head joints']
    return [(f'{name}, {size} ({label})', 1, size, None, None, heat, region, share)
            for (name, heat, region, size), share in sorted(shares.items(), key=lambda kv: (order.index(kv[0][0]),
                                                                                          kv[0][3] == 'large'))]


def regions(joints: list) -> str:
    """The body regions of joints with their numbers, as the sheet Parts writes them ('Legs 12, Torso 1, Arms 10')."""
    counts: dict = {}
    for j in joints:
        counts[j[6]] = counts.get(j[6], 0) + j[1]
    return ', '.join(f'{region} {n}' for region, n in counts.items())


def template_joints(b: dict, averaged_joints: list) -> list:
    """The joints of a block whose joints are AVERAGE: the template's rows in their order, each group of the template
    for which the block states joints (`stated_joints`, the JingChu's knees) replaced by them, then its hands or
    grippers (`added_joints`). Nothing is rescaled: the rows kept keep the template's shares (EVIDENCE.md E7.5 point 2,
    open point A)."""
    groups = [a[0].split(',')[0] for a in averaged_joints]
    stated = {}
    for j in b['stated_joints']:
        group = joint_group(j)[0]
        if group not in groups:
            raise ValueError(f"{b['name']}: its stated joint {j[0]} is of no group of the template ({group}).")
        stated.setdefault(group, []).append(j)
    joints, placed = [], set()
    for a, group in zip(averaged_joints, groups):
        if group not in stated:
            joints.append(a)
        elif group not in placed:
            joints += stated[group]
            placed.add(group)
    return joints + list(b['added_joints'])


def template_block(name: str, maker: str, height: float, stated: float | None, mass: tuple, joints_stated: int,
                   computer: str, *, computer_source: str, joint_sources: str, default_sources: str, **more) -> dict:
    """A robot whose sources give no joint torques (type 1: E5.17; type 2: E7.4, E7.5): its joints a share of its
    mass, split as its type's robots with torques are on average (its block's joints AVERAGE, `joint_sources` saying
    so); its battery from the energy per kg of robot unless a voltage or capacity is given; a computer board as the
    template's, named `computer` as its sources name it (`computer_source`), and the template's power distribution
    board; the rest as E5.14 unless `more` says otherwise (its `sources` else `default_sources`). One copy for every
    type (Matthias, 2026-10-30, "Yes, build it", open point C): each type's builder binds its own texts."""
    defaults = dict(joints_stated=joints_stated,
                    boards=[(computer, 1, 'Boards', 'Torso', COMPUTER, 'ITC', 'E', computer_source),
                            ('Power distribution board', 1, 'Boards', 'Torso', POWER, 'PE_HVS', 'E',
                             'as the G1 (E5.14 point 4)')],
                    joint_sources=joint_sources)
    defaults.update(more)
    return block(name, maker, height, stated, defaults.pop('sources', default_sources), mass, AVERAGE, **defaults)


def with_own_joints(b: dict, joints: list, joint_sources: str, joint_label: dict | None = None) -> dict:
    """A block of the template (template_block(), its joints AVERAGE) whose every body joint its maker's model or page
    now gives (EVIDENCE.md E14.6; Matthias, 2026-11-01, "Yes, build it"): the same block, its joints `joints` followed
    by those the template added (its hands or grippers, wheels, steering and lift motors), so that no joint of it is a
    share of its mass any more. Everything else stays as it was entered, its count of joints for the encoders and
    connectors (`joints_stated`, its maker's) too."""
    out = dict(b)
    out.update(joints=list(joints) + list(b['added_joints']), added_joints=[], stated_joints=[], averaged=None,
               joint_sources=joint_sources)
    if joint_label:
        out['joint_label'] = joint_label
    return out


# Where a joint of a maker's model sits, by the first word of its name: its heat group and body region (E14.6).
JOINT_PLACES = {'Hip': ('Hips', 'Legs'), 'Knee': ('Knees', 'Legs'), 'Ankle': ('Ankles', 'Legs'),
                'Waist': ('Waist', 'Torso'), 'Shoulder': ('Shoulders', 'Arms'), 'Elbow': ('Elbows and wrists', 'Arms'),
                'Wrist': ('Elbows and wrists', 'Arms'), 'Head': ('Elbows and wrists', 'Head')}


def model_joints(rows: list, module) -> list:
    """The body joints of a maker's model file (EVIDENCE.md E14.1): each row (name, count, torque N·m) a joint() at its
    place (JOINT_PLACES, by its name's first word), its module `module` at its torque (its type's rule: type 1's the
    torque over 87.3 N·m/kg, E5.12 point 4; else E6.8's fit), half to 1.5 times (E)."""
    return [joint(name, count, torque, module(torque), *JOINT_PLACES[name.split()[0]]) for name, count, torque in rows]


# --- A hydraulic robot's rows (EVIDENCE.md E27.7) --------------------------------------------------------------------
def isa_actuators(places: dict, version: str | dict, why: str) -> dict:
    """The hydraulic actuators of a robot as Moog's ISA of `version` ('v2' or 'v5', or a version for each place: the
    Atlas (old)'s v5 at its knees only, Matthias, 2026-11-04, "Yes, knees only", E27.8), `places` its count at each place
    (PLACES), `why` where the counts come from (E27.7 point 2): for its block, the rows of the sheets Parts (each place's
    actuators as weighed; their servo valves, 95 g each; their bodies, rods and seals the remainder), Boards (each its
    board, as the small joint's driver board) and Sensors (each a position sensor and two pressure sensors, their
    elements only, their mass in the actuator's)."""
    parts, boards, sensors = [], [], []
    for place, count in places.items():
        kind, region = PLACES[place]
        its = version[place] if isinstance(version, dict) else version
        parts += [(f'Hydraulic actuators, {place}', count, kind, region, spread(ISA_KG[its]), None, None, 'S',
                   f'{why}; as Moog\'s ISA {its}: FRO Table 2 "Dry weight 920 g 1,600 g", ± 5 %', ACTUATORS_STATED),
                  (f'Servo valves, {place}', count, kind, region, spread(VALVE_KG), None, None, 'S',
                   'MOO "Mass: 95 g (3.35 oz)", ± 5 % (E27.7 point 2.2)'),
                  (f'Actuator bodies, rods and seals, {place}', count, kind, region, (None, None, None), None, None,
                   'S, E', 'SEM19 "3D-printed Titanium body"; the remainder (E27.7 point 2.5)', ACTUATOR_BODY)]
        boards.append((f'Actuator boards, {place}', count, kind, region, DRIVER_BOARD_AREA, 'PE_HVS', 'W, E',
                       'SEM19 "Electronic boards": as the small joint\'s driver board, the G1\'s weighed (E27.7 point '
                       '2.3)'))
        sensors += [(f'Actuator position sensors, {place}', count, kind, region, None, 'S',
                     'SEM19 "Position sensor"; elements only, in the actuator (E27.7 point 2.4)',
                     [('position sensor', 1)]),
                    (f'Actuator pressure sensors, {place}', 2 * count, kind, region, None, 'S, E',
                     'SEM19 "Pressure sensors", one for each of the cylinder\'s two chambers (E); elements only, in the '
                     'actuator (E27.7 point 2.4)', [('pressure sensor', 1)])]
    return dict(parts=parts, boards=boards, sensors=sensors)


def hoses(kg: tuple, source: str) -> tuple:
    """A hydraulic robot's hoses on the robot (E27.7 point 9.10): plastics, of `kg` (min, mode, max), an estimate."""
    return 'Hydraulic hoses', 1, HYDRAULICS, 'Whole body', kg, 'Plastics', None, 'E', source


def robot_rows(b: dict, robot_type: int, averaged_joints: list | None = None) -> dict:
    """Every row of one robot's block on the sheets Robots, Joints, Parts, Boards, Sensors and Constants, and the car
    sensor elements of its sensors (sheet SensorElements, by the sensor's name). `robot_type` is the type of its file;
    `averaged_joints` (average_joints() of the type's batch 1) are the joints of a block whose joints are AVERAGE."""
    name = b['name']
    out = {sheet: [] for sheet in ('Robots', 'Joints', 'Parts', 'Boards', 'Sensors', 'Constants', 'SensorElements')}
    out['Robots'].append((name, b['maker'], robot_type, b['height'], b['stated'], b['sources']))

    # Its joints, their modules and driver boards, and two encoders and two connectors per joint. A robot of the
    # template: the template's rows, its stated joints in place of their groups' rows, and its hands or grippers.
    averaged = b['joints'] == AVERAGE
    joints = template_joints(b, b['averaged'] or averaged_joints) if averaged else b['joints']
    for number, (joint_name, count, size, torque, masses, heat, region, *share) in enumerate(joints, start=1):
        low, mode, high = masses or (None, None, None)
        out['Joints'].append((name, number, joint_name, count, size, torque, low, mode, high,
                              share[0] if share else None, 'not stated', heat, region, b['joint_sources'],
                              MAGNETS_BASIS))
    in_robot = b['joints_stated'] or sum(j[1] for j in joints)   # 0: a robot without an electric joint (Atlas (old))
    for size in ('small', 'large'):
        mine = [j for j in joints if j[2] == size]
        if mine:
            count, where = sum(j[1] for j in mine), regions(mine)
            shares = [len(j) > 7 for j in mine]   # a row of the template carries its share as an eighth item
            basis = JOINT_SHARES if all(shares) else JOINT_MIXED if any(shares) else JOINT_MASSES
            out['Parts'].append((name, f'Joint module, {size}', count, 'In the joints', where, None, None, None, None,
                                 None, basis, b['joint_label'][size], b['joint_sources']))
            out['Boards'].append((name, f'Driver board, {size} joint', count, 'In the joints', where, None, None, None,
                                  DRIVER_FROM, 'PE_HVS', 'E', 'as the G1 (E5.12 point 2)'))
    label, source = b['encoders']
    if in_robot:
        out['Parts'].append((name, 'Encoders (two per joint)', 2 * in_robot, 'In the joints', 'as their joints', None,
                             None, None, None, None, 'Sensors and SensorElements (Encoder)', label, source))
        out['Sensors'].append((name, 'Encoder', 2 * in_robot, 'In the joints', 'as their joints', None, None, None,
                               label, f'{source}; elements only'))
        for car_type, per_sensor in ENCODER:
            out['SensorElements'].append(('Encoder', car_type, per_sensor))

    # Its battery: the pack, its cells from their energy, its housing the pack's remainder (a pack no source weighs: a
    # share of its cells, E20), its management board; in its torso, or for a robot on wheels in its base; its cells NMC
    # unless its block names their recipe. A robot that carries no battery has none of these rows (02 then draws no
    # battery for it, EVIDENCE.md E16.2).
    region = b['battery_region']
    if not b['battery']:
        pass
    elif b['pack'] == PACK_CELLS_ONLY:
        out['Parts'].append((name, 'Battery pack', 1, 'Battery pack', region, None, None, None, None, None,
                             PACK_CELLS_ONLY, 'S', b['pack_source']))
    elif b['pack'] is None:
        out['Parts'].append((name, 'Battery pack', 1, 'Battery pack', region, None, None, None, None, None,
                             PACK_FROM_ENERGY, 'S, E',
                             'its mass not stated (E5.14 point 3)' + ('; its cells not NMC (E9.8)' if b['cell_recipe']
                                                                      else '')))
    else:
        (low, mode, high), label, source = b['pack']
        out['Parts'].append((name, 'Battery pack', 1, 'Battery pack', region, low, mode, high, None, None,
                             PACK_STATED, label, source))
    if b['battery']:
        label, source = b['cells']
        out['Parts'].append((name, 'Battery cells', 1, 'Battery pack', region, None, None, None, 'Battery cells',
                             b['cell_recipe'], (CELLS_FROM_CHARGE if b['voltage'] else CELLS_FROM_MASS).format(
                                 CELL_OF_RECIPE if b['cell_recipe'] else NMC_CELL), label, source))
        if b['housing']:
            if b['pack'] is None:
                out['Parts'].append((name, b['housing'], 1, 'Battery pack', region, None, None, None, None, None,
                                     HOUSING_OF_CELLS, 'E', 'E5.19 point 1; a share of its cells (E20)'))
            else:
                out['Parts'].append((name, b['housing'], 1, 'Battery pack', region, None, None, None, None, None,
                                     HOUSING, 'E', 'E5.19 point 1'))
        out['Boards'].append((name, 'Battery management board', 1, 'Battery pack', region, *BATTERY_BOARD,
                              'area times Constants board mass per cm2', 'BMS', 'E', 'as the G1 (E5.14 point 4)'))

    # Its other boards and its sensors, as its sources name them.
    for board, count, kind, region, area, category, label, source in b['boards']:
        out['Boards'].append((name, board, count, kind, region, *area, 'area times Constants board mass per cm2',
                              category, label, source))
    # The cameras E31 found for a robot whose parts named none (EVIDENCE.md E31, "Yes, A to H"): as their source states
    # them (points 1 and 2), or a row without a number whose number 02 draws (point 3) and, where a source names a
    # microphone or speech, a microphone array of four.
    estimated = []
    if name in CAMERAS_ESTIMATED:
        estimated.append((ESTIMATED_CAMERAS, None, 'Head', 'Head', None, 'E', CAMERAS_NUMBER_SOURCE, CAMERA))
        if CAMERAS_ESTIMATED[name]:
            estimated.append(microphones(f'E31 point 3: its sources name {CAMERAS_ESTIMATED[name]}'))
    for sensor, count, kind, region, grams, label, source, units in (b['sensors'] + CAMERAS_STATED.get(name, [])
                                                                     + estimated):
        out['Sensors'].append((name, sensor, count, kind, region, *(grams or (None, None, None)), label, source))
        for car_type, per_sensor in units or []:
            out['SensorElements'].append((sensor, car_type, per_sensor))

    # Its cables and connectors, screws and other parts, shell and frame.
    out['Parts'].append((name, 'Cable conductors and insulation', 1, 'Cables', 'Whole body', None, None, None, None,
                         None, 'from Constants: length, cross-sections, insulation', b['cables'][1], b['cables'][2]))
    label, source = b['connectors']
    if in_robot:
        out['Parts'].append((name, 'XT30 (2+2) connectors (two per joint)', 2 * in_robot, 'Cables', 'Whole body',
                             *CONNECTOR_KG, None, None, None, label, source))
    for part, count, kg, grade, label, source in b['screws']:
        out['Parts'].append((name, part, count, 'Frame and shell', 'Whole body', *kg, steel_of(grade), grade, None,
                             label, source))
    for part, count, kind, region, kg, material, grade, label, source, *computed in b['cooler'] + b['parts']:
        out['Parts'].append((name, part, count, kind, region, *kg, material, grade, computed[0] if computed else None,
                             label, source))
    if b['oil']:
        # A hydraulic robot's oil (EVIDENCE.md E27.7 point 6): its volume in Constants, its density the file's.
        values, label, source = b['oil']
        out['Parts'].append((name, 'Hydraulic oil', 1, HYDRAULICS, 'Whole body', None, None, None, 'Other', None, OIL,
                             label, source))
    if b['lift_column']:
        # Its lift column beside its motor (a joint): its stated mass, or a share of the robot's mass less its motor.
        kg, label, source = b['lift_column']
        out['Parts'].append((name, LIFT_PART, 1, 'Lift column', 'Torso', *(kg or (None, None, None)), None, None,
                             None if kg else LIFT, label, source))
    if b['shell']:
        shell, source = b['shell']
        out['Parts'].append((name, shell, 1, 'Frame and shell', 'Whole body', None, None, None, 'Plastics', None, SHELL,
                             'E', source))
    frame, material, source, *grade = b['frame']
    out['Parts'].append((name, frame, 1, 'Frame and shell', 'Whole body', None, None, None, material,
                         grade[0] if grade else None, FRAME, 'E', source))

    # Its own constants: its mass, its battery's voltage and capacity (or none: its energy per kg of robot), its cables.
    values, label, source = b['mass']
    out['Constants'].append((name, 'Robot mass, with battery', *values, 'kg', label, source))
    if b['voltage']:
        for quantity, unit, (values, label, source) in (('Battery voltage', 'V', b['voltage']),
                                                         ('Battery capacity', 'Ah', b['capacity'])):
            out['Constants'].append((name, quantity, *values, unit, label, source))
    values, label, source = b['cables']
    out['Constants'].append((name, b['cable_quantity'], *values, 'm', label, source))
    if b['oil']:
        values, label, source = b['oil']
        out['Constants'].append((name, OIL_VOLUME, *values, 'l', label, source))
    if name in CAMERAS_ESTIMATED:   # E31 point 3: the number of its cameras, drawn by 02 as a whole number
        out['Constants'].append((name, NUMBER_OF + ESTIMATED_CAMERAS, *CAMERAS_NUMBER, 'image sensors', 'E',
                                 CAMERAS_NUMBER_SOURCE))
    return out


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


def sensor_elements(given: list, rows: list) -> list:
    """The sheet SensorElements: the rows `given` (a builder's own, by the sensor's name), then the car sensor elements
    of the generated robots' sensors (`rows`, robot_rows()'s 'SensorElements'), each sensor once; a sensor named twice
    must be made of the same elements."""
    known = {r[0]: [] for r in given}
    for r in given:
        known[r[0]].append(r[1:])
    new: dict = {}
    for sensor, car_type, units in rows:
        new.setdefault(sensor, [])
        if (car_type, units) not in new[sensor]:
            new[sensor].append((car_type, units))
    for sensor, units in new.items():
        if sensor in known and sorted(known[sensor]) != sorted(units):
            raise ValueError(f'{sensor}: named with other elements than in the rows given.')
    return list(given) + [(sensor, *u) for sensor, units in new.items() if sensor not in known for u in units]


def sheets(robots: list, joints: list, parts: list, boards: list, sensors: list, elements: list, constants: list,
           sources: list) -> list:
    """Every sheet after About, in the order of the file: its name, first row, rows and column widths. The robots' own
    rows are a builder's; MagnetGrades, JointParts and Shares are the one set for all, Shares only the rows of a
    component of JointParts or a part of `parts` (01 faults a share of a part the file does not have). The sources of
    E31 (E31_SOURCES) that the file's rows cite follow the builder's own `sources`, each once."""
    named = {r[0] for r in JOINTPARTS_ROWS} | {r[1] for r in parts}
    cited = ' '.join(str(cell) for rows in (robots, parts, boards, sensors, constants) for row in rows for cell in row
                     if cell)
    sources = list(sources) + [row for code, row in E31_SOURCES.items()
                               if re.search(rf'(?<![\w-]){re.escape(code)}(?![\w-])', cited)]
    return [
        ('Robots', ROBOTS_HEADINGS, robots, ROBOTS_WIDTHS),
        ('Joints', JOINTS_HEADINGS, joints, JOINTS_WIDTHS),
        ('MagnetGrades', MAGNETGRADES_HEADINGS, MAGNETGRADES_ROWS, MAGNETGRADES_WIDTHS),
        ('JointParts', JOINTPARTS_HEADINGS, JOINTPARTS_ROWS, JOINTPARTS_WIDTHS),
        ('Parts', PARTS_HEADINGS, parts, PARTS_WIDTHS),
        ('Shares', SHARES_HEADINGS, [r for r in SHARES_ROWS if r[0] in named], SHARES_WIDTHS),
        ('Boards', BOARDS_HEADINGS, boards, BOARDS_WIDTHS),
        ('Sensors', SENSORS_HEADINGS, sensors, SENSORS_WIDTHS),
        ('SensorElements', SENSORELEMENTS_HEADINGS, elements, SENSORELEMENTS_WIDTHS),
        ('Constants', CONSTANTS_HEADINGS, constants, CONSTANTS_WIDTHS),
        ('Sources', SOURCES_HEADINGS, sources, SOURCES_WIDTHS),
    ]


def type_output_path(folder: str) -> str:
    """Where a robot type's file goes: 00's setting `data.parts_taken_apart` with the type's folder ('<n>_<name>', the
    folder its builder sits in), as an absolute path."""
    return absolute(Params().data.parts_taken_apart.format(folder=folder))


def write_file(path: str, about: list, all_sheets: list) -> None:
    """Write the whole file to `path` (its folder made where it is not there): the About sheet first, its lines
    `about`, then every sheet of `all_sheets` (sheets()) in its order."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    book = openpyxl.Workbook()
    sheet = book.active
    sheet.title = 'About'
    for row, line in enumerate(about, start=1):
        if line is not None:
            sheet.cell(row=row, column=1, value=line)
    sheet['A1'].font = Font(bold=True)
    sheet.column_dimensions['A'].width = ABOUT_WIDTH
    for name, headings, rows, widths in all_sheets:
        write_sheet(book, name, headings, rows, widths)
    book.save(path)
