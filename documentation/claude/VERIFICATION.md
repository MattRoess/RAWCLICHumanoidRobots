# Verification and validation

Every check made on this project: what, how, against what, the result, the date, and what it does not cover. Written
by Claude, newest first.

## 2026-10-26

### V34. 01's overview with the four stages

- **What:** the overview page of 01 after 02 and 03 were added to its list of stages.
- **How:** 01 was run with its output folder moved to the session's scratch folder (not `figures/`), and the overview
  opened and read.
- **Result:** the first drawing showed three faults, all corrected: the text of the 01 and 02 boxes ran out of its box
  (the boxes now take the height of the longest text); "nothing is drawn at random yet" (now: 02 draws each mass from a
  triangle); and an open point "The stages that compute the materials of each category: not built yet" (removed).
  Redrawn and read again: every text inside its box. 01 finds no fault.
- **Not covered:** the other pages of 01 were drawn, not read again; only the overview's code changed.

### V33. 03_comparison.py: tests, deliberate faults, and a run on the real inputs

- **What:** 03, as specified in point 15 and recommendation g (HANDOVER.md).
- **How:**
  - **Tests first** (`tests/test_comparison.py`, 5 tests), written before 03 and seen to fail. They run 02 on the
    small workbook (2,000 draws) and require that 03:
    - reads 02's arrays exactly as written;
    - gives a mean, 2.5 % and 97.5 % that agree with 02's summary within 1e-5 of the value (02 computes them in
      float64 before writing float32);
    - draws the four pages;
    - stops without 02's draws;
    - stops on draws that do not belong together: a table one draw short, materials that no longer add up to the
      total, and columns in another order than the first robot type's.
  - **Deliberate faults:** five, each in a scratch copy of 03 (`mutants_03.py` in the session's scratch folder). All
    five were caught: the median shown as the mean; the order of the columns not checked; every robot type read
    from the first folder; the sums not checked; the number of draws not checked.
  - **The real inputs:** 03 run on the draws of V32, its pages into the scratch folder, and all four opened and read.
- **Result:** all tests pass. The first drawing had three faults, all corrected and redrawn:
  - Mixed and Not allocated were blue instead of grey, because the rows are robot types;
  - the kg marks of narrow charts touched (now four at most);
  - the key began in lower case.
  The notes now give the shared list's own definition of Whole body, and say that the part group Battery is the packs,
  while Battery materials is the cells.
- **Not covered:** 03 has not read draws of 200,000.

### V32. 02 on the real inputs, 2,000 draws

- **What:** 02 on the real workbook, shared lists and element recipes, before the real run (which is Matthias's).
- **How:** 02 run with 2,000 draws, seed 1, its outputs moved to the session's scratch folder (`sandbox_02.py`;
  nothing written to `data/` or `figures/`). The summaries read, the six pages opened and read, and five results
  checked by hand:
  - **Robot type 1's cells:** a mean of 1.833 kg, against 1.832 kg for its three builds (1.74, 1.807, 1.95 kg) drawn
    equally often; the interval runs from 1.74 to 1.95 kg, the lightest and the heaviest build.
  - **Robot type 1's plastics:** 6.02 kg at the mean, against 5.5 kg for its row's triangle (4.5 / 5.5 / 6.5) plus
    about 0.53 kg from the battery's rest (2.5 − 1.83 kg, at about 80 %).
  - **Robot type 1's electronics:** 0.643 kg, against 0.533 kg for its row plus 16.5 % of that rest (0.11 kg).
  - **Robot type 1's chromium:** 0.028 kg at the mean, with a median of 0: the stainless can, in half of the draws, is
    18.1 % chromium and 16.8 % of 1.83 kg of cells, 0.056 kg, so 0.028 kg on average.
  - **Robot type 2's nickel:** 0.87 kg, against about 0.86 kg by hand (4.33 kg of cells at the mean, about 19.9 %
    nickel).
  - **Robot type 3:** phosphorus 0.60 kg and no cobalt, as LFP cells have.
  - **Time and memory:** 2.5 s, at most 166 MB, 2.6 MB written.
- **Result:** every check of 01 and 02 passes, and every sum of point 12 holds in every draw of all six robot types.
  The pages were corrected twice:
  - each chart got a line saying what it covers: by element, only the materials that have a recipe so far (9.05 of
    35.0 kg in robot type 1);
  - small masses keep their trailing zeros ("0.150", not "0.15").

  **A result for Matthias:** Not allocated is below zero in 50.8 % of the draws of robot type 1 and 67.4 % of robot
  type 2 (robot types 3 to 6: 0.0, 0.2, 0.0, 0.0 %). In the workbook, the materials of robot types 1 and 2 add up to
  their parts at the mode, so drawn independently the difference sits around zero. For robot type 2 the materials'
  triangles lean further to the right than the parts': 73.5 kg of materials against 71.4 kg of parts at the mean.
  Recommendation b allows it and reports it.
