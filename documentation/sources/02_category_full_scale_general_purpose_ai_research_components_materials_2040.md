# Full-Scale General-Purpose / AI Research Humanoids: Components, Materials and Outlook to 2040
*Matthias Roesslein — October 23, 2026*

Full-scale general-purpose humanoids are best distinguished by their intended breadth of manipulation, learning and human interaction—not by size alone. Unitree H2 provides a useful reference platform, while Tesla Optimus and Figure 03 illustrate overlap with commercial deployment; Apptronik Apollo 2 marks the boundary with industrial utility. The mass-balanced H2 model developed here totals **70.0 kg at Mode**, matching the reported platform mass, but its component weights and material grades remain estimates rather than a verified manufacturing bill of materials.

## 1. Definition and Evidence Framework

This category comprises human-scale, bipedal humanoids intended for diverse manipulation, physical-AI development and human–robot interaction in semi-structured environments, including laboratories, offices and prospective domestic settings. The defining characteristic is versatility: the platform is not optimized exclusively for repetitive logistics, exceptional dynamic performance or hazardous operations.

Research access and general-purpose deployment are related but distinct objectives. H2 is described as an open research and AI platform, whereas Optimus combines consumer and factory ambitions, and Figure 03 combines commercial and domestic applications. These differences justify retaining a broad category while distinguishing its research-oriented and deployment-oriented members.

### Evidence labels

The report uses three explicit numerical classifications:

- **Direct:** A specification or claim attributed to a source in the supplied evidence. This does not imply independent measurement.
- **Estimate:** An engineering assumption, allocation or future scenario.
- **Derived:** Arithmetic calculated from Direct or Estimate inputs. A calculation from estimates remains uncertain.

“Min / Mode / Max” denotes low, central and high modelling cases. These are not measured manufacturing tolerances, confidence intervals or guaranteed operating limits. “Mode” is the central planning assumption, not an empirically established statistical mode.

## 2. Assignment Criteria

The supplied category framework emphasizes human-scale dimensions, articulated manipulation, AI integration and interaction hardware. Its indicative dimensional envelope is **160–185 cm** in height and **50–80 kg** in mass; these are category-design estimates, not universal physical limits.

The following thresholds reproduce the proposed screening framework. They should guide comparison rather than exclude a platform automatically when a specification is unavailable.

| Criterion | Proposed threshold — Estimate | Indicative configuration — Estimate |
| :--- | :--- | :--- |
| Height | 160 cm | 175–180 cm |
| Total articulation | 30 DoF | 50–75 DoF, including hands |
| Compute | 500 TOPS | More than 2,000 TOPS |
| Hand payload | 2 kg | 5–7 kg |
| Walking speed | 1.0 m/s | 1.2–1.5 m/s |

The most important criterion is functional intent. Numeric thresholds alone cannot distinguish a research platform from an industrial humanoid of similar dimensions.

Additional indicators include articulated necks, microphone arrays, stereo vision and tactile sensing. AI-first integration is exemplified by the reported association between H2 Plus and NVIDIA Isaac GR00T, alongside a Jetson Thor AGX compute configuration. These are platform or configuration claims, not evidence that every H2 configuration contains the same equipment.

Articulation must also be counted consistently. H2’s reported **31 chassis DoF** and the H2 Plus hand configuration’s **22 DoF per hand** imply **75 combined DoF**, a Derived value, provided the hand and chassis counts are additive. Comparing chassis-only counts with totals including fingers would otherwise exaggerate differences.

## 3. Boundary Justification and Candidate Accounting

### 3.1 Industrial logistics

Industrial utility platforms prioritize payload, duty cycle and deployment continuity. The supplied comparison describes Apollo 2 as emphasizing payload of **25 kg or more**, swappable batteries and a modular base that can include a wheeled option. Its reported **12 hand DoF** contrast with the more articulated H2 Plus hand configuration.

These features do not make Apollo 2 incapable of research or general-purpose tasks. They indicate a different optimization objective: sustained industrial handling rather than interaction-rich experimentation. Under a broad interpretation encompassing adaptable industrial humanoids, Apollo 2 belongs within the category; under a narrower research-and-interaction interpretation, it falls into industrial logistics.

