# Humanoid Robots Through 2040: Taxonomy, Component Implications, and Market Outlook
*Matthias Roesslein — October 23, 2026*

## Executive Summary

The recommended taxonomy distinguishes six humanoid-robot categories by their dominant mission, operating environment, and resulting engineering requirements—not by locomotion or price alone. These categories are **Compact Research & Developer; Full-Scale General-Purpose / AI Research; Industrial Logistics & Warehousing; Service / Healthcare / Interaction; Heavy-Duty / High-Performance / Hazardous-Environment; and Defense / Public Safety**. The supplied market scenario projects annual shipments rising from an estimated 40,000 in 2025 to 25 million in 2040, with industrial and service applications together accounting for 60% of the modeled 2040 total. These are scenario estimates, not verified shipment observations or a consensus forecast.

The taxonomy connects applications to component and material choices. Compact platforms emphasize manageable mass and experimental accessibility; full-scale general-purpose platforms emphasize manipulation and AI flexibility; industrial platforms emphasize uptime and payload; service platforms emphasize interaction and contact safety; heavy-duty platforms emphasize mechanical and environmental resilience; and defense/public-safety platforms add mission assurance and protection requirements. The representative bill-of-materials anchors are Unitree G1, Unitree H2, UBTECH Walker S2, AgiBot A2, Boston Dynamics Atlas, and a clearly notional defense/public-safety configuration, respectively.

Across the supplied category projections, the common direction is lightweighting, greater use of magnesium, carbon-fiber-reinforced polymers and engineering plastics, improved actuator efficiency, better batteries, and lower unit cost. Exact substitution rates, certification milestones, and advanced battery adoption dates remain speculative. Moreover, several supplied component and material estimates do not reconcile to their stated robot masses; they support architectural comparison more reliably than precise material-demand forecasting.

## 1. Classification Approach and Boundaries

### Mission and engineering requirements define the categories

A useful classification must explain why robots require different actuators, structures, batteries, interfaces, and protection systems. The proposed approach therefore assigns a platform according to its **dominant intended application and associated design constraints**, then records secondary capabilities separately.

The six categories compare as follows. Numerical bands are working definitions from the supplied category analyses, not universal industry standards.

| Category | Dominant requirement | Working boundary | BOM anchor |
| :--- | :--- | :--- | :--- |
| Compact Research & Developer | Accessible experimentation | Typically 1.20–1.45 m; 30–50 kg | Unitree G1 |
| Full-Scale General-Purpose / AI Research | Versatile manipulation and learning | Typically 1.60–1.85 m; 50–80 kg | Unitree H2 |
| Industrial Logistics & Warehousing | Payload and sustained uptime | Typically 10–25 kg handling; multi-shift operation | UBTECH Walker S2 |
| Service / Healthcare / Interaction | Human-facing assistance | Expressive interfaces; moderate loads | AgiBot A2 |
| Heavy-Duty / High-Performance / Hazardous-Environment | Mechanical and environmental resilience | High-output actuation; impact tolerance; hardening | Boston Dynamics Atlas |
| Defense / Public Safety | Mission assurance in high-stakes settings | Secure control; redundancy; mission-specific protection | Notional configuration |

These are engineering clusters rather than rigid size classes. The anchor platforms illustrate different optimization priorities, while overlapping platforms demonstrate why mission must take precedence over any single specification.

### Why locomotion-only and price-only schemes are insufficient

A locomotion-only scheme groups together robots whose requirements differ substantially. A compact research biped, an industrial handling biped, and a protected public-safety biped may share a basic body plan while imposing different demands on torque, thermal management, battery servicing, human contact, and communications security. Conversely, the supplied Apollo comparison includes bipedal and wheeled configurations serving related logistics functions.

Price is also unsuitable as the principal organizing variable. The supplied projections anticipate substantial cost reductions across categories, while research configuration, dexterous hands, protection, and mission equipment can change the cost of an otherwise related platform. Price is therefore better treated as an economic attribute, alongside payload, runtime, and maintainability, rather than as the category boundary.

Size remains useful, especially for separating compact experimental systems from human-scale platforms. However, the supplied service examples span different heights while retaining a common interaction-oriented purpose. Their commonality lies in human-facing interfaces and task design, not a single dimensional threshold.

### Non-humanoid bridging platforms

**Non-humanoid dual-arm systems, mobile manipulators, and quadrupeds are essential comparators and technology lineage, but they are not primary humanoid categories.** They should be considered when comparing manipulation architectures, mobile task execution, perception, actuation, and environmental suitability.

