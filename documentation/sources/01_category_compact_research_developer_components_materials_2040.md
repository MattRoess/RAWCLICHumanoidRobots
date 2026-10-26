# Compact Research & Developer Humanoids: Components, Materials and Outlook to 2040
*Matthias Roesslein — October 23, 2026*

Compact Research & Developer (C-R&D) humanoids are best treated as a distinct experimental-platform category, rather than simply smaller general-purpose workers. The supplied category framework combines a height of 1.20–1.45 m, mass of 30–50 kg and a primary research or developer purpose. Unitree G1 provides the representative 35.0 kg mass anchor, but its detailed component and material allocations remain predominantly estimates—not a manufacturer-verified bill of materials. The outlook through 2040 is a conditional development scenario, with important uncertainties in lightweighting, battery performance and cost.

## 1. Definition and Evidence Basis

C-R&D humanoids are compact bipedal platforms intended principally for laboratory experimentation, embodied-AI development, reinforcement-learning testing and academic benchmarking. Their defining trade-off is to prioritize manageable experimental hardware, portability and dynamic-motion development over the human-scale reach and load-handling emphasis attributed to larger general-purpose humanoids.

The supplied research identifies Unitree G1 as the category’s representative hardware anchor and AgiBot X1 as another research-oriented platform. Manufacturer product information, developer specifications and comparative databases form the stated evidence base.

Three numerical evidence classes are used throughout:

- **Direct:** a value reported in the supplied research as originating in manufacturer or product documentation.
- **Derived:** a calculation from stated inputs, or a value explicitly identified as derived in the supplied research.
- **Estimate:** an inferred component allocation, assumed material specification or future scenario value.

These distinctions apply to individual values, not automatically to an entire table. In particular, a directly reported assembled mass does not make the estimated parts beneath it directly measured. “Min,” “Mode” and “Max” denote the supplied engineering scenarios; they are not statistical confidence limits, and “Mode” is the central allocation rather than a demonstrated statistical mode.

## 2. Category Criteria

The following criteria formalize the supplied category definition. Physical size and primary purpose determine membership; payload, portability and price describe the intended operating and purchasing profile.

| Criterion | Category threshold or profile | Role |
| :--- | :--- | :--- |
| Configuration | Bipedal humanoid | Defining |
| Height | 1.20–1.45 m | Defining |
| Assembled mass | 30–50 kg | Defining |
| Primary purpose | Research, AI training, developer testing | Defining |
| Maximum arm payload | 2–5 kg | Indicative |
| Portability | Compact; often foldable | Indicative |
| Laboratory handling | Manageable with suitable precautions | Intended profile |
| Target acquisition price | $15,000–$45,000 | Indicative estimate |

The price range is the supplied research’s category-level planning estimate, not a dated market quotation. Likewise, the payload range is not established individually for every representative robot and therefore cannot serve as a verified exclusion threshold.

The research describes these platforms as “lab-safe,” but provides no safety certification or standardized validation for that designation. Here, the term means an intended laboratory-handling profile—not permission to operate without tethers, supervision or other appropriate precautions.

## 3. Boundary Justification Versus Full-Scale Humanoids

The supplied framework contrasts C-R&D platforms with full-scale humanoids characterized as approximately 1.6 m or taller and 60 kg or heavier. These are category-design thresholds from the research, not a demonstrated universal industry standard. The full-scale comparison emphasizes human-world tool use, industrial or domestic labor and heavier payload transport.

| Dimension | Compact research platforms | Full-scale general-purpose platforms |
| :--- | :--- | :--- |
| Reference stature | 1.20–1.45 m | Approximately 1.6 m or taller |
| Reference mass | 30–50 kg | Approximately 60 kg or heavier |
| Primary objective | Algorithm and motion development | Labor and task execution |
| Handling emphasis | Laboratory portability | Human-scale working envelope |
| Dynamic emphasis | Agility and experimental recovery | Payload and useful work |

The practical distinction is the experimental operating envelope. The supplied research argues that compact stature and lower mass can reduce handling difficulty and support dynamic maneuvers. It does not provide comparative fall-energy measurements, recovery success rates or gait-cycle data; consequently, superior safety or agility should not be treated as experimentally established across the category.

Physical size alone is also insufficient. A compact robot intended principally for production work would not automatically satisfy the research-purpose criterion, while a larger research robot would remain outside this particular compact category.

### Candidate accounting

The supplied research names **six candidate or comparison robots**. Under the core height, mass and purpose criteria, **four qualify, none is borderline on the reported core specifications, and two are excluded by stated purpose**. Under a stricter reading that requires verified payload and price compliance, all four qualifying robots become provisional because those attributes are not individually documented.