### 3.2 High-performance and hazardous platforms

The supplied framework uses BD Atlas as the high-performance comparator, emphasizing dynamic agility and power density. That is an analytical boundary description rather than a documented Atlas specification set in the supplied evidence.

H2’s reported **360 Nm peak torque** does not establish human-safe contact behavior by itself. The supplied narrative calls this “human-safe,” but provides no supporting safety test or operating envelope. The category boundary should therefore rest on intended precision, manipulation and interaction—not an inferred safety certification.

### 3.3 Complete candidate screen

The supplied narrative identifies **six platform families**: H2, Optimus, Figure 03, Apollo 2, H1 and BD Atlas. H2 Plus is treated as an H2 configuration rather than a separate family. The screen yields **three qualifying families, one borderline family and two excluded comparators**.

| Platform family | Classification | Basis | Alternative reading |
| :--- | :--- | :--- | :--- |
| Unitree H2 / H2 Plus | Qualifying | Open research / AI | Research-oriented core |
| Tesla Optimus | Qualifying | Consumer / factory versatility | Industrial overlap |
| Figure 03 | Qualifying | Commercial / domestic scope | Deployment-oriented core |
| Apptronik Apollo 2 | Borderline | Industrial utility priority | Included under broad scope |
| Unitree H1 | Excluded from current screen | Historical locomotion comparator | Insufficient qualifying specifications |
| BD Atlas | Excluded | High-performance comparator | Insufficient general-purpose evidence |

H2, Optimus, Figure 03 and Apollo 2 classifications follow their stated purposes. H1 and Atlas are retained explicitly as boundary comparators; their exclusion is not a claim that they lack all general-purpose capabilities.

## 4. Representative Robots

Reported specifications below are **Direct** claims unless marked otherwise. The supplied sources do not establish a common measurement protocol, and approximate DoF counts are retained as approximate.

### Dimensions and articulation

| Platform | Height (cm) | Mass (kg) | Chassis DoF | Hand DoF |
| :--- | ---: | ---: | :--- | :--- |
| Unitree H2 / H2 Plus | 182 | 70 | 31 | 22 per hand, Plus |
| Tesla Optimus Gen 3 | 173 | 57 | Approximately 28–30 | 22 per hand |
| Figure 03 | 173 | 61 | Approximately 30+ | 16–20; counting scope unclear |
| Apptronik Apollo 2 | 173 | 73 | 35 | 12; counting scope unclear |

H2 dimensions and chassis articulation are attributed to Unitree, Humanoid Guide and Robots International; its Plus hand configuration is attributed to the supplied Isaac GR00T/H2 Plus source. Optimus figures come from the supplied analysis and comparison sources; Figure 03 figures from the review and specification entry; Apollo 2 figures from Apptronik and Humanoid Guide.

The similar heights and masses show why morphology is an insufficient classifier. Purpose and configuration—not a few kilograms or centimetres—determine the more useful boundary.

### Roles and distinguishing configurations

| Platform | Stated role | Distinguishing feature |
| :--- | :--- | :--- |
| Unitree H2 | Open research / AI | Highly articulated Plus hands |
| Tesla Optimus | Consumer / factory | Mixed deployment ambition |
| Figure 03 | Commercial / domestic | General-purpose deployment scope |
| Apptronik Apollo 2 | Industrial utility | Payload and battery continuity |

These role descriptions preserve the supplied comparison without ranking unmeasured autonomy or manipulation performance. H2 is the most suitable BOM anchor because the supplied dataset contains both a component allocation and a material allocation for it.

## 5. Unitree H2 Component Bill of Materials

### 5.1 Reference configuration and reconciliation

The reference is a **70 kg H2-class configuration** with dexterous hands and research compute. The reported platform mass includes the battery, but the evidence does not establish whether every listed accessory is included in that mass. Accordingly, agreement between the estimated BOM and the reported mass is calibration—not configuration verification.

The supplied narrative and appendix contain different structural-frame allocations. The narrative assigns **15.0 / 18.0 / 22.0 kg**; the appendix assigns **16.0 / 19.6 / 24.0 kg**. Summing the narrative rows gives **51.7 / 68.4 / 89.6 kg**, not its stated **52.1 / 69.0 / 89.6 kg**. The appendix rows correctly sum to **52.7 / 70.0 / 91.6 kg**.