This distinction also prevents market-boundary inflation. A wheeled mobile manipulator may compete for a warehouse task without qualifying as a primary humanoid in this report. Where a platform family offers multiple embodiments, its mission can inform comparison, but humanoid shipment totals should not automatically include every configuration. The supplied Apollo and KUAVO variant descriptions illustrate this boundary issue.

The representative set below is illustrative rather than an exhaustive product-qualification screen. Inclusion does not establish deployment maturity, certified safety, or compliance with every proposed category criterion.

## 2. Representative Robots and Category Anchors

### Compact Research & Developer

The compact category is justified by the combination of smaller dimensions, lower mass, research-oriented access, and portability. Its supplied working bands—1.20–1.45 m and 30–50 kg—separate it from platforms intended principally for human-scale work. Lower inertia and a smaller physical envelope can make experimentation more manageable, but “compact” must not be interpreted as inherently safe.

The Unitree G1 anchors the category at a reported height of 1.32 m and mass of 35 kg, with configuration-dependent degrees of freedom. AgiBot X1 provides an additional research-oriented comparator; the supplied category analysis also identifies Fourier N1 and Booster T2 as laboratory and embodied-AI development examples.

The G1 component model emphasizes integrated motor–reducer–encoder–driver joints. Its supplied modal estimate allocates 17.6 kg to joint modules, 9.7 kg to frame and shell, and 2.5 kg to the battery. These are analytical mass allocations, not a manufacturer-certified material inventory. The teardown and manufacturer specifications support the architecture and total-mass anchor more strongly than every inferred component weight.

### Full-Scale General-Purpose / AI Research

This category covers human-scale platforms whose central objective is adaptable manipulation and learning across tasks. The Unitree H2 anchor is reported at 1.82 m and approximately 70 kg, with 31 chassis degrees of freedom. Its positioning combines full-scale mobility with manipulation and AI research.

The supplied comparisons place Tesla Optimus, Figure 03, and Apptronik Apollo 2 near this boundary. Optimus and Figure represent broad task ambitions, whereas Apollo’s payload and battery-service emphasis pull it toward industrial logistics. Thus, a general-purpose architecture and an industrial deployment role are not mutually exclusive descriptions.

Dexterous hands, sensing, and computation distinguish this category more meaningfully than body height alone. The H2 Plus configuration is associated in the supplied material with an AI-development stack and higher-dexterity hands, but those configuration-specific features should not be attributed automatically to every H2 configuration.

### Industrial Logistics & Warehousing

Industrial logistics humanoids prioritize repeatable handling, operational availability, maintainability, and integration with production or warehouse workflows. Their distinguishing question is not simply whether they can perform a task, but whether they can sustain useful work across shifts.

UBTECH Walker S2 anchors this category through its dual-battery autonomous-swapping architecture. The supplied comparison reports a three-minute swap strategy and a representative 15 kg payload, illustrating why battery servicing can be as consequential as nominal battery capacity. Agility Digit 5, Apollo 2, and Figure 03 provide comparisons in shared-workspace operation, modularity, and generalist manipulation.

The supplied analysis proposes more than 18 operating hours per day as an industrial target. This should be read as a category design objective, not verified utilization for every named robot. Likewise, barrierless operation and safety-controller requirements are evaluation criteria; they do not establish that every comparator has certified approval for every workplace.

### Service / Healthcare / Interaction

Service platforms are distinguished by their front-facing relationship with users: reception, guidance, conversational interaction, and assistance in care or domestic environments. Interaction hardware, compliant behavior, and soft contact surfaces matter more here than maximum lifting performance.

AgiBot A2 is the anchor, with a reported mass of 69 kg and an interaction-oriented head display. Fourier GR-3 contributes the care-focused comparison through soft-touch construction and tactile sensing; Dobot Atom represents delicate commercial manipulation; and Leju KUAVO variants connect service use with research and teleoperation.

The healthcare label requires restraint. The supplied evidence supports care-oriented and non-medical assistance concepts, not a general claim of clinical effectiveness or medical-device authorization. Similarly, expressive interfaces and dialogue capability do not by themselves demonstrate reliable emotional understanding.

### Heavy-Duty / High-Performance / Hazardous-Environment

This category groups systems optimized for high mechanical output, impact tolerance, and demanding environments. Boston Dynamics Atlas is the representative anchor, compared with EngineAI T800, DEEP Robotics DR02, and a high-performance Apollo configuration. These examples emphasize different combinations of dynamic movement, load handling, and environmental resilience.

