# Research Report: Advancements in Humanoid Robot Subsystems and Materials

**Report Date:** 2026-04-21

## Executive Overview
This report provides a detailed technical analysis of the critical subsystems that constitute modern humanoid robots, focusing on electric motors, actuators, wiring systems, sensors, onboard controllers, and material allocation strategies. The objective is to present a comprehensive overview of current specifications, prevailing design philosophies, and technological trends shaping the industry. The analysis reveals a strong emphasis on maximizing performance metrics such as torque density and computational power while minimizing mass to overcome the "mass penalty spiral." Key findings indicate a convergence towards highly integrated, lightweight designs utilizing advanced materials like titanium alloys, carbon fiber composites, and high-performance polymers such as PEEK [14, 16, 17]. Each section presents data in both tabular and narrative formats, detailing specifications, component counts, and comparative analyses across different robot classes and manufacturers, supported by recent industry and academic research.

---

## Electric Motors and Actuators

The performance of a humanoid robot is fundamentally dictated by the capabilities of its actuation system. These systems must deliver high power and torque for dynamic movements like walking, running, and lifting, yet be lightweight, efficient, and robust enough to endure thousands of high-impact cycles [1]. The design of electric motors and actuators is a critical balancing act, governed by the need to escape the "mass penalty spiral," a phenomenon where any additional mass requires more powerful, and thus heavier, actuators, leading to a cascading increase in total system weight and energy consumption [1]. For instance, an excess of just 200 grams in an ankle actuator can translate to a system-level weight penalty of 1.3 kg [1]. Consequently, specific torque (Nm/kg) for rotary actuators and specific force (N/kg) for linear actuators have become the paramount performance metrics [1].

### Actuator Specifications and Architectures

Modern humanoid robots employ a "convergent solution" that typically involves a split architecture [1]. Rotary actuators are predominantly used for joints that require continuous, high-speed rotation, such as hips, knees, ankles, shoulders, and elbows. Linear actuators are often reserved for joints that must absorb significant shock loads, lift heavy weights, or where compact packaging is essential, such as in finger mechanisms or parallel hip linkages [1]. State-of-the-art rotary actuators target a specific torque greater than 10 Nm/kg, with high-demand joints like the hip and knee requiring peak torque densities exceeding 30 Nm/kg [1, 2]. The ZHR-H Series, for example, achieves up to 36 Nm/kg [2]. Linear actuators in viable humanoid applications, such as those using planetary roller screws or hydraulic cylinders, aim for a specific force exceeding 4,000 N/kg, with some hydraulic systems reaching over 10,000 N/kg [1].

A critical design consideration is **back-drivability**, which is the ability of an actuator to yield to external forces. This is essential for shock absorption during impacts, such as heel strikes in walking, which can exert forces two to three times the robot's body weight and occur approximately 5,000 times per hour [1]. Industrial actuators with self-locking mechanisms are unsuitable as they can lead to shear failure under such dynamic loads [1]. To achieve high back-drivability and low reflected inertia, modern humanoid designs favor **Quasi-Direct Drive (QDD)** transmissions with low gear ratios, typically ranging from 6:1 to 30:1 [1, 3]. Common QDD configurations include cycloidal drives (8:1 to 12:1) and planetary gears (6:1 to 10:1) [3]. For applications requiring higher ratios without backlash, harmonic drives with ratios between 30:1 and 50:1 are often employed [3].

Motor topology also plays a crucial role. **Axial flux permanent magnet (AFPM)** motors are increasingly preferred over traditional radial flux motors due to their superior power density (3–5 kW/kg) and torque density (15–25 Nm/kg) [3]. They offer a more compact form factor, with a 20–40% reduction in axial length, and achieve high efficiency of 92–95% at their rated load [3]. In a typical state-of-the-art integrated actuator, the motor constitutes 35–40% of the total weight, followed by the transmission (25–30%), housing (15–20%), and cooling/bearing systems (10–15%) [3].

