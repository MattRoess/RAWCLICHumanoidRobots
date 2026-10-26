# Industrial Logistics & Warehousing Humanoids: Components, Materials and Outlook to 2040
*Matthias Roesslein — October 23, 2026*

Industrial logistics and warehousing humanoids are best distinguished by their operating requirements, not by humanlike appearance: repeated load handling, recoverable energy supply, shared-workspace operation and integration into industrial workflows. UBTECH Walker S2 provides the component anchor for this category, while Agility Digit 5, Apptronik Apollo 2 and Figure 03 illustrate its boundaries. The supplied component model yields an estimated Walker S2 mass of **72.4 kg at the modal configuration**, but its material inventory accounts for only **65.0 kg**; the resulting **7.4 kg gap is unresolved**, so neither inventory should be treated as a verified manufacturing BOM.

## 1. Category Definition

Industrial Logistics & Warehousing covers humanoids configured primarily for manufacturing support and goods movement in human-designed environments. Relevant tasks include picking, placing, assembly support and machine tending. The Walker S2 material describes automotive applications including wire-harness insertion, clip placement and visual quality inspection, placing industrial manipulation—not general social interaction—at the center of its intended role.

The category is therefore application-led. A humanoid can have general-purpose capabilities yet fall within this category when its configuration and operating model prioritize industrial work. Conversely, a broadly capable platform does not qualify merely because it can demonstrate a warehouse task.

### Evidence and numerical conventions

This report distinguishes three evidence classes:

- **Direct:** specifications or descriptions reported in the supplied source-linked material. “Direct” does not mean independently measured or certified.
- **Derived:** arithmetic calculated from reported specifications or estimated inputs. A derived result retains the uncertainty of its inputs.
- **Estimate:** engineering assumptions, component allocations, material allocations and future scenarios.

**Min / Mode / Max** denotes the supplied low, central and high engineering cases. These are not statistical confidence intervals. All component and material masses below are **Estimates**, except explicitly identified **Derived** totals and per-unit calculations.

## 2. Criteria and Category Screen

The supplied category proposal combines functional criteria with ambitious performance targets. These must be separated: industrial suitability can be assessed from intended application, whereas numerical uptime, integration and safety requirements need configuration-specific evidence.

| Criterion | Category interpretation | Proposed target | Evidence limitation |
| :--- | :--- | :--- | :--- |
| Primary application | Industrial handling or manufacturing support | Repeated productive tasks | Application descriptions available |
| Manipulation capability | Load handling with stable locomotion | Estimated 10–25 kg core range | Ratings lack common test conditions |
| Operational availability | Energy recovery without lengthy interruption | Estimated ≥18 h/day | Daily availability not demonstrated |
| Energy strategy | Swap or rapid replenishment | Estimated swap or <10 min charge | Recovery times are not runtime |
| Shared-workspace safety | Protection appropriate to nearby workers | Redundant control and perception | Compliance not established |
| Enterprise integration | Coordination with industrial workflows | FMS/WMS compatibility | Interfaces not documented |

These are screening criteria and design targets, not a declaration that every representative robot satisfies every threshold. The supplied notes also give a broader **10–30 kg** payload range; this report retains **10–25 kg** as the core comparison range and treats the broader range as an estimated category envelope.

The notes propose **SIL2 / PL d** as a safety target, but provide no certification evidence establishing that requirement or demonstrating compliance across the candidates. Accordingly, neither that designation nor a “barrierless” description is treated here as proof of safe deployment.

### Candidate accounting

The supplied comparison contains **four candidates**. Under an industrial-primary-use interpretation, **three qualify**, **one is borderline**, and **none are otherwise excluded**. This is a functional classification, not a compliance assessment.

| Candidate | Classification | Basis | Boundary issue |
| :--- | :--- | :--- | :--- |
| UBTECH Walker S2 | Qualifying | Manufacturing and logistics focus | Daily uptime unverified |
| Agility Digit 5 | Qualifying | Industrial handling and shared workspace | Safety scope unverified |
| Apptronik Apollo 2 | Qualifying | Modular logistics focus | Configuration-dependent capability |
| Figure 03 | Borderline | Generalist, multi-utility positioning | Industrial role versus general purpose |

The application descriptions support Walker S2, Digit 5 and Apollo 2 as industrial-category representatives. Figure 03 qualifies under a permissive, task-based reading when configured for industrial work; under a strict industrial-primary-purpose reading, it is excluded because the supplied comparison positions it as generalist. Those alternative readings produce, respectively, **four qualifying candidates**, or **three qualifying and one excluded**.

## 3. Boundary Justification and Representative Robots

### Reported specifications