The supplied analyses disagree on strict thresholds. Their main criteria propose payload above 25 kg, major-axis peak torque above 400 N·m, and IP66/IP67 protection; an appendix relaxes these to above 20 kg, above 300 N·m, and IP65. Neither set is consistently applied across all examples. The better-supported conclusion is therefore a multi-attribute performance cluster, with individual thresholds retained as comparison metrics rather than universal entry requirements.

High-performance mobility must also be distinguished from hazardous-environment qualification. Agility or high torque alone does not establish suitability for explosive atmospheres, chemical exposure, or every field condition. Proposed future certification milestones remain projections, not present platform attributes.

### Defense / Public Safety

Defense and public safety warrant a separate category because adversarial interference and life-critical missions can alter the architecture even when the underlying mechanics resemble industrial or heavy-duty robots. Relevant considerations include redundant control, secure communications, protected electronics, remote operation, and mission-specific sensing.

The public examples supplied are Norinco Fuxi, EngineAI T800 security/public-safety variants, IHMC Alex in the U.S. Army xTechHumanoid context, and Foundation Phantom-style systems. They provide public reference points, not evidence of a standardized, mature defense-humanoid product class.

The defense BOM anchor is explicitly **notional**, with a target mass of 90 kg. Its armored shell, protected computation, and reinforced structure are scenario assumptions. The supplied sources explain environmental ruggedization, cryptographic standards, and protection-material options, but do not establish that all named robots satisfy the report’s proposed military, cybersecurity, export-control, or ballistic requirements. Such status must be assessed system by system.

## 3. Component and Material Implications

The taxonomy translates into different component priorities rather than six unrelated technologies. Electric actuation, structural alloys, engineering polymers, batteries, sensing, and computation recur throughout the supplied analyses; their proportions and integration strategies differ.

| Category | Actuator emphasis | Structural emphasis | Power and integration emphasis |
| :--- | :--- | :--- | :--- |
| Compact research | Integrated, lightweight joints | Aluminum; polymer/composite covers | Portable, replaceable modules |
| Full-scale general-purpose | Dexterity and broad motion capability | Lightweight frame; articulated hands | AI compute and multimodal sensing |
| Industrial logistics | Sustained torque and serviceability | Load-bearing links; durable joints | Swapping, charging, fleet integration |
| Service/healthcare | Backdrivability and contact response | Soft coverings; interaction surfaces | Audio, vision, displays, tactile sensing |
| Heavy-duty/hazardous | Torque density and shock tolerance | Reinforced alloys; protected joints | Cooling, sealing, high-discharge power |
| Defense/public safety | Resilience and mission reliability | Protected chassis; selective armor | Redundant power and secure electronics |

The practical implication is that a common actuator or material family can serve multiple categories, but not necessarily under the same load spectrum or assurance requirements. Supplier comparisons should therefore consider duty cycle, thermal conditions, shock exposure, and maintainability—not just peak torque or nominal robot mass.

### Limits of the supplied BOM estimates

The material tables are best treated as engineering estimates. They combine reported total masses with inferred component volumes, material substitutions, and configuration assumptions; they are not consistently reconciled inventories.

Several arithmetic discrepancies are material to interpretation:

- The Walker S2 component entries total **72.6 kg**, compared with a stated modal total of **72.0 kg**, while its separate material table totals **65.0 kg**.
- The Atlas component entries total **103.4 kg**, despite a **90 kg** target.
- The detailed notional defense component entries total **95.6 kg**, despite a **90 kg** target.
- The H2 analysis contains alternative frame and material allocations, even though its revised appendix reconciles to **70 kg**.

These are arithmetic checks on the supplied estimates, not revised manufacturer specifications. They prevent a defensible calculation of precise material tonnage from robot shipments. The stronger conclusion is architectural: joints and load-bearing structures are major mass contributors, while protection, cooling, battery strategy, and interaction equipment create category-specific additions.

## 4. Technology and Material Trends, 2025–2040

### Lightweighting without uniform material replacement

Across the category projections, aluminum remains the initial structural reference, with increasing proposed use of magnesium alloys, CFRP, and reinforced engineering plastics. The supplied material discussions identify magnesium for lightweight housings and supports, CFRP for selected reinforcement and covers, and PEEK-family polymers for components where mass, wear, or lubrication requirements motivate substitution.

