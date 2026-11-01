# The arithmetic and the reading scripts of 2026-11-01 (EVIDENCE.md E15 and E16, VERIFICATION.md V134 to V136)

> Saved from Claude's scratch folder on 2026-11-01 (Matthias: "Yes, save them"), so that the work can go on on another Mac. The scratch folders it names (`pages_e15/`, `urdf_e15/`, `imgs_e15/`, `downloads_e15/`, `downloads_e16/`, `texts_e16/`) are not kept: each page, model file and PDF can be read again at the address given. Written by Claude.

Kept as text, not as runnable files: Claude's arithmetic at the modes and its tools for reading pages and model files, not stages of the model.

## E15's modes and E13's shares after batch 3 (`batch3/batch3_plan.py`)

```python
"""Batch 3 of types 3 and 4 (E15) at the modes: Claude's arithmetic, not the model (the run draws every number from its
min, mode and max). Each robot's joints (types 3 and 4's templates; from a stated torque by the seven robots' ratios and
E6.8's fit, E12.5 point 2; or every joint from the maker's model file), hands, battery pack, base and lift, shell, small
parts, and the frame as the remainder; then E13's shares after batch 3. Rough for the small items (boards 0.8 kg,
sensors 0.3 kg, cables 0.036 kg per metre, as batch2_modes.py): approximations, stated. Reads nothing of his."""
FIT = lambda t: 0.0689 * t ** 0.566                      # E6.8: one joint module's kg at its torque (N·m)
LEGS = dict(hip_pitch=1.00, hip_roll=1.00, hip_yaw=0.25, knee=1.00, ankle_pitch=0.33, ankle_roll=0.24,
            waist=0.36, shoulder=0.27, elbow=0.15, wrist=0.08, head=0.08)        # over the knee (the largest)
WHEELS = dict(waist=1.00, waist2=0.54, shoulder=0.235, elbow=0.13, wrist=0.04, head=0.06)  # over the largest waist
L12 = dict(hip_pitch=2, hip_roll=2, hip_yaw=2, knee=2, ankle_pitch=2, ankle_roll=2)
F6 = 0.443 / 6                                            # Fourier's six-joint hand, kg per joint (E7.5 point 4)
GRIP = 0.5                                                # a gripper, kg (E)
def hub(kg_per_wheel):
    return 1.4 if kg_per_wheel <= 35 else 3.75 if kg_per_wheel <= 75 else 4.85 if kg_per_wheel <= 100 else 8.5
GR3 = [366] * 4 + [140.4] * 5 + [108.6] * 2 + [74.4] * 4 + [42.9] * 6 + [17.4] * 6 + [59.4] * 4     # its 31 (V134)
NIX = [102] * 17 + [17] * 4                                                                          # nix2-5.urdf
STAR1 = [35] * 2 + [110] * 8 + [35] * 6 + [220] * 2 + [110] + [255, 100, 400, 400, 100, 100] * 2   # l3 body, 31
R = []
def add(num, name, ftype, types, mass, ev, form, h, joints=('T',), hands=0.0, wh=None, whev='', cells='NMC',
        wheels=0, casters=0, steer=0, lift=False, boards='one (E)', sensors='one IMU (E)', note=''):
    R.append(dict(num=num, name=name, ftype=ftype, types=types, mass=mass, ev=ev, form=form, h=h, joints=joints,
                  hands=hands, wh=wh, whev=whev, cells=cells, wheels=wheels, casters=casters, steer=steer, lift=lift,
                  boards=boards, sensors=sensors, note=note))
def S(m): return (m - 1, m, m + 1)
LISTED = []   # (num, name, why): not drawn, no stated mass (or its source calls it a target, a design, unknown)
def listed(num, name, why): LISTED.append((num, name, why))

# --- group 1 (97 to 137) --------------------------------------------------------------------------------------------
add(97, 'Figure 02', 3, '3', S(70), 'C', 'legs', 1.68, hands=32 * F6, wh=2250, whev='S', sensors='6 RGB cameras (S), microphones, speakers')
add(99, 'FlashBot Arm', 4, '4', S(70), 'C', 'wheels', 1.44, hands=12 * F6, wheels=2, casters=2, sensors='RGB-D, LiDAR, panoramic camera (one each, E)')
add(100, 'Friday', 3, '3', S(115), 'C', 'wheels', 1.76, hands=2 * 0.5, wheels=2, casters=2, boards='AGX Orin (C, E: "Jetson Orin")')
add(101, 'Futuring 2', 4, '4', S(70), 'C', '?', 1.68, hands=2 * GRIP)
add(106, 'G2 Max', 3, '3', S(185), 'C', 'wheels', 1.79, wheels=4, steer=4, note="the catalogue's 185 is the base G2's (AGG2m)")
add(107, 'Galbot G1', 3, '3', S(92.5), 'S', 'wheels', 1.73, hands=2 * GRIP, wh=1440, whev='S', wheels=4, boards='AGX Orin', sensors='stereo 1, RGB 4, depth 2, 3D LiDAR 1, IMU 2, 2 microphone arrays, 2 speakers')
add(108, 'Galbot ET1', 3, '3', S(32), 'S', 'legs', 1.25, boards='RK3588, RDK X5', sensors='stereo camera 1')
add(109, 'Galbot S1', 3, '3', S(320), 'S', 'wheels', 1.79, hands=2 * GRIP, wh=2880, whev='S', wheels=4, steer=4, lift=True, boards='AGX Orin', sensors='stereo 1, 3D LiDAR 3, depth 2, 2 speakers')
add(110, 'Gen 1 (Persona)', 3, '3', (69, 70, 85), 'C', 'legs', 1.75, hands=20 * F6)
add(111, 'GENE.01', 3, '3', (60, 79.7, 80.7), 'S model, C', 'legs', 1.70, hands=42 * F6, sensors='6 cameras, IMU 1 (its model)')
add(112, 'Gento Luna', 3, '3,4', S(90), 'C', 'wheels', 1.70, hands=2 * GRIP, wh=48 * 34.4, whev='S', cells='LFP', wheels=4, boards='AGX Orin', sensors='3D LiDAR 1')
add(113, 'Gino 1', 3, '3', S(63), 'C', 'wheels', 1.68, hands=14 * F6, wheels=4, boards='Jetson Thor (C)', sensors='trinocular 1, fisheye 2, 3D LiDAR 2, palm stereo 2')
add(114, 'GoMate', 3, '3,4', S(45), 'C', 'wheels', 1.40, hands=10 * F6, wheels=4)
add(115, 'GoMate Mini', 3, '3,4', S(60), 'C', 'wheels', 1.70, wheels=4)
add(118, 'GR-3', 4, '4', S(71), 'S', 'legs', 1.65, joints=('model', GR3), hands=12 * F6, wh=936, whev='S', boards='Ryzen 7 8845HS CPU board', sensors='monocular 1, IMU 1, microphone array 1, speaker 1')
listed(124, 'HELIOS', 'the maker discloses nothing (heise); the catalogue\'s "~60–80" a range of its own, no source')
add(125, 'HIVA Haiwa', 4, '4', S(70), 'C', 'wheels', 1.65, hands=12 * F6, wheels=2, casters=2)
add(127, 'HMND 01 Alpha Bipedal', 3, '3', S(90), 'S', 'legs', 1.79, hands=2 * GRIP, boards='AGX Orin, Intel i9 CPU board', sensors='6 RGB, 2 depth, 6-microphone array, 2 wrist RGB')
add(129, 'Hobbs W1', 4, '4', S(75), 'C', 'wheels', 1.70, hands=12 * F6, wh=25.9 * 32, whev='C, E', wheels=2, casters=2, boards='RK3588, J1900 CPU board', sensors='3 ToF, 3 RGB, microphone array, LiDAR')
add(130, 'HONOR', 4, '4', S(80), 'C', 'legs', 1.60, sensors='camera 1')
add(131, 'HONOR A1', 4, '4', S(40), 'C', 'legs', 1.37)
add(133, 'HSR-ER-HR705', 3, '3', S(200), 'S', 'wheels', 1.70, hands=2 * GRIP, wheels=3, sensors='depth 2, fisheye 1, LiDAR 1')
add(136, 'IRON (2024)', 4, '4,3', S(70), 'C', 'legs', 1.78, hands=30 * F6, boards='Turing chip as one board (E)')
add(137, 'IRON (2025)', 3, '3,4', (69, 70, 90), 'C', 'legs', 1.78, hands=44 * F6, boards='3 Turing chips as 3 boards (E)')
# --- group 2 (139 to 186) -------------------------------------------------------------------------------------------
add(139, 'Isaac 1', 4, '4', (39, 40, 45), 'C', 'wheels', 1.75, hands=2 * GRIP, wheels=3, lift=True)
add(141, 'Jaka K1', 3, '3,4', S(40), 'C', 'legs', 1.80)
add(142, 'JAKA Kargo', 3, '3', (179, 180, 200), 'C', 'wheels', 1.57, wheels=2, casters=2, lift=True, boards='Intel i5 CPU board (C)')
add(145, 'Jingchu Elf', 4, '4', (69, 70, 80), 'S', 'wheels', 1.65, wheels=2, casters=2, boards='Orin NX (E: its 1024-core Ampere GPU)', sensors='LiDAR 1, depth 1')
add(146, 'Jupiter', 3, '3,4', (57, 58, 60), 'C', 'legs', 1.65, hands=20 * F6)
add(150, 'KAI', 4, '4,3', S(70), 'C', '?', 1.73, hands=2 * 0.75, wh=1700, whev='C')
add(152, 'Kaleido 9', 3, '3,5', S(99), 'C', 'legs', 1.90, sensors='stereo 1, LiDAR 1')
add(154, 'KAPEX', 3, '3,4', (60, 65, 70), 'C', 'legs', 1.70)
add(155, 'Keenon XMAN-R1', 4, '4,3', S(110), 'C', 'wheels', 1.72, wheels=2, casters=2)
add(156, 'Kengo', 3, '3,4', (39, 40, 65), 'C', 'legs', 1.40, hands=24 * F6, joints=('torque2', 130, {**L12, 'waist': 1, 'shoulder': 6, 'elbow': 2, 'wrist': 6, 'head': 2}, LEGS))
add(160, 'Kinisi KR1', 3, '3', S(100), 'C', 'wheels', 1.62, hands=2 * GRIP, wheels=4, boards='AGX Orin (C, E)', sensors='stereo depth 2, LiDAR 1')
add(161, 'Knowin-X1', 4, '4', S(50), 'C', 'wheels', 1.30, wheels=2, casters=2)
add(162, 'KUAVO 5-W', 4, '4,3', S(156), 'C', 'wheels', 2.00, hands=12 * F6, wheels=4, sensors='4 depth, LiDAR 1')
add(164, 'Kuavo-my', 4, '4', S(45), 'C', 'legs', 1.45)
add(165, 'L1 (Moon Dynamics)', 3, '3', S(60), 'C', 'wheels', 1.65, hands=2 * GRIP, wheels=2)
add(166, 'Laborer C1', 4, '4', S(38), 'S', 'legs', 1.37, joints=('torque', 150, {**L12, 'waist': 1, 'shoulder': 6, 'elbow': 2}, LEGS), boards='Orin NX', sensors='depth 1, LiDAR 1, IMU 1, microphone array, speaker')
add(167, 'Laborer M1', 3, '3', S(86), 'S', 'legs', 1.87, joints=('torque', 430, {**L12, 'head': 1, 'shoulder': 6, 'elbow': 2, 'wrist': 6}, LEGS))
add(173, 'Lumen H1', 4, '4', S(69), 'S', 'legs', 1.69, joints=('torque', 512, {**L12, 'head': 2, 'shoulder': 6, 'elbow': 2, 'wrist': 6}, LEGS), hands=12 * F6, wh=700, whev='S', sensors='LiDAR 1, RGB-D 1')
add(174, 'Lumen S1', 4, '4', S(35), 'C', '?', 1.30, boards='Orin NX (C)', sensors='RGB-D 1, stereo 1, RGB 2, LiDAR 1')
add(178, 'MagicBot (Gen1)', 4, '4', (54, 70, 71), 'S, C', 'legs', 1.74, joints=('torque', 350, {**L12, 'head': 2, 'waist': 2, 'shoulder': 6, 'elbow': 2, 'wrist': 6}, LEGS), hands=12 * F6, wh=1350, whev='S', boards='CPU board, Orin NX (E: its 100 TOPS)', sensors='3D LiDAR 1, depth 2, fisheye 3, microphone array')
add(181, 'MagicBot X1', 3, '3,4', S(70), 'S', 'legs', 1.80, joints=('torque', 350, {**L12, 'head': 2, 'waist': 3, 'shoulder': 6, 'elbow': 2, 'wrist': 6}, LEGS), boards='CPU board, Orin NX', sensors='stereo 1, RGB-D 2')
add(182, 'MagicBot Z1', 4, '4', S(40), 'S', 'legs', 1.37, joints=('torque', 100, {**L12, 'head': 1, 'waist': 1, 'shoulder': 6, 'elbow': 2, 'wrist': 2}, LEGS), wh=55.5 * 10, whev='S, E', boards='CPU board', sensors='3D LiDAR 1, depth 1, fisheye stereo 1, microphone array, speaker')
add(183, 'Maker H01', 4, '4,3', S(64), 'C', 'wheels', 1.60, hands=14 * F6, wheels=2, casters=2, sensors='LiDAR 1')
add(185, 'Martian', 4, '4,3', S(40), 'S', 'legs', 1.48, joints=('torque', 150, {**L12, 'head': 2, 'waist': 3, 'shoulder': 6, 'elbow': 2, 'wrist': 6}, LEGS), hands=22 * F6, wh=48 * 9, whev='S', boards='Orin NX (E: its 40 TOPS, 32 GB)', sensors='depth 1, RGB 2, IMU 1')
add(186, 'Matrix-1', 3, '3', S(67), 'S', 'legs', 1.80, hands=44 * F6, wh=2280, whev='S', sensors='8 RGB cameras (S)')
# --- group 3 (188 to 239) -------------------------------------------------------------------------------------------
add(188, 'MEMO', 4, '4', S(77.1), 'S', 'wheels', 1.70, hands=8 * F6, wheels=2, casters=2, lift=True)
add(189, 'MenteeBot (2024)', 3, '3,4', S(70), 'C', 'legs', 1.75)
add(190, 'MenteeBot V3', 3, '3', (65, 70, 71), 'S, C', 'legs', 1.75, boards='2 AGX Orin (C)')
add(194, 'Mirokaï', 4, '4', (26, 29, 30), 'C', 'wheels', 1.23, hands=4 * F6, wheels=3, boards='2 Orin NX (C, E: "Jetson NX")', sensors='2 RGB-D, 2 infrared, 9 ToF cameras, 4 microphones, 3 IMU')
add(195, 'Moby', 3, '3,5', S(45), 'C', 'legs', 1.70, hands=2 * GRIP, boards='Jetson Thor (C)', sensors='stereo 1, LiDAR 1')
add(197, 'Modular (O-ID)', 3, '3', S(70), 'S', 'wheels', 1.72, hands=2 * GRIP, wheels=4)
add(198, 'Mornine', 4, '4', (65, 70, 71), 'C', 'legs', 1.67, hands=24 * F6, wh=700, whev='C', sensors='panoramic 1, depth 2, 3D LiDAR 1, 6-microphone array')
add(201, 'N2', 4, '4', S(30), 'C', 'legs', 1.18, joints=('torque2', 150, {'hip_pitch': 2, 'hip_roll': 2, 'hip_yaw': 2, 'knee': 2, 'ankle_pitch': 2, 'shoulder': 6, 'elbow': 2}, LEGS), boards='RK3588, Orin NX (C)', sensors='depth 1')
add(204, 'Navigator 2', 3, '3', S(60), 'C', 'legs', 1.65, hands=2 * 0.6, boards='AGX Orin (E: its 275 TOPS)')
add(205, 'NE01', 4, '4', S(40), 'C', 'legs', 1.45, )
add(206, 'NEO Beta', 4, '4,3', S(30), 'C', 'legs', 1.65)
add(207, 'NEO Gamma', 4, '4', S(35), 'C', 'legs', 1.65, sensors='4 microphones, 3 speakers')
add(209, 'NEXO', 3, '3,4', (78, 85, 86), 'C', 'wheels', 1.68, wheels=4, boards='AGX Orin (C)')
add(211, 'NIX', 4, '4', (18, 25.41, 26.41), 'S', 'legs', 0.89, wh=282, whev='S', boards='RK3588', sensors='RGB 1, 4-microphone array, speaker')
add(213, 'North', 3, '3,4', (59, 60, 90), 'C', 'wheels', 1.60, hands=44 * F6, wheels=2, casters=2, boards='Jetson Thor (C)')
listed(214, 'Northstar', 'its 40 kg is a target ("目標是…約 40 公斤", TechOrange; Bloomberg on its plans); no robot weighed')
add(215, 'Nova (ugo)', 3, '3', S(100), 'S', 'wheels', 1.62, hands=2 * GRIP, wh=50.6 * 22, whev='S', cells='LFP', wheels=4, boards='Jetson Thor', sensors='stereo 1, RGB 2')
add(217, 'Onero H1', 4, '4', (35, 68, 69), 'C', 'wheels', 1.74, wheels=2, casters=2, sensors='RealSense 4 (E: head, arms, hands, abdomen)')
add(226, 'P0', 3, '3', S(82), 'S', 'legs', 1.75, hands=2 * GRIP)
add(228, 'Phantom MK1', 3, '6,3', S(80), 'S', 'legs', 1.80, joints=('torque', 160, {**L12, 'waist': 3, 'shoulder': 6, 'elbow': 2, 'wrist': 6}, LEGS), note='shoulder 119 and wrist 20 as stated')
add(237, 'PrimeBOT T1', 4, '4', (8, 8.5, 9), 'C', 'wheels', 0.60, wheels=2)
add(238, 'ProWhite', 4, '4', S(400), 'S', 'wheels', 2.04, hands=2 * GRIP, wh=4000, whev='S', wheels=4, lift=True)
add(239, 'Psi V1', 3, '3', S(150), 'C', 'wheels', 1.80, wheels=2, casters=2, boards='Jetson Thor (S)', sensors='RGB-D 4, fisheye 3')
# --- group 4 (240 to 291) -------------------------------------------------------------------------------------------
add(240, 'Pudu D7 (2024)', 4, '4,3', S(45), 'S', 'wheels', 1.65, wh=1000, whev='S (its least)', wheels=4)
add(240, 'Pudu D7 (2026)', 4, '4,3', S(140), 'S', 'wheels', 1.75, wheels=4, boards='AGX Orin, RK3588', sensors='LiDAR 2')
add(241, 'Pudu D9', 3, '3', S(65), 'S', 'legs', 1.70, joints=('torque', 352, {**L12, 'waist': 2, 'head': 2, 'shoulder': 6, 'elbow': 2, 'wrist': 6}, LEGS), hands=2 * 0.5, wh=720, whev='S', boards='AGX Orin (E: its 275 TOPS)', sensors='RGB 1, RGB-D 1, IMU 1')
add(242, 'PX5', 3, '3,4', S(109), 'C', 'legs', 1.50, hands=2 * 0.43)
add(245, 'QUANTA X2', 3, '3,4', S(95), 'C', 'wheels', 1.64, hands=40 * F6, wheels=2, casters=2, sensors='2D LiDAR 1, RGB-D 3, ToF 2, BEV 3')
add(249, 'RAISE A1', 3, '3', S(55), 'S', 'legs', 1.75, joints=('torque', 350, {**L12, 'waist': 1, 'shoulder': 6, 'elbow': 2, 'wrist': 2, 'head': 2}, LEGS), hands=24 * F6, boards='AGX Orin (E: its 200 TOPS)', sensors='microphone array, LiDAR 1, RGB-D 1')
add(250, 'RayNex G3', 3, '3', S(60), 'S', 'legs', 1.73, hands=12 * F6)
add(258, 'REX G1', 3, '3,4', S(80), 'C', 'wheels', 1.70, wheels=3, lift=True, boards='Jetson Thor (E: its 2070 TFLOPS)')
add(259, 'RNoid', 4, '4', S(90), 'S', 'wheels', 1.70, hands=2 * GRIP, wheels=4, boards='Ryzen 5 CPU board, AGX Orin', sensors='RGB-D 4, LiDAR 2, microphone, speaker')
add(261, 'Robbyant R1', 4, '4', S(110), 'C', 'wheels', 1.60, wheels=2, casters=2, note='its joint modules by Ti5, its chassis by Galaxea (Bloomberg via Oninvest)')
add(262, 'RoBee (Series R)', 3, '3', (179, 180, 293), 'C, S', 'wheels', 1.99, hands=2 * GRIP, wheels=4, lift=True, sensors='depth 4, face camera 1, 3D laser 1, laser scanner 1, thermal 1')
add(263, 'Robin', 3, '3', S(105), 'S', 'wheels', 1.80, hands=2 * GRIP, wheels=4, lift=True)
add(264, 'ROBO-T1', 3, '3', (45, 50, 60), 'C', 'wheels', 1.30, hands=2 * GRIP, wheels=2, casters=2)
add(267, 'ROBOTERA Q5', 4, '4', S(70), 'S', 'wheels', 1.65, hands=22 * F6, wheels=2, casters=4, sensors='3D LiDAR 1, stereo 1')
add(270, 'SA02', 4, '4', S(25), 'C', '?', 1.25, sensors='2 cameras')
add(273, 'Sherpa Mecha', 3, '3', S(180), 'C', 'wheels', 2.00, wheels=2, casters=2, lift=True, sensors='3D LiDAR 1, camera 1')
add(275, 'SkyWalker 2', 3, '3,4', S(55), 'C', '?', 1.65, hands=12 * F6)
add(277, 'Spaceo M1', 4, '4', S(45), 'S', 'wheels', 1.63, joints=('torqueS', 15.7, {'shoulder': 6, 'elbow': 2, 'wrist': 2}, WHEELS), hands=2 * GRIP, wh=25.6 * 45, whev='S', cells='LFP', wheels=2, casters=2, boards='Ryzen 7 CPU board, AGX Orin', sensors='RGB 1, RealSense 1, 2D LiDAR 1, microphone array')
add(278, 'Spaceo Pro', 3, '3', S(60), 'S', 'wheels', 1.63, joints=('torque', 90, {'waist': 1, 'shoulder': 6, 'elbow': 2, 'wrist': 4, 'head': 2}, WHEELS), hands=2 * GRIP, wh=25.6 * 45, whev='S', cells='LFP', wheels=2, casters=2, lift=True, boards='Ryzen 7 CPU board, AGX Orin', sensors='RealSense 1, RGB 3, microphone array', note='shoulder 66 as stated')
add(280, 'Star1', 3, '3,4', S(63), 'C', 'legs', 1.71, joints=('model', STAR1), hands=24 * F6)
listed(282, 'StarBot Flex', 'its maker: "Availability and final specifications to be announced"; the catalogue\'s 50 kg not its')
add(283, 'StarBot Nova', 4, '4', S(31.8), 'S', 'wheels', 1.52, wheels=2, casters=2, sensors='depth 1, RGB 1, IMU 1')
add(284, 'Steve', 4, '4', (99, 100, 140), 'C', '?', 2.00)
add(286, 'Synthia', 4, '4', (9.8, 10.9, 12.0), 'S', 'legs', 1.75, boards='BCM2712 board', sensors='2 cameras, microphone')
add(287, 'Syntro', 3, '3', S(108), 'S', 'wheels', 1.70, hands=24 * F6, wh=1200, whev='S', wheels=3, boards='Intel i5 CPU board', sensors='2D LiDAR 1, camera 1, microphones')
add(291, 'TARA GEN1', 4, '4,3', S(75), 'C', 'wheels', 1.63, wheels=2, casters=2)
# --- group 5 (292 to 354) -------------------------------------------------------------------------------------------
listed(292, 'TARS', 'the catalogue\'s page links a rover team\'s site, its DoF "Assumed 30–40+"; no source of its own')
add(293, 'Tau Humanoid', 4, '4', S(35), 'C', 'legs', 1.32, joints=('G1',), hands=2 * GRIP, note='a modified Unitree G1 (MarketWatch): its joints as the G1\'s')
listed(304, 'Tobi', 'the catalogue itself: TwoLabs "has not yet published hardware specifications"')
add(305, 'Tora DoubleOne P', 3, '3,4', S(70), 'C', 'wheels', 1.64, joints=('torque', 207, {'waist': 2, 'waist2': 2, 'shoulder': 6, 'elbow': 2, 'wrist': 6, 'head': 2}, WHEELS), hands=36 * F6, wh=1214, whev='S', wheels=4, steer=4, lift=True, boards='AGX Orin', sensors='RGB 1, RGB-D 2, 3D LiDAR 1, IMU 2, 2 microphone arrays, speaker')
add(305, 'Tora DoubleOne X', 3, '3,4', S(73), 'C', 'wheels', 1.69, joints=('torque', 207, {'waist': 2, 'waist2': 2, 'shoulder': 6, 'elbow': 2, 'wrist': 6, 'head': 2}, WHEELS), hands=36 * F6, wh=1214, whev='S', wheels=4, lift=True, boards='AGX Orin', sensors='as the P')
add(310, 'U1 Pro male', 4, '4', S(42), 'C', 'legs', 1.83)
add(310, 'U1 Pro female', 4, '4', S(35.2), 'C', 'legs', 1.68)
listed(316, 'Vesoma 1', 'its maker: "design visualisation. Under development."; no robot')
add(317, 'Voxel', 4, '4', S(45), 'C', 'legs', 1.50, hands=2 * GRIP, sensors='stereo 1')
add(319, 'W1 Pro', 3, '3,4', S(110), 'S', 'wheels', 1.64, hands=12 * F6, wheels=2, casters=2, boards='2 boards (E: "Dual-PC")', sensors='stereo 1, LiDAR 2, cameras 2')
add(320, 'Walden', 3, '3', S(90), 'C', 'wheels', 1.65, hands=2 * GRIP, wheels=2, casters=2)
add(321, 'Walker C', 4, '4,3', S(43), 'S', 'legs', 1.63, wh=48 * 15, whev='S', sensors='RGB-D 2, binocular 1, structured-light 3D 2')
add(322, 'Walker C1', 4, '4', S(55), 'S', 'legs', 1.64, boards='Jetson Thor (S)', sensors='fisheye 2, binocular 1, monocular 1, 2 speakers')
add(324, 'Walker S1', 4, '4', S(76), 'S', 'legs', 1.72, joints=('torque', 250, {**L12, 'waist': 3, 'shoulder': 6, 'elbow': 2, 'wrist': 6, 'head': 2}, LEGS), hands=12 * F6, sensors='RGB-D 2, stereo 2, 2 speakers, IMU 1')
add(325, 'Walker S2', 3, '3', S(70), 'S', 'legs', 1.76, hands=22 * F6, wh=2300, whev='C', sensors='fisheye 2, RGB 2, RGB-D 2, microphone array, 2 speakers')
add(328, 'X-Bot', 4, '4,3', S(60), 'C', 'legs', 1.67, boards='Orin NX, Intel NUC CPU board (C)', sensors='depth 1, LiDAR 1')
add(330, 'Xiao Di', 4, '4,3', (57.5, 58.5, 59.5), 'C', 'legs', 1.61)
add(331, 'Xiao Liu', 4, '4', (55, 70, 71), 'C', '?', 1.65)
add(333, 'XiaQi', 4, '4', (68, 69, 69), 'S', 'legs', 1.69, wh=700, whev='S')
add(334, 'XTRON KUAVO-MY', 4, '4,3', (50, 55, 56), 'C', 'legs', 1.66, sensors='stereo depth 1, 6-microphone array, LiDAR 1')
add(339, 'YMBot C', 4, '4', S(75), 'C', 'legs', 1.74)
add(344, 'YMBot H', 4, '4', S(75), 'C', 'wheels', 1.70, wheels=2, casters=2)
listed(345, 'Yogi', 'humanoid.press: height and weight "Not published"; the catalogue\'s 47 kg and aiwiki\'s 8 kg disagree six-fold, neither sourced')
add(346, 'Zerith H1', 4, '4,3', S(55), 'C', 'wheels', 1.80, wheels=2, casters=2, sensors='3D LiDAR 1, depth 1')
add(347, 'Zerith Z1', 4, '4,3', S(33), 'C', 'legs', 1.45, joints=('torque2', 150, {**L12, 'waist': 1, 'shoulder': 6, 'elbow': 2}, LEGS), sensors='RGB 1, depth 1, LiDAR 1, IMU 1')
add(348, 'Zeus 1', 3, '3', S(300), 'C', 'wheels', 1.95, wh=48 * 40, whev='C', wheels=4, lift=True)
add(354, 'PR-OMNI', 3, '3', S(120), 'S', 'wheels', 1.57, hands=2 * GRIP, wh=3000, whev='S', wheels=4, lift=True, boards='AGX Orin, Intel NUC CPU board', sensors='RGB-D 3, LiDAR 2')
# Neo1 (208, types 5 and 3): hydraulic; proposed with types 5 and 6 (question 1), not here.

def joints_kg(r):
    m, form, j = r['mass'][1], r['form'], r['joints']
    if j[0] == 'T':
        return m * (0.447 if form in ('legs', '?') else 0.139)
    if j[0] == 'G1':
        return 0.40 * m                                     # placeholder: the G1's own rows (type 1)
    if j[0] == 'model':
        return sum(FIT(t) for t in j[1])
    T, counts, ratios = j[1], j[2], j[3]
    if j[0] == 'torqueS':                                   # its stated torque is its shoulder's (no waist)
        return sum(n * FIT(T * ratios[k] / ratios['shoulder']) for k, n in counts.items())
    return sum(n * FIT(T * ratios[k]) for k, n in counts.items())
if __name__ == '__main__':
    print(f"{'#':>4s} {'robot':24s} {'kg':>6s} {'form':6s} {'joints':>7s} {'share':>6s} {'hands':>5s} {'Wh':>6s} {'base':>5s} {'lift':>5s} {'frame':>6s} {'%':>4s}")
    for r in R:
        m = r['mass'][1]; form = r['form']; j = joints_kg(r)
        wh = r['wh'] if r['wh'] else m * (14.67 if form in ('legs', '?') else 10.84)
        pack = wh / 164 * (1.5 if r['cells'] == 'LFP' else 1.0)
        base = r['wheels'] * hub(m / r['wheels']) + r['casters'] * 0.27 + r['steer'] * 0.79 if r['wheels'] else 0.0
        liftkg = 0.199 * m if r['lift'] else 0.0
        frame = m - j - r['hands'] - pack - base - liftkg - 0.115 * m - (0.5 + 0.8 + 0.3 + 8 * r['h'] * 0.036)
        flag = ' <-- below a quarter' if frame < 0.25 * m else ''
        print(f"{r['num']:4d} {r['name'][:24]:24s} {m:6.1f} {form:6s} {j:7.1f} {100*j/m:5.0f}% {r['hands']:5.2f} {wh:6.0f} {base:5.1f} {liftkg:5.1f} {frame:6.1f} {100*frame/m:3.0f}%{flag}")
    print('listed only:', len(LISTED), [n for _, n, _ in LISTED])

def shares():
    """E13's shares after batch 3: each robot (and each version; a robot of no stated form as two versions, on legs and
    on wheels) counted in each of its types among 3 and 4; joints on the template where 'T', battery where no Wh."""
    now = {3: (75, 68, 96), 4: (32, 30, 50)}            # E14 as built (V133): joint template, battery template, of
    add = {3: [0, 0, 0], 4: [0, 0, 0]}
    for r in R:
        n = 2 if r['form'] == '?' else 1
        for t in (3, 4):
            if str(t) in r['types'].split(','):
                add[t][2] += n
                add[t][0] += n * (r['joints'][0] == 'T')
                add[t][1] += n * (r['wh'] is None)
    for t in (3, 4):
        j0, b0, n0 = now[t]; j, b, n = add[t]
        print(f'type {t}: {n0} + {n} = {n0 + n} robots and versions; joint template {j0} + {j} = {j0 + j} '
              f'({100 * (j0 + j) / (n0 + n):.0f} %), battery template {b0} + {b} = {b0 + b} ({100 * (b0 + b) / (n0 + n):.0f} %)')
    print('batch 3 alone:', {t: (add[t][0], add[t][1], add[t][2]) for t in (3, 4)})
if __name__ == '__main__':
    shares()
```

