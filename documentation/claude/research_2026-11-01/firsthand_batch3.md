# Batch 3 of types 3 and 4: the makers' figures read first-hand (EVIDENCE.md E15, VERIFICATION.md V134)

> Saved from Claude's scratch folder on 2026-11-01 (Matthias: "Yes, save them"), so that the work can go on on another Mac. The scratch folders it names (`pages_e15/`, `urdf_e15/`, `imgs_e15/`, `downloads_e15/`, `downloads_e16/`, `texts_e16/`) are not kept: each page, model file and PDF can be read again at the address given. Written by Claude.


Model files downloaded to scratch `urdf_e15/` and added up by script (`urdf_e15_sum.py`, the link masses; the joints and
their effort limits):

| File | Links with a mass | Sum (kg) | Joints | Effort limits | Agrees with the agent |
|---|---|---|---|---|---|
| gbionics gene01_0/model.urdf | 80 | 79.668 (hands 1.310; a link "battery" 3.54285) | 73 revolute (31 body: legs 12, torso 2, arms 14, neck 3; hands 42), 17 fixed | every one 1e+09 (a placeholder, not used) | yes |
| FFTAI gr3v2_1_1.urdf | 35 | 69.692 (no hands; its "hand_yaw / pitch / roll" links are the wrist's, 4.01) | 31 revolute: waist 3, head 2, arms 7 × 2, legs 6 × 2 | hip pitch and knee 366, hip roll and yaw and waist yaw 140.4, waist roll and pitch 108.6, shoulder pitch and roll 74.4, ankles 59.4, shoulder yaw, elbow and wrist yaw 42.9, head and wrist pitch / roll 17.4 | yes |
| Lumos nix1_joint21_nomesh.urdf | 22 | 23.320 | 21 revolute | 102 × 17, 20 × 4 (ankles) | yes |
| Lumos nix1_v1 / v2 _joint21_nomesh.urdf | 22 | 23.136 each | 21 revolute | 102 × 17, 20 × 4 | yes |
| Lumos nix2-5.urdf | 22 | 24.642 | 21 revolute | 102 × 17, 17 × 4 | yes |

Maker pages read in the browser pane (get_page_text):

- **107 Galbot G1**, https://www.galbot.com/g1/: 机身重量 "92.5 kg"; 整机高度 "1730 mm"; 电池容量 "48 V 30 Ah"; 自由度（不含底盘和末端执行器）
  "合计 21 颈部 2 · 手臂 7×2 · 腰部 3 · 腿部 2"; "NVIDIA AGX Orin 64GB"; 头部 双目相机 ×1; 躯干 RGB 相机 ×4, IMU ×1; 腕部 深度相机 ×2, 六维力传感器
  ×2; 底盘 3D 激光雷达 ×1, 超声传感器 ×8, IMU ×1; 线性四麦克风阵列 ×2; 喇叭 5 W ×2; 5.5 寸触摸屏; "4 轮全向移动底盘"; IP54; 腿部升降高度差
  650 mm. Agrees with the agent; the speakers, screen and IP54 added.
- **108 Galbot ET1**, https://www.galbot.com/et1/: 站立状态尺寸 "1250 mm"; 带电池重量 "32 kg"; 总自由度 "标准版：26", "专业版 / 旗舰版：26
  + 12（增加灵巧手）"; 双目摄像头; "RK3588 + RDK X5"; 专业版 "Orin Nano 40TOPS", 旗舰版 "NX 100TOPS". Agrees.
- **109 Galbot S1**, https://www.galbot.com/s1/: 整机重量 "320 kg"; 整机高度 "1793 mm"; 升降行程 "750 mm"; 自由度 "颈部 2 · 双臂 7×2 · 升降
  1"; 底盘 "四轮转向全向底盘", 730 × 730 mm; "NVIDIA AGX Orin 64GB"; 头部 双目相机 ×1, 3D 激光雷达 ×1; 胸部 深度相机 ×2, 六维力传感器 ×2;
  底盘 3D 激光雷达 ×2; 电池 "48 V 30 Ah × 2", 热插拔; 7 英寸触摸屏; 喇叭 5 W × 2. Agrees.
- **319 W1 Pro**, https://en.dexforce.com/w1pro.html: Weight "110kg" (W1 Pro and W1 Core); "682mm*550mm*1636mm"; Maximum DOF
  W1 Pro "34" (the page's banner: "40 DOF … omnidirectional chassis solution", "34 DOF … differential"); Neck 2, Waist 2,
  Leg 2; arm "7 DOF (Shoulder: 3; elbow: 1; wrist: 3)"; end effector standard "Dexterous Hand", "6 Active DOF and Humanoid
  5 Fingers"; "Differential (Optional: Omnidirectional)"; head "6cm Baseline Humanoid Binocular Vision"; wrist RGBD
  optional; navigation LiDAR "2 pcs"; navigation cameras "2 pcs"; **Battery Capacity "40 Ah" for the W1 Pro**; "Optional:
  LiFePO4 Battery (40 Ah)" is the **W1 Core's** column, not the Pro's (the agent gave it to the Pro); "Dual-PC Architecture
  (≥300 TOPS)"; no voltage, no chemistry for the Pro.

Maker pages fetched by curl into scratch `pages_e15/` and read as text (`tools_e15/htmltext.py`):

- **112 Gento Luna**, https://www.gentorobotics.ai/products/gento-luna/: "26 DoF (excluding dexterous hands)"; "7-DoF force-controlled
  humanoid arms (single arm rated payload 6 kg …)"; "the 6 degrees of freedom in the waist and legs"; "NVIDIA Jetson Orin AGX
  64GB, delivering up to 275 TOPS"; "1700 mm tall when fully extended … folds down to a minimum height of 790 mm"; "48 V 34.4
  Ah LiFePO battery pack, supporting 4–8 hours"; "quick battery swap"; "3D LiDAR and ultrasonic radar"; "omnidirectional
  mobile chassis". No mass. Agrees. (26 = arms 14 + waist and legs 6 + 6 more not named: head, chassis?)
- **127 HMND 01 Alpha Bipedal**, https://thehumanoid.ai/hmnd-01-alpha-bipedal/: WEIGHT "90 kg"; HEIGHT "179 cm"; DEGREES OF
  FREEDOM "29"; AVG RUN TIME "4 hr"; PAYLOAD "15 kg"; head "RGB Cameras + 2xDepth sensors", "6-mic array, speakers"; "Wrist
  RGB cameras"; "12-DOF 5-finger hand or 1-DOF parallel gripper"; "built on NVIDIA compute". The "six RGB cameras" and the
  "Nvidia Jetson Orin AGX and Intel i9" are the release's (not reread). Agrees.
- **133 HSR-ER-HR705**, https://www.hsrobotics.cn/products_xq/119.html: 自由度 "23（机械臂7×2+头部2+腰部1+腿部3+底盘3）"; 额定负载 "10kg
  （5kg×2）"; 机器人高度 "1700mm"; 机器人重量 "200kg"; 底盘外形尺寸 "745×620×343mm"; 视觉系统 "标配：深度相机×2、鱼眼相机×1；选配：腕部深度相机×2";
  末端工具 "可选配二指夹爪、吸盘、灵巧手等"; 续航时间 "6H+"; 充电 "≤2H"; "SLAM激光导航"; "全向移动". Agrees.
- **99 FlashBot Arm**, https://pudurobotics.com/products/flashbot-arm: "539*515*1440mm"; "15kg" (payload); Charging Time "4h";
  Working Duration "8h (None load)"; "VSLAM + Lidar SLAM"; "10.1 inch Touch Screen"; "Arm: 7"; "Hand: 6 Active + 5 Passive";
  "PUDU DH11 dexterous hands"; "Independent Suspended Chassis"; "RGBD cameras, LiDAR, panoramic cameras, and pressure-sensitive
  skin" (no counts). No mass. Agrees.
- **161 Knowin-X1**, https://knowinai.com/en/product.html: "≤40 cm" folded; "130 cm" extended; "7 DoF" an arm; "Total Degrees of
  Freedom 23 DoF"; "Dual-Arm Payload 6 kg"; "Wheeled chassis"; "Vision · Depth · LiDAR". No mass. Agrees.
- **118 GR-3**, https://support-old.fftai.com/en/docs/GR-X-Humanoid-Robot/GR3/GR-3_Introduction/: "Net Weight ≈71 kg"; 1642 ×
  552 × 292 mm; the joint table "Torque Upper Limit (Nm)" (hip pitch 366.0, hip roll 140.4, hip yaw 140.4, knee 366.0, ankle
  pitch and roll 59.4, …) the same as its model file's; "Max Joint Peak Torque 440N·m" (above every joint of its table:
  not reconciled, the table used); head 2, leg 6, waist 3, arm 7, hand 6 (12 optional); "702Wh + 234Wh", "Lithium-ion
  battery", "3.8kg + 1.3kg", "46.8V", hot swap; "AMD Ryzen 7 8845HS"; "Monocular camera"; IMU "6-axis"; microphone "360-degree";
  speaker 15 W; "Aluminum Alloy + Engineering Plastic + Soft Cover Material". Agrees.
- **145 Jingchu Elf**, https://www.jingchurobot.cn/product_detail/3.html (the address without www does not resolve): "荆楚精灵身高165cm，
  体重约70kg。具备16个自由度（不含手），拥有高精度智能移动底盘"; a second block of the same page "轮式机器人 身高：1.6m 体重：80kg 2轮驱动"; "1024核NVIDIA
  Ampere架构GPU，约117TOPS"; "约8小时综合续航"; "激光雷达和深度相机"; "高扭矩行星减速机模组". Agrees: 70 and 80 kg on one page.
- **178 MagicBot (Gen1)**, https://www.magiclab.top/en/human: Standing Dimensions "1740*580*280 mm"; Total Weight "Approcimately
  70kg"; "Main Structure: Aluminum Alloy，Exterior Parts: PC+ABS Plastic"; "Harmonic Reducer / Planetary Reducer"; Maximum
  Joint Torque "≥ 350 N·m"; "42 (Active Degrees of Freedom)": neck "2 (Yaw ×1 + Pitch ×1)", arm "7 (Shoulder ×3 + Elbow ×1 +
  Wrist ×3)", hand "11 (6 Active DOF, 5 Passive DOF)", waist "2 (Yaw ×1 + Roll ×1)", leg "6 (Hip ×3 + Knee ×1 + Ankle ×2)";
  "8-Core CPU + 100 TOPS AI Processor"; "3D LiDAR + Depth Cameras ×2 + Fisheye Cameras ×3"; "Omnidirectional Microphone Array,
  Speakers"; "25 Ah (1.35 kWh)" (54 V by arithmetic); "3-5 Hours". Agrees. Whether the register's "MagicBot" (54 kg, 138 cm,
  the catalogue's prototype) is the Gen1: not said by the maker.
