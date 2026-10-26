# Service, Healthcare and Interaction Humanoids: Components, Materials and Outlook to 2040
*Matthias Roesslein — October 23, 2026*

Service, healthcare and interaction humanoids are best distinguished by their intended human-facing role, not by body size alone. AgiBot A2 provides a useful 69 kg reference platform for reception and commercial interaction, while Fourier GR-3, Dobot Atom and Leju KUAVO variants illustrate the category’s care, precision-service and research/service boundaries. The component and material models below both reconcile to 69 kg at their modal values, but they are engineering estimates rather than a verified teardown. The outlook through 2040 should likewise be read as a conditional development scenario, not a forecast of established market outcomes.

## 1. Definition and Scope

The **Service / Healthcare / Interaction** category covers humanoids whose principal purpose is to interact with people in commercial, public, care or domestic environments. Its defining priorities are accessible communication, socially legible behavior and lightweight assistance, rather than industrial throughput. Reception, exhibition guidance, visitor assistance and non-medical care support are the principal applications represented in the supplied evidence.

“Healthcare” here denotes a care-oriented application context. It does not establish medical-device status, clinical effectiveness or authorization to perform medical procedures; none of those claims is supported by the supplied data.

The category combines an application definition with engineering preferences. Expressive displays, multimodal perception, tactile sensing, compliant actuation and soft exterior surfaces can support human interaction, but the available evidence does not demonstrate that every representative robot implements every feature. Fourier GR-3’s soft-touch exterior and tactile sensing provide a particularly explicit care-oriented example, while A2’s interaction screen supports its reception and commercial-service positioning.

### Evidence terminology

The report distinguishes three numerical evidence classes:

- **Direct:** A specification reported in the supplied product evidence. A directly reported specification is not necessarily independently measured.
- **Derived:** A value calculated from stated inputs, including arithmetic totals, percentages and per-unit values.
- **Estimate:** An engineering allocation or future scenario not established by a measured component inventory.

Where the supplied BOM labels an actuator mass **Direct**, that original label is retained with a qualification. The citation supplied for its purported actuator datasheet instead identifies an AgiBot X1 product page, so component-level verification remains unresolved.

## 2. Criteria and Boundary Justification

### Category criteria

The following criteria formalize the supplied category definition. Numerical thresholds are proposed classification rules, not demonstrated specifications for every candidate.

| Criterion | Proposed requirement | Evidence limitation |
| :--- | :--- | :--- |
| Primary application | Human-facing service or care | Strongest inclusion criterion |
| Interaction interface | Visual and audio communication | Implementation varies |
| Lightweight manipulation | Typically 1–5 kg per arm | Estimate; not a verified fleet range |
| Continuous payload | Below 10 kg | Proposed screen; basis unspecified |
| Contact behavior | Backdrivable or compliant actuation | Not verified for every candidate |
| Exterior design | Expressive or contact-conscious surfaces | Supporting, not universal |

These criteria prioritize use-case intent. The payload and actuation requirements should not be treated as passed merely because a robot is marketed for service: the supplied comparison lacks sufficient platform-specific data to validate them.

### Boundary versus full-scale general-purpose humanoids

Full-scale dimensions do not determine category membership. A2 is reported at 175 cm and 69 kg, yet its reception, exhibition and commercial-service roles justify its use as the service-category anchor. Its distinguishing feature is therefore the interaction-oriented deployment, not a fundamentally separate body scale.

The boundary remains permeable. A general-purpose or research platform may qualify in a particular service configuration, but that does not make every configuration a service robot. Leju KUAVO is the clearest boundary case because the supplied evidence combines research, modularity, teleoperation and visitor-guidance applications.

### Boundary versus industrial humanoids

The supplied framework distinguishes service humanoids from industrial humanoids by the balance between user interaction and production-oriented manipulation. Speech, expressive interfaces and contact-conscious surfaces support service classification; structural rigidity and repetitive material handling alone do not.