The following figures are **Direct reported values** from the supplied source-linked comparison. They are not normalized measurements: payload posture, duty cycle and the inclusion of batteries or tooling in mass are not consistently specified.

| Robot | Mass (kg) | Payload (kg) | DoF | Reported energy strategy |
| :--- | ---: | ---: | :--- | :--- |
| UBTECH Walker S2 | Approximately 70 | 15 | 52 | 3 min autonomous swap |
| Agility Digit 5 | 129 | 22.7 | — | 9 min rapid charge |
| Apptronik Apollo 2 | 75 | 25 | 30+ | Swap and opportunity charging |
| Figure 03 | 61 | 20 | 30 | 5 h runtime; inductive charging |

Walker S2 figures are associated with the supplied product and specification sources; the other rows follow their respective comparison sources. The energy column deliberately preserves unlike measures: swap duration, charging duration and runtime cannot be ranked as though they were the same metric.

### What the comparison establishes

**Walker S2 anchors the availability-oriented design.** Its reported dual-battery arrangement allows one battery to maintain system power while the other is exchanged. That supports a continuity-of-operation strategy, but a short swap alone does not establish uninterrupted industrial productivity or a measured daily operating duration.

**Digit 5 anchors the shared-workspace boundary.** The supplied description emphasizes redundant safety controllers and cage-free operation alongside its reported load-handling capability. This differentiates its industrial proposition, while leaving the exact safety conditions and certification scope unresolved.

**Apollo 2 anchors configuration flexibility.** The supplied comparison describes modular bipedal and wheeled arrangements, together with swappable batteries and opportunity charging. Its inclusion follows the logistics function; a wheeled arrangement should not be assumed to retain the locomotion characteristics of its bipedal configuration.

**Figure 03 anchors the general-purpose boundary.** The supplied description emphasizes generalist operation and vision-language capabilities for less-scripted tasks. These capabilities may support industrial work, but do not by themselves establish sustained industrial availability, enterprise integration or validated collaborative safety.

### Boundary versus general-purpose and service robots

Full-scale general-purpose humanoids are differentiated here by the breadth of their intended task repertoire. Industrial logistics humanoids are differentiated by the operating conditions and work requirements they prioritize. Figure 03 demonstrates the overlap: general-purpose architecture and industrial deployment are not mutually exclusive.

Service robots fall outside the strict category when service interaction, rather than industrial handling or manufacturing support, defines the principal application. No separate service-robot candidate is described sufficiently in the supplied category data for an additional quantitative screen. The boundary is therefore functional; this report does not invent a size, intelligence or appearance threshold.

## 4. Walker S2 Component BOM

### Scope and accounting method

The supplied Walker S2 BOM is an engineering reconstruction, not a manufacturer-issued parts list. It assigns masses to actuators, reducers, batteries, structure, covers, electronics, sensors, wiring and auxiliary hardware. The compute and sensing descriptions are associated with the supplied Walker S2 equipment source, but the component masses remain **Estimates**.

To avoid double counting, the tables interpret the actuator rows as **excluding the separately listed reducers**. The supplied data does not conclusively establish that accounting boundary. If its actuator estimates already include reducers, the reconstructed total would be overstated.

### Per-unit masses

All values are kilograms per item. Values below are **Derived from estimated group masses divided by quantity**; rounding affects displayed per-unit values only.

| Component | Quantity | Unit Min (kg) | Unit Mode (kg) | Unit Max (kg) |
| :--- | ---: | ---: | ---: | ---: |
| High-torque actuators | 8 | 1.125 | 1.200 | 1.313 |
| Medium-torque actuators | 22 | 0.409 | 0.450 | 0.500 |
| Low-torque actuators | 22 | 0.136 | 0.150 | 0.159 |
| Reducers | 52 | 0.163 | 0.183 | 0.202 |
| Battery packs | 2 | 4.500 | 4.800 | 5.250 |
| Main frame / skeleton | 1 | 16.500 | 18.000 | 20.000 |
| Outer shell / cladding | 1 | 6.000 | 6.500 | 7.200 |
| Controllers / AI compute | 1 | 1.000 | 1.200 | 1.500 |
| Sensor suite | 1 | 0.600 | 0.800 | 1.000 |
| Wiring / power distribution | 1 | 2.200 | 2.500 | 2.800 |
| Thermal hardware / fasteners | 1 | 1.200 | 1.500 | 1.800 |

The reducer unit values are averages across the proposed set, not estimates for identical reducers. The actuator allocation sums to the reported **52 DoF**, but a one-actuator-per-DoF interpretation remains a modeling assumption.

### Component-group totals and proposed construction

All row masses are **Estimates**; the final row is their **Derived** sum. Material and architecture notes describe the supplied reconstruction rather than verified part specifications.