## E15.3's table from the plan

```python
"""E15.3's table from batch3_plan.R (scratch): one row a robot or version, the modes Claude's arithmetic."""
import sys; sys.path.insert(0, '.')
import batch3_plan as b
def kg(x): return f'{x:g}'
def mass(r):
    lo, mo, hi = r['mass']; return f"{kg(round(lo, 2))} / {kg(round(mo, 2))} / {kg(round(hi, 2))} ({r['ev']})"
def joints(r):
    j = r['joints']; m = r['mass'][1]; x = b.joints_kg(r)
    if j[0] == 'T': return f'template ({x:.1f} kg)'
    if j[0] == 'model': return f"every joint from its model (S; {x:.1f} kg, {100 * x / m:.0f} %)"
    if j[0] == 'G1': return "the Unitree G1's (type 1's), E"
    T = j[1]; ev = 'C' if j[0] == 'torque2' else 'S'
    where = 'its shoulder' if j[0] == 'torqueS' else ('its waist' if r['form'] == 'wheels' else 'its knee')
    extra = f"; {r['note']}" if r['note'] and 'stated' in r['note'] else ''
    return f"from {kg(T)} N·m at {where} ({ev}; {x:.1f} kg, {100 * x / m:.0f} %){extra}"
HANDS = {'Friday': '2 × 0.5 kg (C: 20 joints, 500 g)', 'Pudu D9': '2 × 0.5 kg (S: DH11 "500 g")',
         'KAI': '2 × 0.75 kg (E: the KaiHand\'s 750 g)', 'Navigator 2': '2 × 0.6 kg (C: "单手重量 600g")',
         'PX5': '2 × 0.43 kg (C: "430g")'}
def hands(r):
    if r['name'] in HANDS: return HANDS[r['name']]
    h = r['hands']
    if h == 0: return '—'
    if abs(h - 2 * b.GRIP) < 1e-9: return '2 grippers (E)'
    n = h / b.F6
    if abs(n - round(n)) < 1e-6: return f'2 × {round(n) // 2}'
    return f'2 × {h / 2:g} kg (S/C)'
def battery(r):
    if r['wh'] is None: return 'template'
    cell = ', LFP' if r['cells'] == 'LFP' else ''
    return f"{r['wh']:,.0f} ({r['whev']}{cell})"
def base(r):
    if not r['wheels']: return '—'
    parts = [f"{r['wheels']} driven"]
    if r['casters']: parts.append(f"{r['casters']} casters")
    if r['steer']: parts.append('steered')
    s = ', '.join(parts)
    return s + ('; lift' if r['lift'] else '')
print('| # Robot (file) | Mass (kg) | Form | Joints | Hands | Battery (Wh) | Boards | Base, lift |')
print('|---|---|---|---|---|---|---|---|')
for r in b.R:
    form = 'legs / wheels (Q2)' if r['form'] == '?' else r['form']
    name = r['name'] + (f"; {r['note']}" if r['note'] and 'stated' not in r['note'] else '')
    print(f"| {r['num']} {name} ({r['ftype']}) | {mass(r)} | {form} | {joints(r)} | {hands(r)} | {battery(r)} | {r['boards']} | {base(r)} |")
```