- **Not covered:**
  - 200,000 draws were not run (Matthias's). Its size is computed, not measured: 52 columns × 200,000 × 4 bytes, about
    42 MB per robot type and 250 MB in all.
  - Its memory is estimated at around 1 GB: the six robot types are kept in float64 until every draw has been checked.
  - The time is not estimated.

### V31. Deliberate faults in 02

- **What:** whether the tests of 02 catch what they guard.
- **How:** nine faults, each in a scratch copy of 02, with the tests run on it (`mutants_02.py` and the copies in the
  session's scratch folder):
  - the energy not followed;
  - alternatives blended by their probability;
  - always the first build;
  - a kept row with f = 1;
  - a split part counted whole in each region;
  - the rest of a battery row dropped;
  - a split's remainder fixed at 0.8;
  - a recipe drawn for each row on its own (two variants).
- **Result:** all caught. Seven were caught at once. The two recipe variants first passed, and the reason was in the
  faults: 02 keeps a recipe's draws in two stores, its element shares and each item's share, so removing one store
  changed nothing. With both removed, the test caught it: the iron share of two rows that follow the same recipe had a
  standard deviation of 0.030 instead of the triangle's 0.041.
- **Not covered:** faults no one thought of.

### V30. 02_composition.py: tests first

- **What:** 02, as specified in points 1 to 14 and 16 to 17, with the recommendations a to f (HANDOVER.md).
- **How:** `tests/test_composition.py`, 21 tests, written before 02 and seen to fail. They draw the small workbook of
  `tests/test_schemas.py` 2,000 times (seed fixed) into temporary folders. They require:
  - **Seeds:** the same seed gives the same draws, another seed other ones.
  - **Means:** a part, a body region, a material, a split share, a rest share and the drawn energy per kg agree with
    their triangle's mean within four standard errors, and stay within its bounds.
  - **Discrete states:** a build and an alternative are each drawn about half of the time (within four standard
    errors).
  - **One draw per recipe:** a recipe used by two rows is drawn once in each draw (the spread of the triangle itself,
    0.041, within 0.003).
  - **The cells follow their energy:** phosphorus, which sits only in the salt, equals the cells × 10 % × f × its
    share of LiPF6, draw by draw, with f from the drawn build's cell or, for a kept row, from the NMC triangle.
  - **Sums:** every sum of point 12 holds in every draw, and each of its checks, broken in one draw, is caught with
    the right words. Not allocated may fall below zero and the summary gives the share of draws; nothing else does.
  - **Split parts:** a part split by units gives each body region its units' part.
  - **Faults stop it:** a cell recipe that follows the energy of a cell that is not NMC, and a row of the sheet Rows
    whose recipe follows the energy, are faults. A fault in the workbook stops 02 before any file or page is written.
  - **The files:** for each robot type, float32 arrays of 2,000 rows with as many columns as their lists name, adding
    up to the total row by row, the summary in `.csv` and `.xlsx`, and a page.
  - **The numbers on the pages:** three significant figures, trailing zeros kept.
- **Result:** all 21 pass; with the tests of 00, 01 and 03, 129 tests pass, none skipped.
- **Not covered:** the small workbook has two robot types and no kept battery except where a test builds one.

### V29. The kept battery rows name the recipe of their cells

- **What:** robot types 2 and 6 keep their battery rows (E1.7d), and Matthias decided their cells are NMC with the
  car file's recipe (E1.7e). No input said so yet, so 02 could not draw their elements.
- **How:**
  - **Tests first:** two new tests of 01, seen to fail. A kept row without a recipe, or with one that is not in the
    sheet Recipe, is a fault. The real kept rows name 'NMC cylindrical'.
  - **The check:** check 16 in 01.
  - **The data:** 'NMC cylindrical' entered in the two kept rows of `data/researched/shared_lists.xlsx`, with his
    E1.7e words in their column Decided. The file was first copied to the session's scratch folder
    (`shared_lists_before_kept_recipe.xlsx`).
- **Result:** 01's 98 tests pass; 01 finds no fault in the real files.
- **Not covered:** nothing else in the sheet changed.

### V28. The fibre-composite entry

- **What:** the recipe of E1.9c, entered on Matthias's word ("Yes, enter the fibre-composite recipe now, as with the
  plastics: the recipes and the three rows in element_recipes.xlsx, checked by 01 with tests, and the documents.").
- **How:**
  - **Test first.** One new test was written before the data and failed. It reads the real workbook and must find
    the three rows, no fault, and E1.9c's result table at the modes for each epoxy (within 0.06
    percentage points), with sulphur only where the aromatic epoxy is chosen.
  - **The data:** written by a throw-away script; the workbook was first copied to the session's scratch folder
    (`element_recipes_before_composites.xlsx`). 3 compounds, 15 recipe items and 3 rows added. 01 got sulphur's
    atomic mass (IUPAC CIAAW 2024, S 32.06), and check 17's wording names fibre composites.
  - **The pages:** 00 and 01 were run; the checksums of all 20 pages were compared with those before.
- **Result:** all 102 tests pass, none skipped; 01 finds no fault; the robot and shared-lists pages are byte for byte
  unchanged; faults.png changed only in check 17's wording, and was opened and read.
- **Not covered:** no stage draws element masses yet; the epoxy and robot type 3's split are estimates.

### V27. The proposed fibre-composite recipes, drawn in a sandbox

- **What:** the proposal of [EVIDENCE.md](EVIDENCE.md) E1.9c, for robot types 1, 2 and 3.
- **How:** the sandbox of V24, with the recipes of E1.9c and the agreed 'Carbon fibre' and 'E-glass'; 20,000 draws
  per row (seed 1), nothing written to the project. Each group checked for one remainder or alternatives adding to 1,
  shares in order and largest shares at most 1. The modes were computed for each epoxy separately.
- **Result:** both rows add up to 1; no element falls below zero in any draw; the shares are those in E1.9c.
- **Not covered:** the draws are independent; the epoxy, robot type 3's split and the lower bounds of fibre content
  are estimates. Nothing is entered.

### V26. The plastics entry: element_recipes.xlsx, the sheet Rows and 01's checks

- **What:** the plastics recipe of E1.8c with the six values of E1.8d, entered on Matthias's word ("Yes, enter the
  plastics recipe now as laid out: the polymer recipes and the robot rows in element_recipes.xlsx, 01 extended to
  read and check them, with tests, and the documents.").
- **How:**
  - **Tests first.** 9 new tests were written before the code and failed. 6 break one thing each and require exactly
    that fault: two recipes that contain each other, a name both a compound and a recipe, a piece of a covered
    material without a row (the rest of a battery row), a row for a piece that does not exist, a row naming a missing
    recipe, a piece with two rows. 2 check a recipe within a recipe and a complete sheet Rows. 1 reads the real
    workbook and must reproduce E1.8c's result table at the modes, row by row (within 0.06 percentage points, the
    table's rounding).
  - **The data:** written by a throw-away script; the workbook was copied to the session's scratch folder first
    (`element_recipes_before_plastics.xlsx`). 21 compounds, 48 recipe items and 9 rows added; the column 'Cell
    recipe' renamed 'Recipe'.
  - **The pages:** 00 and 01 were run; the checksums of all 20 pages were compared with those before.
- **Result:**
  - All 101 tests pass, none skipped. 01 finds no fault.
  - The 9 rows reproduce E1.8c: for example robot type 3's plastics C 61.1, P 0.5 %; robot type 5's seals Si 19.8 %.
  - The robot and shared-lists pages are byte for byte unchanged, as planned (plastics keep their kilograms);
    faults.png changed only by the new check in its list, and was opened and read.
- **Not covered:** no stage draws element masses yet; the split of each plastics row among its polymers is an
  estimate throughout.

### V25. The nine open points of the plastics recipe, against sources read on the web

- **What:** the nine values of E1.8c that rested on one source, a formula from a name, a picture or an estimate
  ([EVIDENCE.md](EVIDENCE.md), E1.8d).
- **How:** each searched on the web; every source used was opened and read (makers' datasheets and patents as PDF
  text, peer-reviewed articles in the browser, PubChem through its interface). The agreed recipe was redrawn in the
  sandbox of V24 with the values the sources give, 20,000 draws per row, to see what they would change.
- **Result:** four points confirmed as they were (CF-PEEK, BDP, the TPU soft segments, UHMWPE; silica agrees). Six
  values would move: ABS's acrylonitrile and butadiene modes, PC/ABS's and PA66-GF's minimums, the carbon fibre's
  nitrogen, TPU's hard segment. At the modes no element of any row moves by more than 0.5 percentage points.
- **Taken in:** Matthias, "Yes, take the six verified values of E1.8d into the plastics recipe." E1.8c now holds them;
  the redrawn rows still add up to 1 and no element falls below zero in any draw.
- **Not covered:** how each row splits among its polymers cannot be verified on the web.

### V24. The proposed plastics recipes, drawn in a sandbox

- **What:** the proposal of [EVIDENCE.md](EVIDENCE.md) E1.8c, for the nine plastics rows of the six robot types.
- **How:** a throw-away script in the session's scratch folder, using 01's `composition` and atomic masses (plus the
  five further CIAAW masses), 20,000 draws per row (seed 1); nothing written to the project. Each group was checked
  for one remainder or alternatives adding to 1, shares in order, and its largest shares adding up to at most 1.
- **Result:** every row's elements add up to 1; no element falls below zero in any draw; the shares are those in
  E1.8c.
- **Not covered:** the draws are independent; the split of the rows is an estimate throughout. Nothing is entered.

### V23. The battery entry: the sheet Battery cells, element_recipes.xlsx, 01's checks and the robot pages

- **What:** the battery as cells only and the element recipes of the cells, entered on Matthias's word ("Yes, build
  the battery entry as laid out", then "I agree with the cell masses counted from voltage and capacity in E1.7j,
  with robot type 3 from the three LFP cells of E1.7k. Resume the battery entry as laid out.").
- **How:**
  - **Tests first.** 27 new tests were written before the code and failed. 19 build small recipes and small battery
    sheets, break one thing each and require exactly that fault: a composition that does not add up or cannot be
    read, an element without an atomic mass, an unknown compound, two remainders, probabilities adding to 1.1,
    shares out of order or above 1, an item within a missing item; a cell not in the sheet Cells, cells in parallel
    50 % off the capacity, cells in series off the voltage, cells heavier than 85 % of the pack, a build with no
    cells or energy, a rest without a remainder or able to fall below zero, a row both kept and built, a battery
    row with no row, a build not labelled E.
  - **The real files.** Two tests read them. The recipes must give, at the modes, E1.7i's element shares for
    each cell and can (within 0.03 percentage points, because E1.7i used the car file's shares rounded to three
    decimals). Each robot type must get E1.7j and E1.7k's cell masses. Every robot type's materials must still add up
    to the mode of its parts list.
  - **The pages.** 00 and 01 were run; the robot pages of all six robot types and faults.png were opened and read.
- **Result:**
  - All 92 tests pass, none skipped. 01 finds no fault.
  - **The check caught a fault in the agreed recipe:** active material and binder could reach 101 % of a coating.
    Matthias chose to lower the active material's maximum by one point (EVIDENCE.md E1.7i); the modes are unchanged.
  - Cells, kg (lightest / middle / heaviest build): robot type 1 1.74 / 1.807 / 1.95; 3 7.2 / 7.335 / 7.335; 4 2.6 /
    2.755 / 2.919; 5 9.8 / 10.388 / 11.033. Robot types 2 and 6 keep the workbook's rows.
  - The totals stay 35, 70, 72.4, 69, 103.4 and 93.6 kg. Robot type 1's pack rest of 0.693 kg moves to plastics,
    electronics and copper. Not allocated becomes 8.565 kg (robot type 3), 6.745 kg (4) and 15.012 kg (5).
  - The element shares at the modes, % of the cell, nickel-plated / stainless can:
    - NMC: Ni 19.32 / 20.38, Fe 16.45 / 12.39, Cr 0 / 3.04, C 29.68, Li 2.57, Co 1.37.
    - LFP: Fe 29.97 / 25.92, P 7.83, Li 1.75.
- **Not covered:** no stage draws element masses yet; the shared-lists pages still show the workbook's battery rows
  (only the robot pages were asked for); the shares in the workbook files rest on the sources of E1.7, not on new
  checks.

### V22. LFP cells for robot type 3's packs

- **What:** which LFP cells build two 48 V, 9 Ah packs within their 9.6 kg ([EVIDENCE.md](EVIDENCE.md), E1.7k).
- **How:** three further makers' datasheets downloaded and read as text (PDFKit); checked that none is marked
  confidential. For each of the eight LFP cells read, the cells in parallel, the pack capacity and the cell mass were
  computed by script, with the capacity test (±12 %) and the mass test (at most 85 % of the packs).
- **Result:** three cells pass both tests and agree within 0.13 kg: 7.20 to 7.33 kg for both packs, 75 to 76 % of
  their mass.
- **Not covered:** the cells UBTECH uses are not known; the 85 % rests on van de Ven et al.'s few consumer modules.
  Nothing is entered.

### V21. The number of cells from each pack's voltage and capacity

- **What:** the revision of the cell mass Matthias asked for ([EVIDENCE.md](EVIDENCE.md), E1.7j).
- **How:** the pack voltages and capacities were read from the workbook and from AgiBot's own pages (in the
  browser) and a dealer's page; two further LFP datasheets were read as text. The cells in series, in parallel, the
  pack capacity each build reaches and the cell mass were computed by script for every cell type of E1.7c.
