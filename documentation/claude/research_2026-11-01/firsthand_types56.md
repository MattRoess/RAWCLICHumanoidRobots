# Types 5 and 6: the figures read first-hand (EVIDENCE.md E16, VERIFICATION.md V135)

> Saved from Claude's scratch folder on 2026-11-01 (Matthias: "Yes, save them"), so that the work can go on on another Mac. The scratch folders it names (`pages_e15/`, `urdf_e15/`, `imgs_e15/`, `downloads_e15/`, `downloads_e16/`, `texts_e16/`) are not kept: each page, model file and PDF can be read again at the address given. Written by Claude.


The register's types 5 (Heavy-Duty / High-Performance / Hazardous-Environment) and 6 (Defense / Public Safety): 16
robots. Taken apart already with another type: 43 Atlas (type 3's file, both templates), 71 CYBORG RO1 SE and PRO, 72
CYBORG WO1, 81 DR02 and Pro (types 3), 352 Unitree H1 (type 2, its model file). In E15 (batch 3): 152 Kaleido 9, 195 Moby,
208 Neo1 (E15 question 5), 228 Phantom MK1. Not yet entered: 24 Alex, 44 Atlas (old), 191 MH3, 202 Nadia, 288 T800, 301
TITAN, 351 Fuxi.

## PDFs downloaded to `downloads_e16/`, read by PDFKit

| File | From | What it states |
|---|---|---|
| nadia_arxiv_2411.03532.pdf (15 pages) | https://arxiv.org/pdf/2411.03532 (IHMC, Calvert et al., 2024) | "6 degree of freedom (DoF) legs, a 3 DoF spine, 7 DoF arms, and 1 DoF grippers"; "The ankle, knee, hip pitch and roll, and spine pitch and roll joints are actuated by Moog Integrated Smart Actuators (ISAs)[27]"; "The hip and spine yaw joints are actuated by electric motors with planetary drives"; "The arms are powered by cycloidal drive actuators, described in [1]"; "SAKE EZ Grippers[34] are used for the hands"; "a carbon fiber exoskeleton for the thighs, shins, and torso"; "our robot is tethered to a hydraulic pump"; "a ZED 2i[35] facing forward and downward at 43°"; "pelvis-mounted IMU"; an ankle torque sensor. Its ref. [27]: Moog's ISA datasheet at moog.com (now 404) |
| nadia_arms_arxiv_2409.04639.pdf | https://arxiv.org/pdf/2409.04639 (IHMC, Bertrand et al., 2024: Nadia's teleoperation) | Fig. 4, "Performance specifications of cycloidal actuators in the robot's arms", peak / continuous N·m: Shoulder J1 158 / 41, Shoulder J2 158 / 41, Shoulder J3 79 / 23, Elbow 79 / 23, Wrist J1, J2, J3 19 / 7; speeds at 48 V and 72 V; "support a payload of up to 10kg and deliver a torque output up to 158 Nm" |
| alex_arxiv_2609.01518.pdf (20 pages) | https://arxiv.org/pdf/2609.01518 (IHMC, Calvert et al., 2026) | Alex "a custom, fully electric humanoid robot with 29 degrees of freedom"; "PSYONIC Ability Hands [3], which are anthropomorphic 5-finger hands with 6 degrees of freedom each"; "two stereo color cameras in the head", "a ZED X Mini"; neck roll-pitch-yaw and spine actions; no torque, no mass, no battery |
| frontiers_isa_2018.pdf (15 pages) | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2018.00051/pdf (Barasuol et al., IIT with Moog, 2018) | Table 2: ISA v2 / ISA v5 / smart manifold: cylinder bore 16 / 21.5 mm, rod 12 / 12 mm, stroke 80 / 100 mm / 100 deg, "Dry weight 920 g 1,600 g 2,100 g", "Stall load 4,000 N 7,500 N 170 Nm", "Operating pressure 20.7 MPa"; the body "additively manufactured (AM) in a titanium alloy"; one HyQ actuator unit of separate parts "1.3 kg", the ISA v2 "only 0.92 kg" |
| (not obtained) Moog_IntegratedSmartActuator.pdf, Moog-Microhydraulics-Integrated-Smart-Actuator-Datsheet-en.pdf | moog.com | both addresses return Moog's 404 page |

## Makers' pages, read as text

- **IHMC, https://robots.ihmc.us/humanoid-design**: Alex "high power, custom actuators, as well as completely onboard computation,
  perception, and power"; "custom, highly backdriveable, powerful quasi-direct drive actuators. Leveraging careful designed cycloidal
  transmissions"; "These designs are an iteration of the actuators made for Nadia's arms"; "Across its 29 joints". Nadia "powered by a
  combination of electric and hydraulic actuators. It used Moog's Integrated Smart Actuators (ISAs)", "custom electric actuators in the
  pelvis, and commercial off-the-shelf actuators for the arms", "composite materials", "Across its 29 joints".
- **PSYONIC, https://www.psyonic.io/ability-hand**: "The Ability Hand weighs in at 490 grams".
- **SAKE Robotics, https://sakerobotics.com/**: "EZGripper™ … Gripper Weight 365g + 35g (mount)", "Servo Robotis Dynamixel MX-64AR",
  "Operating Voltage 12V", payload 5 kg.
- (already in `firsthand.md`) T800's page and two model files; MH3 (Mirsee's home page); Alex's page "179 cm", "85 kg", "2+ hrs";
  IHMC news "Nadia, which weighed about 100 kilograms"; TITAN's page (no mass).
