"""
Builder of data/researched/2_full_scale_general_purpose_ai_research/parts_taken_apart.xlsx: the robots of type 2 taken
apart so far, part by part.

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

Matthias, 2026-10-29: "commit and push and then to typ 2", then "Yes, as proposed" (A: every robot of type 2 its own
rows, in batches; C: a parts file and builder per type); 2026-10-30: "Yes, all three" (EVIDENCE.md E6.6), "Yes, agree
E6.8" (the proposal for batch 1, points 1 to 13), "Yes, build C"; for batch 2 "Yes, all six" (E7.3), "Yes, agree E7.4"
(type 2's own template), "Yes, agree E7.5", "Yes, build it"; for batch 2b "Yes, all six" (E8.2), "Yes, agree E8.3",
"Yes, build it"; for the robots on wheels "Yes, all five" (E9.2), "Yes, 79 / 80 / 95" (E9.3), "Yes, agree E9.4", "Yes,
agree E9.6", "Yes, build it" (E9.7, its open points A to D as recommended).

WHAT IT DOES
------------
It writes the data file of the robots of type 2 taken apart so far, each part by part, as type 1's builder writes
type 1's (the same sheets, the same machinery in tools/parts_taken_apart.py): batch 1, the five robots whose makers
publish a model file, the Unitree H2, H2 Plus and H1-2 and the Fourier GR-2 and GR-1 (EVIDENCE.md E3, "Those with model
files"), the GR-1 in two versions (one or two depth cameras); batch 2, 24 robots not on wheels (E7.5), the H2-X in
two versions (its second computer an Intel Core i7 or an Orin NX); batch 2b, the 24 others not on wheels (E8.3), the
Walker Tienkung in two versions ("Voice & Vision", "Embodied intelligence"); and the 43 robots on wheels (E9.6), the
AICO 2, the RB-Y1 and the R1-D in two versions each: 96 of type 2's 97 robots, all but the Xialan S0, which has no mass
in any source. Each block gives what the robot's own sources give
(E6.1 to E6.7, E7.1) and, where they stop, what E6.8 and E7.5 agreed: each joint's mass from its torque by type 1's
fit refit with the M107 (E6.8 point 1), its battery from its voltage and capacity (point 6), its boards and sensors by
the template (points 7 and 8), its cables scaled by its height (point 9), its shell and screws by its mass (points 10
and 11), its frame the remainder (point 12). A robot of batch 2 whose maker gives no joint torques takes type 2's own
template (E7.4): its joint modules a share of its mass, split as type 2's seven robots with every joint's torque are
on average (AVERAGE_JOINTS), its battery's energy per kg of robot where its maker gives none. A robot on wheels (E9.6)
has its drive wheels' hub motors, its steering motors and its lift column's motor as joints, its casters and lift
column as parts; one whose maker gives no joint's torque or mass takes the template on wheels (WHEELED_AVERAGE_JOINTS,
the average of the four robots on wheels with every joint), its battery in its base. Each row names its own sources.

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
                               SHARED_CONSTANTS_LAST, SHARED_SOURCES, average_joints, estimate, joint, robot_rows,
                               sensor_elements, sheets, spread, template_block, type_output_path, write_file)

# The robot type of this file, and its folder (the one this builder sits in, named as data/consolidated/'s).
ROBOT_TYPE = 2
FOLDER = os.path.basename(os.path.dirname(os.path.abspath(__file__)))

# --- About ----------------------------------------------------------------------------------------------------------
# The file's own description, one line per row of its first column (None leaves the row empty).
ABOUT = [
    'Robot type 2 part by part: 96 of its 97 robots taken apart so far (batches 1, 2 and 2b and the robots on wheels; '
    'the GR-1, the H2-X, the Walker Tienkung, the AICO 2, the RB-Y1 and the R1-D in two versions each), for where their '
    'critical materials sit',
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
    None,
    "Batch 2 (EVIDENCE.md E7.5, agreed 2026-10-30, \"Yes, agree E7.5\"; entered on \"Yes, build it\"): 24 more robots, the "
    'H2-X in two versions (its second computer an Intel Core i7 or an Orin NX). The Atom Max (as DOBOT\'s Atom), Kuavo-5, '
    "Luna and MagicBot Gen1 by their models' torques; the others by type 2's template (E7.4): the joint modules 20.2 / "
    "40.4 / 60.6 % of the robot's mass, split as type 2's seven robots with every joint's torque on average (their "
    'hands left out), the battery 14.67 Wh per kg of robot where the maker gives no energy; the JingChu\'s knees its '
    "maker's 2 kg, in place of the template's knees.",
    None,
    'The robots on wheels (EVIDENCE.md E9.6, agreed 2026-10-30, "Yes, agree E9.6"; entered on "Yes, build it", E9.7): '
    '43 robots, the AICO 2, the RB-Y1 and the R1-D in two versions each. Each drive wheel a hub motor, by the robot\'s '
    'mass per driven wheel (1.4, 3.75, 4.85 or 8.5 kg, half to 1.5 times), each steering motor 0.79 kg and each lift '
    "motor 0.89 kg (ROBOTIS's), as joints (kinds Wheeled base and Lift column); casters 0.27 kg each; a lift column 19.9 "
    "% of the robot's mass, less its motor, where its maker gives no mass. The Vega 1 Pro, RB-Y1, AI Worker and Reachy 2 "
    "by their models; the others by the template on wheels: the joint modules 7.8 / 15.6 / 23.4 % of the robot's mass, "
    'split as those four on average (their hands, wheels, steering and lift left out), the battery 10.28 Wh per kg of '
    "robot where the maker gives no energy, in the base. The CASBOT W1's cells LFP (its maker's).",
]

# --- Constants: the shared numbers, and type 2's own ----------------------------------------------------------------
# The Ethernet line of the Fourier GR-1 and GR-2 (their pages: "46V电源线和以太网线", a 46 V power line and an Ethernet
# line through every joint): eight conductors of 26 / 24 / 22 AWG, the gauges of Ethernet cables, the gauge not stated
# (E); the minimum widened from 26 AWG's 0.129 mm2 to half the mode (his rule for estimates; E6.8 point 9).
ETHERNET_CS = 'Ethernet conductor cross-section (8 conductors)'
TYPE_TWO_SHARED = [
    # Type 2's own template where a maker gives no joint torques or no battery energy (EVIDENCE.md E7.4, agreed
    # 2026-10-30, "Yes, agree E7.4"): type 2's medians, half to 1.5 times; 01 and 02 read them by these names.
    ('all', 'Joint modules, share of the robot mass', 0.202, 0.404, 0.606, 'share', 'E',
     "type 2's seven robots with every joint's torque (their body joints): 34.1 to 46.6 %, median 40.4 %; half to 1.5 "
     'times (E7.4)'),
    ('all', 'Battery energy per kg of robot', 7.335, 14.67, 22.005, 'Wh/kg', 'E',
     "type 2's twelve robots with a stated energy and mass: 8.7 to 19.3, median 14.67; half to 1.5 times (E7.4)"),
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
    # Batch 2 (EVIDENCE.md E7.1, read 2026-10-29 and 2026-10-30).
    ('AL4', 'AeiROBOT, ALICE 4 (its specification: "160cm / 45kg", 41 DoF)', 'https://eng.arobot4all.com/ALICE4',
     "Manufacturer's specification"),
    ('ATu', "DOBOT, atom_wholebody.urdf (atom-p2: arms and head, 58.91 kg; its legs' and waist's limits a placeholder "
            'of 1000 N·m) and atom_p3.urdf (its legs, 61.81 kg)', 'https://github.com/Dobot-Arm/dobot_atom_urdf',
     "Manufacturer's model files"),
    ('BOL', 'MirrorMe, Bolt (its page: 175 cm, 75 kg)', 'https://www.mirrormetech.com/cn/product_5.html',
     "Manufacturer's page"),
    ('CY1', 'Xiaomi, CyberOne (its page: 21 degrees of freedom, depth vision)', 'https://www.mi.com/cyberone',
     "Manufacturer's page"),
    ('F03', 'Figure AI, Introducing Figure 03 (2025-10-09)', 'https://www.figure.ai/news/introducing-figure-03',
     "Manufacturer's announcement"),
    ('F03m', 'Figure AI, its robot page ("61KG", 1.73 m; EVIDENCE.md E3)', 'https://www.figure.ai/figure',
     "Manufacturer's specification"),
    ('H2Xp', 'Unitree, H2-X (its parameter table)', 'https://www.unitree.com/H2-X', "Manufacturer's specification"),
    ('IGC', 'ROBROS, IGRIS-C (its specification)', 'https://www.robros.co.kr/ko/igrisc', "Manufacturer's specification"),
    ('JC1', 'JCBOT, 荆楚系列 (荆楚一号: its specification)', 'https://www.jingchurobot.cn/product_detail/1.html',
     "Manufacturer's specification"),
    ('KGp', 'PAL Robotics, Kangaroo (its technical specifications)', 'https://pal-robotics.com/robot/kangaroo/',
     "Manufacturer's specification"),
    ('K1p', 'Kepler, Forerunner K1 (its page: 178 cm, 85 kg, 40 DoF, 100 TOPS)',
     'https://www.gotokepler.com/productDetailK1?id=2', "Manufacturer's page"),
    ('K2p', 'Kepler, K2 (its page)', 'https://www.gotokepler.com/productDetailK2?id=3', "Manufacturer's page"),
    ('KU5', 'Leju, KUAVO 5 (its parameter picture, "KUAVO 5 | 5-W 基础参数")', 'https://www.lejurobot.com/en/products/kuavo-5',
     "Manufacturer's specification"),
    ('KU5u', "Leju, biped_s56.urdf (29 joints, 69.44 kg; version 5.6 by Leju's numbering, docs/robot_version版本号说明.md)",
     'https://github.com/LejuRobotics/kuavo-ros-opensource', "Manufacturer's model file"),
    ('OLp', 'LimX Dynamics, Oli (its specifications)', 'https://www.limxdynamics.com/en/products/oli/spec',
     "Manufacturer's specification"),
    ('LUp', 'LimX Dynamics, Luna (its specifications)', 'https://www.limxdynamics.com/en/products/luna/spec',
     "Manufacturer's specification"),
    ('LUu', 'LimX Dynamics, HU_L04_01.urdf (27 joints, 55.64 kg)', 'https://github.com/limxdynamics/luna-description',
     "Manufacturer's model file"),
    ('LS2', 'Lumos Robotics, LUS 2 (its specifications)', 'https://www.lumosbot.tech/products/lus2',
     "Manufacturer's specification"),
    ('MBp', 'MagicLab, MagicBot Gen1 (its page)', 'https://www.magiclab.top/en/human', "Manufacturer's page"),
    ('MBu', 'MagicLab, MAGICBOT.urdf (30 joints, 66.40 kg) and MAGICBOT_with_hand.urdf (its hands: 24 links, 1.178 '
            'kg for both)', 'https://github.com/MagiclabRobotics/magicbot-gen1_description',
     "Manufacturer's model files"),
    ('HG', 'humanoid.guide, its catalogue as read on 2026-10-28 (data/raw/humanoid_guide_2026-10-28.xlsx), through the '
           'register', 'https://humanoid.guide', 'Second-hand catalogue'),
    # Batch 2b (EVIDENCE.md E8.1, read 2026-10-30).
    ('H1mu', 'Unitree, h1.urdf (19 joints, 59.34 kg)',
     'https://github.com/unitreerobotics/unitree_ros/tree/master/robots/h1_description', "Manufacturer's model file"),
    ('OMp', 'X-Humanoid, 天工Omni (its page: "135cm/39.5kg", 31 DoF)', 'https://www.x-humanoid.com/detail/omni.html',
     "Manufacturer's specification"),
    ('TSL', "Tesla, its page of Optimus (no figures)", 'https://www.tesla.com/AI', "Manufacturer's page"),
    ('SNC', 'Sanctuary AI, its milestones (Phoenix named, no figures)', 'https://sanctuary.ai/milestones/',
     "Manufacturer's page"),
    ('PHY', "PHYBOT, its site (its logo only)", 'https://www.phybot.tech/', "Manufacturer's page"),
    ('OLu', "OpenLoong, AzureLoong.urdf (Qinglong: 31 joints, 86.14 kg)", 'https://github.com/loongOpen/loong_base',
     "Manufacturer's model file"),
    ('RCp', 'PAL Robotics, REEM-C (its page: "165 cm", "80kg", "68 DoF")', 'https://pal-robotics.com/robot/reem-c/',
     "Manufacturer's specification"),
    ('L7p', 'Robotera, 星动 L7 (its page and parameters)', 'https://www.robotera.com/#/product/L7',
     "Manufacturer's specification"),
    ('XH1', 'Robotera, 星动XHAND 1 (its parameters: "重量 1100g", 12 active joints)',
     'https://www.robotera.com/#/product/XHAND', "Manufacturer's specification"),
    ('SEp', 'EngineAI, SE01 (its page; its height and DoF on its home page)',
     'https://www.engineai.com.cn/product-se01.html', "Manufacturer's specification"),
    ('ZRT', "Zeroth Robotics, its site (no robot named Sean)", 'https://www.zeroth0.com/', "Manufacturer's page"),
    ('SIA', 'Siasun, its sites (no humanoid)', 'https://www.siasun.com/', "Manufacturer's page"),
    ('UNI', 'Unitree, its list of robots (no Superman)', 'https://www.unitree.com/', "Manufacturer's page"),
    ('TLp', 'PAL Robotics, TALOS (its page: "175 cm", "95 kg")', 'https://pal-robotics.com/robot/talos/',
     "Manufacturer's specification"),
    ('TLu', "LAAS-CNRS, talos_full_v2.urdf (a model of PAL's TALOS, 93.34 kg)",
     'https://github.com/stack-of-tasks/talos-data', 'Second-hand: a user\'s model'),
    ('THu', 'Westwood Robotics, TH02-A7-FULL.urdf (THEMIS, 37.92 kg, no torque limits)',
     'https://github.com/Westwood-Robotics/THEMIS-Simulation-Model', "Manufacturer's model file"),
    ('XHN', 'X-Humanoid, its list of robots (天工3.0, 天轶2.0, 天工Omni)', 'https://www.x-humanoid.com/',
     "Manufacturer's page"),
    ('TLB', 'Tlibot, T1 双足人形机器人 (its parameters) and its list of humanoids',
     'https://www.tlibot.com/product_detail/36.html', "Manufacturer's specification"),
    ('TK2u', 'X-Humanoid, tiangong2.0_pro_urdf.urdf (Tien Kung 2.0: 30 joints, 67.96 kg)',
     'https://github.com/Open-X-Humanoid/TienKung_URDF', "Manufacturer's model file"),
    ('TK3p', 'X-Humanoid, 具身天工3.0 (its parameter picture)', 'https://www.x-humanoid.com/detail/jstg.html',
     "Manufacturer's specification"),
    ('DRU', 'DroidUp, 双足人形机器人—行者二号 (its parameters)', 'https://www.droidup.com/product/2',
     "Manufacturer's specification"),
    ('WTp', 'UBTECH, Walker Tienkung (its specification picture, two versions)',
     'https://www.ubtrobot.com/en/ai-education/products/walker-tienkung', "Manufacturer's specification"),
    ('WTu', 'tienkungrobotics, walker_tienkung.urdf (20 joints, 61.76 kg; its owner not stated)',
     'https://github.com/tienkungrobotics/Walker-TienKung-URDF', 'Model file, owner not known'),
    # The robots on wheels (EVIDENCE.md E9.1 to E9.5, read 2026-10-30).
    ('AGA2', 'AgiBot, its address of the A2-W (now the A2 flagship; the A2-W no longer listed)',
     'https://www.agibot.com.cn/products/A2_W', "Manufacturer's page"),
    ('AGG1', 'AgiBot, AGIBOT G1 (its page: "150kg", "130~180cm", "20 DoF")', 'https://agibot.com/products/G1',
     "Manufacturer's specification"),
    ('AGG2m', 'AgiBot, 精灵G2 产品用户手册 (2.3 整机参数: "重量 185 kg", "1652Wh（34Ah）")',
     'https://www.agibot.com.cn/filepage/362.html', "Manufacturer's user manual"),
    ('RBT', 'ROBOTIS, AI Worker hardware (FFW-SG2: "90 kg", "25V, 80Ah (2,040Wh)", its actuators)',
     'https://ai.robotis.com/ai_worker/hardware_ai_worker.html', "Manufacturer's specification"),
    ('RBTe', 'ROBOTIS e-manual, DYNAMIXEL-Y, -P, -X (YM080-230-R099-RH 1,200 g; YM070-210 790 g; PH42-020-S300-R '
             '340 g; XH540-V150-R 165 g; XH430-V210-R 82 g; YM080-230-B001-RH 890 g)',
     'https://emanual.robotis.com/docs/en/dxl/y/', "The actuators' maker's datasheets"),
    ('RBTm', 'ROBOTIS, ffw_sg2.xml (the AI Worker FFW-SG2: 94.42 kg; its drive links 3.80 kg, its lift link 17.9 kg)',
     'https://github.com/ROBOTIS-GIT/ai_worker', "Manufacturer's model file"),
    ('FLX', 'Flexiv, its robot systems (AICO 2-4 "281kg", AICO 2-10 "395kg", "Dual-wheel differential")',
     'https://flexiv.com/product/robot-system', "Manufacturer's specification"),
    ('ARId', 'PAL Robotics, ARI hardware overview and datasheet ("24V / 40VAh", arms of 5 DoF)',
     'https://docs.pal-robotics.com/edge/hardware/ari/hardware-overview', "Manufacturer's specification"),
    ('KIT', 'KIT H²T, the ARMAR family (ARMAR-7: "8-DoF" arms, "three omni-wheels")', 'https://h2t.iar.kit.edu/397.php',
     "Manufacturer's page"),
    ('ASTp', 'Astribot, Astribot S1 (its page: "80kg", "170cm"; the T1 a banner only)',
     'https://www.astribot.com/en/product', "Manufacturer's specification"),
    ('INF', 'INFIFORCE (ELU.AI), AstroDroid (AD-01 named, no figures)', 'https://infiforce.cn/robot',
     "Manufacturer's page"),
    ('HON', 'Honda, Avatar Robot (its SPEC: "1700mm", "110kg", "56 DOF", wheel 2)',
     'https://global.honda/en/RandD/field/hgrx/honda-multi-fingered-hand/avatar-robot.html',
     "Manufacturer's specification"),
    ('CAS', 'CASBOT, W1 (its parameters: "重量约260kg", "48V/25Ah", "磷酸铁锂", "2+4，两轮差速")',
     'https://casbot.tech/product/w1', "Manufacturer's specification"),
    ('RMD', 'RealMan, Dual-Arm Lift ("≈ 157 kg", "Lifting Stroke 900 mm")',
     'https://www.realman-robotics.com/en/products/dual-arm-lift.html', "Manufacturer's specification"),
    ('TAN', 'Tangible Robots, its site (Eggie not named, no figures)', 'https://tangiblerobots.ai/',
     "Manufacturer's page"),
    ('FEA', 'Feather Robotics, Feather (its technology page and spec sheet: "105 kg", "48 V", "50 Ah")',
     'https://feather.dev/technology', "Manufacturer's specification"),
    ('UNG1D', 'Unitree, G1-D (Ultimate: "Approx. 90kg", "9Ah" and "30Ah", "Diﬀerential drive")',
     'https://www.unitree.com/G1-D/', "Manufacturer's specification"),
    ('UNH2D', 'Unitree, H2-D (Flagship: "Approx. 120Kg", "48V/30Ah (1.44 kWh)", "dual-wheel differential")',
     'https://www.unitree.com/H2-D/', "Manufacturer's specification"),
    ('MGD1', 'MagicLab, MagicBot D1 ("150kg", "Total Capacity 1652Wh", "four‑steering‑wheel chassis")',
     'https://www.magiclabglobal.com/magicbots/magicbot-d1/', "Manufacturer's specification"),
    ('BWM', 'Blue Worm, Mantis Standard (its 核心参数: 1400 mm, "升降范围 550 mm", no mass)',
     'https://www.bluewormrobotics.com/products/mantis-standard', "Manufacturer's specification"),
    ('SPA', 'Spirit AI, its products (no robot named: "全向轮式底盘", "自由度达26个")', 'https://www.spirit-ai.com/product',
     "Manufacturer's page"),
    ('SNC8', 'Sanctuary AI, Phoenix Generation 8 ("It has a wheeled base"; no figures)',
     'https://sanctuary.ai/news/sanctuary-ai-releases-new-generation-of-ai-robots-for-high-quality-data-capture/',
     "Manufacturer's page"),
    ('GAL', 'Galaxea, R1 series (R1 Pro: "126 kg ... including battery", 26 DoF, Jetson AGX Orin 32GB)',
     'https://galaxea-dynamics.com/products/galaxea-r1-series-pioneering-wheeled-dual-arm-robotics',
     "Manufacturer's specification"),
    ('GALg', "Galaxea, the R1's hardware guide (\"48 V\", \"35 Ah\", \"1680 Wh\"; the R1's, not the Pro's)",
     'https://userguide-galaxea.github.io/Product_User_Guide/Guide/R1/Hardware_Guide', "Manufacturer's documentation"),
    ('UNR1', 'Unitree, R1 (R1-A5-D "Approx. 30kg", R1-A7-D "Approx. 32kg", "Chassis DOF 3")',
     'https://www.unitree.com/R1-D/', "Manufacturer's specification"),
    ('RBY', 'Rainbow Robotics, RB-Y1 (A "Total: 131kg", M "Total: 170kg", "50V, 25Ah (1,250Wh)")',
     'https://rainbow-robotics.com/en/products/rb-y1/', "Manufacturer's specification"),
    ('RBYu', 'Rainbow Robotics, rby1a model_v1.2.urdf (132.22 kg; its torque limits)',
     'https://github.com/RainbowRobotics/rby1-sdk', "Manufacturer's model file"),
    ('POL', 'Pollen Robotics, Reachy 2 and its hardware guide ("Up to 50 kg", Orbita 2D "1.900 g", 3D "950 g")',
     'https://docs.pollen-robotics.com/hardware-guide/specifications/general/', "Manufacturer's specification"),
    ('POL21', 'Pollen Robotics, the mobile base (2021: "24V, 35Ah", "6.5kg", "Aluminium, MJF 3D printed plastic '
              'parts, Steel")',
     'https://pollen-robotics.github.io/reachy-2021-docs/advanced/specifications/mobile-base-specs/',
     "Manufacturer's documentation"),
    ('RM01', 'RealMan, RealBot-01 ("≈ 125 kg", "40 Ah (BMS)", 21 DoF)',
     'https://develop.realman-robotics.com/en/wheelRobot/RealBot01/', "Manufacturer's documentation"),
    ('RML2', 'RealMan, RealBot-L2 ("≈ 120 kg", "48V 20Ah", "Lifting stroke 0.3 m")',
     'https://develop.realman-robotics.com/en/wheelRobot/RealBotL2/', "Manufacturer's documentation"),
    ('RMS2', 'RealMan, RealBot-S2 ("≈ 125 kg", "48V 20Ah", "Four-wheel steering, four-wheel drive")',
     'https://develop.realman-robotics.com/en/wheelRobot/RealBotS2/', "Manufacturer's documentation"),
    ('TPd', 'PAL Robotics, TIAGo Pro hardware overview ("Weight 95 Kg", "2 x 36 V, 20 Ah")',
     'https://docs.pal-robotics.com/edge/hardware/tiagopro/hardware-overview', "Manufacturer's documentation"),
    ('TPs', 'PAL Robotics, TIAGo Pro datasheet ("Weight 80 kg", "4x Mecanum Wheels", arms of 7 DoF)',
     'https://pal-robotics.com/datasheet/tiago-pro/', "Manufacturer's datasheet"),
    ('TOR', 'Tokyo Robotics, Torobo ("approx. 120 kg", "omni-directional mobile base")',
     'https://robotics.tokyo/technologies/torobo/', "Manufacturer's specification"),
    ('LXV', 'Lanxin Robotics, VB1, VB1-I and VB2 (their tables; no mass)', 'https://www.lanxinrobotics.com/humanoid-robots/',
     "Manufacturer's specification"),
    ('DXM', 'Dexmate, Vega 1 Pro and its spec sheet ("298 lbs (135 kg)", "Base 4 (2 steering, 2 drive)")',
     'https://www.dexmate.com/product/vega-1-pro', "Manufacturer's specification"),
    ('DXMu', 'Dexmate, vega_1p.urdf (141.00 kg; its torque limits)', 'https://github.com/dexmate-ai/dexmate-urdf',
     "Manufacturer's model file"),
    ('YQB', 'Yue Quan Bionics, 博文W-Bot 2.0 (its 产品参数: "整机重量 60kg", "电池容量2400W·h")',
     'https://www.yqbionics.com/W_Bot', "Manufacturer's specification"),
    ('YMB', 'Yunmu (YMBot), its site and its news of 2026-07-03 (D4: "双臂负载60kg"; no product pages)',
     'https://www.ymbot.com/news', "Manufacturer's page"),
    ('PSI', 'PsiBot, PsiBot-V1 (its parameters: "腰部自由度：2个", "算力平台：Thor"; no mass)',
     'https://www.psibot.ai/products_zh/product_psibot-v1_zh/', "Manufacturer's specification"),
    ('ZLT', 'ZLTECH, hub servo motors for robots (4.5" 2.9 kg to 8" 800 W 8.5 kg, their loads per pair)',
     'https://www.robotmotor.com/hub-motor/', "Component maker's catalogue"),
    ('UUM', 'UU Motor, 4" robot servo hub motor SVH4D ("Motor weight: 1.4kg")',
     'https://www.uumotor.com/4-inch-robot-brushless-servo-hub-motor.html', "Component maker's catalogue"),
    ('TEN', 'Tente, swivel castors 75 mm (5920UAP075L51-10 "Overall weight 0.18 kg"; 1470PAO075P40 0.27 kg)',
     'https://www.tente.com/en-sg/swivel-castor-75-mm/1470pao075p40-tente', "Component maker's catalogue"),
    ('ORM', "Oriental Motor, EL series lifting columns (20.4 to 30.5 kg for 50 to 300 mm)",
     'https://catalog.orientalmotor.com/viewitems/-linear-actuator-dc-input-electric-lifting-columns/'
     'lifting-columns-el-series-electric-lifting-columns', "Component maker's catalogue"),
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
    return ('Main board fan', count, 'Boards', 'Torso', FAN_KG, None, None, 'E',
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
    ('Computer board PC1, Intel Core i5 (motion control)', 1, 'Boards', 'Torso', COMPUTER, 'ITC', 'E',
     "H2d (10 cores, 8 GB); as the X1's and N1's computer boards (E6.8 point 7)"),
    ('Computer board PC2, Intel Core i7 (development)', 1, 'Boards', 'Torso', COMPUTER, 'ITC', 'E',
     "H2d (10 cores, 16 or 32 GB); as the X1's and N1's computer boards (E6.8 point 7)"),
    POWER_BOARD]
H2_MICROPHONES = ('Microphone array (4 microphones)', 1, 'Head', 'Head', MICROPHONES_G, 'E',
                  'H2p "Array Microphone"; as the G1\'s four (E6.8 point 8)', MICROPHONES)
H2_SPEAKER = ('Speaker, high-power', 1, 'Head', 'Head', SPEAKER_G, 'E', 'H2p "High-Power Speaker"; as the G1\'s (E6.8 '
                                                                         'point 8)', [])
H2_IMUS = ('Motion sensor (IMU), torso and pelvis', 2, 'Boards', 'Torso', IMU_G, 'E',
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
        ('Compute module PC3, NVIDIA Jetson Thor T5000', 1, 'Boards', 'Torso', estimate(87), 'ITC', 'E',
         "H2d (its camera on PC3, GMSL2); as the AGX Orin's 100 × 87 mm, the Thor's size not read (E6.8 point 7)"),
        ('Carrier board of the Jetson Thor', 1, 'Boards', 'Torso', (50, 100, 150), 'ITC', 'E',
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
    boards=[('Computer board PC1, Intel i5-1235U (motion control)', 1, 'Boards', 'Torso', COMPUTER, 'ITC', 'E',
             "H1d; as the X1's and N1's computer boards (E6.8 point 7)"),
            ('Computer board PC4, Intel i7-1255U or i7-1265U (development)', 1, 'Boards', 'Torso', COMPUTER,
             'ITC', 'E', "H1d; as the X1's and N1's computer boards (E6.8 point 7)"),
            POWER_BOARD],
    cooler=[fans(2, 'its two Intel computers'), x86_sinks(2)],
    sensors=[('LiDAR, Livox Mid-360', 1, 'Head', 'Head', (265, 265, 265), 'S', 'H1d "MID-360 Lidar"; L1 (265 g)',
              LIDAR),
             ('Depth camera, Intel RealSense D435', 1, 'Head', 'Head', D435_G, 'S',
              'H1d "D435 depth camera"; Intel D400 datasheet, D435 75 g (second-hand), as the G1', DEPTH_CAMERA),
             ('Motion sensor (IMU)', 1, 'Boards', 'Torso', IMU_G, 'E', "H1u imu_link; as the G1's (E6.8 point "
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
    boards=[('Computer board, Intel Core i7 (14 cores)', 1, 'Boards', 'Torso', COMPUTER, 'ITC', 'E',
             "GR2a \"14核高性能CPU\"; as the X1's and N1's computer boards (E6.8 point 7)"),
            ('Perception board, 8-core ARM', 1, 'Boards', 'Torso', COMPUTER, 'ITC', 'E',
             "GR2a (E3); as the X1's and N1's computer boards (E6.8 point 7)"),
            POWER_BOARD],
    cooler=[fans(2, 'its Intel computer and its ARM board'), x86_sinks(1), ARM_SINK],
    sensors=[('Binocular camera', 1, 'Head', 'Head', STEREO_CAMERA_G, 'E',
              'GR2a "双目摄像头"; its mass not stated: as a D435, a stereo camera too (E6.8 point 8)', STEREO),
             ('Motion sensor (IMU), 6-axis', 1, 'Boards', 'Torso', IMU_G, 'E', 'GR2a "IMU 6轴"; as the G1\'s',
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
        boards=[('Computer board, Intel Core i7-13700H (ASUS PN64 mini PC)', 1, 'Boards', 'Torso', COMPUTER,
                 'ITC', 'E', "GR1a; as the X1's and N1's computer boards (E6.8 point 7)"),
                ('Switch board (8 Ethernet ports)', 1, 'Boards', 'Torso', (30, 60, 90), 'ITC', 'E',
                 'GR1a "交换模块配有8个标准千兆以太网接口"; as the N1\'s network switch board (E6.8 point 7)'),
                ('Motion control unit', 1, 'Boards', 'Torso', (30, 60, 90), 'ITC', 'E',
                 "GR1a \"主运动控制单元\"; as the X1's control boards (E6.8 point 7)"),
                ('Power management module', 1, 'Boards', 'Torso', POWER, 'PE_HVS', 'E',
                 'GR1a "电源管理模块"; as the G1\'s power distribution board (E6.8 point 7)')],
        cooler=X86_COOLER,
        sensors=[('Depth camera, Intel RealSense (its model not named)', cameras, 'Head', 'Head', estimate(75), 'E',
                  'GR1a "Realsense"; as a D435, 75 g, half to 1.5 times; one or two, each as often (E6.8 point 8)',
                  DEPTH_CAMERA),
                 ('Motion sensor (IMU)', 1, 'Boards', 'Torso', IMU_G, 'E', "GR1a \"IMU 有\"; as the G1's",
                  [('IMU', 1)])],
        encoders=('S, E', 'GR1a: an absolute encoder at every active leg joint beside its motor\'s; two per joint, as '
                          'type 1'),
        cables=(CABLES_GR1, 'E', CABLES_SOURCE), cable_quantity=CABLE_ETHERNET, screws=screws(52),
        shell=FOURIER_SHELL, frame=FOURIER_FRAME)


FOURIER_GR1_ONE, FOURIER_GR1_TWO = fourier_gr1(1), fourier_gr1(2)


# ======================================================================================================================
# Batch 2: 24 robots, one block each (EVIDENCE.md E7.1 to E7.5; agreed 2026-10-30, "Yes, agree E7.5"; entered on "Yes,
# build it"). Astribot S1, Moz1 and CUE7, on wheels, wait for the wheeled batch (E7.3, question 1).
# ======================================================================================================================

# What every robot of batch 2 has unless its block says otherwise (E7.5 points 6, 8 to 11): the cells NMC (no chemistry
# stated), one motion sensor (its maker names none: a robot that walks balances by one), the cables by its height, the
# screws by its mass, a shell of plastics, an aluminium frame.
CELLS_NOT_STATED = ('E', 'NMC cylindrical, E: no chemistry stated (E7.5 point 6)')
IMU_NOT_NAMED = ('Motion sensor (IMU)', 1, 'Boards', 'Torso', IMU_G, 'E',
                 "its maker names none: one, as every robot that walks balances by one; as the G1's (E7.5 point 8)",
                 [('IMU', 1)])
SHELL_NOT_STATED = ('Shell: plastics', 'not stated; plastics, 11.5 % of the robot (E7.5 point 10)')
FRAME_NOT_STATED = ('Frame', 'Aluminium', 'not stated; aluminium, the remainder (E7.5 point 11)')
# A robot's computer where its maker names none: one, as the X1's and N1's computer boards (E7.5 point 7).
COMPUTER_NOT_NAMED = 'Computer board (not named)'
COMPUTER_SOURCE = "its maker names none: one computer board, as the X1's and N1's (E5.17 point 3; E7.5 point 7)"
# The template's rows of type 2 name what they average (open point B), and every robot of it says so in its joints'
# sources (E7.4, E7.5 point 2).
TEMPLATE_LABEL = "as type 2's seven robots with every joint's torque on average"
TEMPLATE_SOURCES = ("no joint torques in its sources: its joint modules 20.2 / 40.4 / 60.6 % of its mass, split as "
                    "type 2's seven robots with every joint's torque are on average, their hands left out (E7.4; E7.5 "
                    'point 2)')
# A robot whose maker names no degrees of freedom and no source counts them (the Bolt): the median of the seven
# robots' body joints (27, 27, 29, 29, 30, 31, 32), for its encoders and connectors only (E).
JOINTS_MEDIAN = 29


def cables_by_height(height: float) -> tuple:
    """A robot's cables (E7.5 point 9): 8 m per metre of its height (batch 1's 14 m at 1.75 m), to the half metre, half
    to 1.5 times (E)."""
    mode = round(16 * height) / 2
    return (estimate(mode), 'E', f"8 m per metre of its height, {height:g} m, to the half metre (batch 1's 14 m at "
                                 '1.75 m), half to 1.5 times (E7.5 point 9)')


def arm_sinks(count: int) -> tuple:
    """The heat sinks of `count` ARM boards, as the G1's (E5.22; E7.5 point 7)."""
    return (ARM_SINK[0], count) + ARM_SINK[2:]