The appendix version is therefore adopted as the internally consistent, mass-balanced model. This is better supported arithmetically, not independently validated physically.

### 5.2 Actuation and manipulation

All per-unit masses are **Estimate**; all total masses are **Derived**. Quantities are modelled configuration counts consistent with the supplied articulation layout. Values are ordered **Min / Mode / Max**.

| Component | Quantity | Per-unit mass (kg), Estimate | Total mass (kg), Derived | Model basis |
| :--- | ---: | :--- | :--- | :--- |
| Leg actuators | 12 | 0.80 / 1.00 / 1.30 | 9.60 / 12.00 / 15.60 | Higher-torque leg units |
| Arm actuators | 14 | 0.35 / 0.50 / 0.70 | 4.90 / 7.00 / 9.80 | Seven joints per arm |
| Waist actuators | 3 | 0.80 / 1.00 / 1.20 | 2.40 / 3.00 / 3.60 | Torso control |
| Neck actuators | 2 | 0.20 / 0.30 / 0.45 | 0.40 / 0.60 / 0.90 | Pan / tilt |
| Dexterous hands | 2 | 1.00 / 1.50 / 2.00 | 2.00 / 3.00 / 4.00 | Plus-class configuration |

The chassis actuator quantities total **31**, Derived, consistent with the reported chassis DoF. These rows total **25.6 kg at Mode**, Derived, including complete hand assemblies but not the separately allocated bearings and gears.

### 5.3 Structure, energy, sensing and integration

| Component | Quantity | Per-unit mass (kg), Estimate | Total mass (kg), Derived | Model basis |
| :--- | ---: | :--- | :--- | :--- |
| Structural frame | 1 | 16.00 / 19.60 / 24.00 | 16.00 / 19.60 / 24.00 | Calibrated appendix allocation |
| Outer shell | 1 | 4.00 / 6.00 / 8.00 | 4.00 / 6.00 / 8.00 | Polymer / magnesium panels |
| Compute module | 1 | 0.50 / 0.80 / 1.20 | 0.50 / 0.80 / 1.20 | Research compute assembly |
| Battery pack | 1 | 4.80 / 5.50 / 6.50 | 4.80 / 5.50 / 6.50 | Complete pack |
| Sensors / vision | 1 | 0.60 / 1.00 / 1.50 | 0.60 / 1.00 / 1.50 | Integrated sensor suite |
| Wiring / PCBs | 1 | 2.00 / 3.00 / 4.50 | 2.00 / 3.00 / 4.50 | Power and data distribution |
| Bearings / gears | 1 | 4.00 / 6.00 / 8.00 | 4.00 / 6.00 / 8.00 | Separate transmission allocation |
| Thermal management | 1 | 0.50 / 1.00 / 1.50 | 0.50 / 1.00 / 1.50 | Fans and cooling hardware |
| Fasteners | 1 | 1.00 / 1.50 / 2.50 | 1.00 / 1.50 / 2.50 | Separate fastening allocation |
| **Complete BOM** | — | — | **52.70 / 70.00 / 91.60** | **Derived total** |

Reported configuration details include a **15 Ah / 0.97 kWh** battery, stereo cameras, microphones, an IMU and LiDAR. The compute assumption follows the supplied Jetson Thor AGX configuration, reported at **40–130 W**.

Assembly boundaries remain an important limitation. Bearings, reducers, cooling parts and fasteners may already be included in supplier actuator or compute masses. The separate rows assume that they are excluded from those assemblies; otherwise, double counting would result.

## 6. Material Composition by Grade

The material model uses the appendix’s central allocation because it sums to **70.0 kg**. The narrative allocation instead sums to **73.5 kg**, despite describing a 70 kg target. Both versions share aggregate low and high cases of **51.0 kg** and **99.5 kg**, Derived.

All material masses are **Estimate**. Grades are candidate engineering allocations informed by the supplied material analysis, not confirmed H2 procurement specifications.