- **181 MagicBot X1**, https://www.magiclab.top/en/x1: "180×55.4×28" cm; Total Weight "70kg" (X1 and X1 Ultra); Total Active DoF
  "31": head 2, arm 7, waist 3, leg 6; Peak Joint Torque "≥350N・m", Maximum "≥400N・m" (the text: "a peak knee torque of
  ≥350N·m"); "Aerospace-grade Lightweight Aluminum Alloy", "Titanium Alloy", "High-strength Engineering Plastics" (the text adds
  magnesium-aluminium alloy and TPU); "Dual Battery System", hot-swappable, "18Ah" (no voltage); "8-Core High-Performance CPU";
  AI "Orin NX" (X1 Ultra "Up to NVIDIA Jetson AGX Thor"); "Stereo Camera Module", "Head RGB-D Camera", "Waist RGB-D Camera",
  "LiDAR (Optional)"; air cooling. Agrees.
- **182 MagicBot Z1**, https://www.magiclab.top/en/z1: standing "1369*422*200mm"; "Weight with Battery Approximately 40kg" (Dev.
  "40kg+"); "24" joints (Dev. "24 - 50"): leg 6, head 1, waist 1, arm 5; "Maximum Knee Torque* 100N.m" (Dev. "130N.m");
  "permanent magnet synchronous motor"; "15-cell battery"; "Smart Battery (Quick Release) 10000mAh"; charger "62V 5A" (15 cells:
  55.5 V nominal by arithmetic, 555 Wh); "8-core high-performance CPU"; "3D LiDAR + Depth Camera + Binocular Fisheye Camera + Head
  Tactile Sensor"; microphone array; "5W Speaker". Agrees.