### **Table 1: Humanoid Robot Actuator Specifications**
| Component / Joint | Actuator Type | Key Metric | Min/Mode/Max Specification | Associated Robot/Example | Source(s) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **General Rotary** | Rotary | Specific Torque | >10 Nm/kg (Target) | General Humanoids | 1 |
| **Hip / Knee** | Rotary | Peak Torque Density | >30 Nm/kg (State-of-the-Art) | ZHR-H Series (36 Nm/kg) | 2 |
| **Hip (70 kg Robot)** | Rotary | Peak Torque | 100 - 150 Nm | Generic Example (Squat/Stairs) | 1 |
| **General Linear** | Linear | Specific Force | >4,000 N/kg (Target) | General Humanoids | 1 |
| **Roller Screw** | Linear | Specific Force | 3,500 - 5,000+ N/kg | Viable Actuator Technology | 1 |
| **Hydraulic Cylinder** | Linear | Specific Force | 5,000 - 10,000+ N/kg | Viable Actuator Technology | 1 |
| **THOR Hip (Yaw)** | Linear SEA | Peak Torque | 73.74 - 115.02 Nm | THOR Robot | 5 |
| **THOR Hip (Roll)** | Linear SEA | Peak Torque | 125.94 - 174.72 Nm | THOR Robot | 5 |
| **THOR Hip (Pitch)** | Linear (Hoeken's Linkage) | Peak Torque | Up to 100 Nm | THOR Robot | 5 |
| **AFPM Motor** | Motor Component | Power Density | 3 - 5 kW/kg | High-Performance Actuators | 3 |
| **AFPM Motor** | Motor Component | Torque Density | 15 - 25 Nm/kg | High-Performance Actuators | 3 |

### Joint-Specific Designs and Optimization

The hip joint, a complex three-degree-of-freedom spherical joint, exemplifies sophisticated actuator integration. The THOR robot, for example, utilizes a unique design where yaw and roll are driven by a pair of parallel linear series elastic actuators (SEAs), while pitch is controlled by a linear actuator integrated into a Hoeken's linkage [24]. This linkage design allows for a large 150° range of motion with nearly constant torque output [24].

Optimization strategies are multifaceted and crucial for achieving performance targets. Electromagnetic motor designs employ high pole counts and optimized slot fill factors to maximize torque without adding mass [2]. Structural optimization involves creating custom, integrated housings where the motor casing serves as the input for the reducer, and the limb structure directly interfaces with the output flange, eliminating redundant material [2]. Thermal management is another critical area, as continuous operation generates significant heat. Advanced strategies include phase change cooling, which offers a 3-5x improvement over natural convection, and direct coil immersion cooling, which is 3.7 times more effective than a liquid jacket and 10 times better than forced air [3].

---

## Wiring Systems

The wiring harness in a humanoid robot is its nervous system, responsible for transmitting power, data, and control signals to every sensor, actuator, and processor. The weight and complexity of this harness are significant design constraints, especially as the number of electrical components, which can range into the hundreds, increases. A study on in-robot network architectures projected that as the component count scales from a baseline of 92 to potentially 100 times that number, the total required link length and corresponding weight increase proportionally [21]. Therefore, designing lightweight, durable, and highly flexible wiring systems is paramount.

### Design and Material Characteristics

Humanoid robot wire harnesses must endure continuous multi-axis movement, including repeated bending, torsion, and dynamic load cycles, without compromising electrical performance [4, 5, 23]. Manufacturers prioritize several key characteristics to meet these demands. **Durability and flexibility** are achieved by using high-flex cables with stranded wires, typically made of copper, which can withstand intense vibrations without breaking, unlike solid wires [5]. The choice of conductor material balances conductivity and weight; copper is favored for high-current applications due to its excellent conductivity, while aluminum may be used in specific cases where weight savings are the absolute priority, such as in aerospace robotics [5].

Insulation and jacketing materials are selected based on the robot's operating environment to protect against moisture, abrasion, chemicals, and extreme temperatures. Materials like PVC, Polyethylene (PE), Polyurethane (PU), and silicone are common, with some specialized variants capable of withstanding temperatures from 100°C to 200°C [5, 23]. Shielding is integrated to mitigate electromagnetic interference (EMI), a critical concern in a system packed with high-power motors and sensitive sensors. Shielding options include aluminum foil, braided mesh, and twisted-pair wire configurations [4, 23].

The manufacturing process is precise, involving automated cutting, stripping, and crimping to ensure exact lengths and reliable connections [4]. Wires are carefully routed along joints and limbs to manage bend radius and reduce friction and wear [4]. Finally, each assembly undergoes rigorous continuity, stress, and functional testing [4, 23]. Architectural innovations like the Zonal In-Robot Network Architecture (ZIRA) can offer significant weight savings—at least 16% compared to a Domain-based In-Robot Network Architecture (DIRA)—by optimizing the network topology and reducing cable lengths [21].

### **Table 2: Humanoid Robot Wiring System Characteristics**
| Characteristic | Specification / Material | Purpose | Source(s) |
| :--- | :--- | :--- | :--- |
| **Conductor Material** | Stranded Copper (Primary), Aluminum (Weight-Critical) | High conductivity, flexibility, vibration resistance. | 4, 5 |
| **Insulation/Jacketing** | PVC, PE, PU, Silicone | Environmental protection (moisture, abrasion, chemicals). | 4, 5 |
| **Temperature Resistance** | Up to 100°C - 200°C | Performance in high-temperature operating environments. | 4 |
| **Flexibility** | High-flex and flexible cable designs | Withstand continuous multi-axis movement, bending, and torsion. | 3, 4 |
| **EMI Shielding** | Aluminum foil, braided mesh, twisted-pair configurations | Reduce electromagnetic interference for signal integrity. | 4 |
| **Architecture** | Custom harnesses, Zonal In-Robot Network (ZIRA) | Compact integration, optimized routing, weight reduction (≥16%). | 3, 31 |
| **Manufacturing** | Automated cutting, stripping, crimping; managed bend radius | Precision, reliability, electrical continuity, wear reduction. | 3 |
| **Component Count** | 92 (Baseline) to 9200 (Projected) | Influences total harness length and weight. | 29 |

---

## Sensor Suites

A humanoid robot’s ability to perceive, navigate, and interact with its environment is entirely dependent on its sensor suite. These systems are designed to mimic human sensory capabilities, providing the robot with a rich stream of data for motion control, balance, and task execution. The complexity of a humanoid robot dictates its sensor count, which can range from as few as 30 to over 200 individual units [26]. This diverse array of sensors works in concert to enable sophisticated environmental awareness and precise physical interaction.

### Sensor Modalities and Applications

The sensor suite of a typical humanoid robot includes several key modalities. **Vision systems** are fundamental for navigation and object recognition. These often employ a combination of stereo cameras, Time-of-Flight (ToF) cameras, and structural light cameras to capture 3D visual information [26]. For outdoor applications or long-distance measurement, LiDAR (Light Detection and Ranging) is often integrated due to its robustness against sunlight and superior range [26].

**Inertial Measurement Units (IMUs)** are critical for balance and self-perception. By measuring acceleration and angular velocity, an IMU allows the robot’s control system to track its posture and motion state in real-time [26]. This feedback is essential for maintaining stability during dynamic activities like walking or responding to external perturbations.

To provide a sense of touch and force feedback, robots are equipped with a variety of specialized force and torque sensors. **Tactile sensors** are integrated into dexterous hands, with typically one unit per finger (around 10 per robot), allowing the robot to measure the pressure applied to an object [26]. For more delicate manipulation, miniature **nano force sensors**, such as the FUTEK QLA414 which weighs only 0.5 grams, are used in fingertips and knuckles [27]. These provide the high-resolution feedback needed for grasping fragile items and detecting slippage.

For measuring larger forces and torques across the robot's structure, several types of sensors are used. **Load cells**, including miniature in-line models and low-profile load buttons, are integrated into the lower legs and feet [27]. They measure tension and compression loads, providing critical data on force distribution, foot posture, and the robot's center of gravity. At major joints like the wrists, shoulders, knees, and elbows, **6-Degree-of-Freedom (6 DoF) Force/Torque (F/T) sensors** and **strain wave gear torque sensors** are employed [27]. These sensors accurately measure forces and torques in multiple directions with minimal crosstalk, enabling the smooth, coordinated movements necessary for complex manipulation tasks [27]. For instance, NMB Technologies produces 6-axis force sensors with a diameter of just 9.6 mm that can be seamlessly integrated into robotic fingers [28].

### **Table 3: Humanoid Robot Sensor Suite Components**
| Sensor Type | Application / Location | Typical Count | Weight Example | Key Function | Source(s) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Vision System** | Head / Body | 1-5 units | Varies | 3D perception, navigation, object recognition. | 26 |
| **LiDAR** | Head / Torso | 1 unit | Varies | Long-distance measurement, robust in sunlight. | 26 |
| **IMU** | Torso / Pelvis | 1-2 units | - | Measures acceleration & angular velocity for balance. | 26 |
| **Tactile Sensor** | Dexterous Hands (Fingertips) | ~10 units (1 per finger) | - | Measures force/pressure for grip control. | 26 |
| **Nano Force Sensor** | Fingertips, Finger Knuckles | 10+ units | 0.5 g (QLA414) | High-resolution force feedback for delicate manipulation. | 27 |
| **6 DoF F/T Sensor** | Wrists, Torso-Leg Joints | 2-4 units | Varies (low-profile) | Measures forces & torques across 6 axes for dexterity. | 27 |
| **Strain Wave Torque** | Shoulders, Knees, Elbows | 6-12 units | Varies (compact) | High-precision torque measurement for closed-loop control. | 27 |
| **Miniature Load Cell** | Tibial System (Lower Leg) | 2 units | Varies | Measures tension/compression loads on legs. | 27 |
| **Load Button** | Foot System | 4-8 units | Varies | Measures compression forces for balance & CoG calculation. | 27 |
| **Position Sensor** | Integrated into Motors/Joints | ~40 units | - | Hall, optical, magnetic for precise movement control. | 28 |
| **Total Sensor Count** | Entire Robot | - | 30 (Min), 200 (Max) | Dependent on robot function and complexity. | 26 |

---

## Onboard Controllers and Computers

The "brain" of a humanoid robot is its onboard control and computation system, which must process vast amounts of sensor data, run complex AI models, and issue thousands of commands per second to the actuators. The design of these modules is driven by the need for immense computational power housed within a lightweight, power-efficient package. The trend is toward highly integrated platforms that combine AI inference, motion planning, and low-level control, often leveraging powerful embedded GPUs and specialized systems-on-a-chip (SoCs) [6, 8].

A leading example of this sophisticated approach is the architecture developed by Figure for its humanoid robots. The **Helix** control system is a decoupled, multi-system model designed for generalist control. At the highest level, **System 2 (S2)** is a 7-billion parameter Vision-Language Model (VLM) that runs at 7-9 Hz. It processes images and robot state data to perform scene understanding and language comprehension, distilling high-level goals into a continuous latent vector. This information is passed to **System 1 (S1)**, an 80-million parameter visuomotor transformer. Running at 200 Hz, S1 translates the semantic goals from S2 into precise, continuous actions for the robot's upper body, controlling everything from wrist poses to finger movements [6].

The more advanced **Helix 02** model extends this architecture with **System 0 (S0)**, a 10-million parameter neural network that functions as a learned whole-body controller. Operating at a rapid 1 kHz, S0 takes full-body joint states as input and outputs low-level actuator commands, managing balance, contact forces, and coordination across the entire robot. In this setup, S1 is expanded to control the entire body, from legs to individual fingers, by producing full-body joint targets for S0 to track [7]. This entire multi-layered inference pipeline is designed to run on embedded, low-power-consumption GPUs, making it viable for commercial deployment [6, 7].

Other manufacturers are pursuing similar integrated solutions. NEXCOM, in collaboration with NVIDIA, developed the **MARS400 T10** controller based on the NVIDIA Jetson Thor platform. This system integrates AI computing, motion control, and robot control into a single platform to reduce latency and physical space, thereby enabling more compact and energy-efficient robot designs [8]. Similarly, JHCTECH offers powerful control modules for intelligent robotics featuring 6 or 8-core ARM Cortex-A78AE CPUs, Ampere architecture GPUs, and 8GB or 16GB of onboard memory, all designed for fanless operation and a wide power supply range [10]. While specific weight figures for these modules are not publicly detailed, the industry-wide emphasis is clearly on optimizing size, weight, and power (SWaP) through hardware-software co-design and platform integration.

### **Table 4: Humanoid Robot Onboard Controller Specifications**
| System / Manufacturer | Key Components / Architecture | Computational Load (Example) | Design Goal | Source(s) |
| :--- | :--- | :--- | :--- | :--- |
| **Figure Helix** | Decoupled Multi-System AI: S2 (Reasoning) + S1 (Action) | S2: 7B params @ 7-9 Hz; S1: 80M params @ 200 Hz | Onboard, low-power GPU deployment for commercial use. | 6, 7 |
| **Figure Helix 02** | 3-Layer System: S2 (Reasoning) -> S1 (Targeting) -> S0 (Control) | S0: 10M params @ 1 kHz | Learned whole-body control as a single continuous system. | 7 |
| **NEXCOM MARS400 T10** | NVIDIA Jetson Thor-based platform | Integrated AI, motion, and robot control. | Reduce latency, optimize size and weight for compact design. | 8 |
| **JHCTECH** | 6/8-core ARM Cortex-A78AE CPU, Ampere GPU | 8/16GB onboard memory, NVMe support. | High performance for intelligent robotics, machine vision. | 10 |
| **Texas Instruments** | - | Real-time, high-level OS support; Industrial Ethernet. | Scalability, fanless operation, and system longevity. | 9 |

---

## Material Allocation Strategies

The selection and allocation of materials are fundamental to the design of humanoid robots, directly influencing their weight, strength, durability, and cost. The industry is progressively moving away from traditional metals like steel and aluminum toward a sophisticated multi-material approach that leverages advanced composites and high-performance polymers [16, 17]. This strategy is essential for creating lightweight yet robust structures capable of withstanding the dynamic stresses of bipedal locomotion and manipulation. The material choice for a specific component is a calculated decision based on its mechanical requirements, such as stiffness, fatigue resistance, and thermal conductivity.

### Material Analysis by Component and Manufacturer

**Polyether Ether Ketone (PEEK)** has emerged as a key material in next-generation humanoids due to its exceptional properties: high-temperature and wear resistance, self-lubrication, and a density approximately half that of aluminum [14]. Tesla's Optimus-Gen2 robot reportedly achieved a 10 kg weight reduction largely through the strategic use of PEEK in its joints, limbs, and skeletal framework [14, 15, 16]. PEEK gears provide stable transmission, while PEEK bearings offer excellent wear resistance without external lubrication [14]. When reinforced with carbon fiber (CF/PEEK), the material provides even greater strength and stiffness at a density just 58% that of aluminum alloy [19]. UBTech's Walker S robot also utilizes PEEK in its reducers to balance load capacity and weight [14, 19]. A typical humanoid may use around 1 kg of pure PEEK for gears and joints and up to 8 kg of CF/PEEK for its structural limbs [14].

**Carbon Fiber Reinforced Plastics (CFRP)** are prized for their extraordinary strength-to-weight ratio, which can be up to five times better than aluminum [17, 18]. This makes them ideal for frames, limbs, and other large structural components where minimizing weight is critical for improving energy efficiency and dynamic performance. Boston Dynamics' Atlas robot, for instance, famously uses carbon fiber legs [16]. In industrial robot arms, switching from aluminum to CFRP can reduce weight by over 40% while maintaining the necessary strength and rigidity for precision tasks [17].

**Titanium alloys**, such as Ti-6Al-4V, are reserved for the most demanding applications, particularly high-stress joints. Titanium offers a strength-to-weight ratio eight times better than steel by weight and fatigue resistance three times greater than stainless steel [17, 18]. This makes it the material of choice for critical components like hip blocks and knee pivots that must endure millions of high-load cycles without failure. The latest generations of advanced humanoids, including Tesla's Optimus Gen3 and Boston Dynamics' Atlas V11, are reported to use titanium for their high-precision, durable joints [17].

While advanced materials are gaining prominence, **aluminum alloys** like 6061-T6 and 7075-T6 remain a cornerstone of robot construction, accounting for approximately 70% of current usage in general applications [17]. They offer an excellent balance of strength, low density (2.73 g/cm³), cost-effectiveness, and machinability, making them suitable for frames and mechanical structures within actuator systems [17, 18]. **Magnesium alloys**, with the lowest density among structural metals (1.74 g/cm³), are used for housings and structural supports where weight reduction, electromagnetic shielding, and heat dissipation are key concerns [17, 19].

Other specialized polymers serve niche roles. Polyamide (PA) is used in 3D-printed robots like the Poppy humanoid [15, 16]. PC/ABS blends are found in robots like SoftBank's NAO [15, 16]. Polyphenylene Sulfide (PPS) is used for exoskeleton components, while Liquid Crystal Polymer (LCP) is crucial for high-frequency servo motor connectors [15, 16]. Finally, soft materials like **Silicone** and **Thermoplastic Elastomers (TPE)** are used for bionic skin and flexible grippers, enabling safer and more natural human-robot interaction [15, 17, 18].

### **Table 5: Humanoid Robot Material Allocation by Component**
| Material | Key Properties | Primary Application | Component Examples | Manufacturer/Robot Example | Source(s) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Titanium Alloy** | Very high strength-to-weight, fatigue/corrosion resistance. | High-Stress Joints | Hip blocks, knee pivots, precision joints. | Tesla Optimus Gen3, Boston Dynamics Atlas V11 | 14, 17 |
| **Carbon Fiber (CFRP)** | Exceptional strength-to-weight, high stiffness, low weight. | Structural Frame & Limbs | Legs, arms, robot frame. | Boston Dynamics Atlas (Legs) | 16, 17, 18 |
| **PEEK / CF-PEEK** | Lightweight, wear/heat resistant, self-lubricating. | Joints, Gears, Skeleton | Gears, bearings, joint casings, structural limbs. | Tesla Optimus-Gen2, UBTech Walker S | 14, 15, 16, 19 |
| **Aluminum Alloy** | Good strength-to-weight, cost-effective, machinable. | General Frame & Structure | Robot frames, actuator mechanical structures. | 70% of general robot frames, Knee/Hip Actuators | 17, 18 |
| **Magnesium Alloy** | Lowest density structural metal, high vibration absorption. | Housings, Supports | Housings, structural supports. | Baowu Magnesium Industry Robots | 16 |
| **Silicone / TPE** | Soft, flexible, biocompatible, temperature resistant. | Soft Robotics / Skin | Artificial skin, bionic hands, flexible grippers. | Soft Robotics Grippers | 15, 17, 18 |
| **Polyamide (PA)** | Good for 3D printing (SLS). | 3D-Printed Structures | Full robot body and frame. | Poppy Humanoid Robot | 15, 16 |
| **PC/ABS** | Impact strength, processability. | Body Shells | External casing and structural parts. | SoftBank NAO | 15, 16 |
| **Liquid Crystal Polymer** | High-frequency properties, dimensional stability. | Electronic Connectors | Servo motor connectors. | General use in high-density joint robots. | 15, 16 |

# References
1. [Humanoid Robot Actuators: The Complete Engineering Guide - Firgelli](https://www.firgelli.com/pages/humanoid-robot-actuators)
2. [Humanoid Robot Actuator Torque Density: Hip, Knee & Shoulder Specs [2026] - Zhinno Robotics](https://robotics.zhinno.com/blog/humanoid-robot-actuator-torque-density.html)
3. [Cut humanoid robot joint actuator weight by 40–50% - PatSnap Insights Team](https://www.patsnap.com/resources/blog/articles/cut-humanoid-robot-joint-actuator-weight-by-40-50/)
4. [Custom Wire Harness for Humanoid Robot Application - WellPCB](https://www.wellpcb.com/custom-wire-harness/humanoid-robot/)
5. [Choosing the Right Wire Harness for Robots - IT Supply Chain](https://itsupplychain.com/choosing-the-right-wire-harness-for-robots/)
6. [Helix: A Vision-Language-Action Model for Generalist Humanoid Control - Figure.ai](https://www.figure.ai/news/helix)
7. [Introducing Helix 02: Full-Body Autonomy - Figure.ai](https://www.figure.ai/news/helix-02)
8. [NEXCOM Showcases Safe Humanoid Robot Controller and Slim AI-Ready Panel PC & Rugged Edge Solutions @ Embedded World NA - RoboticsTomorrow](https://www.roboticstomorrow.com/news/2025/10/22/nexcom-showcases-safe-humanoid-robot-controller-and-slim-ai-ready-panel-pc-rugged-edge-solutions-embedded-world-na-/25705/)
9. [Humanoid robot system controller design resources - Texas Instruments](https://www.ti.com/solution/humanoid-robot-system-controller)
10. [Anchoring Innovation, JHCTECH Humanoid Robot Control Solution - JHCTECH](https://www.jhc-technology.com/humanoid_robot_control)
11. [Humanoid Robots Push the Bounds of Collaborative Manufacturing | ASSEMBLY - ASSEMBLY](https://www.assemblymag.com/articles/98629-humanoid-robots-push-the-bounds-of-collaborative-manufacturing)
12. [Humanoid Robots in Industrial Manufacturing: What They Can (and Can't) Do in 2026 - EVSINT](https://www.evsint.com/humanoid-robots-industrial-manufacturing-2026/)
13. [PMC10304173 - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10304173/)
14. [Key Material for Humanoid Robots: PEEK Polymer - Junhua ChinaPEEK](https://www.peekchina.com/blog/key-material-for-humanoid-robots-peek-polymer.html)
15. [Plastics for Humanoid Robots You Should Know - Junhua ChinaPEEK](https://www.peekchina.com/blog/plastics-for-humanoid-robots.html)
16. [The new material revolution of humanoid robots - SBFCHEM](https://www.sbfchem.com/index.php/news/1009/The_new_material_revolution_of_humanoid_robots.html)
17. [Materials for Robot Manufacturing and Frame Structures - StocksMantra.com](https://www.stocksmantra.com/materials-for-robot-manufacturing-and-frame-structures/)
18. [Advanced Materials Guide on the Latest Technology Of Robotics - Yijin Solution](https://yijinsolution.com/cnc-guides/advanced-materials-guide-latest-technology/)
19. [Application and development analysis of composite materials in the field of humanoid robots - CMAG](https://www.cmag.com.cn/news/application-and-development-analysis-of-compos-85160017.html)
20. [On the Actuator Requirements for Human-Like Execution of Retargeted Human Motion on Humanoid Robots - h2t.iar.kit.edu](https://h2t.iar.kit.edu/pdf/Klas2023b.pdf)
21. [PMC10007397 - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10007397/)
22. [humanoid robot - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2212827120314566)
23. [Robot Wire Harness | Wire Harness & Cable Assembly Manufacturer - Romtronic](https://www.romtronic.com/custom-wire-harness/robot-wire-harness/)
24. [Design of a Human-Like Range of Motion Hip Joint for Humanoid Robots - RoMeLa](https://www.romela.org/wp-content/uploads/2015/05/2014_design_of_a_human-like_range_of_motion_hip_joint_for_humanoid_robots.pdf)
25. [PMC11013340 - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11013340/)
26. [12821919 1 Transformation Humanoid robots 101 29 April 2025 Key takeaways - institute.bankofamerica.com](https://institute.bankofamerica.com/content/dam/transformation/humanoid-robots.pdf)
27. [Humanoid Robot Sensors | FUTEK - FUTEK](https://www.futek.com/applications/humanoid-robot-sensors)
28. [Humanoid Robots | NMB Technologies - NMB Technologies](https://nmbtc.com/applications/robotics/humanoid-robots/)
29. [What Sensors Do Humanoid Robots Have? - Humanoid Robotics Technology](https://humanoidroboticstechnology.com/articles/what-sensors-do-humanoid-robots-have/)
30. [MDPI - PMC](https://www.mdpi.com/2076-0825/14/5/243)
31. [Materials for Humanoid Robot Frames and Components - Sunrise Metal](https://www.sunrise-metal.com/materials-for-humanoid-robot/)
32. [Robotic Actuators – The Muscle Power of Industry 4.0 - Wevolver](https://www.wevolver.com/article/robotic-actuators-the-muscle-power-of-industry-40)