# Handover

Where the work stands, newest first: what was decided, by whom, and what is open. Written by Claude.

## 2026-10-27: the handover checked; aluminium's further alloys researched

- **Asked, in Matthias's words:** "Check the handover and then continue".
- **The check (V35):**
  - The working tree equals GitHub's `main` and 129 tests pass.
  - No output of 02 or 03 exists yet.
  - Two statements below were corrected: the commit named as the last one, and the backups, which are gone.
- **Continued** with the first open point that is Claude's to do: point 3 below, the element recipes, beginning with
  aluminium, at its first step (sources only).
  - Matthias said yes to downloading the Aluminum Association's two registration records.
  - The further alloys, where robots use them and their composition limits, are in [EVIDENCE.md](EVIDENCE.md)
    E1.1b (V36): 6082, 5052, 5083, and the die castings A380, 383, 384, A360 and ADC12.
  - The workbook names only 6061-T6 and 7075-T6. Nothing is proposed or entered.
- **Then, on his word** "Yes, propose the aluminium recipe per robot type, min / mode / max, from the sources of
  E1.1b, with estimates (E) for the alloy shares, verified on the web with references. Show it to me before anything
  is entered.":
  - The proposal is [EVIDENCE.md](EVIDENCE.md) E1.1c, drawn in a sandbox (V37).
  - Each robot type's aluminium is die cast 0 / 20 / 40 % (E), drawn as A380 or ADC12, half and half (E). The rest is
    wrought: 7075 at a share taken from the workbook's grades, 6061 the remainder.
  - Each alloy's elements have the registered limits as minimum and maximum, and the median of 2 or 3 analyses read
    as the mode.
  - The aluminium comes out 90.3 to 93.1 % Al at the modes, the rest mainly Zn, Si, Cu and Mg.
- **Agreed**, choosing the answer offered: "I agree with the aluminium recipe as proposed in E1.1c, including its
  choices." Not entered yet.
- **Next, his:** whether to enter it now. Entering it would add:
  - in `element_recipes.xlsx`: the seven element compounds, the eleven recipes and the six rows of E1.1c;
  - in 01: the atomic masses of Zn, Sn and Pb, and a test that reproduces E1.1c's table at the modes;
  - in 02: the plain names zinc, tin and lead for its pages.

  02 draws the recipes without any other change. Everything else below stands.
- **Then, on his word** "There are additional material element compositon in the car composition, chek also there":
  - The car projects' aluminium was read and checked (E1.1d, V38). The limits of every alloy in E1.1c, and of A383 and
    A360, equal the registration records.
  - The car files add the European die-casting grades (EN AC-46000, 46100; EN 1706 not read) and the car's mixes of
    extrusions and sheet (no source).
  - They hold no typical contents, so E1.1c's modes stand. Nothing in E1.1c is changed.
- **Then:** "Keep E1.1c as agreed and enter it now, as with the plastics and fibre composites."
  - **Entered (V39):** 7 compounds, 65 recipe items and 6 rows in `element_recipes.xlsx`, copied first; Zn, Sn, Pb in
    01, and check 17's text; the three element names in 02; two new tests.
  - 131 tests pass. Of 01's pages only faults.png's text changed.
  - 02 and 03 were run with 2,000 draws in the scratch folder: aluminium is now in the elements of every robot type.
- **Next, his:** the real run, which now includes aluminium (the four paths below).
- **Then, on his word** "Go on to magnesium: show me what the robots use and the sources first, verified on the web
  with references, and check the car composition files too.": [EVIDENCE.md](EVIDENCE.md) E1.2b (V40).
  - Every grade named for robots is a casting alloy: AZ91/AZ91D (SURENA IV, a die caster), AM60B and AM50A (a die
    caster).
  - The limits come from the producers (TMS compilation) and ICAST.
  - AgiBot's humanoids are "made mainly of magnesium alloy" (TechRadar), which stands against the workbook's robot
    type 4.
  - In the car file, AZ91C-E's means add up to 100.365 %, and its column "Co" is probably copper. Both were reported
    and not changed.
- **Then, on his word** "Yes, propose the magnesium recipe per robot type ... with AZ91D, AM60B and AM50A ...":
  - The proposal is [EVIDENCE.md](EVIDENCE.md) E1.2c, drawn in a sandbox (V41).
  - The limits are B94's for die castings. The modes come from six analyses: three of AZ91D, one of AM60, two of
    AM50.
  - The AM share comes from the workbook's grades, and the AM part is drawn as AM60B or AM50A, half and half.
  - Robot type 3 is AZ91D alone.