def with_defaults(height: float, mass: tuple, more: dict) -> dict:
    """What a block of batch 2 has unless `more` says otherwise (CELLS_NOT_STATED to FRAME_NOT_STATED)."""
    defaults = dict(cells=CELLS_NOT_STATED, sensors=[IMU_NOT_NAMED], cables=cables_by_height(height),
                    screws=screws(mass[0][1]), shell=SHELL_NOT_STATED, frame=FRAME_NOT_STATED)
    defaults.update(more)
    return defaults


def template(name: str, maker: str, height: float, stated: float | None, mass: tuple, joints_stated: int,
             computer: str = COMPUTER_NOT_NAMED, **more) -> dict:
    """A robot of batch 2 whose maker gives no joint torques (E7.5 point 2): the shared template_block() with type 2's
    texts and the defaults of batch 2. `joints_stated` counts its body joints and its hands (one each, as batch 1's),
    for its encoders and connectors; its joints' sources TEMPLATE_SOURCES unless `more` gives its own."""
    joint_sources = more.pop('joint_sources', TEMPLATE_SOURCES)
    return template_block(name, maker, height, stated, mass, joints_stated, computer, computer_source=COMPUTER_SOURCE,
                          joint_sources=joint_sources, default_sources='HG (the register); E7.1, E7.5',
                          **with_defaults(height, mass, more))


def own_joints(name: str, maker: str, height: float, stated: float | None, sources: str, mass: tuple, joints: list,
               **more) -> dict:
    """A robot of batch 2 with every joint's torque in its maker's model (E7.5 point 1), with the defaults of batch 2
    and one computer board where its maker names none."""
    more.setdefault('boards', [(COMPUTER_NOT_NAMED, 1, 'Boards', 'Torso', COMPUTER, 'ITC', 'E', COMPUTER_SOURCE),
                               POWER_BOARD])
    return block(name, maker, height, stated, sources, mass, joints, **with_defaults(height, mass, more))


# --- Parts named by several makers ----------------------------------------------------------------------------------
# A hand of six joints (Kuavo-5, IGRIS-C, JingChu) as Fourier's, 0.443 kg (FH1), half to 1.5 times (E7.5 point 4); one
# of eleven joints (the Kepler K2's; the K1's as the K2's) Fourier's per joint, 0.443 × 11 / 6 kg (E); as small joints.
SIX_JOINT_HAND = joint('Hand (six joints)', 2, None, estimate(0.443), 'Elbows and wrists', 'Arms', size='small')
KEPLER_HAND = joint('Hand (eleven joints)', 2, None, estimate(0.443 * 11 / 6), 'Elbows and wrists', 'Arms',
                    size='small')
# An Orin NX-sized compute module and its carrier where a maker names only its computing power (E7.5 point 7: NVIDIA's
# Orin modules give such figures, my reading, not stated).


def compute_module(power: str, source: str) -> list:
    """The module and its carrier, named by the computing power its maker states (E7.5 point 7)."""
    return [(f'Compute module, {power} (not named)', 1, 'Boards', 'Torso', estimate(ORIN_NX[1]), 'ITC', 'E',
             f"{source}; an Orin NX-sized module, 69.6 × 45 mm (E5.13), half to 1.5 times: NVIDIA's Orin modules give "
             'such figures, my reading, not stated (E7.5 point 7)'),
            ('Carrier board of the compute module', 1, 'Boards', 'Torso', COMPUTER, 'ITC', 'E',
             "as the X1's and N1's computer boards (E7.5 point 7)")]


