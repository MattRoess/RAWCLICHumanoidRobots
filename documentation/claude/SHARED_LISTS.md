# Shared lists of parts, body regions and materials

**Status:**
- Decided by Matthias on 2026-10-26, point by point (see "Decided" below), including the estimate of point 9.
- The placements are in `data/researched/shared_lists.xlsx`, which `01_schemas.py` reads and checks.

Written by Claude on Matthias's
words "draft the shared lists of parts and materials, with where each of the 68 parts and 35 material names goes, for
me to check", "But whats about legs etc." and "Whats about addining more degree of freedome, which means additional
electrical motors".

## Why shared lists

The research describes each of the six robot types in its own words, like six recipes from six cooks. One writes
"flour", another "wheat flour", a third "plain flour". To compare the six robots, every robot needs to be written
with the same words. This draft proposes those words: a few shared lists, with each of the workbook's names placed on
exactly one of them.

## Four ways to look at a robot

| View | The question it answers | Draft |
|---|---|---|
| Part groups | What is it? A motor, a battery, the frame... | 11 groups |
| Body regions | Where does it sit? Legs, arms, torso... | 6 regions |
| Materials | What is it made of? Aluminium, steel, copper... | 13 materials |
| Motors | How many electric motors move the robot? | one count per robot |

Elements (the periodic table: Al, Fe, Cu, Nd, Li, Co...) come later, from the materials. Each material gets a recipe
of its elements from sources, and nothing is entered before Matthias agrees.

**Parts and materials stay two separate views.** The workbook describes each robot once by parts and once by
materials. It says which part is made of which material only in words, so the two cannot be joined without
estimates.

## List 1: part groups

| Part group | What it holds |
|---|---|
| Joint drives | The electric motors that move the joints, with their gearboxes. Some robots list motor and gearbox as one part, others as two; together they compare fairly. |
| Hands | Hand assemblies, with their small motors inside. |
| Battery | The battery packs. |
| Computer | Computers and controllers. |
| Sensors | Cameras, LiDAR, microphones, force sensors. |
| Frame | The skeleton that carries the load. |
| Shell and armour | Covers, panels, padding, armour. |
| Cables | Wiring, connectors, power distribution. |
| Cooling | Fans, heat pipes, cooling loops. |
| Screws and bearings | Fasteners, pins, structural bearings. |
| Mixed | A part the workbook lists as two groups in one (e.g. "wiring and thermal management"). |

## List 2: body regions

| Body region | What it holds |
|---|---|
| Legs | Hips, knees, ankles. |
| Arms | Shoulders, elbows, wrists. |
| Hands | The hands. |
| Torso | Waist, chest, the battery and computer bays. |
| Head | Head and neck. |
| Whole body | Parts spread over the body (frame, shell, cables), and parts the workbook places in several regions without saying how many sit where. |

**The rule.** A part goes to the region the workbook's "Location / Joint" column names. A part placed in several
regions is split only where the workbook gives the number of units in each, using its own mass per unit. That
happens three times; for example, category 1's "Ankles (2 DoF × 2) & shoulders (3 DoF × 2)" gives 4 leg and 6 arm
modules. Every other part placed in several regions goes to "Whole body". No number is invented.

## List 3: materials

| Material | What it holds |
|---|---|
| Aluminium | Aluminium alloys. |
| Magnesium | Magnesium alloys. |
| Titanium | Titanium alloys. |
| Steel | Every steel: bearing, gear, structural, fastener and electrical steel. |
| Copper | Copper wire, windings and busbars. |
| Magnets (NdFeB) | The permanent magnets of the motors. |
| Battery materials | The materials of the battery cells (NMC, LFP and solid-state, as each robot states). |
| Plastics | Plastics and rubbers, including fibre-reinforced plastics the workbook calls polymers (CF-PEEK, PA66-GF) and ballistic fibres (Kevlar, Spectra). |
| Fibre composites | What the workbook calls composites: CFRP and GFRP. |
| Electronics | Circuit boards, chips, glass of screens and optics. |
| Ceramics | Armour ceramics. |
| Mixed | A workbook name that holds several materials in one (e.g. "copper / electronics / NdFeB"). |
| Not allocated | The kilograms the workbook's materials leave out: its parts list is heavier than its material list in categories 3, 5 and 6. |

## The six robots with these lists

`01_schemas.py` draws, for each robot type, its parts with their part group and body region, its
materials with their shared material, and bars of the kg at the mode by part group, body region and
material: `figures/schemas/categories/<n>_<name>_shared_lists.png`. It also draws the robot in one view,
its parts where they sit and its materials as layers: `figures/schemas/categories/<n>_<name>_robot.png`.
The numbers are drawn from the workbook every time 01 runs, so they cannot drift from it.

## Motors and degrees of freedom

A **degree of freedom** is one way a joint can move. A knee has one (bend), a shoulder has three (forward, sideways,
twist). In the body, one motor usually moves one degree of freedom. Hands often have fewer motors than degrees of
freedom, because cords link several finger joints to one motor. **More degrees of freedom therefore mean more
motors, and more motors mean more copper, magnets and steel.**

| Robot type | Degrees of freedom in the definition (sheet `Taxonomy`) | Motors outside the hands in the parts list | Hands in the parts list |
|---|---|---:|---|
| 1 | 23–43 (G1, depending on the version); 28–34 for comparable robots | 23 | none |
| 2 | at least 30; 50–75 including hands; H2: 31 + 22 per hand | 31 | 2 hands, 22 degrees of freedom each |
| 3 | Walker S2: 52 | 52 | inside the 22 small motors ("dexterous hand joints") |
| 4 | A2: 40+ (30 body motors + 19-degree hands) | 30 | 2 hands, 19 degrees of freedom |
| 5 | Atlas: 56; T800 Max: 46 | 28 | 2 hands |
| 6 | Guardian-X: 14 body motors (notional) | 14 | none (the definition names 6-degree hands of the Fuxi) |