| Candidate | Core-criteria result | Strict-profile result | Basis |
| :--- | :--- | :--- | :--- |
| Unitree G1 | Qualifying | Provisional | Compact research/developer platform |
| AgiBot X1 | Qualifying | Provisional | Compact AI-research platform |
| Fourier N1 | Qualifying | Provisional | Compact motion-control platform |
| Booster T2 | Qualifying | Provisional | Compact embodied-AI platform |
| Unitree H2 | Excluded | Excluded | Full-scale labor-oriented comparator |
| Tesla Optimus | Excluded | Excluded | Full-scale labor-oriented comparator |

The supplied research identifies the last two as full-scale comparators but supplies no model-specific dimensions or masses for them. Their exclusion therefore rests on the stated purpose boundary, rather than an independently demonstrated dimensional failure.

## 4. Representative Robots

The representative specifications below reproduce the supplied research’s comparison set. G1 has the strongest model-specific documentation trail in that set, while X1 also has an identified manufacturer product source.

| Robot | Manufacturer | Height (m) | Mass (kg) | DoF | Research emphasis |
| :--- | :--- | ---: | ---: | ---: | :--- |
| Unitree G1 | Unitree Robotics | 1.32 | 35 | 23–43 | Commercial research/education |
| AgiBot X1 | AgiBot | 1.30 | 33 | 34 | Open-source AI research |
| Fourier N1 | Fourier Intelligence | 1.25 | 32 | 28 | Laboratory motion control |
| Booster T2 | Booster Robotics | 1.40 | 38 | 32 | Embodied-AI development |

All four fall within the proposed height and mass envelope. The supplied research also identifies comparative humanoid databases, but does not give model-specific source mappings for the Fourier N1 and Booster T2 rows; those specifications should therefore be treated as supplied comparison data rather than independently verified manufacturer values.

The G1’s reported 23–43 DoF range represents configuration variation, whereas the BOM below allocates **23 integrated joint modules**. It should not be interpreted as covering every higher-DoF configuration or optional subsystem.

## 5. Unitree G1 Component Bill of Materials

### Scope and accounting

The representative assembled-mass anchor is **35.0 kg**, identified as directly reported in the supplied research. The component model uses integrated joint modules combining motor, reducer, encoder and driver; the research attributes its engineering interpretation to teardown analysis and its mass anchor to product/database information.

Component weights below reproduce the supplied allocation. Torque classes and quantities are retained as estimated BOM descriptors, not presented as an independently verified joint-by-joint manufacturer specification. Each three-value sequence is **Min / Mode / Max**, in kilograms.

### Actuation and power

| Component | Qty | Per unit (kg) | Total (kg) | Evidence |
| :--- | ---: | :--- | :--- | :--- |
| Knee module, 120 Nm class | 2 | 1.15 / 1.25 / 1.35 | 2.30 / 2.50 / 2.70 | Estimate |
| Hip/waist module, 60–90 Nm class | 7 | 0.90 / 1.00 / 1.10 | 6.30 / 7.00 / 7.70 | Estimate |
| Ankle/shoulder module, 40 Nm class | 10 | 0.55 / 0.65 / 0.75 | 5.50 / 6.50 / 7.50 | Estimate |
| Arm/wrist module, 15–20 Nm class | 4 | 0.35 / 0.40 / 0.45 | 1.40 / 1.60 / 1.80 | Estimate |
| Smart Li-ion battery, 9,000 mAh, 13S | 1 | 2.30 / 2.50 / 2.70 | 2.30 / 2.50 / 2.70 | Derived* |

The actuation allocation totals **15.50 / 17.60 / 19.70 kg**, calculated from the supplied rows. The battery retains the research’s Derived designation, but the underlying mass calculation is not supplied and cannot be independently reproduced.

### Computing and perception

| Component | Qty | Per unit (kg) | Total (kg) | Evidence |
| :--- | ---: | :--- | :--- | :--- |
| Main controller, RK3588 + Orin | 1 | 0.35 / 0.40 / 0.45 | 0.35 / 0.40 / 0.45 | Estimate |
| Livox MID360 3D LiDAR | 1 | 0.65 / 0.65 / 0.65 | 0.65 / 0.65 / 0.65 | Direct* |
| Intel RealSense D435i | 1 | 0.08 / 0.10 / 0.12 | 0.08 / 0.10 / 0.12 | Direct* |

The supplied research identifies the MID360 product documentation as its perception-component source. Asterisks preserve the research’s original evidence designations: the D435i range is called Direct there, but no dedicated source or explanation for its spread is provided. It is therefore a reported input, not an independently established measurement interval.

