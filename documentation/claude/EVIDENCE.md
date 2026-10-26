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

**No recipe is proposed yet.**

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
| Aluminium | VehicleComposition, 6061 and 7075 | Teal Sheets, Dec 2025 | **Confirmed**, exactly |
| Magnesium | VehicleComposition, AZ91C / AM60A | ICAST datasheets (ASTM B94) | Al and Mn agree; the **grades differ** (the robots use AZ91D / AM60B) |
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