- **Result:** robot types 1, 4 and 5 come out within about 0.15 kg of E1.7d. Robot type 3's only fitting builds
  weigh 95 to 100 % of its packs, so the cells read do not represent its pack.
- **Not covered:** robot type 5's voltage and capacity were not found; robot type 4's 13 or 14 cells in series
  rests on a charging voltage. Nothing is entered.

### V20. The proposed element recipes of the cylindrical cells, drawn in a sandbox

- **What:** the proposal of [EVIDENCE.md](EVIDENCE.md) E1.7i, for the NMC and the LFP cell.
- **How:** a throw-away script in the session's scratch folder, run in the project's `.venv` with 200,000 draws
  (seed 1); nothing written to `data/` or `figures/`. The compounds' element shares were computed from their
  formulas and atomic masses. The recipe at the modes was computed separately for each can.
- **Result:**
  - The elements add up to 100.000 % in every draw, for both cells.
  - The first structure let the parts of the NMC cell exceed the whole cell in 3.5 % of the draws. With the rest
    as the cell's remainder, split by shares, no part falls below 0: the smallest "other" is 0.39 % of the cell. The
    LFP electrolyte, its remainder, stays between 4.5 and 17.1 %.
  - The element shares are those in E1.7i.
- **Not covered:** the draws of the parts are independent except through f; the 50 / 50 can is an estimate. Nothing
  is entered and no stage computes this yet.