This direction should not be read as wholesale replacement of steel or aluminum. The supplied BOMs retain steels in gears, bearings, shafts, and other highly loaded interfaces, alongside copper and permanent magnets in electric drives. In heavy-duty and protected systems, lightweighting competes with impact resistance, sealing, repairability, and armor mass.

Service-oriented projections add soft polymers and contact surfaces, whereas defense/public-safety scenarios add ceramics, aramids, and ultrahigh-molecular-weight polyethylene for selective protection. These are different material responses to different missions, not a single universal humanoid material recipe.

### Actuation, thermal management, and efficiency

The common actuator trajectory is toward improved integration, higher useful output per unit mass, and better thermal control. Compact platforms emphasize integrated joints; full-scale research systems add dexterous manipulation; industrial systems emphasize sustained output; and heavy-duty systems require greater shock tolerance and heat rejection.

The industrial category scenario projects actuator efficiency increasing from **75% in 2025 to 95% in 2040**. This is a modeling assumption in the supplied trajectory, not a measured industry-wide trend. Proposed transverse-flux, axial-flux, advanced reducer, and liquid-cooling developments likewise remain possible pathways rather than established adoption schedules.

### Batteries, runtime, and cost

Better batteries are common to every category projection, but the operating model matters. Industrial robots may gain availability through battery exchange rather than unusually long uninterrupted runtime; service and research platforms place additional value on safe operation near people; rugged systems require protected power delivery and thermal management. Walker S2’s swapping architecture illustrates this distinction.

The supplied scenarios differ substantially in future battery energy density, reaching **550 Wh/kg for compact research** and **700 Wh/kg for industrial and heavy-duty systems by 2040**. These figures are category-model assumptions with potentially different system boundaries, not directly comparable validated pack specifications. Solid-state adoption dates are also inconsistent across the reports.

The following synthesis separates the recurring direction from more speculative milestones.

| Horizon | Recurring scenario direction | Principal uncertainty |
| :--- | :--- | :--- |
| 2025 | Early commercialization; alloy frames; integrated electric joints | Actual shipments and sustained utilization |
| 2030 | More Mg/CFRP; improved batteries; lower production cost | Manufacturing scale and substitution economics |
| 2035 | Greater integration; longer runtime; broader service use | Safety, autonomy, battery maturity |
| 2040 | Lower-cost platforms; modularity; recyclable materials | Advanced composites and structural batteries |

These trajectories are useful for sensitivity analysis, but not as procurement commitments. The strongest cross-category expectation is improvement in mass efficiency, runtime, serviceability, and cost; exact chemistry, material percentage, and adoption year remain less well supported.

## 5. Market Outlook Through 2040

### Measurement and forecast interpretation

The market tables below use **annual unit shipments**, not installed base or revenue. The supplied outlook attributes a **6.5 million-unit 2035** anchor to a Goldman Sachs forecast update, while invoking Morgan Stanley’s **one-billion installed-base vision for 2050** as longer-term context. These measures cannot be substituted for one another.

The supplied research also lists Roots Analysis, MarketsandMarkets, and a China industry source, but does not provide comparable numerical extracts that independently validate the complete shipment path or category allocations. Consequently, the following tables reproduce the **supplied central scenario**; they should not be described as a consensus among those sources.

Source publication dates are not supplied consistently enough to support a current, “as-of” verified shipment statement. In particular, the 2025 values below remain modeled estimates rather than confirmed historical sales.

### Global annual shipments and category shares

The supplied scenario projects the following annual shipments.

| Category | 2025 | 2030 | 2035 | 2040 |
| :--- | ---: | ---: | ---: | ---: |
| Compact Research & Developer | 10,000 | 135,000 | 520,000 | 1,250,000 |
| Full-Scale General-Purpose / AI Research | 8,000 | 225,000 | 1,820,000 | 6,250,000 |
| Industrial Logistics & Warehousing | 14,000 | 360,000 | 2,275,000 | 7,500,000 |
| Service / Healthcare / Interaction | 4,000 | 90,000 | 1,300,000 | 7,500,000 |
| Heavy-Duty / High-Performance / Hazardous-Environment | 2,000 | 45,000 | 325,000 | 1,250,000 |
| Defense / Public Safety | 2,000 | 45,000 | 260,000 | 1,250,000 |
| **Total** | **40,000** | **900,000** | **6,500,000** | **25,000,000** |

The scenario implies substantial absolute growth in every category, but a declining relative role for compact research platforms. Its central structural assumption is that industrial deployment scales before broad service adoption.

Category shares below are calculated directly from those shipment estimates.