def orin_nx_boards(named: str) -> list:
    """A Jetson Orin NX its maker names (`named`, its source's code and words first) at its size, and its carrier."""
    return [('Compute module, NVIDIA Jetson Orin NX', 1, 'Boards', 'Torso', ORIN_NX, 'ITC', 'S',
             f'{named}; 69.6 × 45 mm (E5.13), ± 5 %'),
            ('Carrier board of the Orin NX', 1, 'Boards', 'Torso', COMPUTER, 'ITC', 'E',
             "as the X1's and N1's computer boards (E7.5 point 7)")]
RK3588_BOARDS = [('Compute module, Rockchip RK3588', 1, 'Boards', 'Torso', estimate(RADXA_CM5[1]), 'ITC', 'E',
                  "its module not named: as the Radxa CM5's 55 × 40 mm, an RK3588 module, half to 1.5 times (E5.13; "
                  'E7.5 point 7)'),
                 ('Carrier board of the RK3588', 1, 'Boards', 'Torso', COMPUTER, 'ITC', 'E',
                  "as the X1's and N1's computer boards (E7.5 point 7)")]
# Sensors whose makers name their kind but not their model (E7.5 point 8): a binocular or depth camera as a D435, 75 g,
# half to 1.5 times (STEREO_CAMERA_G); a camera of one sensor and a LiDAR as type 1's of no named model (their kind's
# elements, no mass of their own).


def binocular(source: str, count: int = 1, name: str = 'Binocular camera') -> tuple:
    return (name, count, 'Head', 'Head', STEREO_CAMERA_G, 'E', f'{source}; its mass not stated: as a D435 (E7.5 point '
                                                               '8)', STEREO)


def depth_camera(source: str, count: int = 1) -> tuple:
    return ('Depth camera (not named)', count, 'Head', 'Head', STEREO_CAMERA_G, 'E',
            f'{source}; its mass not stated: as a D435 (E7.5 point 8)', DEPTH_CAMERA)


def camera(name: str, count: int, kind: str, source: str) -> tuple:
    return (name, count, kind, kind, None, 'S', f'{source}; as type 1\'s cameras of no named model (E7.5 point 8)',
            CAMERA)


def lidar(source: str) -> tuple:
    return ('LiDAR, 3D (not named)', 1, 'Head', 'Head', None, 'S',
            f"{source}; as type 1's LiDAR of no named model (E7.5 point 8)", LIDAR)


def imu(source: str, name: str = 'Motion sensor (IMU)') -> tuple:
    return (name, 1, 'Boards', 'Torso', IMU_G, 'E', f"{source}; as the G1's (E7.5 point 8)", [('IMU', 1)])


def microphones(source: str, name: str = 'Microphone array') -> tuple:
    return (name, 1, 'Head', 'Head', MICROPHONES_G, 'E', f"{source}; as the G1's four (E7.5 point 8)", MICROPHONES)


def speaker(source: str) -> tuple:
    return ('Speaker', 1, 'Head', 'Head', SPEAKER_G, 'E', f"{source}; as the G1's (E7.5 point 8)", [])


def voltage_capacity(volts: float, volt_source: str, amp_hours: float, ah_source: str, label: str = 'S') -> dict:
    """A battery's voltage (stated, or from the cells in series) and capacity, ± 5 % (E7.5 point 6)."""
    return dict(voltage=((volts, volts, volts), label, volt_source),
                capacity=(spread(round(amp_hours, 4)), 'S', f'{ah_source}; ± 5 % (E7.5 point 6)'))


# --- The four robots with every joint's torque (E7.5 point 1; the joints named by their axes in the model, D) --------
# The Atom: DOBOT's whole-body file (atom-p2) its arms and head, its legs' limits a placeholder of 1000 N·m, so the legs
# from atom_p3.urdf (the same order of joints); its waist a placeholder too: its own hip yaw's 104.16 N·m (E).
ATOM_JOINTS = [
    fitted('Hip pitch', 2, 207.76, 'Hips', 'Legs'), fitted('Hip roll', 2, 241.42, 'Hips', 'Legs'),
    fitted('Hip yaw', 2, 104.16, 'Hips', 'Legs'), fitted('Knee', 2, 213.8, 'Knees', 'Legs'),
    fitted('Ankle pitch', 2, 89.896, 'Ankles', 'Legs'), fitted('Ankle roll', 2, 89.896, 'Ankles', 'Legs'),
    fitted('Waist yaw', 1, 104.16, 'Waist', 'Torso'),
    fitted('Shoulder pitch', 2, 56, 'Shoulders', 'Arms'), fitted('Shoulder roll', 2, 36, 'Shoulders', 'Arms'),
    fitted('Shoulder yaw', 2, 36, 'Shoulders', 'Arms'), fitted('Elbow pitch', 2, 36, 'Elbows and wrists', 'Arms'),
    fitted('Elbow roll', 2, 18.6, 'Elbows and wrists', 'Arms'),
    fitted('Wrist pitch', 2, 18.6, 'Elbows and wrists', 'Arms'), fitted('Wrist yaw', 2, 18.6, 'Elbows and wrists', 'Arms'),
    fitted('Head yaw', 1, 12, 'Elbows and wrists', 'Head'), fitted('Head pitch', 1, 12, 'Elbows and wrists', 'Head')]
# The Kuavo-5: biped_s56.urdf (decided, E7.3 question 4), its joints named by their axes: in each leg x, z, y, y, y, x
# (hip roll, yaw, pitch, knee, ankle pitch, roll); in each arm y, x, z, y, z, x, y (shoulder pitch, roll, yaw, elbow,
# wrist yaw, roll, pitch); the head z, y.
KUAVO_JOINTS = [
    fitted('Hip roll', 2, 127, 'Hips', 'Legs'), fitted('Hip yaw', 2, 71, 'Hips', 'Legs'),
    fitted('Hip pitch', 2, 132, 'Hips', 'Legs'), fitted('Knee', 2, 280, 'Knees', 'Legs'),
    fitted('Ankle pitch', 2, 91.6, 'Ankles', 'Legs'), fitted('Ankle roll', 2, 68.4, 'Ankles', 'Legs'),
    fitted('Waist yaw', 1, 102, 'Waist', 'Torso'),
    fitted('Shoulder pitch', 2, 66, 'Shoulders', 'Arms'), fitted('Shoulder roll', 2, 75, 'Shoulders', 'Arms'),
    fitted('Shoulder yaw', 2, 57, 'Shoulders', 'Arms'), fitted('Elbow', 2, 75, 'Elbows and wrists', 'Arms'),
    fitted('Wrist yaw', 2, 14.1, 'Elbows and wrists', 'Arms'), fitted('Wrist roll', 2, 14.1, 'Elbows and wrists', 'Arms'),
    fitted('Wrist pitch', 2, 14.1, 'Elbows and wrists', 'Arms'),
    fitted('Head yaw', 1, 1.5, 'Elbows and wrists', 'Head'), fitted('Head pitch', 1, 12, 'Elbows and wrists', 'Head'),
    SIX_JOINT_HAND]
# The Luna: HU_L04_01.urdf, its joints named there.
LUNA_JOINTS = [
    fitted('Hip pitch', 2, 200, 'Hips', 'Legs'), fitted('Hip roll', 2, 200, 'Hips', 'Legs'),
    fitted('Hip yaw', 2, 200, 'Hips', 'Legs'), fitted('Knee', 2, 200, 'Knees', 'Legs'),
    fitted('Ankle pitch', 2, 70, 'Ankles', 'Legs'), fitted('Ankle roll', 2, 70, 'Ankles', 'Legs'),
    fitted('Waist yaw', 1, 70, 'Waist', 'Torso'), fitted('Waist roll', 1, 70, 'Waist', 'Torso'),
    fitted('Waist pitch', 1, 70, 'Waist', 'Torso'),
    fitted('Head yaw', 1, 15.8, 'Elbows and wrists', 'Head'), fitted('Head pitch', 1, 15.8, 'Elbows and wrists', 'Head'),
    fitted('Shoulder pitch', 2, 70, 'Shoulders', 'Arms'), fitted('Shoulder roll', 2, 70, 'Shoulders', 'Arms'),
    fitted('Shoulder yaw', 2, 70, 'Shoulders', 'Arms'), fitted('Elbow', 2, 30, 'Elbows and wrists', 'Arms'),
    fitted('Wrist yaw', 2, 15.8, 'Elbows and wrists', 'Arms')]
# The MagicBot Gen1: MAGICBOT.urdf, its joints named there; its hands MAGICBOT_with_hand.urdf's (24 links, 1.178 kg for
# both, its finger joints' 100 N·m a placeholder: by their mass), half to 1.5 times (E7.5 point 4).
MAGICBOT_JOINTS = [
    fitted('Hip roll', 2, 360, 'Hips', 'Legs'), fitted('Hip yaw', 2, 60, 'Hips', 'Legs'),
    fitted('Hip pitch', 2, 360, 'Hips', 'Legs'), fitted('Knee', 2, 360, 'Knees', 'Legs'),
    fitted('Ankle pitch', 2, 120, 'Ankles', 'Legs'), fitted('Ankle roll', 2, 120, 'Ankles', 'Legs'),
    fitted('Waist roll', 1, 200, 'Waist', 'Torso'), fitted('Waist yaw', 1, 100, 'Waist', 'Torso'),
    fitted('Head yaw', 1, 60, 'Elbows and wrists', 'Head'), fitted('Head pitch', 1, 60, 'Elbows and wrists', 'Head'),
    fitted('Shoulder pitch', 2, 110, 'Shoulders', 'Arms'), fitted('Shoulder roll', 2, 110, 'Shoulders', 'Arms'),
    fitted('Shoulder yaw', 2, 100, 'Shoulders', 'Arms'), fitted('Elbow', 2, 100, 'Elbows and wrists', 'Arms'),
    fitted('Wrist yaw', 2, 100, 'Elbows and wrists', 'Arms'), fitted('Wrist roll', 2, 40, 'Elbows and wrists', 'Arms'),
    fitted('Wrist pitch', 2, 40, 'Elbows and wrists', 'Arms'),
    joint('Hand (six joints, MagicLab)', 2, None, estimate(1.178 / 2), 'Elbows and wrists', 'Arms', size='small')]
TORQUES_SOURCE = ("its joints' torque limits; mass the refit at the torque, 0.0689 kg × torque^0.566, half to 1.5 "
                  'times (E6.8 point 1; E7.5 point 1)')

DOBOT_ATOM = own_joints(
    'DOBOT Atom', 'DOBOT', 1.70, None, 'ATu (DOBOT; its page answered 404); the register\'s "Atom Max" (E7.3 question '
                                       '3); E7.1',
    ((57.91, 58.91, 61.81), 'S, E', 'ATu: its whole-body model 58.91 kg the mode, its legs model 61.81 kg the max; 1 kg '
                                    "below the min (E7.5 point 5); DOBOT states none; the register's 55 kg reported"),
    ATOM_JOINTS, joint_sources='ATu: ' + TORQUES_SOURCE + "; its waist's limit a placeholder: its hip yaw's 104.16 "
                                                          'N·m (E)')
LEJU_KUAVO_5 = own_joints(
    'Leju Kuavo 5', 'Leju', 1.73, 63.5, 'KU5 (Leju), KU5u (its model, 69.44 kg); E7.1',
    ((62.5, 63.5, 69.44), 'S', 'KU5 "63.5kg"; KU5u its model 69.44 kg the max; 1 kg below the min (E7.5 point 5); '
                               "the register's 55 kg reported"),
    KUAVO_JOINTS, joint_sources='KU5u: ' + TORQUES_SOURCE + '; its hands of six joints as Fourier\'s (FH1, E)',
    boards=compute_module('100 TOPS', 'KU5 "100~2070 TOPS", its basic computer') + [POWER_BOARD],
    sensors=[depth_camera('KU5 "4*深度相机"', 4), lidar('KU5 "3d激光雷达"'), IMU_NOT_NAMED])
LIMX_LUNA = own_joints(
    'LimX Luna', 'LimX Dynamics', 1.60, 56, 'LUp (LimX Dynamics), LUu (its model, 55.64 kg); E7.1',
    ((55, 56, 57), 'S', 'LUp "56kg"; ± 1 kg; LUu its model 55.64 kg within (E7.5 point 5); the register\'s 55 kg '
                        'reported'),
    LUNA_JOINTS, joint_sources='LUu: ' + TORQUES_SOURCE + '; its standard hands fists, no joints',
    **voltage_capacity(50.4, 'LUp "Charger Output 58.8V": 14 cells in series (14 × 4.2 V), 14 × 3.6 = 50.4 V', 20,
                       'LUp "Slide-Out Battery Module (x2)", "10,000mAh" each (decided 2026-10-30, E7.3 question 5)',
                       label='S, E'),
    boards=RK3588_BOARDS + RK3588_BOARDS + [POWER_BOARD], cooler=[fans(2, 'its two RK3588 boards'), arm_sinks(2)],
    sensors=[camera('RGB camera', 1, 'Head', 'LUp "RGB Camera"'), imu('LUp "6-Axis"', 'Motion sensor (IMU), 6-axis'),
             microphones('LUp "Microphone"', 'Microphone'), speaker('LUp "Speaker"')])
MAGICLAB_MAGICBOT = own_joints(
    'MagicLab MagicBot Gen1', 'MagicLab', 1.74, 70, 'MBp (MagicLab), MBu (its models, 66.40 kg); E7.1',
    ((66.4, 70, 71), 'S', 'MBp about 70 kg; MBu its model 66.40 kg the min; 1 kg above the max (E7.5 point 5)'),
    MAGICBOT_JOINTS, joint_sources='MBu: ' + TORQUES_SOURCE + '; its hands its model\'s 1.178 kg for both, half to 1.5 '
                                                              'times (E)',
    **voltage_capacity(54, 'MBp "25 Ah (1.35 kWh)": 1350 / 25 = 54 V', 25, 'MBp "25 Ah"', label='S, E'),
    boards=compute_module('8-core CPU and 100 TOPS', 'MBp "8-core CPU", "100 TOPS"') + [POWER_BOARD],
    sensors=[lidar('MBp "3D LiDAR"'), depth_camera('MBp two depth cameras', 2),
             camera('Fisheye camera', 3, 'Head', 'MBp three fisheye cameras'), IMU_NOT_NAMED],
    shell=('Shell: PC+ABS', 'MBp "PC+ABS"; 11.5 % of the robot (E7.5 point 10)'),
    frame=('Frame', 'Aluminium', 'MBp aluminium alloy; the remainder (E7.5 point 11)'))

# The seven robots whose joints give type 2's template: every joint's torque, each robot once (the GR-1's first
# version), their hands left out (E7.4: "split as type 2's own robots on average", agreed 2026-10-30).
SEVEN = [UNITREE_H2, UNITREE_H1_2, FOURIER_GR2, FOURIER_GR1_ONE, LEJU_KUAVO_5, LIMX_LUNA, MAGICLAB_MAGICBOT]
AVERAGE_JOINTS = average_joints([dict(b, joints=[j for j in b['joints'] if not j[0].startswith('Hand')])
                                 for b in SEVEN], TEMPLATE_LABEL)


# --- The robots of the template (E7.5 point 2) -----------------------------------------------------------------------
def unitree_h2x(pc2: str) -> dict:
    """The H2-X in one of its two versions (E7.5 point 12; a discrete state, each drawn as often): its second computer
    an Intel Core i7 or an Orin NX ("PC2：Intel Core i7 Or Orin NX", one of two)."""
    intel = pc2 == 'Intel Core i7'
    second = ([('Computer board PC2, Intel Core i7', 1, 'Boards', 'Torso', COMPUTER, 'ITC', 'E',
                "H2Xp \"Intel Core i7 Or Orin NX\"; as the X1's and N1's computer boards (E7.5 point 7)")] if intel else
              [('Compute module PC2, NVIDIA Jetson Orin NX', 1, 'Boards', 'Torso', ORIN_NX, 'ITC', 'S',
                'H2Xp "Intel Core i7 Or Orin NX"; 69.6 × 45 mm (E5.13), ± 5 %'),
               ('Carrier board of the Orin NX', 1, 'Boards', 'Torso', COMPUTER, 'ITC', 'E',
                "as the X1's and N1's computer boards (E7.5 point 7)")])
    return template(
        f"Unitree H2-X {'Core i7' if intel else 'Orin NX'}", 'Unitree', 1.725, 65, ((65, 66, 70), 'S, E',
                                                          'H2Xp "65+Kg": the floor the min; the H2\'s "About 70kg" (H2p) '
                                                          'the max; the mode 1 kg above the floor (E7.5 point 5)'),
        31, sources='H2Xp (Unitree); E7.1',
        **voltage_capacity(57.6, 'H2Xp "Dual Battery Capacity: 20 Ah (1.152 kWh)": 1152 / 20 = 57.6 V, 16 cells of '
                                 '3.6 V ("Maximum Voltage: 67.2V" = 16 × 4.2 V)', 20, 'H2Xp "20 Ah", both batteries'),
        boards=[('Computer board PC1, 8-core CPU (motion control)', 1, 'Boards', 'Torso', COMPUTER, 'ITC', 'E',
                 'H2Xp "8-core high-performance CPU", not named: as the X1\'s and N1\'s computer boards (E7.5 point '
                 '7)')] + second + [POWER_BOARD],
        cooler=[fans(2, 'its two computers'), ARM_SINK, x86_sinks(1) if intel else ARM_SINK],
        sensors=[binocular('H2Xp binocular camera'), camera('Monocular camera', 1, 'Head', 'H2Xp monocular camera'),
                 IMU_NOT_NAMED],
        shell=('Shell: engineering plastic and energy-absorbing cushioning',
               'H2Xp "High-Strength Engineering Plastic + Energy-Absorbing Cushioning Material"; 11.5 % of the robot '
               '(E7.5 point 10)'),
        frame=('Frame', 'Aluminium', 'H2Xp "Aerospace-Grade Aluminum"; the remainder (E7.5 point 11)'))


AEI_ALICE_4 = template(
    'AeiROBOT ALICE 4', 'AeiROBOT', 1.60, 45, ((44, 45, 46), 'S', 'AL4 "160cm / 45kg"; ± 1 kg (E7.5 point 5); the '
                                                                  "register's Alice, 50 kg, reported (E7.3 question 3)"),
    41, 'Computer board, GENE-RAP6 (Intel)', sources='AL4 (AeiROBOT); E7.1',
    boards=[('Computer board, GENE-RAP6 (Intel)', 1, 'Boards', 'Torso', COMPUTER, 'ITC', 'E',
             "AL4 \"GENE-RAP6\"; as the X1's and N1's computer boards (E7.5 point 7)")] + orin_nx_boards(
        'AL4 "Jetson Orin NX"') + [POWER_BOARD],
    cooler=[fans(2, 'its Intel board and its Orin NX'), x86_sinks(1), ARM_SINK],
    sensors=[depth_camera('AL4 "Depth Cam"'), imu('AL4 "IMU"')])
MIRRORME_BOLT = template(
    'MirrorMe Bolt', 'MirrorMe', 1.75, 75, ((74, 75, 76), 'S', 'BOL "75kg"; ± 1 kg (E7.5 point 5)'), JOINTS_MEDIAN,
    sources='BOL (MirrorMe; its joints not counted: the median of the seven, E); E7.1')