### V19. The build of a cylindrical cell, from the LG M50 measurements

- **What:** the mass of each part of an LG M50 21700 cell ([EVIDENCE.md](EVIDENCE.md), E1.7h).
- **How:** computed by script from Chen et al. 2020's measured weights (68.38 g with the can, 57 g without),
  loadings, coated areas and foil thicknesses, with handbook densities for aluminium and copper. The rest is the
  difference, not a separate measurement. Compared with van de Ven et al. 2024 and Sandia.
- **Result:** can 16.6 %, against 17 % measured by van de Ven et al. in 18650 cells. Coatings 59.8 %, foils 11.6 %,
  the rest 11.9 %, of which Sandia's electrolyte is 5.6 %.
- **Not covered:** the foil areas assume each foil is as long as its longer coated side; the binder and the
  separator are not separated; one cell type only. No recipe is proposed.

### V18. The proposed cell masses, drawn in a sandbox

- **What:** the proposal of [EVIDENCE.md](EVIDENCE.md) E1.7d: cell mass = energy / energy per kg of the cells, and
  the rest = the workbook's battery row − the cell mass, for robot types 1, 3, 4, 5 and, as a check, 2.
- **How:** 200,000 draws in a throw-away script run in the project's `.venv` (seed 1). The energy per kg and the
  workbook rows were drawn as independent triangles. Nothing was written to `data/` or `figures/`. The robot 1 split
  shares were computed from van de Ven et al.'s weighed module shares.
