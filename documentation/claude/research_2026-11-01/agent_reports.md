# The research agents' reports of 2026-11-01, as received (not first-hand; checked in the two firsthand files)

> Saved from Claude's scratch folder on 2026-11-01 (Matthias: "Yes, save them"), so that the work can go on on another Mac. The scratch folders it names (`pages_e15/`, `urdf_e15/`, `imgs_e15/`, `downloads_e15/`, `downloads_e16/`, `texts_e16/`) are not kept: each page, model file and PDF can be read again at the address given. Written by Claude.

---

## Batch 3, group 1: the research agent's report (2026-11-01), as received; not yet checked first-hand

maker = the maker's own page, datasheet, manual or GitHub model file; internet: X = second-hand; hg = humanoid.guide
("Not Verified", often "likely" / "assumed"). Its web-search budget ran out near the end (no further search for XPENG,
Geek+ or GAC press releases). Not readable by its fetch tool: Noetix, Futuring, gbionics.ai (title only or 403). URDF
sums were added by hand from the fetch tool's lists, not by script: to be re-added by script before use.

97 Figure 02, Figure AI (register 70) — figure.ai now shows Figure 03 only (61 kg); /news/figure-02 is 404. Figure's press
release of 6 Aug 2024 (PRNewswire, via vktr.com): hands "16 degrees of freedom", "2.25 KWh custom battery pack in the
robot torso", "6 onboard RGB cameras", "onboard mics and speakers", "3x the computation and AI inference". internet: hg
168 cm, 70 kg, DoF 28, "dual NVIDIA RTX GPU–based modules", 5 h; Interesting Engineering from Figure's teaser video: "A2
actuator has a torque of 50Nm", "L1 and L4 actuators offer 150Nm torque" (peak or rated not said); The Robot Report:
payload 25 kg, "custom motors… for each joint". No mass from Figure.

99 FlashBot Arm, Pudu (register 70) — maker https://pudurobotics.com/products/flashbot-arm: "539*515*1440mm", "Arm: 7",
"Hand: 6 Active + 5 Passive", "8h (None load)", charging 4 h, "RGBD cameras, LiDAR, panoramic cameras, and
pressure-sensitive skin" (no counts), "10.1 inch Touch Screen", "Independent Suspended Chassis", "PUDU DH11 dexterous
hands", payload "15kg". No maker mass. internet: chipsilicon "70 kg (approx.)", hg 70; heise "weighs just 15 kg"
(the payload elsewhere).