- **185 Martian**, https://unix-group.ai/martian/: "148 cm Height", "40 kg Weight", "150 N.m Motor Max Torque", "5 kg Total
  Payload", "9 Ah Battery Capacity", "48 V Rated Voltage"; "6 DoF per leg", "7 DoF per arm", "3 DoF at the waist", "2 DoF at the
  head"; "A 11-DoF industrial-grade dexterous hand"; "40T Computing Power Platform 32GB Ram"; "Depth Camera + RGB*2 + IMU";
  "Bipedal Humanoid Robot". Agrees.
- **186 Matrix-1**, https://matrixrobotics.ai/matrix-1: "180 cm", "67 kg", "10 kg per arm", "196N.m/Kg" (actuator), "2.28 KWh custom
  battery pack", "5 hours", "7.6 km/h", "8 onboard RGB cameras, with LIDAR and ultrasonic sensors … (optional)", "8 cores and
  integrated GPU", microphones and speakers, hand "22 degrees of freedom". No count of the body's joints read (the agent's
  "Actuator: 55, MPA 3.0" not found in the page's text). Legs or wheels not stated.
- **139 Isaac 1**, https://weaverobotics.com/isaac-1: "8 hours", charge "2 hours"; footprint "20.5" × 22" (W × D)"; "3' – 5'9"";
  vertical reach 80", horizontal 38"; Degrees of freedom: Neck "2", Arms "2 × 6", Hands "2 × 1", Torso "2", Base "3"; "wheeled
  base … passively stable"; "collapsible torso"; "soft fabric shells" around a "solid inner structure". No mass. Agrees.
- **150 KAI's hand (KaiHand)**, https://kinetixai.tech/en/kaihand: "37 DoF: 20 active, 1 passive, 16 compliant"; "750 g"; "185 × 90 ×
  40 mm"; "30 N". The robot it belongs to is not named. Agrees.
- **160 Kinisi KR1**, https://www.bearrobotics.ai/kinisi: "Wheeled humanoid mobile manipulator"; "up to 14.4 km/h, a full shift per
  battery"; "IP65"; Payload "To be confirmed at launch"; "Autonomous omnidirectional mobile base (To be confirmed at launch)". No
  mass. Agrees.
- **166 Laborer C1**, https://www.glroad.com/ListIntroduction/info.aspx?itemid=549 (without www it does not resolve): 身高 "137.1CM",
  重量 "38KG", 臂长 "57.9CM", 移动速度 ">2M/S", 电池容量 "10AH", 续航 "2H(行走)、4H(站立)", 全身自由度 "21", 单腿 "6", 腰部 "1", 单臂 "4(可扩展)",
  最大峰值扭矩 "150N.M", 双编码器, 减速比 "25", 算力 "Nvidia Orin NX 100T/157T", "6轴IMU", 感知模块 "交互屏 深度相机 激光雷达", 语音模块 "阵列麦克风+5W
  扬声器". Agrees (21 = legs 12 + waist 1 + arms 8).