- **44 Atlas (old)**:
  - Boston Dynamics' blog, https://bostondynamics.com/blog/build-it-break-it-fix-it/: "its 190-pound frame" (86.2 kg); "Each of the
    hoses is rated for a pressure of 3,000 pounds per square inch (PSI)", burst "closer to 10,000 PSI"; "Atlas's batteries and valves".
  - IEEE Spectrum, 23 Feb 2016, https://spectrum.ieee.org/next-generation-of-boston-dynamics-atlas-robot, quoting Boston Dynamics' video
    text: "electrically powered and hydraulically actuated", "LIDAR and stereo sensors in its head", "about 5' 9" tall … and weighs 180
    lbs" (IEEE: 1.75 m, 82 kg; the DRC Atlas "6'2" (1.9 m) and 345 lbs (156 kg)").
  - IEEE Robots Guide, https://robotsguide.com/robots/atlas2016 ("Atlas HD, or hydraulic", 2016 to 2024): "Height 150 cm", "Weight 80 kg",
    "Lidar and stereo vision", "Hydraulic actuation with custom servo-valves powered by compact hydraulic power system", "Degrees of Freedom
    (DoF) 28", "Mixture of titanium and aluminum 3D-printed parts. Actuators and hydraulic lines embedded in leg structures", "Three on-board
    computers inside torso", "Custom battery".
