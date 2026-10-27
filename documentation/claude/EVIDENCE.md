# Evidence

The check of the project's inputs against sources outside it, with references. Written by Claude, newest first.
How each source is judged follows Matthias's rules for sources (`GitHub/CLAUDE.md`, §8):
- **same kind:** it describes the same kind of material as the robot uses;
- **representative:** it fits the use in a robot;
- **questioned:** a standard, a manufacturer's datasheet, a measurement, a review, a patent or a vendor page;
  first-hand or second-hand;
- **read myself:** the source was opened and read, not judged from a search summary.

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

**Status: agreed by Matthias, 2026-10-27, choosing the answer offered: "I agree with the aluminium recipe as proposed in E1.1c, including its choices." Entered the same day, after E1.1d, on his word "Keep E1.1c as agreed and enter it now, as with the plastics and fibre composites.", in `data/researched/element_recipes.xlsx` (VERIFICATION.md V39). **Under review:** Matthias's rule of the same day ("You should trust standards more than analysis performed at a university") puts the modes of 6061 and ADC12, which rest on university or institute analyses only, and the university analyses among those of 7075 and A380, in question; whether they are set again is his decision.**

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

**Status: agreed. Matthias, 2026-10-27, choosing the answer offered: "I agree with the modes of E1.1e and E1.2d, including their choices." Not entered yet: the workbook still holds the modes of E1.1c.**

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

**Status: proposed; on hold.** Matthias, 2026-10-27: "You should trust standards more than analysis performed at a university. They do NOT know quality measures for analytical procedures. This is different with comercial labs". The modes below rest on university analyses (the AM50 certificate of Jesus et al. excepted) and are to be set again by his rule; nothing is entered.

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

**Status: agreed. Matthias, 2026-10-27, choosing the answer offered: "I agree with the modes of E1.1e and E1.2d, including their choices." It replaces the modes of E1.2c. Not entered yet. The rest of E1.2c (the AM share, AM60B or AM50A half and half, robot type 3 as AZ91D alone) was not put to him on its own.**

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
