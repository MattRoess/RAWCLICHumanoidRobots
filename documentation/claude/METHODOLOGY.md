# Methodology

How the project works, step by step. Written by Claude; kept up to date with every stage.

## The question

What is a humanoid robot made of, by category of humanoid robot, through 2040? Each mass has a minimum, a mode and a
maximum, so that the uncertainty is carried from the start.

## The stages

The stages are numbered files at the top of the project. They are run in order by pressing Run, with no arguments.
Every setting is in `src/params_schema.py`.

| Stage | Reads | Writes | Does |
|---|---|---|---|
| `00_parameters.py` | `src/params_schema.py` | `params.xlsx`, `documentation/claude/PARAMETER_REFERENCE.md` | Checks every setting, says which input files are on disk, writes the register of the settings. |
| `01_schemas.py` | `data/raw/humanoid_robots_2040_workbook.xlsx`, `data/researched/shared_lists.xlsx`, `data/researched/element_recipes.xlsx`, `data/researched/humanoid_register.xlsx`, `documentation/sources/` | `figures/schemas/` | Reads the six categories, their parts lists and their materials, and where each goes in the shared lists; reads the element recipes and counts each robot type's battery cells. Checks that the workbook agrees with itself, that everything is placed, that the recipes and the battery cells hold together, and that the register and its sheet Type 1 hold together (checks 21 and 22). Draws what the workbook defines, each robot type in the shared lists, and each robot type in one view. Nothing is drawn at random. |
| `02_composition.py` | The same three files, through 01's functions; the register (`data/researched/humanoid_register.xlsx`: its sheet Robots, and its sheet Type 1 for robot type 1's robots); for robot type 1 the parts file, the sibling projects' board, sensor and tantalum data where they lie, and RAWCLICVehicleTractionMotor's own magnet code in its own environment; the settings `composition.*` | `data/consolidated/<n>_<name>/`, `data/parts_taken_apart/`, `figures/composition/` | Draws what each robot type is made of, `composition.draws` times (Monte Carlo): its materials, its elements, its part groups and its body regions. Robot type 1 is drawn over the robots of the register's sheet Type 1 from the robots taken apart; the others from the workbook. Writes the draws and a summary for each robot type separately, for stock-and-flow; type 1 taken apart for 04; the pages. |
| `03_comparison.py` | The draws of 02; the names of the robot types from the workbook | `figures/comparison/` | Draws the robot types side by side, by material, element, part group and body region, each with its 95 % interval. Draws nothing at random itself. |
| `04_parts_taken_apart.py` | 02's draws of robot type 1 taken apart (`data/parts_taken_apart/`); the parts file through 01's functions (which joints run hot) | `figures/parts_taken_apart/` | Draws the two figures Matthias approved from 02's draws. Draws nothing at random itself. |

Matthias, 2026-10-26: "The composition has the be for each of the type as there are different stock and flows for
them", and, choosing the answer offered: "One stage, 02_composition.py, with the same code for all six robot types,
writing each type's composition separately for stock-and-flow, and a comparison stage after it." 02 and 03 read the
inputs through the functions of 01, so that what they draw is what the schemas show.