| Material family | Assumed grade / chemistry | Min (kg) | Mode (kg) | Max (kg) | Mode share (%) |
| :--- | :--- | ---: | ---: | ---: | ---: |
| Aluminum alloys | 6061-T6 / 7075-T6 | 22.0 | 26.5 | 35.0 | 37.9 |
| Steel | GCr15 / 42CrMo / 20CrMnTi | 8.0 | 11.0 | 15.0 | 15.7 |
| Plastics | PEEK / CF-PEEK / PC-ABS / PA66-GF | 6.0 | 7.5 | 11.0 | 10.7 |
| Magnesium alloys | AZ91D / AM60 | 4.0 | 6.0 | 9.0 | 8.6 |
| Copper | High-purity ETP | 3.5 | 5.0 | 7.0 | 7.1 |
| Battery materials | NMC or LFP / graphite | 2.5 | 4.5 | 6.0 | 6.4 |
| Titanium alloys | Ti-6Al-4V | 1.5 | 3.0 | 5.0 | 4.3 |
| Permanent magnets | High-coercivity NdFeB | 2.0 | 3.0 | 5.0 | 4.3 |
| Electronics / glass | FR-4 / glass / silicon | 1.0 | 2.0 | 3.5 | 2.9 |
| Carbon-fiber composite | CFRP, T700 / T800 assumption | 0.5 | 1.5 | 3.0 | 2.1 |
| **Total** | — | **51.0** | **70.0** | **99.5** | **100.0** |

Mode shares are **Derived**, calculated against 70.0 kg; displayed percentages differ slightly from 100% when summed because of rounding. Aluminum and steel together account for **37.5 kg**, or approximately **53.6%**, Derived, making them the dominant central-case allocation.

The proposed applications are aluminum in frames and housings; steel in gears, bearings and axles; magnesium in panels and heat sinks; titanium at stressed pivots; and polymers in shells, bushings and spacers. Copper and NdFeB principally support actuation, while carbon-fiber composite is assigned to selected reinforcement. These remain material-use assumptions.

The battery row represents constituent materials rather than the complete pack. Its Mode mass therefore need not equal the BOM battery mass: pack casing, conductors and electronics belong to other material families. Likewise, composite reinforcement and polymer matrices require consistent bookkeeping to avoid overlap.

The BOM and material Min/Max totals differ because they are separate sensitivity models. Only their Mode cases are explicitly mass-balanced to the same robot.

## 7. Development Outlook: 2025–2040

The outlook is a set of **Estimate scenarios**, not a forecast with demonstrated probabilities. The supplied evidence contains no dated retail-price record or manufacturer roadmap substantiating these future values.

### 2025: Deployment-readiness baseline

The supplied baseline uses a planning cost range of **$30,000 to more than $100,000**, depending on configuration, and runtime of **3–5 hours**. These are retained as 2025 modelling assumptions, not verified transaction prices. The central trajectory selects **$40,000**, **70 kg** and **3.5 hours**.

Its deployment emphasis is industrial pilots and university research sales. That mixed direction reinforces the category’s overlap with industrial platforms while leaving research configurability as a distinguishing feature.

### 2030: Production scale and lightweighting

The supplied scenario proposes approximately **20% magnesium** and **15% CFRP** by mass, alongside actuator changes intended to reduce actuator mass by **30%**. Candidate mechanisms include transverse-flux motors and PEEK-based harmonic gearing; none is established here as an H2 product commitment.

Battery energy density of **350 Wh/kg**, runtime of **8–10 hours** and enterprise cost below **$20,000** are scenario targets. The narrative suggests approximately **55 kg**, whereas the trajectory table selects **58 kg**. Both are estimates; the latter is retained for tabular consistency.

### 2035: Household integration

The proposed direction combines multimodal task execution with TPU or silicone interaction surfaces. The claim of autonomy without per-task programming is aspirational, not demonstrated across the representative robots.

The supplied scenario also proposes standardized **2 kW** floor-based inductive charging. Its central planning values are **$12,000**, **52 kg** and **14 hours** of runtime; no supporting deployment schedule is provided.

### 2040: Advanced structures and continuous service

The long-range scenario proposes nano-engineered composite structures, potentially including CNT-based reinforcement, and either solid-state batteries or hydrogen fuel cells. **24-hour operation** is a target rather than an established endurance result.