XIAOMI_CYBERONE = template(
    'Xiaomi CyberOne', 'Xiaomi', 1.77, 52, ((51, 52, 53), 'S', 'HG "52" (the register; Xiaomi\'s launch, second-hand); '
                                                               '± 1 kg (E7.5 point 5)'),
    21, sources='CY1 (Xiaomi: "21个关节自由度"), HG; E7.1',
    sensors=[depth_camera('CY1 depth vision to 8 m'), microphones('CY1 voice; not named'), IMU_NOT_NAMED])
DEEP_ROBOTICS_DR01 = template(
    'Deep Robotics DR01', 'Deep Robotics', 1.70, 80, ((79, 80, 81), 'S', 'HG "80" (the register); ± 1 kg; Deep '
                                                                         "Robotics' page blank (E7.1)"),
    12, sources='HG (the register: 12 DoF; Deep Robotics\' page blank); E7.1')
FIGURE_03 = template(
    'Figure AI Figure 03', 'Figure AI', 1.73, 61, ((60, 61, 62), 'S', 'F03m "61KG"; ± 1 kg (E7.5 point 5); the '
                                                                      "register's 60 kg reported"),
    32, sources='F03, F03m (Figure AI), HG (30 DoF); E7.1',
    added_joints=[joint('Hand (many joints)', 2, None, estimate(0.825), 'Elbows and wrists', 'Arms', size='small')],
    sensors=[binocular('F03 its cameras, their number not stated: one binocular camera (E)'),
             camera('Camera in each palm', 2, 'Arms', 'F03 "an embedded palm camera"'),
             microphones('F03 "the microphone"', 'Microphone'), speaker('F03 "its speaker is twice the size"'),
             IMU_NOT_NAMED],
    shell=('Shell: soft textiles and multi-density foam',
           'F03 "soft textiles", "multi-density foam" (polymers, E); 11.5 % of the robot (E7.5 point 10)'))
UNITREE_H2X_INTEL, UNITREE_H2X_ORIN = unitree_h2x('Intel Core i7'), unitree_h2x('Orin NX')
HONOR_D1 = template(
    'HONOR D1', 'HONOR', 1.69, 45, ((44, 45, 46), 'S', 'HG "45" (the register); ± 1 kg; HONOR\'s page no figures '
                                                      '(E7.1)'), 25, sources='HG (the register: 25 DoF); E7.1')
SIMPLEXITY_I_SERIES = template(
    'Simplexity I-Series', 'Simplexity Robotics', 1.75, 60, ((59, 60, 61), 'S', 'HG "60" (the register); ± 1 kg'), 20,
    sources='HG (the register: 20 DoF; no page of its maker found); E7.1')
ROBROS_IGRIS_C = template(
    'ROBROS IGRIS-C', 'ROBROS', 1.54, 56, ((55, 56, 57), 'S', 'IGC "Weight 56 kg"; ± 1 kg (E7.5 point 5)'), 33,
    sources='IGC (ROBROS: 31 body joints, two hands of six); E7.1', added_joints=[SIX_JOINT_HAND],
    **voltage_capacity(48, 'IGC "17,000mAh 48V"', 17, 'IGC "17,000mAh"'),
    sensors=[binocular('IGC "RGB Stereo"'), depth_camera('IGC "Depth Camera"'),
             imu('IGC "6-Axis IMU"', 'Motion sensor (IMU), 6-axis')])
JCBOT_JINGCHU = template(
    'JCBOT JingChu', 'JCBOT', 1.70, 65, ((64, 65, 66), 'S', 'JC1 "体重约65kg"; ± 1 kg (E7.5 point 5)'), 28,
    'Compute module, 67 TOPS (not named)', sources='JC1 (JCBOT: 26 body joints, two hands of six); E7.1',
    joint_label={'small': 'E', 'large': 'S, E'},
    joint_sources=TEMPLATE_SOURCES + '; its knees JC1\'s "关节重量：2kg" each, ± 5 % (S), in place of the template\'s '
                                     'knees (E7.5 point 2)',
    stated_joints=[joint('Knee (roller-screw module)', 2, None, spread(2), 'Knees', 'Legs', size='large')],
    added_joints=[SIX_JOINT_HAND],
    **voltage_capacity(48, 'JC1 "48V20AH"', 20, 'JC1 "48V20AH"'),
    boards=compute_module('67 TOPS', 'JC1 "6核高性能CPU，32核GPU，AI算力高达67TOPS"') + [POWER_BOARD],
    sensors=[lidar('JC1 "激光雷达"'), depth_camera('JC1 "2个RGBD深度相机"', 2), imu('JC1 "6轴IMU"',
                                                                               'Motion sensor (IMU), 6-axis'),
             microphones('JC1 "麦克风阵列"'), speaker('JC1 "扬声器"')])
KAIST_HUMANOID = template(
    'KAIST Humanoid', 'KAIST DRCD Lab', 1.65, 75, ((74, 75, 76), 'S', 'HG "75" (the register); ± 1 kg'), 25,
    sources="HG (the register: 25 DoF; the lab's page no figures); E7.1")
PAL_KANGAROO = template(
    'PAL Kangaroo', 'PAL Robotics', 1.60, None, ((50, 57.5, 65), 'S', 'KGp "Weight 50-65 kg", by configuration: its '
                                                                      "middle the mode (E7.5 point 5); the register's "
                                                                      '40 kg reported'),
    28, sources='KGp (PAL Robotics: legs 6, torso 2, arms of up to 7 joints); E7.1',
    **voltage_capacity(63, 'KGp "15Ah, 63V. 976Wh"', 976 / 63, 'KGp "976Wh" at 63 V; its "15Ah" gives 945 Wh, 3 % '
                                                               'lower, inside the ± 5 %'),
    sensors=[depth_camera('KGp "4x RGB-D Cameras"', 4), imu('KGp "IMU and AHRS"')],
    cable_quantity=CABLE_ETHERNET)
KEPLER_K1 = template(
    'Kepler K1', 'Kepler', 1.78, 85, ((84, 85, 86), 'S', 'K1p "85kg"; ± 1 kg (E7.5 point 5); the register\'s '
                                                         '"Kepler", 88 kg, reported (E7.3 question 3)'),
    42, 'Compute module, 100 TOPS (not named)',
    sources="K1p (Kepler: 40 DoF, taken as its body's; its hands as the K2's, E); E7.1", added_joints=[KEPLER_HAND],
    boards=compute_module('100 TOPS', 'K1p "100 TOPS"') + [POWER_BOARD],
    sensors=[binocular('K1p visual perception, its cameras not named: one binocular camera (E)'), IMU_NOT_NAMED])
KEPLER_K2 = template(
    'Kepler K2', 'Kepler', 1.75, 75, ((74, 75, 76), 'S', 'K2p 75 kg on legs; ± 1 kg (E7.5 point 5); the register\'s '
                                                         "85 kg (the K1's) reported"),
    32, 'Compute module, 100 TOPS (not named)',
    sources='K2p (Kepler: 52 DoF with two hands of 11; roller-screw and rotary actuators); E7.1',
    added_joints=[KEPLER_HAND], boards=compute_module('100 TOPS', 'K2p "100 TOPS"') + [POWER_BOARD],
    sensors=[binocular('K2p "pure vision system", its cameras not named: one binocular camera (E)'),
             imu('K2p "inertial sensors"')])
LIMX_CL = template(
    'LimX CL', 'LimX Dynamics', 1.64, 45, ((44, 45, 46), 'S', 'HG "45" (the register); ± 1 kg; not on LimX\'s list of '
                                                              'products (E7.1)'),
    52, sources='HG (the register: 52 DoF); E7.1')
LIMX_OLI = template(
    'LimX Oli', 'LimX Dynamics', 1.65, 55, ((54, 55, 55), 'S', 'OLp "≤55kg": the stated bound the max, 1 kg below the '
                                                               'min (E7.5 point 5)'),
    33, sources='OLp (LimX Dynamics: 31 body joints, two grippers of one joint); E7.1',
    added_joints=[joint('Gripper (one joint)', 2, None, (0.41, 0.43, 0.45), 'Elbows and wrists', 'Arms',
                        size='small')],
    **voltage_capacity(50.4, 'OLp "Charger 58.8V": 14 cells in series (14 × 4.2 V), 14 × 3.6 = 50.4 V', 9.5,
                       'OLp "9,500mAh"', label='S, E'),
    boards=RK3588_BOARDS + orin_nx_boards('OLp "Orin NX (157TOPS)"') + [POWER_BOARD], cooler=[fans(2, 'its RK3588 and its Orin NX'),
                                                                   arm_sinks(2)],
    sensors=[depth_camera('OLp "Head Depth Camera", "Chest Depth Camera"', 2), lidar('OLp "LiDAR"'),
             imu('OLp "6-Axis"', 'Motion sensor (IMU), 6-axis'), microphones('OLp "Voice Interaction Module"',
                                                                            'Microphone'),
             speaker('OLp "Voice Interaction Module"')])
LUMOS_LUS2 = template(
    'Lumos LUS2', 'Lumos Robotics', 1.60, 57, ((56, 57, 58), 'S', 'LS2 "Weight 57 kg"; ± 1 kg (E7.5 point 5); the '
                                                                  "register's 65 kg reported"),
    28, sources='LS2 (Lumos: "Total DoF (Joint Modules) 28"); E7.1',
    **voltage_capacity(54, 'LS2 "Rated voltage 54 V"', 10, 'LS2 "Battery capacity 10 Ah"'),
    cells=('S', 'NMC cylindrical: LS2 "Ternary lithium battery"; the cell format E (E7.5 point 6)'),
    boards=[('Compute module, NVIDIA Jetson AGX Orin', 1, 'Boards', 'Torso', AGX_ORIN, 'ITC', 'S',
             'LS2 "NVIDIA Jetson AGX Orin"; 100 × 87 mm (E5.13), ± 5 %'),
            ('Carrier board of the AGX Orin', 1, 'Boards', 'Torso', COMPUTER, 'ITC', 'E',
             "as the X1's and N1's computer boards (E7.5 point 7)"), POWER_BOARD],
    sensors=[lidar('LS2 "3D LiDAR"'), depth_camera('LS2 "Binocular Depth Camera"'),
             microphones('LS2 "4-mic array"'), speaker('LS2 "Speaker"'), IMU_NOT_NAMED],
    frame=('Frame', 'Aluminium', 'LS2 "Material Aluminum alloy"; the remainder (E7.5 point 11)'))
VINMOTION_MOTION_2 = template(
    'VinMotion Motion 2', 'VinMotion', 1.625, None, ((60, 67.5, 75), 'S', 'HG "~60–75" (the register): the range, its '
                                                                          "middle the mode; VinMotion's page no figures "
                                                                          '(E7.1)'),
    36, sources='HG (the register: "~32–40 DoF", its middle); E7.1')
ZHEJIANG_NAVAI_I3 = template(
    'Zhejiang NAVAI-I3', 'Zhejiang Humanoid Robot Innovation Center', 1.80, 70,
    ((69, 70, 71), 'S', 'HG "70" (the register); ± 1 kg'), 44,
    sources="HG (the register: 44 DoF; its maker's page no figures in text); E7.1")
DIGIT_NEZHA_P01 = template(
    'Digit Nezha P01', 'Digit Robotics', 1.45, 65, ((64, 65, 66), 'S', 'HG "65" (the register); ± 1 kg; not on its '
                                                                       "maker's list (E7.1)"),
    54, sources='HG (the register: 54 DoF); E7.1')


# ======================================================================================================================
# Batch 2b: 24 robots, one block each (EVIDENCE.md E8.1 to E8.3; agreed 2026-10-30, "Yes, agree E8.3"; entered on "Yes,
# build it"). Torobo, VB1-I and VB2, on wheels, wait for the wheeled batch (E8.2, question 1). The template of E7.4 and
# its seven robots are unchanged (the spec's open point A).
# ======================================================================================================================

# The Walker Tienkung's joints its model leaves out (E8.3 point 1): its waist its own hip roll's 180 N·m; its
# "Embodied intelligence" version's neck and wrists the medians of type 2's seven robots with every joint's torque,
# head 15.8 and wrist 17.3 N·m (E).
WALKER_WAIST_NM, MEDIAN_HEAD_NM, MEDIAN_WRIST_NM = 180, 15.8, 17.3
# A controller its maker names by "2070" (TOPS or TFLOPS), the Omni's and Tien Kung 3.0's: as the H2 Plus's Jetson Thor
# (2070 is the Thor's figure, my reading), 87 cm², half to 1.5 times, and its carrier as the H2 Plus's (E8.3 point 7).
THOR_SIZED = [('Compute module, "2070" (not named)', 1, 'Boards', 'Torso', estimate(87), 'ITC', 'E',
               "its maker's \"2070\" read as a Jetson Thor's (my reading, not stated); as the H2 Plus's, the AGX "
               "Orin's 100 × 87 mm, half to 1.5 times (E8.3 point 7)"),
              ('Carrier board of the compute module', 1, 'Boards', 'Torso', (50, 100, 150), 'ITC', 'E',
               "as the H2 Plus's carrier board (E8.3 point 7)")]
LAAS = 'TLu, LAAS-CNRS\'s model of PAL\'s robot, second-hand (decided, E8.2 question 6)'

# --- The robots with every joint's torque (E8.3 point 1; the joints named by their place and axis, open point B) ----
# The H1: its page's peaks per joint group (H1p: hips 220, ankles 59, arms 75 N·m), its torso its model's 200 N·m, its
# knees the M107 ("Knee Torque About 360N.m", "Peak Torque Density: 189N.m/Kg": 360 N·m over 1.9 kg).
H1_JOINTS = [
    fitted('Hip yaw', 2, 220, 'Hips', 'Legs'), fitted('Hip roll', 2, 220, 'Hips', 'Legs'),
    fitted('Hip pitch', 2, 220, 'Hips', 'Legs'), joint('Knee', 2, 360, M107, 'Knees', 'Legs'),
    fitted('Ankle', 2, 59, 'Ankles', 'Legs'), fitted('Waist (torso)', 1, 200, 'Waist', 'Torso'),
    fitted('Shoulder pitch', 2, 75, 'Shoulders', 'Arms'), fitted('Shoulder roll', 2, 75, 'Shoulders', 'Arms'),
    fitted('Shoulder yaw', 2, 75, 'Shoulders', 'Arms'), fitted('Elbow', 2, 75, 'Elbows and wrists', 'Arms')]
# Qinglong: AzureLoong.urdf; its arms' joints (J_arm_l_01 to 07) named by their place in the chain.
QINGLONG_JOINTS = [
    fitted('Hip roll', 2, 320, 'Hips', 'Legs'), fitted('Hip yaw', 2, 160, 'Hips', 'Legs'),
    fitted('Hip pitch', 2, 396, 'Hips', 'Legs'), fitted('Knee', 2, 396, 'Knees', 'Legs'),
    fitted('Ankle pitch', 2, 58.5, 'Ankles', 'Legs'), fitted('Ankle roll', 2, 58.5, 'Ankles', 'Legs'),
    fitted('Waist pitch', 1, 315, 'Waist', 'Torso'), fitted('Waist roll', 1, 315, 'Waist', 'Torso'),
    fitted('Waist yaw', 1, 121, 'Waist', 'Torso'),
    fitted('Head yaw', 1, 26, 'Elbows and wrists', 'Head'), fitted('Head pitch', 1, 26, 'Elbows and wrists', 'Head'),
    fitted('Shoulder 1', 2, 80, 'Shoulders', 'Arms'), fitted('Shoulder 2', 2, 80, 'Shoulders', 'Arms'),
    fitted('Shoulder 3', 2, 58, 'Shoulders', 'Arms'), fitted('Elbow', 2, 58, 'Elbows and wrists', 'Arms'),
    fitted('Wrist 1', 2, 11.5, 'Elbows and wrists', 'Arms'), fitted('Wrist 2', 2, 11.5, 'Elbows and wrists', 'Arms'),
    fitted('Wrist 3', 2, 11.5, 'Elbows and wrists', 'Arms')]
# Tien Kung 2.0: tiangong2.0_pro_urdf.urdf, its joints named there.
TIEN_KUNG_2_JOINTS = [
    fitted('Hip roll', 2, 235, 'Hips', 'Legs'), fitted('Hip pitch', 2, 330, 'Hips', 'Legs'),
    fitted('Hip yaw', 2, 235, 'Hips', 'Legs'), fitted('Knee', 2, 330, 'Knees', 'Legs'),
    fitted('Ankle pitch', 2, 55, 'Ankles', 'Legs'), fitted('Ankle roll', 2, 55, 'Ankles', 'Legs'),
    fitted('Waist yaw', 1, 91, 'Waist', 'Torso'),
    fitted('Head yaw', 1, 6.3, 'Elbows and wrists', 'Head'), fitted('Head pitch', 1, 6.3, 'Elbows and wrists', 'Head'),
    fitted('Head roll', 1, 6.3, 'Elbows and wrists', 'Head'),
    fitted('Shoulder pitch', 2, 91, 'Shoulders', 'Arms'), fitted('Shoulder roll', 2, 95, 'Shoulders', 'Arms'),
    fitted('Shoulder yaw', 2, 35, 'Shoulders', 'Arms'), fitted('Elbow pitch', 2, 35, 'Elbows and wrists', 'Arms'),
    fitted('Elbow yaw', 2, 24, 'Elbows and wrists', 'Arms'), fitted('Wrist pitch', 2, 6.3, 'Elbows and wrists', 'Arms'),
    fitted('Wrist roll', 2, 6.3, 'Elbows and wrists', 'Arms')]
# The Walker Tienkung "Voice & Vision": walker_tienkung.urdf's 20 joints and its waist (E); the "Embodied intelligence"
# version its neck, its wrists (E) and two hands of six joints beside them.
WALKER_VISION_JOINTS = [
    fitted('Hip roll', 2, 180, 'Hips', 'Legs'), fitted('Hip pitch', 2, 300, 'Hips', 'Legs'),
    fitted('Hip yaw', 2, 180, 'Hips', 'Legs'), fitted('Knee', 2, 300, 'Knees', 'Legs'),
    fitted('Ankle pitch', 2, 60, 'Ankles', 'Legs'), fitted('Ankle roll', 2, 30, 'Ankles', 'Legs'),
    fitted('Waist yaw', 1, WALKER_WAIST_NM, 'Waist', 'Torso'),
    fitted('Shoulder pitch', 2, 52.5, 'Shoulders', 'Arms'), fitted('Shoulder roll', 2, 52.5, 'Shoulders', 'Arms'),
    fitted('Shoulder yaw', 2, 52.5, 'Shoulders', 'Arms'), fitted('Elbow pitch', 2, 52.5, 'Elbows and wrists', 'Arms')]
WALKER_EMBODIED_JOINTS = WALKER_VISION_JOINTS + [
    fitted('Head yaw', 1, MEDIAN_HEAD_NM, 'Elbows and wrists', 'Head'),
    fitted('Head pitch', 1, MEDIAN_HEAD_NM, 'Elbows and wrists', 'Head'),
    fitted('Head roll', 1, MEDIAN_HEAD_NM, 'Elbows and wrists', 'Head'),
    fitted('Wrist yaw', 2, MEDIAN_WRIST_NM, 'Elbows and wrists', 'Arms'),
    fitted('Wrist pitch', 2, MEDIAN_WRIST_NM, 'Elbows and wrists', 'Arms'),
    fitted('Wrist roll', 2, MEDIAN_WRIST_NM, 'Elbows and wrists', 'Arms'), SIX_JOINT_HAND]