Precision also does not determine the category. Dobot Atom’s reported ±0.05 mm precision is associated in the supplied research with delicate commercial tasks, including coffee preparation and pharmacy-related handling. That positioning supports inclusion here without establishing medical authorization or excluding possible industrial applications.

### Candidate-screen accounting

The supplied comparison contains **five candidate entries**, counting KUAVO-MY/4PRO and KUAVO 5-W separately. Under an application-led reading, **three qualify**, **two are borderline**, and **none is excluded**. Under a strict reading requiring demonstrated compliance with every payload, interface and actuation criterion, **none is fully confirmed**, **all five remain borderline**, and **none is demonstrably excluded**.

| Candidate | Application-led result | Strict technical result | Main reason |
| :--- | :--- | :--- | :--- |
| AgiBot A2 | Qualifying | Borderline | Service role; incomplete threshold evidence |
| Fourier GR-3 | Qualifying | Borderline | Care role; incomplete threshold evidence |
| Dobot Atom | Qualifying | Borderline | Commercial tasks; incomplete threshold evidence |
| KUAVO-MY / 4PRO | Borderline | Borderline | Research/service crossover |
| KUAVO 5-W | Borderline | Borderline | Variant-specific details incomplete |

This accounting avoids treating missing information as either proof of compliance or grounds for exclusion. The application-led reading is better supported because the supplied sources describe intended roles more clearly than they establish common technical thresholds.

## 3. Representative Robots

The comparison below separates reported specifications from unresolved variant attribution.

| Robot | Height (cm) | Mass (kg) | Reported distinguishing feature | Category role |
| :--- | ---: | ---: | :--- | :--- |
| AgiBot A2 | 175 | 69 | 40+ DoF; interaction screen | Reception and commercial service |
| Fourier GR-3 | 165 | 71 | Soft-touch shell; 31 tactile sensors | Care and social interaction |
| Dobot Atom | 153 | 62 | ±0.05 mm precision | Delicate commercial tasks |
| Leju KUAVO family | 173 | 63.5 | Modular platform; KaihongOS | Research and visitor guidance |

A2 specifications and positioning are reported by the product and database entries; GR-3’s care features by its technical and emotional-interaction descriptions; and Atom’s precision by its specifications. The KUAVO dimensions are supplied at family level and should not be assigned automatically to both named variants.

A2 is the most suitable BOM anchor within this evidence set because the supplied model provides a complete system-mass allocation for it. GR-3 is the clearest care-oriented comparator, while Atom demonstrates that precise manipulation can support a service classification. KUAVO demonstrates why variant-level application evidence matters: research capability, teleoperation and visitor guidance do not establish identical configurations or material inventories.

## 4. AgiBot A2 Component BOM

### Basis and interpretation

The BOM represents the supplied **A2 Standard/Interactive model**, normalized to the reported 69 kg system mass. It is a complete top-level mass allocation, not a fastener-level parts list. Assemblies such as the battery, controller, sensor suite and exterior shell include multiple constituent parts.

**Min / Mode / Max** values describe engineering ranges around the supplied modal allocation. They are not statistical confidence intervals, measured manufacturing tolerances or independently verified product variants. Per-unit endpoints are **Derived** from assembly totals and quantities; repeating decimals are rounded.

### Complete top-level component allocation

All weights are in kilograms. Each weight cell gives **Min / Mode / Max**.

