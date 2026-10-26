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
| `01_schemas.py` | `data/raw/humanoid_robots_2040_workbook.xlsx`, `data/researched/shared_lists.xlsx`, `data/researched/element_recipes.xlsx`, `documentation/sources/` | `figures/schemas/` | Reads the six categories, their parts lists and their materials, and where each goes in the shared lists; reads the element recipes and counts each robot type's battery cells. Checks that the workbook agrees with itself, that everything is placed, and that the recipes and the battery cells hold together. Draws what the workbook defines, each robot type in the shared lists, and each robot type in one view. Nothing is drawn at random. |

**Next, not built yet:** one stage per category, computing what its robots are made of. Matthias, 2026-10-26: "we
will go through and do separate code for each of the different categories". Those stages will read the workbook
through the functions of 01 (`read_workbook`, `check_workbook`), so that what they compute is what the schemas show.

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
  - **Kept** (robot types 2 and 6): the workbook's row is cells already and stays.
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
    CFRP, GFRP); and each robot type's plastics row and robot type 3's composites row, split among what they name.
    An item is a compound,
    a group, or another recipe (PA66-GF holds E-glass). A group's items are shares with exactly one remainder, so
    nothing is normalised, or alternatives drawn by their probability (the can: nickel-plated or stainless steel; the
    TPU's soft segment: polyester or polyether, half and half).
  - **Rows:** which recipe each row of the workbook follows, for every shared material that has recipes; so far
    plastics, including robot type 1's battery pack enclosure (plain PC/ABS), and fibre composites.

  The plastics recipe and its sources are in [EVIDENCE.md](EVIDENCE.md), E1.8b to E1.8d; the fibre composites in
  E1.9b and E1.9c. The recipes of the other
  materials will be added to the same workbook. No stage draws element masses yet: that comes with the Monte Carlo
  stages.

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
16. Battery cells: every robot type's battery row is kept or built from cells, not both; each build's cell is in the
    sheet Cells, its cells in series within one cell's voltage of the pack's voltage, its cells in parallel within
    12 % of the pack's capacity, its cells at most 85 % of the packs' mass; the rest has exactly one remainder, shares
    in order, materials of the sheet Lists, and never falls below zero where it goes to a material.
17. Material recipes: every piece of a shared material that has recipes (so far plastics and fibre composites, the
    rest of a battery row included) has exactly one row in the sheet Rows, naming a recipe of the sheet Recipe, and every row names a piece
    that exists.

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
