# Evidence

The check of the project's inputs against sources outside it, with references. Written by Claude, newest first.
How each source is judged follows Matthias's rules for sources (`GitHub/CLAUDE.md`, §8):
- **same kind:** it describes the same kind of material as the robot uses;
- **representative:** it fits the use in a robot;
- **questioned:** a standard, a manufacturer's datasheet, a measurement, a review, a patent or a vendor page;
  first-hand or second-hand;
- **read myself:** the source was opened and read, not judged from a search summary.

## E11. Robot types 3 and 4: research, batch 1 (2026-10-30). Nothing entered

Matthias, 2026-10-30: "Yes, together", then "Yes, start sources" (the sources of types 3 and 4's 178 robots with a mass
still to do, in batches, a source table first, each robot of both types researched once). Batch 1, as type 2's batches:
the first 27 in the register's order (numbers 1 to 58). Read on 2026-10-30: the makers' pages through six web-fetch
reads, and myself in the built-in browser where those got no text (PNDbotics' site and wiki, NEUBILITY, AeiROBOT);
PNDbotics' two model files through GitHub, their masses summed and their limits listed in the page (V109). No PDF and
no download opened (they wait for his word, E11.2 point 4). Catalogue figures (humanoid.guide) are second-hand and
only context. Nothing is entered.

### E11.1 Robot by robot: what the makers state

The register's height, mass and form in brackets; **bold** where the maker's differs or where the robot stands on wheels.

| # | Robot (the register) | What the maker states | Source | Kind |
|---|---|---|---|---|
| 1 | 1X NEO, 1X Technologies (170 cm, 30 kg) | "5'6\"" (167.6 cm, arith.), "66 lbs" (29.9 kg, arith.); DoF hands "22x2", arms "7x2", neck "3", spine "2", legs "6x2" (75, arith.); "1X Tendon Drive actuation", "Low inertia tendon drives"; battery "842 Wh", "4h"; "1X NEO Cortex (Nvidia Jetson Thor)"; "Dual 8.85MP 90Hz Stereo Fisheye", "4 beamforming microphones", speakers in pelvis and chest; "custom 3D lattice polymer", suit and shoes "machine washable nylon"; lift "154 lbs". Torques, battery voltage, frame: not stated | 1x.tech/neo | maker, spec |
| 3 | 4NE1, NEURA Robotics (~180 cm, ~80 kg; legs or wheels) | its spec box, under the heading "Meet 4NE1 Gen 4": "Height (cm) 180", "Weight (kg) 80", "Payload (kg) 10-20", "speed (km/h) 5"; "versions on wheels for industrial floors or with a 7th axis"; a datasheet PDF not opened. Which generation the figures are: the Gen 4's (the heading) | neura-robotics.com/products/4ne1/ | maker, spec (Gen 4's page) |
| 4 | 4NE1 Gen 3.5, NEURA Robotics (180 cm, 80 kg) | no figures: "integrated high-dexterity hands, a high-capacity battery"; "expected to be available end of 2026"; 98,000 €; a datasheet PDF not opened | neura-robotics.com/product/4ne1-reservation/ | maker, no figures |
| 5 | 4NE1 Gen 4, NEURA Robotics (180 cm, **65 kg**; legs or wheels) | "Height (cm) 180", **"Weight (kg) 80"**, "Payload (kg) 10-20"; "A slimmer body with a sleek textile skin, 20% lighter than the generation before"; "Advanced hands"; compute, battery, joints: not stated | as 3 | maker, spec |
| 6 | A2, AgiBot (170 cm, 60 kg) | **no A2 on AgiBot's sites** (English and Chinese); the nearest, A2 Ultra / A2 Lite: "169cm", "≈69kg" / "≈64kg", DoF "40" / "23" (legs 6 × 2, arms 7 / 5 × 2, neck 2 / 1), "Peak Knee Torque 270N·m", "Battery Capacity 14.4Ah", charger "54.6V 8A", "16-core high-performance CPU", "NVIDIA Jetson Orin 64G" (Ultra), 3D LiDAR, RGB-D, RGB, fisheye cameras (Ultra) | agibot.com/products/A2_Ultra | maker, not listed |
| 7 | A2 Max, AgiBot (178 cm, 85 kg) | **not listed**: "AGIBOT A2-Max" only as an option of the inquiry form | as 6 | maker, not listed |
| 8 | A3 Ultra, AgiBot (174 cm, 60 kg) | "174 cm", "60 kg"; arms "7 DOF per arm", legs "6 DOF per leg", waist "3 DOF", hands "Up to 20 DOF"; "700 TOPS"; "Dual battery bays", "8 h", "10-second battery swap"; frame "Magnesium alloy + carbon-fiber nylon"; "LiDAR + 360° surround view", RGB-D in chest, terrain and knee, binocular RGB, "3 wide-angle fisheye cameras", shoulder touch sensors, microphones; its table on agibot.com an image, not read. Torques, battery voltage and energy: not stated | store.agibot.com/products/a3u | maker, spec |
| 14 | AGIBOT A3, AgiBot (173 cm, 55 kg) | "173 cm", "55 kg"; "Dual battery packs · 1152 Wh · Full-tab cells", "10 h", "10-second battery swap"; "150 A maximum current, 12 kW power"; "magnesium alloy, titanium alloy, and TPU flexible materials"; shoulder touch sensing, microphones. DoF, torques, compute: not stated (the catalogue's 31 DoF and 320 N·m not on the page) | agibot.com/products/A3 | maker, spec |
| 17 | AgiBot X2, AgiBot (130 cm, 36 kg) | **two versions**, X2 / X2 Ultra: "Approx.1.31 m", "Approx.35kg" / "Approx.39kg"; DoF "25" / "30" (neck 0 / 1, arms 5 / 7 × 2, waist 3, legs 6 × 2); "Peak Joint Torque 120N·m"; "Approx.500Wh", charger "54.6V 10A"; "RK3588 ×2", Ultra also "Orin NX (157 TOPS)"; 3D LiDAR and RGB-D on the Ultra only; hands only for the Ultra, sold apart | agibot.com/products/X2 | maker, spec |
| 9 | Abi, Andromeda Robotics (120 cm, 50 kg; wheels) | no hardware figures: "Fluent in 90 languages"; legs or wheels not stated (the catalogue: "a wheeled base") | andromedarobotics.ai/product | maker, no figures |
| 10 | Adam Lite, PNDbotics (**160 cm**, 60 kg) | its wiki: **"1.67m"**, "60kg", "25 degrees of freedom" (legs 6 × 2, arms 5 × 2, waist 3); "Knee ~ 340N·m, Hip ~ 340N·m, Ankle ~ 46N·m, Arm ~ 60N·m"; each joint's actuator named (below); "1172W·h capacity, 46.2V max voltage"; "NUC12WSKi7 for motion control" (Intel Core i7-1260P); "Spherical Hand". Its model `adam_lite.urdf`: 58.48 kg over 27 links, 25 joints, limits hips 230, 160, 105, knee 230, ankle 40, 12, waist 110 × 3, arms 65 × 3, 30, 6.4 N·m. The actuators (their pages, "Maximum torque", "Weight/kg"): knee PND-130-7F-P 340 N·m, 4 kg; hip pitch PND-130A-7F-7-P 340, 4; hip roll PND-80-20-50-S 180, 1.5; hip yaw PND-60-17-30-S 48, 1; waist PND-60-17-50-S 89, 1; ankle PND-50-6F5S-30-P 46, 0.7; shoulder pitch and roll PND-50-14A-50-S (its page PND-50-14-S: 60, mass "/"); shoulder yaw and elbow PND-30-14A-50-S 17.5, 0.4; wrist yaw PND-20-14A-50-S 6.2, 0.3 | wiki.pndbotics.com/en/robot/humanoid_robot/, /en/actuator/…; github.com/pndbotics/pnd_models | maker, spec; maker's model |
| 11 | Adam SP, PNDbotics (167 cm, 62 kg) | as 10: "1.67m", "62kg", "41 degrees of freedom" (arms "Shoulder x3 + Elbow x1 + Forearm x1 + Wrist x2 + Dexterous Fingers x6 = 13" each); the same torques, actuators and battery; wrist pitch and roll PND-20-08-50-S 6.4 N·m, 0.2 kg; "NVIDIA Jetson Orin NX 16GB"; "Intel Realsense D455"; "Dexterous Hand" (six joints). Its model `adam_sp.urdf`: 60.25 kg over 55 links, 29 joints, limits as 10's and wrists 6.4 N·m | as 10 | maker, spec; maker's model |
| 12 | AEON, Hexagon (165 cm, 60 kg; legs or wheels) | "Height: 165cm", "Weight: 60kg", "Degrees of freedom: 34"; "Battery: Auto-swap", "5 hours of autonomous work on a single charge"; "Payload: 15 kg short-term, 8 kg constant carry"; "go up the stairs"; its article: "NVIDIA Jetson Thor", "cameras and depth sensors", IMUs, "time-of-flight sensors"; partners maxon, Microsoft, NVIDIA (who supplies what: not stated). Battery voltage and energy, torques, materials, hands: not stated | robotics.hexagon.com/product/; …/aeon-perception-capabilities-nvidia-holoscan/ | maker, spec |
| 18 | Agile One, Agile Robots (174 cm, 69 kg) | "modular fingers, 21 joints, and integrated force and tactile sensors"; "a walking speed of 2 meters per second"; "intelligent cameras, LiDARs"; a proximity sensor; height, mass, battery, torques: not stated. Its Agile Hand page (not said to be Agile ONE's hand): "21 joints and 15 or 16 degrees of freedom, the 1.5 kg Agile Hand" | agile-robots.com/en/products/humanoid-robots/agile-one/; …/agile-hand/ | maker, partial |
| 22 | AIDOL, AIDOL Lab (186 cm, 95 kg) | walking version: "67" degrees of freedom, "186 см", "95 кг", "6 км/ч", payload "10 кг", "до 6 часов" (up to 6 hours); "вычислительному модулю на основе графического процессора" (a GPU-based computing module, not named). Torques, battery, materials: not stated | aidoltech.ru/walking | maker, spec |
| 26 | Alice M1, AeiROBOT (130–180 cm, 97 kg; **wheels**) | "130 - 180cm / 97kg"; "DoF 31 Waist(3), Arm(7*2), Head(2), Hand(6*2)"; "AFE-R360 \| NVIDIA AGX Orin"; "Stereo Camera", "IMU \| 3D Lidar \| Laser Sensor"; a "Mobile platform", its waist "from 1.3m to 1.8m"; a button "URDF DOWNLOAD" (not pressed: a download). Battery, torques, base: not stated | eng.arobot4all.com/2069803258 (in the browser; refused to the fetch, 403) | maker, spec |
| 28 | ALPHA, TeknTrash (200 cm, 90 kg) | **not reachable**: its site refused the connection, to the fetch and to the browser | tekntrash.com | not reachable |
| 29 | AlphaBot 2, AI² Robotics (180 cm, 135 kg; **wheels**) | "a wheeled dual-arm humanoid robot", "1800mm", "135kg (standard configuration)"; "22 degrees of freedom (excluding end effectors)": its legs "a three-joint folding lifting structure with waist yaw", arms "7 degrees of freedom" each, neck "2", chassis "two-wheel differential drive"; peak torques: neck 3.3, waist yaw 66, waist pitch 207, knee 436, ankle 436 N·m (the arms' not stated; its arm "Six-Axis Force Range 200N/7Nm", "Supply Voltage DC 20~30V"; its SDK's example "arm_type": "realman"); "Battery 48V 30Ah", "4~6h"; "NVIDIA Orin AGX 64G"; "Realsense D435" in head, chest and back, "Realsense D405" at the arms' ends, a chassis RGB-D camera, "2D LiDAR", "linear MIC*4"; chassis "Payload ≤100kg", 505 × 650 mm | docs.ai2robotics.com/en/alphabot2/hardware/architecture | maker, spec |
| 31 | Anigon, Anigon Humanoid Robotics (189 cm, 120 kg; **wheels**) | "Height 189 cm", "Full Body 28 DoF", "Each Arm 7 DoF"; "Dual Hot-Swap Batteries"; "Mobile Base: Adaptive Lifting"; "Integrated Torque Sensors", "Electromagnetic" holding brakes; "Wheeled Humanoid Robot, … Dexterous Hands, … Cameras, Torque Sensors, Tactile Sensors, Edge Compute Controller". Mass, battery, compute: not stated; a "Technical Overview" (.txt) not opened. The catalogue's maker, "Aimbo Robotics", is not named on the maker's site | anigon.ch/robot-platform/, anigon.ch | maker, partial |
| 32 | Apollo, Apptronik (173 cm, 72 kg) | **its page answered 404**; the home page: "both bipedal and wheeled mobility options" | apptronik.com | maker, no page |
| 33 | Apollo 2, Apptronik (173 cm, 75 kg; legs or wheels) | no figures: "A bipedal configuration … while a wheeled base offers stability"; "Apptronik's patented actuator technology", "90%+ energy efficiency"; "Swappable batteries"; a chest display | apptronik.com/apollo/apollo-2 | maker, no figures |
| 43 | Atlas, Boston Dynamics (190 cm, 90 kg; types 5 and 3) | "Height 1.9 m", "Weight 90 kg", "DoF 56"; "Battery Life 4 hours", "self-swappable batteries"; "Weight Capacity (Instant) 50 kg", "(Sustained) 30 kg"; "Tactile and 360° camera view"; "IP67"; "all electric"; its spec sheet (PDF) not opened. Torques, battery energy, compute, materials: not stated | bostondynamics.com/atlas | maker, spec |
| 45 | Atom, DOBOT (153 cm, 62 kg) | "28 upper-body degrees of freedom (DoF)", "binocular RGB vision"; its ATOM Max: "41-DoF", "6-DoF hands", "Intel RealSense D455", "1500 TOPS", "high-precision URDF models"; height, mass, battery: not stated. Its model `atom_p3.urdf` (DOBOT's repository): 61.81 kg (E7.1), legs' limits 207.76, 241.42, 104.16, 213.8 (knee), 89.896, 89.896 N·m, torso 182.28, arms 93, 70, 70, 70, 34, 34, 34, head 12. The same files E7.5 took for type 2's Atom Max | dobot-robots.com/products/humanoid-robots/atom.html; github.com/Dobot-Arm/dobot_atom_urdf | maker, partial; maker's model |
| 46 | ATOM, Vbot (160 cm, 50 kg) | **not listed**: Vbot's site shows a robot dog only | vbot.cn | maker, not listed |
| 51 | Billi, NEUBILITY (149.7 cm, 110 kg; **wheels**) | no figures: "Hybrid humanoid combining mobility and manipulation" (in the browser) | neubility.ai/en | maker, no figures |
| 56 | Borg 01, Borg Robotics (173 cm, 62 kg; legs or wheels) | no figures: "IN DEVELOPMENT" | borgrobotic.com | maker, no figures |
| 58 | CALVIN-40, Wandercraft (170 cm, 80 kg) | no figures: "High-torque motors, high-strength structure"; "3D sensor and vision"; "First series delivery expected in H1 2027" | en.wandercraft.eu/calvin-40 | maker, no figures |

### E11.2 Batch 1 together, and the questions for Matthias

| What the makers give | Robots |
|---|---|
| Joints and torques (the maker's table or model file), mass, battery | Adam Lite, Adam SP (the wiki's actuators with their masses, and the models), AlphaBot 2 (torques of its legs, waist and neck), Atom (DOBOT's model) |
| Mass and joints, a battery or not, no torques per joint | NEO, A3 Ultra, AGIBOT A3, X2 (one peak torque), AEON, AIDOL, Alice M1, Atlas, 4NE1 / 4NE1 Gen 4 (mass only) |
| A few words, or nothing | 4NE1 Gen 3.5, A2, A2 Max, Abi, Agile One, ALPHA, Anigon (no mass), Apollo, Apollo 2, ATOM (Vbot), Billi, Borg 01, CALVIN-40 |
| On wheels, by their makers | Alice M1, AlphaBot 2, Anigon, Billi ("hybrid"); Abi by the catalogue |

**Questions, each with my recommendation** (as decided for type 2, E8.2 and E9.2):

| # | Question | Recommendation |
|---|---|---|
| 1 | The mass where the maker's differs from the register's (4NE1 Gen 4: 80 against 65 kg) | the maker's, as E8.2 point 3 |
| 2 | The robots whose makers give no mass (13 above) | the register's (the catalogue's) mass ± 1 kg, labelled the catalogue's, as E8.2 point 5 and E9.2 point 5 |
| 3 | The X2 in two versions (X2, X2 Ultra) | each as often, as the AICO 2 and the RB-Y1 (E9.2) |
| 4 | Downloads, his word first (sizes unknown until fetched): NEURA's two 4NE1 datasheets (PDF), Boston Dynamics' Atlas spec sheet (PDF), AgiBot's manuals of the A3, A3 Ultra and X2, AeiROBOT's ALICE M1 URDF, Anigon's technical overview (text), the Agile Hand flyer (PDF) | yes: they may hold the batteries and joints the pages lack |

**Decided** (Matthias, 2026-10-30: "Yes, all four"): 1 the maker's mass where it differs (4NE1 Gen 4 80 kg); 2 the
register's (the catalogue's) mass ± 1 kg, labelled the catalogue's, for the 13 whose makers give none; 3 the X2 and
the X2 Ultra each as often; 4 the downloads, read in E11.3.

### E11.3 The downloads (on "Yes, all four", point 4), read myself

Downloaded on 2026-10-30 into Claude's scratch folder, each file in a folder of its own (sizes as fetched); read with
the file reader. Nothing entered.

| File (source, size) | What it states |
|---|---|
| NEURA, `NEURA_Robotics_4NE1_Datasheet_Web.pdf` (neurarobotics.px.media, 472 kB, "V7 / 05.06.2026") | **titled "4NE1 Gen 3"**: "Weight 80 kg", "Height 180 cm", "Hands (DoF) 12", "Arms Payload 20 kg" ("Leg-supported configurations can carry up to 100 kg"), "Speed 5 km/h", "Operating Time (h) 24/7", "55 Degrees of Freedom", "Touch-Sensitive Sensor Skin", a Qualcomm logo (compute not named further) |
| NEURA, `4NE1Gen3.5Datasheet.pdf` (2.1 MB, "V6 / 02.01.2026") | "4NE1 Gen 3.5": **"Weight 80 kg"**, "Height 180 cm", "Own Hands (DoF) 12", "Payload 10–100 kg", "Speed 5 km/h", "NVIDIA Thor T5000", "Exchangeable Forearms", "Advanced Intelligent Battery Management", "Sensor Skin". Battery energy, joints: not stated |
| Boston Dynamics, `atlas-spec-sheet.pdf` (433 kB, "Rev: 10/15/2026") | "Height 1.9 m", "Weight 90 kg", "Degrees of Freedom 56"; "Tactile fingers and palm", "360° camera view"; "Battery Life 4 hrs", "with Heavy Lifting 2 hrs", "Autonomous Battery Swap Time 3 min (Charge Time 1.5 hrs)", "Charge Power Requirements 110 V"; "Weight Capacity: Instant 50 kg, Sustained 30 kg, One-Handed 20 kg"; "IP67". Battery energy, joints, materials: not stated |
| Agile Robots, `AR-AgileHand-Productflyer-SCREEN-en.pdf` (357 kB, "10008-REV.2-250530") | the Agile Hand: "Weight 1.5kg", "Joints 21", "Degrees of Freedom 16", "an aluminum open skeleton structure with injection molded plastic shells", "Joint torque and position sensors are integrated in every actuated joint". Agile ONE's page gives its hands "21 joints", the flyer does not name Agile ONE |
| Anigon, `anigon-technical-overview.txt` (7 kB) | "ANIGON FA-L Series … A wheeled humanoid platform": "28 DoF", "Force-controlled dual arms with dexterous hands", "Mobile base", "Integrated RGB-D cameras and tactile sensors", "Dual hot-swap batteries". Mass: not stated |
| AgiBot, the A3 Ultra's user manual (agibot.com/filepage/319.html, an online page, no file) | "Height 1.74 m", "Weight 60 KG", "Active Degrees of Freedom 51–71" (neck 2, arms 7, waist 3, legs 6, hands "10 (optional, up to 20 DOF)"), "Knee Joint Peak Torque 320 N·m", "Battery Capacity 1152 W·h", "Total 8 h", "RK3588 * 2", "NVIDIA Thor"; 3D LiDAR, RGB-D cameras, GPS RTK, UWB |
| AgiBot, the A3 series' user manual (/filepage/290.html; the link of E11.2, /filepage/336, empty) | "Height 1.73 m", "Weight 55 KG", "Active Degrees of Freedom 31" (neck 2, arms 7, waist 3, legs 6), "Knee Joint Peak Torque 320 N·m", "Single Arm Payload 5 kg", "Battery Capacity 1152 W·h", "10 hour", "RK3588 * 2"; no LiDAR, no RGB-D (A3) |
| AgiBot, the X2's user manuals (Feishu wiki) | **not read**: the page loads its contents list only |
| AeiROBOT, the ALICE M1 URDF ("URDF DOWNLOAD") | **not obtained**: the link answers "Invalid access" outside a signed-in session of the maker's site (an account would be needed: not done) |

### E11.4 More on the weights, from the wider internet (on "Try to find more information on the weight")

Matthias, 2026-10-30: "Try to find more information on the weight. See if there is more out in the internet". For the
robots whose makers gave no mass (E11.2), and the 4NE1's two figures. Searched (twelve web searches), then the pages
that name a weight read myself through two web-fetch reads (V111). A search engine's summary is not a source: a figure
counts only where a page read states it.

| # | Robot | Weight found, and where | Kind |
|---|---|---|---|
| 4 | 4NE1 Gen 3.5 | **80 kg**, its datasheet (E11.3) | maker, datasheet |
| 3 | 4NE1 (Gen 3) | **80 kg**, its datasheet (E11.3); Notebookcheck (2025-06-25, on the third generation): "weighing around 110 pounds", not attributed | maker, datasheet; press, against it |
| 5 | 4NE1 Gen 4 | its page's box "Weight (kg) 80", and its text "20% lighter than the generation before"; with Gen 3 and 3.5 at 80 kg, 20 % lighter is 64 kg (arith.), the register's 65 kg. **The maker contradicts itself** (E11.5) | maker, conflicting |
| 6 | A2 | **"Weight 69 kg"**, "Height 169 cm", "Battery 700 wh", "Runtime 2 h", on AgiBot's own A2 page (agibot.com/products/A2; the first read missed it) | maker, spec |
| 7 | A2 Max | none: no AgiBot page states one ("A2-Max" only in its inquiry form, its A2Max URLs serving the A2 Ultra); the search engine's "175 cm, 85 kg" was found on no page read | none |
| 32 | Apollo | Engadget (2023-08-23, its launch): "The 5-foot-8, 160-lb Apollo can lift up to 55 lbs" (72.6 kg, arith.), not attributed in the sentence | press, at launch |
| 33 | Apollo 2 | none (databases repeat the Apollo's) | none |
| 18 | Agile One | heise (2025-11-21, its launch): "Der humanoide Roboter Agile One ist 174 cm groß, wiegt 69 kg und ist in der Lage, Gewichte bis zu 20 kg zu tragen" (174 cm, 69 kg, 20 kg payload), not attributed in the sentence; Origin of Bots the same, not attributed | press, at launch |
| 56 | Borg 01 | Origin of Bots (2026-02-14): "At 173 x 50 x 40 cm and 62 kg", "in-house actuators delivering 270 Nm", "2 m/s top speed wheeled"; editorial, not attributed | second-hand |
| 46 | ATOM (Vbot) | none; Xinhua (2026-08-22, its launch at WRC): "160cm 身高、180cm 臂展和 95cm 腿长" (height, arm span, leg length), "31 个本体自由度" (31 body DoF); a co-founder: its sensors, computer and battery as its robot dog's, "最大的区别主要在关节电机" (the main difference the joint motors) | press, at launch |
| 51 | Billi | none; hellot.net (2026-10-01), "사측에 따르면" (according to the company): payload under 15 kg directly, up to 60 kg in its cargo unit, 4–6 h of work | press, the company's words |
| 28 | ALPHA | none; The Next Web (2026-05-05): "built by RealMan Robotics in China and adapted … by … TeknTrash", not attributed | press |
| 9, 31, 58 | Abi, Anigon, CALVIN-40 | none beyond the catalogue's and databases repeating it | none |

### E11.5 What E11.3 and E11.4 change in E11.2's decisions, and one question

- **Two robots now have a maker's mass:** the A2, 69 kg (its page), and the 4NE1 Gen 3.5, 80 kg (its datasheet). By
  decision 1 (the maker's mass), the A2 69 kg against the register's 60, the Gen 3.5 80 kg as the register's.
- **Eleven robots still have none:** A2 Max, Abi, Agile One, ALPHA, Anigon, Apollo, Apollo 2, ATOM (Vbot), Billi,
  Borg 01, CALVIN-40: decision 2 (the catalogue's ± 1 kg). For three of them the press at their launch gives the same
  weight as the catalogue (Apollo 160 lb = 72.6 kg against 72; Agile One 69 kg; Borg 01 62 kg), not attributed to the
  maker: context, not a source of its own.
- **The 4NE1 Gen 4 (decision 1, 80 kg) is in question:** its page's box says 80 kg, but its text says "20% lighter than
  the generation before", and the datasheets give Gen 3 and Gen 3.5 80 kg each, so the text means 64 kg (arith.). The
  box looks like the earlier generations' figure carried over; the 20 % is the one statement about the Gen 4 itself.

| # | Question | Recommendation |
|---|---|---|
| 5 | The 4NE1 Gen 4's mass: its box's 80 kg (decision 1) or its text's 20 % lighter than 80 kg | 64 kg ± 1 kg from its text ("20% lighter", arith., label S, E), the box's 80 kg reported beside it |

**Decided** (Matthias, 2026-10-30: "Yes, 64 kg"): the 4NE1 Gen 4 63 / 64 / 65 kg, label S, E (its "20% lighter than
the generation before" and its datasheets' 80 kg of Gen 3 and Gen 3.5), its page's box of 80 kg reported beside it; in
place of decision 1's 80 kg for it. The A2 69 kg and the Gen 3.5 80 kg by decision 1; the eleven others by decision 2.

### E11.6 Proposal: batch 1 of types 3 and 4, robot by robot (2026-10-30). Nothing entered

Matthias, 2026-10-30: "Propose the numbers". The method is type 2's (E6.8, E7.5, E8.3, and E9.6 for the robots on
wheels) with the decisions of E11.2 and E11.5; where types 3 and 4 need a choice type 2 did not make, it is **bold**
and a question below. Numbers at the modes are Claude's arithmetic (`types34/batch1_modes.py`, V112); the run draws
every one from its min / mode / max.

| # | What | Proposal |
|---|---|---|
| 1 | **Types 3 and 4's own templates** (question 1) | **on legs: the joint modules 22.4 / 44.7 / 67.1 % of the robot's mass**, the median of the seven robots of types 3 or 4 with every joint (H2 44.7 %, Kuavo 5 34.1, Luna 41.5, MagicBot Gen1 46.6, from type 2's file; Adam Lite 53.0, Adam SP 52.6, Atom 41.2, batch 1), split by kind as they are on average: hips 34.2, knees 16.1, ankles 11.3, waist 8.1, arms 28.2, head 2.2 %. **On wheels: 6.95 / 13.9 / 20.85 %**, the median of the three of types 3 or 4 with every joint (AI Worker 14.3, RB-Y1 A 13.9, Vega 13.2 %; the Reachy 2 is of type 2 only), split as E9.6's. **The battery 7.3 / 14.67 / 22.0 Wh per kg of robot on legs, 5.4 / 10.84 / 16.3 on wheels**: the medians of the robots of types 3 or 4 that state an energy (16 on legs, 14 on wheels). One template for both types: a robot of both has one block |
| 2 | **Joint modules by the makers' figures** | **Adam Lite, Adam SP: each joint its actuator's stated mass** (the wiki: knee and hip pitch 4 kg, hip roll 1.5, hip yaw and waist 1, ankle 0.7, shoulder yaw and elbow 0.4, wrist yaw 0.3, wrist pitch and roll 0.2 kg; ± 5 %, S); **the shoulders' PND-50-14A, whose page gives no mass, E6.8's fit at its 60 N·m, 0.70 kg (E)**. **Atom: E6.8's fit at its model's limits** (as type 2's Atom Max block, E7.5). **AlphaBot 2: E6.8's fit at its stated peaks** (neck 3.3, waist yaw 66, waist pitch 207, knee 436, ankle 436 N·m: 0.14 to 2.15 kg), **its folding legs' knee and ankle as joints, its arms (not stated) the wheeled template's shoulders and elbows (question 3)**. X2's "Peak Joint Torque 120N·m" and the A3's knee 320 N·m: a check, not used |
| 3 | **The template** | every other robot: 1's on legs or on wheels by its form (question 2) |
| 4 | **Hands and grippers** | **as Fourier's six-joint hand per joint (E7.5 point 4), small joints**: 4NE1 Gen 3 and 3.5 two of six ("Hands (DoF) 12"), Gen 4 as Gen 3.5; A2 two of six (its A2 Ultra's "6-DOF Dexterous Hand"); A3 Ultra two of ten (0.74 kg each); NEO two of 22 ("22x2", 1.62 kg each); Adam SP, Alice M1 ("Hand(6*2)"), Anigon, Atlas ("Tactile fingers and palm") two of six. **Agile One: two Agile Hands, 1.5 kg each (E: its flyer's "Weight 1.5kg", 21 joints as Agile ONE's hands; the flyer does not name Agile ONE)**. AlphaBot 2: two grippers as the RH-P12-RN, 0.5 kg (E). None where the maker names none (A3, X2, Adam Lite's "Spherical Hand", AEON, AIDOL, Apollo, Apollo 2, Atom, ATOM, Billi, Borg 01, CALVIN-40, Abi, ALPHA, A2 Max) |
| 5 | **The robot's mass** | decided (E11.2, E11.5): the maker's the mode ± 1 kg, its model's the bound; the catalogue's ± 1 kg for the eleven without |
| 6 | **Battery** | stated: NEO 842 Wh; A2 700; A3 and A3 Ultra 1,152; X2 and X2 Ultra 500; **Adam Lite and SP 1,172 Wh at 39.6 V (E: its "46.2V max voltage" is 11 cells at 4.2 V, 3.6 V each nominal), 29.6 Ah (arith.)**; AlphaBot 2 48 V × 30 Ah (1,440 Wh). Every other robot 1's energy per kg. In the base for a robot on wheels (E9.6) |
| 7 | **Boards** | E7.5 point 7 and E9.6 point 9: a named module its size (E). NEO, 4NE1 Gen 3.5 ("Thor T5000"), AEON and A3 Ultra a Jetson Thor (as the H2 Plus's) and a carrier; A3 Ultra, A3 and X2 two RK3588 boards (as the X1's computer board, E), the X2 Ultra also an Orin NX; Adam Lite and SP an Intel i7 (NUC12WSKi7), the SP also an Orin NX; Alice M1, AlphaBot 2 an AGX Orin and a carrier; **AIDOL's "GPU-based computing module" as an AGX Orin (E)**; the others one computer board (E). A power board each |
| 8 | **Sensors** | each by its kind, as the makers name them (E11.1, E11.3): NEO two fisheye cameras, four microphones, speakers; A3 Ultra a LiDAR, three RGB-D, a binocular, three fisheye cameras, microphones; A3 a binocular camera; X2 Ultra a LiDAR and an RGB-D; Adam SP a RealSense D455; AEON cameras and depth sensors; Agile One cameras and LiDARs; Alice M1 a stereo camera, a LiDAR, an IMU; AlphaBot 2 three D435, two D405, an RGB-D, a 2D LiDAR, a microphone array; the others one IMU (E). Force, torque, touch and tactile sensors left out (E9.6 point 14) |
| 9 | **Cables** | E7.5 point 9: 8 m per metre of height, half to 1.5 times; the Alice M1 at the middle of its 1.3 to 1.8 m (E) |
| 10 | **Shell, screws, frame** | E7.5 points 10, 11: the shell 11.5 % of the mass, the screws 0.5 kg, the frame the remainder, aluminium (E); **A3 and A3 Ultra a frame of magnesium alloy (S: "magnesium alloy, titanium alloy, and TPU", "Magnesium alloy + carbon-fiber nylon"), its titanium and TPU not drawn (no share stated; question 4)** |
| 11 | **On wheels** (E9.6 points 4 to 7) | two driven wheels and two casters unless more is known (AlphaBot 2 "two-wheel differential"); each hub motor by the robot's mass per driven wheel: Abi 1.4 kg, Alice M1, AlphaBot 2, Anigon, Billi 3.75 kg (E); **Anigon a lift column** ("Adaptive Lifting Base"), a share of its mass (E9.6 point 7); the Alice M1's height change its waist's ("dual parallel-link waist"), no column |
| 12 | **Versions** | the X2 and the X2 Ultra each as often (decided) |
| 13 | **Not in** | force, torque, touch and tactile sensors; NEO's lattice polymer and nylon suit beyond the shell; the A3's titanium and TPU; every option; the catalogue's figures beside the makers' |

**Robot by robot** (S stated, E estimated; joints at the modes, the template on legs 44.7 %):

| # Robot | Mass (kg) | Form | Joints | Hands | Battery | Boards | Cables (m) |
|---|---|---|---|---|---|---|---|
| 1 NEO | 28.9 / 29.9 / 30.9 | legs | template (13.4 kg) | 2 × 22 joints | 842 Wh (S) | Jetson Thor, carrier | 6.7 / 13.4 / 20.1 |
| 3 4NE1 (Gen 3) | 79 / 80 / 81 | legs | template (35.8 kg) | 2 × 6 | 1,174 Wh (E) | one computer (E) | 7.2 / 14.4 / 21.6 |
| 4 4NE1 Gen 3.5 | 79 / 80 / 81 | legs | template | 2 × 6 | 1,174 Wh (E) | Jetson Thor, carrier | 7.2 / 14.4 / 21.6 |
| 5 4NE1 Gen 4 | 63 / 64 / 65 | legs | template (28.6 kg) | 2 × 6 | 939 Wh (E) | one computer (E) | 7.2 / 14.4 / 21.6 |
| 6 A2 | 68 / 69 / 70 | legs | template (30.8 kg) | 2 × 6 | 700 Wh (S) | one computer (E) | 6.8 / 13.5 / 20.3 |
| 7 A2 Max | 84 / 85 / 86 | legs | template (38.0 kg) | — | 1,247 Wh (E) | one computer (E) | 7.1 / 14.2 / 21.4 |
| 8 A3 Ultra | 59 / 60 / 61 | legs | template (26.8 kg) | 2 × 10 | 1,152 Wh (S) | 2 RK3588, Thor, carrier | 7.0 / 13.9 / 20.9 |
| 14 AGIBOT A3 | 54 / 55 / 56 | legs | template (24.6 kg) | — | 1,152 Wh (S) | 2 RK3588 | 6.9 / 13.8 / 20.8 |
| 17 X2 | 34 / 35 / 36 | legs | template (15.6 kg) | — | 500 Wh (S) | 2 RK3588 | 5.2 / 10.5 / 15.7 |
| 17 X2 Ultra | 38 / 39 / 40 | legs | template (17.4 kg) | — | 500 Wh (S) | 2 RK3588, Orin NX | 5.2 / 10.5 / 15.7 |
| 9 Abi | 49 / 50 / 51 | wheels | wheeled template | — | 542 Wh (E) | one computer (E) | 4.8 / 9.6 / 14.4 |
| 10 Adam Lite | 58.48 / 60 / 61 | legs | its actuators (31.8 kg) | — | 1,172 Wh (S) | Intel i7 | 6.7 / 13.4 / 20.0 |
| 11 Adam SP | 60.25 / 62 / 63 | legs | its actuators (32.6 kg) | 2 × 6 | 1,172 Wh (S) | Intel i7, Orin NX | 6.7 / 13.4 / 20.0 |
| 12 AEON | 59 / 60 / 61 | legs | template (26.8 kg) | — | 880 Wh (E) | Jetson Thor, carrier | 6.6 / 13.2 / 19.8 |
| 18 Agile One | 68 / 69 / 70 | legs | template (30.8 kg) | 2 Agile Hands | 1,012 Wh (E) | one computer (E) | 7.0 / 13.9 / 20.9 |
| 22 AIDOL | 94 / 95 / 96 | legs | template (42.5 kg) | — | 1,394 Wh (E) | AGX Orin-sized (E) | 7.4 / 14.9 / 22.3 |
| 26 Alice M1 | 96 / 97 / 98 | wheels | wheeled template | 2 × 6 | 1,051 Wh (E) | AGX Orin, carrier | 6.2 / 12.4 / 18.6 |
| 28 ALPHA | 89 / 90 / 91 | legs (question 2) | template (40.2 kg) | — | 1,320 Wh (E) | one computer (E) | 8.0 / 16.0 / 24.0 |
| 29 AlphaBot 2 | 134 / 135 / 136 | wheels | stated + wheeled arms | 2 grippers | 1,440 Wh (S) | AGX Orin, carrier | 7.2 / 14.4 / 21.6 |
| 31 Anigon | 119 / 120 / 121 | wheels | wheeled template; lift column | 2 × 6 | 1,301 Wh (E) | one computer (E) | 7.6 / 15.1 / 22.7 |
| 32 Apollo | 71 / 72 / 73 | legs | template (32.2 kg) | — | 1,056 Wh (E) | one computer (E) | 6.9 / 13.8 / 20.8 |
| 33 Apollo 2 | 74 / 75 / 76 | legs (question 2) | template (33.5 kg) | — | 1,100 Wh (E) | one computer (E) | 6.9 / 13.8 / 20.8 |
| 43 Atlas | 89 / 90 / 91 | legs | template (40.2 kg) | 2 × 6 | 1,320 Wh (E) | one computer (E) | 7.6 / 15.2 / 22.8 |
| 45 Atom (DOBOT) | 60.81 / 61.81 / 62.81 | legs | its model's (25.5 kg) | — | 907 Wh (E) | one computer (E) | 6.1 / 12.2 / 18.4 |
| 46 ATOM (Vbot) | 49 / 50 / 51 | legs | template (22.4 kg) | — | 734 Wh (E) | one computer (E) | 6.4 / 12.8 / 19.2 |
| 51 Billi | 109 / 110 / 111 | wheels | wheeled template | — | 1,192 Wh (E) | one computer (E) | 6.0 / 12.0 / 18.0 |
| 56 Borg 01 | 61 / 62 / 63 | legs (question 2) | template (27.7 kg) | — | 910 Wh (E) | one computer (E) | 6.9 / 13.8 / 20.8 |
| 58 CALVIN-40 | 79 / 80 / 81 | legs | template (35.8 kg) | — | 1,174 Wh (E) | one computer (E) | 6.8 / 13.6 / 20.4 |

At the modes no frame falls below zero; the least is the NEO's, about 3 kg of its 29.9 kg (its two 22-joint hands 3.2 kg,
its pack 5.1 kg at 164 Wh/kg): in some draws it may fall below zero, reported, not cut.

**Questions, each with my recommendation:**

| # | Question | Recommendation |
|---|---|---|
| 1 | Types 3 and 4's own templates (point 1), or type 2's (E7.4: 40.4 %, 14.67 Wh/kg; E9.6: 15.6 %, 10.28 Wh/kg) | their own: the same kind of robot (rule 1 of the sources), seven on legs and three on wheels |
| 2 | The form of the five the register gives "legs or wheels" (4NE1 Gen 3 and Gen 4, AEON, Apollo 2, Borg 01) and of ALPHA ("not stated") | on legs: their makers' figures and pictures are of the robot on legs (AEON "go up the stairs", Apollo 2 "A bipedal configuration" first); ALPHA none, "stands at the line like a human worker" |
| 3 | AlphaBot 2's arms, which its maker does not give | the wheeled template's shoulders and elbows (as the JingChu's stated knees beside its template, E7.5 point 2) |
| 4 | The A3's titanium and TPU, named without a share | not drawn (reported); the frame magnesium alloy |

**Agreed** (Matthias, 2026-10-30: "Yes, agree E11.6"): points 1 to 13 and the four questions as recommended: types 3
and 4's own templates (on legs 22.4 / 44.7 / 67.1 %, on wheels 6.95 / 13.9 / 20.85 %, 14.67 and 10.84 Wh/kg); the
five "legs or wheels" robots and ALPHA on legs; AlphaBot 2's arms the wheeled template's; the A3's titanium and TPU not
drawn, its frame magnesium alloy. Nothing entered: the entry is a step of its own, for his yes.

### E11.7 Spec: the entry of batch 1 of types 3 and 4 (2026-10-30). Nothing built

Matthias, 2026-10-30: "Spec the entry". It enters what was agreed: E11.2 ("Yes, all four"), E11.5 ("Yes, 64 kg") and
E11.6 ("Yes, agree E11.6"), and settles E10.1 point 8 (how types 3 and 4 draw their robots taken apart in type 1 or
2). Found in the code and data for it (V113): 02 draws a type from its own parts file only, with one set of shared
values (constants, joint parts, shares, magnet grades) read from that file; type 1's and type 2's files share 13
constants, 11 equal and 2 under the same names with different values (the templates: "Joint modules, share of the
robot mass" 49 % and 40.4 %, "Battery energy per kg of robot" 12 and 14.67 Wh/kg); no robot is of types 1 and 2 both;
a robot's rows stand in one file only (the register stops otherwise); the element recipes hold types 3 and 4's
aluminium and plastics ("Engineering plastics", "Polymers & elastomers") and type 4's magnesium, 02's `RECIPE_FAMILY`
only types 1 and 2's. Batch 1 by its first type among 3 and 4: 19 robots for type 3 (3, 4, 5, 7, 10, 11, 12, 18, 22,
26, 28, 29, 31, 32, 33, 43, 51, 56, 58), 8 for type 4 (1, 6, 8, 9, 14, 17, 45, 46).

| # | What is built (his words: the agreed points) | Where |
|---|---|---|
| 1 | **A parts file and builder for each of types 3 and 4** (decision C, 2026-10-29: "a parts file and a builder per type"), each robot in the file of its first type among 3 and 4, its block once | `data/researched/3_industrial_logistics_warehousing/parts_taken_apart.xlsx`, `…/4_service_healthcare_interaction/…`; `tools/3_industrial_logistics_warehousing/make_parts_taken_apart.py`, `tools/4_…/make_parts_taken_apart.py` |
| 2 | **Types 3 and 4's templates** (E11.6 point 1) in both files, **under names of their own** ("Joint modules, share of the robot mass, types 3 and 4", "…, types 3 and 4, on wheels", "Battery energy per kg of robot, types 3 and 4", "…, on wheels"), so that no shared value has two numbers under one name; their rows named by what they average; one copy of them for both builders (open point A) | the builders; 01's names of the template quantities |
| 3 | **The 27 robots, 28 blocks** (the X2 in two versions), by E11.6 point by point; every source's code in its file's sheet Sources; the Atom (DOBOT) by the same function as type 2's Atom Max (E7.5), from DOBOT's same model | the builders |
| 4 | **A type drawn over robots of several files** (E10.1 point 8): 02 reads, for each type with a sheet, the parts files of its robots' types; each robot drawn from its own rows with its own file's shared values (one set per file); types 1 and 2 drawn as now, their draws unchanged (by program). Types 3 and 4 then drawn part by part over the robots taken apart so far, on their own with their draws written: type 3 over 72 (51 from types 1 and 2, 21 of batch 1), type 4 over 33 (17 and 16); their draws for stock-and-flow still from the workbook (Q2: 151 with a mass not yet taken apart, 178 less batch 1's 27) | `02_composition.py` (`read_apart_inputs`, `Shared`, `draw_taken_apart`) |
| 5 | **The register**: `TAKEN_APART` of types 3 and 4; the sheets Type 3 and Type 4 "drawn: its own parts" of the 95 taken apart (in any of their types' files), "not drawn: not yet taken apart" of the 151 others with a mass, "not drawn: no mass stated" of the 12 | `tools/make_humanoid_register.py`, 01's `check_type_sheet` |
| 6 | **01** reads and checks every type's file (each as now, check 18 with the templates of point 2); a robot taken apart in a file of one of its types counts for each of its types | `01_schemas.py` |
| 7 | **02's recipes of types 3 and 4** (the workbook's, E1.1): type 3 aluminium "Aluminum alloys", plastics "Engineering plastics"; type 4 aluminium "Aluminum alloys", plastics "Polymers & elastomers", **magnesium "Magnesium alloys"** (the A3's and A3 Ultra's frames, both of type 4 only) | 02's `RECIPE_FAMILY` |
| 8 | **Tests first** (each failing before its code): the 28 blocks against E11.6; the templates' numbers against the seven and three robots; types 1 and 2's draws unchanged; types 3 and 4 over their 72 and 33 robots, each robot as often, a robot of two files' types from its own file's rows; the register's sheets | `tests/` |
| 9 | **Sandbox** before his runs (the register, the four builders, 01, 02 at 2,000 draws, Claude's scratch folder); no remainder below zero, the pages looked at | scratch |
| 10 | **Documents**: README, METHODOLOGY (types 3 and 4 part by part; a type over several files), EVIDENCE E11.8 (where each point landed), VERIFICATION, HANDOVER with his runs by full path, each run saying what it changes | `documentation/claude/`, `README.md` |
| 11 | **Not in**: batch 2 of types 3 and 4; their draws for stock-and-flow from their parts (when all 151 are in); force, torque, touch sensors | — |

**Open points, each with my recommendation:**
- **A. Where the one copy of the templates and of the blocks shared by the two builders lives** (the seven robots on
  legs sit in type 2's builder, type 3's and type 4's). Recommended: one module for types 3 and 4,
  `tools/parts_types_3_and_4.py`, holding their templates and every block of their batches; each builder imports it and
  writes the robots of its type. A new file: your word.
- **B. Pages of types 3 and 4** (01's table of their robots and where their kinds sit; 02's element and material pages
  and the two figures): `output.robot_types_with_pages` 1 and 2 now. Recommended: 1 to 4, so that the entry is looked
  at as type 2's was.
- **C. What the entry leaves behind:** E10.1's wording "not drawn: its type drawn from the workbook; its own parts in
  type n" (`IN_RUN_ELSEWHERE` in the register and in 01, its test, its documents): after point 5 no sheet says it.
  Recommended: removed in the entry, the proof that nothing reads it in VERIFICATION.

### E11.8 Built: the entry of batch 1 of types 3 and 4 (2026-10-30). Nothing committed

Matthias, 2026-10-30: "Yes, build it" (E11.7, open points A to C as recommended). Checks: VERIFICATION.md V114. Not run
on his data: the register, the four parts files and the pages are written by his runs (HANDOVER.md).

| Point | Where it landed |
|---|---|
| 1, A | `tools/parts_types_3_and_4.py` (the one copy: the templates and the 28 blocks; type 2's builder's functions and blocks reused, not copied); `tools/3_industrial_logistics_warehousing/make_parts_taken_apart.py` (19 blocks), `tools/4_service_healthcare_interaction/make_parts_taken_apart.py` (9 blocks, the X2 in two versions) |
| 2 | the templates in `TYPES_34_SHARED`, written into both files; 01's `TEMPLATE_OF_TYPE` and `template_quantity()` (a robot takes the names of its own file's type) |
| 3 | the 28 blocks, by E11.6 point by point; their sources' codes in each file's sheet Sources (`sources()`) |
| 4 | 01's `type_parts()` and `shared_of()`; 02's `read_parts_files()`, `read_apart_inputs(…, files)`, `file_inputs()`, `draw_taken_apart()` (one `Shared` per file, each robot its own file's; `heat_of()`) |
| 5, C | the register's `TAKEN_APART[3]`, `TAKEN_APART[4]`, `taken_apart()`, `in_the_run()`; `IN_RUN_ELSEWHERE` removed from the register and 01, with its branch (V114: nothing reads it) |
| 6 | 01's `check_type_sheets()` (a robot taken apart in any file of its types), each file checked as its own type's |
| 7 | 02's `RECIPE_FAMILY[3]`, `RECIPE_FAMILY[4]` |
| 8 | tests: `TestTypesThreeAndFour` in `test_make_parts_taken_apart.py` and in `test_parts_taken_apart.py`, `test_the_sheets_type_3_and_type_4`, `TestTypesThreeAndFourPages`, 02's page tests over types 1 to 4 |
| 9 | the sandbox at 2,000 draws, V114 |
| 10 | README, METHODOLOGY ("Robot types 3 and 4 part by part, in 02"; checks 18 and 22), this section, V114, HANDOVER |
| B | `output.robot_types_with_pages = (1, 2, 3, 4)` |

**Where the build departs from the text, for his word:**
1. **The DOBOT Atom (register 45).** E11.6's table gives it 60.81 / 61.81 / 62.81 kg and joints of its model's 25.5 kg
   (41.2 % of its mass); E11.7 point 3 says "by the same function as type 2's Atom Max (E7.5), from DOBOT's same model".
   I built it by the second: type 2's Atom Max block, 57.91 / 58.91 / 61.81 kg and type 2's joints, 22.4 kg (38.0 %).
   The templates are the same either way (the median of the seven, 44.7 %, is the H2's). **Decided** (Matthias,
   2026-10-30: "Keep as built"): as built; E11.6's row 45 (60.81 / 61.81 / 62.81 kg, 25.5 kg of joints) is not used.
2. **Its name** in the files: 'DOBOT Atom 153 cm'. 'DOBOT Atom' holds the Atom Max's rows since E7.3, and a name may
   hold no brackets (the register's test; my first name, 'DOBOT Atom (base)', failed it).
3. **The AlphaBot 2's arms**: its stated neck, waist, knee and ankle joints lie outside the template on wheels' groups,
   so its arms are joints of their own: the template on wheels' share (13.9 %) of its mass at the mode (135 kg), split
   as the template splits its shoulders and elbows, per joint, half to 1.5 times (E). They do not follow the drawn
   mass, as a template's share would.
4. **A battery whose maker states only its energy** (NEO 842 Wh, A2 700, A3 and A3 Ultra 1,152, X2 and X2 Ultra 500)
   is written as 48 V (E, as type 2's TLIBOT T1, E8.3 point 6) times the energy over 48 V, the capacity ± 5 % (E7.5
   point 6). 02 uses the voltage only times the capacity (`draw_robot`), so each draw's energy is the stated one ± 5 %,
   whatever the voltage.
5. **Type 3's magnesium recipe**: built first for types 3 and 4; no robot of type 3 has magnesium (the A3's and A3
   Ultra's frames are of type 4 only), so taken out again for type 3, as point 7 says.

**What the sandbox found (V114), for his word:**
- **The 1X NEO's frame falls below zero in 13.5 % of its draws** (20,000 draws of type 4, 590 of them the NEO's): its
  30 kg hold the template's joint modules, 44.7 % (13.4 kg), two hands of 22 joints (3.2 kg), the battery (5 kg) and
  the shell (3.5 kg), so its frame, the remainder, is 3.4 kg on average (95 %: −1.9 to 8.3). Reported, not cut. Every
  other robot of types 3 and 4 below 1 % (type 1's known small ones; the A3 Ultra 0.16 %).
- 01's table title of type 3 ran off its page ("… taken apart so far, each drawn from its own parts (1 of 5)"): it now
  reads as type 2's, "Robot type 3: 72 of its 169 robots with a mass, each drawn from its own parts (1 of 5)".
- Seen in passing, not changed: a robot drawn in another of its types takes that type's recipes; were one to name a
  material that type has no recipe for (none does now), 02 would stop with a KeyError rather than a fault.



## E10. Robot types 3 and 4 together (2026-10-30). Nothing built

Matthias, 2026-10-30: "Can we move to type 3 and 4 together?", then "Yes, together" (to: types 3 and 4 together,
starting with their register sheets, step 5 of the steps robot type 1 went through, HANDOVER).

### E10.1 Spec: the register's sheets Type 3 and Type 4 (step 5). Nothing built

Found in the register and the code (V107): type 3 has 181 robots of the register, 169 with a mass; type 4 135, 131
with a mass; 58 are of both, 258 together. 68 of them are already taken apart in type 1 or 2 (51 of type 3: 47 also of
type 2, 4 also of type 1; 17 of type 4: 11 also of type 2, 6 also of type 1); 190 are still to do, 178 with a mass and
12 without. The column "Taken apart as" holds a robot's rows wherever they are, and a sheet Type n copies it from the
robot's row: 01 (`types_taken_apart()`) and 02 (`run()`) read a type as taken apart when any robot of its sheet has it,
so with sheets Type 3 and Type 4 both would look for the parts files of types 3 and 4, which do not exist, and 02 would
stop. The register writes "not drawn: its type drawn from the workbook, none of its robots taken apart yet" for every
robot of a type none of whose robots is in that type's own file: not true of the 68.

| # | What is built (his words: "Yes, together", the register sheets first; "If there is no mass then it should not be taken into the evaluation") | Where |
|---|---|---|
| 1 | **The sheets Type 3 and Type 4**: every robot of the register whose types include 3 (181) or 4 (135), in the register's order, each its row of the sheet Robots and "In the run" | `tools/make_humanoid_register.py` (`TYPES_LISTED`) |
| 2 | **A type is drawn part by part only from its own parts file**: 01 and 02 read a type as taken apart when a robot of its sheet is "drawn: its own parts" (the register writes it only for the robots of the type's own file), not when its "Taken apart as" is filled; types 3 and 4 stay drawn from the workbook, their draws unchanged | `01_schemas.py` `types_taken_apart()`, `02_composition.py` `run()` |
| 3 | **"In the run" of the 68 taken apart in another of their types**: open point A | the register, 01's check of the sheets |
| 4 | **No mass, no evaluation**: a robot without a mass says "not drawn: no mass stated" in every sheet, also while its type is drawn from the workbook (the 12 of types 3 and 4); the pages count only the robots with a mass: type 2 "all its 96 robots" (02's titles; 01's table titles, its overview's box and input box), no "open" line on the Xialan S0 | the register `in_the_run()`, 01's `check_type_sheet()`, 01's and 02's texts |
| 5 | **01's overview**: the boxes of types 3 and 4 "Its 181 robots of the register listed, 169 with a mass; drawn from the workbook until they are taken apart" (type 4: 135, 131); the open line "Open: robot types 3 and 4 together, then 5 and 6; then the six compared." | `01_schemas.py` |
| 6 | **Tests first**; a sandbox run (the register, 01, 02 at 2,000 draws, Claude's scratch folder): the draws of types 3 and 4 the same as without their sheets (the same seed), compared by program | `tests/`, scratch |
| 7 | **Documents**: README (the register's sheets), METHODOLOGY (check 22), HANDOVER, VERIFICATION; his runs by full path | `documentation/claude/`, `README.md` |
| 8 | **Not in**: the research of their robots (the next step, in batches, a source table first); pages of types 3 and 4 (`output.robot_types_with_pages` stays 1 and 2); how type 3 or 4 will draw a robot taken apart in type 1 or 2 (at their entry: from that file, one copy) | — |

**Open point, with my recommendation:**
- **A. What the sheets Type 3 and Type 4 say of the 68 already taken apart in type 1 or 2.** Recommended: "not drawn:
  its type drawn from the workbook; its own parts in type 2" (or "in type 1"), written by the register and checked by
  01, in place of "… none of its robots taken apart yet", which is not true of them.

**Built** (Matthias, 2026-10-30: "Yes, build it", A as recommended; checks V108; nothing committed):

| Point | Where it landed |
|---|---|
| 1 | `tools/make_humanoid_register.py` `TYPES_LISTED = (1, 2, 3, 4)`; its About sheet |
| 2 | `01_schemas.py` `drawn_part_by_part()`, used by `types_taken_apart()` and by `02_composition.py` `run()` |
| 3, A | `IN_RUN_ELSEWHERE` in the register and in 01; the register's `in_the_run()` (the type whose `TAKEN_APART` holds it), 01's `check_type_sheet()` (the robot's other type) |
| 4 | the register's `in_the_run()` and 01's check: no mass first; 02's `ApartInputs.listed` and 01's titles count the robots with a mass (`lead()`, `robots_table_pages()`, `taken_words()`, `type_card_text()`) |
| 5 | 01's `type_card_text()`, `overview_types(…, listed)`, the open line |
| 6 | tests: `test_the_sheets_type_3_and_type_4`, `test_a_robot_with_its_own_parts_in_another_of_its_types`, `test_a_robot_without_a_mass_is_not_drawn_while_its_type_is_drawn_from_the_workbook`, `test_its_card_and_its_words_on_the_overview_count_only_the_robots_with_a_mass`, type 2's titles; the sandbox |
| 7 | README, METHODOLOGY check 22 and its table of stages, HANDOVER, VERIFICATION V108 |

## E9. Each robot of type 2 its own composition: research, the robots on wheels (2026-10-30). Nothing entered

Matthias, 2026-10-30: "Yes, start sources" (the sources of type 2's 43 robots on wheels, decision B: their own kinds of
part). Read on 2026-10-30: the makers' pages and documentation through seven web-fetch reads (HTML text only), and where
those got no text (script-rendered, pictures, a manual behind a link), in the built-in browser myself; the makers' model
files through GitHub's interface, their masses summed and their joints' limits listed by script. **No PDF was opened**
until his word (E9.2 point 4); then four datasheets were read (E9.3). (The fetch tool saved PAL's two datasheet PDFs, ARI and
TIAGo Pro, to its own folder unasked; neither was opened or read.) A search engine's summary is never a source here:
it only pointed to pages. Nothing is entered.

### E9.1 Robot by robot: what the makers state

The register's height and mass in brackets (the catalogue humanoid.guide, E4); **bold** where the maker's differs.

| # | Robot (the register) | What the maker states | Source | Kind |
|---|---|---|---|---|
| 13 | AGIBOT A2-W, AgiBot (163 cm, 230 kg) | **no longer on AgiBot's sites**: the address /products/A2_W shows the A2 flagship (远征A2 旗舰版, a walking robot); the product menus list A3 Ultra, A3, A2 旗舰版, A2 青春版; G2, G1 Max, G1. A2-W only as an option of the contact form | agibot.com/products/A2_W; agibot.com.cn/products/A2_W (in the browser) | maker, not listed |
| 15 | AGIBOT G1, AgiBot (130–180 cm, 150 kg) | "150kg", "130~180cm"; "20 DoF" without end-effector (the text: "26 DOFs"; head turns and nods, waist bends, rises and lowers); end-effector "6 DoF（Can Replaced with Two-finger Gripper）"; "Jetson AGX Orin 64GB"; "Six-Axis Force" sensors on both arms; "RGBD Camera*3 & Fisheye*5", the chassis "RGBD cameras front and rear and LiDAR"; "Runtime: 4h+"; the chassis turns in place. Battery energy, base, torques: not stated | agibot.com/products/G1 | maker, spec |
| 20 | AI Worker, ROBOTIS (162 cm, 90 kg) | FFW-SG2 (mobile): "90 kg", "604x602x1,623 (mm)"; "Total: 25 DOF; Arm: 7 DOF x 2; Gripper: 1 DOF x 2; Head: 2 DOF x 1; Lift: 1 DOF x 1; Mobile: 6 DOF"; "Swerve Drive", "three wheels positioned in a triangular arrangement", 1.5 m/s; lift 0 to 500 mm; "Battery: 25V, 80Ah (2,040Wh)"; "NVIDIA Jetson AGX Orin 32GB"; ZED Mini, RealSense D405 × 2, LiDAR LakiBeam 1 × 2, IMU; "Aluminum, Plastic". Its actuators by model: arm joints 1–3 YM080-230-R099-RH, 4–6 YM070-210-R099-RH, 7 PH42-020-S300-R; head XH540, XH430; lift YM080-230-B001-RH; wheel steering YM070-210-R051-RH; gripper RH-P12-RN (500 g). Its model `ffw_sg2.xml` (MuJoCo): **94.42 kg**, the base 35.99 kg, the lift 17.9 kg, three wheel-drive links 3.80 kg each; no torque limits (all 1000) | ai.robotis.com/ai_worker/hardware_ai_worker.html; github.com/ROBOTIS-GIT/ai_worker (`ffw_description/mujoco/ffw_sg2/ffw_sg2.xml`) | maker, spec; maker's model |
| 21 | AICO 2, Flexiv (160 cm, 281 kg) | **two versions named AICO 2** (the values by the table's column order): AICO 2-4 "281kg", "2*7" DoF, "Dual-wheel differential", "6h", payload "2*4kg"; AICO 2-10 **"395kg"**, "2*7", "Dual-wheel differential", "4h", "2*10kg"; both "Laser SLAM", force sensing. Height, battery energy, computers: not stated (the panels are pictures) | flexiv.com/product/robot-system | maker, spec |
| 34 | ARI, PAL Robotics (165 cm, 60 kg) | "2 DoF Head", "2 DoF Mobile base", "4 DoF Arms (2x)", a humanoid torso; "24V / 40VAh (Optional 60Ah)", "8-12 hours autonomy"; "CPU Intel i5 / i7 / i9", "GPU Nvidia Xavier NX or Orin … (optional)"; RealSense D435i × 2, T265, LiDAR (optional), 10.1" touchscreen, two LCD eyes, 4 microphones, 2 × 30 W speakers. Its datasheet (E9.3): "Height 165 cm", "Width 53 cm", "Depth 75 cm"; **"Arm (2X) 5"** (shoulder 2, upper arm 1, elbow 1, wrist 1; the docs: 4); "Standard differential drive API". **Mass: not stated, the datasheet neither**. Its model in PAL's repository as xacro, not expanded | docs.pal-robotics.com/edge/hardware/ari/hardware-overview; pal-robotics.com/datasheet/ari (PDF); github.com/pal-robotics/ari_robot | maker, spec, datasheet; maker's model (xacro) |
| 35 | ARMAR-7, KIT (175 cm, 120 kg) | "two 8-DoF torque-controlled anthropomorphic arms and 4-DoF underactuated humanoid hands", "3-DoF head", "A 2-DoF knee/hip kinematic" (the torso bows and changes height), "a holonomic mobile platform … three omni-wheels"; an RGB camera in each hand. **Mass, height, battery, computers: not stated** | h2t.iar.kit.edu/397.php; src.stanford.edu/demo/armar | developer (a lab), spec |
| 40 | Astribot S1, Astribot (170 cm, 80 kg) | "80kg", "170cm", arm span "194cm"; "Single arm DoF" "7"; "4~6hours", "Supports plug-in"; payload per arm "5kg". Torso, base, battery energy, computers, sensors: not stated | astribot.com/en/product | maker, spec |
| 41 | Astribot T1, Astribot (155 cm, 66 kg) | only a banner "Meet Astribot T1", "From ¥89,900 CNY"; **no figures**; its "Buy now" leads to a contact form | astribot.com/en | maker, no figures |
| 42 | AstroD. AD-01, Elu.AI (170 cm, 120 kg) | INFIFORCE (ELU.AI's brand; elu-ai.com leads there) names "AD-01" at work; its AstroDroid page "搭载Hyper-VLA端到端模型"; **no figures** | infiforce.cn, infiforce.cn/robot | maker, no figures |
| 49 | Avatar, Honda (**155 cm, 101 kg**) | **"1700mm Height", "110kg Weight"**, "56 DOF": head 3, arm 8 × 2, hand 16 × 2, waist 3, wheel 2; "1.0m/s". Battery, torques, computers, sensors: not stated (Japanese page the same: 全高1700mm, 重量110kg, 車輪 2) | global.honda/en/RandD/field/hgrx/honda-multi-fingered-hand/avatar-robot.html; …/jp/… | maker, spec |
| 60 | CASBOT W1, CASBOT (112–210 cm, ~260 kg) | "重量约260kg", "高度112cm - 210cm" (收缩 0.95 × 0.615 × 1.12 m, 伸展 … × 2.1 m); "20DoF": arm 7 × 2, neck 2, waist 1, lift column 1, chassis 2; "轮组形式 2+4，两轮差速" (two driven wheels, four more); "电池电压 48v", "电池容量 48V/25Ah", "电池类型 磷酸铁锂" (LFP; 1,200 Wh, arith.), "续航时间 4-5h"; "工控机（i9 cpu+4060显卡）", "交互 3588"; a 360° LiDAR, RGBD × 4, a stereo camera, 2 microphones; gripper 500 g; "合金、工程塑料". The page: its figures "来源于理论计算及实验室测试结果" | casbot.tech/product/w1 | maker, spec |
| 68 | CUE7, Toyota (218 cm, 74 kg) | **no page of Toyota's found** (its global newsroom searched). Second-hand only: 219 cm (Japanese press), **74 kg** (one English article), **78 kg** (another), an inverted two-wheel base, about 30 motors | (press, not the maker) | second-hand |
| 82 | Dual-Arm Lift, RealMan (178 cm, 157 kg) | "≈ 157 kg", "640 × 450 × 1780 mm"; "Lifting Stroke 900 mm"; "dual RM65-B-V arms" (6 DoF each; RM75-B-V optional), "Single Arm Payload 5 kg"; "1.5 m/s", turns in place; "Endurance 3–4 hours"; gripper CTAG2F90D. Battery energy, base, computers: not stated | realman-robotics.com/en/products/dual-arm-lift.html | maker, spec |
| 86 | Eggie, Tangible Robots (160 cm, 45 kg) | the site names no robot, **no figures** | tangiblerobots.ai | maker, no figures |
| 92 | Feather, Feather Robotics (180 cm, 105 kg) | "Total weight" "105 kg" (fully configured); 1200 to 1800 mm ("600 mm travel"); "23 DoF" ("7 per arm · 2 neck · 1 torso · 6 base"); "Holonomic (omnidirectional)", 1.3 m/s; "Dual hot-swappable packs", "48 V", "50 Ah" (2,400 Wh, arith.), "10 hour battery life with 240w load"; "Jetson Nano · Jetson Orin AGX · Jetson Thor"; ZED cameras, 4 microphones; hands of 6 DoF or grippers; its spec sheet (E9.3) the same, the energy not stated | feather.dev, feather.dev/technology, feather.dev/docs/feather-spec-sheet.pdf | maker, spec, datasheet |
| 104 | G1-D, Unitree (160 cm, 90 kg) | two versions: **Standard has no mobile chassis** ("/"); **Ultimate** the wheeled one. Both "Approx. 90kg" with battery, 1260 to 1680 mm; Ultimate "19" DoF: arms 7 × 2, waist 2, column 1, base 2; "Diﬀerential drive", 1.5 m/s; "Upper Body Battery(Quick-release): 9Ah", "Chassis Battery (Built-in): 30Ah" (voltage not stated); "8-core High-performance CPU", optional Orin NX 16 GB; head binocular camera, wrist cameras × 2; chassis LiDAR, depth cameras × 2 | unitree.com/G1-D | maker, spec |
| 105 | G2 Genie, AgiBot (175 cm, **55 kg**) | its user manual (an HTML page, 2026-04-28), 2.3 整机参数: "高度 1225 mm ~ 1795 mm", **"重量 185 kg"**, "自由度（不含末端） 25": head 3, arms 7 × 2 with "关节扭矩传感器 具备", torso 5 ("腰部3自由度", legs 2 "折叠升降"); "底盘 形式 4舵轮" (four steered wheels), 1.5 m/s; "电池数量 2", "电池总容量 1652Wh（34Ah）", "额定电压 48V", "约4h"; computing "500 TOPS (INT8)" or "2070 TFLOPS (FP4)"; head stereo camera 1, fisheye 3, RGBD 1, wrist RGBD 2, chassis LiDAR 2, ultrasonic 8, IMU, 4 microphones, an 8 W speaker, a 6.3" screen; "100%车规级零部件" (the product page) | agibot.com.cn/filepage/362.html (in the browser); agibot.com/products/G2 | maker, user manual |
| 122 | H2-D, Unitree (170 cm, 120 kg) | two versions: "H2-D Standard" (a chassis moved by hand) "Approx. 148Kg"; **"H2-D Flagship" (mobile chassis) "Approx. 120Kg"** with battery. Flagship: 20 DoF: arms 7 × 2, waist 1, head 2, column 1, chassis 2; "dual-wheel differential drive", 1.5 m/s; lift "0.46m"; "48V/30Ah (1.44 kWh)" quick-release base battery; "Maximum Arm Joint Torque: 120N.M"; PCs Intel Core i5 and i7, optional Thor; binocular camera, wrist cameras × 2, LiDAR, depth camera, 2 collision and 2 ultrasonic sensors; "Aerospace-Grade Aluminum, Titanium Alloy, and High-Strength Engineering Plastics" | unitree.com/H2-D | maker, spec |
| 179 | MagicBot D1, MagicLab (180 cm, 150 kg) | "150kg", "1190‑1800mm (H) × 620mm (W) × 670mm (L)"; "25 DoF": neck 2, arms 7 × 2, waist 3, legs 2, chassis "4‑6 DoF"; "four‑steering‑wheel chassis", 1.5 m/s; "Joint Torque Sensing Full‑joint enabled"; "Battery ×2", "Total Capacity 1652Wh", charger "54.75V / 15A", "Runtime 4h"; "Huawei R1, 500 TOPS (INT8)" or "2070 TOPS (FP4)"; RGB, stereo, fisheye × 3, wrist RGBD × 2, LiDAR × 2, ultrasonic × 3 (the text: 8). As the AgiBot G2 in battery and computing | magiclabglobal.com/magicbots/magicbot-d1 (in the browser) | maker, spec |
| 184 | Mantis Standart, Blue Worm (140 cm, 50 kg) | "Mantis Standard「小白」", modular: 整机尺寸 633 × 552 × 1400 mm; "升降范围 550 mm"; "全身自由度 22"; "底盘能力 3 自由度全向移动"; "整机续航 3 h"; arm 7 DoF, "单臂负载 7 kg", "最大电机扭矩 80 N·m" (the single-arm version's table). **Mass: not stated** (second-hand press: about 35 kg) | bluewormrobotics.com/products/mantis-standard (in the browser) | maker, spec |
| 200 | Moz1, Spirit AI (160 cm, 70 kg) | its product page names no robot: "七轴仿生臂", "全向轮式底盘", "自由度达26个", force-controlled joints. **Mass, battery: not stated** | spirit-ai.com/product | maker, no name, few figures |
| 230 | Phoenix Gen 8, Sanctuary AI (170 cm, 70 kg) | "Phoenix Generation 8 … has a wheeled base"; improved cameras; **no figures** | sanctuary.ai/news/… (generation 8) | maker, no figures |
| 247 | R1 PRO, Galaxea (170 cm, **96 kg**) | **"126 kg (277.8 lb) - including battery"** (96 kg is the R1 Lite's); 1700 mm; "26" DoF: arm 7 each, torso 4, chassis "6 , 360° Omnidirectional", 1.5 m/s; "NVIDIA Jetson AGX Orin, 32GB", 200 TOPS. The R1's guide (named the R1's, not the Pro's): "48 V", "35 Ah", "1680 Wh", lithium-ion; "a three-wheel steering vector chassis" (the R1's; the Pro counted with the steered bases below on it); torso torque rated 108, max 304 N·m; ZED 2, D435i × 2, 5 cameras, Livox MID-360 × 1–2 | galaxea-dynamics.com/products/galaxea-r1-series-… (in the browser); userguide-galaxea.github.io (R1) | maker, spec |
| 248 | R1-D, Unitree (160 cm, **52 kg**) | the R1 page, mobile versions **R1-A5-D "Approx. 30kg", R1-A7-D "Approx. 32kg"**; raised "1600x520x440mm"; DoF with gripper 18 / 22: arms 5 or 7 each, waist 1, head 2, chassis 3; "Maximum torque of the shoulder: 60N·m"; "Li-ion Battery", "Approx. 1.5h"; 8-core CPUs, head 10 TOPS; chassis LiDAR, binocular camera | unitree.com/R1-D | maker, spec |
| 251 | RB-Y1, Rainbow Robotics (160 cm, 131 kg) | two models: **A "Total: 131kg"** = upper body 38 (arm 11 × 2, torso 16) + lower body 42 + mobile 51; **M "Total: 170kg"** (mobile 90). 600 × 690 × 1,400 mm; wheel 1 DoF × 2 (A) or × 4 (M), leg 6, arm 7 × 2, head 2; "50V, 25Ah (1,250Wh)" (A), "50V, 50Ah (2,500Wh)" (M); FT sensors in both arms (V1.2); exterior "Aluminum". Its model `rby1a/urdf/model_v1.2.urdf`: **132.22 kg**, the base 60.08 kg; torso limits 270 × 3, 120 × 3 N·m; arms 70, 70, 70, 40, 10, 10, 8 N·m | rainbow-robotics.com/en/products/rb-y1; github.com/RainbowRobotics/rby1-sdk | maker, spec; maker's model |
| 252 | Reachy 2, Pollen Robotics (166 cm, 50 kg) | "Up to 50 kg" (full robot), "136-166 cm"; arms 7 × 2 (Orbita 2D × 2: 60 W Maxon EC45 flat each motor; Orbita 3D × 1: 40 W Maxon ECXT22L), neck 3 (Orbita 3D); mobile base "Weight: 25kg", "3 omni wheels", LiDAR, "8 hours battery life"; "Solidrun Bedrock v3000". Battery voltage and energy: not stated; its two datasheets are no longer online (E9.3) | pollen-robotics.com/reachy-2; docs.pollen-robotics.com/hardware-guide/specifications/… | maker, spec |
| 253 | RealBot-01, RealMan (168 cm, 125 kg) | "≈ 125 kg", "570 × 465 × 1680 mm"; "21 active degrees of freedom": arms 14, waist 3, legs 2, neck 2; "40 Ah (BMS)" (voltage not stated); dual RX75 arms, 5 kg each; "5 depth cameras, 3 fisheye cameras, 1 LiDAR, 2 IMUs", microphones | develop.realman-robotics.com/en/wheelRobot/RealBot01/; realman-robotics.com/en/products/realbot-humanoid.html | maker, spec |
| 254 | RealBot-L2, RealMan (170 cm, 120 kg) | "≈ 120 kg", "650 × 512 × 1700 mm"; "17 DoF"; "Dual-wheel differential drive"; "Lifting stroke 0.3 m"; "48V 20Ah" (960 Wh, arith.), "≈ 6 h"; "Jetson AGX Orin 64G" | develop.realman-robotics.com/en/wheelRobot/RealBotL2/; …/realbot-l2.html | maker, spec |
| 255 | RealBot-S2, RealMan (170 cm, 125 kg) | "≈ 125 kg", "614 × 552 × 1700 mm"; "20 DoF", arm 7 each; "Four-wheel steering, four-wheel drive"; "48V 20Ah" (960 Wh, arith.), "≈ 6 h"; "Nvidia Jetson AGX Orin 64G"; stereo and fisheye cameras, RGBD at the hands, dual LiDAR | develop.realman-robotics.com/en/wheelRobot/RealBotS2/; …/realbot-s2.html | maker, spec |
| 295 | TIAGo Pro, PAL Robotics (**155 cm, 80 kg**) | **"Weight 95 Kg"**, **"Height 120 - 150 cm"**; DoF: mobile base 3, torso lift 1, arm 4, wrist 3, head 2, gripper 1 (one arm or two: not said); "Omnidirectional", "4x Meccanum Wheels", 1 m/s; "Lift stroke 35 cm"; "Series Elastic Actuators (SEA)"; "Battery 2 x 36 V, 20 Ah" (1,440 Wh, arith.), "8-10 hours"; 2 laser range-finders, IMU, wrist force/torque, RealSense D435, microphones; payload 3 kg. **Its datasheet (E9.3) differs: "Weight 80 kg"**, "Height 120–155 cm", "Autonomy 4 hours", "Total DoF 23 DoF Including Default Grippers": arms 7 DoF each, two by default ("Other configurations available (single and no arms)"), torque sensing "On Each Arm Actuator"; lift 1 DoF, "Torso Range 35 cm"; base "Omnidirectional (4 DoF)", "4x Mecanum Wheels"; "Intel i5, RAM 16 GB, 512GB SSD"; battery not stated, an "Additional Battery (for increased autonomy)" an upgrade | docs.pal-robotics.com/edge/hardware/tiagopro/hardware-overview; pal-robotics.com/datasheet/tiago-pro (PDF) | maker, spec, datasheet |
| 307 | Torobo, Tokyo Robotics (166 cm, **160 kg**) | as E8.1: **"approx. 120 kg"**, 1615 mm, arms 7 × 2, waist 3, neck 3, "4-axis undercarriage (omni-directional mobile base)", torque sensors in arms and waist, about 3 h | robotics.tokyo/technologies/torobo | maker, spec |
| 312 | VB1-I, Lanxin (~165 cm, ~60–70 kg) | as E8.1: "Dual-wheel differential motor" (its feature list: "Omnidirectional"), 700 × 610 × 1650 mm, arm 6 joints, "2~3h", gripping load 2 kg. **Mass: not stated** | lanxinrobotics.com/humanoid-robots/vb1-i | maker, spec |
| 313 | VB2, Lanxin (~170 cm, ~65–75 kg) | as E8.1: "Four-wheel omnidirectional wheel", 580 × 480 × 1700 mm, arm 7 joints, "4~6 h", gripping load 5 kg. **Mass: not stated** | lanxinrobotics.com/humanoid-robots/vb2-2 | maker, spec |
| 314 | Vega, Dexmate (171 cm, 135 kg) | "Vega 1 Pro": "298 lbs (135 kg)"; folded 0.66 m, arms raised 2.50 m; "24" DoF: arms 14, torso 3, head 3, "Base 4 (2 steering, 2 drive)", "Omni-directional"; "20 hrs of operation" (battery not stated); "NVIDIA Jetson AGX Thor"; LiDAR × 2, RGB cameras × 4, stereo head; payload 5 kg per arm; its spec sheet (E9.3) the same, no battery. Its model `vega_1p.urdf`: **141.00 kg**, the base 88.43 kg; torso limits 700, 380, 380 N·m; arms 150, 150, 80, 80, 25, 25, 25; head 6, 2.5, 6; two driven wheels 16 N·m (3.7 kg each), two steering 6 N·m | dexmate.com/product/vega-1-pro; github.com/dexmate-ai/dexmate-urdf (`robots/humanoid/vega_1p/vega_1p.urdf`) | maker, spec; maker's model |
| 315 | VersaBot VB-1, Lanxin (165 cm, 75 kg) | Lanxin's "VB1" (taken as the VersaBot VB-1): "700×610×1650", arm 6 joints, "Four-wheel omnidirectional wheel", 0–1.2 m/s, "2~3h", gripping load 2 kg. **Mass: not stated** | lanxinrobotics.com/humanoid-robots/vb1 | maker, spec |
| 318 | W-Bot, Yue Quan Bionics (178 cm, 60 kg) | "博文W-Bot 2.0": "全身尺寸 1.78m", "整机重量 60kg", "43个自由度"; arm 7 each; trunk "髋关节x3 + 膝关节x1 + 踝关节x1+底盘×2 =7" (a folding hip-knee-ankle on a wheeled chassis); "膝关节约 360N·m，踝关节约 160N·m，手臂关节约 60N·m"; "电池容量2400W·h，最大电压48V"; "NVIDIA Jetson Orin NX 16GB×2"; RealSense D435i and D455, Livox 360 LiDAR; a six-axis force sensor | yqbionics.com/W_Bot (in the browser) | maker, spec |
| 335 | Y1, Tlibot (195 cm, 150 kg) | **not on Tlibot's list** (天灵L3 in four versions, T1) | tlibot.com/cpzx/6.html | maker, not listed |
| 336 | Y2-B, Tlibot (160 cm, 85 kg) | as 335 | as 335 | maker, not listed |
| 337 | Y2-P, Tlibot (156.5 cm, 95 kg) | as 335 | as 335 | maker, not listed |
| 340 | YMBot D, Yunmu (165 cm, 100 kg) | YMBot's site has no product pages (home, about, news) | ymbot.com (in the browser) | maker, not listed |
| 341 | YMBot D2, Yunmu (180 cm, 150 kg) | as 340 | as 340 | maker, not listed |
| 342 | YMBot D4, Yunmu (165 cm, 100 kg) | its news of 2026-07-03: "双臂负载60kg的YMBot D4型工业重载搬运人形机器人", "底盘采用优化轮式承重结构与冗余动力系统". **Mass: not stated** | ymbot.com/news (in the browser) | maker, news, few figures |
| 349 | ψ-SynRobot, PsiBot (145 cm, 65 kg) | the home page's "Psi SynRobot" links to "PsiBot-V1": "站立高度：<180cm", "腰部自由度：2个", "颈部自由度：2个", "续航：>8小时", "算力平台：Thor", "4个RGBD相机；3个鱼眼相机". **Mass: not stated** | psibot.ai; psibot.ai/products_zh/product_psibot-v1_zh/ | maker, spec |

### E9.2 The robots on wheels together, and the questions for Matthias

| What the makers give | Robots |
|---|---|
| Mass, joints by part, base, battery, and a model file | AI Worker, RB-Y1, Vega (the files give each part's mass; the RB-Y1's and Vega's also the torques) |
| Mass, joints by part, base, battery (voltage × capacity or Wh) | G2 Genie, MagicBot D1, H2-D, CASBOT W1, Feather, W-Bot (also torques), R1 Pro (battery from the R1's guide), RealBot-L2, RealBot-S2, TIAGo Pro, G1-D (Ah without volts), RealBot-01 (Ah without volts), R1-D (no energy) |
| Mass and joints, no battery | AGIBOT G1, AICO 2, Honda Avatar, Astribot S1, Dual-Arm Lift, Torobo, Reachy 2 (its base 25 kg) |
| Joints and base, no mass | ARI, ARMAR-7, Mantis Standard, VB1-I, VB2, VersaBot VB-1, ψ-SynRobot, Moz1 (no name on the page) |
| Nothing from the maker | A2-W (no longer listed); Astribot T1, AD-01, Eggie, Phoenix Gen 8, YMBot D4 (a news item only); CUE7 (no page of Toyota's found); not on their makers' sites: Y1, Y2-B, Y2-P, YMBot D, D2 |

**What they have in common, for the spec of the kinds of part:** every one is an upper body (arms, head, a waist or
torso of 1 to 6 joints, often a lift column or a folding leg of 2) on a wheeled base. The bases are of four kinds:
two wheels driven differentially, with casters (H2-D, G1-D, AICO 2, RealBot-L2, VB1-I, CASBOT W1 "2+4"; RB-Y1 A by its two wheel joints); three
or four steered wheels (AI Worker, G2 Genie, MagicBot D1, R1 Pro, RealBot-S2, Vega "2 steering, 2 drive"); omni or
mecanum wheels (ARMAR-7, Reachy 2, TIAGo Pro, VB2, VersaBot VB-1, Torobo); one inverted pair (CUE7). The base is the
heaviest part where a file shows it: 36 of 94 kg (AI Worker), 60 of 132 kg (RB-Y1), 88 of 141 kg (Vega), and 25 of 50 kg
by Pollen's page (Reachy 2).

**Questions, each with my recommendation:**
1. **The maker's mass where the register's differs** (E8.2 decided "the maker's mass" for batch 2b): G2 Genie 185 kg
   (register 55), R1 Pro 126 (96), R1-D 30 or 32 (52), TIAGo Pro 95 (80), Honda Avatar 110 (101). Recommended: the same
   rule, the maker's mass.
2. **Versions** (a discrete state, each drawn as often, as the Walker Tienkung): AICO 2 (2-4 281 kg, 2-10 395 kg), RB-Y1
   (A 131 kg, M 170 kg), R1-D (A5-D 30 kg, A7-D 32 kg), H2-D (Standard 148 kg with a chassis moved by hand, Flagship
   120 kg driven), G1-D (Standard without a mobile chassis, Ultimate driven). Recommended: the AICO 2, the RB-Y1 and the
   R1-D in their two versions; the H2-D and G1-D only in their driven version (Flagship, Ultimate), since the other is
   not a robot on wheels that drives.
3. **The robots no maker's source describes** (A2-W, T1, AD-01, Eggie, Phoenix Gen 8, CUE7, Y1, Y2-B, Y2-P, YMBot D,
   D2, D4): kept with the register's mass, as E8.2 kept the robots found nowhere. Recommended: kept; their parts from
   the wheeled template that the spec will propose.
4. **The makers' datasheets that are PDFs** (downloading needs his word): ARI and TIAGo Pro (pal-robotics.com/
   datasheet/…), Reachy 2 (pollen-robotics.com, two datasheets), Vega 1 Pro (cdn.sanity.io, its spec sheet), Feather
   (feather.dev/docs/feather-spec-sheet.pdf), AI Worker (its drawings, robotis.com). They would give ARI's mass and the
   batteries of Reachy 2 and Vega. Recommended: yes, these six makers' own PDFs, read only.
5. **The robots with no mass from their maker** keep the register's (the catalogue's) mass, labelled as the catalogue's:
   ARI 60, ARMAR-7 120, Mantis 50 (press: about 35), VB1-I 60–70, VB2 65–75, VersaBot VB-1 75, ψ-SynRobot 65, Moz1 70.
   Recommended: so, as type 1's robots without a maker's mass.

**Decided:** Matthias, 2026-10-30, "Yes, all five": the maker's mass in the parts file where the maker states it, the
register's reported (G2 Genie 185 kg, R1 Pro 126, R1-D 30 or 32, TIAGo Pro 95, Honda Avatar 110); the AICO 2 (2-4,
2-10), the RB-Y1 (A, M) and the R1-D (A5-D, A7-D) in two versions, each drawn as often; the H2-D only as its Flagship
and the G1-D only as its Ultimate (the driven versions); the 12 robots no maker's source describes kept, with the
register's mass, their parts from the wheeled template the spec will propose; the six makers' PDF datasheets read (E9.3);
the robots with no maker's mass keep the catalogue's, labelled as the catalogue's. The TIAGo Pro's mass was decided again on
PAL's datasheet: 79 / 80 / 95 kg (E9.3). Nothing entered yet: the register's
changes are code, and the spec of the wheeled robots' kinds of part comes first.

Not yet looked at, for the spec: the actuators' own pages that some makers name (ROBOTIS's DYNAMIXEL-Y, Pollen's Orbita
motors) and RealBot-01's joint-limit page.

### E9.3 The makers' datasheets (on "Yes, all five", point 4)

Downloaded on 2026-10-30, each into its own folder in Claude's scratch folder, and read first-hand:

| Datasheet | Got | What it adds to E9.1 |
|---|---|---|
| ARI, pal-robotics.com/datasheet/ari | PDF, 5 pages, 761,989 bytes | its size 165 × 53 × 75 cm; arms 5 DoF each (the docs: 4); differential drive; **no mass** |
| TIAGo Pro, pal-robotics.com/datasheet/tiago-pro | PDF, 2 pages, 1,045,043 bytes | **"Weight 80 kg"**, 4 hours, 23 DoF with two 7-DoF arms; a second battery an upgrade |
| Vega 1 Pro, cdn.sanity.io (linked from dexmate.com) | PDF, 1 page, 517,270 bytes | the same as its page; **no battery** |
| Feather, feather.dev/docs/feather-spec-sheet.pdf | PDF, 2 pages, 544,619 bytes | the same as its page (48 V, 50 Ah, dual packs); no energy in Wh |
| Reachy 2, pollen-robotics.com (two datasheets) | **"Page not found"** (HTTP 404), both | nothing; the battery stays not stated |
| AI Worker FFW-SG2 drawing, robotis.com/service/download.php?no=2215 | a ROBOTIS download page, not a PDF | nothing |

**The TIAGo Pro, for his word:** PAL states two masses. The datasheet: 80 kg, 4 hours, a second battery an upgrade.
The documentation: 95 kg, "2 x 36 V, 20 Ah", 8 to 10 hours. "Yes, all five" took 95 kg (point 1), which rests on the
documentation alone; the register's 80 kg is the datasheet's. Recommended: as the H1's two figures (E8.2), the
datasheet's 80 kg the mode and the documentation's 95 kg the maximum (79 / 80 / 95 kg), and one battery of 36 V, 20 Ah
(720 Wh) as the datasheet's standard robot.

**Decided:** Matthias, 2026-10-30, "Yes, 79 / 80 / 95": the TIAGo Pro's mass 79 / 80 / 95 kg (the datasheet's 80 kg
the mode, the documentation's 95 kg the maximum), one battery of 36 V, 20 Ah (720 Wh). This replaces the 95 kg of
"Yes, all five" (E9.2 point 1) for the TIAGo Pro.

### E9.4 Spec: the kinds of part of a robot on wheels (2026-10-30). Nothing built

Matthias, 2026-10-30: "Spec the wheeled parts" (decision B: "the wheeled robots their own kinds of part"). What exists:
ten kinds of part, the figures' rows (`01_schemas.py` `KINDS`: hip, knee, ankle, waist and arm joints, battery pack,
torso boards and heat sink, head, cables, frame and shell); each joint a module by its torque (E6.8's fit) or, without
torques, a share of the robot's mass (type 2's template, E7.4, from seven robots on legs); the frame the remainder. The
shared lists (`data/researched/shared_lists.xlsx`, placed by his decisions of 2026-10-26) have no body region for a base
and no part group for wheels. The car sensor list (RAWCLICVehicleElectronics 07_) has an "ultrasonic sensor".

What the 43 bring that a robot on legs has not (E9.1): a base on 2 to 4 driven wheels (two driven wheels, differential where
stated: H2-D, G1-D, AICO 2, RealBot-L2, VB1-I, CASBOT W1, ARI; by their two wheel joints: RB-Y1 A, W-Bot, Avatar; steered: AI Worker 3, G2 Genie 4,
MagicBot D1 4, RealBot-S2 4, Vega 2, R1 Pro; omni or mecanum: ARMAR-7 3, Reachy 2 3, TIAGo Pro 4, VB2 4, VersaBot VB-1
4, Torobo, Feather, Mantis, Moz1; an inverted pair: CUE7); a lift column (AI Worker 500 mm, H2-D 460, RealBot-L2 300,
Dual-Arm Lift 900, Feather 600, Mantis 550, TIAGo Pro 350; CASBOT W1, G1-D one joint) or a folding leg of 2 to 6 joints
(G2 Genie, MagicBot D1, RealBot-01, ARMAR-7, W-Bot, RB-Y1); chassis sensors (LiDAR, ultrasonic, depth cameras, collision
sensors); a battery in the base. The base is the heaviest part in the three model files: 36.0 of 94.4 kg (AI Worker,
its lift 17.9 kg more), 60.1 of 132.2 kg (RB-Y1), 88.4 of 141.0 kg (Vega); the files do not split it alike (the RB-Y1's
wheels 1.38 kg each with their motors in the base; the Vega's driven wheels 3.7 kg each; the AI Worker's drive links
3.80 kg and steering links 0.76 kg each), so they cannot give a drive module's mass alone.

| # | His words / what is to be built | Recommendation |
|---|---|---|
| 1 | "their own kinds of part": the kinds of a robot on wheels | **Two kinds added to the ten: "Wheeled base"** (the drive and steering modules: motor, gearbox, brake; the wheels and tyres; the casters; the chassis sensors; the motor-driver boards) **and "Lift column"** (its motor, screw or belt, guides and profile). The rest as the ten: arm, waist and neck joints and hands; a folding leg's joints as hip, knee and ankle joints by the maker's names (as decision B of batch 2b: joints named by their place); the battery; the boards; the head; the cables; the frame and shell, the remainder |
| 2 | **Open A:** a computer that sits in the base is in the kind "Torso boards and heat sink" | rename that kind **"Boards and heat sinks"** for every robot type (type 1's legend changes by one word); the body region says where each board sits |
| 3 | **Open B:** where the new kinds sit in the shared lists (his workbook) | one body region **"Base"** and one part group **"Wheels and wheel drives"** added to its sheet Lists, a backup first; the lift column in "Joint drives", body region "Torso" |
| 4 | the drive and steering modules and the wheels: their number and kind | from the maker (E9.1); not stated: by the base's kind (two driven wheels and two casters), labelled E |
| 5 | their mass | **sources first**: the makers of robot drive units (wheel motors with gearbox and brake, mass and torque) and of casters, and the three model files; then a mass per module proposed robot by robot (as E8.3), half to 1.5 times where estimated. Composition: a motor as a joint module's (copper winding, electrical steel, NdFeB magnets, gear steel, aluminium housing), the wheel's aluminium hub and polyurethane or rubber tyre (Plastics) |
| 6 | the lift column | its stroke from the maker; its mass from lifting-column makers' datasheets by stroke and load (**sources first**); aluminium profile, steel screw and guides, its motor as a joint module's |
| 7 | the battery in the base | as type 2's battery rows: cells from voltage × capacity (or the stated Wh) over the cells' Wh per kg, the pack from the pack's Wh per kg; body region Base. **Open C:** CASBOT W1's pack is LFP ("磷酸铁锂"), a cell type 2 has not: its own LFP cells (sources first); every other robot NMC as type 2 (E1.7e) |
| 8 | the chassis sensors | type 2's sensor rows by the maker's counts; ultrasonic sensors as the car list's "ultrasonic sensor"; collision sensors E |
| 9 | the joints of arms, waist, neck and folding legs | by their torque with E6.8's fit where the maker gives it (Vega, RB-Y1 by their model files; W-Bot; H2-D's arms 120 N·m; the R1's torso 304 N·m); hands and grippers as added joints |
| 10 | **Open D:** the frame and shell, the remainder, in a base that may hold steel or ballast (Vega's base 88 of 141 kg) | **sources first** on how the bases are built; its material the maker's where stated (AI Worker and RB-Y1 aluminium; H2-D aluminium, titanium, plastics; CASBOT W1 alloy and plastics); no material proposed before the sources |
| 11 | a template for robots with few figures and the 12 with none | **a wheeled template of their own, never the legged one**: as E7.4, from the wheeled robots whose makers state it: the joint modules' share of the robot mass (by torques: Vega, RB-Y1, W-Bot); the base's parts per robot mass; the battery energy per kg of robot from the 12 that state an energy (from 4.6 to 40 Wh/kg, median about 10.3, against the legged template's 14.67); the wheels by the most common base. Proposed with its numbers, as E7.4 was |
| 12 | the versions (E9.2, decided) | the AICO 2, RB-Y1 and R1-D in two versions each; the H2-D as its Flagship, the G1-D as its Ultimate; the register changed at the entry |
| 13 | **Open E:** the figures (type 2's pages hold both) | the robot drawn on 02's overview gets a base under its torso, a box on wheels, for "Wheeled base" and "Lift column", in two more colours of the same Tol scale; 01's table of type 2's robots shows the robots on wheels in sections of their own with their base and lift. Said in words here; drawn only on his yes |
| 14 | the order of work | this spec's yes → sources for points 5, 6, 7 (LFP) and 10 → a proposal of each robot's numbers (as E8.3) → the spec of the entry → tests first, then the code → his runs. Type 2's stock-and-flow draws switch to its parts when all 96 with a mass are in (Q2) |

**Decided:** Matthias, 2026-10-30, "Yes, agree E9.4": the 14 points as recommended, open A to E included: the kinds
"Wheeled base" and "Lift column" added to the ten; "Torso boards and heat sink" renamed "Boards and heat sinks" for every
robot type; the body region "Base" and the part group "Wheels and wheel drives" added to the shared lists' sheet Lists
(a backup first), the lift column in "Joint drives", body region "Torso"; the CASBOT W1 its own LFP cells, every other
robot NMC; the bases' material from sources first; the figures as point 13, drawn on his yes. Nothing built yet: by
point 14, the sources come first.

### E9.5 The sources for the wheeled base's parts (E9.4 points 5, 6, 7 and 10). Nothing proposed

Matthias, 2026-10-30: "Yes, start sources". Read on 2026-10-30: the makers' pages through four web-fetch reads (HTML
only) and Tente's two castor pages in the built-in browser myself (the weight read from the page's own data, the
cookie banner declined); the three model files of E9.1 by script. No PDF opened (each PDF found is named, not read).
Search engines' summaries only pointed to pages: none is used as a source, and a source known only from one is marked
"not read".

**Point 5, the drive and steering modules, wheels and casters**

| Source | What it states | Kind | Same kind, representative |
|---|---|---|---|
| ZLTECH, hub servo motors "for robot" (robotmotor.com, 8 product pages) | brushless, gearless, encoder, tyre rubber or PU; per motor: **4.5" 200 W, 5 / 15 N·m (rated / peak), "150kg/2sets", 2.9–3.0 kg; 6.5" 350 W, 6 / 18 N·m, 150 kg per pair, 3.75 kg; 6.5" 500 W, 10 / 30 N·m, 200 kg per pair, 4.85 kg (its text: 5.4); 8" 150 W, 5.5 / 16 N·m, "120kg/2pcs", 3.40 kg (its text: 3.725); 8" 250 W, 4 / 12 N·m, 100 kg per pair, 3.40 kg; 8" 350 W, 6 / 18 N·m, 150 kg per pair, 4.25 kg; 8" 800 W, 20 / 60 N·m, 300 kg per pair, 8.5 kg**; 15" pneumatic 800 W, 9.7 kg (outdoor). Brake: not stated. Conflicts on the pages: the voltage of the title against the table; two weights on two pages | maker, catalogue (design values) | yes: drive wheels of service, cleaning and delivery robots, two driven wheels carrying 100 to 300 kg, as the bases on two driven wheels (E9.4); the 15" outdoor wheel left out |
| UU Motor, 4" robot servo hub motor SVH4D (uumotor.com) | "Motor weight: 1.4kg", "Max load: 50KG" (its text: 35 kg), torques conflicting (20 / 50 N·m against "max torque 7N.m") | maker, catalogue | for the small robots (R1-D, Mantis, 30 to 50 kg); its torques not used |
| The model files (E9.1, by script) | Vega 1 Pro: driven wheels **3.7 kg** each (16 N·m), steering links 0.358 kg (6 N·m), casters 0.2 and 0.3 kg; AI Worker FFW-SG2: drive links **3.80 kg** each, steering links 0.755 kg; RB-Y1 A: wheels 1.378 kg each, their motors inside the base (60.08 kg) | maker's model | yes, the robots' own; the Vega's and the AI Worker's drive wheels agree with ZLTECH's 8" (3.40 to 3.73 kg) |
| ROBOTIS e-manual, DYNAMIXEL YM070-210-R051-RH (the AI Worker's wheel steering) | "Weight" 790 g, Ø70 × 71.1 mm, continuous 8.2, maximum 16.3 N·m, 51:1, frameless BLDC, 24 V, no brake | maker, datasheet | yes, the AI Worker's own steering actuator; the drive motor is not named |
| Pollen, Reachy's mobile base (the 2021 documentation) | "3x Omnidirectional wheels", "300W Max power", "Stall Torque: 13Nm", rated "5Nm, 115rpm"; Hall sensors and an IMU on each wheel; no motor mass | maker, spec | yes, Reachy 2's base (the current page: the same 25 kg and 80 kg payload) |
| Tente, swivel castors 75 mm (tente.com) | **Linea light 5920UAP075L51-10**: polyamide housing and body, injected PU tread, 100 kg (3 km/h), 200 kg static, **"Overall weight 0.18 kg"**; **Agila light 1470PAO075P40**: "light steel sheet" housing, polypropylene body, PU tread, 60 kg, **0.27 kg** | maker, catalogue | yes for the light bases (the Vega's casters 0.2 and 0.3 kg); **no castor read for the heavy bases** (CASBOT W1's "2+4" at 260 kg): RS, Fallshaw and Distrelec refused or sent nothing |
| Left out, not read | industrial AGV drive units (Diequa, Sumitomo, Honpine TYD: 60 to 3,000 kg per wheel); FRC swerve modules (competition robots); Honpine's steering hub motor (its page gone, 404) | — | not the same kind (vehicles for 0.5 to 3 t, or toys of competition), or not read |

**Point 6, the lift column**

| Source | What it states | Kind | Same kind, representative |
|---|---|---|---|
| ROBOTIS, AI Worker | lift "0 ~ 500 mm"; its lift actuator DYNAMIXEL **YM080-230-B001-RH: 890 g**, a motor with a "Spring applied brake", no gear, continuous 0.62 N·m; its model's lift link **17.9 kg** | maker, spec, datasheet, model | yes, a robot's own column; the mechanism around the motor (belt or screw, guides) not described |
| Oriental Motor, EL series (catalog.orientalmotor.com) | ball screw, 6 mm lead, brake; **EL605 50 mm: body 20.4 kg, moving parts 5.5 kg; EL610 100 mm: 22.1 / 5.7 kg; EL620 200 mm: 26.3 / 6.9 kg; EL630 300 mm: 30.5 / 8.1 kg**; "Max. Vertical Transportable Mass ~30 kg"; materials not stated | maker, catalogue | **in part**: an industrial column for at most 30 kg and 300 mm, built heavier than a robot's, and shorter than most of the robots' strokes (300 to 900 mm) |
| Phoenix Mecano, RK PowerLift | stroke "max. 500 mm" (its table: 650), 3,000 N; **no mass** | maker, catalogue | a medical column; no mass, so not usable |
| Left out, not read | Ewellix LIFTKIT (its pages now redirect to Schaeffler's linear-motion list; a summary's 21 kg not used) | — | not read |
| The makers' strokes (E9.1) | AI Worker 500, H2-D 460, RealBot-L2 300, Dual-Arm Lift 900, Feather 600, Mantis 550, TIAGo Pro 350 mm; CASBOT W1, G1-D one lift joint | makers | — |

**Point 7, LFP cells:** the project has them: "LFP cylindrical", its three cells (Antbatt 26650 3.2 Ah and 3.0 Ah,
Power-Sonic 18650; makers' datasheets, E1.7k) and its recipe, decided on 2026-10-26 (E1.7i). The CASBOT W1's page states
"磷酸铁锂" and 48 V 25 Ah, not its cells' format. Nothing new to read.

**Point 10, how the bases are built**

| Source | What it states | Kind |
|---|---|---|
| The makers (E9.1) | AI Worker "Aluminum, Plastic"; RB-Y1 exterior "Aluminum"; H2-D "Aerospace-Grade Aluminum, Titanium Alloy, and High-Strength Engineering Plastics"; CASBOT W1 "合金、工程塑料"; G2 Genie "100%车规级零部件" (no material) | makers, spec |
| Pollen, Reachy's mobile base (2021 documentation) | **"Aluminium, MJF 3D printed plastic parts, Steel"**; 25 kg; its battery "OlenBox M": "24V, 35Ah", **6.5 kg** (840 Wh, arith.; chemistry not stated) | maker, spec |
| The model files | the base's share of the robot: AI Worker 36.0 of 94.4 kg (its lift 17.9 kg more), RB-Y1 60.1 of 132.2 kg, Vega 88.4 of 141.0 kg; the files do not say what the base holds | makers' models |
| Not found | **no source states a steel frame or a ballast in a wheeled humanoid's base**; AMR chassis pages (a fabricator, a patent) known only from a search summary, about carts, not read | — |

**What the sources settle, and what not:**
- The drive wheels of a base on two driven wheels: a hub servo motor of 2.9 to 4.85 kg for 100 to 200 kg per pair,
  8.5 kg for 300 kg per pair (ZLTECH), 1.4 kg for a small robot (UU Motor); two models of the robots agree (3.7, 3.80 kg).
- Steering: one actuator read (ROBOTIS, 0.79 kg) and two models' steering links (0.36, 0.76 kg); no steering drive
  unit's datasheet read.
- Casters: 0.18 to 0.27 kg at 60 to 100 kg (Tente; the Vega's model 0.2 and 0.3 kg); heavy bases not covered.
- Lift column: a robot's own (AI Worker: a 0.89 kg motor, a 17.9 kg lift link) and an industrial one (Oriental Motor,
  20.4 to 30.5 kg, built for 30 kg); no robot column of 300 to 900 mm with a stated mass besides the AI Worker's model.
- The bases' material: aluminium and plastics by every maker who says, steel too in Pollen's, titanium in Unitree's; no
  ballast stated anywhere.
- LFP: settled by E1.7k.

### E9.6 Proposal: type 2's 43 robots on wheels, robot by robot (2026-10-30). Nothing entered

Matthias, 2026-10-30: "Propose the numbers". The method is E9.4's (agreed), on E9.5's sources, with the decisions of E9.2
and E9.3; everything else as type 2's batches (E7.5 points 1 to 13, E6.8's fit, E8.3). Where an input needs a choice
none of these made, it is **bold**. Read for it besides E9.5: ROBOTIS's e-manual for the AI Worker's other three
actuators (PH42-020-S300-R "340 [g]", XH540-V150-R "165 [g]", XH430-V210-R "82 [g]") and its gripper (RH-P12-RN
"500g"); the RB-Y1's grippers in its model (0.533 kg each). Numbers at the modes are Claude's arithmetic
(`wheeled_modes.py`, V99); the run draws every one from its min / mode / max.

| # | What | Proposal |
|---|---|---|
| 1 | **The robot's mass** | E9.2: the maker's the mode, ± 1 kg; **its model's the maximum where higher (AI Worker 94.42, RB-Y1 A 132.22, Vega 141.00 kg), as the H1's (E8.2)**; TIAGo Pro 79 / 80 / 95 (decided); Reachy 2 its "Up to 50 kg" 49 / 50 / 51; Torobo its maker's 120 (the register's 160 reported); the robots with no maker's mass the register's (the catalogue's, so labelled), ± 1 kg, or its range (VB1-I 60 / 65 / 70, VB2 65 / 70 / 75) |
| 2 | **Joint modules stated or by the torques** | Vega 1 Pro and RB-Y1: E6.8's fit at their models' limits, half to 1.5 times (E); the RB-Y1's neck its "Neck Joint Module", 1.5 kg × 2 (S). AI Worker: ROBOTIS's actuators, an arm 3 × 1.2 + 3 × 0.79 + 0.34 kg, its head 0.165 + 0.082 kg (S, ± 5 %). Reachy 2: Pollen's Orbita 2D 1.9 kg × 4 and Orbita 3D 0.95 kg × 3 (S). W-Bot: its page's knee 360, ankle 160, arm joints 60 N·m (14) by the fit; **its three hip joints at its knee's 360 N·m (E)**. Not used, a maximum only: H2-D's arms 120, the R1's torso 304, R1-D's shoulder 60, Mantis's 80 N·m |
| 3 | **The wheeled template** (E9.4 point 11) | **Joint modules 7.8 / 15.6 / 23.4 % of the robot mass**: the four with every joint (Vega 13.2 %, RB-Y1 13.9 %, AI Worker 14.3 %, Reachy 2 20.9 %), their mean, half to 1.5 times as E7.4 (the legged template: 40.4 %); **split as the four on average: waist 20.5 %, shoulders 38.3 %, elbows and wrists 33.6 %, head 7.6 %** (a folding leg's joints with the waist). **Battery 4.62 / 10.28 / 22.86 Wh per kg of robot**: the median of the 12 that state an energy, their least and their most, **the W-Bot's 40 left out of the maximum as the one outlier** (the legged template: 14.67). **Base: two driven wheels and two casters**, the most common of the bases stated (10 of 26). No lift column unless the maker states one |
| 4 | **Drive wheels** | their number by the maker (E9.1), the template's two where not stated; **each a hub motor by the robot's mass per driven wheel: up to 35 kg 1.4 kg (UU Motor); to 75 kg 3.75 kg (ZLTECH's 6.5" and 8", 3.40 to 4.25 kg); to 100 kg 4.85 kg; above 8.5 kg (ZLTECH's 800 W)**, half to 1.5 times (E). The models': Vega 3.7, AI Worker 3.80 kg (E); **Reachy 2 by its motors' torque (rated 5 N·m): ZLTECH's 4.5", 2.9 kg (E)**. **Inside: as a joint module (the G1's joint scaled, E7.5 point 3), its tyre among its plastics (E)**: a hub motor has no gears (ZLTECH: "gearless"), so its steel is overstated here and its other materials understated |
| 5 | **Steering** | per steered wheel 0.79 kg (ROBOTIS YM070-210-R051-RH: S for the AI Worker, E elsewhere, half to 1.5 times); the Vega's model 0.358 kg (E); inside as a joint module |
| 6 | **Casters** | two to a base of two driven wheels, four for CASBOT W1 ("2+4"); 0.27 kg each (Tente's steel-housed 75 mm, half to 1.5 times, E); the Vega's model 0.2 and 0.3 kg; **inside: steel 50 %, plastics the remainder (E: a steel housing, a polypropylene body, a PU tread; no source weighs them)** |
| 7 | **Lift column** | where the maker states one: AI Worker, CASBOT W1, Dual-Arm Lift, Feather, G1-D, H2-D, Mantis, RealBot-L2, TIAGo Pro. The AI Worker's model's 17.9 kg (E); **the others 19.9 % of the robot mass (the AI Worker's 17.9 of 90 kg), half to 1.5 times (E)**: Oriental Motor's industrial columns, 20.4 to 30.5 kg, lie within it for robots of 100 to 150 kg. **Inside: a motor of 0.89 kg as a joint module (ROBOTIS YM080-230-B001-RH: S for the AI Worker, E elsewhere), the rest steel 20 / 30 / 40 % (screw and guides) and aluminium the remainder (profile; E, no source weighs them)**. The catalogue's lifts of Y1 and Y2-P not used (second-hand; the template, as decided) |
| 8 | **Battery** | Stated: AI Worker 25 V × 80 Ah (2,040 Wh); ARI 24 V × 40 Ah (960); CASBOT W1 48 V × 25 Ah, LFP (1,200; decided); Feather 48 V × 50 Ah (2,400); G2 Genie 48 V × 34 Ah (1,652); H2-D 48 V × 30 Ah (1,440); RB-Y1 A 50 V × 25 Ah (1,250), M 50 V × 50 Ah (2,500); RealBot-L2 and -S2 48 V × 20 Ah (960); TIAGo Pro 36 V × 20 Ah (720; decided); W-Bot 2,400 Wh at its "最大电压48V"; **R1 Pro the R1's 48 V × 35 Ah (S for the R1, E for the Pro); Reachy 2 the 2021 base's 24 V × 35 Ah, its pack 6.5 kg (S for that base, E for Reachy 2); MagicBot D1 1,652 Wh at 48 V (E: its charger 54.75 V); G1-D its 9 Ah (upper body) and 30 Ah (base) at 48 V (E, as Unitree's H2-D): 1,872 Wh; RealBot-01 its 40 Ah at 48 V (E, as RealMan's S2 and L2): 1,920 Wh**. Every other robot the template. Packs from their energy over the pack's Wh per kg (E5.14), Reachy 2's stated; body region Base, the G1-D's 9 Ah pack Torso; cells NMC, CASBOT W1's LFP |
| 9 | **Boards** | E7.5 point 7, as each maker names: Jetson AGX Orin (G1, AI Worker, R1 Pro, RealBot-L2, -S2; Feather the middle of its three options), AGX Thor (Vega, ψ-SynRobot, as the H2 Plus's), two Orin NX (W-Bot), Intel boards (ARI, H2-D two, TIAGo Pro, Torobo), an AMD board (Reachy 2's Bedrock v3000, as an Intel board), CASBOT W1's i9 PC and RTX 4060 graphics board and RK3588; **G2 Genie's "500 TOPS (INT8)", "24*A78" as two AGX Orin-sized modules (E, my reading: an AGX Orin has 12 A78 cores); MagicBot D1's "Huawei R1, 500 TOPS" as one AGX Orin-sized module (E); RB-Y1's "dual-PC", "GPU-Equipped" as an Intel board and an AGX Orin-sized module (E); R1-D's two 8-core boards (E)**; the others one computer board (E). Motor drivers inside the joint and wheel modules, as type 2's joints |
| 10 | **Sensors** | E7.5 point 8, each by its kind, robot by robot below; **ultrasonic sensors as the car list's "ultrasonic sensor" (E)**. Left out (no kind yet, as force and touch sensors, E7.5 point 13): collision and low-obstacle sensors, screens and LED eyes, force and torque sensors |
| 11 | **Hands and grippers** | AI Worker's RH-P12-RN "500g" (S); CASBOT W1's gripper "500g" (S); RB-Y1 its model's 0.533 kg (E); **the grippers named without a mass (R1 Pro, R1-D, Reachy 2, TIAGo Pro, Dual-Arm Lift; Lanxin's three by their "gripping load") as the RH-P12-RN's 0.5 kg (E)**; hands of N joints as Fourier's per joint (E7.5 point 4): AGIBOT G1 6, Feather 6, ARMAR-7 4, Honda Avatar 16. Options left out (H2-D's, G1-D's, W-Bot's) |
| 12 | **Cables, shell, screws, frame** | E7.5 points 9 to 11: cables by the height (a range: its top); shell 11.5 %, screws; the frame the remainder, aluminium (the makers who say: AI Worker, RB-Y1, H2-D, CASBOT W1; E elsewhere); the H2-D's titanium as the H2's titanium parts (E); **Reachy 2's frame aluminium (its base "Aluminium, … Steel": the steel not weighed, E)** |
| 13 | **Versions** (decided, E9.2) | AICO 2-4 and 2-10, RB-Y1 A and M, R1-A5-D and R1-A7-D, each as often; H2-D Flagship; G1-D Ultimate |
| 14 | **Not in this proposal** | force, torque and touch sensors; collision sensors; screens; every option; the catalogue's lifts and second-hand masses (CUE7, Mantis); a ballast (no source) |

**Robot by robot** (the register's mass in brackets where it differs; S stated, E estimated, C the catalogue's;
base: driven wheels × kg, steered, casters):

| # Robot | Mass (kg) | Joints | Hands | Base | Lift | Battery (Wh) | Boards | Sensors |
|---|---|---|---|---|---|---|---|---|
| 13 AGIBOT A2-W | 229 / 230 / 231 (C) | template | — | 2 × 8.5, 2 casters | — | 2,364 (E) | one (E) | IMU (E) |
| 15 AGIBOT G1 | 149 / 150 / 151 | template (20 DoF) | 2 × 6 joints | 2 × 3.75, 2 casters (E) | — | 1,542 (E) | AGX Orin 64GB | 8 cameras (3 RGB-D, 5 fisheye), base RGB-D × 2, LiDAR, IMU (E) |
| 20 AI Worker FFW-SG2 | 89 / 90 / 94.42 | ROBOTIS's (S) | 2 × 0.5 (S) | 3 × 3.80, 3 steered | 17.9 kg | 2,040 (S) | AGX Orin 32GB | ZED Mini, D405 × 2, LiDAR × 2, IMU |
| 21 AICO 2-4 | 280 / 281 / 282 | template (2 × 7 arms) | — | 2 × 8.5, 2 casters (E) | — | 2,888 (E) | one (E) | LiDAR, IMU (E) |
| 21 AICO 2-10 | 394 / 395 / 396 | template | — | 2 × 8.5, 2 casters (E) | — | 4,060 (E) | one (E) | LiDAR, IMU (E) |
| 34 ARI | 59 / 60 / 61 (C) | template (14 DoF) | — | 2 × 1.4, 2 casters (E) | — | 960 (S) | Intel | head camera, D435i, 4 microphones, 2 speakers, IMU (E) |
| 35 ARMAR-7 | 119 / 120 / 121 (C) | template (2 × 8 arms, head 3, torso 2) | 2 × 4 joints | 3 × 3.75 (omni) | — | 1,233 (E) | one (E) | 2 hand cameras, binocular (E), IMU (E) |
| 40 Astribot S1 | 79 / 80 / 81 | template | — | 2 × 3.75, 2 casters (E) | — | 822 (E) | one (E) | IMU (E) |
| 41 Astribot T1 | 65 / 66 / 67 (C) | template | — | 2 × 1.4, 2 casters (E) | — | 678 (E) | one (E) | IMU (E) |
| 42 AD-01 | 119 / 120 / 121 (C) | template | — | 2 × 3.75, 2 casters (E) | — | 1,233 (E) | one (E) | IMU (E) |
| 49 Honda Avatar (155 cm, 101) | 109 / 110 / 111 | template (56 DoF) | 2 × 16 joints | 2 × 3.75, 2 casters (E) | — | 1,131 (E) | one (E) | binocular (E), IMU (E) |
| 60 CASBOT W1 | 259 / 260 / 261 | template (20 DoF) | 2 × 0.5 (S) | 2 × 8.5, 4 casters | 51.7 kg (E) | 1,200 (S, LFP) | i9 PC, RTX 4060, RK3588 | LiDAR, RGB-D × 4, stereo, 2 microphones |
| 68 CUE7 | 73 / 74 / 75 (C) | template | — | 2 × 3.75 (inverted pair) | — | 761 (E) | one (E) | IMU (E) |
| 82 Dual-Arm Lift | 156 / 157 / 158 | template (2 × 6 arms) | 2 × 0.5 (E) | 2 × 4.85, 2 casters (E) | 31.2 kg (E) | 1,614 (E) | one (E) | depth camera (E), IMU (E) |
| 86 Eggie | 44 / 45 / 46 (C) | template | — | 2 × 1.4, 2 casters (E) | — | 462 (E) | one (E) | IMU (E) |
| 92 Feather | 104 / 105 / 106 | template (23 DoF) | 2 × 6 joints | 3 × 1.4, 3 steered (E: its "6 base" joints) | 20.9 kg (E) | 2,400 (S) | AGX Orin (E) | ZED, 4 microphones, speaker, IMU (E) |
| 104 G1-D Ultimate | 89 / 90 / 91 | template (19 DoF) | — | 2 × 3.75, 2 casters (E) | 17.9 kg (E) | 1,872 (S, E) | one 8-core (E) | binocular, 2 wrist cameras, LiDAR, 2 depth cameras, IMU (E) |
| 105 G2 Genie (55) | 184 / 185 / 186 | template (25 DoF) | — | 4 × 3.75, 4 steered | — | 1,652 (S) | two AGX Orin-sized (E) | stereo, 3 fisheye, 3 RGB-D, 2 LiDAR, 8 ultrasonic, IMU, 4 microphones, speaker |
| 122 H2-D Flagship | 119 / 120 / 121 | template (20 DoF) | — | 2 × 3.75, 2 casters (E) | 23.9 kg (E) | 1,440 (S) | Intel i5, i7 | binocular, 2 wrist cameras, LiDAR, depth camera, 2 ultrasonic, microphones, speaker, IMU (E) |
| 179 MagicBot D1 | 149 / 150 / 151 | template (25 DoF) | — | 4 × 3.75, 4 steered | — | 1,652 (S, E) | one AGX Orin-sized (E) | RGB, stereo, 3 fisheye, 2 RGB-D, 2 LiDAR, 3 ultrasonic, microphones, 2 speakers, IMU (E) |
| 184 Mantis Standard | 49 / 50 / 51 (C) | template (22 DoF) | — | 4 × 1.4 (omni, E) | 9.9 kg (E) | 514 (E) | one (E) | IMU (E) |
| 200 Moz1 | 69 / 70 / 71 (C) | template (26 DoF) | — | 4 × 1.4 (omni, E) | — | 719 (E) | one (E) | IMU (E) |
| 230 Phoenix Gen 8 | 69 / 70 / 71 (C) | template | — | 2 × 1.4, 2 casters (E) | — | 719 (E) | one (E) | IMU (E) |
| 247 R1 Pro (96) | 125 / 126 / 127 | template (26 DoF) | 2 × 0.5 (E) | 3 × 3.75, 3 steered (the R1's) | — | 1,680 (S, E) | AGX Orin 32GB | ZED 2, D435i × 2, 5 cameras, LiDAR, IMU |
| 248 R1-A5-D (52) | 29 / 30 / 31 | template (18 DoF) | 2 × 0.5 (E) | 4 × 1.4 (E) | — | 308 (E) | two 8-core (E) | binocular, LiDAR, 4 microphones, 2 speakers, IMU (E) |
| 248 R1-A7-D (52) | 31 / 32 / 33 | template (22 DoF) | 2 × 0.5 (E) | 4 × 1.4 (E) | — | 329 (E) | two 8-core (E) | the same |
| 251 RB-Y1 A | 130 / 131 / 132.22 | its model's 20, neck 2 × 1.5 | 2 × 0.533 (E) | 2 × 3.75, 2 casters (E) | — | 1,250 (S) | Intel, AGX Orin-sized (E) | IMU (E) |
| 251 RB-Y1 M | 169 / 170 / 171 | the same | 2 × 0.533 (E) | 4 × 3.75 | — | 2,500 (S) | the same | IMU (E) |
| 252 Reachy 2 | 49 / 50 / 51 | Pollen's Orbita (S) | 2 × 0.5 (E) | 3 × 2.9 (omni) | — | 840 (S, E), pack 6.5 kg | AMD (E) | binocular, depth camera, LiDAR, 3 IMU |
| 253 RealBot-01 | 124 / 125 / 126 | template (21 DoF) | — | 2 × 3.75, 2 casters (E) | — | 1,920 (S, E) | one (E) | 5 depth cameras, 3 fisheye, LiDAR, 2 IMU, microphones |
| 254 RealBot-L2 | 119 / 120 / 121 | template (17 DoF) | — | 2 × 3.75, 2 casters (E) | 23.9 kg (E) | 960 (S) | AGX Orin 64G | stereo, 2 RGB-D, IMU (E) |
| 255 RealBot-S2 | 124 / 125 / 126 | template (20 DoF) | — | 4 × 1.4, 4 steered | — | 960 (S) | AGX Orin 64G | stereo, 2 fisheye, 2 RGB-D, 2 LiDAR, IMU (E) |
| 295 TIAGo Pro (80) | 79 / 80 / 95 | template (23 DoF) | 2 × 0.5 (E) | 4 × 1.4 (mecanum) | 15.9 kg (E) | 720 (S) | Intel i5 | RGB-D, 2 LiDAR (2D), 4 microphones, 2 speakers, IMU |
| 307 Torobo (160) | 119 / 120 / 121 | template (2 × 7, waist 3, neck 3) | — | 4 × 1.4 (omni, E) | — | 1,233 (E) | Intel (E) | IMU (E) |
| 312 VB1-I | 60 / 65 / 70 (C) | template (2 × 6 arms) | 2 × 0.5 (E) | 2 × 1.4, 2 casters (E) | — | 668 (E) | one (E) | depth camera (E), LiDAR, IMU (E) |
| 313 VB2 | 65 / 70 / 75 (C) | template (2 × 7 arms) | 2 × 0.5 (E) | 4 × 1.4 (omni) | — | 719 (E) | one (E) | the same |
| 314 Vega 1 Pro | 134 / 135 / 141.00 | its model's 23 | — | 2 × 3.7, 2 × 0.358 steered, casters 0.2 and 0.3 (its model) | — | 1,387 (E) | AGX Thor | stereo, 2 LiDAR, 4 RGB cameras, IMU (E) |
| 315 VersaBot VB-1 | 74 / 75 / 76 (C) | template (2 × 6 arms) | 2 × 0.5 (E) | 4 × 1.4 (omni) | — | 771 (E) | one (E) | depth camera (E), LiDAR, IMU (E) |
| 318 W-Bot | 59 / 60 / 61 | its page's torques, 19 | — | 2 × 1.4, 2 casters (E) | — | 2,400 (S) | 2 × Orin NX 16GB | D435i, D455, LiDAR, IMU (E) |
| 335 Y1 | 149 / 150 / 151 (C) | template | — | 2 × 3.75, 2 casters (E) | — | 1,542 (E) | one (E) | IMU (E) |
| 336 Y2-B | 84 / 85 / 86 (C) | template | — | 2 × 3.75, 2 casters (E) | — | 874 (E) | one (E) | IMU (E) |
| 337 Y2-P | 94 / 95 / 96 (C) | template | — | 2 × 3.75, 2 casters (E) | — | 976 (E) | one (E) | IMU (E) |
| 340 YMBot D | 99 / 100 / 101 (C) | template | — | 2 × 3.75, 2 casters (E) | — | 1,028 (E) | one (E) | IMU (E) |
| 341 YMBot D2 | 149 / 150 / 151 (C) | template | — | 2 × 3.75, 2 casters (E) | — | 1,542 (E) | one (E) | IMU (E) |
| 342 YMBot D4 | 99 / 100 / 101 (C) | template | — | 2 × 3.75, 2 casters (E) | — | 1,028 (E) | one (E) | IMU (E) |
| 349 ψ-SynRobot | 64 / 65 / 66 (C) | template (waist 2, neck 2) | — | 2 × 1.4, 2 casters (E) | — | 668 (E) | AGX Thor (E) | 4 RGB-D, 3 fisheye, IMU (E) |

**What it gives at the modes** (Claude's arithmetic, `wheeled_modes.py`, V99): joint modules 10.7 to 31.2 % of the
robot mass (the template's 15.6 %; the W-Bot's 31.2 % by its stated torques, its hips E); the base's wheels, steering and
casters 3.3 to 18.2 kg; the lift columns 9.9 to 51.7 kg; the battery packs 1.9 to 24.8 kg. **The frame before cables,
boards and sensors** stays above zero for every robot: least the AI Worker's, 23.5 % of its mass (its lift and battery
large), then the W-Bot's 26.5 %, the G1-D's 30.9 %, Feather's 31.5 %; without a lift most lie at 53 to 62 %. That
remainder is the frame and the base's chassis, in aluminium by every maker who says: **the largest part of a robot on
wheels and the least known**; a ballast or a steel chassis, which no source states, would sit in it.

**Agreed:** Matthias, 2026-10-30, choosing the answer offered: "Yes, agree E9.6" (points 1 to 14 and the robot-by-robot
table, with their estimates). Not entered: the entry (the wheeled kinds of part, the shared lists' region and group,
the register's versions and masses, type 2's builder, tests first) is a step of its own, for his yes.

### E9.7 Spec: the entry of the 43 robots on wheels (2026-10-30). Nothing built

Matthias, 2026-10-30: "Spec the entry". It enters what was agreed: E9.2 ("Yes, all five"), E9.3 ("Yes, 79 / 80 / 95"),
E9.4 ("Yes, agree E9.4", A to E) and E9.6 ("Yes, agree E9.6"). Found in the code for it (V100): 02 takes type 2's
draws for stock-and-flow from its parts by itself once no robot of it with a mass is left (Q2), so this entry makes that
switch (the Xialan S0 has no mass); 02 has one cell recipe for every robot taken apart ("NMC cylindrical"); every
battery row is written to the body region "Torso"; joints go to their kind by their name (`JOINT_KIND`); the magnets'
heat groups are Knees, Hips, Waist, Ankles, Shoulders, Elbows and wrists; the kind name "Torso boards" is in 173 cells of
type 1's parts file, 326 of type 2's, and about 120 places in the builders.

| # | What is built (his words: the agreed points) | Where |
|---|---|---|
| 1 | **The kinds** (E9.4 points 1, 2): "Wheeled base" and "Lift column" added, the kind "Torso boards and heat sink" renamed "Boards and heat sinks" for every robot type (its short name in the parts files "Torso boards" → "Boards"; type 1's parts file changes in that column only, its numbers not) | `01_schemas.py` `KINDS`, `KIND_HOLDS`, `JOINT_KIND` ('wheel', 'steering' → base; 'lift' → lift); the three builders |
| 2 | **Their place in the shared lists** (E9.4 point 3, his workbook): the body region "Base" and the part group "Wheels and wheel drives" added to the sheet Lists, with what each holds; a backup first; `SHARED_LISTS.md` says so | `data/researched/shared_lists.xlsx`; 02's `KIND_PART_GROUP`, `KIND_BODY_REGION` (base → Wheels and wheel drives, Base; lift → Joint drives, Torso) |
| 3 | **A robot on wheels in the shared machinery**: a block's driven wheels (number, hub motor kg), steered wheels, casters, lift column, the battery's body region, its cells' chemistry; the hub, steering and lift motors written as rows of the sheet Joints (inside as a joint module, E9.6 points 4, 5, 7), the casters' and the column's other parts as rows of the sheet Parts with their shares (steel 50 % / plastics the remainder; steel 20 / 30 / 40 % / aluminium the remainder); the wheeled template as a block of its own, its Constants named "… , on wheels" (joint modules 0.078 / 0.156 / 0.234; battery 4.62 / 10.28 / 22.86 Wh per kg; lift column 0.0995 / 0.199 / 0.2985 of the robot mass), its split averaged over the four (E9.6 point 3) | `tools/parts_taken_apart.py` (`block()`, `robot_rows()`, a wheeled `template_block`) |
| 4 | **The 43 robots** (E9.6, 46 blocks with the versions), in the register's order, every source's code in the sheet Sources; the hub motor of each base by its class (E9.6 point 4); the ultrasonic sensors through the car list's "ultrasonic sensor" | `tools/2_full_scale_general_purpose_ai_research/make_parts_taken_apart.py` |
| 5 | **LFP** (E9.4 C): a robot's cells by its own chemistry: the CASBOT W1's "LFP cylindrical" (its cells' Wh per kg from the sheet Cells' LFP cells, its recipe E1.7k), every other robot as now | 02's `CELL_RECIPE` per robot, the parts machinery |
| 6 | **The register**: type 2's 43 taken apart (the versions joined as now), the decisions E9.2, E9.3, E9.6 in its sheet of decisions; its masses unchanged, the makers' in the parts file and the register's reported (as E8.2). After it: 96 of type 2's 97 taken apart, the Xialan S0 "not drawn: no mass" | `tools/make_humanoid_register.py` |
| 7 | **01's checks**: check 18 knows two templates per type, the legged (E7.4) and the wheeled (E9.6): a template robot's shares equal its own template's; every robot on wheels has at least one driven wheel; a lift column only where its block names one | `01_schemas.py` |
| 8 | **01's table of type 2's robots** (E9.4 point 13): the robots on wheels in sections of their own ("On wheels, every joint from its maker", "On wheels, joints a share of the robot's mass"), each row its base (driven wheels, steered, casters) and its lift; its overview box: "96 of its 97 robots …" | `01_schemas.py` |
| 9 | **02's pages** (E9.4 point 13): the twelve kinds in every legend and stacked bar; the robot drawn on type 2's overview gets, beside its feet, a base on wheels with a lift column above it, so that both new kinds have a place; type 1's drawing unchanged | `01_schemas.py` (the drawing, one copy), `02_composition.py` |
| 10 | **Tests first** (each failing before its code): the 46 blocks (masses, hub classes, steering, casters, lifts, batteries, LFP for CASBOT W1 only, versions, hands and grippers); type 1's file unchanged but the one renamed column; the register (96 taken apart, none with a mass left); 02 (each robot as often, a version half as often; LFP cells only in CASBOT W1's draws; type 2's stock-and-flow from its parts); 01 (twelve kinds; check 18 with two templates; the table's pages; no label over another) | `tests/` |
| 11 | **Sandbox** before his runs: both builders, the register, 01's pages of type 2 and 02 whole at 2,000 draws into Claude's scratch folder; no remainder below zero; the pages looked at | scratch only |
| 12 | **Documents**: README, METHODOLOGY (type 2 on wheels, the twelve kinds), SHARED_LISTS.md, EVIDENCE E9.8 (where each decision landed, as E8.4), VERIFICATION, HANDOVER with his runs by full path | `documentation/claude/`, `README.md` |
| 13 | **Not in** (as E9.6 point 14): force, torque, touch and collision sensors; screens; options; the catalogue's lifts and second-hand masses; a ballast. Commit and push on his word | — |

**Open points, each with my recommendation:**
- **A. The magnets of the wheel, steering and lift motors** need a heat group (sheet MagnetGrades, E2.11). No source
  grades a robot's hub motor. Recommended: **the hub motors as the hips** ("carry the body": SH 50 %, UH 40 %, EH 10 %),
  **the steering and lift motors as the waist** ("moves often": SH 60 %, UH 40 %); no new group.
- **B. Type 2's drawing holds robots on legs and on wheels.** Recommended as point 9: the body as now, and beside its feet a
  base on wheels with its lift column, labelled by kind like the joints; the figure's text says which robots have which.
- **C. The two new colours.** Recommended: two colours of Paul Tol's discrete rainbow not yet used, chosen so that no two
  neighbouring kinds look alike; the ten colours unchanged (type 1's figures keep theirs); shown on the sandbox's pages
  first.
- **D. The backup of the shared lists** (his workbook; Claude's scratch folder is emptied overnight, so not there).
  Recommended: a copy beside it, `data/researched/shared_lists_before_wheels_2026-10-30.xlsx` (data, not in git),
  removed only on his word.

### E9.8 The entry: what each point of E9.7 landed in (2026-10-30, on "Yes, build it")

Matthias, 2026-10-30: "Yes, build it" (E9.7's points 1 to 13 and its open points A to D with their recommendations).
Builder: `tools/2_full_scale_general_purpose_ai_research/make_parts_taken_apart.py`; machinery: `tools/parts_taken_apart.py`;
register: `tools/make_humanoid_register.py`. Checks: VERIFICATION.md V101. Nothing committed.

| Point of E9.7 | Where it landed |
|---|---|
| 1, the kinds | `01_schemas.py` `KINDS` (twelve: 'base' "Wheeled base", 'lift' "Lift column", last), `PART_KIND`, `KIND_HOLDS`, `JOINT_KIND` ('wheel', 'steering' → base; 'lift' → lift); "Boards and heat sinks", its short name "Boards" in the three builders; type 1's file differs from the one on disk in that column only (173 cells, V101) |
| 2, the shared lists | his `shared_lists.xlsx`, sheet Lists: ('Part group', 'Wheels and wheel drives', …) before 'Mixed', ('Body region', 'Base', …) before 'Whole body'; every other sheet and row unchanged (V101); `SHARED_LISTS.md`; 02's `KIND_PART_GROUP`, `KIND_BODY_REGION` |
| 3, the machinery | `tools/parts_taken_apart.py`: `block()`'s battery region, cells' recipe, averaged template and lift column; `robot_rows()`; the sheet Shares' rows "Casters" (C45 steel 50 %, plastics the remainder) and "Lift column: aluminium profile, steel screw and guides"; the builder's `wheeled()`, `on_wheels_own()`, `hub_motors()`, `steering()`, `lift_motor()`, `casters()`, `grippers()`, `hands()`, `WHEELED_AVERAGE_JOINTS` and the three Constants "…, on wheels" |
| 4, the 43 robots | 46 blocks in the register's order (`GENERATED`, 102 in all); 45 source codes added to the sheet Sources (AGA2 … ORM); the base's ultrasonic sensors through the car list's "ultrasonic sensor" |
| 5, LFP | the CASBOT W1's cells row grade 'LFP cylindrical'; 01's `CELL_MATERIAL` grade rule; 02's `Shared.cell_draws(recipe)`: one LFP cell of the sheet Cells drawn per draw, its elements by the LFP recipe; its pack its cells times the NMC packs' pack-to-cell ratio (decided, below) |
| 6, the register | `TAKEN_APART[2]`: the 43 added (versions joined by "; "); its sheet Type 2: 96 "drawn: its own parts", the Xialan S0 "not drawn: no mass stated" |
| 7, 01's checks | check 18 by each template's label (`template_of()`, two templates in one file); `TEMPLATE_OUTSIDE` adds wheel, steering, lift; `template_quantity()` takes the numbers on wheels; a robot on wheels without a drive wheel, and a lift column without its lift motor or the reverse, are faults (tests `test_a_robot_on_wheels_with_no_drive_wheel`, `test_a_lift_column_and_its_motor_come_together`) |
| 8, 01's table | the sections "On wheels, every joint from its maker" and "On wheels, joints a share of the robot's mass"; the column Base in plain words (`base_words()`); ‡ for a lift column (`LIFT_MARK`); the layout `T_WHEELS`; the overview box "96 of its 97 robots …" and "Its draws for stock-and-flow from its parts: every robot with a mass is taken apart." |
| 9, the drawing | `draw_kinds()`: the body as before and, beside its feet, a base on wheels (F) and a lift column (G) where the type has them; type 1's drawing unchanged |
| 10, tests first | `tests/test_make_parts_taken_apart.py` `TestTypeTwoOnWheels`; `tests/test_parts_taken_apart.py` `TestTypeTwoOnWheels`; `tests/test_schemas.py` (the wheeled fixtures, the table, the drawing); `tests/test_make_humanoid_register.py` |
| 11, sandbox | scratch only, 2,000 draws (V101) |
| 12, documents | README, METHODOLOGY ("Robot type 2 part by part", point 2c; check 18; the pages), SHARED_LISTS.md, this section, V101, HANDOVER |
| 13, not in | as E9.6 point 14 |
| A, heat groups | the hub motors 'Hips', the steering and lift motors 'Waist' |
| B, the drawing | as point 9 |
| C, the colours | Wheeled base '#BA8DB4', Lift column '#42150A' (Paul Tol's discrete rainbow, not used before); the ten unchanged |
| D, the backup | `data/researched/shared_lists_before_wheels_2026-10-30.xlsx`, waiting for his word to remove it |

**Also found at the entry** (each a consequence of an agreed point, none a new decision):
- **The lift column's steel 15 / 30 / 45 %, not E9.6 point 7's 20 / 30 / 40 %:** 01 refused 20 / 40 as an estimate (E)
  narrower than half to 1.5 times its mode; widened to the rule, the mode unchanged.
- **The AI Worker's voltage 25.5 V, not 25 V:** its maker states "25V, 80Ah (2,040Wh)"; 25 × 80 = 2,000 Wh, so the
  voltage is the stated energy over the stated capacity, as the sources text says.
- **The Unitree G1-D Ultimate's two batteries ("9Ah" and "30Ah") as one pack of 39 Ah at 48 V, in the base,** labelled
  "S, E" (its voltage Unitree's H2-D's, E9.6 point 8).
- **'Battery energy per kg of robot, on wheels' labelled E,** not "S, E": no one source states it (the median of 12).
- **The Vega 1 Pro's casters 2 × 0.25 kg** (its model's 0.2 and 0.3 kg as one figure, half to 1.5 times).
- **A robot on wheels' hands or grippers count one joint each for its encoders and connectors,** as batch 1's do
  (`template()`); the first build counted a pair as one (the AgiBot G1 46 encoders instead of 48; caught by the
  sandbox's table, test `test_encoders_count_each_hand_and_wheel`).
- **01's overview, "Open:"** now says type 2's last robot has no mass yet (it said "robot type 2's other robots").
- **01's small test file** still wrote the old kind "Torso boards" in three rows: now "Boards".

**The CASBOT W1's battery pack with LFP cells** (found at the entry; decided below). Its pack has no mass from its maker, so 02
takes it as its energy over the shared 'Battery pack, Wh per kg (packs not weighed)', 109.3 / 164 / 232.5 Wh/kg, a
figure of NMC packs; its cells are LFP, 117.8 to 125.6 Wh/kg (the sheet Cells' three LFP cells). The pack then weighs
less than its own cells: 7.2 kg against 9.9 kg at the medians, below them in 98.0 % of 2,000 draws (V101), so its
housing, the remainder, falls below zero and 02 stops ("robot type 2: Ni is below zero in 5 draws"). Recommended: for
a pack with no mass whose cells are not NMC, the pack its cells times the NMC packs' pack-to-cell ratio in the same
draw (the NMC cells' Wh/kg over the pack's Wh/kg, 1.45 at the median, never below 1 since the NMC cells' least, 232.5,
is the packs' most): 14.3 kg at the median, 84 Wh/kg, its housing as an NMC pack's in proportion. The other way:
PACK_CELLS_ONLY for it (no housing, its cells alone).

**Decided** (Matthias, 2026-10-30: "Ratio, as recommended"), built after his 02 run of 11:53 had ended (it stopped on
this fault and wrote nothing): `02_composition.py`, the battery step: a pack with no mass whose cells are not
'NMC cylindrical' weighs its cells times the NMC cell's Wh/kg over 'Battery pack, Wh per kg (packs not weighed)', both
of the same draw; `tools/parts_taken_apart.py`: such a pack's row says so (`PACK_BY_RATIO`, its sources "; its cells
not NMC (E9.8)"), and a cells row of another recipe says its cells' Wh/kg is a cell of its recipe in the sheet Cells
(`CELL_OF_RECIPE`; every NMC row's text unchanged). Only the CASBOT W1's three cells change in type 2's file. Checks:
V102.

## E8. Each robot of type 2 its own composition: research, batch 2b (2026-10-30). Nothing entered

Matthias, 2026-10-30: "Yes, start batch 2b" (the sources of the 27 robots of type 2 not on wheels and not yet taken
apart, nothing changed while his run of 02 goes). Read on 2026-10-30: the makers' pages through six web-fetch reads
(HTML text only, no PDF opened) and, where those got no text (script-rendered, refused, rate-limited), in the built-in
browser myself; two spec pictures read myself (Tien Kung 3.0, Walker Tienkung); the makers' model files through
GitHub's interface, their masses summed and their joints' limits listed by script. Nothing is entered.

### E8.1 Robot by robot: what the makers state

The register's height and mass in brackets; **bold** where the maker's differs or where the robot does not stand on legs.

| # | Robot (the register) | What the maker states | Source | Kind |
|---|---|---|---|---|
| 216 | Omni, X-Humanoid (**~165 cm, ~55–75 kg**) | "天工Omni": **"135cm/39.5kg"**, "小型全尺寸科研底座" (a small full-size research platform); 31 DoF ("腿部x6，手臂x7，腰部x3，颈部x2"); "2070 TFLOPS" domain controller (flagship); depth camera, LiDAR, IMU; dexterous hands optional. Battery, torques, materials: not stated | x-humanoid.com/detail/omni.html | maker, spec |
| 221 | OPTIMUS GEN 3, Tesla (180 cm, 52 kg) | Tesla's page: Optimus "a general purpose, bi-pedal, autonomous humanoid robot"; no figures. E3: no maker's page with figures; AI Day 2022 (second-hand) | tesla.com/SI (from /AI) | maker, no figures |
| 222 | Optimus Gen2, Tesla (173 cm, 56 kg) | as 221 | as 221 | maker, no figures |
| 223 | OPTIMUS V2.5, Tesla (176.5 cm, 55 kg) | as 221 | as 221 | maker, no figures |
| 224 | Orca, Cyan Robotics (160 cm, 50 kg) | no maker's site (the catalogue gives none) | — | none |
| 229 | Phoenix, Sanctuary AI (170 cm, 70 kg) | named once ("the same task was executed on both Phoenix and a Franka arm"); no figures. A "17-DOF … hydraulic hand" is not said to be Phoenix's | sanctuary.ai/milestones, /product | maker, no figures |
| 232 | PHYBOT M1, PHYBOT (172 cm, 60 kg) | the site shows its logo only, no text, no links | phybot.tech | maker, no figures |
| 244 | Qinglong V3.0, OpenLoong (165 cm, **75 kg**) | the site names "“青龙”全尺寸通用人形机器人", open source, no figures, no "3.0". Its model `AzureLoong.urdf` (OpenLoong's GitHub): **86.14 kg**, 31 joints: hip roll 320, yaw 160, pitch 396, knee 396, ankles 58.5 × 2 N·m; waist pitch and roll 315, yaw 121; arms 80, 80, 58, 58, 11.5 × 3; head 26 × 2 | openloong.net; github.com/loongOpen/loong_base (`model/AzureLoong.urdf`) | maker, no figures; maker's model |
| 256 | REEM-C, PAL Robotics (165 cm, 80 kg) | "165 cm", "80kg", "68 DoF"; "Battery autonomy: 3h walking / 6h stand-by"; "Torque sensors: In ankles and wrists"; hand payload 1 kg; a legacy robot ("Our first humanoid, conceived in 2013"). Torques, battery energy, computers, materials: not stated. Its model in PAL's repository as xacro, not expanded | pal-robotics.com/robot/reem-c; github.com/pal-robotics/reemc_robot | maker, spec; maker's model (xacro) |
| 265 | Robotera L7 (171 cm, 65 kg) | "1.71 m"; "重量(不含灵巧手）65 KG" (without hands); "总自由度 (含灵巧手）55" (neck 2, arms 7 × 2, waist 3, legs 6 × 2, hands 12 × 2); "膝关节峰值扭矩 400 N · m"; "电池容量 60 V 15 Ah" (900 Wh, arith.); "80 TOPS (X86)+275 TOPS (Orin)"; depth camera, 3D LiDAR, microphone array and speaker. Its hand **XHAND 1: "重量 1100g"**, 12 active joints, gear-driven ("全直驱"), five fingertip tactile arrays. (Robotera's model file on GitHub is of its STAR1, another robot) | robotera.com/#/product/L7, /#/product/XHAND (in the browser) | maker, spec |
| 271 | SE01, EngineAI (**180 cm**, 80 kg) | **"170CM Height"**, "32pcs Total DOF"; "6自由度灵巧手" (hands of 6 DoF; elsewhere "5指"); its joints "行星、谐波、直线" (planetary, harmonic, linear), no torques; battery "1000 mAh", "2hours" (no voltage); "激光雷达＋深度摄像头＋红外摄像头", "RGBD", "扬声器×2", IMU, a force-control sensor; "航空级铝材机身" (aerospace aluminium). Mass: not stated. EngineAI's model files are of its PM01 and T800, not the SE01 | engineai.com.cn/product-se01.html; en.engineai.com.cn | maker, spec |
| 272 | Sean, Zeroth Robotics (155 cm, 45 kg) | **not on Zeroth's site** (its products: M1 EDU, a 50 cm desktop robot; W1; Jupiter, no figures in text) | zeroth0.com (in the browser) | maker, not listed |
| 276 | Songxing, Siasun (165 cm, 85 kg) | no humanoid on Siasun's sites (industrial, mobile, special, healthcare robots) | en.siasun.com, siasun.com | maker, not listed |
| 285 | Superman, Unitree (170 cm, 45 kg) | **no robot of that name on Unitree's site** (its list: As2 … H2-X, H2, H1 / H1-2, G1+, G1, R1, …) | unitree.com | maker, not listed |
| 290 | TALOS, PAL Robotics (175 cm, 95 kg) | "175 cm", "95 kg"; "Full Toque sensors feedback in all joints" (but head, wrists, grippers); force/torque sensors in wrists and ankles, IMU, encoders, temperature; EtherCAT, 2 kHz; "1,5h (walking)"; 6 kg per arm. Torques, battery energy, computers, materials: not stated; a datasheet link not opened. A model file of TALOS (LAAS-CNRS's, from PAL's description): 93.34 kg, its torques: torso 200 × 2, head 8, 4; arms 100, 100, 70, 70, 20, 8, 8; legs 100, 160, 160, 300 (knee), 160, 100; grippers | pal-robotics.com/robot/talos; github.com/stack-of-tasks/talos-data (`urdf/talos_full_v2.urdf`) | maker, spec; a user's model, second-hand |
| 294 | THEMIS V2, Westwood (160 cm, **32 kg**) | Westwood's site down (Cloudflare 522, twice). Its GitHub: "TH02-A7 is the newest and only model of THEMIS that is beeing mass produced", "7-DoF arms" and its "7-DoF three-finger end-effector" EN02; the model `TH02-A7-FULL.urdf` **37.92 kg**, 44 joints, **no torque limits** (all 0) | github.com/Westwood-Robotics/THEMIS-Simulation-Model | maker's model |
| 297 | TianGong Ultra, X-Humanoid (180 cm, 55 kg) | **no page** (the site lists 天工3.0, 天轶2.0, 天工Omni only) | x-humanoid.com | maker, not listed |
| 298 | Tianzhen Z1, Tlibot (167 cm, 45 kg) | **not on Tlibot's list** (天灵L3 in four versions, T1) | tlibot.com/cpzx/6.html | maker, not listed |
| 299 | Tien Kung 2.0, X-Humanoid (170 cm, ~70–90 kg) | no page on the site. X-Humanoid's model `tiangong2.0_pro_urdf.urdf`: 67.96 kg, 30 joints: hip roll 235, pitch 330, yaw 235, knee 330, ankles 55 × 2; waist 91; head 6.3 × 3; arms 91, 95, 35, 35, 24, 6.3, 6.3 | github.com/Open-X-Humanoid/TienKung_URDF | maker's model |
| 300 | Tien Kung 3.0, X-Humanoid (**169 cm, 62 kg**) | its parameter picture: **"身高：170cm 体重：64.5kg"**; "电池数据：15Ah+3Ah" (hot-swappable; no voltage); "最大关节扭矩400Nm"; "总自由度*31 / 头*2 / 腰*3 上肢*14 / 下肢*12", hands optional; "高性能主控4.8G主频", "高算力模组2070tops"; "深度相机+激光雷达+高精度IMU"; CAN FD / EtherCAT | x-humanoid.com/detail/jstg.html (its picture, read myself) | maker, spec |
| 302 | TLIBOT T1, Tlibot (160 cm, 43 kg) | "整机重量 43Kg（含电池，不含皮肤）"; "本体41个自由度（不含灵巧手）" (head 5, arms 9 × 2, waist 4, legs 7 × 2); "髋关节450Nm；膝关节281Nm；脚踝关节148Nm"; "电池 1110Wh"; payload "大于100Kg". Height, computers, sensors, materials: not stated | tlibot.com/product_detail/36.html | maker, spec |
| 307 | Torobo, Tokyo Robotics (166 cm, **160 kg**; form "not stated") | **"approx. 120 kg"**, "1615 mm"; "7-axis dual arms, 3-axis waist …, 3-axis neck …, and 4-axis undercarriage (**omni-directional mobile base**)"; torque sensors in arms and waist; "Up to approx. 3 hours"; one PC, an optional second with an Nvidia RTX 4070 (5070 elsewhere on the page); its hand option "Approx. 2 kg", 12 actuated joints | robotics.tokyo/technologies/torobo, /hand | maker, spec |
| 312 | VB1-I, Lanxin (~165 cm, ~60–70 kg; form **"legs"**) | "Driving mode: **Dual-wheel differential motor**", 700 × 610 × 1650 mm, arms of 6 joints, "2~3h"; mass not stated | lanxinrobotics.com/humanoid-robots/vb1-i | maker, spec |
| 313 | VB2, Lanxin (~170 cm, ~65–75 kg; form **"legs"**) | "Driving mode: **Four-wheel omnidirectional wheel**", 580 × 480 × 1700 mm, arms of 7 joints, "4~6 h"; mass not stated | lanxinrobotics.com/humanoid-robots/vb2-2 | maker, spec |
| 323 | Walker II, DroidUp (170 cm, 32 kg) | "双足人形机器人—行者二号": "体重:32kg；身高:170cm"; "自由度:30DoF"; "基于仿生肌腱驱动技术" (tendons with distributed motors); "单机算力(tops):端6"; vision sensors "(深度、红外、颜色):6组", microphones "8阵列"; "动态续航达6小时". Battery energy, torques, materials: not stated | droidup.com/product/2 | maker, spec |
| 326 | Walker Tienkung, UBTECH (170 cm, **55 kg**) | its specification picture, **two versions**: "Voice & Vision" **about 61 kg**, 21 DoF (arms 4, no neck), hands non-functional, one Jetson AGX Orin; "Embodied intelligence" **about 73 kg**, 42 DoF (neck 3, arms 7, hands of 6 DoF × 2), two AGX Orin, two 6-axis force/torque sensors. Both: "172cm", legs 6, waist 1, "Peak Torque 300N.m", IMU, RGB-D camera × 3, a 720p RGB camera, microphone arrays, speaker; "Capacity: 30Ah + 3Ah, Voltage: 48V" (1,584 Wh, arith.), 3 h; Intel Core i7. A model file `walker_tienkung.urdf` (owner "tienkungrobotics", not stated whose): 61.76 kg, 20 joints (hips 180, 300, 180; knee 300; ankles 60, 30; arms 52.5 × 4) | ubtrobot.com/en/ai-education/products/walker-tienkung (its picture, read myself); github.com/tienkungrobotics/Walker-TienKung-URDF | maker, spec; a model, owner not known |
| 352 | H1, Unitree (180 cm, 47 kg) | "Weight about 47kg", "Height about 180CM"; legs 5 each (hip 3, knee, ankle), arms 4; "Knee Torque About 360N.m，Hip Joint Torque About 220N.m，Ankle Torque About 59N.m，Arm Joint Torque About 75N.m", "Peak Torque Density: 189N.m/Kg" (the M107's, 360 N·m / 1.9 kg: H1p's M107 table, E6.3); "15Ah(0.864KWh)，Max Voltage 67.2V"; Intel Core i5 and i7; "3D LIDAR + Depth Camera". Its model `h1.urdf`: **59.34 kg**, 19 joints, its limits lower than the page's (hips 200, knee 300, ankle 40, arms 40, 40, 18, 18) | unitree.com/h1; github.com/unitreerobotics/unitree_ros (`robots/h1_description/urdf/h1.urdf`) | maker, spec; maker's model |

### E8.2 Batch 2b together, and the questions for Matthias

| What the makers give | Robots |
|---|---|
| Joints and torques (a model file or the page per joint), mass, and most of the rest | H1, Qinglong, Tien Kung 2.0, Walker Tienkung (the Voice & Vision version by its model; the other version's arms and neck have no torques), TALOS (a user's model); TLIBOT T1 (torques per joint group, no file) |
| Joints without torques per joint, mass and most of the rest | Robotera L7 (the knee's 400 N·m only), Tien Kung 3.0 (400 N·m at most), REEM-C (its model not expanded), THEMIS (its model without torques), SE01 (no mass) |
| A few figures | Walker II (mass, DoF, tendon-driven), Omni (mass, DoF) |
| Nothing from the maker | Optimus Gen 3, Gen2, V2.5; Orca; Phoenix; PHYBOT M1; TianGong Ultra; and not on their makers' sites: Sean, Songxing, Superman, Tianzhen Z1 |
| **On wheels by the maker** | Torobo (an omni-directional base), VB1-I, VB2 |

Nothing is entered until Matthias says yes:

| # | Question | Recommendation |
|---|---|---|
| 1 | Torobo, VB1-I and VB2 stand on wheels by their makers; the register says "not stated" or "legs" | their form "wheels": to the wheeled batch, as E7.3 question 1; batch 2b holds 24 |
| 2 | The Omni is 135 cm and 39.5 kg by X-Humanoid, "a small full-size research platform"; the register (catalogue) ~165 cm, 55–75 kg, types 2 and 3 | its type by the register's rules (E4) with the maker's size; at 135 cm it would sit beside type 1's robots (the G1 at 132 cm): a register question, for his word before it is taken apart in type 2 |
| 3 | The maker's mass differs: H1 47 kg by its page, 59.34 kg by its model; Qinglong 86.14 kg by its model (75); Tien Kung 3.0 64.5 kg (62); Walker Tienkung 61 or 73 kg (55); SE01 170 cm (180, its mass not stated); THEMIS 37.92 kg by its model (32) | as decided for batch 2 (E7.3, 2): the maker's in the parts file, the register's reported; the H1 its page's 47 kg the mode and its model's 59.34 kg the maximum, as the H2's (E6.8 point 5) |
| 4 | The Walker Tienkung in two versions ("Voice & Vision", "Embodied intelligence") | two versions, each drawn as often, as the H2-X (E7.5 point 12) |
| 5 | Sean, Songxing, Superman and Tianzhen Z1 are on no list of their makers; Orca has no site | kept, as decided for LimX CL and Nezha P01 (E7.3, 6): the template from the register's mass |
| 6 | TALOS's only model file is LAAS-CNRS's, from PAL's description, not PAL's own | its torques used, labelled second-hand; its mass PAL's 95 kg |

**Decided:** Matthias, 2026-10-30, "Yes, all six": Torobo, VB1-I and VB2 of form "wheels" in the register and in the
wheeled batch, batch 2b 24 robots; the Omni's type checked by the register's rules (E4) with its maker's 135 cm and
39.5 kg, his word on it before it is taken apart in type 2; the maker's mass in the parts file where the maker states
it, the register's reported (the H1 47 kg the mode, its model's 59.34 kg the maximum); the Walker Tienkung in two
versions, each drawn as often; Sean, Songxing, Superman, Tianzhen Z1 and Orca kept, from the register's mass; TALOS's
torques from LAAS's model, labelled second-hand, its mass PAL's 95 kg. Nothing entered yet: the register's change is
code, and the proposal of batch 2b's numbers (as E7.5) comes first.

**The Omni, decided:** Matthias, 2026-10-30: "If 2 stay, it has to be included, as it is just slightly smaler and has
slightly less weight". It stays in type 2 (the register's types unchanged) and is taken apart in batch 2b with its
maker's 135 cm and 39.5 kg; no check of its type by E4. Batch 2b: 24 robots, the Omni among them.

### E8.3 Proposal: batch 2b of type 2, robot by robot (2026-10-30). Nothing entered

Matthias, 2026-10-30: "Propose batch 2b". The method is batch 2's, agreed in E7.5 (points 1 to 13, with E6.8 and the
template of E7.4), with the decisions of E8.2 ("Yes, all six"; the Omni included); only the inputs are new, and where
an input needs a choice E7.5 did not make, it is **bold**. Read for it besides E8.1: the masses of TALOS's grippers
(1.094 kg each, eight links) and THEMIS's hands (0.463 kg each, palm and fingers, nine links) from their models' links.
Numbers at the modes are Claude's arithmetic; the run draws every one from its min / mode / max.

| # | What | Proposal |
|---|---|---|
| 1 | **Joint modules by the torques** | H1, Qinglong, Tien Kung 2.0, Walker Tienkung, TALOS: E6.8's fit at each joint's torque, half to 1.5 times (E). The **H1** its page's peaks per joint group (hips 220, ankles 59, arms 75 N·m) and its model's torso (200 N·m); **its knees the M107, 1.805 / 1.9 / 1.995 kg (S, E)**: its page's "Knee Torque About 360N.m" and "Peak Torque Density: 189N.m/Kg" are the M107's 360 N·m over 1.9 kg, as at the H1-2's knees (E6.8 point 1). The **Walker Tienkung's waist**, not in its model: **its hip roll's 180 N·m (E)**, as the Atom's (E7.5 point 1); **its "Embodied intelligence" version's neck (3) and wrists (3 an arm), not in its model: 15.8 and 17.3 N·m (E: the medians of the head and the wrist joints of type 2's seven robots with every joint's torque)**. **TALOS's torques from LAAS's model, labelled second-hand** (E8.2, 6) |
| 2 | **The template** (E7.4) | Every other robot: the joint modules 20.2 / 40.4 / 60.6 % of its mass, split as type 2's seven robots on average. Robotera L7 and Tien Kung 3.0 state a maximum torque only (400 N·m each), TLIBOT T1 its hips', knees' and ankles' (450, 281, 148 N·m) but not which of its joints they are: a check, not used |
| 3 | **Inside each actuator** | E7.5 point 3: the G1's joint scaled; **the Walker II's tendon-driven joints ("仿生肌腱驱动") and the SE01's linear ones the same (E)**, said wherever shown, as the linear actuators of batch 2 |
| 4 | **Hands and grippers** | Robotera L7: **two XHAND 1, "重量 1100g", 1.045 / 1.1 / 1.155 kg each (S)**; SE01 and the Walker Tienkung "Embodied": six joints a hand, as Fourier's (E); **THEMIS: its two EN02 hands, its model's 0.463 kg each (E)**; **TALOS: its two grippers, its model's 1.094 kg each (E)**. None for the rest (REEM-C's hands: no mass found, its model not expanded; reported) |
| 5 | **The robot's mass** | E8.2, 3: the maker's (or its model's where it states none) the mode, ± 1 kg, its other masses the bounds; the register's where nothing else. H1 46 / 47 / 59.34 (decided); Qinglong 85.14 / 86.14 / 87.14 (its model; the register's 75 reported); Tien Kung 2.0 66.96 / 67.96 / 68.96 (its model; the register's 70–90 reported); THEMIS 36.92 / 37.92 / 38.92 (its model with its hands; the register's 32 reported); TALOS 93.34 (its model) / 95 / 96; **Robotera L7 66.2 / 67.2 / 68.2: its 65 kg "不含灵巧手" and its two hands**; TLIBOT T1 42 / 43 / 44 ("含电池，不含皮肤": its skin not in it, reported) |
| 6 | **Battery** | Stated: H1 864 Wh (57.6 V × 15 Ah, 16 cells by its 67.2 V), L7 60 V × 15 Ah (900 Wh), Walker Tienkung 48 V × 33 Ah (1,584 Wh, its "30Ah + 3Ah"); **TLIBOT T1 its "1110Wh" at 48 V (E, its voltage not stated): 23.1 Ah**; **Tien Kung 3.0 its "15Ah+3Ah" at 48 V (E: as the Walker Tienkung's main and small battery at 48 V): 864 Wh** (the template would give 946 Wh). **The SE01's "1000 mAh" not used** (no voltage, too small for a robot of its size): the template. Every other robot the template, 14.67 Wh per kg |
| 7 | **Boards** | E7.5 point 7. H1 two Intel computers (i5, i7); Walker Tienkung an Intel Core i7 and one or two Jetson AGX Orin (named: 87 cm², ± 5 %) with their carriers; **Robotera L7 an x86 computer ("80 TOPS (X86)") and an Orin of "275 TOPS" (E: AGX Orin-sized, 87 cm², half to 1.5 times; 275 TOPS is the AGX Orin's figure, my reading)**; **Tien Kung 3.0 its main controller ("4.8G主频", an Intel-class board, E) and its "2070tops" module, and the Omni's "2070 TFLOPS" controller: each as the H2 Plus's Jetson Thor, 87 cm² and a carrier 50 / 100 / 150 cm² (E; 2070 is the Thor's figure, my reading)**; the others one computer board (E) |
| 8 | **Sensors** | E7.5 point 8, each by its kind. H1 a LiDAR, a depth camera, an IMU; L7 a depth camera, a LiDAR, a microphone array, a speaker; Walker Tienkung an IMU, three RGB-D cameras, a 720p camera, four microphone arrays ("Linear 4-Mic Array × 4"), a speaker; Tien Kung 3.0 and Omni a depth camera, a LiDAR, an IMU; SE01 a LiDAR, a depth camera, an infrared camera, two speakers, an IMU; **Walker II "(深度、红外、颜色):6组" as six depth cameras (E: a depth camera holds all three) and its "8阵列" as a microphone array**; TALOS an IMU; the rest one IMU (E). Force, torque and touch sensors left out (no kind yet; E7.5 point 13) |
| 9 | **Cables** | E7.5 point 9, 8 m per metre of height. **TALOS ("EtherCAT communication network") two power conductors and an Ethernet line, as the Kangaroo; the Walker Tienkung and Tien Kung 3.0 ("CAN / EtherCAT", "CAN FD/EtherCAT") four conductors, CAN named for the joints (E)** |
| 10 | **Shell, screws, frame** | E7.5 points 10, 11; the SE01's frame "航空级铝材" (S); the others aluminium (E) |
| 11 | **Versions** | **The Walker Tienkung in two, "Voice & Vision" and "Embodied intelligence", each as often (decided, E8.2, 4)** |
| 12 | **Not in this proposal** | Force, torque and touch sensors; REEM-C's hands; the T1's skin; every option; the register's form "wheels" for Torobo, VB1-I and VB2, made with the entry; every second-hand figure but TALOS's torques |

**Robot by robot** (the register's mass in brackets where it differs; S stated, E estimated):

| # Robot | Mass min / mode / max (kg) | Joints | Hands | Battery | Boards | Sensors | Cables (m) |
|---|---|---|---|---|---|---|---|
| 216 Omni (55–75) | 38.5 / 39.5 / 40.5 | template (31 DoF) | — | 579 Wh (E) | a "2070 TFLOPS" module and carrier (E) | depth camera, LiDAR, IMU | 5.5 / 11 / 16.5 |
| 221 Optimus Gen 3 | 51 / 52 / 53 | template | — | 763 Wh (E) | one computer (E) | IMU (E) | 7.25 / 14.5 / 21.75 |
| 222 Optimus Gen2 | 55 / 56 / 57 | template | — | 822 Wh (E) | one computer (E) | IMU (E) | 7 / 14 / 21 |
| 223 Optimus V2.5 | 54 / 55 / 56 | template | — | 807 Wh (E) | one computer (E) | IMU (E) | 7 / 14 / 21 |
| 224 Orca | 49 / 50 / 51 | template | — | 734 Wh (E) | one computer (E) | IMU (E) | 6.5 / 13 / 19.5 |
| 229 Phoenix | 69 / 70 / 71 | template | — | 1,027 Wh (E) | one computer (E) | IMU (E) | 6.75 / 13.5 / 20.25 |
| 232 PHYBOT M1 | 59 / 60 / 61 | template | — | 880 Wh (E) | one computer (E) | IMU (E) | 7 / 14 / 21 |
| 244 Qinglong (75) | 85.14 / 86.14 / 87.14 | its model's 31 | — | 1,264 Wh (E) | one computer (E) | IMU (E) | 6.5 / 13 / 19.5 |
| 256 REEM-C | 79 / 80 / 81 | template (68 DoF) | — | 1,174 Wh (E) | one computer (E) | IMU (E) | 6.5 / 13 / 19.5 |
| 265 Robotera L7 | 66.2 / 67.2 / 68.2 | template (31 body) | 2 XHAND 1 (S) | 900 Wh (S) | x86 computer; Orin and carrier (E) | depth camera, LiDAR, microphones, speaker, IMU | 6.75 / 13.5 / 20.25 |
| 271 SE01 | 79 / 80 / 81 | template (32 DoF) | 2 × 6 joints | 1,174 Wh (E) | one computer (E) | LiDAR, depth and infrared cameras, 2 speakers, IMU | 6.75 / 13.5 / 20.25 |
| 272 Sean | 44 / 45 / 46 | template | — | 660 Wh (E) | one computer (E) | IMU (E) | 6.25 / 12.5 / 18.75 |
| 276 Songxing | 84 / 85 / 86 | template | — | 1,247 Wh (E) | one computer (E) | IMU (E) | 6.5 / 13 / 19.5 |
| 285 Superman | 44 / 45 / 46 | template | — | 660 Wh (E) | one computer (E) | IMU (E) | 6.75 / 13.5 / 20.25 |
| 290 TALOS | 93.34 / 95 / 96 | LAAS's model, 30 body | 2 grippers | 1,394 Wh (E) | one computer (E) | IMU | 7 / 14 / 21, Ethernet |
| 294 THEMIS (32) | 36.92 / 37.92 / 38.92 | template (30 body) | 2 EN02 | 556 Wh (E) | one computer (E) | IMU (E) | 6.5 / 13 / 19.5 |
| 297 TianGong Ultra | 54 / 55 / 56 | template | — | 807 Wh (E) | one computer (E) | IMU (E) | 7.25 / 14.5 / 21.75 |
| 298 Tianzhen Z1 | 44 / 45 / 46 | template | — | 660 Wh (E) | one computer (E) | IMU (E) | 6.75 / 13.5 / 20.25 |
| 299 Tien Kung 2.0 (70–90) | 66.96 / 67.96 / 68.96 | its model's 30 | — | 997 Wh (E) | one computer (E) | IMU (E) | 6.75 / 13.5 / 20.25 |
| 300 Tien Kung 3.0 (62) | 63.5 / 64.5 / 65.5 | template (31 DoF) | — | 864 Wh (S, E) | a main controller; a "2070tops" module and carrier (E) | depth camera, LiDAR, IMU | 6.75 / 13.5 / 20.25 |
| 302 TLIBOT T1 | 42 / 43 / 44 | template (41 DoF) | — | 1,110 Wh (S) | one computer (E) | IMU (E) | 6.5 / 13 / 19.5 |
| 323 Walker II | 31 / 32 / 33 | template (30 DoF, tendons) | — | 469 Wh (E) | one computer (E) | 6 depth cameras, microphone array, IMU | 6.75 / 13.5 / 20.25 |
| 326 Walker Tienkung Voice & Vision (55) | 60 / 61 / 62 | its model's 20 and its waist | — | 1,584 Wh (S) | Intel i7; one AGX Orin and carrier | IMU, 3 RGB-D, a 720p camera, 4 microphone arrays, speaker | 7 / 14 / 21 |
| 326 Walker Tienkung Embodied intelligence (55) | 72 / 73 / 74 | the same and its neck and wrists | 2 × 6 joints | 1,584 Wh (S) | Intel i7; two AGX Orin and carriers | the same | 7 / 14 / 21 |
| 352 H1 | 46 / 47 / 59.34 | its page's 19, knees the M107 | — | 864 Wh (S) | Intel i5 and i7 | LiDAR, depth camera, IMU | 7.25 / 14.5 / 21.75 |

Every robot also: a power distribution and a battery management board; screws by mass; a shell of plastics; the frame
the remainder, aluminium.

**What it gives at the modes** (Claude's arithmetic, `batch2b_inputs.py` and `batch2b_modes.py`, V91):

| Robot | Joint modules | Share | Hands | Battery pack | Frame before cables, boards and sensors |
|---|---|---|---|---|---|
| the 14 robots of the template without hands or stated battery (Omni, the three Optimus, Orca, Phoenix, PHYBOT M1, REEM-C, Sean, Songxing, Superman, TianGong Ultra, Tianzhen Z1, Walker II) | 40.4 % of their mass | 40.4 % | — | 14.67 Wh/kg ÷ 164 | 38 % of their mass |
| 244 Qinglong | 30.1 kg | 35.0 % | — | 7.71 kg | 37.2 kg (43 %) |
| 265 Robotera L7 | 27.1 kg | 40.4 % | 2.20 kg | 5.49 kg | 23.7 kg (35 %) |
| 271 SE01 | 32.3 kg | 40.4 % | 0.89 kg | 7.16 kg | 29.3 kg (37 %) |
| 290 TALOS | 26.1 kg | 27.5 % | 2.19 kg | 8.50 kg | 45.9 kg (48 %) |
| 294 THEMIS | 15.3 kg | 40.4 % | 0.93 kg | 3.39 kg | 13.4 kg (35 %) |
| 299 Tien Kung 2.0 | 24.8 kg | 36.5 % | — | 6.08 kg | 28.3 kg (42 %) |
| 300 Tien Kung 3.0 | 26.1 kg | 40.4 % | — | 5.27 kg | 24.8 kg (39 %) |
| 302 TLIBOT T1 | 17.4 kg | 40.4 % | — | 6.77 kg | 13.3 kg (31 %) |
| 326 Walker Tienkung Voice & Vision | 21.0 kg | 34.4 % | — | 9.66 kg | 22.5 kg (37 %) |
| 326 Walker Tienkung Embodied | 24.1 kg | 33.0 % | 0.89 kg | 9.66 kg | 29.0 kg (40 %) |
| 352 H1 | 21.7 kg | 46.1 % | — | 5.27 kg | 14.0 kg (30 %) |

No remainder falls below zero at the modes; the least, the H1's, 30 % of its mass. TALOS's joints by LAAS's model are
27.5 % of its 95 kg, the least of type 2: its model's limits may lie below PAL's peaks (none stated), so its joints may
be lighter here than they are.

**Agreed:** Matthias, 2026-10-30, choosing the answer offered: "Yes, agree E8.3" (points 1 to 12 and the robot-by-robot
table, with their estimates). Not entered: the entry (type 2's builder, the register's three wheeled robots, tests
first) is a step of its own, for his yes.

### E8.4 The entry: what each decision of E8.2 and E8.3 landed in (2026-10-30, on "Yes, build it")

Matthias, 2026-10-30: "Spec batch 2b's entry", then "Yes, build it" (the spec's points 1 to 6 and its open points A to
C with their recommendations). Builder: `tools/2_full_scale_general_purpose_ai_research/make_parts_taken_apart.py`;
register: `tools/make_humanoid_register.py`. Checks: VERIFICATION.md V93.

| Decision | Where it landed |
|---|---|
| E8.2, 1: Torobo, VB1-I, VB2 on wheels | the register's rows 307, 312, 313: form "wheels", decided in "… E8.2"; with the 40 before, the 43 robots of type 2 not yet taken apart are all on wheels |
| E8.2, the Omni kept in type 2 | `X_HUMANOID_OMNI`, 38.5 / 39.5 / 40.5 kg; the register's types unchanged |
| E8.2, 3: the maker's mass | each block's `mass`; the H1 46 / 47 / 59.34 kg |
| E8.2, 4: the Walker Tienkung in two versions | `walker_tienkung()`: 'Walker Tienkung Vision' and 'Walker Tienkung Embodied' (open point C), each as often |
| E8.2, 5: robots found nowhere kept | `from_the_register()`: Orca, Phoenix, PHYBOT M1, Sean, Songxing, Superman, TianGong Ultra, Tianzhen Z1; `tesla_optimus()` for the three Optimus |
| E8.2, 6: TALOS's torques second-hand | `TALOS_JOINTS`, its sources "LAAS-CNRS's model of PAL's robot, second-hand"; the sheet Sources 'TLu' of kind "Second-hand: a user's model" |
| E8.3, 1: five robots by their torques | `H1_JOINTS` (the knees `M107`), `QINGLONG_JOINTS`, `TIEN_KUNG_2_JOINTS`, `WALKER_VISION_JOINTS` (its waist `WALKER_WAIST_NM`), `WALKER_EMBODIED_JOINTS` (`MEDIAN_HEAD_NM`, `MEDIAN_WRIST_NM`), `TALOS_JOINTS`; Qinglong's and TALOS's arms named by their place, TALOS's legs by their axes (open point B) |
| E8.3, 2: the template | `template()`; E7.4's numbers and seven robots unchanged (open point A) |
| E8.3, 3: tendons and linear joints | unchanged: the shared sheet JointParts, the Walker II's and SE01's sources say so |
| E8.3, 4: hands and grippers | the L7's two XHAND 1 (`added_joints`, 1.045 / 1.1 / 1.155 kg, S), the SE01's and the Walker Tienkung Embodied's `SIX_JOINT_HAND`, THEMIS's two EN02 (0.463 kg, E), TALOS's two grippers (1.094 kg, E) |
| E8.3, 6: batteries | `voltage_capacity()` for the H1, L7, Walker Tienkung; **Tien Kung 3.0 24 / 48 / 72 V (E) at its stated 18 Ah, as type 1's Booster T1 (E5.14 point 2): 01 asks every estimate to span half to 1.5 times**; the T1's stated 1,110 Wh at 48 V, labelled "S, E" (the voltage only splits the stated energy) |
| E8.3, 7: boards | `THOR_SIZED` (Omni, Tien Kung 3.0), the L7's x86 board and Orin, the Walker Tienkung's Intel i7 and one or two AGX Orin, the H1's i5 and i7 |
| E8.3, 8, 9: sensors, cables | each block's `sensors`; TALOS `cable_quantity=CABLE_ETHERNET` |
| Also found at the entry | **the sheet Sources lacked batch 2b's codes** (cited in the rows, not listed: 01 then showed the makers' numbers as a third party's): 23 codes added (H1mu, OMp, TSL, SNC, PHY, OLu, RCp, L7p, XH1, SEp, ZRT, SIA, UNI, TLp, TLu, THu, XHN, TLB, TK2u, TK3p, DRU, WTp, WTu); **batch 2's two Orin NX rows** (ALICE 4, Oli) named no code: now `orin_nx_boards()` names the robot's own; **01's table: the battery's axis leaves room for the longest bar's label** (`WH_ROOM` = 0.9; "1584 Wh" ran into the cells; type 1's axis unchanged, 0 to 800 Wh) |

Matthias, 2026-10-30: "Yes, start batch 2", for the first 27 of type 2's 55 robots not on wheels, in the register's
order: sources only, nothing changed while his run of 02 goes. Earlier the same day: "All 97 first", and "but also look
at the parts where you can find information" (each robot's own sources first; type 1's method, E5.17, only where they
stop). Read myself on 2026-10-29 and 2026-10-30 in the built-in browser and through GitHub's interface, unless it says
second-hand. A second-hand source was read only as a search summary or a press article: context, not a value. Nothing
is entered.

### E7.1 Robot by robot: what the makers state

The register's height and mass in brackets; **bold** where the maker's differs.

| # | Robot (the register) | What the maker states | Source | Kind |
|---|---|---|---|---|
| 25 | Alice (**157 cm, 50 kg**, 31 DoF, "China") | AeiROBOT (Ansan, **South Korea**) has two of the name with pages. **ALICE 4**: "160cm / 45kg", 41 DoF, "GENE-RAP6, Jetson Orin NX", "FSR Sensor, IMU, Depth Cam", "proprietary linear actuators" that "do not use a reducer", with their own motor drivers. **ALICE 3**: "144cm / 27.5kg", 27 DoF (legs 6 × 2, waist 1, arms 7 × 2, head 2), NUC11TNKi7 and Jetson AGX Xavier, an IMU (3DM-GX4-25), a stereo camera (ZED2i), a force-torque sensor (RFT82). A third, ALICE M1, is named without a page. Neither matches the register. Torques, actuator masses, battery: not stated | eng.arobot4all.com/ALICE4, …/ALICE3 | maker, spec |
| 40 | Astribot S1 (170 cm, 80 kg; form "not stated") | "Height 170 cm", "Weight 80 kg"; arms of 7 DoF, 5 kg each; "Endurance 4~6 hours", "Supports plug-in". Its pictures show it **on a wheeled base**. The body's joints, battery capacity, boards: not stated. Second-hand: "1000 Wh", cable-driven actuators | astribot.com/en/product; a datasheet PDF at a.storyblok.com, not opened (a download) | maker, spec; second-hand |
| 47 | Atom Max (170 cm, 55 kg) | DOBOT's page of the Atom answered 404. DOBOT's model files of the **Atom**: `atom-p2`, the whole body, 29 joints (the legs' limits a placeholder of 1000 N·m; arms 56, 36, 18.6; head 12), 58.91 kg; `atom-p3`, the legs only (207.76, 241.42, 104.16, 213.8, 89.896 N·m), 61.81 kg. Whether the Atom Max is this Atom: not stated | github.com/Dobot-Arm/dobot_atom_urdf | maker's models |
| 53 | Bolt (175 cm, 75 kg) | "全尺寸人形机器人" (a full-size humanoid), 175 cm, 75 kg, 50 kg payload, a peak speed "突破11m/s" (above 11 m/s); nothing else | mirrormetech.com/cn/product_5.html | maker, spec |
| 68 | CUE7 (218 cm, 74 kg; form "not stated") | Toyota's own page not found. Second-hand: 74 kg, down from 120 kg (Toyota's research centre on X, as reported); "an inverted two-wheel base", "a wheeled base instead of legs" | techrepublic.com; letsdatascience.com; stuff.co.za | second-hand |
| 69 | CyberOne (177 cm, 52 kg) | Xiaomi's page: a whole-body control of "21个关节自由度" (21 degrees of freedom), depth vision to 8 m at 1 %. Second-hand, from the launch (2022-08-11): 177 cm, 52 kg; 13 joints and 21 DoF, five kinds of joint, 21 drive modules, a peak of 300 N·m at the hip; the arms' motors 500 g, up to 30 N·m rated. Battery: not found | mi.com/cyberone; wallstreetcn.com; inside.com.tw | maker; second-hand |
| 80 | DR01 (170 cm, 80 kg) | Deep Robotics' page of its humanoid loads blank (2026-10-29, 2026-10-30). Second-hand: its own "J60" and "J100" joints (the J100-116P, 2.93 kg at 315 N·m, second-hand, E6.7). Height, mass, battery: not found | deeprobotics.cn/en/wap/humanoid.html (blank); huanqiu.com; roboticsandautomationnews.com | second-hand |
| 98 | Figure 03 (168 cm, **60 kg**) | "9% less mass" than Figure 02; a camera in each palm; fingertip sensors down to "three grams"; "soft textiles", "multi-density foam"; charging coils in the feet, "2 kW"; made by "die-casting, injection molding, and stamping"; actuators, batteries, sensors, structures and electronics "designed completely in-house". No mass, joints or battery capacity. Figure's other page (E3): 1.73 m, **"61KG"**. Second-hand: 2.3 kWh in the torso | figure.ai/news/introducing-figure-03; figure.ai/figure (E3); Digital Today, 2026-09-14 | maker; second-hand |
| 123 | H2-X (**182 cm, 70 kg**) | **"1725*455*245mm"**, **"65+Kg"** with battery; 31 DoF (legs 6, arms 7, waist 3, head 2); arm "150N.m", leg "300N.m" at most; internal-rotor PMSM, crossed roller bearings; "Aerospace-Grade Aluminum + High-Strength Engineering Plastic + Energy-Absorbing Cushioning Material"; local air cooling; "Dual Battery Capacity: 20 Ah (1.152 kWh), Hot-Swappable", "Maximum Voltage: 67.2V" (16 cells in series, arith.); PC1 "8-core high-performance CPU", PC2 "Intel Core i7 Or Orin NX", PC3 optional; a binocular and a monocular camera. The motors' masses: not stated | unitree.com/H2-X | maker, spec |
| 132 | HONOR D1 (169 cm, 45 kg) | HONOR's page: no figures ("an in-house high-dynamic motion system"). Second-hand: 169 cm, 45 kg, 25 DoF, HONOR's own joint modules, liquid-cooled | honor.com/uk/events/honor-robot; marathonhandbook.com | maker, no figures; second-hand |
| 134 | I-Series (175 cm, 60 kg) | No page of the robot found; the catalogue gives no website ("http://N/A"). Second-hand: Simplexity's first generation "produced in small batches" | yicaiglobal.com | second-hand |
| 135 | IGRIS-C (154 cm, 56 kg) | "Height 154 cm", "Weight 56 kg", "17,000mAh 48V" (816 Wh, arith.), charged in 2.5 h; legs 6 × 2, waist 3, arms 7 × 2, neck 2 (31), hands 6 × 2; "RGB Stereo, Depth Camera", "6-Axis IMU, Encoders". Torques, actuator masses: not stated | robros.co.kr/ko/igrisc | maker, spec |
| 144 | JingChu (170 cm, 65 kg) | 荆楚一号: "身高170cm，体重约65kg" (about 65 kg); "26个自由度（不含手）" (26 without the hands), hands of 6 DoF as standard; the knees "行星滚柱丝杠直线驱动模组" (planetary roller-screw linear modules), "大外径：65mm", **"关节重量：2kg"** (the joint's mass 2 kg); the other joints "高扭矩行星减速机模组" (high-torque planetary modules); "48V20AH" (960 Wh, arith.), about 8 h; "激光雷达" (LiDAR), "2个RGBD深度相机" (two RGB-D cameras), "6轴IMU"; "6核高性能CPU，32核GPU，AI算力高达67TOPS"; microphone array, speaker, WiFi 6, Bluetooth 5 | jingchurobot.cn/product_detail/1.html | maker, spec |
| 151 | KAIST (165 cm, 75 kg) | The lab's page: "Full-size humanoid robot for dynamic locomotion", "Fully custom actuator system"; no figures, no page of its own. Second-hand: 75 kg, a knee of 320 N·m peak, a "3K compound planetary gearbox" | dynamicrobot.kaist.ac.kr/new-page; interestingengineering.com | maker, no figures; second-hand |
| 153 | Kangaroo (160 cm, **40 kg**) | "Height 1,60 m", **"Weight 50-65 kg"**, "Total DoF 14-40" by configuration (legs 6, torso 2, arms 4, 5 or 7); "custom linear actuators with integrated force sensors"; "4x RGB-D Cameras", IMU; "Battery 15Ah, 63V. 976Wh"; EtherCAT. PAL's model files exist (github.com/pal-robotics/kangaroo_robot), not yet read | pal-robotics.com/robot/kangaroo | maker, spec |
| 157 | Kepler (**170 cm, 88 kg**) | Kepler's page of its **K1** ("Forerunner"): "178cm", "85kg", 40 DoF, "100 TOPS". No robot of 170 cm and 88 kg on Kepler's pages | gotokepler.com/productDetailK1?id=2 | maker, spec |
| 158 | Kepler K2 (**178 cm, 85 kg**) | **175 cm; 75 kg on legs**, 135 kg on wheels (a bipedal and a wheeled version); 52 DoF (legs 6, arms 7, hands 11 each); a "Planetary roller screw actuator" of "8200N" peak, a "Rotary actuator" of "220N.m" peak, micro actuators; flexible sensors, 6-axis force sensors, vision, inertial sensors; "1h charge/8h endurance"; 100 TOPS. The actuators' masses, battery capacity: not stated. The register's 178 cm and 85 kg are the K1's | gotokepler.com/productDetailK2?id=3 | maker, spec |
| 163 | Kuavo-5 (**168 cm, 55 kg**; "legs or wheels") | Leju's parameter picture: KUAVO 5 **"607x270x1730mm", "63.5kg"**, 41 DoF ("6自由度灵巧手", with hands of 6 DoF), a motor's "400NM" at most, 5 kg per arm, "100~2070 TOPS", "4*深度相机/3d激光雷达" (four depth cameras, a 3D LiDAR), ≥ 2 h, WiFi 6, Bluetooth 5.2; the KUAVO 5-W, on wheels, 156 kg. Leju's model files of the Kuavo 5 (`biped_s50` to `s56`, versions 5.0 to 5.6 by Leju's numbering): s50 and s51 57.15 and 58.49 kg (legs 180 N·m at most); s52 to s56 66.34 to 69.44 kg, all with the same 29 joints (hips 127, 71, 132; knee 280; ankles 91.6, 68.4; waist 102; arms 66, 75, 57, 75, 14.1 × 3; head 1.5, 12). None at 63.5 kg | lejurobot.com/en/products/kuavo-5 (its sixth picture); github.com/LejuRobotics/kuavo-ros-opensource (`docs/robot_version版本号说明.md`) | maker, spec; maker's models |
| 170 | LimX CL (164 cm, 45 kg) | Not on LimX's list of products (Luna, Oli, TRON 1, TRON 2). Second-hand: no figures from LimX; aggregators disagree (157 cm and 20 DoF; 45 kg and 31 DoF) | limxdynamics.com/en; newatlas.com | second-hand |
| 171 | LimX Oli (165 cm, 55 kg) | "165cm", "≤55kg" with battery; 31 DoF (legs 6, arms 7, waist 3, neck 2); "150N·m" at most; "Battery Capacity 9,500mAh", "About 1.5h", "Charger 58.8V 10A", one "Slide-Out Battery Module" (14 cells in series: 479 Wh at 3.6 V, arith.); RK3588 (motion) and "Orin NX (157TOPS)" (perception); depth cameras in the head and the chest (mounts at the wrist and hip), a LiDAR, a 6-axis IMU; air-cooled | limxdynamics.com/en/products/oli/spec | maker, spec |
| 176 | Luna (**165 cm, 55 kg**) | **"160cm"**, **"56kg"** with battery; 27 active DoF (legs 6, arms 5, waist 3, neck 2); "Max Motor Torque 200N·m"; "Slide-Out Battery Module (x2)", "Capacity 10,000mAh", charger "58.8V 10A", "≈4h", charged in "≈1h"; two RK3588 (motion; perception); a 6-axis IMU, an RGB camera, microphone, speaker; air-cooled. Its model file: 27 joints (hips and knee 200 N·m; ankles, waist, shoulders 70; elbow 30; head and wrist 15.8), 55.64 kg | limxdynamics.com/en/products/luna/spec; LimX's `HU_L04_01.urdf` (luna-description) | maker, spec; maker's model |
| 177 | LUS2 (160 cm, **65 kg**) | "Height 160 cm", **"Weight 57 kg"**, "Material Aluminum alloy"; "Total DoF (Joint Modules) 28" (legs 6, waist 1, arms 7: 27, the 28th not named); "Max joint torque 360 N·m"; one arm 5.5 kg without the hand; "Rated voltage 54 V", "Ternary lithium battery" (NMC), "Battery capacity 10 Ah" (540 Wh, arith.), 2 h; "3D LiDAR + Binocular Depth Camera", four microphones, a speaker; "NVIDIA Jetson AGX Orin"; air-cooled. Lumos's own joints: **LUMOS-P-60-30, 570 g, 102 N·m** peak (a two-stage planetary gear, two absolute encoders, the driver inside) and **LUMOS-P-104-24, 1750 g, 380 N·m**. Which joint holds which: not stated | lumosbot.tech/products/lus2; …/products/motor | maker, spec |
| 180 | MagicBot Gen1 (174 cm, 70 kg) | 1740 mm, about 70 kg; aluminium alloy and PC+ABS; 42 DoF; at least 350 N·m; an 8-core CPU, 100 TOPS; a 3D LiDAR, two depth and three fisheye cameras; 25 Ah (1.35 kWh). Its model file: 30 joints (hip roll and pitch, knee 360 N·m; hip yaw 60; ankles 120; waist roll 200, yaw 100; head 60; shoulder pitch and roll 110; shoulder yaw, elbow, wrist yaw 100; wrist roll and pitch 40), 66.4 kg. MagicLab's joint modules: E7.2 | magiclab.top/en/human; github.com/MagiclabRobotics/magicbot-gen1_description (`MAGICBOT.urdf`); magiclab.top/parts/… | maker, spec; maker's model |
| 199 | Motion 2 (160–165 cm, 60–75 kg) | VinMotion's page of the Motion 2: a video, no figures; its news page has no article on it | vinmotion.net/product/motion-2 | maker, no figures |
| 200 | Moz1 (160 cm, 70 kg; form "not stated") | "全向轮式底盘" (an **omnidirectional wheeled chassis**), "自由度达26个" (26 DoF), "七轴仿生臂" (arms of seven axes), its own force-controlled joints | spirit-ai.com/product | maker |
| 203 | NAVAI-I3 (180 cm, 70 kg) | The centre's page of the "NAVIAI i3": "全地形多功能双足机器人" (an all-terrain biped); its figures only in pictures and animation, none readable as text. Its GitHub holds the SDK of the earlier Navigator 2, no model file. Second-hand: 1.8 m, 80 kg, 82 DoF, 2,250 TOPS (a wiki); 41 DoF (another); 9 km/h | zj-humanoid.com/zujian/2; github.com/ZJ-Humanoid; aiwiki.ai; chinadaily.com.cn | maker, no figures; second-hand |
| 210 | Nezha P01 (145 cm, 65 kg) | Not on its maker's list: Digit Robotics (数字华夏) shows the Xialan R03 and S02 and the Xiaqi X02 only. Found nowhere else | digit.com.cn/Products.html | maker, not listed |

### E7.2 Joint modules with a stated mass, against type 2's fit

Type 2's fit (E6.8 point 1): 0.0689 kg × torque^0.566, its band half to 1.5 times the mode. The makers' modules found
in batch 2, read myself:

| Module | Maker | Gear | Peak torque | Mass | The fit at that torque | Mass / fit | Source |
|---|---|---|---|---|---|---|---|
| LUMOS-P-60-30 | Lumos | planetary, two stages | 102 N·m | 570 g | 944 g | 0.60 | lumosbot.tech/products/motor |
| LUMOS-P-104-24 | Lumos | planetary | 380 N·m | 1750 g | 1988 g | 0.88 | lumosbot.tech/products/motor |
| P60N30 | MagicLab | planetary | 60 N·m | 532 g | 699 g | 0.76 | magiclab.top/parts/p60n30 |
| D90 | MagicLab | planetary | 25 N·m | 590 g | 426 g | 1.38 | magiclab.top/parts/d90 |
| P90N20 | MagicLab | planetary | 130 N·m | 1100 g | 1083 g | 1.02 | magiclab.top/parts/p90n20 |
| P110 | MagicLab | planetary | 360 N·m | 1900 g | 1928 g | 0.99 | magiclab.top/en/parts/p110 |
| H60 | MagicLab | harmonic | 90 N·m | 590 g | 880 g | 0.67 | magiclab.top/parts/h60 |
| H70 | MagicLab | harmonic | 96 N·m | 900 g | 912 g | 0.99 | magiclab.top/parts/h70 |
| T28 | MagicLab | ball screw | 750 N | 340 g | (linear) | — | magiclab.top/parts/t28 |
| The JingChu's knee | JCBOT | planetary roller screw | not stated | 2 kg | (linear) | — | jingchurobot.cn/product_detail/1.html |
| *CyberOne's arm motor* | *Xiaomi* | *not stated* | *30 N·m rated* | *500 g* | — | — | *second-hand* |

**What it gives:** all eight rotary modules lie inside the fit's band (0.60 to 1.38 times the mode), the two of 360 and
380 N·m within 12 % of it, as the M107 (E6.7). Which joint of the LUS2 or the MagicBot holds which module: stated by
neither maker.

### E7.3 Batch 2 together, and the questions for Matthias

| What the makers give | Robots | How they would be drawn (the method agreed for type 1 and batch 1) |
|---|---|---|
| Joints and torques (a model file or a page), mass, and most of battery, boards, sensors | H2-X, JingChu, Kuavo-5, LimX Oli, Luna, LUS2, MagicBot Gen1, Kepler K2; the Atom Max by the Atom's files | each joint's module from its torque (E6.8), the makers' modules as a check; the rest as batch 1 |
| Joints without torques, mass, battery, sensors | IGRIS-C, Kangaroo (its model files not yet read) | the joints' share of the mass (E5.17 point 1); the rest as batch 1 |
| The mass and a few figures only | Alice, Bolt, CyberOne, Figure 03, Kepler | type 1's template (E5.17) from the maker's mass, what is stated in its place |
| Nothing from the maker | DR01, HONOR D1, I-Series, KAIST, LimX CL, Motion 2, NAVAI-I3, Nezha P01 | type 1's template from the register's mass; second-hand figures as context only |
| **On wheels**, by the maker or the press | Astribot S1, Moz1 (makers), CUE7 (press) | question 1 |

Nothing is entered until Matthias says yes:

| # | Question | Recommendation |
|---|---|---|
| 1 | Astribot S1 and Moz1 stand on wheels by their makers, CUE7 by the press; the register's form says "not stated" | their form "wheels" in the register: they go to the wheeled batch (B), and batch 2 holds 24 robots |
| 2 | The maker's mass or height differs from the register's: LUS2 57 kg (65); Kangaroo 50–65 kg (40); H2-X 172.5 cm, 65+ kg (182 cm, 70 kg); Luna 160 cm, 56 kg (165 cm, 55 kg); Kuavo-5 173 cm, 63.5 kg (168 cm, 55 kg); Figure 03 61 kg (60); Kepler K2 175 cm, 75 kg on legs (178 cm, 85 kg, the K1's) | the maker's in the parts file, as for the H2 Plus (E6.6, 3); the register's reported, not changed |
| 3 | The register's robot matches none of the maker's: Alice 157 cm, 50 kg (ALICE 4 160 cm, 45 kg; ALICE 3 144 cm, 27.5 kg; and AeiROBOT is Korean, the register says China); "Kepler" 170 cm, 88 kg (the K1 178 cm, 85 kg); Atom Max (the Atom's model files only) | Alice the ALICE 4, the one of type 2's size; "Kepler" the K1; the Atom Max the Atom, the whole body from `atom-p2` and the legs' torques from `atom-p3`, as the GR-1's two files (E6.6, 2) |
| 4 | Kuavo-5: the maker's 63.5 kg and 400 N·m, no model file at 63.5 kg | the 29 joints of `biped_s56` (the newest version 5, the same joints as s52 to s55) and two hands of 6 DoF, with the maker's 63.5 kg |
| 5 | Luna's battery, "Slide-Out Battery Module (x2)" with "10,000mAh": both together, or each? | each: two modules of 10,000 mAh (1,008 Wh at 50.4 V, arith.). The "(x2)" stands at the module, and the Luna lasts "≈4h" where LimX's Oli, as heavy and with one module of 9,500 mAh, lasts "About 1.5h". One reading, not a blend of both (a discrete state is drawn, never blended) |
| 6 | LimX CL and Nezha P01 are on no list of their makers | kept, as the register has them (E4); type 1's template from the register's mass |

**Decided:** Matthias, 2026-10-30, "Yes, all six": Astribot S1, Moz1 and CUE7 of form "wheels" in the register and in
the wheeled batch (B), batch 2 24 robots; the maker's mass and height in the parts file where the maker states them,
the register's reported, not changed; Alice the ALICE 4, "Kepler" the K1, the Atom Max the Atom (`atom-p2`, the legs'
torques from `atom-p3`); the Kuavo-5 the 29 joints of `biped_s56` and two hands of 6 DoF, at 63.5 kg; the Luna two
battery modules of 10,000 mAh; LimX CL and Nezha P01 kept, from the register's mass. Nothing entered yet: the
register's change is code (`tools/make_humanoid_register.py`), and the proposal of batch 2's numbers (as E6.8 for
batch 1) comes first.

### E7.4 Test: a template from type 2's own robots against type 1's (2026-10-30). Nothing entered

Matthias, 2026-10-30, on question 6: "for 6 test, if you can develop a method just using 2 data and see if it is
different than 1 model", then "Yes, build the test" (the spec's points 1 to 6). Type 1's template (E5.17) fills two
inputs from type 1's robots for a robot whose maker gives nothing: **(a)** the joint modules' share of the robot's mass,
49 % (24.5 / 49 / 73.5 %), split into small and large joints as type 1's robots are on average; **(b)** the battery's
energy, 12 Wh per kg of robot (half to 1.5 times). The rest of the template (shell, boards, screws, cables, sensors) has
no type 2 data behind it and stays as E6.8. Computed by a script in Claude's scratch folder, reading only the two parts
files and the makers' model files (V87).

**The robots.** Body joints only, no hands or grippers; each robot once (the H2 Plus is the H2's body; the GR-1 one
version). Type 1: the robots E5.17 used, reproduced (49.3 %, 36.3 to 53.0 %; 12.3 Wh/kg, 6.85 to 21.3). Type 2, (a):
every joint's torque stated, each joint's mass by type 2's fit (E6.8 point 1), the H1-2's knees the M107; the robot's
mass the maker's. Type 2, (b): the makers' energy and mass (E6, E7.1).

| (a) Robot | Joints | Modules | Share of the robot | Large joints' share of the modules |
|---|---|---|---|---|
| *type 1: G1 (weighed), Roboto Origin, RP1, PM01, AI Sapiens K1 (stated); Asimov 1, Booster T1, Booster K1, Unitree R1 (from their torques, 87.3 N·m/kg)* | 22 to 26 | 9.2 to 18.8 kg | **median 49.3 %**, 36.3 to 53.0 % | median 65.9 %, 42.3 to 77.8 % |
| 120 Unitree H2 | 31 | 31.3 kg | 44.7 % of 70 kg | 90.4 % |
| 119 Unitree H1-2 | 27 | 28.3 kg | 40.4 % of 70 kg | 90.0 % |
| 117 Fourier GR-2 | 29 | 22.2 kg | 35.3 % of 63 kg | 61.0 % |
| 116 Fourier GR-1 | 32 | 18.3 kg | 35.2 % of 52 kg | 52.4 % |
| 163 Kuavo-5 (`biped_s56`) | 29 | 21.7 kg | 34.1 % of 63.5 kg | 89.8 % |
| 176 Luna (`HU_L04_01.urdf`) | 27 | 23.2 kg | 41.5 % of 56 kg | 90.3 % |
| 180 MagicBot Gen1 (`MAGICBOT.urdf`) | 30 | 32.6 kg | 46.6 % of 70 kg | 93.2 % |
| **type 2, 7 robots** | | | **median 40.4 %**, 34.1 to 46.6 % | median 90.0 %, 52.4 to 93.2 % |

Left out of (a): the Atom Max, whose waist joint has only the placeholder 1000 N·m in DOBOT's file (its other 28
joints 21.4 kg, 36.3 % of 58.91 kg, a lower bound). Robots with only a maximum torque (H2-X, Oli, LUS2, Kepler K2) or
none (IGRIS-C, Kangaroo, JingChu) cannot give a share.

| (b) Wh per kg of robot | Robots | Median | Range |
|---|---|---|---|
| type 1 | G1, X1, N1, Roboto Origin, RP1, PM01, AI Sapiens K1, Asimov 1, Booster T1, Booster K1 5 Ah, Unitree R1 (11) | 12.3 | 6.85 to 21.3 |
| type 2 | H2 13.9, H1-2 12.3, GR-2 15.1, GR-1 9.3, H2-X 17.7, IGRIS-C 14.6, JingChu 14.8, Kangaroo 17.0 (at 57.5 kg, the middle of "50-65 kg"), Oli 8.7, Luna 18.0, LUS2 9.5, MagicBot Gen1 19.3 (12) | **14.7** | 8.7 to 19.3 |

**The test** (two-sided Mann–Whitney, robot by robot; different if p < 0.05):

| Input | Type 1 | Type 2 | U | p | Different? |
|---|---|---|---|---|---|
| (a) joint modules, share of the robot | 49.3 % (9) | 40.4 % (7) | 56 | **0.008** | **yes** |
| (a) large joints, share of the modules | 65.9 % (9) | 90.0 % (7) | 13 | 0.055 | no, at the edge |
| (b) battery, Wh per kg | 12.3 (11) | 14.7 (12) | 47 | 0.25 | no |

**Checked, the share's difference is the robots, not how their joints' masses were made:** type 1's four robots
estimated at 87.3 N·m/kg, recomputed by type 2's fit, give 50.9, 49.3, 55.1 and 54.7 % (type 1 still 49.3 %, p = 0.008).
Type 1's five robots with stated or weighed joints alone: median 48.0 % against 40.4 %, p = 0.11: five robots are too
few for the test to settle, the medians stay apart. **The direction of what is left:** type 2's joint masses come from
the fit, none but the M107 stated; the makers' modules of batch 2 lie at 0.60 to 1.38 times it (E7.2), Lumos's two at
0.60 and 0.88, so type 2's true share may lie lower still, not higher.

**What it changes** at the mode, for the two robots of question 6 (pack at 164 Wh/kg, shell 11.5 %, screws as E6.8):

| Robot | By | Joint modules | Battery | Frame before cables, boards and sensors |
|---|---|---|---|---|
| 170 LimX CL, 45 kg | type 1's template | 22.1 kg | 540 Wh (pack 3.3 kg) | 13.8 kg |
| | type 2's data | 18.2 kg | 660 Wh (pack 4.0 kg) | 17.0 kg |
| 210 Nezha P01, 65 kg | type 1's template | 31.8 kg | 780 Wh (pack 4.8 kg) | 20.0 kg |
| | type 2's data | 26.3 kg | 954 Wh (pack 5.8 kg) | 24.5 kg |

The joint modules carry most of the copper and the magnets (E5.12 point 1): by type 2's data the modules are 18 % lighter
(40.4 against 49.3 % of the robot), and the copper and magnets in them with them; the aluminium of the frame rises.

**Proposal, for Matthias's yes** (point 6 of the spec; nothing entered): for type 2's robots whose makers give no joint
torques, **the joint modules 40.4 % of the robot's mass (type 2's median), half to 1.5 times: 20.2 / 40.4 / 60.6 %**,
split into small and large joints as type 2's own robots are on average, not type 1's. **The battery 14.7 Wh per kg
(type 2's median), half to 1.5 times: 7.3 / 14.7 / 22.0**: not different from type 1's 12 by the test, but of the same
kind of robot, as his rule for sources asks. Shell, boards, screws, cables and sensors as E6.8.

**Agreed:** Matthias, 2026-10-30, choosing the answer offered: "Yes, agree E7.4". For type 2's robots whose makers give
no joint torques, the joint modules 20.2 / 40.4 / 60.6 % of the robot's mass, split as type 2's own robots on average;
the battery 7.3 / 14.7 / 22.0 Wh per kg of robot. Not entered: it enters with batch 2's proposal and its entry, each
for his yes.

### E7.5 Proposal: batch 2 of type 2, robot by robot (2026-10-30). Nothing entered

Matthias, 2026-10-30: "Propose batch 2". The method is batch 1's, agreed in E6.8 (points 1 to 13), with the decisions
of E7.3 ("Yes, all six") and the template of E7.4 ("Yes, agree E7.4") for what a maker does not give; only the inputs
are new. 24 robots: Astribot S1, Moz1 and CUE7 go to the wheeled batch (E7.3, 1). Read for it besides E7.1:
`MAGICBOT_with_hand.urdf` (MagicLab: 52 moving joints, 24 hand links of 1.178 kg for both hands; the finger joints'
100 N·m a placeholder, so the hands by their mass, not their torque). Numbers at the modes are Claude's arithmetic; the
run draws every one from its min / mode / max.

| # | What | Proposal |
|---|---|---|
| 1 | **Joint modules, robots with every joint's torque** | Atom Max, Kuavo-5, Luna, MagicBot Gen1: E6.8 point 1, type 2's fit at each joint's torque, half to 1.5 times (E); the torques from the makers' models, their pages giving none per joint. The Atom Max's waist: DOBOT's file holds only the placeholder 1000 N·m, so **104.16 N·m (E: its own hip yaw's; the Kuavo-5's single waist joint 102 N·m)**. The makers' modules of E7.2 (MagicLab's P110 1.9 kg at 360 N·m, 0.99 times the fit) are a check: neither maker says which joint holds which |
| 2 | **Joint modules, every other robot** | E7.4: 20.2 / 40.4 / 60.6 % of the robot's mass, split by joint group and class as the seven type 2 robots of E7.4 on average (`average_joints()`, as type 1's). **The JingChu's knees the maker's "关节重量：2kg"**, 1.9 / 2 / 2.1 kg each (S, ± 5 % as E5.12 point 3), its other joint groups as the template: the template alone gives its knees 1.85 kg each (0.92 times the stated), a check |
| 3 | **Inside each actuator** | E6.8 point 3: the G1's weighed small or large joint, scaled. **Linear actuators** (the ALICE 4's "do not use a reducer", the Kangaroo's, the JingChu's roller-screw knees, the Kepler K2's roller screws) **the same (E)**: no linear actuator has been taken apart part by part; MagicLab's T28 (a ball screw, 340 g at 750 N) is the one with a stated mass. Said wherever these robots are shown |
| 4 | **Hands** | Six joints a hand as Fourier's, 0.22 / 0.443 / 0.66 kg each (E6.8 point 4): Kuavo-5, IGRIS-C, JingChu. The Kepler K2's of 11 joints Fourier's per joint × 11, 0.41 / 0.81 / 1.22 kg (E; the H2 Plus's hand of 22 joints, 0.825 kg, a check), the K1's as the K2's (E, the same maker; its hands' joints not stated). The MagicBot's its model's, 0.29 / 0.59 / 0.88 kg each (E). Figure 03's as the H2 Plus's, 0.41 / 0.825 / 1.24 kg (E: a hand of many joints, their number not stated). The Oli's two grippers of one joint as the X1's OmniPicker, 0.41 / 0.43 / 0.45 kg (E). None for the rest: the H2-X's, LUS2's, Luna's, Kangaroo's hands are options (Luna's standard hand a fist, no joints), the others name none |
| 5 | **The robot's mass** | E6.8 point 5 and E7.3, 2: the maker's mass the mode, the bounds its other masses and its models' sums, else the mode ± 1 kg; the register's mass where no maker states one (the register's reported in the table where they differ). **The H2-X's "65+Kg": 65 / 66 / 70 kg (E: the stated floor the minimum, the H2's "About 70kg" the maximum)**; the Oli's "≤55kg" 54 / 55 / 55; the Kangaroo's "50-65 kg" by configuration 50 / 57.5 / 65 |
| 6 | **Battery** | E6.8 point 6: the maker's energy ± 5 % where stated (H2-X, IGRIS-C, JingChu, Kangaroo, Oli, Luna, LUS2, MagicBot); else E7.4's 14.7 Wh per kg of robot, half to 1.5 times. NMC cylindrical cells (stated "Ternary lithium" for the LUS2; E for the others), the pack the energy ÷ 164 Wh/kg. **Figure 03**: the template's 895 Wh; the press's 2.3 kWh (second-hand) lies above the template's maximum (1,342 Wh): reported, not used |
| 7 | **Boards** | E6.8 point 7: each computer the maker names (an Intel board 60 / 120 / 180 cm²; an AGX Orin 87, an Orin NX 31.3, an RK3588 module 22 cm² as the Radxa CM5's, each with a carrier 60 / 120 / 180 cm²); a power distribution board 30 / 60 / 100 and a battery management board 30 / 60 / 96 cm² each robot. **Where the maker names only computing power:** the JingChu's "67TOPS" with six cores, the Kepler robots' and the Kuavo-5's "100 TOPS", the MagicBot's "8-core CPU, 100 TOPS" each an Orin NX-sized module and carrier (E: NVIDIA's Orin modules give these figures, my reading, not stated). Where nothing is named: one computer board 60 / 120 / 180 cm² (E, E5.17 point 3) |
| 8 | **Sensors** | E6.8 point 8, each by its kind: a binocular or a depth camera 37.5 / 75 / 112.5 g (E, as batch 1's); a camera of one sensor (RGB, monocular, fisheye, in the palm) and a LiDAR not named as type 1's of no named model (their kind's elements, no mass of their own); IMU, microphone array and speaker as the G1's (E where not named). **Robots whose makers name no sensor: one IMU (E: a robot that walks balances by one)** |
| 9 | **Cables and connectors** | E6.8 point 9: 8 m per metre of height (batch 1's 14 m at 1.75 m), to the half metre, half to 1.5 times; four conductors and XT30 pairs (E). **The Kangaroo's "EtherCAT"** (an Ethernet line through its joints): two power conductors and an Ethernet line, as the Fourier robots |
| 10 | **Shell** | 11.5 % of the robot's mass (E6.8 point 10), plastics; the makers' words in its name: H2-X "Engineering Plastic + Energy-Absorbing Cushioning Material", MagicBot PC+ABS, Figure 03 "soft textiles" and "multi-density foam" (polymers, E) |
| 11 | **Screws, frame** | Screws E6.8 point 11 (0.2 / 0.5 / 1 kg × mass / 35 kg); the frame the remainder, aluminium (stated by Unitree for the H2-X, Lumos for the LUS2, MagicLab for the MagicBot; E for the others); no titanium named in batch 2 |
| 12 | **Versions** | **The H2-X in two**, its PC2 "Intel Core i7 Or Orin NX" (one of two): each as often (a discrete state, drawn, as the GR-1's cameras). The Kuavo-5's basic computer only (its "2070 TOPS" an option) |
| 13 | **Not in this proposal** | Force and touch sensors (the ALICE 4's FSR, the K2's 6-axis force and "flexible" sensors, Figure 03's fingertips, the Kangaroo's force sensors in its actuators): no kind with its elements in the model yet, grams each; the HONOR D1's liquid cooling (second-hand only); every option a maker sells (dexterous hands, the Oli's computing backpack, the Kuavo-5's 2070 TOPS); the register's form "wheels" for Astribot S1, Moz1 and CUE7, made with the entry; every second-hand figure |

**Robot by robot** (the register's mass in brackets where it differs; S stated by the maker, E estimated):

| # Robot | Mass min / mode / max (kg) | Joints | Hands | Battery | Boards | Sensors | Cables (m) |
|---|---|---|---|---|---|---|---|
| 25 Alice: the ALICE 4 | 44 / 45 / 46 (50) | template (41 DoF, linear) | — | 660 Wh (E) | GENE-RAP6 (Intel); Orin NX and carrier | depth camera, IMU | 6.5 / 13 / 19.5 |
| 47 Atom Max: the Atom | 57.91 / 58.91 / 61.81, its models (55) | 29: arms 56, 36 × 3, 18.6 × 3, head 12 × 2 (`atom-p2`); legs 207.76, 241.42, 104.16, 213.8, 89.896 × 2 (`atom-p3`); waist 104.16 (E) | — | 864 Wh (E) | one computer (E) | IMU (E) | 6.75 / 13.5 / 20.25 |
| 53 Bolt | 74 / 75 / 76 | template | — | 1,100 Wh (E) | one computer (E) | IMU (E) | 7 / 14 / 21 |
| 69 CyberOne | 51 / 52 / 53 | template (21 DoF) | — | 763 Wh (E) | one computer (E) | depth camera, microphone array, IMU (E) | 7 / 14 / 21 |
| 80 DR01 | 79 / 80 / 81 | template | — | 1,174 Wh (E) | one computer (E) | IMU (E) | 6.75 / 13.5 / 20.25 |
| 98 Figure 03 | 60 / 61 / 62 (60) | template | 2, as the H2 Plus's | 895 Wh (E) | one computer (E) | binocular camera (E), 2 palm cameras, microphone, speaker, IMU (E) | 7 / 14 / 21 |
| 123 H2-X, two versions | 65 / 66 / 70 (70) | template (31 DoF; legs ≤ 300, arms ≤ 150 N·m) | — | 1,152 Wh, 16 in series (S) | PC1 (E, Intel-sized); PC2 an Intel board, or an Orin NX and carrier | binocular and monocular camera, IMU (E) | 7 / 14 / 21 |
| 132 HONOR D1 | 44 / 45 / 46 | template (25 DoF, second-hand) | — | 660 Wh (E) | one computer (E) | IMU (E) | 6.75 / 13.5 / 20.25 |
| 134 I-Series | 59 / 60 / 61 | template | — | 880 Wh (E) | one computer (E) | IMU (E) | 7 / 14 / 21 |
| 135 IGRIS-C | 55 / 56 / 57 | template (31 DoF) | 2 × 6 joints | 816 Wh (S) | one computer (E) | binocular camera, depth camera, 6-axis IMU | 6.25 / 12.5 / 18.75 |
| 144 JingChu | 64 / 65 / 66 | template (26 DoF), knees 2 kg each (S) | 2 × 6 joints | 960 Wh (S) | a 67 TOPS module and carrier (E) | LiDAR, 2 RGB-D cameras, 6-axis IMU, microphone array, speaker | 6.75 / 13.5 / 20.25 |
| 151 KAIST | 74 / 75 / 76 | template | — | 1,100 Wh (E) | one computer (E) | IMU (E) | 6.5 / 13 / 19.5 |
| 153 Kangaroo | 50 / 57.5 / 65 (40) | template (14 to 40 DoF, linear) | — | 976 Wh (S) | one computer (E) | 4 RGB-D cameras, IMU | 6.5 / 13 / 19.5, Ethernet |
| 157 Kepler: the K1 | 84 / 85 / 86 (88) | template (40 DoF) | 2, as the K2's | 1,247 Wh (E) | a 100 TOPS module and carrier (E) | binocular camera, IMU (E) | 7 / 14 / 21 |
| 158 Kepler K2 | 74 / 75 / 76 (85) | template (52 DoF with hands; roller screws) | 2 × 11 joints | 1,100 Wh (E) | a 100 TOPS module and carrier (E) | binocular camera, IMU (E) | 7 / 14 / 21 |
| 163 Kuavo-5 | 62.5 / 63.5 / 69.44, its model (55) | `biped_s56`'s 29: hips 127, 71, 132; knee 280; ankles 91.6, 68.4; waist 102; arms 66, 75, 57, 75, 14.1 × 3; head 1.5, 12 | 2 × 6 joints | 932 Wh (E) | a 100 TOPS module and carrier (E) | 4 depth cameras, LiDAR, IMU (E) | 7 / 14 / 21 |
| 170 LimX CL | 44 / 45 / 46 | template | — | 660 Wh (E) | one computer (E) | IMU (E) | 6.5 / 13 / 19.5 |
| 171 LimX Oli | 54 / 55 / 55 | template (31 DoF) | 2 grippers | 479 Wh (S) | RK3588 module and carrier; Orin NX and carrier | 2 depth cameras (head, chest), LiDAR, 6-axis IMU, microphone, speaker | 6.5 / 13 / 19.5 |
| 176 Luna | 55 / 56 / 57 (55) | its model's 27: hips and knee 200; ankles, waist, shoulders 70; elbow 30; head, wrist 15.8 | — (fists) | 1,008 Wh, two modules (S) | 2 RK3588 modules and carriers | RGB camera, 6-axis IMU, microphone, speaker | 6.5 / 13 / 19.5 |
| 177 LUS2 | 56 / 57 / 58 (65) | template (28 DoF) | — | 540 Wh, NMC (S) | AGX Orin and carrier | LiDAR, binocular depth camera, microphone array, speaker, IMU (E) | 6.5 / 13 / 19.5 |
| 180 MagicBot Gen1 | 66.4 (its model) / 70 / 71 | its model's 30: hip roll and pitch, knee 360; hip yaw 60; ankles 120; waist 200, 100; head 60 × 2; shoulders 110 × 2; shoulder yaw, elbow, wrist yaw 100; wrist roll and pitch 40 | 2 × 6 joints | 1,350 Wh (S) | an "8-core, 100 TOPS" module and carrier (E) | LiDAR, 2 depth cameras, 3 fisheye cameras, IMU (E) | 7 / 14 / 21 |
| 199 Motion 2 | 60 / 67.5 / 75 | template | — | 990 Wh (E) | one computer (E) | IMU (E) | 6.5 / 13 / 19.5 |
| 203 NAVAI-I3 | 69 / 70 / 71 | template | — | 1,027 Wh (E) | one computer (E) | IMU (E) | 7.25 / 14.5 / 21.75 |
| 210 Nezha P01 | 64 / 65 / 66 | template | — | 954 Wh (E) | one computer (E) | IMU (E) | 5.75 / 11.5 / 17.25 |

Every robot also: a power distribution and a battery management board; screws by mass; a shell of plastics; the frame
the remainder, aluminium.

**What it gives at the modes** (Claude's arithmetic, `batch2_modes.py` in Claude's scratch folder, V88):

| Robot | Joint modules | Share | Hands | Battery pack | Shell | Frame before cables, boards and sensors |
|---|---|---|---|---|---|---|
| Alice, HONOR D1, LimX CL (45 kg) | 18.2 kg | 40.4 % | — | 4.03 kg | 5.17 kg | 17.0 kg (38 %) |
| Atom Max | 22.4 kg | 38.0 % | — | 5.27 kg | 6.77 kg | 23.7 kg (40 %) |
| Bolt, KAIST (75 kg) | 30.3 kg | 40.4 % | — | 6.71 kg | 8.62 kg | 28.3 kg (38 %) |
| CyberOne | 21.0 kg | 40.4 % | — | 4.65 kg | 5.98 kg | 19.6 kg (38 %) |
| DR01 | 32.3 kg | 40.4 % | — | 7.16 kg | 9.20 kg | 30.2 kg (38 %) |
| Figure 03 | 24.6 kg | 40.4 % | 1.65 kg | 5.46 kg | 7.02 kg | 21.4 kg (35 %) |
| H2-X | 26.7 kg | 40.4 % | — | 7.02 kg | 7.59 kg | 23.8 kg (36 %) |
| I-Series | 24.2 kg | 40.4 % | — | 5.37 kg | 6.90 kg | 22.6 kg (38 %) |
| IGRIS-C | 22.6 kg | 40.4 % | 0.89 kg | 4.98 kg | 6.44 kg | 20.3 kg (36 %) |
| JingChu | 26.6 kg (knees 4.0 S) | 40.9 % | 0.89 kg | 5.85 kg | 7.48 kg | 23.3 kg (36 %) |
| Kangaroo | 23.2 kg | 40.4 % | — | 5.95 kg | 6.61 kg | 20.9 kg (36 %) |
| Kepler (K1) | 34.3 kg | 40.4 % | 1.62 kg | 7.60 kg | 9.78 kg | 30.4 kg (36 %) |
| Kepler K2 | 30.3 kg | 40.4 % | 1.62 kg | 6.71 kg | 8.62 kg | 26.7 kg (36 %) |
| Kuavo-5 | 21.7 kg | 34.1 % | 0.89 kg | 5.68 kg | 7.30 kg | 27.1 kg (43 %) |
| LimX Oli | 22.2 kg | 40.4 % | 0.86 kg | 2.92 kg | 6.33 kg | 21.9 kg (40 %) |
| Luna | 23.2 kg | 41.5 % | — | 6.15 kg | 6.44 kg | 19.4 kg (35 %) |
| LUS2 | 23.0 kg | 40.4 % | — | 3.29 kg | 6.56 kg | 23.3 kg (41 %) |
| MagicBot Gen1 | 32.6 kg | 46.6 % | 1.18 kg | 8.23 kg | 8.05 kg | 19.0 kg (27 %) |
| Motion 2 | 27.3 kg | 40.4 % | — | 6.04 kg | 7.76 kg | 25.5 kg (38 %) |
| NAVAI-I3 | 28.3 kg | 40.4 % | — | 6.26 kg | 8.05 kg | 26.4 kg (38 %) |
| Nezha P01 | 26.3 kg | 40.4 % | — | 5.81 kg | 7.48 kg | 24.5 kg (38 %) |
| *for comparison: batch 1* | *18.3 to 31.3 kg* | *35 to 45 %* | | *2.95 to 5.93 kg* | | *about 22 to 26 kg* |

No remainder falls below zero at the modes; the least, the MagicBot's, 27 % of its mass (its 30 joints' modules by the
fit, 46.6 %, the highest share of the batch). Cables, boards and sensors outside the joints come off the frame too: in
his run of 02 (2026-10-30, 05:04) they draw 1.2 to 1.6 kg for batch 1's robots (the medians of the three added: H2
1.23, H1-2 1.42, GR-2 1.57, GR-1 1.31 kg).

**Agreed:** Matthias, 2026-10-30, choosing the answer offered: "Yes, agree E7.5" (points 1 to 13 and the robot-by-robot
table, with their estimates). Not entered: the entry (type 2's builder, the register's three wheeled robots, 01 and 02
where they need it, tests first) is a step of its own, for his yes.

### E7.6 The entry: what each decision of E7.3 to E7.5 landed in (2026-10-30, on "Yes, build it")

Matthias, 2026-10-30: "Spec the entry", then "Yes, build it" (the spec's points 1 to 7 and its open points A to D with
their recommendations). Builder: `tools/2_full_scale_general_purpose_ai_research/make_parts_taken_apart.py`; shared:
`tools/parts_taken_apart.py`; register: `tools/make_humanoid_register.py`. Checks: VERIFICATION.md V89.

| Decision | Where it landed |
|---|---|
| E7.3, 1: Astribot S1, Moz1, CUE7 on wheels | the register's rows 40, 68, 200: form "wheels", decided in "… E7.3"; not taken apart, so "not drawn: not yet taken apart" |
| E7.3, 2: the maker's mass in the parts file | each block's `mass` (sheet Constants, 'Robot mass, with battery'); the register's masses unchanged, reported in each row's source |
| E7.3, 3: Alice the ALICE 4, "Kepler" the K1, the Atom Max the Atom | `AEI_ALICE_4`, `KEPLER_K1`, `DOBOT_ATOM`; the register's `TAKEN_APART[2]` names them so ('AeiROBOT ALICE 4', 'Kepler K1', 'DOBOT Atom') |
| E7.3, 4: the Kuavo-5 by `biped_s56` | `KUAVO_JOINTS`, with `SIX_JOINT_HAND`; 62.5 / 63.5 / 69.44 kg |
| E7.3, 5: the Luna's two battery modules | `LIMX_LUNA`: 50.4 V × 20 Ah (1,008 Wh at the modes) |
| E7.3, 6: LimX CL and Nezha P01 kept | `LIMX_CL`, `DIGIT_NEZHA_P01`, the template from the register's mass |
| E7.4: type 2's template | `TYPE_TWO_SHARED`: 'Joint modules, share of the robot mass' 0.202 / 0.404 / 0.606 and 'Battery energy per kg of robot' 7.335 / 14.67 / 22.005; `SEVEN` and `AVERAGE_JOINTS` (the seven robots' joints without their hands) |
| E7.5, 1: four robots by their models' torques | `ATOM_JOINTS` (the waist 104.16 N·m, E), `KUAVO_JOINTS`, `LUNA_JOINTS`, `MAGICBOT_JOINTS`; `own_joints()` |
| E7.5, 2: the template; the JingChu's knees | `template()` over the shared `template_block()`; the JingChu's `stated_joints` (1.9 / 2 / 2.1 kg, S) in place of the template's knee rows (`template_joints()`), its other rows the template's shares; 01's check 18 (`TEMPLATE_OUTSIDE`; open point A) |
| E7.5, 3: inside each actuator, linear ones too | unchanged: the shared sheet JointParts, scaled to each module's mass |
| E7.5, 4: hands and grippers | `SIX_JOINT_HAND` (Kuavo-5, IGRIS-C, JingChu), `KEPLER_HAND` (K1, K2), the MagicBot's 0.589 kg each, Figure 03's as the H2 Plus's, the Oli's grippers as the X1's: `added_joints` of a template robot, beside its shares |
| E7.5, 5: masses | each block's `mass`, as E7.5's table |
| E7.5, 6: batteries | `voltage_capacity()`: H2-X, IGRIS-C, JingChu, Kangaroo, Oli, Luna, LUS2 (its cells "Ternary lithium", S), MagicBot; the others no voltage, so the energy per kg of the template |
| E7.5, 7: boards | `compute_module()` (JingChu, K1, K2, Kuavo-5, MagicBot), `ORIN_NX_BOARDS`, `RK3588_BOARDS`, the LUS2's AGX Orin, the ALICE 4's GENE-RAP6; one computer board where none is named; a power distribution board each (`template_block()`) |
| E7.5, 8: sensors | `binocular()`, `depth_camera()`, `camera()`, `lidar()`, `imu()`, `microphones()`, `speaker()`; `IMU_NOT_NAMED` where a maker names none |
| E7.5, 9: cables | `cables_by_height()`; the Kangaroo `cable_quantity=CABLE_ETHERNET` |
| E7.5, 10, 11: shell, screws, frame | `with_defaults()`; the H2-X's, MagicBot's and Figure 03's shells and the H2-X's, LUS2's and MagicBot's frames in their makers' words |
| E7.5, 12: the H2-X in two versions | `unitree_h2x()`: 'Unitree H2-X Core i7' and 'Unitree H2-X Orin NX', each drawn as often |
| Open point B: the template's rows name what they average | `average_joints(blocks, label)`: type 2's rows "(as type 2's seven robots with every joint's torque on average)", type 1's unchanged; 02's notes page takes the words from the rows (`on_estimates()`) |
| Open point C: one copy of the template function | `template_block()` in `tools/parts_taken_apart.py`; type 1's `catalogue_block` binds type 1's texts to it; type 1's file unchanged, cell for cell |
| Open point D: the Kuavo-5's joints named | by their axes in `biped_s56.urdf` (`KUAVO_JOINTS`'s comment) |

**Made at the entry, not spelled out in E7.5** (for Matthias to see; each labelled in its row):
- **The joints counted for encoders and connectors** of a template robot (two of each per joint): the maker's degrees of
  freedom where stated (ALICE 4 41, CyberOne 21, H2-X 31, IGRIS-C 31, JingChu 26, K1 40, K2 30 of its 52 with hands, Oli
  31, LUS2 28), else the register's (DR01 12, Figure 03 30, HONOR D1 25, I-Series 20, KAIST 25, Kangaroo 28, LimX CL 52,
  Motion 2 36 the middle of "~32–40", NAVAI-I3 44, Nezha P01 54), the Bolt, counted nowhere, 29, the median of the seven
  robots (E); each hand or gripper one, as batch 1's.
- **Module sizes that are estimates** (an Orin NX-sized module where a maker names only its computing power, an RK3588
  module as the Radxa CM5's) span half to 1.5 times their mode, by the rule for estimates (01 refused ± 5 %): 15.65 /
  31.3 / 46.95 and 11 / 22 / 33 cm². Named modules (an Orin NX, an AGX Orin) keep their stated size ± 5 %.
- **The Kangaroo's battery** at its stated 976 Wh and 63 V: 15.49 Ah; its "15Ah" gives 945 Wh, 3 % lower, inside the
  ± 5 %.
- **The H2-X's two names** shortened to fit 01's table (the first drawing overlapped its height column).

## E6. Each robot of type 2 its own composition: research, batch 1 (2026-10-29). Nothing entered

Matthias, 2026-10-29: "commit and push and then to typ 2", then "Yes, as proposed" to: A, all register robots of type
2, each its own rows, in batches, batch 1 the five with the makers' model files, with a source table to him first; B,
the wheeled robots their own kinds of part, in their batch; C, a parts file and builder per type. This section is
batch 1's source table. Read myself on 2026-10-29 in the built-in browser and through GitHub's interface, unless it
says E3 (read myself on 2026-10-28). Nothing is entered.

The sources: **H2p**, unitree.com/h2 (the H2's parameter table); **H2d**, Unitree's H2 developer guide, "About H2",
support.unitree.com/home/en/H2_developer/About_H2 (updated 2026-09-03); **H1p**, unitree.com/h1 (the H1 and H1-2
parameter tables and the M107 table); **H1d**, "About_H1-2", support.unitree.com/home/en/H1_developer/About_H1-2
(updated 2026-03-12); the makers' model files: `H2.urdf`, `h2_plus/H2_Plus.urdf`, `h1_2_description/h1_2.urdf`
(github.com/unitreerobotics/unitree_ros), `GR1T2.urdf`, `GR2T2V2.urdf` (github.com/FFTAI/fourier_lab),
`gr1t2/basic_urdf/gr1t2.urdf`, `gr2v3_8_7/basic_urdf/gr2v3_8_7.urdf` (github.com/FFTAI/Wiki-GRx-Models); **FSA**,
Fourier's actuator programming reference, fftai.github.io/fsa/fsa/.

### E6.1 Unitree H2 (120)

| What | Value as given | Source | Kind |
|---|---|---|---|
| Joints | "31 DoF, driven by 31 joint motors"; "Low inertia high-speed internal rotor PMSM"; "Industrial grade crossed roller bearings"; arm "120N.m", leg "360N.m" at most. The model's limits: hips (3) and knee 360 N·m (8 joints), ankle pitch 66.88 (2), ankle roll 19 (2), waist yaw 120, waist roll and pitch 180 (2), head 50 (2), shoulder pitch 130 (2), shoulder roll and yaw, elbow, wrist roll 60 (8), wrist pitch and yaw 10 (4). The motors' model, mass and gearbox: not stated | H2p, H2d, `H2.urdf` | maker, spec; maker's model |
| Battery | "15Ah(0.972KWh)", "Maximum Voltage: 75.6 V", "54–75.6V" at the back port; quick release; "Premium Lithium Battery with Low Internal Resistance". 18 cells in series by arithmetic (75.6 / 4.2 V; 972 Wh / 15 Ah = 64.8 V = 18 × 3.6 V). Mass, chemistry, cell format: not stated | H2p, H2d | maker, spec; arith. |
| Boards | PC1 "Intel Core i5" (motion control, 10 cores, 8 GB), PC2 "Intel Core i7" (development, 10 cores, 16 or 32 GB), each "500 GB or above"; optional PC3 "Jetson Thor (T5000)", "40W ~ 130W", and PC4 "Jetson Orin NX (16GB)". Board sizes: not stated | H2d | maker, spec |
| Sensors | binocular camera, "2 RGB sensor", 2064 × 1552, "Baseline 60mm", on PC1 (MIPI); "Array Microphone and High-Power Speaker"; the model: an IMU in the torso and one in the pelvis. No LiDAR named | H2p, H2d, `H2.urdf` | maker |
| Connectors | on the back: GXT30(2) sockets × 4 (battery and RS-485; 24 V and CAN × 2; 12 V and RS-485), Type-C × 6, RJ45 × 2, two hand connectors. The cables inside: not given | H2d | maker |
| Structure, cooling | "Aircraft-Grade Aluminum + Titanium Alloy + High-Strength Engineering Plastics" (no shares); "Local air cooling" | H2p | maker, spec |
| Mass, height | "About 70kg" with battery; "1820 x 456 x 218mm"; the model's links 75.59 kg | H2p; `H2.urdf` | maker; the register 70 kg, 180 cm |

### E6.2 Unitree H2 Plus (121)

| What | Value as given | Source | Kind |
|---|---|---|---|
| Joints | the H2's 31, with the same limits, and 44 hand joints (22 per hand: 3.3 N·m × 4, 1.864 × 20, 0.638 × 10, 0.5285 × 2, 0.189 × 8); which hand joints have their own motor: not stated | `H2_Plus.urdf` | maker's model |
| Sensors, boards | its binocular camera: 2560 × 1984, on "PC3/GMSL2"; PC3 is the H2's optional Jetson Thor, so the H2 Plus carries it (my reading of the table, not said in words) | H2d | maker |
| Hands | the hand's model: not named | — | — |
| Mass, height | not on Unitree's page (H2p lists the H2 and the H2 EDU only); the model's links 77.24 kg; the register 68 kg (humanoid.guide), lighter than the H2 with hands added | `H2_Plus.urdf`; the register | maker's model; catalogue |

The rest as the H2 (H2p, H2d).

### E6.3 Unitree H1-2 (119)

| What | Value as given | Source | Kind |
|---|---|---|---|
| Joints | "27 joint motors"; "The H1-2 robot uses the self-developed M107 joint motor" (which joints: not stated); "Knee Torque About 360N.m, Hip Joint Torque About 220N.m, Waist Joint About 220N.m, Ankle Joint About 75x2N.m"; shoulder and elbow "About 120N.m", wrist "About 30N.m". The model's limits, all lower: hips 200 N·m (6), knee 300 (2), ankle pitch 60 (2), ankle roll 40 (2), waist 200 (1), shoulder pitch and roll 40 (4), shoulder yaw and elbow 18 (4), wrists 19 (6) | H1p, H1d, `h1_2.urdf` | maker, spec; maker's model |
| **M107** | "Maximum torque" 360 N·m, **"Weight 1.9kg"**, 107 × 74 mm, hollow shaft, dual encoder; low-inertia internal-rotor PMSM | H1p (the M107 table), H1d | maker, spec |
| Battery | "15Ah(0.864KWh)", "Max Voltage 67.2V"; "quickly replaceable"; 16 cells in series by arithmetic (67.2 / 4.2 V; 864 / 15 = 57.6 V = 16 × 3.6 V). Mass, chemistry: not stated | H1p | maker, spec; arith. |
| Boards | PC1 "i5-1235U" (motion control), PC4 "i7-1255U / i7-1265U" (development), 10 cores each, "500GB or more"; optional "Orin NX (Maximum up to 3 devices)" | H1d, H1p | maker, spec |
| Sensors | "MID-360 Lidar" in the head (Livox; 265 g, L1 of E2.1); "D435 depth camera" in the head (75 g, E2.8); the model: an IMU | H1d, `h1_2.urdf` | maker |
| Hands | "Optional Dex5-1 or other ambidextrous hands"; the model `h1_2.urdf` carries two hands of 12 joints at 1 N·m each, `h1_2_handless.urdf` none | H1p; the two models | maker |
| Structure | not stated | — | — |
| Mass, height | "About 70kg", "(1503+285)mm" (1.79 m); the model's links 67.37 kg with two hands | H1p; `h1_2.urdf` | maker; the register 70 kg, 178 cm |

### E6.4 Fourier GR-2 (117)

| What | Value as given | Source | Kind |
|---|---|---|---|
| Joints | 29 body joints (E3). The model's limits: hip pitch and knee 366.05 N·m (4), hip roll 95.47 (2), hip yaw and ankle pitch 54.33 (4), ankle roll 29.84 (2), waist 74.45 (1), shoulder pitch and roll 74.45 (4), shoulder yaw and elbow 42.75 (4), wrists 17.33 (6), head 17.33 (2): seven levels of torque. Hands of 6 joints each, 12 optional (E3) | `gr2v3_8_7.urdf` (29 joints, 62.98 kg); `GR2T2V2.urdf` (21 joints driven, 62.73 kg); E3 | maker's models |
| Actuators | Fourier's own: FSA (motor, driver, gearbox, encoder in one; dual encoders, E3). Fourier's programming reference names seven models, FSA130_20V0, FSA100_15V0, FSA80_10V0, FSA60_08V0, FSA36_10V0, FSA36_08V0, FSA25_08V0, and gearbox ratios of 7 to 120; **no mass**, and which model sits in which joint is not stated. "Seven distinct FSA" in the GR-2 (press release, second-hand), as many as its torque levels | FSA; roboticstomorrow.com, 2024-09-30 | maker, programming reference; press |
| Battery | "≈950 Wh", "≤9 kg", 39.6 V (11 cells in series at 3.6 V, arith.) | E3 | maker, spec |
| Boards | Intel Core i7 (14 cores) and an 8-core ARM perception board | E3 | maker, spec |
| Sensors | binocular camera, 6-axis IMU, microphone, speaker | E3 | maker, spec |
| Structure | "铝合金+工程塑料" (aluminium alloy and engineering plastics; no shares) | E3 | maker, spec |
| Mass, height | "≈63 kg", 1750 mm | E3 | maker; the register 65 kg (humanoid.guide), 175 cm |

### E6.5 Fourier GR-1 (116)

| What | Value as given | Source | Kind |
|---|---|---|---|
| Joints | 32 FSA, "总执行器数量 44/34" (44 or 34 actuators with the hands), "最大关节扭矩 230N.m" (E3). **The two model files disagree on the legs:** `GR1T2.urdf` (fourier_lab, legs only driven) hip pitch and knee 225 N·m, hip yaw 66, hip roll 48, ankle roll 30, ankle pitch 15; `gr1t2.urdf` (Wiki-GRx-Models, all 32 driven) hip pitch and knee 135, hip roll 84.18, hip yaw 65, ankles 41.67 (4), waist 65 (3), shoulder pitch and roll 38.46 (4), shoulder yaw and elbow 30.3 (4), wrist yaw 13.17 (2), wrist roll and pitch 5.25 (4), head 5.25 (3). The maker's 230 N·m fits the first | E3; the two models (both 54.53 kg) | maker, spec; maker's models |
| Actuators | FSA, as the GR-2 (no mass stated) | FSA | maker |
| Battery | "483Wh", 40 V | E3 | maker, spec |
| Boards | i7-13700H; in the torso a power management module, a switch board, the motion controller | E3 | maker, spec |
| Sensors | RealSense depth camera, IMU | E3 | maker, spec |
| Structure | "铝合金+工程塑料" | E3 | maker, spec |
| Mass, height | "≈52kg", 1650 mm | E3 | maker; the register 55 kg (humanoid.guide), 165 cm |

### E6.6 Batch 1 together: what the sources give, and what is missing

| Robot | Joints: count and torques | Actuator masses | Battery | Boards | Sensors | Structure | Mass from the maker |
|---|---|---|---|---|---|---|---|
| 120 H2 | 31, model and page | no | 972 Wh, 18 in series | named | named | Al, Ti, plastics | about 70 kg; model 75.59 |
| 121 H2 Plus | 31 + 44 hand joints, model | no | as the H2 | as the H2, with PC3 | named | as the H2 | not stated; model 77.24 |
| 119 H1-2 | 27, model and page (they differ) | the M107, 1.9 kg, at which joints not stated | 864 Wh, 16 in series | named | MID-360, D435 | not stated | about 70 kg; model 67.37 |
| 117 GR-2 | 29, model | no | 950 Wh, ≤ 9 kg | named | named | Al, plastics | ≈63 kg; models 62.73, 62.98 |
| 116 GR-1 | 32, two models that differ | no | 483 Wh | named | named | Al, plastics | ≈52 kg; models 54.53 |

**Searched, not found:** the mass of any Fourier FSA (Fourier's site, its download centre, which lists only the newer
robots' brochures, its GitHub repositories, its programming reference, searches in English and Chinese); the motors of
the H2; a teardown or parts list of any of the five (E3); any battery pack's mass but the GR-2's; board sizes; the
cables inside.

**The one large joint with a stated mass:** the M107, 1.9 kg at 360 N·m (Unitree, the same kind: an internal-rotor
PMSM joint of a full-size humanoid). Type 1's fit (E2.8e, 0.121 kg × torque^0.441, from AgiBot's three actuators up
to 200 N·m) gives 1.62 kg at 360 N·m, 15 % below it: a check only, not used.

**For Matthias, before the proposal** (the method agreed for type 1, E5.12, E5.14, E5.17, then applies):

| # | Question | Recommendation |
|---|---|---|
| 1 | The H1-2: with hands or without? Unitree sells them as an option | without, as sold; its hands as their own rows only if he wants them |
| 2 | The GR-1's legs: which of Fourier's two model files? | `GR1T2.urdf` (225 N·m): it fits the maker's "230N.m"; the arms from `gr1t2.urdf`, the only file with them |
| 3 | The H2 Plus's mass: the maker gives none; the register has 68 kg (humanoid.guide) | the H2's "About 70kg" and its two hands, their mass the models' difference, 77.24 − 75.59 = 1.65 kg (E); the register's 68 kg reported, not changed |

**Decided:** Matthias, 2026-10-30, "Yes, all three": the H1-2 without hands; the GR-1's legs from `GR1T2.urdf` (225
N·m), its arms, waist and head from `gr1t2.urdf`; the H2 Plus the H2's 70 kg and 1.65 kg for its hands (E).

### E6.7 The large joints: makers' actuators above 120 N·m with a stated mass (2026-10-30, on "continue")

Matthias, 2026-10-30: "get handover and then continue". The handover's next step is the proposal for batch 1; where no
maker states an actuator's mass, it comes from the joint's torque. Type 2's hips and knees reach 360 to 366 N·m, and
the basis had one actuator above 200 N·m, the M107. Searched in English and Chinese for more; read myself unless
said. Nothing is proposed here.

| Actuator | Maker | Peak torque | Mass | N·m per kg | Gear, motor | Source | Kind | Same kind as type 2's joints? |
|---|---|---|---|---|---|---|---|---|
| M107 | Unitree | 360 N·m | 1.9 kg | 189 | hollow shaft, dual encoder, internal-rotor PMSM; gear not stated | unitree.com/h1, the M107 table; About_H1-2 | maker, spec | **yes**: Unitree's own, in the H1-2 |
| R86-3 | AgiBot | 200 N·m | 1.28 kg | 156 | not stated | E2.8e (X1b) | maker, spec | yes in kind (a humanoid's joint), from a type 1 robot |
| RMM10062-2E | RoboParty | 160 N·m (140 in the report's table) | 1197 g measured | 134 | planetary (third party); inner rotor | E5.11 | maker, measured | yes in kind, from a type 1 robot |
| Q90H | EngineAI | 145 N·m | 1.1 kg | 132 | "Full Planetary", internal-rotor PMSM | E5.11 | maker, spec | yes in kind, from a type 1 robot |
| DM-J10010L-2EC | DAMIAO | 120 N·m | 1375 g | 87 | not stated | E5.11 | maker, spec | yes in kind, from a type 1 robot |
| J100-116P | Deep Robotics | 315 N·m | 2.93 kg | 107.5 | not stated | retailers (4gltemall.com, aifitlab.com); the maker's 107.5 N·m/kg only through a search summary, the maker's page (deeprobotics.cn/en/wap/j80j100.html) answered 404 | **second-hand** | a legged robot's joint, from a maker of four-legged robots; not a humanoid's |
| Model 32; Model 25 | Huayan | 459 N·m; 204 N·m | 5.8 kg; 2.53 kg | 79; 81 | ratio 120; 100 ("precision reducer"), frameless torque motor, electromagnetic brake, optional torque sensor | huayan-robotics.net/humanoid-joint-module | maker, spec | **no**: high-ratio and braked, as in collaborative arms, unlike Unitree's joints; Fourier's gear is not stated |
| T800's joints | EngineAI | "450 N·m" | not stated | — | internal-rotor PMSM, crossed roller bearing | en.engineai.com.cn/product-t800 | maker, spec | no mass |
| R120 | Juxie | 450 N·m (from a search summary) | 4.1 kg (the same) | — | 161:1, brake | the maker's brochure, a PDF at worldrobotconference.com | not read: a download, not asked for | — |

**What it gives:** above 200 N·m only the M107 is a humanoid's joint with a mass stated first-hand. Its 189 N·m per kg
lies above every type 1 actuator (87 to 156), as type 1's fit expects: the mass grows more slowly than the torque
(E2.8e, mass ∝ torque^0.441). The J100-116P (second-hand, a four-legged robot's) and Huayan's (another kind of joint)
are context only. For Fourier's FSA neither the mass nor the gear is stated anywhere found (E6.4).

### E6.8 Proposal: batch 1 of type 2, robot by robot, by type 1's method (2026-10-30). Agreed, entered 2026-10-30 (E6.9)

Matthias, 2026-10-30: "Yes, all three" (E6.6). The method is type 1's, agreed: E5.12 (the actuators), E5.14 and E5.17
(the rest), E5.18 (the steels by their use), E5.21 and E5.22 (the boards' rest, the sensors' housings, the coolers, the
XT30 as a mated pair). Only the inputs are new, and where type 1's numbers do not carry to robots twice as heavy, the
change is named. Read for it on 2026-10-30, besides E6.1 to E6.7: Fourier's GR-1 page again (its hands, its computer,
its wiring), and Fourier's hand model `fourier_left_hand_6dof.urdf` and `fourier_right_hand_6dof.urdf`
(Wiki-GRx-Models): 0.443 kg each. Numbers at the modes are Claude's arithmetic; the run draws every one from its min /
mode / max.

| # | What | Proposal |
|---|---|---|
| 1 | **Actuators' masses** | **Changed from type 1:** type 1's torque density (E5.12 point 4) holds a joint's mass proportional to its torque, but the makers' actuators show the mass growing more slowly (E2.8e, E6.7): at 360 N·m it would give 4.1 kg, the M107 weighs 1.9. Instead **type 1's fit of E2.8e, refit on the 12 makers' actuators with a stated mass** (AgiBot's 3, E5.11's 8, the M107; the RMM8463-2E's "< 800 g" is a bound, left out): **mass = 0.0689 kg × torque^0.566**. Every one of the 12 lies within 0.79 to 1.33 times it; the M107 at 0.99. Checked on the G1, not fitted: its small joint 0.43 to 0.52 kg at 25 to 35 N·m against 0.525 weighed, its large 0.87 to 1.12 kg at 88 to 139 N·m against 1.1. Each joint's mass the fit at its peak torque, half to 1.5 times (E). The **M107 where Unitree names it**: the H1-2's knees, "About 360N.m", 1.805 / 1.9 / 1.995 kg (S, ± 5 % as E5.12 point 3) |
| 2 | **Which torque** | As E5.12: the maker's stated peak where it gives one per joint (the H1-2's page: hips and waist 220, knees 360, ankles 75 for each of 2 motors, shoulders and elbows 120, wrists 30 N·m), else the maker's model (H2, H2 Plus, GR-2; the GR-1's legs from `GR1T2.urdf`, its arms, waist and head from `gr1t2.urdf`, decided). Checked: the H1-2's "Peak: About 21Kg" in the hand at its 685 mm arm is 141 N·m at the shoulder, so the page's 120 N·m is plausible and its model's 40 N·m is not the arm's peak |
| 3 | **Inside each actuator** | As E5.12 point 1: the G1's weighed small (below 55 N·m) or large joint, scaled to the actuator's mass; magnets by the joint's heat (legs and waist SH, arms and head H). For a 360 N·m joint the large G1 joint (1.1 kg, 88 to 139 N·m) is the nearest weighed one; that its shares hold at twice the torque is an assumption, said wherever type 2 is shown |
| 4 | **Hands** | As the X1's grippers (joints of small inside): the GR-2's and GR-1's two Fourier hands of 6 joints each (the GR-1's page: "一对灵巧手", 44 actuators = 32 + 12), 0.22 / 0.443 / 0.66 kg each (E: Fourier's hand model, a model's mass, not a datasheet's); the H2 Plus's two hands 0.41 / 0.825 / 1.24 kg each (E, decided: 1.65 kg for both); the H1-2 and the H2 none |
| 5 | **The robot's mass** | As E5.14 point 1 (the maker's mass the mode; the bounds its other masses, its models' sums, the mode ± 1 kg): H2 69 / 70 / 75.59; H2 Plus 70.65 / 71.65 / 77.24; H1-2 66.98 (the hand-less model) / 70 / 71; GR-2 62 / 63 / 64 (its models 62.98 and 63.92; the register's and the press's 65 reported); GR-1 51 / 52 / 55.47 (its models 54.53 and 55.47) |
| 6 | **Battery** | As E5.14 points 2 and 3: energy ± 5 % (H2 and H2 Plus 972, H1-2 864, GR-2 950, GR-1 483 Wh); NMC cylindrical cells (E: "lithium" only, stated for none), their mass the energy ÷ 232.5 / 241.5 / 256 Wh/kg; the pack the energy ÷ 164 Wh/kg, its minimum cut at the cells, its maximum 1.5 times, the GR-2's cut at its stated "≤9 kg": H2 5.93, H1-2 5.27, GR-2 5.79 (≤ 9), GR-1 2.95 kg. The GR-1's page also says "额定容量 5.2Ah 112.3Wh" beside its 483 Wh, unexplained: reported, not used |
| 7 | **Boards** | As E5.14 point 4, one row per board the maker names: each Intel computer 60 / 120 / 180 cm² (E, the template's; H2 and H2 Plus PC1 and PC2, H1-2 PC1 and PC4, GR-2 one, GR-1 one, an ASUS PN64 mini PC); the H2 Plus's Jetson Thor module 87 cm² (E: as the AGX Orin's 100 × 87 mm, the Thor's size not read) and its carrier 50 / 100 / 150 cm² (E, as the T1's); the GR-2's 8-core ARM board 60 / 120 / 180 cm² (E); the GR-1's switch board (8 Ethernet ports, its page) 30 / 60 / 90 cm² (E, as the N1's) and its motion control unit 30 / 60 / 90 cm² (E, as the X1's control boards); each robot a power distribution board 30 / 60 / 100 and a battery management board 30 / 60 / 96 cm² (E, the template's); an Intel board's cooler the X86 one, an ARM board's the ARM one (E5.22) |
| 8 | **Sensors** | As E5.14 point 8, each by its kind's elements and housing (E5.22): H1-2 Livox MID-360 265 g (S) and RealSense D435 72 / 75 / 80 g (S); H2 and H2 Plus a binocular camera 37.5 / 75 / 112.5 g (E: as a D435, a stereo camera too; its mass not stated), 2 IMUs, the microphone array and the speaker as the G1's (E); GR-2 its binocular camera as the H2's (E), an IMU, microphone and speaker as the G1's; GR-1 one or two RealSense cameras, each as often (its page says "双深度相机" in one place and "一个深度相机" in another: a discrete state, drawn), an IMU |
| 9 | **Cables and connectors** | **Changed from type 1** (5 / 10 / 15 m, for robots of 1.2 to 1.3 m): the X1's 11 m listed and the G1's "not longer than 10m" at 1.3 m, scaled by height: 7 / 14 / 21 m for the H2, H2 Plus, H1-2 and GR-2 (1.75 to 1.82 m), 6.5 / 13 / 19.5 m for the GR-1 (1.65 m) (E). Four conductors and XT30 pairs as type 1 (E) for the Unitree robots; for the Fourier robots their page's "46V电源线和以太网线" (a 46 V power line and an Ethernet line through every joint): two power conductors as type 1 and an Ethernet cable of 8 conductors of 26 / 24 / 22 AWG (E: the gauge not stated) |
| 10 | **Shell** | As E5.14 point 6: 11.5 % of the robot's mass, half to 1.5 times, plastics ("High-Strength Engineering Plastics", "工程塑料") (E: no source of type 2 gives a shell's mass) |
| 11 | **Screws, bearings outside the actuators** | **Changed from type 1** (0.2 / 0.5 / 1 kg, the G1's, for robots of 19 to 44 kg): the G1's scaled by the robot's mass, 0.2 / 0.5 / 1 kg × mass / 35 kg: H2, H1-2 0.4 / 1.0 / 2.0, H2 Plus 0.41 / 1.02 / 2.05, GR-2 0.36 / 0.9 / 1.8, GR-1 0.3 / 0.74 / 1.49 kg (E); grades as E5.18 |
| 12 | **Frame** | As E5.14 point 9, the remainder, aluminium (stated by Unitree for the H2, by Fourier; E for the H1-2). The H2's and H2 Plus's "Titanium Alloy" (no share stated): 0.6 / 1.2 / 1.8 % of the robot's mass, Ti-6Al-4V (E: the X1's 0.4 kg of TC4 in 33 kg, the one robot of this project with named titanium parts) |
| 13 | **Not in this proposal** | The register's 68 kg for the H2 Plus (reported, E6.6); the cooling fans inside the joints (none stated); B, the wheeled robots; C, the parts file and builder of type 2 and how 02 draws type 2 (the next step, for his yes) |

**What it gives at the modes** (Claude's arithmetic, to show the order of magnitude):

| Robot | Actuators | Share of the robot | Battery pack | Shell | Frame, the remainder (about) |
|---|---|---|---|---|---|
| 120 H2 | 31.1 kg (8 × 1.93 at 360 N·m) | 44 % | 5.93 kg | 8.05 kg | 22 kg |
| 121 H2 Plus | 31.1 kg and hands 1.65 kg | 46 % | 5.93 kg | 8.24 kg | 22 kg |
| 119 H1-2 | 28.3 kg (6 × 1.46 at 220, 2 M107) | 40 % | 5.27 kg | 8.05 kg | 26 kg |
| 117 GR-2 | 22.2 kg and hands 0.89 kg | 37 % | 5.79 kg | 7.25 kg | 25 kg |
| 116 GR-1 | 18.3 kg and hands 0.89 kg | 37 % | 2.95 kg | 5.98 kg | 22 kg |
| *for comparison: type 1* | | *36 to 53 %, median 49 % (E5.17)* | | | |

No remainder falls below zero at the modes.

**Agreed:** Matthias, 2026-10-30, choosing the answer offered: "Yes, agree E6.8" (points 1 to 13, with their
estimates). Entered with C ("Yes, build C"), E6.9.

### E6.9 The entry: what each point of E6.8 landed in (2026-10-30, on "Yes, build C")

| Point of E6.8 | Where it landed |
|---|---|
| 1 Actuators' masses | `tools/2_full_scale_general_purpose_ai_research/make_parts_taken_apart.py`: `FIT_KG`, `FIT_POWER`, `from_torque()`, `fitted()`; `M107` at the H1-2's knees; the file's sheet Joints, columns Module mass min / mode / max |
| 2 Which torque | the same builder: `H2_JOINTS` (H2u), `H1_2_JOINTS` (H1p's peaks), `GR2_JOINTS` (GR2u), `GR1_JOINTS` (the legs from GR1T2.urdf, the rest from gr1t2.urdf); sheet Joints, column Torque limit |
| 3 Inside each actuator | unchanged: the shared sheet JointParts (`tools/parts_taken_apart.py`), drawn by 02's `draw_robot()`; the class by `LARGE_FROM_NM` |
| 4 Hands | `H2_PLUS_HAND`, `FOURIER_HAND` (joints of small inside); 01's `JOINT_KIND` gains 'hand' (arms) |
| 5 The robot's mass | each block's `mass`; sheet Constants, 'Robot mass, with battery' |
| 6 Battery | each block's `voltage` and `capacity` (sheet Constants), the GR-2's `pack` (4.33 / 5.79 / 9 kg); the cells NMC (E), the pack from its energy over 164 Wh/kg (the shared constant) |
| 7 Boards | each block's `boards` (sheet Boards), its `cooler` (sheet Parts: fans, heat pipes and fins, an ARM sink) |
| 8 Sensors | each block's `sensors` (sheets Sensors, SensorElements); the GR-1's one or two cameras as two versions (`fourier_gr1()`; the register's "Taken apart as" names both) |
| 9 Cables | `CABLES_TALL`, `CABLES_GR1`; the Fourier robots' `cable_quantity=CABLE_ETHERNET` and the shared number 'Ethernet conductor cross-section (8 conductors)' (0.1 / 0.205 / 0.326 mm²: 26 AWG's 0.129 widened to half the mode by the rule for estimates); 01's `CABLE_LENGTHS`, 02's cable copper in `draw_robot()` |
| 10 Shell | each block's `shell`; the shared 'Shell, share of the robot mass' |
| 11 Screws | `screws()`, the G1's 0.2 / 0.5 / 1 kg times the mass over 35 kg |
| 12 Frame, titanium | each block's `frame` (the remainder, aluminium); `titanium()` for the H2 and H2 Plus (Ti-6Al-4V) |
| 13 Not in it | as said there: the register's 68 kg for the H2 Plus unchanged; no joint fans; B, the wheeled robots, not begun |
| Also needed | the G1's weighed driver board area (22.9 cm²), from which every joint's board is scaled, as a shared number in type 2's file ('Driver board area, small joint (the G1's, weighed)'; one copy, `DRIVER_BOARD_AREA`, the G1's row in type 1's file the same) |

## E5. Each robot of type 1 its own composition: research, batch 1 of 4 (2026-10-29). Entered 2026-10-29 (E5.20)

### E5.22 Type 1's last open parts: the X1's newer parts list, its found parts, the N1's switch, the XT connectors (2026-10-29). Entered on his word

Matthias, 2026-10-29: "I want to finish open items first and once for all", then "Yes, 1 to 5" (HANDOVER.md,
2026-10-29, evening).

**1. The X1's newer parts list,** `智元灵犀X1_20250108/智元灵犀X1_BOM清单_20250108.xlsx` (17,678 bytes,
github.com/AGIBOTTech/AGIBOT_x1_hardware, downloaded on his yes into Claude's scratch folder; the maker's own list,
first-hand). One sheet, "结构件包" (the structural package), 167 items: no electrical parts. Against the X1's rows as
entered from the list of 2024-10-24 and the overall BOM of 2025-03-07:
- **The same:** the bearings outside the actuators (10 crossed roller, 9 four-point, 20 deep-groove ball: 12 ×
  61900-2Z and 8 × SB685ZZ, 8 rod ends); the battery case of sheet metal (电池包钣金 1 and 2); the shells (外观件).
- **Screws: 827, not about 980.** 618 socket-head of class 12.9 and 59 countersunk of class 10.9 ("材质碳钢 镀亮镍"),
  142 of stainless 304 ("材质为不锈钢304") and 8 shoulder screws of 304 (塞打螺钉): 677 carbon steel, 150 stainless
  304. The old list said "Screws and pins: 980" (E5.1), screws and pins together; the X1's rows count the pins twice
  (in "Screws (about 980)" and in "steel pins (about 115)").
- **Pins: 90 of SUS440C** (GB/T 119.2, "材质SUS440C"), not 40Cr or C45 steel: 5 × 3×25, 2 × 3×35, 9 × 4×10, 4 × 4×12,
  10 × 4×14, 2 × 4×20, 38 × 4×8, 18 × 5×10, 2 × 5×35 mm; at 7.7 g/cm3 108.6 g in all (arithmetic from the stated
  sizes).
- **Found again, with their numbers and material:** brass threaded inserts "IUT铜螺母" M3 × 12 and M4 × 4, "材质为
  C3604黄铜" (16, as on 2026-10-28); 4 silicone dampers (硅胶减震块); 1 sensor shield (传感器屏蔽罩, its material not
  in this list; stainless in the old one).

**2. The XT connectors' masses** (LCSC, the distributor, product pages of Amass parts, read in the built-in browser;
"商品毛重", the gross weight per piece; Amass's own data sheets give current and wire size, no mass):

| Part (Amass) | LCSC | Gross weight |
|---|---|---|
| XT30(2+2)-F.G.B, cable female, 3 pieces | C19268028 | 1.1224 g |
| XT30PB(2+2)-M, board male | C3040128 | 1 g |
| XT30U-F, cable female ("金属部分采用黄铜材质并经过镀金处理": brass, gold-plated; housing PA) | C99102 | 0.976 g |
| XT60-M / XT60-F | C98733 / C98734 | 3.29 g / 3.21 g |
| XT60H-M | C5334533 | 3.96 g |
| XT90H-F (its male: no weight on its page) | C3040685 | 8.8 g |

**What this settles for the XT30 (point 3):** a mated XT30 (2+2), a cable female and a board male, weighs 2.12 g; the
3 g entered for "one connector" is a mated pair and some, not one piece. Two per joint is two mated pairs (the
daisy chain: each joint's in and out), so the count stands and the mass of one pair falls to the parts' 2.12 g. Its
contacts are brass, gold-plated (Amass, through LCSC), not copper.

**The steel 440C** (Carpenter Technology, a producer, https://www.carpentertechnology.com/alloy-finder/440c, read
first-hand, "Type Analysis", UNS S44004): carbon 0.95 to 1.20, manganese ≤ 1, silicon ≤ 1, chromium 16.00 to 18.00,
molybdenum ≤ 0.75, phosphorus ≤ 0.04, sulfur ≤ 0.03 %, iron the balance. Outokumpu's grade table (read) does not hold it.

**The X1's overall BOM** (`智元灵犀X1_20250307/智元灵犀X1总BOM.xlsx`, 18,808 bytes, downloaded again on his yes; the
maker's newest overall list, 197 rows): of plugs only "XT60E-M" × 1 (a panel male, with its cable female one mated
pair); no XT90 (the older list of 2024-10-24 named XT90 plugs: not entered, the newest list holding none); the sensor
shield "0Crl8Ni9(GB)" (stainless 304); the dampers "硅胶" (silicone); the inserts "黄铜". **Found, left out**
(Matthias, 2026-10-29: "Leave it out"): "对接端子2进8出" × 1, a docking terminal of 2 inputs and 8 outputs,
electrical; no mass or material given.

**Entered** (Matthias, 2026-10-29: "Yes, enter all"; VERIFICATION.md V80): the X1's screws as 677 of 42CrMo4 (0.207 /
0.4145 / 0.622 kg, E) and 150 of stainless 304 (0.0459 / 0.0918 / 0.1377 kg, E), by number from the entered 0.6 kg for
980; its pins 90 of 440C, 0.105 / 0.1086 / 0.112 kg (S, the stated sizes); its shafts and crosses 17-4PH 0.075 / 0.15 /
0.225 kg (E, the former row less its pins); its brass inserts 6.5 / 13 / 19.5 g (E); its sensor shield, 304, 10 / 20 /
30 g (E); its silicone dampers 4 × 1 / 2 / 3 g, plastics (E); its XT60, one mated pair 5.9 / 6.5 / 7.2 g (S, E); the
N1's network switch, a board of 30 / 60 / 90 cm2 as the X1's router board (E); every robot's XT30 one mated pair 1.9 /
2.12 / 2.3 g (S, E; 3 g before), its contacts (35 % of it, as before) brass; the recipe 440C in
`element_recipes.xlsx` from Carpenter's analysis, the mode the middle of each range (S).

### E5.21 The rest of a board beyond its metals: glass, epoxy and bromine (2026-10-29). Entered on his word

Matthias, 2026-10-29: "Yes, build them", point 3b: the rest of the boards (laminate and components) by the recipes
E-glass and Epoxy already in `element_recipes.xlsx`, "the glass share entered only after a source table of FR-4
laminates, agreed by him". What it is: type 1's electronics are 0.82 kg at the mean (his run of 14:34), mostly boards;
of a board's mass 20 % is copper (E2.8b) and about 2 % the other metals (gold to lead, point 3a); the rest, about
0.6 kg in one robot, has no elements yet.

**The sources** (each read myself; what each is; whether it represents a robot's boards):

| Source | What it is | Read | What it says | Represents a robot's boards? |
|---|---|---|---|---|
| Isola Group, FR406 laminate and prepreg, product page with its core and prepreg tables, https://www.isola-group.com/pcb-laminates-prepreg/fr406/ (read 2026-10-29) | Manufacturer's data sheet; an FR-4 epoxy ("FR-4 process compatible", IPC-4101 /21 /24 /26, UL 94 V-0); first-hand | Yes (the page's tables; its PDF data sheet could not be decoded) | "Resin Content %" by glass style. Cores: 1x1080 58.0 %, 1x2116 45.0 %, 2x2116 45.0 and 52.0 %, 1x7628 41.0 %, 2x7628 41.0 %, 3x7628 to 5x7628 40.0 %, 2x106 65.0 %; prepregs: 106 75 %, 1080 65 %, 2116 56 %, 7628 42 to 50 % | Yes: the laminate of multilayer boards. Glass by weight is 100 % less the resin content: 35 to 60 %, 59 to 60 % in the 7628 cores of a 1.6 mm board, 42 to 55 % in the thin 1080 and 2116 plies of dense compute boards. One maker only |
| IPC-TM-650 2.3.16.2, *Treated Weight of Prepreg*, 12/94 (IPC, the industry's standards body), https://www.electronics.org/sites/default/files/test_methods_docs/2.3.16.2.pdf | Industry test method; first-hand | Yes (decoded from its PDF) | "RC = resin content by weight", RC = (1 − BW / TW) × 100, for "woven fabric 'E'-glass reinforced epoxy FR-4 prepreg"; resin specific gravity 1.37, E-glass 2.59 | Yes: it says the makers' resin content is by weight, so their glass is the rest of the weight |
| Lassen, Løkke, Andersen (1999). *Brominated Flame Retardants: Substance Flow Analysis and Assessment of Alternatives.* Danish EPA, Environmental Project 494, § 2.2.1, https://www2.mst.dk/udgiv/Publications/1999/87-7909-416-3/html/kap02_2_eng.htm | Government report; second-hand (from the literature); its words "can approximately be estimated" | Yes (§ 2.2.1) | "FR4 is by far the most used laminate. The laminate typically contains about 15% TPPBA [TBBPA]"; "0.42 kg per m2" of TBBPA in a 1.6 mm FR4 laminate (Legarth 1996); TBBPA "reactive" in FR4 epoxy | Yes in kind (FR-4); an estimate of 1999. Its two figures agree: 1.6 mm of laminate at 55 % glass (IPC's densities) weighs 2.96 kg/m2, and 0.42 kg of it is 14 %. TBBPA is 58.8 % bromine by its formula (C15H12Br4O2), so bromine about 8.8 % of the laminate |
| Marques, Cabrera Marrero, de Fraga Malfatti (2013). A review of the recycling of non-metallic fractions of printed circuit boards. *SpringerPlus* 2: 521, doi:10.1186/2193-1801-2-521 (read through Europe PMC; the PMC page asked for a bot check) | Peer-reviewed review; second-hand for its numbers, no method given for any | Yes | The non-metal part "about 70 wt%" of waste boards (no source of its own); Iji and Yokoyoma 1997, boards "with mounted electronic parts": "glass fiber (65 wt%), cured epoxy resin (32 wt%), and impurities (copper: < 3 wt%...)"; Zheng et al. 2009 by particle size: glass 71.50 / 55.50 / 46.00 %, "resin, etc." 26.86 / 43.45 / 53.52 %; Braun et al. 2001: a board "reinforced with 59,5% of fiber glass sheets"; no bromine figure | In part: whole waste boards of the 1990s and 2000s, some with their components; the glass share of the non-metals, the components' bodies counted in it. Second-hand |

Left out: Shengyi's S1000-2M data sheet (a distributor's copy; its tables are images, nothing could be read); search
summaries and suppliers' blogs with resin contents and bromine (8 to 12 %), not read first-hand; Mou et al. 2007's
table (a formulation of boards made from recycled non-metals, not a board).

**What the sources say together:** glass is 35 to 60 % of the laminate's weight by the maker (59 to 60 % in a 1.6 mm
board of 7628 cores), and 46 to 72 % of the non-metals of whole waste boards (65 % in boards with their parts); epoxy
the rest; bromine about 9 % of an FR-4 laminate (one estimate, 1999; halogen-free laminates exist and no source gives
their share in today's boards).

**Entered as proposed** (Matthias, 2026-10-29: "Yes, enter them"; VERIFICATION.md V77), the shared constants "Board
rest, glass fibre share" and "Board rest, bromine share" of the parts file, for the rest of a board beyond its metals,
in every draw, with the recipes of `element_recipes.xlsx`:

| Share of the rest | Min / mode / max | Label | Basis |
|---|---|---|---|
| Glass fibre (E-glass) | 40 / 55 / 70 % | S, E | the maker's laminates 35 to 60 % and the populated boards 46 to 72 %; the mode between a 1.6 mm board of 7628 (60 %) and a dense board of thin plies (42 to 55 %) |
| Bromine (of the flame retardant) | 4.4 / 8.8 / 13.2 % | E | one source, about 15 % TBBPA in the laminate, 58.8 % of it bromine; half to 1.5 times, as every estimate |
| Epoxy | the remainder (17 to 56 %) | E | its recipe in the file (amine-cured); FR-4 is cured with dicyandiamide, near enough for carbon, hydrogen, oxygen and nitrogen |

**An approximation, said with its direction:** the components' bodies (moulding compound filled with silica, ceramic
capacitors of barium titanate, silicon dies) are counted as glass and epoxy, as in the populated boards' analyses:
silicon is about right, barium and titanium are missing (low), and the glass's calcium, boron and aluminium slightly
high.


### E5.20 The entry: what each agreed outcome landed in (2026-10-29, on "Yes, build it")

Matthias: "Yes, build it" (the entry, HANDOVER.md, points 1 to 10 with the recommendations for A to D); during the
build "only if it is exclude due to a limit given in the code" (check 20 removed) and "With Copper" (the nickel strip).
Checked in VERIFICATION.md V69.

| Outcome | Where it lands |
|---|---|
| E5.17: the TRON 2 not assigned; type 1 31 robots | `tools/make_humanoid_register.py`, row 309 and `TAKEN_APART` (31 numbers, the K1 "Booster K1 5 Ah; Booster K1 2 Ah") |
| Every robot its own rows (point 2, decision A) | `tools/make_parts_taken_apart.py`: the G1, X1, N1 as before; one block each for the 29 others (`ROBOTO_ORIGIN` to `YMBOT_E3`), `robot_rows()`; `g1_plus_rows()`, `asimov_two_rows()` |
| E5.12 points 1 to 4: the actuators | the sheet Joints, module masses per joint (the stated masses, `DM_J10010L` to `QM060`; `from_torque()` over 87.3 N·m/kg); class by `LARGE_FROM_NM` 55 N·m; inside as JointParts (02 `draw_robot`) |
| The placement of each actuator | the Asimov 1's from Menlo's mechanical page (AS1, read 2026-10-29: the actuator at each joint); the RP1's from RoboParty's ROMOMO introduction; the Roboto Origin's, T1's, K1's, PM01's and R1's from their models' torque limits; **the AI Sapiens K1's and the K0's not stated by ROBOTIS: an estimate (E)**, the larger actuators at the hips, knees, waist and (the K1's eleven) the ankle pitch, written in their rows |
| E5.12's table, the RP1 | at the agreed modes (point 3, the RMM8463-2E 0.7 kg) its actuators are 18.8 kg; the table gave 19.2 kg with the RMM8463-2E at its bound, 0.8 kg |
| E5.14 point 1: the masses | the sheet Constants, 'Robot mass, with battery' of each robot |
| E5.14 points 2 and 3: battery | Constants voltage and capacity (± 5 %), or the shared 'Battery energy per kg of robot' (6 / 12 / 18); the pack's stated mass or the shared 'Battery pack, Wh per kg (packs not weighed)' (109.3 / 164 / 232.5); the Asimov's pack without housing |
| E5.14 point 4: boards | the sheet Boards, one row per board named (the template's `COMPUTER`, `POWER`, `BATTERY_BOARD`, `SMALL_BOARD`, the modules `AGX_ORIN`, `ORIN_NX`, `RADXA_CM5`); the RP1's 13 boards in the robot (its e-stop transmitter and charger board are accessories) |
| E5.14 points 5 to 9 | cables (Constants), XT30 connectors two per joint, screws, shell (the shared 'Shell, share of the robot mass'), sensors (by their car sensor types; a sensor without a mass its elements only), frame (the remainder) |
| E5.17 point 1: robots without torques | the sheet Joints, 'Share of the joint modules' (one row per joint group, the shares of batch 1 on average, `average_joints()`), the shared 'Joint modules, share of the robot mass' (24.5 / 49 / 73.5 %) |
| E5.17 points 5 to 7 | the G1+ (the G1's rows and two head joints), the PrimeBOT Q1's mass (9.75 / 19.5 / 29.25 kg), the Asimov 2 (the Asimov 1 times 38 / 35) |
| E5.18: the grades | the column Grade (JointParts, Parts, Shares); the recipes in `data/researched/element_recipes.xlsx` (20CrMnTi, GCr15, 42CrMo4, C45, P20, 17-4PH, Ti-6Al-4V, and the mixtures 'Gear stage 2 steel: 20CrMnTi and GCr15', 'RP1 frame steel: C45 and P20'); M19, M27 and Type 304 read where they lie (`data.traction_motor_steels`); 01 `check_grades`, 02 `Shared.grade_elements` |
| E5.19: Mixed, brass | the sheet Shares: the battery housing (nickel strip with the copper, copper, plastics, housing 'Aluminium or Plastics' or the PM01's aluminium); the X1's grippers two small joints; the RP1's brass parts |
| Decisions C and D | the scaled drawing removed from 02 (and its notes and tests); check 20, `parts.draws`, `parts.seed` and the old page removed |

**Found while entering, Matthias's data:** RAWCLICVehicleTractionMotor's element workbook, sheet CastFeSteel, rows 16
and 17: Type 304's chromium 0.18 at its minimum (cell H16) and 0.02 at its maximum (H17). E5.18 wrote "the sibling's
limits (Cr 18 to 20 ...)": the standard's range, which the sheet's maximum row did not hold. 01's `check_grades`
reported it. **Corrected** on his word ("Yes, correct it", 2026-10-29): H17 0.20, the one cell changed (V70).

**Estimates made while entering** (each E, in its row of the builder):

| Point | Entered |
|---|---|
| AI Sapiens K1, K0 | ROBOTIS states only how many of each actuator: the larger at the hips, knees and waist (the K1's eleven also at the ankle pitch) |
| X1 shafts and pins | 17-4PH 25 / 50 / 75 % of the part, C45 the remainder |
| RP1 frame steel, screws | P20 4 of its 28 steel parts by count (7.14 / 14.29 / 21.43 % of the steel), C45 the remainder; its screws split 753 : 61 by number (12.9 against 304) |
| K1 5 Ah | the Education version's Jetson Orin NX; the Professional's AGX Orin not drawn |
| Joint counts (encoders, connectors only) | E1 26, QUESTER1 28, LightBot-0, LUMO and YMBOT E3 24 |
| "Composite" shells | the Bumi's, AKINCI-5's and Totan O1's drawn as plastics |
| X1 | 62 encoders and 62 connectors, two per joint with its grippers |
| Head joints | in the figures' kind Head (02's standard tables: the part group Sensors) |
| Sensors without a mass | drawn by their elements only, their mass in the frame |

**Agreed:** Matthias, 2026-10-29, choosing the answer offered: "I agree with the estimates made while building the
entry, as listed."

**Not entered, as not in E5.14's list:** fans and heat sinks of the 29 robots (their mass is in the frame); the RP1's
30 V auxiliary battery (said so in E5.14), the bearings outside its actuators and its 80 small magnets in the covers;
Sprout's four time-of-flight sensors; the PM01's navigation LiDAR and the K1 Professional's AGX Orin (other versions).

**Since entered** (Matthias, 2026-10-29: "Can we go through the open items and decide pragmatic solutions", "Yes
build a pragmatic solution list", "Yes, build them"; HANDOVER.md, point 4; VERIFICATION.md V76), each out of its
robot's frame, the estimates agreed with the list:

| Part | Robots | Entered as | Label |
|---|---|---|---|
| The computer's cooler, ARM board (a Jetson, Rockchip, Radxa, Qualcomm, RDK, or not named) | 25 and the T1's Jetson | a fan as the G1's main board fan, 5 / 10 / 20 g (its copper winding by the sheet Shares); the G1's aluminium heat sink, 50 / 100 / 200 g | E |
| The computer's cooler, Intel or AMD laptop-class processor | AKINCI-5, JAKA π, YMBOT E3, the T1's Express-i7 | a fan as above; the X1's and N1's copper heat pipes and fins, 0.055 / 0.12 / 0.19 kg | E |
| The RP1's fans | RP1 | its BOM (RP1a): a main-board fan and two waist fans, each as the G1's; its heat sink as an ARM board's | E |
| The RP1's 30 V auxiliary battery | RP1 | its BOM: two "小电池" (small batteries), no data; RP1d "30V auxiliary battery" (third party): cells 0.12 / 0.25 / 0.5 kg (30 V × 1 / 2 / 4 Ah over the NMC cells' 241.5 Wh/kg), NMC as its main pack | E |
| The RP1's bearings outside its actuators | RP1 | its BOM: 9 parts of bearing steel; each as the X1's on average (0.8 kg over 21), 0.019 / 0.0381 / 0.0572 kg; GCr15 | E |
| The RP1's magnets in its covers | RP1 | its BOM: 80 × N52 NdFeB, 4 × 4 and 4 × 2 mm, how many of each not stated; each 0.188 / 0.283 / 0.377 g (all of the small size to all of the large, sintered NdFeB about 7.5 g/cm³); grade class N | S, E |
| The Sprout's time-of-flight sensors | Sprout | SP1 "4 time-of-flight sensors"; no such type in the car sensor file: each the elements of the LiDAR's laser diode array and photodetector array; 5 / 10 / 20 g each | E |

The PM01's navigation LiDAR and the K1 Professional's AGX Orin stay out: they are of other versions than those drawn.

Matthias, 2026-10-29: "Have you research for the missing data I also want a qualification of the numbers you have. Do
they come from manufature. It is also not just the weight but at ;east the full composition Cu, etc.", "Essential is
not only the mass, the composition. Mass is not enough.", "It is enough to have the total amount of Cu, Gold etc. we do
not need to split it into different parts. If the information is available, then perfect. Use it", "The type of
motors and its enery allows to calculated its approximate composition in therms of Cu, rear earth mognet, electronic
steell aluminum aloys etc.", then "Yes do it". The agreed specification is in HANDOVER.md (2026-10-29, "Research of
the 32 robots of type 1"). Here: for each robot of batch 1 what its sources give for its composition (motors, battery,
boards, structure), each source qualified. **No min / mode / max is proposed:** that follows once Matthias has seen
these tables.

**How read:** every page through the web-fetch tool on 2026-10-29, HTML only, quoted as the page gives it; no PDF,
workbook, CAD or model file downloaded (those are listed at the end, for his yes). **Batch 1:** the 8 robots of type 1
with the most published hardware (268, 37, 269, 54, 148, 234, 311, 19). The G1, X1 and N1 have their own parts (E2) and
are not in it. **Tags:** *maker* = the maker's own page, documentation or repository; *third* = a reseller, a news
site or a catalogue; *spec* = a stated specification; *model* = a simulation model's value (URDF); *claim* = a
marketing statement; *arith.* = Claude's arithmetic, stated nowhere. No source of batch 1 gives a measured value.

### E5.1 Roboto Origin (268, RoboParty, Shanghai)

| What | Value as given | Source | Kind |
|---|---|---|---|
| Motors | 14 × "DM 4340P (48V)", 9 × "DM 10010L" (23 joints); no torque, mass or type on the page | BOM, github.com/Roboparty/roboto_origin/blob/main/assets/BOM_EN.md ("Internal Roboto D-BOM", 20260105, "ATOM 01 v1.0.1") | maker, parts list (names, quantities, CNY prices) |
| Battery | "48V 15Ah Li-ion pack", 140 × 140 × 115 mm; 720 Wh | the same BOM, line 27 | maker, spec in the name; Wh arith. |
| Boards | "RDK X5 8G" compute board; USB hub, 4 USB-to-CAN, DC-DC 48 V to 5 V, power distribution board, 4 CAN adapter boards; sensor "Chaohe HI13 M0-USB" | the same BOM | maker, parts list |
| Structure | 25 CNC parts "120-grit sandblasting / black anodizing" (metal not named; anodising points to aluminium, not stated); 3D-printed rubber soles; steel screws by GB/T standards (material not stated); bearings (one 130 × 165 × 18 mm) | the same BOM | maker, parts list |
| Mass, height | 34 kg, 1.25 m | humanoidroboticstechnology.com, "Source: Roboparty" | third, repeating the maker |

Gives: the motors by name and number, the battery's energy and chemistry, the boards by name. Missing: the motors' mass
and make-up (the maker of the "DM" motors is not named in the BOM; its datasheets are not read yet), the structure's
metal, every part's mass. Not read: RoboParty's documentation site (roboparty.com/roboto_origin/doc), the repositories
rpo_hardware (CAD, PCB) and rpo_description (URDF with link masses).

### E5.2 Asimov 1 (37, Menlo, open-source)

| What | Value as given | Source | Kind |
|---|---|---|---|
| Motors | 25 joints: EC-A6416-P2-25 × 3 (40 / 120 N·m rated / peak), EC-A5013-H17-100 × 4 (30 / 90), EC-A3814-H14-107 × 4 (20 / 60), EC-A4315-P2-36 × 4 (25 / 75), EC-A4310-P2-36 × 10 (12 / 36; at the ankles 40 / 145.4 and 17 / 57.6, unexplained); motor type, gearbox, mass, magnet not stated | docs.menlo.ai/asimov/1/overview/system-tour/mechanical; counts docs.menlo.ai/asimov/1/build/assembly-preparations/part-organisation | maker, spec; the page marks its mechanical tables as possibly out of date |
| Battery | Li-ion "INR18650", 13S4P (52 cells), 46.8 V, 10.5 Ah, 491.4 Wh, "Approximately 2 kg" | docs.menlo.ai/asimov/1/overview/system-tour/electrical | maker, spec ("Current specification") |
| Boards | Radxa CM5 on a carrier board (motion control), Raspberry Pi 5 with Media HAT, head board, power distribution board; 6-axis IMU, 2 MP camera, microphones, 10 W speaker | the same page | maker, spec |
| Structure | "7075 aluminum and MJF PA12 nylon" | the mechanical page | maker, spec (possibly out of date) |
| Mass, height | "Approximately 35 kg", "Approximately 1.2 m" | docs.menlo.ai/asimov/1/bom (served the overview) | maker, spec |

Gives: every motor by model and torque, the battery completely (cells, energy, mass), the structure's two materials.
Missing: the motors' mass and make-up (the maker of the "EC-A" actuators is not named by Menlo), part masses. The full
parts list sits behind an e-mail form (tally.so/r/jaG0va); the CAD files are on github.com/asimovinc/asimov-1, the URDF
with link masses on github.com/menloresearch/asimov-1: not opened.

### E5.3 RP1 (269, RoboParty)

| What | Value as given | Source | Kind |
|---|---|---|---|
| Motors | 24 joints (Pro 30); ROMOMO modules RMM10062-2E (48 V, ratio 22, 44 / 160 N·m rated / peak), RMM6562-2E (48 V, 19.5, 10 / 35 N·m), RMM8463-2E (drawing only); which module at which joint not stated; "inner-rotor motors", "two-stage planetary" | github.com/Roboparty/ROMOMO (values "transcribed from the published specification and test-report PDFs"); motor type and gearbox only cnx-software.com/?p=178402 | maker, spec; third |
| Battery | "48V main lithium battery", "30V auxiliary battery", "10Ah dual-battery system" | cnx-software.com/?p=178402 | third only |
| Boards | 14 boards named with part numbers (main board RBE-MAIN-RK3588S, IMU board, power boards ...); Rockchip RK3588, 8 GB, 32 GB eMMC; Pro also a Jetson Orin NX 16 GB | github.com/Roboparty/RP1_hardware/blob/main/02_PCB/README.md; processors cnx-software | maker (boards); third (processors) |
| Structure | "AL6061" limbs, "AL7075-T6" foot plates, polycarbonate chest, resin covers, polyurethane bumpers | cnx-software.com/?p=178402 | third only; the maker's CMF tables (XLSX) not opened |
| Mass, height | about 39 kg (Pro 41 kg) "including battery and end effectors", 1.35 m | cnx-software.com/?p=178402 | third only |

Gives: the joints' torque classes, the boards by name. Missing at the maker's HTML pages: mass, battery, materials,
which module where. The maker publishes them in files: the whole-robot BOMs RP1.3.4 (5 DOF and 7 DOF arms, sheet
"总BOM" with material information), the CNC, 3D-print and rubber BOMs and their CMF tables (XLSX), the ROMOMO test
reports and drawings (PDF), the CAD (ZIP), the URDF (github.com/Roboparty/RP1_description): **downloads, his yes**.

### E5.4 Booster T1 (54, Booster Robotics)

| What | Value as given | Source | Kind |
|---|---|---|---|
| Motors | 23 joints (head 2, arms 4 each, waist 1, legs 6 each); "Max Joint Torque: 130 N·m", dual encoders; model, type, mass not stated | docs.booster.tech/docs/product-manual/t1/getting-started/specifications/ (counts); torque uk.robotshop.com | maker (counts); third (torque) |
| Battery | 10.5 Ah Li-ion; voltage not stated; "Battery Life 2h" | chipsilicon.pages.dev (capacity); generationrobots.com lists a "10.5 Ah Battery for Booster T1"; life docs.booster.tech | third (capacity); maker (life) |
| Boards | Jetson AGX Orin 32 GB, motion board "Express-i7" (Standard); depth camera, microphone array | docs.booster.tech T1 specifications | maker, spec |
| Structure | not stated | – | – |
| Mass, height | "About 30kg", 1.18 m | docs.booster.tech T1 specifications | maker, spec |

Gives: the joint count and the boards from the maker. Missing: the motors' make-up, the battery voltage (so no Wh), the
structure. The URDF files T1_23dof.urdf (link masses) are in github.com/BoosterRobotics/booster_assets: not opened.

### E5.5 Booster K1 (148, Booster Robotics)

| What | Value as given | Source | Kind |
|---|---|---|---|
| Motors | 22 joints (head 2, arms 4 each, legs 6 each, no waist); "Max Peak Torque: 60 N·m" (joint not named); dual encoders | docs.booster.tech/docs/product-manual/k1/getting-started/specifications/, booster.tech/booster-k1 | maker, spec |
| Motors, per joint | peak torques 60, 50, 36, 14 and 7 N·m | a search result's summary of a RoboCup team sheet (RFC Tsudanuma, hsl.robocup.org); the PDF not opened, so not read first-hand | third, not read |
| Battery | Geek 2 Ah, Education and Professional 5 Ah, "magnetic battery"; voltage not stated by Booster (48 V only in a search result's summary of RoboCup team sheets, not read) | docs.booster.tech K1 specifications | maker (Ah); third, not read (V) |
| Boards | Geek ARM processor (Qualcomm QCS8550 per a reseller); Education Jetson Orin NX 8 GB; Professional Jetson AGX Orin 32 GB; binocular depth camera, 9-axis IMU, microphones, speaker | docs.booster.tech, booster.tech/booster-k1; QCS8550 generationrobots.com | maker; third |
| Structure | not stated | – | – |
| Mass, height | "About 19.5kg", 0.95 m | docs.booster.tech K1 specifications | maker, spec |

Gives: joints, battery capacity by version, boards by version. Missing: the motors' make-up, the voltage from the maker,
the structure. Not opened: the K1 datasheet PDF (static.generation-robots.com/media/datasheet-booster-k1.pdf), the URDF
K1_22dof.urdf (booster_assets).

### E5.6 PM01 (234, EngineAI, Shenzhen)

| What | Value as given | Source | Kind |
|---|---|---|---|
| Motors | 24 joints: Q90H × 6 (hip pitch, hip roll, knee; 145 N·m, ratio 25, **1.1 kg**, 48 V), Q25H × 15 (ankles, arms, head; 50 N·m, ratio 25, **0.5 kg**, 48 V), Q25H-L × 3 (hip yaw, waist; no data); "Full Planetary"; "Ultra-High-Speed Internal Rotor Permanent Magnet Synchronous Motor"; crossed roller bearings | en.engineai.com.cn/open/docs/pm01/01/joint-system; motor type en.engineai.com.cn/product-pm01.html | maker, spec |
| Battery | "Cylindrical Lithium-ion Battery (Ternary Lithium System)", nominal 10 Ah, 46.8 V (13S, two in parallel by arith.), 468 Wh arith., "Total System Mass ≈2.95kg", housing "Aluminum Alloy" | en.engineai.com.cn/open/docs/pm01/01/peripheral-devices | maker, spec |
| Boards | NVIDIA Jetson Orin NX 16 GB; motion unit "Nezha" 4 cores, 8 GB; D435i depth camera and a waist camera; IMU YIS320 (7.7 g); Navigation edition a 3D LiDAR (Livox Mid-360 per EngineAI's navigation README) | en.engineai.com.cn/open/docs/pm01/01/hardware-information, /sensor-system; github.com/engineai-robotics/engineai_navigation | maker, spec |
| Structure | "Structural Material Aviation Aluminum" | en.engineai.com.cn/product-pm01.html | maker, spec |
| Mass, height | 43 to 44.5 kg with battery (three of EngineAI's own pages differ); 1400 mm by the dimension table, 138 cm by its home page; 40 kg third-party | en.engineai.com.cn/product-pm01.html, the development guide, engineai.com.cn | maker, spec (disagreeing); third |

Gives: the most complete set of batch 1 from the maker: every joint's motor with its mass (21 of 24), the battery with
its chemistry, energy and mass, the boards, the structure's material. Missing: the Q25H-L's data, the motors' make-up
(copper, magnet, steel), the shell. Not opened: the user manual PDF (product-support-pm01.html), the URDF
(github.com/engineai-robotics/engineai_robotics_description, folder pm01_edu).

### E5.7 Unitree R1 (311, Unitree Robotics)

| What | Value as given | Source | Kind |
|---|---|---|---|
| Motors | R1: 26 joints (legs 6 each, arms 5 each, waist 2, head 2; R1 Air 20); "Low inertia high-speed internal rotor PMSM"; crossed roller bearings; "Maximum Torque of Arm Joint: About 2kg" (a load); model, mass not stated | unitree.com/R1 | maker, spec |
| Motors, limits | joint effort limits 60 (hip, knee, waist, shoulder pitch and roll), 50 (ankles), 33 (shoulder yaw, elbow, wrist), N·m by the model's convention | github.com/unitreerobotics/unitree_ros, robots/r1_description/R1.urdf | maker, model |
| Battery | "Lithium battery", "About 1h"; voltage, Ah, Wh not stated | unitree.com/R1 | maker, spec |
| Boards | "8-Core High-Performance Processor"; EDU an optional module "such as Orin(40-100TOPS)"; binocular camera (Air monocular), 4 microphones, speaker | unitree.com/R1 | maker, spec |
| Structure | not stated | – | – |
| Mass, height | "About 29kg" with battery (R1, EDU), Air "About 27kg"; 1230 mm; "about 25kg" third-party | unitree.com/R1; cnx-software.com | maker, spec; third |

Gives: joints by region, the motor type, the boards; the URDF's link masses (R1 Air 26.68 kg in all, arith.; leg
5.81 kg each) as a model. Missing: the motors' make-up and mass, the battery's energy, the structure.

### E5.8 AI Sapiens K1 (19, ROBOTIS, Korea)

| What | Value as given | Source | Kind |
|---|---|---|---|
| Motors | 23 joints (arms 5 each, legs 6 each, waist 1): DYNAMIXEL-Q QC060-200-R020-RE × 12 (**435 g**, peak 30.0 N·m, 20:1) and QC080-240-R020-RE × 11 (**845 g**, 72.6 N·m, 20:1); "Low-inertia inner rotor PMSM", 48 V; continuous torque 10.6 / 24.2 N·m, power 200 / 240 W and masses 455 / 865 g on the product page | docs.robotis.com/docs/systems/aisapiens/specifications/hardware; robotis.com/en/product/dynamixel-q.php (marked "Preliminary") | maker, spec |
| Battery | "Li-ion 21700, 13S2P", cell "LG Energy Solution M50LT", 48 V, 10 Ah, "460.8 Wh" (48 × 10 = 480: does not add up; 46.8 V × 9.6 Ah would) | docs.robotis.com/docs/systems/aisapiens/specifications/electrical_system | maker, spec |
| Boards | NVIDIA Jetson Orin NX 16 GB, 256 GB SSD; HAT board (two STM32 MCUs), IMU board (ICM-42688-P or BNO085) | the same page | maker, spec |
| Structure | "Aluminium alloy frame with polymer covers"; covers 3D-printable | humanoid.guide (frame); docs.robotis.com (covers) | third (frame); maker (covers) |
| Mass, height | "Weight 35 kg", "Height 1355 mm" (K1); the K0 34 kg, 1300 mm, QM-060 × 14 and QM-080 × 9, 46.8 V 9 Ah | docs.robotis.com (K1); ai.robotis.com/ai_sapiens/introduction_ai_sapiens.html (K0) | maker, spec, "may change as the product approaches launch" |

Gives: every motor by model and mass (14.5 kg of motors in all, arith.), the battery's cell by maker and model. Missing:
the motors' make-up, the structure from the maker. Not opened: the K1 hardware drawing PDF (docs.robotis.com); the
parts list, STEP files "Coming soon".

### E5.9 Batch 1 together: what the sources give, and what is still missing

With the downloads and model files of E5.10 (read after Matthias's "Yes, download").

| Robot | Motors: count and kind | Motor masses | Battery: Wh, chemistry | Boards | Structure | Mass from the maker |
|---|---|---|---|---|---|---|
| 268 Roboto Origin | yes (BOM) | no | 720 Wh, Li-ion | yes (BOM) | anodised CNC parts, metal not named | 33.76 kg (its model) |
| 37 Asimov 1 | yes, torques | no | 491.4 Wh, 18650 cells, 2 kg | yes | 7075 Al, PA12 | 35 kg; model 35.55 kg |
| 269 RP1 | 24 modules of 3 sizes (BOM), torques | no | not stated by the maker | 15 boards (BOM) | every part's material (BOM) | 39.11 kg (its model) |
| 54 Booster T1 | count only | no | 10.5 Ah, no voltage | yes | no | 30 kg; model 31.74 kg |
| 148 Booster K1 | count, 60 N·m | no | 48 V 5 Ah, 240 Wh (reseller's datasheet) | yes | no | 19.5 kg; model 19.67 kg |
| 234 PM01 | yes, torques | 21 of 24 | 468 Wh, NMC cylindrical, 2.95 kg | yes | aviation aluminium alloy, rubber | 40 to 44.5 kg; model 40.92 kg |
| 311 Unitree R1 | count, PMSM | no | no | yes | no | 27 / 29 kg; model 29.14 kg |
| 19 AI Sapiens K1 | yes, torques | all 23 | 460.8 Wh, LG M50LT 21700 | yes | third only | 35 kg |

**What no maker of batch 1 states:** the copper, magnet and electrical steel inside a motor. For that the motors' own
datasheets are the next sources (the makers of the Roboto Origin's "DM" and the Asimov 1's "EC-A" motors, neither named
by the robot's maker; EngineAI's Q series; ROBOTIS's DYNAMIXEL-Q), and the one weighed robot joint motor of this
project, the G1's from China Post Securities' teardown (E2), the same kind. Whether car traction motors
(RAWCLICVehicleTractionMotor) represent a 0.5 kg robot joint motor is to be questioned before any use (his rule 1, same
kind).

**Downloads that would close most gaps, each his yes** (done on his "Yes, download", E5.10, but the Asimov 1 form,
which needs his e-mail address): RP1's whole-robot BOMs and CMF tables (XLSX,
github.com/Roboparty/RP1_hardware); the ROMOMO test reports (PDF); the Asimov 1 parts list (an e-mail form,
tally.so/r/jaG0va); the PM01 user manual (PDF, EngineAI's support page); the K1 datasheet (PDF, Generation Robots); the
AI Sapiens K1 hardware drawing (PDF, docs.robotis.com); the URDF files of the R1, T1, K1, PM01, Asimov 1, Roboto Origin
and RP1 (link masses, from the makers' GitHub repositories).

### E5.10 The downloads and the makers' model files (2026-10-29, on "Yes, download")

Downloaded into Claude's scratch folder (`downloads/`, one folder each; not into the project), read with openpyxl and
macOS's PDFKit (text only: the PDF page images could not be rendered, `pdftoppm` is not installed).

| File (size) | From | Kind | What it gives |
|---|---|---|---|
| RP1.3.4 BOM, 5-DOF arms (8.1 MB) and 7-DOF arms (8.4 MB) | github.com/Roboparty/RP1_hardware, 04_BOM | maker, parts list, "首发" 2026.9.10 | 422 and 460 rows (sheet 总BOM): every part's number, type, name, quantity and material ("材料要求"); the column "单件重量(Kg)" (unit weight) is **empty in every row**. Actuators: 5-DOF 12 × RMM6562-2E, 8 × RMM10062-2, 4 × RMM8463-2E (24); the 7-DOF adds 4 × RZW5552-2C (28). Materials named: AL6061-T6 (76 CNC parts), AL6061, AL7075, AL5052, steel 45 / AISI 1045 (24), P20 tool steel (4), PC, PU, TPU, ABS (28 printed), PLA (12), UFS9002 resin, EVA and EPP foam, EPDM rubber (8), screws of grade 12.9 steel (753), 304 stainless (61), N52 NdFeB magnets (80, 4 × 4 and 4 × 2 mm, in the covers), PA (18), bearing steel (9), brass (8). 15 boards (main board RBE-MAIN-RK3588S with an Orange Pi CM5, IMU board, power and capacitor boards, ...). Battery: "明美锂离子电池组" (a Mingmei lithium-ion pack) and 2 "小电池" (small batteries), no data. Fans: 2 waist fans, a main-board fan |
| ROMOMO hardware introduction V261013 (0.5 MB, 6 pages) | github.com/Roboparty/ROMOMO | maker, specification, 2026.10 | the three modules' rated / peak torque: RMM6562-2E 10 / 35 N·m (arms, wrists, ankles), **RMM8463-2E 20 / 87 N·m (shoulders, waist)**, RMM10062-2E 44 / 160 N·m (thighs, knees, hips); 48 V (24 to 60 V); driver boards with GaN (6562) or Si MOSFETs, a HPM5E3Y RISC-V controller, dual magnetic encoders, inside each module. No mass, no motor make-up |
| PM01 user manual V1.0 (0.8 MB, 9 pages) | EngineAI's support page (product-support-pm01.html; the server serves it only with that page as referrer) | maker, manual | "航空铝合金和橡胶等轻质材料" (aviation aluminium alloy and rubber), "整机重量约 40kg" in its text and "重量（含电池） 约43kg" in its table; 1388 mm; 23 DOF in its table; joint maximum 145 N·m, "全行星" (full planetary), peak torque density 130 N·m/kg; 10000 mAh battery, 54.6 V 4.5 A charger; local air cooling of the joints |
| Booster K1 datasheet (12.6 MB, 3 pages) | static.generation-robots.com | reseller's datasheet (Booster's figures, not Booster's document) | **battery 5 Ah, voltage 48 V** (240 Wh, arith.), 40 min walking; knee maximum 60 N·m; 22 DOF; 19.5 kg |
| AI Sapiens K1 hardware drawing (8.3 MB, 1 page) | docs.robotis.com | maker, drawing "FOR REFERENCE ONLY", 07/29/2026 | dimensions only (height 1355 mm, ...); its material field is empty in the text |

**The makers' model files** (URDF, raw text from each maker's GitHub repository; Claude's arithmetic: the sum of the
links' `<mass>`, a design model's values, not weighed):

| Robot | File | Links / moving joints | Sum of the links | Heaviest links |
|---|---|---|---|---|
| 268 Roboto Origin | Roboparty/rpo_description, urdf/rpo.urdf | 24 / 23 | 33.757 kg | torso 7.58, base 5.51, each thigh 2.35 kg |
| 37 Asimov 1 | menloresearch/asimov-1, sim-model/asimov_1_25dof/urdf/asimov_1_25dof.urdf | 26 / 25 | 35.552 kg | waist 8.67, pelvis 3.66, each knee 2.48 kg |
| 269 RP1 | Roboparty/RP1_description, urdf/rp1_24dof.urdf | 25 / 24 | 39.109 kg | waist 8.34, base 3.30, each knee 2.56 kg |
| 54 Booster T1 | BoosterRobotics/booster_assets, robots/T1/T1_23dof.urdf | 25 / 23 | 31.738 kg | |
| 148 Booster K1 | BoosterRobotics/booster_assets, robots/K1/K1_22dof.urdf | 25 / 22 | 19.666 kg | |
| 234 PM01 | engineai-robotics/engineai_robotics_description, pm01_edu/urdf/serial_pm01_edu.urdf | 31 / 24 | 40.921 kg | torso 9.01, each knee 4.29, base 4.09 kg |
| 311 Unitree R1 | unitreerobotics/unitree_ros, robots/r1_description/R1.urdf | 41 / 26 | 29.138 kg | |

Each model's sum lies within 0.5 to 1.7 kg of the maker's stated mass; for the Roboto Origin and the RP1 it is the only
mass from the maker. A link's mass holds its motor, structure and wiring together: the models give where the mass sits,
not what it is made of. The AI Sapiens K1's model is shown in ROBOTIS's viewer; no file was found.

**Still no maker states the copper, magnet or electrical steel inside a motor.** Next sources (not yet read): the
actuators' own datasheets (EngineAI's Q90H and Q25H, ROBOTIS's DYNAMIXEL-Q QC060 and QC080, the Roboto Origin's DM 4340P
and DM 10010L, RoboParty's ROMOMO drawings), and the G1's weighed joint (E2), the same kind of motor.

### E5.11 The actuators' own datasheets (2026-10-29, on "Yes, read them")

Matthias: "Yes, read them" (the actuators' datasheets of batch 1, the ROMOMO drawings included). EngineAI's and
ROBOTIS's pages read through the web-fetch tool; RoboParty's drawings and test reports and DAMIAO's handbook downloaded
into Claude's scratch folder (0.39 to 1.8 MB each) and read with PDFKit (the RMM8463-2E drawing, an image only,
rendered and read as a picture).

| Actuator (robot, count) | Mass | Rated / peak torque, ratio | Motor | Source | Kind |
|---|---|---|---|---|---|
| EngineAI Q90H (PM01, 6) | 1.1 kg | – / 145 N·m, 25, "Full Planetary" | internal rotor PMSM (robot page); Ø86 × 62 mm, 48 V | en.engineai.com.cn/open/docs/pm01/01/joint-system (same in Chinese) | maker, spec |
| EngineAI Q25H (PM01, 15) | 0.5 kg | – / 50 N·m, 25, planetary | Ø62 × 60 mm, 48 V | the same | maker, spec |
| EngineAI Q25H-L (PM01, 3) | not stated | not stated | – | the same (name only) | maker |
| ROBOTIS DYNAMIXEL-Q QC060-200-R020-RE (AI Sapiens K1, 12) | 455 g (product page), 435 g (K1 page) | 10.6 / 30.0 N·m, 20 | "Frameless BLDC" / "Low-inertia inner rotor PMSM"; 200 W; Ø58 × 60 mm | robotis.com/en/product/dynamixel-q.php ("Preliminary"); docs.robotis.com K1 hardware | maker, spec, preliminary |
| ROBOTIS DYNAMIXEL-Q QC080-240-R020-RE (AI Sapiens K1, 11) | 865 g / 845 g | 24.2 / 72.6 N·m, 20 | 240 W; Ø78 × 65 mm | the same | maker, spec, preliminary |
| DAMIAO DM-J4340P-2EC 48 V (Roboto Origin, 14) | 375 g | 9 / 27 N·m, 40 | 14 pole pairs, 33 W, 0.88 Ω; Ø57 × 56.5 mm | DAMIAO's 2025 product selection handbook (达妙科技 2025年产品选型手册, worldrobotconference.com), p. 13 | maker, spec |
| DAMIAO DM-J10010L-2EC (Roboto Origin, 9) | 1375 g | 40 / 120 N·m, 10 | 21 pole pairs, 418 W, 0.11 Ω; Ø120 × 53 mm | the same handbook, p. 20 | maker, spec |
| RoboParty RMM6562-2E (RP1, 12) | **533.1 g measured**; ≤ 530 g on the drawing | 10 / 35 N·m, 19.5 | 10 pole pairs, 62.8 W, 0.81 Ω; Ø65 mm; insulation class F (155 °C) | test report RMM6562-2E-关节模组测试报告-1013 ("数据来源于实验室测试": RoboParty's laboratory); drawing RMM6562-2EV1.0 (2026-09-02); github.com/Roboparty/ROMOMO | maker, measured (test report) and spec (drawing) |
| RoboParty RMM10062-2E (RP1, 8) | **1197 g measured**; < 1260 g on the drawing | 44 / 160 N·m (140 in the report's table), 22 | 14 pole pairs, 370 W, 0.179 Ω; Ø100 mm; class F | test report RMM10062-2E-…-1013; drawing RMM10062-2EV1.0 (2026-09-04) | maker, measured and spec |
| RoboParty RMM8463-2E (RP1, 4) | < 800 g | 20 / 87 N·m, 20 | 10 pole pairs, 87.9 W, 0.163 Ω; Ø84 × 63 mm; class F | drawing RMM8463-2EV1.0 (2026-09-04, image) | maker, spec |

**From the test reports, the heat of a joint:** the RMM6562-2E at its rated load (60 rpm, 10 N·m, 60 minutes, 25 °C
room) reached a motor temperature of 71.2 °C, a winding rise of 43.8 K; its heat sink 52.4 °C. Measured, one module.

**The motors' mass in each robot** (Claude's arithmetic from the masses above; the maker's model sum of E5.10 for the
share):

| Robot | Motors | Their mass | Share of the robot |
|---|---|---|---|
| 268 Roboto Origin | 14 × 375 g + 9 × 1375 g | 17.6 kg | 52 % of 33.8 kg |
| 269 RP1 (5-DOF arms) | 12 × 533.1 g + 8 × 1197 g + 4 × < 800 g | < 19.2 kg | < 49 % of 39.1 kg |
| 234 PM01 | 6 × 1.1 kg + 15 × 0.5 kg + 3 × Q25H-L (not stated) | 14.1 kg and the three | 33 % of 43 kg and the three |
| 19 AI Sapiens K1 | 12 × 435 g + 11 × 845 g (K1 page) | 14.5 kg (15.0 by the product page) | 41 % of 35 kg |

**What none of them states:** the copper of the winding, the magnet's mass and grade, the electrical steel, the
housing's alloy, the gears' steel, inside an actuator. The datasheets give the size, the pole pairs, the power and the
winding's resistance, not what the actuator is made of. The one robot joint actuator of this project taken apart and
weighed part by part is the G1's (E2, China Post Securities), the same kind (a planetary joint module with an inner-rotor
PMSM and its driver board). Next, for Matthias's yes: a proposal of how each actuator's mass above becomes its elements
(the G1's weighed shares, questioned for size and gear type), sources first.

### E5.12 Proposal: each actuator of batch 1 from its mass to its elements (2026-10-29). Agreed, entered 2026-10-29 (E5.20)

Matthias: "Yes, propose it" (how each actuator's mass becomes its elements, from the G1's weighed joint, questioned for
size and gear type, sources first). The method is the one already agreed for the X1 and N1 (E2.8e, "Accept all" of
2026-10-27); new are only the actuators' masses (E5.11) and the estimates where no mass is stated. The numbers below are
at the modes, Claude's arithmetic, to show the order of magnitude; the run draws every share and mass from its min /
mode / max.

| # | What | Proposal |
|---|---|---|
| 1 | **Inside each actuator** | The G1's weighed small or large joint (E2.2; builder's sheet JointParts), scaled to the actuator's own mass, the joint's structure (housing, end caps, output flange, small bearings) the remainder, as for the X1 and N1. The class: small below 55 N·m peak torque, large from 55 N·m (E: the geometric middle of the G1's small, 35 N·m, and large, 88 N·m). At the modes the shares are small / large: copper 8.3 / 7.6 %, NdFeB 7.4 / 6.8 %, electrical steel 10.6 / 9.8 %, other steel 41.5 / 45.8 %, aluminium 25.9 / 21.9 %, plastics 3.9 / 3.6 %, driver board 2.4 / 4.5 %; the class moves a share by at most 4.3 percentage points |
| 2 | **Materials to elements**, all as agreed for type 1 | Stator copper 23 / 36 / 45 % of the stator, its coating 2 / 5 / 10 %, electrical steel the remainder; rotor NdFeB 45 / 90 / 100 %, steel the remainder; the NdFeB's grade drawn for the joint's heat group (sheet MagnetGrades: hips, knees, waist and ankles hot), its elements from RAWCLICVehicleTractionMotor's own code; aluminium by type 1's recipe; the driver board's area scaled with it, its metals the car board category's mg per cm²; steel and electrical steel without a recipe yet (their Fe, Si, Cr, Ni, Mn wait on E1.4) |
| 3 | **Masses stated by the maker** (E5.11) | The maker's figure the mode; where the maker gives two, the other figure the bound (QC060 435 / 455 g, QC080 845 / 865 g, RMM6562-2E 530 / 533.1 g, RMM10062-2E 1197 / 1260 g); a single figure ± 5 % (E, the spread between units: Q90H, Q25H, DM-J4340P, DM-J10010L); the RMM8463-2E "< 800 g" 0.35 / 0.7 / 0.8 kg (E, at least half its mode, cut at the stated bound) |
| 4 | **Masses not stated** (E) | Each joint's peak torque (the datasheet's; where none, the maker's model's effort limit, E5.10) divided by the peak torque density of the nine actuators read: 65.7 / 87.3 / 133.7 N·m/kg (min / median / max: RMM6562-2E, DM-J10010L, RMM10062-2E), widened to at least half to 1.5 times its mode (his rule for estimates). Gives the actuators of the **Asimov 1** 9.3 / 18.6 / 27.8 kg, **Booster T1** 7.5 / 14.9 / 22.3 kg, **Booster K1** 4.6 / 9.2 / 13.8 kg, **Unitree R1** 7.3 / 14.6 / 21.9 kg (47 to 53 % of each robot at the mode). The PM01's **Q25H-L** as the Q25H instead (the same family, the same 61 N·m in EngineAI's model): 0.25 / 0.5 / 0.75 kg each |
| 5 | **Questioned: the same kind as the G1's joint** (inner-rotor PMSM, two-stage planetary, driver board inside) | EngineAI Q series: inner-rotor PMSM, "Full Planetary" (maker): the same kind. RoboParty ROMOMO: driver board inside (maker), inner rotor and two-stage planetary (third party): the same kind. ROBOTIS DYNAMIXEL-Q: inner-rotor PMSM (maker), gear type not stated, single-stage by a catalogue (third): with one stage, the G1's two-stage shares overstate the steel and understate the copper and magnet. DAMIAO: motor and gear type not stated. Asimov 1's EC-A models: "P2" and "H14 / H17" read as planetary and harmonic gears from the names only, not stated by Menlo; a harmonic gear is steel as well, its share against the motor not known. Each is written next to its robot; none is corrected without a source |
| 6 | **Not in this proposal** | The rest of each robot (the battery's cells from its Wh and chemistry, the boards, cables, frame and shell), the steel recipe, and how 02 draws each robot from its own totals: the next steps, each for his yes |

**Agreed:** Matthias, 2026-10-29, choosing the answer offered: "I agree with the actuator proposal of E5.12, points 1 to
6, including its estimates." Not entered: where and how it enters the data and 02 is a step of its own, for his yes.

**What it gives at the modes, the actuators only:**

| Robot | Actuators (kg) | Copper (kg) | NdFeB (kg) | Mass basis |
|---|---|---|---|---|
| 268 Roboto Origin | 17.6 | 1.38 | 1.23 | DAMIAO's handbook |
| 269 RP1 | 19.2 | 1.51 | 1.34 | RoboParty's test reports and drawings |
| 234 PM01 | 15.6 | 1.25 | 1.11 | EngineAI's guide; Q25H-L as the Q25H (E) |
| 19 AI Sapiens K1 | 14.5 | 1.14 | 1.02 | ROBOTIS (preliminary) |
| 37 Asimov 1 | 18.6 (E) | 1.44 | 1.29 | estimate from its torques |
| 54 Booster T1 | 14.9 (E) | 1.16 | 1.04 | estimate from its model's torques |
| 148 Booster K1 | 9.2 (E) | 0.73 | 0.65 | estimate from its model's torques |
| 311 Unitree R1 | 14.6 (E) | 1.14 | 1.02 | estimate from its model's torques |
| *for comparison: Unitree G1* | *17.25 (weighed: 9 × 1100 + 14 × 525 g)* | *1.36* | *1.22* | *E2.2* |

### E5.13 The rest of each robot of batch 1: the sources (2026-10-29, on "Yes, go on")

Matthias: "Yes, go on" (the rest of the batch 1 robots: battery cells, boards, cables, frame and shell, sources first,
then propose). Searched on the web (search results only where marked), and the sources of E5.1 to E5.11.

**Batteries**

| Robot | Energy, chemistry, cells | Pack mass | Source | Kind |
|---|---|---|---|---|
| 268 Roboto Origin | "48V 15Ah Li-ion pack", 720 Wh (arith.); 140 × 140 × 115 mm, 2.25 l: 320 Wh/l, an NMC pack's density, not an LFP's (Claude's reading, E); cells not named | not stated | its BOM (E5.1); the pack's maker "孚小二" not found on the web | maker, parts list |
| 37 Asimov 1 | Li-ion INR18650, 13S4P (52 cells), 46.8 V, 10.5 Ah, 491.4 Wh; cell maker not named | "Approximately 2 kg" | docs.menlo.ai, electrical (E5.2) | maker, spec. **Does not add up:** 52 cells of 2.6 Ah weigh about 45 g each, 2.3 kg, more than the pack; 491.4 Wh in 2 kg is 246 Wh/kg, a cell's density with no housing |
| 269 RP1 | "明美锂离子电池组" (Mingmei Li-ion pack) and 2 "小电池" (small batteries); 48 V, 10 Ah (480 Wh) and a 30 V auxiliary pack only from a news site | not stated | its BOM (E5.10); cnx-software (E5.3) | maker (names); third (values) |
| 54 Booster T1 | 10.5 Ah, Li-ion; voltage not stated anywhere | not stated | chipsilicon, Generation Robots (E5.4) | third |
| 148 Booster K1 | 48 V, 5 Ah (Education, Professional; 240 Wh), 2 Ah (Geek; 96 Wh) | not stated | Booster's docs (Ah); Generation Robots' K1 datasheet (48 V) | maker (Ah); reseller (V) |
| 234 PM01 | "Cylindrical Lithium-ion Battery (Ternary Lithium System)", 13S2P, 46.8 V, 10 Ah, 468 Wh (arith.) | "≈2.95kg" | EngineAI's guide, peripherals (E5.6) | maker, spec |
| 311 Unitree R1 | 6000 mAh at 33.12 V (199 Wh) or 32.4 V (194.4 Wh), 9 cells in series (arith.) | not stated | resellers' battery listings (maverickdrone, globaldronehq, search results; one says the 199 Wh are "according to Unitree") | third, not read first-hand |
| 19 AI Sapiens K1 | Li-ion 21700 13S2P, LG Energy Solution M50LT, 48 V, 10 Ah, "460.8 Wh" (26 × 18.2 Wh = 473 Wh, arith.); the M50LT NCM / graphite, about 68 g and 18.2 Wh | not stated | docs.robotis.com electrical (E5.8); the M50LT from LG-branded specifications on third-party sites (dnkpower, nkon; LG's own page not found) | maker (pack); third (cell) |
| *template: G1, X1, N1* | *421, 355, 475 Wh* | *2.5, 2.2, 2.9 kg: 168, 161, 164 Wh per kg of pack* | *E2.8e, accepted* | |

**Compute modules** (search results; NVIDIA's, Raspberry Pi's and D-Robotics' own datasheets not read): Jetson AGX
Orin 100 × 87 mm (87 cm²); Jetson Orin NX 69.6 × 45 mm (31.3 cm², about 26 g by one retailer); Radxa CM5 55 × 40 mm
(22 cm²); Raspberry Pi CM5 55 × 40 mm, 14 to 16 g; the RDK X5's and the Raspberry Pi 5's sizes not found. No carrier
board, power board or battery management board of batch 1 has a size from its maker.

**Cables:** the Roboto Origin's BOM lists its motor cables by length: 4 × 40, 4 × 20, 2 × 10 cm (wire01), 2 × 40, 8 ×
20, 2 × 10 cm (wire02), 10 × 40, 4 × 20 cm (wire03): **10.0 m** (arith.). RP1's harness BOM is a file in
github.com/Roboparty/RP1_hardware, 03_Harness, not downloaded. The Asimov 1 and the AI Sapiens K1 use XT30 (2+2)
connectors at every actuator (maker). No other robot of batch 1 gives a cable length.

**Frame and shell:** materials as their makers name them (E5.2, E5.6, E5.10): Asimov 1 "7075 aluminum and MJF PA12
nylon"; PM01 "aviation aluminium alloy and rubber"; RP1 every part (AL6061-T6 in 76 CNC parts, steel 45 / AISI 1045 in
24, P20 in 4, AL7075, AL5052; shells of ABS, PLA, PC, resin; PU, TPU, EPDM, EPP and EVA foam; about 850 screws of grade
12.9 steel and 304 stainless); Roboto Origin 25 CNC parts "black anodizing" (anodising is aluminium's treatment; the
metal itself not named), 3D-printed soles. No part mass from any maker; the robots' masses from their makers' models
(E5.10).

### E5.14 Proposal: the rest of each robot of batch 1 (2026-10-29). Agreed, entered 2026-10-29 (E5.20)

The template already agreed for the G1, X1 and N1 (E2.8 to E2.8e), filled from each robot's own sources (E5.13). Only
the inputs are new; the drawing and the element recipes are those of type 1.

| # | What | Proposal |
|---|---|---|
| 1 | **The robot's mass** (for the frame's remainder) | The maker's stated mass the mode (its model's sum where it states none); the bounds the lowest and highest of its stated masses, its model's sum and the mode ± 1 kg (E, as the G1's): Roboto Origin 32.8 / 33.8 / 34.8 kg (model), Asimov 1 34 / 35 / 36, RP1 38.1 / 39.1 / 40.1 (model), Booster T1 29 / 30 / 31.7, Booster K1 18.5 / 19.5 / 20.5, PM01 40 / 43 / 44.5 (its manual's 40 kg, its editions' 44.5 kg), Unitree R1 28 / 29 / 30, AI Sapiens K1 34 / 35 / 36 (the K0's 34 kg) |
| 2 | **Battery cells** | Energy = voltage × capacity as the maker states them, ± 5 % (the N1's accepted production tolerance); the cells NMC cylindrical (stated "ternary" or NCM for the PM01 and AI Sapiens K1; for the others Li-ion without chemistry, E, as type 1's robots); their mass the energy ÷ the NMC cells' 232.5 / 241.5 / 256 Wh/kg (E1.7d), their elements by the NMC recipe (E1.7i). Where no voltage is stated: the Booster T1 at 48 V as its sibling K1 (E: 504 Wh); the RP1 at the news site's 48 V 10 Ah (E: 480 Wh, its 30 V auxiliary pack not known, left out and said so); the R1 at the resellers' 194.4 / 199 Wh. The K1 drawn as one of its versions, 5 Ah (Education, Professional) or 2 Ah (Geek), each as often (a discrete state, never blended) |
| 3 | **Battery pack** | The maker's pack mass where stated (PM01 2.95 kg; Asimov 1 "about 2 kg" is less than its cells: the cells kept, the pack's housing 0, and said so); else the energy ÷ 164 Wh/kg (E: the median of the G1's, X1's, N1's and PM01's packs, 159 to 168), its minimum cut at the cells (as the X1's and N1's, "Cut at the cells"), its maximum 1.5 times its mode. Housing the pack less its cells, as type 1 |
| 4 | **Boards** | Inside the actuators: E5.12. The rest by the template's kinds and area ranges (G1, X1, N1; E2.8, E2.8e), one row per board the maker names: compute modules at their stated size (AGX Orin 87 cm², Orin NX 31.3 cm², Radxa CM5 22 cm², ± 5 %), their carrier or base board 60 / 120 / 180 cm² (E, as the X1's and N1's computer boards); power distribution 30 / 60 / 100 cm², battery management 30 / 60 / 96 cm², head, IMU and other small boards 5 / 15 / 30 cm² (E, as the G1's); RP1's 15 boards each by its kind; the boards' metals the car board category of their kind, as type 1 |
| 5 | **Cables and connectors** | The Roboto Origin's listed 10.0 m, 10 / 10.5 / 12 m (E for cables not in its BOM); every other robot 5 / 10 / 15 m (E, as the N1), the K1 3 / 6 / 10 m (E, as the G1, a smaller robot); four conductors, copper and insulation as type 1; XT30 (2+2) connectors two per joint (stated for the Asimov 1 and AI Sapiens K1; E for the others, as type 1) |
| 6 | **Shell** | 11.5 % of the robot's mass at the mode (E: the median of the G1's 12.9, the N1's 11.5 and the X1's 9.1 %), half to 1.5 times; plastics, with the makers' named materials where they exist (RP1, Asimov 1 PA12, PM01 rubber) |
| 7 | **Screws, bearings outside the actuators** | RP1 about 850 screws: 0.26 / 0.52 / 0.78 kg (E, scaled from the X1's 0.6 kg for 980); the others 0.2 / 0.5 / 1 kg (E, as the G1's); steel |
| 8 | **Sensors** | Each camera, LiDAR and IMU the maker names (E5.1 to E5.8) by its car sensor type's elements, as type 1 |
| 9 | **Frame** | The remainder: the robot's mass less every part above and the actuators (E5.12); aluminium (the Asimov 1's 7075 and the PM01's aviation aluminium stated; the Roboto Origin's anodised parts and the others E, as type 1); RP1's frame 10 / 20 / 30 % steel (E: 28 of its 112 CNC parts are steel, by count only), the rest aluminium. A remainder below zero is reported, not cut |

**Agreed:** Matthias, 2026-10-29, choosing the answer offered: "I agree with the proposal of E5.14 for the rest of the
batch 1 robots, points 1 to 9, including its estimates." Not entered.

**Not settled by this proposal:** the steel recipe (E1.4), so iron, chromium, nickel and manganese stay missing; the
RP1's auxiliary battery; the boards' sizes from their makers (only the compute modules have one). Then: how 02 draws
each robot from its own composition, a step of its own for his yes.

### E5.15 Batch 2 of 4: eight more robots of type 1, the sources (2026-10-29). Nothing entered

Matthias: "I want to complete all work with type 1 and see the results!" Batch 2: the eight of the 21 remaining with
the most maker data expected. Read through the web-fetch tool, HTML only, nothing downloaded.

| Robot | What its sources give | Source | Kind |
|---|---|---|---|
| 55 Booster T2 | ~42 kg (Education, Pro), ~43 kg (gripper and hand versions), ~1.4 m; 31 joints (head 2, arms 7 each, waist 3, legs 6 each); "High-speed inner-rotor PMSM", crossed roller bearings, peak 140 N·m (no actuator model or mass); **48 V, 10 Ah** (480 Wh, arith.), chemistry not stated; Education an ARM board, Pro a Jetson Thor T5000; RGB-D cameras in head and waist, wrist cameras, optional Hesai JT128 LiDAR; materials not stated; URDF files in github.com/BoosterRobotics/booster_assets (robots/T2/...) | docs.booster.tech T2 specifications and overview; booster.tech/booster-t2 | maker, spec |
| 103 Unitree G1+ | the G1 with six upgrades: 2 head joints (25 in all), "stronger motors" (shoulder and waist peak torque + 110 %, arms + 43 %, against the G1), binocular and wide-angle cameras, head touch sensing, 6 microphones, external power; "Approx. 35kg" with battery, 1.34 m; "13 string lithium battery", 9000 mAh (the G1's), charger 54 V 5 A; inner-rotor PMSM, crossed roller bearings; 3D LiDAR; URDF g1_pl.urdf in github.com/unitreerobotics/unitree_ros | unitree.com/G1pl, unitree.com/g1 | maker, spec |
| 38 Asimov 2 | **no maker data**: Menlo lists it "In progress", its GitHub "coming soon"; 38 kg, 1.2 m, 27 joints only as the catalogue's "educated estimate" | humanoid.guide (it says so); menlo.ai, github.com/asimovinc | third, estimate |
| 147 K0 (ROBOTIS) | 34 kg, 1.3 m; 23 joints (arms 5, legs 6 each, waist 1); DYNAMIXEL-Q QM-060 × 14 (450 g) and QM-080 × 9 (850 g), 48 V, ratio 12, 16 or 20:1 (13.95 kg of actuators, arith.); 46.8 V 9 Ah (421 Wh, arith.), chemistry not stated; Jetson Orin NX 16 GB; covers 3D-printable; BOM and STEP "Coming Soon". ROBOTIS calls it "the first humanoid in that line: the baseline hardware and software others extend" | ai.robotis.com/ai_sapiens/introduction_ai_sapiens.html ("K0 - AI Sapiens") | maker, spec, "subject to change" |
| 85 E1 (Noetix) | the maker's pages show no text (rendered by script); 40 kg, 1.36 m, 23 to 28 joints, knee 150 N·m peak, crossed roller and deep groove bearings, Jetson Orin Nano Super (development), 2 h | humanoid.guide ("Not Verified"); noetixrobotics.com (title only) | third |
| 57 Bumi (Noetix) | the maker's pages show no text; 17 kg, 98 cm, 21 joints, in-house joints up to 70 N·m, Rockchip RK3576, shell "Composite materials", 3 h | humanoid.guide ("Not Verified") | third |
| 260 Roban2 (Leju) | the maker's pages give no values (its product page only pictures, its manual page empty); 40 kg, 1.45 m, 40 joints (hands 10), "Harmonic/planetary mixed reducers", "Aluminum alloy + ABS composite shells", 2 h | humanoid.guide ("Not verified"); lejurobot.com/en/products/roban2 | third |
| 309 TRON 2 (LimX) | **sold in four set-ups, none with legs and arms together**: dual arms on a stand, a biped "Sole" (987 mm, no arms), wheeled legs (1015 mm), dual arms on a mobile base; a legs-and-arms humanoid exists only as a simulation model (DASF, 26 joints); 46.8 V 9 Ah "ternary lithium" (421 Wh, arith.); "Aluminum alloy, plastic"; Intel Core Ultra (EDU); URDF and MJCF in github.com/limxdynamics/tron2-robot-description; user manual and brochure PDFs not opened | limxdynamics.com/en/products/tron2 and /spec, its manual page | maker, spec; maker, model |

**For Matthias's decision, found in batch 2 (the register's rules, E4; nothing changed):**
- **TRON 2:** LimX sells no form with legs and arms; the one with legs (987 mm) has no arms. By his rule "an upper body
  only not", and its height below type 1's 1.20 m, it may not be a humanoid of type 1.
- **K0 and AI Sapiens K1:** ROBOTIS's own pages make the K0 the baseline of the AI Sapiens line and the K1 its documented
  version (QM against QC actuators, 34 against 35 kg). "No double counting use just 1": one robot or two?
- **Asimov 1 and Asimov 2:** no maker data on the Asimov 2 at all.
- **G1 and G1+:** the G1+ is the G1 with named upgrades; drawn now with the parts of the G1, X1 or N1 scaled, it could
  take the G1's own parts (taken apart) with its two head joints and stronger motors.

**Not readable for the next step:** the Noetix and Leju sites give no text to a reader; their robots' composition can
come only from the third-party catalogue and estimates (E). URDF files of the T2, G1+ and TRON 2 (link masses) are
downloads, not opened.

### E5.16 Batches 3 and 4: the last 13 robots of type 1, the sources (2026-10-29). Nothing entered

Matthias: "Yes, this order" (the list of everything open for type 1, step 1 first). Read through the web-fetch tool,
HTML only, nothing downloaded. **Only two makers give values** (Fauna Robotics, StarBot); for the other eleven the
makers' pages show no text, a "coming soon", or no specifications, and only humanoid.guide's catalogue remains (most
entries marked "Not Verified"; some fields marked there as "assumed" or "Likely", left out here).

| Robot | What its sources give | Kind |
|---|---|---|
| 23 AKINCI-5 (AKINROBOTICS, Turkey) | 42 kg, 1.29 m, 19 joints; in-house inner-rotor BLDC motors; AMD Ryzen 9 PRO 6950H; "Aluminum alloy + composites"; 1 h; maker site refused (HTTP 403) | third |
| 143 JAKA π (JAKA) | 42 kg, 1.22 m, 27 joints (legs 6, arms 6 each: by its prose), up to 120 N·m, BLDC with planetary reducers; "48-volt pack", 2 h; Intel Core Ultra 7 255H; "Aluminum frame with soft-touch polymer covers"; maker pages empty | third |
| 168 LightBot-0 (Light Origins) | 35 kg, 0.9 m; depth camera; 3 h; the maker: "The bipedal humanoid is coming." | third; maker (no values) |
| 175 LUMO (DOBOT) | 35 kg, 1.3 m, hands 5 fingers each; "Aluminum alloy and plastic"; 2 h; DOBOT's page marketing only | third |
| 212 NORI L3 (Nori Robotics) | 40 kg, 1.45 m, 20 joints (16 in the hands), harmonic and planetary reducers, four 720p cameras; "Aluminum alloy with engineering plastics"; 6 h; the maker's site shows another robot (NORI A3) | third |
| 231 PHYBOT C1 (PHYBOT) | 25 kg, 1.25 m, 28 joints (12 in the hands), harmonic or planetary gears, RGB and depth camera; "Composite polymer + aluminum frame"; 3 h | third |
| 236 PrimeBOT Q1 (PrimeBOT) | 0.88 m, 22 joints; **no mass anywhere** ("has not publicly confirmed ... its weight"); maker pages empty | third |
| 246 QUESTER1 (AgiBot) | ~20 to 30 kg, 0.79 m, ~24 to 32 joints, harmonic gearboxes; "Aluminum + plastic composites"; 3 h; not on AgiBot's site | third |
| 279 Sprout (Fauna Robotics) | **22.7 kg, 1.07 m, 29 joints** (neck 2, arms 6, grippers 1, legs 5 each); **Jetson AGX Orin 64 GB**, 1 TB SSD; ZED 2i stereo camera, 4 time-of-flight sensors, IMU, microphones; swappable battery, 3 to 3.5 h, no voltage; "soft exterior" (aluminium only in the catalogue); a "Full specs" PDF on its site, not opened | maker, spec |
| 281 StarBot Astra (StarBot USA) | **"75 lb" (34 kg), "5 ft", 23 joints; battery "48 V", 2 to 5 h** (maker); planetary reducers, a Jetson Orin-class computer (third) | maker; third |
| 308 Totan O1 (WL Robotics) | 34 kg, 1.34 m, 30 joints; "Aluminum alloy frame with composite panels"; 1.5 to 2.5 h; the maker's site title says Westlake Robotics, no values | third |
| 332 Xiao Tuo (TOPSTAR) | 40 kg, 1.2 m, 30 joints; RGB camera and 3D LiDAR; "Aluminum + plastic composites"; 3 h; TOPSTAR's news item gives no values | third; maker (no values) |
| 343 YMBOT E3 (Yunmu) | 35 kg, 1.4 m; Intel 12th-generation Core i9-class CPU; 2 h; maker pages a loading screen | third |

### E5.17 Proposal: batches 2 to 4, by the agreed method (2026-10-29). Agreed, entered 2026-10-29 (E5.20)

The method of E5.12 (actuators) and E5.14 (the rest), agreed; what is new is how each input is filled where the maker
gives nothing, from batch 1's makers' data (the same kind of robot):

| # | Input missing | Proposal (E unless the maker states it) |
|---|---|---|
| 1 | Actuators' masses, no joint torques | 49 % of the robot's mass at the mode (batch 1 and the G1: 36 to 53 %, median 49 %), half to 1.5 times (24.5 / 49 / 73.5 %), split into small and large joints as batch 1's are on average; the K0 by its stated QM-060 and QM-080 masses (13.95 kg) |
| 2 | Battery energy, no voltage or capacity | 12 Wh per kg of robot (batch 1 and the G1, X1, N1: 6.8 to 21, median 12), half to 1.5 times; stated where given: T2 48 V 10 Ah (480 Wh), G1+ the G1's 13 cells 9 Ah, K0 and TRON 2 46.8 V 9 Ah (421 Wh), JAKA π and Astra 48 V (their capacity by the 12 Wh/kg); NMC cells (stated "ternary" for the TRON 2) |
| 3 | Boards | Each computer the catalogue or maker names by the template's computer board (60 / 120 / 180 cm²) or its module size (AGX Orin, Orin NX); the rest of the boards as the template (E5.14, point 4) |
| 4 | Cables, shell, screws, sensors, frame | As E5.14, points 5 to 9; materials as the maker or the catalogue names them ("Aluminum alloy + ..."), else aluminium and plastics as type 1 |
| 5 | **The G1+** | The G1's own parts as taken apart (E2), its mass 35 kg, and its two head joints as two small joints (E); its "stronger motors" (+110 % peak torque at shoulders and waist) not in the G1's parts and said so |
| 6 | **The PrimeBOT Q1's mass** (no source) | 9.75 / 19.5 / 29.25 kg (E: the Booster K1's 19.5 kg, the robot nearest in height, 0.95 against 0.88 m, with a mass from its maker; half to 1.5 times). Its mode lies above type 1's 15 kg, so it is drawn |
| 7 | **The Asimov 2** (no maker data) | The Asimov 1's composition (E5.2, E5.12, E5.14) scaled to the catalogue's 38 kg (E) |

**Four register questions** (found in batch 2, E5.15), each with a recommendation:

| Question | Recommendation |
|---|---|
| TRON 2: no form sold with both legs and arms | Not assigned: "not assigned: no form with legs and arms" (as "an upper body only not"); 31 robots of type 1 |
| K0 and AI Sapiens K1: one line | Both kept, two versions with their own actuators and batteries (as the G1 and G1+) |
| Asimov 2: no maker data | Kept, as point 7 |
| G1+: the G1 upgraded | As point 5 |

**Agreed:** Matthias, 2026-10-29, choosing the answer offered: "I agree with the proposal of E5.17 for batches 2 to 4,
points 1 to 7, and with the four recommendations on the register questions." Not entered: the TRON 2's entry in the
register's builder (not assigned) is made with the entry step, tests first.

### E5.18 Proposal: the steels and the titanium of type 1, part by part (2026-10-29). Agreed, entered 2026-10-29 (E5.20)

Matthias, "Yes, this order", step 4 (the steel recipe) and step 5 (titanium; Mixed follows, E5.19). Type 1 is now
taken apart part by part (E2, E5), so the open question of E1.4, each steel family's share in a robot, is answered by
the parts themselves: **each steel part takes the grade of its use**. The sources rank as Matthias set on 2026-10-27:
the standard (here through datasheets that quote it, read first-hand), commercial analyses, university analyses only
as context. Each grade's mode: a commercial typical value read first-hand where one exists, else the middle of the
standard's range (E), from 0 to the maximum where only a maximum is given (his rule). Iron the explicit remainder.

**The grades and their limits** (wt%; read 2026-10-29 unless named in E1.4):

| Grade | Limits | Source | Kind |
|---|---|---|---|
| Electrical steel M19, M27 | M19 Si 2.5 to 3.5, M27 Si 2.4 to 3.1, with C, Mn, Al, P, S up to their maxima | RAWCLICVehicleTractionMotor, `10_MaterialElementDefinitions.xlsx`, sheet ElectricalSteel, read where it lies (as the magnets); ASTM A677's scope (E1.4) | sibling's data, from the standard |
| 20CrMnTi (gears) | C 0.17 to 0.23, Si 0.17 to 0.37, Mn 0.80 to 1.10, Cr 1.00 to 1.30, Ti 0.04 to 0.10, P and S ≤ 0.030, Cu ≤ 0.30 | steelestores.com and otaisteel.com, quoting GB/T 3077; Cu Total Materia (E1.4) | datasheets quoting the standard |
| GCr15 (bearings) | C 0.95 to 1.05, Si 0.15 to 0.35, Mn 0.25 to 0.45, Cr 1.40 to 1.65, Ni ≤ 0.30, Mo ≤ 0.10, Cu ≤ 0.25, P and S ≤ 0.025 | steelestores.com, quoting GB/T 18254 | datasheet quoting the standard |
| 42CrMo4 (flanges, shafts, links; the 12.9 screws) | C 0.38 to 0.45, Si 0.15 to 0.40, Mn 0.60 to 0.90, Cr 0.90 to 1.20, Mo 0.15 to 0.30, P ≤ 0.025, S ≤ 0.035 | Astrup's datasheet, EN 10083-3 (E1.4); for screws of class 12.9 ISO 898-1 asks C 0.30 to 0.50 and Cr, Ni, Mo or V (Optimas, E1.4b), which 42CrMo4 meets | datasheet quoting the standard |
| C45 (RP1's "45" and AISI 1045 parts) | C 0.42 to 0.50, Si ≤ 0.40, Mn 0.50 to 0.80, Cr ≤ 0.40, P and S ≤ 0.045; **Ni and Mo: the page gives Ni ≤ 0.10 and Mo ≤ 0.40, another source the reverse** (Cr + Mo + Ni ≤ 0.63 by Saarstahl): proposed Ni ≤ 0.40 and Mo ≤ 0.10, the reading that keeps Cr + Mo + Ni ≤ 0.63 at the modes | steelestores.com, quoting EN 10083-2 | datasheet quoting the standard; conflict reported |
| P20 (RP1, 4 parts) | C 0.28 to 0.40, Si 0.20 to 0.80, Mn 0.60 to 1.00, Cr 1.40 to 2.00, Mo 0.30 to 0.55, P and S ≤ 0.030 | otaisteel.com, quoting ASTM A681 and GB 1299 | supplier quoting the standards |
| 304 (RP1's pins and screws) | the sibling's limits (Cr 18 to 20, Ni 8 to 10.5, C ≤ 0.08, Mn ≤ 2, Si ≤ 0.75); modes Outokumpu's typical C 0.04, Cr 18.1, Ni 8.1 | RAWCLICVehicleTractionMotor, sheet CastFeSteel; Outokumpu (E1.4b) | sibling's data; producer's typical (commercial) |
| 17-4PH (the X1's shafts) | modes Outokumpu's typical C 0.02, Cr 15.5, Ni 4.8, Cu 3.4, Nb; limits not found (ASTM A564 not read): ± 50 % of each mode (E, his rule for estimates) | Outokumpu (E1.4b) | producer's typical |
| Ti-6Al-4V (the X1's TC4 links) | Al 5.50 to 6.75, V 3.50 to 4.50, Fe ≤ 0.40, O ≤ 0.20, C ≤ 0.08, N ≤ 0.05, H ≤ 0.015, Ti the remainder | voestalpine's datasheet, ASTM B348 (E1.3) | producer's datasheet quoting the standard |

**Each steel part of type 1 and its grade:**

| Part (sheets JointParts, Parts; the template of E5.14) | Grade | Why |
|---|---|---|
| Motor stator's electrical steel; motor rotor's steel | M19 or M27, each as often (a discrete state) | non-oriented silicon steel of motors; the two grades of the sibling's traction motors (E for a robot's laminations) |
| Gears: stage 1 sun, planets, ring; stage 2 ring | 20CrMnTi | KOFON's humanoid joints (E1.4b, search result only) and the workbook's types 2 and 6 name it for gears |
| Stage 2 planets, carrier and crossed roller bearing (its steel) | 20CrMnTi 30 / 50 / 70 %, GCr15 the remainder (E: gears and the bearing in one weighed group) | |
| Small bearings; bearings outside the actuators; RP1's bearing steel | GCr15 | China's standard bearing steel; the G1's crossed roller bearing is Chinese-made (E2.2) |
| Output flange; lower-leg links; links and shafts not named | 42CrMo4 (E) | the workbook's shaft and high-strength steel |
| Screws (all robots), the joints' "Other" steel | 42CrMo4 as class 12.9 (RP1 states "12.9级") (E) | ISO 898-1 |
| RP1's "45" / AISI 1045 parts; the X1's steel pins | C45 | named by RP1's BOM; pins E |
| RP1's P20 parts; RP1's 304 parts; the X1's 17-4PH shafts | P20; 304; 17-4PH | named by their makers |
| Titanium: the X1's TC4 links | Ti-6Al-4V | named by AgiBot (E2.8e) |

**What it adds** (type 1's steel 9.9 kg at the median in one robot, V64): iron as each grade's remainder, and
chromium (1.15 % in the gears, 1.5 % in the bearings, 1.05 % in the screws and shafts at the modes; 18.1 % in RP1's
304), manganese, silicon (about 3 % in the electrical steel), molybdenum, nickel (304, 17-4PH), titanium (20CrMnTi,
Ti-6Al-4V), vanadium (Ti-6Al-4V). The robot's totals follow from the run, not computed here. Brass (RP1, 8 parts)
and the battery's Mixed parts are not in this proposal.

**Agreed:** Matthias, 2026-10-29, choosing the answer offered: "I agree with the steel and titanium proposal of E5.18,
including its estimates and the C45 reading of Ni and Mo." Not entered.

### E5.19 Proposal: Mixed, brass (2026-10-29). Agreed, entered 2026-10-29 (E5.20)

Matthias, "Yes, this order", step 5 (titanium and Mixed). Type 1's Mixed is: each robot's **battery pack less its cells
and its management board** (housing, cell holders, nickel strips or busbars, wires; in the parts file "Battery housing,
busbars and wires"), and the X1's two **OmniPicker grippers** (0.43 kg each, AgiBot's manual, E2.8e). RP1's 8 brass
parts are named by its BOM.

**Sources, read 2026-10-29 (web-fetch tool, HTML only):**

| Source | What it gives | Kind |
|---|---|---|
| sevarg.net, iZip Ultra 2011 pack, parts 1 to 3 (36 V, 10 Ah, 50 Samsung 18650 cells, 10S5P) | "black plastic retainers" holding the cells, nickel strip "0.2mm thick" (measured with a micrometer), 10 mm and 8 mm wide, sense wires, a BMS, padding tape, heat shrink; **nothing weighed** | first-hand teardown, not weighed |
| sevarg.net, Schwinn Tailwind pack (24 V, Toshiba prismatic cells) | plastic shell, a metal plate, thick busbars, ribbon cable, potted BMS; nothing weighed | first-hand teardown; prismatic cells, not the same kind |
| teswaybike.com, "We Tear Down an eBike Battery" | "The casing is typically made from tough materials like aluminum or high-impact plastics"; no pack opened | seller's article, a claim |
| EngineAI, PM01 pack (E5.6) | housing "Aluminum Alloy", the pack 2.95 kg | maker, spec |
| Searched, not found | a weighed split of a small cylindrical-cell pack; the composition shares of e-bike packs (a VTT report on crushed e-bike batteries is a PDF, not opened) | – |

**Not weighed anywhere: every share below is an estimate (E).** Claude's arithmetic for scale: the G1's pack, 2.5 kg,
less its cells (421 Wh ÷ 241.5 Wh/kg = 1.74 kg) leaves 0.76 kg; the PM01's 2.95 kg less 26 cells of about 68 g
(1.77 kg) leaves 1.18 kg; one nickel piece of 0.2 × 8 × 20 mm weighs 0.28 g, two to six per cell.

| # | Part | Proposal |
|---|---|---|
| 1 | Battery pack less cells and management board | nickel strip (nickel) 1 / 3 / 6 %; copper wires and busbars 5 / 10 / 15 %; cell holders, insulation and tape (plastics) 5 / 10 / 20 %; the housing the remainder (E). The housing aluminium where the maker says so (PM01); elsewhere aluminium or plastics, each as often (a discrete state, E: the seller's "aluminum or high-impact plastics"). Every share at least half to 1.5 times its mode |
| 2 | The X1's OmniPicker grippers | as a small joint of the G1 (E5.12's shares at the mode: copper 8.3 %, NdFeB 7.4 %, electrical steel 10.6 %, steel 41.5 %, aluminium 25.9 %, plastics 3.9 %, driver board 2.4 %), drawn as the small joint (E: a gripper is a motor, gears and a frame) |
| 3 | RP1's brass parts | brass, Cu 58 / 62 / 65 %, zinc the remainder (E: the common free-cutting and H62 brasses; their standards not read); their mass 5 / 10 / 20 g each (E) |

**Agreed:** Matthias, 2026-10-29, choosing the answer offered: "I agree with the Mixed proposal of E5.19, points 1 to 3,
including its estimates." Not entered.

## E4. A register of every known humanoid, each in one type: research, first pass (2026-10-28). Nothing entered

Matthias: "I want that all know humanoid robots at the end can be assigned to types. It should be possible also to
assign themeven they are out of limts. Nothing is left behind as the field is fluid and changes fast"; "If there is a
given purpose usecase for a robot, then it should go to the respective type. Except it does not fit, due to on or no
legs arms . We have to be a bit more open. We can not explude"; "There should be no double counting. A robot has to be
in one but not two types. Boarder cases have to be decide manually"; then "Yes, research the list".

**The list:** humanoid.guide's database (https://humanoid.guide/humanoid-robots-database/, "349 humanoids", read
2026-10-28): every English product page of its category humanoids, 349, read with its attribute table (availability,
nationality, the maker's website, joints, height, weight, payload, "Main market", manufacturer) and whether its page
speaks of wheels. A catalogue, second-hand: makers may edit their entries ("Edit this robot (Only if you are this robot
manufacturer)"), some say "Verified". 343 give a height, 328 a mass; 190 are prototypes, 122 "In production"; 2 are
marked obsolete. Not in it: the Fourier N1, the Norinco Fuxi, the UBTECH Walker S. Possibly listed twice: Optimus and
Optimus Gen2, CyberOne and CyberOne v2, Asimov and Asimov 1, YMBot D and D4 (same maker, height, mass and joints).

**A first pass, by keywords** (Claude's scratch folder, `humanoid_register_first_pass_2026-10-28.xlsx`): each robot's
"Main market" matched to the six types' purposes, research and education to type 1 or 2 by size, no stated use by the
nearest size. Type 1: 35, type 2: 85, type 3: 125, type 4: 90, type 5: 12, type 6: 2; border cases 145 (94 speak of
wheels, 51 with uses pointing to two types); 59 without a stated use; 214 outside their type's size (types 3 to 6's
ranges are the workbook's comparators' spans, narrow).

**Why it is not a proposal:** the catalogue's "Main market" lists many uses, often alphabetically, so keywords cannot
weigh them; the first pass contradicts the workbook for its own anchors and comparators (the Atlas to 3, the workbook 5;
the AgiBot A2 to 2, the workbook 4; Foundation's Phantom to 3 or 6, the workbook 6; the H2 to 3, the workbook 2; the
T800 to 3, the workbook 5); and "speaks of wheels" catches walking robots too (the Apollo 2, the Digit).

### E4.1 Batch 1 of 7: robots 1 to 50 (alphabetical), each read and a type proposed (2026-10-28). Not entered

Matthias: "Yes: the robots the workbook names keep its type; every other robot read (its catalogue page and maker's
description) and proposed a type with a one-line reason, in batches, border cases marked for me."

**What was read:** every robot's humanoid.guide page (attribute table and description, second-hand: the catalogue's
own text, not the maker's), and its whole text searched for wheels, legs and walking. The maker's own page where the
catalogue left the form open: Hexagon AEON (https://robotics.hexagon.com/product/), AgiBot G1
(https://www.agibot.com/products/G1), AgiBot A3 (https://www.agibot.com/products/A3), Astribot
(https://www.astribot.com/en; its product pages answered 404). TeknTrash's page did not load.

**How a type was proposed** (Claude's reading, for Matthias to accept or change):
- R1. A robot the workbook's Taxonomy names keeps the workbook's type.
- R2. Otherwise the use the robot is built for, from the catalogue's "Main market" and its description, decides: the
  type whose definition (Taxonomy, column B) matches the main use.
- R3. Uses spread over several types with none ahead: type 2, whose definition is "adaptable task execution across
  research, commercial, and factory pilot environments".
- R4. Research, education and developer platforms: type 1 when compact, type 2 when full-scale (the two research
  types), by size.
- R5. Size decides only where the use does not; a robot outside its type's height or mass is noted, not refused.

**Form:** "legs" or "wheels" where the text read says so; "no wheels named" where the catalogue page never speaks of
wheels and states no legs either. The workbook's types 1 and 3 are defined as bipedal ("portable bipedal form
factor"; "wheeled variants (e.g., wheeled Apollo/KUAVO) are comparators, not primary bipedal humanoids").

| # | Robot (maker) | Catalogue: status, height, mass | Type | Form | Size against the type | Reason | Border |
|---|---|---|---|---|---|---|---|
| 1 | NEO (1X Technologies, US) | prototype, 170 cm, 30 kg | 4 | no wheels named | mass below (62–71 kg) | home chores and conversation, soft body ("Consumer home use") | |
| 2 | 4NE-1 (NEURA Robotics, DE) | prototype, 180 cm, 80 kg | 3 | no wheels named | height above (~1.70–1.75 m) | "from industrial to domestic settings", collaborative work | maybe the same robot as 3 |
| 3 | 4NE1 (NEURA Robotics) | early production, ~180 cm, ~80 kg | 3 | legs or wheels ("Some models run on wheels for factory floors") | height above | everyday tasks, industrial automation, services | maybe the same robot as 2 |
| 4 | 4NE1 Gen 3.5 (NEURA Robotics) | in production, 180 cm, 80 kg | 3 | no wheels named | height above | factories and warehouses (industrial manufacturing, logistics) | |
| 5 | 4NE1 Gen 4 (NEURA Robotics) | in production, 180 cm, 65 kg | 3 | legs or wheels ("NEURA also offers wheeled versions") | height above | three of its four uses industrial (logistics, machine tending, manufacturing), the fourth home assistance | |
| 6 | A2 (AgiBot, CN) | prototype, 170 cm, 60 kg | 4 | no wheels named | the workbook: 1.75 m, 69 kg | R1: type 4's anchor | |
| 7 | A2 Max (AgiBot) | prototype, 178 cm, 85 kg | 3 | no wheels named | height above | "physical strength", logistics, healthcare, manufacturing | the heavy variant of type 4's anchor; healthcare also named |
| 8 | A3 Ultra (AgiBot) | in production, 174 cm, 60 kg | 4 | no wheels named (the A3 walks, see 14) | mass below | commercial service, guided tours, reception, retail | |
| 9 | Abi (Andromeda Robotics, AU) | in production, 120 cm, 50 kg | 4 | wheels ("Instead of legs, it uses a wheeled base") | both below | social companion in care facilities, retail, public venues | |
| 10 | Adam Lite (PNDbotics, CN) | prototype, 160 cm, 60 kg | 2 | no wheels named | inside | R3: "platform for various industrial and service applications", open SDK, no single use | |
| 11 | Adam SP (PNDbotics) | prototype, 167 cm, 62 kg | 2 | legs ("full-size biped") | inside | R3: "factory floors as well as dynamic research labs" (the catalogue's summary line describes another robot, "Steve") | |
| 12 | AEON (Hexagon, SE) | prototype, 165 cm, 60 kg | 3 | unclear: the maker "Ready to roll", "go up the stairs" | both slightly below | the maker: "deployed in industries", manipulation, inspection, reality capture | form |
| 13 | AGIBOT A2-W (AgiBot) | pilot, 163 cm, 230 kg | 3 | wheels | mass above (61–129 kg) | industrial automation, logistics, manufacturing | |
| 14 | AGIBOT A3 (AgiBot) | in production, 173 cm, 55 kg | 4 | legs (the maker: "somersaults", "aerial walking"; the catalogue's "wheeled" is its carrying case) | mass below | stage performance, guided tours, retail | |
| 15 | AGIBOT G1 (AgiBot) | pilot, 130–180 cm, 150 kg | 2 | wheels (the maker: "The chassis allows in-place turning") | mass above (50–80 kg) | the maker: "General purpose robot designed for data collection and model inference", "industrial, commercial, and domestic scenarios" | not the Unitree G1 |
| 16 | AgiBot X1 (AgiBot) | prototype, 130 cm, 33 kg | 1 | legs | inside | R1: named in type 1 | |
| 17 | AgiBot X2 (AgiBot) | in production, 130 cm, 35–37 kg | 4 | legs ("walks, runs, dances") | both below; type 1's size | four of its six uses face people (elderly care, entertainment, home service, public interaction) | |
| 18 | Agile ONE (Agile Robots SE, DE) | prototype, 174 cm, 69 kg | 3 | legs ("a life-sized biped") | inside | "a shop-floor teammate", logistics, manufacturing | |
| 19 | AI Sapiens K1 (ROBOTIS, KR) | in production, 135.5 cm, 35 kg | 1 | legs ("arms, legs, and waist") | inside | R4: open-source research platform | |
| 20 | AI Worker (ROBOTIS) | in production, 162 cm, 90 kg | 3 | wheels ("swerve-drive base", "semi-humanoid") | height below | welding, wiring, inspection on the factory floor | |
| 21 | AICO 2 (Flexiv Robotics) | in production, 160 cm, 281 kg | 3 | wheels; two arms on a base ("a mobile, dual-arm robot") | mass above | manufacturing, logistics | form: two arms on a cart |
| 22 | AIDOL (AIDOL, RU) | prototype, 186 cm, 95 kg | 3 | legs ("walk on two legs") | height above | catalogue: industrial automation, logistics | its text stresses face and dialogue (type 4); the catalogue's summary line describes another robot |
| 23 | AKINCI-5 (AKINROBOTICS, TR) | prototype, 129 cm, 42 kg | 3 | legs ("AI-supported walking") | both below; type 1's size | "Built for manufacturing, and logistics" | the catalogue's market "Robotics R&D and automation industry"; type 1's size |
| 24 | Alex (IHMC, US) | prototype, 175 cm, 85 kg | 6 | legs ("biped") | inside | R1: named in type 6 | |
| 25 | Alice (AeiROBOT) | prototype, 157 cm, 50 kg | 2 | no wheels named | between types 1 (≤1.45 m) and 2 (≥1.60 m) | R4: research platform | size between types 1 and 2; nationality China here, South Korea at 26 (same maker) |
| 26 | Alice M1 (AeiROBOT, KR) | in production, 130–180 cm, 97 kg | 3 | wheels ("omnidirectional wheeled base") | inside by mass | construction, manufacturing, shipbuilding | |
| 27 | ALLEX (WIRobotics, KR) | prototype, not given | 2 | upper body ("introduced initially as an upper-body system") | not given | R3: "general-purpose humanoid platform"; cleaning, home service, logistics | form: upper body |
| 28 | ALPHA (TeknTrash, UK) | prototype, 200 cm, 90 kg | 3 | not stated ("a mobile, collaborative system") | height above | sorting in recycling plants, two 6-DoF arms, 5 kg lift | "dirty, repetitive, and dangerous": type 5? nothing hardened stated |
| 29 | AlphaBot 2 (AI² Robotics, CN) | in production, 180 cm, 135 kg | 3 | wheels ("a six-wheeled base") | both slightly above | factories (HKC, Dongfeng Liuzhou), also airports | |
| 30 | Ambidex (NAVER LABS, KR) | in production, 186 cm, not given | 4 | not stated; arms | height above | safe, delicate handling with force feedback; no use given | no stated use; form |
| 31 | Anigon (Aimbo Robotics, CH) | prototype, 189 cm, 120 kg | 3 | wheels | height above | logistics, manufacturing, warehousing | |
| 32 | Apollo (Apptronik, US) | prototype, 173 cm, 72 kg | 3 | no wheels named | inside | logistics and warehousing (crates, totes, boxes) | |
| 33 | Apollo 2 (Apptronik) | prototype, 173 cm, 75 kg | 3 | legs or wheels ("switch it to a wheeled base") | inside | R1: qualifying in type 3 | the workbook also names it in type 2 (borderline) and type 5 (Apollo 'High-Perf', borderline) |
| 34 | ARI (PAL Robotics, ES) | in production, 165 cm, 60 kg | 4 | wheels | mass below | talks with people and guides them in offices, shops, hospitals, museums | |
| 35 | ARMAR-7 (KIT, DE) | prototype, 175 cm, 120 kg | 4 | wheels | mass above | household and nursing-care assistance | |
| 36 | Asimov (MenloAI, SG) | in production, 120 cm, 35 kg | 1 | no wheels named | height slightly below | R4: DIY kit for developers and labs | maybe the same robot as 37 |
| 37 | Asimov 1 (MenloAI) | in production, 120 cm, 35 kg | 1 | no wheels named | height slightly below | R4: DIY kit for engineers and researchers | maybe the same robot as 36 |
| 38 | Asimov 2 (MenloAI) | prototype, 120 cm, 38 kg | 1 | no wheels named | height slightly below | R4: the next open platform (the catalogue's specs estimated from Asimov 1) | |
| 39 | Astra (Apptronik) | prototype, 100–140 cm, 25–40 kg | 3 | upper body, "mounts onto various" bases | both below | "modular mobility for industrial tasks"; manufacturing, interactive service | form: upper body |
| 40 | Astribot S1 (Astribot, CN) | in production, 170 cm, 80 kg | 2 | not stated | inside | R3: AI training, logistics, research, service | |
| 41 | Astribot T1 (Astribot) | in production, 155 cm, 66 kg | 2 | wheels | height below | the maker: "All-in-One AI Robot", "validate your AI ideas"; catalogue: service, research, home, industrial | |
| 42 | AstroDroid AD-01 (ELU.AI, CN) | prototype, 170 cm, 120 kg | 3 | wheels | inside | manufacturing, logistics, retail | |
| 43 | Atlas (Boston Dynamics, US) | early production, 190 cm, 90 kg | 5 | legs | height above | R1: type 5's anchor | |
| 44 | Atlas (old) (Boston Dynamics) | prototype, 150 cm, 89 kg | 5 | legs | height below | the same maker's earlier research Atlas; no use given | which robot: its size and page address ("atlas-2013") point to the older Atlas, its text to the electric one of 2024 |
| 45 | Atom (DOBOT, CN) | prototype, 153 cm, 62 kg | 4 | legs ("straight-knee walking") | inside | R1: named in type 4 | |
| 46 | ATOM (Vbot, CN) | prototype, 160 cm, 50 kg | 4 | legs ("quiet feet") | mass below | homes, offices, public service, retail | |
| 47 | Atom Max (DOBOT) | prototype, 170 cm, 55 kg | 2 | legs ("straight-knee walking") | inside | R4: research labs, education, teleoperation development | |
| 48 | Avatar (Avatar Robotics, US) | in production, 180 cm, not given | 3 | not stated | height above | teleoperated warehouse robot, light manufacturing | |
| 49 | Avatar (Honda R&D, JP) | prototype, 155 cm, 101 kg | 2 | wheels | mass above | R3: remote work in medical support, equipment maintenance, disaster response, space | uses over types 3, 4 and 5 |
| 50 | Axol (Almond AI, US) | in production, 61 cm, 19.5 kg | 1 | two arms on a table or cart, no legs, no head | both below | R4: physical-AI research, compact | form: "not a humanoid robot in the traditional sense" (the catalogue) |

**Batch 1 by type, as first proposed:** type 1: 6; type 2: 9; type 3: 21; type 4: 11; type 5: 2; type 6: 1. Wheels:
13 (three more, 4NE1, 4NE1 Gen 4 and Apollo 2, offered with legs or wheels); upper body or arms only: 5 (AICO 2 also
on wheels); form not stated or unclear: 4.

**Decided, 2026-10-28** (the form): "Wheels are also accepted. What is not, is just the upper body. We can refine the
unclear once, after going through all the batches, as the rules might be improved." Read so: a robot on wheels goes to
its use type as a robot on legs does; a robot that is only an upper body, with no legs and no wheels of its own, is not
assigned. Applied to batch 1:
- not assigned, an upper body only: 27 ALLEX ("introduced initially as an upper-body system"), 50 Axol (two arms "to
  bolt onto a table or cart");
- unclear, left for the end: 39 Astra ("mounts onto various" bases, mobile ones among them?), 30 Ambidex (arms; a
  base not stated);
- no longer a border case, legs and wheels both accepted: 12 AEON (type 3 either way), 21 AICO 2 (two arms on its
  own wheeled base, type 3).

Batch 1 by type after this: type 1: 5; type 2: 8; type 3: 20 and Astra unclear; type 4: 10 and Ambidex unclear;
type 5: 2; type 6: 1; not assigned: 2.

### E4.2 Batch 2 of 7: robots 51 to 100 (2026-10-28). Not entered

Read and proposed as batch 1 (E4.1: rules R1 to R5; legs and wheels accepted, an upper body only not assigned,
unclear forms left for the end). **What was read:** every robot's humanoid.guide page, its whole text searched for
wheels, legs and walking; the maker's own page where the catalogue left the form open: Clone Robotics
(https://www.clonerobotics.com: "Clone is a bipedal android companion"), Wandercraft (https://en.wandercraft.eu/),
Svaya Robotics (https://svayarobotics.com/), Faraday Future (https://robotics.ff.com/us/); Sharpa's and CasiVision's
pages gave no text.

| # | Robot (maker) | Catalogue: status, height, mass | Type | Form | Size against the type | Reason | Border |
|---|---|---|---|---|---|---|---|
| 51 | Billi (NEUBILITY, KR) | prototype, 149.7 cm, 110 kg | 3 | wheels ("uses wheels instead of legs") | height below | distribution, industrial logistics, manufacturing, material handling | |
| 52 | Bimanual (Svaya Robotics, IN) | early production, 155 cm, 70 kg | 2 | unclear: two arms, a base not stated ("Instead of chasing extreme mobility") | height below | R4: "research-focused platform"; industrial R&D, research and education | form: an upper body only? left for the end |
| 53 | Bolt (MirrorMe Technology, CN) | prototype, 175 cm, 75 kg | 2 | legs (sprints at "over 11 meters per second") | inside | R4: research, sparring partner for sprinters, technology demonstration | its speed and 50 kg load are type 5's marks (">2.5 m/s"), its use is not |
| 54 | Booster T1 (Booster Robotics, CN) | prototype, 118 cm, 30 kg | 1 | no wheels named | height slightly below | R4: open-source platform for developers and researchers | |
| 55 | Booster T2 (Booster Robotics) | in production, 140 cm, 43 kg | 1 | no wheels named | inside | R1: named in type 1 | |
| 56 | Borg 01 (Borg Robotics, US) | prototype, 173 cm, 62 kg | 3 | legs or wheels ("switch between walking on two legs and a wheeled base") | inside | "designed for industrial and manufacturing environments" | |
| 57 | Bumi (Noetix Robotics, CN) | in production, 98 cm, 17 kg | 4 | no wheels named | both far below | "companionship and learning at home", for children | maker education and programming also named (type 1) |
| 58 | CALVIN-40 (Wandercraft, FR) | pilot, 170 cm, 80 kg | 3 | no wheels named; headless | inside | heavy logistics in factories (Renault Douai, tyres) | |
| 59 | CASBOT 02 (CASBOT, CN) | early commercial, 163 cm, 50 kg | 4 | legs ("walks upright") | mass below | museums, shopping centres, reception; education, exhibitions, retail | |
| 60 | CASBOT W1 (CASBOT) | in production, 112–210 cm, ~260 kg | 3 | wheels | mass above | "high-precision handling ... mobile manipulation in logistics" | |
| 61 | CASIVIBOT (CasiVision, CN) | in production, 140 cm, 55 kg | 4 | not stated | height and mass below | "guide users, deliver items"; healthcare, hospitality, commercial service | |
| 62 | Centaur-G1 (Elite Robots, CN) | in production, 150 cm, 260 kg | 3 | wheels ("omnidirectional wheeled base") | mass above | "for precision manufacturing" (±0.1 mm) | eldercare and home service also named (type 4) |
| 63 | Cinnamon 1 (Donut Robotics, JP) | prototype, ~160–180 cm, ~60–90 kg | 2 | legs ("walks on two legs") | inside | R3: construction, industrial automation, security, service | security also named (type 6?) |
| 64 | CLOiD (LG Electronics, KR) | pilots, ~120–130 cm, ~60–70 kg | 4 | wheels ("on a wheeled base rather than legs") | height below | hotels, retail, airports, offices | |
| 65 | Clone Alpha (Clone Robotics, PL) | prototype, 170 cm, 60 kg | 4 | legs (the maker: "bipedal") | mass below | the maker: "android companion"; the catalogue: no use | |
| 66 | Cruzr S2 (UBTECH, CN) | in production, 175 cm, 150 kg | 3 | wheels | mass above | "demanding industrial and commercial use", 15 kg payload | |
| 67 | Cruzr Y1 (UBTECH) | in production, 170 cm, 90 kg | 3 | wheels (a wheeled base and two arms) | inside | transporting, loading, picking, sorting in factories and warehouses | |
| 68 | CUE7 (Toyota, JP) | prototype, 218 cm, 74 kg | 2 | not stated | height above | R4: research robot, basketball shooting | |
| 69 | CyberOne (Xiaomi, CN) | prototype, 177 cm, 52 kg | 2 | no wheels named | inside | R4: a demonstrator of Xiaomi's AI, emotion recognition | maybe the same robot as 70 |
| 70 | CyberOne v2 (Xiaomi) | prototype, 177 cm, 52 kg | 2 | no wheels named | inside | R4: AI development, research, "future service robotics" | maybe the same robot as 69 |
| 71 | CYBORG RO1 (Cyborg Robotics, CN) | in production, 180 cm, 75 kg | 5 | legs ("walks on two legs") | inside | the maker's aim: "high-risk industries such as power, gas, oil, chemicals"; hazardous-site inspection | no sealing stated; otherwise type 3 |
| 72 | CYBORG WO1 (Cyborg Robotics) | in production, 160 cm, 170 kg | 5 | wheels | height below, mass above | as 71: hazardous-site inspection, power, gas, oil, chemicals, mining | as 71 |
| 73 | D01 (Sharpa, SG) | early production, 162 cm, 40 kg | 2 | not stated | mass below | R3: food service, hospitality, manufacturing, research, retail | |
| 74 | DEUX (XYZ, KR) | in production, 155 cm, 60 kg | 4 | wheels ("swerve-drive base") | mass below | "service robot" in stores, offices, hospitals, homes | |
| 75 | Dex (Richtech Robotics, US) | prototype, 137 cm, 60 kg | 3 | wheels (the mobile version) | height below | factory floor: logistics, manufacturing, warehouse | its second, stationary version is an upper body only |
| 76 | DexBot (BOSHIAC, CN) | prototype, 160–175 cm, 80 kg | 3 | legs or wheels ("operate on legs or wheels") | inside | industrial automation, logistics, manufacturing | |
| 77 | Digit (Agility Robotics, US) | in production, 180 cm, 76 kg | 3 | legs | inside | "built for logistics and warehouse automation" (the text: 1.75 m, 65 kg) | |
| 78 | Digit 5 (Agility Robotics) | production-ready, 180 cm, 129 kg | 3 | no wheels named | inside | R1: named in type 3 | |
| 79 | Dora (Noetix Robotics) | prototype, 100 cm, 20 kg | 4 | legs ("walks stably over grass, snow or stairs") | both far below | household errands, education, elder care | |
| 80 | DR01 (DEEP Robotics, CN) | prototype, 170 cm, 80 kg | 2 | no wheels named | inside | R4: "embodied intelligence explorer" for AI research | |
| 81 | DR02 (DEEP Robotics) | in production, 175 cm, 65 kg | 5 | no wheels named | mass below | R1: named in type 5 (IP66) | |
| 82 | Dual-Arm Lift (RealMan Robotics, CN) | in production, 178 cm, 157 kg | 2 | wheels | mass above | R4: data collection, embodied AI, research; also industrial automation | |
| 83 | Duatic Alpha (Duatic, CH) | prototype, 175 cm, 90 kg | 3 | wheels ("wheeled half-humanoid") | inside | warehouses and factories, heavy loads | |
| 84 | DUCO (SIASUN, CN) | prototype, ~150–160 cm, ~90–110 kg | 3 | wheels | height below | "industrial collaboration and logistics tasks" | |
| 85 | E1 (Noetix Robotics) | in production, 136 cm, 40 kg | 1 | legs (running, long jump) | inside | R4: "for research and education" | entertainment and guided tours also named (type 4) |
| 86 | Eggie (Tangible Robots, US) | prototype, 160 cm, 45 kg | 4 | wheels ("humanoid torso ... on a mobile wheeled base") | mass below | guides visitors, interaction and service; exhibitions, home assistance | |
| 87 | Elf Xuan 2.0 (AheadForm, CN) | prototype, 165 cm, 50 kg | — | an upper body only ("lifelike upper-body humanoid") | — | not assigned (decided 2026-10-28); its use, reception and stage, would be type 4 | |
| 88 | Elixis (Addverb, IN) | prototype, 175 cm, 75 kg | 3 | legs ("walks on two legs") | inside | logistics, warehousing, manufacturing; healthcare and retail also | |
| 89 | Elixis-W (Addverb) | prototype, 183 cm, 75 kg | 3 | wheels | height above | factories and warehouses, intralogistics | |
| 90 | Eno (Genesis AI, US) | prototype, 170 cm, 120 kg | 2 | wheels ("a wheeled platform rather than legs") | mass above | R3: "general-purpose robot" for factories, laboratories, hospitals, logistics | |
| 91 | F-Series (Realbotix, US) | in production, 165 cm, 50 kg | 4 | wheels ("on a wheeled base") | mass below | "human connection rather than physical labor"; elder care, hospitality, entertainment | |
| 92 | Feather (Feather Robotics, US) | in production, 180 cm, 105 kg | 2 | wheels ("omnidirectional base") | mass above | R3: warehouses, factories, restaurant kitchens, labs; physical-AI developers | |
| 93 | Fengxing-001 (AVIC, CN) | prototype, 180 cm, 80 kg | 3 | legs ("give its legs extra load-bearing strength") | height above | aircraft support work, electro-hydraulic drive | aviation fits no type plainly (3, 5 or 6) |
| 94 | FF Futurist (Faraday Future, US) | production-ready, 169 cm, 69 kg | 4 | not stated | inside | customer interaction, professional service, workplace assistance | |
| 95 | FF Master (Faraday Future) | production-ready, 131 cm, 39 kg | 4 | not stated | both below; type 1's size | home assistant, interaction, education | |
| 96 | FF Nova (Faraday Future) | in production, 49.7 cm, 2.8 kg | 1 | legs, and a detachable wheeled base | both far below | R4: developers, K–12 STEM, university research | |
| 97 | Figure 02 (Figure AI, US) | prototype, 168 cm, 70 kg | 3 | no wheels named | height slightly below | industries, logistics, warehouse | |
| 98 | Figure 03 (Figure AI) | prototype, 168 cm, 60 kg | 2 | no wheels named | inside | R1: qualifying in type 2 | the workbook also names it in type 3 (borderline) |
| 99 | FlashBot Arm (Pudu Robotics, CN) | in production, 144 cm, 70 kg | 4 | wheels ("an independent chassis") | height below | "delivery and smart service tasks"; hospitality, household, retail restocking | |
| 100 | Friday (Holiday Robotics, KR) | prototype, 173 cm, 115 kg | 3 | wheels ("fast wheeled mobility") | inside | the catalogue's market: manufacturing; its text: labs, factories, public spaces | |

**Batch 2 by type:** type 1: 4; type 2: 11 and Bimanual unclear; type 3: 18; type 4: 12; type 5: 3; type 6: 0; not
assigned: 1 (Elf Xuan 2.0, an upper body). Catalogue faults: the summary lines of Billi, Eno and Figure 02 describe
other robots; Friday's nationality is blank.

### E4.3 Batch 3 of 7: robots 101 to 150 (2026-10-28). Not entered

Read and proposed as batches 1 and 2. **What was read:** every robot's humanoid.guide page, its whole text searched
for wheels, legs and walking. The makers' pages tried for the form (Noetix, Galbot, JAKA, Futuring, Kinetix AI,
Persona AI) gave no sentence on it. The type 2 robots decided on 2026-10-28 ("Those with model files": the H2, H2 Plus,
H1-2, GR-2, GR-1) keep type 2, as the workbook's named robots keep theirs. **Not in the catalogue:** the Unitree H1,
which the workbook names (type 2 excluded, type 5 borderline); the catalogue has only the H1-2.

| # | Robot (maker) | Catalogue: status, height, mass | Type | Form | Size against the type | Reason | Border |
|---|---|---|---|---|---|---|---|
| 101 | Futuring 2 (Futuring Robot, CN) | prototype, ~150–160 cm, 70 kg | 4 | not stated | height below | companion, healthcare and assisted living, public service and hospitality; also education and research | |
| 102 | G1 (Unitree, CN) | in production, 127 cm, 35 kg | 1 | legs | inside | R1: type 1's anchor | |
| 103 | G1+ (Unitree) | in production, 134 cm, 35 kg | 1 | no wheels named | inside | R4: the upgraded G1, "for research and education", "in labs and classrooms" | the catalogue's market: industrial manufacturing, logistics |
| 104 | G1-D (Unitree) | in production, 160 cm, 90 kg | 2 | wheels in its Ultimate version; the other version a lifting column on a stand | mass above | R4: AI training data collection, developers, research | its version without the wheeled base is an upper body only |
| 105 | G2 Genie (AgiBot) | prototype, 175 cm, 55 kg | 3 | wheels | inside | "built to industrial standards ... on factory floors and in public venues" | |
| 106 | G2 Max (AgiBot) | in production, 179 cm, 185 kg | 3 | wheels | mass above | heavy-payload factory work, palletizing | |
| 107 | Galbot (Galbot G1, CN) | prototype, 173 cm, 88 kg | 3 | wheels (the ET1 page: "the G1, which rolls rather than walks") | inside | "next-generation industrial robot", material handling | |
| 108 | Galbot ET1 (Galbot) | prototype, 173 cm, 65 kg | 3 | legs ("first fully bipedal humanoid") | inside | automotive industry, industrial automation, manufacturing (specs estimated by the catalogue) | |
| 109 | Galbot S1 (Galbot) | in production, 179 cm, 320 kg | 3 | not stated | mass far above | heavy loads in factories | |
| 110 | Gen 1 (Persona AI, US) | prototype, 175 cm, 70 kg | 5 | not stated | mass below | heavy industry: welding in shipyards and steel plants, teleoperated | no sealing stated; otherwise type 3 |
| 111 | GENE.01 (Generative Bionics, IT) | concept (production expected Q4 2026), ~170 cm, ~60–80 kg | 3 | not stated | inside | industrial automation, collaborative robotics | |
| 112 | Gento Luna (Gento Robotics, CN) | prototype, 170 cm, 90 kg | 2 | wheels | mass above | R3: commercial services, home service, industrial inspection, research and education | |
| 113 | Gino 1 (Geek+, CN) | in production, 168 cm, 63 kg | 3 | wheels | inside | "general-purpose humanoid built specifically for warehouses" | |
| 114 | GoMate (GAC Group, CN) | prototype, 140 cm, 45 kg | 2 | wheels (a four-wheel mode and a second posture) | height below | R3: car production, education, elderly care, logistics, security patrol | factory deployment planned (type 3); security patrol (type 6?) |
| 115 | GoMate Mini (GAC Group) | prototype, 170 cm, 60 kg | 2 | wheels ("legs that end in wheels") | inside | R3: car production lines, campus and subway security, guided tours | security is two of its five uses (type 6?) |
| 116 | GR-1 (Fourier, CN) | prototype, 165 cm, 55 kg | 2 | legs ("walk at 5 km/h") | inside | decided 2026-10-28: a type 2 robot | |
| 117 | GR-2 (Fourier) | prototype, 175 cm, 65 kg | 2 | no wheels named | inside | decided 2026-10-28: a type 2 robot | |
| 118 | GR-3 (Fourier) | in production, 165 cm, 71 kg | 4 | no wheels named | inside | R1: named in type 4 | |
| 119 | H1-2 (Unitree) | in production, 178 cm, 70 kg | 2 | no wheels named | inside | decided 2026-10-28: a type 2 robot | |
| 120 | H2 (Unitree) | prototype, 180 cm, 70 kg | 2 | legs | inside | R1: type 2's anchor | |
| 121 | H2 Plus (Unitree) | pilot, 180 cm, 68 kg | 2 | legs | inside | R1: named in type 2 | the same body as 140 |
| 122 | H2-D (Unitree) | in production, 170 cm, 120 kg | 2 | wheels in its Flagship version; the other a column | mass above | R4: AI training data collection, developers, research | its version without the wheeled base is an upper body only |
| 123 | H2-X (Unitree) | prototype, 182 cm, 70 kg | 2 | no wheels named | inside | the H2 body; R3: research, service, security ("serve and guard you") | security (type 6?) |
| 124 | HELIOS (ORBIT Robotics, CH) | prototype, 160 cm, ~60–80 kg | — | unclear: four arms, no legs, for microgravity | — | space research | form: left for the end |
| 125 | HIVA Haiwa (Haier, CN) | prototype, 165 cm, 70 kg | 4 | wheels ("a stable, wheeled mobile base") | inside | household chores, "Housework Terminator" | |
| 126 | HMND 01 (Humanoid, UK) | prototype, 175 cm, 70 kg | 3 | legs ("walking speed of up to 1.5 m/s") | inside | "industrial, logistics, and service automation" | maybe the same robot as 127 |
| 127 | HMND 01 Alpha (Humanoid) | prototype, 179 cm, 90 kg | 3 | legs ("Bipedal") | height above | industrial, logistics, retail restocking, warehouse | maybe the same robot as 126 |
| 128 | Hobbs (Noetix Robotics) | in production, ~120–140 cm, ~40–50 kg | — | unclear: "smooth upper-body motion", "a mobile upper body", works "at table height" | — | research and education, service demonstration | form: an upper body only? left for the end |
| 129 | Hobbs W1 (Noetix Robotics) | in production, 170 cm, 75 kg | 4 | wheels | mass above | "guide expert": reception, exhibition and hospital guidance | |
| 130 | HONOR (HONOR, CN) | prototype, 160 cm, 80 kg | 4 | not stated | mass above | "service and natural human interaction": retail, workplaces, homes | |
| 131 | HONOR A1 (HONOR) | prototype, 136.9 cm, 40 kg | 4 | legs (running) | both below; type 1's size | public spaces, retail, stage and events | |
| 132 | HONOR D1 (HONOR) | prototype, 169 cm, 45 kg | 2 | legs (ran a half-marathon) | mass below | no use given; full-scale (R5) | no stated use |
| 133 | HSR-ER-HR705 (Huashu Robot, CN) | prototype, 170 cm, 200 kg | 3 | wheels | mass above | "wheeled industrial humanoid" for factories | |
| 134 | I-Series (Simplexity Robotics, CN) | prototype, 175 cm, 60 kg | 2 | legs ("balance during walking") | inside | R3: AI research, industrial automation, logistics, retail | |
| 135 | IGRIS-C (ROBROS, KR) | production, 154 cm, 56 kg | 2 | not stated | height slightly below | R3: "AI research and industrial proof-of-concept deployments" | the catalogue's market: industrial manufacturing (type 3) |
| 136 | IRON (XPeng, CN; the 2025 robot) | prototype, 173 cm, 70 kg | 4 | not stated | inside | the catalogue: "Early focus on commercial deployments", stores | factory work also named (type 3) |
| 137 | IRON (XPeng; the earlier prototype) | prototype, 180 cm, 90 kg | 2 | not stated | height above, mass above | R3: retail, healthcare, logistics | an earlier robot of the same name as 136 |
| 138 | Isaac 0 (Weave Robotics, US) | in production, 170 cm, not given | — | an upper body only ("it stays in one place") | — | not assigned (decided 2026-10-28); its use, laundry folding at home, would be type 4 | |
| 139 | Isaac 1 (Weave Robotics) | pre-order, 160 cm, 40 kg | 4 | wheels | mass below | home chores: laundry, tidying | |
| 140 | Isaac GR00T (NVIDIA, US) | pilot, 180 cm, 68 kg | 2 | legs | inside | the H2 Plus body with Sharpa hands and Jetson Thor ("pairs a Unitree H2 Plus humanoid body") | listed twice: the same robot as 121 |
| 141 | JAKA K1 (JAKA Robotics, CN) | prototype, 165 cm, 40 kg | 2 | not stated | mass below | R3: "both industrial and service roles" | |
| 142 | JAKA Kargo (JAKA Robotics) | in production, 156.5 cm, 180 kg | 3 | wheels | mass above | sorting, material handling, loading in factories and warehouses | |
| 143 | JAKA π (JAKA Robotics) | in production, 122 cm, 42 kg | 4 | no wheels named | both below; type 1's size | retail, entertainment, companion and elderly care; also higher education | higher education and size (type 1) |
| 144 | JingChu (JCBOT, CN) | in production, 170 cm, 65 kg | 2 | legs ("walks on two legs") | inside | R3: "mainly for education and service work" | education (type 2) or service (type 4) |
| 145 | Jingchu Elf (JCBOT) | prototype, 165 cm, 70 kg | 4 | wheels ("a precise, two-wheel-drive base") | inside | guides and serves people: reception, exhibition halls | |
| 146 | Jupiter (Zeroth, CN) | early production, 165 cm, 60 kg | 2 | not stated | inside | R3: front-of-house service, logistics, research, security patrol, training | security (type 6?) |
| 147 | K0 (ROBOTIS, KR) | prototype, 130 cm, 34 kg | 1 | not stated | inside | R4: open research platform (CAD, source code) | |
| 148 | K1 (Booster Robotics, CN) | in production, 95 cm, 19.5 kg | 1 | no wheels named | both far below | R4: education, research labs, competitions | |
| 149 | K2 Bumblebee (Kepler, CN) | prototype, 175 cm, 75 kg | 2 | not stated | inside | R4: research, education, AI labs | |
| 150 | KAI (Kinetix AI, CN) | prototype, 173 cm, 70 kg | 4 | not stated | inside | "closer to a household assistant than a factory-only system" | |

**Batch 3 by type** (rows counted): type 1: 4; type 2: 20 rows, 19 robots (Isaac GR00T is the H2 Plus); type 3: 11;
type 4: 11; type 5: 1; type 6: 0; unclear, left for the end: 2 (HELIOS, Hobbs); not assigned: 1 (Isaac 0, an
upper body). **A question that recurs:** robots for civilian security patrol (campus, subway, "serve and guard"):
GoMate, GoMate Mini, H2-X, Jupiter, and Cinnamon 1 in batch 2. The workbook's type 6 is "reconnaissance, riot control,
EOD/hazmat, disaster response, and combat logistics", with ruggedisation; patrol robots are not described so. They are
proposed to type 2 (several uses) until Matthias decides.

**Decided, 2026-10-28** (security): "If it is clear security then 6 seems to me better, just the definition has to be
changed. If there are other purpose then they stay in 2". So a robot built for security alone goes to type 6; one with
security among other uses stays in type 2. Applied: GoMate, GoMate Mini, H2-X, Jupiter and Cinnamon 1 each name other
uses besides security, so all five stay in type 2; none of batches 1 to 4 is a security robot alone. **Still open:**
type 6's definition (the workbook's Taxonomy, row 7) is to be changed to take in civilian security; the workbook is
Matthias's.

### E4.4 Batch 4 of 7: robots 151 to 200 (2026-10-28). Not entered

Read and proposed as batches 1 to 3. **What was read:** every robot's humanoid.guide page, its whole text searched
for wheels, legs and walking; no maker's page was needed beyond them.

| # | Robot (maker) | Catalogue: status, height, mass | Type | Form | Size against the type | Reason | Border |
|---|---|---|---|---|---|---|---|
| 151 | KAIST Humanoid v0.9 (KAIST DRCD Lab, KR) | prototype, 165 cm, 75 kg | 2 | legs ("full-size bipedal") | inside | R4: a university research robot | |
| 152 | Kaleido 9 (Kawasaki, JP) | prototype, 190 cm, 99 kg | 5 | legs ("waist and leg joints") | both above | disaster response, heavy industry | disaster response is also in type 6's definition |
| 153 | Kangaroo (PAL Robotics, ES) | prototype, 160 cm, 40 kg | 2 | legs ("bipedal"); its text speaks of no arms | mass below | R4: research in dynamic legged locomotion | size between types 1 and 2; arms not stated |
| 154 | KAPEX (LG and KIST, KR) | prototype, 175 cm, 65 kg | 2 | legs ("bipedal motion") | inside | R3: home, industrial automation, logistics, manufacturing, research | |
| 155 | Keenon XMAN-R1 (KEENON, CN) | in production, 172 cm, 110 kg | 4 | not stated | mass above | "embodied service robot" for hospitality and logistics (the catalogue's market reads "China") | |
| 156 | Kengo (Galaxea Dynamics, CN) | prototype, 170 cm, 65 kg | 2 | legs ("bipedal") | inside | R3: factories, commercial spaces, homes | |
| 157 | Kepler (Kepler Forerunner K1, S1, D1, CN) | prototype, 170 cm, 88 kg | 2 | not stated | mass above | R3: "industrial, research, and safety applications" | one entry for three models |
| 158 | Kepler K2 (Kepler Forerunner K2) | prototype, 178 cm, 85 kg | 3 | not stated | height above | "commercial and industrial applications", manufacturing, logistics | maybe the same robot as 149, K2 Bumblebee (batch 3, type 2) |
| 159 | Kinisi 01 (Kinisi Robotics, US) | prototype, not given | 3 | wheels ("a low-profile omnidirectional base") | not given | warehouse pick and place, retail restocking | the same robot as 160 ("Kinisi 01 (KR1)") |
| 160 | Kinisi KR1 (Kinisi Robotics) | prototype, 162 cm, 100 kg | 3 | wheels | height below | warehouse tasks, pick and place, sorting | the same robot as 159 |
| 161 | Knowin-X1 (Knowin, CN) | prototype, 140 cm, 50 kg | 4 | wheels | height below | home: tidying, laundry, folding | |
| 162 | KUAVO 5-W (Leju Robotics, CN) | in production, 200 cm, 156 kg | 4 | wheels | both above | R1: named in type 4 ("Borderline crossover") | its uses are mostly industrial (manufacturing, logistics, data collection) |
| 163 | Kuavo-5 (Leju Robotics) | prototype, 168 cm, 55 kg | 2 | legs or wheels ("switch between walking and wheeled locomotion") | inside | R3: home, industrial automation, logistics, research | |
| 164 | Kuavo-my (Leju Robotics) | prototype, 145 cm, 45 kg | 4 | not stated | both below | R1: named in type 4; a guide in exhibition halls and shopping centres | the workbook's KUAVO-MY is 1.73 m, 63.5 kg; the catalogue also lists an XTRON KUAVO-MY (166 cm, 55 kg) |
| 165 | L1 (Moon Dynamics, CN) | in production, 165 cm, 60 kg | 3 | wheels ("a wheeled-bipedal base") | slightly below | heavy loads in warehouses and factories | |
| 166 | Laborer C1 (Glroad, CN) | in production, 138 cm, 38 kg | 4 | legs ("bipedal") | both below; type 1's size | hotel reception, station guidance, tours, performance | |
| 167 | Laborer M1 (Glroad) | in production, 187 cm, 86 kg | 3 | legs ("bipedal") | height above | industrial heavy-load handling, 50 kg with both arms | 430 N·m joints and a 50 kg load are type 5's marks |
| 168 | LightBot-0 (Light Origins, CN) | prototype, 90 cm, 35 kg | 1 | legs (walks, climbs, jumps) | height far below | R4: research and education | |
| 169 | LimX (CL-1, LimX Dynamics, CN) | prototype, 157 cm, 50 kg | 2 | legs (dynamic stair climbing) | height slightly below | no use given; a stair-climbing demonstrator (R5) | no stated use; maybe inside 170, the CL series |
| 170 | LimX CL (LimX Dynamics) | prototype, 164 cm, 45 kg | 2 | legs (stair climbing) | mass below | R3: household services, industrial automation, R&D | one entry for a series (CL-1 to CL-3) |
| 171 | LimX Oli (LimX Dynamics) | in production, 165 cm, 55 kg | 2 | not stated | inside | R4: "full-size humanoid for embodied AI R&D" (the catalogue's market reads "Global") | |
| 172 | LinkerArm A7 (LinkerBot, CN) | in production, 140 cm, 40 kg | — | a robot arm ("a seven-axis robotic arm") | — | not assigned (decided 2026-10-28): arms only | |
| 173 | Lumen H1 (HECbot, CN) | in production, 169 cm, 69 kg | 4 | not stated | inside | "interactive service work": reception, retail, eldercare | |
| 174 | Lumen S1 (HECbot) | in production, 130 cm, 35 kg | 4 | not stated | both below; type 1's size | companionship, eldercare, entertainment, exhibitions | |
| 175 | LUMO (DOBOT, CN) | in production, 130 cm, 35 kg | 4 | legs ("walks in a natural, humanlike way") | both below; type 1's size | "companion humanoid" for homes and schools | |
| 176 | Luna (LimX Dynamics) | prototype, 165 cm, 55 kg | 4 | not stated | inside | home assistance, service; "approachable in social and service environments" | |
| 177 | LUS2 (Lumos Robotics, CN) | early production, 160 cm, 65 kg | 2 | not stated | inside | R4: "a practical research platform" | |
| 178 | MagicBot (MagicLab, CN) | prototype, 138 cm, 54 kg | 4 | not stated | height below | entertainment, events, public shows | |
| 179 | MagicBot D1 (MagicLab) | in production, 180 cm, 150 kg | 3 | wheels | both above | "industrial wheeled humanoid" for factories and warehouses | |
| 180 | MagicBot Gen1 (MagicLab) | in production, 174 cm, 70 kg | 2 | legs ("walks on two legs") | inside | R3: "general-purpose": research labs, flexible factory work, customer service | |
| 181 | MagicBot X1 (MagicLab) | in production, 170 cm, 65 kg | 2 | not stated | inside | R3: commercial services, healthcare, home, manufacturing, logistics | |
| 182 | MagicBot Z1 (MagicLab) | prototype, 140 cm, 40 kg | 4 | not stated | both below; type 1's size | education, home companionship | |
| 183 | Maker H01 (GigaAI, CN) | prototype, 160 cm, 64 kg | 4 | wheels | inside | home service, hospitality, reception, workplace assistance | |
| 184 | Mantis Standart (Blue Worm, CN) | in production, 140 cm, 50 kg | 2 | wheels | height below | R3: commercial service, data collection, manufacturing, home, warehousing | modular: some of its forms are an arm or an upper body only |
| 185 | Martian (Unix Group, CN) | prototype, 160 cm, 50 kg | 4 | legs ("walks with stable balance") | mass below | the catalogue's markets: home service, office and mall, reception and guiding | its text: "industrial and research environments" (type 3 or 2) |
| 186 | Matrix-1 (Matrix Robotics, CN) | prototype, 180 cm, 67 kg | 3 | legs (walks 7.6 km/h) | height above | "light-duty manufacturing and logistics work" | |
| 187 | MATRIX-3 (Matrix Robotics) | prototype, ~160–180 cm, not given | 2 | legs ("Its body walks") | not given | R3: commercial robotics, logistics, service | |
| 188 | MEMO (Sunday Robotics, US) | prototype, 170 cm, 77 kg | 4 | wheels ("wheeled, semi-humanoid") | mass above | household chores | |
| 189 | MenteeBot (Mentee Robotics, IL) | prototype, 175 cm, 70 kg | 2 | not stated | inside | R3: "both domestic and industrial applications" | an earlier version of 190 |
| 190 | MenteeBot V3 (Mentee Robotics) | prototype, 175 cm, 65 kg | 3 | not stated | inside | "warehouse automation", 25 kg payload | |
| 191 | MH3 (Mirsee Robotics, CA) | in production, 180 cm, 125 kg | 5 | not stated | mass above | critical infrastructure, infrastructure maintenance; teleoperated | healthcare and defence also named (type 6?) |
| 192 | MICO (Flexiv Robotics) | in production, 150 cm, 79 kg | — | unclear: "full-upper-body humanoid system", "does not walk or run" | — | industrial manufacturing, logistics, research | form: an upper body only? left for the end |
| 193 | MIRO (Midea, CN) | prototype, not given | 3 | wheels | not given | "purpose-built for next-generation factory automation" | |
| 194 | Mirokaï (Enchanted Tools, FR) | prototype, 123 cm, 29 kg | 4 | rolls on a ball ("a unique rolling globe system") | both below | social environments, interaction and light logistics | |
| 195 | Moby (Noble Machines, US) | prototype, 170 cm, 45 kg | 3 | not stated | mass below | its text: "general-purpose industrial robot built for hazardous and physically demanding work" | the catalogue's markets: hospitality, research, service; hazardous (type 5?); maybe the same robot as 196 |
| 196 | Moby (old) (Under Control Robotics, US) | prototype, 170 cm, 45 kg | 3 | not stated | mass below | the same name, size, joints and markets as 195 | maybe the same robot as 195 |
| 197 | Modular (O-ID, JP) | early production, 172 cm, 70 kg | 3 | wheels | inside | warehouses, factories, commercial spaces | |
| 198 | Mornine (AiMOGA, Chery, CN) | in production, 167 cm, 70 kg | 4 | legs ("bipedal") | inside | car dealerships, reception, retail, sales | |
| 199 | Motion 2 (VinMotion, VN) | prototype, ~160–165 cm, ~60–75 kg | 2 | legs ("controlled walking") | inside | R3: factory automation, research and education | |
| 200 | Moz1 (Spirit AI, CN) | prototype, 160 cm, 70 kg | 2 | not stated | inside | R3: AI research, education, service robotics | |

**Batch 4 by type** (rows counted): type 1: 1; type 2: 17; type 3: 12 (Kinisi 01 and KR1 one robot, Moby and Moby
(old) maybe one); type 4: 16; type 5: 2; type 6: 0; unclear, left for the end: 1 (MICO); not assigned: 1 (LinkerArm
A7, an arm).

**Decided, 2026-10-28** (robots listed twice): "No double counting use just 1". Each robot the catalogue lists twice
is one entry. The pairs, read as the same robot (same maker, and the same size and joints or a text saying so), and
the entry kept:
- 2 4NE-1 and 3 4NE1: 3 kept (type 3);
- 36 Asimov and 37 Asimov 1: 37 kept (type 1);
- 69 CyberOne and 70 CyberOne v2: 69 kept (type 2);
- 121 H2 Plus and 140 Isaac GR00T: 121 kept (type 2, the workbook's name);
- 126 HMND 01 and 127 HMND 01 Alpha: 127 kept (type 3);
- 149 K2 Bumblebee and 158 Kepler K2: 158 kept; proposed type 3 (its entry: "commercial and industrial
  applications"; 149's entry: research and education, type 2), for Matthias to confirm;
- 159 Kinisi 01 and 160 Kinisi KR1: 160 kept (type 3);
- 169 LimX CL-1 and 170 LimX CL: 170 kept (type 2), the series that holds the CL-1;
- 195 Moby and 196 Moby (old): 195 kept (type 3);
- 220 Optimus and 222 Optimus Gen2 (batch 5): 222 kept (type 2).
Generations of one line (NEO, NEO Beta, NEO Gamma; Atlas and Atlas (old); Phoenix and Phoenix Gen 8) are different
robots and stay separate.

**Decided, 2026-10-28** (two types; identical robots): "Double assignment possible, but no two identical. This chnges
the statistics", then "Double assignment means 1 robot can be two types. Identical one means they are assigned to the
same type but the rest is identical. For example sold by different companies under different names, but be the same.
Identical". This replaces "A robot has to be in one but not two types": a robot may be in two types. Two entries that
are the same robot (also sold by different companies under different names) are one entry. **Still open:** which
robots get two types, and how a robot in two types is counted in the statistics.

### E4.5 Batch 5 of 7: robots 201 to 250 (2026-10-28). Not entered

Read and proposed as batches 1 to 4. **What was read:** every robot's humanoid.guide page, its whole text searched
for wheels, legs and walking.

| # | Robot (maker) | Catalogue: status, height, mass | Type | Form | Size against the type | Reason | Border |
|---|---|---|---|---|---|---|---|
| 201 | N2 (Noetix Robotics, CN) | prototype, 118 cm, 30 kg | 4 | legs ("bipedal gait") | both far below; type 1's size | home, education, elder care | |
| 202 | Nadia (IHMC, US) | prototype, 190 cm, 100 kg | 6 | legs ("biped") | both above | defence, disaster response; the forerunner of Alex (type 6) | research also named |
| 203 | NAVAI-I3 (Zhejiang Humanoid Robot Innovation Center, CN) | prototype, 180 cm, 70 kg | 2 | legs ("walks with steady posture") | inside | R4: research institutions, labs, AI development | |
| 204 | Navigator 2 (Zhejiang Humanoid Robot Innovation Center) | prototype, 165 cm, 60 kg | 3 | legs ("stable walking at speeds of up to 6 km/h") | slightly below | the catalogue's summary: "for industrial applications" | |
| 205 | NE01 (GENISOM AI, CN) | prototype, 145 cm, 40 kg | 4 | not stated | both below; type 1's size | commercial performances, cultural tourism; research also | |
| 206 | NEO Beta (1X Technologies, US) | prototype, 165 cm, 30 kg | 4 | not stated | mass below | the NEO line, for homes; "homes, workplaces, and industrial settings" | an earlier NEO (1) |
| 207 | NEO Gamma (1X Technologies) | prototype, 165 cm, 35 kg | 4 | not stated | mass below | "home-focused humanoid" | an earlier NEO (1) |
| 208 | Neo1 (Neodra Dynamics, CN) | prototype, 400 cm, 1,200 kg | 5 | not stated | both far above | construction, demolition, mining, nuclear, deep sea, rescue | a 4 m, 1.2 t hydraulic "mecha": a humanoid robot in this study's sense? |
| 209 | NEXO (Galaxea Dynamics, CN) | prototype, 168 cm, 85 kg | 3 | wheels ("a slim, wheeled base") | inside | logistics, manufacturing, commercial services | |
| 210 | Nezha P01 (Digit Robotics, CN) | prototype, 145 cm, 65 kg | 2 | legs ("dynamic legged locomotion") | height below | R4: research, education, AI labs; "full-size" | height of type 1, mass of type 2 |
| 211 | NIX (Lumos Robotics, CN) | prototype, 80 cm, 20 kg | 4 | legs ("walks steadily on two legs") | both far below | public spaces, homes, learning; "service-oriented" | |
| 212 | NORI L3 (Nori Robotics, CN) | in production, 145 cm, 40 kg | 1 | wheels ("a wheeled mobile base with two robotic arms") | inside | R4: research, education, AI development (the catalogue's summary line describes another robot) | |
| 213 | North (Sharpa, SG) | prototype, 160 cm, 90 kg | 2 | wheels | mass above | R3: "service and industrial settings"; food service, hospitality, manufacturing, research | |
| 214 | Northstar (UMA, FR) | prototype, 165 cm, 40 kg | 2 | not stated | mass below | R3: home, healthcare, logistics, manufacturing | |
| 215 | Nova (ugo, JP) | prototype, 162 cm, 90 kg | 3 | wheels ("a four-wheel mecanum base") | mass above | industrial, manufacturing, warehousing | |
| 216 | Omni (X-Humanoid, CN) | prototype, ~165 cm, ~55–75 kg | 2 | legs ("fluid walking") | inside | R3: interactive service, logistics, research | |
| 217 | Onero H1 (SwitchBot, JP) | prototype, ~120–130 cm, ~35 kg | 4 | not stated | both below; type 1's size | home assistance, smart home | |
| 218 | OpenArm 02 (Enactic, JP) | in production, not given, 30 kg | — | two arms ("OpenArm has no legs, wheels, or wings") | — | not assigned (decided 2026-10-28): arms only | |
| 219 | Operator OP1 (Ultra Robotics, US) | in production, 180 cm, 140 kg | — | stationary ("does not walk anywhere", "a 5-by-5-foot fixed base") | — | not assigned (decided 2026-10-28): an upper body on a fixed base | |
| 220 | Optimus (Tesla, US) | prototype, 173 cm, 56 kg | →222 | — | — | its text describes "Generation 2"; the same size and joints as 222 | listed twice: counted as 222 |
| 221 | OPTIMUS GEN 3 (Tesla) | in production, 180 cm, 52 kg | 2 | no wheels named | inside | R1: qualifying in type 2 | |
| 222 | Optimus Gen2 (Tesla) | prototype, 173 cm, 56 kg | 2 | no wheels named | inside | R1: the workbook's type 2 lists "Optimus Gen 2/Gen 3" | |
| 223 | OPTIMUS V2.5 (Tesla) | prototype, 176.5 cm, 55 kg | 2 | legs ("walks, runs, climbs stairs") | inside | the step between Gen 2 and Gen 3, both in type 2 | |
| 224 | Orca (Cyan Robotics, CN) | prototype, 160 cm, 50 kg | 2 | legs ("bipedal") | at the lower limits | R4: research labs, universities, education | |
| 225 | Origin (HIRO Industries, US) | prototype, 160 cm, not given | — | an upper body ("It has no legs and does not walk"; "dual-arm workstation robot") | — | not assigned (decided 2026-10-28) | |
| 226 | P0 (Pink Robotics, DE) | prototype, 175 cm, 82 kg | 3 | not stated | inside | logistics sorting | |
| 227 | Panther (Unix Group, CN) | pilot, 160 cm, not given | 3 | wheels ("a mobile chassis") | height below | industrial logistics, manufacturing, warehouses | |
| 228 | Phantom MK1 (Foundation, US) | prototype, 175 cm, 80 kg | 6 | not stated | inside | R1: named in type 6 | |
| 229 | Phoenix (Sanctuary AI, CA) | prototype, 170 cm, 70 kg | 2 | not stated | inside | R3: "adapt to multiple industries" | an earlier Phoenix than 230 |
| 230 | Phoenix Gen 8 (Sanctuary AI) | prototype, 170 cm, 70 kg | 2 | wheels ("rolls on a wheeled base") | inside | R4: "mainly to capture high-quality training data"; industrial, logistics | |
| 231 | PHYBOT C1 (PHYBOT, CN) | prototype, 125 cm, 25 kg | 1 | not stated | mass below | R4: research, education, AI labs | |
| 232 | PHYBOT M1 (PHYBOT) | early production, 172 cm, 60 kg | 2 | not stated | inside | R3: embodied AI testing, research labs, heavy object handling, logistics | |
| 233 | pib.Pro (isento robotics, DE) | in production, 80 cm, not given | — | unclear: not stated, its forerunner pib a 3D-printed kit | — | education, research | form: an upper body only? left for the end |
| 234 | PM01 (EngineAI, CN) | prototype, 138 cm, 40 kg | 1 | legs ("bipedal walking gait") | inside | R4: open-source testbed for AI research | |
| 235 | PR-34D (Perceptyne, IN) | pilots, not given | — | unclear: "semi-humanoid", "dual-arm system" on assembly lines | — | car and electronics assembly | form: an upper body only? left for the end |
| 236 | PrimeBOT Q1 (PrimeBOT, CN) | prototype, 88 cm, not given | 4 | not stated | height far below | "consumer-grade personal robot" | developers and robotics education also (type 1) |
| 237 | PrimeBOT T1 (PrimeBOT) | prototype, 60 cm, 8.5 kg | 4 | wheels ("upright on wheeled legs"); changes into a four-legged form | both far below | consumer home use | form: half the time a quadruped |
| 238 | ProWhite (PL-Universe, CN) | in production, ~155–165 cm, ~45–55 kg | 4 | legs ("basic walking") | mass below | reception, guidance in hotels, offices, exhibition halls | |
| 239 | Psi V1 (PsiBot, CN) | in production, 175 cm, 150 kg | 3 | not stated | mass above | industrial automation, light industrial tasks | |
| 240 | Pudu D7 (Pudu Robotics, CN) | prototype, 165 cm, 45 kg | 4 | wheels ("an omnidirectional chassis") | mass below | "service robot": elevators, item transport, sorting | |
| 241 | Pudu D9 (Pudu Robotics) | prototype, 170 cm, 55 kg | 3 | legs ("bipedal") | mass below | the catalogue's summary: "versatile industrial applications"; two 20 kg arms | |
| 242 | PX5 (XPeng, CN) | prototype, 150 cm, 109 kg | 2 | legs ("bipedal locomotion") | height below, mass above | R3: "industrial and domestic tasks", industry and retail | |
| 243 | QDH (Apptronik, US) | prototype, ~165 cm, ~60–70 kg | — | unclear: 14 joints, its body not stated | — | logistics, manufacturing, research | form: an upper body only? left for the end |
| 244 | Qinglong V3.0 (OpenLoong, CN) | early production, 165 cm, 75 kg | 2 | legs ("It can walk") | inside | R4: academic research, humanoid R&D | |
| 245 | QUANTA X2 (X Square Robot, CN) | prototype, 172 cm, 95 kg | 2 | wheels | mass above | R3: "general-purpose service tasks" in homes, public venues, labs, logistics | |
| 246 | QUESTER1 (Q1, AgiBot) | prototype, 79 cm, ~20–30 kg | 1 | not stated | both far below | R4: embodied AI research, education | |
| 247 | R1 PRO (Galaxea Dynamics) | in production, 170 cm, 96 kg | 2 | wheels | mass above | R3: industrial automation and R&D, research labs, warehouse pick and place | |
| 248 | R1-D (Unitree) | in production, 160 cm, 52 kg | 2 | wheels (the R1-A7-D version) | inside | R4: AI training data collection, developers, research | |
| 249 | RAISE A1 (AgiBot) | prototype, 175 cm, 55 kg | 3 | legs ("stable bipedal walking") | inside | manufacturing, logistics; AgiBot's first generation | |
| 250 | RayNex G3 (NineRay, CN) | in production, 173 cm, 60 kg | 3 | legs ("80 kg walking load") | inside | industrial, manufacturing; 100 kg deadlift | its loads are type 5's marks |

**Batch 5 by type:** type 1: 4; type 2: 17; type 3: 9; type 4: 10; type 5: 1; type 6: 2; unclear, left for the end: 3
(pib.Pro, PR-34D, QDH); not assigned: 3 (OpenArm 02, Operator OP1, Origin); listed twice: 1 (Optimus).

**Received, 2026-10-28, its reading open** (industry): "If industry is listed industry. It could be just heavy duty in
industry". Two readings, for Matthias to choose; nothing has been moved yet:
- *Narrow:* where type 3 and type 5 compete, a robot whose use is industry is type 3, heavy duty or not; type 5 keeps
  the hazardous environments. Moves Persona Gen 1, CYBORG RO1 and WO1, Kaleido 9 and Neo1 from 5 to 3 (each lists
  industry); Laborer M1 and RayNex G3 stay 3. The robots with industry among other uses stay in type 2 (R3).
- *Wide:* any robot that lists industry is type 3. Moves, besides those five, about 37 robots from type 2 (R3: Adam SP,
  KAPEX, Kengo, MagicBot X1, North, PX5, R1 PRO and others) and NEO Beta from type 4.
Settled by the rule for two types (E4.6).

### E4.6 The rule for two types, applied to batches 1 to 5 (2026-10-28). Not entered

**Decided, 2026-10-28:** "Rule holds", on this rule as Claude proposed it: (1) a robot that lists industry has type 3
as one of its types; heavy duty in industry stays type 3; type 5 is for hazardous environments only; (2) a second type
where another use is as strong: service, home or care type 4, research type 2 (type 1 if compact), hazardous type 5;
(3) security alone type 6; (4) type 2 alone for research platforms and robots with no leading use; (5) at most two
types. Shown with Kengo 3 and 4, A2 Max 3 and 4, CYBORG RO1 and WO1 3 and 5, Kaleido 9 3 and 5, AKINCI-5 3 and 1,
Laborer M1 and RayNex G3 3, KAPEX 3 and 4 or 3 and 2 (for Matthias).

**How Claude read it in the cases the rule leaves open** (for Matthias to check):
- *Industry* is manufacturing, industrial work, factories, warehouses, machine tending and logistics; "light
  logistics" and delivery inside buildings (FlashBot Arm, NIX, Mirokaï) are service.
- *Research as a second type* where the robot is offered as a research or developer platform or research is about a
  third of its uses; education for children is not research. A research institute's own mission robot (Alex, Nadia)
  keeps its mission type.
- *A robot the workbook names* keeps the workbook's type; if it lists industry, type 3 is its second.
- *Three or more kinds of use:* the two that lead; where research and service tie beside industry, research (type 2),
  marked.
- Two border cases are resolved by the two types: Kepler K2 and K2 Bumblebee (one robot) is 3 and 2; KUAVO 5-W is 4 and
  3.

**What changes** (number, robot: before, after; the robots not listed keep their one type):

| # | Robot | Before | After | Why | For Matthias |
|---|---|---|---|---|---|
| 3 | 4NE1 | 3 | 3, 4 | everyday tasks, services | |
| 5 | 4NE1 Gen 4 | 3 | 3, 4 | home assistance | |
| 7 | A2 Max | 3 | 3, 4 | healthcare | |
| 10 | Adam Lite | 2 | 3, 4 | "industrial and service applications" | |
| 11 | Adam SP | 2 | 3, 4 | industrial automation, service robotics | its text: research labs (3 and 2?) |
| 13 | AGIBOT A2-W | 3 | 3, 2 | research labs | |
| 15 | AGIBOT G1 | 2 | 2, 3 | data collection; industrial, manufacturing | |
| 17 | AgiBot X2 | 4 | 4, 3 | light industrial assistance | |
| 20 | AI Worker | 3 | 3, 2 | R&D | |
| 21 | AICO 2 | 3 | 3, 2 | research | |
| 22 | AIDOL | 3 | 3, 4 | its text: face and dialogue | |
| 23 | AKINCI-5 | 3 | 3, 1 | R&D, compact | |
| 29 | AlphaBot 2 | 3 | 3, 4 | public service, hospitality | |
| 33 | Apollo 2 | 3 | 3, 4 | retail | the workbook also names it in 2 and 5 (borderline) |
| 34 | ARI | 4 | 4, 2 | research | |
| 35 | ARMAR-7 | 4 | 4, 2 | research | |
| 40 | Astribot S1 | 2 | 2, 3 | logistics | service also |
| 41 | Astribot T1 | 2 | 2, 3 | industrial | service and home also |
| 42 | AstroDroid AD-01 | 3 | 3, 2 | research and education | |
| 43 | Atlas | 5 | 5, 3 | industrial automation, logistics, manufacturing | type 5's anchor lists industry only |
| 45 | Atom (DOBOT) | 4 | 4, 3 | "industrial automation to customer service" | |
| 57 | Bumi | 4 | 4, 1 | maker education, programming | |
| 60 | CASBOT W1 | 3 | 3, 2 | research | retail also |
| 61 | CASIVIBOT | 4 | 4, 3 | industrial and commercial service | |
| 62 | Centaur-G1 | 3 | 3, 4 | eldercare, home service | |
| 63 | Cinnamon 1 | 2 | 3, 4 | construction, industrial automation; service | security among other uses |
| 66 | Cruzr S2 | 3 | 3, 4 | healthcare | |
| 71 | CYBORG RO1 | 5 | 3, 5 | industrial manufacturing; hazardous sites | |
| 72 | CYBORG WO1 | 5 | 3, 5 | as 71 | |
| 73 | D01 | 2 | 3, 4 | manufacturing; food service, hospitality, retail | |
| 81 | DR02 | 5 | 5, 3 | industries, inspection, logistics | |
| 82 | Dual-Arm Lift | 2 | 2, 3 | industrial automation | |
| 84 | DUCO | 3 | 3, 4 | service robotics | |
| 85 | E1 | 1 | 1, 4 | entertainment, guided tours | |
| 86 | Eggie | 4 | 4, 2 | research and education | |
| 88 | Elixis | 3 | 3, 4 | healthcare, retail | |
| 90 | Eno | 2 | 3, 4 | manufacturing, logistics; healthcare, hospitality | |
| 92 | Feather | 2 | 2, 3 | manufacturing; labs and developers | |
| 98 | Figure 03 | 2 | 2, 3 | industries (the workbook: type 3 borderline) | |
| 102 | G1 (Unitree) | 1 | 1, 3 | its text: "research, industrial, and development tasks" | type 1's anchor |
| 103 | G1+ | 1 | 1, 3 | industrial manufacturing, logistics | |
| 105 | G2 Genie | 3 | 3, 2 | research and education | |
| 110 | Gen 1 (Persona AI) | 5 | 3 | heavy duty in industry | |
| 112 | Gento Luna | 2 | 3, 4 | industrial inspection; commercial and home services | |
| 114 | GoMate | 2 | 3, 4 | car production, logistics; elderly care | security among other uses |
| 115 | GoMate Mini | 2 | 3, 4 | car production lines; tours, public venues | security among other uses |
| 120 | H2 | 2 | 2, 3 | industries, logistics | |
| 134 | I-Series | 2 | 2, 3 | industrial automation, logistics | |
| 135 | IGRIS-C | 2 | 2, 3 | industrial manufacturing | |
| 136 | IRON (2025) | 4 | 4, 3 | factory work | |
| 137 | IRON (earlier) | 2 | 3, 4 | industrial tasks; retail, healthcare | |
| 141 | JAKA K1 | 2 | 3, 4 | "both industrial and service roles" | |
| 143 | JAKA π | 4 | 4, 1 | higher education | |
| 144 | JingChu | 2 | 2, 4 | education and research; service | |
| 146 | Jupiter | 2 | 3, 4 | logistics; front-of-house service | security and research among other uses |
| 150 | KAI | 4 | 4, 3 | light industrial | |
| 152 | Kaleido 9 | 5 | 3, 5 | heavy industry; disaster response | |
| 154 | KAPEX | 2 | 3, 4 | industrial automation, logistics, manufacturing; home | or 3 and 2 (research) |
| 155 | Keenon XMAN-R1 | 4 | 4, 3 | "industries like hospitality and logistics" | |
| 156 | Kengo | 2 | 3, 4 | factories; commercial spaces, homes | |
| 157 | Kepler (Forerunner series) | 2 | 2, 3 | industrial, research | rescue also |
| 158 | Kepler K2 (and K2 Bumblebee) | 3 | 3, 2 | industrial; research and education (149's entry) | |
| 162 | KUAVO 5-W | 4 | 4, 3 | industrial manufacturing, logistics | |
| 163 | Kuavo-5 | 2 | 2, 3 | industrial automation, logistics | home also |
| 170 | LimX CL | 2 | 2, 3 | industrial automation | household also |
| 175 | LUMO | 4 | 4, 1 | education, research | |
| 176 | Luna | 4 | 4, 2 | research | |
| 179 | MagicBot D1 | 3 | 3, 2 | education, research | |
| 180 | MagicBot Gen1 | 2 | 2, 3 | manufacturing | entertainment, hospitality also |
| 181 | MagicBot X1 | 2 | 3, 4 | manufacturing, logistics; services, healthcare, home | |
| 183 | Maker H01 | 4 | 4, 3 | its text: "factory floors or service environments" | |
| 184 | Mantis Standart | 2 | 2, 3 | manufacturing, warehousing | commercial and home service also |
| 185 | Martian | 4 | 4, 3 | its text: "industrial and research environments" | |
| 187 | MATRIX-3 | 2 | 3, 4 | logistics; commercial, service | |
| 189 | MenteeBot | 2 | 3, 4 | "both domestic and industrial applications" | |
| 195 | Moby (Noble Machines) | 3 | 3, 5 | its text: "hazardous and physically demanding work" | the catalogue's markets: hospitality, research |
| 199 | Motion 2 | 2 | 2, 3 | factory automation | |
| 200 | Moz1 | 2 | 2, 4 | service robotics | |
| 206 | NEO Beta | 4 | 4, 3 | "industrial settings" | |
| 208 | Neo1 | 5 | 5, 3 | heavy manufacturing | |
| 209 | NEXO | 3 | 3, 4 | commercial services | |
| 213 | North | 2 | 3, 4 | manufacturing; food service, hospitality, retail | |
| 214 | Northstar | 2 | 3, 4 | logistics, manufacturing; home, healthcare | |
| 216 | Omni | 2 | 2, 3 | logistics | interactive service also |
| 221 | OPTIMUS GEN 3 | 2 | 2, 3 | industrial automation, logistics, manufacturing | home also |
| 223 | OPTIMUS V2.5 | 2 | 2, 3 | as 221 | home also |
| 228 | Phantom MK1 | 6 | 6, 3 | industries | |
| 229 | Phoenix | 2 | 2, 3 | "multiple industries" | |
| 230 | Phoenix Gen 8 | 2 | 2, 3 | industrial, logistics | |
| 232 | PHYBOT M1 | 2 | 2, 3 | industrial logistics, heavy object handling | |
| 236 | PrimeBOT Q1 | 4 | 4, 1 | developers, robotics education | |
| 240 | Pudu D7 | 4 | 4, 3 | "multi-industry automation" | |
| 242 | PX5 | 2 | 3, 4 | "industrial and domestic tasks" | |
| 245 | QUANTA X2 | 2 | 3, 4 | logistics; cleaning, home service | research also |
| 247 | R1 PRO | 2 | 2, 3 | industrial automation, warehouse pick and place | |

**Batches 1 to 5 after the rule** (computed from the tables and the changes above in Claude's scratch folder,
`apply_two_types.py`): 223 robots with a type (250 entries, less 10 listed twice, 8 not assigned, 9 unclear), 94 of
them with two types. In each type, a robot with two types counted in both: type 1: 22; type 2: 61; type 3: 129;
type 4: 93; type 5: 9; type 6: 3. Unchanged and still for Matthias: ALPHA (3; hazardous, 5?), Fengxing-001 (3; 5 or
6?), MH3 (5; defence, 6?).

### E4.7 Batch 6 of 7: robots 251 to 300 (2026-10-28). Not entered

Read as batches 1 to 5, with the rule for two types (E4.6) and one entry per identical robot. **What was read:**
every robot's humanoid.guide page, its whole text searched for wheels, legs and walking. "Size" is against the first
type.

| # | Robot (maker) | Catalogue: status, height, mass | Types | Form | Size | Reason | For Matthias |
|---|---|---|---|---|---|---|---|
| 251 | RB-Y1 (Rainbow Robotics, KR) | in production, 160 cm, 131 kg | 3, 2 | wheels ("mobile manipulator") | mass above | "real-world industrial tasks"; built for "the generative AI era" | |
| 252 | Reachy 2 (Pollen Robotics, FR) | prototype, 166 cm, 50 kg | — | unclear: "a bimanual system", its base not stated | — | research and developers | form: an upper body only? left for the end |
| 253 | RealBot-01 (RealMan Robotics, CN) | in production, 168 cm, 125 kg | 2, 3 | wheels | mass above | "for research, automation, and practical manipulation": embodied AI, data collection; industrial automation | home service also |
| 254 | RealBot-L2 (RealMan Robotics) | in production, 170 cm, 120 kg | 4, 2 | wheels ("a two-wheel base") | mass above | home service, retail guidance; data collection | |
| 255 | RealBot-S2 (RealMan Robotics) | in production, 170 cm, 125 kg | 3, 2 | wheels ("a four-wheel mobile base") | mass above | industrial automation; data collection, embodied AI | home service, retail also |
| 256 | REEM-C (PAL Robotics, ES) | in production, 165 cm, 80 kg | 2 | legs ("full-size biped") | inside | R4: research and education in universities and labs | |
| 257 | Reflex (Reflex Robotics, US) | prototype, not given | 3 | wheels ("a stable wheeled base") | not given | warehousing and logistics | |
| 258 | REX G1 (RoboScience, CN) | prototype, 170 cm, 80 kg | 3, 4 | wheels | inside | factories, logistics, warehousing; homes, retail, supermarkets | |
| 259 | RNoid (Robot.com, US) | production-ready, 160 cm, 50 kg | 4 | not stated | mass below | hospitality, reception, workplace assistance | |
| 260 | Roban2 (Leju Robotics, CN) | prototype, 145 cm, 40 kg | 1 | not stated | inside | R4: research labs, education, demonstrations | |
| 261 | Robbyant R1 (Ant Group, CN) | in production, 160 cm, 110 kg | 4 | wheels | mass above | kitchens, hospitality, museum tours, healthcare, public services | |
| 262 | RoBee (Oversonic Robotics, IT) | in production, 190 cm, 180 kg | 3 | not stated | both above | industrial: "demanding, repetitive, or unsafe work" | |
| 263 | Robin (Roboligent, US) | in production, 150 cm, 80 kg | 3 | wheels ("a mobile base") | height below | factory automation, logistics, manufacturing, warehouse | |
| 264 | ROBO-T1 (Robo Robotics, US) | in production, 130 cm, 50 kg | 3 | not stated | height below | industrial automation, manufacturing | |
| 265 | Robotera L7 (Robotera, CN) | prototype, 171 cm, 65 kg | 3, 2 | legs ("full-size biped") | inside | factory and industrial automation; research labs | |
| 266 | Robotera M7 (Robotera) | in production, 119 cm, 43 kg | — | an upper body ("upper-body humanoid robot"; the L7's text: "a fixed-base upper-body") | — | not assigned (decided 2026-10-28) | |
| 267 | ROBOTERA Q5 (Robotera) | in production, 165 cm, 70 kg | 4 | wheels | inside | hospitality, retail, healthcare, tourism | |
| 268 | Roboto Origin (RoboParty, CN) | prototype, 125 cm, 34 kg | 1 | legs ("bipedal") | inside | R4: open source for makers, researchers, students | |
| 269 | RP1 (RoboParty) | prototype, 130 cm, 34 kg | 1 | legs ("bipedal") | inside | R4: research, developers, education; the successor of 268 | |
| 270 | SAO2 (EngineAI, CN) | in production, 125 cm, 25 kg | 4 | not stated | both below | a companion for teenagers in living rooms and dorms (its text: "SA02") | |
| 271 | SE01 (EngineAI) | prototype, 180 cm, 80 kg | 2 | not stated | inside | no use given; full-scale (R5) | no stated use |
| 272 | Sean (Zeroth Robotics, CN) | prototype, 155 cm, 45 kg | 2, 4 | not stated | both below | AI development, research; home assistance, retail | |
| 273 | Sherpa Mecha (Ati Robotics, US) | prototype, 200 cm, 180 kg | 3 | wheels ("does not walk on legs") | both above | factory work: automotive, electronics, energy, food, pharma | |
| 274 | Shimizu's Robot (Shimizu Corporation, JP) | prototype, 155 cm, not given | 3 | legs ("walks its site") | height below | construction site inspection | its maker builds, Sony is the partner: maybe another maker's robot, then identical to its entry |
| 275 | SkyWalker 2 (EIR Technology, CN) | production-ready, 165 cm, 55 kg | 3, 4 | not stated | slightly below | manufacturing, inspection; elder care, intelligent services | |
| 276 | Songxing (SIASUN, CN) | early production, 165 cm, 85 kg | 3, 2 | legs ("It can walk") | inside | industrial; industrial R&D, research and education | |
| 277 | Spaceo M1 (Muks Robotics, IN) | in production, 167 cm, 65 kg | 4 | wheels ("rolling at a brisk 2 m/s") | inside | "service android": healthcare, hospitality, retail restocking | |
| 278 | Spaceo Pro (Muks Robotics) | in production, 167 cm, 65 kg | 3 | wheels ("integrated wheels") | inside | heavy-duty factory work, 200 kg payload | |
| 279 | Sprout (Fauna Robotics, US) | in production, 107 cm, 22.7 kg | 1, 4 | legs ("basic walking") | both below | R4: "ready for developers and researchers"; homes, schools, public places | |
| 280 | Star1 (Robotera) | prototype, 171 cm, 63 kg | 3, 4 | legs (12 leg joints, runs 3.6 m/s) | inside | the catalogue's summary: "industrial and commercial" | |
| 281 | StarBot Astra (StarBot, US) | pre-order, 152 cm, 34 kg | 1 | legs ("walks on two legs") | height above | R4: universities, research institutes, R&D teams | height between types 1 and 2 |
| 282 | StarBot Flex (StarBot) | prototype, 175 cm, 50 kg | 4 | wheels | mass below | restaurants, hotels, retail | |
| 283 | StarBot Nova (StarBot) | prototype, 152 cm, 32 kg | 4 | wheels | both below | restaurants, hospitality, retail | |
| 284 | Steve (Sulu.be, BE) | in production, 210 cm, 140 kg | 4 | not stated | both above | a character at events: entertainment, hospitality | |
| 285 | Superman (Unitree) | prototype, 170 cm, 45 kg | 2 | legs; "no hands and no grippers" | mass below | research, technology demonstration (jumps, sprints) | form: no hands |
| 286 | Synthia (Syntheva Robotics, NO) | prototype, 165 cm, 30 kg | — | unclear: "start with just the head and add a torso, arms and legs later" | — | companionship, entertainment | form: left for the end |
| 287 | Syntro (WorkFar, US) | in production, 170 cm, 108 kg | 3 | not stated | inside | industrial automation, logistics, manufacturing | |
| 288 | T800 (EngineAI) | prototype, 173 cm, 60 kg | 5, 6 | no wheels named | mass below | R1: the workbook names the T800 Max in type 5 and the T800's security variants in type 6 | the catalogue's markets match AEON's; its nationality reads "US" |
| 289 | Taku (DYNA Robotics, US) | in production, 170 cm, not given | 4, 3 | wheels ("four steerable wheels") | not given | hotels, laundry, restaurants, commercial services; warehouses | |
| 290 | TALOS (PAL Robotics) | in production, 175 cm, 95 kg | 2 | legs ("full-size biped") | mass above | R4: research labs | |
| 291 | TARA GEN1 (iHub Robotics, IN) | in production, 163 cm, 75 kg | 4, 3 | not stated (3 joints) | inside | reception, patient support, airport assistance; industries, logistics | form: 3 joints only |
| 292 | TARS (TARS Robotics, CN) | prototype, 160–175 cm, 80 kg | 3 | not stated | inside | industrial automation, logistics, manufacturing | |
| 293 | Tau Humanoid (Tau Robotics, US) | in production, 132 cm, 35 kg | 4 | not stated | both below | home and office cleaning, teleoperated | |
| 294 | THEMIS V2 (Westwood Robotics, US) | in production, 160 cm, 32 kg | 2, 3 | legs ("walks and runs") | mass below | the catalogue's summary: "logistics, service, and research" | service also |
| 295 | TIAGo Pro (PAL Robotics) | in production, 155 cm, 80 kg | 2, 3 | wheels | height below | "the next generation of its popular TIAGo research robot"; industry, logistics | healthcare, agrifood also |
| 296 | Tian Yi 2.0 (X-Humanoid, CN) | in production, ~160–180 cm, not given | 3, 4 | not stated | not given | inspection in warehouses and industrial facilities; service | patrol among other uses |
| 297 | TianGong Ultra (X-Humanoid) | prototype, 180 cm, 55 kg | 2 | legs ("shock-absorbing legs") | inside | research, technology demonstration (half-marathon) | |
| 298 | Tianzhen Z1 (Tlibot, CN) | prototype, 167 cm, 45 kg | 4, 2 | not stated | mass below | commercial interaction, exhibition guidance; research | |
| 299 | Tien Kung 2.0 (X-Humanoid) | in production, 170 cm, ~70–90 kg | 2 | legs ("bipedal motion") | inside | R4: AI development, robotics research | |
| 300 | Tien Kung 3.0 (X-Humanoid) | prototype, 169 cm, 62 kg | 2 | legs ("walk up stairs") | inside | R4: industrial R&D, research, robotics labs | |

**Batch 6** (counted from the table): 47 robots with a type, 18 of them with two; in each type, a robot with two types
counted in both: type 1: 5; type 2: 17; type 3: 22; type 4: 19; type 5: 1; type 6: 1. Unclear, left for the end: 2
(Reachy 2, Synthia); not assigned: 1 (Robotera M7, an upper body). To check in batch 7: UBTECH's "Walker Tienkung"
against X-Humanoid's Tien Kung robots (299, 300), possibly one robot under two names.

### E4.8 Batch 7 of 7: robots 301 to 349 (2026-10-28). Not entered

Read as batch 6. **What was read:** every robot's humanoid.guide page, its whole text searched for wheels, legs and
walking.

| # | Robot (maker) | Catalogue: status, height, mass | Types | Form | Size | Reason | For Matthias |
|---|---|---|---|---|---|---|---|
| 301 | TITAN (RoboForce, US) | prototype, 210 cm, not given | 3, 5 | wheels ("a rugged, modular base with a humanoid upper body") | height above | "dull, dirty and dangerous jobs in harsh industrial environments": solar, mining, manufacturing, logistics, space | |
| 302 | TLIBOT T1 (Tlibot, CN) | in production, 160 cm, 43 kg | 2 | legs ("walks on two legs") | mass below | R4: "general-purpose humanoid applications", R&D | |
| 303 | TM Xplore 1 (Techman Robot, TW) | prototype, 160–175 cm, not given | 3 | wheels | inside | electronics and semiconductor factories, logistics, warehouses | |
| 304 | Tobi (TwoLabs, US) | prototype, 150 cm, 60 kg | 4 | "semi-humanoid", a base not stated | height below | elder care in nursing homes: feeding, mobility support, companionship | |
| 305 | Tora DoubleOne (PaXini, CN) | in production, 168 cm, 70 kg | 3, 4 | wheels | inside | factories, warehouses; public spaces, service | |
| 306 | ToraOne (PaXini) | prototype, 186 cm, not given | 3, 4 | not stated | height above | "industries, healthcare, and service sectors" | the catalogue names "Tokyo Robotics" as maker, its text PaXini |
| 307 | Torobo (Tokyo Robotics, JP) | prototype, 166 cm, 160 kg | 3, 2 | not stated | mass above | the catalogue's summary: "industrial, academic, and research" | |
| 308 | Totan O1 (WL Robotics, CN) | limited production, 134 cm, 34 kg | 1 | not stated | inside | R4: AI research teams, universities, labs (its text: "Titan O1") | |
| 309 | TRON 2 (LimX Dynamics) | in production, 132 cm, 35 kg | 1 | changes between two arms, two legs, two legs on wheels | inside | R4: embodied AI research, data collection, education, industrial prototyping | one of its forms is two arms only |
| 310 | U1 Pro (UBTECH) | pre-order, 183 cm, 42 kg | 4 | not stated | height above, mass below | "a social companion rather than a labor robot" (the catalogue's markets are Martian's) | |
| 311 | Unitree R1 (Unitree) | in production, 122 cm, 25 kg | 1 | legs (runs, cartwheels) | mass below | R4: hobbyists, developers, research labs | |
| 312 | VB1-I (Lanxin Robotics, CN) | in production, ~165 cm, ~60–70 kg | 2, 3 | legs ("walks on two legs") | inside | embodied AI, research; industrial trials | maybe the same robot as 315 |
| 313 | VB2 (Lanxin Robotics) | in production, ~170 cm, ~65–75 kg | 2, 3 | legs ("walks on two legs") | inside | embodied AI, industrial research; logistics | |
| 314 | Vega (Dexmate, US) | in production, 171 cm, 135 kg | 3, 2 | wheels ("an omni-directional mobile base") | mass above | industrial automation; R&D labs | |
| 315 | VersaBot VB-1 (Lanxin Robotics) | limited production, 165 cm, 75 kg | 2 | not stated | inside | R4: applied humanoid R&D, research and education | maybe the same robot as 312 |
| 316 | Vesoma 1 (Vesoma, DE) | prototype, 170 cm, 75 kg | 3, 4 | not stated | inside | "factories, warehouses, and care work" | |
| 317 | Voxel (Tuesday Labs, US) | prototype, 150 cm, 45 kg | 4 | legs ("Z-shaped legs") | mass below | home: tidying, fetching, watering plants | |
| 318 | W-Bot (Yue Quan Bionics, CN) | in production, 178 cm, 60 kg | 2 | wheels (folding legs on a wheeled base) | inside | "manipulation in tight spaces"; no use beyond it (R5) | no stated use |
| 319 | W1 Pro (DexForce, CN) | production, 163 cm, 110 kg | 3, 4 | wheels | mass above | industrial automation, logistics, inspection; service | |
| 320 | Walden (Walden Robotics, US) | early production, 165 cm, 90 kg | 3 | wheels | inside | factories and warehouses | |
| 321 | Walker C (UBTECH) | prototype, 163 cm, 43 kg | 4, 3 | not stated | mass below | its text: guiding and reception; the catalogue's markets: industries, logistics, manufacturing | the markets contradict the text |
| 322 | Walker C1 (UBTECH) | prototype, 165 cm, 50 kg | 4 | not stated | mass below | commercial service, exhibitions, hospitality | |
| 323 | Walker II (DroidUp, CN) | in production, 170 cm, 32 kg | 4, 2 | legs ("biped") | mass below | guided tours, stage and events; education and research | security patrol among other uses |
| 324 | Walker S1 (UBTECH) | prototype, 172 cm, 76 kg | 4 | not stated | mass above | its text: "home and office environments" | UBTECH's Walker S line is its factory line (the S2 is type 3's anchor) |
| 325 | Walker S2 (UBTECH) | prototype, 176 cm, "43, 73" kg | 3 | legs ("bipedal locomotion") | inside | R1: type 3's anchor | |
| 326 | Walker Tienkung (UBTECH) | in production, 170 cm, 55 kg | 2 | legs (runs, climbs stairs) | inside | R4: universities, research institutes, developers; built with the Beijing Humanoid Robot Innovation Center | maybe the same robot as 299, Tien Kung 2.0 (X-Humanoid is that centre) |
| 327 | Wanda 2.0 (Unix Group) | in production, 142–168 cm, not given | 3 | legs ("It walks") | not given | industrial automation, logistics, manufacturing | |
| 328 | X-Bot (Yue Quan Bionics) | in production, 167 cm, 60 kg | 4, 3 | legs ("walks on two legs") | inside | delivery, guided tours, medical assistance, reception; industrial support | |
| 329 | Xialan S0 (Digit Robotics) | prototype, 169 cm, not given | 2 | not stated | inside | R4: academic institutions, embodied AI, robotics research | |
| 330 | Xiao Di (BYD, CN) | prototype, 161 cm, 58.5 kg | 4, 3 | legs ("walks") | inside | car dealership service, education; industrial uses | |
| 331 | Xiao Liu (Tencent Robotics X, CN) | prototype, 165 cm, 70 kg | 4 | wheels | inside | eldercare, home assistance | |
| 332 | Xiao Tuo (TOPSTAR, CN) | prototype, 120 cm, 40 kg | 1, 3 | not stated | inside | R4: research and education; "light industrial tasks" | |
| 333 | XiaQi (Digit Robotics) | production platform, 169 cm, 69 kg | 4 | not stated | inside | exhibition guidance, reception, marketing | |
| 334 | XTRON KUAVO-MY (Leju Robotics) | prototype, 166 cm, 55 kg | 4, 3 | legs (7 joints a leg, jumps) | inside | R1: the workbook's KUAVO-MY is type 4; "research and industrial use" | which entry is the workbook's (1.73 m, 63.5 kg): 164 or 334? |
| 335 | Y1 (Tlibot) | in production, 195 cm, 150 kg | 3, 2 | wheels | both above | handling, warehousing; research | service also |
| 336 | Y2-B (Tlibot) | in production, 160 cm, 85 kg | 2, 4 | wheels | mass above | research; service, light handling | |
| 337 | Y2-P (Tlibot) | in production, 156.5 cm, 95 kg | 3, 2 | wheels | height below | handling, warehousing; research | service also |
| 338 | Y4 (Tlibot) | in production, 144.5 cm, 95 kg | — | stationary ("a fixed-station, dual-arm robot", "does not drive around") | — | not assigned (decided 2026-10-28) | |
| 339 | YMBot C (Yunmu, CN) | prototype, 174 cm, 75 kg | 4 | legs ("walks on two legs") | inside | cultural tourism, exhibitions, museums | |
| 340 | YMBot D (Yunmu) | in production, 165 cm, 100 kg | 3, 2 | wheels | mass above | "industrial wheeled humanoid"; data collection | home and security also; maybe the same robot as 342 |
| 341 | YMBot D2 (Yunmu) | prototype, 180 cm, 150 kg | 3, 2 | wheels | both above | heavy industry, precision assembly; data collection | |
| 342 | YMBot D4 (Yunmu) | prototype, 165 cm, 100 kg | 3, 2 | wheels | mass above | industrial operations, logistics; data collection | security and service also; maybe the same robot as 340 |
| 343 | YMBOT E3 (Yunmu) | prototype, 140 cm, 35 kg | 1 | legs ("bipedal") | inside | R4: universities, research, robotics education (the catalogue's summary line describes YMBot C) | |
| 344 | YMBot H (Yunmu) | prototype, 170 cm, 75 kg | 4 | wheels | mass above | visitor reception in museums, showrooms, malls | |
| 345 | Yogi (Cartwheel Robotics, US) | prototype, 150 cm, 47 kg | 4 | legs ("walks with steady coordination") | mass below | workplace assistance, light logistics, education | |
| 346 | Zerith H1 (Zerith Robotics, CN) | in production, ~180 cm, 55 kg | 4, 3 | wheels | height above, mass below | its text: cleaning and restocking in hotels; the markets: industrial automation, logistics, inspection, service | the markets are W1 Pro's, word for word |
| 347 | Zerith Z1 (Zerith Robotics) | in production, 145 cm, 33 kg | 4, 3 | legs ("stands upright on two legs") | both below | its text: lobbies and corridors; the same markets as 346 | as 346 |
| 348 | Zeus 1 (PL-Universe, CN) | production-ready, 160–175 cm, ~300 kg | 3 | not stated | mass far above | heavy-duty factory work | |
| 349 | ψ-SynRobot (PsiBot, CN) | prototype, 145 cm, 65 kg | 3, 2 | wheels | height below | light industrial tasks, logistics automation; research and education | |

**Batch 7:** 48 robots with a type, 24 of them with two; not assigned: 1 (Y4, a fixed station).

### E4.9 The register after all seven batches (2026-10-28). Not entered

**Counted** (VERIFICATION.md V60): 349 catalogue entries; 10 listed twice and counted once; 10 not assigned (an upper
body or arms only); 11 unclear, left for the end; **318 robots with a type, 136 of them with two.** In each type, a
robot with two types counted in both: type 1: 32; type 2: 95; type 3: 178; type 4: 134; type 5: 11; type 6: 4. By the
first type only: 27, 68, 125, 89, 6, 3.

**Left for the end, as decided** ("We can refine the unclear once, after going through all the batches"):
- *form unclear, an upper body only?* Ambidex, Astra, Bimanual, HELIOS (four arms, for space stations), Hobbs, MICO,
  pib.Pro, PR-34D, QDH, Reachy 2, Synthia (sold from a head upward);
- *maybe one robot under two entries:* VB1-I and VersaBot VB-1 (Lanxin); Walker Tienkung (UBTECH) and Tien Kung 2.0
  (X-Humanoid, the centre UBTECH built it with); YMBot D and D4 (Yunmu);
- *which entry is the workbook's KUAVO-MY* (1.73 m, 63.5 kg): Kuavo-my (145 cm) or XTRON KUAVO-MY (166 cm);
- *robots the workbook names that the catalogue lacks:* Fourier N1 (type 1), Norinco Fuxi (type 6), Unitree H1 (type
  2 excluded, type 5 borderline), UBTECH Walker S (the S1's forerunner);
- *the catalogue's text against its own markets:* Walker C, Walker S1, Zerith H1 and Z1 (markets copied from another
  entry), T800 (markets as AEON's), U1 Pro (markets as Martian's);
- *the points marked "For Matthias"* in E4.6 to E4.8 (second types where research and service tie; MH3, ALPHA,
  Fengxing-001; Superman without hands; Neo1 at 4 m and 1.2 t).

**Still open, for later:** how a robot with two types counts in the statistics (in full in both, split, or one of its
two drawn in each Monte Carlo draw); type 6's definition widened to civilian security (the workbook is Matthias's); the
register file itself (`data/researched/humanoid_register.xlsx`, proposed, not built) and 01's check 20 turned from a
fault into a flag.

### E4.10 The refinement pass: the unclear forms and the pairs, from the makers (2026-10-28). Decided, not entered

**Decided, 2026-10-28:** "Proposals hold", on the proposals below. Still open, asked and not answered: whether HELIOS
in space is also type 5; whether PR-OMNI is added; whether Walker Tienkung and Tien Kung 2.0 are one robot (kept as two
until a source says so).

Matthias: "Start refinement" ("read the makers' pages for the 11 unclear forms and the 3 maybe-identical pairs, and
propose each"). Read first-hand in the browser unless marked *second-hand* (a search summary or another site).

**The eleven unclear forms:**

| Robot | What the maker says | Proposal |
|---|---|---|
| Ambidex (NAVER LABS) | "양팔 로봇" (a two-arm robot), "양팔 로봇 플랫폼 연구" (research on a two-arm robot platform); no base named (https://www.naverlabs.com/ambidex) | not assigned: arms only |
| Astra (Apptronik) | "one of Apptronik's most important upper-body humanoid platforms" (https://apptronik.com/company/our-work, read through WebFetch); apptronik.com/astra answers "Page Not Found" | not assigned: an upper body |
| QDH (Apptronik) | "As an upper-body platform, QDH helped explore ..."; its "ability to be paired with different mobility bases" (same page). A search summary that QDH added legs is second-hand and contradicts the maker | not assigned: an upper body |
| MICO (Flexiv) | "humanoid-style, modular, dual-arm robotic system", two Enlight arms under one control box; no base named (Flexiv's Automate 2026 news page, through WebFetch); the catalogue: "does not walk or run" | not assigned: two arms (Flexiv's mobile one is AICO 2, type 3) |
| Bimanual (Svaya Robotics) | "Bimanual Humanoid Robot", "17 actuators", "arms with 7 degrees of freedom each"; no legs and no base named (https://svayarobotics.com/product/#bimanual) | not assigned: two arms and a torso |
| PR-34D (Perceptyne) | not on the maker's site; its dual-arm robots there are PR-OMNI ("Mobility: Holonomic drive, Vertical Gantry") and PR-DUO (a work station, "at the same work-station"; 120 kg, 5'2") (https://www.perceptyne.com/, /product/duo) | not assigned as PR-34D (not found); PR-OMNI, wheeled, is missing from the catalogue: add as type 3? |
| pib.Pro (isento) | the maker's page names no body (https://pib.rocks); its forerunner pib is described as a 3D-printed robot with a face, moving arms and a torso (*second-hand*, 3printr, Onshape) | not assigned, weakly: an upper body by its forerunner |
| Hobbs (Noetix) | the maker's page did not load; the catalogue: "smooth upper-body motion", "a mobile upper body", works "at table height"; reports of the Hobbs W1 speak of a separate upper-body "dual arms" module (*second-hand*) | not assigned, weakly: an upper body |
| HELIOS (ORBIT Robotics) | "In microgravity, legs serve little purpose ... HELIOS uses four arms to navigate station interiors, hold position, and handle tasks"; first work "cargo + inventory workflows", then "full orbital operations support" (https://www.orbitrobotics.ch/) | type 3 (cargo, inventory, maintenance); it moves by its arms, so it is more than an upper body. For Matthias: no legs; space, type 5? |
| Reachy 2 (Pollen Robotics) | "The ideal bimanual mobile manipulator for AI & robotics labs"; "available on an omnidirectional mobile base", "Three omniwheels"; 136–166 cm, "Up to 50 kg" (https://pollen-robotics.com/reachy-2/) | type 2, wheels; without the optional base an upper body |
| Synthia (Syntheva Robotics) | "lifelike, bipedal companions starting at just $6,490" (https://robotics.syntheva.no/) | type 4, legs; also sold from a head upward |

**The three pairs:**
- *VB1-I and VersaBot VB-1 (Lanxin):* two robots. The VB-1 is "a wheeled humanoid with a human-like upper body and no
  legs", the VB1-I "a full-scale bipedal humanoid" (*second-hand*: aiwiki.ai, humanoid.guide; Lanxin's own pages not
  found). Both stay; the VB-1's form becomes wheels.
- *Walker Tienkung (UBTECH) and Tien Kung 2.0 (X-Humanoid):* not shown to be one robot. UBTECH and the Beijing Humanoid
  Robot Innovation Center launched the "Tiangong Walker" research robot together, RMB 299,000 (*second-hand*: TechNode
  2025-03-13, heise); X-Humanoid's page gives no details of a 2.0 (https://www.x-humanoid.com/detail/jstg.html). Same
  centre, same height (170 cm), both research; the masses differ (55 kg against the catalogue's estimate of ~70–90
  kg). Proposed: both stay until a source says they are the same; Matthias decides.
- *YMBot D and D4 (Yunmu):* two products, on two product pages of the maker (*second-hand*: a search summary; the
  pages, ymbot.com/detail/4 and /detail/7, open only after a login, not attempted). Both stay.

**The register after these proposals** (recounted in Claude's scratch folder, as V60): 321 robots with a type, 136 of
them with two; 18 not assigned (an upper body or arms only); none unclear. In each type, a robot with two types counted
in both: type 1: 32; type 2: 96; type 3: 179; type 4: 135; type 5: 11; type 6: 4. Not yet counted: the four robots
the workbook names that the catalogue lacks (Fourier N1, Norinco Fuxi, Unitree H1, UBTECH Walker S), and PR-OMNI if
it is added.

### E4.11 Five robots the catalogue lacks, added (2026-10-28). Decided, not entered

**Decided, 2026-10-28:** "They hold", on the five proposals below.

**Decided, 2026-10-28** (type 1's lower limit): "All larger than 15 kg", then "Below 15 kg not part of the type 1". So
the FF Nova (2.8 kg) leaves type 1 (it keeps type 1 in the register only if Matthias says so; proposed: not assigned).
The PrimeBOT Q1 (88 cm) has no stated mass: an estimate is needed to say which side of 15 kg it lies.

Matthias: "Yes, add them" ("add Fourier N1, Norinco Fuxi, Unitree H1, UBTECH Walker S and Perceptyne PR-OMNI, each
read from its maker or source, with a proposed type"). Numbered on from the catalogue's 349. Read first-hand in the
browser unless marked.

| # | Robot (maker) | What the maker or source says | The workbook | Types | Form | Reason | For Matthias |
|---|---|---|---|---|---|---|---|
| 350 | N1 (Fourier, CN) | "1.3 m", "38 kg", 23 joints, open source (https://support-old.fftai.com/en/docs/GR-X-Humanoid-Robot/Fouriern1/N1_Introduction/, through a search summary; its model file read for type 1, E2.8e) | qualifying in type 1 (1.25 m, 32 kg, 28 DoF, [S14]) | 1 | legs | R1, and R4: an open-source developer robot | |
| 351 | Fuxi (NORINCO, CN) | "special-purpose humanoid robot, which can conduct reconnaissance, patrolling and operations in hazardous areas", "sentry duties", teleoperated by "external avatar", "around 90 kilograms" (DefenseMirror, 2026-08-19, the workbook's [S33]: https://defensemirror.com/news/41857/China___s_NORINCO_Unveils____Fuxi____Humanoid_Battlefield_Robot) | provisionally qualifying in type 6 (1.80 m, 90 kg) | 6 | not stated ("full-size humanoid") | R1; defence and security alone | |
| 352 | H1 (Unitree, CN) | "Full-size universal humanoid robot", "Height about 180CM", "Weight about 47kg", "Moving speed of 3.3m/s"; "the first full-size general-purpose humanoid robot that can run in China" (https://www.unitree.com/h1) | excluded from type 2; borderline in type 5 ("specs not supplied") | 2, 5 | legs | its maker: general purpose (type 2); the workbook's type 5, its speed above type 5's ">2.5 m/s" | the workbook excluded it from type 2, by its 47 kg; type limits no longer exclude (decided 2026-10-28) |
| 353 | Walker S (UBTECH, CN) | "our new industrial humanoid robot", "synchronized operations on the factory assembly line", "a height of 1.7 meters", "41 servo joints", "walk stably on mobile production lines" (https://www.ubtrobot.com/en/humanoid/products/walker-s) | only in a source's title ([S51], "UBTECH Walker S / S2") | 3 | legs | factory assembly lines | the maker also lists a "Walker S Lite", not in the catalogue |
| 354 | PR-OMNI (Perceptyne, IN) | "The future of Industrial Robotics", "5'2"", "120 kg", "4 Wheel holonomic drive", "Dual arms, 7 DOF each", head 2 DOF (https://www.perceptyne.com/product/omni) | not named | 3 | wheels | industrial work | |

**The register with these five** (recounted in Claude's scratch folder, VERIFICATION.md V60): 326 robots with a type,
137 of them with two; 18 not assigned. In each type, a robot with two types counted in both: type 1: 33; type 2: 97;
type 3: 181; type 4: 135; type 5: 12; type 6: 5.

## E3. Robot type 2 taken apart: the robots and their sources, 2026-10-28. Nothing entered

Matthias: "Yes, start robot type 2: find the robots inside its limits and their sources, and show me the sources table
before anything is entered." **The workbook's type 2** (sheet Taxonomy, row 3): "Full-Scale General-Purpose / AI
Research", "Height: 1.60–1.85 m (indicative 1.75–1.80 m)", "Mass: 50–80 kg" (not marked "defining", as type 1's
are), anchor the Unitree H2 (1.82 m, 70.0 kg, 31 chassis DoF); "Qualifying: Unitree H2/H2 Plus, Tesla Optimus Gen 3,
Figure 03. Borderline (industrial overlap): Apptronik Apollo 2. Excluded: Unitree H1, BD Atlas." Its parts list
(rows 24 to 37) is labelled Estimate throughout.

**The robots, and what each has** (read myself, 2026-10-28, unless said):

| Robot | The maker's height and mass | Model file (the maker's) | Parts-level source | In the workbook |
|---|---|---|---|---|
| Unitree H2 | "1820 x 456 x 218mm", "About 70kg" with battery; 31 joints; legs "360N·m", arms "120N.m"; "15Ah(0.972KWh)", "Maximum Voltage: 75.6 V"; "Local air cooling"; "Aircraft-Grade Aluminum + Titanium Alloy + High-Strength Engineering Plastics"; Intel Core i5 and i7; binocular camera, microphone array, speaker (https://www.unitree.com/h2) | `H2.urdf` (https://github.com/unitreerobotics/unitree_ros, robots/h2_description): 31 joints, links 75.59 kg; hips and knees 360 N·m, ankles 19 and 66.88, waist 120 / 180 / 180, head 50, shoulders 130 / 60 / 60, elbow 60, wrist 60 / 10 / 10 N·m | none found (no teardown, no BOM; Chinese press only) | anchor, qualifying |
| Unitree H2 Plus | as the H2, with dexterous hands | `H2_Plus.urdf`: 75 joints, links 77.24 kg | none | qualifying |
| Unitree H1-2 | "Height about 178CM", "About 70kg"; 27 joints; knee "About 360N.m", hip and waist "About 220N.m"; "15Ah(0.864KWh)" (https://www.unitree.com/h1) | `h1_2.urdf`: links 67.37 kg | none | not named (the H1, 47 kg, excluded) |
| Fourier GR-2 | "1750 mm × 552 mm × 275 mm", "≈63 kg", "铝合金+工程塑料"; 29 body joints (legs 6 + 6, waist 1, head 2, arms 7 + 7) and hands of 6 joints each (12 optional); torque limits hip pitch and knee 366.05, hip roll 95.47, hip yaw and ankle pitch 54.33, ankle roll 29.84, waist and shoulder pitch and roll 74.45, shoulder yaw and elbow 42.75, wrists and head 17.33 N·m, peak "436 N·m"; battery "≈950 Wh", "≤9 kg", 39.6 V; Intel Core i7 (14 cores) and an 8-core ARM perception board; binocular camera, 6-axis IMU, microphone, speaker; dual encoders (https://support-old.fftai.com/docs/GR-X-Humanoid-Robot/GR2/GR-2_Introduction/) | `GR2T2V2.urdf` (https://github.com/FFTAI/fourier_lab, models/gr2t2v2): links 62.73 kg; the same torque limits | none | not named |
| Fourier GR-1 | "1650X524X325mm", "≈52kg", "铝合金+工程塑料"; "总执行器数量 44/34", 32 FSA, "最大关节扭矩 230N.m"; i7-13700H; RealSense depth camera, IMU; battery "483Wh", 40 V; in the torso a power management module, a switch board, the motion controller (https://support-old.fftai.com/docs/GR-X-Humanoid-Robot/GR1/GR-1_Introduction/) | `GR1T2.urdf` (fourier_lab, models/gr1t2): links 54.53 kg; only the legs' 12 joints actuated in the file | none | not named |
| Figure 03 | "5'8"" (1.73 m), "61KG", payload "20KG" (https://www.figure.ai/figure) | none | none | qualifying |
| Tesla Optimus Gen 3 | no maker's page found; the workbook 1.73 m, 57 kg [S18, S48]; AI Day 2022 (second-hand): 73 kg, actuators 20 / 110 / 180 N·m rotary and 500 / 3,900 / 8,000 N linear, no masses | none | none (broker BOMs of cost, not mass) | qualifying |
| Apptronik Apollo 2 | the maker's page answered 404; the workbook 1.73 m, 73 kg | none | none | borderline |

**Searched, not found:** a teardown or a parts list of any type-2 robot (English and Chinese); per-actuator masses of
Optimus. The G1's weighed joint (type 1) is the only joint taken apart part by part.

**What this means, for Matthias to decide:**
1. *Which robots are type 2.* The workbook names the H2 (and H2 Plus), Optimus Gen 3 and Figure 03, Apollo 2
   borderline. Inside its limits too, not named there: the H1-2, the GR-2 and the GR-1, each with the maker's model
   file. The AgiBot A2 (type 4's anchor) may lie inside type 2's limits as well: the types overlap in size, and the
   workbook separates them by use.
2. *Which robots can be taken apart.* With a maker's model file (joints, torques, link masses), as the N1 was: the H2,
   H2 Plus, H1-2, GR-2, GR-1. With specifications only, no joints and no parts: Optimus, Figure 03, Apollo 2.
3. *The joints' masses.* The fit on AgiBot's actuators (E2.8e) reaches 200 N·m; type 2's hips and knees are 360 N·m,
   beyond it.

**Decided, 2026-10-28** (point 1 and 2): "Those with model files": type 2 is informed by the Unitree H2, H2 Plus,
H1-2 and the Fourier GR-2 and GR-1; Optimus Gen 3, Figure 03 and Apollo 2 stay out, having specifications only (no
joints, no parts), and this is said wherever type 2's results are shown.

### What was asked

Matthias, 2026-10-27: "where the hell the materilas are in the robot", "It is kind of parts. SO one disassble the
robost accordingly the material composition of the sensor and PCB are also messing", "What is the lenght of the
cables etc.", "Not only this also about the different parts and motors and there strength and tpes and gear
boxes!!", "Everything, which makes up the robot", "Start with the first one", and, on the sold Nikkei BP report, "I
do not have the possiblity to buy it. Find other sources." Robot type 1 is Compact Research & Developer; its anchor
robot in the workbook is the Unitree G1 (35 kg). This section is research only: nothing is entered or coded before
Matthias has seen it.

### E2.1 The sources

| # | Source | What it is | Same kind / representative | Read myself |
|---|---|---|---|---|
| U1 | Unitree, G1 product page. https://www.unitree.com/g1/ | Manufacturer's specification (design values, claims) | The anchor robot itself | Yes |
| U2 | Unitree, G1 developer documentation, "About G1". https://support.unitree.com/home/en/G1_developer/about_G1 | Manufacturer's documentation for developers | The anchor robot itself | Yes |
| U3 | Unitree, `g1_29dof.urdf` (the robot's model file: every joint's torque limit, every link's mass). https://raw.githubusercontent.com/unitreerobotics/unitree_ros/master/robots/g1_description/g1_29dof.urdf | Manufacturer's model file; masses and limits as designed, not measured | The anchor robot, 29-joint EDU version | Yes |
| U4 | Unitree, G1 brochure (Chinese), 2025. https://www.worldrobotconference.com/profile/robot/download/2025/07/08/杭州宇树-G1宣传册_20250708194541A200.pdf | Manufacturer's brochure | The anchor robot | Yes; nothing beyond U1 |
| L1 | Livox, Mid-360 specifications. https://www.livoxtech.com/mid-360/specs | Manufacturer's datasheet | The LiDAR in the G1's head (U2) | Yes |
| **T1** | **China Post Securities (Su Qianye, Sheng Wei, Yang Shuaibo), 《宇树G1人形机器人拆解报告》, 2026-03-30, 59 slides. https://pdf.dfcfw.com/pdf/H3_AP202603311820899944_1.pdf** | **A securities firm's own teardown of a basic G1 (23 joints): parts photographed and weighed; costs are its estimates** | **The anchor robot** | **Yes, the report itself** (East Money's report server) |
| T2 | SemiAnalysis, "China's Unitree Will Dominate Global Robotics", 2026-06-09. https://newsletter.semianalysis.com/p/chinas-unitree-will-dominate-global | An industry analyst's design examination and supplier quotes | The anchor robot, EDU version (29 joints) | Free part only; the hardware detail is behind the paywall |
| T3 | Munro & Associates, *Munro Live*, Unitree G1 teardown video, June 2026. https://www.youtube.com/watch?v=OXuqGuTgXGU | An engineering consultancy's teardown | The anchor robot | **No, second-hand** through Humanoid.guide: https://humanoid.guide/unitree-g1-teardown-reveals-actuator-and-cooling-tradeoffs/ |
| T3k | Munro's knee-actuator report (by "Grant"), in Chinese on Zhihu: https://zhuanlan.zhihu.com/p/2086097814052984275 | An engineering consultancy's measured teardown of one knee joint | The anchor robot's knee | **No, second-hand**: Zhihu asks for a login; read through the summary in SMZDM: https://post.smzdm.com/p/awwo7o5g/ |
| T4 | Nikkei BP, 『人型ロボット「Unitree G1」徹底分解・分析レポート』, 2026-07-31, 254 pages. https://info.nikkeibp.co.jp/nxt/campaign/b/291730/ | A technical publisher's full teardown, sold at 660,000 yen | The anchor robot | **No**: Matthias cannot buy it |
| T5 | EEWorld, summary of T1 to T4. https://en.eeworld.com.cn/news/robot/eic733333.html and https://en.eeworld.com.cn/news/robot/eic733333_2.html | Trade-press summary by a platform user; second-hand | The anchor robot | Yes; replaced by T1 wherever T1 says the same |
| C1 | "Lenz's law", 宇树G1拆解分析 - 主控部分 (main control board), 2025-10-23. https://jishuzhan.net/article/1981300479431868417 (copy of a CSDN blog) | A private person's teardown of the main control board | The anchor robot | Yes |
| J1 | JONVER (Jiangyin; makes harnesses, busbars, connectors), G1 teardown article, 2026-04-15. https://www.jonver.cn/newsdetail_195 | A harness supplier's summary; it repeats T1 | The anchor robot | Yes; adds nothing to T1 |
| B1 | Maverick Drone (a dealer), G1 battery. https://www.maverickdrone.com/collections/all/products/g1-battery | Dealer's product page | The anchor robot's battery | Yes |
| G1 | Simplexity, "Unitree Go2 Motor Teardown". https://www.simplexitypd.com/blog/unitree-go2-motor-teardown/ | An engineering consultancy's teardown | **Not the same kind**: the motor of Unitree's four-legged Go2 | Yes |
| V1 | YC Insulation (sells insulation sleeving), "Robot Wire Harness Protection". https://ycsleeve.com/news-en/news-robot-wire-harness-en-2026-05-06.html | Vendor marketing, citing "GGII Robotics data" without a reference | **Not representative**: no robot named | Yes |
| A1 | Cui, Park, Park (Hanyang University), *Sensors* 23 (2023) 2627. https://doi.org/10.3390/s23052627 | A university model of in-robot networks | **Not representative**: no real robot | Yes |

**Left out:** G1, V1 and A1 do not describe the G1. LTEC's G1 teardown (https://www.ltec-biz.com/25l-0907-1/) is sold
at 980,000 yen or more and was not used.

### E2.2 The joints

The basic G1 has 23 joints, each one module of motor, two-stage planetary gearbox, two encoders and a driver board,
with the cables running through its hollow centre (T1, slides 3 and 20; U1, U2).

| Joint | Number (basic version) | Torque limit (U3) | Module (T1, slides 11, 18, 43) |
|---|---|---|---|
| Hip pitch, roll, yaw | 6 | 88 N·m | large: about 80 mm across, 1,100 g |
| Knee | 2 | 139 N·m (U3); 90 N·m basic, 120 N·m EDU (U1, U2, T1) | large |
| Waist yaw | 1 | 88 N·m | large |
| Ankle pitch, roll (in the lower leg, driving the ankle through rods) | 4 | 35 N·m | small: about 60 mm across, 70 mm high, 525 g |
| Shoulder pitch, roll, yaw; elbow; wrist roll | 10 | 25 N·m | small |
| *EDU only:* waist roll, pitch | 2 | 35 N·m | — |
| *EDU only:* wrist pitch, yaw | 4 | 5 N·m | — |

9 large × 1,100 g + 14 small × 525 g = 17,250 g, 49 % of the robot (T1, slide 43). The workbook (rows 8 to 11) has
17.6 kg at the mode.

**One small joint, weighed part by part** (T1, slide 43, figure 37: a lower-leg joint of the basic G1):

| Part | g | Material, as T1 gives it |
|---|---|---|
| Motor stator | 94.3 | "铜线+包胶", copper wire and its coating |
| Motor rotor | 42.9 | "磁钢", permanent magnet |
| Magnet carrier (rotor hub) | 16.9 | aluminium, and a plastic bearing |
| Stage 1 sun gear | 8.0 | steel |
| Stage 1 planets, carrier and stage 2 sun gear | 25.3 | steel |
| Stage 1 ring gear | 24.1 | steel |
| Stage 2 planets, carrier and crossed roller bearing | 74.0 | carrier aluminium, the rest steel |
| Stage 2 ring gear | 23.8 | steel |
| Driver board | 12.8 | PCB |
| Two small bearings | 11.0 | steel |
| Housing | 79.3 | aluminium |
| Two end caps | 23.7 | aluminium |
| Output flange | 50.8 | steel |
| Other | 38.1 | not given |
| **Total** | **525** | |

- **Checked:** the parts add up to 525.0 g; motor 94.3 + 42.9 = 137.2 g and gearbox 8 + 25.3 + 24.1 + 74 + 23.8 =
  155.2 g, as T1's text says.
- **Questioned:** a stator is copper wound on an electrical-steel core, but T1 names only the copper and its coating.
  The steel core's share of the 94.3 g is not given. The rotor's 42.9 g is called "magnet"; whether it holds a steel
  back ring is not given. "Other" (38.1 g) is not explained.
- **Motor:** low-inertia, high-speed, internal-rotor permanent-magnet synchronous motor, "定子绕组 + 永磁磁钢 +
  一体化转子轮毂", up to 3,000 to 5,000 rpm (T1, slides 19, 21). The magnet grade is not given.
- **Gearbox:** two planetary stages; stage 1 sun 18, planets 14, ring 60; stage 2 sun 16, planets 20, ring 60; "总减速比
  ~20.58" (T1, slide 22). The ratio follows from the teeth ((1 + 60/18)(1 + 60/16) = 20.58), but the planets do not fit
  the rings (18 + 2 × 14 = 46 and 16 + 2 × 20 = 56, not 60), so the tooth counts are doubtful.
- **Bearing:** Luoyang Baina crossed roller bearing CRBT355A 10E4J3, 35 mm bore, the only part with a maker's logo
  (T1, slide 23). Gear wheels from Meihu (美湖股份), by Meihu's own statement (T1, slide 15).
- **Driver board:** round, Unitree's own, field-oriented control, every chip's marking removed (T1, slide 24); 12.8 g
  in the small joint. Its size is not given.

**The knee joint** (T3k, second-hand): 80 mm across, 64 mm thick, "含线缆 1085.1 克" (1,085.1 g with its cables); an
18-slot, 16-pole permanent-magnet motor; two planetary stages, stage 1 sun 16, four planets 20, ring 56; stage 2 sun
12, four planets 18, ring 48; 22.5:1. These teeth fit (16 + 2 × 20 = 56; 12 + 2 × 18 = 48) and give 4.5 × 5 = 22.5.
An IKO crossed roller bearing; encoders on the rotor and on the output; a stack of driver boards; die-cast aluminium
back cover; the cables run through a hollow aluminium tube with a PTFE liner. Unknown to Munro: the magnet grade, the
chips. T3 gives "about 15:1" for the G1's joints.

### E2.3 The electronics

**Boards (PCBs)**

| Board | Number | What the sources give |
|---|---|---|
| Joint driver board | 1 per joint, 23; the knee holds "a stack" (T3k) | Round; 12.8 g in a small joint (T1) |
| Main control board, in the back | 1 | Rockchip RK3588S, two BIWIN BMW2CX32H2A-32G-X memory chips (8 GB together), one FORESEE FEMDNN064G-58AAA 64 GB storage chip; the other chips' markings removed; aluminium heat sink and fan (T1, slides 26, 27, 39). C1: a core board on a base board |
| Development computer, NVIDIA Jetson Orin NX on Unitree's own base board, with an NVMe SSD | 1 (EDU only) | U2, T1 (slide 28), C1; module 69.6 × 45 mm (retailer pages) |
| Head control board with its own MCU | 1 | T1, slide 37 |
| Power distribution unit (PDU) and DC-DC converter | 1 each | T1's cost table (slide 12); no size |
| Capacitor buffers at the end joints of the arms and legs | several | T1, slide 38 |
| Battery management board, with NTC temperature sensors | 1 | T1, slide 42 |
| The boards inside the LiDAR, camera and microphone array | — | Not given |

**No source gives a board area.** The only board mass is the small joint's driver board, 12.8 g.

**Sensors**

| Sensor | Number | What the sources give |
|---|---|---|
| Livox Mid-360 LiDAR, head | 1 | 65 × 65 × 60 mm, 265 g, 6.5 W, built-in IMU ICM40609 (L1) |
| Intel RealSense D435i depth camera, head | 1 | T1, U2; size and mass not yet read (Intel's site did not answer) |
| Microphone array | 1, four silicon microphones 20 mm apart | T1, slide 33 |
| Speaker, 5 W peak | 1 | T1, slide 33 |
| IMU, torso and pelvis | 2 | Mounting points in U3 |
| Joint encoders | 2 per joint, 46 | U1, U2, T3k (rotor and output) |
| Temperature sensors (NTC) | in the main chip and the battery management | T1, slide 42 |

### E2.4 The cables

- **Length:** "全身线束不超过10m" (the whole-body harness is not longer than 10 m) (T1, slide 3).
- **Layout:** power and signal cables run inside the hollow joint shafts; the motors of one arm or one leg are
  connected in series (T1, slide 35), on XT30 connectors, "XT30 2+2 连接器上下游菊花链串接", daisy-chained (T3k).
  The head's sensors reach the main board over high-speed differential lines through the head's MCU board (T1, slide
  37); the LiDAR and camera data go over serial or USB, not the joint bus (T1, slide 34).
- **Joint bus disagrees:** CAN (T1, slides 34, 36; J1); RS485, about 6 lines: 2 arms, 2 legs, head, waist (C1, from the
  board, partly hidden under tape).
- **Parts named:** capacitor buffers, the XT30 harness, the harness terminals (T1's cost table: 30, 90 and 150 yuan).
- **Not given anywhere:** the cross-sections of the wires, so no copper per metre, and the length of each kind of
  cable.

### E2.5 The battery

Quick-release pack of 13 lithium cells in series, 46.8 V nominal, 9,000 mAh, 0.42 kWh, about 2.5 kg (T1, slide 25);
with its own battery management (B1, T1). 120 × 80 × 182 mm (B1). Cell format and number of cells: not given.

### E2.6 The frame, the shell and the cooling

- **Torso:** "躯干采用全塑料件", plastic parts throughout: engineering plastics (ABS, PA) and silicone (T1, slide 44).
- **Limbs:** aluminium alloy links with diamond-shaped cut-outs; the lower-leg links are steel, "身体中唯一采用钢材质结构件",
  the only steel structural part; every other structural part is aluminium (T1, slides 18, 44, 45). The hands of the
  basic version are plastic and do not move (T1, slide 18).
- **Back:** outer shell, then a foam cushion, then an inner plastic layer over the main board (T1, slide 26).
- **Cooling:** main board, aluminium heat sink and fan (basic), with a vapour chamber added in the EDU version; knees,
  copper vapour chamber and copper strip into the structure; waist joint, a small centrifugal fan (T1, slides 39 to
  41); hips, two centrifugal fans (T3).
- **Screws:** not given.

### E2.7 What is still missing

- **The large joint part by part.** Only its total (1,100 g, T1; 1,085.1 g with cables, T3k) and its make-up (T3k).
- **Inside the parts:** the stator's steel core against its copper; the magnet grade and any steel in the rotor; what
  "Other" (38.1 g) is.
- **Board areas,** except that the small joint's board weighs 12.8 g.
- **The wires' cross-sections** and the length of each kind of cable.
- **The battery cells,** the D435i's size and mass, the screws.

T1 is the only first-hand teardown with masses. T3k (Munro's knee report) is behind Zhihu's login; Munro's full video
with Chinese subtitles is on Bilibili (https://www.bilibili.com/video/BV15jek6wEZH), and a Bilibili video on the
G1's joint motor (https://www.bilibili.com/video/BV1oye46dEt6); neither was watched.

### E2.8 Proposal: robot type 1 part by part, with estimates (E) where the reports stop. Not entered

Asked, Matthias, 2026-10-27: "Can based on these reports the other parts be estimated? They would be labeled
accordingly and have a large uncertainty", then "Yes do so. Try to avoid normalization, if there are indications
normaization will bias all the values".

**How.** Every part is estimated on its own basis; nothing is rescaled to fit a total. Where parts must make up a
measured whole, one part is the explicit remainder, named below; which one is Matthias's decision. The sums against
the measured totals are checks (V45), not corrections. Masses are for one piece, in g; min / mode / max.

**The uncertainty of an estimate** (Matthias, 2026-10-27: "Estimates should be larger than known numbers"; applied on
his "Yes"): every value marked E spans at least half to 1.5 times its mode, wider where its basis is wider. A bound
is cut only at a stated limit, named where it applies. Known numbers keep their sources' ranges.

**Bases added for the estimates** (read myself unless said):
- Intel, D435i specifications: 90 × 25 × 25 mm, no mass.
  https://www.intel.com/content/www/us/en/products/sku/190004/intel-realsense-depth-camera-d435i/specifications.html
  The D435's 75 g is from Intel's D400 datasheet as quoted in a RealSense forum reply (second-hand):
  https://support.realsenseai.com/hc/en-us/community/posts/19069743039891/comments/19071249439891
- XT30 wire range 20 to 16 AWG (TME's listing of the XT30-F, second-hand through a search summary):
  https://www.tme.com/in/en/details/xt30-f/dc-power-connectors/amass/ ; Munro: the G1's joints are joined by "XT30
  2+2" connectors, two power and two signal contacts (T3k).
- RK3588S whole boards 90 × 60 mm (Firefly ROC-RK3588S-PC) and 85 × 56 mm (ArmSoM Sige7s), from search summaries
  of https://www.cnx-software.com/2023/07/01/firefly-rockchip-rk3588-sbc-32gb-ram/ and
  https://itsfoss.com/news/armsom-sige7s/ (second-hand).
- **The copper share of the stator:** no source of the kind (E2.10); 23 / 36 / 45 % from measured car traction
  motors and Matthias's car auxiliary-motor workbook, agreed by Matthias on 2026-10-27 ("Yes use this numberrs").

**1. Small joints, 14** (hips are not small: ankles 4, arms 10). T1 weighed one lower-leg joint part by part; the
same part in the other 13 joints is taken as the weighed mass ± 50 % (E). The workbook's own modules differ by ± 24 %
around T1's 525 g (rows 9 to 11: 0.65 and 0.40 kg).

| Part | g (min / mode / max) | Materials (share of the part) |
|---|---|---|
| Stator | 47.2 / 94.3 / 141.5 | copper 0.23 / 0.36 / 0.45 (E2.10, agreed); coating 0.02 / 0.05 / 0.10 (E); **electrical steel the remainder** |
| Rotor | 21.5 / 42.9 / 64.4 | NdFeB 0.45 / 0.90 / 1.00 (E; T1 calls it "magnet"; at most 100 %); steel the remainder |
| Magnet carrier | 8.5 / 16.9 / 25.4 | plastic bearing 0.05 / 0.15 / 0.30 (E); aluminium the remainder |
| Gears: stage 1 sun, stage 1 planets and carrier with stage 2 sun, both ring gears | 4.0–38.0 each; 81.2 at the mode together | steel (T1) |
| Stage 2 planets, carrier, crossed roller bearing | 37.0 / 74.0 / 111.0 | aluminium 0.125 / 0.25 / 0.40 (E; T1: carrier aluminium); steel the remainder |
| Driver board | 6.4 / 12.8 / 19.2 | PCB (T1) |
| Two small bearings | 5.5 / 11.0 / 16.5 | steel (T1) |
| Housing; two end caps | 39.7 / 79.3 / 119.0; 11.9 / 23.7 / 35.6 | aluminium (T1) |
| Output flange | 25.4 / 50.8 / 76.2 | steel (T1) |
| Other | 19.1 / 38.1 / 57.2 | copper 0.10 / 0.25 / 0.40, steel 0.20 / 0.40 / 0.60 (E, no basis: wires, screws, encoder magnets); plastics the remainder |

**2. Large joints, 9** (hips 6, knees 2, waist 1). No part was weighed. Each part = the small joint's part × a factor
(E) from the joints' sizes and torques: 80 against 60 mm across (area 1.78 ×), 64 against 70 mm high, the joint's
surface 1.39 ×, the mean output torque of the large joints 99.3 against 27.9 N·m (3.56 ×; U3), and Munro's "stack"
of driver boards in the knee (T3k). Materials as in the small joint. Limit: no factor below 1.0, as a large joint's
part is not lighter than the small joint's.

| Part | Factor (min / mode / max) | Why |
|---|---|---|
| Stator, rotor, magnet carrier | 1.0 / 1.78 / 2.67 | the motor's cross-section |
| Gears and stage 2 assembly | 1.17 / 2.33 / 3.56 | from the cross-section alone to growing with the torque; mode 3.56^(2/3) |
| Driver board | 1.78 / 3.56 / 5.33 | one, two or three boards of the larger size |
| Two small bearings | 1.0 / 1.78 / 2.67 | the area |
| Housing | 1.0 / 1.39 / 2.09 | the surface |
| Two end caps, output flange, other | 1.0 / 1.78 / 2.67 | the area |

Check: the large joint's modes add up to 1,012 g; its draws to 912 / 1,034 / 1,158 g (2.5 % / mean / 97.5 %), against
1,100 g (T1) and 1,085.1 g (T3k). Nothing is scaled to meet it.

**3. Battery.** Cells from the energy, as the project already does for its battery rows: 46.8 V × 9 Ah = 421.2 Wh
(T1) over the NMC cell's 256 / 241.5 / 232.5 Wh/kg (E1.7d) = 1,645 / 1,744 / 1,812 g; kept, as both are sourced and
the cells cannot outweigh the 2.5 kg pack. Battery management board 30 / 60 / 96 cm² (E; at most the pack's 120 × 80
mm, B1). **The pack's housing, busbars and wires are the remainder of its 2.5 kg (T1): 0.66 / 0.73 / 0.80 kg**; their
materials are not known.

**4. Boards outside the joints.** Mass = area × 0.28 / 0.56 / 0.84 g/cm² (E): the small driver board's 12.8 g on a
round board 54 mm across (22.9 cm²), ± 50 %.

| Board | Area, cm² (E) | g | Basis |
|---|---|---|---|
| Main control board (RK3588S, core board on base board) | 50 / 100 / 150 | 14 / 56 / 126 | whole RK3588S boards 48 to 54 cm² as the least; C1 |
| Head control board | 5 / 15 / 30 | 1 / 8 / 25 | none beyond T1's naming it |
| Power distribution unit and DC-DC converter | 30 / 60 / 100 | 8 / 34 / 84 | T1's cost table names them |
| Capacitor buffer boards, 4 | 2 / 5 / 10 each | 0.6 / 3 / 8 each | one per arm and leg end (T1) |
| Battery management board | 30 / 60 / 96 | 8 / 34 / 81 | above |
| Driver boards in the joints | 11.5 / 22.9 / 28.3 per small joint (at most the 60 mm joint); × 1.78 to 5.33 per large joint | weighed (T1) and above | T1, T3k |

**5. Cooling** (E): main board heat sink 50 / 100 / 200 g aluminium; 4 fans 5 / 10 / 20 g each (copper 0.05 / 0.10 /
0.20, plastics the rest); 2 knee vapour chambers with their copper strips 10 / 20 / 40 g each, copper.

**6. Sensors.** LiDAR 265 g (L1); D435i 72 / 75 / 80 g (Intel's D435, 75 g, second-hand; kept as a sourced number);
microphone array 5 / 10 / 20 g (E); speaker 17.5 / 35 / 60 g (E); 2 IMUs 1 / 2 / 5 g each (E). Their insides are not
yet known; for now each is all "electronics".

**7. Cables** (E). 3 / 6 / 10 m of four conductors (at most T1's "not over 10 m"); the body's routes (two legs about
0.9 m, two arms about 0.6 m, waist and head about 0.5 m, plus battery and sensor leads) give about 5 to 6 m. Two power
conductors of 0.52 / 0.82 / 1.31 mm² (20 / 18 / 16 AWG, the XT30's range, kept) and two signal conductors of 0.065 /
0.13 / 0.20 mm². Copper 31 / 102 / 271 g; insulation and jackets 0.5 / 1 / 1.5 × the copper; 46 XT30 (2+2)
connectors, two per joint, 1.5 / 3 / 4.5 g each, copper 0.175 / 0.35 / 0.525.

**8. Others.** Fixed plastic hands of the basic version (T1), 2 × 120 / 170 / 220 g (U3: 0.170 kg each, a design
value, kept). Screws 200 / 500 / 1,000 g steel: **no source; E**.

**9. Frame and shell: the robot's remainder.** 35 kg (34 / 35 / 36, "About 35kg", U1) minus everything above: 12.0 /
13.8 / 15.5 kg. Split by estimate: plastics (the torso's plastic parts, covers, silicone, foam; T1) 2.25 / 4.5 / 6.75
kg; the steel lower-leg links (T1) 0.3 / 0.6 / 1.0 kg; **aluminium the remainder**, 6.1 / 8.6 / 11.1 kg, never below
zero.

**Checks against the workbook's own material sheet, robot type 1** (kg; this proposal 2.5 % / mean / 97.5 %, V45):

| Material | This proposal | Workbook (min / mode / max) | Reading |
|---|---|---|---|
| Aluminium | 10.4 / 12.7 / 15.1 | 10.5 / 12 / 13.5 | agree |
| Steel | 7.6 / 8.6 / 9.6 | 7.0 at the mode (bearing and gear 4.2 + structural 2.8) | the proposal is higher |
| Plastics | 4.0 / 5.8 / 7.6 | 6.7 at the mode (polymers 5.5 + CFRP 1.2) | close; T1 names no carbon fibre |
| Copper | 1.2 / 1.5 / 1.9 | 3 / 3.8 / 4.5 | **the workbook has about two and a half times as much** |
| Battery cells | 1.67 / 1.73 / 1.79 | 2 / 2.5 / 3, the whole pack | the pack's rest is 0.73 kg |
| Electrical steel | 1.2 / 1.7 / 2.2 | none | the workbook has none |
| Electronics (boards, sensors) | 1.0 / 1.2 / 1.4 | 1.5 at the mode (0.5 + 1.0 miscellaneous and optics) | close |
| Magnets (NdFeB) | 0.7 / 1.0 / 1.4 | 1.2 / 1.5 / 1.8 | the proposal is lower |
| Cables (copper, insulation, connectors) | 0.27 / 0.45 / 0.66 | row 18: 1.1 / 1.3 / 1.5 | **the workbook has about three times as much** |

**Checks against the workbook's own parts list, robot type 1** (sheet `Components & Materials`, rows 8 to 20; asked,
Matthias: "Compare with already existing data. Aluminum is used also for cooling"; kg, 2.5 % / mean / 97.5 %, V45):

| Workbook row | This proposal | Workbook (min / mode / max) | Reading |
|---|---|---|---|
| 8, knee actuators (2) | 1.82 / 2.07 / 2.32 | 2.3 / 2.5 / 2.7 | lower |
| 9, hip and waist actuators (7) | 6.39 / 7.24 / 8.10 | 6.3 / 7.0 / 7.7 | agree |
| 10, ankle and shoulder actuators (10) | 4.56 / 5.25 / 5.93 | 5.5 / 6.5 / 7.5 | lower: T1 gives every small joint 525 g, the workbook 650 g |
| 11, elbow and wrist actuators (4) | 1.82 / 2.10 / 2.37 | 1.4 / 1.6 / 1.8 | higher: the workbook gives 400 g |
| 8 to 11, all joints | 15.2 / 16.7 / 18.1 | 15.5 / 17.6 / 19.7 | agree |
| 12, battery pack | 2.5 | 2.3 / 2.5 / 2.7 | agree |
| 13, main compute | 0.17 / 0.25 / 0.34 (boards outside the joints and the heat sink) | 0.35 / 0.40 / 0.45 | lower |
| 14, LiDAR | 0.265 (Livox datasheet) | 0.65, labelled "Direct", citing Livox (S46) | **the workbook's value does not match its own source** |
| 15, depth camera | 0.072 / 0.075 / 0.080 | 0.08 / 0.10 / 0.12 | close |
| 16 and 17, frame and shell | 12.0 / 13.8 / 15.5 (the remainder) | 8.3 / 9.7 / 11.1 | **higher by about 4 kg** |
| 18, harness | 0.27 / 0.45 / 0.66 | 1.1 / 1.3 / 1.5 | a third |
| 19, fasteners and structural bearings | 0.28 / 0.57 / 0.90 (screws; the bearings are inside the joints) | 1.8 / 2.2 / 2.6 | a quarter |
| 20, cooling fans and heat pipes ("Copper heatpipes & Al 6063 fins") | 0.06 / 0.09 / 0.13, plus the heat sink in row 13 | 0.45 / 0.55 / 0.65 | **far lower** |
| no row: microphones, speaker, IMUs; the basic version's fixed hands | 0.05; 0.34 | — | not in the workbook |

- **The 4 kg in the frame and shell come from the rows above:** where this proposal is lower (harness, fasteners,
  cooling, LiDAR, compute, joints), the remainder grows. Together, frame, shell, harness, fasteners and cooling are
  14.9 kg here and 13.75 kg in the workbook; Unitree's model file (U3), less the joints, battery, boards and
  sensors, leaves about 13 kg (an approximate reading of its link masses). The totals agree; the split between the
  frame and the smaller rows does not, and the remainder carries every low estimate.
- **Aluminium in the cooling, which this proposal undercounts:** the main board's "大面积铝制散热片+风扇" (a large
  aluminium heat sink and fan; T1, slide 39), counted at 50 / 100 / 200 g; the knees' heat pipe has an aluminium
  condensing section (T3) and leads the heat through a copper strip into the aluminium structure (T1, slide 40), but
  the knees are counted as copper only; the workbook's row 20 names "Al 6063 fins".
- **The LiDAR in the workbook:** row 14 gives 0.65 kg, min = mode = max, labelled "Direct", citing Livox's MID-360
  specifications (S46, https://www.livoxtech.com/mid-360); Livox's specifications give 265 g
  (https://www.livoxtech.com/mid-360/specs). Reported, not changed.

**Matthias's answers to the comparison** (2026-10-27): on the aluminium in the cooling, "Is with the joins often
used": the cooling aluminium is counted with the joints (their aluminium housings, T1 and T3), and the knees'
vapour chambers and copper strips are now part of the knee joints; no further research on the cooling. On the harness
and screws: "Do not go to much in detail. It is essential, where the critcal materials are": the harness and the
screws stay as estimated, and the frame and shell stay the remainder.

**Where the materials of interest sit in robot type 1** (kg, means by body region; total 2.5 % / mean / 97.5 %; V45).
Each part is split over the regions by its count of pieces there: small joints legs 4 (ankles), arms 10; large joints
legs 8 (hips 6, knees 2), torso 1 (waist); boards and sensors where T1 places them; cables and screws over the whole
body.

| Material | Legs | Arms | Torso | Head | Whole body | Total |
|---|---|---|---|---|---|---|
| Copper | 0.83 | 0.42 | 0.08 | 0 | 0.18 (cables) | 1.17 / 1.52 / 1.90 |
| NdFeB (Nd, Pr, Dy, Tb, B) | 0.62 | 0.34 | 0.06 | 0 | 0 | 0.69 / 1.02 / 1.39 |
| Battery cells (Li, Ni, Co, Mn, graphite) | 0 | 0 | 1.73 | 0 | 0 | 1.67 / 1.73 / 1.79 |
| Boards and sensors (Au, Ag, Pd, Si, Ga, Ge) | 0.42 | 0.14 | 0.20 | 0.40 | 0 | 0.97 / 1.16 / 1.35 |
| Aluminium in the joints and the heat sink | 2.40 | 1.36 | 0.35 | 0 | — | 3.47 / 4.11 / 4.78 |
| Aluminium in the frame | — | — | — | — | 8.6 (the remainder) | 6.1 / 8.6 / 11.1 |
| Electrical steel (Si) | 1.04 | 0.56 | 0.10 | 0 | 0 | 1.23 / 1.71 / 2.22 |

- **The joints hold 88 % of the copper and all of the NdFeB**; about 60 % of each sit in the legs.
- **Half the boards' mass (0.41 / 0.59 / 0.76 kg, 51 %) is the 23 joints' driver boards**, not the main board; the
  head holds the LiDAR, the camera and the head board (0.40 kg).
- **The battery metals are all in the torso**, in one quick-release pack.
- Not yet resolved to elements: the boards' gold, silver and palladium and the sensors' gallium and germanium (no
  composition yet), the magnets' Nd, Pr, Dy and Tb (the recipe of E1.6 exists).

**Where the proposal is weakest:** "Other" in the joint, the rotor's NdFeB share (E2.10 points below 90 %), the board
areas outside the joints, the screws and the frame-and-shell split. The two gaps marked in bold (copper and cables) both
depend on the copper in the stators and the harness; either the workbook is high or these estimates are low.

**Decided by Matthias, 2026-10-27** (step 1 of bringing robot type 1 into the project, answers chosen from the options
offered): the remainders "Accept all" (the stator's electrical steel, the rotor's steel, the magnet carrier's
aluminium, gear stage 2's steel, the joint's "Other" plastics, the battery pack's housing, busbars and wires, the
robot's frame and shell, and the frame's aluminium); the rotor's NdFeB "Keep 45 / 90 / 100 %"; the other values
marked E "Accept all"; the hot joints "Hips, knees, waist, ankles" (magnets for 150 °C as the base, 180 and 200 °C as
scenarios; the arms 120 °C).

### E2.8b The boards' and sensors' composition from Matthias's other projects (2026-10-27). Not entered

Asked, Matthias: "There is information concerning the PCB composition in the data center work. There is also
information cocnerning the sensors in the electronics of cars". Read (his workbooks, not changed):
`RAWCLICDataCenters/data/researched/02_DataCenterPCBComposition.xlsx` (sheet `PCB`, mg per cm² by board type);
`RAWCLICVehicleElectronics/Data/04_VehiclePCBComposition.xlsx` (mg per cm² by car board category) and
`07_VehicleSensorComposition.xlsx` (sheet `Sensor Details`, mg per sensor element, 58 types, "not the complete module
housing"; sources named in its sheet `Methodology`: makers' datasheets, teardowns, IMDS/GADSL, papers).

**Boards: the closest board type by function.**

| G1 board | Car category (`04_`) | Data-centre type (`02_`) |
|---|---|---|
| Joint driver boards (23; motor inverter, MCU) | PE_HVS (inverters, DC/DC; Cu 25, Au 0.02 mg/cm²) | PowerSupplyUnit (Cu 488 × 0.65 coverage, Au 0) |
| Main control board (RK3588S) | ITC (holds the "Combined cluster+infotainment SoC"; Cu 12, Au 0.1) | ComputeMainBoard (Cu 753 × 0.65, Au 1) |
| Power distribution, DC-DC, capacitor buffers | PE_HVS | PowerSupplyUnit |
| Battery management | BMS | — |
| Head control board | VCC (control units) | — |

- **The two projects disagree by about 20 times on copper and 10 times on gold per cm².** On the G1's weighed driver
  board (12.8 g on 22.9 cm², 559 mg/cm²), the car value makes copper 4.5 % of the board's mass, the data-centre value
  57 %. For the 23 driver boards (about 1,054 cm²): copper 26 g (car) against 334 g (data centre); gold 21 mg against
  0 mg.
- The car gold (0.02 to 0.1 mg/cm²) is near the measured whole boards of Bizzo et al. 2014, about 0.08 mg/cm², as
  recorded in `RAWCLICDataCenters/documentation/claude/EVIDENCE.md` (§ 10.3); that project's own audit calls its board
  composition "constructions" (§ 10.5).

**Sensors: the car sensor elements that make up the G1's sensors.**

| G1 sensor | Car sensor elements (`07_`, per unit, mode) |
|---|---|
| LiDAR Livox Mid-360 (905 nm) | laser diode array (Ga 30, As 30, In 3, Au 0.5 mg), photodetector array (Si 60, Ga 1, As 1, Au 0.3 mg), IMU |
| Depth camera D435i | 2 IR camera sensors, 1 CMOS image sensor, laser diode array (the IR projector), IMU |
| Microphone array | 4 MEMS microphones (Si 4, Cu 2, Au 0.02 mg each) |
| IMUs, torso and pelvis | 2 IMU (Si 35, Cu 12, Au 0.12 mg each) |
| Joint encoders, 2 per joint | 46 angle sensors (Hall/AMR IC with NdFeB or ferrite magnet; Nd 20, Dy 0.5, Au 0.06 mg each) |

Together about 5 mg gold, 61 mg gallium, 61 mg arsenic, 0.9 g neodymium (in the encoders), at the modes; no
germanium. The car rows are the sensor elements only; the modules' boards, aluminium housings and glass are not in
them. Speakers are not among the car types.

**Copper of the boards: Bizzo et al. 2014, read myself** (Bizzo, Figueiredo, de Andrade, *Materials* 7 (2014)
4555–4566, https://pmc.ncbi.nlm.nih.gov/articles/PMC5455934/; UNICAMP, a university): about 12 kg of whole PC boards
(XT, 486, Pentium) with their components, ground, digested in aqua regia, measured by AAS and ICP, no quality control
reported; Table 3 sets its result beside 13 other studies. Following Matthias's rule for analyses made only at
universities ("combine them and use respective large uncertainties"), the 14 copper values are combined: **12.5 / 20.0 / 28.7
wt%** (min / mean / max). Gold (8 studies after 2000: 29 to 420 ppm, median 111), silver (79 to 5,210 ppm, median 450)
and palladium (33 to 220 ppm, three studies) bracket the car values (at 0.56 g/cm²: gold 36 to 179 ppm, silver 179 to
536 ppm, palladium 9 to 89 ppm at the modes), which therefore fit; the car copper (4.5 % of the weighed board) does
not. Asked, Matthias: "Yes if they fit, show me the results".

**Result: the critical elements in the boards and sensors of robot type 1** (mg; means by region; total 2.5 % / mean
/ 97.5 %; a scratch Monte Carlo, V45). Boards: copper = board mass × 12.5 / 20.0 / 28.7 wt%; gold, silver,
palladium, tin, nickel = board area × the car category's mg/cm²; sensors: the car sensor elements, with their own
ranges.

| Element | Legs | Arms | Torso | Head | Total |
|---|---|---|---|---|---|
| Copper | 87,800 | 28,900 | 39,700 | 2,800 | 102,000 / 159,000 / 227,000 |
| Gold | 21 | 8 | 16 | 5 | 35 / 51 / 73 |
| Silver | 229 | 73 | 83 | 2 | 216 / 388 / 626 |
| Palladium | 8 | 3 | 8 | 1 | 12 / 19 / 28 |
| Tantalum | 78 | 25 | 36 | 2 | 63 / 140 / 248 |
| Gallium | 0 | 0 | 0 | 127 | 33 / 127 / 262 |
| Arsenic | 0 | 0 | 0 | 126 | 33 / 126 / 259 |
| Indium | 0 | 0 | 0 | 29 | 8 / 29 / 59 |
| Neodymium (encoder magnets) | 1,155 | 961 | 96 | 0 | 809 / 2,212 / 4,027 |
| Dysprosium (encoder magnets) | 44 | 37 | 4 | 0 | 24 / 85 / 163 |
| Germanium | — | — | — | — | none |

- **The joints' driver boards and encoders hold 61 % of this gold and 77 % of this copper.** Gallium, arsenic and
  indium are all in the head, in the LiDAR's and the depth camera's lasers and detectors.
- The boards' copper adds about 0.16 kg to the robot's 1.52 kg of E2.8 (it was inside "electronics" there).
- **Tantalum** (Matthias: "There is the tantalum for the PBC of the data center"): board mass × 0 / 100 / 450 ppm,
  from `RAWCLICDataCenters/data/researched/04_DataCenterElementComposition.xlsx`, sheet `BoardsAndComponents` (E;
  Fraunhofer's 445 ppm in pyrolysed board material; agreed there by Matthias on 2026-10-16). It is given per kg of
  board, as the G1's boards are, so it fits.
- **Silicon is left out** (Matthias: "Si is not needed even it is on the critcal").
- **Not covered:** the sensor modules' boards and housings; the speaker. The board areas are drawn independently of
  the board masses, which ignores that a larger board is also heavier.

### E2.8c The complete picture of robot type 1 (2026-10-27). Not entered

Asked, Matthias: "Show me first the complete picture". The parts (E2.8), the boards and sensors (E2.8b) and the
battery cells resolved with the project's own recipe 'NMC cylindrical' through `02_composition.py`'s `RecipeDraws`
(Li 2.58, Ni 19.9, Co 1.37, Mn 1.30, C 29.1, Cu 8.36 % of the cells at the mean), summed draw by draw (V45). Means by
region; total 2.5 % / mean / 97.5 %.

| Material or element | Unit | Legs | Arms | Torso | Head | Whole body | Total |
|---|---|---|---|---|---|---|---|
| Copper | kg | 0.92 | 0.45 | 0.26 | 0.003 | 0.18 | 1.47 / 1.82 / 2.21 |
| NdFeB magnets | kg | 0.62 | 0.34 | 0.06 | 0 | 0 | 0.69 / 1.02 / 1.39 |
| Aluminium in the joints and the heat sink | kg | 2.40 | 1.36 | 0.35 | 0 | 0 | 3.47 / 4.11 / 4.78 |
| Aluminium in the frame (the remainder) | kg | — | — | — | — | 8.6 | 6.1 / 8.6 / 11.1 |
| Lithium | kg | 0 | 0 | 0.045 | 0 | 0 | 0.042 / 0.045 / 0.047 |
| Nickel | kg | 0.001 | 0 | 0.35 | 0 | 0 | 0.32 / 0.35 / 0.37 |
| Cobalt | kg | 0 | 0 | 0.024 | 0 | 0 | 0.023 / 0.024 / 0.025 |
| Manganese | kg | 0 | 0 | 0.023 | 0 | 0 | 0.021 / 0.023 / 0.024 |
| Carbon (graphite) | kg | 0 | 0 | 0.50 | 0 | 0 | 0.47 / 0.50 / 0.54 |
| Gold | g | 0.021 | 0.008 | 0.016 | 0.005 | 0 | 0.034 / 0.051 / 0.073 |
| Silver | g | 0.23 | 0.07 | 0.08 | 0.002 | 0 | 0.22 / 0.39 / 0.62 |
| Palladium | g | 0.008 | 0.003 | 0.008 | 0.001 | 0 | 0.012 / 0.019 / 0.028 |
| Tantalum | g | 0.08 | 0.03 | 0.04 | 0.002 | 0 | 0.06 / 0.14 / 0.25 |
| Gallium | g | 0 | 0 | 0 | 0.13 | 0 | 0.03 / 0.13 / 0.26 |
| Indium | g | 0 | 0 | 0 | 0.03 | 0 | 0.007 / 0.029 / 0.059 |
| Neodymium in the encoders | g | 1.15 | 0.96 | 0.10 | 0 | 0 | 0.8 / 2.2 / 4.0 |
| Magnesium, titanium, germanium | — | none in robot type 1 (T1 names none) | | | | | |

- Silicon is left out (Matthias).

**The magnets' elements, the grade following the joint's heat** (Matthias: "I told you to take the NdBFe composition
from the car traction motors. There is the temperature issue. SO heavy used joints, which can only be aircooled have
to have high temperature NdBFe"). The fractions are drawn by RAWCLICVehicleTractionMotor's own
`magnet_element_draws` (`src/composition.py`; grade bands from its `data/raw/10_MaterialElementDefinitions.xlsx`,
sheet `PermanentMagnetNdFeB`; uniform between a class's bounds, Nd split into Nd and Pr, iron the balance), run in
that project's environment, read-only. Grade classes: Nd + Pr 0.29–0.32 in every class; Dy H 0.02–0.05, SH
0.04–0.07, UH 0.06–0.09, EH 0.08–0.10; Tb SH 0–0.005, UH and EH 0–0.01.

- **Which joints run hot (proposed, Matthias's decision):** the hips (6, fans), knees (2, passive vapour chamber, "高负载关节（如承受
  90N·m扭矩的膝关节）" derate when hot, T1 slide 42), waist (1, fan) and ankles (4, carrying the robot): heavily used
  and air-cooled, so **SH, UH or EH**, the traction motors' three scenarios; the arms (10, at most 2 kg payload):
  **H**.

| Element, g (total 2.5 % / mean / 97.5 %) | Hot joints SH (150 °C) | UH (180 °C) | EH (200 °C) | Where |
|---|---|---|---|---|
| Neodymium | 175 / 262 / 359 | the same | the same | legs 160, arms 86, torso 16 |
| Praseodymium | 30 / 50 / 75 | the same | the same | legs 31, arms 16, torso 3 |
| Dysprosium | 28 / 49 / 77 | 38 / 63 / 95 | 46 / 73 / 106 | legs 34 to 56, arms 12, torso 3 to 6 |
| Terbium | 0.1 / 1.7 / 3.9 | 0.2 / 3.5 / 7.8 | 0.2 / 3.5 / 7.8 | legs, torso |
| Cobalt (in the magnets) | 32 / 55 / 83 | 42 / 68 / 102 | 51 / 82 / 120 | legs, arms, torso |
| Boron | 7 / 11 / 16 | the same | the same | legs, arms, torso |

NdFeB in all 23 joints: 0.69 / 1.02 / 1.39 kg (34 g per small joint, 61 g per large one, at the mean).

### E2.8d The spread between robots of type 1: what is known so far (2026-10-27; open point G)

Matthias: "You have just individual examples. The different realisations of such a type could vary on the compositon
parts etc quite a bit. This has to be in the results." Read so far (search summaries, second-hand unless said):

| Robot | What is there | Mass, joints | Source |
|---|---|---|---|
| Unitree G1 | the teardown, parts weighed (T1) | 35 kg, 23 joints (9 large, 14 small) | T1, U1 to U3 (read myself) |
| AgiBot X1 | open source: its BOM list, STEP and SolidWorks files offered for download (not opened) | ≤ 33 kg; 29 joints: PowerFlow R86-2 × 9 (0.76 to 0.81 kg, 50 to 80 N·m), R86-3 × 6 (1.25 to 1.28 kg, 150 to 200 N·m), R52 × 10, L28 × 4 | https://www.agibot.com/DOCS/OS ; https://agibot.com/products/X1 |
| Fourier N1 | open source: a complete BOM reported in its package (not opened) | about 38 kg, 1.3 m, 23 joints; FSA2.0 actuators; aluminium alloy and engineering plastics | https://www.yicaiglobal.com/news/chinese-robotics-pioneer-fourier-unveils-first-open-source-android |
| Booster T1 | specifications only | about 30 kg, 1.2 m, 23 joints, up to about 130 N·m, 10.5 Ah | a spec sheet of unclear provenance, via https://openelab.io/blogs/learn/booster-t2-vs-t1-education-vs-pro |
| Booster T2 | specifications only | about 1.4 m, 31 joints, 48 V 10 Ah; 125 lb (57 kg) for the T2 Pro (a dealer) | https://www.maverickdrone.com/collections/land/products/booster-t2 |

- **The workbook's Taxonomy, row 2 (category 1):** defining range 1.20 to 1.45 m and 30 to 50 kg; 23 to 43 joints (28
  to 34 across comparators); arm payload 2 to 5 kg; comparators AgiBot X1 (1.30 m, 33 kg, 34 joints), Fourier N1 (1.25 m,
  32 kg, 28 joints), Booster T2 (1.40 m, 38 kg, 32 joints).
- **Found, not verified:** the N1 at about 38 kg against the workbook's 32 kg; the T2 Pro at 57 kg against 38 kg.
  Reported, not changed.

**Read myself, on Matthias's "Yes go for it" (downloads into Claude's scratch folder, nothing into the project):**

- **AgiBot X1, its BOM** (`智元灵犀X1_BOM清单_20241024.xlsx`, 34 kB, and `智元灵犀X1总BOM.xlsx`, 19 kB, from
  https://github.com/AGIBOTTech/AGIBOT_x1_hardware, linked from https://www.agibot.com/DOCS/OS): every part with its
  quantity, type (machined, plastic, bought-in, standard) and material; **no masses**.
  - Joints: PowerFlow R86-3 × 6, R86-2 × 9, R52 × 10, linear L28 × 4 (the ankles' push rods), 2 grippers. Masses and
    torques from AgiBot's product page (https://agibot.com/products/X1, read myself): R86-3 1.28 kg, 200 N·m peak;
    R86-2 0.81 kg, 80 N·m; R52 0.45 kg, 19 N·m; L28 0.20 kg, 110 N. The joints weigh 20.27 kg of the X1's 33 kg (61 %;
    the G1's 49 %).
  - Frame of 6061-T6 machined parts; titanium-alloy ankle links (4); 40Cr steel wrist and ankle shafts; shells of
    3D-printed resin; rubber feet and handle; a stainless-steel battery case.
  - Electronics: an i7-13620H mini PC, a router, two data control units (Xyber-DCU), two IMUs (YIS320), an Intel D435,
    two 48-to-24 V converters, a 5 V module, a 95 W supply. Battery: 48 V, 8 Ah, NMC ("三元"), 12 cells in series.
  - Cables with a stated length: 10.2 m (of which 8.0 m XT30 (2+2) joint cables), plus 0.8 m to the linear actuators
    and grippers. Screws and pins: 980.
- **Fourier N1, its model file** (`FOURIERN1.urdf`, 34 kB, from https://github.com/FFTAI/fourier_lab, models/fouriern1;
  Fourier's own): the links add up to 39.7 kg; 23 joints in three torque classes: 95 N·m × 4 (hip pitch, knees), 54
  N·m × 7 (hip roll and yaw, waist, shoulder pitch), 30 N·m × 12 (ankles, shoulder roll and yaw, elbows, wrists). The
  N1's BOM was not found on Fourier's GitHub (its software repository `fourier-grx-N1` holds documents only).

**Decided by Matthias, 2026-10-27:**
- **Types kept apart** ("We have to see, that there is not a mixup between the different types"): a robot, or a
  configuration of it, counts for a type only where its maker's own height and mass lie inside the type's defining
  limits of the workbook's Taxonomy (type 1: 1.20 to 1.45 m, 30 to 50 kg). Type 1 is informed by the **Unitree G1,
  AgiBot X1 and Fourier N1**; the **Booster T2 Pro** (1.4 m, 57 kg) is outside type 1 and outside type 2's height ("2
  question yes"). The **Booster T1** was first counted in; Booster's own page gives it 1.18 m (E2.8e, T1a), below type
  1's 1.20 m, and Matthias took it out: "No, the T1 is out of type 1 (1.18 m). Type 1 is informed by the G1, X1 and N1."
- **No bootstrap** ("Ok no bootstrap. I want to make sure, that we represent the samples outside als."): with n robots,
  the next robot of the type lies outside their range with a chance of 2 / (n + 1), 50 % for three; resampling them
  can never reach it. The method must reach beyond the robots known, within the type's limits.
- **The method** (his choice from the options offered, "Real robot, varied"): each draw starts from one real robot of
  the type (G1, X1 or N1), kept whole so that its joints, materials and electronics stay consistent; its mass is
  then drawn within the type's limits around its own, and what follows mass is scaled with it.
- **How often each robot is drawn:** "Equal". **Which parts follow the drawn mass:** "Yes" to the frame, shell, battery
  and joints, not the electronics and sensors. **The X1, N1 and T1 where their data stop:** "We can assume, they are
  similar within given ranges. So come up with well founded estimates" (the T1 since taken out, above).

### E2.8e Step 2b: the X1, N1 and T1 as robots of type 1 (2026-10-27). Proposal, not entered

Matthias: "Yes, go on with step 2b: the well-founded estimates for the X1, N1 and T1, shown to me before they enter the
data file." Each robot needs what the G1 has in `parts_taken_apart.xlsx`: its joints (number, torque, module mass,
which of the G1's two joint designs its inside follows, magnet class), its battery, its boards, its sensors, its cables,
its hands, its frame and shell. Where a robot's data stop, it is taken as the G1 ("similar within given ranges").

**Sources, read for this step** (first-hand unless said):

| Code | What | What it is |
|---|---|---|
| X1a | AgiBot's X1 BOM list `智元灵犀X1_BOM清单_20241024.xlsx` and overall BOM `智元灵犀X1总BOM.xlsx`, https://github.com/AGIBOTTech/AGIBOT_x1_hardware | the maker's design lists; quantities and materials, no masses |
| X1b | AgiBot's X1 page, https://agibot.com/products/X1 (read for E2.8d) | the maker's claims: actuator masses and peak torques, ≤ 33 kg |
| X1c | AgiBot's X1 model file, `resources/robots/x1/urdf/x1.urdf` of https://github.com/AgibotTech/agibot_x1_train | the maker's model, legs only: 12 joints and their limits; all links 35.3 kg |
| X1d | AgiBot's OmniPicker manual, https://cdn.robotshop.com/media/A/Agb/RB-Agb-14/pdf/omnigripper-manual.pdf | the maker's: "Weight 0.43kg" |
| N1a | Fourier's N1 page, https://support-old.fftai.com/docs/GR-X-Humanoid-Robot/Fouriern1/N1_Introduction/ | the maker's specification table |
| N1b | Fourier's N1 model file `FOURIERN1.urdf` (E2.8d) | the maker's model: 23 joints, 39.7 kg |
| N1c | a teardown article on Zhihu, https://zhuanlan.zhihu.com/p/1899242762072749284 | second-hand (behind a login; through a search summary only): actuators FSA80-29E (about 96 N·m peak), FSA60-43E (about 51), FSA45-30E (about 29) |
| T1a | Booster's T1 page, https://www.booster.tech/booster-t1/, as printed on 31/01/2026 by the RoboCup team Tech United, https://hsl.robocup.org/wp-content/uploads/2026/03/large_Tech_United-specs-697dddb13c298.pdf | the maker's claims (the live page did not show the T1 when fetched) |
| T1b | Booster's T1 model file `resources/T1/T1_serial.urdf` of https://github.com/BoosterRobotics/booster_gym | the maker's model: 23 joints and their limits, 31.6 kg |
| T1c | Bipedal Robotics GmbH's T1 documentation, https://docs.bipedal.de/projects/t1/html/overview.html | a reseller's, citing Booster: boards, optional LiDAR |
| T1d | the RoboCup team Robotedge's T1 sheet, https://hsl.robocup.org/wp-content/uploads/2026/03/large_Robotedge-specs-698021eff19c7.pdf | second-hand: "Lithium-ion (24V - 48V)" |
| NV | NVIDIA, https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin | the maker's: the AGX Orin module "100mm x 87mm" |

**The joint masses, where a maker gives none (N1, T1).** AgiBot gives three rotary actuators with their mass and peak
torque (X1b): R52 0.45 kg at 19 N·m, R86-2 0.81 kg at 80 N·m, R86-3 1.28 kg at 200 N·m. Fitted on them: mass = 0.121 kg
× torque^0.441 (each within 3.4 %). Checked on the G1, not used to fit: its weighed small joint 0.525 kg against 0.50 to
0.58 kg from the fit at 25 to 35 N·m; its large joint 1.1 kg against 0.87 to 1.07 kg at 88 to 139 N·m. The fit gives a
joint's mass from its torque; its inside follows the G1's large joint above 40 N·m and the G1's small joint below
(JointParts, scaled to the joint's mass). Magnets as for the G1: legs and waist hot and air-cooled (SH), arms and head
H.

**AgiBot X1** (1.3 m; ≤ 33 kg, X1b; the legs-only model 35.3 kg, X1c)

| Item | Number | Min | Mode | Max | Label | Basis |
|---|---|---|---|---|---|---|
| R86-3: hip pitch, hip roll, knee | 6 | 1.22 kg | 1.28 kg | 1.34 kg | S | X1b; where they sit X1c (150 N·m in the model, 200 peak); large inside, SH |
| R86-2: hip yaw | 2 | 0.77 kg | 0.81 kg | 0.85 kg | S | X1b; X1c (50 N·m); large inside, SH |
| R86-2: waist | 3 | 0.77 kg | 0.81 kg | 0.85 kg | S, where E | X1a "腰部连杆组件"; 9 − 2 − 4 = 3; large inside, SH |
| R86-2: shoulder pitch and roll | 4 | 0.77 kg | 0.81 kg | 0.85 kg | S, where E | 7 joints per arm; large inside, H |
| R52: shoulder yaw, elbow, wrist | 10 | 0.43 kg | 0.45 kg | 0.47 kg | S, where E | X1b; small inside, H |
| L28 push rods: ankles | 4 | 0.19 kg | 0.20 kg | 0.21 kg | S | X1b, X1c (ankles 80 N·m); small inside, SH |
| OmniPicker grippers | 2 | 0.41 kg | 0.43 kg | 0.45 kg | S | X1d |
| Battery: 12 cells in series, NMC ("三元"), 8 Ah | 1 | 346 Wh | 355 Wh | 384 Wh | S | X1a: "48V8AH三元电池", "12S为佳"; 12 × 3.6 V, 12 × 3.7 V, the label's 48 V |
| Battery pack mass, stainless-steel case | 1 | 1.4 kg | 2.2 kg | 3.3 kg | E | the G1's 168 Wh/kg (2.5 kg for 421 Wh); X1a "不锈钢" case; the lower cut at 250 Wh/kg cells |
| i7-13620H mini PC board (ITC) | 1 | 60 cm² | 120 cm² | 180 cm² | E | X1a; a 4 × 4 inch board is 104 cm² |
| Xyber-DCU control boards (ITC) | 2 | 30 cm² | 60 cm² | 90 cm² | E | X1a |
| Router board, GL.iNet MT2500A (ITC) | 1 | 30 cm² | 60 cm² | 90 cm² | E | X1a |
| Power boards: 48-to-24 V × 2, 5 V module, 95 W supply, soft start × 2 (PE_HVS) | 6 | 10 cm² | 20 cm² | 30 cm² | E | X1a |
| Battery management board (BMS) | 1 | 30 cm² | 60 cm² | 96 cm² | E | as the G1 |
| Depth camera, Intel RealSense D435 | 1 | 72 g | 75 g | 80 g | S | X1a; as the G1 |
| Motion sensors YIS320 | 2 | 1 g | 2 g | 5 g | E | X1a; as the G1's IMU |
| Cables | 1 | 10 m | 11 m | 12 m | S | X1a: the lengths listed add up to 11.0 m (8.0 m XT30 2+2) |
| Titanium (TC4) links: waist × 2, ankle × 4 | 6 | 0.2 kg | 0.4 kg | 0.6 kg | E | X1a "钛合金TC4"; masses not given |
| Stainless 17-4PH shafts and crosses; steel pins | 9 + about 115 | 0.1 kg | 0.3 kg | 0.5 kg | E | X1a "0Cr17Ni4Cu4Nb", "40Cr" |
| Screws (about 980) | 1 | 0.3 kg | 0.6 kg | 0.9 kg | E | X1a (M2 to M5) |
| Bearings outside the actuators (crossed roller × 10, four-point × 9, ball × 20, rod ends × 8, spherical × 12) | 1 | 0.4 kg | 0.8 kg | 1.2 kg | E | X1a |
| Shell: 3D-printed resin (BOM list) or ABS (overall BOM) | 1 | 1.5 kg | 3 kg | 4.5 kg | E | X1a; the two lists differ |
| Rubber feet and handle | 3 | 0.1 kg | 0.2 kg | 0.3 kg | E | X1a "橡胶" |
| Frame: aluminium 6061-T6 and 7075-T6 | 1 | | | | E | the remainder of the robot, as for the G1 |

The X1's joints weigh 20.3 kg of its 33 kg (61 %), the G1's 49 %.

**Fourier N1** (1.245 m; "≈39 kg" in N1a's table, 38 kg in its text, 39.7 kg in N1b)

| Item | Number | Min | Mode | Max | Label | Basis |
|---|---|---|---|---|---|---|
| Joints of 90 N·m: hip pitch, knee | 4 | 0.44 kg | 0.88 kg | 1.32 kg | E | N1a (90 N·m; N1b 95); the fit; large inside, SH |
| Joints of 54 N·m: hip roll and yaw (4), waist (1) | 5 | 0.35 kg | 0.70 kg | 1.05 kg | E | N1a; the fit; large inside, SH |
| Joints of 54 N·m: shoulder pitch | 2 | 0.35 kg | 0.70 kg | 1.05 kg | E | N1a; the fit; large inside, H |
| Joints of 30 N·m: ankles | 4 | 0.27 kg | 0.54 kg | 0.81 kg | E | N1a; the fit; small inside, SH |
| Joints of 30 N·m: shoulder roll and yaw, elbow, wrist | 8 | 0.27 kg | 0.54 kg | 0.81 kg | E | N1a; the fit; small inside, H |
| Battery: Li-ion, 39.6 V (11 cells), 475 Wh | 1 | 475 Wh | 475 Wh | 475 Wh | S | N1a: "475WH", "39.6V", "46.2V" charge limit |
| Battery pack mass | 1 | 1.9 kg | 2.9 kg | 3.2 kg | S, E | N1a "≤3.2kg" (the upper cut); 1.9 kg at 250 Wh/kg cells |
| Cell chemistry | | | NMC | | E | 3.6 V per cell; N1a says only "锂离子电池" |
| Computer board, Intel Core i7-13700H (ITC) | 1 | 60 cm² | 120 cm² | 180 cm² | E | N1a |
| Power distribution board (PE_HVS); battery management board (BMS) | 1 + 1 | | | | E | as the G1 |
| Motion sensor, 6-axis | 1 | 1 g | 2 g | 5 g | E | N1a; N1b imu_link |
| Cables | 1 | 5 m | 10 m | 15 m | E | between the G1's E (6 m) and the X1's 11 m, wider |
| End pieces of the arms | 2 | 0.05 kg | 0.1 kg | 0.15 kg | S, E | N1b 0.099 kg each |
| Shell (engineering plastics), screws | | | | | E | N1a "铝合金-工程塑料"; as the G1 |
| Frame: aluminium alloy | 1 | | | | E | N1a; the remainder, as for the G1 |

The N1's joints from the fit: 15.0 kg of 39 kg (38 %). N1c's three actuator types match N1a's three torque classes.

**Booster T1** (1.18 m, ~30 kg, T1a; 31.6 kg in T1b)

| Item | Number | Min | Mode | Max | Label | Basis |
|---|---|---|---|---|---|---|
| Knees, 60 N·m | 2 | 0.37 kg | 0.74 kg | 1.11 kg | E | T1b; the fit; large inside, SH |
| Hip pitch, 45 N·m | 2 | 0.33 kg | 0.65 kg | 0.98 kg | E | T1b; the fit; large inside, SH |
| Hip roll and yaw, 30 N·m; waist, 30 N·m | 4 + 1 | 0.27 kg | 0.54 kg | 0.81 kg | E | T1b; the fit; small inside, SH |
| Ankle pitch 20 N·m, ankle roll 15 N·m | 2 + 2 | 0.20 kg | 0.40 to 0.45 kg | 0.68 kg | E | T1b; the fit; small inside, SH |
| Arms, 18 N·m | 8 | 0.22 kg | 0.43 kg | 0.65 kg | E | T1b; the fit; small inside, H |
| Head, 7 N·m | 2 | 0.15 kg | 0.29 kg | 0.44 kg | E | T1b; the fit; small inside, H |
| Battery: 10.5 Ah | 1 | 378 Wh | 454 Wh | 529 Wh | S, E | T1a "Battery: 10.5Ah"; the voltage is not given: 10, 12 or 14 cells (36, 43.2, 50.4 V); T1d "24V - 48V" |
| Battery pack mass | 1 | 1.5 kg | 2.8 kg | 4.2 kg | E | 160 Wh/kg, between the G1's 168 and the N1's ≥ 148; the lower cut at 250 Wh/kg cells |
| Cell chemistry | | | NMC | | E | not given |
| NVIDIA Jetson AGX Orin module (ITC) | 1 | 87 cm² | 87 cm² | 87 cm² | S | T1a; NV 100 × 87 mm |
| Its carrier board (ITC) | 1 | 50 cm² | 100 cm² | 150 cm² | E | Booster's own; not described |
| Motion board, Intel Core i7-1370P (ITC) | 1 | 60 cm² | 120 cm² | 180 cm² | E | T1a; T1c "Intel Express-i7" |
| Power distribution (PE_HVS), battery management (BMS), head board (VCC) | 1 + 1 + 1 | | | | E | as the G1 |
| Depth camera (Intel; model not given) | 1 | 72 g | 75 g | 150 g | E | T1a "Depth Camera", T1c "Intel depth camera" |
| Motion sensor, 9-axis | 1 | 1 g | 2 g | 5 g | E | T1a |
| Circular 6-microphone array; speaker | 1 + 1 | | | | E | T1a; as the G1's |
| Cables | 1 | 5 m | 10 m | 15 m | E | as for the N1 |
| Hands (without joints) | 2 | 0.16 kg | 0.33 kg | 0.49 kg | E | T1b left_hand_link 0.327 kg |
| Shell, screws; frame: aluminium (the remainder) | | | | | E | not given; as the G1 |

The T1's joints from the fit at the model's limits: 11.2 kg of 30 kg (37 %). Read as peak torques scaled like the
knee's (130 N·m against 60 in T1b), they would weigh 15.8 kg, within the upper bounds; but then the arms' actuators
would nearly equal the arms' links in T1b (4.1 kg), so the model's limits are taken as the mode.

**Found, for Matthias to decide (nothing entered):**
1. **The T1 is 1.18 m** (T1a: "118×47×23 cm"), below type 1's 1.20 m. By the rule of 2026-10-27 ("a robot counts for
   a type only where its maker's own height and mass lie inside the type's limits") it falls out of type 1; its ~30 kg
   lies on the lower limit. **Decided:** "No, the T1 is out of type 1 (1.18 m). Type 1 is informed by the G1, X1 and
   N1." The T1's table above stays as the record of what was read; it does not enter the data file.

**Decided, 2026-10-27** (Matthias's answers to points 2 to 5): the X1's R86-2 "9"; the X1's phone "Count it as a
board (E)"; "Standard robot" (no optional parts); the makers' stated masses (X1 33 kg, N1 39 kg). Then: "Use the
monte carlo approach for most possible". **Proposed on that, not entered:**
- every value still fixed gets a range where a range is not invented: the N1's battery 451 / 475 / 499 Wh (E, ±5 %
  production tolerance on Fourier's rating); the G1's battery pack 2.25 / 2.5 / 2.75 kg (E; the teardown's "~2.5kg")
  and its capacity 8.55 / 9 / 9.45 Ah (E, ±5 %);
- the X1's phone board: 20 / 50 / 100 cm², car category ITC, mass per cm² from Constants (E). No measured area of a
  phone's main board found: HilPCB (https://hilpcb.com/en/blog/iphone-consumer-electronics/) gives the iPhone X's
  two stacked halves as about 135 % of the iPhone 8 Plus board, no cm²; the 2025 study of 45 phone boards
  (https://www.sciencedirect.com/science/article/pii/S0921344925006184) refused access. Its display (indium) and
  battery are not covered by "a board";
- fixed, because a range would be invented: the counts (joints, boards, screws; the spread between robots comes from
  drawing the robot), the Orin module's 100 × 87 mm, the G1's 46.8 V (13 cells), copper's density, the cell chemistry
  (NMC; the X1 "三元"); open: the G1's LiDAR, 265 g in Livox's specification.

**Accepted, 2026-10-27:** "Yes, accept the ranges as proposed; keep the LiDAR fixed." Not yet in the data file.

**Specification for entering them, proposed, waiting for his yes** (his words: "the well-founded estimates for the
X1, N1 and T1, shown to me before they enter the data file"):
1. One data file for the robots of type 1, `data/researched/parts_taken_apart.xlsx` (recommended; the alternative is a
   file per robot). A new sheet `Robots`: robot, maker, type, the maker's height and stated mass, sources.
2. A first column `Robot` on Joints, Parts, Boards, Sensors and Constants: the G1's rows as they are, the X1's and
   N1's from this section.
3. Joints: module mass min / mode / max (kg), new: the X1's from AgiBot (S), the N1's from the fit (E), empty for the
   G1 (its JointParts, as now). `Module` (small, large) says which of the G1's insides a joint follows, scaled to its
   mass.
4. JointParts, Shares and SensorElements stay one set for all three ("similar within given ranges"); SensorElements
   gains the X1's YIS320 (as IMU); the X1's phone is a board (ITC), not a sensor.
5. Constants: each robot's own values (stated mass, battery, cable length) per robot; the shared ones (board g/cm²,
   copper share of boards, cross-sections, copper density, insulation) once, for all. The G1's accepted ranges: battery
   pack 2.25 / 2.5 / 2.75 kg, capacity 8.55 / 9 / 9.45 Ah.
6. 01, tests first: every robot has its rows on every sheet; every robot's maker height and stated mass lie inside its
   type's Taxonomy limits (the check that would have caught the T1); module masses positive, min ≤ mode ≤ max; a robot
   not in `Robots` stops 01; the one-robot layout is refused (the old goes entirely).
7. The present file is replaced by the new one, without a copy (its G1 rows are kept, changed only by the two accepted
   ranges; the builder, Claude's scratch one-off, rebuilds it).
8. In the same step: METHODOLOGY.md (check 18), README.md (the data file's row), VERIFICATION.md, HANDOVER.md.
9. Not in this step: the Monte Carlo of 04 (step 5): drawing the robot, equally often, and its mass within the type's
   limits.

**Built, 2026-10-27** ("Yes, build points 1 to 8 as specified, tests first"; checks VERIFICATION.md V50). Entered for
the X1 and N1 exactly the items of the tables above. Two things to bring to Matthias:
- **The robots' own masses** got the G1's ± 1 kg (G1 34 / 35 / 36 kg): X1 32 / 33 / 34 kg (AgiBot's Chinese page
  "33kg"), N1 38 / 39 / 40 kg. The heights in the sheet Robots: G1 1.32 m (U1 "1320x450x200mm"), X1 1.30 m (AgiBot,
  "130 cm", read 2026-10-27, which also gives "31DoF": 29 body joints and 2 grippers), N1 1.245 m.
- **The G1's parts not carried over** to the X1 and N1, as they are not in the tables above: encoders (two per
  joint), XT30 connectors, the main board's heat sink and fan, the hip and waist fans, the knee vapour chambers, the
  lower-leg links, the capacitor buffer boards, the microphones and speaker, a head board. The N1's page states dual
  encoders ("双编码器"); the X1's BOM lists XT30 cables.
2. **The X1's R86-2**: 9 in the BOM list (2024-10-24), 6 in the overall BOM. Nine is taken: 6 + 9 + 10 + 4 = 29, the
   X1's stated 29 body joints.
3. **The X1's head holds a mobile phone** (X1a overall BOM "手机", with a phone holder): its gold, silver, palladium and
   tantalum are not in any sibling project's data. Count it (as a board of E area, ITC) or leave it out?
4. **Optional parts**: the N1's depth camera ("选配") and the T1's LiDAR (T1c, "optional"). Proposed: the standard
   robot, without them.
5. **Masses**: the X1 ≤ 33 kg (X1b) against 35.3 kg in its legs-only model (X1c); the N1 38 / ≈39 / 39.7 kg. Proposed:
   the makers' stated 33 kg and 39 kg as each robot's own mass, from which the method draws.

**Decided, 2026-10-28** (Matthias, on the two points brought to him above: "X1 max 35.3 kg", "Encoders", "XT30
connectors", "Main board cooler", "Yes, download"; then "Yes, build", with A to C as recommended; checks VERIFICATION.md
V52). Read first-hand today: N1a and X1e again, X1c's 58 links summed (35.323 kg), and X1a's two BOMs downloaded again
into Claude's scratch folder (`智元灵犀X1_BOM清单_20241024.xlsx`, 33,806 bytes; `智元灵犀X1总BOM.xlsx`, of the folder
20250307, 18,808 bytes). AgiBot's English page (X1b) refused the connection.

| Robot | The maker's figures for its mass | Entered (kg) |
|---|---|---|
| G1 | "About 35kg" (U1); its model file 35.115 kg (U3) | 34 / 35 / 36, unchanged |
| X1 | "重量 33kg" (X1e); "≤ 33 kg" (X1b, 2026-10-27); its model file's links 35.32 kg (X1c) | 32 / 33 / 35.3 (S, E: the min 1 kg below, as the G1's) |
| N1 | "体重38公斤" in the text, "净重 ≈39 kg" in the table (N1a); its model file 39.7 kg (N1b) | 38 / 39 / 40, unchanged |

| The G1's part | X1 (X1a, read today) | N1 (N1a, read today) | Decided |
|---|---|---|---|
| Encoders, two per joint | the actuators are bought-in units ("套餐件", "执行器"); no encoder named | "双编码器 16bit/14bit" | X1 58 (E, two per joint); N1 46 (S) |
| XT30 (2+2) connectors, two per joint, 1.5 / 3 / 4.5 g | cables "XT30(2+2)连接线": 19 with a plug at both ends, 12 at one, 6 terminating resistors, 2 to the L28: 58 plugs | none named | X1 58 (S, the count; the mass E as the G1's); N1 46 (E, as the G1) |
| Main board heat sink and fan | none; the computer is a bought-in mini PC ("i7-13620H迷你主机", "工控机MiniPC") on a 19 V, 95 W supply ("XW-2290-19-95W") | none; an Intel Core i7-13700H computer | for both: a fan as the G1's, 5 / 10 / 20 g (E); heat pipes and fins 0.055 / 0.12 / 0.19 kg, copper (E, below) |
| Hip and waist fans; knee vapour chambers; lower-leg links; capacitor buffer boards; microphones and speaker; head board | none (its own titanium links, steel shafts and soft-start boards are entered) | none; the head without joints, vision sensors optional ("可自主加载视觉传感器") | not carried over |

**The heat sink of an Intel i7-H mini PC: the sources.** No maker or review found gives the mass of a mini PC's
cooler (searched in English and Chinese; the reviews of the Beelink EQi13 Pro, Geekom GT13 Pro and Lenovo IdeaCentre
Mini with these processors give the whole machine only). Two makers' figures of other coolers for mobile processors,
as context only:

| Code | Source | What it is | Same kind? Representative? | Value |
|---|---|---|---|---|
| FW1 | Framework, Laptop 13 Heatsink and Fan Kit, https://frame.work/products/heatsink-and-fan-kit | maker's specification, a design value | a laptop's cooler; "28W continuous processor load and up to 60W turbo", below the i7-H's class | "Weight: 67.5g" with its fan; "Copper fin pack", "Dual 5mm heat pipes" |
| DY1 | Dynatron, I2, https://www.dynatron.co/product-page/i2 | maker's specification | a 1U server cooler for Intel's mobile socket PGA988 (Core i3 / i5 / i7 mobile); its power not on the page (45 W at retailers, second-hand) | "199g ±5g" with its 50 mm fan; "Copper 1100 Skiving Fins" |
| — | Framework, Laptop 16 heatsink, https://frame.work/products/16-heatsink-amd-ryzen-7040-series | maker's | "up to 45W continuous processor power": the right class | no mass given; left out |

Entered (E): heat pipes and fins 0.055 / 0.12 / 0.19 kg, the two figures less a 10 g fan (57.5 g and 189 g) inside
the range, the mode between them; copper, as both makers' coolers (an upper bound for the copper if a mini PC's fins
are aluminium, point B); the fan 5 / 10 / 20 g as the G1's main board fan, its copper winding from the sheet Shares.

**Points A to C, as recommended:** A, an XT30 counted as the G1's are (one per cable end; whether a mated plug and
socket count once or twice is open for all three robots); B, the heat sink copper; C, the data file written by
Matthias pressing Run on `tools/make_parts_taken_apart.py`.

**Found today, not entered (his decision):** N1a lists a network switch ("交换机") in the N1's chest, not in its
Boards rows; X1a lists XT60 and XT90 plugs and cables on the battery side, 16 brass threaded inserts ("IUT铜螺母",
"黄铜"), a stainless sensor shield ("传感器屏蔽罩") and 4 silicone dampers, none in the X1's rows; a newer BOM list,
`智元灵犀X1_BOM清单_20250108.xlsx` (17,678 bytes), exists in X1a's repository and was not downloaded.

**The battery packs' lower cut, decided 2026-10-28** (Matthias: "Cut at the cells", option 1; checks VERIFICATION.md
V56). The X1's and N1's packs were cut below at 250 Wh/kg cells, but 04 draws the cells from 00's NMC range, 232.5 /
241.5 / 256 Wh/kg (E1.7d): a light pack met heavy cells, and the battery housing, the pack's remainder, fell below
zero (Matthias's run of 04: the X1's in 1.00 % of its draws, the N1's in 0.80 %). The rule stays (a pack weighs at least
its cells and its management board); its numbers follow the model's own cells: the largest energy (voltage × capacity
at their maxima) over 232.5 Wh/kg, plus the largest management board (96 cm2 × 0.84 g/cm2 = 81 g), the board divided
by the lightest robot's mass factor (30 kg over the robot's largest own mass), as pack and cells shrink with the mass
and the board does not.

| Robot | Energy, max | Heaviest cells | Needed | Pack, entered (kg) |
|---|---|---|---|---|
| G1 | 442 Wh | 1.902 kg | 1.999 kg (factor 0.833) | 2.25 / 2.5 / 2.75, unchanged (the teardown's "~2.5kg" ± 10 %) |
| X1 | 384 Wh | 1.652 kg | 1.746 kg (factor 0.850) | **1.75** / 2.2 / 3.3 (was 1.4) |
| N1 | 499 Wh | 2.146 kg | 2.254 kg (factor 0.750) | **2.26** / 2.9 / 3.2 (was 1.9) |

The housing can now reach 0 kg in the most extreme draw, never below; a real pack has a case (the X1's is stainless
steel), so this bound is a physical floor, not a likely mass. The X1's frame still falls below zero in about 0.8 % of
its draws (a separate remainder, not changed here).

### E2.9 What the split into parts is for, and the materials it follows (Matthias, 2026-10-27)

**His words:** "if the total material declartion is a good source, then the slipt into parts is just to get a deeper
look into the robot, so that there is information on where the interesting materials are and the recycling can be
optimized. This means adjust your strategy accordingly." On the materials: "Add the three elements as they are
relevant for the objective of this work".

**The strategy:**
1. Where a good material declaration of the whole robot exists (by the source rules), its totals stand; the parts
   only show where the materials sit.
2. Where none exists, as for robot type 1 now (the workbook's material sheet is labelled Estimate, row 2 note; no G1
   declaration found), the parts are the best basis and the workbook's material sheet is the check.
3. The detail goes into the parts that hold the materials below; the aluminium frame and the plastic shell stay
   coarse.
4. No normalisation: one named part per material takes a declared total's remainder (Matthias's decision which);
   parts that contradict a declared total are reported as a finding.
5. Each part says where it sits and which of the materials below it holds.

**The materials followed:** the workbook's sheet `Critical Raw Materials` (EU 2024 critical and strategic raw
materials): aluminium; copper; neodymium, praseodymium, dysprosium and terbium (in NdFeB); magnesium; titanium;
lithium, nickel, cobalt, manganese and graphite; silicon; boron; gallium and germanium. **Added by Matthias: gold,
silver and palladium**, for the boards and contacts.

### E2.10 The copper share of a G1 stator: searched, not found (2026-10-27)

Asked, Matthias: "Search once more. It is better than just estimate. Encrease this effort in general".

**Searched, and what came of it:**
- **A material declaration of the G1:** none found (Unitree, dealers, RoHS/REACH pages).
- **The workbook's own copper row** (row 8, 3 / 3.8 / 4.5 kg): labelled "Estimate"; its sources S15
  (https://chinabizinsider.com/unitree-g1-teardown-decoding-the-economics-and-engineering-of-the-worlds-best-selling-humanoid-robot/)
  and S38 (https://www.winwinchip.com/blog/detail/humanoid-robot-electronics-components-design-guide-2026/80.html)
  were read and give no copper figure.
- **Chinese sources** (broker reports, copper-industry articles, Zhihu, CSDN): the only per-motor figure is a
  copper-industry article's assumption for Tesla's Optimus, a 750 g frameless motor with "铜含量占总质量的 10%-15%"
  (https://www.copperexpo.com.cn/zh-cn/media/hyzxdt/2026/2/5.html, a repost from the WeChat account 先进铜基材料). The
  article marks its figures as assumptions and contradicts itself (100 to 200 g of winding per motor elsewhere). Not
  used. Zhihu's teardowns of the G1 joint and of AgiBot's R86-3 joint ask for a login.
- **Makers' data:** Kollmorgen's TBM2G frameless motors name their materials but no masses (the PDF answered 403);
  no environmental product declaration of a frameless or servo motor with a copper mass was found.
- **Teardowns and hobby rewinds** weighing a stator's copper and core separately: none found.
- **Munro's actuator video:** Matthias has seen it; it does not give the share.

**Indications without a number:** Munro found "unused winding space" in the G1's motors (T3, through Humanoid.guide),
and Unitree advertises a "Low Copper Consumption Coil" (T2). Both point to the lower side.

**What the physics allows (E):** a slotted stator's copper share = 8.96 s k (1 + e) / (8.96 s k (1 + e) + 7.65 (1 −
s)), with s the slots' share of the lamination's cross-section, k the copper fill of the slots and e the end turns'
extra copper. With s 0.35 / 0.42 / 0.50, k 0.40 / 0.50 / 0.60 (0.55 in a design study:
https://arxiv.org/pdf/2405.00882) and e 0.2 / 0.4 / 0.6, the share is 23 / 37 / 53 %. s and e are estimates without
a source.

**Compared with car motors, from Matthias's own projects** (asked, Matthias: "Can you compare with other motor
compositions like the car electic motors or utility motors in car"). The share is the winding's copper over copper
plus electrical steel:

| Motors | Share | Basis |
|---|---|---|
| Traction motors 2018–2021, all winding types | 23.9 % (5.90 kg winding, 18.77 kg lamination) | **measured** on 46 production machines: Drexler, Kampker, Born et al., *Elektrotech. Inftech.* 142, 312–345 (2025), doi:10.1007/s00502-025-01331-3, as recorded in `RAWCLICVehicleTractionMotor/documentation/METHODOLOGY.md` (§ 4.1) |
| Traction motors 2022–2023, all winding types | 23.3 % (4.51 / 14.81 kg) | the same |
| Traction motors 2018–2021, round wire | about 29 % (7.82 kg; lamination taken as the all-type mean) | the same; approximate |
| Car auxiliary motors: small steppers | 27 / 36 / 45 % | `RAWCLICVehicleElectronics/Data/05_VehicleElectricMotorsWeight.xlsx`, sheet `SmallStepperMotors` (Matthias's workbook; no source named in the sheet) |
| Car auxiliary motors: medium steppers | 30 / 37 / 44 % | the same, sheet `MediumStepperMotors` |
| Car auxiliary DC motors | 25 to 43 %, modes 31 and 36 % | the same; their steel includes the rotor, so the stator's own share is higher |
| Physics (above) | 23 / 37 / 53 % | E |

- **What fits the G1 best:** the traction motors are the same type (permanent-magnet synchronous) and measured, but
  hundreds of times larger, with long stacks; the auxiliary steppers are near the G1's size (150 to 1,000 g against
  the G1's 154 g motor) but a different type, and their shares carry no source.
- **The magnets, for comparison:** the auxiliary sheets give the magnet as "NdFeB & retentive Steel", 10 % (small) and
  19 % (medium) of the motor; the G1's rotor, which T1 calls "magnet", is 28 % of its motor (42.9 of 154.1 g). A rotor
  of magnets on an aluminium carrier needs a steel ring behind them, so the G1's 42.9 g likely holds steel too; this
  points to an NdFeB share of the rotor below the 90 % proposed in E2.8.
- **What the share does to the robot's copper:** the 23 stators weigh about 2.83 kg at the E2.8 modes; their copper
  is 0.65 kg at 23 %, 1.02 kg at 36 %, 1.27 kg at 45 %.

### E2.11 The magnets' grade by each joint's heat: research in progress (2026-10-28)

Matthias: "2. Has to be done properly. Heat has to matter and so the distribution will be different depending on the
joint"; "Joints have no fans, just passive cooling"; "I have seen the Munrow movies. Fans is not a sustainable
solution"; "2 fans ok" (the G1's two hip-area fans and waist fan stay as parts; for the magnets every joint is judged as
passively cooled); "3. grad by heat". Now: one grade class per joint (sheet Joints, base case SH for legs and waist, H
for arms; UH and EH named as scenarios but not drawn). To come: a distribution over grade classes for each kind of
joint, from sources, shown before any number.

**Read so far** (first-hand unless said):

| Source | What it is | What it says | Fits? |
|---|---|---|---|
| Humanoid.guide, "Rare-Earth Magnets in Humanoid Joints", Humanoid Actuation Report, August 2026, https://humanoid.guide/rare-earth-magnets-humanoid-robot-joints/ | an industry report's article, no author | sintered NdFeB; "Higher temperature classes such as SH, UH and EH carry more" heavy rare earths; better heat paths let a designer "drop a temperature class – from UH to SH"; analysts: 35–79 g dysprosium per humanoid; no grade named for any robot, no joint temperatures | general; no robot of type 1 |
| Mainrich International, "Magnet Requirements for Humanoid Robot Actuators", 2026-01-05, updated 2026-09-12, https://www.mainrichinternational.com/resources/articles/magnets-for-humanoid-robot-actuators-complete-guide | a magnet seller's guide (vendor marketing) | "No single industry-standard grade is established here"; no grade by joint, no temperatures | no |
| Aibang Robotics, 2026-05-08, https://www.aibangbots.com/a/8521 | a Chinese industry article | no grade class for joints; high-temperature NdFeB with Tb or Dy for "150~200°C" in the future; Optimus about 3.5 kg NdFeB | no |
| Munro (T3, through Humanoid.guide, second-hand), read again 2026-10-28 | teardown summary | the G1's actuators cooled through their aluminium housings into the structure; the knees a copper heat pipe on the stator, "high duty cycle joints"; two centrifugal fans in the hip area | the G1 |
| T1 slide 42 (China Post Securities, read 2026-10-27) | teardown | "高负载关节（如承受90N·m扭矩的膝关节）" derate when hot | the G1 |
| Search summaries, not read first-hand: Unitree's G1 SDK reports a surface and a winding temperature per motor, no limit published; Honor's marathon robot: the knee about 150 W of heat, the main thermal limit (press); NimbRo (RoboCup, arXiv 1909.02385): knee fans lowered the knee by about 20 °C | — | — | to be read |

**Read since** (2026-10-28, later):

| Source | What it is | What it says | Fits? |
|---|---|---|---|
| OFweek Robot, "拆解宇树 G1 人形机器人：线束集成、热管理以及轻量化设计", 2026-04-07, https://robot.ofweek.com/2026-04/ART-898890-8420-30684472.html (read in the browser) | a trade article on the G1's teardown | "作为主要承重件，膝关节承受的功率负载最大", the knee, the main load-bearing part, carries the largest power load; cooled passively, copper strip into the structure; the waist a small centrifugal fan "快速排除驱动电路产生的热量" (for the drive circuit); the knee's thermal derating "为了保护电机磁钢不因高温退磁", to keep its magnets from demagnetising | the G1; heat by joint, first-hand |
| Mainrich, "Radial Multi-pole Ring Magnets for Robot Joint Motors", 2026-09-02 | a magnet seller (vendor marketing) | no grade by joint, no robot named; "A suffix is a nominal material class, not a guaranteed motor temperature limit" | no |
| Search summaries only: a Mainrich page calls N48SH "the most popular robotics grade" and N45UH for hotter duty; vendor sizing guides (winding limit 130–150 °C, magnet 100–120 °C, case above 80 °C without active cooling); NimbRo knee heat; Honor's marathon robot knee about 150 W | vendor, press | — | not first-hand; context only |

**Searched, not found** (English and Chinese): any maker's magnet grade for a humanoid or robot joint motor (Unitree,
AgiBot, Fourier, CubeMars, T-Motor, MyActuator, Kollmorgen, TQ); any measured magnet or winding temperature by joint;
Unitree publishes a surface and a winding temperature per motor in its SDK, but no limit. The grade classes' rated
temperatures agree across the sources: H 120 °C, SH 150 °C, UH 180 °C, EH 200 °C (RAWCLICVehicleTractionMotor's sheet
PermanentMagnetNdFeB, its own sources).

**What the sources settle, and what they do not:** the order of heat between joints, for the G1 (passively cooled, as
Matthias judges every joint): the knees first (the largest power load, derating to protect the magnets; Munro's
"high duty cycle joints"), then the hips (carrying the body; air from fans in the G1, not counted), the waist (moving
often), the ankles (carrying the robot, small joints in the G1), the arms last. Which grade class a maker puts in which
joint: no source. So the probabilities below are estimates (E).

**Accepted, 2026-10-28** ("Accept as proposed": "Accept the grade distributions by joint as proposed, the classes tied
within a draw. Build it into the builder and 04, tests first"; built, VERIFICATION.md V59): each kind of joint a
discrete distribution over grade classes, drawn in each draw (never blended):

| Joints | H (120 °C) | SH (150 °C) | UH (180 °C) | EH (200 °C) | Basis |
|---|---|---|---|---|---|
| Knees | | 0.3 | 0.5 | 0.2 | the largest load, passive, derating to protect the magnets (OFweek, T1 slide 42, T3) |
| Hips | | 0.5 | 0.4 | 0.1 | carry the body; passive as judged |
| Waist | | 0.6 | 0.4 | | moves often (OFweek); passive as judged |
| Ankles | | 0.6 | 0.4 | | carry the robot; small joints |
| Shoulders | 0.5 | 0.5 | | | hold the arm, low load |
| Elbows, wrists | 0.7 | 0.3 | | | the lowest load |

Within one draw the classes are tied (proposed): one draw decides how hot a maker designs for, and every joint takes the
class at that point of its own distribution, so that a robot built for heat is built for it throughout; drawn
independently by joint, the hot cases would average out and the dysprosium's band would come out too narrow. The
dysprosium of each class from RAWCLICVehicleTractionMotor's own code, as now (H 0.02–0.05, SH 0.04–0.07, UH 0.06–0.09,
EH 0.08–0.10 of the magnet). Replaces the sheet Joints' base class and scenarios (the old goes entirely).

## E1. The element recipes of the 13 shared materials: the sources, 2026-10-26

### What was asked, and how it was done

Matthias, 2026-10-26:
- "Yes, start researching the element recipes of the 13 materials, and show me the sources first";
- "Confirm your work with indepenedet research in the internet";
- "Document in detail the verification with your own internet research".

**This section holds sources, not numbers to enter.** No min / mode / max is proposed here; that waits for Matthias
(his rule 4: the sources first).

**The steps:**
1. **The siblings first** (rule: "has this been solved here?"):
   - `VehicleComposition/Data/14_VehicleMaterialElementDefinitions.xlsx` and `22_MaterialElementComposition.xlsx`;
   - `RAWCLICVehicleTractionMotor/data/raw/10_MaterialElementDefinitions.xlsx`;
   - the battery element files of `RAWCLICVehicleBattery`, read by `RAWCLICStockAndFlow/src/battery_composition.py`;
   - the board metals of `RAWCLICDataCenters/documentation/claude/EVIDENCE.md` §15.
2. **Each material against the web.** Searches by Claude, then each source opened and read on 2026-10-26, unless it
   says "not read". The "Read" column says how:
   - **"Yes"**: the document's full text was read, a PDF through its text layer (macOS PDFKit, a script in the
     session's scratch folder). These are the Teal Sheets, voestalpine, ICAST, Yang et al., Toray, CoorsTek, EPA and
     Astrup.
   - **"Yes (extract)"**: the web page was read through the fetch tool, which returns the passages asked for. These
     are Alro, KEMPER, Total Materia, DIN Media, Wikipedia, Bizzo et al. (PMC) and PJOES.
   - Search results alone are marked as such and are not used for any number.
3. **Grades.** The grades each robot type uses are those of the workbook's sheet `Material Composition per Cat`
   (`data/raw/humanoid_robots_2040_workbook.xlsx`), as placed in `data/researched/shared_lists.xlsx`.

**Two of the 13 shared materials have no recipe, and cannot have one:**
- **"Mixed":** names that hold several unnamed materials.
- **"Not allocated":** kilograms the workbook gives no material for.

They stay as kilograms without elements. The other 11 follow.

---

### E1.1 Aluminium

**The robots use** 6061-T6 and 7075-T6, in all six robot types, always written together ("Al 6061-T6 / 7075-T6"). The
workbook does not say how much of each.

**What the siblings hold:** `VehicleComposition/Data/14_…`, sheets `Wrought6000sLow/High` and `Wrought7000sLow/High`,
rows EN AW-6061 and EN AW-7075, with the minimum and maximum of each element. No source is written in the sheet.

**Independent source:**

| Source | Kind | Read | What it says (wt%) |
|---|---|---|---|
| The Aluminum Association, *International Alloy Designations and Chemical Composition Limits for Wrought Aluminum and Wrought Aluminum Alloys* ("Teal Sheets"), revised December 2025. https://www.aluminum.org/tealsheets (PDF, 5.5 MB) | The registration record of the alloys, the controlling composition for ASTM B209/B221 | Yes, the 6061 and 7075 rows | **6061:** Si 0.40–0.8, Fe ≤0.7, Cu 0.15–0.40, Mn ≤0.15, Mg 0.8–1.2, Cr 0.04–0.35, Zn ≤0.25, Ti ≤0.15, others each ≤0.05, total ≤0.15, Al the remainder. **7075:** Si ≤0.40, Fe ≤0.50, Cu 1.2–2.0, Mn ≤0.30, Mg 2.1–2.9, Cr 0.18–0.28, Zn 5.1–6.1, Ti ≤0.20, others each ≤0.05, total ≤0.15, Al the remainder. |

**Verdict:**
- **Confirmed:** the sibling's minimums and maximums for both alloys equal the Teal Sheets, element by element.
- **Representative:** yes. These are the two alloys the workbook names, and composition limits do not depend on
  the use.
- **Open, Matthias's decision:** the share of 6061 and of 7075 in each robot type, which no source gives. An
  element range spanning both alloys would be an estimate.


#### E1.1b Further aluminium alloys a humanoid robot plausibly uses

Matthias, 2026-10-26, on aluminium: "I asume similar other aluminum alloys are also taken. Therefore the scope should
be expanded and a more mixed approach taken". Researched on 2026-10-27, after "Check the handover and then continue".
The workbook and the project's sources name only 6061-T6 and 7075-T6 (E1.1). **Sources only: no min / mode / max is
proposed here.**

**Where each alloy is used, and who says so:**

| Use in the robot | Alloy | Source | Kind | Read | What it says |
|---|---|---|---|---|---|
| Most main components of a research humanoid | 7075, 6061 | Liao, Q., Zhang, B., Huang, X., Huang, X., Li, Z., Sreenath, K., *Berkeley Humanoid: A Research Platform for Learning-based Control*, 2024. https://arxiv.org/abs/2407.21781 | Research paper (preprint), a humanoid built and run | Yes (extract), full text, §3.3 | "We use 7075 and 6061 aluminum for building most of the main components", with SKD11 steel for the gearbox and linkage |
| Most parts of a research humanoid | 7075 | Ning, Y., Liu, S., Yang, T., Zheng, L., Shi, L., *The NING Humanoid: The Concurrent Design and Development of a Dynamic and Agile Platform*, 2024. https://arxiv.org/abs/2408.01056 | Research paper (preprint), a humanoid built and run | Yes (extract), full text, §III-A | "most parts are manufactured as aluminum 7075 and the key stress components are machined with high stiffness steel" |
| Body plates and legs; the upper body's outer frame | 6061; extrusions of an unnamed grade | Xia, B., Li, B., Lee, J., Scutari, M., Chen, B., *The Duke Humanoid: Design and Control For Energy Efficient Bipedal Locomotion Using Passive Dynamics*, 2024. https://arxiv.org/abs/2409.19795 | Research paper (preprint), a humanoid built and run | Yes (extract), full text, §III-A | "the body plates and legs are custom-machined from aluminum 6061"; the outer frame "built using off-the-shelf aluminum extrusions" |
| Joint and reducer housings, arm links, base castings; covers, shrouds, gripper bodies, encoder housings; joints that carry the motor's heat | A380; ADC12; A360 | CharMax Precision (die caster, Dongguan), *Designing Robot Joint and Reducer Housings for Die Casting*, 14 Oct 2026. https://www.charmaxdiecasting.com/blog/robot-joint-reducer-housing-die-casting/ | Manufacturer's design guide, for robot joints in general, with a commercial interest; names no robot | Yes (extract) | A380 for "Joint and reducer housings" and arm links ("A380 is the default because robot castings are machined heavily"); ADC12 for covers and encoder housings; A360 for joints that are also the motor's heat path. No composition given |
| General structure; high-load links and joint yokes; structural extrusions and rails; welded structures and panels; formed covers; die-cast housings | 6061-T6; 7075; 6082-T6; 5083; 5052; A380, A383/A384, 360/A360 | E-Business International (E-BI, contract manufacturer, Beaverton OR), *Choosing the Right Aluminum for Humanoid Robotics*, 6 Mar 2026. https://e-bi.com/choosing-the-right-aluminum-for-humanoid-robotics/ | Contract manufacturer's guide, written for humanoid robots, with a commercial interest; names no robot maker | Yes (extract) | 6061-T6 "the default for prototypes and general structure"; 7075 for "high-load links, compact joint yokes"; 6082-T6 for "structural extrusions (especially outside the US supply chain), rails, long members"; 5083 for "welded structures, panels"; covers of formed sheet "typically 5052/5xxx"; A380 for "general die cast housings and covers"; A383/A384 for "intricate housings"; 360/A360 for housings exposed to moisture or thermal cycling |

**Searched and not found:**
- **The alloys of the anchor robots** (Unitree G1 and H2, UBTECH Walker S2, AgiBot A2, the electric Atlas). For the G1,
  retailers write "aerospace-grade aluminum alloy" and cite Unitree's user manual V1.5, which was not read. No grade
  is named.
- **Tesla Optimus:** Humanoid.guide (https://humanoid.guide/humanoid-actuator-supplier-landscape/, read) says only
  that Xusheng "machines the joint housings and structural parts". It names no material and cites no source for the
  sentence. Other pages say die-cast aluminium housings; seen only as search summaries.
- **The hydraulic Atlas** (before 2024): 3D-printed aluminium and titanium parts, according to trade press quoting
  Marc Raibert (IEEE Spectrum, 2016). Seen only as search summaries, and no alloy is named.
- **AlSi10Mg and A356:** no source about robots names them. They are left out.
- **The grade of the Duke Humanoid's off-the-shelf extrusions.**

**The composition limits**, read in the registration records (wt%; a single number is a maximum; Al is the
remainder):
- **Wrought:** The Aluminum Association, *International Alloy Designations and Chemical Composition Limits for
  Wrought Aluminum and Wrought Aluminum Alloys* ("Teal Sheets"), revised December 2025.
  https://www.aluminum.org/sites/default/files/2026-01/Teal%20Sheets%20December%202025.pdf. Read: yes, the full text
  of all 42 pages.
- **Castings:** The Aluminum Association, *Designations and Chemical Composition Limits for Aluminum Alloys in the
  Form of Castings and Ingot* ("Pink Sheets"), revised August 2025.
  https://www.aluminum.org/sites/default/files/2025-10/Pink%20Sheets%202025.pdf. Read: yes, the full text of all 25
  pages. The rows are those of die castings (footnote 5: "D = Die Casting").
- **ADC12:** Yamaha Motor, *Japanese Industrial Standards Data – Aluminum alloy die casting*, which reproduces JIS H
  5302:2006, Table 2. https://global.yamaha-motor.com/business/cf/data/jis/aadc.html. Read: yes (extract). The ICAST
  datasheet for JIS H 5302 ADC12 and a Japanese technical bulletin give the same limits, seen only in search summaries.

| Alloy | Si | Fe | Cu | Mn | Mg | Cr | Ni | Zn | Ti | Sn | Pb | Others each / total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6061 | 0.40–0.8 | 0.7 | 0.15–0.40 | 0.15 | 0.8–1.2 | 0.04–0.35 | – | 0.25 | 0.15 | – | – | 0.05 / 0.15 |
| 6082 | 0.7–1.3 | 0.50 | 0.10 | 0.40–1.0 | 0.6–1.2 | 0.25 | – | 0.20 | 0.10 | – | – | 0.05 / 0.15 |
| 7075 | 0.40 | 0.50 | 1.2–2.0 | 0.30 | 2.1–2.9 | 0.18–0.28 | – | 5.1–6.1 | 0.20 (a) | – | – | 0.05 / 0.15 |
| 5052 | 0.25 | 0.40 | 0.10 | 0.10 | 2.2–2.8 | 0.15–0.35 | – | 0.10 | – | – | – | 0.05 / 0.15 |
| 5083 | 0.40 | 0.40 | 0.10 | 0.40–1.0 | 4.0–4.9 | 0.05–0.25 | – | 0.25 | 0.15 | – | – | 0.05 / 0.15 |
| A380.0 (380.0: Fe 2.0) | 7.5–9.5 | 1.3 | 3.0–4.0 | 0.50 | 0.10 | – | 0.50 | 3.0 | – | 0.35 | – | – / 0.50 |
| 383.0 (A383.0: Mg 0.10–0.30) | 9.5–11.5 | 1.3 | 2.0–3.0 | 0.50 | 0.10 | – | 0.30 | 3.0 | – | 0.15 | – | – / 0.50 |
| 384.0 (A384.0: Zn 1.0) | 10.5–12.0 | 1.3 | 3.0–4.5 | 0.50 | 0.10 | – | 0.50 | 3.0 | – | 0.35 | – | – / 0.50 |
| A360.0 (360.0: Fe 2.0) | 9.0–10.0 | 1.3 | 0.6 | 0.35 | 0.40–0.6 | – | 0.50 | 0.50 | – | 0.15 | – | – / 0.25 |
| ADC12 (JIS H 5302:2006) | 9.6–12.0 | 1.3 | 1.5–3.5 | 0.5 | 0.3 | – | 0.5 | 1.0 | 0.30 | 0.2 | 0.2 | not given |

(a) Teal Sheets footnote 10: for extruded and forged 7075, Zr + Ti may be limited to 0.25 % instead, where supplier
and purchaser agree.

The 6061 and 7075 rows are those E1.1 read; the December 2025 edition has not changed them.

**What the further alloys change**, against the 6061 and 7075 of E1.1:
- **Silicon:** the die castings hold 7.5 to 12 %, the wrought alloys at most 1.3 %. How much of the aluminium is die
  cast decides the silicon.
- **Copper and zinc:** A380, 383, 384 and ADC12 hold 1.5 to 4.5 % copper and up to 3 % zinc; 7075 holds 1.2 to 2.0
  % copper and 5.1 to 6.1 % zinc; 6082 and the 5xxx alloys hardly any of either.
- **Magnesium:** up to 4.9 % in 5083, at most 0.10 % in most die castings (0.6 % in A360).
- **Elements only the castings bring:** nickel (up to 0.50 %), tin (up to 0.35 %) and lead (up to 0.2 %, ADC12).
  Zinc, tin and lead are not yet in 01's table of atomic masses.
- **The limits are maxima and ranges, not typical contents.** A recipe needs a mode inside each range, which no
  record gives.

**What drives a robot's range:** the share of each family of alloys, which no source gives.
- **Machined wrought 6xxx:** 6061, 6082.
- **High-strength 7075.**
- **Die-cast housings:** A380, 383/384, ADC12; A360 where the housing carries heat.
- **Formed and welded 5xxx sheet:** 5052, 5083.

The three research humanoids are machined, from 6061 and 7075. The die castings come from manufacturers' guidance
for housings made in quantity, the kind of production 2040 implies. The shares would be estimates (E), for
Matthias's decision. E1.1 already left open the share of 6061 against 7075.

#### E1.1c Proposal: the aluminium recipe of each robot type

Matthias, 2026-10-27, choosing the answer offered: "Yes, propose the aluminium recipe per robot type, min / mode /
max, from the sources of E1.1b, with estimates (E) for the alloy shares, verified on the web with references. Show it
to me before anything is entered."

**Status: agreed by Matthias, 2026-10-27, choosing the answer offered: "I agree with the aluminium recipe as proposed in E1.1c, including its choices." Entered the same day, after E1.1d, on his word "Keep E1.1c as agreed and enter it now, as with the plastics and fibre composites.", in `data/researched/element_recipes.xlsx` (VERIFICATION.md V39). **Its modes are replaced** by E1.1e and E1.1f, entered on 2026-10-27 (V43). Before that, under review: Matthias's rule of the same day ("You should trust standards more than analysis performed at a university") puts the modes of 6061 and ADC12, which rest on university or institute analyses only, and the university analyses among those of 7075 and A380, in question; whether they are set again is his decision.**

**The gaps, checked on the web (2026-10-27).** The registration records give limits; the mode of each element is the
median of the analyses read (the mean where there are two). The analyses give the composition of the metal each study
used.

| Alloy | Source read | Kind | Read | What it says (wt%) |
|---|---|---|---|---|
| 6061 | Kazemi, M., Ghiasvand, A., *Effect of cone angle of cylindrical pin in the SFSW and DFSW on mechanical properties of AA6061-T6 alloy*, J. Mater. Sci.: Mater. Eng., 2021. https://doi.org/10.1186/s40712-021-00131-9, Table 1 | The plate a study used | Yes, the table on the journal's page | Mg 0.81, Si 0.61, Cu 0.29, Fe 0.2, Cr 0.13, Mn 0.03, Zn 0.02, Ti 0.01 |
| 6061 | Ghiasvand, A., Kazemi, M., Mahdipour Jalilian, M., Ahmadi Rashid, H., *Effects of tool offset, pin offset, and alloys position on maximum temperature in dissimilar FSW of AA6061 and AA5086*, same journal, 2020. https://doi.org/10.1186/s40712-020-00118-y, Table 1 | The plate a study used; the same group as above, another lot | Yes, the table | Mg 0.918, Mn 0.083, Cu 0.328, Cr 0.065, Si 0.663, Fe 0.491 |
| 6061 | Summers, P.T., Chen, Y., Rippe, C.M., Allen, B., Mouritz, A.P., Case, S.W., Lattimer, B.Y., *Overview of aluminum alloy mechanical properties during and after fires*, Fire Science Reviews, 2015. https://doi.org/10.1186/s40038-015-0007-5, Table 1 | The plate tested (6061-T651) | Yes, the table | Si 0.66, Fe 0.4, Cu 0.24, Mn 0.07, Mg 0.9, Cr 0.18, Zn 0.02, Ti 0.02 |
| 7075 | National Bureau of Standards (now NIST), *Certificate of Analysis, Standard Reference Material 1259, Aluminum Alloy 7075*, 3 May 1978. https://tsapps.nist.gov/srmext/certificates/1259.pdf | Certified values from six laboratories | Yes, the scanned certificate, rendered and read | Si 0.18, Fe 0.205, Cu 1.60, Mn 0.079, Cr 0.173, Ni 0.063, Zn 5.44, Mg 2.48. Material of 1978: its Cr lies below today's minimum, 0.18 |
| 7075 | Zhou, Z., Zheng, Q., Ding, C., Yu, G., Peng, G., Piao, Z., *Investigation of Two-Dimensional Ultrasonic Surface Burnishing Process on 7075-T6 Aluminum*, Chin. J. Mech. Eng., 2021. https://doi.org/10.1186/s10033-021-00540-z, Table 1 | The plate a study used | Yes, the table | Si 0.36, Fe 0.42, Cu 1.58, Zn 5.8, Ti 0.11, Mn 0.17, Mg 2.45, Cr 0.225. The group's 2022 paper (https://doi.org/10.1186/s10033-022-00828-8) prints the same values and is counted once |
| 7075 | Alba-Galvín, J.J., González-Rovira, L., Botana, F.J., Lekka, M., Andreatta, F., Fedrizzi, L., Bethencourt, M., *Application of Commercial Surface Pretreatments on the Formation of Cerium Conversion Coating (CeCC) over High-Strength Aluminum Alloys 2024-T3 and 7075-T6*, Metals 11, 930, 2021. https://doi.org/10.3390/met11060930, Table 1 | "certified by the metal manufacturer (Castle Metals France)" | Yes, the table and the sentence | Si 0.08, Fe 0.13, Cu 1.7, Mn 0.02, Mg 2.5, Cr 0.19, Zn 5.7, Ti 0.04 |
| A380 | Samuel, A.M., Zedan, Y., Elsharkawi, E.A., Abdelaziz, M.H., Samuel, F.H., *The Role of Mg Content and Aging Treatment on the Tensile and Fatigue Properties of Die-Cast 380 Alloy*, Materials 15, 8844, 2022. https://pmc.ncbi.nlm.nih.gov/articles/PMC9785003/, Tables 2 and 3 | An industrial A380.1 ingot; the method is not stated | Yes (extract) | Si 9.18, Cu 3.22, Fe 1.01, Mg 0.06, Mn 0.15, Zn 2.29, Ti 0.02 |
| A380 | Cao, H., Wang, C., Che, J., Luo, Z., Wang, L., Xiao, L., Wang, J., Hu, T., *Effect of Flow State of Pure Aluminum and A380 Alloy on Porosity of High Pressure Die Castings*, Materials 12, 4219, 2019. https://pmc.ncbi.nlm.nih.gov/articles/PMC6947587/, Table 1 | Measured by X-ray fluorescence | Yes (extract) | Si 9.146, Cu 3.140, Mg 0.104, Fe 0.154, Zn 0.141, Mn 0.103, Ni 0.101, Sn 0.100 |
| A380 | Arconic, certified reference material ALCOA-KC380, sold by LGC Standards. https://www.lgcstandards.com/GB/en/p/ALCOA-KC380, "Analyte Data" | A calibration disk, not production metal; Mg 0.20 lies above A380.0's limit | Yes, the page | Si 9.0, Fe 1.2, Cu 3.6, Mn 0.30, Mg 0.20, Cr 0.060, Ni 0.20, Zn 0.60, Ti 0.070, Sn 0.060, Pb 0.050 |
| ADC12 | Yeom, G.-Y., Lim, H.K., Kim, S.K., Hyun, S.-K., Yoon, Y.-O., *Effects of Mg Enhancement and Heat Treatment on Microstructures and Tensile Properties of Al2Ca-Added ADC12 Die Casting Alloys*, J. Mater. Sci. Technol. 32, 1043-1048, 2016. https://doi.org/10.1016/j.jmst.2016.07.015, Table 1, "ADC12" | The conventional ADC12 die cast in the study | Yes, the table on the journal's page | Si 11.8, Fe 0.93, Cu 2.04, Mn 0.23, Mg 0.24, Zn 0.99, Ni 0.07 |
| ADC12 | Mizutani, Y., Kodera, M., Hosono, K., Niikawa, M., *Development of manufacturing technique for aluminum die-casting due to high quality and cost reduction III*, Research report of the Gifu Prefectural Industrial Technology Research Institute, 2018. https://www.gitec.rd.pref.gifu.lg.jp/files/reports/2018/metal_2018_06.pdf | Measured with a spark emission spectrometer (Shimadzu PDA-7000) | Yes, the PDF's text layer | Si 11.08, Mg 0.29, Cu 2.14, Fe 0.65, Mn 0.19, Zn 0.72 |
| Which parts are die cast | EMP Tech Co., Ltd. (die caster), *Humanoid Robot Die Casting: Building the Skeleton at Scale*, 16 Oct 2026. https://empcasting.com/humanoid-robot-aluminum-die-casting.html | Manufacturer's page, with a commercial interest | Yes (extract) | Joint housings and actuator cases "die cast + CNC"; arm and leg links "CNC 6061/7075, some casting"; the torso frame "extrusion + machining, 6xxx". No share is given |
| Zn, Sn, Pb | IUPAC CIAAW, *Abridged Standard Atomic Weights 2024*. https://www.ciaaw.org/abridged-atomic-weights.htm | The standard | Yes (extract) | Zn 65.38, Sn 118.71, Pb 207.2. The other elements of the alloys agree with 01's table |

**Level 1, each robot type's row 'Aluminum alloys':**

| Robot type | Die cast, % of the row | Wrought | 7075, % of the wrought | 6061 |
|---|---|---|---|---|
| 1 | 0 / 20 / 40 (E) | The remainder | 0 / 32 / 64 (E) | The remainder of the wrought |
| 2 | 0 / 20 / 40 (E) | The remainder | 39 / 68 / 97 (E) | The remainder |
| 3 | 0 / 20 / 40 (E) | The remainder | 22 / 43 / 63 (E) | The remainder |
| 4 | 0 / 20 / 40 (E) | The remainder | 29 / 57 / 84 (E) | The remainder |
| 5 | 0 / 20 / 40 (E) | The remainder | 43 / 71 / 100 (E) | The remainder |
| 6 | 0 / 20 / 40 (E) | The remainder | 26 / 62 / 98 (E) | The remainder |

- **The die-cast share, the same in every robot type (E):**
  - **0 %** is the three research humanoids, which machine all their aluminium (E1.1b).
  - **40 %**, the maximum, is about the part of the aluminium outside the frames. Frames are extruded and machined
    (EMP Tech); EMP and CharMax die cast the housings. The workbook's frame parts weigh 54, 74, 72 and 56 % of the
    aluminium rows of robot types 1 to 4, at the modes. Those of types 2 to 4 also hold titanium or magnesium, so these
    are upper bounds. Robot type 5's frame is about 59 %: its 25 kg less the 12 kg of titanium it names. Outside the
    frames that leaves about 26 to 46 %.
  - **20 %**, the mode, is half of that: half of the housings die cast by 2040.
  - **Robot type 6** is the exception the workbook makes: it gives its frame 22 kg of aluminium, the whole row, yet
    names 7075 housings for its actuators.
- **The 7075 share of the wrought aluminium (E), from the workbook's grade for each part, weighted by the part's mass
  at the mode:**
  - the minimum counts only the parts the workbook makes of 7075 alone;
  - the maximum adds the parts it makes of "6061 / 7075";
  - the mode adds half of those.

  Robot type 1: 0 kg of parts of 7075 alone, 9.1 kg of 6061 or 6063 alone, 16.0 kg of both. Robot type 2: 18.0 /
  1.6 / 26.6. Robot type 3: 9.6 / 15.9 / 18.0. Robot type 4: 12.8 / 6.9 / 24.1. Robot type 5: 30.4 / 0 / 41.0.
  Robot type 6: 13.2 / 1.2 / 36.8. The masses are of whole parts (with their steel, copper and magnets), not of
  their aluminium: an estimate. The workbook's 6063 heat-sink fins (robot types 1 and 3) count as 6061.

**Level 2, the die-cast alloy:** A380 or ADC12, drawn half and half (E). CharMax names both, for different parts;
E-BI and EMP name A380. ADC12 is the Japanese standard's grade, used where die casters follow JIS.

**Level 3, each alloy's elements**, wt%, min / mode / max; aluminium the remainder:

| Element | 6061 | 7075 | A380 | ADC12 |
|---|---|---|---|---|
| Si | 0.40 / 0.66 / 0.8 | 0 / 0.18 / 0.40 | 7.5 / 9.146 / 9.5 | 9.6 / 11.44 / 12.0 |
| Fe | 0 / 0.40 / 0.7 | 0 / 0.205 / 0.50 | 0 / 1.01 / 1.3 | 0 / 0.79 / 1.3 |
| Cu | 0.15 / 0.29 / 0.40 | 1.2 / 1.60 / 2.0 | 3.0 / 3.22 / 4.0 | 1.5 / 2.09 / 3.5 |
| Mn | 0 / 0.07 / 0.15 | 0 / 0.079 / 0.30 | 0 / 0.15 / 0.50 | 0 / 0.21 / 0.5 |
| Mg | 0.8 / 0.90 / 1.2 | 2.1 / 2.48 / 2.9 | 0 / 0.10 / 0.10 (a) | 0 / 0.265 / 0.3 |
| Cr | 0.04 / 0.13 / 0.35 | 0.18 / 0.19 / 0.28 | — | — |
| Zn | 0 / 0.02 / 0.25 | 5.1 / 5.7 / 6.1 | 0 / 0.60 / 3.0 | 0 / 0.855 / 1.0 |
| Ti | 0 / 0.015 / 0.15 | 0 / 0.075 / 0.20 | — | 0 / 0 / 0.30 (E) |
| Ni | — | — | 0 / 0.15 / 0.50 | 0 / 0.07 / 0.5 |
| Sn | — | — | 0 / 0.08 / 0.35 | 0 / 0 / 0.2 (E) |
| Pb | — | — | — | 0 / 0 / 0.2 (E) |

- **The minimum and maximum** are the registered limits (E1.1b); an element with only a maximum may lie anywhere
  below it, so its minimum is 0.
- **The mode** is the median of the analyses above, or the mean where there are two. ADC12's nickel comes from one
  analysis.
- **(E) where no analysis gives the element:** the mode is 0. That covers ADC12's tin, lead and titanium.
- **(a)** A380's median, 0.104, rounds to its limit of 0.10 under the Pink Sheets' rounding rule (footnote 2), so the
  mode is the limit.
- **"Others"** stay in the aluminium: up to 0.15 % in the wrought alloys and 0.50 % in A380. The aluminium is
  overstated by at most that much.
- **Independence:** each element is drawn on its own, though an alloy's elements are not independent of each other;
  no source gives how they vary together.

**The result, % of the aluminium**, from the sandbox (V37): 20,000 draws per robot type; every draw adds up to 1 and
no element falls below zero.

| Robot type | At the modes, with A380 | At the modes, with ADC12 | 95 % of the draws |
|---|---|---|---|
| 1 | Al 93.07, Si 2.23, Zn 1.59, Cu 1.21, Mg 1.14, Fe 0.47 | Al 92.81, Si 2.69, Zn 1.64, Mg 1.18, Cu 0.99, Fe 0.43 | Al 90.6–95.3, Si 0.9–4.1, Zn 0.5–2.9, Cu 0.7–1.7, Mg 0.8–1.6 |
| 2 | Al 90.76, Zn 3.23, Si 2.10, Mg 1.60, Cu 1.59, Fe 0.42 | Al 90.50, Zn 3.28, Si 2.55, Mg 1.63, Cu 1.36, Fe 0.37 | Al 88.7–92.6, Zn 2.2–4.5, Si 0.8–4.0, Cu 1.1–2.0, Mg 1.2–2.1 |
| 3 | Al 92.36, Si 2.19, Zn 2.09, Cu 1.33, Mg 1.28, Fe 0.45 | Al 92.11, Si 2.65, Zn 2.14, Mg 1.32, Cu 1.10, Fe 0.41 | Al 90.4–94.1, Si 0.8–4.0, Zn 1.4–3.0, Cu 0.8–1.8, Mg 1.0–1.7 |
| 4 | Al 91.46, Zn 2.73, Si 2.14, Cu 1.47, Mg 1.46, Fe 0.43 | Al 91.21, Zn 2.78, Si 2.60, Mg 1.49, Cu 1.25, Fe 0.39 | Al 89.4–93.4, Zn 1.8–3.9, Si 0.8–4.0, Cu 1.0–1.9, Mg 1.1–1.9 |
| 5 | Al 90.56, Zn 3.36, Si 2.08, Mg 1.64, Cu 1.62, Fe 0.41 | Al 90.31, Zn 3.41, Si 2.54, Mg 1.67, Cu 1.39, Fe 0.37 | Al 88.5–92.3, Zn 2.3–4.7, Si 0.7–3.9, Cu 1.1–2.1, Mg 1.3–2.2 |
| 6 | Al 91.14, Zn 2.95, Si 2.12, Cu 1.53, Mg 1.52, Fe 0.43 | Al 90.89, Zn 3.00, Si 2.58, Mg 1.56, Cu 1.30, Fe 0.38 | Al 88.8–93.3, Zn 1.7–4.4, Si 0.8–4.0, Cu 1.0–2.0, Mg 1.1–2.1 |

In every robot type, chromium, manganese, titanium, nickel, tin and lead each stay below 0.25 %.

**What entering it would add:**
- in `element_recipes.xlsx`:
  - seven compounds: silicon, magnesium, chromium, zinc, titanium, tin, lead;
  - the four alloy recipes, 'Die-cast aluminium' and one recipe per robot type;
  - six rows in the sheet Rows;
- in 01, the atomic masses of Zn, Sn and Pb.

**Choices in this proposal that are Matthias's:**
- the die-cast share, 0 / 20 / 40 % in every robot type, robot type 6 included;
- the 7075 share taken from the workbook's grades, weighted by whole parts' masses;
- A380 and ADC12 drawn half and half;
- left out of the recipe:
  - 6082, 5052 and 5083 (named only by E-BI);
  - A360 (named by CharMax for joints that carry heat) and 383/384;
  - the 6063 fins, which count as 6061;
- a mode of 0 for ADC12's tin, lead and titanium, which no analysis gives;
- "others" left in the aluminium.

#### E1.1d The car projects' aluminium compositions, checked

Matthias, 2026-10-27, after agreeing to E1.1c: "There are additional material element compositon in the car
composition, chek also there". E1.1 had read only the 6061 and 7075 rows. Read on 2026-10-27; nothing changed, in
those files or here.

**What the car projects hold for aluminium.** No sheet names its source.

| File | Sheets | What they hold |
|---|---|---|
| `VehicleComposition/Data/14_VehicleMaterialElementDefinitions.xlsx` | `castAlAlloys1` | 8 cast alloys (48000, 45000, 319, 356, 357, 43100, 42000, 46200), one value per element |
| same | `castAlAlloys2Low`, `castAlAlloys2High` | 53 European casting alloys (EN AC-21000 to EN AC-48000), a low and a high value per element. Among them are the die-casting grades EN AC-46000 (AlSi9Cu3(Fe), the European counterpart of A380), EN AC-46100 (AlSi11Cu2(Fe), close to ADC12), EN AC-46500, EN AC-47100 and EN AC-43400 |
| same | `Wrought1000sLow` to `Wrought7000sHigh` | Every series of wrought alloy (EN AW), a low and a high value per element: 17 alloys of the 2000s, about 60 of the 5000s, 44 of the 6000s, 29 of the 7000s |
| same | `castAlAlloysDefinition1`, `…Definition2`, `extrusion…`, `forging…`, `sheetAlAlloysDefinition` | The car's mixes, with fixed fractions: castings 48000 and 45000 half and half, or 21000 / 21100 / 41000 / 42000 / 45400 at 0.3 / 0.3 / 0.2 / 0.1 / 0.1; extrusions 6005A, 6008, 6061, 6063, 6082 at 0.2 each; forgings 2017A / 2024 / 2219 / 2618A at 0.2 / 0.3 / 0.3 / 0.2; sheet 5182 / 5083 / 5754 / 5052 at 0.3 / 0.2 / 0.3 / 0.2 |
| `VehicleComposition/Data/15_VehicleComonentMaterialElementDefinitions.xlsx` | `AlSiCuDefinition`, `AlSiMgDefinition`, `Al_5xxx…`, `Al_6xxx…`, `Al_7xxxAlDefinition` | The same alloys, in other mixes of equal fractions. "AlSiCu" is nine casting alloys (EN AC-46000, 46100, 46200, 46500, 43400, 43300, 42100, 42200, 47100); "7xxx" is 7003, 7020, 7021, 7075, 7108 |
| `VehicleComposition/Data/34_MaterialElementComponentComposition.xlsx` (and `22_…`) | `materialAlSiCucomposition` and four more | One min, mean and max per element for each mix: the lowest low, an average over the mix and the highest high. Not an analysis |
| `RAWCLICVehicleTractionMotor/data/raw/10_MaterialElementDefinitions.xlsx` (the same sheet in `RAWCLICVehicleElectronics/Data/`) | `CastAl` | A380.0, A380.1, A380.2, A383.0, A383.1, A360.0, A360.1, A360.2, minimum and maximum as fractions. The motors' cast housings (TractionMotor's SOURCE_AUDIT: "cast aluminium") |

**Checked against the registration records of E1.1b:**
- **Wrought:** the car file's 6061, 6063, 6005A, 6082, 5052, 5083 and 7075 equal the Teal Sheets, element by element.
  6005A's condition Mn + Cr 0.12–0.50 cannot be written in two columns and is missing.
- **Castings:** the traction-motor project's A380.0, A383.0 (with Mg 0.10–0.30) and A360.0 equal the Pink Sheets,
  element by element.
- **Not checked:** the 53 EN AC alloys. Their standard, EN 1706, was not read (paywalled, E1.13), so their limits rest
  on the car file alone.

**What this means for E1.1c:**
- **The limits:** a sibling project confirms independently those of the four alloys in E1.1c (6061, 7075, A380; ADC12
  has no car row). Nothing in E1.1c is contradicted.
- **No typical contents:** the car files hold limits only, so E1.1c's modes, from the analyses, stand alone.
- **Alloys E1.1c leaves out:**
  - **A383 and A360:** their limits are now in two sources (Pink Sheets, TractionMotor). Both are named for robots
    (E1.1b: E-BI A383/A384, CharMax and E-BI A360). They were left out by Matthias's agreed choice.
  - **The European die-casting grades** EN AC-46000 and EN AC-46100: the same family as A380 and ADC12. No source
    about robots names them; CharMax mentions "EN AC-46000 and AlSi9Cu3 grades" only in its description of the
    Al-Si family. Their limits are unverified.
  - **The car's mixes of extrusions** (6005A, 6008, 6061, 6063, 6082) **and sheet** (5182, 5083, 5754, 5052): car
    choices with no source given. Robot sources name 6061 (all), 6082 (E-BI) and 5052/5083 (E-BI) only (rule 8.1:
    a value for one kind of thing comes from sources about that kind).
  - **Forgings of the 2000s:** no source about robots names them.

**For the materials still to come**, the same file holds:
- **magnesium** AM60A-F and AZ91C-E (already E1.2: the robots use AZ91D and AM60B);
- **cast irons** GG10 to GG30, GGG40 and GGG60;
- **mild steels** AISI 1008 to 1020, S275 and S355;
- **car-body steels** (Docol and others; HSS, UHSS, AHSS);
- **circuit boards** (four kinds), **cables**, and **magnets** NdFeB1 to 3 (already E1.6b).

Car-body steels and cast iron are not named for robots (E1.4b).

#### E1.1e The modes of E1.1c set again by Matthias's rule

Matthias, 2026-10-27: "You should trust standards more than analysis performed at a university. They do NOT know quality measures for analytical procedures. This is different with comercial labs", then: "Yes, redo the modes of E1.2c and of the entered E1.1c by my rule: first search for commercial values (certificates, certified reference materials, producers' nominal compositions) for every alloy, read first-hand with references; where none exists, the middle of the standard's range (E)."

**Status: agreed. Matthias, 2026-10-27, choosing the answer offered: "I agree with the modes of E1.1e and E1.2d, including their choices." Entered the same day, with ADC12 from its combined analyses (E1.1f): Matthias, 2026-10-27: "Yes, enter both: rewrite the aluminium modes as in E1.1e, and enter the magnesium recipe of E1.2c (its AM share, AM60B or AM50A half and half, robot type 3 as AZ91D alone) with the modes of E1.2d. Tests first, as before, and the documents." (VERIFICATION.md V43).**

**The order each mode follows:**
1. **A standard's nominal composition.** SAE's Aerospace Material Specifications state it in their titles.
2. **Commercial analyses:** certified reference materials, and producers' certificates of analysis. Each independent
   material counts once, as the mean of its lots; the mode is the median over the materials.
3. **A producer's nominal composition.**
4. **Otherwise the middle of the standard's range (E),** from 0 to the maximum where only a maximum is given.

A value above the standard's maximum takes the maximum. The minimum and maximum stay the registered limits. University
analyses are no longer used for any number (memory rule "standards over academic analyses").

**The sources** (all read first-hand on 2026-10-27):

| Source | Kind | Read | What it gives (wt%) |
|---|---|---|---|
| SAE International, AMS4027P, *Aluminum Alloy, Sheet and Plate 1.0Mg - 0.60Si - 0.28Cu - 0.20Cr (6061; -T6 Sheet, -T651 Plate)*, revised 29 April 2022, current. https://saemobilus.sae.org/content/AMS4027P | Standard (AMS D Nonferrous Alloys Committee) | Yes, the page | 6061 nominal: Mg 1.0, Si 0.60, Cu 0.28, Cr 0.20 |
| SAE International, AMS4045N, *Aluminum Alloy Sheet and Plate, 5.6Zn - 2.5Mg - 1.6Cu - 0.23Cr, 7075 (-T6 Sheet, -T651 Plate)*, revised 21 September 2026, current. https://saemobilus.sae.org/content/AMS4045N | Standard | Yes, the page | 7075 nominal: Zn 5.6, Mg 2.5, Cu 1.6, Cr 0.23 |
| Arconic, SS-6061, certified reference material for wrought alloy analysis. https://crms.arconic.com/hu/p/ss-6061 | Commercial; lab registered to ISO 9001 | Yes, the lot tables in the browser | Lots MM (2018), NS (2021), RX = RY (2026): Mg 1.02–1.03, Si 0.640–0.653, Fe 0.340–0.366, Cu 0.299–0.300, Cr 0.226–0.231, Zn 0.081, Mn 0.050–0.053, Ti 0.038–0.041 |
| Arconic, SS-7075. https://crms.arconic.com/hu/p/ss-7075 | As above | Yes | Lots HR (2016), HU (2018), JD (2020), JU = JW, JX = JY, JZ = KA (2026): Zn 5.73–5.82, Mg 2.56–2.60, Cu 1.57–1.61, Cr 0.203–0.205, Si 0.159–0.164, Fe 0.139–0.158, Mn 0.079–0.082, Ti 0.038–0.045 |
| NIST SRM 1259, *Aluminum Alloy 7075*, 1978 (E1.1c) | Certified, six laboratories | Yes | Si 0.18, Fe 0.205, Mn 0.079 (and the elements the standard sets) |
| Castle Metals France, certificate, in Alba-Galvín et al. 2021 (E1.1c) | A producer's certificate | Yes | Si 0.08, Fe 0.13, Mn 0.02, Ti 0.04 |
| Arconic, KC-380, certified reference material for casting alloy analysis. https://crms.arconic.com/hu/p/kc-380 | Commercial | Yes | Lots BD, BE (2023): Si 9.07, Fe 1.23–1.24, Cu 3.59, Mn 0.30, Mg 0.20, Ni 0.20, Zn 0.60, Sn 0.06 |
| Arconic, SS-380. https://crms.arconic.com/hu/p/ss-380 | Commercial | Yes | Lots EJ (2014), FH, FJ = FK, FL = FM (2025): Si 8.87–8.89, Fe 0.90–0.93, Cu 3.59, Mn 0.40–0.41, Mg 0.20, Ni 0.30, Zn 0.35, Sn 0.0002–0.0006 |
| NIST, *Certificate of Analysis, SRM 1256b, Aluminum Alloy 380*, 4 April 2006. https://tsapps.nist.gov/srmext/certificates/1256B.pdf | Certified (NIST and collaborating laboratories) | Yes, the PDF's text layer | Si 9.362, Fe 0.865, Cu 3.478, Mn 0.3857, Mg 0.0637, Ni 0.4135, Zn 1.011, Pb 0.1075; Sn 0.0091 (reference value) |

**Not used:**
- **Arconic SS-383** (https://crms.arconic.com/hu/p/ss-383; lots of 2019 and 2026). It is AA 383, not ADC12: its Zn
  2.5 and Pb 0.21–0.22 lie above ADC12's limits of 1.0 and 0.2.
- **No commercial value was found for ADC12:** no reference material, and no producer's page with a typical
  composition.
- **The university analyses of E1.1c** (Kazemi & Ghiasvand, Ghiasvand et al., Summers et al., Zhou et al., Samuel
  et al., Cao et al.) and the research institutes' ADC12 analyses (Yeom et al., Mizutani et al.).

**The modes**, wt% (min / mode / max; the limits unchanged), with where each comes from:

| Element | 6061 | 7075 | A380 | ADC12 |
|---|---|---|---|---|
| Si | 0.40 / **0.60** / 0.8 standard | 0 / **0.160** / 0.40 commercial (3) | 7.5 / **9.07** / 9.5 commercial (3) | 9.6 / **10.8** / 12.0 middle (E) |
| Fe | 0 / **0.354** / 0.7 commercial (1) | 0 / **0.148** / 0.50 commercial (3) | 0 / **0.923** / 1.3 commercial (3) | 0 / **0.65** / 1.3 middle (E) |
| Cu | 0.15 / **0.28** / 0.40 standard | 1.2 / **1.6** / 2.0 standard | 3.0 / **3.59** / 4.0 commercial (3) | 1.5 / **2.5** / 3.5 middle (E) |
| Mn | 0 / **0.051** / 0.15 commercial (1) | 0 / **0.079** / 0.30 commercial (3) | 0 / **0.386** / 0.50 commercial (3) | 0 / **0.25** / 0.5 middle (E) |
| Mg | 0.8 / **1.0** / 1.2 standard | 2.1 / **2.5** / 2.9 standard | 0 / **0.10** / 0.10 commercial (3), median 0.20 above the limit: the limit | 0 / **0.15** / 0.3 middle (E) |
| Cr | 0.04 / **0.20** / 0.35 standard | 0.18 / **0.23** / 0.28 standard | — | — |
| Zn | 0 / **0.081** / 0.25 commercial (1) | 5.1 / **5.6** / 6.1 standard | 0 / **0.603** / 3.0 commercial (3) | 0 / **0.5** / 1.0 middle (E) |
| Ti | 0 / **0.040** / 0.15 commercial (1) | 0 / **0.041** / 0.20 commercial (2) | — | 0 / **0.15** / 0.30 middle (E) |
| Ni | — | — | 0 / **0.298** / 0.50 commercial (3) | 0 / **0.25** / 0.5 middle (E) |
| Sn | — | — | 0 / **0.0091** / 0.35 commercial (3) | 0 / **0.10** / 0.2 middle (E) |
| Pb | — | — | — | 0 / **0.10** / 0.2 middle (E) |

The shares of E1.1c (die cast, 7075) are unchanged.

**The result, % of each robot type's aluminium at the modes** (V42; in brackets E1.1c as entered):

| Robot type | With A380 | With ADC12 |
|---|---|---|
| 1 | Al 92.94 (93.07), Si 2.18, Zn 1.60, Cu 1.28, Mg 1.20, Fe 0.41 | Al 92.84 (92.81), Si 2.53, Zn 1.58, Mg 1.21, Cu 1.06 |
| 2 | Al 90.70 (90.76), Zn 3.19, Si 2.05, Cu 1.66, Mg 1.64 | Al 90.61 (90.50), Zn 3.17, Si 2.40, Mg 1.65, Cu 1.44 |
| 3 | Al 92.25 (92.36), Si 2.14, Zn 2.08, Cu 1.40, Mg 1.34 | Al 92.16 (92.11), Si 2.49, Zn 2.06, Mg 1.35, Cu 1.18 |
| 4 | Al 91.38 (91.46), Zn 2.70, Si 2.09, Cu 1.54, Mg 1.50 | Al 91.29 (91.21), Zn 2.68, Si 2.44, Mg 1.51, Cu 1.33 |
| 5 | Al 90.52 (90.56), Zn 3.32, Si 2.04, Cu 1.69, Mg 1.67 | Al 90.42 (90.31), Zn 3.30, Si 2.39, Mg 1.68, Cu 1.47 |
| 6 | Al 91.07 (91.14), Zn 2.92, Si 2.08, Cu 1.60, Mg 1.56 | Al 90.98 (90.89), Zn 2.90, Si 2.42, Mg 1.57, Cu 1.38 |

The main elements move by about 0.1 percentage point. The trace elements move more: ADC12's nickel, tin and lead
now sit in the middle of their ranges (0.25, 0.10, 0.10 %) instead of near 0.

**Choices that are Matthias's:**
- ADC12 entirely from the middle of the JIS ranges, its nickel, tin and lead included;
- one value per independent reference material, the median over materials;
- A380's magnesium at its limit of 0.10, although all three reference materials hold more or less than that (0.20,
  0.20, 0.064);
- the reference materials' elements outside a grade's registered list (such as nickel at 0.05 in SS-6061) left in
  the aluminium.

#### E1.1f ADC12 from its combined analyses (Matthias's second rule)

Matthias, 2026-10-27: "If the elemental analysis of a material is only based on university analysis, then combine them and use respective large uncertainties. Except one of the analyis is for obvious reasons wrong". It came while E1.1e was being entered, before anything was written.

**What it changes:** ADC12 alone; no standard nominal, reference material or producer value exists for it (E1.1e).
- **The modes** of Si, Fe, Cu, Mn, Mg and Zn are now the mean of the two research institutes' analyses: Yeom et al.
  2016 (KITECH) and Mizutani et al. 2018 (Gifu Prefectural Industrial Technology Research Institute), both read in
  E1.1c.
- **Ni** comes from Yeom et al. alone.
- **Sn, Pb and Ti** stay the middle of the JIS ranges: no analysis gives them.
- **Neither analysis is obviously wrong:** every value lies within the JIS limits.
- **The uncertainty** is the JIS full range (minimum and maximum unchanged), labelled E.

| Element | ADC12, wt% (min / mode / max) | Instead of (E1.1e) |
|---|---|---|
| Si | 9.6 / **11.44** / 12.0 | 10.8 |
| Fe | 0 / **0.79** / 1.3 | 0.65 |
| Cu | 1.5 / **2.09** / 3.5 | 2.5 |
| Mn | 0 / **0.21** / 0.5 | 0.25 |
| Mg | 0 / **0.265** / 0.3 | 0.15 |
| Zn | 0 / **0.855** / 1.0 | 0.5 |
| Ni | 0 / **0.07** / 0.5 | 0.25 |
| Sn, Pb, Ti | 0 / **0.10, 0.10, 0.15** / 0.2, 0.2, 0.30 | unchanged |

**% of each robot type's aluminium at the modes, with ADC12** (E1.1e's in brackets): 1: Al 92.72 (92.84); 2: 90.48
(90.61); 3: 92.03 (92.16); 4: 91.17 (91.29); 5: 90.30 (90.42); 6: 90.86 (90.98). With A380, unchanged.

**Status: entered** with E1.1e, on Matthias, 2026-10-27's word (VERIFICATION.md V43).
---

### E1.2 Magnesium

**The robots use:**
- robot types 2, 4 and 6: AZ91D / AM60;
- robot type 3: AZ91D.

**What the siblings hold:** `VehicleComposition/Data/14_…`, sheet `magnesiumAlloys`:
- AM60A-F: Mg 93, Al 6, Mn 0.4, Zn 0.1 (means);
- AZ91C-E: Mg 91, Al 8.5, Mn 0.2, Zn 0.6 (means).

Source written: "ASTM International, B07, 2008". These are the **sand-cast** grade AZ91C and the older AM60A, not the
die-cast grades AZ91D and AM60B the robots use.

**Independent sources:**

| Source | Kind | Read | What it says (wt%) |
|---|---|---|---|
| ICAST Alloys LLP, *ANSI/AA AZ91D*, datasheet (2025). https://icastllp.com/material_db_pdf/ANSI%20AA%20AZ91D.pdf | A casting supplier's datasheet, citing ASTM B94/B275/B951. Second-hand, with the supplier's own disclaimer | Yes | **AZ91D:** Al 8.3–9.7, Zn 0.35–1.00, Mn 0.15–0.50, Si ≤0.10, Fe ≤0.005, Cu ≤0.030, Ni ≤0.002, other ≤0.02, Mg the remainder. |
| ICAST Alloys LLP, *ASTM B94 AM60B*, datasheet. https://icastllp.com/material_db_pdf/ASTM%20B94%20AM60B.pdf | As above | Yes | **AM60B:** Al 5.5–6.5, Mn 0.24–0.60, Zn ≤0.22, Si ≤0.10, Fe ≤0.005, Cu ≤0.010, Ni ≤0.002, other ≤0.02, Mg the remainder. |
| US patent 5,055,254 (search result only) | Patent | No | Older ASTM impurity limits for AZ91; not used. |

**Verdict:**
- **Al and Mn agree** with the sibling's means.
- **The grades differ:** the robots' AZ91D has Al 8.3–9.7 (middle 9.0) against AZ91C's mean of 8.5, and much
  lower impurities.
- **Not confirmed first-hand:** the standard ASTM B94 itself was not read (paywalled). Its numbers come through a
  supplier.


#### E1.2b Magnesium: what the robots use, and the sources

Matthias, 2026-10-26, on magnesium: "Silar as for the aluminum alloy, but I asume here the selection is more limited".
On 2026-10-27: "Go on to magnesium: show me what the robots use and the sources first, verified on the web with
references, and check the car composition files too." **Sources only: no min / mode / max is proposed here.**

**What the workbook says** (`data/raw/humanoid_robots_2040_workbook.xlsx`):

| Robot type | Row, kg (min / mode / max) | Grade | The parts that name magnesium |
|---|---|---|---|
| 2 | 4.0 / 6.0 / 9.0 | AZ91D / AM60 | Outer shell and body panels ("Magnesium alloy (AZ91D / AM60) & PC-ABS / PA66-GF"); heat sinks ("Al 6061 / AZ91D Mg") |
| 3 | 2.0 / 4.0 / 6.0 | AZ91D | Main structural frame ("Al 6061-T6 / 7075-T6 & Magnesium AZ91D") |
| 4 | 5.0 / 6.2 / 8.0 | AZ91D / AM60 | Frame ("& Magnesium AZ91D / AM60"); controller housing ("Al & AZ91D Mg") |
| 6 | 3.0 / 5.0 / 7.0 | AZ91D / AM60 | No part names it |

Robot types 1 and 5 have none. The category reports expect more magnesium by 2040, "for lightweight housings and
supports" (`00_overview_categories_market_shares_2040.md`).

**Where magnesium is used in robots, and who says so:**

| Use | Alloy | Source | Kind | Read | What it says |
|---|---|---|---|---|---|
| Leg structure of a research humanoid | AZ91 | Yousefi-Koma, A. et al., *SURENA IV: Towards A Cost-effective Full-size Humanoid Robot for Real-world Scenarios*, 2021. https://arxiv.org/abs/2108.13515 | Research paper (preprint), a humanoid built and run | Yes (extract), full text, §II-B | "The structural parts are made of an magnesium alloy (AZ91)", optimised by FEM; the arms aluminium and carbon fibre (§II-D) |
| The body of Honda's ASIMO; a second, 7 kg humanoid | Not named | Byko, M., *Personification: The Materials Science and Engineering of Humanoid Robots*, JOM, November 2003. https://www.tms.org/pubs/journals/JOM/0311/Byko-0311.html | Society journal, feature by its managing editor | Yes, the page | "With a body of lightweight magnesium coated with a plastic resin"; the second robot "Made of magnesium, it is shorter than ASIMO (half a meter), weighs less (7 kg)" |
| AgiBot's humanoids (A3, X2) | Not named | Richards, J., TechRadar, 7 July 2026, at AgiBot's event. https://www.techradar.com/tech/robots-should-understand-you-talk-to-you-and-work-for-you-chinese-robotics-company-agibot-is-heralding-a-robot-revolution-i-met-the-humanoids-up-close | Journalist's report; second-hand | Yes, the page | "The units are made mainly of magnesium alloy, with titanium reinforcements at pressure points to ensure rigidity" |
| Robot joint, gearbox, servo and controller housings, cobot joint modules | AZ91D, AM60B, AM50A (not assigned to parts) | Magnecast (Shenzhen Shixin Metal Products Co., Ltd.), *Custom Magnesium Die Cast Components*, © 2026. https://magnecast.com/magnesium-die-casting/components/ | Die caster's page, with a commercial interest; names no robot maker | Yes (extract) | Lists the housings; "Tie AZ91D, AM60B, AM50A, HPDC, tooling, CNC machining" to each part's release |
| Joints of Tesla Optimus and UBTECH Walker X | AZ91D, ZM5 | ZheJiang Dongrun Casting Industry Co., Ltd., *Die Casting Applications in Robotics & Automation*, 10 Feb 2026. https://www.dongruncasting.com/news/Die-Casting-Applications-in-Robotics-Automation.html | Die caster's news page; promotional; **cites no source** | Yes (extract) | "Tesla's Optimus humanoid robot uses AZ91D magnesium alloy for joint components"; "AZ91D, ZM5 (used in Tesla Optimus and UBTECH Walker X)". Not used for any number |
| Humanoid parts, joints and actuators | Not named | Shanghai Metals Market, *Lightweight + High Performance Magnesium Alloys Lead the New Track in Automotive and Robotics Industries*, 31 Oct 2025. https://news.metal.com/newscontent/103599630/ | Market news | Yes (extract) | Lizhong to supply "high-performance magnesium alloy materials and lightweight parts" for Vision Intelligence's humanoids; Yongmaotai's magnesium actuators and joints "still in the framework stage" |

**Searched and not found:**
- A grade named by the anchor robots' makers (Unitree, UBTECH, AgiBot, Boston Dynamics) or by Tesla.
- A wrought magnesium alloy (sheet or extrusion, such as AZ31B) named for a robot. No source about robots names
  one; every grade named is a casting alloy.
- AE44 and the rare-earth alloys: no source about robots names them.

**The composition limits** (wt%; a single number is a maximum; Mg is the remainder):
- **ASTM B93 (ingot) and B94 (die castings):** not read. ASTM sells them. A copy of B93 from 2004 on a university
  server was found and not used.
- **The producers' limits, compiled by TMS:** Materials Technology@TMS, *Magnesium Die Casting Alloy Compositions*,
  2007. https://www.tms.org/Communities/FTAttachments/DiecastingCompositionsREV.pdf. A society's compilation of
  producers' figures. Read: yes, the pages rendered and read as images, since the text layer scrambles the table.
- **The casting limits (B94), through a supplier:** ICAST (E1.2), read before.

| Alloy | Source | Al | Zn | Mn | Si | Cu | Ni | Fe | Others |
|---|---|---|---|---|---|---|---|---|---|
| AZ91D | Dead Sea Magnesium, AVISMA, Rima (TMS) | 8.5–9.5 | 0.45–0.90 | 0.17–0.40 | 0.05 | 0.025 | 0.001 | 0.004 | 0.01 each |
| AZ91D | ICAST, ASTM B94 castings (E1.2) | 8.3–9.7 | 0.35–1.00 | 0.15–0.50 | 0.10 | 0.030 | 0.002 | 0.005 | 0.02 |
| AZ91D, nominal | Magnesium Elektron; Kutz (ed.), *Handbook of Materials Selection*, 2002 (TMS) | 9; 9 | 0.5; 0.7 | 0.3; 0.26 | | | | | |
| AM60B | Dead Sea Magnesium, AVISMA, Rima (TMS) | 5.6–6.4 | 0.20 | 0.26–0.50 | 0.05 | 0.008 | 0.001 | 0.004 | 0.01 each (AVISMA: Be 0.0005–0.0015) |
| AM60B | ICAST, ASTM B94 castings (E1.2) | 5.5–6.5 | 0.22 | 0.24–0.60 | 0.10 | 0.010 | 0.002 | 0.005 | 0.02 |
| AM60B, nominal | Magnesium Elektron; Kutz 2002 (TMS) | 6; 6.9 (a) | –; 0.22 | 0.5; 0.42 | | | | | |
| AM50A | Dead Sea Magnesium, AVISMA, Rima (TMS) | 4.5–5.3 | 0.20 | 0.28–0.50 | 0.05 | 0.008 | 0.001 | 0.004 | 0.01 each |
| AM50A, nominal | Magnesium Elektron; Kutz 2002 (TMS) | 5; 4.9 | –; 0.22 | 0.5; 0.32 | | | | | |

(a) 6.9 lies above AM60B's range of 5.6–6.4: an error in the compilation or in the handbook.

- **The two sets of limits agree:** the ingot limits (B93) are narrower than the castings' (B94) because a casting
  is allowed what the melt takes up or loses.
- **ZM5:** Dongrun's Chinese grade (GB/T 1177). Its limits were not read, and no other source names it.

**The car composition files, checked:**
- `VehicleComposition/Data/14_…` and `15_…`, sheet `magnesiumAlloys`, hold two alloys, each with one mean per element
  ("ASTM International, B07, 2008"), mixed half and half (`magnesiumDefinition`):
  - AM60A-F: Mg 93, Al 6, Mn 0.4, Si 0.01, "Co" 0.01, Zn 0.1, Ni 0.02;
  - AZ91C-E: Mg 91, Al 8.5, Mn 0.2, Si 0.015, "Co" 0.04, Zn 0.6, Ni 0.01.
- `34_…` (`materialsMgAlloyscomposition`) holds their average.
- `31_ComponentMaterial.xlsx` and `2_VehicleCompositionNewData.xlsx` hold magnesium per car component and segment, not
  compositions.
- No other project in the GitHub folder holds a magnesium composition.
- **Two faults in the car file, reported, not changed:**
  - **AZ91C-E's means add up to 100.365 %**, so Mg is not the remainder.
  - **The column "Co" (cobalt)** is probably copper: the magnesium standards set a limit for copper and none for
    cobalt.
- **The grades are not the robots':** AZ91C is a sand-casting grade and AM60A the older AM60. The robots name the
  die-casting grades AZ91D and AM60B (E1.2).

**For Matthias, before any proposal:**
1. **Which alloys:** the workbook names AZ91D and AM60 (AM60B); Magnecast adds AM50A; ZM5 rests on one promotional
   page. No source about robots names a wrought magnesium alloy, which agrees with his "the selection is more
   limited".
2. **AgiBot:** TechRadar's "made mainly of magnesium alloy" stands against the workbook's robot type 4 (anchor AgiBot
   A2): 6.2 kg of magnesium and 28.5 kg of aluminium at the modes. It is a journalist's sentence, about the A3 and
   X2 rather than the A2. The workbook is Matthias's.
3. **Typical contents:** the sources give limits and a few nominal values; the modes would come from analyses, as
   for aluminium.

#### E1.2c Proposal: the magnesium recipe of each robot type

Matthias, 2026-10-27, choosing the answer offered: "Yes, propose the magnesium recipe per robot type, min / mode /
max, from the sources of E1.2b, with AZ91D, AM60B and AM50A, estimates (E) for the alloy shares, and the modes from
analyses verified on the web with references. Show it to me before anything is entered."

**Status: entered, with the modes of E1.2d and E1.2e (VERIFICATION.md V43).** Before that: on hold. Matthias, 2026-10-27: "You should trust standards more than analysis performed at a university. They do NOT know quality measures for analytical procedures. This is different with comercial labs". The modes below rest on university analyses (the AM50 certificate of Jesus et al. excepted) and are to be set again by his rule; nothing is entered.

**The limits:** ASTM B94 for die castings, through ICAST's datasheets. The robots' parts are castings; the producers'
ingot limits of E1.2b are narrower.
- https://icastllp.com/material_db_pdf/ANSI%20AA%20AZ91D.pdf
- https://icastllp.com/material_db_pdf/ASTM%20B94%20AM60B.pdf
- https://icastllp.com/material_db_pdf/ASTM%20B94%20AM50A.pdf

Read: yes, the text layer of each PDF, 2026-10-27.

**The analyses read for the modes:**

| Alloy | Source | Kind | Read | What it says (wt%) |
|---|---|---|---|---|
| AZ91D | Cui, L., Liu, Z., Hu, P., Shao, J., Li, X., Du, C., Jiang, B., *The Corrosion Behavior of AZ91D Magnesium Alloy in Simulated Haze Aqueous Solution*, Materials 11, 970, 2018. https://doi.org/10.3390/ma11060970, Table 1 | As-cast AZ91D used in a study; method not stated | Yes (extract) | Al 8.56, Zn 0.54, Mn 0.22, Si 0.054; Ni, Fe and Cu each below 0.005 |
| AZ91D | Dini, H., *As-cast AZ91D Magnesium Alloy Properties: Effects of Microstructure and Temperature*, doctoral thesis, Jönköping University, 2017. https://www.diva-portal.org/smash/get/diva2:1165186/FULLTEXT01.pdf, Table 3 | Commercial ingots; spark OES, the average of three analyses | Yes, the PDF's text layer | Al 8.5, Zn 0.67, Mn 0.25, Fe 0.0023, Ni 0.0017, Cu 0.021, Si 0.017 |
| AZ91 | Wang, C., Deng, K., Bai, Y., *Microstructure, and Mechanical and Wear Properties of Grp/AZ91 Magnesium Matrix Composites*, Materials 12, 1190, 2019. https://doi.org/10.3390/ma12071190, Table 1 | The matrix alloy of a study; not said to be AZ91D, method not stated | Yes (extract) | Al 9.35, Zn 0.7, Mn 0.25, Si 0.02 |
| AM60 | Zheng, T., Hu, Y., Meng, W., Tang, A., Pan, F., *Corrosion and Residual Strength Analysis of High Pressure Die Casting AM Series Mg Alloys*, Materials 12, 2624, 2019. https://doi.org/10.3390/ma12162624, Table 1 | High-pressure die cast; ICP-OES | Yes (extract) | Al 5.71, Zn 0.15, Mn 0.27; no trace elements |
| AM50 | Yang, M., Liu, X., Xing, L., Chen, Z., *Corrosion and Mechanical Behavior of the As-Cast and Solid-Solution-Treated AM50 Magnesium Alloy in Different Media*, Materials 16, 2406, 2023. https://doi.org/10.3390/ma16062406, Table 1 | As-cast; ICP-AES | Yes (extract) | Al 4.8687, Mn 0.2823, Zn 0.1232, Si 0.0161, Cu 0.0015, Ni 0.0008 |
| AM50 | Jesus, W., Reis, T., Marques, L., Souza, H., Lima, E., Silva, A., *Microstructural Constituents, Local Hardness Contrast, and Tensile Variability of As-Cast AM50 Magnesium Alloy*, Solids 7, 45, 2026. https://doi.org/10.3390/solids7050045, §2 | Commercial ingots; "the manufacturer's specification" | Yes, the page | Al 4.91, Zn 0.04, Mn 0.30, Cu 0.0029, Si 0.03, Fe 0.0012, Ni 0.0010, Be 0.0005 |

**Not used:**
- **The AM60B of a graphene study** (https://pmc.ncbi.nlm.nih.gov/articles/PMC11433534/): its Si 0.10, Fe 0.005, Cu 0.01
  and Ni 0.002 are B94's maxima, so the table is limits, not an analysis.
- **The AM50 of Braszczyńska-Malik et al. 2026** (https://doi.org/10.3390/ma19091776): only "a nominal chemical
  composition of 5 wt.% Al and 0.45 wt.% Mn".
- **An OSTI report** on die-cast AZ91D plates (https://www.osti.gov/pages/servlets/purl/2283885): the server refused
  the connection.

**Level 1, each robot type's row 'Magnesium alloys':**

| Robot type | Workbook grade | AM part, % of the row (E) | AZ91D | AM part drawn as |
|---|---|---|---|---|
| 2 | AZ91D / AM60 | 0 / 43 / 86 | The remainder | AM60B or AM50A, half and half (E) |
| 3 | AZ91D | — | All of it: the workbook names AZ91D alone | — |
| 4 | AZ91D / AM60 | 0 / 44 / 88 | The remainder | AM60B or AM50A, half and half (E) |
| 6 | AZ91D / AM60 | 0 / 50 / 100 | The remainder | AM60B or AM50A, half and half (E) |

- **The AM share (E):** the rule of the aluminium (E1.1c), the workbook's grade for each part weighted by the part's
  mass at the mode. No part names AM60 alone, so the minimum is 0. The maximum adds the parts that name "AZ91D / AM60";
  the mode, half of those.
  - Robot type 2: heat sinks of AZ91D alone 1.0 kg, panels of both 6.0 kg.
  - Robot type 4: controller housing of AZ91D alone 2.2 kg, frame of both 16.0 kg.
  - Robot type 6: no part names magnesium, so its row's grade "AZ91D / AM60" counts as both.
- **AM60B or AM50A (E):** the workbook names AM60; AM50A is named by Magnecast (E1.2b). They are drawn half and half,
  as A380 and ADC12 were for aluminium.

**Level 2, each alloy's elements**, wt%, min / mode / max; magnesium the remainder:

| Element | AZ91D | AM60B | AM50A |
|---|---|---|---|
| Al | 8.3 / 8.56 / 9.7 | 5.5 / 5.71 / 6.5 | 4.4 / 4.889 / 5.4 |
| Zn | 0.35 / 0.67 / 1.0 | 0 / 0.15 / 0.22 | 0 / 0.0816 / 0.22 |
| Mn | 0.15 / 0.25 / 0.50 | 0.24 / 0.27 / 0.60 | 0.26 / 0.2912 / 0.60 |
| Si | 0 / 0.02 / 0.10 | 0 / 0 / 0.10 (E) | 0 / 0.0231 / 0.10 |
| Fe | 0 / 0.0023 / 0.005 | 0 / 0 / 0.005 (E) | 0 / 0.0012 / 0.004 |
| Cu | 0 / 0.021 / 0.030 | 0 / 0 / 0.010 (E) | 0 / 0.0022 / 0.010 |
| Ni | 0 / 0.0017 / 0.002 | 0 / 0 / 0.002 (E) | 0 / 0.0009 / 0.002 |

- **The minimum and maximum** are B94's limits; an element with only a maximum may lie anywhere below it, so its
  minimum is 0.
- **The modes:**
  - **AZ91D:** the median of its three analyses; Fe, Cu and Ni from Dini's, the only one that measured them (Cui's
    are "below 0.005").
  - **AM60B:** Zheng's single analysis. Its Si, Fe, Cu and Ni are 0 (E): no analysis gives them.
  - **AM50A:** the mean of its two analyses; Fe from Jesus et al. alone.
- **"Others"** (B94: 0.02 at most) and beryllium (about 0.0005) stay in the magnesium.
- **Independence:** each element is drawn on its own (as for aluminium).

**The result, % of the magnesium**, from the sandbox (V41): 20,000 draws per robot type; every draw adds up to 1 and
no element falls below zero.

| Robot type | At the modes, with AM60B | At the modes, with AM50A | 95 % of the draws |
|---|---|---|---|
| 2 | Mg 91.94, Al 7.34, Zn 0.446, Mn 0.259 | Mg 92.30, Al 6.98, Zn 0.417, Mn 0.268 | Mg 90.4–93.4, Al 5.96–8.62, Zn 0.21–0.71, Mn 0.23–0.46 |
| 3 | Mg 90.48, Al 8.56, Zn 0.67, Mn 0.25 (AZ91D alone) | the same | Mg 89.4–90.7, Al 8.39–9.50, Zn 0.43–0.93, Mn 0.18–0.46 |
| 4 | Mg 91.97, Al 7.31, Zn 0.441, Mn 0.259 | Mg 92.34, Al 6.95, Zn 0.411, Mn 0.268 | Mg 90.4–93.5, Al 5.89–8.64, Zn 0.20–0.71, Mn 0.23–0.46 |
| 6 | Mg 92.17, Al 7.14, Zn 0.410, Mn 0.260 | Mg 92.59, Al 6.72, Zn 0.376, Mn 0.271 | Mg 90.5–93.9, Al 5.50–8.56, Zn 0.16–0.69, Mn 0.24–0.47 |

Silicon, copper, iron and nickel stay below 0.09 % in every draw.

**What entering it would add:**
- in `element_recipes.xlsx`:
  - the three alloy recipes, 'AM magnesium' and the recipes of robot types 2, 4 and 6;
  - four rows in the sheet Rows, robot type 3's naming 'Magnesium AZ91D' directly;
  - no new compound and no new atomic mass: every element is already there.

**Choices in this proposal that are Matthias's:**
- the AM share from the workbook's grades, robot type 6 from its row's grade;
- robot type 3 as AZ91D alone, as the workbook names it;
- AM60B and AM50A half and half;
- AM60B's trace elements at 0, from its one analysis without them;
- the AZ91 of Wang et al. counted as AZ91D;
- "others" and beryllium left in the magnesium;
- the B94 casting limits rather than the producers' ingot limits.

#### E1.2d The modes of E1.2c set again by Matthias's rule

Matthias, 2026-10-27: "You should trust standards more than analysis performed at a university. They do NOT know quality measures for analytical procedures. This is different with comercial labs", then: "Yes, redo the modes of E1.2c and of the entered E1.1c by my rule: first search for commercial values (certificates, certified reference materials, producers' nominal compositions) for every alloy, read first-hand with references; where none exists, the middle of the standard's range (E)."

**Status: agreed. Matthias, 2026-10-27, choosing the answer offered: "I agree with the modes of E1.1e and E1.2d, including their choices." It replaces the modes of E1.2c. Entered the same day with E1.2c, with the university-only elements combined (E1.2e): Matthias, 2026-10-27: "Yes, enter both: rewrite the aluminium modes as in E1.1e, and enter the magnesium recipe of E1.2c (its AM share, AM60B or AM50A half and half, robot type 3 as AZ91D alone) with the modes of E1.2d. Tests first, as before, and the documents." (VERIFICATION.md V43).**

**The order each mode follows:**
1. **A standard's nominal composition.** SAE's Aerospace Material Specifications state it in their titles.
2. **Commercial analyses:** certified reference materials, and producers' certificates of analysis. Each independent
   material counts once, as the mean of its lots; the mode is the median over the materials.
3. **A producer's nominal composition.**
4. **Otherwise the middle of the standard's range (E),** from 0 to the maximum where only a maximum is given.

A value above the standard's maximum takes the maximum. The minimum and maximum stay the registered limits. University
analyses are no longer used for any number (memory rule "standards over academic analyses").

**The sources** (read first-hand, 2026-10-27):

| Source | Kind | Read | What it gives (wt%) |
|---|---|---|---|
| SAE International, AMS4490K, *Magnesium Alloy Castings, Die 9.0Al - 0.70Zn (AZ91D, Temper F) As Cast*, revised May 2017. https://saemobilus.sae.org/standards/ams4490k-magnesium-alloy-castings-die-90al-070zn-az91d-temper-f-cast | Standard (AMS D Nonferrous Alloys Committee) | Yes, the page | AZ91D nominal: Al 9.0, Zn 0.70 |
| Magnesium Elektron, nominal compositions, compiled by TMS 2007 (E1.2b) | A producer's nominal values | Yes, the compilation | AZ91D Mn 0.3; AM60B Al 6, Mn 0.5 |
| The maker's certificate of an AM50 lot, quoted in Jesus et al. 2026 (E1.2c) | A producer's certificate | Yes | Al 4.91, Zn 0.04, Mn 0.30, Si 0.03, Fe 0.0012, Cu 0.0029, Ni 0.0010 |

**Not found:**
- **Reference materials of AZ91D, AM60B or AM50A.** MBH lists AM60A- and AM90A-type discs, other grades with copper up
  to 0.31.
- **An SAE specification of AM60B or AM50A.**
- **The university analyses of E1.2c** are no longer used.

**The modes**, wt% (min / mode / max; the limits of E1.2c, ASTM B94):

| Element | AZ91D | AM60B | AM50A |
|---|---|---|---|
| Al | 8.3 / **9.0** / 9.7 standard | 5.5 / **6.0** / 6.5 producer nominal | 4.4 / **4.91** / 5.4 certificate |
| Zn | 0.35 / **0.70** / 1.0 standard | 0 / **0.11** / 0.22 middle (E) | 0 / **0.04** / 0.22 certificate |
| Mn | 0.15 / **0.30** / 0.50 producer nominal | 0.24 / **0.50** / 0.60 producer nominal | 0.26 / **0.30** / 0.60 certificate |
| Si | 0 / **0.05** / 0.10 middle (E) | 0 / **0.05** / 0.10 middle (E) | 0 / **0.03** / 0.10 certificate |
| Fe | 0 / **0.0025** / 0.005 middle (E) | 0 / **0.0025** / 0.005 middle (E) | 0 / **0.0012** / 0.004 certificate |
| Cu | 0 / **0.015** / 0.030 middle (E) | 0 / **0.005** / 0.010 middle (E) | 0 / **0.0029** / 0.010 certificate |
| Ni | 0 / **0.001** / 0.002 middle (E) | 0 / **0.001** / 0.002 middle (E) | 0 / **0.0010** / 0.002 certificate |

The shares of E1.2c (the AM part, AM60B or AM50A half and half, robot type 3 AZ91D alone) are unchanged.

**The result, % of each robot type's magnesium at the modes** (V42; in brackets E1.2c):

| Robot type | With AM60B | With AM50A |
|---|---|---|
| 2 | Mg 91.39 (91.94), Al 7.71, Zn 0.446, Mn 0.386 | Mg 91.99 (92.30), Al 7.24, Zn 0.416, Mn 0.30 |
| 3 | Mg 89.93 (90.48), Al 9.0, Zn 0.70, Mn 0.30 (AZ91D alone) | the same |
| 4 | Mg 91.43 (91.97), Al 7.68, Zn 0.440, Mn 0.388 | Mg 92.04 (92.34), Al 7.20, Zn 0.410, Mn 0.30 |
| 6 | Mg 91.63 (92.17), Al 7.50, Zn 0.405, Mn 0.40 | Mg 92.32 (92.59), Al 6.96, Zn 0.370, Mn 0.30 |

Magnesium falls by about half a percentage point, mostly because AZ91D's aluminium is now the standard's 9.0 instead
of the university median of 8.56.

**Choices that are Matthias's:**
- AZ91D's manganese and AM60B's aluminium and manganese from Magnesium Elektron's nominal values;
- the trace elements of AZ91D and AM60B in the middle of their ranges;
- AM50A from a single lot's certificate.

#### E1.2e The magnesium elements known only from university analyses (Matthias's second rule)

Matthias, 2026-10-27: "If the elemental analysis of a material is only based on university analysis, then combine them and use respective large uncertainties. Except one of the analyis is for obvious reasons wrong".

**What it changes**, against E1.2d (wt%, min / mode / max; the limits unchanged, labelled E):
- **AZ91D's trace elements:**
  - Si 0 / **0.0303** / 0.10: the mean of Cui et al. 2018, Dini 2017 and Wang et al. 2019, instead of 0.05;
  - Fe 0 / **0.0023** / 0.005, Cu 0 / **0.021** / 0.030, Ni 0 / **0.0017** / 0.002: Dini 2017 alone, instead of
    0.0025, 0.015, 0.001. Cui et al.'s "below 0.005" is not a number and is left out.
- **AM60B's zinc:** 0 / **0.15** / 0.22, from Zheng et al. 2019, instead of 0.11. Its Si, Fe, Cu and Ni stay the
  middle of their ranges: no analysis gives them.
- **Nothing obviously wrong:** every value lies within the B94 limits. The AM60B table of the graphene study, which
  only repeats B94's maxima, was already left out (E1.2c).

**% of each robot type's magnesium at the modes** (E1.2d's in brackets):

| Robot type | With AM60B | With AM50A |
|---|---|---|
| 2 | Mg 91.38 (91.39), Al 7.71, Zn 0.463, Mn 0.386 | Mg 92.00 (91.99) |
| 3 | Mg 89.94 (89.93), Al 9.0, Zn 0.70, Mn 0.30 | the same |
| 4 | Mg 91.42 (91.43), Al 7.68, Zn 0.458, Mn 0.388 | Mg 92.04 (92.04) |
| 6 | Mg 91.62 (91.63), Al 7.50, Zn 0.425, Mn 0.40 | Mg 92.33 (92.32) |

**Status: entered** with E1.2c and E1.2d (VERIFICATION.md V43).
---

### E1.3 Titanium

**The robots use** Ti-6Al-4V (Grade 5): robot types 2, 5 and 6.

**What the siblings hold:** nothing.

**Independent sources:**

| Source | Kind | Read | What it says (wt%) |
|---|---|---|---|
| voestalpine Specialty Metals Europe, *Titanium Grade 5 (Ti6Al4V)*, datasheet (created 2026-03-23). https://www.voestalpine.com/specialtymetals/eu/app/uploads/sites/251/2026/03/Titanium-Grade-5-Ti6Al4V.pdf | Manufacturer's datasheet, Table 1 "Chem. composition (wt%) ASTM B348" | Yes | Al 5.50–6.75, V 3.50–4.50, Fe ≤0.40, O ≤0.20, C ≤0.08, N ≤0.05, H ≤0.015, others each ≤0.10, total ≤0.40, Ti the remainder. |
| Performance Titanium; titanium.com (AMS 4928); Bibus (search results only) | Supplier pages | No | The same Al and V; H ≤0.0125 and Fe ≤0.30 in AMS 4928. The differences are in traces. |

**Verdict:**
- **Representative:** Grade 5 is the grade the workbook names.
- **Not read:** the standard ASTM B348 itself.

---

### E1.4 Steel

**The robots use** different steels:

| Robot type | Steel in the workbook | kg at the mode |
|---|---|---|
| 1 | bearing steel 52100 | 4.2 |
| 1 | high-strength steel, grade not given | 2.8 |
| 2 | GCr15 / 42CrMo / 20CrMnTi | 11 |
| 3 | 42CrMo / GCr15 / fastener steel | 10 |
| 4 | GCr15 / 42CrMo | 9 |
| 5 | Si-Fe electrical steel (motor laminations) | 15 |
| 5 | 52100 / GCr15 | 5.5 |
| 6 | 20CrMnTi / 42CrMo (gears) | 4 |
| 6 | 52100 / GCr15 | 3.5 |

**What the siblings hold:**
- **VehicleComposition:** car-body steels only (mild steel AISI 1008–1020, HS, UHS, AHS), not these grades.
- **RAWCLICVehicleTractionMotor:** electrical steel M19 (Si 2.5–3.5 %) and M27 (Si 2.4–3.1 %), sheet
  `ElectricalSteel`.

**Independent sources:**

| Grade | Source | Kind | Read | What it says (wt%) |
|---|---|---|---|---|
| 52100 | Alro Steel, *52100*, data page. https://www.alro.com/divsteel/metals_gridpt.aspx?gp=0063 | Steel distributor; cites only "AISI 52100" | Yes (extract) | C 0.98–1.10, Cr 1.30–1.60, Mn 0.25–0.45, Si 0.15–0.30, S ≤0.025, P ≤0.025, Fe the remainder. |
| 52100 / GCr15 | Search results: Total Materia (ASTM A295), machinemfg comparison (GB/T 18254) | Second-hand | No | **ASTM A295:** C 0.93–1.05, Cr 1.35–1.60. **GB/T 18254 GCr15:** C 0.95–1.05, Cr 1.40–1.65, Mn 0.25–0.45, Si 0.15–0.35. Narrower than Alro's figures. |
| 42CrMo4 | Astrup AS, *42CrMo4 M*, material data sheet (2014). https://astrup.no/wp-content/uploads/2024/05/42CrMo4-M.pdf | Steel distributor's datasheet, "EN 10083-3 / 42CrMo4" | Yes | C 0.38–0.45, Si 0.15–0.40, Mn 0.60–0.90, P ≤0.025, S ≤0.035, Cr 0.90–1.20, Mo 0.15–0.30. |
| 20CrMnTi | Total Materia, *GB 20CrMnTi*. https://www.totalmateria.com/en-us/material/1030176 | Materials database, citing GB/T 3077-2015 | Yes (extract), in part: Si, Mn and Ti are behind a registration | C 0.17–0.23, Cr 1.00–1.30, Cu ≤0.30. |
| 20CrMnTi | metal.com listing; a measured bar in an IOP *Materials Research Express* paper (search results only) | Second-hand | No | Mn 0.80–1.10, Ti 0.04–0.10. Measured: Si 0.229, Mn 0.954, Ti 0.048. |
| Electrical steel | ASTM A677-16 (reapproved 2023), *Nonoriented Electrical Steel Fully Processed Types*, scope on DIN Media. https://dinmedia.de/en/standard/astm-a-677/254091836 | The standard's published scope | Yes (extract) | "low-carbon, silicon-iron, or silicon-aluminum-iron alloys containing up to about 3.5% silicon" and "a small amount of aluminum". |

**Verdict:**
- **Confirmed:** the sibling's electrical steel (Si up to 3.5 %) is consistent with ASTM A677.
- **New:** 52100/GCr15, 42CrMo4 and 20CrMnTi had no sibling data. They come from datasheets that cite the standards;
  the standards themselves (ASTM A295, EN 10083-3, GB/T 3077, GB/T 18254) were not read.
- **Representative:** yes, these are the grades the workbook names, except two:
  - robot type 1's "high-strength steel, unspecified grade";
  - robot type 3's "fastener steel".

  These have no grade, so their recipe would be an estimate.
- **Open, Matthias's decision:** where a robot type names several grades together, the share of each is not given.

#### E1.4b Further steels a humanoid robot plausibly uses

Matthias, 2026-10-26, on steel: "Try to find additional posible alloys, and see what the ranges for the emental
composition could be".

**Where each steel is used, and who says so:**

| Use in the robot | Steel | Source | Kind | Read | What it says |
|---|---|---|---|---|---|
| Flexspline of strain-wave (harmonic) gears | 40CrNiMoA = AISI 4340 | Yu, Z., Gong, J., *Introducing Kinematic Fundamentals of Strain Wave Gear for Robotic Arm Joint*, ASEE conference paper (Penn State Erie). https://peer.asee.org/introducing-kinematic-fundamentals-of-strain-wave-gear-for-robotic-arm-joint.pdf | Conference paper | Yes, §4 | "Commercially available strain wave gear uses heat treated 40CrNiMoA (AISI 4340) to achieve required design life." |
| Sun and planet gears of humanoid joints | 20CrMnTi, carburized | KOFON Motion Group, project page on DirectIndustry | Manufacturer's claim | **No:** HTTP 403. Search summary only | 20CrMnTi for sun and planet gears, above HRC 60. Agrees with the workbook's 20CrMnTi. |
| Bolts of property class 10.9 and 12.9 (the workbook names "Class 10.9–12.9" for robot type 2) | Quenched and tempered alloy steel | Optimas, *Chemical compositions of carbon and alloy steel bolts, screws and nuts*, citing EN ISO 898-1. https://optimas.com/technical-resources/chemical-compositions-of-carbon-and-alloy-steel-bolts-screws-and-nuts/ | Fastener distributor quoting the standard | Yes (extract) | **10.9 alloy steel:** C 0.20–0.55, P ≤0.025, S ≤0.025, B ≤0.003. **12.9 alloy steel:** C 0.30–0.50, same P, S, B. Footnote g: alloy steel holds at least Cr 0.30, Ni 0.30, Mo 0.20 or V 0.10 %. |
| Stainless screws (named in the parts list of robot type 1), stainless hardware (robot types 2 and 6) | 304 (A2), 316 (A4) | Outokumpu, *Steel Grades, Properties and Global Standards*, table of typical composition. https://www.outokumpu.com/-/media/from-sharepoint/documents/product/outokumpu-steel-grades-properties-global-standards.pdf | Producer's grade table | Yes | **1.4301 / 304:** C 0.04, Cr 18.1, Ni 8.1. **1.4401 / 316:** C 0.04, Cr 17.2, Ni 10.1, Mo 2.1. Typical values, not limits. |
| High-strength stainless shafts and parts | 17-4PH (1.4542, 630) | Outokumpu, as above | Producer's grade table | Yes | C 0.02, Cr 15.5, Ni 4.8, Cu 3.4, with Nb. |
| Stainless rolling bearings | 440C | Wikipedia, *440C*. https://en.wikipedia.org/wiki/440C | Encyclopedia (second-hand) | Yes (extract) | C 0.95–1.20, Cr 16.0–18.0, Mn ≤1.00, Si ≤1.00, Mo ≤0.75; used for ball and roller bearings. |
| Shafts, high-strength parts | AISI 4340 | Alro Steel, *4340*. https://www.myalro.com/gradeinfo/Metals_Gridpt.aspx?gp=0078 | Steel distributor | Yes (extract) | C 0.38–0.43, Mn 0.60–0.80, Si 0.15–0.35, Ni 1.65–2.00, Cr 0.70–0.90, Mo 0.20–0.30. |

**Searched and not found:**
- The steel of the screws, rollers and nuts of planetary roller screws (Tesla Optimus is reported to use 14). Only
  their design was found.
- The steel of the circular spline of strain-wave gears.
- European case-hardening gear steels (18CrNiMo7-6, 16MnCr5) in robot joints.

**The ranges across all the candidate grades**, wt% (from E1.4 and the table above; Fe is the rest):

| Element | Lowest | Highest | Which grades set the ends |
|---|---|---|---|
| Cr | 0 | about 18 | Electrical steel has none; 304 and 440C 16–18 |
| Ni | 0 | about 10 | Most grades none; 4340 1.65–2.00; 17-4PH 4.8; 304 8.1; 316 10.1 |
| Mo | 0 | about 2.1 | 42CrMo4 0.15–0.30; 4340 0.20–0.30; 316 2.1 |
| Mn | small | about 1.1 | 20CrMnTi 0.80–1.10 |
| Si | 0.15 | 3.5 | Electrical steel up to about 3.5 |
| C | under 0.02 | 1.20 | Electrical steel against 52100 and 440C |
| Cu | 0 | 3.4 | 17-4PH |
| Ti, Nb, V, B | traces | ≤0.10 Ti; Nb in 17-4PH; ≥0.10 V where used for bolts; ≤0.003 B | 20CrMnTi, 17-4PH, ISO 898-1 |

**What drives a robot's range:** the share of each family of steel, which no source gives:
- bearing steels (52100/GCr15, 440C);
- gear steels (20CrMnTi, 4340 for flexsplines);
- shaft and bolt steels (42CrMo4, ISO 898-1 classes 10.9 and 12.9);
- stainless steels (304, 316, 17-4PH);
- electrical steel.

The stainless share decides chromium and nickel; the electrical-steel share decides silicon. Every robot with motors
has laminations, although only robot type 5 names electrical steel. The shares would be estimates (E), for
Matthias's decision.

---

### E1.5 Copper

**The robots use:**
- robot types 1, 2, 5 and 6: high-purity copper (ETP, oxygen-free);
- robot type 4: copper with silver solder;
- robot type 3: the split copper of point 9.

**What the siblings hold:**
- **RAWCLICVehicleTractionMotor, sheet `Copper`:** ETP Cu 99.9–100 %, O ≤400 ppm; OF Cu ≥99.95 %.
- **VehicleComposition:** cables Cu 85 % (insulated) or 99 %, labelled "estimate".

**Independent sources:**

| Source | Kind | Read | What it says |
|---|---|---|---|
| KEMPER, *Cu-ETP*, alloy page. https://www.kemper-group.com/en-en/rolled-products/alloys/cu-etp/ | Copper rolling mill, "EN CW004A / UNS C11000" | Yes (extract) | Cu ≥99.9 %, O ≤0.04 %. |
| Copper Development Association, C11000. https://www.copper.org/resources/properties/db/ | Industry association | **No:** HTTP 403 | — |
| Righton Blackburns; TLT (search results only) | Distributors, citing EN 13601 and EN 1652 | No | Cu ≥99.90 %. |

**Verdict:**
- **Confirmed:** the sibling's ETP (Cu ≥99.9 %, O ≤0.04 % = 400 ppm) matches KEMPER.
- **For the robots:** copper is about 99.9 % Cu. Robot type 4's silver solder is not quantified by any source here.

---

### E1.6 Magnets (NdFeB)

**The robots use:**

| Robot type | Magnet in the workbook |
|---|---|
| 1 | "NdFeB magnets" |
| 2 | "High-coercivity NdFeB" |
| 3 | the split magnets of point 9 |
| 4 | "NdFeB with Dy/Tb" |
| 5 | "NdFeB SH/UH grades" (SH: up to 150 °C, UH: up to 180 °C) |
| 6 | "NdFeB, Dy/Tb-doped" |

**What the siblings hold:**
- **RAWCLICVehicleTractionMotor, sheet `PermanentMagnetNdFeB`**, by grade class:
  - all classes: Nd 0.29–0.32, B about 0.01, Pr ≤0.01;
  - SH: Dy 0.04–0.07, Co 0.04–0.08;
  - UH: Dy 0.06–0.09, Co 0.06–0.10;
  - EH: Dy 0.08–0.10, Co 0.08–0.12.

  The sheet's source column documents only the temperature classes (radialmagnet.com, stanfordmagnets.com), not the
  element shares.
- **VehicleComposition, sheet `PermanentMagnet`**, with no source named:
  - NdFeB1: Nd 22–31, Pr 0.07–13, Dy 0.77–4.2, Co 0.54–4.2, Ni 0.02–6.4;
  - NdFeB2: Nd 31, Dy 4.5, Co 2 (means);
  - NdFeB3: Nd 23.8, Dy 1.6 (means).

**Independent sources:**

| Source | Kind | Read | What it says |
|---|---|---|---|
| Yang, Y., Walton, A., Sheridan, R. et al. (2017). REE Recovery from End-of-Life NdFeB Permanent Magnet Scrap: A Critical Review. *J. Sustain. Metall.* 3: 122–149. https://doi.org/10.1007/s40831-016-0090-4; read at https://research.chalmers.se/publication/510753/file/510753_Fulltext.pdf | Peer-reviewed review, open access | Yes: §1, §2 and Table 5 | NdFeB "contains about 31–32 wt% REEs (mainly 21–31 wt% (Nd + Pr), 0–10 wt % Dy plus small amounts of Gd and Tb)"; "some NdFeB magnets could contain up to 5 wt% Co". "Dysprosium is essential for high-temperature applications such as in EVs/HEVs." Table 5, the generic magnet of electric motors agreed in the EU project MORE (after Walachowicz et al.): Fe 67, B 1, Co 2, Nd 20, Dy 10 %. |
| US patents 9,468,972 and others; NIMS/MEXT "Elements Strategy" digest (search results only) | Patents; a Japanese government programme digest | No | Conventional traction-motor magnets 6–10 wt% Dy; hybrid-car magnets 8–10 wt% Dy; reduced-Dy diffusion magnets 0.3–5 wt%. |
| Arnold Magnetic Technologies, *The Important Role of Dysprosium in Modern Permanent Magnets* (search result only) | Manufacturer's white paper | No | — |

**Verdict: the siblings are not confirmed.**
- **Cobalt:** RAWCLICVehicleTractionMotor gives SH 4–8 %, UH 6–10 % and EH 8–12 %. The review allows "up to 5 wt%";
  the MORE motor magnet has 2 %.
- **Rare earths in total:** the sibling's Nd 29–32 % plus Dy 4–10 % gives 33–42 %, against the review's 31–32 %. In
  the review, Dy replaces part of the Nd; it is not added on top.
- **VehicleComposition:** its Pr maximum of 13 % and Ni up to 6.4 % (the nickel is a coating, not the magnet alloy)
  are outside the review's figures.
- **Dy:** the review (0–10 %, MORE 10 %), the patents and NIMS/MEXT (6–10 % in traction motors) agree with each
  other.
- **Representative:** robot joint motors are smaller and cooler than car traction motors. Robot type 5's SH/UH
  grades fit the high-temperature end; robot types 1 and 2 name no grade. That choice is Matthias's.
- **Not read:** the MORE report (Walachowicz et al.) itself; manufacturers' composition tables, which most do not
  publish.

#### E1.6b The magnet composition sheet of the car projects, checked

Matthias, 2026-10-26: "There is a material composition sheet available for magnets. It is with the cars. Check it
there. There are all the different composition, which allow also higher temperatures".

**The sheet:** `RAWCLICVehicleElectronics/Data/Sources/permanent_magnet_elemental_composition.xlsx`, sheet `NdFeB`.
- It holds 27 grades in seven temperature classes: N (60–80 °C), M (100), H (120), SH (150), UH (180), EH (200) and
  AH (220 °C). Each grade gives the range of every element, plus its magnetic properties, density, applications and
  relative cost; the sheet `Ferrite` gives four ferrite grades.
- No source is written in the sheet, and no code or document of RAWCLICVehicleElectronics or
  RAWCLICVehicleTractionMotor names the file.
- `RAWCLICVehicleTractionMotor/data/raw/10_MaterialElementDefinitions.xlsx` holds the same numbers as minimum and
  maximum, so the two siblings are one source.

**Check 1, whether each grade can add up to 100 %.** The smallest and the largest sum of each grade's ranges were
computed. The sheet adds Dy and Co on top of an unchanged Nd (29–32 %) and nearly unchanged Fe (60–65 %), so the sums
rise with the temperature class:

| Class | Grades | Smallest sum | Largest sum | Rare earths (Nd+Dy+Tb+Pr) | Co |
|---|---|---|---|---|---|
| N | N35–N52 | 92–94 % | 101–103 % | 29–33 % | 0 |
| M | N35M–N50M | 94–97 % | 106–110 % | 29–36 % | 0–5 % |
| H | N35H–N48H | 98–99 % | 112–113 % | 31–38 % | 2–6 % |
| SH | N35SH–N48SH | 98–101 % | 113–116 % | 33–41 % | 4–8 % |
| UH | N35UH–N45UH | **102–105 %** | 118–121 % | 35–43 % | 6–10 % |
| EH | N35EH–N42EH | **106–108 %** | 122–124 % | 37–44 % | 8–12 % |
| AH | N35AH–N40AH | **109–110 %** | 125–126 % | 38–45 % | 10–13 % |

**From N48SH up, no composition within the stated ranges adds up to 100 %.** The smallest sum is already above 100 %.

**Check 2, against independent sources:**

| Source | Kind | Read | What it says |
|---|---|---|---|
| Arnold Magnetic Technologies, *The Important Role of Dysprosium in Modern Permanent Magnets*, Rev. 150903a (2015). https://www.arnoldmagnetics.com/wp-content/uploads/2017/10/Important-Role-of-Dysprosium-in-Modern-Permanent-Magnets-150906.pdf | Magnet manufacturer's white paper | Yes | "Substituting Dy for a portion of the neodymium (Nd) in Neo magnets increases the room temperature value of HcJ". Table 1, "Approximate Dy content of Neo magnets ... typical from 1985 to 2011": H 2.8, SH 4.2, UH 6.5, EH and AH 8.5–11.0 wt%. Electric traction drives need "Dy as high as 11%". Dy diffusion reduces "4+% Dy for SH grades to ~2% while 8‐11% grades are reduced to 4‐5%". |
| Yang et al. 2017 (E1.6) | Peer-reviewed review | Yes | Rare earths 31–32 wt% in total (Nd+Pr 21–31, Dy 0–10); Co "up to 5 wt%". |

**Verdict:**
- **Dy by class is confirmed.** The sheet's Dy (H 2–5, SH 4–7, UH 6–9, EH 8–10, AH 9–11 %) agrees with Arnold's typical
  values (2.8, 4.2, 6.5, 8.5–11 %).
- **Nd is not.** Dy replaces part of the Nd (Arnold, Yang), so the total of rare earths stays near 30–33 %. In the
  sheet it rises to 45 %.
- **Co is not.** The sheet's 6–13 % in the UH to AH classes has no support in the sources read; Yang gives "up to 5
  wt%".
- **The sheet's structure stays usable.** Its grade classes by temperature, with Dy by class, carry over to the robot
  types: Nd + Pr becomes the rest of the rare earths after Dy and Tb, Co is held within the literature, and Fe is the
  remainder. That is a proposal for Matthias.
- **A fault in the derived sibling file:** `RAWCLICVehicleElectronics/Data/Sources/elemental_composition_ratios.xlsx`,
  sheet `Magnet_High_Ratio`, holds negative maxima, for example B −0.012, Al −0.005 and Cu −0.001. The "~1.0-1.2" and
  "<0.5" texts appear to have been read as negative numbers. Reported, not changed; it is Matthias's data.

---

### E1.7 Battery materials

**The robots use:**

| Robot type | Battery materials in the workbook |
|---|---|
| 1 | Li-ion materials, assumed NMC |
| 2 | NMC or LFP / graphite |
| 3 | LiFePO4 (LFP) system |
| 4 | NMC / graphite / electrolyte |
| 5 | NMC high-discharge active materials |
| 6 | Li-NMC / LFP / solid electrolyte |

The scope differs by robot type: "active materials" in robot type 5, the whole "system" in robot type 3.

**What the siblings hold:**
- **RAWCLICVehicleBattery:** element and component masses of car battery packs by chemistry (LFP, NMC middle, NMC
  high nickel), from many sources.
- **RAWCLICStockAndFlow** reads them per draw (`src/battery_composition.py`). That module notes that "the elements do
  NOT add up to the pack": the casing, the separator and most of the electrolyte have no element rows.

**Independent sources:**

| Source | Kind | Read | What it says |
|---|---|---|---|
| U.S. EPA (2013), *Application of Life-Cycle Assessment to Nanoscale Technology: Lithium-ion Batteries for Electric Vehicles* (EPA 744-R-12-001), Chapter 2, Table 2-1. https://19january2021snapshot.epa.gov/sites/static/files/2015-04/documents/lithium_batteries_ch2.pdf | Government LCA report; confidential manufacturer data shown as ranges | Yes: Table 2-1 | Pack of 10–12 kg, mass %: Li-ion cathode material 22–31, Al collector 4–9, graphite 8–13, Cu collector 1–12, electrolyte 8–15 (LiPF6 1–2), separator 2–3, cell casing 3–20, BMS 2, pack housing 17–23. The chemistries assessed include LiMnO2, LiNiCoMnO2 and LiFePO4. |
| Dai, Q., Kelly, J.C., Gaines, L., Wang, M. (2019). Life Cycle Analysis of Lithium-Ion Batteries for Automotive Applications. *Batteries* 5(2): 48 (GREET/BatPaC, NMC111). https://www.mdpi.com/2313-0105/5/2/48 | Peer-reviewed, Argonne | **No:** HTTP 403 | — |
| Argonne, GREET battery updates (Iyer and Kelly 2023; Dai et al. 2018). https://greet.anl.gov/files/battery_updates | Laboratory memos | **No:** HTTP 403 | — |
| Cathode formulas LiNi(x)Mn(y)Co(z)O2 and LiFePO4 | Chemistry: element shares from the formula | — | To be computed from atomic masses when the recipes are proposed. |

**Verdict:**
- **Partly confirmed:** the sibling's car-pack data cannot be checked number by number against EPA's ranges. EPA's
  shares are of whole packs with housing, while the robot's "battery materials" are cell materials.
- **The most important sources were not readable:** Argonne's BatPaC/GREET (both blocked).
- **Open, Matthias's decisions:**
  - what "battery materials" holds in each robot type: cells, or only active materials;
  - which chemistry each robot type gets where the workbook names two or three.

#### E1.7b The battery composition of the car project, checked

Matthias, 2026-10-26: "There are a full composition of battery materials in the batteries for cars. Check them".

**The file:** `RAWCLICVehicleBattery/data/raw/BATT_consolidated_composition.xlsx`.
- One sheet per car pack: BEV 25 to 100 kWh, HEV 1 kWh, PHEV 20 kWh. Read here: `BATTinELV_BEV_60kWh`.
- Per chemistry (LFP, LMFP, LMO, NMC low, middle and high nickel, NCA), the components in kg per kWh (code `c-p`) and
  the elements in each component (code `e-c`).
- Every minimum and maximum is 0.9 and 1.1 times the value: a convention, not a measured spread (the project's
  README).

**Check 1, the cathodes against their formulas.** The element shares of each cathode active material, against the
shares computed from the formula and the atomic masses (wt%):

| Chemistry in the file | Li | Ni | Mn | Co | Fe | P | Al | O | The formula it matches |
|---|---|---|---|---|---|---|---|---|---|
| LFP | 4.4 | | | | 35.4 | 19.6 | | 40.6 | LiFePO4, exactly |
| NMC low Ni | 7.2 | 20.3 | 19.0 | 20.4 | | | | 33.2 | NMC111, exactly |
| NMC middle Ni | 7.2 | 34.9 | 12.7 | 12.2 | | | | 33.0 | Between NMC532 and NMC622 (Ni : Mn : Co about 0.58 : 0.22 : 0.20) |
| NMC high Ni | 7.1 | 52.6 | 3.6 | 3.8 | | | | 32.8 | Between NMC811 and NMC955 (about 0.87 : 0.06 : 0.06) |
| NCA | 7.2 | 48.9 | | 9.2 | | | 1.4 | 33.3 | NCA 80/15/5, exactly |

For comparison, from the formulas: NMC532 Ni 30.4, Mn 17.1, Co 12.2; NMC622 Ni 36.3, Mn 11.3, Co 12.2; NMC811 Ni 48.3,
Mn 5.6, Co 6.1; NMC955 Ni 54.2, Mn 2.8, Co 3.0.

**Check 2, how the cell is built.** Shares of the cell's mass, without the pack parts (frame, enclosures, thermal
conductor, cables, cell terminals), in %:

| Component | LFP | NMC middle Ni | NMC high Ni |
|---|---|---|---|
| Cathode active material | 46.7 | 48.1 | 46.0 |
| Anode active material | 23.1 | 22.1 | 22.2 |
| Electrolyte | 12.7 | 11.3 | 10.0 |
| Copper foil | 9.8 | 10.3 | 12.4 |
| Aluminium foil | 4.1 | 4.4 | 5.2 |
| Casing | 2.5 | 2.4 | 2.5 |
| Separator | 1.2 | 1.4 | 1.7 |
| The cell, kg per kWh (Wh per kg) | 4.27 (234) | 3.25 (308) | 3.03 (330) |

**Check 3, what has no elements.** The elements cover 84 to 86 % of the cell. Not covered:
- **The electrolyte** holds only its Li (0.7 %). From that Li the salt LiPF6 is 15 to 17 % of the electrolyte, which
  agrees with EPA's LiPF6 of 1 to 2 % within an electrolyte of 8 to 15 % (E1.7). The solvent and the rest of the salt
  are not itemised. Computed from the formulas, LiPF6 at 12 to 16 % in EC and DMC (1 : 1 by mass, an assumption)
  gives C 34 to 36, O 45 to 47, F 9 to 12, H 5, P 2 to 3 and Li 0.5 to 0.7 %.
- **The separator and the casing** have no element rows. Separators are commonly polyethylene or polypropylene, and
  casings aluminium (pouch, prismatic) or nickel-plated steel (cylindrical, van de Ven et al.); the polymers are not
  checked against a source.

**Check 4, silicon in the anode.** The NMC middle and high nickel anodes hold 10.5 and 11.5 % Si; LFP, NMC low nickel
and NCA none. Ank et al. found no silicon in Tesla's NMC811 cell. One cell does not show the market, so the Si share
is neither confirmed nor refuted.

**Check 5, the robots' battery masses against their energy.** The workbook's energy of each robot times the car
cells' kg per kWh gives the cell mass that energy needs. Robot 1's energy is computed from 9 Ah × 13 cells × 3.65 V,
an assumed nominal voltage.

| Robot type | Energy, kWh | Chemistry used here | Cells for that energy, kg | Workbook "battery materials", kg (mode) | Ratio | Pack, kg |
|---|---|---|---|---|---|---|
| 1 | 0.43 | NMC middle Ni | 1.4 | 2.5 | 1.8 | 2.5 |
| 2 | 0.97 | NMC middle Ni | 3.2 | 4.5 | 1.4 | 5.5 |
| 3 | 0.86 | LFP | 3.7 | 8.5 | **2.3** | 9.6 |
| 4 | 0.70 | NMC middle Ni | 2.3 | 9.5 | **4.2** | 14.5 |
| 5 | 2.5 | NMC high Ni | 7.6 | 7.0 | 0.9 | 14.0 |
| 6 | 2.5 | NMC middle Ni | 8.1 | 9.0 | 1.1 | 10.0 |

- Robot type 1's 2.5 kg equals its whole pack, which the parts list gives with a PC/ABS enclosure, copper busbars and
  a BMS board.
- In robot types 3 and 4 the "battery materials" are 2.3 and 4.2 times the cells their energy needs. Either they hold
  more than cells, or the energy is understated. The workbook's own GAP-04 notes the same at pack level (90 and 48 Wh
  per kg).
- Robot type 5's 7 kg of "active materials" and robot type 6's 9 kg fit their 2.5 kWh.
- The car cells are large automotive cells. Small cylindrical cells hold less per kg, so the ratios are a guide, not
  a measurement.

**Independent sources:**

| Source | Kind | Read | What it says |
|---|---|---|---|
| van de Ven, J.J.M.M., Yang, Y., Abrahami, S.T. (2024). A closer look at lithium-ion batteries in E-waste and the potential for a universal hydrometallurgical recycling process. *Scientific Reports* 14: 16661. https://doi.org/10.1038/s41598-024-67507-7 | Peer-reviewed **measurement**: cells from laptops, power banks, phones, watches and earbuds dismantled by hand and weighed | Yes: section "Battery cells composition", Fig. 4 | 18650 cells: cathode 44, anode 32, casing 17 (nickel-plated steel), separator 3.6, loss 2.7 wt%. Pouch cells: cathode 51, anode 38, casing 3.3, separator 4.1, loss 3.5 wt%. The electrodes include their foils and part of the electrolyte; the rest of the electrolyte evaporates into "loss". "When the cell casing is excluded, the relative share of the other components is the same for both cell types." |
| Ank, M. et al. (2023). Lithium-Ion Cells in Automotive Applications: Tesla 4680 Cylindrical Cell Teardown and Characterization. *J. Electrochem. Soc.* 170: 120536. https://iopscience.iop.org/article/10.1149/1945-7111/ad14d0 | Peer-reviewed teardown of one automotive cell | Yes: abstract and text, without the last quarter of the page | 355.9 g; NMC811 cathode; graphite anode with "no detectable presence of silicon". No mass by component. |
| Quinn, J.B. et al. (2018). Energy Density of Cylindrical Li-Ion Cells: A Comparison of Commercial 18650 to the 21700 Cells. *J. Electrochem. Soc.* 165: A3284. https://iopscience.iop.org/article/10.1149/2.0281814jes | Peer-reviewed measurement | Yes | Only whole-cell masses (18650: 42 to 49 g; 21700: 68 to 70 g); no mass by component. Not used for any number here. |

**Verdict:**
- **The cathodes are confirmed:** each matches its formula.
- **The build of the cell agrees with measured pouch cells:** cathode with its foil 51 to 52 % against 51 %; anode
  with its foil and the electrolyte against 38 % plus loss. Its casing of 2.5 % is that of pouch or prismatic cells.
  A cylindrical cell has a steel can of about 17 % (van de Ven et al.), which the car data does not hold.
- **14 to 16 % of the cell has no elements:** the electrolyte except its Li, the separator and the casing. They can
  be completed from formulas.
- **The ±10 % band is a convention**, not a spread of the data.
- **Decided by Matthias, 2026-10-26**, choosing the answer offered: "Battery materials should be the cells only in
  every robot type; the housing, BMS and busbars belong to the other materials."
- **What that means for each robot type's battery row in the workbook** (the workbook stays as it is):

  | Robot type | The row holds, in the workbook's words | Mode, kg | Against "cells only" |
  |---|---|---|---|
  | 1 | "9,000 mAh 13S battery pack allocation" | 2.5 | The whole pack (2.5 kg in the parts list, with PC/ABS enclosure, copper busbars and BMS board): more than cells |
  | 2 | "Constituent cell materials for 0.97 kWh pack" | 4.5 | Cells already |
  | 3 | "LiFePO4 (LFP) system", two 48 V 9 Ah packs | 8.5 | A system; the enclosures are already in the plastics row. 2.3 times the car cells for 864 Wh |
  | 4 | "Active cell constituents of 700 Wh swappable pack" | 9.5 | Called cells, but 4.2 times the car cells for 700 Wh: the kg and the energy contradict each other |
  | 5 | "NMC high-discharge active materials" | 7.0 | Active materials only: less than cells, which also hold foils, electrolyte, separator and casing |
  | 6 | "2.5 kWh solid-state concept battery cell materials" | 9.0 | Cells already |

- **Open, Matthias's decisions:**
  - how the cell mass is set in robot types 1, 3, 4 and 5, and where the rest of each row goes;
  - which chemistry where the workbook names two or three (robot types 2 and 6);
  - the cell format (cylindrical with a steel can, or pouch), which the workbook does not name;
  - the Si in the NMC anodes.
- **Not yet researched:** the kg per kWh of the cells robots use. The car cells are large automotive cells, not the
  same kind, so they are only a guide here. Researched since: E1.7c.

#### E1.7c The cells humanoid robots use: the sources

Matthias, 2026-10-26, choosing the answer offered: "Set the cell mass from each robot's energy, with the kg per kWh
of the cells robots actually use. Research those robot cells first and show me the sources. The rest of each row goes
to the other materials or to Not allocated."

**Which cells robots use.** No robot maker read here names its cells. What was found:

| Source | Kind | Read | What it says |
|---|---|---|---|
| Suk Dae-geon (2026-09-14). Humanoid robot battery race shifts to uptime as capacity expansion hits limits. *Digital Today* (Chinese edition). https://www.digitaltoday.co.kr/cn/view/102893/humanoid-robot-battery-race-shifts-to-uptime-as-capacity-expansion-hits-limits | Trade press, second-hand | Yes | Most humanoid makers still buy electric-car cylindrical or pouch cells. Commercial Li-ion cells hold about 250 to 300 Wh/kg, less at system level with BMS and packaging. LG Energy Solution is adapting its 2170 cylindrical cell to robots; Samsung SDI supplies high-nickel tabless cylindrical cells. Tesla Optimus and Figure 03 carry 2.3 kWh in the torso. No cell named for any robot. |
| CM Batteries (2026-06-26). A Panoramic View of Global Humanoid Robot Battery Suppliers. https://cmbatteries.com/?p=23989 | Blog of a battery supplier, which has a commercial interest; supply claims, not robot specifications | Yes | Tesla Optimus: 21700 cylindrical (Panasonic). Unitree H1: 21700 cylindrical (one supplier) and pouch (another). UBTECH Walker X and EngineAI: pouch, all-solid-state. Cell claims: 280 to 350 Wh/kg (Sunwoda), 480 Wh/kg (Xin Jie). |
| EEWorld (2026). Unitree G1 Humanoid Robot: Latest Teardown Analysis. https://en.eeworld.com.cn/news/robot/eic733333.html | Summary of four teardowns (China Post Securities, SemiAnalysis, Munro, Nikkei xTECH); second-hand | Yes, in the browser | G1 battery: "Lithium battery, 9000mAh, 0.42kWh, weight 2.5kg". That is 168 Wh/kg for the pack. No cell format. |
| Figure AI (2025-07-17). F.03 Battery Development. https://www.figure.ai/news/f-03-battery-development | Robot maker's own blog | Yes | 2.3 kWh. Cell format, chemistry, cell count and pack mass not stated. |

**What a cell holds per kg.** Computed from each datasheet's capacity, voltage and weight. Where the sheet gives a
minimum capacity and a maximum weight, these are used, so the value is the lowest the sheet allows.

| Cell | Chemistry, format | Source | Kind | Read | Capacity × voltage / weight | Wh/kg |
|---|---|---|---|---|---|---|
| Samsung SDI INR18650-35E | NMC/NCA (not named), 18650 | Samsung SDI specification, Version 1.0, applied 2016-04-11; copy at https://mikrocontroller.net/attachment/476470/Samsung__35E.pdf | Manufacturer's specification | Yes, the PDF | min 3,350 mAh × 3.60 V / 50 g max | 241 |
| Samsung SDI INR21700-50E | NMC/NCA (not named), 21700 | Samsung SDI specification INR21700-50E2, Version V1.0; copy at https://shop.aceongroup.com/cdn/shop/files/RLII-CSI-1618_Samsung_50E_DATASHEET.pdf. Version 0.2 of 2017 (https://static.chipdip.ru/lib/378/DOC012378044.pdf): 3.6 V, 69 g, also 256 | Manufacturer's specification | Yes, the PDFs | min 4,900 mAh × 3.63 V / 69.5 g max | 256 |
| Molicel INR21700-P45B | Not named, 21700, high power (45 A) | Molicel product page, https://www.molicel.com/inr21700-p45b/ | Manufacturer's page; the datasheet only on request | Yes | 4.5 Ah typical × 3.6 V = 16.2 Wh; the page states 242 Wh/kg | 242 |
| Tesla 4680 (first generation) | NMC811, 4680 | Ank et al. 2023 (E1.7b) | Peer-reviewed **measurement** of one cell | Yes | 355.9 g, measured at C/3 | 232.5 |
| A123 ANR26650M1-B | LFP, 26650, high power (70 A) | A123 Systems datasheet; copy at https://piekarz.pl/pdf/49579 | Manufacturer's datasheet, an older cell | Yes, the PDF | 2.5 Ah nominal (2.4 min) × 3.3 V / 76 g | 109 (104 at the minimum) |
| Keeppower IFR32700 | LFP, 32700, 3C | Keeppower product page, https://keeppower.com.cn/products_detail.php?id=836 | Cell brand's page; weight "Approximately" | Yes | 6,000 mAh × 3.2 V / 141 g | 136 |
| EVE C33 33140 | LFP, 33140 | Evlithium shop page, https://www.evlithium.com/LiFePO4-Battery/33140-15ah-lifepo4-battey-cell.html | **Reseller**, not EVE | Yes | 15.2 Ah average (14.5 min) × 3.2 V / 267 ± 6 g. The page's "up to 285wh/kg" does not follow from its own numbers | 182 (174 at the minimum) |

**Left out, and why:**
- The ANSMANN 21700 with a built-in EVE 50E (https://docs.rs-online.com/0e57/A700000015726491.pdf): 75 g including a
  protection circuit and a USB-C socket, so not a bare cell.
- Shop listings of the same cells: their weights differ from the manufacturers' sheets.
- The car file's cells (234 Wh/kg for LFP, 285 to 330 for NMC): large automotive cells, not the cells robots use;
  context only. Its LFP is above every LFP cell read here (104 to 182).
- Solid-state cells (robot type 6): only the supplier's claims above (280 to 480 Wh/kg); no datasheet read.

**Checked against the robots' packs** (pack energy and mass from the workbook, for robot type 1 also EEWorld):

| Robot type | Pack, Wh/kg | NMC cells at 232 to 256 Wh/kg | LFP cells at 104 to 182 Wh/kg |
|---|---|---|---|
| 1 | 168 | 1.6 to 1.8 kg, 66 to 72 % of the pack | — |
| 2 | 176 | 3.8 to 4.2 kg, 69 to 76 % of the pack | 5.3 to 9.3 kg: more than the 5.5 kg pack |
| 3 | 90 | — | 4.7 to 8.3 kg of the 9.6 kg packs |
| 4 | 48 | 2.7 to 3.0 kg, **only 19 to 21 %** of the 14.5 kg pack | — |
| 5 | 179 | 9.8 to 10.8 kg, 70 to 77 % of the 14 kg packs | — |
| 6 | 250 | 9.8 to 10.8 kg, 98 to 108 % of the 10 kg pack | — |

- **Robot type 2:** only NMC cells fit its 0.97 kWh into 5.5 kg; LFP cells of the kinds read cannot.
- **Robot type 4:** its 700 Wh and 14.5 kg do not fit together for any cell read here (the workbook's own GAP-04).
  Either the energy or the mass is wrong; that is Matthias's data, reported and not changed.
- **Robot type 5:** 10 kg of cells, of which the active materials (about two thirds, E1.7b) are about 7 kg: this
  agrees with the workbook's 7 kg of "active materials".
- **Robot type 6:** today's NMC cells would fill the whole pack; its 2.5 kWh in 10 kg needs the concept cells it
  names.

**Verdict:**
- **Cylindrical NMC cells: four sources agree** on 232 to 256 Wh/kg: three manufacturers' sheets and one measurement.
  Only one source for high-power cells (242).
- **LFP cells: three sources, spread from 104 to 182 Wh/kg**, depending on the cell's size and power. Two are not
  manufacturers' sheets.
- **Which cell each robot uses is known for none of the six.** The trade press and a supplier say cylindrical or
  pouch cells bought from car makers' suppliers.
- **Not read:** pouch cell datasheets; solid-state cells; the 2017 version of the A123 sheet.
- **No min / mode / max is proposed yet.** Proposed since: E1.7d.

#### E1.7d Proposal: the cell mass of each robot type, and where the rest of each row goes

Matthias, 2026-10-26, choosing the answer offered: "Yes, propose the cell mass min / mode / max for each robot type
from these sources, and where the rest of each row goes. Show it to me before anything is entered."

**Status: agreed by Matthias, 2026-10-26, choosing the answer offered: "I agree with the cell-mass proposal as written
in E1.7d, for robot types 1, 3, 4 and 5, with robot types 2 and 6 kept as in the workbook." Not entered yet; where it
is entered is still his decision.**

**The rule proposed.** In each draw: cell mass = energy / energy per kg of the cells. The rest = the workbook's row −
the cell mass. The workbook is not changed.

**The energy per kg of the cells (E, from E1.7c), triangular:**

| Cells | Minimum, Wh/kg | Mode | Maximum | Basis |
|---|---|---|---|---|
| NMC, cylindrical | 232.5: Tesla 4680, measured | 241.5: the median of the four sources (Samsung 35E 241 and Molicel P45B 242 either side) | 256: Samsung 50E | Four sources that agree; the high-power cell (P45B) sits at the mode |
| LFP, cylindrical | 104: A123 26650 at its minimum capacity | 136: Keeppower 32700, the middle source | 182: EVE 33140, average capacity | Three sources, widely spread |

**The energy of each robot** is one number in every source, so its spread is not carried; the spread comes from the
cells. Robot type 1: 0.42 kWh (EEWorld; 9 Ah × 13 × 3.6 V gives 0.421). Robot type 3: 0.864 kWh (two packs of
48 V, 9 Ah). Robot type 4: 0.70 kWh. Robot type 5: about 2.5 kWh.

**The result, checked with 200,000 draws in a sandbox (V18):**

| Robot type | Energy, kWh | Cells | Cell mass, kg: bounds and at the modes | 95 % of draws | Workbook row, kg | The rest, kg: at the modes (bounds) | Where the rest goes |
|---|---|---|---|---|---|---|---|
| 1 | 0.42 | NMC | 1.64 / 1.74 / 1.81 | 1.66 to 1.79 | 2.0 / 2.5 / 3.0 | 0.76 (0.19 to 1.36); never below 0 | To plastics, electronics and copper, by the measured shares below |
| 3 | 0.864 | LFP | 4.75 / 6.35 / 8.31 | 5.01 to 7.73 | 7.5 / 8.5 / 9.5 | 2.15 (−0.81 to 4.75); below 0 in 0.2 % of the draws | Not allocated (7.4 kg at the mode) |
| 4 | 0.70 | NMC | 2.73 / 2.90 / 3.01 | 2.77 to 2.98 | 8.0 / 9.5 / 11.0 | 6.60 (4.99 to 8.27); never below 0 | Not allocated (0 kg at the mode) |
| 5 | 2.5 | NMC | 9.77 / 10.35 / 10.75 | 9.88 to 10.65 | 5.0 / 7.0 / 9.0 | −3.35 (−5.75 to −0.77): the cells are heavier than the row | The missing cell parts come out of Not allocated (18.4 kg at the mode) |

The cell mass "at the modes" is the energy divided by the mode of the energy per kg; the mode of a quotient is not
exactly the quotient of the modes, which is why the 95 % column is given as well.

**Why each rest goes where it goes:**
- **Robot type 1:** the workbook's 2.5 kg is the whole pack and names what is not cells: a PC/ABS enclosure, copper
  busbars and a BMS board. The plastics row ("External covers and internal brackets") does not hold the enclosure,
  so nothing is counted twice. The split of the rest, from van de Ven et al. 2024 (E1.7b), who weighed the battery
  modules of three laptops and five power banks; the shares are of the mass outside the cells:

  | Goes to | Laptops | Power banks | Proposed, min / mode / max |
  |---|---|---|---|
  | Electronics (BMS) | 10.5 % | 22.4 % | 10.5 / 16.5 / 22.4 % (mode: the middle, E) |
  | Copper (wiring) | 5.6 % | 1.7 % | 1.7 / 3.7 / 5.6 % (mode: the middle, E) |
  | Plastics (casing, glue, separating pads) | 83.9 % | 75.9 % | The remainder |

  At the modes that is electronics 0.13 kg, copper 0.03 kg and plastics 0.60 kg. Representative in kind (small packs
  of cells with a plastic casing, a BMS board and wiring), but few devices.
- **Robot type 3:** its enclosures are already in the plastics row ("Outer cladding, battery enclosures & hybrid
  housings"). No source says what the other 2 kg of the "system" are; a BMS and wiring are 3 to 7 % of a small pack
  (van de Ven et al.), well below 2 kg. In the 0.2 % of draws where the cells exceed the row, Not allocated gives the
  difference, so no mass is negative.
- **Robot type 4:** nothing in the workbook explains 6.6 kg. The housing, BMS and busbars (about 5 kg) are already
  outside the 9.5 kg. The 700 Wh is the A2's "(Standard)" battery (https://www.humanoid.press/database/database-agibot-a2/,
  read 2026-10-26, which gives 55 kg for the Standard and about 69 kg for the Flagship), while the anchor robot
  weighs 69 kg. Whether the Flagship has a larger battery is not known. Matthias's data: reported, not changed.
- **Robot type 5:** the row's 7 kg are "active materials". The active materials are 68 to 70 % of an NMC cell in
  the car file (cells without a steel can), and 68 % of 10.35 kg is 7.0 kg, so the row agrees with the cells. The
  cells' other parts (foils, electrolyte, separator, casing, about 3.3 kg) are not in any row. They come out of
  Not allocated.

**Not proposed, and why:**
- **Robot types 2 and 6** keep the workbook's rows, which are cells already. For robot type 2, the energy would give
  3.8 to 4.2 kg against the row's 2.5 / 4.5 / 6.0; as a remainder this would fall below 0 in 32 % of the draws. For
  robot type 6 there is no datasheet for solid-state cells.
- **The element recipe of the cells** comes after this: the car file's cell recipe, completed from formulas, with a
  steel can for cylindrical cells (E1.7b).
- **Where these numbers are entered** (for example a sheet beside Splits in `shared_lists.xlsx`) is a later
  decision. Matthias, 2026-10-26, choosing the answer offered: "Enter the cell masses later, together with the
  battery element recipe. Continue with the open battery points first."

#### E1.7e Battery point 1: the chemistry of robot types 2 and 6

The workbook names "NMC or LFP / graphite" for robot type 2 and "Li-NMC / LFP / solid electrolyte" for robot type 6.

**The voltage tells the chemistry.** NMC and NCA cells have a nominal 3.6 V and a full charge of 4.2 V; LFP cells
3.2 V and 3.65 V.

| Robot type | What a source states | NMC or NCA cells | LFP cells |
|---|---|---|---|
| 1, Unitree G1 | 9 Ah, 13 cells in series, 0.42 kWh (EEWorld, E1.7c; the workbook) | 13 × 3.6 V × 9 Ah = 0.421 kWh: **fits** | 13 × 3.2 V × 9 Ah = 0.374 kWh: does not |
| 2, Unitree H2 | 15 Ah (0.972 kWh), maximum 75.6 V | 75.6 V / 4.2 V = 18 cells; 18 × 3.6 V × 15 Ah = 0.972 kWh: **fits exactly** | 75.6 V / 3.65 V = 20.7 cells, not a whole number: does not |

Source for robot type 2: Global Drone HQ, *Unitree H2 Battery*, https://globaldronehq.com/products/unitree-h2-battery,
read 2026-10-26. An authorised dealer's shop page, not Unitree's; it cites no manual. The 15 Ah and 0.97 kWh agree
with the workbook's sources S16 and S17.

**The mass tells it too** (E1.7c): LFP cells for 0.97 kWh weigh 5.3 to 9.3 kg, more than robot type 2's 5.5 kg pack.
Robot type 6 keeps 9 kg of cells (7 to 11) for 2.5 kWh, which is 278 Wh/kg at the mode (227 to 357): above every LFP
cell read (104 to 182), and at the mode above the cylindrical NMC cells too (232 to 256). It fits large NMC cells
(the car file's 285 to 330) or the solid-state cells it names (suppliers' claims of 280 to 480).

**The car project on solid-state:** RAWCLICVehicleBattery carries only the packaging of solid-state cells; their
cathode, anode and electrolyte are `unknownBatteryMaterial` (its README, stage 05). No element recipe for a solid
electrolyte exists in the sibling projects.

**Verdict:**
- **Robot type 2: NMC-type cells.** Both the voltage and the mass exclude LFP. NMC and NCA cannot be told apart by
  voltage.
- **Robot type 1:** the workbook's "assumed NMC" is confirmed the same way.
- **Robot type 6:** LFP is excluded by the mass. The cathode is NMC; whether the electrolyte is liquid (a recipe
  exists, E1.7b) or solid (no recipe yet, to be researched) is Matthias's decision.
- **Which NMC grade** (low, middle or high nickel) belongs to the element recipe, the last battery point.
- **Decided by Matthias, 2026-10-26**, choosing the answer offered: "Robot types 2 and 6 both get NMC cells with a
  liquid electrolyte, using the car file's NMC recipe."
- **The grade, decided by Matthias, 2026-10-26:** "Use the NMC igh" (cut off), then "high and not liquid so that
  all the compositons are the same". Asked what "not liquid" meant, he chose "Liquid, the car recipe": high-nickel
  NMC with the car file's liquid electrolyte, the same recipe in every NMC robot type (1, 2, 4, 5, 6). Asked about
  robot type 3, he chose "Robot 3 stays LFP".
- **His reason, 2026-10-26:** "Nickel high is a mixture of two high containing nickel batrtery chemistries, which
  makes it easier to just go with one chemistry". This agrees with check 1 of E1.7b: the car file's high-nickel
  cathode lies between NMC811 and NMC955 (Ni : Mn : Co about 0.87 : 0.06 : 0.06), not on one grade.

#### E1.7f Battery point 2: the cell format

**Why it matters for the elements.** The format decides the casing, and the casing is the largest difference between
cells (van de Ven et al. 2024, E1.7b, measured):
- **Cylindrical:** a nickel-plated steel can, 17 % of an 18650 cell's mass.
- **Pouch:** a laminated foil, 3.3 % of the cell. The car file's casing (2.5 %) is of this kind.

EPA 2013 (E1.7) gives the cell casing as 3 to 20 % of a pack, which spans both.

**What is known about robots** (E1.7c): no maker names its cells. The trade press says robot makers buy car makers'
cylindrical or pouch cells. A supplier's blog names 21700 cylindrical cells for Tesla Optimus, 21700 or pouch cells
for Unitree H1, and pouch solid-state cells for UBTECH Walker X and EngineAI.

**What the agreed masses imply:**

| Robot type | Cell mass | Format it fits |
|---|---|---|
| 1, 3, 4, 5 | From the energy, with the Wh/kg of cylindrical cells (E1.7d, agreed) | Cylindrical, by construction: every cell source read is cylindrical |
| 2 | Workbook, 4.5 kg (2.5 to 6.0) | Cylindrical NMC cells would weigh 3.8 to 4.2 kg: fits |
| 6 | Workbook, 9 kg (7 to 11) for 2.5 kWh, 278 Wh/kg at the mode | Above cylindrical cells (232 to 256); fits large car or pouch cells (285 to 330) |

**Not readable:** Waldmann et al. 2020 (housing of 18650 and 21700 cells): ScienceDirect refused the request
(2026-10-26).

**Proposal for Matthias:** cylindrical cells, with a nickel-plated steel can, for robot types 1 to 5; pouch cells,
with the car file's casing, for robot type 6. The share of the can and its elements come with the element recipe.

**Decided by Matthias, 2026-10-26**, asked which format all robots should share: "Cylindrical for all". Every robot
type gets cylindrical cells with a nickel-plated steel can.
- **Noted, not acted on:** robot type 6 keeps the workbook's 9 kg of cells (E1.7d). Cylindrical NMC cells for its
  2.5 kWh would weigh 9.8 to 10.8 kg, so at the mode the row is lighter than such cells.

#### E1.7g Battery point 3: silicon in the anode of the NMC cells

**The car file:** the high-nickel NMC anode holds 11.5 % Si as an element (the middle-nickel one 10.5 %), with the
rest carbon. It lists no oxygen, so the Si is not written as silicon oxide.

**Cylindrical NMC cells of the kind the robots use (21700, 4680), read:**

| Source | Cell | Kind | Read | Silicon in the anode |
|---|---|---|---|---|
| Chen, C.-H., Brosa Planella, F., O'Regan, K., Gastol, D., Widanage, W.D., Kendrick, E. (2020). Development of Experimental Techniques for Parameterization of Multi-scale Lithium-ion Battery Models. *J. Electrochem. Soc.* 167: 080534. https://iopscience.iop.org/article/10.1149/1945-7111/ab9050 | LG M50, 21700, NMC811 | Peer-reviewed **measurement** (EDS) of one cell type | Yes, the first 100,000 characters of the page | "the weight percentage of graphite and silicon oxide is 90% and 10% by weight"; SiOx with x = 0.64. That is **Si 7.3 % and O 2.7 %** of the anode (computed from the formula) |
| Sandia National Laboratories, Engine Combustion Network, *21700 M50LT*. https://ecn.sandia.gov/battery-safety/21700-m50lt/ | LG M50LT, 21700, NMC811 | National laboratory's page; its inventory is "from similar M50 cells" | Yes | "the anode is graphite with 1% silicon". Also: "the cell mass is 5.6% electrolyte"; a "stainless steel casing" |
| Ank et al. 2023 (E1.7b) | Tesla 4680, NMC811 | Peer-reviewed measurement of one cell | Yes | "no detectable presence of silicon" |
| Pham, T.A. et al. (2026). From cathode to anode: Understanding lithium loss in 21700-type Ni-rich NCM‖Graphite-SiOx cells. *J. Power Sources* 662. https://arxiv.org/abs/2511.05892 | A 21700 cell, maker not named | Peer-reviewed | Yes, the abstract page only | Graphite with SiOx; no share given. Not used for a number |

**Verdict:** the three cells measured hold 0, about 1 and 7.3 % Si in the anode. The car file's 11.5 % is above
all of them.

**Proposal for Matthias**, the same in every NMC robot type:
- Si in the anode: minimum 0 % (Tesla 4680), mode 1 % (LG M50LT, the middle of the three), maximum 7.3 % (LG M50).
- The Si comes as silicon oxide, so O = 0.365 kg per kg of Si (SiO0.64, Chen et al.).
- Graphite (C) is the remainder of the anode.

**Decided by Matthias, 2026-10-26**, choosing the answer offered: "Si in the anode 0 / 1 / 7.3 % as silicon oxide,
with graphite as the remainder, the same in every NMC robot type."

**Found on the way, for the element recipe (not proposed yet):**
- Sandia gives 5.6 % electrolyte for this 21700 cell, against 10 to 13 % in the car file's cells (E1.7b).
- Sandia names a stainless steel casing for the M50LT, while van de Ven et al. found nickel-plated steel in 18650
  cells. The elements of the can differ (stainless steel carries Cr and Ni).

#### E1.7h Battery point 4: the element recipe of the cylindrical cells, the sources

What is decided so far: cylindrical cells in every robot type (E1.7f); high-nickel NMC with the car file's liquid
electrolyte in robot types 1, 2, 4, 5 and 6, LFP in robot type 3 (E1.7e); 0 / 1 / 7.3 % Si as silicon oxide in the
NMC anode (E1.7g). The car file's cells have no steel can, so the build of a cylindrical cell is needed.

**1. How a cylindrical cell is built, by mass:**

| Part | LG M50, 21700, NMC811: Chen et al. 2020 | 18650 cells: van de Ven et al. 2024 | Car file, NMC high nickel, no can (E1.7b) |
|---|---|---|---|
| Can and cap | **16.6 %** (68.38 g with the can, "57 g without", measured) | **17 %** (nickel-plated steel), measured | 2.5 % (a thin casing) |
| Cathode coating (active material, binder, carbon) | 37.1 % | 44 % with its foil and some electrolyte | 46.0 % (active material) |
| Aluminium foil | 3.3 % | in the cathode | 5.2 % |
| Anode coating | 22.7 % | 32 % with its foil and some electrolyte | 22.2 % |
| Copper foil | 8.3 % | in the anode | 12.4 % |
| Electrolyte, separator, tabs, insulators | 11.9 % together | separator 3.6 %, "loss" (mostly electrolyte) 2.7 % | electrolyte 10.0 %, separator 1.7 % |

- **How the LG M50 column was computed:** the cell and the inner part were weighed by Chen et al. The coatings are
  their measured loadings (24.69 and 14.85 mg/cm²) times the coated areas (1027 and 1046.5 cm², Table II). The foils
  are their measured thickness (16.3 and 11.7 µm) times length (79 and 83.5 cm) and width (6.5 cm) times the
  handbook densities of aluminium (2.70 g/cm³) and copper (8.96 g/cm³). The rest is the difference.
- **Sandia** (E1.7g) gives 5.6 % electrolyte for the LG M50LT. With the LG M50 numbers, that leaves about 4.3 g
  (6 %) for separator, tabs and insulators.
- **Ohneseit et al. 2023** (below) measured the can wall: 0.23 to 0.27 mm in five 21700 cells.

**2. What each part is made of:**

| Part | What the sources say |
|---|---|
| Cathode | Decided: the car file's high-nickel NMC, and LiFePO4. Measured in 21700 cells: Ohneseit et al. found Li(x)Ni0.807Mn0.092Co0.102O2 (NMC811) and LiFePO4; Chen et al. and Ank et al. also NMC811. NMC811 holds less nickel than the car file's high-nickel grade (Ni 48 % against 53 % of the cathode). |
| Binder in the coatings | Ank et al. infer PVDF (C, H, F). No source read gives its share. |
| Anode | Decided: graphite with 0 / 1 / 7.3 % Si as silicon oxide. Ohneseit et al. measured "carbon +1.6% silicon" in the NMC cell, 1 to 1.4 % in the NCA cells and "no silicon" in the LFP cell. |
| Foils | Aluminium (cathode) and copper (anode), all sources. |
| Electrolyte | Solvents measured by Ohneseit et al. (GC-MS), mass %: NMC cell DMC 77.9, EMC 5.0, EC 17.1; LFP cell EMC 29.5, DEC 37.9, EC 32.6. Sandia: "78% dimethyl carbonate". The salt LiPF6 is 15 to 17 % of the electrolyte in the car file (from its Li, E1.7b). |
| Separator | Ohneseit et al.: polyethylene with an Al2O3 coating, in all five cells. The coating's share is not given. |
| Can | Sandia: "stainless steel casing" (LG M50LT). van de Ven et al.: nickel-plated steel (18650). Baazouzi et al.: hard cases are "usually made of aluminum or stainless steel". No source read gives the thickness of the nickel plating. |
| Tabs | Baazouzi et al.: "usually made of copper or nickel" for the anode and aluminium for the cathode. No mass given. |

**New sources read for this point:**

| Source | Kind | Read | Used for |
|---|---|---|---|
| Ohneseit, S., Finster, P., Floras, C., Lubenau, N., Uhlmann, N., Seifert, H.J., Ziebert, C. (2023). Thermal and Mechanical Safety Assessment of Type 21700 Lithium-Ion Batteries with NMC, NCA and LFP Cathodes. *Batteries* 9(5): 237. https://doi.org/10.3390/batteries9050237 | Peer-reviewed **measurement** (ICP-OES, CGHE, GC-MS, CT) of five commercial 21700 cell types, makers not named | Yes, in the browser, Tables 5 to 8 | Cathode, anode Si, separator, electrolyte solvents, can wall |
| Baazouzi, S., Feistel, N., Wanner, J., Landwehr, I., Fill, A., Birke, K.P. (2023). Design, Properties, and Manufacturing of Cylindrical Li-Ion Battery Cells—A Generic Overview. *Batteries* 9(6): 309. https://doi.org/10.3390/batteries9060309 | Peer-reviewed review with teardowns (Fraunhofer IPA) | Yes, in the browser, searched for materials and masses | Can and tab materials; it gives no masses |
| Chen et al. 2020 (E1.7g), read again for the masses | Measurement | Yes, the first 100,000 characters | The build of the LG M50 |

**Gaps, before any recipe:**
- The share of binder and conductive carbon in the coatings.
- The share of the Al2O3 coating on the separator.
- The can: stainless steel or nickel-plated steel, and the nickel plating's thickness.
- The build of an LFP cylindrical cell: no source read weighs its parts.

**No recipe is proposed yet.** Proposed since: E1.7i.

#### E1.7i Proposal: the element recipe of the cylindrical cells

Matthias, 2026-10-26, choosing the answer offered: "Yes, propose the element recipe of the NMC and LFP cylindrical
cells, min / mode / max, from these sources, with estimates (E) for the gaps. Show it to me before anything is
entered."

**Status: agreed by Matthias, 2026-10-26, choosing the answer offered: "I agree with the element recipe of the NMC
and LFP cylindrical cells as proposed in E1.7i." Entered the same day, on his word "Yes, build the battery entry as
laid out", in `data/researched/element_recipes.xlsx` (VERIFICATION.md V23).**

**Corrected while entering it:** the new check of 01 found that the active material and the binder could add up to
101 % of a coating at their maxima (cathode 98 + 3 %, anode 97 + 4 %), leaving the conductive carbon below zero. The
sandbox of V20 had not checked the coatings' remainders. Asked, Matthias chose "Lower active max": the active
material's maximum is one point lower, cathode 94 / 96 / **97** % and anode 95 / 96 / **96** %. The modes, and so the
table below, are unchanged.

**Level 1, the parts of an NMC cell** (robot types 1, 2, 4, 5, 6), % of the cell's mass:

| Part | Min | Mode | Max | Basis |
|---|---|---|---|---|
| Can and cap | 16.6 | 16.8 | 17.0 | LG M50 16.6 (Chen et al., measured) and 18650 17 (van de Ven et al., measured); mode the middle (E) |
| Cathode coating | 35.7 | 37.1 | 39.3 | LG M50 × f |
| Anode coating | 21.9 | 22.7 | 24.1 | LG M50 × f |
| Aluminium foil | 3.2 | 3.3 | 3.5 | LG M50 × f |
| Copper foil | 8.0 | 8.3 | 8.8 | LG M50 × f |
| The rest | 7.4 | 11.8 | 14.6 | **The remainder of the cell** (11.9 % in the LG M50) |
| — electrolyte, share of the rest | 23 % | 47 % | 70 % | E: van de Ven's "loss" 2.7 %, Sandia's 5.6 % and the car file's electrolyte in a can 8.5 %, each over 11.8 %; the top lowered from 72 to 70 % so that the last line never falls below 0 |
| — separator, share of the rest | 9 % | 13 % | 28 % | E: 1.1 % (Chen's 12 µm × two layers of an assumed 85 × 6.7 cm × polyethylene's 0.95 g/cm³ × an assumed 60 % solid), 1.5 % (the car file in a can), 3.6 % (van de Ven), each over 11.8 %; the top lowered from 31 to 28 % for the same reason |
| — tabs, insulators, other | | 4.7 % of the cell | | The remainder of the rest |

- **f** is the cell's energy per kg in the same draw (E1.7d) divided by its mode, 241.5 Wh/kg: 0.963 to 1.060. A
  cell that holds more energy per kg has heavier electrodes and a lighter rest. This pairs the recipe with the
  cell mass draw by draw.

**Level 1, the parts of an LFP cell** (robot type 3): no source weighs an LFP cylindrical cell, so the car file's
LFP cell is put in the same can (E). Its parts are multiplied by 83.2 / 97.5 = 0.853: the mass beside a 16.8 % can,
over the car cell's 97.5 % beside its own casing. This conversion is done once, on fixed numbers; no draw is divided
by a sum.

| Part | Min | Mode | Max | Basis |
|---|---|---|---|---|
| Can and cap | 16.6 | 16.8 | 17.0 | As for NMC |
| Cathode coating | 35.8 | 39.8 | 43.8 | Car file × 0.853, with the car file's own ±10 % |
| Anode coating | 17.7 | 19.7 | 21.7 | As above |
| Copper foil | 7.6 | 8.4 | 9.2 | As above |
| Aluminium foil | 3.2 | 3.5 | 3.9 | As above |
| Separator | 0.9 | 1.0 | 1.1 | As above |
| Electrolyte | 4.5 | 10.8 | 17.1 | **The remainder of the cell**; never below 0 |

**Level 2, the elements of each part:**

| Part | Elements | Basis |
|---|---|---|
| Can | Drawn as one of two states, 50 / 50 (E: one source for each). **Nickel-plated steel:** Ni 0.9 / 1.8 / 2.7 %, Mn 0.1 / 0.25 / 0.4 %, C 0.02 / 0.05 / 0.08 %, Fe the remainder. **Stainless 304:** Cr 18.1, Ni 8.1, C 0.04 %, Fe the remainder | Nickel: E, 1 / 2 / 3 µm a side on a 0.25 mm wall (Ohneseit et al.: 0.23 to 0.27 mm); no source read gives the plating. Mn and C: E, a deep-drawing steel, no source read. 304: Outokumpu's typical values (E1.4b); its Mn and Si, not in those values, stay in the Fe |
| Cathode coating | Active material 94 / 96 / 97 % (corrected, see above), PVDF binder 1 / 2 / 3 %, conductive carbon the remainder | E: no source read gives the shares. Active: the car file's high-nickel NMC (Li 7.1, Ni 52.6, Mn 3.6, Co 3.8, O 32.8 %), or LiFePO4 by its formula. PVDF by its formula (C, H, F) |
| Anode coating | Active material 95 / 96 / 96 % (corrected, see above), binder 2 / 3 / 4 %, conductive carbon the remainder | E. Active, NMC cells: graphite with 0 / 1 / 7.3 % Si as SiO0.64 (decided, E1.7g). LFP cells: graphite only (Ohneseit et al.: "no silicon"). Binder: half SBR, half sodium CMC (C, H, O, Na), E |
| Foils | Aluminium, copper | All sources |
| Electrolyte | LiPF6 12 / 15 / 17 %, the solvents the remainder | Salt: E from EPA (about 13 %) and the car file (15 to 17 %). Solvents in Ohneseit et al.'s measured mix: NMC DMC 77.9, EMC 5.0, EC 17.1 %; LFP EMC 29.5, DEC 37.9, EC 32.6 %. Elements from the formulas |
| Separator | Al2O3 coating 20 / 35 / 50 %, polyethylene the remainder | Coating found by Ohneseit et al.; its share is E, no source gives it |
| Tabs, insulators, other (NMC only) | Ni 6 %, Al 2 %, polypropylene the remainder | E: tabs of nickel and aluminium (Baazouzi et al.), the rest taken as polymer; the LG M50 does not say what this 4.7 % is |

**The result, % of the cell's mass.** At the modes, for each can, and the 95 % range of 200,000 draws in a sandbox
(V20; both cans drawn):

| Element | NMC, nickel-plated can | NMC, stainless can | NMC, 95 % of draws | LFP, nickel-plated can | LFP, stainless can | LFP, 95 % of draws |
|---|---|---|---|---|---|---|
| C | 29.7 | 29.7 | 27.3 to 30.6 | 25.4 | 25.4 | 23.7 to 27.1 |
| Ni | 19.3 | 20.4 | 18.8 to 21.2 | 0.3 | 1.4 | 0.2 to 1.4 |
| Fe | 16.5 | 12.4 | 12.3 to 16.6 | 30.0 | 25.9 | 25.0 to 30.9 |
| O | 14.7 | 14.7 | 13.9 to 15.9 | 20.1 | 20.1 | 19.4 to 20.9 |
| Cu | 8.3 | 8.3 | 8.1 to 8.7 | 8.4 | 8.4 | 7.8 to 9.1 |
| Al | 3.7 | 3.7 | 3.6 to 4.0 | 3.7 | 3.7 | 3.4 to 4.0 |
| P | 0.17 | 0.17 | 0.09 to 0.24 | 7.8 | 7.8 | 7.3 to 8.3 |
| Li | 2.6 | 2.6 | 2.5 to 2.7 | 1.75 | 1.75 | 1.6 to 1.9 |
| Cr | 0 | 3.0 | 0 to 3.1 | 0 | 3.0 | 0 to 3.1 |
| Co | 1.35 | 1.35 | 1.31 to 1.42 | — | — | — |
| Mn | 1.33 | 1.28 | 1.25 to 1.39 | 0.04 | 0 | 0 to 0.06 |
| F | 1.06 | 1.06 | 0.71 to 1.37 | 1.7 | 1.7 | 1.2 to 2.1 |
| H | 1.14 | 1.14 | 0.79 to 1.38 | 0.80 | 0.80 | 0.59 to 1.02 |
| Si | 0.22 | 0.22 | 0.09 to 1.37 | 0 | 0 | 0 |
| Na | 0.03 | 0.03 | 0.02 to 0.03 | 0.02 | 0.02 | 0.02 to 0.03 |

- The elements add up to 100.000 % in every draw, for both cells.
- **To know:** the car file's high-nickel cathode holds less cobalt (3.8 %) than the NMC811 measured in 21700 cells
  (about 6 %, E1.7h). With NMC811, the NMC cell's Co would be about 2.2 % instead of 1.35 %. The grade is decided;
  this is only noted. Matthias's reason for the one grade is in E1.7e: the car file's high nickel already mixes two
  high-nickel chemistries.

#### E1.7j The cell mass from the number of cells: the pack's voltage and capacity

Matthias, 2026-10-26, after the plan to enter the battery data was agreed and before anything was built: "The number
of cells, which also defines the cell mass depends on the voltage, which these batteries have and the robots use".
The build is paused until he agrees to this revision of E1.7d.

**The rule proposed:** cells in series = the pack's voltage / the cell's voltage; cells in parallel = the pack's
capacity / the cell's capacity, to the nearest whole number. A cell type builds the pack only if its whole cells come
within ±12 % of the stated capacity (E). Cell mass = number of cells × the mass of one cell, from its datasheet.
Each draw picks one of the cell builds that fit, all equally likely (E): a build is a discrete state, so it is drawn,
not blended into a triangle.

**What the packs are** (read 2026-10-26):

| Robot type | Pack | Source |
|---|---|---|
| 1, Unitree G1 | 13 cells in series, 9 Ah | The workbook ("9,000 mAh, 13S"); EEWorld (E1.7c) |
| 2, Unitree H2 | Maximum 75.6 V, so 18 cells in series (75.6 / 4.2 V); 15 Ah | Global Drone HQ (E1.7e) |
| 3, UBTECH Walker S2 | 48 V, so 15 LFP cells in series (48 / 3.2 V); 9 Ah; two packs | The workbook ("48 V, 9 Ah", "LiFePO4") |
| 4, AgiBot A2 | 14.4 Ah; "Charging Voltage 48V DC", so 13 or 14 NMC cells in series (700 Wh / 14.4 Ah = 48.6 V lies between) | AgiBot's own store, *AGIBOT A2 Ultra*, https://store.agibot.com/products/a2-ultra (69 kg, 169 cm, like the anchor robot); AgiBot's product page, https://agibot.com/products/A2: "Battery 700 wh", 69 kg. Read in the browser |
| 5, Boston Dynamics Atlas | About 2.5 kWh (the workbook); voltage and capacity not found | Searched: Boston Dynamics gives runtimes and a 3-minute swap, no voltage or capacity |
| 6, Guardian-X | Kept as in the workbook (decided, E1.7d) | — |

**Two further LFP cell sheets read for robot type 3:**

| Cell | Source | Kind | What it says |
|---|---|---|---|
| Enix Energies (NX) 26650, LFP | https://docs.rs-online.com/4ad1/0900766b812fdd10.pdf (part ACL9013) | Brand's sheet via a distributor | 2300 mAh, 3.2 V, 80 g |
| Antbatt 26650, LFP | https://www.antbatt.com/wp-content/uploads/2019/09/26650-3.2V-3800mAh-datasheet.pdf | Maker's sheet | 3800 mAh, 3.2 V, 87.5 g, "139.0Wh/kg" |
| Not used: a 3200 mAh LFP 26650 sheet (86 g) | Posted on a TI forum | Maker's sheet | Marked by its maker "strictly confidential", so not used in this public project |

**The cell builds, and the cell mass they give:**

| Robot type | Builds that fit (cells; pack capacity against stated) | Cell mass, kg: min / mode / max | E1.7d, from the energy |
|---|---|---|---|
| 1 | 35E 13S3P (39; +12 %), 50E 13S2P (26; +9 %), P45B 13S2P (26; 0 %) | 1.74 / 1.81 / 1.95 | 1.64 / 1.74 / 1.81 |
| 2 | 35E 18S4P (72; −11 %), 50E 18S3P (54; −2 %), P45B 18S3P (54; −10 %) | 3.60 / 3.61 / 3.75 | Kept as the workbook's 2.5 / 4.5 / 6.0 (decided); shown as a check only |
| 3 | A123 15S4P (120 over both packs; +11 %), Enix 15S4P (120; +2 %) | 9.12 / — / 9.60 | 4.75 / 6.35 / 8.31 |
| 4 | 35E 4P, 50E 3P and P45B 3P, each with 13 or 14 in series (39 to 56; −7 to +2 %) | 2.60 / 2.76 / 2.92 | 2.73 / 2.90 / 3.01 |
| 5 | No voltage or capacity: whole cells for 2.5 kWh. 35E 208, 50E 141, P45B 155, 4680 31 | 9.80 / 10.39 / 11.03 | 9.77 / 10.35 / 10.75 |

The mode is the median of the builds (E); the draws pick a build, so the mode only summarises.

**Robot type 3 does not fit:** the only cells read that build a 48 V, 9 Ah pack weigh 9.1 to 9.6 kg, 95 to 100 % of
the two packs' 9.6 kg in the parts list. That leaves nothing for the BMS, the wiring and the enclosure the parts list
names. The other LFP cells read miss the capacity (Antbatt −16 %, Keeppower +33 %, EVE +69 %). A cell of about 3 Ah
(three in parallel) would give about 7.7 kg, 80 % of the packs, but the only such sheet found is marked
confidential. So the cells read do not represent robot type 3's pack; that is Matthias's decision.

**What changes for the rest of each row** (E1.7d): robot type 1's rest 0.69 kg at the mode (was 0.76); robot type 4's
rest 6.7 kg to Not allocated (was 6.6); robot type 5's missing cell parts 3.4 kg from Not allocated (was 3.35).

#### E1.7k Robot type 3: LFP cells that build its 48 V, 9 Ah packs

Matthias, 2026-10-26, choosing the answer offered: "Search for a citable LFP cell sheet that builds a 48 V, 9 Ah pack
within the packs' 9.6 kg (for example about 3 Ah, three in parallel), and show me the sources."

**New sheets read, all public, none marked confidential:**

| Cell | Source | Kind | What it says |
|---|---|---|---|
| Antbatt 26650, LFP, 3.2 Ah | https://www.antbatt.com/wp-content/uploads/2019/09/26650-3.2V-3200mAh-datasheet.pdf | Maker's datasheet (Antbatt Co. Ltd.) | 3200 mAh, 3.2 V, 81.5 g, "125.6Wh/kg", 9.6 A continuous |
| Antbatt 26650MP, LFP, 3.0 Ah, high power | https://www.antbatt.com/wp-content/uploads/2019/09/26650MP-3.2V-3000mAh-datasheet.pdf | Maker's datasheet | 3000 mAh, 3.2 V, 81.5 g, "117.8Wh/kg", 30 A continuous |
| Power-Sonic PSL-FP-IFR18650EC, LFP, 1.5 Ah | https://cdn.power-sonic.com/documents/PSL-FP-IFR18650EC_Data_Sheet.pdf | Maker's datasheet (Power-Sonic Corporation) | 1.5 Ah, 3.2 V, 4.8 Wh, "Approximate Weight 0.09 lbs (40g)", an "energy cell" |

Seen only in shop listings, not used: 26650 LFP cells of 3.0 to 3.3 Ah at 81 to 88 g, and 32650 cells of 5 Ah at 137 to
150 g. They agree with the sheets above.

**Two tests for each cell, for two packs of 15 cells in series (48 V):**
- **Capacity:** its whole cells in parallel come within ±12 % of 9 Ah (E1.7j).
- **Mass:** its cells weigh at most 85 % of the packs' 9.6 kg, so that the BMS, wiring and enclosure the parts list
  names still fit. The 85 % is the largest share of cells van de Ven et al. weighed in battery modules (laptops 85 %,
  power banks 71 %, E1.7b), E. Robot types 1, 2 and 5 pass it with 65 to 79 %.

| Cell | Build (both packs) | Pack capacity | Cells, kg | Share of the 9.6 kg packs | Capacity | Mass |
|---|---|---|---|---|---|---|
| Antbatt 26650, 3.2 Ah | 15S3P × 2 = 90 | 9.6 Ah (+7 %) | 7.33 | 76 % | yes | yes |
| Antbatt 26650MP, 3.0 Ah | 15S3P × 2 = 90 | 9.0 Ah (0 %) | 7.33 | 76 % | yes | yes |
| Power-Sonic 18650, 1.5 Ah | 15S6P × 2 = 180 | 9.0 Ah (0 %) | 7.20 | 75 % | yes | yes |
| A123 26650, 2.5 Ah | 15S4P × 2 = 120 | 10.0 Ah (+11 %) | 9.12 | 95 % | yes | **no** |
| Enix 26650, 2.3 Ah | 15S4P × 2 = 120 | 9.2 Ah (+2 %) | 9.60 | 100 % | yes | **no** |
| Antbatt 26650, 3.8 Ah | 15S2P × 2 = 60 | 7.6 Ah (−16 %) | 5.25 | 55 % | **no** | yes |
| Keeppower 32700, 6 Ah | 15S2P × 2 = 60 | 12.0 Ah (+33 %) | 8.46 | 88 % | **no** | **no** |
| EVE 33140, 15.2 Ah | 15S1P × 2 = 30 | 15.2 Ah (+69 %) | 8.01 | 83 % | **no** | yes |

**Proposal for Matthias:** robot type 3's cells from the three builds that pass both tests, each drawn equally likely
(E): **7.20 / 7.33 / 7.33 kg** (min / mode / max). Against the workbook's row 7.5 / 8.5 / 9.5 kg, the rest is
1.17 kg at the mode, to Not allocated (E1.7d). The three cells agree closely, so the spread is narrow; the cells robot
type 3 really uses are not known (E1.7c).

---

### E1.8 Plastics

**The robots use:** PA66, ABS, PC, PC/ABS, PEEK, CF-PEEK, PA66-GF, TPU, silicone, Kevlar (aramid), Spectra
(UHMWPE).

**What the siblings hold:** VehicleComposition treats plastics as a material without elements.

**Independent sources:**

| Source | Kind | Read | What it says |
|---|---|---|---|
| Wikipedia, *Nylon 66*. https://en.wikipedia.org/wiki/Nylon_66 | Encyclopedia (second-hand) | Yes (extract) | Repeat unit (C12H22N2O2)n. |
| Wikipedia, *Polyether ether ketone*. https://en.wikipedia.org/wiki/Polyether_ether_ketone | Encyclopedia (second-hand) | Yes (extract) | Repeat unit (C19H12O3)n, 288.3 g/mol. |
| The other repeat units (PC, ABS, TPU, silicone, aramid, UHMWPE) | Standard chemistry | Not fetched | — |

**Verdict:**
- **What the formulas give:** the elements of the pure polymers: carbon, hydrogen, oxygen and nitrogen, plus silicon
  for silicone.
- **What no source gives:** the glass-fibre share of PA66-GF, the carbon-fibre share of CF-PEEK, and the fillers,
  flame retardants and pigments. A recipe for them would be an estimate.
- **Open, Matthias's decision:** whether plastics need elements at all, or stay "plastics". Their elements are not
  critical raw materials.

#### E1.8b Plastics: what the robots use, and the sources

Matthias, 2026-10-26, choosing the answer offered: "Yes, go on to material 8, plastics: show me what the robots use
and the sources first."

**What the robots use: the workbook's rows placed in Plastics** (sheet Materials of the shared lists):

| Robot type | Row in the workbook | Grade, as the workbook writes it | kg, min / mode / max | Where, from the parts list |
|---|---|---|---|---|
| 1 | Engineering polymers | PA66 / ABS / PC | 4.5 / 5.5 / 6.5 | Covers, brackets |
| 2 | Engineering plastics | PEEK / CF-PEEK / PC-ABS / PA66-GF | 6 / 7.5 / 11 | Shells, bushings, spacers, hand parts, bearing cages |
| 3 | Engineering plastics | ABS/PC / PA66-GF | 5.5 / 6.5 / 7.5 | Cladding, flame-retardant battery enclosures, actuator housings |
| 4 | Polymers & elastomers | PC/ABS / TPU / PA66-GF | 6 / 7.5 / 9.5 | Shell, soft-touch coating, hand structure, fingertip pads |
| 5 | Composites & polymers | CF-PEEK / PA66-GF | 3 / 5 / 8 | Shell panels, hand covers |
| 5 | Sealing elastomers | TPU / silicone | 1.5 / 2.5 / 4 | IP67 seals, boots, impact pads |
| 6 | Reinforced polymers | CF-PEEK / PA66-GF | 8 / 10 / 12 | Armour backing matrix, covers |
| 6 | Protective ballistic fibers | Kevlar 49 / Spectra (aramid / UHMWPE) | 2 / 3 / 5 | Spall liners, joint protection |

Robot type 1 has also received its battery pack's enclosure, glue and pads (E1.7d). The polymers inside other rows
(cable insulation of PTFE, PVC or FEP; fan impellers of PBT; Viton seals) belong to those rows, not here.

**Sources read, 2026-10-26:**

| Source | Kind | What it says |
|---|---|---|
| Wikipedia, *Nylon 66* and *Polyether ether ketone* (E1.8) | Encyclopedia | PA66 (C12H22N2O2)n; PEEK (C19H12O3)n |
| Wikipedia, *Acrylonitrile butadiene styrene*. https://en.wikipedia.org/wiki/Acrylonitrile_butadiene_styrene | Encyclopedia | (C8H8)x·(C4H6)y·(C3H3N)z; "The proportions can vary from 15% to 35% acrylonitrile, 5% to 30% butadiene and 40% to 60% styrene" (not said to be by mass) |
| Wikipedia, *Polycarbonate*. https://en.wikipedia.org/wiki/Polycarbonate | Encyclopedia | (C16H14O3)n; nothing on PC/ABS |
| Wikipedia, *Polydimethylsiloxane*. https://en.wikipedia.org/wiki/Polydimethylsiloxane | Encyclopedia | Repeat unit [Si(CH3)2O]; nothing on fillers in silicone rubber |
| Wikipedia, *Kevlar*. https://en.wikipedia.org/wiki/Kevlar | Encyclopedia | Repeat unit [-CO-C6H4-CO-NH-C6H4-NH-], that is C14H10N2O2 |
| Wikipedia, *Ultra-high-molecular-weight polyethylene*. https://en.wikipedia.org/wiki/Ultra-high-molecular-weight_polyethylene | Encyclopedia | The polyethylene repeat unit (in a picture, so (C2H4)n by the name); Spectra and Dyneema are UHMWPE fibres |
| Wikipedia, *Thermoplastic polyurethane*. https://en.wikipedia.org/wiki/Thermoplastic_polyurethane | Encyclopedia | Diisocyanates with short-chain diols (hard segments) and polyester or polyether soft segments; no proportions |
| Ernzen, J.R. et al. (2022). Tuning Thermal, Morphological, and Physicochemical Properties of Thermoplastic Polyurethanes (TPUs) ... *Polymers* 14(15): 3164. https://pmc.ncbi.nlm.nih.gov/articles/PMC9371192 | Peer-reviewed study | MDI with 1,4-butanediol (and DPG), polyester polyols; "~50 wt.% HS" (hard segment). One study, not a market average |
| US patent 8,586,491 B2 (2013), Owens Corning, quoting ASTM D578. https://patents.google.com/patent/US8586491 | Patent quoting the standard (the standard itself not read) | E-glass: SiO2 52–56, CaO 16–25, Al2O3 12–16, B2O3 5–10, MgO 0–5, Na2O+K2O 0–2, TiO2 0–0.8, Fe2O3 0.05–0.4, F 0–1.0 wt% |
| BASF, *Ultramid A3WG6 RC BK23372*, Product Information 02/2024 (download.basf.com) | Maker's datasheet | "a Polyamide 66, reinforced with 30% of glass fiber"; PA66-GF30; 1370 kg/m³ |
| Victrex, *VICTREX PEEK 450CA30*. https://cdn.victrex.com/en/downloads/datasheets/victrex-peek-450ca30 | Maker's datasheet | "30% carbon fibre reinforced PolyEtherEtherKetone (PEEK)"; 1.40 g/cm³ |
| Henan Xunyu Chemical, *Fumed silica for silicone rubber*. https://fumed-silica.net/applications/silicone-rubber/ | Supplier's page, a commercial interest | Fumed silica "5.0-35" wt% in HTV silicone rubber, "5-30" in LSR |
| Zhang, H., Yang, D., Wei, H., Yue, H., Gao, M., Shang, G. (2025). Research progress of flame retardant modified polycarbonate/acrylonitrile butadiene styrene alloys: a review. *PeerJ Materials Science*. https://doi.org/10.7717/peerj-matsci.39 | Peer-reviewed review, read in the browser | For UL94 V-0 in PC/ABS: organophosphorus (BDP, RDP, TPP) 10–12 wt%; brominated TBBPA + Sb2O3 10–15 wt%. The studies it cites use PC:ABS of 65:35, 7:3 and 9:1 |

**Elements of each polymer, from its formula** (computed with the atomic masses of 01, plus N 14.007):

| Polymer | C | H | O | N | Si |
|---|---|---|---|---|---|
| PA66 | 63.7 | 9.8 | 14.1 | 12.4 | |
| PC | 75.6 | 5.5 | 18.9 | | |
| PEEK | 79.2 | 4.2 | 16.6 | | |
| ABS, at the middle of its ranges (25 / 17.5 / 57.5) | 85.6 | 7.8 | | 6.6 | |
| Aramid (Kevlar) | 70.6 | 4.2 | 13.4 | 11.8 | |
| UHMWPE | 85.6 | 14.4 | | | |
| PDMS (silicone) | 32.4 | 8.2 | 21.6 | | 37.9 |
| TPU hard segment (MDI + BDO) | 67.0 | 5.9 | 18.8 | 8.2 | |

E-glass at the middle of ASTM D578's ranges holds O 47.8, Si 25.2, Ca 14.6, Al 7.4, B 2.3, Mg 1.5 % and traces.

**Verdict:**
- **The polymers are known by their formulas.** They bring C, H, O and N; silicone brings Si.
- **The fillers are known from one grade each:** 30 % glass in PA66-GF (BASF), 30 % carbon fibre in CF-PEEK
  (Victrex). The workbook names no grade number, so other shares (for example 15 or 50 %) are possible.
- **Gaps, before any recipe:**
  - how each robot's row splits among the polymers it names (for example robot type 2's PEEK / CF-PEEK / PC-ABS /
    PA66-GF); no source gives it;
  - the PC:ABS ratio in the robots (the studies use 65:35 to 9:1) and ABS's own monomer shares;
  - whether the flame-retardant enclosure of robot type 3 uses phosphorus or bromine, and how much;
  - TPU's soft segment (polyester or polyether) and its hard-segment share (one study: 50 %);
  - silicone rubber's silica (5 to 35 %, from a supplier only);
  - pigments and stabilisers, which no source here gives;
  - aramid against UHMWPE in robot type 6's ballistic fibres.
- **No recipe is proposed yet.** Proposed since: E1.8c.

#### E1.8c Proposal: the plastics recipe of each robot type

Matthias, 2026-10-26, choosing the answer offered: "Propose the plastics recipe per robot type, min / mode / max,
from these sources, with estimates (E) for the gaps. Show it to me before anything is entered."

**Status: agreed by Matthias, 2026-10-26, choosing the answer offered: "I agree with the plastics recipe as proposed in
E1.8c, including its four choices." After the verification of E1.8d, again choosing the answer offered: "Yes, take the
six verified values of E1.8d into the plastics recipe." The tables below hold them. Entered the same day, on his
word "Yes, enter the plastics recipe now as laid out", in `data/researched/element_recipes.xlsx` (VERIFICATION.md
V26).**

**Level 1, how each row splits among the polymers it names (E: no source gives it).** The first polymer the workbook
names is the remainder. Each of the other k − 1 polymers takes 1/(2k) / 1/k / 1/(k − 1) of the row, so all are
equal at the mode and the remainder never falls below zero.

| Robot type | Row | Remainder | The others, each (min / mode / max) |
|---|---|---|---|
| 1 | Engineering polymers | PA66 | ABS, PC: 17 / 33 / 50 % |
| 1 | The battery pack's enclosure, glue and pads (E1.7d) | PC/ABS, all of it | — |
| 2 | Engineering plastics | PEEK | CF-PEEK, PC/ABS, PA66-GF: 12.5 / 25 / 33 % |
| 3 | Engineering plastics | PC/ABS, flame-retardant | PA66-GF: 25 / 50 / 75 % |
| 4 | Polymers & elastomers | PC/ABS | TPU, PA66-GF: 17 / 33 / 50 % |
| 5 | Composites & polymers | CF-PEEK | PA66-GF: 25 / 50 / 75 % |
| 5 | Sealing elastomers | TPU | Silicone rubber: 25 / 50 / 75 % |
| 6 | Reinforced polymers | CF-PEEK | PA66-GF: 25 / 50 / 75 % |
| 6 | Protective ballistic fibers | Aramid | UHMWPE: 25 / 50 / 75 % |

**Level 2, what each polymer is made of:**

| Polymer | Its parts, min / mode / max | Basis |
|---|---|---|
| PA66, PC, PEEK, aramid, UHMWPE | Their formulas | E1.8b |
| ABS | Acrylonitrile 15 / **21** / 35 %, butadiene 5 / **20** / 30 %, styrene the remainder | Wikipedia's ranges; the modes from Bärwinkel et al. 2016 and Rutkowski & Levin 1986 (E1.8d) |
| PC/ABS | PC **60** / 70 / 90 %, ABS the remainder | Bärwinkel et al. 2016 (60 %, E1.8d) and the studies in Zhang et al. 2025 (65:35, 7:3, 9:1) |
| PC/ABS, flame-retardant (robot type 3 only, whose battery enclosures the workbook calls flame-retardant) | BDP 10 / 11 / 12 %, PC/ABS the remainder | Zhang et al. 2025: organophosphorus 10–12 % for UL94 V-0; BDP, a phosphate (C39H34O8P2, from its name), E |
| PA66-GF | Glass fibre **13** / 30 / 50 %, PA66 the remainder | DuPont Zytel 70G13 (13 %), BASF A3WG6 (30 %) and A3WG10 (50 %), E1.8d |
| E-glass | CaO 16 / 20.5 / 25, Al2O3 12 / 14 / 16, B2O3 5 / 7.5 / 10, MgO 0 / 2.5 / 5, Na2O 0 / 1 / 2, TiO2 0 / 0.4 / 0.8, Fe2O3 0.05 / 0.225 / 0.4, F 0 / 0.5 / 1 %, SiO2 the remainder (53.4 % at the modes) | ASTM D578 through US 8,586,491; the mode the middle of each range (E) |
| CF-PEEK | Carbon fibre 20 / 30 / 40 %, PEEK the remainder | Victrex's 30 % as the mode; the bounds E |
| Carbon fibre | **N 0.5 / 2 / 4.5 %, C the remainder** | Mitsubishi Rayon, US 4,814,157 (N 0.5–4.5 %); Toray T700S and Kim et al. 2016 (C over 93 %), E1.8d |
| TPU | Hard segment (MDI + butanediol, C19H20N2O4) **38.6 / 48.9 / 56.9** %; soft segment the remainder: polyester (poly(butylene adipate), C10H16O4) or polyether (PTMEG, C4H8O), drawn half and half | The three commercial grades in Santiago-Calvo et al. 2021; the soft segments from SONGWON, ChemicalBook and Wikipedia (E1.8d); the half and half E |
| Silicone rubber | Silica (SiO2) 5 / 20 / 35 %, PDMS the remainder | The silica supplier's 5–35 % |

The further atomic masses (N 14.007, B 10.81, Ca 40.078, Mg 24.305, Ti 47.867) are from the same IUPAC CIAAW table
as before, read 2026-10-26.

**The result, % of each row**, with the six verified values (at the modes; in brackets the 95 % of 20,000 draws in a
sandbox, V24 and V25):

| Robot type, row | C | O | H | N | Si | Ca | Al | P | Others |
|---|---|---|---|---|---|---|---|---|---|
| 1, Engineering polymers | 75.2 (71.7–78.5) | 11.0 | 7.8 | 6.0 (4.3–8.1) | | | | | |
| 1, battery pack enclosure | 78.8 | 13.2 | 6.3 | 1.7 | | | | | |
| 2, Engineering plastics | 71.8 (68.0–75.4) | 16.4 | 5.1 | 2.7 | 1.9 | 1.1 | 0.6 | | B 0.2, Mg 0.1, Na 0.1 |
| 3, Engineering plastics | 61.1 (51.7–67.8) | 19.0 | 6.5 | 5.1 | 3.7 (1.8–6.6) | 2.2 | 1.1 | 0.5 (0.3–0.7) | B 0.3, Mg 0.2, Na 0.1, F 0.1 |
| 4, Polymers & elastomers | 62.3 (56.1–68.0) | 21.0 | 6.7 | 4.8 | 2.5 | 1.5 | 0.7 | | B 0.2, Mg 0.2, Na 0.1, F 0.1 |
| 5, Composites & polymers | 64.7 (54.3–73.0) | 17.9 | 4.9 | 4.6 | 3.7 | 2.2 | 1.1 | | B 0.3, Mg 0.2, Na 0.1, F 0.1 |
| 5, Sealing elastomers | 44.7 (37.4–53.5) | 26.7 | 6.8 | 2.0 | 19.8 (12.2–27.6) | | | | |
| 6, Reinforced polymers | 64.7 (54.3–72.9) | 17.9 | 4.9 | 4.6 | 3.7 | 2.2 | 1.1 | | B 0.3, Mg 0.2, Na 0.1, F 0.1 |
| 6, Protective ballistic fibers | 78.1 (75.2–81.1) | 6.7 | 9.3 | 5.9 | | | | | |

**Choices in this proposal that are Matthias's:**
- the equal split of each row, with the first-named polymer as the remainder;
- the flame retardant only in robot type 3, and phosphorus-based (the review also names brominated ones, 10–15 %);
- robot type 1's battery enclosure as PC/ABS without flame retardant (the workbook does not call it flame-retardant);
- pigments and stabilisers are not itemised: no source gives them.

#### E1.8d The nine open points of the plastics recipe, verified on the web

Matthias, 2026-10-26: "Have you verified as much as possible with your own investigation in the internet. Add alwaus
the references". Then, choosing the answer offered: "Yes, verify the nine open plastics points on the web now, read
every source yourself, and show me the results with their references before anything is entered."

Every source below was opened and read on 2026-10-26: PDFs as text through PDFKit, web pages through the fetch tool
or in the browser.

| # | Point | Source read | Kind | What it says | Verdict |
|---|---|---|---|---|---|
| 1 | ABS proportions | Rutkowski, J.V., Levin, B.C. (1986). Acrylonitrile-Butadiene-Styrene Copolymers (ABS): Pyrolysis and Combustion Products and their Toxicity — A Review of the Literature. *Fire and Materials* 10: 93–105. https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=101640 | Review, US National Bureau of Standards | The SAN "can be composed of 65-76% styrene and 24-35% acrylonitrile"; "formulations of ABS plastics are rarely the same and poorly defined" | Wikipedia's ranges hold. With about 20 % rubber, 24–35 % of the SAN is 19–28 % of the ABS |
| 1 | ABS proportions | Bärwinkel, S., Seidel, A., Hobeika, S., Hufen, R., Mörl, M., Altstädt, V. (2016). Morphology Formation in PC/ABS Blends during Thermal Processing and the Effect of the Viscosity Ratio of Blend Partners. *Materials* 9(8): 659. https://pmc.ncbi.nlm.nih.gov/articles/PMC5509270/ | Peer-reviewed; three authors from Covestro, a PC/ABS maker | Emulsion-ABS of "50 wt % of polybutadiene" with a shell of 28 % acrylonitrile and 72 % styrene, mixed 1:1 with SAN of 24 % acrylonitrile and 76 % styrene | Its ABS is 25 % butadiene, 19 % acrylonitrile, 56 % styrene (computed) |
| 2 | Glass in PA66-GF | DuPont, *Zytel 70G13HS1L BK031* datasheet (copy at https://Protolabs.com/media/fclldzar/zytel-70g13hs1l.pdf) | Maker's datasheet | "13% glass fiber reinforced ... polyamide 66"; PA66-GF13 | The lowest grade read: 13 % |
| 2 | Glass in PA66-GF | BASF, *Ultramid A3WG10 CR BK00564*, Product Information 09/2026 (https://download.basf.com/p1/8a8081c57fd4b609017fd65cc5d26e20/en/ULTRAMID%25C2%25AE_A3WG10_CR_BLACK_00564) | Maker's datasheet | PA66-GF50 | The highest grade read: 50 %. With BASF's 30 % (E1.8b): 13 / 30 / 50 % |
| 3 | Carbon fibre in CF-PEEK | Victrex, *Product portfolio summary* (https://www.victrex.com/-/media/downloads/literature/en/victrex_productportfoliosummaryus.pdf) and *VICTREX PEEK 90HMF40* datasheet (https://cdn.victrex.com/-/media/downloads/datasheets/victrextds_90hmf40.pdf) | Maker's documents | Grades with 20 % (450CA20, 90HMF20), 30 % (90CA30, 150CA30, 450CA30, 650CA30) and 40 % carbon fibre (450CA40, 90HMF40) | **Confirmed:** 20 / 30 / 40 % |
| 4 | What carbon fibre holds besides carbon | US patent 4,814,157 (1989), Mitsubishi Rayon. https://patents.google.com/patent/US4814157A/en | Patent of a carbon fibre maker | "average nitrogen content in the whole carbon fibers which is measured by elementary analysis is 0.5-4.5% by weight" | The rest is mostly nitrogen, but only 0.5–4.5 %, not the 3–7 % of E1.8c |
| 4 | | Kim, M.-A., Jang, D., Tejima, S., Cruz-Silva, R., Joh, H.-I., Kim, H.C., Lee, S., Endo, M. (2016). Strengthened PAN-based carbon fibers obtained by slow heating rate carbonization. *Scientific Reports* 6: 22988. https://doi.org/10.1038/srep22988 | Peer-reviewed, read in the browser | Carbonisation removes "nitrogen, oxygen, and hydrogen ... leaving a material with at least 93 wt% of carbon content"; its measured numbers are in its supplement, not read | The rest is nitrogen, oxygen and hydrogen; agrees with Toray's ">93%" |
| 5 | The flame retardant BDP | PubChem, CID 9874825. https://pubchem.ncbi.nlm.nih.gov/compound/9874825 (read through its interface: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/bisphenol%20A%20bis(diphenyl%20phosphate)/property/MolecularFormula,MolecularWeight,IUPACName/JSON) | Chemical database of the US National Library of Medicine | C39H34O8P2, 692.6 g/mol | **Confirmed** |
| 6 | PC:ABS ratio | Bärwinkel et al. 2016 (row 1) | As above | "60 wt % of the polycarbonate, 20 wt % of the emulsion-ABS, and 20 wt % of the chosen SAN"; cites a 90/10 blend | 60 % PC, below E1.8c's lowest 65 % |
| 7 | TPU hard segment | Santiago-Calvo, M. et al. (2021). Analysis of the Foaming Window for Thermoplastic Polyurethane with Different Hard Segment Contents. *Polymers* 13(18): 3143. https://pmc.ncbi.nlm.nih.gov/articles/PMC8472128/ | Peer-reviewed | Cites "three different commercial TPU grades ... HS contents of 38.6 wt.%, 48.9 wt.%, and 56.9 wt.%" (Nofar et al. 2019) | Commercial grades: 38.6 / 48.9 / 56.9 % |
| 7 | TPU soft segments | Wikipedia, *Polytetrahydrofuran*. https://en.wikipedia.org/wiki/Polytetrahydrofuran | Encyclopedia | "(C4H8O)n"; "a starting material for thermoplastic polyurethane" | **Confirmed** |
| 7 | | SONGWON, *Polyester Diols* technical sheet V3.1. https://www.songwon.com/assets/images/contentModelImages/SONGWON_Technical_Sheet_Polyester-Diols_V3.1.pdf | Maker's sheet | Poly(1,4-butylene adipate), CAS 25103-87-1, from adipic acid and butanediol; "'S' Grade: Thermoplastic polyurethane" | The polyester soft segment is confirmed |
| 7 | | ChemicalBook, *Poly(1,4-butylene adipate)*. https://www.chemicalbook.com/ChemicalProductProperty_EN_CB0154123.htm | Chemical database | "(C6H10O4.C4H10O2)x", CAS 25103-87-1 | The repeat unit, minus two water, is C10H16O4 (computed): **confirmed** |
| 8 | Silica in silicone rubber | Ouyang, L., Wang, Z., Gong, D., Zhang, C. (2026). Preparation of Heat-Resistant Methyl Vinyl Phenyl Silicone Rubber and Study on Its Flexible Strain-Sensing Performance. *Polymers* 18(10): 1149. https://pmc.ncbi.nlm.nih.gov/articles/PMC13211187/ | Peer-reviewed, a phenyl silicone (a related kind) | Best at "30 phr SiO2 (Fumed silica)" with 100 phr rubber, 2 phr oil, 3 phr Si69 | About 22 % silica by mass (computed): agrees with E1.8c's mode of 20 % |
| 9 | UHMWPE | Wikipedia, *Polyethylene*. https://en.wikipedia.org/wiki/Polyethylene | Encyclopedia | "(C2H4)n"; "UHMWPE is polyethylene with a molecular weight numbering in the millions" | **Confirmed** |

**Seen only in search summaries, not used:** two patents naming commercial ABS with 15.6 % and about 22 % butadiene;
retailer and distributor listings of PA66-GF15 grades.

**What the verification changes in E1.8c** (taken in on Matthias's word, 2026-10-26: "Yes, take the six verified values
of E1.8d into the plastics recipe."):

| Point | Agreed (E1.8c) | From the sources read |
|---|---|---|
| ABS acrylonitrile, mode | 25 % | 21 % (Bärwinkel 19 %, NIST 19–28 %) |
| ABS butadiene, mode | 17.5 % | 20 % (Bärwinkel 25 %, Wikipedia 5–30 %) |
| PC in PC/ABS, minimum | 65 % | 60 % (Bärwinkel) |
| Glass in PA66-GF, minimum | 15 % | 13 % (DuPont) |
| Carbon fibre | C 93 / 95 / 97 %, N the rest | N 0.5 / 2 / 4.5 % (Mitsubishi Rayon), C the rest |
| TPU hard segment | 30 / 40 / 50 % | 38.6 / 48.9 / 56.9 % (the three commercial grades) |
| CF-PEEK 20 / 30 / 40 %; BDP; PTMEG and PBA; silica 5 / 20 / 35 %; UHMWPE | — | Confirmed, unchanged |

At the modes, these changes move no element of any robot type's row by more than 0.5 percentage points (V25): for
example robot type 5's composites C 64.2 → 64.7 % and N 5.1 → 4.6 %, robot type 1's polymers N 6.3 → 6.0 %.

---

### E1.9 Fibre composites

**The robots use:**
- robot type 1: CFRP, grade not given;
- robot type 2: CFRP with T700 / T800 fibre;
- robot type 3: CFRP / GFRP.

**What the siblings hold:** nothing.

**Independent sources:**

| Source | Kind | Read | What it says |
|---|---|---|---|
| Toray Composite Materials America, *TORAYCA T700S*, data sheet, Rev. 11/24/2025. https://www.toraycma.com/wp-content/uploads/T700S-Data-Sheet.pdf | Manufacturer's data sheet | Yes | "Chemical Composition: Carbon >93%". |
| E-glass, ASTM D578 (through patents US 8,586,491 and others, and an ECHA dossier; search results only) | Patents quoting the standard | No | SiO2 52–62, CaO 16–25, Al2O3 12–16, B2O3 0–10, MgO 0–5, Na2O+K2O 0–2, TiO2 0–1.5 wt%. |

**Verdict:**
- **The fibres are known:** carbon fibre is mostly carbon (over 93 %). E-glass is known through second-hand quotes
  of ASTM D578.
- **What no source gives:** the share of fibre and resin in the robots' composites. Usual laminates have 50–60 %
  fibre by volume, but no source here states it for the robots, so it would be an estimate.

#### E1.9b Fibre composites: what the robots use, and the sources, verified on the web

Matthias, 2026-10-26, choosing the answer offered: "Yes, go on to material 9, fibre composites: show me what the robots
use and the sources first, verified on the web with references."

**What the robots use: the workbook's rows placed in Fibre composites** (sheet Materials of the shared lists). Robot
types 5 and 6's CF-PEEK went to Plastics (E1.8c).

| Robot type | Row in the workbook | Grade, as the workbook writes it | kg, min / mode / max | Where, from the parts list |
|---|---|---|---|---|
| 1 | Carbon-fiber composite | CFRP, unspecified grade | 0.8 / 1.2 / 1.6 | Shell segments of the external shell |
| 2 | Carbon-fiber composite | CFRP, T700 / T800 assumption | 0.5 / 1.5 / 3.0 | Selective reinforcement of the structural frame |
| 3 | Fiber composites | CFRP / GFRP | 3.0 / 4.5 / 6.0 | Reinforcements of the main structural frame |

**Sources read, 2026-10-26** (PDFs as text through PDFKit, web pages through the fetch tool or in the browser):

| Part | Source | Kind | What it says |
|---|---|---|---|
| Carbon fibre | Toray, *TORAYCA T700S* data sheet (E1.9). https://www.toraycma.com/wp-content/uploads/T700S-Data-Sheet.pdf | Maker's datasheet | "Chemical Composition: Carbon >93%" |
| Carbon fibre | Toray, *TORAYCA T800S* data sheet. https://www.toraycma.com/wp-content/uploads/T800S-Data-Sheet.pdf | Maker's datasheet | "Chemical Composition: Carbon >96%" |
| Carbon fibre | Mitsubishi Rayon, US 4,814,157 (E1.8d). https://patents.google.com/patent/US4814157A/en | A carbon fibre maker's patent | Nitrogen 0.5–4.5 % by elemental analysis; already the recipe 'Carbon fibre' in element_recipes.xlsx (N 0.5 / 2 / 4.5 %, C the rest) |
| Fibre and resin in CFRP | Hexcel, *HexPly 8552* product data sheet. https://www.hexcel.com/wp-content/uploads/2026/01/HexPly_8552_us_DataSheet-1.pdf | Maker's datasheet | "an amine cured, toughened epoxy resin system supplied with unidirectional or woven carbon or glass fibers"; resin content 33–38 % (carbon tapes) and 32–42 % (carbon fabrics) of the prepreg, so 58–68 % fibre by mass |
| Epoxy resin | PubChem, bisphenol A diglycidyl ether (DGEBA), CID 2286. https://pubchem.ncbi.nlm.nih.gov/compound/2286 | Chemical database | C21H24O4, 340.4 g/mol |
| Hardener, aromatic | PubChem, dapsone (4,4'-diaminodiphenyl sulfone, DDS), CID 2955. https://pubchem.ncbi.nlm.nih.gov/compound/2955 | Chemical database | C12H12N2O2S, 248.30 g/mol |
| Hardener, cycloaliphatic | PubChem, 4,4'-methylenebis(2-methylcyclohexylamine), CID 91555. https://pubchem.ncbi.nlm.nih.gov/compound/91555 | Chemical database | C15H30N2, 238.41 g/mol |
| Mix ratio | Huntsman, *ARALDITE LY 564 / ARADUR 2954*. https://products.huntsman.com/products/araldite-ly-564-aradur-2954 (read in the browser) | Maker's product page | "a low-viscosity epoxy resin, formulated liquid amine hardener. Used in aerospace and industrial composites"; "Mix Ratio 0.35 %(W) Hardener : Resin", that is 35 parts hardener per 100 resin |
| Glass fibre | ASTM D578 through US 8,586,491 (E1.8b); already the recipe 'E-glass' in element_recipes.xlsx | Patent quoting the standard | E-glass oxides |
| Glass in GFRP | Avient, *Glasforms Pultruded Rods, Tubes & Custom Profiles*. https://www.avient.com/node/10713 | Maker's page | Glass-fibre profiles: "Glass Content, % by weight" 65–75 (ASTM D2584); resins polyester, vinyl ester and epoxy |
| Glass in GFRP | Łukasiewicz Institute of Electrical Engineering, *Profiles glass-epoxy*. https://iel.lukasiewicz.gov.pl/wp-content/uploads/sites/24/2024/10/Profiles-glass-epoxy.pdf | Maker's datasheet | Epoxy resin, E-glass; "Glass content in the plastic (by weight) >79 %" (PN-EN ISO 1172) |
| Atomic mass of S | IUPAC CIAAW 2024. https://www.ciaaw.org/abridged-atomic-weights.htm | Standard table | S 32.06 |

**Checks made with the numbers read:**
- At the stoichiometric ratio (two epoxy groups per DGEBA, four amine hydrogens per diamine), DGEBA takes 36.5
  parts DDS or 35.0 parts of the cycloaliphatic diamine per 100. The 35 parts agree with Huntsman's mix ratio.
- Elements, computed from the formulas (%):

| | C | O | H | N | S | Others |
|---|---|---|---|---|---|---|
| Epoxy, DGEBA + DDS | 69.8 | 17.2 | 6.5 | 3.0 | 3.5 | |
| Epoxy, DGEBA + cycloaliphatic diamine | 74.5 | 13.9 | 8.6 | 3.0 | | |
| CFRP, 62 % carbon fibre (the middle of Hexcel's 58–68 %) in the second epoxy | 89.1 | 5.3 | 3.2 | 2.4 | | |
| GFRP, 70 % E-glass (the middle of Avient's 65–75 %) in the second epoxy | 22.3 | 37.4 | 2.6 | 0.9 | | Si 17.5, Ca 10.3, Al 5.2, B 1.6, Mg 1.1, Na 0.5 |

**Not read, or seen only in search summaries, and not used:**
- the safety data sheet of HexPly 8552S (its page came back empty); a search summary says it lists an epoxy
  (TGMDA) at 15–40 % and dapsone at 1–15 %;
- distributors' Toray T700S and T800S prepregs with 37 and 43 % resin (the pages could not be opened);
- that ARADUR 2954 is this cycloaliphatic diamine: only a search summary of a recycling study says so; Huntsman's
  page names only "formulated liquid amine hardener".

**Verdict:**
- **The fibres are known first-hand:** carbon fibre over 93 % (T700S) and over 96 % carbon (T800S), the rest mainly
  nitrogen; E-glass by ASTM D578. Both recipes already exist in element_recipes.xlsx.
- **The fibre content is known from makers:** CFRP prepregs 58–68 % carbon fibre by mass (Hexcel); GFRP profiles 65 to
  over 79 % glass (Avient, Łukasiewicz).
- **The matrix is known only by its kind:** "amine cured epoxy" (Hexcel, Huntsman). Which hardener, aromatic (with
  sulphur) or cycloaliphatic, no source says for robots.
- **Gaps, before any recipe:**
  - the robots' resin and hardener (the robots' makers publish neither);
  - CFRP against GFRP in robot type 3's row;
  - the fibre sizing (a thin coating), which no source here gives;
  - whether robot shells use the prepreg's fibre content or a lower one (wet lay-up, short fibres).
- **No recipe is proposed yet.** Proposed since: E1.9c.

#### E1.9c Proposal: the fibre-composite recipe of each robot type

Matthias, 2026-10-26, choosing the answer offered: "Propose the fibre-composite recipe per robot type, min / mode /
max, from these sources, with estimates (E) for the gaps, verified on the web with references. Show it to me before
anything is entered."

**Status: agreed by Matthias, 2026-10-26, choosing the answer offered: "I agree with the fibre-composite recipe as
proposed in E1.9c, including its four choices." Entered the same day, on his word "Yes, enter the fibre-composite
recipe now, as with the plastics", in `data/researched/element_recipes.xlsx` (VERIFICATION.md V28). The two epoxies
are alternatives within an item 'Epoxy system' of the recipe 'Epoxy'.**

**The gaps, checked on the web first (2026-10-26):**

| Gap | Source read | Kind | What it says | Used for |
|---|---|---|---|---|
| Sizing on carbon fibre | Toray, *TORAYCA T700S* data sheet, Rev. 11/24/2025. https://www.toraycma.com/wp-content/uploads/T700S-Data-Sheet.pdf | Maker's datasheet | Sizing types and amounts: "50C (1.0 %) Epoxy, phenolic, polyester, vinyl ester"; "60E (0.2 %) Epoxy"; "F0E (0.6 %) Vinyl ester, compatible with epoxy" | Sizing 0.2 / 0.6 / 1.0 % of the fibre; its chemistry not given, taken as epoxy (DGEBA), E |
| Fibre content below prepreg | Explore Composites!, *Basic Numbers and Calculations for Composites*. https://explorecomposites.com/articles/design-for-composites/basic-numbers-and-calculations-for-composites/ | A hobbyist's website: its author writes he is "not a real engineer"; weak | Fibre volume: open moulded "20-40%", vacuum-bagged wet lay-up and infusion "40-55%", prepreg "50-70%"; carbon 1.75–2, E-glass 2.55–2.6, epoxy 1.2–1.45 g/cm³ | Only for the lower bounds below, as an estimate (E) |
| Which epoxy | none found | — | No robot maker names its resin | The two amine epoxies of E1.9b, half and half (E) |
| CFRP against GFRP in robot type 3 | none found | — | — | The rule of the plastics (E1.8c): the first named the remainder, the other 25 / 50 / 75 % (E) |

**Level 1, each robot type's row:**

| Robot type | Row | Recipe |
|---|---|---|
| 1 | Carbon-fiber composite | CFRP, all of it |
| 2 | Carbon-fiber composite | CFRP, all of it (T700 or T800 fibre: both over 93 % carbon, the recipe 'Carbon fibre') |
| 3 | Fiber composites | CFRP the remainder; GFRP 25 / 50 / 75 % (E) |

**Level 2, the recipes:**

| Recipe | Its parts, min / mode / max | Basis |
|---|---|---|
| CFRP | Carbon fibre (sized) **50 / 62 / 68 %** by mass, epoxy the remainder | Mode and maximum: Hexcel HexPly 8552, resin 32–42 %, so fibre 58–68 % (E1.9b), the middle 62 %. Minimum: 40 % fibre by volume (vacuum-bagged or infused, Explore Composites!) is 50 % by mass with carbon 1.8 and epoxy 1.2 g/cm³ (computed), E |
| Carbon fibre, sized | Sizing 0.2 / 0.6 / 1.0 %, taken as DGEBA; carbon fibre the remainder | Toray T700S (above); the sizing's chemistry E |
| Carbon fibre | N 0.5 / 2 / 4.5 %, C the remainder | Already in element_recipes.xlsx (E1.8d) |
| GFRP | E-glass **59 / 70 / 80 %** by mass, epoxy the remainder | Mode: Avient's 65–75 %, the middle. Maximum: Łukasiewicz "> 79 %". Minimum: 40 % by volume is 59 % by mass with glass 2.58 and epoxy 1.2 g/cm³ (computed), E. Avient also uses polyester and vinyl ester; epoxy is taken throughout, E |
| E-glass | ASTM D578 oxides | Already in element_recipes.xlsx (E1.8c) |
| Epoxy | Aromatic amine or cycloaliphatic amine, drawn half and half | E: no source says which robots use |
| Epoxy, aromatic amine | DDS 36.5 parts per 100 DGEBA (26.7 %), DGEBA the remainder | The stoichiometric ratio from the PubChem formulas (E1.9b); Hexcel 8552 is "amine cured" |
| Epoxy, cycloaliphatic amine | Diamine 35 parts per 100 DGEBA (25.9 %), DGEBA the remainder | Huntsman's mix ratio, 35 per 100, which the stoichiometry confirms (E1.9b) |

Not itemised: the sizing on glass fibre; no source read gives it.

**The result, % of each row, at the modes** (V27: 20,000 draws, every row adds up to 1, no element below zero):

| Row | With the aromatic epoxy | With the cycloaliphatic epoxy | 95 % of the draws (both epoxies drawn) |
|---|---|---|---|
| CFRP, robot types 1 and 2 | C 87.2, O 6.6, H 2.5, N 2.4, S 1.3 | C 89.0, O 5.4, H 3.3, N 2.4 | C 84.5–89.9, O 4.9–8.1, N 1.7–3.6, S 0–1.6 |
| Robot type 3, CFRP and GFRP | C 54.1, O 22.5, Si 8.7, Ca 5.1, Al 2.6, H 2.2, N 1.6, S 1.2, B 0.8, Mg 0.5 | C 55.7, O 21.4, Si 8.7, Ca 5.1, H 2.9, Al 2.6, N 1.7, B 0.8, Mg 0.5 | C 41.3–67.5, O 15.8–28.5, Si 5.2–12.5, Ca 3.0–7.6 |
| GFRP alone, for comparison | O 38.4, C 20.9, Si 17.5, Ca 10.3, Al 5.2 | O 37.4, C 22.3, Si 17.5, Ca 10.3, Al 5.2 | — |

The further atomic mass, S 32.06, is from the IUPAC CIAAW table (E1.9b).

**Choices in this proposal that are Matthias's:**
- the two epoxies, half and half;
- robot type 3's split, CFRP the remainder and GFRP 25 / 50 / 75 %;
- the lower bounds of fibre content, which rest on a weak source;
- the glass fibre's sizing left out.

---

### E1.10 Electronics

**The robots use:**
- robot type 1: Silicon / FR-4;
- robot type 2: FR-4 / glass / silicon;
- robot type 3: the split electronics of point 9;
- robot type 4: face glass / silicon IC material;
- robot type 5: FR-4 / silicon / optical glass;
- robot type 6: FR-4 / silicon / solder.

These are circuit boards and chips, with glass of displays and lenses in robot types 2, 4 and 5.

**What the siblings hold:**
- **VehicleComposition, sheet `ElectronicsPCB`** (source "EVA2"), the metals of car boards: Cu 2.5–7.4 %, Al
  1.1–2.2 %, Ag 0.03–0.05 %, Au 0.005–0.023 %, Pd 0.001–0.004 %.
- **RAWCLICDataCenters, EVIDENCE.md §15:** board metals per cm² of board, from the literature (Charles et al. 2017,
  DIMMs measured; Bizzo et al. 2014) adjusted for today's boards, and lead-free solder (SAC305).

**Independent sources:**

| Source | Kind | Read | What it says (wt% of whole boards with components) |
|---|---|---|---|
| Bizzo, W.A., Figueiredo, R.A., de Andrade, V.F. (2014). Characterization of Printed Circuit Boards for Metal and Energy Recovery after Milling and Mechanical Separation. *Materials* 7(6): 4555–4566. https://doi.org/10.3390/ma7064555; read at https://pmc.ncbi.nlm.nih.gov/articles/PMC5455934/ | Peer-reviewed **measurement** (aqua regia digestion, AAS and ICP) of about 12 kg of boards from discarded PCs (XT, 486, Pentium) | Yes (extract): Table 3 | Cu 14.2, Sn 4.79, Pb 2.50, Fe 3.08, Ni 0.41, Zn 0.18, Sb 0.05, Ag 317 ppm, Au 142 ppm; metals 27.6 % in total. Brominated flame retardants named, not measured. |
| Szałatkiewicz, J. (2014). Metals Content in Printed Circuit Board Waste. *Pol. J. Environ. Stud.* 23(6): 2365–2369. https://www.pjoes.com/Metals-Content-in-Printed-Circuit-Board-Waste,89421,0,2.html | Peer-reviewed | Abstract only; the numbers are in the PDF, not read | Boards of PCs, mobile phones and mixed waste; gold, palladium and copper the most valuable. |
| Wu et al. (2017), review of copper and precious metals from waste boards, *Front. Environ. Sci. Eng.* 11(5): 8. https://academic.hep.com.cn/fese/EN/Y2017/V11/I5/8 | Peer-reviewed review | **No:** site down for maintenance (26–29 October 2026) | Search snippet only: Cu 16–40, Sn 1–9, Pb 0.8–5.5 %. |
| Holgersson et al. (2018), metals of the boards of routers, mobile phones and smartphones, *Resour. Conserv. Recycl.* 133: 300–308 | Peer-reviewed measurement | No: not open | Lead lower in modern smartphones. |

**Verdict: the siblings and the literature disagree by a factor of 2–5 on copper.**
- **Copper:** VehicleComposition's EVA2 boards hold 2.5–7.4 % copper; Bizzo's measured PC boards 14.2 %; Wu's review
  16–40 %. The EVA2 basis (whole components or boards only) is not stated in the sheet.
- **Not representative:** Bizzo's boards are old and soldered with lead, and today's boards are lead-free. Robot
  compute boards (Jetson, Orin, RK3588) are closer to the data-centre and phone boards than to old PC boards.
- **Open, Matthias's decision:** which basis to use: RAWCLICDataCenters' adjusted board metals, a measured modern
  board, or an estimate. Glass of displays and lenses needs its own small recipe.

---

### E1.11 Ceramics

**The robots use:** alumina (Al2O3) and silicon carbide (SiC) armour plates, robot type 6 only.

**What the siblings hold:** nothing.

**Independent sources:**

| Source | Kind | Read | What it says |
|---|---|---|---|
| CoorsTek, *Advanced Alumina* datasheet (2017). https://www.coorstek.com/media/4235/advanced-alumina.pdf | Manufacturer's datasheet | Yes: the grade line | AD-94 nominal 94 % Al2O3, AD-96 96 %, FG-995 98.5 %, AD-995 99.5 %, AD-998 at least 99.8 %, PlasmaPure at least 99.9 %. Densities 3.70–3.92 g/cm³. |
| MatWeb (search result only) | Database | No | CoorsTek armour grades CAP 3 (99.5 %) and CAP 4 (98.5 %). |

**Verdict:**
- **Alumina:** armour alumina is 96–99.5 % Al2O3. The elements follow from the formula (Al 52.9 %, O 47.1 % of
  Al2O3); the rest is sintering aids that no source here names.
- **SiC:** Si 70.0 %, C 30.0 % by formula.
- **Open:** the workbook does not split robot type 6's 6 kg into alumina and SiC.

---

### E1.12 Summary

| Material | Sibling data | Independent check | Verdict |
|---|---|---|---|
| Aluminium | VehicleComposition, 6061 and 7075 | Teal Sheets, Dec 2025; further alloys (E1.1b): Teal and Pink Sheets, JIS H 5302 | **Confirmed**, exactly; 6082, 5052, 5083 and five die-casting alloys (A380, 383, 384, A360, ADC12) added from robot sources |
| Magnesium | VehicleComposition, AZ91C / AM60A | ICAST datasheets (ASTM B94); producers' limits compiled by TMS (E1.2b) | Al and Mn agree; the **grades differ** (the robots use AZ91D / AM60B); the car file's AZ91C adds up to 100.365 % (E1.2b) |
| Titanium | none | voestalpine datasheet (ASTM B348) | New; the standard not read |
| Steel | TractionMotor, electrical steel M19 | ASTM A677 scope; Alro, Astrup, Total Materia | Electrical steel **confirmed**. Bearing and gear steels new, from datasheets. Two steels have no grade. |
| Copper | TractionMotor, ETP | KEMPER | **Confirmed** |
| Magnets | TractionMotor; VehicleComposition | Yang et al. 2017 (review, MORE); patents, NIMS/MEXT | **Not confirmed:** the siblings' Co (4–12 %) and total rare earths (33–42 %) exceed the review's 5 % and 31–32 %. Dy 6–10 % confirmed for motors. |
| Battery materials | Battery project (car packs, elements) | EPA 2013, Table 2-1; formulas; van de Ven et al. 2024 (measured); Ank et al. 2023 | Cathodes **confirmed** by their formulas; the cell build agrees with measured pouch cells; electrolyte, separator and casing **lack elements**; no steel can for cylindrical cells. Robot types 3 and 4 hold 2.3 and 4.2 times the cells their energy needs (E1.7b). **Argonne not readable** |
| Plastics | none | formulas (Wikipedia) | Polymer elements known; fillers and fibre shares not given |
| Fibre composites | none | Toray T700S; ASTM D578 through patents | Fibres known; the fibre share not given |
| Electronics | VehicleComposition (EVA2); DataCenters | Bizzo et al. 2014 (measured) | **Disagree:** Cu 2.5–7.4 % against 14.2 % measured; Bizzo's boards are old and leaded |
| Ceramics | none | CoorsTek | Purity confirmed; the alumina/SiC split is open |
| Mixed, Not allocated | — | — | No recipe possible |

### E1.13 What was not read, and why

- **The standards themselves** (paywalled): ASTM B94, B348, A295, D578; EN 10083-3, EN 13601; GB/T 3077, 18254. Read
  instead through datasheets that cite them.
- **Blocked (HTTP 403):** Argonne's GREET memos, Dai et al. 2019 (MDPI) and copper.org.
- **Site down for maintenance:** Wu et al. 2017.
- **Seen only as abstracts or search summaries, not used for any number:** Szałatkiewicz 2014, Holgersson 2018, the
  patents and the NIMS/MEXT digest; Waldmann et al. 2020 (*J. Power Sources* 472: 228614, 18650 against 21700 cells,
  https://doi.org/10.1016/j.jpowsour.2020.228614), whose housing shares of about 20 and 18 wt% were seen only in a
  search summary.
- **Not answered from the IEA:** its 2021 report on critical minerals was found, but no battery mineral intensities
  were read from it.