- **Then Matthias, on E1.2c:** "You should trust standards more than analysis performed at a university. They do NOT
  know quality measures for analytical procedures. This is different with comercial labs".
  - **The rule, kept as a memory for every later session:** for a composition, rank the sources as follows:
    1. the standard or registration record;
    2. commercial analyses (certified reference materials, producers' certificates and nominal compositions);
    3. university analyses, as context only, never the basis of a number.
  - **What it puts in question:**
    - E1.2c's modes, all from university analyses except AM50A's certificate;
    - in the entered E1.1c, the modes of 6061 and ADC12 (university or institute analyses only), and the university
      analyses among those of 7075 and A380.
  - **Commercial values read so far:**
    - 7075: NIST SRM 1259 and Castle Metals France's certificate;
    - A380: Arconic's reference material KC380 (its Mg above A380.0's limit);
    - AZ91D, AM60B, AM50A: Magnesium Elektron's nominal Al, Zn and Mn;
    - AM50: the maker's certificate quoted by Jesus et al. 2026.
  - **Proposed order for a mode:**
    1. commercial values read first-hand (certificates and reference materials, then producers' nominal values);
    2. else the middle of the standard's range (E), from 0 to the maximum where only a maximum is given.

    For 6061 and ADC12, and for most trace elements, commercial values would be searched for first.
- **Then:** "Yes, redo the modes of E1.2c and of the entered E1.1c by my rule ...".
  - Aluminium: [EVIDENCE.md](EVIDENCE.md) E1.1e. The modes come from SAE's nominal compositions (6061, 7075) and from
    certified reference materials: Arconic's SS-6061, SS-7075, KC-380 and SS-380, and NIST's SRM 1259 and 1256b.
    ADC12 has no commercial value and takes the middle of the JIS ranges (E).
  - Magnesium: E1.2d. The modes come from SAE's AMS4490K for AZ91D, Magnesium Elektron's nominal values, and the AM50
    certificate. The trace elements of AZ91D and AM60B take the middle of their ranges (E).
  - Drawn in a sandbox (V42); nothing is entered. E1.1c stays in the workbook as it is.
- **Agreed:** Matthias, 2026-10-27, choosing the answer offered: "I agree with the modes of E1.1e and E1.2d, including their choices." Not entered yet.
- **Next, his:**
  - whether to enter E1.1e (rewriting the aluminium modes in the workbook);
  - whether to enter the magnesium recipe of E1.2c with the modes of E1.2d. E1.2c's shares were not agreed on their own.

## 2026-10-26, end of the day: where everything stands (start here)

Matthias, leaving: "Handover. I will need to go I let you work". Nothing was started after it: every next step
below waits for his word.

### What is built, and on GitHub

- **The stages**, each run by pressing Run:
  - `00_parameters.py`: the settings;
  - `01_schemas.py`: what the workbook defines, the shared lists and the robot in one view;
  - `02_composition.py`: the Monte Carlo draws of each robot type, for stock-and-flow;
  - `03_comparison.py`: the robot types side by side.
- **The inputs**, all three checked by 01 and 02:
  - `data/raw/humanoid_robots_2040_workbook.xlsx`: Matthias's, never changed;
  - `data/researched/shared_lists.xlsx`: placements, splits, battery cells;
  - `data/researched/element_recipes.xlsx`: the cells, the compounds and the recipes of the battery cells, the
    plastics and the fibre composites.
- **Tests:** 129 pass (`./.venv/bin/python -m unittest discover -s tests`).
- **On GitHub:** https://github.com/MattRoess/RAWCLICHumanoidRobots, `main`. The stages and tests are those of commit
  c512345; the commits after it change documents only. Code and documents only; the git folder is
  `$HOME/gitdirs/RAWCLICHumanoidRobots.git`.
- **Not run at full size:** 02 and 03 have run only with 2,000 draws, into Claude's scratch folder. `data/consolidated/`,
  `figures/composition/` and `figures/comparison/` do not exist yet. `figures/schemas/` was last drawn before 02
  existed: its overview still says "not built yet" until 01 is run again.

### Waiting for Matthias

1. **The real run, his:** press Run on, in this order:
   - `/Users/rm/Library/Mobile Documents/com~apple~CloudDocs/Documents/GitHub/RAWCLICHumanoidRobots/00_parameters.py`
   - `/Users/rm/Library/Mobile Documents/com~apple~CloudDocs/Documents/GitHub/RAWCLICHumanoidRobots/01_schemas.py`
   - `/Users/rm/Library/Mobile Documents/com~apple~CloudDocs/Documents/GitHub/RAWCLICHumanoidRobots/02_composition.py`
   - `/Users/rm/Library/Mobile Documents/com~apple~CloudDocs/Documents/GitHub/RAWCLICHumanoidRobots/03_comparison.py`

   The draws come to about 250 MB, computed, not measured. Memory is estimated at around 1 GB; the time was not
   measured.
2. **Not allocated below zero:** in about half of robot type 1's draws and two thirds of robot type 2's, because
   their materials and their parts are drawn independently (V32). Whether to tie the two is his decision.
3. **The element recipes of the other materials**, one at a time, as before: sources first, then a proposal, then his
   agreement, then the entry. His comments are in the table "His comments, material by material" below:
   - aluminium: "a more mixed approach": the further alloys and their sources are in E1.1b, the recipe in E1.1c,
     agreed and entered on 2026-10-27 (V39);
   - magnesium: "the selection is more limited";
   - titanium: robot types 2, 5 and 6;
   - steel: researched in E1.4b;
   - copper, with the silver of the circuit boards;
   - magnets: the high-temperature grades for the joints, E1.6b;
   - electronics;
   - ceramics.

   The decisions still open for them, from "Open: Matthias's decisions, before any min / mode / max" below:
   - the magnets' basis and Dy content;
   - the circuit boards' basis;
   - the grade shares: 6061 against 7075; GCr15 against 42CrMo and 20CrMnTi; alumina against SiC;
   - the steels without a grade.
4. **Smaller points, all his:**
   - whether the shared-lists pages also show the battery as cells;
   - a range of motors per robot (SHARED_LISTS.md, point 11), and a better split by body region (point 5);
   - whether the earlier model `HumanoidRobotsMC/` stays or goes;
   - whether reports 05 and 06 exist;
   - the `.md` and `*_original.md` pairs among the earlier research;
   - rewriting the first commit (557967b), which still holds `PARAMETER_REFERENCE.md`;
   - a reader of humanoid robots in RAWCLICStockAndFlow, which is another repository (recommendation e).

**Settled since the older "Open" lists below:**
- the repository exists;
- the stages are 02 and 03, his choice of one stage for all six robot types, not 02 to 08;
- the shared lists live in `data/researched/`;
- the battery, the plastics and the fibre composites are entered (V23, V26, V28).

### For the next session

- Read the folder's `CLAUDE.md`, then this section, then the section below.
- To test 02 and 03 on the real inputs without touching `data/` or `figures/`:
  - load the stage with importlib, registered as 'composition' or 'comparison';
  - take `current()` from `src/params_schema.py`;
  - set `composition.draws` to a few thousand;
  - point `output.composition_dir`, `output.composition_figures_dir` and `output.comparison_dir` at a scratch folder;
  - call the stage's `run(params)`.

  The scripts of the session of 2026-10-26 (`sandbox_02.py`, `sandbox_03.py`, `mutants_02.py`, `mutants_03.py`)
  were in its scratch folder and are gone.
- The backups made before each data entry were in the same scratch folder: `shared_lists_before_battery.xlsx`,
  `shared_lists_before_kept_recipe.xlsx`, `element_recipes_before_plastics.xlsx`,
  `element_recipes_before_composites.xlsx`. They are gone: the folder was empty on 2026-10-27. Git does not hold the
  workbooks, so the files in `data/` are the only copies.

## 2026-10-26: 02_composition.py and 03_comparison.py built and tested with few draws

### Asked, in Matthias's words

- "I agree with the specification of 02_composition.py and 03_comparison.py and with the recommendations a to g. Build
  it step by step, tests first, and test with few draws only."

### Built

- **`02_composition.py`:** points 1 to 14 and 16 to 18 of the specification below. It reads and checks the inputs with
  01's functions, draws each robot type, checks every draw, and only then writes, for each robot type separately,
  `data/consolidated/<n>_<name>/` (the draws as float32 `.npy` with their columns in `.txt`, and `summary.xlsx` /
  `summary.csv`) and a page into `figures/composition/`.
- **`03_comparison.py`:** point 15. It reads 02's files as they are, checks that they belong together, and draws
  `figures/comparison/materials.png`, `elements.png`, `part_groups.png`, `body_regions.png`: one small chart per item,
  one row per robot type, each with its 95 % interval.
- **Settings** in `src/params_schema.py`: `composition.draws` (200,000), `composition.seed` (1), the output folders,
  and the NMC cells' energy per kg (below, point 2).
- **Tests:** 21 of 02 and 5 of 03, written first; 129 tests pass in all. 14 deliberate faults were all caught (V31,
  V33). 02 and 03 were run on the real inputs with 2,000 draws, outside `data/` and `figures/`, and every page read
  (V32, V33). 01's overview names the four stages (V34).
- **Documents:** METHODOLOGY ("What 02 draws", "What 02 writes", "What 03 draws"), README, SHARED_LISTS, VERIFICATION
  V29 to V34.

### Choices made while building, confirmed by Matthias

Matthias, 2026-10-26, choosing the answer offered: "I confirm the eight choices made while building 02 and 03, as listed in
HANDOVER.md."

1. **The kept battery rows name their cells' recipe.** No input said that robot types 2 and 6 follow the NMC recipe,
   which he decided in E1.7e, so 02 could not draw their elements. 'NMC cylindrical' is now in the column "Cell or
   material" of their two kept rows in `data/researched/shared_lists.xlsx`, and 01 requires a kept row to name a
   recipe (check 16). The file was copied first (V29).
2. **Three more settings than point 17 named:** `composition.nmc_wh_per_kg_min`, `_mode`, `_max` (232.5 / 241.5 /
   256 Wh/kg, E1.7d). Recommendation f needs these numbers, and the parameter file is where a number of the code
   lives.
3. **A recipe is drawn once in each draw**, and used wherever it sits in the robot type. Robot type 5's two plastics
   rows hold the same TPU, and robot type 3's CFRP and GFRP hold the same epoxy: each shares one draw. The other
   reading, a draw for each row, narrows the band (V31).
4. **02's own check:** an item that follows a cell's energy may sit only in the recipe of NMC cells, used as the
   recipe of cells.
5. **Each robot type has its own random numbers**, from the seed and its number, so that it gives the same draws
   however many robot types are drawn.
6. **02 writes nothing unless all six robot types pass every check.** It keeps them in memory meanwhile: around 1 GB
   at 200,000 draws, estimated, not measured.
7. **The summary** has, per material, "In the elements" (Yes, Partly, No, or "Not in this robot type"), and its
   kilograms that are in the elements at the mean.
8. **A limit, not changed:** numpy draws an alternative only when the probabilities of its group add up to 1 within
   about 1e-8. 01 allows 0.001. An entry between the two would stop 02 with numpy's error rather than a fault line.
   Every entry so far is 0.5 / 0.5.

### A result for Matthias

Not allocated is below zero in 50.8 % of robot type 1's draws and in 67.4 % of robot type 2's (2,000 draws). The
other robot types are at 0 to 0.2 %. In the workbook, these two robot types' materials add up to their parts at the
mode, so drawn independently the difference sits around zero. For robot type 2 the materials' triangles lean further
right than the parts' (73.5 kg against 71.4 kg at the mean). Recommendation b allows it and reports it; whether the
parts and the materials should be tied to each other is his decision.

### The real run: his

In order, each by pressing Run:
1. `/Users/rm/Library/Mobile Documents/com~apple~CloudDocs/Documents/GitHub/RAWCLICHumanoidRobots/00_parameters.py`
2. `/Users/rm/Library/Mobile Documents/com~apple~CloudDocs/Documents/GitHub/RAWCLICHumanoidRobots/01_schemas.py`
3. `/Users/rm/Library/Mobile Documents/com~apple~CloudDocs/Documents/GitHub/RAWCLICHumanoidRobots/02_composition.py`
4. `/Users/rm/Library/Mobile Documents/com~apple~CloudDocs/Documents/GitHub/RAWCLICHumanoidRobots/03_comparison.py`

The draws come to about 42 MB per robot type, 250 MB in all.

### Open

- The element recipes of aluminium, magnesium, titanium, steel, copper, magnets, electronics (with silver) and
  ceramics: until then their kilograms are drawn, their elements are not.
- RAWCLICStockAndFlow has no reader of humanoid robots yet (recommendation e).
- The earlier open points below stand.

## 2026-10-26: the specification of 02_composition.py and 03_comparison.py (agreed by Matthias; built, see above)

### Asked, in Matthias's words

- "When can we start with the code for the six different robot types. Do you want to keep them as separate code or as
  one combined. The composition has the be for each of the type as there are different stock and flows for them".
- Then, choosing the answer offered: "One stage, 02_composition.py, with the same code for all six robot types,
  writing each type's composition separately for stock-and-flow, and a comparison stage after it. Write the
  specification first, as a numbered checklist, before building."

### The specification, as agreed

**What 02 reads and checks**
1. The workbook, the shared lists (with Splits and Battery cells) and element_recipes.xlsx, through 01's reading
   functions (one copy of the code). It runs 01's checks first and **stops** on any fault, saying which.
2. The settings in `src/params_schema.py`, through 00: the number of draws, the seed, the output folders (point 17).

**What 02 draws, for each robot type, the same code for all six** (N draws, every one independent unless said)
3. Each part's mass of all units: a triangle on the workbook's minimum, mode and maximum.
4. Each material row's mass: a triangle on its minimum, mode and maximum.
5. Splits (robot type 3's electrical group): each share a triangle, the remainder 1 minus the others.
6. The battery as cells (E1.7j, E1.7k): one cell build drawn per draw, all builds equally likely; cells = their number ×
   the mass of one cell; the rest = the row's draw minus the cells, split by its shares; Not allocated takes its part.
7. The element recipes: every share a triangle, every remainder 1 minus the others, every alternative drawn as a
   discrete state (the can, TPU's soft segment, the epoxy). The NMC cell's coatings and foils move with the drawn
   cell's energy per kg ("Follows the energy", E1.7i).
8. Not allocated = the parts' sum minus the materials' sum, draw by draw.
9. Materials without a recipe yet (aluminium, magnesium, titanium, steel, copper, magnets, electronics, ceramics) and
   Mixed: their kg are drawn; their elements are not, and the outputs say so. A recipe added later needs no code
   change.

**What 02 writes, for each robot type separately** (`data/consolidated/<n>_<name>/`, the folder another repository
reads; not in git)
10. The draws, kg per robot, as arrays of N rows (`.npy`, float32, like RAWCLICVehicleTractionMotor), each with the list
    of its columns (`.txt`): by shared material; by element; by part group; by body region; the robot's total. Row i
    is the same draw in every array, so stock-and-flow can pair them.
11. A summary table (`.xlsx` and `.csv`): per material and per element the mean, the median and the 95 % interval,
    and which materials are not yet in the elements.

**What 02 checks, with tests first**
12. In every draw: materials plus Not allocated equal the parts' sum; the elements add up to the materials that have
    recipes; cells plus rest equal the battery row; no mass below zero except Not allocated.
13. Tests on the small workbook with few draws: the same seed gives the same draws; means agree with the triangles'
    means; a discrete state is drawn about as often as its probability; the sums of point 12 hold.

**What 02 and 03 draw as figures** (`figures/`; not in git)
14. 02, one page per robot type: kg by material and kg by element, each with its 95 % interval.
15. 03 reads the six robot types' draws from 02, never re-deriving them, and draws them side by side: by material, by
    element, by part group and body region, each with its 95 % interval.

**Running, settings, documents**
16. Both run by pressing Run, no arguments. The real run is Matthias's; Claude tests with few draws in a sandbox.
17. New settings: `composition.draws`, `composition.seed`, and the output folders of 02 and 03.
18. METHODOLOGY, README, VERIFICATION and HANDOVER updated in the same step; the parameter reference is regenerated
    by 00.

### Recommendations a to g, agreed by Matthias

- **a. A part's units:** drawn together (one triangle on all units) or each unit on its own. Recommended: together,
  as the workbook gives one range per part.
- **b. Not allocated below zero:** the parts and the materials are drawn independently, so in some draws the
  materials exceed the parts. Recommended: allowed, and reported as the share of draws below zero.
- **c. Materials without a recipe yet:** run 02 now, with their elements missing and said so, or wait for all
  recipes. Recommended: now; the recipes come in without a code change.
- **d. Number of draws:** 200,000, as RAWCLICVehicleTractionMotor and RAWCLICDataCenters. With float32 this is about
  0.8 MB per column, some 50 MB per robot type. Recommended: 200,000.
- **e. Format for stock-and-flow:** RAWCLICStockAndFlow has no humanoid robots yet. Recommended: the sibling pattern of
  point 10, so its reader can follow `src/traction_draws.py`.
- **f. The NMC cell's energy per kg for robot types 2 and 6**, whose battery rows are kept: drawn from the NMC triangle
  of E1.7d (232.5 / 241.5 / 256 Wh/kg). Recommended.
- **g. Which items go into the figures** of points 14 and 15: his decision; recommended as listed there.

## 2026-10-26: the project on GitHub

- **Asked, in Matthias's words:** "Generate a new repository on GitHub, which is public. and start to commit and
  push".
- **Done:** https://github.com/MattRoess/RAWCLICHumanoidRobots, public, branch `main`. The git folder lives in
  `$HOME/gitdirs/RAWCLICHumanoidRobots.git`, like the siblings'; the project folder holds only the `.git` pointer.
- **Left out, by `.gitignore`:** every data file (`.xlsx`, `.csv`, `.png` except the diagram in
  `documentation/sources/`), `figures/`, `.venv/`, `.DS_Store`, and the earlier model `HumanoidRobotsMC/`. Asked, he
  chose "Leave it out" for the earlier model, until he decides whether it stays, and "Commit them" for the sources in
  `documentation/sources/` (reports and diagram), which the licence does not cover.
- **Then, in Matthias's words:** "No figures or other items, which are generated by the code should go into the github
  repository". The one such file committed, `documentation/claude/PARAMETER_REFERENCE.md` (written by 00), was taken
  out of the repository and added to `.gitignore`; it stays on disk. The first commit (557967b) still holds it in
  its history; rewriting history is his decision.

## 2026-10-26, late night: the materials one at a time, with Matthias's comments

### Asked, in Matthias's words

- "Can we go through the material compostion. I want to comment on some of them", then, on a list of all materials at
  once: "Not in this way!!!" and "I want to comment on each material separetely damit!!". One material per message
  since then.

### His comments, material by material

| Material | His words | Done since |
|---|---|---|
| Aluminium | "I asume similar other aluminum alloys are also taken. Therefore the scope should be expanded and a more mixed approach taken" | Researched, 2026-10-27: [EVIDENCE.md](EVIDENCE.md) E1.1b, V36. Recipe: E1.1c, V37, agreed 2026-10-27. Car files checked: E1.1d, V38. Entered: V39 |
| Magnesium | "Silar as for the aluminum alloy, but I asume here the selection is more limited" | Researched, 2026-10-27: [EVIDENCE.md](EVIDENCE.md) E1.2b, V40. Recipe proposed: E1.2c, V41 |
| Titanium | "2, 5 and 6 are robots, which require titanium. It is expensive, but has strutural reasons most likely. Therefore keep in mind, if the other types of robots grow, then they might also require parts of titanium, as magnesium is not stable enough" | Nothing yet |
| Steel | "Try to find additional posible alloys, and see what the ranges for the emental composition could be" | Researched: [EVIDENCE.md](EVIDENCE.md) E1.4b |
| Copper | "There could be also silver for the printed cuircuit boards. This should be taken into account. It will be part of the PCB" | To be taken up with the electronics |
| Magnets | "There is a material composition sheet available for magnets. It is with the cars. Check it there. There are all the different composition, which allow also higher temperatures"; then "Yes use the high temperature once for the joins, which are often use like knees, elbows etc." | Checked: E1.6b, V15 |
| Fibre composites | Chose the answers offered: "Yes, go on to material 9, fibre composites: show me what the robots use and the sources first, verified on the web with references", then "Propose the fibre-composite recipe per robot type ...", then "I agree with the fibre-composite recipe as proposed in E1.9c, including its four choices." | Sources: E1.9b. Recipe: E1.9c, V27, agreed. Entered: V28 |
| Plastics | Chose the answers offered: "Yes, go on to material 8, plastics: show me what the robots use and the sources first", then "Propose the plastics recipe per robot type ...", then "I agree with the plastics recipe as proposed in E1.8c, including its four choices." | Sources: E1.8b. Recipe: E1.8c, V24, agreed. Verified on the web: E1.8d, V25; six values taken in on his word. Entered: V26 |
| Battery materials | "There are a full composition of battery materials in the batteries for cars. Check them"; then he chose the answer offered: "Battery materials should be the cells only in every robot type; the housing, BMS and busbars belong to the other materials." | Checked: E1.7b, V16. The robots' cells: E1.7c, V17. The cell mass per robot type: E1.7d, V18, agreed. Chemistry, grade, format, silicon: E1.7e to E1.7g, decided. The cells' element recipe: E1.7i, V20, agreed. Not entered yet |

No recipe is proposed and nothing is entered: each waits for his agreement.

### Open

1. **Battery materials, cells only.** In robot types 2 and 6 the row is cells already. In 1 it is the whole pack, in 3
   a "system", in 4 cells whose kg contradict the 700 Wh, and in 5 active materials only. He chose: "Set the cell
   mass from each robot's energy, with the kg per kWh of the cells robots actually use. Research those robot cells
   first and show me the sources. The rest of each row goes to the other materials or to Not allocated." The
   sources are in E1.7c and were shown to him. Then: "Yes, propose the cell mass min / mode / max for each robot
   type from these sources, and where the rest of each row goes. Show it to me before anything is entered." The
   proposal is E1.7d. **Agreed**, choosing the answer offered: "I agree with the cell-mass proposal as written in
   E1.7d, for robot types 1, 3, 4 and 5, with robot types 2 and 6 kept as in the workbook." Then: "Enter the cell
   masses later, together with the battery element recipe. Continue with the open battery points first."
2. **Battery materials, further, one point at a time:**
   - the chemistry of robot types 2 and 6 (E1.7e): decided, "Robot types 2 and 6 both get NMC cells with a liquid
     electrolyte, using the car file's NMC recipe.";
   - the NMC grade (E1.7e): decided, high nickel with the car file's liquid electrolyte, the same recipe in every NMC
     robot type; robot type 3 stays LFP;
   - the cell format (E1.7f): decided, "Cylindrical for all";
   - the Si in the anodes (E1.7g): decided, 0 / 1 / 7.3 % as silicon oxide, graphite the remainder, in every NMC
     robot type;
   - the cells' element recipe: the sources in E1.7h; the proposal in E1.7i, **agreed**: "I agree with the element
     recipe of the NMC and LFP cylindrical cells as proposed in E1.7i."
   - All battery points are settled. Open: where and how the cell masses and the recipe are entered, together, as he
     asked ("Enter the cell masses later, together with the battery element recipe").
   - He agreed the plan to enter them ("Yes, build the battery entry as laid out ..."), then, before anything was
     built: "The number of cells, which also defines the cell mass depends on the voltage, which these batteries
     have and the robots use". The build is paused; the revised cell mass is E1.7j, shown to him. Robot type 3 did
     not fit the cells read; he asked: "Search for a citable LFP cell sheet that builds a 48 V, 9 Ah pack within the
     packs' 9.6 kg ...". Three makers' cells fit (E1.7k): 7.20 / 7.33 / 7.33 kg. He agreed: "I agree with the cell
     masses counted from voltage and capacity in E1.7j, with robot type 3 from the three LFP cells of E1.7k. Resume
     the battery entry as laid out."
   - **Entered** (V23): the sheet Battery cells in `shared_lists.xlsx`, the new `element_recipes.xlsx` (setting
     `data.element_recipes`), checks 15 and 16 in 01 with 27 new tests, the robot pages showing cells only. The new
     check found the coatings could reach 101 %; he chose "Lower active max" (E1.7i).
   - **Not done, his to decide:** whether the shared-lists pages should also show the battery as cells; the recipes of
     the other materials.
3. **The materials still to go through:** plastics (what the robots use and the sources, E1.8b; the recipe proposed
   on "Propose the plastics recipe per robot type, min / mode / max ...", E1.8c, V24; **agreed**: "I agree with the
   plastics recipe as proposed in E1.8c, including its four choices."; not entered yet; then, on his question
   whether everything was verified, the nine open points were checked on the web, E1.8d, V25; six values moved
   slightly and he took them in: "Yes, take the six verified values of E1.8d into the plastics recipe."; then
   entered on "Yes, enter the plastics recipe now as laid out", V26),
   fibre composites (what the robots use and the sources, verified on the web, E1.9b; the recipe proposed on
   "Propose the fibre-composite recipe per robot type ...", E1.9c, V27; **agreed**: "I agree with the fibre-composite
   recipe as proposed in E1.9c, including its four choices."; entered on "Yes, enter the fibre-composite recipe
   now, as with the plastics", V28),
   electronics (with the silver), ceramics.
4. **The decisions listed in the section below**, as far as his comments have not settled them.

## 2026-10-26, night: the sources of the element recipes, checked on the web

### Asked, in Matthias's words

- "Yes, start researching the element recipes of the 13 materials, and show me the sources first".
- "Confirm your work with indepenedet research in the internet".
- "Document in detail the verification with your own internet research".

### Done

- The siblings' element data were found and checked against web sources read first-hand.
- The details are in [EVIDENCE.md](EVIDENCE.md) E1, and the summary in [VERIFICATION.md](VERIFICATION.md) V14.
- No recipe is proposed and nothing is entered.

### Open: Matthias's decisions, before any min / mode / max

1. **Magnets:** the siblings exceed the literature on Co and the total rare earths. Which basis, and which Dy content
   for each robot type?
2. **Circuit boards:** VehicleComposition's EVA2 copper against measured boards. Which basis?
3. **Battery materials:** what they hold in each robot type, and which chemistry where the workbook names several.
   Argonne could not be read.
4. **Grade shares:** 6061 against 7075; GCr15 against 42CrMo and 20CrMnTi; alumina against SiC. No source gives them.
5. **Plastics and fibre composites:** elements or not, and the fibre shares.
6. **Steels without a grade:** robot type 1's "high-strength steel" and robot type 3's "fastener steel".

## 2026-10-26, evening: a page per robot type to verify, and the robot in one view

### Decided, in Matthias's words

- **"I need schema for each of the six types of robots, so that I can verify them".** He chose two things:
  - one extra page per robot type, drawn by 01, with every part and material and its place on the shared lists;
  - the placements in `data/researched/shared_lists.xlsx`, a workbook he can correct in Excel.

  Since then this workbook is the one place that holds the placements, and 01 checks it.
- **"The lists under schemas are OK, but for me this is not a schema, which explains things in details. I want theat
  one can understand the robot and its compostion and parts in one vew".** A robot page per type: the robot drawn to
  its height, at one scale for all six, with its parts where they sit, its body regions and its motors.
- **For the materials**, first "No I want to see it as a robot. Be more inovbative and visual" (drawn as layers in a
  robot outline), then, on seeing it: "It looks better as robot, but the material compsotion as bar plat". The
  materials are now bars beside the robot, on one kg scale for all six pages.

### Where it stands

- 01 reads the third sheet of the workbook (`Material Composition per Cat`) and checks it: no fault.
- It draws 3 pages per robot type, 18 in all, plus the overview and the faults.
- 55 tests pass (V11), and every page was read (V12).
- Nothing is committed.

### Open

1. **Matthias's check of the placements**, on the shared-lists and robot pages. Seen on 2026-10-26: "The robot pages
   work."
2. **Point 9: done the same evening.** Robot 3's "Electrical & magnetics group" is split by an estimate: magnets
   15.5 / 30 / 30.1 %, electronics 12 / 20 / 24.6 %, copper the remainder, from robot types 2, 4 and 5. At the mode
   that is copper 2.1, magnets 1.26 and electronics 0.84 kg. Matthias's words: "Robots 2, 4 and 5", "Copper as the
   remainder", "A sheet 'Splits' in shared_lists.xlsx". Found: for 52 motors the 4.2 kg is light, so part of the
   copper and magnets may sit in the 7.4 kg "Not allocated", which stays as it is (SHARED_LISTS.md, point 9; V13).
3. **The element recipes**, and the stages 02 to 08.

## 2026-10-26, later: the aim of the comparison, and the shared lists decided

### The aim, in Matthias's words

- "I want that it is possible to compare on a material level between the 6 types of roboy".
- Then, the start of the message cut off: "…ts and also on a component or parts level". Read as: by materials, by
  elements, and by parts.
- "So come up with a proposition, which I can understand as 20 year old, not familiar with the topic".

### Proposed, and taken up by Matthias

Describe all six robots with the same shared lists, then compare them side by side.

1. **Shared lists** of part groups, body regions and materials. Matthias asked for them to be drafted, adding "But
   whats about legs etc." (body regions) and "Whats about addining more degree of freedome, which means additional
   electrical motors" (a motor count per robot).
2. **An element recipe for each material**, with min / mode / max from sources, agreed before it is entered.
3. **One stage per robot type, 02 to 07.** Each draws its parts and materials (Monte Carlo) and translates them to the
   shared lists.
4. **One comparison stage, 08**, showing the six robots side by side.

### Decided

- [SHARED_LISTS.md](SHARED_LISTS.md) was drafted: 11 part groups, 6 body regions, 13 materials, and the motors per
  robot. Every one of the 68 parts and 35 material names is placed once (V10).
- Matthias went through its eleven points one by one and chose the recommended answer each time. The decisions are
  listed in SHARED_LISTS.md, "Decided".

### Category 1, gone through

- Its report agrees with the workbook on every number (V9).
- The report also holds a material table (10 families, 28.9 / 35 / 41.3 kg) and an outlook to 2040 (mass 35 → 22 kg).
- What its stage computes follows from the shared lists above; it is not built yet.

### Open

1. **Point 9:** done the same evening; see the section above.
2. **The element recipes** of the 13 materials: research, sources, min / mode / max, Matthias's agreement.
3. **Where the shared lists live** once code reads them (for example a workbook in `data/researched/`), and the
   stages 02 to 08.
4. **Later steps:**
   - a range of motors per robot (point 11);
   - a better split by body region (point 5).

## 2026-10-26: the project set up like RAWCLICDataCenters, and the schema of the six categories

### Where it stands

- `00_parameters.py` and `01_schemas.py` exist and run. 01 reads the six categories and their 68 parts from
  `data/raw/humanoid_robots_2040_workbook.xlsx`, finds no fault, and draws `figures/schemas/`: the overview, one page
  per category and the faults.
- 25 tests pass (`./.venv/bin/python -m unittest discover -s tests`). Every check is recorded in
  [VERIFICATION.md](VERIFICATION.md).
- Nothing is committed: the project has no git repository yet.

### Decided today, in Matthias's words

- **Python in Positron.** "Prepare it so it works in Positron with Python and its virual environment". Python 3.14.4
  from pyenv in `.venv` inside the project folder. Packages: at first only ipykernel. Then he asked to "add numpy,
  pandas, matplotlib, scipy, openpyxl and tqdm to requirements.txt, pinned like the siblings": the pins of
  RAWCLICVehicleBattery, and tqdm as in RAWCLICDataCenters. He confirmed that Positron's console and terminal use the
  `.venv`.
- **Copied from the Empa folder.** "I had in my Empa folder a previous project concerning humanoid robots and their
  composition can you copy it content here". He chose three of the four parts on offer:
  - the model code and its input workbook (`HumanoidRobotsMC/HumanoidRobotsMC.py`, now
    `data/02_HumanoidlRobots.xlsx`);
  - the research folder;
  - the component diagram.

  He did not take the model's outputs. The three research scripts were removed afterwards on his word: they could not
  run here (fixed paths `/home/ubuntu/...`), and their originals stay in `Empa/RAWCLIC/Robots/HumanoidRobots/`.
- **Documents together.** "Move all documents into the documents source folder. I want them united there": the
  research reports, the two research workbooks and the diagram.
- **The layout of RAWCLICDataCenters.** "We will follow the code, as it is in the datacenter folder so 00 for
  parameters and 01 prodcing schema and documenting everything in thos project". Asked about the open points, he
  chose:
  - the 2040 workbook, not the old HRC workbook;
  - folders like DataCenters: `Documents/Source/` became `documentation/sources/`, the workbook the code reads moved to
    `data/raw/`, and `Data/` became `data/`;
  - an overview, one page per category, and a page of faults.
- **Six categories.** "As far as I understand the new research there are four or five different type of categrories
  for humanoid robots. Draw a repective schema and the we will go through and do separate code for each of the
  different categories". The research has six. Asked, he chose to draw all six.

### Found today

- The workbook agrees with itself: no fault in any of the nine checks.
- Category 5, Boston Dynamics Atlas: the parts add up to 103.4 kg at the mode, against a stated mass of 90 kg
  (+13.4 kg, +14.9 %). The workbook states this itself. Category 3 is +2.4 kg (+3.4 %), category 6 +3.6 kg (+4.0 %),
  and categories 1, 2 and 4 match exactly.
- Category 6's anchor robot, "Guardian-X", is notional, and its stated 90 kg is a target labelled Estimate.
- Categories 5 and 6 have no report of their own in `documentation/sources/`. The workbook's last row names "Reports
  00–06", so reports 05 and 06 may exist elsewhere.
- In category 5 the subsystem "Structure & Protection" is split over rows 71 and 75 to 76. The page groups the rows;
  the workbook is unchanged.

### Open: Matthias's decisions

1. **The stages of the categories.** "we will go through and do separate code for each of the different
   categories". Which category first, and what each stage computes.
2. **The earlier model.** `HumanoidRobotsMC/HumanoidRobotsMC.py` and `data/02_HumanoidlRobots.xlsx` describe four
   classes (HRC-1 to HRC-4), a different classification from the six categories. Neither is part of the stages, and
   nothing reads them. Whether a category stage takes the model over, or it goes, is his decision.
   The model reads `../Data/02_HumanoidlRobots.xlsx` with a capital D. That works on both Macs, whose file system
   ignores case, but would fail on one that does not.
3. **Reports 05 and 06.** Whether they exist, and whether they belong in `documentation/sources/`.
4. **Git.** The project has no repository, no `.gitignore` and no remote yet.
5. **`.md` and `*_original.md` pairs** among the earlier research. What the difference is has not been looked at.