- **167 Laborer M1**, itemid=548: 身高 "187CM", 重量 "86KG", 双臂负载 "50KG", ">1.2M/S", 电池容量 "22AH", 续航 "2H", 全身自由度 "27", 单腿 "6",
  头部 "1", 单臂 "1", 最大峰值扭矩 "430N.M". Agrees. "单臂 1" does not add up to 27; 27 = legs 12 + head 1 + 14, so arms of 7 each by
  arithmetic (the catalogue's "7-DoF arms" the same): E.
- Glroad's home page, https://www.glroad.com/: "身高180cm,体重100kg,自由度31+2,移动速度>5km/h,负重能力>40kg,最大关节扭矩380N·m" (a model not named);
  a news quote "95公斤", "全套金属仿生关节". Not used (no robot named).
- **173 Lumen H1**, https://www.hecbot.cn/product.html?type=22: "身高169cm，净重≈69kg"; 电池 "700 Wh"; 续航 "2 h"（支持换电）; 主动自由度 "40个（双臂7x2、
  双腿6x2、头部2、灵巧手6x2）"; "自研一体化关节峰值扭矩512Nm"; 底盘 "最大运行坡度8%（=5°），最大越障高度20mm"; 自主导航速度 "最大0.8m/s"; 底盘感知 "激光雷达 +
  RGBD相机"; 原地掉头宽度 "60 cm"; 2 kg. Agrees. Legs of 6 and a chassis on one page: the form needs a reading (question).
- **188 MEMO**, https://www.sunday.ai/technology (its text full of zero-width characters, stripped): Height "1.7 meters"; Weight "170
  pounds" (77.1 kg); reach 0.8 m and 2.1 m; Arms "2×7", Hands "2×4", Torso "1", Lower Body "4"; Navigation Max "1 meter/s";
  Runtime "4 hours"; Charge time "1 hour"; Materials "A blend of rigid and elastic polymers"; Hand "IP67", Lower Arm "IP66".
  Agrees (IP67 / IP66 read this time).
- **189 / 190 MenteeBot**, https://www.menteebot.com/bot/: "175cm", "70kg", "1.5m/s", "25kg", DoF "40"; "Self-made actuators fully
  integrated on-board sensors and drivers"; "Advanced, redundant, reliable, fail-safe compute". The page names **no version**
  (the agent gave it to the V3). "Mentee Robotics is now Mentee by Mobileye."
- **197 Modular, O-ID**, https://o-id.net/ (its numbers one character a text run): "172 cm" HEIGHT, "70 kg" WEIGHT, "16 kg"
  PAYLOAD, "30 DoF" AXES, "9" MODULES. The wording "Specs indicative" not found in the text (it may be in an image); the
  agent's quote not confirmed.
- **226 P0**, https://www.pink-robotics.com/: Height "1,75m", Weight "82kg", Motion System "32 DoF", Payload "8kg"; "This prototype was
  designed and made by us in Germany". Agrees.
- **228 Phantom MK1**, https://www.foundation.bot/phantom: "5'-11"" (1.8m); WEIGHT "176 lbs (80kg)"; PAYLOAD CAPACITY "88.2lbs (40kg)"
  and "40l (20kg)" (two figures); DEGREES OF FREEDOM "29º"; SPEED "1.7 m/s"; "CYCLOID ACTUATORS"; MAX PEAK TORQUE "160Nm"; BACK-DRIVING
  "<1.0-Nm"; "9 RAD/S @ 48V", "12 … 72V"; WRIST "20 Nm"; LEGS ">160"; SHOULDER "119". "Phantom is our first production humanoid
  robot" (no version). Agrees, but for the second payload.
- **215 Nova, ugo**, https://ugo.plus/ai/ugo-nova/: "(h)126〜162cm（折りたたみ時〜最大延伸時） (w) 56cm (d) 65cm"; "約 100 kg"; 頭部 "2軸（yaw 1軸 + pitch
  1軸）"; 腕部 "7軸＋ハンド1軸2指（双腕）"; 腰部 "4軸（yaw 1軸 + pitch 3軸）"; 車体部 "4軸（メカナム4輪）"; カメラ "ヘッド x1（ステレオカメラ）", "ハンド x2（RGBカメラ）";
  "NVIDIA Jetson Thor"; "約6時間（バッテリー：LiFePO4 | 50.6V | 22Ah）" (1,113 Wh by arithmetic); 充電 "約2.5時間"; "約0.4km/h ~ 3.6km/h". Agrees.
- **238 ProWhite**, https://en.pl-universe.com/Products/ProWhiteRobot: Charging Time "2 h"; Battery Capacity "40 v 100 Ah" (4,000 Wh
  by arithmetic); "AC/DC, Plug-in, Battery Swap"; Endurance "≥8 h"; "1051mm(L)*800(W)*2035mm(H)"; Weight "400 kg"; arm DoF "6"; arm
  span "910 mm"; per arm "≈ 7 kg"; operating height "0.7-1.3 m"; ">2.5 m/s"; "Four-wheel omnidirectional"; total load "12 kg";
  "Liftable torso"; "modular end effectors". Agrees.
- **239 Psi V1**, https://www.psibot.ai/en/products/product_psibot-v1/: "Standing Height ：<180cm"; "Single Arm Reach：683mm"; "Battery
  Life：>8hours"; "Sensor：RGBD*4；Fisheye Camera*3"; "Computing Platform：Thor"; "Cable / Auto return charging"; "Waist：2-DOF"; "Neck：
  2-DOF". No mass. Agrees.
- **211 NIX**, https://lumosbot.tech/products/luxiaoming: "892*445*176 mm"; "25.41 kg (total, incl. battery)"; "89 cm"; "21 DOF"
  (single arm, waist, single leg named; their numbers in images); "RGB camera"; "4-mic array / speaker / mini wireless microphone";
  "282 Wh"; "2 h"; "Quick-detach"; "67.2 V / 2.5 A"; "102 N·m"; "Max payload 3 kg"; "RK3588". Agrees, with its model files above.

Group 4, first-hand:

| File | Links with a mass | Sum (kg) | Joints | Effort limits | Agrees |
|---|---|---|---|---|---|
| roboterax/models star1/urdf/l3_with_hand_fixedpin_xml.urdf (robot "l3") | 77 | 64.001 (hand-named links 2.245) | 55 revolute (31 body, 24 hand), 23 fixed | neck 35 × 2; shoulder pitch, roll, arm yaw, elbow pitch 110; elbow yaw, wrist pitch, roll 35; waist pitch and roll 220, yaw 110; hip roll 255, hip yaw 100, hip pitch 400, knee 400, ankles 100; fingers 1.1 and 0.4 | yes |