- **Result:**
  - The bounds and the 95 % intervals are those in E1.7d.
  - The rest never falls below 0 in robot types 1 and 4. It does in 0.2 % of the draws for robot type 3 and in every
    draw for robot type 5, where the cells are heavier than the row. In robot type 2 it would be 32 %, which is why
    robot type 2 is not proposed.
- **Not covered:** the independence of the energy per kg and the workbook row is an assumption. Nothing is entered
  and no stage computes this yet.

### V17. The cells humanoid robots use, and their Wh per kg

- **What:** which cells the six robots use, and the energy per kg of those kinds of cells.
- **How:**
  - Searched the web for robot batteries and cell datasheets.
  - Every source used was opened and read: four PDFs as text through PDFKit, web pages through the fetch tool, the
    EEWorld page in the browser.
  - The Wh/kg was computed from each sheet's capacity, voltage and weight (minimum capacity and maximum weight where
    given), not taken from a summary.
  - The cell masses were checked against each robot's pack energy and mass from the workbook.
  - Everything is in [EVIDENCE.md](EVIDENCE.md), E1.7c.
- **Result:**
  - Cylindrical NMC cells hold 232 to 256 Wh/kg in four sources, and LFP cells 104 to 182 Wh/kg in three.
  - No source names the cells of any of the six robots.
  - Only NMC fits robot type 2's pack. Robot type 4's 700 Wh and 14.5 kg contradict each other. Robot type 5's
    7 kg of active materials agrees with its 2.5 kWh.
- **Not covered:** pouch and solid-state cell datasheets; two of the LFP sources are not manufacturers' sheets. No
  min / mode / max is proposed and nothing is entered.

### V16. The battery composition of the car project

- **What:** `RAWCLICVehicleBattery/data/raw/BATT_consolidated_composition.xlsx`, sheet `BATTinELV_BEV_60kWh`, and
  the robots' battery masses against their energy.
- **How:**
  - The cathodes' element shares were computed by script from the file and compared with the shares from the
    formulas (LiFePO4, NMC111 to NMC955, NCA) and the atomic masses.
  - The cell's component shares were computed without the pack parts and compared with a measured teardown (van de
    Ven et al. 2024).
  - The elements were summed per component to find what has none.
  - Each robot's energy from the workbook was multiplied by the car cells' kg per kWh.
  - Everything is in [EVIDENCE.md](EVIDENCE.md), E1.7b.
- **Result:**
  - The cathodes match their formulas: LFP, NMC111 and NCA 80/15/5 exactly; NMC middle and high nickel lie between
    two standard grades.
  - The cell build agrees with measured pouch cells; the casing (2.5 %) has no steel can, which is 17 % of an 18650
    cell.
  - 14 to 16 % of the cell has no elements: the electrolyte except its Li, the separator and the casing.
  - Robot types 3 and 4 hold 2.3 and 4.2 times the cell mass their energy needs.
- **Not covered:** the other pack sizes of the file (only BEV 60 kWh read); the Si share of the anodes; any source
  on robot cells themselves. No recipe is proposed and nothing is entered.