Physical labor and specialized elder care are proposed application directions. Describing humanoids as the “primary interface” for these roles would imply adoption evidence that is absent; the defensible interpretation is a possible future role.

### Central trajectory

| Year | Unit cost (USD), Estimate | Mass (kg), Estimate | Runtime (h), Estimate | Proposed material emphasis |
| :--- | ---: | ---: | ---: | :--- |
| 2025 | 40,000 | 70 | 3.5 | Aluminum / steel |
| 2030 | 18,000 | 58 | 9.0 | Magnesium / aluminum |
| 2035 | 12,000 | 52 | 14.0 | CFRP / PEEK |
| 2040 | 8,000 | 45 | 24.0 | Nano-composites |

This trajectory is useful for sensitivity analysis, not purchasing or capacity planning without additional evidence. It assumes simultaneous improvements in mass, endurance, autonomy and cost that the supplied data do not independently validate.

## 8. Appendix: Calculation and Interpretation Rules

The report’s calculations follow four conventions:

1. **Component total:** Quantity multiplied by per-unit mass for each Min, Mode and Max case.
2. **Robot total:** Sum of component totals without additional hidden mass allowance.
3. **Material share:** Material Mode mass divided by 70.0 kg, multiplied by 100.
4. **Combined articulation:** Chassis DoF plus both hand counts, only where counting boundaries are compatible.

The principal reconciliations are summarized below. All recalculated values are **Derived**.

| Dataset | Supplied total, Min / Mode / Max (kg) | Recalculated total (kg) | Treatment |
| :--- | :--- | :--- | :--- |
| Narrative BOM | 52.1 / 69.0 / 89.6 | 51.7 / 68.4 / 89.6 | Not adopted |
| Appendix BOM | 52.7 / 70.0 / 91.6 | 52.7 / 70.0 / 91.6 | Adopted |
| Narrative materials | 70 kg target | 51.0 / 73.5 / 99.5 | Not adopted |
| Appendix materials | 51.0 / 70.0 / 99.5 | 51.0 / 70.0 / 99.5 | Adopted |

Internal consistency supports selecting the appendix models, but does not convert them into Direct evidence. The highest-value follow-up would be a configuration-specific weighed BOM, verified assembly boundaries, confirmed material grades and standardized runtime measurements.

## 9. Sources

**H2 platform and configuration evidence:** Unitree’s H2 product information, Humanoid Guide’s H2 entry and Robots International’s specifications support reported dimensions, mass, articulation and sensor details. The supplied Isaac GR00T/H2 Plus source supports the research-compute and hand configuration claims.

**Comparative platform evidence:** Apptronik and Humanoid Guide support Apollo 2 specifications and industrial positioning. The supplied Optimus analysis and comparison support its reported specifications; the Figure 03 review and specification entry support its dimensional and articulation claims.

**Materials and battery evidence:** The supplied humanoid-material analysis informs candidate grades and applications, while the battery documentation supports the reported capacity claims. Neither establishes a verified H2 material inventory.

**Model provenance:** Component masses, material allocations, category thresholds and the 2025–2040 trajectory originate in the supplied category model. They are explicitly retained as Estimate inputs or Derived calculations, rather than attributed to manufacturer specifications.

---

## Sources

1. <https://www.unitree.com/H2/>
2. <https://humanoid.guide/product/h2/>
3. <https://apptronik.com/apollo/apollo-2>
4. <https://optimusk.blog/blog/tesla-optimus-gen-2/>
5. <https://blog.robozaps.com/b/figure-03-review>
6. <https://humanoid.guide/welcome-apollo-2/>
7. <https://anintent.com/blog/nvidia-isaac-groot-humanoid-robot-unitree-h2-plus/>
8. <https://www.robotsinternational.com/Unitree-H2-Humanoid-Robots.htm>
9. <https://blog.robozaps.com/b/tesla-optimus-vs-apptronik-apollo>
10. <https://www.originofbots.com/robot/figure-03-by-figure-ai-details-specifications-rating>
11. <https://www.robotlar.org/en/humanoid-robots/unitree-h2>
12. <https://partinchem.com/blog/whats-the-secret-to-lighter-more-durable-robots/>