| Component or assembly | Qty | Per-unit mass | Total mass | Evidence class | Supplied confidence |
| :--- | ---: | ---: | ---: | :--- | :--- |
| PowerFlow R86-3: hips, knees, ankle pitch | 10 | 1.250 / 1.280 / 1.320 | 12.50 / 12.80 / 13.20 | Direct, provisional | High |
| PowerFlow R86-2: shoulders, waist, ankle roll | 10 | 0.790 / 0.810 / 0.850 | 7.90 / 8.10 / 8.50 | Direct, provisional | High |
| PowerFlow R52: arms, neck, wrists | 10 | 0.430 / 0.450 / 0.480 | 4.30 / 4.50 / 4.80 | Direct, provisional | High |
| Integrated active/passive hands | 2 | 1.000 / 1.200 / 1.400 | 2.00 / 2.40 / 2.80 | Estimate | Medium |
| Swappable 700 Wh battery pack | 1 | 13.00 / 14.50 / 16.00 | 13.00 / 14.50 / 16.00 | Derived, supplied | Medium |
| 200 TOPS controller and I/O | 1 | 1.80 / 2.20 / 2.50 | 1.80 / 2.20 / 2.50 | Estimate | Medium |
| Machined frame and skeleton | 1 | 14.00 / 16.00 / 18.00 | 14.00 / 16.00 / 18.00 | Estimate | Medium |
| Shell, coating and interaction screen | 1 | 3.50 / 4.50 / 5.50 | 3.50 / 4.50 / 5.50 | Estimate | Medium |
| LiDAR, depth cameras and microphones | 1 | 1.20 / 1.50 / 2.00 | 1.20 / 1.50 / 2.00 | Estimate | High |
| Power and data harness | 1 | 2.00 / 2.50 / 3.50 | 2.00 / 2.50 / 3.50 | Derived, supplied | Medium |
| **Allocated system total** | — | — | **62.20 / 69.00 / 76.80** | Derived sum | — |

The modal allocation matches the directly reported 69 kg system mass. The lower and upper totals are arithmetic sums of component endpoints, not evidence that A2 is sold in those mass configurations.

### Reconciliation and limitations

The actuator groups sum to **25.40 kg**, or **36.8%** of modal system mass; the battery and frame contribute **14.50 kg** and **16.00 kg**, respectively. These are **Derived** results from the supplied BOM. Consequently, actuation, energy storage and structure dominate this model, although their exact allocations remain incompletely verified.

Several issues prevent treating the table as a confirmed manufacturer BOM:

- **Joint-count reconciliation:** The model contains 30 grouped actuators, while A2 is described as having 40+ DoF. The separately listed hands have a supplied 19-DoF active/passive description, but the data do not resolve how those freedoms map to actuator count.
- **Actuator provenance:** The purported PowerFlow datasheet reference resolves to an X1 product-page citation. It does not securely substantiate the listed A2 actuator masses.
- **Derived inputs:** The battery and harness masses are labeled Derived in the supplied model, but their original derivations are absent.
- **Confidence labels:** “High” and “Medium” reproduce the supplied assessment; they are not independently calculated confidence measures.

The battery allocation also requires caution. Dividing the supplied 700 Wh capacity by the estimated 14.50 kg pack mass gives approximately **48 Wh/kg**, a **Derived pack-level value**. This is not consistent on its face with the outlook’s roughly 250 Wh/kg energy-density assumption unless the latter uses a different basis, which the supplied data do not specify.

## 5. Material Composition

### Estimated inventory by material grade

The following table preserves the supplied grade groupings. Every allocation is an **Estimate**, not a verified manufacturer material declaration. Where several grades share a row, their individual masses cannot be separated from the available evidence.

| Material group and grade | Min (kg) | Mode (kg) | Max (kg) | Modal share (%) |
| :--- | ---: | ---: | ---: | ---: |
| Aluminum: 7075-T6 / 6061-T6 | 25.0 | 28.5 | 32.0 | 41.3 |
| Ferrous metals: GCr15 / 42CrMo | 7.0 | 9.0 | 11.0 | 13.0 |
| Battery constituents: NMC / graphite / electrolyte | 8.0 | 9.5 | 11.0 | 13.8 |
| Polymers: PC/ABS / TPU / PA66-GF | 6.0 | 7.5 | 9.5 | 10.9 |
| Magnesium: AZ91D / AM60 | 5.0 | 6.2 | 8.0 | 9.0 |
| Conductors: copper / silver solder | 4.0 | 4.8 | 5.5 | 7.0 |
| Magnets: NdFeB with Dy/Tb | 2.0 | 2.5 | 3.0 | 3.6 |
| Glass/silicon: face glass / IC material | 0.8 | 1.0 | 1.5 | 1.4 |
| **Total** | **57.8** | **69.0** | **81.5** | **100.0** |