### V15. The magnet composition sheet of the car projects

- **What:** `RAWCLICVehicleElectronics/Data/Sources/permanent_magnet_elemental_composition.xlsx`, sheet `NdFeB`, 27
  grades in seven temperature classes.
- **How:** the smallest and largest sum of each grade's element ranges were computed by script, and the Dy, Nd and
  Co compared with Arnold Magnetics 2015 and Yang et al. 2017. Details in [EVIDENCE.md](EVIDENCE.md), E1.6b.
- **Result:** Dy by class agrees with Arnold. From N48SH up no composition within the ranges adds up to 100 %,
  because Nd is not reduced where Dy is added, and Co reaches 13 % against the literature's 5 %. A derived sibling
  file holds negative maxima (reported, not changed).
- **Not covered:** the sheet has no source, so its origin is unknown.

### V14. The element recipes: the siblings' data against independent web research

- **What:** the element data the sibling projects already hold for the 11 shared materials that can have a recipe,
  and the web sources for what they lack.
- **How:**
  - The siblings' workbooks were read first.
  - Each material was then searched on the web, and every source used was opened and read: PDFs in full, web pages
    through the fetch tool.
  - The judgement follows Matthias's source rules: same kind, representative, questioned, read myself.
  - Everything is in [EVIDENCE.md](EVIDENCE.md), E1, with each URL, the kind of source, what was read and what it
    says.
- **Result:**
  - **Confirmed:** aluminium 6061 and 7075 (VehicleComposition equals the Aluminum Association's Teal Sheets of
    December 2025, element by element), electrical steel (TractionMotor within ASTM A677) and ETP copper
    (TractionMotor equals KEMPER).
  - **Differs:**
    - **Magnets:** TractionMotor's Co of 4–12 % and its total rare earths of 33–42 % exceed the review of Yang et al.
      2017 (Co up to 5 %, rare earths 31–32 %).
    - **Circuit boards:** VehicleComposition's copper of 2.5–7.4 % is against 14.2 % measured by Bizzo et al. 2014.
    - **Magnesium:** VehicleComposition holds AZ91C and AM60A, not the robots' AZ91D and AM60B.
  - **New, with no sibling data:** titanium Ti-6Al-4V, the bearing and gear steels, carbon fibre, alumina.
  - **Not readable:** Argonne's battery data (blocked), the standards themselves (paywalled), one review (site down).
- **Not covered:** no recipe is proposed yet, and no number is entered. That waits for Matthias's decisions on the
  sources.

### V13. Point 9: the split of robot 3's "Electrical & magnetics group"

- **What:** the estimate in the sheet Splits of `shared_lists.xlsx` and how 01 uses it.
- **How:**
  - Robot 3's report was read first: §5 says the workbook "supports only their combined mass".
  - The shares were computed from the workbook's modes of robot types 2, 4 and 5 (not typed by hand) and rounded to
    three decimals.
  - Ten tests in `TestSplits` cover the split itself (it adds back to the material's kilograms, at the mode and at
    the bounds) and eight faults: no remainder, two remainders, shares out of order, shares leaving the remainder
    below zero, a piece not labelled E, a piece in "Mixed", a name split without saying "Split", and "Split"
    without its pieces.
  - The real-file test checks robot 3 at the mode: magnets 1.26, electronics 0.84, copper 2.1, Mixed 2.3 kg.
- **Result:**
  - 65 tests pass.
  - Robot 3 still adds up to 72.4 kg.
  - Its pages show the three pieces marked E: dotted bars, and on the list page their shares and basis under the
    group.
  - Bounds of the pieces: magnets 0.54–1.51, electronics 0.42–1.23, copper 1.59–3.63 kg.
- **Not covered:** no source outside the workbook supports the shares. They are the workbook's own Estimates of
  other robot types.

### V12. The shared-lists pages and the robot pages, opened and read

- **What:** the six `*_shared_lists.png` and the six `*_robot.png` pages of `figures/schemas/categories/`.
- **How:** each page opened as an image and read against the workbook and `shared_lists.xlsx`.
- **Result:** the defects below were found and fixed; all pages were redrawn and read again.
  - **Shared-lists pages:**
    - the text of the "Not allocated" row ran into the next column;
    - there was too much space above the materials;
    - a heading touched its neighbour;
    - one reason named CF-PEEK for robot 3, whose grades hold none. The wording was corrected in
      `shared_lists.xlsx`; no placement changed.
  - **Robot pages:**
    - an evidence label was lowercased ("direct");
    - the empty space above a short robot was unexplained, so the 1.85 m line was added;
    - "Hands: no motors" now reads "its motors are inside, not counted";
    - the whole-body box listed the same parts for every robot, and now lists the robot's own;
    - the "Legs" label of robot 6 lay on the whole-body box.
  - **Matthias's changes:** after seeing the first robot pages ("It looks better as robot, but the material
    compsotion as bar plat"), the materials robot was replaced by bars, on one kg scale for all six pages.