### Structure and secondary systems

| Component | Qty | Per unit (kg) | Total (kg) | Evidence |
| :--- | ---: | :--- | :--- | :--- |
| Primary aluminum frame | 1 | 5.50 / 6.50 / 7.50 | 5.50 / 6.50 / 7.50 | Estimate |
| External CFRP/ABS/PA shell | 1 | 2.80 / 3.20 / 3.60 | 2.80 / 3.20 / 3.60 | Estimate |
| Wiring harness/connectors | 1 | 1.10 / 1.30 / 1.50 | 1.10 / 1.30 / 1.50 | Estimate |
| Fasteners and bearings | 1 | 1.80 / 2.20 / 2.60 | 1.80 / 2.20 / 2.60 | Estimate |
| Fans and heatpipes | 1 | 0.45 / 0.55 / 0.65 | 0.45 / 0.55 / 0.65 | Estimate |

A quantity of one denotes an aggregate assembly or allowance, not necessarily a single physical part. The estimate includes secondary hardware explicitly rather than treating it as an unallocated residual.

### Mass reconciliation

| Accounting measure | Min (kg) | Mode (kg) | Max (kg) | Evidence |
| :--- | ---: | ---: | ---: | :--- |
| Component-row sum | 30.53 | 35.00 | 39.47 | Derived |
| Supplied rounded total | 30.5 | 35.0 | 39.5 | Derived |
| Reported assembled anchor | — | 35.0 | — | Direct |

The original research labels the entire total range Direct. Only the central assembled anchor supports that interpretation; the minimum and maximum are sums of estimated or derived component bounds. The corrected distinction preserves the supplied numbers without implying that complete robots were measured at both endpoints.

## 6. Material Composition by Grade

The material model is a second allocation of the same representative robot, not an additional mass inventory. It estimates materials across actuators, structure, electronics and battery systems. All quantities below are **Estimates**; named grades are assumed allocations rather than a verified manufacturer material declaration.

| Material grade or family | Principal allocation | Min (kg) | Mode (kg) | Max (kg) |
| :--- | :--- | ---: | ---: | ---: |
| Al 6061-T6 / 7075-T6 | Links and structural frame | 10.5 | 12.0 | 13.5 |
| PA66 / ABS / PC | Covers and internal brackets | 4.5 | 5.5 | 6.5 |
| Bearing steel, 52100 | Bearings and gearbox elements | 3.5 | 4.2 | 5.0 |
| Copper | Windings and wiring | 3.0 | 3.8 | 4.5 |
| High-strength steel, unspecified | Impact reinforcement | 2.2 | 2.8 | 3.5 |
| Li-ion materials, assumed NMC | Battery allocation | 2.0 | 2.5 | 3.0 |
| NdFeB magnets | Permanent-magnet motors | 1.2 | 1.5 | 1.8 |
| CFRP, unspecified grade | Shell segments | 0.8 | 1.2 | 1.6 |
| Solder / glass / other | Sensors and miscellaneous parts | 0.8 | 1.0 | 1.2 |
| Silicon / FR-4 | Control electronics | 0.4 | 0.5 | 0.7 |
| **Total** | **Estimated material allocation** | **28.9** | **35.0** | **41.3** |

Aluminum represents approximately **34.3%** of central mass, while the two steel categories together represent **20.0%**; both percentages are Derived from this table. The central model consequently remains metal-dominated despite its lightweight shell materials.

Several limitations matter. The aluminum grades and polymer families are grouped rather than individually resolved, the reinforcement steel has no specified grade, and NMC battery chemistry is expressly assumed. Battery “materials” also form an aggregate allocation; the research does not separate active materials, enclosure, electrolyte and internal conductors.

The material envelope, **28.9–41.3 kg**, differs from the component envelope, **30.53–39.47 kg**. Their central values reconcile at **35.0 kg**, but their bounds are independent assumptions and must not be treated as matched minimum- and maximum-build configurations.

## 7. Development Outlook: 2025–2040

The following trajectory reproduces the supplied research’s scenario. Every value is an **Estimate**, including the 2025 baseline: the research provides neither dated quotations nor sufficient supporting measurements to treat the series as observed market history.

| Scenario year | Mass (kg) | Battery energy density (Wh/kg) | Cost (USD) | Status |
| :--- | ---: | ---: | ---: | :--- |
| 2025 | 35 | 220 | 16,000 | Estimated baseline |
| 2030 | 28 | 350 | 12,000 | Projection |
| 2035 | 25 | 450 | 10,000 | Projection |
| 2040 | 22 | 550 | 8,000 | Projection |