| Category | 2025 (%) | 2030 (%) | 2035 (%) | 2040 (%) |
| :--- | ---: | ---: | ---: | ---: |
| Compact Research & Developer | 25 | 15 | 8 | 5 |
| Full-Scale General-Purpose / AI Research | 20 | 25 | 28 | 25 |
| Industrial Logistics & Warehousing | 35 | 40 | 35 | 30 |
| Service / Healthcare / Interaction | 10 | 10 | 20 | 30 |
| Heavy-Duty / High-Performance / Hazardous-Environment | 5 | 5 | 5 | 5 |
| Defense / Public Safety | 5 | 5 | 4 | 5 |
| **Total** | **100** | **100** | **100** | **100** |

Industrial logistics peaks at a modeled 40% share in 2030, while service reaches parity with industrial logistics at 30% in 2040. These are unit shares; the supplied data do not establish corresponding revenue shares.

Defense/public safety remains explicit throughout: **2,000 estimated units in 2025**, **45,000 in 2030**, **260,000 in 2035**, and **1.25 million in 2040**. Its allocation is particularly uncertain because the public examples do not demonstrate a shipment trajectory at that scale. It should be retained as a separate scenario segment, not inferred from heavy-duty civilian shipments.

### Regional allocation

The supplied scenario assigns the following regional shares.

| Region | 2025 (%) | 2030 (%) | 2035 (%) | 2040 (%) |
| :--- | ---: | ---: | ---: | ---: |
| China | 40 | 40 | 39 | 38 |
| United States | 25 | 26 | 27 | 28 |
| Korea | 7 | 8 | 8 | 8 |
| Rest of world | 28 | 26 | 26 | 26 |
| **Total** | **100** | **100** | **100** | **100** |

Applied mechanically to the modeled 2040 total, these shares imply **9.5 million units for China, 7 million for the United States, 2 million for Korea, and 6.5 million for the rest of the world**. These are calculated scenario allocations, not independently sourced regional forecasts.

The underlying outlook combines manufacturing, deployment, supply-chain, and AI-development arguments without defining whether “regional share” means production origin, vendor headquarters, or customer destination. That ambiguity must be resolved before using the split for trade, factory-capacity, or deployment planning. No category-by-region matrix is supplied, so regional defense/public-safety shares cannot be estimated defensibly.

## 6. Conclusions and Sources

The six-category taxonomy is most useful when treated as a mission-based engineering framework with explicit secondary attributes. It preserves the distinction between compact experimentation and human-scale work, separates industrial availability from interaction-oriented assistance, and distinguishes physical ruggedness from defense/public-safety mission assurance. Non-humanoid bridging platforms remain indispensable comparators, but should not be added automatically to humanoid shipment totals.

For planning through 2040, the supplied evidence supports a directional expectation of lighter structures, more selective use of magnesium and composites, improved electric actuation, better battery systems, and lower cost. The market scenario provides a coherent allocation exercise, but neither its rapid shipment growth nor its exact regional and category shares should be presented as established outcomes. Reconciled BOMs, a consistent shipment definition, and dated regional evidence are prerequisites for precise material-demand or investment calculations.

### Sources and evidence scope

Manufacturer product information anchors platform identity and selected specifications, including the compact research, full-scale, industrial, service, and high-performance examples. Teardowns and secondary technical databases provide additional configuration and architectural detail, with weaker support for exact material inventories.

Public defense examples and standards explain the rationale for a separate mission-assurance category, but do not verify universal compliance or deployment maturity. The defense BOM remains notional.

Market publications supply forecast context; the complete annual shipment path, category allocations, and regional split are the supplied analytical scenario. They are kept distinct here from source-reported platform specifications and from the arithmetic checks performed on the supplied estimates.

---

## Sources