- **351 Fuxi**:
  - Global Times' reporter at NORINCO's innovation institute's show, via https://www.163.com/dy/article/KDLOLOCA0514R9OJ.html:
    "伏羲机器人整机高180厘米，重85公斤" (the Fuxi as a whole 180 cm, 85 kg), "巡逻值守、安防安保等特种场景"; the institute's 梁健: "伏羲的6自由度灵巧手"
    (Fuxi's six-DoF dexterous hand); the show had "伏羲机器人、伏羲Lite机器人以及安保机器人".
  - Global Times, https://www.globaltimes.cn/page/202608/1368491.shtml (NORINCO's teleoperation system): "for full-size humanoid robots
    weighing around 90 kilograms" (a class, not the Fuxi's own mass).
- **The DRC Atlas (2015), for its kind of power**: IEEE Spectrum, https://spectrum.ieee.org/atlas-drc-robot-is-75-percent-new-completely-unplugged,
  quoting DARPA: "Atlas will now carry an onboard 3.7-kilowatt-hour lithium-ion battery pack, with the potential for one hour of 'mixed
  mission' operation"; "a new variable-pressure pump"; "the upgraded robot is 6-foot-2 (1.88 meters) and weighs 345 pounds (156.5 kg)";
  "Three onboard perception computers"; "Re-sized actuators in the hip, knee, and back". A different robot (the 2013 to 2015 one, 156.5
  kg): its 3.7 kWh over 156.5 kg is 23.6 Wh per kg, against types 3 and 4's legged template's 14.67.
- **191 MH3**:
  - aiwiki, https://aiwiki.ai/wiki/mirsee_robotics_mh3/raw (its table cites Mirsee's site and Aparobot): "Weight (with battery) 125 kg (276
    lb)", "Aluminum 6061", "IP54", "Wheeled (Mecanum omnidirectional)", "Mobile base payload capacity >300 kg", "31", "DOF per hand 6",
    "Arm payload 30 kg per arm", "Battery life 10 hours", "Wireless charging; hot-swappable modular batteries", "NVIDIA Jetson",
    "4000 x 3000 (12 MP)", "Hadron (stereo vision)", "BLDC (brushless DC)", "Harmonic and planetary", "M-Drive (patented hydrostatic)",
    "Power-off brakes".
  - Interesting Engineering, https://interestingengineering.com/ai-robotics/canada-firms-humanoid-robot-hazardous: "Built on a wheeled
    mobile platform"; "can lift to 66 pounds (30 kilograms) with each arm, operate for up to 10 hours on a single charge, and features 31
    degrees of freedom"; "Hadron Vision System, an embedded stereo vision platform powered by NVIDIA Jetson processors"; its Advanced Mobile
    Platform "uses Mecanum wheels", "supports payloads exceeding 661 pounds (300 kilograms)"; "modular hot-swappable battery systems".
- **301 TITAN**, RoboForce's releases on PR Newswire (19 May 2025, and its GTC one) and The Robot Report: "Titan currently comes in wheeled
  and tracked base variations"; "1mm precision", "a 40kg payload, 1100mm of arm reachability, and an 8-hour production runtime"; "a 40 kg
  dual-arm payload". **No mass** in any of them (nor on its page, V134): listed only, as the register has it ("Not specified").

## Agent 2's findings, read again by me (pages fetched into `pages_e15/`)

- **288 T800, EngineAI's developer documents** (each "更新于 2026年10月16日"):
  - https://engineai.com.cn/open/docs/t800/05/08 (battery): 电池类型 "三元锂电池"; 标称容量 "20Ah"; 标称电压 "61.2V"; 电池能量 "1.22kWh";
    工作电压范围 "50V ~ 71.2V"; 最大放电持续电流 "90A"; 续航时间 ">=3H 一般行走"; 充电时间 "2.5H"; 快拆换电 "支持"; 充电方式 "电池单独充电（机身不支持）";
    系统总质量 "≈7.2KG"; PACK 外壳材质 "铝合金".
  - https://engineai.com.cn/open/docs/t800/05/02 (specification): 型号 "T800开发版 | T800PRO版"; 带电重量 "约84.5kg | 约85.3kg"; 总自由度 "25 |
    29+14(灵巧手)"; 单臂自由度 "5 | 7"; 关节类型 "行星 | 行星+直线力控"; 感知传感器 "自研双目+激光雷达"; 基础算力 "NEZHA"; 颈部 "2", 腰部 "1", 单腿 "6";
    腿关节最大峰值扭矩 "450 N*m"; 高算力模组 "NVIDIA Jetson AGX Orin 64GB"; 智能电池类型 "三元锂电池（1.22KWh）"; 续航时间 "2h（标配）"; 充电功率 "71.4V*10A";
    "USB A 3.0 (内部连接NeZha N97)". (The product page's "modular solid-state lithium battery" and 3–5 h disagree; the developer
    documents are the newer and the detailed ones.)
  - https://engineai.com.cn/open/docs/t800/05/05 (joint motors): Q25H / Q50H / Q200H / Q300H / Q300H-L: 最大力矩 "50 | 160 | 222 | 370 |
    415" N·m; 质量 "0.5 | 0.95 | 1.65 | 2.1 | 2.6" kg; 减速比 "25 | 25 | 14.45 | 24 | 24"; 额定电压 "48 | 63 | 63 | 63 | 63"; 关节类型 "全行星"; the
    text: Q25H "峰值扭矩52 N·m", "L05直线关节和F17手指关节". Matched to the joints by the model files' efforts (415, 370, 222, 160, 52), the
    pairing the documents' own figures.
  - https://engineai.com.cn/open/docs/t800/05/03 (computers): "Nezha" 4 cores, 8GB, 64GB; "NVIDIA Jetson AGX Orin 64GB", 12 cores, 64GB,
    "256G SSD".
  - https://engineai.com.cn/open/docs/t800/05/04 (sensors): 视觉感知 RGB 头部 "1（双目）"; 激光雷达 头部 "1"; IMU 躯干中心 "1" (YIS320, "7.7g"); 扭矩传感器
    主要关节 (no count); 麦克风阵列 "环麦 ×4"; 高保真扬声器 "2个"; PRO "单手 5 个触觉传感器"; "Odin2相机" in the head.
  - https://engineai.com.cn/open/docs/t800/05/06 (hand, PRO only): 重量 "单手 740g"; "灵巧手自由度7个" (thumb 3, index 2, middle 2); F17 finger
    joint "30g", "最大力矩 1Nm"; "工作电压 24V".