# TALOS: LAAS's model, its legs' joints named by their axes (z, x, y, y, y, x: hip yaw, roll, pitch, knee, ankle pitch,
# roll), its torso z and y, its head y and z, its arms' joints by their place; its two grippers its model's 1.094 kg
# each, half to 1.5 times (E8.3 point 4).
TALOS_JOINTS = [
    fitted('Hip yaw', 2, 100, 'Hips', 'Legs'), fitted('Hip roll', 2, 160, 'Hips', 'Legs'),
    fitted('Hip pitch', 2, 160, 'Hips', 'Legs'), fitted('Knee', 2, 300, 'Knees', 'Legs'),
    fitted('Ankle pitch', 2, 160, 'Ankles', 'Legs'), fitted('Ankle roll', 2, 100, 'Ankles', 'Legs'),
    fitted('Waist yaw', 1, 200, 'Waist', 'Torso'), fitted('Waist pitch', 1, 200, 'Waist', 'Torso'),
    fitted('Head pitch', 1, 8, 'Elbows and wrists', 'Head'), fitted('Head yaw', 1, 4, 'Elbows and wrists', 'Head'),
    fitted('Shoulder 1', 2, 100, 'Shoulders', 'Arms'), fitted('Shoulder 2', 2, 100, 'Shoulders', 'Arms'),
    fitted('Shoulder 3', 2, 70, 'Shoulders', 'Arms'), fitted('Elbow', 2, 70, 'Elbows and wrists', 'Arms'),
    fitted('Wrist 1', 2, 20, 'Elbows and wrists', 'Arms'), fitted('Wrist 2', 2, 8, 'Elbows and wrists', 'Arms'),
    fitted('Wrist 3', 2, 8, 'Elbows and wrists', 'Arms'),
    joint('Gripper (PAL)', 2, None, estimate(1.094), 'Elbows and wrists', 'Arms', size='small')]

UNITREE_H1 = own_joints(
    'Unitree H1', 'Unitree', 1.80, 47, 'H1p (Unitree), H1mu (its model, 59.34 kg); E8.1',
    ((46, 47, 59.34), 'S', 'H1p "About 47kg" the mode, ± 1 kg; H1mu its model 59.34 kg the max (decided, E8.2 '
                           'question 3)'),
    H1_JOINTS, joint_label={'small': 'E', 'large': 'E'},
    joint_sources=('H1p: the peak torque of each joint group ("Knee Torque About 360N.m，Hip Joint Torque About '
                   '220N.m，Ankle Torque About 59N.m，Arm Joint Torque About 75N.m"); its torso its model\'s 200 N·m; the '
                   'knees the M107 (its "Peak Torque Density: 189N.m/Kg", 360 N·m over 1.9 kg), ± 5 %; the others the '
                   'refit at their torque, half to 1.5 times (E8.3 point 1)'),
    **voltage_capacity(57.6, 'H1p "15Ah(0.864KWh)": 864 / 15 = 57.6 V, 16 cells of 3.6 V ("Max Voltage 67.2V" = 16 × '
                             '4.2 V)', 15, 'H1p "15Ah"'),
    boards=[('Computer board, Intel Core i5 (platform functions)', 1, 'Boards', 'Torso', COMPUTER, 'ITC', 'E',
             "H1p; as the X1's and N1's computer boards (E8.3 point 7)"),
            ('Computer board, Intel Core i7 (user development)', 1, 'Boards', 'Torso', COMPUTER, 'ITC', 'E',
             "H1p; as the X1's and N1's computer boards (E8.3 point 7)"), POWER_BOARD],
    cooler=[fans(2, 'its two Intel computers'), x86_sinks(2)],
    sensors=[lidar('H1p "3D LIDAR"'), depth_camera('H1p "Depth Camera"'), IMU_NOT_NAMED])
OPENLOONG_QINGLONG = own_joints(
    'OpenLoong Qinglong', 'OpenLoong', 1.65, None, 'OLu (OpenLoong\'s model, 86.14 kg; its site gives no figures); E8.1',
    ((85.14, 86.14, 87.14), 'S, E', "OLu its model's 86.14 kg, ± 1 kg (E5.14 point 1: its maker states none); the "
                                    "register's 75 kg reported (E8.2 question 3)"),
    QINGLONG_JOINTS, joint_sources='OLu: ' + TORQUES_SOURCE + '; its arms\' joints by their place in the chain')
X_HUMANOID_TIEN_KUNG_2 = own_joints(
    'X-Humanoid Tien Kung 2.0', 'X-Humanoid', 1.70, None, 'TK2u (X-Humanoid\'s model, 67.96 kg; no page of its own); '
                                                           'E8.1',
    ((66.96, 67.96, 68.96), 'S, E', "TK2u its model's 67.96 kg, ± 1 kg (E5.14 point 1); the register's 70–90 kg "
                                    'reported'),
    TIEN_KUNG_2_JOINTS, joint_sources='TK2u: ' + TORQUES_SOURCE)


def walker_tienkung(embodied: bool) -> dict:
    """The Walker Tienkung in one of its two versions (E8.2 question 4; a discrete state, each drawn as often): "Voice
    & Vision", about 61 kg, 21 DoF and one AGX Orin; "Embodied intelligence", about 73 kg, 42 DoF with its neck, wrists
    and two hands of six joints, two AGX Orin."""
    orins = 2 if embodied else 1
    joints = WALKER_EMBODIED_JOINTS if embodied else WALKER_VISION_JOINTS
    return own_joints(
        f"Walker Tienkung {'Embodied' if embodied else 'Vision'}", 'UBTECH', 1.72, 73 if embodied else 61,
        'WTp (UBTECH, its specification picture), WTu (a model of its "Voice & Vision" version); E8.1',
        ((72, 73, 74) if embodied else (60, 61, 62), 'S',
         f'WTp "About {73 if embodied else 61}kg"; ± 1 kg (E8.3 point 5); the register\'s 55 kg reported'),
        joints, joint_sources=('WTu: ' + TORQUES_SOURCE + '; its waist, not in its model, its hip roll\'s 180 N·m (E)'
                               + ('; its neck and wrists, not in its model, the medians of type 2\'s seven robots, 15.8 '
                                  'and 17.3 N·m (E); its hands of six joints as Fourier\'s (E)' if embodied else '')),
        **voltage_capacity(48, 'WTp "Voltage: 48V"', 33, 'WTp "Capacity: 30Ah + 3Ah"'),
        boards=[('Computer board, Intel Core i7 (motion control)', 1, 'Boards', 'Torso', COMPUTER, 'ITC', 'E',
                 "WTp \"CPU: Intel Core i7\"; as the X1's and N1's computer boards (E8.3 point 7)"),
                ('Compute module, NVIDIA Jetson AGX Orin', orins, 'Boards', 'Torso', AGX_ORIN, 'ITC', 'S',
                 f'WTp "NVIDIA Jetson AGX Orin{" x 2" if embodied else ""}"; 100 × 87 mm (E5.13), ± 5 %'),
                ('Carrier board of the AGX Orin', orins, 'Boards', 'Torso', COMPUTER, 'ITC', 'E',
                 "as the X1's and N1's computer boards (E8.3 point 7)"), POWER_BOARD],
        cooler=[fans(1 + orins, 'its Intel computer and its AGX Orin'), x86_sinks(1), arm_sinks(orins)],
        sensors=[imu('WTp "High-Precision IMU"'), depth_camera('WTp "RGB-D Camera x 3"', 3),
                 camera('Camera, 720p RGB', 1, 'Head', 'WTp "720p RGB Monocular Camera x 1"'),
                 ('Microphone array', 4, 'Head', 'Head', MICROPHONES_G, 'E',
                  "WTp \"Linear 4-Mic Array x 4\"; as the G1's four (E8.3 point 8)", MICROPHONES),
                 speaker('WTp "Speaker x 1"')])


PAL_TALOS = own_joints(
    'PAL TALOS', 'PAL Robotics', 1.75, 95, 'TLp (PAL Robotics), TLu (LAAS-CNRS\'s model, 93.34 kg); E8.1',
    ((93.34, 95, 96), 'S', 'TLp "95 kg"; TLu its model 93.34 kg the min; 1 kg above the max (E8.3 point 5)'),
    TALOS_JOINTS, joint_sources=LAAS + ': ' + TORQUES_SOURCE + '; its grippers its model\'s 1.094 kg each, half to 1.5 '
                                                                'times (E)',
    sensors=[imu('TLp "IMU"')], cable_quantity=CABLE_ETHERNET,
    cables=cables_by_height(1.75)[:2] + (cables_by_height(1.75)[2] + '; TLp "EtherCAT": two power conductors and an '
                                                                      'Ethernet line, as the Kangaroo (E8.3 point 9)',))

# --- The robots of the template (E8.3 point 2) ----------------------------------------------------------------------
X_HUMANOID_OMNI = template(
    'X-Humanoid Omni', 'X-Humanoid', 1.35, 39.5, ((38.5, 39.5, 40.5), 'S', 'OMp "135cm/39.5kg"; ± 1 kg (the Omni '
                                                                           'kept in type 2, decided 2026-10-30, E8.2)'),
    31, sources='OMp (X-Humanoid: 31 DoF); E8.1', boards=THOR_SIZED + [POWER_BOARD],
    sensors=[depth_camera('OMp "深度相机"'), lidar('OMp "激光雷达"'), imu('OMp "高精度 IMU"')])


def tesla_optimus(name: str, height: float, kg: float, dof: int) -> dict:
    """One of Tesla's three Optimus of the register: Tesla's page names no figure (E8.1), so the template from the
    register's mass and the catalogue's degrees of freedom."""
    return template(f'Tesla Optimus {name}', 'Tesla', height, kg, ((kg - 1, kg, kg + 1), 'S',
                                                                   f'HG "{kg:g}" (the register); ± 1 kg; Tesla\'s page '
                                                                   'no figures (E8.1)'),
                    dof, sources=f'TSL (Tesla, no figures), HG (the register: {dof} DoF); E8.1')


TESLA_OPTIMUS_GEN_3 = tesla_optimus('Gen 3', 1.80, 52, 80)
TESLA_OPTIMUS_GEN_2 = tesla_optimus('Gen 2', 1.73, 56, 22)
TESLA_OPTIMUS_V2_5 = tesla_optimus('V2.5', 1.765, 55, 65)


def from_the_register(name: str, maker: str, height: float, kg: float, dof: int, why: str) -> dict:
    """A robot whose maker gives no figure, or is not found (E8.2 question 5): the template from the register's mass
    and the catalogue's degrees of freedom (where none, the median of the seven robots, E)."""
    return template(name, maker, height, kg, ((kg - 1, kg, kg + 1), 'S', f'HG "{kg:g}" (the register); ± 1 kg; {why}'),
                    dof, sources=f'HG (the register: {dof} DoF{"" if dof != JOINTS_MEDIAN else ", E"}); {why}; E8.1')


CYAN_ROBOTICS_ORCA = from_the_register('Cyan Robotics Orca', 'Cyan Robotics', 1.60, 50, 40, 'no site of its maker')
SANCTUARY_PHOENIX = from_the_register('Sanctuary Phoenix', 'Sanctuary AI', 1.70, 70, 75,
                                      "SNC names Phoenix, no figures")
PHYBOT_M1 = from_the_register('PHYBOT M1', 'PHYBOT', 1.72, 60, 32, "PHY: its maker's site shows its logo only")
PAL_REEM_C = template(
    'PAL REEM-C', 'PAL Robotics', 1.65, 80, ((79, 80, 81), 'S', 'RCp "80kg"; ± 1 kg (E8.3 point 5)'), 68,
    sources='RCp (PAL Robotics: "68 DoF"; its hands no mass, its model not expanded); E8.1')
ROBOTERA_L7 = template(
    'Robotera L7', 'Robotera', 1.71, None, ((66.2, 67.2, 68.2), 'S', 'L7p "重量(不含灵巧手）65 KG" and its two XHAND 1 '
                                                                    'of 1.1 kg (XH1); ± 1 kg (E8.3 point 5)'),
    33, 'Computer board, x86 (80 TOPS)', sources='L7p (Robotera: 55 DoF with its hands of 12), XH1; E8.1',
    joint_label={'small': 'S, E', 'large': 'E'},
    joint_sources='XH1: its two hands "重量 1100g", ± 5 % (S); ' + TEMPLATE_SOURCES,
    added_joints=[joint('Hand (XHAND 1, twelve joints)', 2, None, spread(1.1), 'Elbows and wrists', 'Arms',
                        size='small')],
    **voltage_capacity(60, 'L7p "电池容量 60 V 15 Ah"', 15, 'L7p "15 Ah"'),
    boards=[('Computer board, x86 (80 TOPS)', 1, 'Boards', 'Torso', COMPUTER, 'ITC', 'E',
             "L7p \"80 TOPS (X86)\"; as the X1's and N1's computer boards (E8.3 point 7)"),
            ('Compute module, Orin (275 TOPS)', 1, 'Boards', 'Torso', estimate(87), 'ITC', 'E',
             'L7p "275 TOPS (Orin)": the AGX Orin\'s figure (my reading), 100 × 87 mm, half to 1.5 times (E8.3 point '
             '7)'),
            ('Carrier board of the Orin', 1, 'Boards', 'Torso', COMPUTER, 'ITC', 'E',
             "as the X1's and N1's computer boards (E8.3 point 7)"), POWER_BOARD],
    cooler=[fans(2, 'its x86 computer and its Orin'), x86_sinks(1), ARM_SINK],
    sensors=[depth_camera('L7p "深度相机"'), lidar('L7p "3D激光雷达"'), microphones('L7p "麦克风阵列"'),
             speaker('L7p "扬声器"'), IMU_NOT_NAMED])
ENGINEAI_SE01 = template(
    'EngineAI SE01', 'EngineAI', 1.70, None, ((79, 80, 81), 'S', 'HG "80" (the register; EngineAI states no mass); ± 1 '
                                                                 'kg'),
    34, sources='SEp (EngineAI: "32pcs Total DOF", taken as its body\'s, two hands of six), HG; E8.1',
    added_joints=[SIX_JOINT_HAND],
    sensors=[lidar('SEp "激光雷达"'), depth_camera('SEp "深度摄像头", "RGBD"'),
             camera('Infrared camera', 1, 'Head', 'SEp "红外摄像头"'),
             ('Speaker', 2, 'Head', 'Head', SPEAKER_G, 'E', "SEp \"扬声器×2\"; as the G1's (E8.3 point 8)", []),
             imu('SEp "运控IMU传感器"')],
    frame=('Frame', 'Aluminium', 'SEp "航空级铝材机身"; the remainder (E8.3 point 10)'))
ZEROTH_SEAN = from_the_register('Zeroth Sean', 'Zeroth Robotics', 1.55, 45, 16, "ZRT: not on its maker's site")
SIASUN_SONGXING = from_the_register('Siasun Songxing', 'Siasun', 1.65, 85, 38, "SIA: no humanoid on its maker's sites")
UNITREE_SUPERMAN = from_the_register('Unitree Superman', 'Unitree', 1.70, 45, 20, "UNI: no robot of that name at "
                                                                                 'Unitree')
WESTWOOD_THEMIS = template(
    'Westwood THEMIS', 'Westwood Robotics', 1.60, None, ((36.92, 37.92, 38.92), 'S, E',
                                                         "THu its model's 37.92 kg with its hands, ± 1 kg (its maker's "
                                                         "site down); the register's 32 kg reported"),
    32, sources='THu (Westwood\'s model TH02-A7: 30 body joints, two EN02 hands, no torque limits); E8.1',
    added_joints=[joint('Hand (EN02, three fingers)', 2, None, estimate(0.463), 'Elbows and wrists', 'Arms',
                        size='small')])
X_HUMANOID_TIANGONG_ULTRA = from_the_register('X-Humanoid TianGong Ultra', 'X-Humanoid', 1.80, 55, JOINTS_MEDIAN,
                                              'XHN: no page of it')
TLIBOT_TIANZHEN_Z1 = from_the_register('Tlibot Tianzhen Z1', 'Tlibot', 1.67, 45, JOINTS_MEDIAN,
                                       "TLB: not on its maker's list")
X_HUMANOID_TIEN_KUNG_3 = template(
    'X-Humanoid Tien Kung 3.0', 'X-Humanoid', 1.70, 64.5, ((63.5, 64.5, 65.5), 'S',
                                                           'TK3p "身高：170cm 体重：64.5kg"; ± 1 kg; the register\'s 62 kg '
                                                           'reported'),
    31, 'Computer board, main controller (4.8 GHz)', sources='TK3p (X-Humanoid, its parameter picture: 31 DoF); E8.1',
    voltage=((24, 48, 72), 'E', 'TK3p no voltage: 48 V as the Walker Tienkung\'s main and small battery, half to 1.5 '
                                'times (E8.3 point 6; as type 1\'s Booster T1, E5.14 point 2)'),
    capacity=(spread(18), 'S', 'TK3p "电池数据：15Ah+3Ah"; ± 5 % (E8.3 point 6)'),
    boards=[('Computer board, main controller (4.8 GHz)', 1, 'Boards', 'Torso', COMPUTER, 'ITC', 'E',
             "TK3p \"高性能主控4.8G主频\", an Intel-class board (E); as the X1's and N1's computer boards"),
            ] + THOR_SIZED + [POWER_BOARD],
    cooler=[fans(2, 'its main controller and its module'), x86_sinks(1), ARM_SINK],
    sensors=[depth_camera('TK3p "深度相机"'), lidar('TK3p "激光雷达"'), imu('TK3p "高精度IMU"')])
TLIBOT_T1 = template(
    'Tlibot T1', 'Tlibot', 1.60, 43, ((42, 43, 44), 'S', 'TLB "43Kg（含电池，不含皮肤）"; ± 1 kg; its skin not in it'),
    41, sources='TLB (Tlibot: "本体41个自由度"; its hip, knee, ankle 450, 281, 148 N·m, a check); E8.1',
    **voltage_capacity(48, 'TLB states its energy, "电池 1110Wh", not its voltage: 48 V only splits it into volts and '
                           'amp-hours (E8.3 point 6)', 1110 / 48, 'TLB "电池 1110Wh" at 48 V', label='S, E'))
DROIDUP_WALKER_II = template(
    'DroidUp Walker II', 'DroidUp', 1.70, 32, ((31, 32, 33), 'S', 'DRU "体重:32kg"; ± 1 kg (E8.3 point 5)'), 30,
    sources='DRU (DroidUp, 行者二号: "自由度:30DoF", tendon-driven, its joints as the G1\'s, E); E8.1',
    sensors=[depth_camera('DRU "视觉传感器（深度、红外、颜色):6组"', 6), microphones('DRU "听觉传感器:8阵列"'),
             IMU_NOT_NAMED])
WALKER_TIENKUNG_VISION, WALKER_TIENKUNG_EMBODIED = walker_tienkung(False), walker_tienkung(True)