- **240 Pudu D7**, https://www.pudurobotics.com/products/d7 (the 2026 one): Height "68.9 in（175 cm）"; Weight "308.6 lbs（140 kg）"; arm rated
  "7 kg", peak "10 kg"; maximum "20 kg"; "≥4 h"; "360° Omni Chassis", "Dual-LiDAR Omni Chassis"; DoF "*excluding end effectors 23";
  "275 TOPS (Optional Chip Upgrade)"; "NVIDIA Jetson Orin + RK 3588 dual-chip platform"; "7-DoF humanoid arms"; "180° rotating waist";
  "Dual-battery design … hot swapping"; "Front and rear LiDAR"; end effectors optional. Agrees. (The 2024 D7's 45 kg is the release's,
  not reread.)
- **241 Pudu D9**, https://www.pudurobotics.com/products/d9: "170 cm"; "65 kg"; "Total DOF 42", "Single-leg DOF 6", "Single-arm DOF 7"; DH11
  "Active DOF 6", "Passive DOF 5"; "Maximum Joint Torque 352 N·m"; "20 kg", arm "10 kg"; sensors RGB, RGBD, tactile, IMU; "275 TOPS";
  Battery "15 Ah (0.72 kWh)" (48 V by arithmetic); speaker "Stereo". Agrees.
- **245 QUANTA X2**, https://x2robot.com/en/product/quantum2: "62 （Dexterous Hand）"; "164cm"; torso "6"; arm 765 mm, "6kg", dual "12kg";
  gripper "2", dexterous hand "20"; chassis "2"; 2D LiDAR "1", ultrasonic "4", RGB-D "3", single-point TOF "2", BEV camera "3". No mass.
  Agrees.
- **249 RAISE A1**, https://www.agibot.com/products/A1: Height "175 cm"; Weight "55 kg"; "7 km/h"; DoF "49 +"; arm "5 kg"; "200 TOPS" (and
  "200Teraflops"); microphone array; Lidar; RGB-D camera; Skill-hand "Active DoF 12 Passive DoF 5"; PowerFlow "Peak Torque 350N·m"; "Reverse
  Knee". No battery. Agrees (the "1.6KG" a joint not in the text read).
- **250 RayNex G3**, https://www.nineraygroup.com/en/humanoid.html: "173 cm", "60 kg", "32 DoF (Body)"; "Full-body 44 Force Control Units";
  "Linear & Harmonic Rotary Joints"; "Frameless Torque Motor"; "Maximum joint thrust density 4500N/kg"; "AIU"; "8H Run Time"; deadlift 100 kg.
  Agrees.
- **258 REX G1**, https://www.robosci.com/rex-g1/: "22个自由度（2头颈、7×2臂、2腰部、1升降以及3底盘）"; "双臂抱持10KG"; width 540 mm, length 540–640 mm,
  "高度覆盖1100–1700mm"; "单次续航最长可达4小时", "热插拔换电"; "2070 TFLOPS 端侧算力". No mass. Agrees.
- **263 Robin**, https://www.roboligent.com/robin/: "Two 7-DOF arms on an omni-directional base, with a motorized lifting column"; "7 / 14
  kg"; "1,000 mm" reach; "6–12 hr"; "105 kg Total weight, 680 × 600 mm footprint"; "Parallel gripper, 120 mm stroke"; "Five-finger hand
  available". Agrees.
- **264 ROBO-T1**, https://robo.inc/: "two 6-DOF robot arms with grippers". No mass. Agrees.
- **273 Sherpa Mecha**, https://www.atirobotics.ai/products/humanoid/sherpa-mecha/: "Dual-arm mobile manipulator on autonomous wheeled base";
  "26 lbs (12 kg)"; "Dual arms with 19 degrees of freedom"; reach "900 mm"; "1,100 mm – 2,000 mm — extending torso"; "Carbon-fibre" arms;
  "3D LiDAR and Camera"; Battery "55 Ah × 2 — 2 hr charge". No mass. Agrees.
- **277 Spaceo M1**, https://muksrobotics.com/spaceo-m1: "1625x420x390 mm"; "Weight (With Battery) ~45 kg"; "12 dof": arm 5, base 2; "Maximum
  Torque of Arm Joint About 160 kg cm" (15.7 N·m); BLDC servo; "Aluminium body with polymer covers"; microphone array; RGB camera; "2D
  LiDAR"; "Intel RealSense Depth Camera"; "RYZEN 7, 16GB RAM, 500GB SSD"; "Orin AGX (~275 TOPS) / RTX 5070"; "25.6V, 45Ah LiFePO4 Battery"
  (1,152 Wh by arithmetic). Agrees.
- **278 Spaceo Pro**, https://muksrobotics.com/spaceo-pro: "(1625-2100)x450x450 mm"; "60 kg"; "20 (Waist and Gripper (optional))": arm 6, hand
  "1 to 16", base 2, waist 1, head (number not in the text); arm joint "66 Nm", waist "90 Nm"; BLDC servo; "Aluminium body with polymer
  covers"; RealSense; "RGB Camera*3"; "RYZEN 7"; "Jetson Orin AGX (~275 TOPS)"; "25.6V, 45Ah LiFePO4 Battery". Agrees.
- **282 StarBot Flex / 283 StarBot Nova**, https://www.starbotusa.com/: Flex "5 ft 9 in", "A foldable wheeled humanoid", "Availability and
  final specifications to be announced"; Nova "5 ft", "70 lb" (31.8 kg), "2–3 kg", "10–12 hrs", "3 hrs"; "two 7-DOF arms", "Wheeled base,
  differential drive", "Depth cameras (Intel RealSense class), RGB camera, IMU" (a "Nova reference configuration"). Agrees.