The workbook fixes the number of motors of each robot at one value, while the definitions allow a range. For
category 1, that is 23 to 43. The number of motors could become a range too: minimum, most likely and maximum. Each
extra motor would then add the mass of one joint drive. This needs three things the workbook does not give:
1. the range of motors per category, from the definitions and the comparable robots;
2. which size of motor the extra ones are (G1's extra degrees of freedom are mainly in wrists, waist and hands, so
   small motors);
3. how much copper, magnet, steel and aluminium one motor holds, from sources.

## Decided, 2026-10-26

Matthias went through the eleven points one by one ("Let's go through the 11 points to check in SHARED_LISTS.md one
by one") and chose the recommended answer each time.

1. **Gearboxes go with the motors in "Joint drives".** Rows 35 (robot 2), 44 (robot 3) and 84 (robot 6) are separate
   gearbox rows; they join the motors, so all six robots compare the same way.
2. **Hands are shown as the workbook has them.** Robots 2, 4 and 5 list hands. Robot 3's hands are inside its small
   motors (row 43), and robots 1 and 6 list none. Every comparison of hands notes that robots 1, 3 and 6 are not
   comparable for hands.
3. **The three mixed parts stay "Mixed":**
   - robot 3 row 51, cooling with screws, 1.5 kg;
   - robot 5 row 73, computer with sensors, 3 kg;
   - robot 5 row 74, cables with cooling, 5 kg.

   No number is invented. Robot 5 therefore shows no computer, sensors, cables or cooling of its own.
4. **Robot 4 row 62**, "Exterior shell, soft coating and interaction head screen", goes to Shell and armour; its face
   display is counted as shell.
5. **"Whole body" is kept for now:** 39 % of the mass in robot 1, 54 % in 2, 72 % in 3, 54 % in 4, 83 % in 5 and
   69 % in 6. Body regions are compared only as far as the workbook allows. A better split can follow later as its
   own step: the motors by each robot's joint layout from its specifications, and the frame and shell with
   estimates.
6. **Robot 3 row 41**, "Hips, knees & primary load-bearing joints", goes to Legs.
7. **The materials are named as the workbook names them.** CF-PEEK, PA66-GF, Kevlar and Spectra go to Plastics;
   CFRP and GFRP go to Fibre composites.
8. **Electrical steel** (robot 5, motor laminations) goes to Steel, and **electrical conductors** (robot 4, copper
   with silver solder) go to Copper, so no robot looks as if it had none.
9. **Robot 3's "Electrical & magnetics group"** (4.2 kg: copper, electronics, NdFeB magnets, circuit boards) **is
   split by estimate** into copper, magnets and electronics. Kept as "Mixed", it would make robot 3 show no copper
   and no magnets despite its 52 motors.
   Decided on 2026-10-26, after the basis was shown: "Robots 2, 4 and 5", "Copper as the remainder", "A sheet
   'Splits' in shared_lists.xlsx". Robot 3's own report says the workbook "supports only their combined mass", so
   this is purely an estimate (E):
   - **The shares** come from the full-size robots that exist, robot types 2, 4 and 5. Each is the share in copper,
     magnets and electronics together, at the mode: the smallest, the middle and the largest of the three.
     - Magnets: 15.5 % (5), 30.0 % (2), 30.1 % (4).
     - Electronics: 12.0 % (4), 20.0 % (2), 24.6 % (5).
     - Robot 1 is much smaller and robot 6 notional, so they are not representative.
   - **Copper is the remainder**, 1 minus the other two (45.3 / 50 / 72.5 %). The three pieces add back to the
     group's 3.5 / 4.2 / 5 kg, with no normalising.
   - **At the mode:** copper 2.1 kg, magnets 1.26 kg, electronics 0.84 kg.
   - **Found while proposing it:** for 52 motors the 4.2 kg is light. The other full-size robots hold 5–11 % of their
     joint drives' mass in magnets, which would mean 1.7–3.4 kg of magnets alone in robot 3. Part of its copper and
     magnets may therefore sit in its 7.4 kg "Not allocated". Its report says that gap "should not be distributed
     proportionally without additional information", so the estimate splits only the 4.2 kg.
10. **"Not allocated" is shown** as its own bar in every comparison of materials: 7.4, 18.4 and 17.6 kg at the mode in
    robots 3, 5 and 6. Nothing is rescaled.
11. **The number of motors stays fixed for now**, as the workbook gives it, and is shown beside each robot: 23, 31,
    52, 30, 28 and 14 outside the hands. A range of motors follows later as its own step. It needs research on the
    ranges, the motor sizes and what one motor is made of.

## Where every part and material name goes

In `data/researched/shared_lists.xlsx`. Since 2026-10-26 it is the one place that holds the placements;
the code reads it, and Matthias corrects it in Excel. Its sheets:
- **Lists:** the shared part groups, body regions and materials.
- **Parts:** one row per part, with its part group, body region or split by units, motors and why.
- **Materials:** one row per material name, with its shared material and why. A name split by an estimate says
  "Split".
- **Splits:** the pieces of a split name, each with its share (min / mode / max), the remainder, the label E, the
  basis and the decision.

`01_schemas.py` checks every placement (see METHODOLOGY.md, "The checks").

## How the draft was checked

A script placed every part and every material name, and stopped on any one missing or placed twice. All 68 parts
and all 35 names are placed exactly once. For each of the six robots, the part groups, the body regions and the
materials with "Not allocated" each add up to the mode of the robot's parts list. The three splits by number of
units add up to the units of their row.