- **Not covered:** whether each placement is right. That is Matthias's check of these pages.

### V11. The material sheet and the shared lists, each check seen to catch its fault

- **What:** the new checks of `check_workbook` (sheet `Material Composition per Cat`) and of `check_shared_lists`.
- **How:** `tests/test_schemas.py`. The small test workbook gained a material sheet and small shared lists in the
  real layouts. Each test breaks one thing:
  - **six faults of the material sheet:** a sum row, a share, the unallocated row against the parts and against the
    stated mass, a minimum above its mode, a colour against its evidence;
  - **fourteen faults of the shared lists:** a part not placed, placed twice, under another name, under another
    robot type, in a group or region not listed, with a region and a split at once, with a split that does not add
    up, with more motors than units; a material name not placed, placed in a material not listed, placed in "Not
    allocated", or not in the workbook.

  Further tests cover the sums by group, region and material; the robot's height; the label spacing; the motors per
  region; the bounds; and the drawing of the pages. On the real files: all 68 parts and 35 names are placed. For
  every robot type, the groups, the regions and the materials with "Not allocated" each add up to the mode of its
  parts list, and the motors are 23, 31, 52, 30, 28 and 14.
- **Result:** 55 tests pass. On the real workbook, the material sheet shows no fault: its sums, shares and
  unallocated rows all agree with the parts lists.
- **Found while testing:** the first test workbook left out one column of the material sheet. The test was wrong,
  not 01.

### V10. The draft of the shared lists

- **What:** [SHARED_LISTS.md](SHARED_LISTS.md): the 68 parts placed in part groups and body regions, the 35
  material names placed in shared materials.
- **How:** a script read the parts through `read_workbook` of 01 and the material rows of the sheet
  `Material Composition per Cat`. It stopped on any part or name missing or placed twice. Its tables were put into
  the draft by a second script, not copied by hand.
- **Result:**
  - All 68 parts and all 35 names are placed exactly once.
  - For each robot type, the part groups, the body regions and the materials with "Not allocated" each add up to
    the mode of its parts list: 35, 70, 72.4, 69, 103.4 and 93.6 kg.
  - The three splits by number of units add up to their rows' units.
  - The motors counted outside the hands: 23, 31, 52, 30, 28 and 14.
- **Not covered:** whether the placements are right. That is Matthias's check of the draft.

### V9. Category 1: its report against the workbook

- **What:** `documentation/sources/01_category_compact_research_developer_components_materials_2040.md` (Matthias,
  2026-10-23) against the workbook's rows for category 1:
  - `Taxonomy` row 2;
  - `Components & Materials` rows 8 to 23;
  - `Material Composition per Cat` rows 5 to 16;
  - `Actuators by Joint` rows 5 to 8;
  - `Material Trajectories 2025-2040` rows 5 to 7.
- **How:** every number of the report's tables read and compared with its cell, by hand. The report's group totals
  (§5 and the appendix) were recomputed from the rows.
- **Result:** every number agrees.
  - The 13 parts: number, mass of one and of all units, evidence.
  - The sum: 30.53 / 35 / 39.47 kg.
  - The 10 material families: 28.9 / 35 / 41.3 kg in total.
  - The four joint modules (23 units).
  - The 2025–2040 trajectory.
  - The category limits: 1.20–1.45 m, 30–50 kg, 2–5 kg payload, $15,000–45,000.
  - The report's group totals add up: joint modules 15.5 / 17.6 / 19.7 kg, which the report calls "actuation" and
    which leaves out the battery. Its appendix adds up to 35.00 kg.
- **The report's own limits, not faults of the workbook:**
  - The battery is labelled Derived, but its derivation is not supplied.
  - The depth camera is labelled Direct, but its spread has no source.
  - The material bounds (28.9–41.3 kg) are independent of the parts' bounds (30.53–39.47 kg). Only the modes meet,
    at 35 kg.
  - The 2025 cost is $16,000 in the table but near $12,000 in the text.
  - The projected masses of 2030 to 2040 (28, 25, 22 kg) fall below the category's 30 kg lower limit.
- **Not covered:**
  - The report's web sources were not opened.
  - The market units of category 1 (sheet `Market Units & Shares 2025-2040`) come from report 00 and were not
    compared with it.

### V8. The pages of 01, opened and read

- **What:** all eight pages of `figures/schemas/`: the overview, the six category pages and `faults.png`. Also a
  category page and a faults page drawn from a test workbook with one deliberate fault.