- **286 Synthia**, https://robotics.syntheva.no/products/synthia: "165 - 190 cm"; "9.8 - 12.0 kg"; "BCM2712 CPU (base model)" or "RK3588S";
  "dual cameras", "microphone"; "23 powerful and precise servos"; modular, the most basic "only Synthia's head". Agrees.
- **287 Syntro**, https://www.workfar.com/product/syntro: "5′ 8″ (1.7m)"; "25″ (0.64m)"; payload "44 lbs (20kg)"; "240 lbs (108kg)"; "Head: 2 /
  Arms: 4 (x2) / Wrist: 3 (x2) / Hands: 12 (x2) / Waist: 2 / Wheels: 3"; "Maxon Motors and Harmonic Drives"; "2D LiDAR / Camera(s) /
  Computer Vision / Microphone(s)"; "Intel Multi Core I5"; "Swappable Batteries 1.2 kWh"; "3 All-directional Omni Wheels"; "Aluminum /
  Stainless Steel / Carbon Steel / Brass / Acetal / Carbon-fiber Filament". Agrees.

Downloaded (on "download what ever is possibel") to scratch `downloads_e15/`, read by PDFKit (`tools_e12/pdftext.swift`) and,
where its digits are not text, rendered and read by Vision OCR (`tools_e12/pdfpages.swift`, `ocr.swift`):

| File | From | Pages | What it states |
|---|---|---|---|
| rnoid_specs.pdf | https://lp.robot.com/rnoid/specs.pdf ("Reision no. 003 May 14 2026") | 1 | **259 RNoid**: "1.7 m Height", "0.55 m Wheel base", "90 kg Total weight", "Dual 7-DOF Arm DOF", "0.82 m Arm length", "4 kg per arm", "Modular End effector", "4-DOF Torso", "2-DOF Neck", "2 m/s", "Battery 3 hours, Supports plug-in", "AMD Ryzen 5 7640HS Base computing", "NVIDIA Jetson AGX Orin AI module", "RGB-D camera … Head and chest", "2x RGB-D camera Wrists cameras", "360° front + rear mapping LiDAR", "Mic and speaker", "8 units Ultrasonic sensors", "smooth omnidirectional movement". Agrees |
| q5_brochure.pdf | https://a.storyblok.com/f/298593/x/5695abe67b/q5-brochure-en-robotera.pdf | 2 (digits by OCR) | **267 ROBOTERA Q5**: "582*519*1650 mm"; Weight "70 Kg"; DoF "44"; dual-arm payload "10 kg"; arm span "1380 mm"; "3D Laser Radar+Stereo Camera"; "> 4hour"; Supply Voltage "60 V"; "Neck: 2 DoF", "Waist: 1 DoF", "Arms: 7 DoF X 2", "Hands: 11 DoF X 2", "Legs: 3 DoF", "Chassis: 2 DoF"; "Drive Wheels X2", "Omni Wheels X4"; "Binocular Camera"; "3D LIDAR"; XHAND Lite "11 DoF"; chassis 582 × 519 × 225 mm. Agrees |
| Oversonic_Robee-R-2026-eng.pdf | https://oversonicrobotics.com/download/ (its media page) | 6 | **262 RoBee, Series R** (10/2026): "165 — 199 cm", "Up to 293 kg", footprint "65 * 71 cm", arm reach "95 cm"; depth cameras (head, chest, waist, base), "Laser 3D", "Laser scanner safety", thermal camera, speakers "60 W", microphone; "Omnidirectional drive"; "Batteries included 2", "Lithium ion", "Up to 8 hours", "Quick battery change"; single arm "7.5 kg", double "15 kg"; end effectors "Mechanical gripper, vacuum gripper, humanoid hand, others"; IP64. Agrees |
| Oversonic_Robee-M-2026-eng.pdf | the same | 6 | **RoBee, Series M** (10/2026, medical): "180 cm", "150 kg", "56 * 53 cm", "70 cm"; "8 mecanum Ø 100mm"; "Batteries included 1", "Lithium ion", "Up to 4 hours"; arm "5 kg", double "10 kg"; "Degrees of freedom per arm 6", "per leg 6"; "Laser 3D", depth cameras, "Humanoid hand". Agrees |
| Oversonic_Robee-F-2025-eng.pdf | the same | 4 | **RoBee, Series F** (10/2025, intralogistics): "850 kg", "200 cm", "80 * 120 cm"; "7-axis articulated arms"; "pneumatic support structure with vertical motion"; "Cameras included 8"; "Batteries included 6", "Lithium ion + Graphene supercap"; rear axle transport 500 kg; arm 10 kg, double 20 kg. Agrees. Which series the register's "RoBee" (180 kg) is: not said |

Group 5, first-hand (UBTECH's figures are in images: the page's large images found in the browser pane, downloaded to
scratch `imgs_e15/`, read by Vision OCR):