1. https://www.unitree.com/g1/ — <https://www.unitree.com/g1/>
2. <https://www.unitree.com/H2/>
3. ubtrobot.com/en/humanoid/products/walker-s2 — <https://www.ubtrobot.com/en/humanoid/products/walker-s2>
4. AgiBot Official Product Page - A2 — <https://www.agibot.com/products/A2>
5. <https://bostondynamics.com/products/atlas/>
6. <https://apptronik.com/apollo/apollo-2>
7. <https://humanoid.guide/welcome-apollo-2/>
8. Fourier GR-3 Care-bot Technical Overview — <https://www.robotsasia.com/Fourier-GR-3-Care-Bot-Humanoid-Robot.htm>
9. Dobot Atom Product Specifications — <https://www.dobot-robots.com/products/humanoid-robots/atom.html>
10. Leju KUAVO-MY (4PRO) Details — <https://www.originofbots.com/robot/kuavo-my-by-leju-robotics-details-specifications-rating>
11. Leju KUAVO 5-W and Service Variants — <https://humanoid.guide/product/kuavo-5/>
12. https://robostore.com/blogs/news/unitree-g1-edu-ultimate-technical-specifications — <https://robostore.com/blogs/news/unitree-g1-edu-ultimate-technical-specifications>
13. https://www.agibot.com/products/X1 — <https://www.agibot.com/products/X1>
14. https://humanoid.guide/humanoid-robots-database/ — <https://humanoid.guide/humanoid-robots-database/>
15. https://chinabizinsider.com/unitree-g1-teardown-decoding-the-economics-and-engineering-of-the-worlds-best-selling-humanoid-robot/ — <https://chinabizinsider.com/unitree-g1-teardown-decoding-the-economics-and-engineering-of-the-worlds-best-selling-humanoid-robot/>
16. <https://humanoid.guide/product/h2/>
17. <https://www.robotsinternational.com/Unitree-H2-Humanoid-Robots.htm>
18. <https://optimusk.blog/blog/tesla-optimus-gen-2/>
19. <https://blog.robozaps.com/b/figure-03-review>
20. <https://anintent.com/blog/nvidia-isaac-groot-humanoid-robot-unitree-h2-plus/>
21. remio.ai/post/agility-digit-5-humanoid-robot — <https://www.remio.ai/post/agility-digit-5-humanoid-robot>
22. humanoid.guide/product/figure-03/ — <https://humanoid.guide/product/figure-03/>
23. AgiBot A2 Database Entry — <https://www.humanoid.press/database/database-agibot-a2/>
24. Fourier GR-3 Emotional Intelligence Release — <https://interestingengineering.com/innovation/fourier-gr3-carebot-robot-emotion>
25. <https://en.engineai.com.cn/product-t800>
26. <https://humanoid.guide/product/atlas/>
27. <https://humanoid.guide/product/t800/>
28. <https://theresarobotforthat.com/blog/humanoid-robot-safety-standards-2026/>
29. China's Humanoid Robot Mirrors Humans — <https://interestingengineering.com/ai-robotics/chinas-humanoid-robot-mirrors-humans>
30. EngineAI T800 Humanoid Details — <https://www.humanoid-robots.io/robot/t800-by-engineai>
31. U.S. Army xTechHumanoid Winners — <https://www.army.mil/article/295812/robotics_competition_winners_advance_military_exploration_of_humanoid_capabilities>
32. Foundation Phantom MK1 Specs — <https://www.originofbots.com/robot/phantom-mk1-by-foundation-details-specifications-rating>
33. Norinco Fuxi Battlefield Robot — <https://defensemirror.com/news/41857/China___s_NORINCO_Unveils____Fuxi____Humanoid_Battlefield_Robot>
34. MIL-STD-810H Ruggedization — <https://systelusa.com/blog/what-is-mil-std-810h/>
35. FIPS 140-3 Cybersecurity Standard — <https://securew2.com/blog/fips-140-3>
36. Ballistic Protection Materials Comparison — <https://www.tradelogic360.com/news/Intelligence_Dimension/Ballistics_RF_Electromagnetics/Ballistic_Protection_Materials_Compared_Weight_Threat_Level_and_Cost.html>
37. <https://partinchem.com/blog/whats-the-secret-to-lighter-more-durable-robots/>
38. Humanoid Robot Electronics Design Guide 2026 — <https://www.winwinchip.com/blog/detail/humanoid-robot-electronics-components-design-guide-2026/80.html>
39. Advanced Materials in Humanoid Robotics Report — <https://www.peekchina.com/blog/plastics-for-humanoid-robots.html>
40. <https://www.patsnap.com/resources/blog/articles/cut-humanoid-robot-joint-actuator-weight-by-40-50/>
41. <https://finance.yahoo.com/technology/ai/articles/goldman-sachs-just-supercharged-humanoid-135551371.html>
42. <https://www.morganstanley.com/insights/articles/humanoid-robot-market-5-trillion-by-2050>
43. <https://www.rootsanalysis.com/humanoid-robot-market>
44. <https://www.marketsandmarkets.com/Market-Reports/humanoid-robot-market-99567653.html>
45. <https://www.wicinternet.org/pdf/ApplicationsandDevelopmentProspectsofHumanoidRobots.pdf>