- **How:** each page opened as an image and read line by line against the workbook rows it names.
- **Result:**
  - First drawing: three defects, all fixed and redrawn.
    1. The report file names ran out of their boxes on the overview, and broke mid-word on the category pages. They
       now break after underscores, tested by `test_a_long_file_name_is_broken_after_underscores`.
    2. Category 5 showed "Structure & Protection" twice, because the workbook splits it over rows 71 and 75 to 76.
       Each subsystem is now shown once, tested by `test_a_subsystem_split_in_the_sheet_is_shown_once`.
    3. Shares were shown with three decimals (+14.889 %). They now have one, as the workbook writes them (+14.9 %).
  - On the page with a deliberate fault, the faulty row is drawn in red, and `faults.png` lists the fault with its
    sheet and row.
- **Not covered:** the pages were read on screen, not printed.

### V7. The real workbook, read by 01

- **What:** `data/raw/humanoid_robots_2040_workbook.xlsx`, sheets `Taxonomy` and `Components & Materials`.
- **How:** `test_six_categories_68_parts_and_no_fault` and a run of `01_schemas.py`.
- **Against:**
  - the workbook's own statement of 68 parts (row 3);
  - two numbers read by hand from the sheet: category 5, sum of the parts at the mode 103.4 kg (row 77), stated mass
    90 kg (row 78).
- **Result:** 6 categories, 68 parts, 297 units. All nine checks pass with no fault. Both hand-read numbers match.
- **Not covered:** whether the workbook's numbers are right. That needs the sources, report by report, and categories
  5 and 6 have no report here.

### V6. Each check of 01, seen to catch the fault it guards

- **What:** the nine checks of `check_workbook` (listed in `CHECKS_DONE` and in [METHODOLOGY.md](METHODOLOGY.md)).
- **How:** `tests/test_schemas.py` builds a small workbook in the layout of the real one: two categories, three
  parts, a notional anchor robot. Each test breaks one thing and asserts that exactly one fault (two for a minimum
  above the mode of both masses) is reported, with the right row and words. Thirteen faults are tested:
  - a minimum above the mode;
  - a mass of all units that is not the number times the mass of one;
  - a missing mass;
  - a sum row that disagrees with its parts;
  - a sum row with the wrong number of units;
  - a difference row that disagrees, in kg and as a share;
  - a row coloured against its evidence;
  - an evidence not in the key;
  - a last row that disagrees with the sum rows;
  - a wrong stated number of parts;
  - a category named differently in the two sheets;
  - a category without a parts list.

  The small workbook unbroken reads without fault.
- **Result:** all pass.
- **Not covered:** a fault the checks do not look for. The checks test the workbook's agreement with itself only.

### V5. The overview against the stage files

- **What:** the list of stages on the overview (`STAGES` in `01_schemas.py`).
- **How:** `test_the_overview_names_every_stage_of_the_project` compares it with the numbered `.py` files at the
  top of the project.
- **Result:** both are 00 and 01. A new stage fails the test until the overview names it.

### V4. The settings and their register

- **What:** `src/params_schema.py`, `00_parameters.py`, `params.xlsx`, `PARAMETER_REFERENCE.md`.
- **How:** `tests/test_parameters.py` (5 tests) and a run of `00_parameters.py`.
- **Result:**
  - The settings as written are valid, and each of the 7 has a description.
  - Five settings that cannot be used each stop with a ParameterError: a non-xlsx workbook, an empty sheet name, a
    tolerance of 0 or 0.08 kg, and 10 dpi.
  - The register and the reference list all 7.
  - The run reports the workbook and the sources as present.

### V3. The Python environment

- **What:** `.venv` against `requirements.txt`.
- **How:**
  - every pinned package's installed version compared with its pin, and each imported;
  - `pip check`;
  - a kernel started from the `.venv`, as Positron's console does, running one line;
  - a login terminal with the `.venv` activated: `which python pip`, `python --version`.
- **Result:**
  - All seven pins match, every package imports, and `pip check` finds no broken requirement.
  - The kernel runs the `.venv`'s Python 3.14.4 with the project folder as working directory.
  - Matthias confirmed that Positron shows `.venv (Python 3.14.4)`, that the console starts, and that Positron's
    terminal uses the `.venv`.
- **Not covered:** Claude did not press Positron's Run button. The stages were run with `./.venv/bin/python` from the
  project folder, which is what the settings in `.vscode/settings.json` make Run do.
- **Found:** without activation, `python3` in a terminal is a different Python (3.14.2, `/Library/Frameworks/`).

### V2. The files copied from the Empa folder

- **What:** the 30 files copied from `Empa/RAWCLIC/` (the model code, its input workbook, 26 research files, the
  diagram's two files).
- **How:** `cmp` of every copy against its original, byte for byte.
- **Result:** all 30 identical. Before the three research scripts were removed, their originals in Empa were compared
  again and found identical.

### V1. The documents moved into one folder

- **What:** the move of 25 documents into `Documents/Source/` (since renamed `documentation/sources/`), and the move
  of the 2040 workbook to `data/raw/`.
- **How:** files counted before and after; moves made without overwriting (`mv -n`).
- **Result:** 11 + 25 = 36 files, no name clashed. After the workbook moved to `data/raw/`, 35 remain in
  `documentation/sources/`.