- **305 Tora DoubleOne**, https://paxini.com/images/en/tora-double-parameter.png ("*Data from Paxini AI Lab"), by OCR: P "671 mm × 548 mm ×
  1276~1638 mm (adjustable height)", X "767 mm × 486 mm × 1330~1692 mm"; armspan "2028 mm"; single arm "844 mm"; "Total Joint Motors
  (excluding dexterous hands & drive wheels)" P "20", X "22"; P "4WD&4WS omnidirectional chassis", X "4-wheel drive active
  obstacle-surmounting chassis"; "Nvidia Jetson AGX Orin Dev. Kit 64G"; "RGB Camera: 1 (head). RGBD Camera: 2 (head, abdomen). 3D LIDAR: 1
  (head). Ultrasonic Sensors: 6 (chassis). IMU: 2 (head, chassis)."; "Front and rear 8-Microphone Array"; "10 W Speaker"; "47 Ah (1214.01
  Wh), supports quick release" (25.8 V by arithmetic); "Approx. 8 hours"; arm "3 kg", dual "10 kg"; "Peak Joint Torque (full body) 207
  Nm"; obstacles "20 cm". **No mass.** Agrees. (The agent's "最大 52 个关节自由度" not in this image.)
- **321 Walker C**, https://www.ubtrobot.com/en/humanoid/products/WalkerC (text): Height "163cm"; Battery "Lithium Battery 48V 15Ah" (720
  Wh); Weight "43kg"; "Charging: 1.5h, Walking: 2h, Standing: 4h"; Degrees of Freedom "20"; Camera "RGBD*2, All-Scenario Binocular
  Structured Light3D Camera*2"; "electric-driven". Agrees.
- **322 Walker C1**, https://www.ubtrobot.com/en/humanoid/products/walker-c1 (the address WalkerC1 gives "can't be found"), images
  pages3-item1-en.png: "53 of DOF", "Height 164cm", "Weight 55kg"; pages4-bg-en.jpg: "NVIDIA® Jetson Thor™ 2070 TFLOPS (FP4)" (the agent
  did not give it); pages10-info-en.png: "Fish-eye Camera*2", "Binocular Camera*1", "LCD Display*1", "Monocular Camera*1", "Speaker*2",
  "Dexterous Hands (Optional)*2"; "Automotive-grade Battery" (no capacity). Agrees.
- **324 Walker S1**, https://www.ubtrobot.com/en/humanoid/products/walker-s1, images: "Height 172cm", "Weight 76kg", "Load 15kg",
  "Self-developed Integrated Joints … Peak Torques 250N.m", "Dexterous Hands 6 Tactile Sensor Array", "Panoramic Fisheye Cameras", "3D
  Stereoscopic Vision"; "RGBD*1" (head), "Stereo RGB Camera*2", "Speaker*2", "RGBD*1" (torso), "IMU", "Six-axis Force Sensor*2" twice.
  Agrees. No count of joints by the maker (the agent's 41 is aiwiki's).
- **325 Walker S2**, https://www.ubtrobot.com/en/humanoid/products/walker-s2, images: "Height 176cm", "Weight 70kg", "52 of DOF", "Gen-4
  Industrial Dexterous Hands 11 of DOF", "Single-hand Grasp: 7.5kg", "4 Array Microphones", "2 Speakers", "Rigid-flex Heterogeneous
  Composite", "Aerospace-grade Aluminum Alloy", "3D Printed Primary Frame", "3D Knitted High-elastic Fiber Material"; "Fish-eye Camera*2",
  "RGB Camera*2", "LED Screen*1", "Microphone*1", "Speaker*2", "RGBD Camera*1" (front and back), "Six-axis Force Sensor*2", "Dexterous
  Hands*2"; text: "dual-battery … hot-swappable". Agrees. (Its 2.3 kWh and 48 V are batterydesign.net's, second-hand.)
- **333 XiaQi**, https://www.digit.com.cn/ProductsDetail/93.html, image 6386850727352790969116244.png (or its neighbour) by OCR: "169cm",
  "≤ 69kg", "60cm", "700woh" (700 Wh), "≥2h", "1kg", "≥1.2m/s". Agrees (the "40+主动自由度" not read by OCR).
- **346 Zerith H1**, https://www.zerith.com/product/ZerithH1/: "轮臂人形机器人"; arm span "1788 mm"; reach up to "2156 mm"; "7 轴" arms; "1.5" m/s;
  "23总 自由度"; "4 h 连续作业"; "1 kg 单臂负载". No mass. Agrees.
- **354 PR-OMNI**, https://www.perceptyne.com/product/omni: Height "5'2""; Weight "120 kg"; Body Material "Aluminium"; "Dual arms, 7 DOF
  each"; Head "2 DOF"; "4 Wheel holonomic drive"; "Indoor SLAM with dual LiDARs"; "Force-torque sensing at every joint"; "3 RGBD cameras (2
  wrists + 1 head)"; Vertical Gantry Range "800 mm"; Runtime "6 hours"; "3 kWh (2 × 1.5 kWh, swappable)"; "Nvidia Jetson Orin + Intel NUC
  5th Gen"; "Payload - 5kg". Agrees.
- **317 Voxel**, https://tuesdaylabs.com/robot: "7-DOF Arms with Fully Actuated Wrists", "1-DOF Grippers", "Z-Shaped Legs with
  Impact-Aware Feet", "Stereo RGB + Wide-Field Vision". No mass. Agrees.
- **293 Tau Humanoid**, https://www.tau-robotics.com/: no figures in its text. Agrees.

Groups 1 and 3, the makers' releases and pages, first-hand:

- **97 Figure 02**, Figure's release of 6 Aug 2024 as carried by https://www.vktr.com/the-wire/figure-unveils-figure-02-…: "2.25 KWh custom
  battery pack in the robot torso"; "6 onboard RGB cameras"; hands "16 degrees of freedom"; "onboard mics and speakers"; "3x the
  computation and AI inference". No mass. Agrees.