## A model file's link masses, joints and effort limits

```python
"""Add up the link masses of a URDF and list its joints and effort limits (E15 check, scratch only)."""
import sys, collections
import xml.etree.ElementTree as ET
for path in sys.argv[1:]:
    root = ET.parse(path).getroot()
    total = 0.0; rows = []
    for link in root.iter('link'):
        m = link.find('inertial/mass')
        if m is not None:
            v = float(m.get('value')); total += v; rows.append((link.get('name'), v))
    print(f'== {path}: {len(rows)} links with a mass, total {total:.3f} kg')
    hand = sum(v for n, v in rows if any(k in n.lower() for k in ('hand','finger','thumb','index','middle','ring','pinky','little','palm')))
    print(f'   links named like a hand: {hand:.3f} kg')
    for n, v in rows:
        if 'batt' in n.lower(): print('   battery link', n, v)
    kinds = collections.Counter(j.get('type') for j in root.iter('joint'))
    print('   joints:', dict(kinds))
    for j in root.iter('joint'):
        if j.get('type') in ('revolute', 'continuous', 'prismatic'):
            lim = j.find('limit')
            print(f"   {j.get('name'):40s} effort {lim.get('effort') if lim is not None else '-'}")
```

## A saved page's visible text

```python
"""Print the visible text of a saved HTML page, one text run a line (E15 first-hand reading, scratch only)."""
import sys
from html.parser import HTMLParser
class T(HTMLParser):
    skip = 0; out = []
    def handle_starttag(self, tag, a):
        if tag in ('script', 'style', 'noscript'): self.skip += 1
    def handle_endtag(self, tag):
        if tag in ('script', 'style', 'noscript') and self.skip: self.skip -= 1
    def handle_data(self, d):
        d = ' '.join(d.split())
        if d and not self.skip: self.out.append(d)
t = T(); t.feed(open(sys.argv[1], encoding='utf-8', errors='replace').read())
print('\n'.join(t.out))
```

## Fetch a page and its text

```bash
#!/bin/zsh
# get.sh NAME URL: save the page to pages_e15/NAME.html and its text to pages_e15/NAME.txt
S=/private/tmp/claude-501/-Users-rm-Documents-GitHub-RAWCLICDataCenters/9d2a0390-a98f-45e9-8e5e-43d8b0550be4/scratchpad
curl -sSL -m 40 -A 'Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15' -o $S/pages_e15/$1.html "$2"
python3 -I $S/tools_e15/htmltext.py $S/pages_e15/$1.html > $S/pages_e15/$1.txt
echo "$1: $(wc -c < $S/pages_e15/$1.html) bytes html, $(wc -l < $S/pages_e15/$1.txt) text lines"
```