| Component | Min (kg) | Mode (kg) | Max (kg) | Proposed construction |
| :--- | ---: | ---: | ---: | :--- |
| High-torque actuators | 9.0 | 9.6 | 10.5 | 42CrMo shafts; 7075-T6 housings |
| Medium-torque actuators | 9.0 | 9.9 | 11.0 | 6061-T6 housings |
| Low-torque actuators | 3.0 | 3.3 | 3.5 | Sintered gears; hybrid housings |
| Reducers | 8.5 | 9.5 | 10.5 | Harmonic and cycloidal units |
| Battery packs | 9.0 | 9.6 | 10.5 | LiFePO4; PC/ABS enclosure |
| Main frame / skeleton | 16.5 | 18.0 | 20.0 | Aluminum, magnesium, composites |
| Outer shell / cladding | 6.0 | 6.5 | 7.2 | ABS/PC, fabric, silicone |
| Controllers / AI compute | 1.0 | 1.2 | 1.5 | Processor and accelerator assembly |
| Sensor suite | 0.6 | 0.8 | 1.0 | Cameras, IMU, force/torque sensing |
| Wiring / power distribution | 2.2 | 2.5 | 2.8 | Copper, insulation, circuit boards |
| Thermal hardware / fasteners | 1.2 | 1.5 | 1.8 | Aluminum heatsinks; steel fasteners |
| **Derived total** | **66.0** | **72.4** | **80.3** | **Leaf-component sum** |

The source reconstruction identifies an Intel i7 and NVIDIA Jetson AGX Orin 64GB compute arrangement, together with binocular RGB, RGB-D, inertial and six-axis force/torque sensing. These are reported equipment descriptions, not independently verified configuration details.

### Reconciliation with the supplied totals

The supplied actuator subtotal is **21.5 / 23.0 / 25.0 kg**, whereas its detailed actuator rows sum to **21.0 / 22.8 / 25.0 kg**. The supplied overall total of **64.0 / 72.0 / 80.0 kg** also differs from the leaf-row sum of **66.0 / 72.4 / 80.3 kg**.

This report uses the detailed-row arithmetic because it is reproducible. That choice resolves an accounting inconsistency, not the underlying uncertainty in component masses. The reported approximately **70 kg** robot specification remains a separate Direct figure, rather than being silently replaced by the BOM estimate.

## 5. Material Composition

The following is the complete supplied material allocation. Every row is an **Estimate**; totals are **Derived** sums. Where several grades share a row, the data supports only their combined mass—not separate grade-level quantities.

| Material family / proposed grades | Min (kg) | Mode (kg) | Max (kg) |
| :--- | ---: | ---: | ---: |
| Aluminum: 6061-T6 / 7075-T6 | 22.0 | 25.0 | 28.0 |
| Steel: 42CrMo / GCr15 / fastener steel | 8.0 | 10.0 | 12.0 |
| Magnesium: AZ91D | 2.0 | 4.0 | 6.0 |
| Plastics: ABS/PC / PA66-GF | 5.5 | 6.5 | 7.5 |
| Composites: CFRP / GFRP | 3.0 | 4.5 | 6.0 |
| Copper / electronics / NdFeB / FR-4 | 3.5 | 4.2 | 5.0 |
| Battery constituents: LiFePO4 system | 7.5 | 8.5 | 9.5 |
| Glass / fabric / silicone | 1.5 | 2.3 | 3.0 |
| **Allocated material total** | **53.0** | **65.0** | **77.0** |

Aluminum is the largest estimated material allocation. However, the grouped electronics row combines chemically different materials, and the battery row combines constituents rather than providing a chemical inventory. This is consequently a grade-identified engineering estimate, not a complete grade-resolved material declaration.

### Material mass closure

| Accounting measure | Min (kg) | Mode (kg) | Max (kg) |
| :--- | ---: | ---: | ---: |
| Derived component total | 66.0 | 72.4 | 80.3 |
| Derived material allocation | 53.0 | 65.0 | 77.0 |
| **Unallocated difference** | **13.0** | **7.4** | **3.3** |

The modal material inventory covers a **Derived 89.8%** of the modal component estimate. The unallocated difference is an accounting residual, not evidence for a particular missing material. It should not be distributed proportionally without additional information.

## 6. Development Outlook: 2025–2040

The supplied trajectory is an **Estimate scenario**, not a sourced market forecast or manufacturer commitment. Its baseline and future values are retained to make the proposed development direction explicit.

| Estimated metric | 2025 | 2030 | 2035 | 2040 |
| :--- | ---: | ---: | ---: | ---: |
| System mass (kg) | 70 | 60 | 50 | 45 |
| Payload (kg) | 15 | 25 | 35 | 45 |
| Energy density (Wh/kg) | 180 | 350 | 500 | 700 |
| Actuator efficiency (%) | 75 | 85 | 92 | 95 |
| Unit-cost assumption (USD) | 106,000 | 65,000 | 40,000 | 25,000 |