100 Friday, Holiday Robotics (register 115) — maker site title only. internet: Humanoids Daily (citing "specs released
by the company", 13 Nov 2025): "176cm tall, weighing 115kg", base 66 kg, hand "20-DoF", 500 g a hand,
"hot-swappable batteries", "differential drive wheeled base", payload 5 kg an arm; News1: 176 cm, 115 kg, 64 DoF over
head, arms, hands, waist and wheels, 40 in the two hands; hg: 63 DoF, "7-DoF arms and a 5-DoF torso", "BLDC", "QDD",
"NVIDIA Jetson Orin", 4 h, "Aluminum".

101 Futuring 2 / F2, Futuring Robot (register 70) — maker site title only; Gasgoo blocked. internet: hg 70 kg, "~150–160"
cm, 26 DoF, hands 12, wheeled, "2-finger gripping claws", "likely NVIDIA-based", "Likely aluminum alloy + composite";
originofbots 168 × 50 × 40 cm, 70 kg, 28 DoF (21 in its timeline citing Gasgoo), bipedal in one place and wheeled in
another; its "2.25 kWh", six RGB cameras, 20/25 kg and 1.2 m/s are Figure 02's figures (its price is labelled "based
on Figure 02"). Sources conflict on the form.

106 G2 Max, AgiBot (register 185) — IT之家 (26 Oct 2026, AgiBot launch): "单臂负载 20kg、双臂额定负载 40kg、双臂峰值负载可达 50kg".
No Max mass, DoF or battery from AgiBot. hg: 185 kg, 179 cm, 50 DoF, hands 24, Jetson Thor T5000, IP42 (185 kg is the
base G2's maker mass). Base G2 (maker): AgiBot "AGIBOT G2 SPECS" PDF
(https://cdn.robotshop.com/media/A/Agb/RB-Agb-09/pdf/AgiBot-G2-Specification.pdf), user manual 2026-04-28
(https://www.agibot.com.cn/filepage/362.html), RBTX datasheet: "Weight 185kg"; 1225–1795 mm; "Active Degrees of Freedom
26": neck 3, "Single Arm DOF 7", "Waist & Leg DOF 5", "Chassis DOF 4" (manual: 25 excluding end effectors; figure "3-DOF
Waist", "2-DOF Leg"); "Number of Batteries 2", "Total Battery Capacity 1652Wh", "1652Wh（34Ah）", "额定电压 48V",
hot-swappable; "NVIDIA Jetson T5000"; "3D LiDAR 2", "Stereo Camera 1", "Fisheye Camera 3", "Head RGBD Camera 1", "Wrist
RGBD Camera 2", "Ultrasonic Sensor ×8", chassis IMU, 4 microphones; "4舵轮设计"; arm torque sensors.

107 Galbot G1, Galbot (register 88) — maker https://www.galbot.com/g1/: "92.5 kg"; 1730 mm; DoF "合计 21": neck 2, arms 7×2,
waist 3, legs 2 (excluding chassis and end effector); "48 V 30 Ah", 8 h; "NVIDIA AGX Orin 64GB" 275 TOPS; head stereo ×1,
torso RGB ×4, wrist depth ×2, chassis "3D 激光雷达 ×1", IMU torso ×1 and chassis ×1, "线性四麦克风阵列 ×2", wrist six-axis
force ×2, ultrasonic ×8; 4-wheel omnidirectional base 600/600/625 mm. Maker 92.5 against the register's 88.

108 Galbot ET1, Galbot (register 65, legs) — maker https://www.galbot.com/et1/: "1250 mm"; with battery "32 kg"; DoF
"标准版：26", Pro / Flagship "26 + 12（增加灵巧手）"; "RK3588 + RDK X5", Pro "Orin Nano 40TOPS", Flagship "NX 100TOPS";
"双目摄像头". Maker 32 against the register's 65.

109 Galbot S1, Galbot (register 320) — maker https://www.galbot.com/s1/: "整机重量 320 kg"; 1793 mm; "颈部 2 · 双臂 7×2 · 升降 1";
"48 V 30 Ah × 2", hot-swap, 8 h; "NVIDIA AGX Orin 64GB 275 TOPS"; head stereo ×1 and 3D LiDAR ×1, chest depth ×2 and
six-axis force ×2, chassis 3D LiDAR ×2; "四轮转向全向底盘" 730 × 730 mm; lift 750 mm; "双臂最高 50 kg".

110 Gen 1, Persona AI (register 70) — maker pages without numbers ("quick change battery interface", "textiles
integrated protective skin", "200°C pre heat zone"). internet: hg 175 cm, 70 kg, 32 DoF, hands 20, "Electric BLDC
actuators", "Harmonic drive reducers", 4 h, "NVIDIA Jetson Thor-class compute (estimate)", "Aluminum alloy frame";
originofbots 175 cm, "85 kg" (no source). Legs not confirmed by any page read.

111 GENE.01, Generative Bionics (register 70) — maker sites 403. Maker URDF
https://raw.githubusercontent.com/gbionics/gb-robot-models/main/share/gb_robot_models/robots/gene01_0/model.urdf ("GENE.01
1.0"; closed loops as serial equivalents): masses add up to 79.67 kg by hand (body 78.36, hands 1.31, a "battery" link of
3.54285 kg); 31 body joints (legs 12, torso 2, arms 7×2, neck 3) and 42 hand joints; every effort limit "1e+09"
(placeholder); 6 camera frames, chest_imu ×1. internet: originofbots "approximately 60 kilograms", 170 cm, 40–60 DoF,
3–5 h, "AMD's edge-processing architecture"; hg "~60–80"; Synapticon actuators (startupbusiness.it, IE); tactile skin.

112 Gento Luna, Gento Robotics (register 90) — maker https://www.gentorobotics.ai/products/gento-luna/: "1700 mm", folds to
"790 mm"; "26 DoF (excluding dexterous hands)", "7-DoF… Arm", "6 degrees of freedom across the waist and legs"; "48 V
34.4 Ah LiFePO battery pack", "4–8 hours", "quick battery swap"; "NVIDIA Jetson Orin AGX 64GB"; "3D LiDAR and ultrasonic
radar" (no counts); omnidirectional wheeled chassis; 6 kg an arm. No maker mass; hg 90; hg "2-finger gripping claws".

113 Gino 1, Geek+ (register 63) — maker page lists "GINO" without figures. internet: 财联社 (10 Feb 2026): "机器人双臂14个自由度",
"7主动自由度三指灵巧手", "50Ah的大容量电池", wireless charging "3KW", NVIDIA Thor "2,070 FP4 TFLOPS", "三目主视觉和前后鱼眼相机",
"前后半球形3D激光雷达", "手心双目相机和触觉传感器", omnidirectional wheeled chassis, "双臂最大20Kg"; hg 168 cm, 63 kg.

114 GoMate, GAC (register 45) — no maker page. internet: CnEVPost (per GAC, 26 Dec 2024): "about 1.4 meters in
quadrupedal mode", "up to 1.75 meters in bipedal mode", "38 degrees of freedom", "all-solid-state batteries",
"six-hour battery life"; heise 174 / 137 cm, five fingers, GAC joint motors, obstacles to 30 m. Mass: none on any page
read (45 kg only in hg's search listing, not opened). Wheel-leg, four- and two-wheel modes.

115 GoMate Mini, GAC (register 60) — internet: hg 170 cm, 60 kg, 27 DoF, "GAC in-house actuators", 8 h, wheel-legs,
two-, three- or five-finger hands. No maker page with figures.

118 GR-3, Fourier (register 71) — maker https://support-old.fftai.com/en/docs/GR-X-Humanoid-Robot/GR3/GR-3_Introduction/
and maker URDF https://raw.githubusercontent.com/FFTAI/Wiki-GRx-Models/master/GRX/GR3/gr3v2_1_1/basic_urdf/gr3v2_1_1.urdf:
165 cm, about 71 kg net, battery packs 3.8 + 1.3 kg; URDF masses 69.69 kg by hand, no hands; DoF "up to 55": head 2, arm 7
each, waist 3, leg 6 each, hand 6 or 12; peak torques (the URDF effort limits match): hip pitch and knee 366.0, hip roll,
hip yaw and waist yaw 140.4, waist roll and pitch 108.6, shoulder pitch and roll 74.4, ankle pitch and roll 59.4,
shoulder yaw, elbow and wrist yaw 42.9, head and wrist pitch / roll 17.4; "Max joint peak torque" 440; battery 702 + 234
Wh, 46.8 V, lithium-ion, hot-swap, 3 h; AMD Ryzen 7 8845HS; 1 monocular camera, 1 six-axis IMU, microphones "360°";
"aluminium alloy, engineering plastic, soft cover".

124 HELIOS, ORBIT Robotics (register 70) — maker site title only; heise: "Orbit Robotics does not disclose further
information", "a large part of the load-bearing components is 3D printed"; New Atlas: four arms, tendon drive. internet:
hg "~60–80" kg, 160 cm, 28 DoF, hands 14, 3 h, "Aluminum alloys and carbon fiber". No legs.

125 HIVA Haiwa, Haier (register 70) — maker news without figures. internet: IT之家 (26 Jul 2025, Haier launch): "身高 165cm，
体重 70kg", "全身 44 个自由度", "采用底座移动方式"; hg hands 12, "Electric servo motors", 1 h, "Aluminum alloy frame".

127 HMND 01 Alpha Bipedal, Humanoid (register 90) — maker https://thehumanoid.ai/hmnd-01-alpha-bipedal/ and its 2 Dec 2025
release: "179 cm", "90 kg"; "29 degrees of freedom excluding end-effectors"; "12-DOF 5-finger hand or 1-DOF parallel
gripper"; "three hours of swappable power" (product page "4 hr"); "Nvidia Jetson Orin AGX and Intel i9"; head "six RGB
cameras, two depth sensors, and a six-microphone array", wrist RGB cameras and F/T sensors; payload 15 kg.

129 Hobbs W1, Noetix (register 75) — maker pages title only. internet: aiwiki (citing noetixrobotics.com/en/hobbs-w1 for
every row; not read first-hand): "1,700 mm"; "75 kg"; head 2.8 kg; arm 3.3 kg; "54 active" DoF, head "32 active and 8
passive", "5 DoF per arm", hand 6 active and 5 passive; "32 Ah (21V to 29.4V)"; RK3588 and Intel J1900; "3 ToF sensors
on chassis", 2 RGB eyes, 1 RGB chest, linear four-microphone array, LiDAR; "Two-wheel differential drive with universal
wheels"; face "Platinum silicone". housebots gives 20 kg (conflicts).

130 HONOR, HONOR (register 80) — maker page names A1 and D1 without numbers. internet: hg (MWC 2026) "approximately 160 cm",
"80 kg", 20 DoF, hands 10, 2 h, "forehead-mounted camera"; 财联社 / IT之家: race robot "闪电" "身高 169cm"; Xinhua: lower-limb
joint "实现400牛米峰值扭矩输出"; 财联社: "132款核心金属结构件" by Lens Technology. Which robot the register's "HONOR" is: not said.

131 HONOR A1, HONOR (register 40, legs) — internet: hg 136.9 cm, 40 kg, five fingers, liquid-cooled joints, 10 km/h,
"most likely aluminium"; 元气仔 "身高136.9cm" (财联社, IT之家); no page says A1 is 元气仔.

133 HSR-ER-HR705, Huashu (register 200) — maker https://www.hsrobotics.cn/products_xq/119.html: "200kg"; "机器人高度 1700mm";
chassis "745×620×343mm"; DoF "23（机械臂7×2+头部2+腰部1+腿部3+底盘3）"; "6H+", charging "≤2H"; depth ×2, fisheye ×1 (optional
wrist depth ×2); "SLAM激光导航"; "全向移动"; end effectors optional; payload "10kg（5kg×2）".

136 / 137 IRON, XPENG (register 70 and 90) — internet only: 2024 IRON (cnmra): "178 cm tall, weighs 70 kg, and has 62
degrees of freedom", hands 15, Turing chip 3000 TOPS, "next-gen linear actuators"; new IRON (Nov 2025; ifeng, 36Kr,
Gasgoo, TechNode, IT之家): "82个自由度" (ifeng) or "全身共有 65 个自由度" (36Kr), "身高约 1.78 米", "体重达到 70kg", hands 22,
three Turing chips "2250 TOPS", "全固态电池", battery capacity "尚未公布", "金属骨架", "全包覆柔性皮肤"; mass-production IRON
(8 Sep 2026, huacheng.gz-cmc.com): 76 DoF, 21 a hand. hg 173 cm, 70 kg, 60 DoF, hands 22, 4 h. XPENG's own page: no
numbers. No source gives 90 kg for any IRON.

The agent's summary: something was found for every robot. No maker figures: Persona Gen 1, HELIOS, HONOR, HONOR A1,
GoMate Mini, Gino 1, Futuring 2 (site unreadable), Hobbs W1 (site unreadable; aiwiki quotes it). Register masses not
matched by the maker: ET1 32 (register 65), Galbot G1 92.5 (88), G2 Max (185 is the base G2), IRON (no 90 kg anywhere).

---

## Batch 3, group 2: the research agent's report (2026-11-01), as received; not yet checked first-hand

[maker] = the maker's own page; [internet: X] = second-hand; hg = humanoid.guide; n.f. = none found. Its web-search budget
ran out early: MagicBot, Maker H01, Martian, Matrix-1 only from known addresses. Unreadable: kawasakirobotics.com (403),
galaxea-dynamics.com and zeroth0.com (429), autonews.gasgoo.com (468), jaka.com, lejurobot.com, keenon.com, the KinetixAI
KaiBot page, gigaai.cc (script-only). No URDF or MJCF; Leju's kuavo-ros-opensource has model folders (biped_s45 …
biped_s400049, kuavo5_seat, wheel_arm_upper_body) without a product named for each.

139 Isaac 1, Weave — maker weaverobotics.com/isaac-1: height "3' – 5'9"", footprint 20.5" × 22", DoF neck 2, arms 2 × 6,
hands 2 × 1, torso 2, base 3; "8 hours", charge "2 hours"; "wheeled base", passively stable, telescoping body; "soft
fabric shells" around a "solid inner structure"; no mass. internet: hg 40 kg, 160 cm, 21 DoF; Origin of Bots "45 kg"
(no source).

141 Jaka K1, JAKA — maker page unreadable. internet: Jiemian (CIIF launch, 26 Sep, probably 2024) "高1.8米", "全身具备29个活动关节",
"双臂共有14个自由度", "7轴拟人型构造", "单臂负载能力可达3公斤", legs not yet walking; hg 40 kg, 165 cm, 18 DoF, 3 h; Applicad Thai: a
7-DoF arm and a "RoboHub" controller (Intel Core i5 Gen 12, "Weigh 2.0 Kg").

142 JAKA Kargo, JAKA — maker page unreadable. internet: hg table 180 kg, its text "about 200 kilograms with everything
onboard", 156.5 cm, 21 DoF, 4 h, Intel Core i5, wheeled, waist column "up to 800 mm", 5 kg an arm, "Steel + aluminum
alloy".

145 Jingchu Elf, Hubei Jingchu — maker jingchurobot.cn/product_detail/3.html: "荆楚精灵身高165cm，体重约70kg"; a second block on
the same page "身高：1.6m 体重：80kg 2轮驱动"; "具备16个自由度（不含手）"; "高扭矩行星减速机模组"; "约8小时综合续航"; NVIDIA Ampere GPU "约117TOPS"
(an Orin NX class figure); "激光雷达和深度相机"; wheeled, 2-wheel drive.

146 Jupiter, Zeroth — maker site 429. internet: IFA exhibitor listing (presumably from Zeroth) "165 cm", "58 kg", "25
joints", hands "22 points of articulation (10 per hand)", "2 hours 20 minutes"; hg 60 kg, 30 DoF, 4 h; Origin of Bots 60
kg, "Legged (bipedal walking)".

150 KAI, KinetixAI — maker KaiBot pages without specifications; maker KaiHand page: "37 DoF: 20 active, 1 passive, 16
compliant", 750 g, 12 V (robot not named). internet: IE (30 Apr 2026) "173 centimeters", "70 kilograms", "115 degrees of
freedom", "72 DoF in its hands", "1.7-kilowatt-hour (kWh) semi-solid-state battery", 4 h, "aluminum alloy and composite
materials"; hg the same mass and height. Legs or wheels n.f.

152 Kaleido 9, Kawasaki — maker 403. internet: Mynavi (5 Dec 2025) "身長は190cm", "体重は99kg", "全身に30軸(ハンドは別)の自由度",
"ロボット本体のみだと稼働時間は30分ほど", "頭部にステレオカメラ", "胸にはLIDARセンサー"; hg 190 cm, 99 kg, 3 h, "Magnesium alloy skeleton with
3D-printed resin exterior panels". Legs.

154 KAPEX, LG with KIST — internet: Hankyung (13 Nov 2025) "키 170㎝, 체중 60㎏대"; hg 65 kg, 175 cm, "40–50 DOF", hands 20;
Hellot in-house actuators. Legs.

155 Keenon XMAN-R1, KEENON — maker pages without figures. internet: hg 110 kg, 172 cm, 36 DoF; humanoid.press "Keenon does
not publish height/weight", "Bipedal walking"; China.com "搭载 11 项多模态传感器"; Jiemian "轮式和人形结合的构造" (wheeled).

156 Kengo, Galaxea — internet: IT之家 (2 Jun 2026) Galaxea "暂未公布" the parameters, "单关节扭矩超 130N·m", "仅用两款核心模组覆盖全身关节";
hg 65 kg, 170 cm, 32 DoF; Robotic Gizmos 1.4 m; Origin of Bots "140 x 44 x 22.5 cm footprint and 40 kg weight". Legs.

160 Kinisi KR1, Kinisi (now Bear Robotics) — maker bearrobotics.ai/kinisi: "Wheeled humanoid mobile manipulator", "a full
shift per battery", up to 14.4 km/h, IP65; no mass. internet: IE (26 Nov 2025, attributed to Kinisi) "hot-swappable 48 V
lithium-ion battery", 6–8 h, "onboard NVIDIA Jetson module", "stereo depth cameras, a 180° LiDAR array", 10 kg; hg 100
kg, 162 cm, 21 DoF, "Aluminium".

161 Knowin-X1, Knowin — maker knowinai.com/en/product.html: "130 cm" extended, "≤40 cm" folded, "7 DoF" an arm, "23 DoF"
total, "Vision · Depth · LiDAR", "Wheeled chassis", 6 kg both arms; no mass. internet: ifeng (28 Sep 2026) "整机重约50kg",
"身高约1.4m".

162 KUAVO 5-W, Leju — maker pages without figures. internet: hg 156 kg, 200 cm, 40 DoF, "500 N·m peak torque", 6 h, "4
depth cameras", omnidirectional wheeled base, "Aluminium alloy and steel"; Mike Kalil "more than 8 hours", 20 kg.

164 Kuavo-my, Leju — maker pages without figures. internet: hg 45 kg, 145 cm, 26 DoF; CAICT CTTL-T (4 Mar 2024, KUAVO
without a variant) "weighing about 45kg", "26 degrees of freedom of the whole body"; hg "XTRON KUAVO-MY" 55 kg, 166 cm, 30
DoF (7 a leg, 7 an arm), options 1500 / 1660 mm and 50 / 55 kg. Whether these are the same robot: unclear.

165 L1, Moon Dynamics — no maker site. internet: 36Kr (14 Aug 2026) "165 cm tall", "weighs 60 kg", "dual-wheel-legged",
"a wheel under each of its two legs", 25 kg while moving; 瑞财经 (6 Nov 2025) "高165cm", "自重60kg", "单臂具备6个自由度"; hg 18 DoF,
hands 12, "2-finger gripping claws", 3 h, "Aluminum alloy".

166 Laborer C1, Glroad — maker glroad.com/ListIntroduction/info.aspx?itemid=549: 身高 "137.1CM", 重量 "38KG", 臂长 "57.9CM";
全身 "21", 单腿 "6", 腰部 "1", 单臂 "4(可扩展)"; 最大峰值扭矩 "150N.M", 减速比 "25"; 电池容量 "10AH", 续航 "2H(行走)、4H(站立)"; 算力 "Nvidia
Orin NX 100T/157T", "6轴IMU", "交互屏 深度相机 激光雷达", "阵列麦克风+5W扬声器"; legs, ">2M/S".

167 Laborer M1, Glroad — maker itemid=548: "187CM", "86KG"; 全身 "27", 单腿 "6", 头部 "1", 单臂 "1" (does not add up to 27); 最大峰值扭矩
"430N.M"; "22AH", "2H"; legs; 双臂负载 "50KG". internet: hg "7-DoF arms", head depth camera. Glroad's home page also names an
unnamed model "身高180cm,体重100kg,自由度31+2,…最大关节扭矩380N·m".

173 Lumen H1, Guanggu Dongzhi (HECbot) — maker hecbot.cn/product.html?type=22: "身高169cm，净重≈69kg"; "40个（双臂7x2、双腿6x2、头部2、灵巧手6x2）";
"自研一体化关节峰值扭矩512Nm"; "700 Wh", "2 h", "支持电池快换及充电"; "激光雷达 + RGBD相机"; legs listed and also a chassis (底盘), how they
combine not said.

174 Lumen S1, HECbot — maker page shows only the name (the table on it is H1's). internet: hg 35 kg, 130 cm, "31 body
DoF", 2 h, "NVIDIA Jetson Orin NX (157 TOPS)", "RGB-D depth camera, front stereo RGB, rear RGB, interaction camera",
LiDAR.

178 MagicBot, MagicLab — MagicLab lists X1, Z1 and "Gen1" (/en/human); no product named plain "MagicBot". The register's 54
kg / 138 cm is hg's (prototype, 42 DoF). Maker Gen1 page magiclab.top/en/human: "1740*580*280 mm", "Approcimately 70kg";
42 active DoF: neck 2, arm 7 each, hand 11 each (6 active, 5 passive), waist 2, leg 6 each; "≥ 350 N·m"; "25 Ah (1.35
kWh)", 3–5 h; 8-core CPU plus 100 TOPS; 3D LiDAR, depth ×2, fisheye ×3, microphone array, speakers; legs; "Aluminum
alloy" structure, "PC+ABS" exterior. Reseller: net 40 kg, total about 70 kg. MagicHand S01 (maker): 11 DoF, weight "580"
(no unit), 12 V.

181 MagicBot X1, MagicLab — maker magiclab.top/en/x1: "180×55.4×28" cm, total "70kg"; active "31": head 2, arm 7, waist 3,
leg 6; peak "≥350N・m", maximum "≥400N・m"; "Dual Battery System", "Hot-swappable Battery", "18Ah"; "8-Core High-Performance
CPU", "Orin NX" (X1 Ultra "Up to NVIDIA Jetson AGX Thor"); "Stereo Camera Module", "Head RGB-D Camera", "Waist RGB-D
Camera", "LiDAR (Optional)"; "Aerospace-grade Lightweight Aluminum Alloy", "Titanium Alloy", "High-strength Engineering
Plastics". Register 65 kg / 170 cm is hg's.

182 MagicBot Z1, MagicLab — maker magiclab.top/en/z1 (standard / Development Version): "1369*422*200mm"; "Approximately 40kg"
/ "40kg+"; 24 / 24–50 DoF: leg 6 each, head 1, waist 1, arm 5 each; knee "100N.m" / "130N.m"; "15-cell battery",
"10000mAh", charger "62V 5A", 2 h; 8-core CPU; "3D LiDAR + Depth Camera + Binocular Fisheye Camera + Head Tactile Sensor";
microphone array; 5 W speaker; "high-strength aluminum alloy and engineering plastics". Legs.

183 Maker H01, GigaAI — maker site title only. internet: hg 64 kg, 160 cm, 28 DoF, hands 14, "dual 7-DOF arms", 360°
LiDAR, wheeled, "Aluminum alloy + ABS composite shells"; ChipSilicon (contradicts itself, no sources).

185 Martian, Unix Group — maker unix-group.ai/martian/: 148 cm, 40 kg; legs 6 a leg, arms 7 an arm, waist 3, head 2, hand
"11-DoF dexterous hand"; "Motor Max Torque 150 N.m"; "9 Ah", "48 V"; "40T Computing Power Platform 32GB Ram"; "Depth Camera
+ RGB*2 + IMU"; legs. Register 50 kg / 160 cm is hg's.

186 Matrix-1, Matrix Robotics — maker matrixrobotics.ai/matrix-1: "180 cm", "67 kg"; "Actuator: 55, MPA 3.0"; hand "22
degrees of freedom"; "Peak Torque Density: 196N.m/Kg"; "2.28 KWh custom battery pack"; 5 h; "8 cores and integrated GPU";
"8 onboard RGB cameras"; "LIDAR and ultrasonic sensors … (optional)"; microphone array; speaker; 10 kg an arm. Legs or
wheels not stated.

The agent's summary: something for every robot. No readable maker hardware: JAKA K1, JAKA Kargo, Jupiter (IFA listing
only), KAI (KaiHand only), Kaleido 9, KAPEX, XMAN-R1, Kengo, KUAVO 5-W, Kuavo-my, L1, Lumen S1, Maker H01; Kinisi KR1 no
mass. Maker against register: Jingchu Elf 70 or 80 (70), MagicBot X1 70 (65), Martian 40 (50), MagicBot Gen1 about 70
(54).

---

## Batch 3, group 3: the research agent's report (2026-11-01), as received; not yet checked first-hand

maker = the maker's own page, release or model file; internet: X = second-hand; hg = humanoid.guide ("Not verified").
Its web-search budget ran out at PrimeBOT, ProWhite and PsiBot (and Foundation's battery, compute and sensors). HTTP 429
on every try: sharpa.com, switch-bot.com, galaxea-dynamics.com. "Sum" = the agent's own addition of the maker's numbers.

188 MEMO, Sunday Robotics — maker https://www.sunday.ai/technology: Height "1.7 meters", Weight "170 pounds"; home page
"rests at 4 feet", vertical reach "2.1 meters"; "Arms: 2×7", "Hands: 2×4", "Torso: 1", "Lower Body: 4" (sum 27); runtime
"4 hours", charge "1 hour"; "stable wheelbase", 1 m/s; "soft-to-the-touch silicone shell", "A blend of rigid and elastic
polymers"; IP67 / IP66 seen once, not twice. internet: hg 77 kg, 170 cm, 20 DoF; Humanoids Daily: "telescoping 'Z-axis'
spine", "custom dual-gripper". No torque, battery capacity, computer or sensors.

189 MenteeBot (2024) and 190 MenteeBot V3, Mentee Robotics — maker https://www.menteebot.com/bot/ (V3 only): "175cm",
"70kg", DoF "40", "Self-made actuators fully integrated on-board sensors and drivers", 1.5 m/s, payload "25kg".
internet: hg MenteeBot 70 kg / 175 cm / 40 DoF / 3 h, V3 65 kg / 55 DoF / 4 h (the register's 65 matches hg, not the
maker's 70); IE (V3): "dual Jetson Orin AGX processors", "hot-swappable battery system … more than three hours", 360°
vision with back and fisheye side cameras; The Robot Report (2024): "only vision-based cameras". Legs or wheels not
stated. Nothing from the maker for the 2024 prototype.

194 Mirokaï, Enchanted Tools — maker pages: no numbers. internet: IEEE Robots Guide "29 kg", "123 cm", "26 DoF (Neck: 3
DoF; Arm: 4 DoF x 2; Hand: 2 DoF x 2; Ear 1 DoF x 2; Wrist: 3 DoF x 2; Ball mobile base: 3 DoF)", "26 motors", "8 torque
sensors", 4 h, "2 NVIDIA Jetson NX", "2 RGBD cameras, 2 infrared cameras, and 9 time-of-flight cameras", "6 ultrasound
sensors", "4 microphones", "3 inertial measurement units (IMUs)", "Ball-bot mobile platform", "External shell made of
plastic parts. Internal structure parts mostly made of aluminum."; Kanematsu (distributor) "Height：123cm, Weight：26㎏";
hg 29 kg.

195 Moby, Noble Machines — maker: battery "5 hours", payload "23KG/50LB", 0.8 m/s, "Modular end-effectors"; no mass.
internet: Mike Kalil 170 cm, "a reported 34 degrees of freedom", "headless", "on two legs", "a single NVIDIA Jetson Orin";
NVIDIA case study: Jetson Thor dev kit, actuators with Schaeffler; Orbbec case study: "Orbbec Gemini 336L stereo 3D
cameras" (no count), "Livox MID-360 LiDAR"; hg 45 kg (the only mass), 170 cm, hands 10, "Composite polymer + aluminum
frame".

197 Modular, O-ID — maker https://o-id.net/ ("Specs indicative — full datasheet on request."): "172" cm, "70" kg, "30" DoF,
modules HEAD, TORSO.CORE, SHOULDER, ELBOW, FOREARM, DEX.GRIP, HOLONOMIC .BASE, payload "16" kg. internet: hg
"Electric servo/BLDC actuators + wheel hub motors", 4 h, "Aluminum alloy + composites".

198 Mornine (M1), AiMOGA (Chery) — no maker page readable. internet: CarNewsChina (citing the JD.com listing) and
ChinaEVHome "weighs 70kg", "167cm", "40 degrees of freedom throughout its body (excluding dexterous hands)", "0.7 kWh",
"one wide-angle camera", "two depth cameras", "one 3D LiDAR", "four ultrasonic radars"; IT之家 (2025-03-19) "167cm、65kg",
"41 个自由度", "单手 12 自由度", "最大关节扭矩为 512N・m", "0.7kwh", 2 h, "2 个深度相机、1 个全景相机", "3D 激光雷达", "4 颗超声雷达、1
颗 6 麦克风阵列"; humanoid.press "Full bipedal walking"; hg "Aluminum alloy".

201 N2, Noetix — maker pages title only. internet: RBTX 30 kg, "1,180 mm", 18 DoF, "peak torque of 150 Nm", "48V
quick-swap lithium battery", "up to 2 hours", "edge AI computing up to 67 TOPS", "3D vision sensors", "aluminum alloy
structure"; TMTPost 1.2 m, 30 kg; hg five joints a leg, four an arm, "48 V/7 Ah", "Rockchip RK3588s" plus Jetson,
structured-light depth camera.

204 Navigator 2, Zhejiang Humanoid Robot Innovation Center — maker site fetch failed. internet: ifeng / 潮新闻 (the centre's
published parameters) "身高165厘米", "体重60公斤", "AI算力达到275Tops"; mydrivers "体重约60公斤", "全身具备 41个自由度"; CSDN "可持续作业
2 个小时", hand "15 个手指关节，6 个主动自由度", "单手重量 600g"; hg 20 DoF. Legs.

205 NE01, GENISOM AI — maker pages show no numbers (a footnote on the maximum joint peak torque without its value).
internet: hg 145 cm, 40 kg, "In-house CHAMP integrated joint modules (180 N·m max peak torque)", 540 Wh, 2 h, aluminium;
ifeng: bipedal.

206 NEO Beta, 1X — maker announcement: no figures; maker hands page (version not named, "ship on every NEO"): "25 Degree
of Freedom" a hand ("22 fully actuated DoF in the fingers and palm, plus 3 at the wrist"), "3.5 Nm at the thumb CMC and
2.6 Nm at the finger MCP joints", wrist "17.75 Nm", "The motors live in the forearm". internet: Kozminski techblog "5 feet
5 inches", "66 pounds", "Clothed in fabric"; hg 30 kg, 165 cm, 55 DoF. Legs.

207 NEO Gamma, 1X — maker https://www.1x.tech/discover/introducing-neo-gamma: "1X's Tendon Drive", "four microphones",
speakers one in the chest and two in the pelvis, suit "3D printed from durable and soft nylon"; no mass. internet: hg 35
kg, 165 cm, 25 DoF. For context, the later home NEO (maker https://www.1x.tech/neo; a different version): 66 lbs, 5'6",
hands 22x2, arms 7x2, neck 3, spine 2, legs 6x2, 842 Wh, "Dual 8.85MP 90Hz Stereo Fisheye", 4 microphones, "Nvidia Jetson
Thor", "custom 3D lattice polymer" body.

208 Neo1, NeodraDynamics — maker release via PR Newswire APAC: "4-meter", "7-DOF humanoid arm", a micro digital hydraulic
cylinder of "1.1 kg" driving "1,000 kg", "5-finger dexterous hand", dual-arm payload "500 kg"; no mass. internet: Gadget
Review "weighing about 1.2 tons"; IE "41 active degrees of freedom" (39 hydraulic, two electric forearm joints); hg 1200
kg, 400 cm, actuators "1.6 kg, 10 kN"; hg news "stationary machine". Power source not published.

209 NEXO, Galaxea — maker release (Kyodo / PR Newswire): "30 degrees of freedom", "8-hour runtime", "wheeled dual-arm
robot", dual-arm payload "20 kg". internet: hg 85 kg, 168 cm, hands 12, "NVIDIA Jetson AGX Orin"; originofbots 78 kg
(compiled, not confirmed), swappable batteries, omnidirectional base.

211 NIX, Lumos — maker product page (NIX S3): "25.41 kg (total, incl. battery)", "89 cm", DoF "21" (arm 4, waist 1, leg 6),
"Peak joint torque 102 N·m", "282 Wh", 2 h, "Quick-detach", charger "67.2 V / 2.5 A", "RK3588", RGB camera, "4-mic array /
speaker", payload 3 kg, no hands; maker docs (Nix1) "Weight: 18 kg"; maker URDFs (github.com/LumosRobot/lumos_assets):
nix1_joint21 23.320 kg, nix1_v1 / v2 23.13632 kg, nix2-5 24.6422 kg; 21 revolute joints; effort 102 on hip, knee,
torso, shoulder, elbow, ankles 20 (nix1) or 17 (nix2-5). Register 20.

213 North, Sharpa — maker site 429. internet: hg 90 kg, 160 cm, 67 DoF, hands 44, Jetson Thor, wheeled base; Robotics
Center store "Net weight 60 kg"; IE SharpaWave hand 22 active DoF.

214 Northstar, UMA — maker page fields blank. internet: Bloomberg via The Star "about 40 kilograms (88 pounds)", "on wheels
instead of legs", "metallic" prototype; TechOrange: a target of about 40 kg; hg 165 cm, 24 DoF, hands 12.

215 Nova, ugo — maker https://ugo.plus/ai/ugo-nova/: "約 100 kg"; "(h)126〜162cm"; "腕部：7軸＋ハンド1軸2指（双腕）", "腰部：4軸（yaw
1軸 + pitch 3軸）", "頭部：2軸", "全22自由度", "車体部：4軸（メカナム4輪）"; "LiFePO4 | 50.6V | 22Ah", "約6時間"; "NVIDIA Jetson Thor";
"ヘッド x1（ステレオカメラ）", "ハンド x2（RGBカメラ）"; "可搬最大10kg". Register 90.

217 Onero H1, SwitchBot — maker site 429. internet: humanoid.press "174 cm (prototype spec)", "68 kg", 52 DoF; hg "~35" kg,
"~120–130" cm; IE and Yanko Design 22 DoF, "multiple Intel RealSense cameras", "cylindrical wheel base". Databases
contradict.

226 P0, Pink Robotics — maker https://www.pink-robotics.com/: "1,75m", "82kg", "32 DoF", payload "8kg". internet: hg hands
10, "2-finger gripping claws"; Humanoids Daily "In-house 3D printing and laser welding". Legs or wheels not found.

228 Phantom MK1, Foundation — maker https://www.foundation.bot/phantom (no version named): "5'-11", (1.8m)", "176lbs,
(80kg)", "29º" (metadata "19 DOF"), "proprietary cycloid actuators", "MAX PEAK TORQUE, 160Nm", "WRIST TORQUE, 20 Nm", "LEGS
TORQUE, >160 Nm", "SHOULDER TORQUE, 119 Nm", "VOLTAGE, 48V / 72V", payload "88.2lbs, (40kg)", 1.7 m/s. Battery, computer,
sensors not searched (budget).

237 PrimeBOT T1, PrimeBOT — maker pages empty. internet: hg only: 8.5 kg, 60 cm, 16 DoF, "QDD", 4 h, wheeled legs.

238 ProWhite, PL-Universe — maker https://en.pl-universe.com/Products/ProWhiteRobot: "Weight: 400kg",
"1051mm(L)*800(W)*2035mm(H)", arm "6" DoF, "Battery Capacity: 40v 100 Ah", "≥8h", "Four-wheel omnidirectional", "Liftable
torso", payload 7 kg an arm. internet: hg "~45–55" kg (the register's legs and 50 kg match hg, not the maker).

239 Psi V1, PsiBot — maker https://www.psibot.ai/en/products/product_psibot-v1/: "<180cm", "Waist：2-DOF", "Neck：2-DOF",
">8hours", "Computing Platform：Thor", "RGBD*4；Fisheye Camera*3", reach 683 mm; no mass. internet: hg 150 kg, 175 cm, 42
DoF, hands 22, Orin AGX (conflicts with the maker's Thor).

The agent's summary: something for every robot. No maker figure: Mornine, N2, Navigator 2, NE01, North, Northstar,
Onero H1, PrimeBOT T1. Partial: MenteeBot 2024 (nothing), NEO Gamma (no mass), Neo1 (no maker mass). Register against the
maker: ProWhite 400 kg four wheels (register legs, 50), Nova 100 (90), MenteeBot V3 70 (65), NIX 25.41 (20).

---

## Batch 3, group 4: the research agent's report (2026-11-01), as received; not yet checked first-hand

M = maker; I:<outlet> = internet, second-hand.

240 Pudu D7 (register 45 kg, wheels)
- 2024 version (M, Pudu press release via PRNewswire 19 Sep 2024, https://www.aap.com.au/aapreleases/cision20240919ae10581; also therobotreport.com): "weighs 45 kilograms", "stands 165 cm tall"; arms "30 degrees of freedom", "expanding to 50 with a dexterous hand attachment"; "a battery exceeding 1 kWh", "over 8 hours"; "fully omnidirectional chassis"; arms "can lift 10 kilograms".
- Current page (M, https://www.pudurobotics.com/products/d7, 2026 next-generation D7): "308.6 lbs（140 kg）", "68.9 in（175 cm）"; "23 (excluding end effectors)"; "7-DoF humanoid arms"; "180° rotating waist"; "360° Omni Chassis", "Dual-LiDAR Omni Chassis"; "Dual-battery design provides up to 4 hours of runtime, with hot swapping"; "NVIDIA Jetson Orin + RK 3588 dual-chip platform", "275 TOPS (Optional Chip Upgrade)"; "Front and rear LiDAR with vision, tactile, and auditory sensing"; arm rated 7 kg, peak 10 kg; max 20 kg; "Optional: Gripper / Dexterous Hand (grippers, three-finger and five-finger dexterous hands)".
- Launch release 1 Jun 2026 (https://technode.global/?p=124055): "payload capacity of up to 14 kg", "dual front-and-rear LiDAR", "fully autonomous battery swapping".
- None found: torque, actuators, materials.

241 Pudu D9 (register 55 kg, legs) — M https://www.pudurobotics.com/products/d9
- "65 kg"; "170 cm"; "Total DOF 42", "Single-leg DOF 6", "Single-arm DOF 7"; "Peak joint torque 352 N·m"; "15 Ah (0.72 kWh)"; "275 TOPS"; "RGB, RGBD, Tactile sensors, IMU"; hand PUDU DH11 "500 g", "11 (6 Motor)"; payload 20 kg, 10 kg per arm.

242 PX5, Xpeng (register 109 kg, legs) — maker: none found
- I:humanoid.guide https://humanoid.guide/product/px5: 109 kg, 150 cm, 22 DoF, 1.5 h; hands 11 DoF, "hand unit … weighs only 430g"; arm 7 DoF, "3kg maximum payload/5kg self-weight".
- I:Aparobot https://www.aparobot.com/robots/px5: "With battery, 109 kg"; 1500 mm; "22 DOF"; ">2 hours" (no sources).
- I:KrASIA, I:36Kr (现在，PX5只有1.5米; 小鹏自研了高性能的关节; 2小时以上), I:Electrek.

245 QUANTA X2, X Square Robot (register 95 kg, wheels) — M https://x2robot.com/en/product/quantum2
- mass not stated by the maker; "164cm"; "Whole-Body Degrees of Freedom 62 (Dexterous Hand)", torso 6, chassis 2, gripper 2, hand 20; 6 kg per arm; 2D LiDAR ×1, ultrasonic ×4, RGB-D ×3, TOF ×2, BEV cameras ×3.
- I:humanoid.guide: 95 kg, 172 cm, "tendon drive", "composite shell over alloy frame".

249 RAISE A1, AgiBot (register 55 kg, legs) — M https://www.agibot.com/products/A1
- 55 kg; 175 cm; "49+" DoF; "PowerFlow" joints, "Peak Torque 350N·m", "weighing only 1.6KG"; "200 TOPS" (also "200Teraflops"); microphone array, Lidar, RGB-D; hand "Active DoF 12 Passive DoF 5"; arm load 5 kg. No battery. No URDF found.

250 RayNex G3, NineRay (register 60 kg, legs) — M https://www.nineraygroup.com/en/humanoid.html
- "60 kg", "173 cm", "32 DoF (Body)"; "Full-body 44 Force Control Units"; "Linear & Harmonic Rotary Joints", "Frameless Torque Motor", "Maximum joint thrust density 4500N/kg"; "AIU"; "8H Run Time".
- I:China Daily HK: "seven for each arm, six for each leg, and three each for the neck and waist"; I:humanoid.guide hands 12 DoF, "Aluminum/Composite".

258 REX G1, RoboScience (register 80 kg, wheels) — M https://www.robosci.com/rex-g1/
- mass not stated; 高度覆盖1100–1700mm; 22个自由度: "2头颈、7×2臂、2腰部、1升降以及3底盘"; 热插拔换电, 4小时; 2070 TFLOPS; 双臂抱持10KG.
- I:humanoid.guide: 80 kg (no source), "Not Verified".

259 RNoid, Robot.com (register 50 kg) — M spec sheet https://lp.robot.com/rnoid/specs.pdf rev. 003
- "90 kg Total weight"; "1.7 m Height"; "0.55 m Wheel base", omnidirectional; "Dual 7-DOF" arms, "4-DOF Torso", "2-DOF Neck"; 4 kg per arm; "Battery 3 hours, Supports plug-in"; "AMD Ryzen 5 7640HS", "NVIDIA Jetson AGX Orin"; RGB-D head and chest, "2x RGB-D camera — Wrists", front + rear LiDAR, "8 units Ultrasonic sensors", mic and speaker.

261 Robbyant R1 (register 110 kg, wheels) — maker: none found (robbyant.com lists R2 and KUAVO 4 Pro; /product/R1 404)
- I:humanoid.guide: 110 kg, 160 cm, 34 DoF, "48 V DC geared motors with encoders" ("Not verified"); I:aiwiki (uncited); I:Oninvest citing Bloomberg: "joint modules were provided by Ti5 robot", "chassis by Galaxea AI".

262 RoBee, Oversonic (register 180 kg) — M brochures https://oversonicrobotics.com/media
- Series R 10/2026 (Oversonic_Robee-R-2026-eng.pdf): "Up to 293 kg"; 165–199 cm; omnidirectional drive; depth cameras head, waist, base; "Laser 3D", "Laser scanner safety"; "Batteries included 2", "Lithium ion", "Up to 8 hours"; 7.5 kg per arm.
- Series M 10/2026: "180 cm", "150 kg"; "8 mecanum Ø 100mm"; "Degrees of freedom per arm 6", "per leg 6"; 1 battery, lithium ion, up to 4 h; 5 kg per arm.
- Series F 10/2025: "850 kg", 200 cm, "7-axis articulated arms", 6 batteries "Lithium ion + Graphene supercap", 8 cameras.

263 Robin, Roboligent (register 80 kg, wheels) — M https://www.roboligent.com/robin/
- "105 kg Total weight"; 680 × 600 mm; "Two 7-DOF arms", own force-controlled actuators; omni base with motorized lifting column, floor to 2 m; payload 7 / 14 kg; runtime "6–12 hr"; "Parallel gripper, 120 mm stroke"; five-finger hand available.

264 ROBO-T1, Robo Robotics (register 50 kg) — M https://robo.inc/: "two 6-DOF robot arms with grippers"; no mass.
- I:humanoid.guide 50 kg, 130 cm, 12 DoF, "Aluminum + composites" ("Not verified"); I:Origin of Bots "Approx. 45–60 kg", wheeled.

267 ROBOTERA Q5 (register 70 kg, wheels) — M brochure https://a.storyblok.com/f/298593/x/5695abe67b/q5-brochure-en-robotera.pdf
- "582*519*1650 mm"; "70 Kg"; 44 DoF: "Neck: 2 DoF", "Arms: 7 DoF × 2", "Hands: 11 DoF × 2", "Waist: 1 DoF", "Legs: 3 DoF", "Chassis: 2 DoF"; "Drive Wheels ×2", "Omni Wheels ×4"; "3D Laser Radar+Stereo Camera"; "Load Runtime > 4hour", "Supply Voltage 60 V"; "XHAND Lite 11 DoF".

270 SA02 (SAO2), EngineAI (register 25 kg) — maker: no page
- I:TechNode citing EngineAI's WeChat: "1.25-meter-tall", "25-kilogram", "28 degrees of freedom", "dual high-definition cameras"; I:ifeng/ZOL reading the official poster: 身高约为1.25米, 体重约为25公斤, 26个以上自由度（含手指）, 两个高清摄像头.

273 Sherpa Mecha, Ati Robotics (register 180 kg, wheels) — M https://www.atirobotics.ai/products/humanoid/sherpa-mecha/ and brochure sherpa-mecha.pdf
- mass not stated; "1100 mm – 2000 mm — extending torso"; "19 degrees of freedom across two arms"; "3D LiDAR and Camera"; "55 Ah × 2"; payload 12 kg; "Carbon-fibre" arms.
- I:humanoid.guide: 180 kg, 200 cm, 21 DoF.

275 SkyWalker 2, EIR Technology (register 55 kg) — maker: no data
- I:36Kr Japan: 身長165センチ、体重55キロ, 2時間; I:humanoid.guide: 55 kg, 165 cm, 55 DoF, hands 12.

277 Spaceo M1, Muks Robotics (register 65 kg, wheels) — M https://muksrobotics.com/spaceo-m1
- "Weight (With Battery) ~45 kg"; single arm 5 DoF, base 2, total 12; "Maximum Torque of Arm Joint ~160 kg cm"; BLDC servo; "25.6V, 45Ah LiFePO4"; Ryzen 7, "Orin AGX (~275 TOPS) / RTX 5070"; RGB 5MP, RealSense depth, 2D LiDAR, 4-mic array; "Aluminium body with polymer covers".

278 Spaceo Pro, Muks Robotics (register 65 kg, wheels) — M https://muksrobotics.com/spaceo-pro
- "Weight (With Battery) 60 kg"; total 20 DoF: arm 6 each, base 2, waist 1, head 2; "Maximum Torque of Arm Joint 66 Nm", "Waist Joint 90 Nm"; "25.6V, 45Ah LiFePO4"; Ryzen 7, "Jetson Orin AGX (~275 TOPS)"; "RGB Camera*3 5MP", RealSense depth, 4-mic; "Aluminium body with polymer covers".

280 Star1, Robotera (register 63 kg, legs) — M GitHub https://github.com/roboterax/models, star1/urdf/l3_with_hand_fixedpin_xml.urdf
- README 55 DoF: legs 6×2, arms 7×2, hands 12×2, waist 3, head 2; URDF robot "l3", 55 revolute joints; efforts: neck 35 ×2; arm shoulder pitch, roll, arm yaw, elbow pitch 110; elbow yaw, wrist pitch, roll 35; waist pitch, roll 220, yaw 110; hip roll 255, hip yaw 100, hip pitch 400, knee 400, ankle pitch 100, roll 100; fingers 1.1 and 0.4; link masses about 64.0 kg (to be summed by script).
- I:Gamersky: 400Nm 最大关节扭矩; 双腿12、双臂14、腰部3、颈部2; I:humanoid.guide: 63 kg, 171 cm, 4 h.

282 StarBot Flex (register 50 kg, wheels) — M https://www.starbotusa.com/: "5 ft 9 in", foldable wheeled; "final specifications to be announced". I:humanoid.guide 50 kg.

283 StarBot Nova (register 32 kg, wheels) — M https://www.starbotusa.com/: "70 lb"; "5 ft"; "two 7-DOF arms"; "Wheeled base, differential drive"; depth cameras (RealSense class), RGB camera, IMU; "10–12 hrs".

284 Steve, Sulu.be (register 140 kg) — maker: no figures. I:GE Reports 2015: "weighs 100 kilograms", "stands two meters tall"; I:humanoid.guide 140 kg.

286 Synthia, Syntheva (register 30 kg, legs) — M https://robotics.syntheva.no/products/synthia: "9.8 - 12.0 kg"; "165 - 190 cm"; "23 powerful and precise servos"; BCM2712 or RK3588S; two cameras, a microphone; modular, starting as a head on a headstand.

287 Syntro, WorkFar (register 108 kg) — M https://www.workfar.com/product/syntro
- "240 lbs (108kg)"; "1.7m"; 45 DoF: head 2, arms 4 ×2, wrist 3 ×2, hands 12 ×2, waist 2, wheels 3; "3 All-directional Omni Wheels"; "Maxon Motors and Harmonic Drives"; "Swappable Batteries 1.2 kWh"; "Intel Multi Core I5"; 2D LiDAR, cameras, microphones; "Aluminum / Stainless Steel / Carbon Steel / Brass / Acetal / Carbon-fiber Filament".

291 TARA GEN1, iHub Robotics (register 75 kg) — maker: title only
- I:humanoid.guide: 75 kg, 163 cm, "Closed Loop Stepper", "Harmonic Drive", "Mild steel", 8 h; I:aiwiki (uncited): wheeled.

Summaries (the agent's): no maker data at all: PX5, Robbyant R1, SkyWalker 2, Steve, TARA GEN1 (SA02 only relayed). No maker mass: PX5, QUANTA X2, REX G1, Robbyant R1, ROBO-T1, Sherpa Mecha, SkyWalker 2, StarBot Flex, Steve, TARA GEN1. Maker mass not the register's: Pudu D7 (45 in 2024, 140 kg the 2026 one), D9 65, RNoid 90, RoBee R ≤293 / M 150 / F 850, Robin 105, Spaceo M1 45, Spaceo Pro 60, StarBot Nova 70 lb, Synthia 9.8–12.

---

## Batch 3, group 5: the research agent's report (2026-11-01), as received; not yet checked first-hand

maker = the maker's own page, image or press release; internet: X = second-hand. Its web-search budget ran out near the
end (no maker site searched for TARS). JS-only sites: ymbot.com, yqbionics.com, lejurobot.com, the ubtrobot.com U1 Pro
page. No URDF or MJCF of these 25 makers found.

292 TARS, TARS Robotics (它石智航) — maker: none found (humanoid.guide's tarsupv.com is a rover team). humanoid.guide
("Not verified"): 80 kg, 160–175 cm, DoF "Assumed 30–40+", "Electric servo actuators", runtime 3 h, "Aluminum + plastic
composites".

293 Tau Humanoid, Tau Robotics — maker https://www.tau-robotics.com/: cameras on head and wrists, a speaker, microphones
disabled. humanoid.guide ("Not Verified"): 132 cm, 35 kg, "Planetary reducers", "2 per gripper", "Aluminium alloy and
engineering plastics", 2 h; humanoid.guide news citing MarketWatch: "modified Unitree G1 robots", "pincer hands"; aiwiki
citing USA Today: about 77 lb, 4 ft 4 in.

304 Tobi, TwoLabs — maker: no hardware. humanoid.guide ("Not Verified"; says TwoLabs "has not yet published hardware
specifications"): 60 kg, 150 cm, 16 DoF, hands 6, 5 h, "Aluminum frame with soft-touch polymer covers".

305 Tora DoubleOne, PaXini — maker parameter image https://paxini.com/en/robot/doubleOne
(/images/en/tora-double-parameter.png, "*Data from PaXini AI Lab"); models P (omnidirectional) and X (obstacle-crossing):
- P "671 mm x 548 mm x 1276~1638 mm"; X "767 mm x 486 mm x 1330~1692 mm"; armspan 2028 mm; no mass.
- "Total Joint Motors (excluding dexterous hands & drive wheels)": P "20", X "22"; "最大 52 个关节自由度".
- "Peak Joint Torque (full body) 207 Nm".
- Battery "47 Ah (1214.01 Wh), supports quick release"; "Approx. 8 hours".
- "Nvidia Jetson AGX Orin Dev. Kit 64G"; "RGB Camera: 1 (head). RGBD Camera: 2 (head, abdomen). 3D LiDAR: 1 (head).
  Ultrasonic Sensors: 6 (chassis). IMU: 2 (head, chassis)."; "Front and rear 8-Microphone Array"; "10 W Speaker".
- P "4WD&4WS omnidirectional chassis" (双舵轮设计); X "4-wheel drive active obstacle-surmounting chassis".
- Hands: any of PaXini's tactile dexterous hands; arm rated 3 kg, dual 10 kg.
- internet: rbtx Model X 73 kg, 1,687 mm, 58 DoF, "18‑DOF hands"; Model P 70 kg, 1,671 mm, 56 DoF; humanoid.guide 70 kg.

310 U1 Pro, UBTECH — maker page: no figures; UBTECH release (GlobeNewswire via adnkronos): the series "88
high-degree-of-freedom joints, a battery life of 2 to 4 hours". internet: humanoid.press "Male model: 183 cm, 42 kg",
"Female model: 168 cm, 35.2 kg", 88 DoF, bipedal, "Silicone skin".

316 Vesoma 1 — maker: "design visualisation. Under development."; no figures. humanoid.guide: 170 cm, 75 kg ("exists
only as a design vision").

317 Voxel, Tuesday Labs — maker https://tuesdaylabs.com/robot: "7-DOF Arms with Fully Actuated Wrists", "1-DOF Grippers",
"Z-Shaped Legs", "Stereo RGB + Wide-Field Vision". humanoid.guide: 45 kg, 150 cm, 22 DoF.

319 W1 Pro, DexForce — maker https://en.dexforce.com/w1pro.html:
- "110kg"; "682mm*550mm*1636mm"; arm "7 DOF (Shoulder: 3; elbow: 1; wrist: 3)"; "Waist: 2 DOF"; "Neck: 2 DOF"; "Leg: 2
  DOF"; hands "6 DOF per dexterous hand" / "2 DOF per two-finger gripper"; chassis "8 DOF for omnidirectional" / "2 DOF
  for differential"; "Max total DOF: 40pcs" / "34".
- "Optional: LiFePO4 Battery (40 Ah)"; "Dual-PC Architecture (≥300 TOPS)"; binocular vision, "Wrist-Mounted Cameras×2",
  navigation cameras 2, "LiDAR 2 pcs"; "Differential (Optional: Omnidirectional)"; dexterous hand standard; 10 kg an arm.

320 Walden, Walden Robotics — maker: no figures; IEEE Spectrum: wheeled base, two-finger grippers. humanoid.guide: 90 kg,
165 cm, 24 DoF.

321 Walker C, UBTECH — maker https://www.ubtrobot.com/en/humanoid/products/WalkerC: "43kg", "163cm", DoF "20", "Lithium
Battery 48V 15Ah", walking 2 h; "RGBD*2, All-Scenario Binocular", "Structured Light3D Camera*2", IMU; electric.

322 Walker C1, UBTECH — maker page images: "53 of DOF", "Height 164cm", "Weight 55kg"; "Fish-eye Camera*2", "Binocular
Camera*1", "Monocular Camera*1", "Speaker*2", "Microphone*4", "High-precision IMU*1" ×2, "Dexterous Hands(Optional)*2".

324 Walker S1, UBTECH — maker images: "Height 172cm", "Weight 76kg", "Load 15kg", "Self-developed Integrated Joints …
Peak Torques 250N.m"; "RGBD*1" head, "Stereo RGB Camera*2", "Speaker*2", "RGBD*1" torso, IMU, "Six-axis Force Sensor*2"
wrists and ×2 ankles. internet: aiwiki 41 DoF: legs 12, arms 14, hands "10+", waist 3, neck 2.

325 Walker S2, UBTECH — maker images: "Height 176cm", "Weight 70kg", "52 of DOF"; "Gen-4 Industrial Dexterous Hands: 11
of DOF"; "4 Array Microphones, 2 Speakers"; materials "Rigid-flex Heterogeneous Composite, Aerospace-grade Aluminum
Alloy, 3D Printed Primary Frame, 3D Knitted High-elastic Fiber Material"; "Fish-eye Camera*2", "RGB Camera*2", "RGBD
Camera*1" front and back, "Six-axis Force Sensor*2"; dual battery, swap in 3 minutes. internet: batterydesign.net
"Total energy = 2.3 kWh", "Nominal voltage = 48 V", "two battery packs".

328 X-Bot, Yue Quan Bionics — maker JS-only; humanoid.guide ("Not Verified"): 167 cm, 60 kg, 51 DoF, knee/hip "~340
N·m", ankle "~46", arm "~60"; "NVIDIA Jetson Orin NX 16GB" + "Intel NUC12 i7"; D435, 360° LiDAR; 2 h.

330 Xiao Di, BYD — no BYD page; The Next Web citing KrASIA quoting a deleted BYD post: "1.61 metres", "58.5kg"; IE: 31
DoF (from a CNIPA patent); 163.com: 31 DoF.

331 Xiao Liu, Tencent Robotics X — maker: none; IT之家: parameters not yet disclosed by Tencent, "键绳传动" (tendon drive).
humanoid.guide: 70 kg, 165 cm, 38 DoF, wheeled; humanoid.press (contradicting): ~55–60 kg, bipedal.

333 XiaQi (夏起 X02), Digit Robotics — maker parameter image https://www.digit.com.cn/ProductsDetail/93.html: 身高 "169cm";
重量 "≤69kg"; "40+主动自由度"; 电池 "700w•h"; 续航 "≥2h"; 单手负载 "1kg".

334 XTRON KUAVO-MY, Leju Robotics — maker: no specifications; internet: chipsilicon 55 (45–55) kg, 166 cm, 30 DoF, "360
peak" Nm; humanoid.guide 145 cm, 45 kg, 26 DoF; robozaps 45 kg, 147 cm.

339 YMBot C, Jiangsu Yunmu — maker JS-only; humanoid.guide ("Not Verified"): 75 kg, 174 cm, walks on two legs, bionic
skin.

344 YMBot H, Jiangsu Yunmu — maker JS-only; humanoid.guide: 75 kg, 170 cm, wheeled base, 6 h.

345 Yogi, Cartwheel Robotics (shut down in 2026, humanoid.press) — maker site unrelated now; humanoid.press: height and
weight "Not published"; humanoid.guide ("Not verified"): 47 kg, 150 cm, 36 DoF; aiwiki (uncited): 76 cm, 8 kg, 250 Wh.

346 Zerith H1, Zerith Robotics — maker https://www.zerith.com/product/ZerithH1/: "23总自由度", 7-axis arms, floor to
2156 mm, "4h", "1 kg 单臂负载", wheeled-arm humanoid. internet: rbtx "55 kg", "1,800 mm", "universal wheel chassis", 3D
LiDAR, depth; pconline 55 kg.

347 Zerith Z1 — maker: no page; 36Kr Japan: 27 joint axes, 最大トルク150Nm; rbtx: "33 kg", "1,450 mm", 21 DoF, "up to 150 Nm
peak joint torque", RGB, depth, LiDAR, IMU; pconline: 33 kg 含电池, 145 cm, removable battery.

348 Zeus 1, PL-Universe — maker site does not list it; China Industry News (the company's WRC 2025 "大白"): height
165~195 cm, "300Kg的整机重量", 7-DoF arms, "48V、40Ah电池", ≥8 h, four-wheel omnidirectional; RoboHorizon names it
"Zeus 1": 1.6–1.9 m, 300 kg. Whether 大白 is the Zeus 1 is not stated by the maker.

354 PR-OMNI, Perceptyne — maker https://www.perceptyne.com/product/omni: 5'2"; "120 kg"; "Aluminium"; "Dual arms, 7 DOF
each"; head "2 DOF"; "3 RGBD cameras (2 wrists + 1 head)"; dual LiDARs; "3 kWh (2 × 1.5 kWh, swappable)"; 6 h; "Nvidia
Jetson Orin + Intel NUC 5th Gen"; "4 Wheel holonomic drive"; "Vertical gantry range: 800 mm".

The agent's summary: no maker hardware figure: TARS, Tobi, Vesoma 1, Walden, X-Bot, Xiao Di, Xiao Liu, XTRON KUAVO-MY,
YMBot C, YMBot H, Yogi, Zerith Z1, Zeus 1; U1 Pro series-level only; no maker mass: Tora DoubleOne, U1 Pro. Maker mass
against the register: Walker S2 70 (register 73), Walker C1 55 (50), W1 Pro 110 (110), XiaQi ≤69, PR-OMNI 120, Walker C
43, Walker S1 76.

---

## Types 5 and 6, seven new robots: the research agent's report (2026-11-01), as received; not yet checked first-hand

maker = the maker's own page, release, blog, GitHub or paper (for Alex and Nadia IHMC's own pages and papers);
internet: X = second-hand. Its WebFetch passes pages through a small model; the EngineAI URDF values were read twice.

44 Atlas (old, hydraulic), Boston Dynamics — maker blog "Build It. Break It. Fix It.": "its 190-pound frame" (86.2 kg),
hoses "rated for a pressure of 3,000 pounds per square inch", "custom titanium fittings", "braided Teflon", "plastic
covering"; BD's 2016 video text via IEEE Spectrum: "about 5' 9" tall", "weighs 180 lbs" (81.6 kg), "electrically powered
and hydraulically actuated", "LIDAR and stereo sensors in its head"; BD blog "Flipping the Script": "a time-of-flight depth
camera", "IMUs, joint positions, and force sensors"; "grippers" (image alt text). internet: Wikipedia (citing
bostondynamics.com/atlas, 2020) "150 cm … 80 kg (180 lb)", 2021 "5 feet tall (1.5m) and weighs 190 pounds (85 kg)", 28 DoF
(2013) and 20 DoF (2021), "three onboard computers"; IEEE Robots Guide 150 cm, 80 kg, 28 DoF, "Custom battery",
"Mixture of titanium and aluminum 3D-printed parts"; hg 150 cm, 89 kg (its text "around 190 pounds"). No torque, no
battery figure. BD's own spec page is no longer online.

191 MH3, Mirsee Robotics — maker https://www.mirsee.com/: "31 degrees of freedom" (MH2 24, MH1 28), "10 Hour Runtime",
"Wireless Charging", "Power off brakes", "Best in class Hands", "Highest Payload Mobile Base"; no mass. internet: hg 180
cm, 125 kg ("Not verified"), hands 6, "BLDC", "Harmonic & Planetary", "12MP", "Aluminum 6061", IP54; aiwiki "Weight (with
battery) 125 kg (276 lb)"; originofbots 75 kg (and "Legged", wrongly); IE "Hadron Vision System … NVIDIA Jetson",
"wheeled mobile platform" with mecanum wheels.

288 T800, EngineAI — maker https://en.engineai.com.cn/product-t800 and the CN page: "173cm"; "Varies by Configuratoin:
75kg~85kg" ("随配置版本有所差异，范围：75kg～85kg"); editions: Basic / Open Source 25 (neck 2, waist 1, arm 5, leg 6), Pro
"29+14（Dexterous Hand）=43" (arm 7, leg 6, hand 7, waist 1, neck 3 EN / 2 CN), Max "32+14=46" (neck 3, waist 3); "Max torque
450 N·m"; "Ultra-High-Speed Internal Rotor Permanent Magnet Synchronous Motor"; "modular solid-state lithium battery",
"C24标配（支持快拆）", 3–5 h; "RK3588S" (CN), Basic "Orin NX 16G", others "AGX Orin 64G"; binocular camera; 3D LiDAR (Pro,
Max); "Aviation Aluminum + Titanium" ("航空铝+钛合金"); hand "7 degrees of freedom … 5 kg … tactile". Maker GitHub
engineai_robotics_description: serial_t800.urdf (v1.1, 25 moving joints): hip pitch 415, hip roll 370, hip yaw 222, knee
415, ankles 160, torso yaw 222, shoulder 160 × 3, elbow pitch 160, elbow yaw 52, head 52 × 2; masses 84.988 kg by hand;
serial_t800pro.urdf (43 DoF, v1.2): the same plus wrist 5 × 2 and fingers 1.1 × 7 a hand, 85.227 kg by hand. internet:
chipsilicon "Ternary Li: 71.4V / 20Ah …; Solid-state opt.: 74.8V / 40Ah"; 4gltemall "72V". Register 60 kg = hg's.

301 TITAN, RoboForce — maker https://www.roboforce.ai/technology and two releases: height "2.10m", "1.50m-2.10m 600mm
Lifting Range", payload "40kg" peak dual arm, reach "1100mm", "8h" "Per Battery Pack", "tracked, wheeled, and other
mobility configurations", end-effector images; **no mass**. internet: originofbots "120 kg" (unsourced, not confirmed);
hg, aiwiki, The Robot Report, Aparobot: no weight.

24 Alex, IHMC — maker https://robots.ihmc.us/alex-humanoid: "179 cm", "85 kg"; "29 degrees of freedom"; "2+ hrs"; "1.5+
m/s"; "15+ kg"; "custom, highly backdriveable, powerful quasi-direct drive actuators"; IHMC news (19 Nov 2025): "will
weigh 85 kilograms with a battery"; arXiv 2609.01518 (IHMC): "PSYONIC Ability Hands … 6 degrees of freedom each", "ZED X
Mini". No torque figures (the actuators page has no text).

202 Nadia, IHMC — maker IHMC news (19 Nov 2025): "weighed about 100 kilograms"; arXiv 2411.03532 (IHMC): "6 degree of
freedom (DoF) legs, a 3 DoF spine, 7 DoF arms, and 1 DoF grippers", Moog Integrated Smart Actuators (ankle, knee, hip
pitch and roll, spine pitch and roll), electric hip and spine yaw, cycloidal arm actuators, "tethered to a hydraulic
pump", "ZED 2i", pelvis IMU, "SAKE EZ Grippers", "carbon fiber exoskeleton for the thighs, shins, and torso". internet:
IEEE 2022 (Griffin) "about 90 kilograms right now, without the hydraulic pump or battery on board"; hg 190 cm, 100 kg.

351 Fuxi (伏羲), NORINCO — internet only: Global Times reporter via 163.com (6 Nov 2025) "伏羲机器人整机高180厘米，重85公斤", the
institute's "伏羲的6自由度灵巧手"; NORINCO's release (19 Aug 2026, via Global Times and People's Daily): its teleoperation
system for "full-size humanoid robots weighing around 90 kilograms" (a class, not Fuxi's mass); originofbots 170–180 cm,
"Approx. 90 kg", 2–4 h, bipedal. NORINCO's own page did not load.

The agent's summary: something from the maker for every robot. No battery voltage or capacity: Atlas, MH3, TITAN, Alex,
Nadia (T800's only from resellers). No joint torque: all but the T800. TITAN: no DoF, no materials, no mass anywhere but
originofbots' unsourced 120 kg. Register against the sources: T800 60 (maker 75–85, URDF 85.0–85.2), MH3 125 (aggregators
only), Atlas 89 (hg only; BD 180 lb in 2016, "190-pound"), Fuxi 90 (a class; 85 kg reported).

---

## Types 5 and 6, agent 2 (2026-11-01): T800, MH3, TITAN, Moby, Kaleido, Neo1, Phantom, Fuxi; as received, checked in types56_firsthand.md
T800 (maker docs engineai.com.cn/open/docs/t800/...): 05/08 battery "三元锂电池", "标称容量 20Ah", "标称电压 61.2V", "电池能量 1.22kWh", "最高充电限制电压 71.2V", "系统总质量 ≈7.2KG", "PACK 外壳材质 铝合金", "快拆换电 支持", "电池单独充电（机身不支持）"; 05/02 "三元锂电池（1.22KWh）", "带电重量 约84.5kg" (Dev), "约85.3kg" (PRO); 05/05 motors Q25H 50 N·m 0.5 kg 48 V, Q50H 160 N·m 0.95 kg 63 V, Q200H 222 N·m 1.65 kg, Q300H 370 N·m 2.1 kg, Q300H-L 415 N·m 2.6 kg, "全行星", "双编码"; 05/03 "Nezha" PC 4 cores, AGX Orin 64GB; 05/04 head binocular RGB 1, lidar 1, IMU 1, torque sensors, "环麦 ×4", 2 speakers, Odin2 depth camera; 05/06 hand 7 DoF, "单手 740g", 5 tactile sensors.
MH3: no mass (maker pages, Financial Post, IE, CTV, BNN); FP quoting the CEO "lift up to 11 kilograms in each arm" vs IE 30 kg; Mirsee innovations: M-Drive haptic, hybrid hydrostatic actuator for its plastic surgical robots, Hadron Jetson, AMP base (not tied to MH3).
TITAN: no mass, DoF or Wh; RoboForce 2026-03 news "Powered by NVIDIA Jetson Thor at the edge" (the company's stack); TechCrunch Jan 2025 prototype "about one and a half meters tall".
Moby: maker's blog (UCR Substack 18 Mar 2025) "Moby's 72 Kg body moves with an average power consumption of 200W", "five to six-hour shifts", "a single NVIDIA Jetson Orin"; NVIDIA case study Jetson Thor dev kit (later), Schaeffler actuators; Arm newsroom STM32 controllers; legs.
Kaleido 9: Mynavi 30 axes, torque kept from 8, 30 min on the robot alone, chest LIDAR, head stereo; Kawasaki blog 2026-03 the Kaleido Station on wheels as a charging station; Kaleido 7 (PC Watch 2022) 179 cm, 83 kg, 34 DoF; Kaleido 8 (robotatta) 86 kg, linear motors in some joints; Kawasaki 2019 85 kg, 32 axes; Japanese blog 2025 magnesium alloy frame, 6-axis ankle force sensors.
Neo1: maker release Sep 2026 1.1 kg cylinder, 7-DOF arm, 5-finger hand, 500 kg; maker release Oct 2026 (reposts) "4-Meter & 1.2-Ton", "41 full-body active degrees of freedom", "all 39 core joints use self-developed miniature digital hydraulic linear actuators", "Weighing only 1kg", "two forearm rotational joints adopting electric drive"; power unit none found; neodradynamics.com TLS untrusted.
Phantom MK1: maker page torques; TBS News (UNB, BBC-based, 9 Jun 2026) MK-1 "lacks a battery", MK-2 about 6 h, 360° cameras; AMD deal 23 Jul 2026 (Pulse 2.0, Defined VC) "AMD Kria AI system-on-modules powered by AMD Ryzen AI Embedded X100", hands "23 degrees of freedom" via FPGAs; NBC caption "5 feet 11 inches", "nearly 180 pounds".
Fuxi: 6-DoF hand; The News Lens "身高約180公分、重約85至90公斤"; 科技日报 exhibits without figures; ifeng's 72 V/30 Ah about humanoids in general.
PDFs: a WRC 2026 image-only PDF (Fuxi search); global.kawasaki.com/news_230921-1e.pdf (not opened).

---

## Types 5 and 6, agent 1 (2026-11-01): Atlas (electric and hydraulic), H1, DR02, CYBORG; as received, checked in firsthand_types56.md

Atlas, electric: no joint torque found (BD's pages, its webinar, Hyundai Mobis news, IEEE Spectrum, Korean press);
webinar: "two types of motors that can be used in any one of the joints", "only one fan in the robot, and it's in the
head"; The Financial News (Korea, LS Securities): "Each Atlas unit contains 31 body actuators"; BD: "Hyundai Mobis will
supply the actuators"; battery "four hour battery life", swaps in under three minutes, two batteries; Battery-Tech
Network ("industry sources"): "46-series cylindrical ternary battery cells"; BD release: "NVIDIA Jetson Thor computing
platform"; BD product page "Tactile and 360° camera view", IP67; hands (BD blog) "13 degrees of freedom (DOF), directly
actuated", "four DOF opposable thumb", "single actuator type", "GR2 had 7 … GR3 now has 13"; "90 kg (198 lbs)", "1.9 m",
56 DoF.

Atlas, hydraulic (2016 to 2024): no torque found; BD blog: hoses "3,000 pounds per square inch (PSI)", burst "closer to
10,000 PSI"; Fluid Power World 2018 (BD's Aaron Saunders): "28 active degrees of freedom", its HPU "approaching a Kilowatt
per kg", "Atlas' manifold has 18 valves", "30-60 minutes", "about 1.5 meters tall and weighs 80 kg"; BD's 2016 text via
The Robot Report "electrically powered and hydraulically actuated", "LIDAR and stereo sensors in its head"; BD blog
"IMUs, joint positions, and force sensors", "time-of-flight depth camera … 15 frames per second"; masses 82 kg (2016),
86 kg ("190-pound"), 80 kg (FPW, IEEE Robots Guide). The DRC Atlas (2013 to 2015, a different robot): DARPA "330-pound",
"28 hydraulically actuated joints", 2015 "345 pounds (156.5 kilograms)", "3.7-kilowatt-hour lithium-ion battery pack",
"new variable-pressure pump"; DRCSim atlas_v5.urdf (OSRF, not BD) efforts knee 890, hip pitch 840, ankle pitch 740 N·m,
link masses 157.083 kg.

Unitree H1: page "Knee Torque About 360N.m", "Hip Joint Torque About 220N.m", "Ankle Torque About 59N.m", "Arm Joint
Torque About 75N.m"; H1-2 waist 220, ankle "75x2", shoulder and elbow 120, wrist 30; "15Ah(0.864KWh)", "Max Voltage
67.2V"; Intel Core i5 and i7, Orin NX optional; "3D激光雷达 + 深度相机"; h1.urdf efforts hip 200, knee 300, ankle 40, torso
200, shoulders 40 / 40 / 18, elbow 18, its links 59.338 kg; h1_2_handless.urdf 66.984 kg.

DEEP Robotics DR02: page "约68kg" / Pro "约78kg" (with battery), 21 / 31 DoF, 72 V, AGX Orin (Pro); ElectronicsForU "20Ah,
1440Wh swappable battery"; model files DR02-pro.urdf (31 joints, efforts 363 / 137 / 50, 78.085 kg) and DR02-std.urdf
(21, 67.575 kg); J-series datasheets (J80-27P 1.48 kg 84 N·m, J100-64P 2.72 kg 180, J100-116P 2.93 kg 315), not tied to
the DR02.

Cyborg Robotics: R01 page ">400N·m", "48V15000mAH（SE）", "48V30000mAH（PRO）", backup "48V3500mAh", "75kg（SE），80kg
（PRO）", 62 DoF, "12核275TOPS"; China Daily (promotional) "峰值扭矩达411Nm"; W01 page "562N.m" (no joint named), "170kg",
53 DoF, 5 h; hand page "750g", "16（主动6，欠驱动10）", "腱绳驱动"; downloads: product manual id=713, brand manual 711,
brochures 709 and 708 (read by Claude, V135).

PDFs it named: BD's spec sheet (read in E14.5); Kuindersma et al. 2014 (MIT, the DRC Atlas); the H1 user manual of a
reseller (mybotshop); Cyborg's four downloads.