- **195 Moby**, Noble Machines' own blog (Under Control Robotics, 18 Mar 2025,
  https://undercontrolrobotics.substack.com/p/real-world-world-building-ucr-develops): "Moby's 72 Kg body moves with an average power
  consumption of 200W", "five to six-hour shifts", "a 60-pound (27 kg) payload", "A single NVIDIA Jetson computer powers the entire onboard
  software stack". NVIDIA's case study, https://www.nvidia.com/en-us/case-studies/noble-machines/: "NVIDIA Jetson Thor processes sensor data",
  "co-develops humanoid actuators with Schaeffler". **The maker's 72 kg against E15's 45 (the catalogue's): E15's row to be corrected.**
- **152 Kaleido 9**: Kawasaki's blog, https://kawasakirobotics.com/in/blog/20260316_kaleido9/: "increasing movement speed while maintaining
  torque", "LiDAR … self-localization", the Kaleido Station "using wheels", "planned to function as a charging station". Kawasaki's Japanese
  blog, https://kawasakirobotics.com/jp/blog/202511_kaleido/ (on the 2019 Kaleido, "身長178cm、体重85kg"): "骨格部品に、アルミより軽量なマグネシウム合金を採用"
  (the skeleton's parts of a magnesium alloy, lighter than aluminium), the exterior "3Dプリンターによる樹脂製", "バッテリー搭載". PC Watch, 15 Mar 2022, on
  the Kaleido 7: "身長179cm、体重83kg、自由度は34", "3本指のハンド".
- **228 Phantom MK1**: The Business Standard (UNB, after the BBC), https://www.tbsnews.net/node/1457841: "Phantom MK-1 … lacks a battery"; MK-2
  "about six hours on a single charge"; "Cameras provide a 360-degree view". Pulse 2.0 on Foundation and AMD,
  https://pulse2.com/foundation-robotics-and-amd-partner-to-power-phantom-humanoid-robots-for-industrial-and-defense-applications/: "AMD
  Kria AI system-on-modules powered by AMD Ryzen AI Embedded X100" for the production robots, "custom robotic hands will use AMD FPGAs to
  coordinate 23 degrees of freedom", "IP67". **No battery in the MK-1 against E15's template battery: E15's row to be corrected.**
- **208 Neo1**, NeodraDynamics' release of October 2026 (reposted, https://www.thailand-business-news.com/?p=334399): "4-Meter & 1.2-Ton";
  "41 full-body active degrees of freedom. Except for two forearm rotational joints adopting electric drive, all 39 core joints use
  self-developed miniature digital hydraulic linear actuators. Weighing only 1kg, a single actuator generates ton-level continuous thrust";
  its September release "1.1 kg". No power unit, battery or tether in either.

## Agent 1's findings, read again by me

| File | Links with a mass | Sum (kg) | Joints | Effort limits | Agrees |
|---|---|---|---|---|---|
| DeepRoboticsLab/deep_robotics_model DR02/urdf/pro/DR02-pro.urdf ("automatically created by SolidWorks to URDF Exporter") | 34 | 78.085 (the page "约78kg") | 31 revolute, 8 fixed | 363 × 7 (hip y and x, knee, waist y), 137 × 14 (hip z, ankle y, waist z and x, shoulders, elbows), 50 × 10 (ankle x, wrists, neck) | yes |
| DR02/urdf/standard/DR02-std.urdf | 22 | 67.575 (the page "约68kg") | 21 revolute, 2 fixed | 363 × 6, 137 × 13, 50 × 2 | yes |

- **71 / 72 Cyborg's product manual 2026** (`downloads_e16/cyborg_713.pdf`, 7 pages, from https://www.cyb-org.cn/index.php?c=download&id=713;
  its brochure id=709 the same 7 pages; id=711 and 708 the 2-page brand manuals): R01 "体重≈ 80 Kg", "75kg (SE) , 80kg (PRO)",
  "1800*578*327mm", "62" (腿 "6*2", 腰 "2", 手臂 "7*2", 灵巧手 "16*2"), "最大关节扭矩 400N.m", "高密度大扭矩关节电机模组", "自研大推力直线模组 10000N",
  "8 核 200TOPS", "主电池 48V30000mAh + 备用电源 48V3500mAh", "48V 15000 mAH (SE) , 48V 30000 mAH (PRO)"; W01 "710 * 585 * 1600mm", "170kg",
  "53" (底盘 "3", 腰 "2", 手臂 "7", 灵巧手 "16"), "最大关节扭矩 562 N.m" (no joint named), "单臂 6.5kg", "8 核 200TOPS", 单目相机, RGBD, IMU,
  激光雷达, 红外, 六维力, 线性4麦, 扬声器, 超声波, "5h", chassis "704 * 470 * 397mm", no battery capacity; H02 hand "750g", "关节数量 16", "电机数量
  6", "腱绳驱动", "12V". (Its website's "12核275TOPS" and ">400N·m" are older wording.)
- **43 Atlas, electric**: Boston Dynamics' release, https://bostondynamics.com/news/boston-dynamics-expands-collaboration-with-nvidia/:
  "Atlas robot is leading development of humanoids using the NVIDIA Jetson Thor computing platform"; its blog
  https://bostondynamics.com/blog/robot-hands-for-modern-ai-and-real-work/: "13 degrees of freedom (DOF), directly actuated", "The four DOF
  opposable thumb", "all with a single actuator type", "dense pressure tactile sensors", "GR2 had 7 degrees of freedom. GR3 now has 13";
  The Financial News (Korea, LS Securities), https://en.fnnews.com/news/202609020840218266: "Each Atlas unit contains 31 body actuators";
  Battery-Tech Network, https://battery-tech.net/battery-markets-news/lg-energy-solutions-batteries-power-atlas-humanoid-robot/ ("Industry
  sources"): "LG Energy Solution has supplied 46-series ternary cells for Boston Dynamics' Atlas". No torque, no battery capacity.
- **44 Atlas (old)**: Fluid Power World, 23 Mar 2018, https://www.fluidpowerworld.com/?p=131942, quoting Boston Dynamics' Aaron Saunders: "This
  newer Atlas model is about 1.5 meters tall and weighs 80 kg", "completely power autonomous (running between 30-60 minutes …) and has 28
  degrees of freedom"; the HPU "approaching a Kilowatt per kg of density", "It sits in the center of the robot", "integrated into a printed
  part … around the reservoir"; "Atlas' manifold has 18 valves, which service the upper body"; the legs "integrated the structure, the
  manifold and the fluid routing and actuator cylinders all into one structure". No masses of its parts.