- **206 / 207 NEO Beta and NEO Gamma**, https://www.1x.tech/discover/introducing-neo-gamma: "1X's Tendon Drive", "four microphones (front,
  back, left, and right)", a "three-speaker system", the suit "3D printed from durable and soft nylon"; no mass. https://www.1x.tech/discover/
  neos-hands: "25 Degree of Freedom (DOF), tendon-driven hands for the NEO humanoid platform", "Peak torques reach 3.5 Nm at the thumb CMC and
  2.6 Nm at …", "gear ratios of approximately 5:1 to 15:1", "The motors live in the forearm", IP68 (no version named). **The home NEO**,
  https://www.1x.tech/neo (a later version, not Beta or Gamma): Height "5'6"", Weight "66 lbs" (29.9 kg), Hands "22x2", Arms "7x2", Neck "3",
  Spine "2", Legs "6x2", Battery "842 Wh", "4h", "1X NEO Cortex (Nvidia Jetson Thor)", "4 beamforming microphones", "3 stage speaker",
  "Dual 8.85MP 90Hz Stereo Fisheye", "custom 3D lattice polymer", "machine washable nylon", IP44 body. Agrees.
- **208 Neo1**, NeodraDynamics' release on PR Newswire APAC: "a 4-meter hydraulic-electric hybrid humanoid", "500 kg dual-arm payload", "micro
  digital hydraulic cylinder that weighs 1.1 kg", "a 5-finger dexterous hand and a 7-DOF humanoid arm". No mass. Agrees.
- **209 NEXO**, Galaxea AI's release (PR Newswire, https://kyodonewsprwire.jp/release/202608244591): "Nexo, its new‑generation wheeled dual‑arm
  robot with 30 degrees of freedom, 20 kg dual‑arm payload and 8‑hour runtime". No mass. Agrees.
- **205 NE01**, https://www.genisomai.com/en/product-robot/ne01: no figures in its text. Agrees.
- **130 / 131 HONOR**, https://www.honor.com/global/events/honor-robot/: "HONOR Robotics D1", "HONOR Robotics A1"; no figures. Agrees.
- **110 Persona Gen 1**, https://persona.ai/humanoid/: "Targeting 2 work shifts per day", "engineered textile skin", a swappable battery; no
  figures. Agrees.
- **129 Hobbs W1**, Noetix's page in the browser pane (https://www.noetixrobotics.com/en/mobile/detail/W1; the pane is sent to the mobile
  page, its specification table not shown even at 1440 px): "Wheeled Full-Body Form", "54 Active DoF", head "32 active DoF and 8 passive DoF",
  "The dual arms feature 22 active DoF", "LiDAR, ultrasonic sensors, and depth cameras", "biomimetic platinum silicone skin". The mass 75 kg,
  the 32 Ah and the computers are aiwiki's (citing this page), **not read first-hand**.

Types 5 and 6, first-hand:

| File | Links with a mass | Sum (kg) | Joints | Effort limits | Agrees |
|---|---|---|---|---|---|
| engineai_robotics_description t800/urdf/serial_t800.urdf ("170-T800-AL-newsystem-20251127") | 35 | 84.988 | 25 revolute, 9 fixed | hip pitch 415, hip roll 370, hip yaw 222, knee 415, ankles 160; torso yaw 222; shoulder 160 × 3, elbow pitch 160, elbow yaw 52; head 52 × 2 | yes |
| t800pro/t800pro_43dof/urdf/serial_t800pro.urdf | 51 | 85.227 | 43 revolute, 7 fixed | the same, plus wrists 5 × 4 and fingers 1.1 × 14 | yes |

- **288 T800**, https://en.engineai.com.cn/product-t800: "173cm"; Weight "Varies by Configuratoin: 75kg~85kg"; Basic and Open Source 25 (neck 2,
  leg 6, waist 1, arm 5, hand "/"); "Max Torque【1】 450 N·m"; "Ultra-High-Speed Internal Rotor Permanent Magnet Synchronous Motor"; "Aviation
  Aluminum + Titanium"; "Intel Wide Field-of-view Binocular Camera (Head)"; Basic 3D LiDAR "/"; "8 CORE High-performance CPU"; Basic "Orin NX
  16G"; "Intelligent Quick Disassembly Supported"; "Lithuim"; "3～5h"; "29 DOF throughout the body (excluding dexterous hands)"; "7 degrees of
  freedom (DOF) per hand, a payload capacity of 5 kg"; "modular solid-state lithium battery". Agrees. Voltage and capacity not stated.
- **191 MH3**, https://www.mirsee.com/: "MH3", "10 Hour Runtime", "31 degrees of freedom", "Wireless Charging", "Best in class Hands", "Highest
  Payload Mobile Base", "Power off brakes" (MH2: "8 Hour Runtime", "24 degrees of freedom", "Omni-directional Mobile Base"). No mass. Agrees.
- **24 Alex**, https://robots.ihmc.us/alex-humanoid: "179 cm", "85 kg", "1.5+ m/s", "2+ hrs", "15+ kg", "High-power custom actuators". IHMC
  news https://www.ihmc.us/news20251119/: "Nadia, which weighed about 100 kilograms. The estimate is that Alex will weigh 85 kilograms w[ith a
  battery]". Agrees (the 29 joints not found in the page's text read).
- **202 Nadia**: the IHMC news above, "weighed about 100 kilograms". Agrees. (arXiv 2411.03532 not reread.)
- **301 TITAN**, https://www.roboforce.ai/technology: "2.10m", "1.50m-2.10m", "600mm Lifting Range", Payload "40kg" "Dual Arm", "1100mm" arm
  reach, "8h Per Battery". **No mass.** Agrees.