The research calls the 2040 cost inflation-adjusted but supplies no base year. Battery energy density is likewise not defined consistently as cell-level or pack-level, limiting interpretation of both cost and runtime projections.

### 2025: Initial scaling

The scenario emphasizes production stabilization and aluminum-based structures. Its narrative suggests pricing near **$12,000** as manufacturing volumes increase, whereas its summary table uses **$16,000**. Neither figure has a dated supporting quotation, so neither is better supported as an observed price; the table value is retained only as the internally consistent trajectory baseline.

### 2030: Lightweighting

The proposed material transition introduces **AZ91D magnesium** for non-impact structures and **carbon-fiber-reinforced PEEK** for shells. The scenario describes a **15–20%** mass reduction and a representative mass near **28 kg**; relative to the **35 kg** baseline, that endpoint is a Derived **20%** reduction.

The research pairs **350 Wh/kg** with an estimated **four-hour** runtime, but supplies no usable-energy, average-power or duty-cycle calculation. Runtime therefore remains a separate projection, not a result demonstrated by the energy-density figure.

### 2035: Greater integration

The scenario proposes integrated liquid cooling in joint modules and solid-state batteries, with a representative mass of **25 kg**. It anticipates sustained high-torque operation in compact form and lower laboratory fire risk. These are proposed outcomes, not established product capabilities or demonstrated safety findings.

### 2040: Personal laboratory assistants

The endpoint envisages modular, plug-and-play joints, repairs by non-experts and a shift toward fully recyclable bio-composites. Its representative mass is **22 kg**, with an estimated cost of **$8,000**. Neither recyclability nor repairability is supported by a quantified validation method in the supplied research.

The outlook also creates a classification issue: the projected **28 kg**, **25 kg** and **22 kg** platforms fall below the present **30 kg** lower boundary. They are therefore prospective descendants of the category, not strict members under unchanged criteria.

## 8. Appendix: Consolidated Accounting and Limitations

The component model can be condensed into the following auditable group totals.

| Component group | Quantity basis | Mode mass (kg) | Evidence |
| :--- | :--- | ---: | :--- |
| Integrated joint modules | 23 modules | 17.60 | Estimate |
| Frame and shell | 2 aggregate assemblies | 9.70 | Estimate |
| Battery | 1 pack | 2.50 | Derived input |
| Compute and perception | 3 assemblies | 1.15 | Mixed |
| Wiring and secondary systems | 3 allowances | 4.05 | Estimate |
| **Total** | **Representative configuration** | **35.00** | **Derived sum** |

The research’s condensed appendix calls several multi-component groups a quantity of one. The quantity basis above clarifies the accounting without changing mass allocations.

For scientific use, the principal unresolved needs are configuration-specific weighed components, a grade-resolved material declaration, documented battery mass derivation and dated commercial evidence. Until those are available, the strongest conclusion is that the supplied central allocations reconcile arithmetically—not that the component or material model has been independently validated.

## Sources

Manufacturer and developer documentation identified in the supplied research comprises the Unitree G1 official specifications, the G1 EDU technical specification compilation and the AgiBot X1 product overview. These support the representative-platform context, subject to configuration and source-mapping limitations noted above.

The supplied engineering evidence also identifies a G1 teardown and economics analysis, comparative humanoid databases, and the Livox MID360 product documentation. These provide the stated basis for the teardown-informed allocation, platform comparisons and perception-component input.

Detailed component weights, material grades and future trajectories remain the supplied research’s estimates except where explicitly designated otherwise. No dated source evidence accompanies the price scenarios, and no cited source is presented here as validating the outlook through 2040.

---

## Sources

1. https://www.unitree.com/g1/ — <https://www.unitree.com/g1/>
2. https://robostore.com/blogs/news/unitree-g1-edu-ultimate-technical-specifications — <https://robostore.com/blogs/news/unitree-g1-edu-ultimate-technical-specifications>
3. https://www.agibot.com/products/X1 — <https://www.agibot.com/products/X1>
4. https://humanoid.guide/humanoid-robots-database/ — <https://humanoid.guide/humanoid-robots-database/>
5. https://www.robotlar.org/en/humanoid-robots — <https://www.robotlar.org/en/humanoid-robots>
6. https://chinabizinsider.com/unitree-g1-teardown-decoding-the-economics-and-engineering-of-the-worlds-best-selling-humanoid-robot/ — <https://chinabizinsider.com/unitree-g1-teardown-decoding-the-economics-and-engineering-of-the-worlds-best-selling-humanoid-robot/>
7. https://www.livoxtech.com/mid-360 — <https://www.livoxtech.com/mid-360>