The data file of the robots of type 1 taken apart, `data/researched/parts_taken_apart.xlsx`, is written by
`tools/make_parts_taken_apart.py` (Matthias, 2026-10-27: "Yes, put the builder in tools/make_parts_taken_apart.py as
proposed, with its test and documents"; rewritten on 2026-10-28, "Yes, rewrite"). It is not a stage: it writes an
input, not a result, and holds the values agreed in EVIDENCE.md E2.8 to E2.8e; a change to them is made there, not in
the `.xlsx`. Pressing Run on it replaces the file. `tests/test_make_parts_taken_apart.py` checks that what it writes
passes 01's checks 18 to 20 and equals the file on disk, cell by cell.

## The workbook

`data/raw/humanoid_robots_2040_workbook.xlsx`, Matthias's workbook of the 2026 research. It is read and never
changed. 01 reads two of its sheets:

- **`Taxonomy`** defines each category: what it is for, its height and mass, its joints (degrees of freedom) and
  payload, its anchor robot. One row per category, numbered "1." to "6.".
- **`Components & Materials`** holds the parts list of each anchor robot. Per part it gives the subsystem, the part,
  where it sits in the robot, how many units the robot has, the mass of one unit and of all units (minimum, mode,
  maximum, kg), the main material, the evidence and the source references. Each category's parts are closed by
  three rows:
  - the sum of the parts;
  - the stated mass of the anchor robot;
  - the difference between the two: the sum's mode minus the stated mass, in kg and as a share.

  The last row of the sheet is the sum over all six categories.
- **`Material Composition per Cat`** describes the same anchor robots by material, as a second, separate view: per
  material its grade, minimum, mode and maximum in kg, its share and its evidence. Each category's materials are
  closed by two rows: their sum, and the kilograms they leave unallocated. The unallocated row gives the gap to the
  parts list in its mode column and the gap to the stated mass in its maximum column. The workbook names which part
  is made of which material only in words, so parts and materials cannot be joined without estimates.

**Evidence.** Every row is labelled Direct, Derived or Estimate, and coloured by the workbook's own colour key:

- **Direct** (no fill): reported in a manufacturer or sensor datasheet.
- **Derived** (light yellow): calculated from other numbers.
- **Estimate** (light orange): engineering reconstruction, teardown or scenario model.

The schemas use the same colours. The workbook's numbers have not been checked against their sources independently.
None of them may be called measured unless its evidence says Direct.

## The six categories

The table is generated from the workbook by the functions of 01, not typed by hand.

| # | Category | Anchor robot | Parts | Units | Sum of the parts, kg (min / mode / max) | Stated mass, kg | Mode minus stated | Report of its own |
|---|---|---|---|---|---|---|---|---|
| 1 | Compact Research & Developer | Unitree G1 (China) | 13 | 32 | 30.53 / 35 / 39.47 | 35 (Direct) | +0 kg (+0.0 %) | `01_category_compact_research_developer_components_materials_2040.md` |
| 2 | Full-Scale General-Purpose / AI Research | Unitree H2 / H2 Plus (China) | 14 | 42 | 52.7 / 70 / 91.6 | 70 (Direct) | +0 kg (+0.0 %) | `02_category_full_scale_general_purpose_ai_research_components_materials_2040.md` |
| 3 | Industrial Logistics & Warehousing | UBTECH Walker S2 (China) | 11 | 112 | 66 / 72.4 / 80.3 | 70 (Direct) | +2.4 kg (+3.4 %) | `03_category_industrial_logistics_warehousing_components_materials_2040.md` |
| 4 | Service / Healthcare / Interaction | AgiBot A2 (China) | 10 | 38 | 62.2 / 69 / 76.8 | 69 (Direct) | +0 kg (+0.0 %) | `04_category_service_healthcare_interaction_components_materials_2040.md` |
| 5 | Heavy-Duty / High-Performance / Hazardous-Environment | Boston Dynamics Atlas [electric] (US) | 9 | 37 | 84.4 / 103.4 / 123.9 | 90 (Direct) | +13.4 kg (+14.9 %) | none |
| 6 | Defense / Public Safety | Notional 'Guardian-X' Configuration | 11 | 36 | 74.8 / 93.6 / 113.6 | 90 (Estimate) | +3.6 kg (+4.0 %) | none |
| | All six | | 68 | 297 | 370.63 / 443.4 / 525.67 | | | |

Two things to know when reading it:

- The anchor robot of category 6 is **notional**: a configuration the research assumes, not a robot that exists. Its
  stated mass of 90 kg is a target, labelled Estimate.
- In category 5 the parts add up to 13.4 kg more than the stated mass of Atlas. The workbook states this difference
  itself; the check confirms only that it is computed correctly.

## The shared lists

To compare the six robot types, every robot is written in the same words (Matthias, 2026-10-26: "I want that it is
possible to compare on a material level between the 6 types of roboy"):
- 11 part groups (what a part is);
- 6 body regions (where it sits);
- 13 materials;
- the number of motors.

Each of the 68 parts and the 35 material names of the workbook is placed on these lists in
`data/researched/shared_lists.xlsx`. Matthias decided the placements point by point; the decisions and their
reasons are in [SHARED_LISTS.md](SHARED_LISTS.md). The rules:
- A part placed in several regions is split only where the workbook gives the units of each region, and goes to
  "Whole body" otherwise.
- A workbook name that holds several materials or groups goes to "Mixed". One exception is split by an estimate:
  robot 3's "Electrical & magnetics group", into magnets, electronics and copper as the remainder (point 9, sheet
  Splits). Each piece is its share of the name's kilograms, so the pieces add back to the workbook's minimum, mode
  and maximum, and every page marks them E.
- The kilograms the materials leave out of the parts list are shown as "Not allocated". Nothing is rescaled.

## The battery as cells only, and the element recipes

Matthias, 2026-10-26: "Battery materials should be the cells only in every robot type; the housing, BMS and busbars
belong to the other materials", and "The number of cells, which also defines the cell mass depends on the voltage,
which these batteries have and the robots use". The sources and every decision are in
[EVIDENCE.md](EVIDENCE.md), E1.7b to E1.7k.

- **The sheet Battery cells** of `data/researched/shared_lists.xlsx` says, for each robot type's battery row:
  - **Kept** (robot types 2 and 6): the workbook's row is cells already and stays. The row names the recipe its cells
    follow: the NMC cylindrical cell, as Matthias decided ("Robot types 2 and 6 both get NMC cells with a liquid
    electrolyte, using the car file's NMC recipe", E1.7e).
  - **Build** (robot types 1, 3, 4, 5): one way to build the packs from a cell: cells in series (from the pack's
    voltage) × cells in parallel (from its capacity) × packs, or, where no voltage or capacity was found (robot type
    5), the whole cells that hold the pack's energy. The cell mass is the number of cells × the mass of one cell from
    its datasheet. Every build of a robot type is equally likely; the pages show the middle one (the median) and the
    lightest to the heaviest.
  - **Rest**: where the workbook's row minus the cells goes. Robot type 1: its pack's enclosure, BMS and busbars,
    split into plastics (the remainder), electronics and copper by shares weighed in small battery packs. Robot types
    3, 4 and 5: Not allocated, which in robot type 5 gives up the 3.4 kg its cells weigh more than its row.

  The kilograms of each robot are unchanged; only where they sit moves.
- **The element recipes**, `data/researched/element_recipes.xlsx`:
  - **Cells:** the datasheet of every cell a build uses.
  - **Compounds:** each compound as a formula (atoms × the atomic masses of IUPAC 2024) or as mass shares.
  - **Recipe:** the parts of each recipe as a tree, down to their compounds: the NMC and the LFP cylindrical cell;
    the polymers (ABS, PC/ABS, flame-retardant PC/ABS, PA66-GF with its E-glass, CF-PEEK with its carbon fibre, TPU,
    silicone rubber); the fibre composites (two amine epoxies drawn half and half, carbon fibre with its sizing,
    CFRP, GFRP); the aluminium alloys 6061, 7075, A380 and ADC12 and the magnesium alloys AZ91D, AM60B and AM50A
    by their elements; and each robot type's plastics, aluminium and magnesium rows and robot type 3's composites
    row, split among what they name (each aluminium row: a die-cast part drawn as A380 or ADC12, the rest wrought,
    7075 and 6061; each magnesium row: an AM part drawn as AM60B or AM50A, the rest AZ91D, robot type 3 AZ91D
    alone). An item is a compound,
    a group, or another recipe (PA66-GF holds E-glass). A group's items are shares with exactly one remainder, so
    nothing is normalised, or alternatives drawn by their probability (the can: nickel-plated or stainless steel; the
    TPU's soft segment: polyester or polyether, half and half; the die-cast aluminium: A380 or ADC12, half and half;
    the AM magnesium: AM60B or AM50A, half and half).
  - **Rows:** which recipe each row of the workbook follows, for every shared material that has recipes; so far
    aluminium, magnesium, plastics, including robot type 1's battery pack enclosure (plain PC/ABS), and fibre
    composites.

  **The modes of an alloy's elements** follow Matthias's rules of 2026-10-27, best first:
  1. a standard's nominal composition (SAE AMS);
  2. certified reference materials and producers' certificates (the median over independent materials);
  3. a producer's nominal composition;
  4. where only university or research-institute analyses exist, their mean, leaving out any obviously wrong (E);
  5. otherwise the middle of the standard's range (E).

  The minimum and maximum are always the standard's limits.

  The sources:
  - aluminium: [EVIDENCE.md](EVIDENCE.md), E1.1 to E1.1f;
  - magnesium: E1.2 to E1.2e;
  - plastics: E1.8b to E1.8d;
  - fibre composites: E1.9b and E1.9c.

  The recipes of the other materials will be added to the same workbook; 02 takes them up without a change to its
  code.

## The checks

Before drawing, 01 checks that the workbook agrees with itself and that the shared lists place everything. The
list is `CHECKS_DONE` in `01_schemas.py`:

1. Every part has a number above zero, and a minimum, mode and maximum for the mass of one unit and of all units.
2. Every minimum is at most its mode, and every mode at most its maximum.
3. For every part, the mass of all units is the number times the mass of one unit, for the minimum, the mode and
   the maximum.
4. Every row's evidence is Direct, Derived or Estimate, and its colour is the one the colour key gives that
   evidence.
5. For every category, the sum row equals the sum of the parts' masses and of their numbers.
6. For every category, the difference row equals the sum's mode minus the stated mass, in kg and as a share.
7. The last row equals the sum of the categories' sum rows.
8. The number of parts equals the number stated at the top of the sheet (68).
9. The same categories, with the same numbers and names, are in all three sheets, and every category has its
   parts, its materials and their closing rows.
10. Materials:
    - every minimum is at most its mode, and every mode at most its maximum;
    - the sum row equals the sum of the materials;
    - every share equals the material's mode over the sum's mode.
11. Materials: the unallocated row equals the parts' sum minus the materials' sum at the mode, and the stated mass
    minus the materials' sum.
12. Shared lists: every part is placed exactly once, under its own name and robot type, in a part group and body
    region of the sheet Lists. A split adds up to the part's units, and the number of motors is a whole number from
    0 to the units.
13. Shared lists: every material name is placed exactly once, in a material of the sheet Lists.
14. Shared lists: every material name marked "Split" has its pieces in the sheet Splits:
    - exactly one remainder;
    - the shares of the others in order between 0 and 1, with their largest adding up to at most 1;
    - each piece labelled E and in a material of the sheet Lists.
15. Element recipes: every compound can be read and its mass shares add up to 1; every item of a recipe sits within
    an item of the same recipe and is a compound, another recipe or a group; no name is both a compound and a recipe,
    and no recipe contains itself; the items of a group are shares with exactly one remainder, in order and leaving it
    above zero even at the bounds, or alternatives whose probabilities add up to 1; every cell has its recipe, its mass
    and its energy.
16. Battery cells: every robot type's battery row is kept or built from cells, not both; a kept row names the recipe
    its cells follow; each build's cell is in the sheet Cells, its cells in series within one cell's voltage of the pack's voltage, its cells in parallel within
    12 % of the pack's capacity, its cells at most 85 % of the packs' mass; the rest has exactly one remainder, shares
    in order, materials of the sheet Lists, and never falls below zero where it goes to a material.
17. Material recipes: every piece of a shared material that has recipes (so far aluminium, magnesium, plastics and
    fibre composites, the rest of a battery row included) has exactly one row in the sheet Rows, naming a recipe of the
    sheet Recipe, and every row names a piece that exists.
18. Robot type 1 taken apart (`data/researched/parts_taken_apart.xlsx`, EVIDENCE.md E2.8 to E2.8e): the robots of
    type 1, the Unitree G1, the AgiBot X1 and the Fourier N1 (Matthias, 2026-10-27: "Type 1 is informed by the G1, X1
    and N1"), each named in the sheet Robots and with rows of its own on the sheets Joints, Parts, Boards, Sensors and
    Constants; JointParts, Shares and SensorElements are one set for all ("We can assume, they are similar within
    given ranges"), a joint with a module mass following the joint parts of its size scaled to that mass. Checked:
    every min, mode and max in order, and every estimate (E) at least half to 1.5 times its mode, cut only at 100 % for
    a share and at 1 for a large joint's factor (Matthias, 2026-10-27: "Estimates should be larger than known
    numbers"); every label W (weighed), S (source) or E; every group of shares with exactly one remainder that never
    falls below zero; every material and body region on the shared lists; every part or component of one material, of
    shares, or computed; for each robot its joints adding up to its joint modules, each number once, its module masses
    all three or none and in order, exactly one part taking its remainder (the frame), and its own constants (mass,
    battery, cable length) there; every joint in a heat group of the sheet MagnetGrades, each group a distribution
    over known grade classes, each class once, its probabilities adding up to 1, every group the heat group of a joint;
    every sensor element of a listed sensor; every shared constant there. A file of one robot only, without the column
    Robot, and the sheet Joints with its former base grade class and scenarios, stop the reading: the old layout goes
    entirely.
19. Robot type 1 taken apart, against the sibling projects' files it reads where they lie (for every robot) (absolute paths in
    `data.vehicle_pcb_composition`, `data.vehicle_sensor_composition`, `data.data_center_element_composition`,
    `data.traction_motor_magnets`; never copied, never written): every car board category with its gold, silver,
    palladium, tin and nickel (RAWCLICVehicleElectronics, `04_VehiclePCBComposition.xlsx`); every car sensor type
    (`07_VehicleSensorComposition.xlsx`); a tantalum row (RAWCLICDataCenters, `04_DataCenterElementComposition.xlsx`,
    sheet BoardsAndComponents); every magnet grade class a heat group can draw (RAWCLICVehicleTractionMotor,
    `10_MaterialElementDefinitions.xlsx`, sheet PermanentMagnetNdFeB). A file that is not there is a fault.
20. Robot type 1 taken apart, against the workbook's sheet Taxonomy: every robot's maker height and stated mass (sheet
    Robots) inside its type's defining limits, read from the sheet (type 1: "Height: 1.20–1.45 m (defining)", "Mass:
    30–50 kg (defining)"); a type that the sheet does not have, or whose limits cannot be read, is a fault (Matthias,
    2026-10-27: "We have to see, that there is not a mixup between the different types"; on this rule the Booster T1,
    1.18 m, is not taken apart; the register keeps it in type 1, on Matthias's yes of 2026-10-29).
21. The register of every known humanoid robot (`data/researched/humanoid_register.xlsx`, sheet Robots; EVIDENCE.md E4
    to E4.11): every number once; a robot with types has one or two different robot types of the six, a robot without
    has an entry saying why (not assigned, or the same robot as an entry with types); every form known; every mass
    min, mode and max or none, in order from 0; no robot of type 1 below its lowest mass (15 kg,
    `composition.type_one_lowest_kg`); the three robots taken apart in the parts file and of type 1.
22. The register's sheet Type 1 (Matthias, 2026-10-29: "There has to be an excel sheet where all the robots of the
    different types are fully listed. For now it has to be just all for type 1."): every robot of type 1 of the sheet
    Robots, its leading or its second type, listed once and nothing else, every cell as in its row of the sheet Robots;
    its column "In the run" what 02 does with it: "drawn: its own parts" for a robot taken apart, "drawn: the parts of
    the Unitree G1, AgiBot X1 or Fourier N1, scaled to its mass" for a robot with a stated mass, "not drawn: no mass
    stated" for a robot without. A register without the sheet stops 02.

02 runs every one of these checks, and one of its own (`check_composition`): an item that follows the energy of a cell
(the NMC cell's coatings and foils) sits only in the recipe of NMC cells, used as the recipe of cells; never in a row
of the sheet Rows, nor within another recipe, where there is no cell to take the energy from. Unlike 01, 02 stops on
any fault, before anything is written.

Two numbers count as equal when they differ by at most `checks.tolerance_kg` (0.001 kg). A fault does not stop the
drawing: the faulty row is drawn in red, the fault is listed on `faults.png` and counted on the overview.

The checks test whether the workbook agrees with itself, not whether its numbers are right. That needs the sources,
report by report.

## What the schemas show

`01_schemas.py` draws into `figures/schemas/`:

- **`overview.png`**: the stages, how every mass is given, the six categories (anchor robot, number of parts and
  units, sum of the parts, stated mass, report), the faults found, what is open.
- **`categories/<n>_<name>.png`**, one page per category:
  - its definition;
  - four boxes: the anchor robot, height and mass, joints and payload, and the sum of the parts against the stated
    mass, with whether the category has a report of its own;
  - the parts list, grouped by subsystem, each part with where it sits, its number, the mass of one and of all units
    (min / mode / max), the main material, the evidence and the sources, coloured by evidence.

  The workbook does not always keep a subsystem's rows together. Category 5 has "Structure & Protection" in rows 71
  and 75 to 76, so a page groups them, in the order in which each subsystem first appears.
- **`categories/<n>_<name>_shared_lists.png`**, one page per robot type in the shared lists, so that Matthias can
  verify every placement:
  - every part with its part group, body region and motors;
  - every material with its shared material and the reason for its place;
  - bars of the kg at the mode by part group, body region and material.
- **`categories/<n>_<name>_robot.png`**, the robot type in one view:
  - **On the left, the robot.** It is drawn to its height, at the same scale on all six pages (a dotted line marks
    1.85 m, the tallest). Its outline is the shell and its dark lines are the frame. Battery, computer, sensors,
    cables and cooling sit where they are; a dot marks each joint with motors, and a ring marks joints whose motors
    the workbook places in several regions without numbers.
  - **Labels.** The part groups are labelled on the left, the body regions and what is spread over the whole body
    in the middle.
  - **On the right, its materials as bars**, all 13 in the same order and on the same kg scale on all six pages,
    each with a line from the sum of its minimums to the sum of its maximums (bounds, not a likely range).
  - **The battery as cells only** (dotted, E), from the sheet Battery cells: the bar is the middle build, its line
    the lightest to the heaviest build; a note says how the cells were counted and where the rest of the workbook's
    row went. A bar that takes part of that rest says "partly an estimate (E)". Robot types 2 and 6 say that their
    row is cells already and kept.
  - The page says when the workbook gives no height for the anchor robot (categories 3, 5, 6), so that the middle of
    the category's height range is drawn.
- **`faults.png`**: every fault in red, or "No fault found", then what was checked and what was not.

Masses are rounded to three decimals on the pages; the checks use the workbook's full values.

## What 02 draws

`02_composition.py` draws each robot type `composition.draws` times (200,000; the tests and Claude's checks use a few
thousand). The same code serves all six robot types. Matthias agreed the specification and its recommendations a to
g on 2026-10-26 (HANDOVER.md). In each draw:

1. **Each part:** the mass of all its units, one triangle on the workbook's minimum, mode and maximum (recommendation
   a: the units of a part are drawn together, as the workbook gives one range per part). Its part group takes it,
   and its body region; a part split by units gives each region its units' part.
2. **Each material row:** a triangle on its minimum, mode and maximum. A row split by the sheet Splits: each share a
   triangle, the remainder 1 minus the others.
3. **The battery as cells:** one build drawn, all builds of the robot type equally likely; the cells are their number
   times the mass of one cell. The rest, the row minus the cells, is split by the shares of the sheet Battery cells.
   A kept row is cells as it is.
4. **The elements:** each piece of a material that has a recipe, times the recipe's element shares, drawn:
   - every share a triangle, every remainder 1 minus the others;
   - every group of alternatives one state, drawn by its probabilities, never blended (the can, the TPU's soft
     segment, the epoxy);
   - a recipe drawn once in each draw and used wherever it sits in the robot type: the hard-segment share of TPU is
     one uncertain quantity, not one per row (drawing it per row would narrow the band);
   - the NMC cell's coatings and foils are their mode times f, the cell's energy per kg over the mode of the NMC
     cells, 241.5 Wh/kg (E1.7i): of the drawn build's cell, or, for a kept row, drawn from the NMC triangle 232.5 /
     241.5 / 256 Wh/kg (recommendation f; the settings `composition.nmc_wh_per_kg_min`, `_mode`, `_max`).
5. **Not allocated:** the parts minus the materials. The two are drawn independently, so it is below zero where the
   drawn materials weigh more than the drawn parts (recommendation b: allowed, and the summary gives the share of
   draws).
6. **Materials without a recipe yet** (titanium, steel, copper, magnets, electronics, ceramics, and Mixed): their kilograms are drawn; their elements are not, and the summary and the pages say so
   (recommendation c).

Each robot type has its own random numbers, from `composition.seed` and its number, so that it gives the same draws
however many robot types are drawn. Nothing is normalised.

After drawing, 02 checks every draw (`draw_faults`), and writes nothing if one fails:
- the materials and Not allocated add up to the parts, and so do the part groups and the body regions;
- the elements add up to the materials that have recipes, within 0.1 %: the compounds written as mass shares are
  rounded to five decimals, and 01 lets a compound's shares add up to 1 within 0.001;
- the cells and the rest add up to the battery row;
- nothing is below zero except Not allocated.

## What 02 writes

For each robot type, a folder `data/consolidated/<n>_<name>/` (the folder another repository reads; not in git):

| File | What it holds |
|---|---|
| `materials.npy` | kg per robot by shared material (13 columns, Not allocated included), one row per draw, float32 |
| `elements.npy` | kg per robot by element, for the materials that have recipes (every element the compounds hold, in the order of the periodic table) |
| `part_groups.npy`, `body_regions.npy` | kg per robot by part group and by body region |
| `total.npy` | the robot's mass, the sum of its parts |
| `<name>.txt` | the columns of each `.npy`, one name per line |
| `summary.xlsx`, `summary.csv` | per material and per element: the mean, the median, the 95 % interval (2.5 % and 97.5 %), the share of draws below zero, and whether the material is in the elements (Yes, Partly, No) with its kilograms that are |

Row i is the same draw in every array of a robot type, so that stock-and-flow can pair them (the format of
RAWCLICVehicleTractionMotor, recommendation e). With 200,000 draws that is 52 columns × 200,000 × 4 bytes, about
42 MB per robot type.

And a page per robot type, `figures/composition/<n>_<name>.png`: its kg by material (all of the robot, Not allocated
included) and its kg by element (only the materials that have a recipe so far). Each bar is the mean; its line spans
95 % of the draws. The numbers stand beside the bars, with three significant figures, so that a few grams of an
element are not printed as 0.

**Elements not shown.** The element pages of 02 and 03 leave out hydrogen, nitrogen, oxygen and fluorine
(`composition.elements_not_shown`; Matthias, 2026-10-29: "Hydrogene and Oxygen have to go you should know this. Same
for F, and N", as RAWCLICStockAndFlow's figures leave out nitrogen, fluorine and oxygen, and RAWCLICDataCenters'
oxygen). The draws keep them: `elements.npy` and the summary hold every element, so that the elements still add up to
the materials in every draw and stock-and-flow can read any of them. Each page says in a note which elements it leaves
out. 02 stops when the setting names a symbol that is not an element.

## Robot type 1 over its robots, in 02 (since 2026-10-28)

Matthias, 2026-10-28: "Do it for all the robots which are in type 1. Do the code and the figure!!", "Why is it in 04",
"Yes in 02 it is all type 1 in.!", and on the preview "Yes, code it in 02". The drawing of robot type 1 taken apart
moved from 04 into 02 unchanged but for the choice of robot and mass; what follows ("What 04 draws") describes that
drawing as it was built in 04, with these changes:

1. **Each draw is one of the robots of the register's sheet Type 1** (`data/researched/humanoid_register.xlsx`), all
   equally often. Matthias, 2026-10-29: "I want the all the know type 1 robots are integrated and included in the run"
   and "There has to be an excel sheet where all the robots of the different types are fully listed. For now it has to
   be just all for type 1." The sheet lists every robot of type 1 of the sheet Robots (its leading or its second type),
   with every cell of its row there and what the run does with it ("In the run"; check 22): 32 robots on 2026-10-29,
   31 drawn (3 with their own parts, 28 with the parts of the G1, X1 or N1 scaled to their mass), the PrimeBOT Q1 not
   drawn (no mass stated). The Booster T1 (1.18 m, 30 kg) is in it, on Matthias's yes of 2026-10-29. Robots lighter
   than 15 kg are not of type 1 (`composition.type_one_lowest_kg`, Matthias: "Below 15 kg not part of the type 1"; 01
   checks the register).
2. **Its mass:** a triangle on its register mass (the stated mass ± 1 kg, or its stated range). The G1, X1 and N1
   drawn as themselves take their own mass range from the parts file.
3. **Its parts:** those of the robot taken apart that it is, else those of the G1, X1 or N1, each as often; the factor
   its mass over that robot's own scales what followed the varied mass before (answer B). The varied mass between 30
   and 50 kg is gone: the register's robots give the spread between realisations.
4. **As 02 writes every robot type:** its materials (Not allocated 0, as the frame takes the rest), its elements (all
   it holds; every robot type now has the same element columns, 0 where none is drawn), its part groups and body
   regions (its ten kinds placed whole: the joints in Joint drives, the battery in Battery, the torso boards in
   Computer, the head in Sensors, the cables in Cables, the frame and shell in Frame; hips, knees, ankles in Legs,
   waist, battery and boards in Torso, arms in Arms, head in Head, cables, frame and shell in Whole body).
5. **Its pages:** a notes page, then its elements nine a page, each the histogram of one robot's total over the draws,
   median solid and mean dotted with their numbers above the panel, 95 % dashed, own scale (Matthias: "Do not repeat
   the comments on all slides have it on a separate one"; "can you better adust the hight"); hydrogen, nitrogen,
   oxygen and fluorine not shown (above, "Elements not shown"), their draws kept.

## What 04 draws (as built on 2026-10-28; its drawing now in 02, above)

`04_parts_taken_apart.py` drew robot type 1 taken apart (Matthias, 2026-10-28: "Yes, build steps 5 and 6: stage 04
and its two approved figures, tests first, tried in a sandbox with few draws"; his answers A to E in HANDOVER.md,
2026-10-28). Before drawing it makes every check 02 makes, 01's checks 18 to 20 of the data file, and its own: every
joint, part, board and sensor goes to one of the ten kinds of part of the figures, and every part is of one material,
of shares, or computed in a way the stage knows. A fault stops it before anything is written.

**Each draw** (N = `parts.draws`, 200,000 for the real run; every triangle on the data file's min, mode and max; the
counts of joints, boards and screws fixed):

1. One robot of type 1, the G1, X1 or N1, each equally likely ("Equal"), kept whole ("Real robot, varied").
2. Its own mass, a triangle on its range (sheet Constants: G1 34 / 35 / 36 kg, X1 32 / 33 / 35.3 kg, N1 38 / 39 /
   40 kg). Its varied mass, a triangle with type 1's limits from the workbook's Taxonomy (30 and 50 kg) as minimum and
   maximum and its own mass as mode (answer A). Because the three robots sit low in 30 to 50 kg, the mean robot of the
   draws is heavier than they are, about 39 kg.
3. The factor varied over own scales what follows mass (answer B, "Joints whole, as listed"): every joint with all
   inside it (its driver board and encoders too), and the parts of the kinds "Frame and shell" and "Battery pack" (the
   pack's mass and its energy). Not scaled: the boards outside the joints, the sensors, the cables and connectors, the
   fans and heat sinks, the hands and grippers.
4. The joints, kind by kind (sheet Joints). Each component of the G1's joint (sheet JointParts) is drawn once in each
   draw for each joint size and shared by all the joints of that size, as they are one design: the small one's grams
   times its spread, the large one's the small one's grams times its factor. All small joints take the spread, the
   weighed one too (an approximation that widens the band slightly). The X1's and N1's joints follow the G1's of their
   size, times their module mass, drawn for each joint kind, over the G1 joint's mass at its modes (525 g small,
   1,011.717 g large). This divides by a fixed number, not by the draw's own sum, so nothing is normalised. The
   joint's structure (housing, two end caps, output flange, two small bearings) is the explicit remainder, so that the
   joint weighs its drawn module mass; the structure is split among its components in the G1's weighed proportions at
   their modes (Matthias, 2026-10-28, "Yes, build it"; VERIFICATION.md V57, V58). Without it, the X1's joints came
   out at 0.92 to 1.11 times AgiBot's stated masses and its frame fell below zero in 0.8 % of its draws.
5. A component or part of shares (sheet Shares): each share a triangle, the remainder 1 minus the others (02's
   `shares_drawn`), drawn once in each draw.
6. The battery: the pack's mass; its cells the pack's voltage times its capacity (both times the mass factor) over the
   NMC cells' energy per kg (`composition.nmc_wh_per_kg_*`); its housing the pack less its cells and its management
   board, a remainder. The cables: their length times two power and two signal conductors' cross-sections times
   copper's density, and their insulation as a share of that copper. The frame: the varied mass less every other part,
   a remainder.
7. A remainder below zero (a frame, a battery housing, a joint's structure) is reported (share of its robot's draws),
   never cut.

**The elements:**
- Aluminium and plastics by the recipes type 1's workbook rows follow ('Aluminium, robot type 1, Aluminum alloys';
  'Plastics, robot type 1, Engineering polymers'), the battery cells by 'NMC cylindrical' with its energy per kg drawn
  (02's `RecipeDraws`, each recipe drawn once in each draw); copper is copper.
- The magnets by heat (Matthias, 2026-10-28: "Heat has to matter and so the distribution will be different depending
  on the joint", "Accept as proposed"; EVIDENCE.md E2.11): every joint in a heat group (sheet Joints), each group a
  distribution over grade classes (sheet MagnetGrades: knees SH 0.3 / UH 0.5 / EH 0.2, hips SH 0.5 / UH 0.4 / EH 0.1,
  waist and ankles SH 0.6 / UH 0.4, shoulders H 0.5 / SH 0.5, elbows and wrists H 0.7 / SH 0.3; estimates on the
  order of heat the sources give, every joint judged as passively cooled). In each draw one draw of heat, from 0 to
  1, decides how hot the robot is built for, and every group takes the class at that point of its cumulative
  probabilities (classes in the order of the heat they stand): the classes are tied within a draw, so that the hot
  cases do not average out. The class is a discrete state, never blended. Its element fractions from
  RAWCLICVehicleTractionMotor's own `magnet_element_draws`, run in that project's own environment where it lies
  (answer C). It does not normalise: Nd, Pr, Dy, Tb and the trace elements are drawn uniform between the class's
  bounds, iron is their remainder. Its seed is its own.
- Boards: copper their mass times the copper share of a board (Bizzo et al. 2014, sheet Constants); gold, silver,
  palladium, tin and nickel their area times the car board category's mg per cm2 (RAWCLICVehicleElectronics `04_`);
  tantalum their mass times the data centres' share (RAWCLICDataCenters `04_`). A board's mass is its area times the
  board mass per cm2, except the joints' driver boards, whose mass is their JointParts component.
- Sensors: their car sensor elements (RAWCLICVehicleElectronics `07_`) times their units; the encoders, two per joint,
  by their elements only (their mass is inside the joint's components).
- Steel, titanium, the mixed parts (grippers, battery housing) have no recipe: their kilograms are drawn, not their
  elements.

**What it writes**, into `data/parts_taken_apart/` (answer D; not in git): `robots.npy` (the robot of each draw, its own
and its varied mass), `parts.npy` (every joint kind, part, board and sensor of every robot, kg; 0 in the draws of the
other robots), `materials.npy` (every material in every kind of part), `elements.npy` (every element in every kind of
part), each float32 with its columns in a `.txt`, row i the same draw in every file; and `summary.csv`.

**Its figures**, into `figures/parts_taken_apart/`, on pages of a screen's shape (Matthias, 2026-10-28: "Have the
overview on several pages. I can not read it. too smal, you should notice this before you sjhow me. Elements is an
edge case. Also quite small"): 16 × 9 inches, no text below 14 points, so that fit to a 1920 × 1080 screen the
smallest text is about 23 pixels tall; `tests/test_parts_taken_apart.py` draws every page and fails below 18. On every
page the centre of a distribution is its median, a solid line, and its mean, a dotted one, each with its number
(Matthias, 2026-10-28: "Showing the mean is wrong. It is not a good measure. Use the median or show boths"; his answer
"Both, median first"); the 2.5th and 97.5th percentile dashed.
- `robot_type_1_elements_1.png` and `_2.png`, the element figure Matthias approved ("Yes, the element figure is right
  now", V49), for the three robots: one panel per element, three across (page 1 copper, aluminium, silver, gold,
  palladium, tantalum; page 2 neodymium and praseodymium, dysprosium, gallium, indium); in each the histogram of the
  robot's total over the draws (70 bars, the height the share of the draws), each bar split into the kg its draws hold
  in each kind of part, the kind with the smaller mean lower; each panel its own scale and unit; one legend at the top
  in Paul Tol's discrete rainbow (frame and battery swapped).
- `robot_type_1_overview_1.png` to `_5.png`, the overview Matthias approved ("Looks good to me", 2026-10-27), for three
  robots (answer E, "Groups, histograms"), two elements a page in the same order: left the robot (01's body shapes)
  with its joint groups numbered on both sides (a red ring where their magnets are for 150 °C) and its other kinds
  lettered, a short key below; right the two elements one above the other, one row per kind of part holding it,
  labelled with its mark on the robot ("1  Hip joints", "A  Battery pack"), each row a histogram of its kg scaled to
  the row, the median and the mean in two columns of numbers at the right, hatched where more than half the mean rests
  on parts whose mass is an estimate (label E).

In both, a kind of part holding an element in fewer than 2.5 % of the draws is not drawn.

## What 03 draws

`03_comparison.py` reads what 02 wrote, as it is, and draws nothing at random itself (point 15 of the specification).
It first checks that the files belong together: every robot type with every table, the same number of draws, the same
columns in the same order, and its materials, part groups and body regions adding up to its total in every draw.

It draws one page per view into `figures/comparison/`: `materials.png`, `elements.png`, `part_groups.png`,
`body_regions.png`. Each holds one small chart per material (element, part group, body region) with one row per robot
type: the mean as a bar, a line over 95 % of the draws, and the mean written beside it. Each chart has its own kg
scale, so that a material of a few grams can be read as well as one of 25 kg. Matthias, 2026-10-26: "I want that it
is possible to compare on a material level between the 6 types of roboy". `elements.png` leaves out hydrogen, nitrogen,
oxygen and fluorine, with 02's function and setting ("Elements not shown", above).