The modal inventory closes at 69 kg, with aluminum the largest estimated material group. Percentage shares are **Derived** from the modal masses; their individually rounded values need not sum exactly to the displayed total.

### Relationship to the component BOM

Component and material tables describe the same system from different perspectives and must not be added together. Aluminum can occur in both the skeleton and actuator housings, while polymers can occur in shells, flexible joints and internal parts. The supplied material model assigns ferrous metals to gears, bearings and fasteners, and copper principally to windings and power distribution.

The **9.50 kg** battery-constituent estimate is not the mass of the complete **14.50 kg** battery assembly. Their **5.00 kg** difference is a **Derived** residual, but the data do not provide a material-by-component matrix identifying its composition. Similarly, the magnesium allocation is not tied to a separately identified magnesium assembly in the BOM.

The material endpoint totals differ from the component endpoint totals because the two sets of ranges were supplied independently. Only the modal inventories are reconciled. Neither set supports a probabilistic uncertainty claim, and exact commercial grades—including the named face-glass type—remain unverified.

## 6. Development Outlook: 2025–2040

### Quantitative scenario

All values below are **Estimates** from the supplied trajectory. The cost figures are scenario assumptions, not dated quotations or observed market prices.

| Metric | 2025 | 2030 | 2035 | 2040 |
| :--- | ---: | ---: | ---: | ---: |
| Modal mass (kg) | 69 | 55 | 48 | 42 |
| Assumed cost (USD) | 50,000 | 25,000 | 12,000 | 8,000 |
| Runtime (hours) | 2.0 | 4.0 | 6.0 | 8.0 |
| Compute capacity (TOPS) | 200 | 1,000 | 5,000 | 20,000 |

The trajectory combines lower mass and cost with longer runtime and greater compute capacity. It is a scenario for category development, not a validated product roadmap.

### 2025: Pilot-commercialization baseline

The supplied baseline emphasizes aluminum–magnesium structures and movement from research demonstrations toward reception and exhibition roles. A2’s reported commercial-service positioning supports the application choice, but the broader claims about deployment geography and adoption scale are not independently established in the supplied evidence.

The roughly **250 Wh/kg** energy-density assumption is an **Estimate** with an unspecified cell-versus-pack basis. It should therefore remain separate from the BOM’s derived pack-level figure.

### 2030: Lighter structures and richer interaction

The scenario proposes carbon-fiber-reinforced polymer limbs and a **15–20% estimated mass reduction**, alongside more nuanced social navigation and “empathetic AI.” Its modal mass decreases from 69 kg to 55 kg, equivalent to a **Derived reduction of approximately 20.3%**.

That arithmetic is close to the stated reduction range, but it does not prove that material substitution alone delivers the change. No component redesign, composite-grade allocation or validation data are supplied.

### 2035: Non-medical care integration

The scenario associates solid-state batteries with safety improvements and **4–6 hours** of runtime, while the quantitative table selects **6 hours**. It also anticipates greater use in elderly-care facilities for non-medical assistance.

The supplied statement of “2× runtime” is ambiguous. Six hours is **three times** the 2025 table value, while four hours is twice that baseline. The tabulated trajectory is the clearer numerical statement; the multiplication claim requires a specified comparator.

### 2040: Domestic-service scenario

The final stage proposes bio-based, recyclable polymers and a transition toward household-appliance roles. Its estimates are **42 kg**, **8 hours** of runtime and **USD 8,000** cost, but no adoption evidence or cost model establishes domestic ubiquity.