These values form an illustrative pathway, not procurement specifications. In particular, the cost row is a scenario assumption rather than an observed quotation, and the energy-density row does not specify whether it refers to cells or complete packs.

### 2025: availability-oriented industrialization

The supplied baseline emphasizes early commercialization, aluminum/steel actuation and battery-swap infrastructure. Walker S2's reported autonomous swapping provides the clearest example of this availability strategy. The evidence does not establish fleet-wide utilization, maintenance downtime or a measured daily production duty cycle.

### 2030: lightweighting and energy storage

The scenario proposes semi-solid-state batteries, an estimated **40%** energy-density improvement, an **80% magnesium/CFRP structural mix**, and approximately **15%** body-weight reduction. These are hypotheses, not demonstrated Walker S2 developments.

There is an internal numerical conflict: increasing the trajectory's energy density from **180 to 350 Wh/kg** represents a **Derived 94.4% increase**, not **40%**. The narrative and numerical table therefore cannot be treated as one consistent battery forecast. The change from **70 to 60 kg** is a **Derived 14.3%** reduction, broadly matching the lightweighting direction.

### 2035: coordinated operation and selective substitution

The scenario anticipates autonomous fleet coordination, zero-touch energy servicing and selective replacement of internal metal parts with PEEK or CF-PEEK. The data does not quantify the associated material substitution or provide supporting wear and maintenance results. Those substitutions should therefore remain separate from the present-day material inventory.

### 2040: structural integration

The long-range scenario proposes structural batteries and titanium-magnesium alloys, alongside a **45 kg** robot carrying **45 kg**. This gives a **Derived payload-to-mass ratio of 1.00**, but is not a demonstrated capability. Commodity status and widespread adoption of these materials are speculative outcomes, not established endpoints.

The practical development test is whether lower mass and greater payload can coexist with availability, maintainability and shared-workspace requirements. The supplied trajectory does not resolve those trade-offs.

## 7. Appendix: Calculation Basis and Limitations

### Battery consistency check

The supplied reconstruction assumes **two 48 V, 9 Ah packs**. Using those inputs gives:

- **Derived nominal combined energy:** 2 × 48 × 9 = **864 Wh**.
- **Derived pack-level specific energy at modal battery mass:** 864 Wh ÷ 9.6 kg = **90 Wh/kg**.

This differs from the outlook's estimated **180 Wh/kg** baseline. A cell-versus-pack distinction might explain the difference, but the supplied data does not establish that explanation. The chemistry assignment and pack-mass model should therefore remain provisional.

### Interpretation rules

The BOM is complete only at the supplied component-group level; it is not a procurement-level inventory. Tooling, configuration boundaries and possible overlaps between component groups remain insufficiently defined. Likewise, no common payload test protocol or measured availability dataset is provided for the four robots.

For engineering decisions, the highest-priority missing evidence is a reconciled component and material mass balance, followed by configuration-specific payload, energy and safety documentation. Until then, the report supports category comparison and scenario analysis—not certified performance, lifecycle assessment or material purchasing quantities.

## 8. Sources

Product positioning and reported Walker S2 specifications draw on the UBTECH product description and the supplied Walker S2 specification entry. Equipment descriptions draw on the Terra Robotics material, while the industrial application context is associated with the supplied Walker review.

The comparative positioning uses the supplied Digit 5 summary, Apptronik material and Figure 03 technical summary. These sources support the reported product descriptions; they do not establish the estimated component masses, grade allocations or development trajectory.

The BOM, material inventory and outlook are explicitly identified as Estimates from the supplied category data. Arithmetic reconciliations are Derived and are presented separately from source-reported specifications.

---

## Sources

1. ubtrobot.com/en/humanoid/products/walker-s2 — <https://www.ubtrobot.com/en/humanoid/products/walker-s2>
2. blog.robozaps.com/b/ubtech-walker-s-review — <https://blog.robozaps.com/b/ubtech-walker-s-review>
3. remio.ai/post/agility-digit-5-humanoid-robot — <https://www.remio.ai/post/agility-digit-5-humanoid-robot>
4. <https://apptronik.com/apollo/apollo-2>
5. humanoid.guide/product/figure-03/ — <https://humanoid.guide/product/figure-03/>
6. humanoidhub.ai/robots/ubtech-walker-s2 — <https://www.humanoidhub.ai/robots/ubtech-walker-s2>
7. terra-robotics.de/en/products/ubtech-walker-s2 — <https://terra-robotics.de/en/products/ubtech-walker-s2>