# ======================================================================================================================
# The robots on wheels: 43 robots, 46 blocks (EVIDENCE.md E9.1 to E9.6; agreed 2026-10-30, "Yes, agree E9.4", "Yes,
# agree E9.6"; entered on "Yes, build it", E9.7, its open points A to D as recommended). The AICO 2, the RB-Y1 and the
# R1-D in two versions each; the H2-D as its Flagship, the G1-D as its Ultimate (E9.2).
# ======================================================================================================================

# A drive wheel's hub motor where no source of the robot weighs it (E9.6 point 4): by the robot's mass per driven
# wheel, each class its makers' rating per motor (E9.5), half to 1.5 times (E); inside as a joint module (the G1's joint
# scaled, though a hub motor has no gears: its steel overstated, its other materials understated).
HUB_CLASSES = [(35, 1.4, 'UUM "Motor weight: 1.4kg", 35 to 50 kg a motor'),
               (75, 3.75, 'ZLT\'s 6.5" and 8" robot hub motors, 3.40 to 4.25 kg for 100 to 150 kg a pair'),
               (100, 4.85, 'ZLT\'s 6.5" 500 W hub motor, 4.85 kg for 200 kg a pair'),
               (float('inf'), 8.5, 'ZLT\'s 8" 800 W hub motor, 8.5 kg for 300 kg a pair')]
# A steered wheel's steering motor (E9.6 point 5): ROBOTIS's YM070-210-R051-RH, the AI Worker's, "790 [g]", 16.3 N·m;
# and a lift column's motor (point 7): its YM080-230-B001-RH, "890 [g]" with a spring-applied brake.
STEERING_KG, STEERING_NM, LIFT_MOTOR_KG, LIFT_MOTOR_NM = 0.79, 16.3, 0.89, 1.24
# A caster (E9.6 point 6): Tente's steel-housed 75 mm, "0.27 kg", half to 1.5 times (E); inside by the sheet Shares.
CASTER_KG = 0.27
# A gripper named without a mass (E9.6 point 11): as ROBOTIS's RH-P12-RN, "500g", half to 1.5 times (E).
GRIPPER_KG = 0.5
# The template on wheels (E9.6 point 3): its rows name what they average.
WHEELED_TEMPLATE_LABEL = "as type 2's four robots on wheels with every joint on average"
WHEELED_TEMPLATE_SOURCES = ("its maker gives no joint's torque or mass: its joint modules 7.8 / 15.6 / 23.4 % of its "
                            "mass, split as type 2's four robots on wheels with every joint (Vega 1 Pro, RB-Y1, AI "
                            'Worker, Reachy 2) are on average, their hands, wheels, steering and lift left out (E9.6 '
                            'point 3)')
# A robot on wheels whose maker names no body joints: the median of the stated ones (E9.6; 12 to 26, median 18).
WHEELED_JOINTS_MEDIAN = 18
# A lift column whose maker gives it no mass (E9.6 point 7): 19.9 % of the robot, the AI Worker's lift link (17.9 of
# 90 kg), half to 1.5 times, less its motor.
LIFT_BY_SHARE = (None, 'E', "its maker gives no mass: 19.9 % of the robot (the AI Worker's lift link, 17.9 of 90 kg), "
                            'half to 1.5 times, less its motor (E9.6 point 7)')
TYPE_TWO_SHARED += [
    # The template on wheels (EVIDENCE.md E9.6 point 3, agreed 2026-10-30, "Yes, agree E9.6"); 01 and 02 take them for
    # a robot on wheels.
    ('all', 'Joint modules, share of the robot mass, on wheels', 0.078, 0.156, 0.234, 'share', 'E',
     "type 2's four robots on wheels with every joint (Vega 1 Pro 13.2, RB-Y1 13.9, AI Worker 14.3, Reachy 2 20.9 %): "
     'their mean, 15.6 %; half to 1.5 times (E9.6 point 3)'),
    ('all', 'Battery energy per kg of robot, on wheels', 4.62, 10.28, 22.86, 'Wh/kg', 'E',
     "the 12 robots on wheels whose makers state an energy: their median 10.28, their least 4.62 (CASBOT W1) and most "
     "22.86 (Feather), the W-Bot's 40.0 left out as the one outlier (E9.6 point 3)"),
    ('all', 'Lift column, share of the robot mass, on wheels', 0.0995, 0.199, 0.2985, 'share', 'E',
     "the AI Worker's lift link in its model, 17.9 of 90 kg; half to 1.5 times (E9.6 point 7)"),
]


def hub_motors(count: int, robot_kg: float) -> tuple:
    """The drive wheels of a robot on wheels: their hub motors by its mass per driven wheel (E9.6 point 4)."""
    load = robot_kg / count
    mode, why = next((kg, why) for limit, kg, why in HUB_CLASSES if load <= limit)
    return joint('Wheel hub motor', count, None, estimate(mode), 'Hips', 'Base', size='large'), why


def steering(count: int, stated: bool = False) -> tuple:
    """The steering motors of a robot's steered wheels: ROBOTIS's YM070-210-R051-RH, stated for the AI Worker (± 5 %),
    else as it (E)."""
    return joint('Steering motor', count, STEERING_NM, (spread if stated else estimate)(STEERING_KG), 'Waist', 'Base',
                 size='small')


def lift_motor(stated: bool = False) -> tuple:
    """The motor of a lift column: ROBOTIS's YM080-230-B001-RH, stated for the AI Worker (± 5 %), else as it (E)."""
    return joint('Lift column motor', 1, LIFT_MOTOR_NM, (spread if stated else estimate)(LIFT_MOTOR_KG), 'Waist',
                 'Torso', size='small')


def casters(count: int, kg: float = CASTER_KG, source: str = 'TEN: a 75 mm castor, 0.27 kg (E9.6 point 6)') -> tuple:
    """A robot's casters (E9.6 point 6), inside by the sheet Shares (steel and plastics)."""
    return ('Casters', count, 'Wheeled base', 'Base', estimate(kg), None, None, 'E', source)


def grippers(name: str = 'Gripper', kg: float = GRIPPER_KG, label: str = 'E') -> tuple:
    """Two grippers, as small joints: as the RH-P12-RN (E), or a stated mass ± 5 % (S)."""
    return joint(name, 2, None, (spread if label == 'S' else estimate)(kg), 'Elbows and wrists', 'Arms', size='small')


def hands(joints_each: int) -> tuple:
    """Two hands of `joints_each` joints, as Fourier's six-joint hand per joint (E7.5 point 4), as small joints."""
    return joint(f'Hand ({joints_each} joints)', 2, None, estimate(0.443 * joints_each / 6), 'Elbows and wrists', 'Arms',
                 size='small')


# Sensors of a robot's base (E9.6 point 10): its LiDAR, depth cameras and cameras of no named model as type 1's, its
# ultrasonic sensors as the car list's "ultrasonic sensor".
def base_lidar(source: str, count: int = 1) -> tuple:
    return ('LiDAR in the base (not named)', count, 'Wheeled base', 'Base', None, 'S',
            f"{source}; as type 1's LiDAR of no named model (E9.6 point 10)", LIDAR)


def base_depth_camera(source: str, count: int = 1) -> tuple:
    return ('Depth camera in the base (not named)', count, 'Wheeled base', 'Base', STEREO_CAMERA_G, 'E',
            f'{source}; its mass not stated: as a D435 (E9.6 point 10)', DEPTH_CAMERA)


def base_camera(source: str, count: int) -> tuple:
    return ('Camera in the base', count, 'Wheeled base', 'Base', None, 'S',
            f"{source}; as type 1's cameras of no named model (E9.6 point 10)", CAMERA)


def ultrasonic(source: str, count: int) -> tuple:
    return ('Ultrasonic sensor', count, 'Wheeled base', 'Base', None, 'S',
            f'{source}; as the car list\'s "ultrasonic sensor" (E9.6 point 10)', [('ultrasonic sensor', 1)])


def agx_orin(source: str, count: int = 1, label: str = 'S') -> list:
    """An NVIDIA Jetson AGX Orin its maker names (± 5 %), or one read from a figure (E), and its carrier."""
    size = AGX_ORIN if label == 'S' else estimate(87)
    return [('Compute module, NVIDIA Jetson AGX Orin', count, 'Boards', 'Torso', size, 'ITC', label,
             f'{source}; 100 × 87 mm (E5.13)' + (', ± 5 %' if label == 'S' else ', half to 1.5 times (E9.6 point 9)')),
            ('Carrier board of the AGX Orin', count, 'Boards', 'Torso', COMPUTER, 'ITC', 'E',
             "as the X1's and N1's computer boards (E9.6 point 9)")]


def intel(what: str, source: str) -> tuple:
    """An Intel (or AMD) computer board, as the X1's and N1's (E9.6 point 9)."""
    return (f'Computer board, {what}', 1, 'Boards', 'Torso', COMPUTER, 'ITC', 'E',
            f"{source}; as the X1's and N1's computer boards (E9.6 point 9)")


def thor(source: str) -> list:
    """An NVIDIA Jetson AGX Thor its maker names: as the H2 Plus's, the AGX Orin's 100 × 87 mm, half to 1.5 times, and
    its carrier (E9.6 point 9)."""
    return [('Compute module, NVIDIA Jetson AGX Thor', 1, 'Boards', 'Torso', estimate(87), 'ITC', 'E',
             f"{source}; as the H2 Plus's, the AGX Orin's 100 × 87 mm, half to 1.5 times (E9.6 point 9)"),
            ('Carrier board of the compute module', 1, 'Boards', 'Torso', (50, 100, 150), 'ITC', 'E',
             "as the H2 Plus's carrier board (E9.6 point 9)")]


def wheeled(name: str, maker: str, height: float, stated: float | None, mass: tuple, body_joints: int, *, sources: str,
            driven: int, steered: int = 0, caster_count: int = 0, lift: bool = False, added: tuple = (),
            computer: str = COMPUTER_NOT_NAMED, **more) -> dict:
    """A robot on wheels whose maker gives no joint's torque or mass (E9.6 point 3): the template on wheels for its body
    joints (WHEELED_AVERAGE_JOINTS), its hands or grippers (`added`), its drive wheels by its mass per driven wheel, its
    steering and lift motors and casters, its lift column a share of its mass, its battery in its base (its energy per kg
    of robot on wheels where its maker gives none). `body_joints` counts its body joints, for its encoders and
    connectors; its hands or grippers count one each, as batch 1's (`template`)."""
    wheel, why = hub_motors(driven, mass[0][1])
    joints = [wheel] + ([steering(steered)] if steered else []) + ([lift_motor()] if lift else [])
    sources_of_joints = (WHEELED_TEMPLATE_SOURCES + f'; its {driven} drive wheels each a hub motor as {why}, half to 1.5 '
                         'times (E9.6 point 4)' + ('; its steering and lift motors as ROBOTIS\'s (E)' if steered or lift
                                                   else ''))
    return template(name, maker, height, stated, mass,
                    body_joints + sum(hand[1] for hand in added) + driven + steered + int(lift), computer,
                    sources=sources,
                    averaged=WHEELED_AVERAGE_JOINTS, joint_sources=sources_of_joints,
                    added_joints=list(added) + joints, battery_region='Base',
                    parts=([casters(caster_count)] if caster_count else []) + more.pop('parts', []),
                    lift_column=LIFT_BY_SHARE if lift else None, **more)


def from_the_register_on_wheels(name: str, maker: str, height: float, kg: float, why: str, *, driven: int = 2,
                                caster_count: int = 2, body_joints: int = WHEELED_JOINTS_MEDIAN, **more) -> dict:
    """A robot on wheels no maker's source describes (E9.2 point 3) or with no maker's mass (point 5): the register's
    (the catalogue's) mass, ± 1 kg, labelled as the catalogue's; the template on wheels on two driven wheels and two
    casters unless more is known."""
    return wheeled(name, maker, height, kg, ((kg - 1, kg, kg + 1), 'S', f'HG "{kg:g}" (the register, the catalogue\'s); '
                                                                         f'± 1 kg; {why}'),
                   body_joints, sources=f'HG (the register); {why}; E9.1', driven=driven, caster_count=caster_count,
                   **more)


# --- The robots on wheels with every joint (E9.6 point 2): the template on wheels is their average ------------------
# The Vega 1 Pro: vega_1p.urdf's torque limits, its joints named by their place in its chain; its two driven wheels
# (3.7 kg each), two steering links (0.358 kg) and two casters (0.2 and 0.3 kg) its model's, half to 1.5 times (E).
VEGA_JOINTS = [
    fitted('Waist 1', 1, 700, 'Waist', 'Torso'), fitted('Waist 2', 1, 380, 'Waist', 'Torso'),
    fitted('Waist 3', 1, 380, 'Waist', 'Torso'),
    fitted('Head 1', 1, 6, 'Elbows and wrists', 'Head'), fitted('Head 2', 1, 2.5, 'Elbows and wrists', 'Head'),
    fitted('Head 3', 1, 6, 'Elbows and wrists', 'Head'),
    fitted('Shoulder 1', 2, 150, 'Shoulders', 'Arms'), fitted('Shoulder 2', 2, 150, 'Shoulders', 'Arms'),
    fitted('Shoulder 3', 2, 80, 'Shoulders', 'Arms'), fitted('Elbow', 2, 80, 'Elbows and wrists', 'Arms'),
    fitted('Wrist 1', 2, 25, 'Elbows and wrists', 'Arms'), fitted('Wrist 2', 2, 25, 'Elbows and wrists', 'Arms'),
    fitted('Wrist 3', 2, 25, 'Elbows and wrists', 'Arms'),
    joint('Wheel hub motor', 2, 16, estimate(3.7), 'Hips', 'Base', size='large'),
    joint('Steering motor', 2, 6, estimate(0.358), 'Waist', 'Base', size='small')]
# The RB-Y1: model_v1.2.urdf's torque limits, its six joints below the arms ("Leg 6 DOF", its model's torso) with the
# waist (E9.6 point 3); its neck its "Neck Joint Module", 1.5 kg each (S); its grippers its model's 0.533 kg (E).
RBY1_JOINTS = [
    fitted('Waist 1', 1, 270, 'Waist', 'Torso'), fitted('Waist 2', 1, 270, 'Waist', 'Torso'),
    fitted('Waist 3', 1, 270, 'Waist', 'Torso'), fitted('Waist 4', 1, 120, 'Waist', 'Torso'),
    fitted('Waist 5', 1, 120, 'Waist', 'Torso'), fitted('Waist 6', 1, 120, 'Waist', 'Torso'),
    fitted('Shoulder 1', 2, 70, 'Shoulders', 'Arms'), fitted('Shoulder 2', 2, 70, 'Shoulders', 'Arms'),
    fitted('Shoulder 3', 2, 70, 'Shoulders', 'Arms'), fitted('Elbow', 2, 40, 'Elbows and wrists', 'Arms'),
    fitted('Wrist 1', 2, 10, 'Elbows and wrists', 'Arms'), fitted('Wrist 2', 2, 10, 'Elbows and wrists', 'Arms'),
    fitted('Wrist 3', 2, 8, 'Elbows and wrists', 'Arms'),
    joint('Neck module (Rainbow)', 2, 30, spread(1.5), 'Elbows and wrists', 'Head', size='small'),
    grippers('Gripper (its model)', 0.533)]
# The AI Worker FFW-SG2: ROBOTIS's actuators by model (RBTe), ± 5 % (S); its drive links its model's 3.80 kg (E).
AI_WORKER_JOINTS = [
    joint('Shoulder 1', 2, 61.4, spread(1.2), 'Shoulders', 'Arms'),
    joint('Shoulder 2', 2, 61.4, spread(1.2), 'Shoulders', 'Arms'),
    joint('Shoulder 3', 2, 61.4, spread(1.2), 'Shoulders', 'Arms'),
    joint('Elbow', 2, 31.7, spread(0.79), 'Elbows and wrists', 'Arms'),
    joint('Wrist 1', 2, 31.7, spread(0.79), 'Elbows and wrists', 'Arms'),
    joint('Wrist 2', 2, 31.7, spread(0.79), 'Elbows and wrists', 'Arms'),
    joint('Wrist 3', 2, 5.1, spread(0.34), 'Elbows and wrists', 'Arms'),
    joint('Head pitch', 1, 6.4, spread(0.165), 'Elbows and wrists', 'Head'),
    joint('Head yaw', 1, 2.6, spread(0.082), 'Elbows and wrists', 'Head'),
    joint('Wheel drive motor', 3, None, estimate(3.80), 'Hips', 'Base', size='large'), steering(3, stated=True),
    lift_motor(stated=True), grippers('Gripper (RH-P12-RN)', label='S')]
# Reachy 2: Pollen's Orbita 2D ("Weight 1.900 g") at its shoulders and elbows, Orbita 3D ("950 g") at its wrists and
# neck, ± 5 % (S); its three omni wheels' motors by their rated 5 N·m as ZLTECH's 4.5" (2.9 kg; E).
REACHY_JOINTS = [
    joint('Shoulder (Orbita 2D)', 2, 16.5, spread(1.9), 'Shoulders', 'Arms'),
    joint('Elbow (Orbita 2D)', 2, 16.5, spread(1.9), 'Elbows and wrists', 'Arms'),
    joint('Wrist (Orbita 3D)', 2, 15, spread(0.95), 'Elbows and wrists', 'Arms'),
    joint('Neck (Orbita 3D)', 1, 15, spread(0.95), 'Elbows and wrists', 'Head'),
    joint('Wheel hub motor', 3, 5, estimate(2.9), 'Hips', 'Base', size='large'), grippers()]
# The W-Bot: its page's torques ("膝关节约 360N·m，踝关节约 160N·m，手臂关节约 60N·m"), its three hip joints at its knee's
# 360 N·m (E9.6 point 2, E); its arm "肩关节x3 + 肘关节x1 + 小臂关节x1 + 手腕关节x2".
W_BOT_JOINTS = [
    fitted('Hip 1', 1, 360, 'Hips', 'Legs'), fitted('Hip 2', 1, 360, 'Hips', 'Legs'),
    fitted('Hip 3', 1, 360, 'Hips', 'Legs'), fitted('Knee', 1, 360, 'Knees', 'Legs'),
    fitted('Ankle', 1, 160, 'Ankles', 'Legs'),
    fitted('Shoulder 1', 2, 60, 'Shoulders', 'Arms'), fitted('Shoulder 2', 2, 60, 'Shoulders', 'Arms'),
    fitted('Shoulder 3', 2, 60, 'Shoulders', 'Arms'), fitted('Elbow', 2, 60, 'Elbows and wrists', 'Arms'),
    fitted('Wrist 1 (forearm)', 2, 60, 'Elbows and wrists', 'Arms'), fitted('Wrist 2', 2, 60, 'Elbows and wrists', 'Arms'),
    fitted('Wrist 3', 2, 60, 'Elbows and wrists', 'Arms'), hub_motors(2, 60)[0]]


def on_wheels_own(name: str, maker: str, height: float, stated: float | None, sources: str, mass: tuple, joints: list,
                  **more) -> dict:
    """A robot on wheels with every joint from its maker (E9.6 point 2): its battery in its base."""
    more.setdefault('battery_region', 'Base')
    return own_joints(name, maker, height, stated, sources, mass, joints, **more)