The narrative’s **90% cost-reduction** claim conflicts with the numerical trajectory. A decline from USD 50,000 to USD 8,000 is a **Derived 84% reduction**; a 90% reduction would imply USD 5,000. The explicit cost table is better supported internally because its endpoints are stated, although neither outcome is independently forecast.

## 7. Appendix: Calculation and Interpretation Notes

| Check | Calculation basis | Derived result |
| :--- | :--- | ---: |
| Component modal closure | Sum of BOM modes | 69.00 kg |
| Component endpoint envelope | Sum of minima / maxima | 62.20–76.80 kg |
| Material modal closure | Sum of material modes | 69.00 kg |
| Material endpoint envelope | Sum of minima / maxima | 57.80–81.50 kg |
| Actuator mass share | 25.40 / 69.00 | 36.8% |
| Pack-specific energy | 700 Wh / 14.50 kg | Approximately 48 Wh/kg |
| Scenario mass reduction | 69 kg to 42 kg | 39.1% |
| Scenario cost reduction | USD 50,000 to USD 8,000 | 84% |

These checks establish arithmetic consistency, not physical verification. The principal unresolved needs are a manufacturer-level component inventory, an actuator-to-joint mapping, a component-to-material crosswalk and dated evidence for cost and deployment claims.

## 8. Sources

### Product and application evidence

- **AgiBot Official Product Page — A2:** Product identity and service positioning.
- **AgiBot A2 Database Entry:** Reported platform specifications and comparison context.
- **Fourier GR-3 Care-bot Technical Overview:** Care-oriented specifications and contact interfaces.
- **Fourier GR-3 Emotional Intelligence Release:** Emotional-interaction positioning.
- **Dobot Atom Product Specifications:** Dimensions, precision and commercial-task context.
- **Leju KUAVO-MY (4PRO) Details:** Research/service configuration context.
- **Leju KUAVO 5-W and Service Variants:** Variant and service-application context.

### Contextual evidence and provenance limits

- **AgiBot X1 Product Page:** Supplied under the actuator-datasheet attribution; insufficient to verify the A2 actuator masses.
- **Humanoid Robot Electronics Design Guide 2026:** Listed as contextual evidence; no extracted passage verifies the specific BOM allocations.
- **Advanced Materials in Humanoid Robotics Report:** Listed as materials context; no extracted passage establishes the A2 grade-level inventory.

The detailed mass allocations and future trajectory originate in the supplied engineering model. Their estimate status is retained throughout rather than presented as manufacturer-confirmed data.

---

## Sources

1. AgiBot Official Product Page - A2 — <https://www.agibot.com/products/A2>
2. Fourier GR-3 Care-bot Technical Overview — <https://www.robotsasia.com/Fourier-GR-3-Care-Bot-Humanoid-Robot.htm>
3. Dobot Atom Product Specifications — <https://www.dobot-robots.com/products/humanoid-robots/atom.html>
4. AgiBot A2 Database Entry — <https://www.humanoid.press/database/database-agibot-a2/>
5. Leju KUAVO-MY (4PRO) Details — <https://www.originofbots.com/robot/kuavo-my-by-leju-robotics-details-specifications-rating>
6. Leju KUAVO 5-W and Service Variants — <https://humanoid.guide/product/kuavo-5/>
7. Fourier GR-3 Emotional Intelligence Release — <https://interestingengineering.com/innovation/fourier-gr3-carebot-robot-emotion>
8. https://www.agibot.com/products/X1 — <https://www.agibot.com/products/X1>
9. Humanoid Robot Electronics Design Guide 2026 — <https://www.winwinchip.com/blog/detail/humanoid-robot-electronics-components-design-guide-2026/80.html>
10. Advanced Materials in Humanoid Robotics Report — <https://www.peekchina.com/blog/plastics-for-humanoid-robots.html>