DEXMATE_VEGA = on_wheels_own(
    'Dexmate Vega 1 Pro', 'Dexmate', 1.71, 135, 'DXM (Dexmate), DXMu (its model, 141.00 kg); E9.1',
    ((134, 135, 141.0), 'S', 'DXM "298 lbs (135 kg)" the mode, ± 1 kg; DXMu its model 141.00 kg the max (E9.6 point 1)'),
    VEGA_JOINTS, joint_sources='DXMu: ' + TORQUES_SOURCE + "; its wheels, steering and casters its model's masses (E)",
    parts=[casters(2, 0.25, "DXMu: its model's casters, 0.2 and 0.3 kg (E9.6 point 6)")],
    boards=thor('DXM "NVIDIA Jetson AGX Thor"') + [POWER_BOARD],
    sensors=[binocular('DXM "Stereo RGB camera"'), base_lidar('DXM "2× LiDAR, one front and one rear"', 2),
             base_camera('DXM "4× RGB cameras"', 4), IMU_NOT_NAMED])
RAINBOW_RBY1_A, RAINBOW_RBY1_M = (on_wheels_own(
    f'Rainbow Robotics RB-Y1 {model}', 'Rainbow Robotics', 1.40, kg, 'RBY (Rainbow Robotics), RBYu (its model); E9.1',
    (((130, 131, 132.22), 'S', 'RBY "Total: 131kg" the mode, ± 1 kg; RBYu its model 132.22 kg the max (E9.6 point 1)')
     if model == 'A' else ((169, 170, 171), 'S', 'RBY "Total: 170kg" (its model M); ± 1 kg')),
    RBY1_JOINTS + [hub_motors(wheels_, kg)[0]],
    joint_label={'small': 'S, E', 'large': 'E'},
    joint_sources=('RBYu: ' + TORQUES_SOURCE + '; its neck its "Neck Joint Module", "1.5 kg" each, ± 5 % (S); its '
                   f'grippers its model\'s 0.533 kg (E); its {wheels_} drive wheels as {hub_motors(wheels_, kg)[1]} (E)'),
    parts=[casters(2)] if model == 'A' else [],
    **voltage_capacity(50, 'RBY "50V"', 25 if model == 'A' else 50, f'RBY "{25 if model == "A" else 50}Ah"'),
    boards=[intel('Intel (its Robot PC)', 'RBY "dual-PC", the Robot PC'),
            ('Compute module, GPU (not named)', 1, 'Boards', 'Torso', estimate(87), 'ITC', 'E',
             'RBY "GPU-Equipped" User PC: as an AGX Orin, 100 × 87 mm, half to 1.5 times (my reading; E9.6 point 9)'),
            ('Carrier board of the compute module', 1, 'Boards', 'Torso', COMPUTER, 'ITC', 'E',
             "as the X1's and N1's computer boards (E9.6 point 9)"), POWER_BOARD],
    cooler=[fans(2, 'its two computers'), x86_sinks(1), ARM_SINK])
    for model, kg, wheels_ in (('A', 131, 2), ('M', 170, 4)))
ROBOTIS_AI_WORKER = on_wheels_own(
    'ROBOTIS AI Worker', 'ROBOTIS', 1.623, 90, 'RBT (ROBOTIS: the FFW-SG2), RBTe (its actuators), RBTm (its model); E9.1',
    ((89, 90, 94.42), 'S', 'RBT "90 kg" the mode, ± 1 kg; RBTm its model 94.42 kg the max (E9.6 point 1)'),
    AI_WORKER_JOINTS, joint_label={'small': 'S', 'large': 'S, E'},
    joint_sources=('RBTe: ROBOTIS\'s actuators by model, their weights ± 5 % (S): arm joints 1-3 YM080-230-R099-RH '
                   '1,200 g, 4-6 YM070-210-R099-RH 790 g, 7 PH42-020-S300-R 340 g; head XH540-V150-R 165 g, '
                   'XH430-V210-R 82 g; steering YM070-210-R051-RH 790 g; lift YM080-230-B001-RH 890 g; gripper '
                   'RH-P12-RN "500g"; its drive links its model\'s 3.80 kg (RBTm, E)'),
    lift_column=(estimate(17.01), 'E', "RBTm its model's lift link 17.9 kg less its motor's 0.89 kg, half to 1.5 times "
                                       '(E9.6 point 7)'),
    **voltage_capacity(25.5, 'RBT "Battery: 25V, 80Ah (2,040Wh)": 2,040 / 80 = 25.5 V', 80, 'RBT "80Ah"'),
    boards=agx_orin('RBT "NVIDIA Jetson AGX Orin 32GB"') + [POWER_BOARD],
    sensors=[binocular('RBT "Stereolabs ZED Mini"'), depth_camera('RBT "Intel RealSense D405 (x2)"', 2),
             base_lidar('RBT "LakiBeam 1 (x2)"', 2), imu('RBT "IMU"')],
    frame=('Frame', 'Aluminium', 'RBT "Exterior Materials Aluminum, Plastic"; the remainder (E9.6 point 12)'))
POLLEN_REACHY_2 = on_wheels_own(
    'Pollen Robotics Reachy 2', 'Pollen Robotics', 1.66, 50, 'POL (Pollen Robotics), POL21 (its base, 2021); E9.1',
    ((49, 50, 51), 'S', 'POL "Up to 50 kg"; ± 1 kg (E9.6 point 1)'), REACHY_JOINTS,
    joint_label={'small': 'S, E', 'large': 'E'},
    joint_sources=('POL: Orbita 2D "1.900 g" and Orbita 3D "950 g", ± 5 % (S); its wheels\' motors (POL21: rated '
                   '5 N·m) as ZLT\'s 4.5", 2.9 kg, half to 1.5 times (E); its grippers as the RH-P12-RN (E)'),
    **voltage_capacity(24, 'POL21 "24V, 35Ah" (the 2021 base\'s battery, E for Reachy 2)', 35, 'POL21 "35Ah"',
                       label='S, E'),
    pack=(spread(6.5), 'S, E', 'POL21 "6.5kg" (the 2021 base\'s battery, E for Reachy 2); ± 5 %'),
    boards=[intel('Solidrun Bedrock v3000 (AMD)', 'POL "Solidrun Bedrock v3000", "Fanless industrial PC"'),
            POWER_BOARD],
    cooler=[x86_sinks(1)],
    sensors=[binocular('POL "Stereo"'), depth_camera('POL "RGB-D"'), base_lidar('POL "LiDAR"'),
             ('Motion sensor (IMU)', 3, 'Wheeled base', 'Base', IMU_G, 'E',
              "POL21 \"Hall Sensors and IMU on each wheel\"; as the G1's (E9.6 point 10)", [('IMU', 1)])],
    frame=('Frame', 'Aluminium', 'POL21 "Aluminium, MJF 3D printed plastic parts, Steel" (its base); aluminium the '
                                 'remainder, its steel not weighed (E9.6 point 12)'))
YUE_QUAN_W_BOT = on_wheels_own(
    'Yue Quan Bionics W-Bot', 'Yue Quan Bionics', 1.78, 60, 'YQB (Yue Quan Bionics, 博文W-Bot 2.0); E9.1',
    ((59, 60, 61), 'S', 'YQB "整机重量 60kg"; ± 1 kg'), W_BOT_JOINTS,
    joint_sources=('YQB: "膝关节约 360N·m，踝关节约 160N·m，手臂关节约 60N·m"; its three hip joints at its knee\'s 360 N·m '
                   '(E); mass the refit at the torque, half to 1.5 times; its drive wheels as ' + hub_motors(2, 60)[1]
                   + ' (E)'),
    parts=[casters(2)],
    **voltage_capacity(48, 'YQB "最大电压48V", taken as its voltage (E)', 2400 / 48, 'YQB "电池容量2400W·h" at 48 V',
                       label='S, E'),
    boards=[('Compute module, NVIDIA Jetson Orin NX', 2, 'Boards', 'Torso', ORIN_NX, 'ITC', 'S',
             'YQB "NVIDIA Jetson Orin NX 16GB×2"; 69.6 × 45 mm (E5.13), ± 5 %'),
            ('Carrier board of the Orin NX', 2, 'Boards', 'Torso', COMPUTER, 'ITC', 'E',
             "as the X1's and N1's computer boards (E9.6 point 9)"), POWER_BOARD],
    cooler=[fans(2, 'its two Orin NX'), arm_sinks(2)],
    sensors=[depth_camera('YQB "Intel Realsense D435i深度相机＆D455深度相机"', 2), base_lidar('YQB "Iivox 360雷达"'),
             IMU_NOT_NAMED])
# The template on wheels: the joints of the four with every joint, their hands, wheels, steering and lift left out.
WHEELED_AVERAGE_JOINTS = average_joints(
    [dict(b, joints=[j for j in b['joints'] if j[0].split()[0] not in ('Wheel', 'Steering', 'Lift', 'Gripper', 'Hand')])
     for b in (DEXMATE_VEGA, RAINBOW_RBY1_A, ROBOTIS_AI_WORKER, POLLEN_REACHY_2)], label=WHEELED_TEMPLATE_LABEL)

# --- The robots on wheels of the template (E9.6 points 3 to 12) -------------------------------------------------------
AGIBOT_A2_W = from_the_register_on_wheels('AgiBot A2-W', 'AgiBot', 1.63, 230,
                                          "AGA2: no longer on AgiBot's sites")
AGIBOT_G1 = wheeled(
    'AgiBot G1', 'AgiBot', 1.80, 150, ((149, 150, 151), 'S', 'AGG1 "150kg"; ± 1 kg'), 20,
    sources='AGG1 (AgiBot: "20 DoF", its hands of six); E9.1', driven=2, caster_count=2, added=(hands(6),),
    boards=agx_orin('AGG1 "Jetson AGX Orin 64GB"') + [POWER_BOARD],
    sensors=[depth_camera('AGG1 "RGBD Camera*3"', 3), camera('Camera, fisheye', 5, 'Head', 'AGG1 "Fisheye*5"'),
             base_depth_camera('AGG1 "RGBD cameras front and rear"', 2), base_lidar('AGG1 "LiDAR"'), IMU_NOT_NAMED])
FLEXIV_AICO_2_4, FLEXIV_AICO_2_10 = (wheeled(
    f'Flexiv AICO 2-{n}', 'Flexiv', 1.60, kg, ((kg - 1, kg, kg + 1), 'S', f'FLX "{kg}kg" (AICO 2-{n}); ± 1 kg'), 14,
    sources=f'FLX (Flexiv: AICO 2-{n} "2*7" DoF, "Dual-wheel differential"); E9.1', driven=2, caster_count=2,
    sensors=[base_lidar('FLX "Laser SLAM"'), IMU_NOT_NAMED]) for n, kg in ((4, 281), (10, 395)))
PAL_ARI = wheeled(
    'PAL ARI', 'PAL Robotics', 1.65, None, ((59, 60, 61), 'S', 'HG "60" (the register, the catalogue\'s); ± 1 kg; PAL '
                                                              'states none (E9.2 point 5)'), 12,
    sources='ARId (PAL: head 2, arms 5 × 2, base 2; "Standard differential drive"), HG; E9.1', driven=2,
    caster_count=2, computer='Computer board, Intel i5',
    **voltage_capacity(24, 'ARId "24V / 40VAh"', 40, 'ARId "40VAh"'),
    boards=[intel('Intel i5', 'ARId "CPU Intel i5 / i7 / i9"'), POWER_BOARD], cooler=[fans(1, 'its computer'), x86_sinks(1)],
    sensors=[camera('Camera, head', 1, 'Head', 'ARId "Head Camera 8 MP RGB"'), depth_camera('ARId "RealSense D435i"'),
             microphones('ARId "4x high performance digital microphone array"'),
             ('Speaker', 2, 'Head', 'Head', SPEAKER_G, 'E', "ARId \"2 x 30 W Hi-Fi\"; as the G1's (E9.6 point 10)", []),
             IMU_NOT_NAMED])
KIT_ARMAR_7 = wheeled(
    'KIT ARMAR-7', 'KIT', 1.75, None, ((119, 120, 121), 'S', 'HG "120" (the register, the catalogue\'s); ± 1 kg; KIT '
                                                             'states none (E9.2 point 5)'), 21,
    sources='KIT (arms 8 × 2, head 3, torso 2, hands of four, "three omni-wheels"), HG; E9.1', driven=3,
    added=(hands(4),),
    sensors=[camera('Camera, hand', 2, 'Head', 'KIT "A RGB camera is integrated in each of these hands"'),
             binocular('KIT "several integrated camera systems" (E: one binocular)'), IMU_NOT_NAMED])
ASTRIBOT_S1 = wheeled('Astribot S1', 'Astribot', 1.70, 80, ((79, 80, 81), 'S', 'ASTp "80kg"; ± 1 kg'), 14,
                      sources='ASTp (Astribot: arms of 7 DoF); E9.1', driven=2, caster_count=2)
ASTRIBOT_T1 = from_the_register_on_wheels('Astribot T1', 'Astribot', 1.55, 66, 'ASTp: a banner only')
ELU_AI_AD_01 = from_the_register_on_wheels('ELU.AI AstroDroid AD-01', 'ELU.AI', 1.70, 120, 'INF: AD-01 named, no figures')
HONDA_AVATAR = wheeled(
    'Honda Avatar', 'Honda', 1.70, 110, ((109, 110, 111), 'S', 'HON "110kg Weight"; ± 1 kg; the register\'s 101 kg '
                                                               'reported'), 22,
    sources='HON (Honda: head 3, arms 8 × 2, hands 16 × 2, waist 3, wheel 2); E9.1', driven=2, caster_count=2,
    added=(hands(16),), sensors=[binocular('HON "the robot\'s eyes" (E: one binocular)'), IMU_NOT_NAMED])
CASBOT_W1 = wheeled(
    'CASBOT W1', 'CASBOT', 2.10, 260, ((259, 260, 261), 'S', 'CAS "重量约260kg"; ± 1 kg'), 17,
    sources='CAS (CASBOT: arms 7 × 2, neck 2, waist 1, lift 1, "2+4，两轮差速"); E9.1', driven=2, caster_count=4,
    lift=True, added=(grippers('Gripper (CASBOT)', label='S'),), computer='Computer board, Intel i9',
    **voltage_capacity(48, 'CAS "电池电压 48v"', 25, 'CAS "电池容量 48V/25Ah"'), cell_recipe='LFP cylindrical',
    cells=('S', 'LFP cylindrical: CAS "电池类型 磷酸铁锂"; the cell format E (E9.6 point 8)'),
    boards=[intel('Intel i9', 'CAS "工控机（i9 cpu+4060显卡）"'),
            ('Graphics board, NVIDIA RTX 4060', 1, 'Boards', 'Torso', COMPUTER, 'ITC', 'E',
             "CAS \"4060显卡\"; as the X1's and N1's computer boards (E9.6 point 9)")] + RK3588_BOARDS + [POWER_BOARD],
    cooler=[fans(2, 'its PC and graphics board'), x86_sinks(2), ARM_SINK],
    sensors=[base_lidar('CAS "腹部可扩展360球型激光"'), depth_camera('CAS "RGBD相机（结构光）" 4', 4),
             binocular('CAS "双目相机 1，头部"'), microphones('CAS "胸部2麦线阵"'), IMU_NOT_NAMED],
    frame=('Frame', 'Aluminium', 'CAS "合金、工程塑料": alloy, aluminium (E); the remainder (E9.6 point 12)'))
TOYOTA_CUE7 = from_the_register_on_wheels('Toyota CUE7', 'Toyota', 2.18, 74, 'no page of Toyota\'s found (E9.1)',
                                          caster_count=0)
REALMAN_DUAL_ARM_LIFT = wheeled(
    'RealMan Dual-Arm Lift', 'RealMan', 1.78, 157, ((156, 157, 158), 'S', 'RMD "≈ 157 kg"; ± 1 kg'), 12,
    sources='RMD (RealMan: dual RM65-B-V arms of 6 DoF, "Lifting Stroke 900 mm"); E9.1', driven=2, caster_count=2,
    lift=True, added=(grippers('Gripper (CTAG2F90D)'),),
    sensors=[depth_camera('RMD "Vision Sensor: Integrated" (E: one depth camera)'), IMU_NOT_NAMED])
TANGIBLE_EGGIE = from_the_register_on_wheels('Tangible Robots Eggie', 'Tangible Robots', 1.60, 45,
                                             'TAN: Eggie not named, no figures')
FEATHER = wheeled(
    'Feather Robotics Feather', 'Feather Robotics', 1.80, 105, ((104, 105, 106), 'S', 'FEA "Total weight 105 kg"; ± 1 '
                                                                                      'kg'), 16,
    sources='FEA (Feather: "7 per arm · 2 neck · 1 torso · 6 base", its hands of six); E9.1', driven=3, steered=3,
    lift=True, added=(hands(6),), **voltage_capacity(48, 'FEA "Battery voltage 48 V"', 50, 'FEA "Battery capacity 50 Ah"'),
    boards=agx_orin('FEA "Jetson Nano · Jetson Orin AGX · Jetson Thor": the middle one (E)', label='E') + [POWER_BOARD],
    sensors=[binocular('FEA "Zed 2i · Zed X · Zed X Mini"'), microphones('FEA "4-microphone array with speaker"'),
             speaker('FEA "with speaker"'), IMU_NOT_NAMED])
UNITREE_G1_D = wheeled(
    'Unitree G1-D Ultimate', 'Unitree', 1.68, 90, ((89, 90, 91), 'S', 'UNG1D "Approx. 90kg"; ± 1 kg'), 16,
    sources='UNG1D (Unitree: arms 7 × 2, waist 2, column 1, base 2, "Diﬀerential drive"); E9.1', driven=2,
    caster_count=2, lift=True,
    **voltage_capacity(48, "UNG1D states no voltage: 48 V as Unitree's H2-D (E9.6 point 8)", 39,
                       'UNG1D "Upper Body Battery(Quick-release): 9Ah", "Chassis Battery (Built-in): 30Ah"',
                       label='S, E'),
    computer='Computer board, 8-core',
    sensors=[binocular('UNG1D "Head HD Binocular Camera *1"'), camera('Camera, wrist', 2, 'Head',
                                                                       'UNG1D "Wrist HD Camera *2"'),
             base_lidar('UNG1D "LiDAR *1"'), base_depth_camera('UNG1D "Depth Camera *2"', 2), IMU_NOT_NAMED])
AGIBOT_G2 = wheeled(
    'AgiBot G2', 'AgiBot', 1.795, 185, ((184, 185, 186), 'S', 'AGG2m "重量 185 kg"; ± 1 kg; the register\'s 55 kg '
                                                              'reported'), 22,
    sources='AGG2m (AgiBot: head 3, arms 7 × 2, torso 5, "4舵轮"); E9.1', driven=4, steered=4,
    **voltage_capacity(48, 'AGG2m "额定电压 48V"', 1652 / 48, 'AGG2m "电池总容量 1652Wh（34Ah）" at 48 V'),
    boards=[('Compute module, "500 TOPS" (not named)', 2, 'Boards', 'Torso', estimate(87), 'ITC', 'E',
             'AGG2m "500 TOPS (INT8)", "24*A78": two AGX Orin, 100 × 87 mm, half to 1.5 times (my reading; E9.6 '
             'point 9)'),
            ('Carrier board of the compute module', 2, 'Boards', 'Torso', COMPUTER, 'ITC', 'E',
             "as the X1's and N1's computer boards (E9.6 point 9)"), POWER_BOARD],
    cooler=[fans(2, 'its two modules'), arm_sinks(2)],
    sensors=[binocular('AGG2m "头部双目 1"'), camera('Camera, fisheye', 3, 'Head', 'AGG2m "头部鱼眼 3"'),
             depth_camera('AGG2m "头部RGBD 1", "腕部RGBD 2"', 3), base_lidar('AGG2m "底盘激光雷达 2"', 2),
             ultrasonic('AGG2m "底盘超声波雷达 8"', 8), imu('AGG2m "底盘IMU"'), microphones('AGG2m "4麦克风阵列"'),
             speaker('AGG2m "头部扬声器 1"')])
UNITREE_H2_D = wheeled(
    'Unitree H2-D Flagship', 'Unitree', 1.70, 120, ((119, 120, 121), 'S', 'UNH2D "Approx. 120Kg" (Flagship); ± 1 kg'),
    17, sources='UNH2D (Unitree: arms 7 × 2, waist 1, head 2, column 1, chassis 2); E9.1', driven=2, caster_count=2,
    lift=True, **voltage_capacity(48, 'UNH2D "48V/30Ah (1.44 kWh)"', 30, 'UNH2D "30Ah"'),
    boards=[intel('Intel Core i5 (PC1)', 'UNH2D "PC1: Intel Core i5"'),
            intel('Intel Core i7 (PC2)', 'UNH2D "PC2: Intel Core i7"'), POWER_BOARD],
    cooler=[fans(2, 'its two Intel computers'), x86_sinks(2)],
    sensors=[binocular('UNH2D "Humanoid Binocular Camera"'), camera('Camera, wrist', 2, 'Head',
                                                                     'UNH2D "Wrist HD Camera ×2"'),
             microphones('UNH2D "Microphone Array"'), speaker('UNH2D "High-Power Speaker"'),
             base_lidar('UNH2D "LiDAR ×1"'), base_depth_camera('UNH2D "Depth Camera ×1"'),
             ultrasonic('UNH2D "Ultrasonic Sensor ×2"', 2), IMU_NOT_NAMED],
    parts=[titanium(120, 'UNH2D "Titanium Alloy": a share of its mass as the H2\'s (E6.8 point 12)')],
    frame=('Frame', 'Aluminium', 'UNH2D "Aerospace-Grade Aluminum, Titanium Alloy, and High-Strength Engineering '
                                 'Plastics"; the remainder (E9.6 point 12)'))
MAGICLAB_MAGICBOT_D1 = wheeled(
    'MagicLab MagicBot D1', 'MagicLab', 1.80, 150, ((149, 150, 151), 'S', 'MGD1 "150kg"; ± 1 kg'), 21,
    sources='MGD1 (MagicLab: neck 2, arms 7 × 2, waist 3, legs 2, "four‑steering‑wheel chassis"); E9.1', driven=4,
    steered=4, **voltage_capacity(48, 'MGD1 "Total Capacity 1652Wh"; its charger "54.75V": 48 V (E)', 1652 / 48,
                                  'MGD1 "1652Wh" at 48 V', label='S, E'),
    boards=[('Compute module, Huawei R1 (500 TOPS)', 1, 'Boards', 'Torso', estimate(87), 'ITC', 'E',
             'MGD1 "Huawei R1, 500 TOPS (INT8)": as an AGX Orin, 100 × 87 mm, half to 1.5 times (E9.6 point 9)'),
            ('Carrier board of the compute module', 1, 'Boards', 'Torso', COMPUTER, 'ITC', 'E',
             "as the X1's and N1's computer boards (E9.6 point 9)"), POWER_BOARD],
    sensors=[camera('Camera, head', 1, 'Head', 'MGD1 "Head RGB Camera ×1"'), binocular('MGD1 "Head Stereo Camera ×1"'),
             camera('Camera, fisheye', 3, 'Head', 'MGD1 "Head Fisheye Camera ×3"'),
             depth_camera('MGD1 "Wrist RGBD Camera ×2"', 2), base_lidar('MGD1 "Chassis 3D LiDAR ×2"', 2),
             ultrasonic('MGD1 "Chassis Ultrasonic Sensor ×3" (its text: 8)', 3), microphones('MGD1 "Microphone Array"'),
             ('Speaker', 2, 'Head', 'Head', SPEAKER_G, 'E', "MGD1 \"Hi‑Fi driver ×2\"; as the G1's (E9.6 point 10)", []),
             IMU_NOT_NAMED])
BLUE_WORM_MANTIS = from_the_register_on_wheels(
    'Blue Worm Mantis Standard', 'Blue Worm', 1.40, 50, 'BWM: no mass (the press: about 35 kg, second-hand)',
    driven=4, caster_count=0, body_joints=18, lift=True)
SPIRIT_AI_MOZ1 = from_the_register_on_wheels('Spirit AI Moz1', 'Spirit AI', 1.60, 70,
                                             'SPA: no robot named ("全向轮式底盘", "自由度达26个")', driven=4,
                                             caster_count=0, body_joints=26)
SANCTUARY_PHOENIX_8 = from_the_register_on_wheels('Sanctuary Phoenix Gen 8', 'Sanctuary AI', 1.70, 70,
                                                  'SNC8: "a wheeled base", no figures')
GALAXEA_R1_PRO = wheeled(
    'Galaxea R1 Pro', 'Galaxea', 1.70, 126, ((125, 126, 127), 'S', 'GAL "126 kg ... including battery"; ± 1 kg; the '
                                                                   "register's 96 kg (the R1 Lite's) reported"), 18,
    sources="GAL (Galaxea: arms 7 × 2, torso 4, chassis 6), GALg (the R1's: three steered wheels); E9.1", driven=3,
    steered=3, added=(grippers('Gripper (Galaxea)'),),
    **voltage_capacity(48, 'GALg "48 V" (the R1\'s battery, E for the Pro)', 35, 'GALg "35 Ah"', label='S, E'),
    boards=agx_orin('GAL "NVIDIA Jetson AGX Orin, 32GB"') + [POWER_BOARD],
    sensors=[binocular('GALg "Zed 2" (the R1\'s)'), depth_camera('GALg "RealSense D435i" × 2', 2),
             base_camera('GALg "5 x Monocular Camera"', 5), base_lidar('GALg "LIVOX MID-360"'), imu('GALg "IMU"')])
UNITREE_R1_A5_D, UNITREE_R1_A7_D = (wheeled(
    f'Unitree R1-{model}', 'Unitree', 1.60, kg, ((kg - 1, kg, kg + 1), 'S', f'UNR1 "Approx. {kg}kg" ({model}); ± 1 kg; '
                                                                          "the register's 52 kg reported"),
    body, sources=f'UNR1 (Unitree: {model}, arms {arm} × 2, waist 1, head 2, "Chassis DOF 3"); E9.1', driven=4,
    added=(grippers('Gripper (Unitree)'),),
    boards=[('Computer board, 8-core (body)', 1, 'Boards', 'Torso', COMPUTER, 'ITC', 'E',
             "UNR1 \"Body: 8-core high-performance CPU\"; as the X1's and N1's computer boards (E9.6 point 9)"),
            ('Computer board, 8-core (head, 10 TOPS)', 1, 'Boards', 'Torso', COMPUTER, 'ITC', 'E',
             "UNR1 \"Head: 8-core high-performance CPU + 10 TOPS\"; as the X1's and N1's computer boards"), POWER_BOARD],
    cooler=[fans(2, 'its two computers'), arm_sinks(2)],
    sensors=[binocular('UNR1 "Binocular Camera"'), base_lidar('UNR1 "Chassis LiDAR"'), microphones('UNR1 "4-Array"'),
             ('Speaker', 2, 'Head', 'Head', SPEAKER_G, 'E', "UNR1 \"Dual Speakers (3W×2)\"; as the G1's", []),
             IMU_NOT_NAMED])
    for model, kg, body, arm in (('A5-D', 30, 13, 5), ('A7-D', 32, 17, 7)))
REALMAN_REALBOT_01 = wheeled(
    'RealMan RealBot-01', 'RealMan', 1.68, 125, ((124, 125, 126), 'S', 'RM01 "≈ 125 kg"; ± 1 kg'), 21,
    sources='RM01 (RealMan: arms 14, waist 3, legs 2, neck 2); E9.1', driven=2, caster_count=2,
    **voltage_capacity(48, "RM01 states no voltage: 48 V as RealMan's S2 and L2 (E9.6 point 8)", 40,
                       'RM01 "40 Ah (BMS)"', label='S, E'),
    sensors=[depth_camera('RM01 "5 depth cameras"', 5), camera('Camera, fisheye', 3, 'Head', 'RM01 "3 fisheye cameras"'),
             base_lidar('RM01 "1 LiDAR"'), ('Motion sensor (IMU)', 2, 'Boards', 'Torso', IMU_G, 'E',
                                            "RM01 \"2 IMUs\"; as the G1's (E9.6 point 10)", [('IMU', 1)]),
             microphones('RM01 "a head-mounted microphone array"')])
REALMAN_REALBOT_L2 = wheeled(
    'RealMan RealBot-L2', 'RealMan', 1.70, 120, ((119, 120, 121), 'S', 'RML2 "≈ 120 kg"; ± 1 kg'), 16,
    sources='RML2 (RealMan: "17 DoF", "Dual-wheel differential drive", "Lifting stroke 0.3 m"); E9.1', driven=2,
    caster_count=2, lift=True, **voltage_capacity(48, 'RML2 "48V 20Ah"', 20, 'RML2 "20Ah"'),
    boards=agx_orin('RML2 "Jetson AGX Orin 64G"') + [POWER_BOARD],
    sensors=[binocular('RML2 "Stereo RGB"'), depth_camera('RML2 hand "RGBD"', 2), IMU_NOT_NAMED])
REALMAN_REALBOT_S2 = wheeled(
    'RealMan RealBot-S2', 'RealMan', 1.70, 125, ((124, 125, 126), 'S', 'RMS2 "≈ 125 kg"; ± 1 kg'), 20,
    sources='RMS2 (RealMan: "20 DoF", "Four-wheel steering, four-wheel drive"); E9.1', driven=4, steered=4,
    **voltage_capacity(48, 'RMS2 "48V 20Ah"', 20, 'RMS2 "20Ah"'),
    boards=agx_orin('RMS2 "Nvidia Jetson AGX Orin 64G"') + [POWER_BOARD],
    sensors=[binocular('RMS2 "Stereo RGB ×1"'), camera('Camera, fisheye', 2, 'Head', 'RMS2 "fisheye ×2"'),
             depth_camera('RMS2 hand "RGBD"', 2), base_lidar('RMS2 "dual LiDAR"', 2), IMU_NOT_NAMED])
PAL_TIAGO_PRO = wheeled(
    'PAL TIAGo Pro', 'PAL Robotics', 1.55, 80, ((79, 80, 95), 'S', 'TPs "Weight 80 kg" the mode, TPd "Weight 95 Kg" '
                                                                  'the max, 1 kg below (decided, E9.3)'), 16,
    sources='TPs, TPd (PAL: arms 7 × 2, lift 1, head 2, "Omnidirectional (4 DoF)", "4x Mecanum Wheels"); E9.1',
    driven=4, lift=True, added=(grippers('Gripper (PAL Pro)'),), computer='Computer board, Intel i5',
    **voltage_capacity(36, 'TPd "2 x 36 V, 20 Ah": one battery, the datasheet\'s standard robot (decided, E9.3)', 20,
                       'TPd "20 Ah"'),
    boards=[intel('Intel i5', 'TPs "Intel i5, RAM 16 GB"'), POWER_BOARD], cooler=[fans(1, 'its computer'), x86_sinks(1)],
    sensors=[depth_camera('TPs "RGB-D Camera"'), base_lidar('TPs "2x Laser Range Finder"', 2),
             microphones('TPs "4-Mic Array"'),
             ('Speaker', 2, 'Head', 'Head', SPEAKER_G, 'E', "TPs \"2x 4W Loudspeakers\"; as the G1's", []), imu('TPd "IMU"')])
TOKYO_ROBOTICS_TOROBO = wheeled(
    'Tokyo Robotics Torobo', 'Tokyo Robotics', 1.615, 120, ((119, 120, 121), 'S', 'TOR "approx. 120 kg"; ± 1 kg; the '
                                                                                 "register's 160 kg reported"), 20,
    sources='TOR (Tokyo Robotics: arms 7 × 2, waist 3, neck 3, "omni-directional mobile base"); E8.1, E9.1',
    driven=4, computer='Computer board (one PC)',
    boards=[intel('one PC', 'TOR "one PC"'), POWER_BOARD], cooler=[fans(1, 'its PC'), x86_sinks(1)])
LANXIN_VB1_I, LANXIN_VB2, LANXIN_VERSABOT_VB_1 = (wheeled(
    f'Lanxin {model}', 'Lanxin Robotics', height, None, (mass, 'S', f'HG "{words}" (the register, the catalogue\'s); '
                                                                     'Lanxin states none (E9.2 point 5)'),
    body, sources=f'LXV (Lanxin: {model}, arms of {arm} joints, {base_}); HG; E9.1', driven=driven,
    caster_count=caster_count, added=(grippers('Gripper (Lanxin)'),),
    sensors=[depth_camera('LXV "Panoramic RGB-D Depth Vision System" (E: one)'), base_lidar('LXV "3D Laser SLAM"'),
             IMU_NOT_NAMED])
    for model, height, mass, words, body, arm, base_, driven, caster_count in (
        ('VB1-I', 1.65, (60, 65, 70), '~60–70', 12, 6, '"Dual-wheel differential motor"', 2, 2),
        ('VB2', 1.70, (65, 70, 75), '~65–75', 14, 7, '"Four-wheel omnidirectional wheel"', 4, 0),
        ('VersaBot VB-1', 1.65, (74, 75, 76), '75', 12, 6, '"Four-wheel omnidirectional wheel"', 4, 0)))
TLIBOT_Y1, TLIBOT_Y2_B, TLIBOT_Y2_P = (
    from_the_register_on_wheels(f'Tlibot {model}', 'Tlibot', height, kg, "TLB: not on its maker's list")
    for model, height, kg in (('Y1', 1.95, 150), ('Y2-B', 1.60, 85), ('Y2-P', 1.565, 95)))
YUNMU_YMBOT_D, YUNMU_YMBOT_D2, YUNMU_YMBOT_D4 = (
    from_the_register_on_wheels(f'Yunmu YMBot {model}', 'Yunmu', height, kg, why)
    for model, height, kg, why in (('D', 1.65, 100, 'YMB: no product pages'), ('D2', 1.80, 150, 'YMB: no product pages'),
                                    ('D4', 1.65, 100, 'YMB: a news item only ("双臂负载60kg")')))
PSIBOT_SYNROBOT = from_the_register_on_wheels(
    'PsiBot ψ-SynRobot', 'PsiBot', 1.45, 65, 'PSI: waist 2, neck 2, "算力平台：Thor", no mass',
    boards=thor('PSI "算力平台：Thor"') + [POWER_BOARD],
    sensors=[depth_camera('PSI "4个RGBD相机"', 4), camera('Camera, fisheye', 3, 'Head', 'PSI "3个鱼眼相机"'),
             IMU_NOT_NAMED])

# Every robot of type 2 taken apart, in the register's order of numbers (13 A2-W to 352 H1; batch 1: 116 GR-1, 117
# GR-2, 119 H1-2, 120 H2, 121 H2 Plus; batch 2b from 216 Omni; the robots on wheels among them), the robots of the
# template with its rows (AVERAGE_JOINTS), those of the template on wheels with theirs (their blocks name them).
GENERATED = [robot_rows(b, ROBOT_TYPE, AVERAGE_JOINTS) for b in (
    AGIBOT_A2_W, AGIBOT_G1, ROBOTIS_AI_WORKER, FLEXIV_AICO_2_4, FLEXIV_AICO_2_10,
    AEI_ALICE_4, PAL_ARI, KIT_ARMAR_7, ASTRIBOT_S1, ASTRIBOT_T1, ELU_AI_AD_01, DOBOT_ATOM, HONDA_AVATAR, MIRRORME_BOLT,
    CASBOT_W1, TOYOTA_CUE7, XIAOMI_CYBERONE, DEEP_ROBOTICS_DR01, REALMAN_DUAL_ARM_LIFT, TANGIBLE_EGGIE, FEATHER,
    FIGURE_03, UNITREE_G1_D, AGIBOT_G2, FOURIER_GR1_ONE, FOURIER_GR1_TWO, FOURIER_GR2, UNITREE_H1_2, UNITREE_H2,
    UNITREE_H2_PLUS, UNITREE_H2_D, UNITREE_H2X_INTEL, UNITREE_H2X_ORIN,
    HONOR_D1, SIMPLEXITY_I_SERIES, ROBROS_IGRIS_C, JCBOT_JINGCHU, KAIST_HUMANOID, PAL_KANGAROO, KEPLER_K1, KEPLER_K2,
    LEJU_KUAVO_5, LIMX_CL, LIMX_OLI, LIMX_LUNA, LUMOS_LUS2, MAGICLAB_MAGICBOT_D1, MAGICLAB_MAGICBOT, BLUE_WORM_MANTIS,
    VINMOTION_MOTION_2, SPIRIT_AI_MOZ1, ZHEJIANG_NAVAI_I3,
    DIGIT_NEZHA_P01, X_HUMANOID_OMNI, TESLA_OPTIMUS_GEN_3, TESLA_OPTIMUS_GEN_2, TESLA_OPTIMUS_V2_5, CYAN_ROBOTICS_ORCA,
    SANCTUARY_PHOENIX, SANCTUARY_PHOENIX_8, PHYBOT_M1, OPENLOONG_QINGLONG, GALAXEA_R1_PRO, UNITREE_R1_A5_D,
    UNITREE_R1_A7_D, RAINBOW_RBY1_A, RAINBOW_RBY1_M, POLLEN_REACHY_2, REALMAN_REALBOT_01, REALMAN_REALBOT_L2,
    REALMAN_REALBOT_S2, PAL_REEM_C, ROBOTERA_L7, ENGINEAI_SE01, ZEROTH_SEAN,
    SIASUN_SONGXING, UNITREE_SUPERMAN, PAL_TALOS, WESTWOOD_THEMIS, PAL_TIAGO_PRO, X_HUMANOID_TIANGONG_ULTRA,
    TLIBOT_TIANZHEN_Z1, X_HUMANOID_TIEN_KUNG_2, X_HUMANOID_TIEN_KUNG_3, TLIBOT_T1, TOKYO_ROBOTICS_TOROBO, LANXIN_VB1_I,
    LANXIN_VB2, DEXMATE_VEGA, LANXIN_VERSABOT_VB_1, YUE_QUAN_W_BOT, DROIDUP_WALKER_II, WALKER_TIENKUNG_VISION,
    WALKER_TIENKUNG_EMBODIED, TLIBOT_Y1, TLIBOT_Y2_B, TLIBOT_Y2_P, YUNMU_YMBOT_D, YUNMU_YMBOT_D2, YUNMU_YMBOT_D4,
    PSIBOT_SYNROBOT, UNITREE_H1)]


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
