# Verification and validation

Every check made on this project: what, how, against what, the result, the date, and what it does not cover. Written
by Claude, newest first. The first section says what verification and validation mean here and how each is done; the
entries V1 to V222 below it are the checks themselves.

## What verification and validation mean, and how they are done here (2026-11-08)

Matthias, 2026-11-08: "I want a full verification and validation report, where you also define what this means and how
you have implemented it according to the meaning. I also mean correct results!!!"

### The meaning

- **Verification** answers: *does the code compute what the model, as written down, says?* The model is written down in
  METHODOLOGY.md, EVIDENCE.md, the schemas of 01 and the code's comments. A verified number is the number the written
  method gives for the given inputs, with no error of the code in between. Verification says nothing about whether the
  inputs or the method describe real robots.
- **Validation** answers: *do the model's results describe the real robots, and the real numbers of robots in the world,
  well enough for what the model is for* (the materials and elements in humanoid robots, in one robot and in all robots
  in use 2025 to 2040, as a basis for recycling)? A result is validated when it agrees, within its uncertainty, with
  independent data that did not go into it: a maker's stated mass, a teardown's weighing, a published composition, a
  world statistic. A comparison with the model's own input validates nothing (GitHub/CLAUDE.md §3: "A cross-check that
  stops at the input does not validate the model").
- **Correct results**, as he asks for them, are results that are verified, and validated wherever independent data
  exist. Where no independent data exist, a result rests on its sources (EVIDENCE.md, a source table before every min,
  mode and max) and carries its uncertainty (min, mode and max on every input, 95 % of the draws on every result). This
  report then says so plainly: *not validated, rests on its sources*.

### How verification is done (what each method is, and where)

| # | Method | What it proves | Where |
|---|---|---|---|
| V-1 | **Tests first, seen to fail, then passing** | that the code does what the specification says, case by case, and that the test can fail | `tests/` (649+ tests); each entry below names its tests and that they failed before the change |
| V-2 | **Hand calculations** | that a result equals the same number worked out independently from the inputs, draw by draw (e.g. the neodymium in a joint's magnets = the magnets' kg × the neodymium share; the small PCBs' copper in use = joint sets × 0.2 kg + packs × 0.1 kg) | in the tests; each entry below says which |
| V-3 | **Deliberate faults** (mutations) | that the tests see the kind of error they are meant to see: a fault is put into a scratch copy of the code (a wrong lifetime, a part booked to the next part, a percentile at 5 and 95 instead of 2.5 and 97.5 …), and the tests must fail. A fault the tests do not catch gets a new test | scratch copies, never the project; each entry lists every fault and what caught it |
| V-4 | **Checks built into the code that stop the run** | that what must add up does add up in every draw of every run, also at 200,000 draws: 02 the materials to the robot's mass, the elements by material, by place and by part to the elements, the mass by part to each kind, each material's elements to its kilograms whose elements are drawn (since V224; before, that check compared the elements with themselves); 03 the same once more on what 02 wrote; 04 the stock balance in every quarter, the article's robots at every year end, the joint sets as many as the robots, the packs never fewer than needed | `02_composition.py` `draw_faults`, `check_taken`; `03_comparison.py` `problems`; `04_stock_and_flow.py` `check`; 01's checks of every input (faults pages) |
| V-5 | **Each stage checks the one before** | that what a stage reads is what the stage before wrote and belongs together | 03 reads 02's tables and stops on any miss; 04 stops on a column of 02 that is no kind, part and element |
| V-6 | **Regenerated data compared cell by cell** | that a regenerated input file changes only where it should | the parts files against their builders (`scratchpad/builders/compare.py`); the tests compare each builder with its file on disk |
| V-7 | **Every page checked as it is saved, and looked at** | his figure rules: no text beyond the page or its panel, no text over data, text 14 pt and up (02, 03; 04's A4 pages as 07's), no project words, no legend over a line; and by eye: what each page shows and whether its numbers make sense | `tests/test_comparison.py` `page_problems`; the sandbox runs (below); each entry names the pages looked at |
| V-8 | **Documents drawn from the code's own lists, tested** | that the schemas and the overview say what the code does: the page of how a robot is taken apart is drawn from `TAKEN_APART`, the overview's stages from `STAGES` | `tests/test_schemas.py` |
| V-9 | **The whole suite after every change; the chain in a sandbox** | that nothing else broke; that 01 → 02 → 03 → 04 run together on the project's own inputs at 2,000 draws, into scratch folders, every page checked (V-7) | the entries below; never against `data/` or `figures/`, never 200,000 draws (his runs) |

### How validation is done

| # | Method | What it proves | Where |
|---|---|---|---|
| A-1 | **Every input from representative sources**, each questioned (measured, a design value or a claim; first-hand or second-hand) and shown in a source table before its min, mode and max are entered | that the inputs describe the kind of thing they are used for (GitHub/CLAUDE.md §8) | EVIDENCE.md, an entry per input |
| A-2 | **Results against independent data** | that the results describe the real robots: a result compared with data that did not go into it | the table "What is validated" below |
| A-3 | **Uncertainty carried to the result** | that a result shows how well it is known: min, mode and max on every input, never a single number; 95 % of the draws on every result; a 0 not part of a distribution | METHODOLOGY.md; every page |
| A-4 | **Order of magnitude and sense, by eye** | that no result is absurd: each new result looked at, traced to its inputs where it surprises (e.g. V222: 617 g of aluminium in the gears of a type 1 robot, traced to the second gear stage's carrier, 12.5 to 40 % aluminium in the parts file) | each entry below |

### What is validated: every result compared with independent data (as of 2026-11-08)

Collected from V1 to V221 and EVIDENCE.md, and the comparison of 2026-11-08 (V222, rows A11 to A13). "Independent" means
the data did not go into that result.

| # | Result of the model | Against | The numbers | Verdict | Where |
|---|---|---|---|---|---|
| A1 | the G1's large joint, from its small joint's parts and size factors | T1 (teardown, weighed) 1,100 g; T3k (second-hand) 1,085 g | draws 912 / 1,034 / 1,158 g, mean 6 % under T1 | within its range; nothing scaled to meet it. Partly the same sources (T1's small joint, T3k's dimensions); on the proposal's scratch run, not on 02's | V45, E2.8 |
| A2 | type 1's joint mass from torque (fitted on AgiBot's three) | the G1's weighed joints (T1) | small 0.525 kg vs 0.50–0.58 from the fit; large 1.1 vs 0.87–1.07 | close; not used to fit | E2.8e |
| A3 | type 1's fit at 360 N·m | Unitree M107, maker's 1.9 kg | 1.62 kg, 15 % below | a check only (the M107 then went into type 2's fit) | E6.7 |
| A4 | type 2's joint-mass fit (12 makers) | the G1's weighed joints (T1) | small 0.525 vs 0.426–0.515; large 1.1 vs 0.868–1.124 | close; not used to fit | V83, E6.8 |
| A5 | type 2's fit | 8 makers' modules found later (Lumos, MagicLab) | mass / fit 0.60 to 1.38 | all inside half to 1.5 times | V86, V87, E7.2 |
| A6 | type 2's joint template on the JingChu | JCBOT's stated knee 2 kg | 1.85 kg (0.92) | close; the stated value then entered | V88 |
| A7 | the RP1's cable copper at the model's min / mode / max | RoboParty's own harness list and drawings | maker 171–375 g (about 12 m); model 52 / 170 / 406 g (10 m) | within the model's range; at its min / mode / max, not on its draws | V150, E22.1 |
| A8 | the G1's frame, shell, harness, fasteners, cooling together | U3, Unitree's design file, link masses (approximate reading) | 14.9 kg vs about 13 kg | totals agree; the split does not | V45, E2.8 |
| A9 | the G1's materials in the proposal | his workbook's estimates (not measured) | aluminium 12.2 vs 12 kg agrees; copper 1.2–1.9 vs 3–4.5 kg; cables a third; fasteners a quarter; cooling a sixth | not independent measured data: an estimate against an estimate | V45, V149, E2.8 |
| A10 | 04's element inflow and stock (his run of 2026-11-06) | world mine production 2025 and reserves (RAWCLICDataCenters' ElementReference, USGS MCS 2026) | inflow above a year's world production from 2033 (Nd, Pr) to 2039 (B, Ag, Au, Nb); stock above reserves from 2039 (Nd) | a comparison of scale, driven by the article's robots (an input); not repeated since V210 | V209 |
| A11 | dysprosium in one robot, each type (02, sandbox of V222, 2,000 draws) | "analysts: 35–79 g dysprosium per humanoid" (Humanoid.guide, an industry article, no robot named) | medians type 1 57 g, 2 75, 3 83, 4 64, 5 101, 6 90; 95 % from 7 to 237 g | type 1 inside; types 2 to 6 at or above the top of the range, every 95 % overlapping it. The source is second-hand and names no mass of robot: weak | V222 |
| A12 | NdFeB magnets in one robot, each type | "Optimus about 3.5 kg NdFeB" (Aibang Robotics, a Chinese industry article, a claim) | medians 1.0 (type 1), 1.4, 1.5, 1.2, 1.8, 1.6 kg; 97.5 % 1.9 to 3.8 kg | **the model about half the claim**; 3.5 kg only in the top of types 2, 3, 5's draws. Reported, not changed; a claim, second-hand | V222 |
| A13 | copper in one robot, per 60 kg of robot | CRU via rehack.com: "4-8 kg of copper for actuators and wiring" in a robot of about 60 kg (a search result, not read; second-hand of second-hand) | medians 3.3 (type 1), 2.4, 2.3, 2.5, 2.8, 2.1 kg; 97.5 % 3.9 to 4.7 kg | **the model below the range** (by 1.5 to 2.5 times at the medians). Reported, not changed; the weakest of sources | V222 |

**Compared with inputs only** (these validate no result, they verify): the G1's small joint against T1's own parts
(V45); its battery 421 Wh against T1's 0.42 kWh (V45); the sandbox's elements against the project's own earlier G1
figures (V53); joints against the makers' module masses they are built from (V57, V58, V144); type 2's template against
type 1's (V87); every result's mean against its triangle's (V32, V44, V213); the robots in use against the article's
(V216). Inputs against outside sources (A-1, not results): the recipes (V14: aluminium 6061 and 7075 exactly; magnets
not confirmed, Co 4–12 % against 5 %; board copper 2.5–7.4 % against 14.2 % measured, then replaced by Bizzo's), the
magnets (V15), the cells (V16, V19), gallium (V192, V194), the boards (E2.8b), the rotor's magnet share (E2.10), the
workbook's LiDAR (V45), the makers' model files (V95, E5), the runtimes (E39); and the article's robots against
humanoid forecasts (E40, E41: 250 times the humanoids shipped in 2025), which he decided: "Use the numbers in the
article".

**Not validated, rests on its sources** (no independent data found, or none compared):
- the elements of one robot of every type beyond A11 to A13 (lithium, cobalt, nickel, gold, silver, palladium,
  gallium, indium, tantalum, terbium …): no independent per-robot data found;
- types 2 to 6 have no teardown ("T1 is the only first-hand teardown with masses", E2.8); most of their element kg
  rests on parts labelled E (V187: copper 78 to 98 %, Nd+Pr 76 to 98 %, gold 77 to 96 %, by type);
- the boards' areas and metals (no measured area of a robot's main board; the car and data-centre data 20 times apart on
  copper per cm², E2.8b); the boards' layers and the large capacitors at the joint motors (in the model since E51, V223:
  their inputs from makers' declarations and drivers, no independent figure of a humanoid's capacitors found); the
  layers check finds the measured copper above what a thin board's layers hold (V223);
- the magnets' grade by joint, gallium by grade, the stator's copper share (E2.10);
- the cables of any robot but the RP1 (V150);
- the housings of the 304 packs no source weighs (E20);
- 04: the robots in use are the article's, with no band; no humanoid maker publishes a joint life, none a lifetime in
  years (V205, V212); collection and charging efficiency not built (E46);
- 03 compares the types only with each other.

**What this means for correct results.** Every result is verified: the code computes what the documents say, the
totals add up in every draw, the tests see the errors they are meant to see (V-1 to V-9). Validated against independent
data are some masses of one robot (A1 to A8) and, weakly, the dysprosium (A11). Two outside figures, both second-hand
claims, are higher than the model: NdFeB about twice (A12), copper 1.5 to 2.5 times (A13). Whether the model is low or
the claims are high cannot be settled with them; it needs a first-hand source (a teardown of a second robot, a maker's
material declaration). Until then the elements of one robot are **not validated**; they rest on their sources and their
95 % ranges.


## 2026-11-13

### V228. Every figure checked by the shared figure tests (FigureTests 0.5.0); what they found, fixed (his "Yes, 1 to 7")

Matthias, 2026-11-13: "There is now the package for figure testing. I want that you intergate the new results with the
robots and als test all the figures", "Yes, 1 to 7"; on the way "Do not label every point!!!", "the y axis scales are
shit", "I want B", "Yes, build the three rules as proposed", "Yes, both", and on the robot and overview pages "These two
figures look ugly. The different text are much to close. It looks overloaded", "Yes, all".

- **The check.** `tests/test_all_figures.py` (new): FigureTests' proofs (every rule caught on a figure drawn with its
  fault, passed without it), the version installed against the pin of `requirements.txt` (0.5.0; installed from
  FigureTests' folder until its tag v0.5.0 is pushed, on his word), and every numbered stage 01 to 05 run as by pressing
  Run with 200 runs of each robot type on his workbooks, every output folder in a temporary folder, every figure checked
  at the moment it is saved. This project's settings: the robots' and makers' names written together, read from his
  register and workbook (proper names, not code names); the schema pages in `figures/schemas/`; the jargon "inflow",
  "outflow", "Plan A"; the notes pages as pages of text (`_notes_<k>.png`: no foot of three sentences to keep).
- **First run** (before any change, the rules of 0.4.1): 01 148, 02 1,108, 03 309, 04 8, 05 0 faults (after the
  colour rules of 0.5.0). **Each kind, and what was done:**
  - *Words:* "draws", "mean", "percentile", "inflow" and an underscore on pages → "model runs", "median", "95 %
    interval", plain words (01, 02, 03, 05).
  - *Means:* every page, table and number at the median (02's means pages became the medians pages `_medians_`; the
    lists' columns: held in, median, middle half, 95 %).
  - *Legends:* every distribution page names its median and 95 % interval (02, 03, 04, 05).
  - *The same number beside every point* (04: "12 %" at each of 16 years) → written once per line, where it changes;
    the new rule repeated_label (FigureTests).
  - *Axes:* 04's and 05's mass axes in powers of ten again (written-out numbers took a third of each panel).
  - *Colours* (the rules colour_blind, colour_normal, text_contrast): 04's and 05's types and quantities in nine new
    colours told apart under both rules; 01's robot drawings and 02's overview rows each kind in its group's colour (four
    colours, every pair at least 34.3 apart, 15.5 colour blind); 02's parts element pages removed (point A below); 03's
    mass page six main materials and the rest grey (point B); 03's material pages by group (point C); the cameras' blue
    on the element pages (#0077BB, at least 25.2 from every other material colour, 22.9 colour blind); 01's overview the
    sibling projects' olive (#AAAA00, 22.9 from every other box colour, 21.1 colour blind); 03's body regions the head
    orange (#EE8026, 26.0 and 11.6); each mark's letter white or dark by its contrast.
  - *Crowded texts* (the new rule text_gap of FigureTests 0.5.0, two separate texts at least half the larger font size
    apart): with the rule, 01 396, 02 830, 03 145 places, before any change. 02's overview rows 0.42 inches each, one
    text height between two labels (they stood 5.3 to 9.4 pt apart, ink to ink, measured on his type 2 page), an
    element whose rows a page cannot hold in two panels on the same scale, the legend below the panels; 01's robot page
    the robot, its marks and the four groups, one line a kind, what each holds on a page of its own
    (`_kinds_of_part.png`); the panels of 02's and 03's pages 14 pt apart (4 before), their mass numbers 9 pt below the
    axis and their titles 10 pt above it (the share axis's "0" stood 2 to 7 pt from the first mass, "0.8"); 01's box
    titles and list items further from their text; the robot tables' height and joints columns moved. The rule does not
    catch 01's robot page as it was (its rows 14.6 pt apart): what crowded it was the amount of text, now on its own
    page.
- **Point A** (his "Yes, all"): split by the four groups, 02's parts element pages would repeat 02's pages by group:
  on the sandbox's runs the group medians of each critical element from the places and from the parts agree to within
  1 % (the largest difference in a single run, 19 % of a group's largest run, the aluminium of the electronics, where a
  joint's fan is a place's and a PCB's part). Removed: `element_pages`, `element_page`, `stacked_panel`, `place_view`,
  `place_colour`, `ELEMENT_PANELS`, their tests; the parts folder's series 'elements' and 'numbers'.
- **Point B:** the six materials with the largest medians of his run of 2026-11-08, added over the six types
  (`data/consolidated/<type>/materials.npy`): aluminium alloys 186.0 kg, steel 71.8, plastics 57.9, battery cells 22.9,
  electrical steel 16.8, copper 12.1 (then boards and components 10.5, NdFeB magnets 8.5). Steel, plastics and
  electrical steel in Tol's blue, ochre and light cyan: of 25 published colours used by no other material, the three
  whose closest pair with copper's, aluminium's and the cells' colours stands furthest (18 % above both thresholds),
  each at least 4.5 : 1 against the black median line. 03 prints when a run's six differ.
- **Point C:** each material of 03 by the group of the kind of part it sits in (01's KIND_GROUP, the kinds placed whole,
  as the part groups of 03 already were).
- **The data centres' stage:** 07 until 2026-11-12, 08 since; its file, its scenarios A, B, C and its 20 elements' columns
  the same (read 2026-11-13: the header, the first and last rows). The copy tool's own function run on 08's file into a
  scratch folder: 57 s, every scenario, run and year of 2025 to 2040 written exactly once (its own check), the first 167
  rows of the file equal to the copy within 6e-8 (float32). Scenario A's copper in use at the end of 2040, median of the
  first 2,000 runs, 1.56e13 kg in 08's copy and in 07's: the data centres' own result, not the copy's. The copy in
  `data/raw/` is still of 07's file of 2026-10-23: his run of the tool brings it up to date.
- **Tests, as far as they ran before his handover** ("write handover, commit and push as I have to leave soon"):
  passing: test_parameters, test_schemas (its two failures of today, the overview's boxes and the new page, fixed and
  rerun), test_composition, test_make_humanoid_register, test_make_parts_taken_apart, test_stock_and_flow (47, brought
  to 04 as it is: medians, one legend below the panels). FigureTests: 40 pass. **Not verified:** test_parts_taken_apart,
  test_comparison and test_combined_stock_and_flow were updated (medians, legends with the median and 95 % samples,
  "runs", the medians pages, the removed element pages, a checker that knows a page saved tight) and rerun, the rerun
  stopped at the handover: the parts run had shown one failure and one error, not read. test_all_figures stopped after
  02: 01 10 faults (the robot table's masses on the joints, which I had moved; fixed after that run started, by
  measured widths), 02 1 fault (not read; the medians page's column narrowed after the run started).
- **Sandbox at 2,000 runs** (every stage, his inputs, 05 on the first 2,000 runs of 08's copy): **not run** (its script
  was ready in the scratch folder).
- **Found by him at the end, not changed (his word first):** "These titles look ugly. Font terrible why the hell such a
  bold": the panel titles of 02, 03 and 04 are set in bold (02 in 11 places, 03 in 2, 04 in 4; 01's headings 17); the
  data centres' 08 writes its titles in normal weight.
- **Not covered:** the figures of 200 and 2,000 runs, not of 200,000 (his run); a text's gap is measured between the
  boxes matplotlib gives, not the ink; the colour rules read the colours a panel draws, not how they look printed.

## 2026-11-09

### V227. His runs of 02, 03, 04, the copy and 05 read back (2026-11-09, his "Yes, both")

- **Times:** every output as his runs of 2026-11-08 left it (02 14:48:11 to 14:49:13; 03 15:15:51 to 15:16:53; 04's
  draws 15:20:35, its pages to 15:24:13; the copy 15:55:48; 05 15:56:04 to 15:59:05): nothing put back by iCloud.
- **Code changed after his runs** (yesterday's session record, every edit): 01 only its overview (05's stage and
  output boxes), 02 only strontium's name, the settings only 05's four keys, 04 only the element page it shares with 05
  (split out, its note wrapped). None changes a number of 02, 03 or 04; only 01's overview pages (14:32) lack 05.
- **02, all six types, all 200,000 draws:** `taken_apart` added up by element equals `data/consolidated/<type>/elements`,
  `taken_apart_mass` equals `total`, and by 01's groups equals `part_groups`, each within 1e-7 of the robot's mass
  (float32); every part one of 01's 14. The layers check: joint driver boards 6 to 11 % of their draws above the copper
  their layers hold, battery and head boards about a third, the small 2-layer boards on the cables 92 %, the computer
  boards 2 %, as in the sandbox (V223); the bounds by hand 127.2 (4 layers) and 181.0 mg/cm2 (6 layers).
- **Every page of 02, 03, 04, 05 and 01 (592):** no ink in the outermost 3 pixels of any page (a text run off a page
  leaves ink there). Deliberate fault: a page with a note too long for it is flagged (28 and 18 pixels at the sides), one
  that fits is not.
- **Looked at:** 02's group pages (24) and part lists (30); 03's group pages (22), the mass by group (1) and the part lists
  (70); all 41 of 04's pages; 05's 12 distribution pages and 27 of its 69 element pages (A's 23, B's first 4).
- **04:** three lines of its summary (copper in stock 2040, neodymium in 2030, gallium out 2035) recomputed from its draws:
  the same to six digits. The robots built and in use equal the article's. Copper per robot in use 7.55 kg at the end of
  2025, 3.98 kg at the end of 2040: the battery packs, 9.6 a robot in 2025 and 3.05 in 2040, a day's work each robot
  (METHODOLOGY, 04 step 4, his words), not a fault.
- **05:** its robot lines equal 04's summary (12,672 numbers, identical); its data-centre lines equal the statistics of
  the copy computed afresh (10,368 numbers, within 4.6e-6, the six digits of the file); its stored draws together equal
  the copy plus 04 draw by draw (first 20,000 draws, all years, elements, flows and scenarios, within 6e-8); strontium,
  which no robot holds, "–" in the robots' lines.
- **Found, not changed (for his decision):**
  1. *"0 %" for a part that is held:* 02's `part_rows` (also 03's and 04's lists) writes the share rounded down to a
     whole percent: titanium in type 3's frame (0.597 % of the draws), lithium and tantalum in type 4's sensors (0.780 %)
     read "held in 0 %" in 02's and 03's lists, magnesium in type 3's frame (0.6 %) in 03's.
  2. *02's and 03's lists choose their elements differently:* 02 the elements its type holds in at least 2.5 % of its
     draws, 03 those any type holds so; magnesium in the frames of types 3 and 4 is in 03's lists, not in 02's. Within an
     element, neither has a threshold for a part.
  3. *05, a fault of my build:* on the pages of an element only one side holds (dysprosium, indium, magnesium, terbium,
     titanium the robots only; strontium the data centres only; 18 pages), the legend names the side that holds none, which
     has no line, and the robots' line lies hidden under "both together". 04's `log_panel` draws every series given;
     05's test counted an empty line as drawn.
  4. *The handover's state of 2026-11-05* reads "164 with the Neo1 not drawn … 11": drawn are 163 and 10, the Neo1 an
     outlier listed in types 3 and 5 (V-entry of 2026-11-04).
- **Not covered:** 42 of 05's element pages (B's other 19, C's 23), not looked at: RAWCLICDataCenters' 07 will have two
  cases instead of three (Matthias, 2026-11-09: "the datacenter will be only two cases not three. Let me first work on
  this"), so the copy and 05 will be run again.

## 2026-11-08

### V226. 05: the AI data centres of RAWCLICDataCenters' 07 and the humanoid robots of 04 together (EVIDENCE.md E52)

Matthias, 2026-11-08: "write 05 combination of results of 04 and 07 with the distributions", then "Yes, build it" to the
specification's rows 1 to 8. Built: `tools/copy_data_center_draws.py` (07's element draws copied into
`data/raw/data_center_stock_and_flow/`, GitHub/CLAUDE.md §6) and `05_combined_stock_and_flow.py`.

- **Tests** (`tests/test_combined_stock_and_flow.py`, 8 tests), passing. They were written with the code, not run
  before it existed; what they catch is shown by the deliberate faults below:
  - *the copy:* every number of a made-up 07 file found again in the copy, at its scenario, draw, year, flow and element;
    07's "collected" and the years before 2025 left out; a missing row and a doubled row each stop the tool with no
    `source.txt`;
  - *the combination, every kg by hand:* for each scenario, flow and year, each element's data centres + robots draw i
    with draw i, an element only one of the two holds counted from that one alone (the elements: the union, 23);
  - *its summary:* mean, median, 2.5th and 97.5th percentile of each line against numpy on the same draws;
  - *its pages:* 69 element pages and 12 distribution pages, every page within his rules (`page_problems`), each legend
    naming exactly the lines drawn;
  - *its checks:* other numbers of draws or of years in the two inputs stop 05 ("do not pair draw by draw"); no copy of
    07 stops it and names the tool.
- **Deliberate faults, each in a scratch copy** (V-3), 10 of 10 caught by the tests: the robots of the next year; one
  part of the robots only; the data centres of scenario A for all three; the data centres of another flow; the draws
  shuffled (robot draws reversed); an element matched to the wrong column; the copy keeping 2024 to 2039; the copy not
  checking doubled rows; the copy taking "collected" for "out"; the pairing check switched off (caught by a crash on the
  unequal shapes, not by the check's words).
- **Sandbox on real data** (scratch, nothing in `data/` or `figures/`): 07's first 2,000 draws cut from its
  `stock_flow_draws.csv`, copied by the tool (1 s), and 04's 2,000 draws of the sandbox chain; 05 wrote 81 pages in 78 s,
  every page within his rules, no legend over a line.
- **Order of magnitude:** copper in stock at the end of 2040, scenario A, read directly from 07's file and from the
  copy: the same to four digits, so the copy is exact. Its size, far above the world's copper mine production of a year,
  is 07's (RAWCLICDataCenters' VERIFICATION: its scenario A from ai-2040.com's compute, brought to Matthias on
  2026-10-22), not a fault of 05. 07's numbers are not written here: this repository is public, RAWCLICDataCenters is
  private. The robots: 70 billion in use at the end of 2040 (04, from ai-2040.com); per robot, medians, aluminium
  36.5 kg, copper 3.97 kg, lithium 0.307 kg, neodymium 0.377 kg.
- **A fault found by looking, which the automatic check missed:** on the distribution pages the note at the foot ran off
  the page on both sides ("each panel…", "…not drawn" cut). Two causes: the shared page (04's `split_elements_page`,
  also 04's own element pages) wrote its note as one line, unwrapped; and `page_problems` laid each page out at the
  screen's 100 dpi, where the line measured 4 to 1,916 of 1,920 px (99.6 %), while the page is saved at 150 dpi, where the
  letters come out a little wider. **Fixed:** `page_problems` now lays each page out at the dpi it is saved with (the
  three hooks of 02/03, 04 and 05 pass it); then 05's tests failed on the 12 distribution pages, as they should; the
  shared page now wraps its note to the page's width (07's characters a line, scaled to the page's width and its 11 pt)
  and leaves room for its lines; 05's 8 and 04's 48 tests pass, the sandbox again 81 pages with no problem. **Looked at:**
  05's `A/distributions/elements_2040.png` (the note on three lines inside the page) and 04's `elements_2040.png` drawn
  from the sandbox chain (three lines, inside).
- **His run, read back:** the copy tool 15:55:06 to 15:55:48 (`element_draws.npy` 2.30 GB, from 07's file of 2026-10-23
  14:38:09); 05 15:56:04 to 15:59:05, after the last change of its code (05 15:28:38, 04's shared page 15:45:25): 81
  pages, 23 element pages and 4 distribution pages in each scenario's folder. Looked at: `B/distributions/elements_2040.png`
  (200,000 draws, the note on three lines inside the page, each legend naming what is drawn) and `C/elements/Copper.png`.
- **The whole suite,** after the last change of the code (the page check at the saved dpi, the wrapped note): 689 tests
  in 1,069 s, OK (681 before, and 05's 8).
- **Not covered:** the tool on the real 9 GB file and 05 at 200,000 draws (his runs; at 200,000 draws the copy holds about
  2.2 GB and 05's draws about 2.6 GB, scaled from 2,000 draws; the time is not measured); the element pages of scenarios
  B and C looked at one by one (checked by `page_problems` only).

### V225. His run of 01 read back (2026-11-08, 14:32)

- **Times:** his 01 wrote `figures/schemas/` at 14:32:30 to 14:32:31: `overview_1.png`, `overview_2.png`, `notes.png`,
  `taken_apart.png`, `faults_1.png` to `faults_3.png`; `01_schemas.py` last changed 12:43:42: the run is of the final code.
- **Faults:** "No fault found in the inputs." The three pages are 01's list of what it checks.
- **Looked at:** `taken_apart.png`: the four groups and 14 parts with the descriptions as corrected (magnet carriers,
  gear carriers, the drivers' capacitors), every text inside its box.
- **A gap of mine, closed:** the sandbox runs of V222 to V224 read 01's pages and its exit code, not its count of faults
  (01 ends with 0 also where it finds faults); his run shows none. Sandbox runs from now on read the count.
- **Not covered:** his runs of 02 (going at the handover), 03 and 04.

### V224. 02's check that every material's elements add up to its kilograms (his "Yes, fix it")

- **What was wrong** (found in V223): `Robot.element` added each element's kilograms both to the elements (the table
  recipe_elements) and to `in_recipes`, "the kilograms of each material that follow a recipe"; `draw_faults` then
  compared the two, one sum with itself. It could never fail: the capacitors' organic rest doubled passed it.
- **What it is now:** two counts that come from different places. `Robot.in_recipes`, a material's kilograms whose
  elements are drawn, is counted where the mass is booked (`Robot.drawn`): a material with a recipe, a grade, the
  magnets' or the cells' fractions; a board, less what sits on it (its encoders, its capacitors' titanate); a sensor, its
  car sensor elements' kilograms; the large capacitors; the titanate; the cells. `Robot.elements_of`, the kilograms of the
  elements booked under a material, is counted where each element is booked. 02 checks every material in every draw
  (`check_recipes`, after `check_taken`): its elements within 0.1 % of its kilograms (02's COMPOUND_TOLERANCE: the
  element recipes' compounds are written to five decimals), and stops otherwise, naming the material and the draws.
  `draw_faults`' sum over all materials now compares the two counts too.
- **Tests first, seen to fail** (no `elements_of`, no `check_recipes`), then passing: a capacitor and a board booked
  directly, both counts their kilograms by hand; type 1 drawn at 200 draws passes; its electronics, cells and aluminium
  each made 1 % off: 02 stops each time.
- **Deliberate faults, each in a scratch copy** (V-3), every one stopping 02 with the new check's words ("Boards and
  components: its elements miss its kilograms whose elements are drawn in 178 draws (by up to 0.171 kg)"; "Battery
  cells: … in 200 draws (by up to 3.07 kg)"): the capacitors' organic rest doubled; the cells' kilograms not counted; a
  board counted with what sits on it; a sensor not counted; the titanate not counted; a board missing its bromine; a
  recipe's first element left out.
- **All six robot types as drawn pass it:** at 1,000 draws (the tests of the parts) and in the sandbox chain at 2,000
  draws (01 46 pages, 02 372, 03 208, 04 41, every page within his rules, no legend over a line).
- **The whole suite:** 681 tests in 1,001 s, OK.
- **Not covered:** a material booked whole without any elements (a material with no recipe, as Other) is not in the
  check: it holds no elements by design, as before.

### V223. The large capacitors at the joint motors and on the capacitor boards; the boards' layers (EVIDENCE.md E51)

- **His words:** "There are also quite large capacitors close to each joint motor ... So have them correct!!", "PCBs have
  different size and layors etc.", "Yes, enter 1 to 8".
- **Sources read first-hand before the proposal** (A-1): the CubeMars driver manual (2 × 180 µF 63 V, 8 × 20 mm, Rubycon),
  FROLYT's declaration (its shares add up to 100 %), RoboParty's BOM of the RP1's motor-capacitor board (5 cans of 13 ×
  30 mm). TDK's two declarations: its server refused my download; read by the helper as files.
- **The builders** (V-6): all six files rebuilt in scratch and compared row by row with the files on disk: added in each
  the 15 shared constants; in type 1 the four capacitor boards changed (2 / 5 / 10 → 10 / 20 / 30 cm²; the RP1's "Leg board
  YCL.E000057" → "Motor capacitor board RBE-PWR-MCAP") and the RP1's own count added; nothing else. Written; all six
  again equal to their builders. A test of 01's pages then caught my label of the G1's buffer board, "S, E": its size is
  the RP1's board's, for the G1 an estimate: "E".
- **Tests** (V-1, V-2), all passing:

| What | How |
|---|---|
| the rows as agreed (0 / 2 / 4; 0.68 / 1.5 / 2.6 g; 2 / 5 / 8; 2.6 / 5.3 / 8.0 g; the four capacitor boards at 10 / 20 / 30 cm²; no leg board; the RP1's 5) | the builder's file read by 01 |
| 01's checks: a robot's count naming a board that is no capacitor board of it; a count from 0 on a capacitor board; a liquid capacitor's shares reaching 1.4 at their maxima | deliberate faults in the file, each its fault (V-3) |
| which boards carry capacitors (3 names yes, 4 no); the capacitors a small PCB | by hand |
| every kg by hand, type 1 with the numbers, masses and shares fixed: the capacitors' copper and tin in the G1, the RP1 and the X1 = (its joints × 2 × 1.5 g + its capacitor boards × their capacitors × 5.3 g) × the share, draw by draw; the RP1's motor-capacitor boards its maker's 5, its capacitor boards the shared 4; aluminium 47 % (liquid) or 40 % (hybrid) in every draw, each kind in 35 to 65 % of them | by hand |
| a joint whose module mass its maker states keeps it, with 4 capacitors of 100 g each (the X1's joints within their module masses) | by hand |
| the capacitors' elements in the small PCBs; the type's elements adding up (02's `draw_faults`) | test |
| one robot's capacitors booked directly, the shared draws set by hand: all of their mass in their elements, no more; aluminium of interest 48 % (liquid) and 46 % (hybrid), not the kaolinite's or the glass's; copper; the part Small PCB | by hand |
| the layers check: the most copper of 2, 4 and 6 layers 73.4, 127.2 and 181.0 mg/cm²; the layers by kind; with every board not weighed 0.56 g/cm² and 20 % copper (112 mg/cm²) the small boards above in every draw, the head's, battery's and computer's in none; one driver board of 150 mg/cm² not above (its group's most, 6 layers), one small board of the same above | by hand |

- **Deliberate faults, each in a scratch copy** (V-3); every one caught, two only after a test was added:

| Fault | Caught by |
|---|---|
| the capacitors outside the joint module | every kg by hand; the stated module mass |
| the kind never drawn (always liquid) | every kg by hand (aluminium 47 % or 40 %); one capacitor by hand |
| the kaolinite's aluminium as an element of interest | every kg by hand; one capacitor by hand |
| the organic rest doubled | one capacitor by hand (a test added for it). 02's existing check "the elements do not add up to the materials that have recipes" did not catch it: it compared the elements booked with the kilograms booked as elements, the same sum (`draw_faults`); fixed on his word in V224 |
| the maker's own count ignored | every kg by hand |
| the capacitors a PCB | the small PCBs; the component a small PCB |
| no board a capacitor board | 7 tests |
| a capacitor's grams taken as kg | every kg by hand |
| the layers check at the fewest layers of a group | one driver board by hand (a test added for it) |
| a small board of 4 layers | the layers check by hand |

- **Sandbox, the whole chain at 2,000 draws** (V-9): 01 46 pages, 02 372, 03 208, 04 41, every page within his rules, no
  legend over a line; robots in use 10,000,000 (2025) and 70,000,000,000 (2040); at most 2.4 GB.
- **The results, by eye** (A-4): the large capacitors in one robot about 42 to 67 g (median by type; 95 % 12 to 237 g),
  held in 84 to 93 % of the draws (none where a robot draws 0 on its drivers and has no capacitor board); their aluminium
  20 to 32 g, copper and tin 0.1 to 0.2 g each. By hand at the modes: 25 joints × 1 to 2 × 1.6 g, and the G1's 4 boards ×
  5 × 5.3 g, about 40 to 190 g: the same order.
- **The layers check, found** (02's report, each type's `summary.csv`): the share of the boards' draws whose copper is
  above what all their layers could hold: the small boards in the cables (2 layers, 73.4 mg/cm²) 92 to 100 %; the head's
  boards (4, 127.2) 34 to 50 %; the battery's (4) 31 to 33 %; the joints' driver boards (4 / 4 / 6, 181) 6 to 12 %; the
  computer's (6) 2 %. The measured copper share (Bizzo, mixed boards with their components) at 0.56 g per cm² gives
  112 mg/cm² at the mode, more than a thin board's layers hold; and a driver board's weighed mass and its area are drawn
  apart, so its copper per cm² reaches some 480 mg. Reported to him, not changed (row 8: the copper stays measured).
- **The whole suite, first run:** 679 tests in 993 s; 3 failures and 1 error, each from this change, each understood:
  (1) the G1's copper in its cables, a hand calculation of before (buffer boards of 5 cm², no capacitors): the code gave
  exactly the new hand values, 102.144 g of cable copper + 8.96 g of board copper (4 × 20 cm² × 0.56 × 20 %) + the
  capacitors' copper by kind and number (111.687 g liquid with 5 a board, 111.316 g hybrid …); the test now says so;
  (2) the list of the electronics' components named the old five; (3) the capacitors' colour, Tol's dark blue, was a
  sensor kind's already: now his dark cyan `#225555`; (4) the means page's copper row, now with the capacitors' 268 mg,
  wraps "Battery cells" over two lines: the test compared the raw lines, now the words. Those tests again: 30, OK.
- **The whole suite, second run:** 679 tests in 954 s, OK, on the final code of this entry.
- **Validation:** the capacitors' inputs rest on makers' declarations and two makers' joint drivers (A-1); no
  independent figure of a humanoid's capacitors in grams was found to compare a result with: **not validated**.
- **Not covered:** his runs of 01 to 04 at 200,000 draws.

### V222. How a robot is taken apart: four groups and 14 parts in 01, 02, 03 and 04 (EVIDENCE.md E50)

- **His words:** "I want a detailed list of the component, so it is easy to understand and establish a recycling to know
  how to take it apart!!!"; the four groups and their subcategories in his words; "Also the joints the can be split up in
  smaller parts. I waht schemas for this"; "I want it 100% correct. No problem to rerun"; "Yes do it"; "Yes, add 1 to 3".
- **What is verified, and how** (the methods of the section above):

| Step | What | How (method) | Result |
|---|---|---|---|
| 01, the list | four groups, 14 parts, each once, every kind of part in a group | tests (V-1) | pass |
| 01, the rule | 36 rows placed by hand as his words say (a hip fan a PCB, a driver board a small PCB, the battery management board a small PCB, a sensor's housing a sensor, the RP1's cover magnets the shell, a wheel's motor magnets the magnets, a head actuator's valve the hydraulics …); 5 rows that must stop it | tests, hand (V-1, V-2) | pass |
| 01, every row of all six parts files | each row 02 books has a part | 01's check on the six files as the builders write them (V-4) | 0 rows unplaced; a made-up row caught with its row number (V-3) |
| 01, the page | every group, part and description on it, nothing outside its box, no text below 14 points, no project words; looked at | tests (V-7, V-8), by eye | pass; two descriptions corrected after the sandbox (below) |
| The builders | the head's hydraulic actuators, valves, boards and sensors in the head joints | all six files rebuilt in scratch, compared cell by cell with the files on disk (V-6): before the change 0 cells differ in all six; after it 13 (type 3: 1, type 5: 12), all Head → Head joints; written; all six again equal to their builders | as intended, nothing else |
| 02, the booking | every element and every kilogram to its kind and part; parts add up to each kind in every draw | built-in check `check_taken` (V-4); test in all six types at 1,000 draws (V-1) | pass |
| 02, by hand (type 1) | the joints' neodymium = the magnets' kg × 0.24 in every joint kind; the RP1's cover magnets in the shell, only in its draws; gold: the computer's a PCB, the driver boards' and the battery board's small PCBs; the cables' copper wires; the cells' lithium cells; the head's indium sensors; the encoders' neodymium sensors; the G1's hip fans' copper a PCB; the battery group = the battery kind less its board; the body = the frame and shell kind | V-2 | pass |
| 02, type 5 | the Atlas HD's head actuator in the head joints: its titanium hydraulics, its position sensor's neodymium a sensor | V-2 | pass |
| 02, the groups' mass | the four groups add up to the robot's mass in every draw (types 1 and 5) | V-1, V-2 | pass |
| 03 | the parts add up to the elements (its own check, V-4/V-5); copper of type 2 by group and part by hand (V-2); the page of copper by group, type 2's mean | V-1, V-2 | pass |
| 04, every kilogram by hand | each part's kg in the stock, the inflow and the outflow = its kg of one robot × the units that carry it, added over the types; the small PCBs' copper = joint sets × 0.2 kg + packs × 0.1 kg (each with its own lifetime); every other part 0 | V-2 | pass |
| 04, the summary | each element by group and by part, its mean, 2.5 % and 97.5 % over the draws above 0, every flow | V-2 | pass |
| 04, the pages | the elements of 2040 split by the four groups, legend in their order, copper's mean by hand; the list of 2040 part by part, the small PCBs' row by hand; a list made by hand with a part held in half the draws | V-1, V-2, V-7 | pass |

- **Deliberate faults, each in a scratch copy** (V-3); every one caught:

| Stage | Fault | Caught by |
|---|---|---|
| 04 | the packs' parts with the robots' lifetime | every kg by hand, the summary (3 tests) |
| 04 | the joints' parts with the robots' lifetime | every kg by hand |
| 04 | a part booked to the next part | every kg by hand, the summary, the list (3) |
| 04 | a group summed from one of its parts | the summary ("–" where the group holds copper) |
| 04 | the page summing one part of each group | the page's copper by hand |
| 04 | the summary's 95 % at 5 and 95 | the summary (a test added for it: it was missed at first) |
| 04 | the summary's mean over every draw, zeros too | the summary (2) |
| 04 | every type's units times type 1's robot | every kg by hand |
| 02, 04 | the list's statistics over every draw, zeros too (two ways) | the list over the draws that hold it (a test added for it: missed at first) |
| 01 | every circuit board a PCB | the rows by hand, type 1 by hand (gold of the driver boards), the groups' mass (3) |
| 01 | no rule for the magnets | the rows by hand, the magnets by hand, the pages of the groups (3) |
| 01 | a fan in the joints placed nowhere | 01's check of every row (the G1's hip fans named), the rows by hand; 02 stops (10) |
| 01 | the cover magnets as the joints' magnets | the rows by hand, the RP1 by hand (3) |
| 02 | a sensor's housing placed by its name | 02 stops: the housing has no part (`taken_part`) (7) |
| 02 | the cells' mass not booked by part | 02 stops: the battery's parts miss its mass (`check_taken`) (7) |
| 02 | the groups' mass all in the joints | the four groups by hand |
| 02 | the check of the split switched off | the faults in the split |
| 03 | the groups as the parts | copper by group by hand |
| 03 | the check of the parts switched off | the parts that do not add up |

- **Sandbox, the whole chain** (V-9) on the project's own inputs at 2,000 draws a type, into scratch folders
  (`scratchpad/check_1108/sandbox_chain.py`): 01 0 faults, 46 pages; 02 372 pages (156 s); 03 208 pages (76 s); 04 41
  pages (31 s); every page within his figure rules, no legend over a line; robots in use at the end of 2025 10,000,000,
  of 2040 70,000,000,000; the whole run 287 s, at most 2.1 GB of memory. Looked at: the schema page; type 1's first page
  of elements by group and its first list page; 03's mass by group; 04's elements of 2040 by group and its first list
  page of 2040.
- **By eye, and what it found** (A-4): type 1's aluminium in the gears, 617 g a robot, traced to the parts file (the
  second gear stage's carrier 12.5 / 25 / 40 % aluminium) and the 392 g in the motors to the magnet carriers (aluminium):
  right, but the page's words said "the steel gear stages" and "copper windings, electrical steel" only. Corrected:
  "gear stages, their carriers, bearings inside the joints", "rest of the motors: windings, steel, magnet carriers".
  The titanium of the small PCBs in 2040, 744 kt (about 11 g a robot), is the barium titanate of the driver boards'
  ceramic capacitors (E38 point 4, unchanged). The groups on 04's page agree with the parts on its list (aluminium in the
  joints 453 Mt: motors 40, gears 67, housings 345, hydraulics where held).
- **Found, not changed:** 02 and 03 keep a type's pages open until it is saved in full (matplotlib's "More than 20
  figures" warning, there before today, V221's suite too); the new pages add to it. RAWCLICVehicleElectronics' documents
  give its board sizes in mm², its code in cm² (its `docs/06_PCB_MODEL_DESIGN.md`, `04_PCBAreaMC/PCBAreaMC.py:386`).
- **The whole suite, first run:** 668 tests in 998 s; 51 failures and 2 errors, all from two causes. (1) 01's new check of
  every row (`taken_apart_faults`) left out the rows drawn with the joints only by their kind; the test files' joint
  modules stand in a joint kind ("Joint module, small" in the ankles), so every check of a test file found four faults
  more (49 tests of `TestPartsTakenApart`). 02 knows those rows by what they are computed from ("the sum of JointParts",
  "the Joints' module masses", "the Joints' shares"; the encoders' "Sensors and SensorElements"): these markers now stand
  in 01 (`FROM_JOINTS`, `FROM_SENSORS`), 02 reads them there (one copy), and the check leaves those rows out as 02 does.
  (2) Two tests of 02 still named the old part group "Frame" and the old series of pages; they name the four groups'
  "Body" and the series with 'groups' and 'parts'. Those tests and all of 01's, again: 265, OK.
- **The whole suite, second run:** 668 tests in 973 s, OK (on the code of this entry; started before the capacitors
  of V223 were begun, every module loaded at its start).
- **Validation:** the change books what the model already computed into finer parts; every total is unchanged (the parts
  add up to the kinds, the kinds to the robot, in every draw); it changes no value of an input. New today: the elements
  of one robot against the three outside figures the documents hold (rows A11 to A13 of "What is validated" above, from
  this sandbox): dysprosium within or above the analysts' 35–79 g; NdFeB about half the Optimus claim of 3.5 kg; copper
  below CRU's 4–8 kg per 60 kg. All three sources second-hand; reported, not changed.
- **Not covered:** his runs of 01, 02, 03 and 04 at 200,000 draws (04's element files about 4.2 GB each); the layers and
  sizes of the boards and the large capacitors at the joint motors (E51, open).

### V221. The titles by the year alone; the elements' distributions exactly as RAWCLICDataCenters' 05 (EVIDENCE.md E49)

- **His words:** "Sorry end of goes away. This is not needed"; "I also want finally see the distribution. Exactkly the
  figures we have worked out for the data centers!!!".
- **Tests first, seen to fail**, then passing: the robots-in-use page titled "2025: 10,000,000 robots" to "2040:
  70,000,000,000 robots", its rows "Robot type 3, 2040"; no text "End of" on any page; the pages by exact name (the
  overview, the element pages, `distributions/robots_in_use.png` and its numbers, `distributions/elements_2025.png` to
  `elements_2040.png`); on the page of 2040 a panel each for lithium, aluminium and copper (neodymium not held), in 02's
  order; copper's mean and 95 % by hand (all parts added up, in its unit); the page's legend the three parts drawn; and
  a page made by hand ("A 0 is not part of a distribution"): copper held in half of 400 draws, in the bodies only,
  lithium in none: copper's mean and 95 % over the 200 draws that hold it, "held in 50 % of the draws" written, no
  panel for lithium, the legend the one part drawn. 46 tests of 04 and 6 of the settings, OK.
- **Deliberate faults**, each in a scratch copy of 04, each caught by the check meant for it (46 tests, 1 failing): the
  elements of the year before; the joint sets left out of the total; the zeros in the mean (the total and the parts
  both over every draw: the mean half the true one); the share held not written; a legend of every part, drawn or not;
  the median as the line; the 95 % at 5 and 95. A first version of the zeros fault, over every draw in the total only,
  was caught by a crash, not by a check, and does not count.
- **Sandbox** on the first 2,000 of his draws of 02: 29 pages (the overview, 22 element pages, the robots-in-use page and
  its numbers, the four pages of the elements), all within his figure rules, no legend over a line. The page of 2040
  looked at: 22 panels, each split by part, its mean and 95 %; titanium's draws spread from near 0 to about 200 Mt, most
  of them pressed into its first bars (05's form has no logarithmic axis); magnesium held in 11 % of the draws.
- **The whole suite:** 649 tests in 766 s, OK (started before the test of the element held in some draws was added,
  with the code of 04 as it stands; that test and the rest of 04's and the settings' tests run after it: 52, OK).
- **Not covered:** his run of 04 at 200,000 draws.

### V220. The article's values at the end of each year; the estimate of 2041 withdrawn (EVIDENCE.md E48)

- **His words:** "Follow the artcile!! 70 x 10E9".
- **Tests first, seen to fail** (6 failures, 3 errors), then passing: `robots_2041` gone; the targets one path of 64
  quarters, the end of 2025 10 M, half way through 2025 geometric from 8.62 M, the end of 2026 11.6 M, the end of 2040
  70 × 10⁹; the start 10 M / 1.16; the cohorts of 1 January 2025 holding 8.62 M; one chunk: the year ends the article's
  2025 to 2040, the start 8.62 M, a wrong start caught; the run: the robots at the year ends the article's 10 M to 70 ×
  10⁹ in every draw, the summary's first stock 10 M, the robots-in-use page titled "End of 2025: 10,000,000 robots" to
  "End of 2040: 70,000,000,000 robots". 45 tests of 04 and 6 of the settings, OK.
- **Deliberate faults in scratch copies of 04, each caught** (5): the values at 1 January again; the start without the
  growth; the start not checked; the year ends at the third quarter; the types started at the 2025 value.
- **Sandbox** on the first 2,000 of his draws of 02: 04 ran, the robots in use at the end of 2025 10,000,000 and of 2040
  70,000,000,000; 69 pages, all within his figure rules, no legend over a line; the robots-in-use page looked at.
- **The whole suite:** a run on this state finished after the change of V221 had begun and does not count; run on the
  state of V221.
- **Not covered:** his run of 04 at 200,000 draws; the article's own dating of its robots (1 January), put to him.

### V219. 04's years exactly as RAWCLICDataCenters' 07; the robots at 1 January 2041 (EVIDENCE.md E48)

- **His words:** "Both have to be exactly the same, as we have to combine both data!!!", "Both have to be on the same x
  axis scale!!", to the table of the estimate of 1 January 2041 "Yes!!", "Do never ever give me 2039".
- **Tests first, seen to fail** (9 failures, 7 errors), then passing:
  - the setting `robots_2041` 158.2 / 163.7 / 166.3 × 10⁹, equal to 70 × 10⁹ × 2.26, × 70^(1/5), × 29.7 / 12.5 (to
    0.1 %); refused out of order, as a single number, with a min of 0;
  - the quarters by hand: 64; the first quarter's middle 2025.125, the last quarter's end 2041.0; 65 times of the
    types' draws; a workbook value read at its 1 January; the settings at 2025.0, 2032.5, 2040.0;
  - the targets: 2 draws × 64 quarters; the end of 2025 11.6 M (1 January 2026), half way geometric, the end of 2039 70
    × 10⁹, the end of 2040 each draw's 2041, the quarter before it geometric towards it;
  - the cohorts and the robots of 1 January 2025 by hand with 64 quarters;
  - one chunk: the check passes; the article's 1 January 2026 to 2040 at the year ends, the draw's 2041 at the end of
    2040; a wrong end of 2040 caught ("not the draw's estimate"); the stock of 2025 its end, 11.6 M, start + built −
    retired = 11.6 M;
  - the run: every file 16 years (flows 2025 to 2040, stocks the end of 2025 to the end of 2040); the robots at the year
    ends the article's of 1 January 2026 to 2040 and, at the end of 2040, the run's own draws of 2041 (its random numbers
    recomputed in their order); the summary's years 2025 to 2040 for stocks and flows alike, its first stock 11.6 M; the
    robots-in-use page titled "End of 2025: 11,600,000 robots", "End of 2030: 35,700,000 robots", "End of 2035:
    2,260,000,000 robots" and "End of 2040: … to … robots" (95 % of the run's 2041 draws); type 3 at the end of 2040 by
    hand; the element pages at the year ends; every page within his figure rules.
  45 tests of 04 and 6 of the settings, OK.
- **Deliberate faults in scratch copies of 04, each caught** (7): the end of 2040 the 2040 value, without 2041; the
  stocks at the start of the year; the check without 2041; the workbook's years at 1 July; 2041 drawn before the other
  random numbers; the title of 2040 one draw's; the summary a year late.
- **Measured at 200,000 draws** with 04's own random numbers (65 times): the types' bands at the last quarter of 2040
  ±29.9 to 30.1 % (wanted ±30.0 %); each type's draws within 0.0022 of its triangle; type 3 off its own draws by at most
  0.109 % of its half-width; the six adding up to 1 to 2.2 × 10⁻¹⁶; correlations at the last quarter of 2040 −0.71 to
  +0.29; a draw quarter to quarter at least 0.9988; about 34 s.
- **Sandbox** on the first 2,000 of his draws of 02: 04 ran, the robots in use at the end of 2025 11,600,000, at the
  end of 2040 162.7 × 10⁹ on average; 69 pages, all within his figure rules, no legend over a line. Looked at: the
  robots-in-use page (the end of 2040 159.3 to 165.5 × 10⁹, 95 % of the draws) and the overview (2025 to 2040, as 07).
- **The whole suite:** a run on this state finished after the change of V220 had begun and does not count; run on the
  state of V220.
- **Not covered:** his run of 04 at 200,000 draws; the combination with 07 (not built).

### V218. 04 at 1 July; the robots in use of the six types on one page (EVIDENCE.md E47)

- **His words:** "why is the largest part of the triangal cut off? Furthermroe can you not combine the 6 types to 1",
  "I want to see at the end how many robots there are", "not 39 I want 2040", "SHit it to 1st of July", "Yes".
- **Tests first, seen to fail** (6 failures, 2 errors: the modes, spread, shares and packs at the workbook's years now
  at 1 July; the dates; the summary's years; the pages), then passing:
  - the dates by hand: the model's first day 2025.5, the first quarter's middle 2025.625, the last quarter's end 2040.5,
    the types' first time 2025.5; a workbook value of 2030 read at 2030.5, half way at 2028.0; a setting of 2025 and
    2040 at 2025.5, 2033.0, 2040.5; the flow years named '2025/26' and '2039/40';
  - the modes, spreads, shares and packs by hand as before, at 2025.5, 2033.0 and 2040.5;
  - the run: the stocks of the summary at 2025 to 2040 (1 July), the flows at 2025/26 to 2039/40; the pages by exact
    name (the overview, the element pages, `distributions/robots_in_use.png` and its numbers, the element distribution
    pages and theirs); the combined page's four panels titled "1 July 2025: 10,000,000 robots" to "1 July 2040:
    70,000,000,000 robots", six rows each, type 1 at the top and type 6 at the bottom, each labelled where its bars stand;
    type 3 at 1 July 2040 by hand (median, mean, 95 % in its panel's unit); its bars from its smallest to its largest
    draw, the axis holding every draw of the six; every row named on the page of numbers; the element distribution
    pages at "1 July 2025" to "1 July 2040"; every page within his figure rules, no legend over a line.
  44 tests of 04 and 6 of the settings, OK.
- **Deliberate faults in scratch copies of 04, each caught** (9, one after a check was added): the workbook's years at 1
  January; the settings' years at 1 January; the model from 1 January; the flows named by the calendar year; the page's
  axis cut at 99.5 %; the page a year early; the title one type's robots instead of all; type 1 at the bottom; the rows'
  bars cut at 99.5 % (passed at first: only the axis was checked; then the bars of each row checked to reach its smallest
  and largest draw, caught).
- **Sandbox** on the first 2,000 of his draws of 02: 04 ran, the robots in use at 1 July 2025 10,000,000 and 2040
  70,000,000,000; 69 pages (the overview, 22 element pages, 46 distribution pages and their numbers), all within his
  figure rules, no legend over a line. Looked at: the combined page (four years, six rows each, nothing cut) and the
  overview (stocks at 1 July, flows in the middle of their year).
- **The whole suite:** a run on this state finished after the change of V219 had begun and does not count; run on the
  state of V219.
- **Not covered:** his run of 04 at 200,000 draws with this code.

### V217. The types' shares page from the results of the run (EVIDENCE.md E46)

- **His words:** "I want to see the triangulas from the MC and not some faque trianguals. You are again Lying to me. You
  know I want to see results and not this!!!", "Never never again do something like this!!! write a roule",
  "requirement!!", "I only want to see results or schemas, of the implementation".
- **Tests first, seen to fail** (the shares page's panel of type 3 in 2039 by hand from `units_in` and `article_in`),
  then passing: type 3 in 2039 and type 1 in 2025, each type's robots built in the year over all robots built, their
  median, mean and 95 % by hand; every panel of the page only its four lines (median, mean, 2.5 %, 97.5 %), nothing drawn
  over the bars; the page of numbers within the page (the unit "% of the robots built in the year" ran beyond it,
  shortened to "% of the robots built"). 42 tests of 04 and 6 of the settings, OK.
- **Deliberate faults in scratch copies of 04, each caught:** the robots built of all types of the year before; the next
  type's robots; the robots in use instead of built; a line drawn over the bars.
- **The page from his run of 2026-11-08** (200,000 draws, its files read only, the page written into the scratch folder):
  within his figure rules (page_problems); 2025: type 1 9.83 % (8.78–10.88 %), type 3 42.12 % (37.61–46.62 %); 2039:
  type 1 5.15 % (3.63–6.66 %), type 3 30.48 % (21.50–39.44 %); the six adding up to 100 % in every draw to 10⁻⁵
  (float32). Looked at.
- **The whole suite:** a run started on this state overlapped the edits of V218 and does not count; run on the state
  of V218.
- **Not covered:** his run of 04 with this code (it rewrites the page).

### V216. His runs of 00 and 04 read back (04 on his 200,000 draws of 02)

- **His words:** "I am runing 04", then "04 is done".
- **The times:** `params.xlsx` 09:24:08 (00); 04's draw files opened 09:24:47 to 09:24:48 (after putting the robot
  types together), written by 09:27:01; `summary.csv` 09:27:23; all 71 pages at 09:27 (the overview, 22 element pages,
  48 distribution pages and their numbers): each after the last change of the code (`04_stock_and_flow.py` 2026-11-07
  15:53:11, commit fa790ed 16:36).
- **The numbers** (`summary.csv`): the robots in use the article's, 10 M (2025) and 70 × 10⁹ (2040), in every draw;
  each type's share of the robots built in the year, 95 % of the draws: 2025 ±10.7 % of its mean for every type (type
  1 9.83 %, 8.78–10.88 %; type 3 42.12 %, 37.61–46.62 %), 2039 ±29.4 to 29.5 % (a year's share mixes its four quarters,
  each within ±10 % to ±30 %, whose modes move within the year: a little wider than one quarter's); 3,036 rows of the
  elements by part.
- **The pages looked at:** the overview, the types' shares (every type, type 3 too, on its own triangle), the robots in
  use by type, neodymium in use (by bodies and joint sets).
- **Not covered:** the pages not opened (the other element pages and their numbers).

## 2026-11-07

### V215. The sources on collection and on charging read myself (EVIDENCE.md E46.1, E46.2)

- **What:** the numbers the two research agents reported, checked against the sources themselves before any of them
  is shown to Matthias.
- **How:** web pages in the built-in browser (ADAC, Delta's specification tab, Conductix, WiBotic, Figure, arXiv, EUR-Lex
  Directive 2012/19/EU Art. 7 and Regulation (EU) 2023/1542 Arts 60, 61); PDFs from the files the fetch tool saved, their
  text extracted with pypdf of RAWCLICRecoveryModel's environment into the scratch folder (Reick et al., Kaewnoen et al.,
  Beckers et al., the DOE rule, the Global E-waste Monitor 2024 summary, Eurostat's WEEE page, the Commission's battery
  evaluation, the CWIT summary), each number found in its table or page.
- **Result:** every number checked as the agents gave it, with one sharpening: the Commission's 2–4 % a year of car
  batteries is its "conservative approach" beside the makers' 99 %, which leaves out exports.
- **Not covered:** the sources marked "agent only" in E46.1 and E46.2 (not opened by me); the UK's and Eurostat's ratios,
  which the agent computed.

### V214. The distribution pages of 04 and the elements by part in its summary (EVIDENCE.md E46)

- **His words:** "Ok it looks good. But I also want the distributions. Check with the data centers, what else has to be
  done"; to the table of what RAWCLICDataCenters' 07 has and 04 had not, "Yes, as recommended".
- **Tests first, seen to fail** (1 failure, 4 errors: `count_unit`, `mass_unit`, `triangle_bars`, `DISTRIBUTIONS_DIR`,
  the summary's rows by part missing), then passing:
  - the units by hand: 600,000 robots in thousands, 2.4 million in millions, 3.8 billion in billions (over the draws
    above 0); 2.5 × 10⁸ kg in kt, 1.2 × 10⁹ kg in Mt, 500 kg in kg, 0.5 kg in g;
  - a triangle's share in each bar by hand: 0 / 1 / 2 in four bars of 0.5, 0.125, 0.375, 0.375, 0.125;
  - the run on the made-up draws: its pages by exact name, the overview, the element pages, and in `distributions/`
    the robots in use by type, the types' shares and each element held, each followed by `_numbers.png`; 24 panels with
    numbers on the robots' and the shares' pages, 4 on an element's; the first panel by hand (robot type 1, 2025: its
    median, mean and 95 % in its unit); type 3's panel of 2039 Q4 by hand from the run's own random numbers (median,
    mean, 95 %); every panel's title on the page of numbers after it; the copper page's legend the two parts that hold
    it (bodies, joint sets), lithium's the battery packs; every page within his figure rules (page_problems) and no
    legend over a line;
  - the summary by part: 16 rows each of copper in the bodies, the joint sets, the battery packs; each mean over its
    draws above 0, by hand; the packs' copper '–'; the joint sets' copper of 2025 1.5 kg × the joint sets in use.
  43 tests of 04 and 6 of the settings, OK.
- **Deliberate faults in scratch copies of 04** (35), each caught after one check was changed: the robots' page with
  the next type, with the year before; the mass unit and the robots' unit one step too late; the triangle's bars summed
  instead of each; the page of numbers with one row only; the element page without the packs; every part's summary the
  bodies'; the types' page always at 2025 (passed at first: the check compared type 6, whose own draws, and so their
  median and mean, are the same at every time; changed to type 3, which shows the pairing; then caught); and the 26 of
  V213.
- **Sandbox** on the first 2,000 of his draws of 02: 04 ran, 71 pages (the overview, 22 element pages, 48 distribution
  pages and their numbers), all within his figure rules, no legend over a line. Looked at: the robots in use by type,
  the types' shares (each its triangle drawn over its bars), copper and magnesium in use, the page of numbers of the
  robots. Found and fixed: the ticks of a linear axis written by 02's number format (one decimal from 1) read "0.96, 1,
  1.1" for ticks 0.96, 1.04, 1.12; each tick now with the decimals its spacing needs (`panel_style`).
- **The whole suite:** 647 tests, OK (12 min 14 s), on this state.
- **Not covered:** his run at 200,000 draws; collection and electricity (researched, nothing built).

### V213. Every robot type its own triangle, put together by the rearrangement algorithm (EVIDENCE.md E44)

- **His words:** "I want that you developt an algorthym that has for all 6 types around 10% +- in 2025 and 30%+- in
  2040. All have to have close to this value!!"; to the linked prototype "NO type 3 is not triangular!! You are
  cheating"; to the rearranged prototype "Yes, build it". It replaces the conditioning of V212.
- **Prototypes before proposing** (scratch, 200,000 draws, my scripts): linked draw, every band right, type 3
  bell-shaped (shown; rejected); rearrangement from unlinked types, every type a triangle but two types correlated −0.99
  in 2039 and type 1 −0.31 from 2025 to 2039 (found myself, not shown); rearrangement from the linked draw, every type a
  triangle, the faults gone (shown; agreed).
- **Tests first, seen to fail** (2 failures, 9 errors: `type_points`, `type_ends`, `link_correlation`, `rearrange`,
  `unit_triangle`, `linked_scores`, `SHARE_TIMES`, `BALANCING_TYPE` missing; the setting's new limit), then passing:
  - the unit triangle by hand (−1, −0.5, 0, 0.5, 1 at 0, 0.125, 0.5, 0.875, 1); 95 % of it within ±0.776393;
  - the link by hand: 0.0872 / 0.2472 = 0.35275 (2025), −0.07 / 0.33 = −0.21212 (2040); a type 3 of 80 % (made up)
    refused;
  - the linked scores: no link gives the scores themselves; at 0.35 and −0.21 each pair correlated so (to 0.01), each
    with variance 1;
  - the rearrangement by hand: (1, 1), (−1, −1) become (−1, 1), (1, −1), both adding up to 0; on 1,000 draws each type
    keeps exactly its own draws and the largest sum falls below 5 % of before;
  - type 3 its own random number: other numbers for type 3 alone change the draws; the same numbers, the same draws;
  - the shares by hand: at the point h, mode × (1 + h × spread / 0.7764), the ends 12.880, 25.760, 38.640 % in 2025,
    2032.5, 2040; type 3 1 minus the others; every other type at its top in 2025, type 3 1 − 1.1288 × 58 %;
  - on 20,000 draws with the settings in force, at 1 January 2025 and all 60 quarters: the six add up to 1 to 10⁻¹²,
    all above 0, type 3 off its own draws by under 1 % of its half-width, each of the six types' draws within
    Kolmogorov's 99 % bound of its own triangle at every time, 95 % within ±10 % (2025) and ±29.8 % (last quarter) to
    3 %, every mean at its mode (0.5 %), type 3 against every other type in 2025, each type's point quarter to quarter
    correlated above 0.99;
  - a spread of 0.8 refused (the foot below 0);
  - the run on the made-up draws says what type 3 lies off its own draws, and every type's share of each year's robots
    built lies inside its triangle in every draw (type 3 within what the run says: 23 % of its half-width with 40
    draws).
  39 tests of 04 and 6 of the settings, OK.
- **Deliberate faults in scratch copies of 04** (26), each caught after one test was added: no rearrangement; the
  rearrangement with even weights, in the same order instead of the opposite, stopping after one column; the link
  without its mean, by the wrong sign, not checked; the unit triangle a straight line; the ends the spread itself;
  type 3 not its own draws (passed at first: no test checked type 3's own random number; the test above added, then
  caught); a new pairing every quarter; what type 3 lies off its draws not measured; the run not put together; the
  shares divided by their sum; type 3 its mode, the sum not one number; the spread not widening; the modes not scaled;
  and the ten of V208 and V211.
- **The delivered shares**, 200,000 draws with 04's own random numbers, at 1 January 2025 and every quarter: 31 s, the
  points 244 MB; the six add up to 1 to 2.2 × 10⁻¹⁶; type 3 off its own draws by at most 0.109 % of its half-width;
  the largest gap of any type's draws to its triangle 0.0022 (random draws: 0.0030 at 95 %); 95 % of the draws: every
  type ±10.0 % in 2025, ±16.8 to 16.9 % in 2030 Q1, ±23.5 % in 2035 Q1, ±29.8 to 29.9 % in 2039 Q4 (wanted ±10.0,
  16.8, 23.5, 29.8 %); every mean on its mode to 5 × 10⁻⁴; the lowest share 2.85 %; a draw quarter to quarter at
  least 0.9988, 2025 to 2039 Q4 0.59 (type 3) to 0.83; correlations 2025 −0.86 to +0.37, 2039 Q4 −0.71 to +0.28.
- **Sandbox** on the first 2,000 of his draws of 02: 04 ran (type 3 off its own draws by at most 1.571 % of its
  half-width with 2,000 draws), the article's robots at 1 January; its 23 pages within his figure rules, no legend over
  a line or a value; the overview looked at (type 3's band in the share panel as wide as the others'). Two preview pages
  looked at (scratch only, not part of 04): each type's share at four times, 200,000 draws, its own triangle drawn over
  them; the robots in use of each type in 2025, 2030, 2035, 2040: every type ±9.8 to 10.3 % in 2025 and ±27.6 to
  29.1 % in 2040, the six adding up to the article's in every draw.
- **The whole suite:** 643 tests, OK (12 min 56 s), on this state.
- **Not covered:** his run at 200,000 draws; the rearrangement's pairing is one of many that add up, chosen by its
  start (the linked draw), not the only possible one.

### V212. The robot types conditioned on adding up to 1, as RAWCLICRecoveryModel's condition_on_sum (EVIDENCE.md E44)

- **His words:** "All types have to have the same uncertainty!!! This is a must!!!", "The summ of the total has to be
  correct", "Check all the privous code. You have do it correct before!! It is an approximatoion", "All all code!!";
  to "Which do you want in 04?" (Conditioning or a linked draw of my own): "Conditioning".
- **The earlier code, read myself:** RAWCLICRecoveryModel `src/sampling.py` (`condition_on_sum`, `_systematic`,
  `triangular_density`; its default rule `condition`); RAWCLICStockAndFlow `code/03_02_adjustedflows.py`; this
  project's `02_composition.py` (`shares_drawn`, `RecipeDraws.parts_of`); RAWCLICDataCenters' rack classes;
  RAWCLICVehicleComposition's factors; RAWCLICVehicleTractionMotor `composition.py`.
- **Measured before proposing** (200,000 draws, my scripts; 95 % of the draws as a share of the mode, own triangle
  ±7.8 % in 2025 and ±23.3 % in 2040): type 3 as the rest ±5.6 % and ±31.7 %; conditioning types 1, 5, 6 ±7.7 % and
  ±23.2 %, types 2, 4 ±7.1 % and ±21.4 %, type 3 ±4.3 % and ±23.1 %, effective sample 0.872; the linked draw all six
  7.7 to 7.8 % and 22.8 to 23.3 %. Shown to him with the reason type 3 is narrower in 2025.
- **Tests first, seen to fail** (8 errors: `DERIVED_TYPE`, `triangle_density`, `systematic`, `condition_on_sum`,
  `conditioned_points` missing), then passing:
  - the density by hand (the triangle 0 / 1 / 2: 0, 0, 0.5, 1, 0.5, 0, 0 at −0.5 to 2.5; 10 at the mode of
    0.4 / 0.5 / 0.6);
  - three candidates by hand: densities (0.5, 0.5), (1, 0.25), (0, 1), weights 0.5, 0.5, 0, kept 0, 0, 1 at u =
    0.25, effective sample 2/3;
  - the weights 0, 3, 1, 0 give 1, 1, 1, 2 at u = 0.3, 0.5 and 0.999: in proportion, never one of weight 0;
  - no candidate adding up stops with a message;
  - a case known exactly: two shares, each its triangle 0.4 / 0.5 / 0.6, adding up to 1; the kept follow f(x)², so
    their 2.5 %, 25 %, 50 %, 75 %, 97.5 % points are 0.43684, 0.47937, 0.5, 0.52063, 0.56316 (drawn without the
    condition 0.42236 at 2.5 %), met to 10⁻³ on 200,000 draws; the effective sample 8/9 to 0.005;
  - with the settings in force on 20,000 candidates: the six add up to 1 to 10⁻¹², type 3 inside its own triangle in
    2025 and every quarter, effective sample above 0.8, every type spread, every mean at its mode (to 0.5 %), no type
    wider than its own triangle, in 2040 every type within 10 % of its own triangle, type 3 negatively correlated with
    each other type, the spread of 2040 more than twice that of 2025;
  - a spread of 90 % (made up): candidates with type 3 below 0 occur and none is kept;
  - the run on the made-up draws prints the effective sample, and type 3's share of each year's robots built lies in
    every draw between the lowest and the highest bound of its triangle in the year's quarters.
  45 tests of 04 and the settings, OK.
- **Deliberate faults in scratch copies of 04, each caught** (23): no conditioning, every weight 1; the density squared;
  the arithmetic mean over the years; only 2025 weighed; the density not 0 outside its triangle; the resampling without
  its random number; all draws dropped without a message; the run not conditioned; the effective sample by the kept
  draws, not the weights; the shares divided by their sum; type 3 drawn on its own, the sum not one number; one random
  number for all types; the spread not widening; the modes not scaled to what type 1 leaves; the three lifetime factors
  each ignored (V211); and V208's seven. The fault "the totals summed from the types" of the morning is dropped: with the
  sum exact it is the same as the code.
- **The delivered shares**, 200,000 candidates with 04's own random numbers (seed 1, the resampling's u 0.5857): the
  six add up to 1 to 2.2 × 10⁻¹⁶ in every draw; every mean on its mode (to 3 × 10⁻⁴ of it); 169,806 distinct draws,
  effective sample 0.8716; 6.44 % of the candidates outside type 3's triangle at a workbook year, weight 0; no kept draw
  outside it in any quarter. The bands (95 % as a share of the mode), 2025 / 2040: type 1 ±7.7 / 23.2 %, type 2
  ±7.1 / 21.2 %, type 3 ±4.2 / 23.1 %, type 4 ±7.2 / 21.5 %, type 5 ±7.8 / 23.3 %, type 6 ±7.7 / 23.2 %; 2030 and 2035
  in METHODOLOGY.md, step 2 of 04.
- **Sandbox** on the first 2,000 of his draws of 02, copied into the scratch folder: 04 ran, effective sample 87.6 %,
  the article's robots at 1 January; its 23 pages within his figure rules, no legend over a line or a value; the overview
  looked at (the share panel: every type's band widening from 2025 to 2040). A preview page of the robots in use of each
  type in 2025, 2030, 2035 and 2040, the distribution of the draws, looked at (scratch only, not part of 04): the six add
  up to the article's in every draw; type 3 ±4.2 % in 2025, ±20.7 % in 2040, the others ±7.0 to 7.9 % and ±20.0 to
  22.5 % (robots in use mix the years they were built in).
- **The whole suite:** 643 tests, OK (12 min 55 s), on this state with the lifetimes of V211.
- **Not covered:** his run at 200,000 draws; the approximation of the path (the geometric mean over the workbook's four
  years) not compared with another weighting.

### V211. The lifetimes in 04 drawn per draw: 30 % shorter, 20 % longer (EVIDENCE.md E45)

- **His words:** "Is the lifetime also with uncertainties. I want that is is 30% short and 20% longer. Also with the
  batteries"; on the sandbox's overview "where are the uncertainbties", "I see NO uncertainty bads".
- **Tests first, seen to fail** (3 failures, 4 errors; then 3 errors for the joints), then passing: the setting
  `lifetime_factor` 0.70 / 1.0 / 1.20 and refused (a single number, a 0, out of order); by hand, at the factor 0.7 the
  robots of 4.9 years as many left as at 7 years with 1 (0.6), at 1.2 those of 8.4 years (0.6), none gone before 3.5
  years, all gone at 12; the packs at 80 % and 0.7, 560 charges as 800 at 1 (0.4); the joints at 1.2, 12,000 hours as
  10,000 at 1 (0.870); in one chunk the robots built in 2025 and retired in 2030, the packs and the joint sets worn out
  in 2030 differ from draw to draw. 37 tests of 04 and the settings, OK.
- **Deliberate faults in scratch copies of 04, each caught:** the robots', the packs' and the joints' factor each
  ignored; and the eleven of V210.
- **Sandbox** on the first 1,000 of his draws of 02: 04 ran, its 23 pages within his figure rules, no legend over a line
  or a value; the overview looked at and sent to him. Bands (mean, 95 %): robots built 2025 2.49 M (2.26–2.86 M), retired
  2025 0.89 M (0.66–1.26 M), retired 2039 159 M (45–438 M); joint sets built 2025 7.24 M (6.15–8.83 M), worn out 2035
  471 M (335–676 M); packs built 2025 52 M (37–74 M), worn out 2035 1.34 B (0.65–2.30 B); the robots in use the
  article's in every draw. One chunk of 20,000 draws counted in 9.3 s (4.5 s before: the robots now have one survival
  a draw), peak memory 2.0 GB: about 1.5 minutes of counting at 200,000 draws (an estimate, not run).
- **The whole suite:** not run on this state alone (a run of the morning, its output last written at 11:56, stopped
  in the middle of 02's tests when the types changed); run on the state of V212, which holds these lifetimes (V212).
- **Not covered:** his run at 200,000 draws; the packs in use still with almost no band (single runtimes), the robots in
  use with none (the article).

### V210. The robot types' shares in 04: every type drawn, one of the six bought (EVIDENCE.md E44)

- **His words:** "All have a triangular distribution, where I assume that gets larger over time. so 5% towards 15%",
  "I buy one of the six different types. SO the items are correlated", "the last type is not just the rest to 100%",
  "Check how we have done it before"; to the corrected table "Yes, build it".
- **How it was done before, read myself:** RAWCLICStockAndFlow `code/03_02_adjustedflows.py`
  (`sample_future_segment_share_inflow_draws`), `documentation/MODEL_DESCRIPTION.md` § 7.1, `documentation/HANDOVER.md`
  (2026-10-05, the collection share); RAWCLICDataCenters `documentation/claude/EVIDENCE.md` § 4.1 and METHODOLOGY step
  B; RAWCLICRecoveryModel `documentation/DESIGN_monte_carlo.md` § 4.
- **Measured before proposing** (200,000 draws, my script): the six modes adding up to 85 % in 2025 lift every type
  through the division (type 1 11.77 % instead of 10 %); scaled to 1, each mean stays on its mode.
- **Tests first, seen to fail** (3 failures, 7 errors: the new settings and functions missing), then passing:
  the settings (`research_share` 10 % and 5 %, `type_share_spread` 5 % and 15 %, the two old triangles gone; refused: a
  share of 0 or 1, years other than 2025 and 2040, a spread of 0 or 1, one year only); the modes by hand (2025: 10, 24,
  42, 12, 6, 6 %; 2032.5: 7.5 % and the workbook's 26.5, 37.5, 15, 5, 4.5 % × 92.5 / 88.5; 2040: 5, 25, 30, 30, 5,
  5 %; adding up to 1 every quarter); the spread 5, 10, 15 % in 2025, 2032.5, 2040; every type at the same point of its
  triangle (middle, foot, top) gives the modes; type 1 at its top and the others at their foot in 2025: 0.105 / 0.96 =
  10.94 %; on 20,000 draws the shares add up to 1, all above 0, every type spread, its mean at its mode (to 3 × 10⁻⁴),
  the spread in 2040 more than twice that of 2025, type 2 and type 3 correlated below −0.3; in one chunk of 04 every
  type's robots of 2040 differ from draw to draw. 35 tests of 04 and the settings, OK.
- **Deliberate faults in scratch copies of 04, each caught:** the shares not divided by their sum; one random number for
  all types; the spread not widening; the modes not scaled to what type 1 leaves; type 3 the rest again; and, again, the
  seven faults of V208 (draw i not paired, the outflow without the cohorts' losses, packs rounded, joints in the body,
  the packs' fade ignored, zeros in the statistics).
- **The delivered shares** on 200,000 draws with 04's own random numbers: the sum 1 to 4.4 × 10⁻¹⁶ in every draw;
  every mean on its mode (type 3 2040 29.99 %); the 95 % band a little narrower than the triangle (2025 type 1 9.60–10.41
  % against 9.50–10.50 %; 2040 type 1 4.38–5.65 % against 4.25–5.75 %, type 3 27.13–32.84 % against 25.50–34.50 %), the
  extremes a little beyond it (2040 type 1 3.95–6.28 %); correlations in 2025: type 3 with types 1, 2, 4, 5, 6 −0.38,
  −0.68, −0.42, −0.31, −0.31; type 2 with the small ones −0.04 to −0.10; the small types among themselves +0.04 to +0.13
  (when types 2 and 3 are low, all the others rise).
- **Sandbox** on the first 1,000 of his 200,000 draws of 02, copied into the scratch folder (the scratch copy of
  yesterday was emptied overnight): 04 ran, the article's robots at 1 January, every type's robots with a band (type 1
  2025 1.00 M, 0.96–1.04 M; 2040 3.77 B, 3.33–4.25 B); its 23 pages within his figure rules, no legend over a line or a
  value; the overview looked at.
- **The whole suite:** run once with the lifetimes of V211 built on top (V211); the run started on this state alone was
  stopped when the lifetimes came.
- **Not covered:** his run at 200,000 draws.

## 2026-11-06

### V209. His runs of 00, 01 and 04 read back (04 on his 200,000 draws of 02)

- **His words:** "04 has run".
- **The times:** `params.xlsx` 16:31:36 (00), `figures/schemas/overview_1.png` and `_2.png` 16:31:49 to 16:31:50 (01),
  04's draws 16:32:56 to 16:32:57, `summary.csv` 16:33:08, its 23 pages 16:33:09 to 16:33:17: each after the last change
  of the code (`04_stock_and_flow.py` 15:57:51, `01_schemas.py` 15:58:17, `src/params_schema.py` 15:52:47). It read 02's
  draws of his run of 13:35 to 13:37 (V202). None of 04's files evicted by iCloud (`stat`: not dataless).
- **The files:** sizes as 200,000 draws give them (`units_in.npy` 216,000,128 bytes = 200,000 × 15 × 3 × 6 × 4 + its
  header; `elements_stock.npy` 844,800,128); 3.09 GB in all.
- **The numbers, by hand:** the robots in use the article's at every 1 January (10 M, 23 M in 2030, 1.0 B in 2035, 70 B
  in 2040); the six types adding up to 70.0 B in 2040 (3.77, 17.98, 22.03, 19.39, 3.50, 3.34 B); the packs in use at 1
  January 2025 113 M = 10 M × (10 % × 12 + 20 % × 7 + 50 % × 12 + 10 % × 12 + 5 % × 6 + 5 % × 24), the same in every
  draw (types 1 and 3 both 12 packs a robot, so the research share does not move it); in 2040 223.9 B, above the need of
  213.6 B (the robots of each type × 5, 1, 4, 3, 3, 6), the packs of the years when more were needed still in use; built
  in 2025 2.43 M robots, 0.83 M retired, as the sandbox (V208). Magnesium held in 12.1 % of the draws, indium 98.5 %,
  every other element 100 %.
- **Looked at:** the overview and all 22 element pages: every text within its page, no legend over a line or a written
  value, the world's values dashed or written in the panel, dysprosium's and terbium's pages saying they have none.
- **What the pages show** (the mean over the draws above 0 against the world's 2025 value): the inflow above the world's
  production in a year from 2033 (neodymium, praseodymium), 2034 (lithium, magnesium), 2035 (titanium, cobalt, nickel,
  gallium), 2036 (aluminium), 2037 (copper, palladium), 2038 (tantalum), 2039 (boron, silver, gold, niobium); never for
  manganese, tin, lead, indium; the stock above the world's reserves from 2039 (neodymium) and 2040 (cobalt, nickel,
  praseodymium). Dysprosium 6.0 Mt and terbium 278 kt in use in 2040, with no world numbers to set beside them.
- **Removed on his word** ("Yes, remove them"): the first 04's `data/stock_and_flow/robots.csv` and
  `figures/stock_and_flow/stock_and_flow.png` (15:04), no code naming either, moved by exact name into the Trash; the
  folders hold only the new 04's files.
- **Not covered:** his pages checked by eye, not by `page_problems` (that ran on the sandbox's pages, V208).

### V208. Stage 04 rebuilt as RAWCLICDataCenters' 07: robots, joint sets, battery packs and their elements (EVIDENCE.md E42, E43)

- **His words:** "I want the same figures as for the datacenters, but expand them all the essential critcial and
  statigic elements. Also have real lifetimes not something fixed like this. I want to see uncerttainites", "Add also the
  limit in stock and production like for the data centers", "Yes, build it", "No look at the robots as a unit with
  exception of the batteries", "Have at least so many battery packs ready for use as it is needed to have them for 1 day
  to switch. So they can recharge slowly", "Yes, replace joints".
- **07 read again myself** for its method and its pages (RAWCLICDataCenters `07_data_center_stock_and_flow.py`:
  `follow_target`, `check_balance`, `to_years`, `log_panel`, `world_reference`, `mass_label`, `mass_text`,
  `save_figure`, `plot_scenario`, its sheet ElementReference as `parse_scenarios` reads it); USGS's data file read for
  the world rows of magnesium, titanium and indium, their units and notes ("Gross weight of magnesite (magnesium
  carbonate)", "titanium dioxide (TiO2) content").
- **Tests:** `tests/test_stock_and_flow.py`, 26 tests, written after the code (not first), so each was made to fail by
  a deliberate fault instead (below). By hand: a lifetime's survival at 4.9, 7, 8.5 and 10 years (1, 0.6, 0.15, 0); a
  triangle's value at 0.1 and 0.4 (6 and 7 years); a joint set at 10,000 hours (0.870 left) and a pack at 800 charges
  at 80 % and at 1,000 charges at 75 % (0.4 left each); the quarters between the article's years (2025 Q2 √(10 M × 11.6
  M)); units living one year, 100 in use (25 in and 25 out every quarter); a falling target (inflow 0, the stock 75 above
  the target 40, back on it three quarters later); the robots of 1 January 2025 adding up to 10 M, built at the article's
  16 % a year; his workbook's shares, runtimes and energy densities as he wrote them; the types' shares at 2025, 2032.5
  and 2040 (type 3 50 %, 41.5 %, 30 %), adding up to 1 at every point; the packs a robot holds in 2025 (12, 7, 12, 12,
  6, 24) and 2040 (5, 1, 4, 3, 3, 6); one chunk of 30 draws with the settings in force adding up (the article at every
  1 January to 10⁻¹², the joint sets as the robots, the packs at least the need; 2025's retired between 0.5 and 1.2 M);
  the statistics over the draws above 0 ("held in"); the masses written as 07's; the legend moved off a line and a
  written value; the world's numbers read (copper 23 Mt, palladium "at least", magnesium 1,100 kt and its reserves by
  its formula, titanium at least, indium no reserves, no dysprosium or terbium); 04 run on made-up draws of 02 (40
  draws, four elements): every kg by hand, draw i paired (aluminium t × (1 + i / 40) kg a robot of type t), the joint
  sets' copper, the packs' lithium, nothing else in them, neodymium 0 in every draw and no page, the summary's "–", the
  four pages within his figure rules and no legend over a line or a value; without 02's draws it stops; a column of 02
  that is no kind of part stops it. The settings' tests with 04's nine settings and the two world files, and the
  settings refused (a year missing, out of order, 0, a single number, a capacity of 100 %, a share above 1, 25 or 0
  hours, a runtime missing or 0).
- **Deliberate faults in a scratch copy of 04, each caught** (the project's file not touched): draw i not paired (the
  made-up draws reversed); the outflow without what the cohorts lose (04 stops); the packs rounded instead of rounded up;
  type 3 the workbook's share instead of the remainder; the joints counted in the body; the packs' fade ignored; the
  zeros kept in the statistics. In `check`, on one chunk: an outflow, a stock of all robots, of one type, of the joint
  sets 0.1 % off; packs 1 % below the need; an inflow below 0: each named.
- **Hand check by another route** (the sandbox run, draws 1 and 2): each of the 22 elements at 1 January 2025 from 02's
  whole-robot table plus the extra packs (packs a robot holds − 1 times the columns "Battery pack: …"), the robots of
  each type from the shares written out: 04's files agree to 7.2 × 10⁻⁸ (float32); neodymium 4,183,052 kg and 3,039,812
  kg both ways.
- **Sandbox run** on the scratch copy of 02's draws (1,000 draws of the six types, built from his builders' parts
  files): 9 s; 22 element pages; "no world production or reserves for Dysprosium, Terbium". One chunk of 20,000 draws
  counted in 4.5 s, checked in 0.1 s: about a minute of counting at 200,000 draws (an estimate, not run); its files about
  3.1 GB (arithmetic).
- **Looked at:** the overview and all 22 element pages. Fixed on looking: indium's dashed world production ran under
  the legend (now the legend moves to the first corner where no line or written value lies under it, tested); a single
  line held in fewer than all draws had no legend to say so (now it has one, "stock, held in 99 % of the draws"). Every
  page then within his figure rules (`page_problems`) and no legend over a line or a value, all 23 checked as saved.
- **The whole suite:** 630 tests (762 s), all OK, on the final code (01's overview box of 04 first ran one line past its foot; seen on the page, its words shortened, `TestOverviewBoxes` then OK).
- **Not covered:** his run on his 200,000 draws of 02; the robots' own numbers have no band (the article fixes the
  stock, the lifetime is spread among the robots, as 07); the runtimes of types 1, 3 and 5 (2 / 2 / 4 h) and the
  charges to 80 % (500 / 800 / 1,000) kept on his word ("Yes, keep them"); type 2's runtime of 24 h in 2040 gives one pack a robot, which
  leaves it no time to charge; the joint sets and packs of a retired robot go on in a new one (07's approximation,
  their flows slightly low); dysprosium and terbium without world numbers, indium without reserves, magnesium's
  reserves and titanium's by their formulas (E).

### V207. The joint actuators' rated lives researched (EVIDENCE.md E43)

- **His words:** "How is it with the joint motors. How do the limit".
- **How:** a reading agent read reducer, screw, motor and robot makers' pages (no PDF); I read again myself
  Nabtesco's press release ("market standard of 7,000 hours to 10,000 h", for humanoid robots and cobots), Harmonic
  Drive's CSG page ("L10 of 10,000 hours", "42% longer" than CSF) and AgiBot's A3 page ("a designed lifespan of up to 3
  years").
- **Found:** E43. No humanoid maker publishes a joint life; strain-wave gears 7,000 to 10,000 h, planetary and
  robot-arm gearboxes 30,000 to 40,000 h, at rated torque.
- **Not covered:** the reducer makers' PDF catalogues (the life formula, the CSF and CSD figures); the joints' real
  torques in use; nothing entered.

### V206. Stage 04 built: the article's robots in use, built and retired (EVIDENCE.md E42)

- **His words:** "Use the numbers in the article and not what you have research", "Do exactly what has been done for
  the datacenter", "It gives 70x10E9", "We have damit to implement what is in this artcle and nothing else!".
- **The article read again myself:** the economics explorer with its preset "AI 2040 Plan A Scenario" active, its
  inputs `cs_delta_robot` 0.20 ("Robot depreciation (δR) 5-year robot life") and `delta_R` 0.10 ("δR (robot capital
  depreciation)"); its model/costSide.js: "new(t) = S(t+1) − S(t)·(1−δ)" booked forward, the stocks "Jan-1
  (start-of-year)", "delta_robot: 0.20, // 5-year robot life", its stock in the formula `R_phys`, "human-equiv physical
  workers"; the main page: "AIs and robots can work 24/7".
- **Tests first, seen to fail** (04 missing), then passing: `tests/test_stock_and_flow.py`, 9 tests: the settings hold
  the article's 16 values and 0.20 and are checked (a year missing, no robots, one year only, 0 and 1 as the
  depreciation); by hand, 2025 built 11.6 M − 0.8 × 10 M = 3.6 M, retired 2.0 M; 2039 built 70 B − 0.8 × 29.7 B =
  46.24 B; every year in use + built − retired = the next 1 January; never below 0 on a made-up falling path, as the
  article's max(0, …); without depreciation built = the growth; 04 run into a temporary folder: 0, its table 2025 to
  2040 (2040 without flows), its page within his figure rules (`page_problems`). 01: the overview names every stage
  (now five), its fifth stage box and output box, "Open: nothing."; its list of words no page may show takes the sibling
  files' numbers as they stand in the headings ("04_)", "07_,"), so that it no longer catches 04's own name. The
  settings' tests with 04's four settings.
- **Deliberate faults, each caught** (the file restored, its hash compared): built without the article's 80 % ("1600000.0
  != 3600000.0"; the balance fails in 2025); nothing retired (the balance fails, and 04 stops: 1 != 0).
- **Looked at** (drawn into the scratch folder): 04's page (the three series on one logarithmic axis from 10⁶ to 10¹¹,
  every year a tick, the legend and the source within the page); 01's overview page 1 (five stages, each text within its
  box; 04's output box).
- **The whole suite:** 613 tests (775 s), all OK.
- **Not covered:** his runs of 00 (the register of the settings), 01 (the overview) and 04.

### V205. The share of humanoids in ai-2040.com's robots researched (EVIDENCE.md E41)

- **His words:** "Yes, a share".
- **How:** a reading agent read market researchers', makers' and banks' pages (no PDF); I read again myself IDC's
  2025 shipments (about 18,000, about 508 % up; its definition with wheeled forms), Barclays' installations (about
  2,000 in 2024, 15,000 in 2025, 60,000 projected for 2026), Morgan Stanley's article (more than 1 B in use by 2050;
  China 302.3 M, US 77.7 M) and podcast (US 40,000 by 2030, 8 M by 2040, 63 M by 2050). The share computed by a
  scratch script (installations summed, flows geometric between the sources' years, the article's robots of E40).
- **Found:** the share rises from 0.17 % (start of 2026) to about 3.5 % (2030) and falls to about 0.15 % (2040).
- **Not covered:** retirements before 2030 (none assumed; with a 5-year life the 2025 robots leave in 2030, a few
  percent of the 2030 stock); the PDFs (Goldman Sachs, BofA, Citi GPS, Morgan Stanley's fact card); nothing entered.

### V204. ai-2040.com's robots read first-hand (EVIDENCE.md E40)

- **His words:** "Get the article, which was already the bases for the work on the stock and flow modeling of the
  datacenters. Read it and use the stock numbers for the humanoid robots".
- **How:** RAWCLICDataCenters' METHODOLOGY § 11 and EVIDENCE § 23 read for which article and which data; in the browser
  pane the economics explorer (its preset "AI 2040 Plan A Scenario" checked active, the Input Table's rows Robots,
  Human-equivs per Robot, the shares by country), the main page's source (searched for robots, humanoid, form factor,
  the footnotes 103, 146, 174) and the authors' spreadsheet's sheet `plan-a-side-panel` (every row label: no robot
  count). Nothing downloaded.
- **Found:** E40. The article's robots are all robots, of every form; 10 M in 2025, 70 B in 2040; no humanoid share.
- **Not covered:** the article's PDF and supplements other than the economics one; nothing entered.

### V203. His run of 03 after E38 points 2 and 4 read back

- **His words:** "03 is done".
- **03:** 94 pages in `figures/comparison/`, 13:41:31 to 13:42:10, all after 02's draws (13:37:57); as many as before
  (V197); no iCloud copy "… 2".
- **Looked at:** comparison_elements_9, gallium in the sensors of the six types (cameras and other sensors stacked,
  the median, the mean and the 95 % interval in every panel, type 6's the LiDARs' alone, every text within its panel).
- **With V200 to V202 his runs of today are read back.** The five tests that read his parts files on disk and failed in
  V199 pass on his new files: the two builders' comparisons and 01's "the real file holds together" (V200), and the
  page check of the six types, 02 and 03 (2 tests, 102 s, OK). Nothing committed.

### V202. His run of 02 after E38 points 2 and 4 read back

- **His words:** "02 run complet, run 03".
- **02:** the draws of the six types 13:35:02 to 13:37:57 (`data/consolidated/`, `data/parts_taken_apart/`, 20 files a
  type, none older than his six parts files of 13:02 to 13:03); 138 pages in `figures/composition/` and 156 files in
  `figures/parts_taken_apart/`, all of his run; no iCloud copy "… 2".
- **The new places in his 200,000 draws** (each kind over all its regions): the temperature sensors 100 % of the draws
  (type 5 89.9 %: its hydraulic robots); the force and torque sensors 2.6 / 2.1 / 0.8 % (types 2 to 4), the tactile
  sensors 5.2 / 3.3 / 2.4 / 19.9 / 19.9 % (types 2 to 6), the touch screens 1.7 % (type 1) and 0.6 % (type 3), the 4G/5G
  modems 1.5 / 1.5 / 0.8 % (types 2 to 4), the satellite receiver 1.0 % (type 2); the circuit boards' titanium, the
  joints' capacitors', in every draw (type 5 90 %), median 6.2 / 9.1 / 10.0 / 7.6 / 13.4 / 11.1 g (types 1 to 6).
- **The places against the elements**, every element of every type, draw by draw: the largest difference 3.0e-7 of the
  element's largest draw (the stored numbers' rounding).
- **Looked at:** type 2's page 1 of where the critical elements sit (copper): the rows "temperature sensors" (100 %),
  "force and torque sensors, arms" (2.6 %: above 2.5 %, so a row in his run, none in the sandbox's 1,000 draws at
  2.0 %), "tactile sensors, arms" (5.2 %), in their colours, every number apart.
- **Not covered yet:** his run of 03 (running).

### V201. The numbers for the stock and flow model researched (EVIDENCE.md E39): runtime, battery exchange, lifetime, infrastructure

- **His words:** "While 02 and 03 run, can you investigate some numbers for the stock and flow model …" (E39).
- **How:** his sources and workbook searched first (report 03; the sheets Material Trajectories and Market Units);
  RAWCLICDataCenters' EVIDENCE § 23 (ai-2040.com) and RAWCLICStockAndFlow's MODEL_DESCRIPTION read for how they treat
  lifetimes; three reading agents read the makers', users' and analysts' pages (no PDF, no download, no sign-in); I read
  again myself in the browser pane: Agility's investor exhibit at sec.gov (the 5-year useful life, 31,000 h, 120 h a
  week; Digit 4's 4 h and its charge ratios), Agility's FAQ (dock 208–240 VAC 25 A, Wi-Fi, workcell), CRU (7 years, 5
  to 10), ai-2040.com's economics explorer ("5-year robot life", "3-year chip life"), the Strange Review (200–500
  cycles, 3 to 5 months, and what it rests on), Fourier's GR-3 and N1 manuals (≥500 cycles at 80 % DOD; ≥800 cycles to
  80 % SOH), Figure 03's pages (2.3 kWh, 5 h, 2 kW, inductive stand). Wood Mackenzie's page not found again by me.
- **Found:** E39's four tables. Only Fourier states a cycle life; no maker states a lifetime in years (Agility's 5
  years an illustrative assumption); his report 03's 200 to 500 cycles and 3 to 5 months rest on the newsletter alone;
  no source gives a dock's or station's mass, robots per dock, or spare packs per robot.
- **Not covered:** the PDFs (IFR's World Robotics method, Goldman Sachs, Morgan Stanley's Humanoid 100, the Atlas spec
  sheet, AgiBot G2's datasheet); nothing entered in any file or code.

### V200. His runs of the six builders and of 01 after E38 points 2 and 4 read back

- **His words:** "I have run make 1 to 6 and now 01 runs", then "I am runing 02".
- **The six parts files:** written 13:02:27 to 13:03:38, all after the last change to the code (12:44:58, the
  deliberate faults' restoring, the hashes the same); no iCloud copy "… 2". Each equal, sheet by sheet and cell by cell,
  to what its builder writes into a temporary folder (types 1 to 6; types 1 and 2 also by their tests
  `test_what_it_writes_equals_the_data_file_on_disk`, now passing, and 01's `test_the_real_file_holds_together`).
  Their temperature sensors: every robot of the six files but type 5's two hydraulic Atlas versions (31, 102, 99, 85,
  3 of 5, 5); the makers' sensors 27 rows as E38's table (1, 12, 6, 6, 2, 0; 8 written 'A or B'); the two capacitor
  numbers in every file.
- **01:** 45 pages 13:04:03 to 13:04:11, all after the six files; "No fault found in the inputs". Looked at: type 3's
  page of where its kinds of part sit (mark 6, "Head joints"; the hip joints "a driver board and its sensors (encoders,
  temperature sensors)"; every text within the page) and the faults page 1.
- **The two estimates set to his rule** (V199) are in his files by his run of the builders; his word on them not yet
  given.
- **Not covered yet:** his run of 02 (200,000 draws, running) and of 03.

### V199. The missing sensor kinds and the joints' capacitors built (EVIDENCE.md E38 points 2 and 4); the three constants removed

- **His words:** to "Go ahead with points 1 to 3 as proposed?" (the table of the sensors robot by robot, the table of the
  capacitors with the KEMET/YAGEO declaration's flag, the three constants no stage reads): "Yes, all three".
- **Point 3:** 01's `JOINT_SHARE_ON_WHEELS`, `ENERGY_PER_KG_ON_WHEELS` and `SCREEN_MUTED` removed by exact name; `grep`
  over every `.py` afterwards: no reader.
- **Tests first, seen to fail** (10 of 13: `sensor_count`, `TITANATE`, `E38_SOURCES`, `CAPACITORS` missing; the new
  kinds None; no temperature sensors in the builders' files), passing after the build: `TestNewSensorsAndCapacitors`
  (02: the kinds by their car elements; the temperature sensors in every joint; every kind its own colour; a number
  fixed, 'A or B' one or the other about half the draws each (20,000 draws), drawn whole from a constant with the
  triangle's mean; barium titanate by the formula; type 1's temperature sensors' cobalt in every draw, its barium in
  the joints alone, the circuit boards' titanium to its barium as the formula, draw by draw, 1e-9) and
  `TestE38SensorsAndCapacitors` (the six builders: every robot with electric joints its temperature sensors, two or
  one a motor where the SDKs say so, else drawn; the makers' sensors robot by robot with their numbers, kinds and
  regions; no other robot holds them; their car elements; the capacitors' two shared numbers in every file; every E38
  source code cited on the sheet Sources; 01's check of a number written 'A or B').
- **01 stopped two of my proposed estimates** (his rule, every estimate at least half to 1.5 times its mode): the
  temperature sensors 1 / 1 / 2 a motor, set to half to twice the joint motors, mode one a motor; the tactile arrays
  not counted 2 / 10 / 10, set to 2 / 6 / 10. The MagicBot Z1's 1 / 1 / 2 kept: a drawn number of a sensor its maker
  states is cut at one, a stated limit (01's `floor` for 'Number: …'). Both changes to be confirmed by him. **Found
  by 01 in the test too:** type 1's Asimov 2, copied from the Asimov 1, dropped its drawn number; its builder copies it
  now.
- **Deliberate faults, each caught** (each file restored, its hash compared): the temperature sensors' kind left out
  (no kind: "None != 'temperature sensors'"; 02 stops: "its car sensor elements (temperature sensor) are no kind of
  sensor"); 'A or B' blended to its mean ("Items in the first set but not the second"); the capacitors added on top of
  the board instead of out of its glass and epoxy (`TestHandCalculations`' electronics wholly drawn: 300 of 300 draws
  mismatched); 01's whole-number condition of 'A or B' removed ("[] is not true"); the Unitree H1 set to two a motor
  ("38.0 != 19.0").
- **Older tests set to it:** the two of type 2's robots whose makers name no sensor (their E38 rows apart, as E31's);
  titanium now also the circuit boards' (the capacitors); the combinations of car elements with the new ones; indium
  also the touch screens'; 01's small test file with the two capacitor numbers; the words of what the hip joints hold
  kept as short as before ("a driver board and its sensors (encoders, temperature sensors)": longer, they pushed type
  3's last text off its page).
- **The sandbox** (scratch folder): the six builders wrote their files there, 02 drew the six types at 1,000 draws on
  them and 03 compared them: both 0 (no fault), 294 and 94 pages, no page against his figure rules (`page_problems`).
  Held, of the draws: the temperature sensors 100 % (type 5 90.9 %: its hydraulic robots have no electric joints); the
  force and torque sensors 2.0 / 1.4 / 1.1 % (types 2 to 4), the 4G/5G modems 1.7 / 1.9 / 0.3 %, the touch screens 2.0 %
  (type 1) and 0.3 % (type 3), the satellite receiver 1.5 % (type 2), the tactile sensors 4.1 / 3.3 / 2.9 / 17.8 / 17.7 %
  (types 2 to 6; each kind over all its regions, measured from the draws). Below 2.5 % a place draws no row, as every place (HELD_SHARE): those are in the draws, not on the
  pages. The circuit boards' titanium, the capacitors', in every draw, median 8.6 g a type 2 robot (its barium about 25
  g by the formula, not an element of interest).
- **Looked at:** type 2's pages of where the critical elements sit 1 to 3 (copper, aluminium, silver, gold: the rows
  "temperature sensors", "tactile sensors, arms" in their colours, the numbers apart), type 2's element page 1
  (titanium in the alloy and in the sensors: **the capacitors' titanium has no panel there**, it shows on the pages of
  where it sits and the means pages; for him to decide).
- **The colours** (CIE Lab difference to the nearest other colour of those pages, computed with all chosen):
  temperature sensors `#EE3377` 30.4, force and torque sensors `#225522` 23.7, tactile sensors `#FFAABB` 24.9, touch
  screens `#EECC66` 24.0, 4G/5G modems `#BB5566` 30.4, satellite receivers `#997700` 20.5; the joint encoders' since 23.7.
- **The whole suite:** 604 tests (749 s), 5 failures, each reading his parts files on disk, which have none of the new
  rows until he runs the builders: the page check of the six types (02 and 03: 02 stops on the missing capacitor
  numbers), type 1's and type 2's builders against their files, 01's "the real file holds together".
- **Not covered:** his runs (the builders, 01, 02 at 200,000 draws, 03: read back in V200 to V203); the KEMET/YAGEO
  declaration's numbers in this public repository's builder: asked again, "Yes, they may" (2026-11-06).

### V198. The head joints a kind of their own, the sensors by where they sit (EVIDENCE.md E38 points 6 and 7)

- **His words:** "I want thigs resolved. Gallium stays with the magnets, as it is more than for the sensors"; to the
  table of four open items, "Yes do it and if all open items are solve check also for obsolete code".
- **Tests:** `TestHeadJoints` written first and seen to fail ("KeyError: 'headjoints'"; "'headjoints' not found" among
  neodymium's kinds), passing after the build: the kind "Head joints" with mark 6, a spot and a colour of its own; the
  joints named head or neck in it; part group Joint drives, body region Head; type 1's head neodymium in the head joints
  and none in the kind Head. Written with the build: `TestSensorsByKind`'s `test_a_sensors_place_its_kind_and_region`
  (type 1's cameras and LiDARs placed with the head, the encoders without a region) and
  `test_a_sensor_of_no_region_is_a_fault` (a camera's region set to 'Neck': `check_parts` names it); the older place
  tests set to kind and region; `test_schemas`' list of kinds with "Head joints".
- **Deliberate faults, each caught** (each file restored after, its hash compared): the head joint sent back to the kind
  Head in 01 (`TestHeadJoints`: "'head' != 'headjoints'", "'head' unexpectedly found" among neodymium's kinds); the region
  left off a sensor's place in 02 ("'Boards and components: cameras' != 'Boards and components: cameras, head'").
- **The whole suite:** 591 tests (732 s), one failure, the one expected: the type 2 builder's output against its file on
  disk (`TestTypeTwo.test_what_it_writes_equals_the_data_file_on_disk`: KIT ARMAR-7's hand camera 'Arms' in the
  builder, 'Head' on disk; one row more, AgiBot G2's depth cameras in the head and in the wrists). It passes once he
  runs the type 2 builder. The type 3 and 4 builder has no such test; its file changes too (the Onero's cameras).
- **The builders read:** every sensor's region in the six parts files; the wrist and hand cameras of seven robots stood
  in the head (E38 point 7), set by the words already in the builders. Not yet in the parts files: they change when he
  runs the builders; until then the type 2, 3 and 4 files hold the old regions.
- **Looked at** (drawn at 1,000 draws into the scratch folder): type 2's overview page 1 ("6 Head joints" on the robot,
  the rows "LiDARs, head", "LiDARs, wheeled base", "Cameras, head", "Cameras, torso", "Cameras, arms", "Cameras, wheeled
  base", "Microphones, head", "Ultrasonic sensors, wheeled base", "Motion sensors, torso").
- **Code no stage reads** (the scan "check also for obsolete code"): 01's `JOINT_SHARE_ON_WHEELS` (line 1542),
  `ENERGY_PER_KG_ON_WHEELS` (1543) and `SCREEN_MUTED` (3828): `grep` over every `.py` and `.md` of the repository finds
  only their definitions (the names of the template's quantities are built from `JOINT_SHARE` and `ON_WHEELS` where
  read). Read by tests only, kept as decided (E28 point 3, V156): 01's `PROJECT_WORDS` and 02's `texts_over_data`, the checks
  of his rules on plain words and on text over a chart. All 36 settings of `src/params_schema.py` are read by a stage.
  Nothing removed: asked once.

### V197. His runs of 02 and 03 after E38 read back

- **His words:** "02 is done I run 03".
- **02:** its draws of the six types 11:06:56 to 11:07:35, 200,000 each; `places.npy` and `places_estimated.npy` 11:07:46
  to 11:09:51; all after the commit `5594a1c` (10:49:59). 138 pages in `figures/composition/` (126 before E38), 156 files
  in `figures/parts_taken_apart/` (138); no iCloud copy "… 2". The places' columns written by the pages' names, "LiDARs
  (boards and components): Al" (no stage reads `places.npy`); `by_material`'s columns, which 03 reads, as before
  ("Boards and components: cameras: …"). The places against the elements and the estimated places against the
  estimated kinds, every element of every type, draw by draw: the largest difference 8.7e-8 of the element's largest draw.
- **03:** 94 pages, 11:10:27 to 11:11:05 (86 before: one page and its numbers more for each of gallium, neodymium,
  dysprosium and boron).
- **Looked at:** type 2's page 2 of where the critical elements sit (Nd+Pr, Dy and Ga each in the magnets, by joint, and
  in the sensors, by kind; gallium in the sensors median about 125 mg, in the magnets about 650 mg, over the draws that
  hold it), type 2's element page 3 by material (Dy and Ga in two panels each), comparison_elements_9 (gallium in the
  sensors, the six types; type 6 the LiDARs' alone).

### V196. The magnets' and the sensors' part of an element apart (EVIDENCE.md E38 point 5)

- **His words:** "Gallium apart"; to the proposal of three points, "Yes do it like this. Nd etc. are then similar as Ga
  in elements in Magnets" (read as: every element the magnets and the sensors both hold, and nothing else; cobalt, of the
  magnets and the battery cells, keeps its one panel; said to him before building).
- **Tests first, seen to fail** (`magnets_split`, `element_pages` missing): `TestMagnetsAndSensorsApart` (four): the
  rule on made-up draws (magnets and sensors: two panels; magnets alone, sensors alone, or a third holder in 2.5 % of the
  draws or more: one; a third holder below 2.5 %: two); type 1's element pages, every element of the rule with "… in the
  magnets" and "… in the sensors" and no panel of its plain name (neodymium among them), cobalt one panel; the two
  panels and anything not drawn adding up to the element in every draw (1e-9), nothing else held; the pages of where the
  critical elements sit, every figure element once in order, Nd+Pr in two panels, the sensors' panel of sensor kinds
  only, the magnets' of none. 03's `test_the_magnets_and_the_sensors_apart`, its test draws now giving dysprosium,
  gallium and neodymium from the magnets and the sensors as 02's draws do: two pages each, the magnets' without a
  legend, the sensors' with the cameras and the other sensors; cobalt one page. All pass after the build.
- **Deliberate faults, each caught:** 02's split switched off ("'Nd' not found in []"; "('Nd+Pr', 'magnets') not
  found"); 03's switched off ("KeyError: 'Dysprosium (Dy) in the magnets of one robot of each robot type'").
- **An older test set to it:** `test_an_element_held_in_some_draws_shows_the_draws_that_hold_it` sought a panel of
  boron's plain name; it now checks each of an element's panels with its own draws (KeyError 'Boron (B)' before).
- **Looked at** (02 for the six types and 03 at 1,000 draws, the scratch folder): type 2's page 2 of where the critical
  elements sit (Nd+Pr, Dy and Ga each in the magnets, by joint, and in the sensors, by kind: the encoders' Nd+Pr about 2
  g, Dy about 80 mg; the cameras' and LiDARs' Ga median about 130 mg over the draws that hold it), type 2's element page
  3 by material (dysprosium and gallium in two panels each), 03's comparison_elements_8 and 9 (gallium in the magnets,
  one colour and no legend; in the sensors, cameras and other sensors).
- **The page check of the six types:** 2 tests, 100 s, OK. **The whole suite:** first run 587 tests, 1 error (the
  older test above); after it was set, 587 tests (726 s), all OK.
- **Not covered:** his runs at 200,000 draws.

### V195. GaN power transistors in humanoid joint drives ("Yes, research GaN", "Let it finish")

- **His words:** "Essential for sensors and GaN high voltage electronics", "Yes, research GaN", "I do not think GaN is
  essential for robots, as they have no high voltage motors and batteries", "Let it finish". A reading agent read the
  makers' guides, datasheets, declarations and filings (not read again by me). Nothing entered.
- **Robot makers:** none of Unitree, UBTech, Fourier, AgiBot, Tesla, Figure, 1X, Boston Dynamics or Agility states GaN
  in a document of its own; no charger stated with GaN. Second-hand only: AgiBot with Innoscience GaN, "three chips per
  motor" (trade press, 2025).
- **Chip makers' humanoid joint drives, all at 48 V with 100 V GaN:** TI TIDA-010979 (three DRV7167A half-bridges, two
  GaN FETs each, 1 kW, "to drive a humanoid robot joint"), TI TIDA-010936 (three LMG2100R044); EPC91118 and EPC91120
  (three EPC23104 or EPC23102 each, "intended for humanoid robot joints motors"; the guides name the Unitree A1 motor's
  size), EPC91122 and EPC91132 (one EPC33110 module of three half-bridges); Infineon REF_HUMA_MTR_48V_25A (GaN) beside a
  silicon twin of the same ratings; Innoscience INNDMD48V25A1 (six INN100EA035A) and INNDMD48V22A1 (three ISG3204LA).
  Innoscience's FY2025 results (HKEX): GaN shipped "in the robotics field", sales of RMB 1.26 million, no robot named.
- **Gallium nitride per device** (EPC's material composition declarations, "approximate … based on engineering
  calculation"): EPC23104 0.0474 mg of a 34.5 mg part; EPC23102 0.0661 mg of 35.1 mg; EPC2619 0.0181 mg of 5.4 mg. No
  declaration found for TI's, Infineon's or Innoscience's parts. Gallium is 83 % of GaN's mass (69.72 of 83.73 g/mol, my
  arithmetic): about 0.04 to 0.055 mg Ga per EPC half-bridge part, so about 0.12 to 0.17 mg per joint of three.
- **Silicon for the same job:** TI's own MOSFET design TIDA-01629 (six 100 V NexFET MOSFETs) beside its GaN design,
  "720mm2" against "320mm2"; Infineon's silicon twin; no source states what share of humanoid joint drives use GaN.
- **Not opened:** epc-co.com's web pages (403), TI's material-content pages (sign-in), Infineon's humanoid pages (only
  their navigation loaded).

### V194. Gallium in NdFeB magnets: who found it, why, how much, and when hot ("I need to understand it")

- **His words:** "I want investigation on the Gallium in the magnets. Check the internet to tell me, who found it and
  why it is there. I need to understand it", "But is the gallium suited for the high performance magnets in the joints,
  which get sometimes really hot", "I just want very good argument". A reading agent read the sources (patents in full,
  journal abstracts on the publishers' pages, open-access papers); I read again myself, in the browser pane, the two
  that carry the answer: EP 0258609 A2 and the Scientific Reports table. Nothing in the model or his data changed.
- **Who:** Hitachi Metals, EP 0258609 A2 "Permanent magnet with good thermal stability", priority 23 July 1986 (JP
  172987/86), inventors M. Tokunaga, M. Endoh and others (read myself): "The addition of Ga leads to remarkable
  improvement of coercive force", z (Ga in the formula) 0.001 to 0.15, "the most preferred amount of Ga is 0.005-0.05".
  The first papers: Endoh, Tokunaga, Harada (Hitachi Metals), IEEE Trans. Magn. 23 (1987) 2290 (of 20 elements Ga raised
  the coercivity most); Tokunaga et al., IEEE Trans. Magn. 23 (1987) 2287 (Nd-Dy-Fe-Co-B with Ga, for starter motors);
  independently Inomata et al. 1987 and Hu et al. (Beijing) 1989. Mitsubishi Materials for HDDR powder: US 5,228,930
  (priority 1989) and the paper he sent (Takeshita & Nakayama 1994).
- **Why:** first (1986 to 1990) with cobalt for thermal stability: the patent, "The addition of Ga serves to raise the
  Curie temperature of the BCC phase, effective for improving the temperature characteristics" (read myself); later
  explained by new Nd-(Ga,Fe,Co) grain-boundary phases and better wetting (Fidler, Groiss, Tokunaga 1990); since about
  2011 to 2016 in low-boron magnets with little or no Dy and Tb: an R6T13Ga (Nd6Fe13Ga) grain-boundary phase that is not
  ferromagnetic keeps the coercivity high (Showa Denko WO 2013/008756; Sasaki, Ohkubo, Hono et al., NIMS and Toyota,
  2016; Proterial US 11174537); Vacuumschmelze 2001: with Co, Cu and Al, corrosion resistance and the coercivity Co
  takes away. Its cost: Ga in the main phase lowers the remanence (Proterial), may lower the squareness (EP 3261101).
- **How much:** the makers' patents 0.05 to 1.0 mass % (Proterial), 0.08 to 0.30 (TDK, with Tb diffusion), 0.5 to 1.0
  wt % (Yantai Shougang, free of heavy rare earths); the 1987 magnets about 0.9 to 1.8 mass % (the agent's conversion of
  the published formulas); measured by ICP-OES in end-of-life magnets (Rathfelder et al., Sci. Rep. 2025, Table 2, read
  myself): M2 Ga 0.16 wt % (with Co 2.45, Dy 3.48, Tb 0.47), M1 (a wind turbine's) none stated ("–"). Not in every
  grade; no maker's grade sheet stating Ga per grade was found.
- **When hot:** the reason it was introduced: with Co, below 5 % irreversible loss after 140 °C without Dy, after 260 °C
  with Dy (Hitachi Metals 1987, abstracts); Ga added to Dy and Co, not in place of them, in the hot grades
  (Vacuumschmelze 2001); in place of Dy and Tb only in the Dy-free low-boron magnets. Not found first-hand: a
  temperature coefficient of coercivity with and without Ga; Ga per SH, UH, EH or AH grade.
- **Against the model:** his workbook's 0 to 0.1 % of the magnet's mass in every grade lies at or below these sources
  (most at 0.05 to 1.0 %, the one measured magnet 0.16 %). Reported, not changed.
- **Not opened:** ScienceDirect (Sasaki et al. 2016; Huang et al. 2022: 403), AIP (bot check), IEEE full texts (sign-in;
  abstracts read). The agent's browser attempt at the MRS-J PDF opened a file-save dialog in the browser pane; nothing
  was saved.

### V193. The sensors by kind built (EVIDENCE.md E38 point 1); the research of points 2 and 4; the gallium's sources

- **His words:** see E38; then "combine all the cameras and time of flight and lidar are the same", "Have LIDAR etc.
  first and then just in brackets boards and components", "Nd is in the head joint and not just in the head", "I just
  want very good argument, as the galium in NdFeB is most likely lost and Gallium is stategigc. Essential for sensors and
  GaN high voltage electronics", "Yes, research GaN".
- **Every combination of car sensor elements** in the six parts files (11, read from the files): each a kind
  (`sensor_kind`); the speakers hold none and no element of interest. `TestSensorsByKind` (nine): the eleven
  combinations, the kinds of camera the element pages' cameras; every sensor of the six files a kind (over 500 rows); a
  combination of no kind a fault of `check_parts`; type 1's indium in the LiDARs and the cameras only, its gallium the
  sensors' alone in the test's draws (the test's fixed magnets hold none: my first assertion of gallium in the hips was
  wrong for them and corrected); the kinds adding up to the cameras and the other sensors of the element pages, draw by
  draw (1e-9); every place its own colour; the overview two elements a page where their rows fit; the names "LiDARs
  (boards and components)" on every page. Seen failing before the build (`sensor_kind`, `SENSOR_KINDS`, `shown_name`
  missing; indium "Boards and components: cameras", "… other sensors"), passing after.
- **Deliberate faults, each caught:** the LiDARs left with no kind (the six files' test and the combinations' test
  fail); no kind carried to the places (02 stops: "Sensors 2: Unitree G1, LiDAR, Livox Mid-360: its car sensor elements
  … are no kind of sensor"); the overview always two elements a page ("Cu: 0.000023 on 0.17": two numbers on one another;
  "34 not less than or equal to 24").
- **The overview:** with the kinds, copper's and aluminium's panels hold up to 18 rows; two on a page gave rows of 13
  points under 14-point labels, the numbers on one another (found by `test_an_overview_row_held_in_some_draws…`); built:
  two elements a page while 24 rows fit, else one (type 1: copper alone, aluminium with silver, gold with palladium,
  tantalum with neodymium and praseodymium, dysprosium with gallium, indium: six pages, five before); the columns of
  numbers set apart by each column's widest number (`text_width`, from the font's outlines); the headings 2 points
  above the panel (on indium's page of one short panel they had stood above its title). The test reads each row's
  numbers left to right since the columns may move.
- **The colours** (CIE Lab difference to the nearest other colour of those pages, computed): LiDARs 31.6, cameras 14.1
  (to the hip joints'; the cameras' purple of E32 kept), joint encoders 30.3, hydraulic actuators' sensors 31.6,
  microphones 29.8, ultrasonic sensors 30.3, motion sensors 33.6.
- **Looked at** (drawn at 1,000 draws into the scratch folder): type 1's overview pages 1 and 2, type 2's overview pages
  1 and 6, type 2's and type 5's pages of where the critical elements sit (page 2: indium in the LiDARs and the cameras,
  gallium in the joints and the sensors), type 2's element page 1 and type 1's means page 1 (the names "… (boards and
  components)"), type 2's notes page (the kinds named).
- **The page check of the six types** (`TestEveryPageOfTheSixTypes`): passing after each change. **The whole suite:** 582
  tests (693 s), all OK.
- **Where the sensors' gallium and indium sit** (the parts files, the car list's modes times each sensor's count, not
  drawn): the head 72 to 100 % of the sensors' gallium, the wheeled base 5 to 26 % (types 2 to 5), the arms 1 to 3 %, the
  torso up to 1 %. **The kind Head's neodymium** (his run): 4.7 to 15.5 g a robot (1.8 to 3.7 % of the robot's), all in
  the head joints' motor magnets; the kind Head also holds the sensors' housings, the speakers, the head boards' laminate
  and two robots' hydraulic head actuators.
- **The gallium in the magnets, first-hand:** the paper he sent, Takeshita & Nakayama (Mitsubishi Materials), "HDDR
  process and Nd-Fe-B magnet powders", Trans. MRS Japan 14B (1994) 955–960: Ga, Zr and Hf added "in a small amount" make
  the HDDR powder anisotropic; 0.5 to 2.0 at % Ga gives the largest remanence and a coercivity of 13 kOe; the mechanism
  "we are now studying". Proterial's US 11174537 B2, claim 1 read in the browser pane: Ga 0.05 to 1.0 mass % required, an
  R-T-Ga phase in the grain boundary "whereby high HcJ can be obtained". Schönfeldt et al. 2023: MRI scrap magnets Ga
  0.22 wt %. The model's: his traction-motor workbook, 0 to 0.1 % in every grade.
- **The research of point 2** (a reading agent, every row from the maker's own page, SDK file or manual, 30 robots of 20
  makers): temperature readings per joint motor in the SDKs of Unitree (two per motor) and Booster (one per joint) and
  in their batteries' states (a field shows a reading, not a count of sensors); Wi-Fi on most makers' pages, 4G or 5G as
  an option on AgiBot's G2 and X2 Ultra, MagicLab's Gen1, Engine AI's T800 Max, 1X's NEO and PNDbotics' Adam; six-axis
  force sensors at the wrists stated by UBTech (Walker S1, S2), Galbot (G1) and Kepler (K2); tactile sensors in the hands
  (Unitree Dex3-1: 33 per hand; Dex5-1: 94; Kepler K2: 25 per finger; Leju: 5 per hand), touch screens and touch sensors
  in heads and chests (Galbot, Engine AI PM01, AgiBot X2, MagicLab Z1, Fourier GR-3: 31 tactile sensors in head and
  torso); an infrared camera once (Engine AI SE01), no infrared illuminator stated; satellite positioning once (Xiaomi
  CyberOne). Nothing entered.
- **The research of point 4** (a reading agent): no first-hand source names the capacitors of a commercial humanoid's
  joints; mjbots' moteus (16 × 10 µF 50 V MLCC 1206), Ben Katz's Cheetah driver (ceramic), TI's humanoid joint drive
  TIDA-010979 (17 × 10 µF ceramic), ODrive v3.5 (8 × 470 µF aluminium electrolytic); the compositions of KEMET/YAGEO
  MLCCs and tantalum capacitors, TDK EPCOS aluminium electrolytic and hybrid polymer capacitors and Panasonic's
  aluminium electrolytics read. Nothing entered.
- **Not covered:** points 2 to 4 entered (they wait for his word and for the research on GaN and on the gallium of the
  magnets, running); his runs.

### V192. The sensors and the gallium checked ("Yes sensors"; "I have a hard time believing Galium is directly in NdFeB magnets")

- **His words:** "What I miss at the moment are the sensors. Temperature LIDAR, Cameras etc.", "Theses sensors are the
  location for cirticial raw materials such as indium galium etc.", "Yes sensors", then "I have a hard time believing
  Galium is directly in NdFeB magnets. It soulds much more like other sonsor types check the internet. Gold and Neodyn
  are not interesting for me. It is cameras LiDAR temperature and other sensor typoes. We have them all in the. car
  lectronic sensors". Nothing changed in code or data.
- **The sensors' share of each element** (his run of 2026-11-06, `places.npy`, means): indium 100 % in the sensors
  (7 to 19 mg a robot); gallium 3 to 10 % in the sensors, 90 to 97 % in the joints' NdFeB magnets; gold 11 to 14 % in
  the sensors, the rest the boards'; neodymium about 1 % in the sensors (the encoders' magnets). At the modes (parts
  files, not drawn) the sensors' indium and gallium come from the depth cameras and the LiDARs about half each. The car
  list's indium of a laser diode array is 0 / 3 / 30 mg, so the drawn mean is about 3.7 times the mode.
- **The magnets' gallium:** from RAWCLICVehicleTractionMotor's `data/raw/10_MaterialElementDefinitions.xlsx`, sheet
  PermanentMagnetNdFeB (`traction_motor_magnets`): every one of its 28 grades Ga 0 (row "min") to 0.001 of the
  magnet's mass (row "max"); the sheet names no source for its composition columns (its one source column is of the
  temperatures). Read first-hand on the internet: the TU Darmstadt news page of Schönfeldt et al. 2023 (J. Alloys
  Compd. 939, 168709): the "nominal composition" of scrap magnets of MRI scanners, Ga 0.22 wt % (Nd 28.04, Dy 0.80,
  Tb 0.44, B 1.06, Co 1.65, Al 0.34, Cu 0.18, Fe the balance), no method of measurement named. Not opened: Frenzel et
  al. 2016, "The Global Anthropogenic Gallium System" (ACS and its supplement: HTTP 403); two Fraunhofer records
  (publica.fraunhofer.de 451801 and 503725: a bot-protection page, not passed). A search summary's statements (magnets
  22 to 37 % of the world's primary gallium; 0.1 to 0.5 wt % Ga added for coercivity in research alloys) are not read
  first-hand and are not passed on as content.
- **The car list's sensor types holding Ga, In, Ge, As, Ta or Co** (`07_VehicleSensorComposition.xlsx`, sheet Sensor
  Details, min / mode / max mg): laser diode array Ga 5/30/150, In 0/3/30; photodetector array Ga 0/1/10, In 0/2/20 (both
  in the model); IR LED array Ga 2/8/30, In 0.5/2/8; cellular modem Ga 1/5/20, Ta 1/5/20; capacitive touch sensor In
  2/15/80; GNSS receiver Ge 0.1/0.5/2, Ta 2/8/30; RF transceiver Ge 0/0.2/2; temperature sensor Co 0.1/2/15; force,
  torque and pressure/force sensors Ni, Mn; and car-only types (PM2.5, rain/light, isolation monitoring, wheel speed).
  None of the second group is in any robot's parts.
- **A fault in the documents:** 02's notes page (`02_composition.py`, the sentence on the electronics), its comment on
  the components and METHODOLOGY name "satellite receivers and modems with their antennas" among the other sensors; no
  robot in any parts file holds a satellite receiver or a modem (`grep` of the builders: none).
- **Not covered:** the proposal of points 1 to 3 (the sensors by kind; the missing kinds from the car list; the
  documents' fault) waits for his word.

### V191. His run of 03 read back

- **03:** 86 pages in `figures/comparison/`, written 06:44:09 to 06:44:45, every one after 02's draws (none older); no
  iCloud copy "… 2"; as many pages as the page check of V188.
- **Looked at:** `comparison_elements_23.png`, the sensors' titanium (types 2 and 3 on their logarithmic axes, the
  cameras' 0.1 to 10 mg and the ultrasonic sensors' 50 to 470 mg both visible; types 1, 4, 5, 6 linear);
  `comparison_elements_4.png`, copper ("Copper metal: windings, busbars, heat pipes" in the legend, within the page).
- **His runs of E35, E36 and E37:** all done and read back (V189 to V191).

### V190. His runs of 01 and 02 read back

- **His words:** "01 has run already only 03 is missing", "02 is done and 03 running".
- **01:** `figures/schemas/overview_1.png` and `_2.png` written 06:20:35, after the builders (06:19 to 06:20); the
  overview looked at: four stages from `STAGES`, 03 writing "The comparison pages", no "later" (E35).
- **02:** its process from 06:21 to 06:44; every type's draws in `data/consolidated/` 06:41:10 to 06:41:44, 200,000 each;
  the new `places.npy` and `places_estimated.npy` of every type 06:41:55 to 06:43:40; 126 pages in
  `figures/composition/`, 138 files in `figures/parts_taken_apart/` (its sources figures included); no iCloud copy
  "… 2". The places against the elements, and the estimated places against the estimated kinds, draw by draw, every
  element of every type: the largest difference 8.7e-8 of the element's largest draw (float32's rounding).
- **Looked at:** type 2's and type 3's element pages 1 (the sensors' titanium on its logarithmic axis, the cameras'
  0.1 to 10 mg and the ultrasonic sensors' 50 to 470 mg both visible; every other panel linear), type 1's and type 2's
  element pages 2 ("Copper metal: windings, busbars, heat pipes", "Nickel metal: the battery's nickel strips" in the
  legend, within the page), type 5's parts page of elements 2 (indium in the cameras and the other sensors, gallium in
  the joints' magnets and the sensors).
- **Seen before his run, not by any code:** `figures/composition/`, `figures/parts_taken_apart/` and
  `figures/comparison/` were gone at 06:30 (`figures/` changed 06:20); the code removes no folder (02 and 03 remove only
  numbered pages beyond those drawn, by exact name). 02 wrote its two again; 03 its own.
- **Not covered:** 03 (running at the time of writing).

### V189. His runs of the six builders read back

- **His words:** "I have run make 1 to 6", then "02 is runing".
- **The files:** the six `data/researched/<n>_<name>/parts_taken_apart.xlsx` written 2026-11-06 06:19:08 to 06:20:11,
  after the builders' last change (`aa9a1c5`, 2026-11-05 17:20); no iCloud copy "… 2" in `data/` or `figures/`.
- **Against the code:** `tests/test_make_parts_taken_apart.py`, 136 tests (125 s), all pass; the two
  `test_what_it_writes_equals_the_data_file_on_disk` of types 1 and 2, failing since E35, now pass: each file is what
  its builder writes.
- **Not covered:** 01, 02 and 03 on these files (02 running at the time of writing).

### V188. Copper and nickel by what they are; every page of the six types checked by a test (EVIDENCE.md E37)

- **His words:** "Yes, relabel" (2026-11-05); "Relabel and page check" (2026-11-06).
- **Tests first, seen to fail:** `TestCopperAndNickelNamed` (02, two: every metal of `WHOLE` named and no other, the
  colour of copper as it was; type 1's element pages' legends and means pages with the two names and never a bare
  "Copper 1.4 kg", its materials pages with "Copper" and "Nickel: strips of the battery"), failing on
  `ELEMENT_PAGE_NAMES` missing and "'Copper metal: …' not found"; 03's
  `test_copper_and_nickel_by_what_they_are_on_the_element_pages` (its test draws now give copper and nickel from their
  own metals, as 02's). My first test expected a materials page titled "Nickel": it is "Nickel: strips of the battery",
  as it was; the test was wrong, not the code, and was corrected. After the build all pass, 03's fifteen too.
- **The page check:** `TestEveryPageOfTheSixTypes` (02 for the six types at 1,000 draws, then 03, in a temporary
  folder, every page checked as it is saved): 263 pages of 02 and 86 of 03, as many as V186's scratch check, no
  problem; 88 s.
- **Deliberate faults, each caught:** the relabel switched off (both relabel tests fail); the logarithmic axis switched
  off (the four panels of the sensors' titanium, types 2 and 3 on 02's and 03's pages, medians at 0.2 % and 0.7 % of
  their bars); every legend in one row (22 legends of 02 and 12 of 03 beyond the page); every legend without its last
  colour (88 panels of 02, 100 of 03); every page's title above the page (every page).
- **The shares of the material Copper** written in E37, the code's comment and METHODOLOGY computed from his run of
  2026-11-05 (200,000 draws): the joints 71 to 91 %, the wheeled base 2 to 13 %, the battery pack 6 to 11 %, the head 2
  to 3 %, the boards and computers 0.6 to 1.8 %; the material Nickel the battery pack's alone (26 to 88 g). I had first
  written "79 to 91 %" from yesterday's sandbox; corrected before anything was committed.
- **Seen, not changed (reported):** at 1,000 draws 02 warns "Mean of empty slice" (`02_composition.py`, the share of a
  robot's draws below zero, for a robot no draw picked: 172 robots and versions in 1,000 draws); and matplotlib warns
  that more than 20 pages are open at once (02 keeps a type's pages open until it saves them).
- **Looked at** (drawn once more at 1,000 draws into the scratch folder): type 1's and type 2's element pages 1 and 2
  (the legend in two columns within the page, "Copper metal: …" and "Nickel metal: …" among the materials), type 1's
  means page 1 ("Nickel metal: the battery's nickel strips 26 g", "Copper metal: windings, busbars, heat pipes 1.4
  kg"), 03's copper page (the new name) and its page of the mass by material ("Copper").
- **The whole suite:** first run 574 tests (651 s), 3 failed: the two builder tests waiting for his runs, and
  `test_six_panels_a_page_with_the_legend_and_the_means_of_its_materials`, which expected the bare "Copper" in the
  element pages' legend; set to the new names in the materials' order. Rerun: 574 tests (658 s), only the two builder
  tests failing.
- **Not covered:** his runs at 200,000 draws; 01's pages (their own tests).

### V187. The handover read, the code and the data checked ("read the handover and check the code")

- **His words:** "read the handover and check the code. Furthermore check the lessons learened and how we work
  together. I want that everything is verifyed and based on solid data or solid data model". Nothing changed.
- **The repository:** clean, `main` = `origin/main` = `9aef9dd`. **His runs not yet done:** 01's pages written
  2026-11-05 04:55, the builders' files 14:23 to 15:24, 02 15:09 to 15:18, 03 15:23; the code last changed 17:20
  (`aa9a1c5`). **The whole suite:** 569 tests (550 s), the 2 `test_what_it_writes_equals_the_data_file_on_disk` failing
  until his builders run, as at V186. 01's overview against the stages: as the code. No function of E35 and E36 unused.
- **The scratch page checker of V186** was gone with the scratch folder (emptied overnight): the six types' pages were
  checked by no test (the repository's tests: type 1's pages and 03's test draws). Built as a test in V188.
- **How solid the data are** (01's `template_shares` over his parts files; 02's `elements` and `estimated` of his run):

  | Type | Robots and versions | Mass stated by a source | Joints on the template | Battery on the template | Cu on parts labelled E | Nd+Pr | Au |
  |---|---|---|---|---|---|---|---|
  | 1 | 31 | all (12 "S, E") | 42 % | 39 % | 80 % | 76 % | 83 % |
  | 2 | 102 | all (11) | 66 % | 62 % | 95 % | 93 % | 94 % |
  | 3 | 172 | all (5) | 80 % | 72 % | 97 % | 97 % | 96 % |
  | 4 | 137 | all (3) | 75 % | 72 % | 98 % | 98 % | 96 % |
  | 5 | 14 | all | 29 % | 36 % | 88 % | 88 % | 87 % |
  | 6 | 8 | all | 38 % | 38 % | 78 % | 77 % | 77 % |

  Types 2 to 4 above E13's half on both templates after E14's research pass: E13 rule 4, said on their notes pages.
  The board copper from 14 university analyses of whole PC boards (E2.8b; Bizzo 2014's own XT, 486 and Pentium
  boards), the boards' precious metals and the sensors' elements from car electronics (RAWCLICVehicleElectronics, the
  sensor elements only); E2.8b records the car and data-centre board data about 20 times apart on copper per cm².
- **`estimated.npy` misleads:** 02 follows the kilograms on parts labelled E for the eleven elements of the overview
  pages only (`TRACKED`); the table's columns of lithium, cobalt, nickel, manganese, titanium and the rest are 0 kg
  always, which reads "nothing estimated". The overview's hatching is right. Reported, not changed.
- **The sensors** (his question during the build: "What I miss at the moment are the sensors. Temperature LIDAR,
  Cameras etc.", "Theses sensors are the location for cirticial raw materials such as indium galium etc."): the parts
  files hold joint encoders, cameras, motion sensors, LiDARs, microphones, speakers, ultrasonic and time-of-flight
  sensors and the hydraulic actuators' position and pressure sensors; no temperature, force or torque, tactile or
  current sensor in any robot. The car list holds rows for them ("temperature sensor": NTC, Co 2, Ni 5, Mn 8 mg;
  "capacitive touch sensor": In 15 mg). The indium and gallium drawn today: the laser diode arrays (LiDARs, the depth
  cameras' projectors: In 3, Ga 30 mg each) and the photodetector arrays (LiDARs: In 2, Ga 1 mg); the CMOS and IR image
  sensors hold neither in the car list. On the pages they show only as "cameras" and "other sensors".

## 2026-11-05

### V186. His figures fixed: the legends, the places, the sensors' titanium and its axis (EVIDENCE.md E36)

- **His words:** "1_elements_2 has text for the legend cut", "There are also legend colors missing", "2 element_1",
  "parts_taken element indum is head. it is sensors. Cameras.", "Yes, fix all three"; "where the hell is titanium in
  the sensor", "Yes, add it"; "Titanium in sensors the x axis is not good, You know this", "Yes, build it".
- **Points 1 to 4, tests:** `TestLegendsAndPlaces` (six: every legend within its page, every colour a page draws in its
  legend, the places adding up to the elements to 1e-9, indium the cameras' and the other sensors' and copper's
  windings still their joints, the sensors' titanium a panel of its own in mg); 03's
  `test_the_sensors_titanium_a_page_of_its_own`. Two older tests set to his later words: the overview's rows by place
  (indium in the cameras, held in some draws, in place of the head), and the light alloys' legend (E33's "no legend
  entry of a light alloy" now: the alloy named in the legend of the page that draws it; the expected panels with "Titanium
  (Ti) in the sensors").
- **Point 5, tests first, seen to fail:** `TestAxisNotPressedLeft` (three): a panel shaped as type 2's sensors'
  titanium (96 % of 10,000 draws 1 to 10 mg, 4 % 100 to 470 mg) logarithmic, its median at least 5 % along its bars,
  its bars evenly spaced on the logarithmic axis, its ticks plain numbers; a narrow spread linear; every panel of type
  1's pages its median at least 5 % along its bars. Failing before the build ("'linear' != 'log'", `LOG_BELOW`
  missing), passing after. 03's `test_no_median_in_the_first_part_of_its_axis`: type 2's sensors' titanium in the
  test's draws spread as above, its panel the one logarithmic of the six, no panel of 03's pages with its median in the
  first 5 % of its bars.
- **Deliberate fault:** the rule switched off (`logarithmic` always False): both tests fail, 03's at
  "comparison_elements_23.png, type 2: 0.010 not ≥ 0.05". It first passed with the rule off (0.0549): the test
  measured along the drawn axis, whose margins moved the median past 5 %; since then it measures along the bars, from
  the smallest draw to the axis's end, as the rule does.
- **The source of the spread** read first-hand: RAWCLICVehicleElectronics' `07_VehicleSensorComposition.xlsx`, sheet
  Sensor Details, row "ultrasonic sensor" (PZT ceramic disc): titanium 10 / 40 / 120 mg; in the sandbox's draws the
  robots above 30 mg: type 2 the AgiBot G2 (median 359 mg), the MagicBot D1 (162) and the H2-D Flagship (109), 3.9 % of
  the draws; type 3 the G2 and the D1, 1.1 %.
- **02 and 03 in the sandbox** (2,000 draws, the repository's code): 02 "done in 1 min 17 s", 03 86 pages. The page
  check of every page as it is saved (legends within the page, every colour drawn in a legend, every text and panel
  within the page, and since today every panel's median at least 5 % along its bars): 263 pages of 02, 86 of 03, no
  problem. Panels with a median: 286 (02) and 221 (03); logarithmic: 4, the sensors' titanium of types 2 and 3 on 02's
  element pages 1 and on comparison_elements_23 (their medians at 31 % and 37 % along the bars); the smallest median of
  a linear panel at 7.4 %.
- **Looked at:** 1_elements_1 and 1_elements_2 (the legend in two rows, the alloys named, the Ti alloy and Ti sensors
  panels); type 5's parts elements_2 (indium as cameras and other sensors) and overview_5 (their rows); type 2's and 3's
  elements_1 and comparison_elements_23 (the logarithmic panels: the cameras' 0.1 to 10 mg and the ultrasonic sensors'
  50 to 470 mg both visible, ticks 0.1, 0.3, 1 … 300; the four other types linear as before); type 2's numbers_1 (the
  sensors' titanium held in 97 %, median 1.7 mg, mean 13 mg, 95 % 0.4 to 164 mg, beyond 0.51 % up to 920 mg); the notes
  pages of type 2, of its parts figures and of 03, page 1 (the sentence of the logarithmic axis, within the page).
- **Seen, older than today, not changed (reported):** on the numbers pages a share held rounded to "100 %" where not
  quite every draw holds it (type 2's manganese), and the "Held in" column a few pixels below the others.
- **The whole suite:** 569 tests (551 s), 2 failed: the two `test_what_it_writes_equals_the_data_file_on_disk` of
  types 1 and 2, as at V185 (his files of 15:24 hold the citations of before E35 until his runs of the builders). Its
  first run (548 s) had 2 more: the two older tests above, since set to his later words.
- **Not covered:** his runs (the builders, 01, 02 at 200,000 draws, 03). At 200,000 draws the medians move a little;
  the panel nearest the 5 % at 7.4 %.

### V185. The ten open items solved ("Yes, all ten"; EVIDENCE.md E35)

- **His words:** "can we solve the open items?", "in a pragmatic way", "Yes, all ten".
- **Tests first, seen to fail:** item 7, `TestSourcesOfTheShares` (three: every code the Shares cite on the sheet
  Sources, M30 on types 5 and 6, Bizzo 2014 and Drexler 2025 in every file), failing "(3, 'Bizzo 2014')", "(3, 'T1')":
  type 3's Shares cite T1, which its Sources lacked, beside M30, Bizzo and Drexler; item 5,
  `test_it_stops_where_the_draws_hold_an_outlier` (03), failing on `outliers_in_draws` missing; item 6,
  `test_the_notes_say_the_cameras_no_source_counts_are_estimated`, failing on the words missing; items 2 and 4,
  `test_the_overview_draws_its_stages_from_stages_03_among_them` (failing: STAGES of two fields) and
  `test_the_mass_axis_without_the_outlier` (failing: "1600" among type 3's page's texts). After the build all pass,
  with the Neo1's and the overview's earlier tests and 03's twelve.
- **Item 3:** the 28 files "… 2" of 4 November listed by their exact paths, each deleted only where its plain-named
  file (today's run) was there; none left (`find data figures -name '* 2*'`: 0).
- **The builders in the sandbox:** their files against his (written 14:23 to 15:24): only the motor stator's Shares
  row (its basis "Drexler 2025"), the board copper constant (its source "Bizzo 2014") and the sheet Sources changed:
  Bizzo 2014, Drexler 2025, T3, T3k added to types 3 to 6, T1 to 3, 5 and 6, M30 to 5 and 6. No number changes.
- **01, 02, 03 in the sandbox** (2,000 draws): 01 "No fault found."; overview_1 looked at (four stages from `STAGES`, 03
  writing the comparison pages, no "later", the arrows of the inputs into 01's box), overview_2 ("Open: the
  stock-and-flow model (04)."), type 5's robots table (its mass axis 0 to 200 kg, the Neo1's row "1200 kg" without a
  dot); 02's notes of type 4, page 4: the sentence of the cameras' estimate in its place, on the page (its nested
  bracket "(an estimate))" then written ", an estimate"); 03 its check passed on the sandbox's draws, 84 pages.
- **Item 10:** over every parts file (01's `type_parts`), the robots taken apart of each type's robots with a mass:
  30/30, 96/96, 164/164, 124/124, 11/11, 5/5 (each type's own file alone: fewer, a robot taken apart in another type's
  file); `open_words` with the register and the files "Open: the stock-and-flow model (04)."; the materials "No" and
  "Partly" in the elements from his run's `summary.xlsx` of each type.
- **The whole suite:** 559 tests (537 s), 3 failed: the two `test_what_it_writes_equals_the_data_file_on_disk` of
  types 1 and 2 (his files hold the citations "Drexler et al. 2025", "Bizzo et al. 2014" until his runs of the
  builders), and `test_no_source_row_from_a_robots_name`, which held T1 off type 3's Sources: T1 is cited by the rows
  of MagnetGrades ("T1 slide 42") and JointParts ("T1 slide 43") every file holds, which item 7 searches; changed to
  check that T1 comes from those citations and L1 (a robot's name only) stays off; its class OK.
- **Not covered:** his runs (the six builders, 01, 03); 02's notes at his next run of 02.

### V184. His runs after the cameras (E31) and the removal (V183), read back

- **His words:** "I have run make 01 to 06 now 02 runs", "02 and 03 have run I also have run again the make 01 and 02".
- **The parts files:** types 3 to 6 written 14:23:54 to 14:24:29, types 1 and 2 again at 15:24:39 and 15:24:46; all
  six equal the sandbox's build of the final code, sheet by sheet, row by row.
- **02 and 03:** 02 wrote `data/consolidated` (84 files) and `figures/composition` (126) from 15:09:31, `data/parts_taken_apart`
  (96) and `figures/parts_taken_apart` (138) to 15:12:28; 03 `figures/comparison` (84) from 15:23:57 to 15:24:30. No file
  of them older than the builders' runs. The names as the sandbox's, but one page more: type 4's notes, 6 pages in his
  run, 5 in the sandbox. The sixth holds the closing paragraph; the difference is page 4's paragraph "Below zero where a
  remainder is …: the part group Frame is below zero in 3 draws (0.0015 % of the draws)", reported, not cut (E21). The 3
  draws are the 1X NEO's (draws 105015, 187879, 194714; −0.07 to −0.22 kg), its frame below zero in 256 of its 1,646
  draws (15.6 %); before E31 the same (the sandbox of the morning: 2 of its 18 draws; V146, E21: about 16 %, its stated
  842 Wh in its stated 29.9 kg). Not from the cameras: the NEO is not among E31's robots, its rows unchanged.
- **The draws:** 200,000 in every type; each element by material equals it by part, the copper fixed in alloys aside,
  within 1 × 10⁻⁷. The cameras' titanium held in 86.6, 97.9, 98.1, 98.4, 100 and 100 % of the draws of types 1 to 6
  (the sandbox's at 2,000 draws 86.9, 97.4, 98.2, 98.5, 100, 100), its median above 0 0.99 to 1.71 mg; type 1's 86.6 %
  its 26 robots of 30 with cameras (86.7 %). Looked at: 03's indium page (the cameras and the other sensors, mg).
- **The two tests that failed in V183** (`test_what_it_writes_equals_the_data_file_on_disk`, types 1 and 2): run again
  after his runs of the builders, both OK.
- **Not covered:** the other pages, not opened one by one; the rest of the suite not run again (the code unchanged
  since V183's run).

### V183. The code under tools that nothing needs, found and removed ("Yes, remove 1 to 4")

- **His words:** "there is code, which is not needed anymore under tools", then "Yes, remove 1 to 4".
- **How found** (`scratchpad/cameras_build/unused_in_tools.py`, `unused_in_tools2.py`, read only): every top-level name
  of the nine files under tools/ (functions, classes, constants) counted in the code of every Python file of the project,
  comments and strings left out: none used nowhere. Every explicit import of tools/ counted in its file. Every source row
  of the six files as the builders write them searched in every other cell of its file.
- **Removed, each with its proof:** (1) `tools/parts_types_3_and_4.py`, the aliases `binocular, depth_camera, camera,
  lidar, imu, microphones, speaker = T2.…`: since today's move the same functions (`T2.camera is parts_taken_apart.camera`,
  True for all seven) come with the file's `from parts_taken_apart import *`; `base_lidar` and `base_depth_camera`,
  type 2's own, kept. (2) There, `SHARED_CONSTANTS_FIRST` and `SHARED_CONSTANTS_LAST`, imported and used nowhere in the
  file. (3) My two-line pointer comment in type 2's builder. (4) The source rows `N1c` (type 1's builder) and `ORM`
  (type 2's), cited by no cell of any file (N1c named in EVIDENCE only).
- **Checked:** the six builders run in the sandbox; their files against those of before the removal: types 3 to 6
  identical, type 1 without N1c, type 2 without ORM, nothing else. The whole suite: 552 tests (1,288 s, beside his run
  of 02), 550 OK; the 2 failing `test_what_it_writes_equals_the_data_file_on_disk` of types 1 and 2, his files of
  14:23 still holding N1c and ORM ("['N1c', 'A teardown article on Zhihu…" and "['ORM', 'Oriental Motor…" the only
  differences). His files of types 3 to 6 (14:23 to 14:24) equal the build; 02 and 03 read no Sources, so his run of
  02 is the same either way.
- **Found, not changed (his word):** the servo valve's Shares rows of types 5 and 6 cite M30, which neither file's
  Sources holds; the shared rows cite "Bizzo et al. 2014" and "Drexler et al. 2025", not the codes "Bizzo 2014" and
  "Drexler 2025".
- **Not covered:** his reruns of the builders of types 1 and 2.

### V182. The cameras built (E31, "Yes, A to H"): tests, the files, the sandbox

- **Tests first, seen to fail** (the code not yet written): 01's six (`test_a_sensor_of_a_drawn_number_is_read_without_fault`
  and five planted faults: no constant, a constant without its row, a number beside it, a count of 3.5, a count from
  0), failing on `NUMBER_OF` missing; the builders' eight (`TestCamerasE31`: the 144 robots each in one point, points 1
  and 2 their image sensors and microphones as counted by hand from the sources, point 3's row and constant 1 / 3 / 12 E
  and its microphones in the 31, point 4 none, the Phantom without battery and its source the BBC, every E31 code on the
  sheet Sources, the prefix 01's, every file passing 01's checks), failing "0.0 != 8 : Foundation Phantom MK1" and on
  the names missing; 02's three (`TestDrawnNumbers`: 400,000 whole numbers of 1 / 3 / 12 each at the widened triangle's
  share, a hand-written CDF, within four standard errors, their mean 16/3 ± 0.02; a count of one value; type 1 at 6,000
  draws: the Sapiens K1's estimated cameras in every one of its draws and none outside, their mean 16/3 times the JAKA
  π's one camera, ± 25 %), failing on `whole_numbers` missing. After the build all 17 pass.
- **The files the builders write, against those on disk** (`scratchpad/cameras_build/diff_parts.py`, read only): only
  rows added, 206 in Sensors, 27 in SensorElements, 122 constants "Number: Cameras (number not stated)", 25 sources E31-…;
  removed only the Phantom's row of Robots (its sources' words, TBS → E31-BBC) and the source TBS. Type 5's file
  unchanged; every other row of every file as before (the helpers moved from type 2's builder write the same rows).
- **The sandbox** (`scratchpad/sandbox_e31`, the code of this build, the inputs copied, 2,000 draws): the six builders,
  01 ("No fault found."), 02 (1 min 25 s), 03 (84 pages). Each element by material equals it by part, the copper fixed
  in alloys aside, within 1 × 10⁻⁷ in every type. The cameras' titanium held in 87 to 100 % of the draws (before 47 to
  91 %), its median above 0 1.0 to 1.7 mg; type 1's 87 % its four robots of point 4. Gallium and indium of the cameras
  rise only where a depth camera was stated (type 2: 41 → 48 %): the estimated cameras are colour sensors (point C),
  which hold neither. Looked at: 03's indium page (cameras and other sensors, mg, nothing written over the panels).
- **The whole suite:** 552 tests (518 s), 4 failed. Two expected: `test_what_it_writes_equals_the_data_file_on_disk` of
  types 1 and 2, the builders' files against those on disk, which are the old ones until his runs of the builders. Two
  older tests of E7.5 point 8 ("one motion sensor where the maker names none"), which counted every sensor of a block:
  changed to leave aside the rows whose sources are E31's (TestCamerasE31 checks those); what each checks unchanged,
  both pass (23 tests of their classes OK).
- **Not covered:** his runs (the builders of types 1, 2, 3, 4 and 6, 02 at 200,000 draws, 03).

### V181. The cameras' sources of point 2 read first-hand (E31, "Yes, A to H")

- **What:** every source a camera count of E31's points 1 and 2 rests on, opened and read by me before the robot was
  entered (the rule "Read it yourself"; the agents' findings second-hand to me), the two searches' quotes against the
  pages.
- **How:** the built-in browser, its pages' text searched for the words of cameras and microphones (camera, 相机,
  摄像头, カメラ, камер, microphone, 麦克风, voice); tables printed in images looked at (KEENON, UBTECH, Leju); sites that
  show their text only by script read from their own data feed or script file (Yunmu); two PDFs downloaded on his word
  ("Yes, download both") into the scratch folder and read with macOS's own PDFKit (Astribot S1 542,745 bytes, TALOS
  608,559 bytes); X-Humanoid's brochure from its text as extracted in the second search. No cookie banner accepted, no
  verification step passed.
- **Confirmed, as the searches had them (23 robots):** Phantom MK1 (Newsweek's caption "Phantom MK1 has eight cameras in
  its head."; the article's text says the CEO "envisions Phantom … with eight cameras in its head"); TALOS (one RGB-D
  block, "RGB 1280x720 at 30 fps", "Depth 640x480"; "Speakers 5 W", no microphone); REEM-C ("Stereo camera as eyes",
  "Back camera", "4 omnidirectional microphones"); AgiBot A2 ("six high-definition cameras", "sound source
  localization", "voice commands"); DOBOT ATOM Max ("a 60FPS Full HD vision system, and Intel RealSense D455 depth
  sensing"; "binocular" is the ATOM D's, not used); XMAN-R1 ("Depth Vision Cameras *4", "HD Wide-Angle Cameras *4",
  "High-definition omnidirectional microphones"); U1 Pro ("6-microphone array built into the head … 2 RGB cameras built
  into the eyes"); YMBot D (the script file's camera block after "YMBOT D chassis humanoid robot": "Active binocular
  structured light depth camera", "Color camera resolution: 1280 x 800"; its data feed "耳部收声/喇叭"); 4NE1 Gen 3 (The
  Robot Report: "With the patented Omnisensor and seven cameras", "speakers, and microphones"); AIDOL (3DNews: "две
  стереокамеры", "семь микрофонов"); MenteeBot V3 (Ynet: "five cameras", "voice commands"); Apollo (CNN: "a perception
  camera"); PrimeBOT T1 (IE: "a flip camera", "a multi-microphone array"); Digit (RealSense: "Embedded in the neck of the
  robot, RealSense Depth Camera D455"); Astribot S1 (its sheet with astribot.com's addresses: head RGB-D ×1 and stereo
  ×1, gripper RGB-D ×2, chest RGB-D ×1); Dora (archived: "深度相机 3 斜向下 2 向前 1", "结构光深度相机", "阵列麦克风 6");
  JAKA Kargo ("Vision camera 2"); JAKA π ("Using a camera on its head", "listen to commands"); Moz1 ("头部相机（Intel
  D455） 1", "腕部相机（Intel D405） 2"); Tien Kung 2.0 ("全场景双目结构光3D相机*3" in the 具身天工2.0 block, 173 cm,
  73 kg); Y1 ("头部深度相机*1、7自由度带 视觉机械臂*2", "realsense D435相机", "讯飞语音节点已启动"); YMBot D4 ("双目相机/
  激光雷达/六维力传感器 RGBD相机/鱼眼相机", "阵列麦克风"); CUE7 ("頭部のステレオカメラ"; "ドリブル用のカメラセンサーを
  ＣＵＥ７の腰に配置した。").
- **Not confirmed, so to point 3 (4 robots):** NEO Beta (its count the production NEO's), GENISOM NE01 (page blank, no
  archived copy), Galaxea Kengo (Gasgoo HTTP 468), Leju Kuavo-my (the page now the KUAVO 4Pro's: 1.66 m, about 55 kg,
  against the register's 145 cm and 45 kg).
- **Not covered:** the sources of point 3's microphones (the searches' quotes, not reopened); the robots of point 4
  (the first search's quotes, re-read in part in V176); whether the image sensors' kinds (a camera as one colour sensor,
  a depth camera as the D435's) fit each robot's actual cameras.

### V180. His runs of 02 and 03 after E32, E33 and E34, read back

- **His words:** "02 has run", "03 is done" (2026-11-05).
- **The runs and the code:** the code of commit `b840133` (2026-11-05 11:12:17 +0100), byte for byte the sandbox's
  (`02_composition.py`, `03_comparison.py`, `00_parameters.py`, compared with `cmp`). 02 wrote its four folders from
  11:34:10 to 11:37:00, 03 `figures/comparison/` from 11:49:24 to 11:49:58; 200,000 draws in every robot type.
- **Every file:** the names in `data/consolidated`, `data/parts_taken_apart`, `figures/composition`,
  `figures/parts_taken_apart` and `figures/comparison` (84 pages) the same as the sandbox's; every one rewritten by
  the runs, except the 28 iCloud copies "… 2" in `data/parts_taken_apart` of types 5 and 6 (untouched, his decision)
  and `comparison_materials_6.png`.
- **`comparison_materials_6.png` dated 05:22:47:** 03 writes its pages in order, and this one lies between
  `comparison_numbers_6` and `_7`, both 11:49:30. Its content is the run's: nothing written over its panels (the code of
  05:22, `53c5ae0`, wrote the numbers over every panel, `numbers_above`), bars of 200,000 draws, its lines as
  `comparison_numbers_7` (11:49:30) gives them (type 1 median 399 g; type 6 median 8.9 kg, mean 12 kg, 95 % 8.2 to
  16 kg). Only its date is off; the cause not established (iCloud likely).
- **The draws, draw for draw, all six types** (`scratchpad/check_run_02.py`, read only): each element by material adds
  up to the element by part, the largest relative gap 1.1 × 10⁻⁷ (float32), the copper fixed in alloys (E25) left out,
  which the element by part does not count; with it only copper differs, as built.
- **Titanium and gallium, all six types:** never on the circuit boards. Titanium in the titanium alloy (types 1, 2, 3, 5,
  6) and in the cameras and the other sensors; gallium in the magnets, the cameras (not type 6) and the other sensors.
  The components the elements show: circuit boards, cameras, other sensors, cables; the connectors carry no element of
  their own (their brass's copper fixed in alloys and booked by that material, E25; their plastics no element), as E32
  point 2 builds it.
- **Against the sandbox (2,000 draws):** the shares held and the medians above 0 of titanium and gallium by source and of
  the aluminium alloys' aluminium agree within the sandbox's spread (type 5's titanium alloy held in 10.1 % against
  9.7 %, median 32.6 against 32.2 kg). The one exception, type 6's titanium alloy (median 8.0 against 13.5 kg): two
  robots, the IHMC Nadia ISA v2 (7.6 kg, 20,019 draws) and v5 (13.9 kg, 19,903 draws), each within 0.3 % of the
  sandbox; the median of the two lies where they meet and falls on the side holding a few more draws.
- **Pages looked at:** 03's `comparison_elements_1` (aluminium in the aluminium alloys: one colour, no legend, nothing
  written; medians 12.6, 31.3, 28.6, 36.3 kg for types 1, 2, 5, 6, as the draws), `_21` (tin, by component: nearly all
  the circuit boards'), `_22` (titanium in the titanium alloy: 357 g, 860 g, 32.6 kg, 8.0 kg, as the draws; types 3 and
  4 one line each), `comparison_materials_6` and `comparison_numbers_7`. 02's type 5: `robot_type_5_elements_1` and
  `_2` with their pages of numbers (the critical elements by kind of part, titanium not among them; nothing over the
  panels), `5_…_elements_1` with `5_…_numbers_1` (magnesium and aluminium "in the alloys", titanium "in the alloy",
  33 kg held in 10 %).
- **E29's first and third findings, confirmed in his run** (as the handover of the morning asked): terbium held in
  100 % of the draws of every type (type 3's 99.781 % was the Neo1's); steel no longer stretched, type 3 at most
  80.9 kg (97.5 %: 35.8 kg), type 5 at most 35.2 kg (25.4 kg); the Neo1 in no type's `robots.txt`.
- **Not covered:** the other pages, not opened one by one; the means pages; the tests not run again (the code unchanged
  since V179's 535 OK).

### V179. The numbers of the panels on pages of their own (E34)

- **His words:** "Do we really need all this text in the figure. It might be better to have it separate", "Yes,
  hopefully now it is OK" (2026-11-05).
- **Tests first, seen to fail:** `test_the_numbers_on_a_page_of_their_own` (02, type 1: every element and material
  page and every page of its figures of where the critical elements sit followed by a page of numbers, each panel's row
  on it, nothing beside any panel's title; lithium's median and mean as its draws give them) failed "'elements' !=
  'numbers'"; 03's of the same name failed "0 != 41" (no page of numbers).
- **The older tests that read the numbers above a panel** (12 in the whole suite after the build: the share held, the
  median and mean, the axis's end, a long title against its numbers, the order of the pages, the footnotes, 03's list
  of pages and its panels): changed to read the numbers each panel keeps (`numbers_of`, the same as its row on the page
  of numbers) and to take the pages of numbers in their place; what each checks unchanged.
- **The whole suite:** 535 tests OK (502 s).
- **The sandbox** (2,000 draws, 02 and 03 redrawn): 03 writes 84 pages (2 of notes, 41 of panels, 41 of numbers); looked
  at 03's titanium page (titles, bars, lines, axes, the places of types 3 and 4, no number) and its page of numbers
  (types 1, 2, 5, 6: held in 3.8, 3, 9.7, 19 %; medians 361 g, 941 g, 32 kg, 14 kg), and type 3's first material page
  of 02 (nine panels, nothing written over them).
- **Not covered:** his runs (200,000 draws); the overview pages of where the elements sit keep their labels at the right
  of each row (not in the proposal).

### V178. The light alloys' metals drawn as their alloy, the rest beside (E33)

- **His words:** "Work out a pragmatic solution", "Yes" (2026-11-05).
- **Tests first, seen to fail** (`AttributeError`: no `alloy_split`, `ALLOY_OF`):
  `test_the_light_alloys_metals_drawn_as_their_alloy_the_rest_beside` (type 1: aluminium and titanium drawn as their
  alloy alone, the alloy's draws unchanged, "beside it: battery cells …, electronics …", the collections adding up to
  the element, copper as before, both panels' numbers with the line); `test_a_light_alloys_metal_its_alloy_drawn_the_rest_beside`
  (03: every panel of aluminium and titanium with the line; type 4 without titanium alloy: its place "Titanium alloy:
  none in this robot type" and the line). 03's test data now gives aluminium, magnesium and titanium their own alloys.
- **The whole suite, first run:** 533 tests, 3 failures, all of this step: the older test of an element held in some
  draws (type 1's titanium panel now "in 3.6 % of the draws", the alloy's, not 50 %: the test now takes the alloy's draws
  for the three metals), and types 3 and 4's first element page (smallest text 16.7 px: the empty titanium place kept its
  hidden axes' tick labels at 10 pt; now no ticks). Those three OK after the fix (98 s). The whole suite to be run again
  after the labels below.
- **The sandbox** (2,000 draws): 03's titanium page each type's alloy alone (type 1 in 3.8 % of the draws, median
  361 g; type 5 median 32 kg; type 6 Nadia's two versions, 7.6 and 14 kg), the electronics beside (1.2 to 21 mg);
  type 3's place "held in 0.5 %", type 4's "none". 03's aluminium page the alloys alone, "battery cells 60 to 186 g,
  electronics 8.3 to 14 g" beside.
- **Found by him and fixed in two steps:** (1) the labels misled ("What are you showing, alloy total what???"):
  relabelled on "Yes, relabel", 03's title "Aluminium (Al) held in the aluminium alloys of one robot of each robot
  type", no legend, 02's panel "Aluminium (Al) in the alloys"; (2) the line beside did not belong on the figure ("A
  figure is a figure and not text"): taken off, the left-out amounts named once on the notes pages. Tests changed
  first and seen to fail each time (the line still there; `alloy_split` still a pair), then OK; the older test of an
  element held in some draws now reads the panels by their new titles.
- **The whole suite, final:** 533 tests OK (480 s).
- **The sandbox, final** (2,000 draws, 02 and 03 redrawn): 03's aluminium page the title, six panels of the alloys'
  aluminium with their median, mean and axis note only; 02's element page of type 5: "Magnesium (Mg) in the alloys",
  "Aluminium (Al) in the alloys", "Titanium (Ti) in the alloy", no legend entry for them.
- **Not covered:** his runs (200,000 draws).

### V177. The electronics by their components (E32), built

- **His words:** "senors are par of the elctronics!!", "3 yes", "Yes, include them", "yes do it" (2026-11-05).
- **Test first, seen to fail:** `test_the_electronics_by_their_components` (type 1, 1,000 draws; `AttributeError`: no
  `ELECTRONICS_COMPONENTS`): the five components; no element of interest from the electronics unsplit; titanium from
  the cameras, never the circuit boards; the kind of part Cables the electronics only; a connector's brass copper fixed
  (('Brass', 'Cu') in the fixed copper) and its zinc in the cables' recipe elements; the electronics' detail whole;
  `sensor_component` of a depth camera, a LiDAR, an encoder. Changed: the copper by material (the electronics' circuit
  boards and cables among its sources), the legend and the means page of copper's element page.
- **Found by the suite and fixed:** type 3's means page ran off the page (`test_every_page_is_readable_fit_to_a_screen`):
  the electronics' name five times in a line. Now once, its components after it (`mean_words`); the test of the means
  page made to look at copper's row (it had passed without reaching it).
- **The whole suite:** 531 tests OK (474 s).
- **The sandbox** (a copy of the project, 2,000 draws): 02 (1 min 23 s) and 03 (43 pages, they add up). Read back, means
  over all draws: titanium from "cameras" and "other sensors" only (0.0001 to 0.01 g), the titanium alloy apart; gallium
  from the magnets (0.52 to 0.91 g), the cameras and the other sensors; copper from the circuit boards (163 to 297 g) and
  the cables (177 to 259 g) among its sources, brass's copper fixed (23 to 26 g); the kind Cables holding the electronics
  only. Looked at: 03's titanium and aluminium pages, type 3's means page 1.
- **Found, not of this step:** titanium's panels mix the alloy (hundreds of g to 32 kg, in 0.5 to 19 % of the draws) and
  the sensors (below 3 mg, in about half): their numbers describe neither (types 1, 2, 3, 5, 6; the only element so,
  checked over all elements of all types). Aluminium's panel is the alloys' alone. Matthias: "the titanium figures does
  not make any sense", "the aluminum alloy figure is shit. It is just the al in the alloy". Proposal waiting.
- **Not covered:** his runs (200,000 draws); the name (Electronics or Boards and components, his word).

### V176. The research of E31 checked: the Phantom MK1's battery and seven camera findings re-read

- **His words:** "Yes, research both" (2026-11-05).
- **The Phantom MK1's battery,** read by me in the browser: foundation.bot (Phantom, Cortex, home; no battery, no sensor
  named); bbc.com/news/articles/cedpxwe26l1o (8 June 2026, the sentence "Phantom MK-1, which I am shown, doesn't have a
  battery" found in the page's text); militarnyi.com (31 May 2026, "lacks sufficient battery life"). A mirror of the BBC
  article (bbctodays.pages.dev) answered 404, the BBC's own page was read instead.
- **Seven of the agents' maker findings re-read** by me in the page's text (`innerText`, or the page's HTML where the
  text sits in a hidden tab): Rainbow RB-Y1 ("The vision camera is not provided."), AgiBot A2 ("six high-definition
  cameras"; the RGB-D and fisheye callouts are not in the text, likely images), DOBOT Atom Max ("a 60FPS Full HD vision
  system, and Intel RealSense D455 depth sensing", in a hidden tab), Fourier N1 ("Stereo camera (Optional)"), Torobo
  ("Wide-angle stereo camera x 1 Fisheye camera x 1 Depth camera x 1 Stereo microphone x 1", the optional head),
  GENISOM NE01 ("Stereo Camera 1080p", "Microphone Standard", 1328 mm): each as the agent reported.
- **The counts of E31's table** made by me from the six reports: 6 + 10 + 18 + 10 + 15 + 7 + 78 = 144 robots, the 145 of
  V175 less the Neo1 (not drawn, not researched).
- **Not covered:** the other findings not re-read by me (the agents' quotes from images, Chinese script text and third
  parties as they reported them); class g's robots searched with fewer than four lookups.

### V175. Nickel and titanium of the boards traced (types 3 and 6; all types)

- **His words:** "I want to investigate nickel 06 with a very low value for borads same with 3, I do not understand, why
  there is titanium on the boards. Where do you have the information. I want both investigated." Nothing changed.
- **Nickel**, his run of 02 (200,000 draws, 05:08 to 05:10) and 03's page `comparison_elements_14.png` read: the olive
  bar near 0 in type 6's panel is 40 % of its draws, the robots that carry no battery: the Phantom MK1 (20.1 %, 1.7 g at
  the mean) and Nadia ISA v2 and v5 (10.0 and 9.95 %, 1.4 g), whose only nickel is that of their boards and sensors; in
  type 3 the Phantom MK1 (0.63 %, 1.7 g). Every other robot 0.2 to 1.1 kg, from its battery cells and nickel strips. The
  boards' and sensors' own nickel 1.3 to 3 g per robot in every type: the board's area times
  RAWCLICVehicleElectronics' `Data/04_VehiclePCBComposition.xlsx` (sheet PCPComposition, mg per cm²: PE_HVS, the joints'
  driver boards, 0.2 / 0.5 / 1; ITC 0.4 / 0.8 / 1.5; BMS 0.3 / 0.6 / 1.2; no source per value in the sheet), plus the
  sensors'. "No battery": Nadia tethered (E27.7 point 4); the Phantom MK1 from "Phantom MK-1 … lacks a battery", the BBC
  relayed by UNB (E15, E16.2: second-hand, class C), not read at Foundation's own pages.
- **Titanium:** none in the board metals (`BOARD_METALS`; the PCB sheet has no Ti). It comes from the sensors, which 02
  counts as "Boards and components": RAWCLICVehicleElectronics' `Data/07_VehicleSensorComposition.xlsx`, sheet Sensor
  Details, Ti in mg per sensor element: CMOS image sensor 0.05 / 0.2 / 1, IR camera sensor 0.03 / 0.1 / 0.5, MEMS
  microphone array 0.01 / 0.05 / 0.2, GNSS receiver 5 / 20 / 80 (its BaTiO₃ patch antenna), ultrasonic sensor and
  transducer 10 / 40 / 120 (PZT ceramic). The sheet's Methodology: compositions "derived from known material formulas"
  (PZT 6 % Ti), its sources named in general (datasheets, teardowns, IMDS/GADSL, papers), no source per value; its
  Element Legend: Ti "PZT piezoelectrics, thin-film resistors". Per robot: median 1.0 to 1.8 mg.
- **Why in about half the draws only** (held 49.9, 54.2, 47.8, 48.4, 90.0, 59.8 % in types 1 to 6): the robots of the
  parts files without a camera or microphone among their sensors (only encoders, motion sensors, a LiDAR in the base):
  type 1 15 of 31, type 2 46 of 102, type 3 55 of 99, type 4 37 of 85, type 5 none of 5, type 6 the Fuxi on legs and on
  wheels.
- **Seen in passing:** the titanium alloy of types 5 and 6 (10 and 20 % of their draws) is the hydraulic robots' Moog
  ISA actuators (E27.7): Atlas HD ISA v2 32.3 kg, v5 knees 32.7 kg; Nadia ISA v2 7.6 kg, v5 14.0 kg; types 1 to 3 the
  AgiBot X1 (0.36 kg) and the Unitree H2s (0.75 to 1.28 kg).
- **Not covered:** whether the robots without a camera have one (their makers not read for it here); the Phantom MK1's
  battery first-hand; the sibling's values against sources of their own.

### V173. The handover of 2026-11-04 against the code and the outputs on mac-mini

- **His words:** "Get the the handover and check with the code here. icloud is still syching", then "Yes, align git".
- **Git:** `git fetch`, then `git diff --name-only origin/main` (no tracked file different, `.DS_Store` aside) and
  `git ls-files --others --exclude-standard` (nothing untracked): the files were GitHub's `main` at `d02a2eb`
  (2026-11-04 15:21), the local `main` at `fa75985`, 8 commits behind. On his word `git reset --mixed origin/main`:
  `main` at `d02a2eb`, `git status` clean; no file touched.
- **The handover against the code:** V172's alphabetical element pages are in `03_comparison.py`; E30 not built (no
  "outlier" in the code; every place E30 names exists: 01's `IN_RUN_*`, `check_type_sheet`, `robots_table_rows`, the
  register builder's `in_the_run`, 02's `read_apart_inputs`, `lead`, `taken_apart_notes`, the console line); its line
  "Not committed" out of date (`d02a2eb` holds V172, E30 and the entry). The run paths under `~/Library/Mobile Documents/…`
  are the same files as `~/Documents/GitHub/…` here (one inode).
- **The test suite** on the code as it was: 523 tests OK (454 s).
- **The outputs** (`stat`, `cmp`; numpy headers read, nothing written): in `data/parts_taken_apart/5_…/` and `6_…/` iCloud
  kept 14 files "… 2" each: the "… 2" his run of 2026-11-04 14:57 (type 5 15 robots drawn with the Neo1, the Atlas HD ISA
  v2 and v5 knees; type 6 8 with the Nadia ISA v2 and v5), the plain names his run of 2026-11-01 18:01 (12 and 6); both
  sets 200,000 draws, columns as their lists; `by_material` from 2026-11-04 only. `figures 2/` holds the other Mac's
  pages of 2026-11-04 (comparison 43, composition 84, parts_taken_apart 126, schemas 45 files); `figures/` only
  `parts_taken_apart/` of types 3 to 6 of 2026-11-01. No file "dataless". Nothing deleted: his decision.
- **Not covered:** the other Mac (whether iCloud brought the old plain names there too); his runs since 2026-11-04.

### V174. The Neo1 an outlier, not drawn (E30), built

- **His words:** "Ok it is neo. It should be out. Mark it as outlier." (2026-11-04); "Yes, 3 to 5" (2026-11-05).
- **Tests first, seen to fail** (2026-11-05, before the build; `AttributeError`: no `IN_RUN_OUTLIER`, `check_outliers`,
  `outlier_robots`; the settings' tests 4 failures and 1 error): `test_the_neo1_the_one_outlier` and six refused values of
  `composition.outliers` (test_parameters); `test_the_neo1_an_outlier_in_the_sheets_of_types_3_and_5` and the counts of
  the sheets Type 3 (163 drawn, 17 without a mass, 1 outlier) and Type 5 (10, 1, 1) (test_make_humanoid_register);
  `test_an_outlier_says_it_is_not_drawn` (also where taken apart; the old words a fault; the outlier's words without the
  setting a fault) and `test_an_outlier_of_the_setting_not_in_the_register` (test_schemas, a small register);
  `test_the_neo1_an_outlier_marked_in_the_tables_and_left_out_of_what_is_drawn` (types 3 and 5: the table keeps every
  robot, the Neo1 alone marked, on one page with the key's words, the titles "all its 163 / 10 robots with a mass", the
  pages readable with no overlap, the cards, the counts, the templates 137 / 124 / 172; type 4 unchanged);
  `test_the_neo1_an_outlier_not_drawn_in_types_3_and_5_and_named_on_their_notes` (02: not in the inputs or the draws, its
  rows kept in type 3's file, `listed` 163 and 10, the lead "Robot type 5, all its 10 robots", the sentence on the notes
  and nowhere else); `test_its_notes_name_the_outlier_not_drawn` (03). Changed: type 3 drawn over 163 robots in 172
  versions (was 164 in 173); the words for the Neo1's joints read from type 3's file, where its rows stay.
- **After the build:** the new and changed tests OK (19 of 01's pages, 02 and 03: 163 s; 43 fast: 3 s), but one, as it
  must until his run of the register builder: `test_what_it_writes_equals_the_register_on_disk` (the file on disk lacks
  the About line and "not drawn: an outlier"). The whole suite (476 s): 530 tests, 528 OK; the 2 failures both the
  register on disk, written before the change: that one, and `test_the_real_register_holds_together`, where 01's new
  check finds the Neo1 "drawn: its own parts" in the sheets Type 3 and Type 5 ("but an outlier is not drawn"). Both
  pass once he runs the register builder (his run 2, before 01).
- **The sandbox** (a copy of the project in the session's scratch folder, `composition.draws` 2,000, its own `data/` and
  `figures/`): the register builder (Type 3 181, Type 5 12 robots), 00 (the setting in force), 01 ("No fault found"; 46
  pages), 02 (1 min 23 s: type 3 "drawn part by part over 163 robots …; not drawn, an outlier: 208 Neo1", type 5 over 10,
  the same; they add up), 03 (43 pages, they add up). Read back: no type's `register.txt` names the Neo1; type 3 91.8 kg
  at the mean, its heaviest draw 395 kg; type 5 92.9 kg, 171 kg (E30's table at 200,000 draws: 92.5, 396; 92.5, 171);
  steel at the mean 14.7 and 14.9 kg (E30: 14.7, 15.0), at most 73 and 31 kg; type 3's terbium in 100 % of its draws
  (E29's first finding gone at 2,000 draws). Looked at: 01's `overview_2.png` (the cards of types 3 and 5), the robots
  tables of type 3 (page 2 of 11) and type 5 (page 1 of 2), type 5's notes page 1, 03's notes page 1: as described.
- **Not covered:** his runs (200,000 draws); the other Mac; the robots tables' mass axis, still to 1,600 kg for the
  Neo1's row (his word).

## 2026-11-04

### V172. 03's element pages in alphabetical order of their names

- **His words:** "Alphabtetic is easier to find", then, of the two answers offered, "Elements only" (2026-11-04).
- **Test first, seen to fail:** `test_the_element_pages_in_alphabetical_order_of_their_names` (the fixture's 22 elements):
  the pages began "Lithium, Boron, Magnesium, Aluminium …". After the change (`pages`: the elements sorted by
  `element_label`, 'Aluminium (Al)' …): the eight tests of `tests/test_comparison.py` OK (115 s); the material pages
  checked to keep 02's order.
- **Not covered:** his run of 03 (the same 22 element pages, so the same 22 files, now in the new order); the rest of the
  suite not rerun (no other test reads 03; the change is in 03's `pages` only).

### V171. His runs of 02 and 03 after E29 read back

- **His words:** "I'll run both", "Both are done!!" (2026-11-04).
- **Times** (`stat`, against the code's): 02_composition.py changed 14:14:55, 03_comparison.py 14:29:21. 02 wrote
  `data/consolidated/` 14:55:18 to 14:55:46, `by_material.npy` of the six types 14:55:54 to 14:57:28 (with `materials.npy`,
  the last table 03 reads), its last page 14:57:43; no table of 02 older than its code. 03's pages 14:57:54 to 14:58:27,
  after 02 had ended: 43, all `comparison_*`, nothing else in `figures/comparison/`.
- **The draws, read back** with 03's own functions (nothing written): 200,000 draws each, `problems` none. Each element by
  material against the element, largest relative miss 1.2e-07 (float32); the copper fixed by alloy against "Cu fixed in
  alloys", largest miss 4.7e-07 kg; the alloys holding copper per type: aluminium alloys, brass, the magnets and steel in
  all, magnesium alloys in types 3 to 5, stainless steel in types 1, 5 and 6.
- **All 43 pages,** redrawn in memory from his draws by the scratch script `scripts/check_03_pages.py` (the tests' rules,
  33 s): no text over data, no drawn text below 14 pt, nothing off the page. 15 material pages (no type holds ceramics),
  22 element pages. A type without a panel: magnesium alloys (types 1, 2, 6 none; 3 and 4 in 0.59 % and 1.63 %),
  titanium alloy (3 in 1.22 %, 4 none), stainless steel (2, 3, 4 none), fibre composites (1 to 5 none), Other (1, 2, 4
  none; 3 in 0.62 %), magnesium the element as its alloys.
- **Looked at by me:** the total by material, steel and the magnets by kind of part, titanium by material, the body regions,
  the second notes page. The means of the total, 34, 84, 99, 67, 193 and 87 kg, as V168's (34.3, 84.3, 99.3, 66.7, 192.8,
  87.0).
- **Found, reported, not changed** (EVIDENCE.md E29, "Found"): (1) steel's panels of types 3 and 5 pressed into their first
  bars by the Neo1 (976 kg of steel; one of type 5's 11 robots, 9 % of its draws), as the total, part groups and body
  regions of type 5 less so; (2) titanium by material: in types 1, 2, 3, 5 and 6 the boards' milligrams and a titanium
  alloy's kilograms in one panel, its mean over 100 times its median ("median 0.0000014 kg, mean 5.5 kg"), the bars one at
  0; the only page so (checked over every material, element and the total); (3) terbium, type 3: held in 99.781 %, written
  "in 100 % of the draws", the only share so rounded. All three as on 02's pages, drawn by 02's functions.
- **Not covered:** the pages not looked at by me are checked by the script only.

### V170. 03 built (EVIDENCE.md E29): tests, faults, the suite, a sandbox run and its pages

- **His words:** "Yes, agree E29", "Yes, build 03" (2026-11-04).
- **Tests first, seen to fail:** `tests/test_comparison.py` rewritten (seven tests: six robot types' draws written in 02's
  own files into a temporary folder, 400 draws, each adding up as 02's do; then 03 run on them) and one test in
  `tests/test_parts_taken_apart.py` (`TestCopperSplit`, 02's new table). Before the code: 8 errors (02 had no
  `FIXED_MARK`, no table `by_material`).
- **02:** `by_material_table` writes each element of interest by the material it comes from, '<element>: <material>',
  and the copper fixed in each alloy, '<element>: <material> (fixed in alloys)', into `data/parts_taken_apart/<n>_<name>/
  by_material.npy`. Checked on type 1 at 2,000 draws: each element's columns add up to the element (rtol 1e-5, float32),
  the fixed columns are copper only and add up to "Cu fixed in alloys"; "Cu: Copper" and "Cu: Brass (fixed in alloys)"
  among them.
- **03, deliberate faults (each seen to stop it, nothing drawn):** a table one draw short (type 2's total); the materials
  1 % off their total (type 1); the materials by kind of part 1 % off (type 4); the elements by material 1 % off (type 5);
  a table missing (type 3's `by_material.npy`): 03 returns 1 and makes no folder.
- **03, the pages (fixture):** every page of E29 written, named `comparison_<series>_<k>.png` (notes, total, a page per
  material held, a page per element held, part groups, body regions, copper); a material no type holds (ceramics in the
  fixture) has no page; a type without the item (terbium in type 1) has no panel, five panels drawn and its place
  saying so, the share scale on the first panel drawn in each row (types 2 and 4 there); no text over data, no drawn text
  below 14 pt, nothing drawn off the 16 × 9 page (the legend's rows included); the four pages of the old form and a page
  numbered beyond those drawn removed by their exact names, another file in the folder untouched.
- **The suite:** 522 tests, OK, 470 s (before the share scale's change, whose test file then passed alone: 7 tests, OK).
- **Sandbox** (the scratch copy, `composition.draws` 2,000; his register and parts files of today copied in, read only
  from the project): 02 exit 0 in 1 min 24 s; 03 exit 0 in 33 s, "6 robot types, 2,000 draws each: they add up", 43 pages
  (2 of notes, 1 total, 15 materials: no type holds ceramics, 22 elements, part groups, body regions, copper). All 43
  checked by a script with the tests' rules (`scripts/check_03_pages.py` in the scratch folder): `problems` none; no text
  over data, nothing below 14 pt, nothing off the page.
- **Looked at by me:** the total by material, copper by kind of part, magnesium alloys (types 1, 2 and 6 none; 3 and 4
  held in 0.45 % and 1.1 %, no panel), titanium alloy, copper by material, terbium, the part groups, copper three ways, the
  first notes page. The copper by material and the copper three ways give the same medians per type (2.1, 3.5, 3.7, 2.9,
  4.3, 3.6 kg), as they must (both the inflow), and the same as V169's preview. The means of the total, 34, 84, 100, 67,
  187 and 87 kg at 2,000 draws, against V168's 34.3, 84.3, 99.3, 66.7, 192.8 and 87.0 at 200,000 (type 5's: the Neo1,
  1,200 kg, one of its 11 robots, drawn a little less often at 2,000).
- **Checked against the draws:** terbium's "in 100 % of the draws" on type 3: held in 99.9 % (2 of 2,000 draws without,
  both the Neo1's); 02's `panel_number` writes a share from 10 % as a whole number. On 02's pages too. Reported, not changed
  (EVIDENCE.md E29, "Found"). Type 5's "in 97 %": 96.65 %, its 67 draws without all the Neo1's.
- **Nothing left behind:** what the old 03 used of 02 and 01 (`interval_bars`, `mass`, `MUTED`, `MARGIN`, `schemas.write`,
  `wrap`, `save`) is still used by 02 or 01 itself; the old 03's own functions went with its file's rewrite.
- **Not covered:** his run at 200,000 draws (02 must be rerun first, for its new table); the pages not looked at by me
  (the other materials and elements, body regions, the second notes page) are checked by the script only.

### V169. 03's preview (EVIDENCE.md E29): the Copper page

- **His words:** "Yes, agree E29" (2026-11-04).
- **How:** a script in the scratch folder (`scripts/preview_03_copper.py`), reading the project's inputs only, each type
  drawn in memory at 2,000 draws, six panels of 02's own `by_material_panel` (copper, inflow, by the material it comes
  from, copper fixed in alloys grey), one legend, 02's `make_room`; nothing written into the project.
- **Result:** 02's `texts_over_data`: none; 16 × 9 inches at 150 dpi, its smallest text 14 pt, 23 px on a 1920 × 1080
  screen. Medians 2.1, 3.5, 3.7, 2.9, 4.3 and 3.6 kg; the long type names on two lines.
- **Not covered:** the other pages; 02 writing its split by material (03 reads it, E29 question 2).

### V168. His runs after E28 read back: 02 closed

- **His words:** "02 is runing", "done" (2026-11-04). Read only.
- **Times:** the register 13:46:36 and type 5's file 13:46:43 (its "Atlas HD ISA v2", "Atlas HD ISA v5 knees") after
  their code (13:22:14); 01's pages 13:47:13 after 01's (13:25:35); 02's outputs 13:48:57 to 13:51:02 after 02's
  (13:10:04). No page of `figures/composition/` or `figures/parts_taken_apart/` older than the run; no robot of types 1
  to 6 "not yet taken apart".
- **The draws:** each type 200,000; materials adding up to the total (≤ 2.3 × 10⁻⁷); no median of 0; nothing below zero
  in the summaries; means 34.3, 84.3, 99.3, 66.7, 192.8 and 87.0 kg.
- **The notes** (02's `on_estimates` over his files): "the joints' masses estimated, no torque stated" type 3 the
  AlphaBot 2 and Neo1, type 5 Neo1, type 6 Nadia's two versions; the battery's energy 124, 5 and 3 robots, each type's
  count.
- **The robots tables** (01's, built from his files): no text over text in any of the six; the joints of the Atlas
  (old) 28 and 28, Neo1 41, Nadia 31.
- **Not covered:** the pages by eye (their checks through the functions that draw them).

### V167. The robots tables: the Atlas (old)'s names and the hydraulic robots' joints (EVIDENCE.md E28 points 6, 7)

- **His words:** "Yes, fix both" (2026-11-04).
- **Measured first:** text over text in every robots table of the six types (his files): only the Atlas (old)'s two
  names, over the column Height of type 5's table.
- **Tests first:** `TestRobotsTablesOfTheHydraulicRobots` (no text over text in any of the six tables, built in a
  temporary folder with the register; the Atlas (old) 28 joints, Neo1 41, Nadia 31, the T800 Dev 25 as before) and the
  tests renamed to "Atlas HD ISA v2" and "Atlas HD ISA v5 knees" failed before the code, pass after.
- **Found in the sandbox's preview after it:** the joints written "28.0" and "41.0" (the counts read as decimals), "1200
  kg" touching "41.0"; the test checked 28 == 28.0. A test of whole numbers added (failed, then passed); the count made
  whole. The preview again: names inside their column, "28", "28", "41", the heading inside its band.
- **The suite:** 520 tests, all pass but the register on disk (its builder writes the new names until his run).
- **Not covered:** his runs; the Atlas HD's cell "Joints" of "where its numbers come from" stays white (its actuators
  stand in the sheet Parts, the cell reads the sheet Joints), reported.

### V166. Closing 02: the package built (EVIDENCE.md E28)

- **His words:** "Yes, do the package" (2026-11-04).
- **Measured first:** the robots tables' heading "Frame and shell" 1.3 px past the band's right edge on every type's
  table (his files, 100 dpi); after the fix at least 0.1 inch inside on all six (a test).
- **Tests first:** three new tests (the headings inside the band; `estimate_kinds`' 'joint estimates' for Neo1 and Nadia,
  the DR02 'joint torques' only, 01's table groups unchanged; 02's notes naming Neo1 and Nadia under "the joints'
  masses estimated, no torque stated") failed before the code, pass after. The removals: the tests that used the four
  functions changed first (element_shares the tests' own helper, its ten checks of the recipes kept; taken_count for
  taken_words; the triangles patches gone; the template's 44.7 % computed in its test) and passed before and after.
- **Found in the build:** cutting `median_share` by a script took the module's lines after it up to the next function
  (AVERAGE_JOINTS, TYPES_34_SHARED); seen in its diff (38 lines), the file restored from git and only the function
  removed; the other three cuts checked line by line (only their functions), the spacing as before.
- **The new kind of joint estimate across the six files:** Neo1 (only), Nadia's two versions and the AI² AlphaBot 2
  (both kinds).
- **The suite:** 518 tests, all pass. **The sandbox** (2,000 draws): 01 "No fault found", 02 "02 done in 1 min 21 s".
- **Found in its preview (type 5's robots table, 01), mine from E27:** the Atlas (old)'s two names run over the
  Height and Mass columns (text over text, no test catches it); the Joints column counts electric joints only (the
  Atlas (old) 0, Neo1 2). Reported, for his word.
- **Not covered:** his runs of 01 and 02.

### V165. His rerun of 02 after V164 read back

- **His words:** "I rerun 02", "02 run complet" (2026-11-04). Read only.
- **Times:** every page and draw of the rerun (12:58:29 to 13:00:34) after the fix in 01 (12:45:36); no page of
  `figures/composition/` or `figures/parts_taken_apart/` older than it.
- **The notes:** types 5 and 6's notes page 1 read by eye: the battery's energy lists five and three robots, as "the
  battery of 5" and "the battery of 3" say; Neo1, Nadia and the Phantom MK1 no longer. Types 3, 5 and 6 by 02's
  `on_estimates` over his files and register: 124, 5 and 3 robots listed, each type's battery count of
  `template_shares` (137, 124, 173; 4, 5, 15; 3, 3, 8), none of them without a battery.
- **The draws:** each type 200,000; materials adding up to the total (largest relative difference 2.3 × 10⁻⁷); no
  median of 0; nothing below zero in the summaries. Means 34.3, 84.3, 99.3, 66.7, 192.8 and 87.0 kg.
- **Not covered:** type 3's notes pages by eye (their list checked through the function that writes it).

### V164. The notes pages: no battery estimate for a robot without a battery

- **His words:** "Yes, fix it" (2026-11-04), to "Shall I fix the notes pages' battery wording (01's estimate_kinds)?" (V163).
- **What:** 01's `estimate_kinds` gives "battery per kg" only to a robot that carries a battery (`has_battery`); 02's
  notes pages list under "the battery's energy a share of the robot's mass" only those. 01's pages unchanged (its robots
  table reads the joints' kinds only); 02's draws unchanged.
- **Tests first:** `TestNoBatteryNoBatteryEstimate`: the Phantom MK1, Nadia's two versions and Neo1 without, the Alex,
  the Kaleido 9 and the MH3 with; it failed before the fix, passes after.
- **The suite:** 515 tests, all pass (the register on disk too, since his run of its builder).
- **The sandbox** (02 at 2,000 draws): type 5's notes list five robots under the battery's energy ("the battery of 5"),
  type 6's three ("the battery of 3"); Neo1, Nadia and the Phantom MK1 no longer.
- **Not covered:** his run of 02. The notes' "the joints' masses from their torques" still names Neo1 and Nadia (their
  forearm and pelvis joints' masses estimated, not from torques): not asked, reported.

### V163. His runs of E27 read back

- **His words:** "all are run, check. Are we now done with all robots?" (2026-11-04). Read only.
- **Times** (each output against the code that writes it): the register 12:03:53 and type 5's file 12:04:08, after
  their code's last change (11:48:14); 01's pages 12:04:19; 02's draws and pages 12:06 to 12:08, after 02's last change
  (10:46). Types 3 and 6's files (11:47) and types 1, 2 and 4's (2 November) older than the shared module's change of
  11:48: every one of the six files and the register rebuilt in a temporary folder by the code as it is now equals the
  file on disk cell by cell.
- **What they hold:** every robot with a mass of types 1 to 6 drawn from its own parts (30, 96, 164, 124, 11, 5; 301
  robots, none "not yet taken apart"); 23 robots of types 1 to 6 have no stated mass, listed, not drawn (his rule). The
  Atlas (old) "ISA v5 at the knees": its knees 1.6 kg, its other places 0.92 kg. 01's checks of the six files (in
  memory): no fault.
- **02's draws** (each type 200,000; the parts files read in slices): every draw's parts and materials add up to its
  total (largest relative difference 2.4 × 10⁻⁷, the files' single precision); no median of 0; no quantity of a summary
  below zero. No remainder of types 5 and 6 below zero. Frames below zero, reported by 02, none of them changed by E27:
  type 3 the Matrix-1 (85 of 1,223 draws of it, 7 %), the Figure 02 (2.6 %), the Walker S2 (2.2 %), the Agile One and
  the 1X NEO Beta (one draw each); type 4 the 1X NEO (16 %, E21), the MagicBot (0.57 %) and five with one or two draws;
  type 1 twelve, each in 0.015 to 0.14 % of its draws.
- **Pages:** types 3, 5 and 6's 104 pages (42 in `figures/composition/`, 62 in `figures/parts_taken_apart/`) all of this
  run, none left from before. Read by eye: type 5's notes page 1 and overview page 1, type 6's notes page 1 and overview
  page 1. **Found: the notes pages list robots that carry no battery under "the battery's energy a share of the robot's
  mass"** (type 5: Neo1; type 6: Nadia's two versions and the Phantom MK1, the Phantom since E16.6): 01's
  `estimate_kinds` takes every robot without a battery voltage for one, a battery or not; type 5's page says "the
  battery of 5" and names 6. Its "the joints' masses from their torques" also names Neo1, whose two joints have no
  torque (an estimated mass). Reported, not changed.
- **Not covered:** the other 100 pages by eye (the suite's page tests check every page kind on the sandbox: no text over
  data, readable, no project words).

### V162. The Atlas (old)'s v5 at its knees only

- **His words:** "Yes, knees only" (2026-11-04), EVIDENCE.md E27.8.
- **Tests first:** the builders' and the drawing tests changed to the version "ISA v5 at the knees" (its knees 1.6 kg
  each, its other places 0.92 kg) and a new test, its frame and the v2 version's above zero in every draw (3,000
  draws): 6 failed before the code, all 15 pass after.
- **The suite:** 513 tests, all pass but the register on disk, as in V161 (until his run of its builder).
- **The sandbox** (2,000 draws; the register, type 5's builder, 01 "No fault found", 02 "02 done in 1 min 22 s"): type 5
  drawn over its 11 robots (15 with their versions), no remainder of it below zero any more. Reported still, not new
  and untouched by this step: the Figure 02's frame below zero in 8.3 % of its draws (type 3; its frame 18 % of it at
  the modes, E15.7) and the 1X NEO's in 11.1 % (type 4, E21).
- **Not covered:** his runs.

### V161. E27.7 built: tests first, the suite, the sandbox

- **His words:** "Yes, build it" (2026-11-04), E27.7 as agreed ("Yes, agree E27.7").
- **Tests first:** 13 new tests of the builders, the register and the new kind (`TestHydraulicRobots`,
  `TestHydraulicsKind`, the register's sheets Type 3 to 6) failed before the code (V161's run at 14 tests: 4
  failures, 9 errors); 3 drawing tests (`TestHydraulicActuators`: the body the actuators less their valves, boards and
  sensors in every draw, never below zero, among the remainders; the oil its volume times its density; the Atlas (old)
  without an electric joint, its parts adding up to its mass) failed before types 5 and 6 were built into the tests'
  folder. All pass.
- **01's new checks seen to catch their fault:** a body without its actuators, oil without its volume, actuators too
  light for their valves and boards (three tests, each a fault put in on purpose).
- **The suite:** 512 tests, all pass but one, as expected: the register on disk differs from what its builder now
  writes (`test_what_it_writes_equals_the_register_on_disk`) until his run of `tools/make_humanoid_register.py`.
  Tests changed to the agreed state: type 3's 164 robots in 173 versions, its template 137 of 173; types 5 and 6 none
  left to take apart; the kinds' names with the new one; type 3's order with Neo1.
- **The sandbox** (`scratchpad/sb_e277`, a copy of the code and `data/raw` and `data/researched`, its draws 2,000, its
  outputs in it): the register and the six builders, 01 ("No fault found"), 02 ("02 done in 1 min 21 s"); types 5 and
  6 drawn part by part over 11 and 5 robots, type 3 over its 164. From its draws: Neo1 1,200 kg, its 39 actuators about
  48 kg, its frame of steel about 976 kg, its shell 140 kg (the template's 11.5 %); Nadia's frame and shell 59 to 67
  kg; every actuator body above zero; **the Atlas (old) with the v5 its frame below zero in 2.1 % of its draws**
  (E27.8). The new row drawn on type 5's pages (its preview) with no text over its data.
- **Not covered:** his runs (the register, the builders of types 3, 5 and 6, 01, 02 at 200,000 draws); 03; types 3,
  5 and 6's pages read page by page (the sandbox's overview page 1 of type 5 only).

### V160. The oil's density read (EVIDENCE.md E27.7 point 6)

- **His words:** "Yes, agree E27.7" (2026-11-04), its point 9.6: "download and read both before 6 is entered".
- **How:** the two datasheets downloaded into an empty folder of the scratchpad (`pdfs_oil/`; 212,004 and 447,875
  bytes, as their servers' headers said, each a 2-page PDF), their text taken out with PDFKit, each table read.
- **Result:** ENEOS 5606J 0.869 g/cm³ and Chevron 5606 0.87 kg/l, both at 15 °C, typical values; the mode 0.87 holds.
- **Not covered:** the density at the robots' working temperature (both at 15 °C); the oil any of the three robots
  uses (none states it).

### V159. The facts behind E27.7's spec

- **His words:** "all as recommended" (2026-11-04), E27's questions 2 to 14; the spec next.
- **Read:** Neo1's 41 joints by region on the Sina page itself (上海证券报's reporter), its words in E27.7; the DRC
  Atlas's IEEE Spectrum page (no split of the 28); the register builder (`mass_bounds`, `ADDED`, `TAKEN_APART`: a
  register mass is the catalogue's, a block's own mass is drawn, as the Moby's); `tools/parts_taken_apart.py`
  (`block`, `robot_rows`, the shell's share 0.0575 / 0.115 / 0.1725); 02's `Shared` (the joint sizes 'small' and
  'large' only) and its magnets by grade class; the sibling's car sensor types (`07_VehicleSensorComposition.xlsx`,
  sheet Sensor Details: 'position sensor', 'pressure sensor' among them).
- **Arithmetic:** the G1's weighed motor (JointParts: stator 94.3 g at 36 % copper and 5 % plastics, rotor 42.9 g at
  90 % magnets, carrier 16.9 g) 22 % copper, 25 % magnets, 39 % electrical steel; MiniHyQ's motor 11 % of its unit,
  so 2.4, 2.75 and 4.3 % of the unit; Neo1's motor 20 % (E) of its actuator, so 4.4, 5 and 7.8 %; the ISA's rod (12 mm,
  120 to 140 mm of steel) and piston 0.12 and 0.15 kg of 0.825 and 1.505 kg; Neo1's shell 69 / 138 / 207 kg.
- **Not covered:** whether 01 and 02 take a robot without electric joints, and magnets named by grade class in a
  part's shares: tests first, in the build.

### V158. The seven PDFs read (EVIDENCE.md E27.6)

- **His words:** "Yes, download them" (2026-11-04), the seven PDFs of E27.5.
- **How:** downloaded with `curl` into an empty folder of the scratchpad (`pdfs_e27/`), each checked as a PDF by
  `file`, its size equal to its server's header; the text taken out with macOS's PDFKit (`osascript`; poppler and
  pypdf not installed, nothing installed) and searched for masses, materials, oil and parts; each quote in E27.6
  read in its paragraph or table.
- **Result:** E27.6. Two readings of tables taken out as text, checked in their row: HyQ's "70kg (external hydraulic
  system), 91kg (onboard hydraulic system)" and the Type 30's weight column, whose five rows stand in the order of its "Five Basic Sizes", Series 30 to 35
  (0.19 kg the first, the Series 30's; the series' names come out of the PDF apart from the table, so the row is
  matched by its order).
- **Arithmetic:** HyQ's hydraulics on board 91 − 70 = 21 kg; MiniHyQ's pump, motor and gearbox 1.94, 1.36 and 0.43
  of 12 kg = 16, 11 and 4 %.
- **Not covered:** the figures in the PDFs (images; their labels only as text); the oil's density.

### V157. The hydraulic robots' sources read first-hand (EVIDENCE.md E27)

- **His words:** "Yes, prepare it" (2026-11-04), the research step of E16.5 question 4.
- **What:** the three agents' quotes behind E27, against the pages themselves.
- **How:** each page opened in the built-in browser, its text searched for the quoted words: New Atlas on Neo1; the
  163.com interview of Neo1's founder; IEEE Spectrum on Nadia (2022) and on HyQReal (2019); Moog's 24 Series page;
  the Frontiers paper's Tables 1 and 2 and its ISA text; habr.com's Atlas article; Calvert's thesis (arXiv HTML).
  The PDFs' sizes from their servers' headers only (`curl -I`), nothing downloaded.
- **Result:** every quote E27 marks "read" stands on its page as written. The agents' readings agree with the pages,
  but on one point: the agent saw Nadia's "3 DoF electric pelvis" (2022) against the 2024 paper's electric hip and
  spine yaw as a disagreement; they agree (two hip yaws and the spine yaw, three).
- **Arithmetic:** type 5's mean mass with Neo1 188 kg, without 86 kg; type 3's 97 and 90 (the register's modes, each
  robot as often).
- **Not covered:** the sources E27 marks "agent" (P4's release showed no text to me; Neo1's site refused its
  certificate); the seven PDFs (E27.5, his permission first).

### V156. Are types 1 to 6 complete, and are 01 and 02 done? A check of the state

- **His words:** "Read the handover and check all the code and then tell me what are the next step. Do you have now
  all the data of type 1 to 6? This is essential as I want to be sure that 01 and 02 are done and verified"
  (2026-11-04). Read only; nothing run into `data/` or `figures/`.
- **Git:** `main` equals GitHub (`11ae306`, 2026-11-02 15:56), no change in the working tree.
- **The robots of each type** (the register and the six parts files on disk, through 01's `taken_count`): type 1 30
  of its 30 robots with a mass taken apart; type 2 96 of 96; type 3 163 of 164 (left: 208 Neo1); type 4 124 of 124;
  type 5 9 of 11 (left: 44 Atlas (old), 208 Neo1); type 6 4 of 5 (left: 202 Nadia). Without a stated mass, not in the
  evaluation: 1, 1, 17, 11, 1 and 0. The three left are the hydraulic robots kept for their own research step (E15.7
  point 10, E16.5 question 4); until they are in, 02 writes types 3, 5 and 6's draws from the workbook.
- **01's checks on the real inputs** (every check of its `main`, without drawing): 22 checks, the six parts files
  among them, no fault.
- **The suite:** 497 tests, all pass (`scratchpad/tests_check_1104.log`).
- **The outputs on disk against the code:** 01's pages of 2026-11-02 13:58 and 02's draws and pages of 14:00, before
  the last commits of `01_schemas.py` (14:49) and `02_composition.py` (15:56): no `copper.npy`, no means pages, the Al,
  Mg and Ti elements still the alloys' whole mass. 01 and 02 are to be run again.
- **Code called by no code, only by tests:** `taken_words` (01; its caller replaced by E23 in `98a83f5`, not listed
  then), `element_shares` (01) and `triangles` (02), known since E19, `median_share` (`tools/parts_types_3_and_4.py`,
  since 2026-10-30: a test checks the template's 0.447 with it); `texts_over_data` (02) is the rule E26 checks with, by
  design.
- **Not covered:** the outputs of the next run of 01 and 02 (to be checked after it).
- **Date:** 2026-11-04.

## 2026-11-02

### V155. E26: no text over a chart, the rule and the pages

- **His words:** "Cupper is bad. Text over the figures. Build a rule, which prevents this. The figure is first and not
  the text Tex can go to other places"; "Yes, build it" on the preview (2026-11-02).
- **The rule as a test first:** `TestNoTextOverData` failed on 13 texts (the Cu panel's list; the median and mean
  labels of Copper, Aluminium, Silver, Gold, Tantalum, Nd+Pr and Dysprosium on the critical elements' figure); passes
  after the change. Four tests of the old layout rewritten to the new places (the numbers above the panel; the means
  on their own pages; the order of the page series). The suite: 497 tests, all pass (`scratchpad/tests_rule2.log`).
- **Pages looked at:** the preview of type 1 (element page 2, means page 1, the critical elements' page 1: no text
  over a bar or a line); 02 in the scratch copy (2,000 draws), "they add up", "02 done", two means pages for every
  type; type 4's means page 1 read (its copper row: Copper 2.1 kg; Aluminium alloys (fixed) 490 g; Battery cells
  306 g; Boards and components 210 g; Brass (fixed) 24 g; Steel (fixed) 9.8 g; NdFeB magnets (fixed) 1.3 g).
- **Not covered:** 01's pages (its tables are text in boxes by design; the box rule of V151 covers its overview);
  the workbook types' pages; his run of 02.
- **Date:** 2026-11-02.

### V154. E25 built: copper recycled as copper, fixed in alloys, and the inflow

- **His words:** "So we have to add it to the inflow cupper, but we have to destiguish, what is fixed in alloys like
  Al aalloysa nd brass", "and what can be recycled as elemental Cu", "Yes, build it" (2026-11-02).
- **Tests first:** the four new tests failed before the code (no table 'copper', no `COPPER_COLUMNS`, no copper.txt);
  pass after it. The suite: 496 tests, all pass (`scratchpad/tests_E25b.log`).
- **Scratch run of 02** (2,000 draws): "they add up"; every type's `copper.npy`, the inflow's mean per robot: type 1
  2.08 kg (recycled 1.89, fixed 0.19), type 2 3.76 (3.01, 0.75), type 4 3.13 (2.60, 0.53); types 3, 5 and 6 as written
  from the workbook 3.30, 9.72 and 4.56 kg (0.32 to 0.34 kg fixed).
- **Page looked at:** type 1's element page 2: "Copper (Cu), inflow", its bars of copper, boards, cells and the grey
  "Copper fixed in alloys", the panel's list: Copper 1.6 kg, Boards and components 166 g, Aluminium alloys (fixed)
  158 g, Battery cells 147 g, Brass (fixed) 26 g, Steel (fixed) 7.5 g, NdFeB magnets (fixed) 1 g, Stainless steel
  (fixed) 190 mg. The list of eight lines pushes the bars low in the panel (readable; reported).
- **Not covered:** his run of 02; 03 with the new table (not run, as decided).
- **Date:** 2026-11-02.

### V153. E24 built: the light alloys' elements are the metal they hold

- **His words:** "I need both alloy mass and then also the Al mass. The first for the total weight and the last for
  the inflow needs", "Yes do it as writen in A" (2026-11-02).
- **Tests first:** `TestLightAlloysTheirMetal` failed before the code (the aluminium's and magnesium's share exactly 1);
  passes after it. The suite: 492 tests, all pass (`scratchpad/tests_E24.log`).
- **Audit** (`scratchpad/housing/elements_audit.py` on the sandbox, 4,000 draws a type): the Al, Mg and Ti counted from
  the alloys equal the metal their recipes hold, in all six types (Al 12.6 to 45.6 kg per robot from the aluminium
  alloys, where the whole alloys counted 13.6 to 49.5 before; Mg 0.15 to 3.28 kg; Ti 0.004 to 0.030 kg); the counted
  elements equal what 02 writes to 4 × 10⁻¹⁵. The materials (the alloys' whole mass) unchanged.
- **Not covered:** his run of 02 with this code; the pages looked at (no layout changed).
- **Date:** 2026-11-02.

### V152. 02 removes a numbered page it no longer draws

- **His words:** "02 removes them itself" (2026-11-02); then "I am runing 02": the change made and tested in the scratch
  copy `sb_e157` only (CLAUDE.md §4), put into the project after his run had written its last page (14:02:36; nothing
  written after it, checked at 14:07).
- **Tests first:** `TestPagesNoLongerDrawn` (a folder of a series' pages 1 to 4, another series, another prefix, an
  odd name: only pages 3 and 4 and the series not written removed, by name; 02's figures with a page 9 of an earlier
  run: removed, a gap in the numbers too). Both failed before the code; the first version of the code stopped at the
  first missing number, which the test caught.
- **Scratch run of 02** (2,000 draws): it said and removed exactly the 7 pages of E23
  (`1_compact_research_developer_materials_3.png`, `_4.png`, `_materials_3.png` of types 2 to 6); every type 2 material
  pages; "02 done". The suite in the scratch copy: 490 tests, all pass.
- **The suite in the project:** 490 tests, all pass (`scratchpad/tests_remove_project.log`).
- **Not covered:** his own next run with this code.
- **Date:** 2026-11-02.

### V151. E23 built: the material pages, overview_1's box, overview_2's open line

- **His words:** "Yes, build it" (2026-11-02), on the specification after "Sorry overview_1 is bad", the steels and the
  aluminium alloys ("the material is much too detailed").
- **Tests first:** `TestMaterialPages.test_the_material_pages_show_the_steels_and_the_aluminium_alloys_whole` (each of
  the four whole, the sum of its grades in every draw to 10⁻¹²; the magnets, cells and nickel as before; the pages of
  where each grade sits and the alloys table keep the grades), `TestOverviewBoxes` (every text in its box, both overview
  pages, all six types; the open line from the register). Each failed before the code: the box test on overview_1's
  "type 1: all its 30 robots with a mass; type …", the open line on "robot types 3 and 4 together".
- **The suite:** 488 tests, all pass (`scratchpad/tests_pages.log`); the on-disk comparisons pass since his builders'
  run of 13:15 to 13:16.
- **Pages looked at** (the sandbox, 2,000 draws): overview_1 (its box in three lines inside it), overview_2 (the open
  line as above), type 1's two material pages (Steel, Stainless steel, Electrical steel, Aluminium alloys each one
  panel; Copper, Brass, Nickel, Titanium alloy, the magnets with their heat classes, the cells, the boards, plastics).
  01 "No fault found"; 02 "they add up", "02 done".
- **Found:** 02 leaves a page it no longer draws in its folder (EVIDENCE.md E23, 7 pages after his next run).
- **Not covered:** his run of 01 and 02 with this code; the pages of types 2 to 6 looked at one by one.
- **Date:** 2026-11-02.

### V150. The cables' copper against one robot's own harness, the RoboParty RP1

- **His words:** "whats about the wires for the Cu?", "Contiune", "Yes, download it", "Yes, download them".
- **How:** RoboParty's harness list and its 43 drawings of the RP1 (EVIDENCE.md E22.1), every wire, strand and length
  transcribed (`scratchpad/rp1_text/rp1_copper.py`), the copper summed by gauge; against 02's cables for the RP1 (its
  row 'Cable length (four conductors)' 5 / 10 / 15 m; the shared cross-sections).
- **Result:** the RP1's harness holds 171 to 375 g of copper in about 12 m of cable; the model gives it 170 g at its
  modes (52 to 406 g). The low end equals the model's mode; the high end, 2.2 times it, is within the model's range.
  The span comes from one unknown: the size of the joint cables' wire CQ-RXG0250 (28 AWG, as RoboParty's other power
  conductors, or 0.25 mm², as its name's digits might say).
- **Not covered:** a second robot's harness (none other is published); the joint modules' inner wiring (in the joints'
  copper); the battery's own wires (in the battery housing).
- **Date:** 2026-11-02.

### V149. The elements of interest audited: each against all of it that 02 draws, material by material

- **His words:** "Are the elements now correct. Does Cu Element account for all the Cu, which can be recycled to Cu
  metal", then "I want this verified and documented. I need to have the accurate Cu element Nd etc." (2026-11-02).
- **How:** `scratchpad/housing/elements_audit.py` (results `scratchpad/housing/elements_audit.csv`), on 02's own draws
  in the sandbox `sb_e157` (the code of commit 8892b93 and after; his inputs but for one row read by nothing), 4,000
  draws of each of the six robot types part by part: for each of the 23 elements of interest, every kg of it that 02
  draws (`Robot.element`: by the recipes, the magnets' fractions, the car and data-centre files), by the material that
  holds it, against the kg it counts as the element of interest (`Robot.declare`), and that count against the elements
  table 02 writes (`compose_taken_apart`). The mean kg per robot.
- **The count is what 02 writes:** in all six types and all 23 elements, the largest difference 4 × 10⁻¹⁵ of the
  element (the rounding of the computer). In his run of 200,000 draws (V148) 02's own checks passed in every draw: the
  elements of interest add up to the materials they come from, copper, nickel and the light alloys each their metal
  whole, no other material giving more than it weighs.
- **Counted whole, all of it in the robot:** Li, Co, Nd, Pr, Dy, Tb, Nb, Ga, Pd, Ag, In, Ta, Au: what 02 draws of them
  is all counted (Nd: 0.27 to 0.51 kg per robot, from the magnets and 2.4 to 2.7 g from the boards; Dy 0.06 to
  0.12 kg; Co 0.09 to 0.20 kg). Sr: drawn in none of the six types (no recipe holds it).
- **Counted in part, the rest left in another material** (mean kg per robot, the range over the six types):

| Element | Counted from | Left in, not counted |
|---|---|---|
| Cu | Copper 1.58 to 3.08; the boards and components 0.17 to 0.32; the battery cells' foils and tabs 0.15 to 0.45 | the aluminium alloys 0.16 to 0.71; brass 0.024 to 0.026; the steels 0.008 to 0.015; the magnets 0.001 to 0.002; the magnesium alloys below 0.001. The Cu element is 91 % of all the copper in type 1, 80 to 84 % in types 2 to 6 |
| Ni | the battery cells 0.35 to 1.07; Nickel 0.026 to 0.087; the boards 0.001 to 0.002 | the aluminium alloys 0.006 to 0.023; the steels 0.002 to 0.004; stainless steel 0.0007 (type 1) |
| Al | the aluminium alloys **whole**, 13.6 to 49.5 (the aluminium they hold: 12.6 to 45.6); the battery cells' foils 0.06 to 0.18; the boards 0.008 to 0.016 | plastics 0.07 to 0.16; the magnesium alloys 0.015 to 0.33; electrical steel 0.006 to 0.011; the magnets 0.003 to 0.005; the boards' glass 0.02 to 0.05 |
| Mg | the magnesium alloys **whole**, 0.17 to 3.65 (types 3 to 5; the magnesium they hold 0.15 to 3.28) | the aluminium alloys 0.17 to 0.76; plastics 0.01 to 0.03; the boards 0.005 to 0.01 |
| Ti | the titanium alloy **whole**, 0.005 to 0.034 (types 1 to 3; the titanium it holds 0.004 to 0.030) | the aluminium alloys 0.009 to 0.035; the steels 0.003 to 0.006; plastics 0.002 to 0.005; the boards 0.001 to 0.002 |
| Mn | the battery cells 0.023 to 0.070 | the steels 0.06 to 0.13; the aluminium alloys 0.017 to 0.065; electrical steel 0.004 to 0.008; the magnesium alloys up to 0.012 |
| B | the magnets 0.011 to 0.022; the boards 0.0001 | the boards' glass 0.008 to 0.015; plastics 0.02 to 0.05 |
| Sn | the boards 0.004 to 0.007 | the aluminium alloys 0.003 to 0.011 |
| Pb | the boards 0.001 to 0.002 | the aluminium alloys 0.001 to 0.005 |

- **What it means:** an element of interest counts what is recovered as that element (E19 point 3). Copper, nickel and
  the light alloys count their whole mass: the Al element is the aluminium alloys' mass, 8 to 9 % more than the
  aluminium in them (their Si, Mg, Cu, Zn and the rest counted with it); the Mg element 11 % more than the magnesium of
  the magnesium alloys; the Ti element 11 to 12 % more than the titanium of Ti-6Al-4V. An element inside another
  material is not counted: it goes where that material goes when recycled (the copper of an aluminium alloy into
  remelted aluminium, of a steel into remelted steel; the boron and titanium of glass fibre stay bound).
- **The wires** (his question "whats about the wires for the Cu?"; `scratchpad/housing/copper_by_part.py`, the same
  draws, the copper by the part it sits in): all counted in the Cu element, as the material Copper: the cables'
  conductors 0.18 (type 1) to 0.26 kg per robot (length × cross-sections × 8.96 g/cm³, 02's cables step); the
  battery's wires and busbars 0.08 to 0.26 kg; the joints' windings and copper 1.3 to 2.5 kg; heat pipes up to 0.03 kg.
  Not counted: the connectors' contacts, brass (XT30, XT60), 0.023 to 0.026 kg. The cables rest on estimates: their
  length 8 m per metre of height (the G1's "全身线束不超过10m", T1; the Roboto Origin's BOM 10.0 m), their cross-sections
  estimated (no source states them: power 0.52 / 0.82 / 1.31 mm², the XT30's wire range, second-hand; signal 0.065 /
  0.13 / 0.2 mm², E). The one comparison so far (EVIDENCE.md, the G1 against the workbook): the model's whole harness
  0.27 / 0.45 / 0.66 kg against the workbook's 1.1 / 1.3 / 1.5 kg, a third (the workbook's row an estimate too).
- **Open, for his decision:** brass's copper (0.024 to 0.026 kg, about 1 % of the copper), recyclable to copper in a
  secondary copper smelter but usually remelted as brass; and whether the Al, Mg and Ti elements should be the light
  alloys' whole mass (as agreed in E19) or the metal they hold.
- **Not covered:** the input numbers themselves (the recipes' fractions, against independent sources in V14 and after;
  the parts' masses, in EVIDENCE.md per robot); the types drawn from the workbook (3, 5 and 6 for their written draws)
  beyond their totals: Cu by the recipes 3.3 to 9.7 kg, the Cu element 0.14 to 0.42 kg less.
- **Date:** 2026-11-02.

### V148. E20's leftovers removed; his runs of 12:45 to 12:50 read

- **His words:** "Yes, remove them" (2026-11-02), on the list with proof in EVIDENCE.md E20.3.
- **Removed, by name** (2026-11-02 12:46:59): the row 'Battery pack, Wh per kg (packs not weighed)' of
  `SHARED_CONSTANTS_LAST` (`tools/parts_taken_apart.py`); `PACK_BY_RATIO` and its comment (the same file);
  `PACK_WH_PER_KG` (`01_schemas.py`) and its name in `02_composition.py`; the two lines of
  `tests/test_make_parts_taken_apart.py` that checked the row. Afterwards no Python file of the project names any of
  them (grep over 00 to 03, `src/`, `tools/`, `tests/`). E20's check in 01 refuses the old rule coming back (a pack with
  no mass whose housing is the pack's remainder is a fault).
- **The suite:** 485 tests, 2 fail: types 1 and 2's builders against their files on disk, which still hold the row
  (`scratchpad/tests_E20_removed.log`).
- **Sandbox** (`sb_e157`, 2,000 draws): the six files rebuilt hold the share's row and not the old one; 01 "No fault
  found"; 02 "they add up", "02 done in 1 min 46 s".
- **His runs, read on disk (read only):** the six parts files at 12:45:07 to 12:45:53, a minute before the removal, so
  they hold the share's row and the old row (read by nothing); 01's pages at 12:46:11; 02 wrote `data/consolidated/`
  at 12:48:03 to 12:48:49 and `data/parts_taken_apart/` at 12:48:57 to 12:50:46, with `figures/composition/` and
  `figures/parts_taken_apart/`: **02 ran to the end**, 200,000 draws per type. In its draws nothing is below zero but Not
  allocated, except type 4's part group Frame in 2 draws (the 1X NEO's frame, reported under E21). No battery
  housing put a material below zero (E20).
- **Not covered:** his run's console, which only he saw; his notes page of type 4 not looked at by me.
- **Date:** 2026-11-02.

### V147. E21 A built: below zero where a remainder is, reported, not stopped

- **His words:** "A, as recommended" (2026-11-02), on EVIDENCE.md E21, after "Research the NEO first".
- **Tests first:** the five new tests (EVIDENCE.md E21.4) failed before the code (1 failure, 3 errors at the first
  run), and pass after it.
- **The suite:** 485 tests, 3 fail, the same three as in V146: they compare with the parts files on disk, written at
  11:48 before E20's A (`scratchpad/tests_E21.log`).
- **02 in the sandbox** (`sb_e157`, every builder of 2026-11-02 with E20 and E21, 2,000 draws, set in the sandbox's
  copy of `src/params_schema.py`): "they add up"; "02 done in 1 min 22 s"; pages and draws written into the sandbox.
  No quantity below zero at 2,000 draws, so no report there; per robot as before: the Matrix-1's frame below zero in
  7.7 % of its draws, the 1X NEO's in 16.7 %.
- **The case that stopped 02 at 200,000 draws** (V146: the part group Frame of type 4 below zero in 2 draws) can only
  be below zero where a frame is, which is a remainder; such draws are now reported. The path is covered by the tests
  (a part group below zero with and without a remainder below zero in its draw), not by a run at 200,000 draws.
- **Not covered:** 02 at 200,000 draws (his run); the real `data/` and `figures/`.
- **Date:** 2026-11-02.

### V146. E20 A built: a battery housing of a pack no source weighs a share of its cells

- **His words:** "A, as recommended" (2026-11-02), on EVIDENCE.md E20 (its open point too: the most 0.859).
- **Tests first:** the new and changed tests (EVIDENCE.md E20.3) failed before the code (4 failures, 7 errors), and pass
  after it.
- **The suite:** 481 tests, 3 fail, all comparing with the parts files on disk, written at 11:48 before A (types 1
  and 2's files against their builders; type 1's file against 01's check, 24 faults). One test still held E9.8's
  pack text for the CASBOT W1; it now checks its housing by share (`scratchpad/tests_E20b.log`).
- **02's own draws** (`scratchpad/housing/housing_in_02.py`, the sandbox `sb_e157` rebuilt with A, 20,000 draws per
  type, types 1 to 6): no battery housing below zero; every housing of a pack no source weighs between 0.2076 and
  0.8569 of its cells (the row's 0.207 and 0.859, with the cells' energy drawn); 02's `draw_faults` none in any type.
  01 in the sandbox: "No fault found". The new row's texts name no source code (checked against all 378 codes).
- **02 itself in the sandbox:** meant at 2,000 draws, it ran at 200,000, because my copy of the project's files into
  the sandbox replaced its parameters (`00_parameters.py`); in the scratch folder only, and it wrote nothing. It
  stopped: **"robot type 4: Frame is below zero in 2 draws"**, the part group Frame (the frame, the remainder, with the
  shell and screws). The cause, by `scratchpad/housing/frame_type4.py` (type 4, 20,000 draws): the 1X NEO, its frame
  below zero in 16 % of its draws, its frame, shell and screws together 0.45 kg at the least of its 180 draws, 6.9 kg
  at the median; every other robot of type 4 far from zero. So E20's "they do not stop 02" and V144's frames "without
  stopping the run" held at 2,000 draws only.
- **His runs on disk:** the register and the six parts files (2026-11-02 11:47 and 11:48), `params.xlsx` (11:48) and
  01's pages (11:49), not 02 (`data/consolidated/` of 2026-11-01 17:59). The parts files on disk hold the housings
  before A, so 01 now finds 24 faults in type 1's ("its battery pack has no mass, so its housing is a share of its
  cells"), until the six builders are run again.
- **Not covered:** 02 at 200,000 draws past type 4's frame; the real `data/` and `figures/`.
- **Date:** 2026-11-02.

### V145. Battery housings below zero: counted robot by robot, and in his run of 1 November

- **Why:** 02 stopped on type 4 in the sandbox (V144). The 5.6 % for the PrimeBOT T1 came from about 18 of its draws
  (2,000 draws over 124 robots), too few to say anything.
- **How:** `scratchpad/housing/housing_below_zero.py`, an independent count. For every robot of the six parts files in
  the sandbox `sb_e157` with a battery housing (319), it draws the pack, the cells and the management board as 02
  does (independent triangles; the energy from the voltage and capacity, else the template's energy per kg, on wheels
  where the robot has a wheel joint, as 01's `on_wheels`), 400,000 draws per robot, and counts the draws with the
  housing below zero.
- **Result:** 208 of the 304 robots whose pack is not weighed; none of the 10 weighed packs and none of the 5 drawn by
  the ratio. Most often: PrimeBOT T1 2.03 %, Booster K1 2 Ah 1.43 %, Syntheva Synthia 0.38 %, Unitree R1 0.12 %;
  every other robot below 0.06 %. By file: type 1 24 of 29 robots, type 2 58 of 102, type 3 53 of 97, type 4 70 of 85,
  type 5 none of 3, type 6 3 of 3.
- **Against his real run** (`data/parts_taken_apart/1_compact_research_developer/`, 1 November 18:00, read only): the
  housings below zero in type 1's 200,000 draws are the Booster K1 2 Ah's 44 (expected by the count: 47 in its 3,306
  draws), the Unitree R1's 13 (8 in 6,768), the Noetix Bumi's 4 (3), the Booster K1 5 Ah's 1 (2). The count matches
  his run in each robot, within its chance spread. That run did not stop, because the housing's nickel strip was
  entered as Copper then (the code at commit 3179242), and its type's copper stayed above zero.
- **What it means:** since E19 the strip is the material Nickel, so 02 at 200,000 draws stops on type 1 (about 60
  draws), whether or not batch 3 is in. V142's and V143's sandbox at 2,000 draws could not show it (0.6 such draws
  expected in type 1). Lesson: a remainder's share below zero is counted over many draws per robot, not over a type's
  sandbox draws.
- **Not covered:** the frames below zero (they do not stop 02); the weighed packs at 200,000 draws of 02 itself.
- **Date:** 2026-11-02.

### V144. Batch 3 of types 3 and 4 built (E15.7, E15.8)

- **His words:** "Move on" (2026-11-02, after E19), on E15.7 as agreed ("E15's entry"), its open points A to E as
  recommended.
- **Tests first:** `TestTypesThreeAndFourBatchThree` (each block's mass, form, hands, battery, boards and wheels
  against E15.3; the 17 joints from a stated joint against E15.3's masses, within 5 %; the GR-3's 26.9 and the Star1's
  32.9 kg from their models; the Tau's rows the G1's) and the register's (54 and 58 robots taken apart; the seven
  without a mass) were written first and failed (nine) before the blocks. Also: no row of the sheet Sources from a
  robot's name (it failed: "Moon Dynamics L1" and "ROBO-T1" gave the rows L1 and T1).
- **The suite:** 477 tests, 5 fail, all comparing with the files on disk that his runs rewrite (the register's
  "for stock-and-flow" words, the old name "Electronics" in the parts files of types 1 and 2, the real grades, the
  real parts file); the test of the real register, extended to types 5 and 6's files (open point E), passes
  (`scratchpad/tests_E15_7c.log`).
- **Sandbox** (`scratchpad/sb_e157`, a copy of the project with batch 3 built, every path inside it): the register and
  the six builders run; 01 "No fault found"; 02 at 2,000 draws **stopped: "robot type 4: Nickel is below zero in 1
  draw"**. Type 4 is now drawn from its robots (open point B), and 02 stops on a material below zero other than Not
  allocated. The cause, robot by robot over the draws (`scratchpad/draw_all_2.py`, which draws as 02 does without its
  stop): the PrimeBOT T1's battery housing, its pack less its cells and management board (an 8.5 kg robot on the
  template's battery), below zero in 5.56 % of its draws. Below zero in some draws without stopping the run (no material
  of the type falls below zero with them): the 1X NEO's frame in 22.22 % (batch 1), the Matrix-1's in 7.69 %.
- **At the modes** (E15.7 point 8): no remainder below zero; frames below a quarter of the robot: Figure 02 18.2 %,
  Matrix-1 15.5 %, Walker S2 18.5 %, Star1 21.8 %, KAI 24.2 %, Tora DoubleOne P 22.0 %, Spaceo Pro 24.4 % (seven; E15.2
  counted nine on its own numbers).
- **Types 1, 2, 5 and 6 unchanged** (by program, the same seed, against `draws_e19_removed.npz`): every material and
  element within 6 × 10⁻¹⁴ kg; every type's workbook draws identical.
- **Summaries of types 3 and 4:** no median of 0 and no 2.5 % bound below zero; type 4's Nickel below zero in 0.05 %
  of its draws (the one draw above).
- **E13's shares** as built: type 3 the joint template 137 of 172, the battery template 124; type 4 103 and 98 of 137.
  E15.5 expected 139 and 99: its count missed two of type 3's robots off the template, and the Tau's battery is the
  G1's (E15.8 point 6). Pinned in test_schemas.
- **Pages looked at:** 02's pages of types 3 and 4 (15 each, `scratchpad/pages_34/`): the notes page that ran off the
  page (robots resting on estimates, one paragraph longer than a page) now goes on over the next page; 01's table had
  "Humanoid HMND 01 Alpha Bipedal" over the height column, shortened to "Humanoid HMND 01 Bipedal".
- **Not covered:** 200,000 draws; the real `data/` and `figures/` (his runs, HANDOVER); 02 past type 4's stop; each
  block's numbers against their sources again beyond the tests (they were typed from the record read first-hand).
- **Date:** 2026-11-02.

### V143. E19's leftovers removed; the documents

- **His words:** "Yes, remove them" (2026-11-02), on the list with proof that nothing else reads them.
- **Removed, by name:** E17's split: `SIDES`, `side_columns()`, the table `'metal'` and its two checks in `draw_faults`,
  `Robot.metal`, `Robot.as_metal()`, `Draws.metal`, `Shared.recipe_metal`, `Shared.grade_metal()`,
  `Shared.graded_metal`, and with them `RecipeDraws.metal()` and `element_label`'s "as metal" form, read by nothing
  once the rest was gone; its tests `TestAsMetal` (test_composition, 3 tests; test_parts_taken_apart, 1). The setting
  `composition.elements_not_shown`, its check in `src/params_schema.py` and in 02, `shown_elements()`,
  `not_shown_note()`, 03's use of them; its tests (test_composition 2, test_parts_taken_apart `TestElementsNotShown`,
  test_comparison 1; three cases and the key in test_parameters). 02's `MATERIAL_TITLES`, 01's `MAY_HAVE_GRADE`.
  `page_elements`, `page_notes` and 03's `view_columns` and `view_notes` lost the setting they no longer read. Kept:
  the column "As metal" and `RecipeDraws.drawn()`, which give the battery cells' foils and tabs.
- **Proof that no draw moved:** the scratch copy drew every robot type part by part and from the workbook, 2,000
  draws, the same seed (`scratchpad/draw_all_2.py`), against the draws before the removal: the materials and the kg
  each material gives equal draw by draw (0.0 kg), the elements within 6 × 10⁻¹⁴ kg (the order of a sum). The removed
  calls only read shares already drawn and kept.
- **The suite:** 477 tests (8 removed); 15 fail, all known: batch 3's nine (not built) and six that compare the builders
  with the files on disk (old material names until Matthias reruns them, HANDOVER 2026-11-02).
- **Documents:** README (02's and 03's rows), METHODOLOGY (the materials, the elements of interest, the checks, what
  02 writes, the pages, 03), EVIDENCE E19 (agreed and built) and E17 (replaced), SHARED_LISTS (the new names), HANDOVER
  (what changed, his runs by full path, what is open).
- **Found, not acted on:** 02's `triangles()` and 01's `element_shares()` are called only by tests (so before E19).
- **Date:** 2026-11-02.

### V142. E19 step 4 built: the element pages by material, the material pages, the alloys table

- **His words:** "Yes, build them" (2026-11-02, on the preview of type 5, V141).
- **What changed:** 02 only, and 03's notes. The element pages of a robot type taken apart six a page, each element
  split by the material it comes from (`by_material_panel`, its kg per material kept as `Draws.by_material`), the
  materials' means in the panel, one legend of the page's materials (Paul Tol's muted scheme, `MATERIAL_COLOURS`); the
  material pages each material of the one list, then its grades (`material_panels`, `grade_words`); the alloys table
  (`alloy_rows`, `alloys_pages`; what each holds, `holds_words`, from the recipes, the sibling's steels and the
  magnets' drawn fractions); the notes pages rewritten. The panel code shared, not copied: `stacked_bars` (the
  approved stacked form, also the parts figures'), `centre_lines`, `numbers_above`, `panel_axes`. The magnesium alloys
  now by their alloys as the aluminium (`ALLOYS`): type 4's recipe is AM50A or AM60B, and AZ91D. Corrected on the way
  (each test first): the sentence "the materials that have a recipe so far" on the workbook page and in 03; "Battery
  materials" in 03's notes (missed by step 1); the material Other grey again in 03 (step 1 had renamed Mixed); the
  "where it comes from" figures of the stainless and electrical steels again (step 1 had made them materials of their
  own, and the figures named only Steel); "its NdFeB magnets sit".
- **Tests (each written first and seen to fail):** each element by material adds up to it by kind of part in every
  draw (1e-12); six panels a page, the legend in the colours' order, copper's three materials written in its panel;
  the material pages in the one list's order, each material then its grades; the alloys table: 20CrMnTi "Cr 1–1.3, Mn
  0.8–1.1 … ; Fe the rest", 7075, brass "Cu 58–65; Zn the rest", the nickel strip "Ni 100", the magnet classes, its kg
  the median of the draws that hold it; type 4's AM50A, AM60B and AZ91D each a row (each in about 2 % of the draws,
  no panel), AZ91D's nickel (0.002 %) left out; the notes; the sources figures of every steel; the readability test
  now also over type 5 (its title had run off its notes page: "how to read its pages" now).
- **Looked at:** 02's own pages of types 4 and 5, drawn in the scratch copy (`scratchpad/draw_pages_E19.py`, 2,000
  draws): the element pages, the material pages, the alloys table, the notes, a sources figure.
- **The suite:** 485 tests; the same 19 fail as in V141 (batch 3, the files on disk before his reruns, the four
  leftovers).
- **Date:** 2026-11-02.

### V141. E19 step 3 and the preview of step 4 (type 5)

- **His words:** "Yes, agree E19" (point 6: one parts vocabulary, "Boards and heat sinks" → "Boards and computers", the
  battery "Battery pack" the part and "Battery cells" the material; point 7: a scratch preview of type 5 first; point 4:
  the alloys table on the material pages).
- **Step 3:** the kind of part renamed in 01's `KINDS`, the one place it is named (every reader grepped: 01, 02, 03,
  `src/`, `tools/`, `tests/`; the other "heat sink" hits are parts' names, not the kind). The test of the kinds' names
  was changed first and seen to fail, then passed after the rename. The battery's two names were already so since step
  1.
- **The preview** (`scratchpad/preview_E19/preview.py`, in Claude's scratch folder; nothing in the project): type 5
  part by part, 2,000 draws, from the scratch copy of V140. Element pages: each element stacked by the material it
  comes from, its kg per material from 02's own `Robot.declare`, noted by a wrapper; material pages: each material, then
  its grades; the alloys table from the recipes, the sibling's steels and the magnets' drawn fractions. Each page looked
  at: 16 × 9 inches at 150 dpi, fit to a 1920 × 1080 screen 0.8 of its size, so the 14-point text is about 23 pixels;
  fixed before showing: the materials' means over the bars at nine panels a page (six now), the table's heading off the
  page, titles broken at "die-cast", near-zero shares printed as 6.1e-05, a row cut at the page's foot.
- **The suite in the project after steps 2 and 3:** 480 tests, 19 fail: batch 3's nine (not built), six that read the
  parts files and the register on disk (old names, e.g. "the material 'Electronics' is not in the shared lists", until
  Matthias reruns the six builders and the register), and V140's four leftovers.
- **Date:** 2026-11-02.

### V140. E19 step 2: only the elements of interest, from what is recovered as elements

- **His words:** "Yes, agree E19" (EVIDENCE.md E19 point 3 and questions 2 to 4: the elements of interest only;
  copper, nickel and the aluminium, magnesium and titanium alloys their element whole; the magnets Nd, Pr, Dy, Tb, Co,
  B, Nb, Ga; the battery cells Li, Ni, Co, Mn and their foils' Cu and Al; the boards and sensors their metals of
  interest; steel, stainless steel, electrical steel, brass, plastics, composites and ceramics stay materials).
- **What changed:** 02 only (both paths: from the workbook and part by part), its tests. `INTEREST`, `WHOLE`,
  `MAGNET_ELEMENTS`, `CELL_ELEMENTS`, `CELL_METALS` and `declared()` say which material gives which element; the
  elements written are those (`elements.npy`, the summaries); every element of the recipes is still drawn and checked
  to add up, as `recipe_elements`, but not written. New checks in every draw: the elements of interest add up to the
  materials they come from; copper, nickel and the light alloys each its element whole; no other material gives more
  than it weighs. Each check was seen to catch a draw broken on purpose (`TestSums`).
- **How it was checked:** the copy of the project in Claude's scratch folder of V139 (its parts files and register
  built anew), with step 2's 02 copied in, drew every robot type part by part and from the workbook at 2,000 draws,
  the same seed (`scratchpad/draw_all_2.py`), against step 1's draws (`scratchpad/compare_E19_2.py`).
- **Result:**
  - the materials equal step 1's draw by draw (largest difference 0.0 kg); the elements of the recipes equal step 1's
    elements draw by draw (2.8 × 10⁻¹⁴ kg): nothing drawn moved;
  - in all twelve (six types part by part, six from the workbook) only elements of interest are written; copper,
    nickel and the light alloys equal their element in every draw; no other material gives more than it weighs; no
    fault of the new checks;
  - at the mean, the element Cu is now below the copper of the recipes in every type (type 2 part by part 3.00 of
    3.75 kg, type 5 3.84 of 4.56 kg): the brass's copper and the alloys' copper stay in them (V137 answered); the
    element Al is above the aluminium of the recipes (type 2 46.8 against 42.5 kg), as an alloy counts whole as its
    base metal (question 2); Co, Li, Nd, Dy, Ag, Au and Ta are unchanged; Mn and Ni lose the steels' share (type 2 Mn
    0.06 of 0.23 kg);
  - left out as not of interest, per robot at the mean: type 2 part by part 34.9 of 84.1 kg of elements (Fe 16.7, C
    10.4, O 3.0, Zn 1.5, Si 1.5 kg …); the sensors' tungsten 1 to 3 mg; no platinum or germanium in any robot drawn;
  - from the workbook, the titanium alloy is now its titanium without a recipe: types 2, 5 and 6 Ti 3.2, 11.7 and
    6.0 kg (before, none: no recipe).
- **The suite in the project:** passes but for the known ones (batch 3 not built; the parts files and the register on
  disk awaiting Matthias's reruns) and four tests of what E19 replaces, listed for removal on his word: E17's two
  columns per element (`TestAsMetal.test_written_in_two_columns_and_two_rows_each`), and the hydrogen, nitrogen, oxygen
  and fluorine "kept in the draws" (`TestRun`, `TestElementsNotShown`, `test_comparison`): not elements of interest,
  they are no longer drawn as elements.
- **Found, not acted on:** type 4 part by part, its part group Frame below zero in 1 of the 2,000 draws (a robot's
  frame, the remainder of its mass). Type 4 is still drawn from the workbook (batch 3 not built), so no run stops on
  it; once it is drawn part by part, 02's check "nothing below zero" would stop the run.
- **Not covered:** the pages (step 4 of E19); the alloys table (point 4, next).
- **Date:** 2026-11-02.

### V139. E19 step 1: the one list of materials changes names only

- **His words:** "Yes, agree E19" (EVIDENCE.md E19 point 2 and question 1: one fixed list of materials, each name what
  it is).
- **What changed:** the shared lists (sheet Lists: Copper, Brass, Nickel, Aluminium alloys, Magnesium alloys, Titanium
  alloy, Steel, Stainless steel, Electrical steel, NdFeB magnets, Battery cells, Boards and components, Plastics, Fibre
  composites, Ceramics, Other, Not allocated; the sheets Materials, Splits and Battery cells after them), the element
  recipes' sheet Rows, both copied first to Claude's scratch folder; 01, 02, 03, the six builders and the shared parts
  module (a stainless steel, an electrical steel, brass and the nickel strip each under its own material, by its
  grade: `steel_of()` for the screws); the tests' fixtures and expectations.
- **How it was checked:** two copies of the project in Claude's scratch folder: the code of the last commit (fa75985)
  with the data as they were before E17 (the recipes and shared lists from the backups, the parts files on disk), and
  the code now with its six parts files and the register built anew. Each drew every robot type, part by part where
  it is taken apart and from the workbook, at 2,000 draws, the same seed (`scratchpad/draw_all.py`,
  `scratchpad/compare_E19_1.py`).
- **Result:** every new material equals, draw by draw, the old one or ones it came from (Steel = Steel + Stainless
  steel + Electrical steel; Copper = Copper + Brass + Nickel; each renamed one itself), in all six types part by part
  and from the workbook: the largest difference 3 × 10⁻¹⁴ kg. Every element equal but the workbook's Cu, which since
  E17 holds the workbook's copper: types 1 to 6 by 3.8, 5.2, 2.4, 4.8, 8.5 and 3.5 kg on average (type 5: Cu 1.21 kg
  before, 9.72 after; its copper 8.50 kg, V137).
- **The suite in the new copy:** passes but for batch 3's tests (its blocks not built, E15.7) and the stale register test
  (types 5 and 6, E15.7 open point E). In the project itself the tests that read the parts files and the register on
  disk fail until Matthias reruns the six builders and the register.
- **Not covered:** the pages (step 4 of E19, after his preview).
- **Date:** 2026-11-02.

### V138. Each element by the material and grade that hold it (for E18)

- **His words:** "What is permanent magnets and the Magnets of the different grades. The grade are all NdBFe or not?",
  "We need a much better declaration of the materials and elements. Check with the datacenters, how it was done there. I
  assume Vanadium and Cr are part of steel", "So if elements are in alloys, then one has to know it".
- **How:** a scratch script (`scratchpad/copper/elements_by_holder.py`, not in the project) ran 02's part-by-part
  drawing for types 1 to 6 at 2,000 draws on the inputs on disk, writing nothing, with 02's `Robot.material` and
  `Robot.element` wrapped to note the material and grade that hold each kilogram of each element; the metal from
  E17's code. Its output: `scratchpad/copper/elements_by_holder.txt`.
- **Result (means per robot, the holders above 0.5 %):**
  - **V:** type 2 1.3 g, type 3 0.4 g, all in the titanium alloy Ti-6Al-4V; none in a steel (no steel grade of the
    recipes or of the sibling's sheets holds vanadium).
  - **Cr:** type 3 324 g: the gear and alloy steels 52 % (20CrMnTi 18, 42CrMo4 18, the gear stage 2 mixture 14, GCr15
    3 %), the battery cells 22 % (their stainless steel 304 can), the aluminium alloys 26 % (6061 and 7075, 0.2 % Cr);
    type 5 346 g, 55 / 23 / 22 %.
  - **Co:** the magnets 59 to 63 %, the battery cells' cathode 37 to 41 %. **Nd, Dy, Tb:** the magnets, over 99 %.
  - **Cu:** as metal 74 to 77 % (types 2 and 5: 2.77 of 3.75 kg, 3.52 of 4.56 kg), the rest in the aluminium alloys,
    the boards and sensors, and brass. **Ni:** the cells 90 %, as metal 8 % (the nickel strips and the cells' tabs).
  - **Fe:** the steels about 90 %, the magnets 5 %, the cells' can 4 %.
- **The magnets:** every grade class is sintered NdFeB. 02 draws each joint group's class by heat (sheet MagnetGrades),
  and its element fractions are RAWCLICVehicleTractionMotor's `magnet_element_draws`, read where it lies (Nd, Pr, Dy,
  Tb, B, Co, Al, Cu, Nb, Ga, iron the balance). The classes N, M, H, SH, UH, EH and AH are rated to 80, 100, 120, 150,
  180, 200 and 230 °C (that project's `magnet_grade_temperature`, which says no source of its own states them). The
  material page's "Permanent magnets" is all of them together; each "Magnets, grade class …" panel is the same
  kilograms of one class.
- **RAWCLICDataCenters, read for comparison** (its `05_data_center_elements.py` and EVIDENCE.md § 19): the elements of
  interest only, each element's distribution split by where it comes from (stacked bars adding up to the total, the
  mean of each part written in the panel), and stainless steel left as steel ("Stainless steel stays as sainless steel
  not down to the elements. Exclude it"): no Fe, O or Cr there.
- **Not covered:** the cells' elements by their parts (can, cathode, anode, foils) are one holder here, "Battery
  materials"; the Cr of the cells is their can's by the recipe (only the 304 can holds chromium).
- **Date:** 2026-11-02.

### V137. Copper: the element Cu above the material Copper, in every robot type

- **His words:** "I see for 5 and 6 a considerable different between copper material and copper element. There is more
  copper lements. This can not be, what is the reason", then "It is for all types of robots. This can not be".
- **What was looked at:** his 02 run of 2026-11-01 17:59 (`figures/composition/5_..._materials_1.png`: Copper, median
  2.9 kg; `..._elements_2.png`: Cu, median 4.5 kg), and every type's `data/consolidated/<type>/summary.csv`.
- **How:** a scratch script (`scratchpad/copper/cu_by_material.py`, not in the project) ran 02's own part-by-part
  drawing (`draw_taken_apart`, `compose_taken_apart`) for types 1 to 6 at 2,000 draws on the inputs on disk, writing
  nothing, with 02's `Robot.element` wrapped to add up each kilogram of Cu by the material that holds it.
- **Result (means per robot):**

  | Type | Material Copper | Element Cu | Cu in Copper | in Aluminium | in Battery materials | in Electronics | in Steel |
  |---|---|---|---|---|---|---|---|
  | 1 | 1.640 | 2.079 | 1.599 (76.9 %) | 0.158 (7.6 %) | 0.147 (7.1 %) | 0.166 (8.0 %) | 0.008 |
  | 2 | 2.485 | 3.750 | 2.396 (63.9 %) | 0.713 (19.0 %) | 0.396 (10.6 %) | 0.234 (6.2 %) | 0.011 |
  | 3 | 2.752 | 3.979 | 2.660 (66.9 %) | 0.632 (15.9 %) | 0.407 (10.2 %) | 0.265 (6.7 %) | 0.013 |
  | 4 | 2.239 | 3.180 | 2.165 (68.1 %) | 0.477 (15.0 %) | 0.308 (9.7 %) | 0.217 (6.8 %) | 0.010 |
  | 5 | 3.193 | 4.564 | 3.092 (67.8 %) | 0.680 (14.9 %) | 0.453 (9.9 %) | 0.321 (7.0 %) | 0.015 |
  | 6 | 2.928 | 4.111 | 2.857 (69.5 %) | 0.631 (15.3 %) | 0.306 (7.5 %) | 0.300 (7.3 %) | 0.015 |

  The element counts copper wherever it sits; the material Copper only the parts made of copper (windings, cables,
  brass, the battery's nickel strips). The rest of the Cu is in the aluminium alloys (the element recipes in
  `data/researched/element_recipes.xlsx`: 7075 1.2 / 1.6 / 2.0 % Cu, A380 3.0 / 3.59 / 4.0 %, ADC12 1.5 / 2.09 / 3.5 %,
  6061 0.15 / 0.28 / 0.4 %; each type's mix of die-cast and wrought), in the battery cells (the NMC recipe's copper),
  in the boards (copper their mass times the copper share) and in the steels. Each Cu is drawn once, from the one
  material that holds it: no double count. The Cu in Copper is 96 to 98 % of the material Copper, the rest brass's zinc
  and the nickel strips.
- **Second finding:** the summaries of the draws of types 3 to 6, drawn from the workbook, give Copper "In the
  elements: No" (type 5: Copper 8.50 kg, Cu 1.21 kg; type 3: 2.37 and 0.93; type 4: 4.77 and 0.64; type 6: 3.50 and
  1.07). There, the element recipes hold no row for the workbook's Copper (the sheet of rows names only "Aluminum
  alloys" for types 1 to 6), so its kilograms are drawn but not turned into Cu (02's "Materials without a recipe yet").
  Types 1 and 2, drawn from their parts, give "Yes". Reported to him, not changed.
  The columns add up to the element (type 5: 3.092 + 0.680 + 0.453 + 0.321 + 0.015 + 0.003 in magnets and magnesium =
  4.564 kg); the sensors' Cu (their car elements) is in Electronics.
- **Not covered:** whether the alloys' mix of each type is right (his recipes, not checked here).
- **Date:** 2026-11-02.

## 2026-11-01

### V136. Types 5 and 6 entered (E16.6)

- **His words:** "Yes, agree both" (E15 and E16), then "move move. Find all the data for 5 and 6 and then fill in the
  data in the respective sheets. So I can then have all dat for the run of 01 and 02. Move Move".
- **His run read back first:**
  - The four builders 15:57 to 15:58, 01 15:58, 02 16:10 to 16:12, all after E14's commit (14:28).
  - Every summary has no median of 0 and no 2.5 % below zero.
  - The suite showed 2 failures: type 1's table tests, written before E14 and not updated with it. Both are now
    corrected to E14's state (the Booster T2, the Bumi and the E1 from torques; the E1's mass its maker's).
- **Tests first** (each failed before its code):
  - `TestTypesFiveAndSix`: 10 tests on the files, the T800's motors and battery, the DR02's model joints, the Alex's
    arms, the MH3 and Fuxi, the Atlas's hands and Thor, E15's three robots, the template names, a robot without a
    battery in 01's table, and the makers' masses.
  - The register's sheets Type 5 and Type 6.
  - The recipe families.
  - The counts of type 3: 94 robots, 99 with versions; its templates 75 and 70 of 99.
- **Sandbox** in Claude's scratch folder (`sandbox_e16/`): the register, the six builders, 01 and 02 at 2,000 draws,
  every output patched to scratch.
  - First run: 01 stopped in type 5's table on a template name of type 2's. Fixed by `TEMPLATE_OF_TYPE` 5 and 6 and
    its test.
  - Second run: 02 found no recipes of types 5 and 6. Fixed by `RECIPE_FAMILY` with type 5's magnesium type 3's,
    and its test.
  - Third and fourth runs: 01 "No fault found", 02 done. Type 5 drawn over 9 robots, type 6 over 4. Their summaries
    hold no median of 0 and no 2.5 % below zero.
  - The pages looked at: the robot tables of types 5 and 6. After the fourth run they show the Phantom MK1 "no battery"
    with an empty battery cell (the third gave it a template's 1,174 Wh: fixed in 01, `has_battery`), and the Alex's mass
    from the maker (its sources' kind fixed to "Manufacturer's").
- **Against his files** (`compare.py`): types 1, 2 and 4's parts files row for row the same as his of 15:57. Type 3's
  changes only the six robots of the entry: the Atlas, the DR02 (27.4 kg of joints, 40 %), the DR02 Pro (35.5 kg,
  45 %), the Kaleido 9, the Moby and the Phantom MK1 (22.2 kg, 28 %).
- **The whole suite:** 455 tests. On the last code only the register-equals-the-file-on-disk test fails, until his run
  of the register.
- **Not covered:**
  - His runs at 200,000 draws.
  - Type 1's F, Na, Ca and Br in the head have a 2.5 % bound of about −2e-07 kg at 2,000 draws. They had it before
    this entry too (E14's sandbox); his 200,000-draw summary has none.
  - The hydraulic robots and E15's other 112 robots, not entered.

### V135. Types 5 and 6's research read again first-hand (E16)

- **His words:** "do now all the rest for type 5 and 6 research all data use the internet as much as possible and read
  also .pdf".
- **What:** every figure E16 uses for the 16 robots of types 5 and 6, against its source; three reading agents found
  them, the maker first.
- **How:**
  - Eight PDFs downloaded (`downloads_e16/`) and read by PDFKit: IHMC's arXiv 2411.03532 (Nadia's hardware), 2409.04639
    (Nadia's arm actuators, Fig. 4) and 2609.01518 (Alex); Barasuol et al. 2018 (the ISA, Table 2); Cyborg's product
    manual 2026, its brochure and its two brand manuals.
  - Moog's two ISA datasheet addresses return Moog's 404 page.
  - Four model files added up by script (`urdf_e15_sum.py`):
    - DR02-std.urdf: 67.575 kg, 21 joints.
    - DR02-pro.urdf: 78.085 kg, 31 joints.
    - serial_t800.urdf: 84.988 kg, 25 joints.
    - serial_t800pro.urdf: 85.227 kg, 43 joints.
    - Their effort limits listed.
  - EngineAI's six T800 developer documents (battery, specification, motors, computers, sensors, hand) and the other
    makers' pages, blogs and releases (IHMC, PSYONIC, SAKE, Boston Dynamics, Noble Machines, Kawasaki, Mirsee, RoboForce,
    NeodraDynamics), each fetched into the scratch folder and read as text. The outlets: IEEE Spectrum, the IEEE Robots
    Guide, Fluid Power World, Global Times via 163.com, Interesting Engineering, aiwiki, The Business Standard, Pulse
    2.0, Mynavi, PC Watch, The Financial News and Battery-Tech Network.
  - The quotes are in `documentation/claude/research_2026-11-01/firsthand_types56.md` (saved from the scratch folder).
- **Result:** the agents' figures agree with their sources. Corrections, each now in E15 or E16:
  - Moby's mass is its maker's 72 kg, not the catalogue's 45; E15's row is changed.
  - The Phantom MK1 has no battery; E15's row is changed.
  - The CYBORG RO1's torque is 400 N·m in its 2026 manual (">400" on its site), and its computing is "8 核 200TOPS".
  - The T800's battery is NMC (its developer documents), not the product page's "solid-state".
  - Kaleido's magnesium skeleton is its maker's, not only the catalogue's.
- **Not covered:**
  - The figures are research. Nothing is entered or run on his data.
  - The Moog ISA's own datasheet (404); Nadia's ISAs are sized from the IIT paper's two versions.
  - The hydraulic robots' power units: no source states their masses.
  - The Cyborg WO1's battery capacity.
  - The electric Atlas's joint torques and battery capacity, which no source gives.
  - Downloads not read: the MIT DRC Atlas paper (Kuindersma 2014, too large for the reading agent), the H1 user manual
    (H1 entered by its model), DEEP Robotics' offline document ZIP.
  - The modes are Claude's arithmetic.

### V134. Batch 3's research read again first-hand (E15)

- **His words:** "move forward to get all the data. Search in the internet. Use all information avaibalbe read .pdf",
  "download what ever is possibel", "continue research", "I want 1 to 4 finally done".
- **What:** every maker figure the five reading agents relied on for batch 3's 123 robots (and the seven new robots of
  types 5 and 6), against the source itself.
- **How:**
  - 68 makers' pages and releases fetched into Claude's scratch folder (`pages_e15/`) and read as text by a parser
    (`tools_e15/htmltext.py`), or in the browser pane where a site needs its scripts (Galbot, Noetix, UBTECH, Persona,
    MenteeBot, KinetixAI, Pink, PsiBot).
  - Figures held in images: UBTECH's Walker C1, S1 and S2, PaXini's Tora DoubleOne, Digit's XiaQi, ROBOTERA's Q5
    brochure, each read by Vision OCR (`tools_e12/ocr.swift`).
  - Five PDFs downloaded (`downloads_e15/`) and read by PDFKit: RNoid's spec sheet (rev. 003), ROBOTERA's Q5 brochure,
    and Oversonic's RoBee R, M and F brochures.
  - Nine model files added up by script (`urdf_e15_sum.py`: the link masses, the joints, their effort limits):
    - GENE.01: 79.668 kg; 73 joints, every effort 1e+09.
    - GR-3: 69.692 kg; 31 joints, the efforts its page's table.
    - NIX ×4: 23.320, 23.136, 23.136 and 24.642 kg.
    - Star1: 64.001 kg; 55 joints.
    - T800: 84.988 and 85.227 kg.
  - The form of five robots from their makers' photos: P0, Persona's robot, MenteeBot V3 and XiaQi on legs, Psi V1 on
    wheels.
- **Result:** the agents' figures agree with their sources, with these exceptions:
  - The W1 Pro's LiFePO4 option is the W1 Core's.
  - MenteeBot's page is the V3's (its image's name).
  - The Walker C1 carries a Jetson Thor, which the agent missed.
  - Matrix-1's "Actuator: 55" and O-ID's "Specs indicative" are not in the pages' text.
  - The UBTECH Walker C1's address "WalkerC1" gives "can't be found"; its page is `walker-c1`.
  - Each figure is recorded with its quote in `documentation/claude/research_2026-11-01/firsthand_batch3.md` (saved from the scratch folder).
- **Not covered:**
  - The internet's figures (news, databases) are as the agents read them. I reread only humanoid.guide's GoMate (45 kg)
    and the pages of the robots of no stated form.
  - Hobbs W1's mass and battery are aiwiki's citing Noetix: Noetix's specification table is not shown in the browser
    pane, even at 1440 px.
  - JS-only maker sites not read: jaka.com, lejurobot.com, keenon.com, gigaai.cc, zeroth0.com, galaxea-dynamics.com,
    sharpa.com, switch-bot.com, kawasakirobotics.com.
  - The modes in E15 are Claude's arithmetic (`batch3_plan.py`, in `documentation/claude/research_2026-11-01/arithmetic.md`), not a run.
  - Nothing was entered or run on his data.

### V133. The Booster T2 by type 2's fit

- **His words:** "Yes, agree" (E14 as built, the Booster T2's joints by type 2's fit).
- **Test first:** `TestE14Entry.test_every_joint_from_its_makers_file` changed to the fit for the T2, run, failed; then
  the builder changed (`T2.from_torque`, the one copy of the refit): all 6 of `TestE14Entry` pass.
- **Its frame** (`sandbox_e14/t2_frame.py`, Claude's scratch folder: type 1 alone at 20,000 draws, from its builder's
  file as written now, his files only read): 676 of the T2's draws. Its joints come to 24.9 kg at the mean, 59 % of its
  42.3 kg. Its frame is 8.31 kg at the mean, 4.70 to 11.68 kg over 95 % of its draws, never below zero (4.1 % before,
  V132).
- **The whole suite:** 443 tests, the same 2 failing as in V132 (the comparisons of types 1's and 2's builders with his
  files on disk).
- **Not covered:** his runs at 200,000 draws.

### V132. E14's entry built (E14.6, E14.7)

- **His words:** "Yes, build it" (E14.6 with E14.5's points A to C).
- **Tests first** (`TestE14Entry`, 6 tests): written before the code, all 6 failed. After the code they pass:
  - every robot's body joints as its maker's file (names, counts, torques; 18 robots and versions), off the template,
    each module by its type's rule;
  - the Dual-Arm Lift's arms by RealMan's modules;
  - the G2's and the RealBots' arms beside their other joints on the template;
  - the Bumi's and the E1's joints from their stated joint by type 1's rule, and the Bumi's 48 V × 5.1 Ah;
  - the A2's 28 joints from its knee's 270 N·m;
  - THEMIS's mass (35.5, 36.5, 37.92 kg), its 518.4 Wh, its Ryzen board and its two Orin NX.
- **Older tests changed** with the reason beside each, nine in all:
  - the counts of template robots (type 1's file 16 → 13, twice; E13's shares, type 2's card: 67 and 63; types 3 and 4:
    75 / 68 and 32 / 30);
  - type 2's lists of template robots (without the H2-X, Oli, Tien Kung 3.0 and those on wheels now their makers');
  - THEMIS's mass, battery and sensors;
  - one test at the modes that took the Noetix E1 as its template robot of 40 kg, now the Nori L3 (the same 40 kg,
    the same numbers).
- **The whole suite:** 443 tests, 2 failing: the comparisons of types 1's and 2's builders with his files on disk, which
  pass after his builder runs.
- **Sandbox** (`sandbox_e14/run.py`, Claude's scratch folder, 2,000 draws, his files only read), the code of 33e192f (a
  scratch worktree, removed after) against the working tree:
  - The register, the four builders, 01 and 02 ran to the end (01 no fault; 02 0).
  - **Robots changed** (`compare.py`, every sheet, row by row): type 1's file 3 of 32 (the Booster T2, Bumi, E1); type
    2's 18 of 103 (the 13 of E14.6 point 2, the G2, the three RealBots, THEMIS); type 4's 5 of 20 (the A2, A3, A3 Ultra,
    X2, X2 Ultra); type 3's none. **Every other robot's rows identical**; the Sources and About sheets gain their new
    lines.
  - **The joint modules at their modes, now, and their share of the robot's mass:**

    | Robots | Joint modules | Share of the robot's mass |
    |---|---|---|
    | Unitree H2-X | 29.4 kg | 45 % |
    | Tien Kung 3.0 | 28.7 kg | 44 % |
    | LimX Oli | 21.4 kg | 39 % |
    | AgiBot A3, A3 Ultra | 25.3 and 26.7 kg | 46 and 45 % |
    | AgiBot X2, X2 Ultra | 18.8 and 19.7 kg | 54 and 51 % |
    | AgiBot A2 | 24.4 kg | 35 % |
    | Unitree R1-A5-D, R1-A7-D | | 45 and 46 % |
    | PAL REEM-C | | 20 % |
    | Robots on wheels | | 9 to 20 % |
    | Noetix Bumi, E1 | | 46 % |
    | **Booster T2** | **29.7 kg** | **71 %** |

  - **E13's shares on the new files:** type 1 13 of 31 on the joint template, 12 on the battery template ("Its robots
    on templates", below half); type 2 67 and 63 of 102; type 3 75 and 68 of 96; type 4 32 and 30 of 50, as forecast.
- **Found: the Booster T2's frame below zero in 4.1 % of its draws**, new. Its model's limits are high (its legs 135,
  its waist 135 to 144 N·m), and type 1's rule, the torque over 87.3 N·m/kg, puts 29.7 kg of its 42 kg in its joints.
  Type 2's fit would put 24.9 kg there (59 %). The Booster T1 by the same rule puts 50 % there. The 1X NEO's frame is
  still below zero, as before (13.9 % of its draws at 2,000; 11.1 % before: other draws). **For his word.**
- **Not covered:** his runs at 200,000 draws.

### V131. E14's downloads read

- **His words:** "download what ever is possibel".
- **How:** the nine PDFs E14.1 names, by `curl` into `downloads_e14/` (Claude's scratch folder): every one HTTP 200 and
  `application/pdf`, 0.43 to 17.96 MB, each opened as a PDF (`file`).
  - Seven were read as text with macOS's PDFKit (`tools_e12/pdftext.swift`).
  - Two have no text, so their pages were rendered by PDFKit (`tools_e12/pdfpages.swift`) and read by macOS's text
    recognition (`tools_e12/ocr.swift`): LimX's Oli brochure (4 pages, its pages 2 and 3 also by eye) and RealMan's
    specs V1.6 (32 spreads, 62 pages).
- **Result:** as E14.5's table: THEMIS Gen2.5 "36.5kg", "Dual 259.2 Wh Li-Ion packs", its computers and cameras;
  RealMan's WHJ modules (WHJ60 1040 g at 60 N·m, WHJ30 750 g at 30, WHJ10-B 455 g, WHJ10-N 425 g at 10), the RealBots'
  7-DoF arms with the RM75's force-torque sensor, the Dual-Arm Lift's "RM65-B-V"; the Oli's two D435i and its IMU. The
  PAL, Boston Dynamics and NEURA sheets hold nothing new for the model.
- **By eye:** RealMan's page 5 (printed 08/62), its WHJ table: every mass, rated torque and brake as recognized (WHJ03
  170 g, 3 N·m, soft; WHJ10-B 455 g, 10, pin; WHJ10-N 425 g, 10, soft; WHJ30 750 g, 30, pin; WHJ60 1040 g, 60, pin).
  The pin brakes of WHJ60 and WHJ30 and the soft brake of WHJ10-N fit the RM65's "Mechanical Brakes on Joints 1-3,
  Soft Brakes 4-6" and the RM75's "1-4", "5-7".
- **Not covered:** RealMan's other pages were searched in their recognized text, not read by eye (the RealBots' pages
  15 to 18 were read in it in full).

### V130. The research pass's second round read again; E14's shares computed

- **What:** the figures of round 2 that E14 uses, first read by two reading agents, and E14's effect on E13's shares.
- **How, the pages:** opened in the browser pane, their text searched on the page.
  - AgiBot's A2 Ultra and A2 Lite table: "≈69kg", "≈64kg", "Peak Knee Torque" "270N·m", "Battery Capacity" "14.4Ah",
    "Charger Output 54.6V 8A";
  - AgiBot's X2 table: "Approx.35kg", "Approx.39kg", 25 and 30 DoF, arms 5 and 7, "Peak Joint Torque 120N·m",
    "Approx.500Wh";
  - Unitree's H2-D page: "33.5Kg / Approx. 148Kg / Approx. 120Kg", "Maximum Arm Joint Torque 120N.M" ×3, "Column DOF"
    2 and 1, the three batteries 972, 864 and 1,440 Wh;
  - Unitree's R1-D page: "Maximum torque of the shoulder 60N·m" ×4, 11 / 13 / 30 / 32 kg;
  - Unitree's G1-D page: "Approx. 90kg", "Upper Body Battery(Quick-release): 9Ah", "Chassis Battery (Built-in): 30Ah";
  - PAL's Kangaroo page: "Weight 50-65 kg", "Battery 15Ah, 63V. 976Wh" (already entered);
  - Noetix's Bumi and E1 pages (V123).
  - The 1X NEO's page showed no specifications in the pane. Its "842 Wh" is already entered from 1X's page (1XN).
- **How, the model files:** parsed on the page, as V123. AgiBot's a3_ultra_t3d0 (63 joints, 60.01 kg; the A3's 31
  limits and two hands of 16); RealMan's RM65-B-V (60, 60, 30, 10, 10, 10; 7.27 kg); PAL's `pal_sea_arm` tiago-pro
  limits (arm 43, 43, 26, 26; wrist 26, 26, 26). Every value is as the agents reported.
- **The shares:** `pass/shares_after.py` (Claude's scratch folder) over his files of 11:49 (only read): each type's
  robots and versions drawn, by the register's sheets; on the joint template now and after E14's 21 robots and versions
  come off, the G2 staying. Type 1 16 → 13 of 31, type 2 80 → 67 of 102, type 3 80 → 75 of 96, type 4 40 → 32 of 50.
  Battery template: type 1 13 → 12, type 4 31 → 30.
- **Not covered:** nothing is entered; the robots listed in E14 as not yet searched; the PDFs (not downloaded).

### V129. His runs of 11:49 to 11:58 read back

- **His runs:** the register at 11:49:31, type 1's builder at 11:49:50, 01 at 11:50:04, 02 at 200,000 draws from 11:50
  to 11:58:25, ended without fault. His type 3 and 4 files are of 10:38, built after their builders' code (10:23 to
  10:28); type 2's file is of 2026-10-30 13:50, after its code. 03 has not been run (`figures/comparison/` is empty).
- **Times** (each output against the code that makes it; `02_composition.py` of 11:45:25):
  - all 72 files of `data/consolidated/`, 56 of `data/parts_taken_apart/`, 39 pages of `figures/composition/` and 92 of
    `figures/parts_taken_apart/` written between 11:56 and 11:58;
  - none is older.
- **The summaries:** none of the ten (consolidated, types 1 to 6; part by part, types 1 to 4) has a median or 2.5 %
  of 0 for anything held. Held in some draws only: 5, 6, 2, 1, 1, 1 rows (consolidated) and 110, 246, 277, 262 (part
  by part), the same counts as in V126's sandbox.
- **Looked at:**
  - type 1's "where its aluminium 6061 sits", the page his run of 11:42 stopped on: drawn, the frame and shell 4.9 kg
    held in 100 % (its 72 draws below zero left out);
  - type 3's notes page: "Not yet taken apart: 77 of its 168 robots of the register with a mass"; the sentence on the
    axis's end.
- **Tests:** one test out of date. `test_schemas.TestPartsTakenApart.test_the_real_file_holds_together` counted 32
  robots in his type 1 file, which since batch 2 holds 31 (the PrimeBOT Q1 out). It was changed with the reason beside
  it. After that the 86 tests that compare with his files pass (the register, the parts files, 01's tests of type 1's
  file), and **the whole suite: 437 tests, all pass**.
- **Not covered:** 03 (not run); iCloud's copies of the pages (Documents synced by iCloud: their times to be checked
  again if a page looks older).

### V128. His 02 run stopped on a draw below zero; the logarithmic pages over the draws above 0

- **Found by his run** of `02_composition.py` at 200,000 draws (after f838731). It stopped in `sources_figure` on type
  1's pages of where a material sits: "ValueError: Axis limits cannot be NaN or Inf". Before stopping it had written
  every type's consolidated draws and summaries and type 1's part-by-part draws (11:42). Type 1's pages and all of
  types 2 to 4 were still those of 10:57 and 10:58.
- **Cause, read from his draws** (`data/parts_taken_apart/1_compact_research_developer/materials.npy`, only read):
  remainders below zero in a few draws, reported by 02 and not cut. Type 1's frame aluminium was below zero in 72 of
  200,000 draws (as low as −1.8 kg), its battery pack's aluminium in 33, its copper and plastics in 69. V126 had made
  these pages take the draws that are not 0, and the logarithm of a negative mass is NaN. The tests and the sandboxes
  ran at 2,000 to 3,000 draws and met none: 72 in 200,000 is fewer than one in 2,000.
- **His words:** "Yes, fix it" (the pages over the draws above 0, said on the notes, test first).
- **Test first** (`TestDrawsBelowZero`): a kind with 400 of 20,000 draws below zero, sorted as the page's first row. It
  reproduced his error ("Axis limits cannot be NaN or Inf"). After the fix:
  - its median and its share held are those of the draws above 0;
  - the element, critical and overview panels draw with such draws, their limits finite.
  - A first version passed by chance, with the negative kind second, where `min` passed over its NaN; it was sharpened
    before the code was changed.
- **Fixed:** `sources_figure` takes the draws above 0, and its notes sentence says that a draw below zero has no
  place on a logarithmic axis. Every other `log10` of 02 already had only draws above 0, and the linear panels already
  left out the draws not above 0 (searched: every `log10`, `set_xlim` and `set_ylim` of 02 and 03). The summaries keep
  the negative draws in their statistics. The rule, `CLAUDE.md` §7, has a clause for logarithmic axes.
- **Not covered:** his run again (it rewrites everything). A rare draw of another kind is not foreseen by a test at
  2,000 draws. A test with synthetic draws, as here, is the way to catch it.

### V127. The axis of the distribution panels at the 99.5th percentile, built

- **His words:** "Yes, build it", his answer to the next-step box's question, which asked about the axis of V124. The
  question of the RAWCLICDataCenters session is a separate one and was left for him to answer there.
- **Tests first** (`TestAxisEnd`, on 20,000 lognormal draws with a long tail, as type 2's): written before the code, all
  6 erred (no `AXIS_END`). They check the following:
  - the setting is 99.5;
  - the element panel's 70 bars end at the 99.5th percentile, its axis below 1.1 times it, and its bars' heights add up
    to the share of the draws on the axis (nothing rescaled), with "… % beyond the axis, up to … kg" above the panel;
  - the same for the critical elements' panel, both kinds' bars together;
  - the overview's axis ends at its largest row's 99.5th percentile, with nothing piled into the last bar;
  - no words where nothing lies beyond;
  - a long title of a critical element is clear of its words.
- **After the code:** the 6 pass, and the 21 figure tests of `test_parts_taken_apart.py` pass (readability, overlap,
  centre, notes, held in). One older test now checks the first line of the critical panel's right-hand words (the
  share held), as that text may now also hold the words on the axis's end. **The whole suite:** 435 tests, the same 5
  failing as in V126 (they compare with his files on disk).
- **Built:** `02_composition.py`:
  - `AXIS_END = 99.5`, `axis_end`, `beyond_words`;
  - `element_panel` and `stacked_panel`: bars from the smallest draw to the end, the words above the title's line;
  - `ridge_panel`: the end at the largest row's 99.5th percentile (the 99.9th before), the draws beyond left out (they
    were piled into the last bar), the words on its axis's label;
  - the notes pages, one sentence each.
- **Sandbox** (`sandbox_zero/run.py` into `sandbox_zero/axis/`, 2,000 draws): 01, 02 and 03 ran to the end. The draws
  are identical to V126's run, 54 of 54 files.
- **Looked at, type 2:**
  - the material page 1: copper's axis to about 7 kg, where it ran to 13 kg before, and "0.5 % beyond the axis, up to
    12 kg"; the magnets' classes held in some draws, "in 68 % of the draws", then their numbers and the words;
  - the critical elements page 1: its panels' words above their titles, clear of them;
  - the overview page 1: copper's axis to 3.6 kg (4.7 before), aluminium's to about 137 kg (225), the label "0.071 %
    beyond the axis, up to 7.3 kg (of its rows' draws)". Its rows share one axis, so aluminium's small rows stay
    narrow.
  - At 2,000 draws the shares beyond read 0.51 to 0.6 % where few draws hold a material; at 200,000 they are 0.5 %.
- **Not covered:** his 02 run at 200,000 draws. The share of the axis the 95 % interval now takes was measured in V124
  for an axis from 0 to the 99.5th percentile, not again on these pages, which begin at the smallest draw as before.

### V126. The zero rule built: every statistic over the draws that are not 0

- **His words:** "Yes, build it", to the fix of V125 (test first; the axis of V124 not asked for, not built).
- **Tests first:** written before the code and run: 10 failed or erred (`statistics_of` over the draws not 0, a
  remainder's negative draws kept, none for a quantity 0 in every draw; the page of a workbook type; 03's number beside
  a row and its agreement with 02's summary; the pages of where a material sits, type 2; the summary of a type taken
  apart, type 2; the catalogue's "0.0" not a mass; type 3's sheet, 13 robots without a mass). After the code: all 15
  of the new and changed tests pass. **The whole suite:** 429 tests; 6 failed, one of them type 3's card ("169 with a
  mass", now 168: the Reflex), changed with the reason beside it and passing; the other 5 the same as before the change
  (V122): they compare with his files on disk (the register, type 1's parts file, 01's three tests of type 1's file)
  and pass after his runs.
- **Built:** `02_composition.py` `statistics_of` (the one function of every statistic of 02 and 03: mean, median and
  95 % over the draws not 0, "Held in (% of the draws)", None where 0 in every draw; the share below zero of all the
  draws as before); `statistics` and `summary.csv` of a type taken apart with "Held in"; `summary.csv` and `.xlsx` of
  every type with "Held in", "In the elements, mean" over the same draws; `interval_chart` with a column "Held in";
  `sources_figure` over the draws that hold it, three columns as the overview (its axes 0.52 of the page); the notes'
  "Not yet in the elements" with the share held; the run log. `03_comparison.py` `statistics` with the share held,
  `beside` ("2.00 (40 %)"). `tools/make_humanoid_register.py` `stated` and `mass_bounds`: a catalogue's 0 not stated.
- **Sandbox** (`sandbox_zero/run.py`, Claude's scratch folder: the register, the four builders, 01, 02 and 03 at 2,000
  draws, every output there, his files only read), from the working tree and from e34c0b7 (a scratch worktree, removed
  after):
  - **The draws unchanged:** all 54 `.npy` files of `data/consolidated/` and `data/parts_taken_apart/` identical.
  - **No median or 2.5 % of 0 for something held** in any of the ten summaries (6 consolidated, 4 taken apart); held in
    some draws only: 5, 6, 1, 1, 1, 1 rows (consolidated, types 1 to 6; 2 for type 3) and 110, 246, 277, 262 (taken
    apart, types 1 to 4); 0 in every draw: their statistics empty.
  - **The Reflex:** in the register no height, no stated mass, no min, mode or max, its basis "the catalogue reads 0.0:
    not stated, so no mass"; on the sheet Type 3 "not drawn: no mass stated"; 02 names it among type 3's 13 not drawn.
  - 01 no fault; 02 and 03 ran to the end (0).
- **Looked at:** type 2's "where its copper sits" (the wheeled base 533 g, held in 47 %; the lift column 69 g, 9.9 %;
  the hips 566 g, 54 %; no line from the left edge; every number within the page); 03's `materials.png` (titanium
  "0.400 (3.8 %)" for type 1, "1.12 (3 %)" for type 2, where the mean of all the draws was 0.013 and 0.033 kg).
- **Not covered:** his runs (the register, 01, 02 at 200,000 draws, 03); the other RAWCLIC repositories (RAWCLICDataCenters
  is a session of its own).

### V125. Every 0 in the statistics, the figures and the inputs

- **His words:** "It can not be that median is 0. If a value is 0 then it is NOT part of the distribution", then "Check
  for all with 0 values. There needs to be a rule, if it is generally 0 then, it is not part of the distribution".
- **How:** every statistic in `01_schemas.py`, `02_composition.py`, `03_comparison.py` and `tools/` read (grep of
  median, percentile, mean, histogram, violin); his outputs of 1 November 10:56 to 10:58 (`data/consolidated/*/`,
  `data/parts_taken_apart/*/`, `figures/`) only read; the inputs scanned for a minimum, mode or maximum of 0 (the four
  parts files built from the committed code into Claude's scratch folder, the register, his workbook
  `data/02_HumanoidlRobots.xlsx`, the catalogue `data/raw/humanoid_guide_2026-10-28.xlsx`). Scripts in Claude's
  scratch folder: `axis_measure_apart.py`, `zero_inputs.py`.
- **Counting the zeros (wrong):**
  - `sources_figure`, the pages "where its … sits" (`figures/parts_taken_apart/<type>/sources/`): the violins over the
    draws above 0, but the dots, the 95 % lines, the written median and mean and the order of the rows over all the
    draws. Type 2's copper: the wheeled base and the lift column "0 mg" as their median; the lift column's mean 6.7 g
    while its violin sits near 70 g; the hips', knees', ankles' and waist's 95 % lines from the left edge.
  - `write_taken_apart`'s `statistics`, `data/parts_taken_apart/<type>/summary.csv`: a median of 0 for an element in
    a kind of part held in some draws in 37 (type 1), 86 (2), 97 (3) and 83 (4) rows.
  - `statistics_of`, `data/consolidated/<type>/summary.csv` and `.xlsx`: a median of 0 for one held in some draws in
    5, 5, 1, 0, 1 and 0 rows (types 1 to 6: titanium, V, As, In, W; titanium, V, As, In, Zr; Pb; Pb); the notes
    page's "Not yet in the elements: … (median …, mean …)" is written from these rows.
  - `interval_bars` (02's page of a type drawn from the workbook, 03's comparison pages) and 03's `statistics`: the
    mean bar and the 95 % line over all the draws.
  - 02's run log, the critical elements in one robot: over all the draws.
- **Over the draws above 0 already (right):** `element_panel` (the material and element pages), `stacked_panel` (the
  critical elements), `ridge_panel` (the overview), each with "in … % of the draws".
- **The inputs:** no minimum, mode or maximum of 0 in the four parts files or in his workbook. One in the register:
  robot 257, Reflex (Reflex Robotics, type 3, on wheels), a mass of 0 / 0 / 1 kg, made by `mass_bounds` from the
  catalogue's row 258, whose height, mass, degrees of freedom and walking speed all read "0.0" (not stated). It is not
  taken apart, so it is not drawn; it is counted among type 3's robots with a mass (and "not yet taken apart").
- **RAWCLICDataCenters** (read only, its summaries of 22 and 23 October): the same counting of zeros, a median of 0 for
  one held in some draws in `data_center_it_materials/material_summary.csv` 607 rows, `data_center_pcb_area/
  summary_statistics.csv` 264, `data_center_infrastructure_materials/quantity_summary.csv` 30, `item_summary.csv` 15,
  `material_summary.csv` 12, `data_center_pcb_area/pcb_area_summary.csv` and `pcb_counts_summary.csv` 13 each; its 03
  "where the copper comes from" and its distribution panels over all the draws.
- **Rule written:** `/Users/rm/Documents/GitHub/CLAUDE.md` §7, "A 0 is not part of a distribution".
- **Not covered:** nothing is changed yet; the other RAWCLIC repositories are not checked.

### V124. How much of each distribution panel's axis the tail takes

- **His words:** "The distribution figures show the distribution pressed to the left side. You give away have of the x
  axis."
- **How:** `axis_measure_apart.py` and `axis_cut.py` (Claude's scratch folder) on his draws of 1 November
  (`data/parts_taken_apart/*/`, 200,000 draws a type, only read): each material and element summed over its kinds of
  part, the draws above 0, as the pages draw them.
- **Result:** the axis runs from the smallest to the largest draw. The 97.5th percentile sits at 62 % (type 1), 34 %
  (2), 36 % (3) and 47 % (4) of the axis, the median over the panels; type 2's copper runs to 13 kg with 97.5 % of the
  draws below 5 kg. An axis ending at each panel's 99.5th percentile would put it at 86, 66, 70 and 77 %; at the 99th
  at 91, 79, 82 and 85 %; at the 99.9th at 77, 51, 54 and 65 %. RAWCLICDataCenters bins its histograms the same way,
  from the smallest to the largest draw.
- **Not covered:** nothing is changed yet; proposed to him (the 99.5th percentile), not agreed.

### V123. The model files of the research pass, read again (E13 rule 3)

- **What:** the torque limits and link masses four reading agents reported from the makers' model files.
- **How:** each file opened in the browser pane (raw.githubusercontent.com), parsed on the page: every moving joint's
  `effort`, the sum of the `<mass>` values.
- **Result:** every value as reported: Booster T2 (31 joints, 41.99 kg); AgiBot X2-Ultra v1.4.0 (31, 44.80 kg), X2-EDU
  (29, 41.20 kg), A3 T3.0 (31, 56.80 kg) and T2.5 (57.98 kg), G2's body and arm macros (body 5 × 50, head 3 × 50, arms
  108 / 108 / 35 / 35 / 35 / 18 / 18); Unitree H2-D (24, 133.94 kg), H2-X (31, 67.60 kg), G1-D (34, 71.00 kg), R1-A7-D
  (29, 38.54 kg; its lift's effort written as 0), R1-A5 (13, 14.79 kg); Galaxea R1 Pro 2025 (28, 93.27 kg) and 2026
  (92.83 kg, its grippers' effort 0); RealMan RM65-B (6, 7.17 kg) and RM75-B (7, 7.78 kg); Tien Kung 3.0 (31, 65.82
  kg); LimX Oli HU_D04 (31, 52.55 kg); PAL REEM-C's legs (v0 and v1), arms, wrists (joint 5 "TODO: Check effort
  value!"), torso and head, ARI's arms and wheels, Kangaroo's legs, ankles and pelvis. Read on Noetix's own pages: Bumi
  "关节模组最大扭矩 70N.m", "48V 5.1Ah", "17kg"; E1 "膝关节最大扭矩150Nm", "整机重量40kg", "10.6Ah" (no voltage).
- **Not covered:** the files' efforts are limits of simulation models (rated or peak not stated); nothing is entered.

### V122. The entry of batch 2 of types 3 and 4 (EVIDENCE E12.6, E12.7), built and run in the sandbox

- **His words:** "Yes, build it" (E12.6, open points A to C as recommended).
- **Tests first:** written before the code and run: 15 failed or erred (the 30 blocks' names and masses, the ratios, the
  joints from a stated joint, the hands and batteries, the lifts, the robots listed only, the register's sheets and
  masses, the shares and their words, type 2's card). E13 rule 1's test passed before the code, as the templates of
  types 1 to 4 already span half to 1.5 times; its narrowed copy (a battery template 10 / 14.67 / 20 Wh/kg) is caught.
- **Found by the tests and the sandbox while building, and fixed:** the DUCO's chest cameras of the kind "Torso", none of
  the figures' kinds: 02 stopped on it before drawing ("1 fault(s) in the inputs; nothing is drawn"), set to Head; four
  names too long for 01's table ("Cyborg Robotics CYBORG RO1 SE" over the height column), shortened (E12.7 point 2);
  older tests that counted the PrimeBOT Q1 (type 1's 17 robots on the template, 32 versions, type 4's 131 with a mass),
  changed to the new counts with the reason beside each.
- **Read first-hand in the build:** Origin of Bots' Centaur G1 page ("WEIGHT 85 kg"), the min agreed in E12.5 question 2,
  which E12.4 had from a search summary only.
- **The ratios, by program** (the builder's `joint_ratios`): on legs over the knee hip pitch 1.00 (0.47 to 1.00), hip
  roll 1.00 (0.45 to 1.13), hip yaw 0.25, knee 1.00, ankle pitch 0.33, ankle roll 0.24, waist 0.36, shoulder 0.27, elbow
  0.17, wrist 0.08, head 0.08; on wheels a second waist joint 0.77 (0.54 to 1.00), shoulder 0.24, elbow 0.13, wrist
  0.04, head 0.06 (E12.7 point 1: two differ from E12.5's figures).
- **Sandbox** (`sandbox_e126/run.py`, Claude's scratch folder): the register, the four builders, 01 and 02 at 2,000
  draws, from the commit c6d5570 (a scratch worktree, removed after) and from the working tree, every output into the
  scratch folder, his files only read. Working tree: 01 no fault; 02 no fault, type 1 over 30 robots (31 versions),
  type 2 over 96 (102), type 3 over 91 (96), type 4 over 47 (50); one remainder below zero, the 1X NEO's frame (11.1 %
  of its draws, known, E11.8). **Type 2 unchanged:** its 13 part-by-part draw files identical to the commit's; the
  draws for stock-and-flow of types 2 to 6 identical (50 of 50 files); type 1's differ (the PrimeBOT Q1 out): its mean
  33.7 kg before, 34.2 kg after (95 %: 17.0 to 42.7, then 17.4 to 42.6).
- **E13 rule 1's measure repeated** (`goal/uncertainty.py` on the new files): the robots on templates still wider than
  those on their own data (joints per kg 0.71 against 0.24; cells 0.79 against 0.12; Cu 0.56 against 0.42; Nd 1.09
  against 0.86); the shares: type 1 16 and 13 of 31, type 2 80 and 64 of 102, type 3 80 and 69 of 96, type 4 40 and 31
  of 50, as E12.6 counted.
- **Looked at:** 01's `overview_2.png` (each card of types 1 to 4 ends "Most of its robots rest on templates: …", inside
  its box); 02's notes page of type 3 (its 91 robots, the 78 not yet taken apart, the line on templates).
- **What the PrimeBOT Q1's leaving left behind** (open point A): a search of the stages, `src`, `tools` and `tests` finds
  no reader of `PRIMEBOT_Q1` or `MASS_ESTIMATES`; the PrimeBOT Q1 named only in comments and in tests that it is
  listed only; METHODOLOGY's line rewritten; EVIDENCE E5.17 kept as the record.
- **Size at 200,000 draws** (×100 the sandbox's): type 3's part-by-part draws about 2.7 GB, type 4's 1.8 GB.
- **The whole suite:** 421 tests; 5 failures, each waiting for his runs: the register's builder and type 1's builder against his files on disk (they hold the PrimeBOT Q1 and batch 1 only), and three tests of 01's table of type 1, which read his type 1 file on disk (`TestScreenPages`); 1 skipped, the check of his real register and files (types 3 and 4's are not on disk).
- **Not covered:** his runs at 200,000 draws; the tests that compare with his files on disk wait for his runs 1 to 4.

### V121. What the spec of batch 2's entry (EVIDENCE E12.6) rests on, checked in the code and data

- **His words:** "Spec the entry".
- **In the code (read only):** the register's `register_rows` takes a robot's mass from the catalogue, and from
  `MASS_ESTIMATES` where an estimate is agreed (only 236, the PrimeBOT Q1); 01's `type_card_text` takes a type's masses
  from its parts files (`apart.constants`), so a robot listed only must have no rows there; type 1's template is
  `average_joints(BATCH_ONE)`, without the PrimeBOT Q1 (a `catalogue_block`); the PrimeBOT Q1's other readers: its
  block and `rows_of` in type 1's builder, `TAKEN_APART[1][236]`, the register's About line, two tests in
  `test_make_humanoid_register.py` and two in `test_schemas.py`, METHODOLOGY's line on it.
- **In the data, by program** (the register as its builder writes it, Claude's scratch folder): batch 2 by its first
  type among 3 and 4: type 3's file 62, 63, 66, 67, 71, 72, 73, 75, 76, 77, 78, 81, 83, 84, 88, 89, 90, 93 (18), type
  4's 59, 61, 64, 74, 79, 91, 94, 95 (8). After the entry, with the Clone Alpha (65) and the PrimeBOT Q1 (236) without a
  mass: type 1 31 listed, 30 with a mass, all drawn; type 3 181, 169, 91 drawn, 78 not yet; type 4 135, 129, 47 drawn,
  82 not yet, 6 without a mass.
- **Corrected while counting:** E12.5 point 12's shares (97 and 51 robots and versions after batch 2) are 96 and 50
  (type 3 gains 21, the PrimeBOT Q1 leaves type 4): the joint template 80 of 96 and 40 of 50, the battery template 69
  of 96 and 31 of 50; written in E12.6.
- **Not covered:** nothing built or run.

### V120. Batch 2's proposal (EVIDENCE E12.5) at its modes

- **His words:** "Propose the numbers"; "Batteries, where the energy is given, can be estimated compositon and weight due
  to chemistry. Also the joints can be well estimated, based on the other joints."
- **The joint ratios, by program** (`batch2/joint_ratios.py`, `wheeled_ratios.py`, Claude's scratch folder, reading the
  builders' blocks): over the seven robots on legs with every joint (H2, Kuavo 5, Luna, MagicBot Gen1, Adam Lite, Adam
  SP, Atom), each joint kind's largest torque over the robot's largest: the knee the largest in six (the Atom's hip roll
  241.4 over its knee's 213.8 N·m); the medians and ranges in E12.5 point 2. On wheels, the Vega 1 Pro's and RB-Y1's
  waists the largest (700, 270 N·m); the AI Worker has no waist (its shoulders the largest), so its ratios not used for
  the waist.
- **At the modes** (`batch2/batch2_modes.py`): every block's joints (the template, or from its stated joint by the
  ratios and E6.8's fit), hands, pack (its Wh at 164 Wh per kg), base (E9.6's hub motor classes, casters 0.27, steering
  0.79 kg), lift (19.9 %), shell (11.5 %), and the small items roughly (screws 0.5, boards 0.8, sensors 0.3 kg, cables
  0.036 kg per metre); the frame the remainder. First run: the Dora from its second-hand 120 N·m at 64 % joints, a
  frame of 1.2 kg (6 %); proposed on the template instead (5.1 kg, 25 %). The Cruzr S2 and Y1 first with four wheels;
  set to the template's two and two casters, as no source counts them.
- **E13's shares after batch 2** counted from the register's types and V119's counts: type 3 joints 81 of 97, battery
  70 of 97; type 4 joints 41 of 51, battery 32 of 51.
- **Not covered:** the model's own draws (the sandbox comes with the entry); the small items are rough, so a frame
  near a quarter of the mass is not proven safe in every draw.

### V119. How uncertain the robots on templates are, and how many of each type they are (EVIDENCE E13)

- **His words:** "If the composition is based on mass based estimates the composition has larger uncertainties,
  furthermore they should not be the majority of a given type. Otherwise additional rules have to be formulated."
- **How:** `goal/uncertainty.py` in Claude's scratch folder: types 1 to 4 drawn by 02's own `draw_taken_apart` at
  20,000 draws over the tests' inputs (the four parts files as their builders write them, the register as its builder
  writes it), the magnets' fractions fixed (the tests' `fixed_magnets`); writes nothing. A robot's joints count as the
  template where any of its body joints is a share of its joint modules (sheet Joints, "Share"); its battery where it
  has no voltage and capacity of its own (sheet Constants). Per robot (at least 50 draws), the 95 % interval over the
  median of its joint modules, battery cells, Cu, Nd, Dy, Li and Co per kg of its mass; then the median over robots.
- **First run corrected:** robots with fewer than 200 draws were left out, which dropped every robot in two versions;
  the threshold set to 50, every robot and version counted (type 2: 102, type 3: 75).
- **Result:** E13's two tables. The templates' widths come from the standing rule (half to 1.5 times the mode); the
  robots' own data narrow them (a stated battery ± 5 %, each joint fitted from its own torque).
- **Not covered:** the magnets' own spread (fixed here); a robot of two types is counted in each; nothing changed.

### V118. The internet for the robots the makers leave empty, and which robots rest on estimates only (EVIDENCE E12.4)

- **His words:** "If you are not able to find data from the company, check the internet. If you find nothing, then list
  the robot, but do not include it into the evalution. I do not want a robot in the data, where all data are soly based
  on estimates".
- **The internet, batch 2:** 16 searches (standard), their results used only to find pages; the pages read first-hand
  (four web-fetch reads, the built-in browser); refused pages listed in E12.4, nothing bypassed (GlobalSpec's security
  check). Found in passing: the DEUX's mass and battery on its maker's page, which the first read had missed because the
  table loads only at the page's foot; E12.1 corrected.
- **Which robots rest on estimates only, by program** (`goal/estimates_only.py`, Claude's scratch folder; the four parts
  files as their builders write them, read with 01's `read_parts_taken_apart` and `row_base`): a robot's own sources
  are the codes its row of the sheet Robots names; a row counts as its own when its sources name one of them. Result
  (162 robots and versions): mass from the maker 95, a third party 66, estimated 1; with a stated figure of their own
  composition 120 (a row of their own labelled S or W, a joint torque, stated module masses); names of their own only
  12; nothing of their own but the mass 28 (listed in E12.4). Per register type, those with a stated figure of their
  own: type 1 22 of 31, type 2 73 of 96, type 3 56 of 72, type 4 22 of 33, type 5 2 of 2.
- **Checked by hand:** the Apollo and the Borg 01 (counted "nothing of their own"): every row of theirs read; their
  mass is the catalogue's, every other row "E" or a template (E11.6 points 6, 7, 10). The Noetix Bumi (counted "names
  only"): its computer and shell material from the catalogue, all its figures estimates.
- **Corrected while writing:** E12.4 first gave the stricter reading's counts as "about 68" and "about 64"; counted by
  program instead (73, 56).
- **Not covered:** a row whose sources name the robot's own source under a code its row of Robots does not list would
  be missed (the two read by hand had none); nothing changed in the register or the files.

### V117. Batch 2's downloads (EVIDENCE E12.3)

- **His words:** "Yes, agree E12.2" (point 5: open Agility's, Elite's and DEEP Robotics' sheets; not the ZIP, the
  brochure or the manuals).
- **DEEP Robotics:** its DR02 page links no sheet; its resource centre lists one DR02 document, "产品手册 PDF / 6.952
  MB"; downloaded with `curl` into a folder of its own in Claude's scratch folder (7,289,406 bytes, "PDF document,
  version 1.4"), its text taken out with macOS's PDFKit (`tools_e12/pdftext.swift`, scratch): two pages, the table of
  E12.3. The 1,440 Wh over 20 Ah gives 72 V, the voltage of its power socket on the same sheet (arith., not stated as
  the battery's).
- **Agility and Elite:** each sheet behind a form asking for personal data and a CAPTCHA; nothing entered, nothing
  submitted (his data is not entered into a form without his word).
- **Not covered:** the DR02 sheet's figures are the maker's laboratory data, as it says; the Digit's and the
  Centaur-G1's sheets.

### V116. Batch 2 of types 3 and 4: what was read (EVIDENCE E12)

- **His words:** "Yes, batch 2".
- **Which robots, by program:** the register as its builder writes it (into Claude's scratch folder), its robots of
  type 3 or 4 with a mass and no rows of their own, in the register's order: 151; the first 27, numbers 59 to 95.
- **How read:** seven web-fetch reads of the makers' pages (each asked for verbatim figures, "not stated" where a page
  gives none, no file opened); then myself in the built-in browser for the pages that gave no text or refused
  (CasiVision; UBTECH's two spec diagrams, as pictures on their pages; Faraday Future's spec tables, which the fetch
  did not see; Addverb's Elixis-W tab; Elite; Sharpa; XYZ; Noetix; Addverb's GitHub folder); four searches for the
  makers' pages of LG, Siasun, AVIC and Noetix, used as leads only.
- **Refused or failing:** Sharpa's page answered "429 Too Many Requests" to the fetch (read in the browser); XYZ's
  "403" (read in the browser); BOSHIAC's site fails on its certificate (not bypassed, not read); Noetix's English host
  does not resolve (its Chinese site read in the browser); DEEP Robotics' English page "404" (its Chinese page read);
  LG's CES launch release not found on its sites.
- **Not opened** (downloads, his word first): Agility's product sheet, Elite's parameter table, DEEP Robotics' product
  sheet and offline documents (ZIP), UBTECH's brochure and downloads, Cyborg's manuals, a Siasun PDF (not of the DUCO).
- **Checked in the writing:** E12.2's counts recounted from E12.1 (a mass for 11, not 15 as first written; voltage and
  capacity or energy for 4, not 5; a named computer for 10, not 14).
- **Not covered:** the robots' parts (nothing proposed or entered); the catalogue's figures not checked beyond being
  named second-hand.

### V115. Where the dataset stands against his goal (2026-11-01)

- **His words:** "It is the goal to have most of the humanoid robots being part of the dataset and than most of the data
  are based on data given in the internet".
- **How:** `goal/coverage.py` and `goal/joints.py` in Claude's scratch folder: the register and the four parts files
  written by their builders into the scratch folder (his files only read), counted with 01's own functions
  (`read_register`, `cell_rows`, `row_base`: weighed, the maker, a third party, estimated).
- **Coverage:** 354 entries; 324 with a robot type; 311 with a type and a mass; 154 taken apart (type 1 31, type 2 96,
  type 3 72, type 4 33, type 5 2, type 6 0, a robot of two types counted in each); 157 to do (by leading type: 3 78, 4
  70, 5 5, 6 4); 13 with a type and no mass, not in the evaluation.
- **Where the numbers come from**, over the 162 robots and versions of the four files, cell by cell as 01's table
  colours them: mass from the internet 99 %; joints estimated 91 % (by kind: the template's share of the mass 75 %, from
  stated torques by the fit 23 %, weighed 1 %, stated module masses 1 %); battery estimated 60 %, stated 40 %; boards
  estimated 84 %; frame and shell estimated 99 % (the frame is the remainder).
- **Before his runs:** the register on disk is of 2026-10-30 14:44 and the files of types 3 and 4 are not on disk
  (`stat`), so these counts are of what the builders write, not yet of his files.
- **Not covered:** the share of each robot's mass that rests on stated numbers (the cells count robots, not kg).

## 2026-10-30

### V114. The entry of batch 1 of types 3 and 4 (EVIDENCE E11.7, E11.8), built and run in the sandbox

- **His words:** "Yes, build it" (E11.7, open points A to C as recommended).
- **Tests first, as far as it is on record:** the tests of the 28 blocks, the templates, the register's sheets and the
  drawing over several files were written before their code was finished; that each failed before its code is not on
  record for all of them (the builders' check against 01 is seen failing), so it is not claimed. The test that each
  robot of type 3 is drawn with its own file's shared numbers (`test_each_robot_drawn_with_its_own_files_shared_numbers`)
  was written after its code, so it was proved by two deliberate faults in 02, the file restored byte for byte
  afterwards (checked with `cmp`):
  every robot with the first file's numbers stopped 02 with a KeyError (a template name type 1's file does not hold);
  type 4's robots with type 3's file's numbers, whose names are the same, failed the test ("3 != 4 : AgiBot X2").
- **Corrected in the tests, against the register:** type 3 has 75 versions (the AgiBot X2, the Flexiv AICO 2 and the
  Rainbow RB-Y1 in two each), type 4 34 (the X2): I had written 74 and 35. The register's test of every robot with its
  own rows got batch 1's 27 numbers from E11.7's list (not from the code), and then caught a name of mine with
  brackets, 'DOBOT Atom (base)', now 'DOBOT Atom 153 cm' (E11.8, point 2).
- **The pages, by test:** 01's pages of types 3 and 4 had no test; the new `TestTypesThreeAndFourPages` (type 2's
  checks: readable fit to a screen, every text inside the page, none overlapping another, no project words) failed on
  type 3's table title, which ran off the page; fixed (E11.8). 02's page tests now run over types 1 to 4 (every page
  readable and inside the page; no panel title over its numbers): pass.
- **The whole suite:** 412 tests; 1 failure, the comparison of the register's builder with his register on disk (it
  holds batch 1 only after his run); 1 skipped, the check of his real register and files (types 3 and 4's files are not
  on disk yet).
- **Sandbox** (`sandbox_types34.py` in Claude's scratch folder: the register, the four parts files, 01 and 02 at 2,000
  draws, every output into the scratch folder; nothing written into the project's `data/` or `figures/`): 01 no fault;
  02 no fault, type 3 drawn over 72 robots (75 versions), type 4 over 33 (34).
  - **Types 1 and 2 unchanged, by program:** their 13 draw files each (`.npy` and `.txt`) identical to the sandbox of
    14:38 (before the entry), 26 of 26; their `summary.csv` differs in the last digits only (V108). The draws for
    stock-and-flow of all six types identical, 60 of 60 files.
  - **Remainders below zero**, measured at 20,000 draws of each type (`below_zero_34.py`, the tests' inputs, writes
    nothing): type 3 none; type 4 the 1X NEO's frame 13.46 % of its draws (E11.8), the others below 1 % (type 1's known
    ones as in type 1; the AgiBot A3 Ultra's frame 0.16 %); type 2 none. At 2,000 draws the NEO had 56 draws (14.3 %).
  - **Looked at:** 01's table of type 3 (its title cut, before the fix) and where its kinds sit; 02's notes of type 3
    (its 72 robots, the 97 not yet taken apart); type 4's figure of copper and aluminium by kind (its wheeled base and
    lift column in 24 % and 3.2 % of the draws).
  - **Size at 200,000 draws** (×100 the sandbox's): type 3's part-by-part draws about 2.3 GB, type 4's 1.4 GB.
- **Read in the code and data:** only the AgiBot A3 and A3 Ultra have magnesium (their frames), both of type 4 only, so
  type 3's magnesium recipe was taken out (E11.7 point 7). 02 uses a battery's voltage only times its capacity
  (`draw_robot`), so the 48 V (E) of a battery stated by its energy leaves its energy the stated one ± 5 %.
- **What the entry leaves behind (open point C):** `IN_RUN_ELSEWHERE` and its branch removed from the register and 01;
  a search of the code, tests, README and documents finds it only in a test that asserts it is gone and in the
  history of EVIDENCE E10.1 and V108; README's and METHODOLOGY's descriptions of it rewritten.
- **Not covered:** his runs (the register, the two new files, 01 and 02 at 200,000 draws); the DOBOT Atom's mass and
  joints and the NEO's frame wait for his word (E11.8).

### V113. What the spec of batch 1's entry (EVIDENCE E11.7) rests on, checked in the code and data

- **His words:** "Spec the entry".
- **In the code (read only):** 02's `read_apart_inputs` reads one parts file per type (`schemas.parts_path` of its
  category); its `Shared` is built once per type from that file's constants ("all"), joint parts, shares and magnet
  grades; `RECIPE_FAMILY` names types 1 and 2 only; the register's `taken_apart_as` stops where a robot stands in two
  types' files.
- **In the data (read only, by program):** no robot of the register is of types 1 and 2 both; type 1's and type 2's
  files share 13 constants of robot "all", 11 equal, 2 different under one name ("Joint modules, share of the robot
  mass" 0.245 / 0.49 / 0.735 against 0.202 / 0.404 / 0.606; "Battery energy per kg of robot" 6 / 12 / 18 against
  7.335 / 14.67 / 22.005); type 2's file alone has 5 more (the wheeled template's three, the driver board area, the
  Ethernet line). The element recipes: "Aluminium, robot type 3/4, Aluminum alloys", "Plastics, robot type 3,
  Engineering plastics", "Plastics, robot type 4, Polymers & elastomers", "Magnesium, robot type 4, Magnesium alloys"
  (and "Magnesium AZ91D", type 3's in E1.2). Batch 1 by its first type among 3 and 4: 19 and 8 robots (listed in
  E11.7); of type 3 21, of type 4 16.
- **Corrected while writing:** "163 with a mass not yet taken apart" was 178 less 27, 151.
- **Not covered:** nothing built or run.

### V112. Batch 1's proposal (EVIDENCE E11.6) at its modes

- **His words:** "Propose the numbers".
- **How:** `types34/every_joint.py` and `types34/batch1_modes.py` in Claude's scratch folder (Claude's arithmetic, not
  the model), reading his register and his type 1 and type 2 parts files (read only): which of the 68 robots of types 3
  and 4 already taken apart have every joint's module mass (by their rows in the files: shares or not, module masses
  given or the joint parts), their joint modules' share of their mass at the modes, by kind (01's `JOINT_KIND`); batch
  1's Adam Lite and SP from the wiki's actuator masses (the shoulders by E6.8's fit at 60 N·m), the Atom by E6.8's fit
  at its model's limits; the batteries' energy per kg of robot where stated (his files' voltage × capacity; batch 1's
  makers); each robot's battery, cables (8 m per metre), hub motor class (E9.6 point 4) at the modes.
- **Results:** on legs, seven of types 3 or 4 with every joint, 34.1 to 53.0 %, median 44.7 % (mean 44.8 %), split
  hips 34.2, knees 16.1, ankles 11.3, waist 8.1, arms 28.2, head 2.2 %; on wheels three, 13.2 to 14.3 %, median 13.9 %;
  energy per kg, 16 on legs: median 14.67 (10.14 to 28.07), 14 on wheels: median 10.84 (4.62 to 22.86) Wh/kg. No frame
  below zero at the modes; the least the NEO's, about 3 kg (by hand: 29.9 kg less its template joints 13.4, its two
  22-joint hands 3.2, its pack 5.1, shell 3.4, screws 0.5 and about 0.9 kg of cables, boards and sensors).
- **Not covered:** the run's draws (only the modes); the type 1 robots of types 3 and 4 whose joints follow the weighed
  joint parts (the G1, G1+), not in the template; the wheeled template's split (taken as E9.6's).

### V111. Batch 1's downloads and the wider search for weights (EVIDENCE E11.3 to E11.5)

- **His words:** "Yes, all four" (point 4: the downloads), then "Try to find more information on the weight. See if
  there is more out in the internet".
- **Downloads** (curl, each into its own new folder of Claude's scratch folder; sizes as fetched): NEURA's two
  datasheets (472 kB, 2.1 MB), Boston Dynamics' spec sheet (433 kB), the Agile Hand flyer (357 kB), Anigon's overview
  (7 kB); read with the file reader, all pages. AgiBot's manuals are online pages (read in the browser, their
  specification sections); the X2's Feishu manual loaded its contents list only (not read); the ALICE M1 URDF's link
  refused outside a signed-in session (not obtained).
- **Wider search:** twelve web searches (A2 Max, Apollo, Apollo 2, Agile One, CALVIN-40, 4NE1 Gen 4, Abi, ATOM, Billi,
  Anigon, ALPHA, Borg 01), then two web-fetch reads of the pages they named: AgiBot's A2 and A2Max URLs and its Chinese
  site; Notebookcheck; Engadget (IoT World Today refused, 403); heise in English and German; Origin of Bots (twice);
  The Next Web; Robotics Tomorrow (Waste Today empty; aiwiki.ai refused, 429; asiae.co.kr reset twice); Xinhua, 36Kr,
  Gelonghui; VentureSquare and hellot.net. A search engine's summary was used only to find pages: its "175 cm, 85 kg"
  for the A2 Max was on no page read, and is not reported as found.
- **Found:** the A2's own page states 69 kg (the first read had missed the page); the Gen 3.5's datasheet 80 kg; the
  Gen 3's 80 kg; the Gen 4's own page contradicts itself (80 kg against 20 % lighter): E11.5, question 5.
- **Not covered:** the press figures' own sources (none named); the X2's manuals; the ALICE M1 URDF.

### V110. His runs of 14:44 read back: the register with four sheets, 01, 02

- **Times:** the register 14:44:20 (sheets About, Robots, Type 1 to Type 4), 01's pages 14:44:32 to 14:44:34, 02 from
  14:44:54 to 14:55:40. 02's outputs all rewritten: `data/consolidated/` 72 of 72, `data/parts_taken_apart/` 28 of 28,
  `figures/composition/` 19 of 19, `figures/parts_taken_apart/` 48 of 48 (no older file left, V106).
- **01:** its overview 2 as V108's sandbox (looked at): type 2's card, types 3 and 4's, the open line.
- **02, for stock-and-flow, 200,000 draws:** type 2 84.3 kg at the mean (95 %: 37.8 to 230.1), as V104; type 3 72.9
  (70.8 to 75.0) and type 4 69.3 (67.0 to 71.7), from the workbook.
- **Not covered:** his console; the pages one by one.

### V109. Types 3 and 4, batch 1's sources (EVIDENCE E11): read first-hand

- **His words:** "Yes, start sources".
- **Which robots:** the register's robots of type 3 or 4 with a mass and no rows of their own (178, by program from
  his register of 14:44), the first 27 in its order: 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 17, 18, 22, 26, 28, 29,
  31, 32, 33, 43, 45, 46, 51, 56, 58.
- **How:** six web-fetch reads (the catalogue page for the maker's link, then the maker's own pages; no PDF and no
  download opened), and myself in the built-in browser where they got no text: PNDbotics' site (its pages words only)
  and its wiki (the Adam line's table, its joints' actuators, the actuators' pages), NEUBILITY, AeiROBOT (refused to
  the fetch with 403, read in the browser). TeknTrash's site refused both. PNDbotics' models `adam_lite.urdf` and
  `adam_sp.urdf` read through GitHub's raw files in the page: their links' masses summed (58.48 and 60.25 kg) and the
  limits of their moving joints listed, by script (Claude's arithmetic). DOBOT's `atom_p3.urdf`: its links' masses as
  the read reported them, summed by hand to 61.82 kg, as E7.1's 61.81 kg.
- **Against what:** each figure in E11.1 is the maker's words as read, with its page; the catalogue's figures are
  named second-hand where they are given. Conflicts named in the table (4NE1 Gen 4's mass, Adam Lite's height, the
  catalogue's DoF and runtimes against AlphaBot 2's and AEON's makers').
- **Not covered:** the PDFs and downloads (E11.2 point 4, his word); AgiBot's Chinese product pages; the other news
  pages of Hexagon; whether the catalogue's A2 and A2 Max are AgiBot's A2 Ultra and A2 Lite (not stated anywhere read).

### V108. The register's sheets Type 3 and Type 4 built (EVIDENCE E10.1, "Yes, build it")

- **His words:** "Yes, build it" (E10.1's points 1 to 8, open point A as recommended).
- **Tests first** (each failing before its code, 5 of them: an unknown constant, an unknown function, the old
  wording, the old count): `tests/test_make_humanoid_register.py` `test_the_sheets_type_3_and_type_4` (181 and 135
  robots in the register's order; type 3: 47 "its own parts in type 2", 4 "in type 1", 12 "no mass stated", 118
  from the workbook; type 4: 11, 6, 4, 114; 01's check finds nothing; `types_taken_apart` still 1 and 2);
  `tests/test_schemas.py` `test_a_robot_with_its_own_parts_in_another_of_its_types`,
  `test_a_robot_without_a_mass_is_not_drawn_while_its_type_is_drawn_from_the_workbook`,
  `test_its_card_and_its_words_on_the_overview_count_only_the_robots_with_a_mass` (type 2's card naming the Xialan
  S0, types 3 and 4's, type 5's as before, the input box's words), type 2's table title "all its 96 robots with a
  mass"; `tests/test_parts_taken_apart.py` 02's title "Robot type 2, all its 96 robots" and its count of the robots
  with a mass, 96 (it held 97: changed to the agreed rule, point 4).
- **After:** the whole suite, 399 tests; 398 pass. The one that fails compares the register's builder with his
  register on disk (2 sheets there, 4 now), until he reruns it.
- **Sandbox** (scratch, 2,000 draws; the register, both builders, 01, 02): 01 "No fault found"; 02 reads the parts
  files of types 1 and 2 only, draws types 3 to 6 from the workbook, "02 done in 27 s". **The draws of types 3 and 4
  against the sandbox's run before the sheets** (14:07, the same seed), by program: all 11 files of each identical.
  Types 1 and 2: every `.npy` and `.txt` identical; their `summary.csv` differ in the 16th significant digit (e.g.
  0.21402169130393084 against …087), and **two runs of the same code differ the same way** (31 and 25 lines): the
  summary's last digits vary from run to run (floating-point sums in an order that changes between runs), not from
  this change. Reported, not changed.
- **Looked at:** 01's overview 2 (type 2's card with the Xialan S0 not in the evaluation; types 3 and 4 "Its 181
  robots of the register listed, 169 with a mass; drawn from the workbook until they are taken apart", 135 and 131;
  the open line "Open: robot types 3 and 4 together, then 5 and 6; then the six compared.").
- **Not covered:** his runs; the other pages one by one; why the summaries' last digits vary (seen, not investigated).

### V107. What the spec of types 3 and 4's register sheets (EVIDENCE E10.1) rests on, checked in the data and code

- **His words:** "Can we move to type 3 and 4 together?", "Yes, together".
- **In the register** (`data/researched/humanoid_register.xlsx` of his run of 11:52, its sheet Robots, by program):
  type 3 181 robots, 169 with a mass (forms: wheels 76, legs 46, not stated 40, no wheels named 11, legs or wheels 7,
  four arms 1); type 4 135, 131 with a mass (wheels 44, not stated 43, legs 36, no wheels named 8, legs or wheels 3, a
  ball 1); of both 58; together 258. Taken apart already ("Taken apart as" filled): 68 (type 3 51, type 4 17); by
  types: 3 alone 63, 4 alone 60, 3 and 4 58, 2 and 3 47, 2 and 4 11, 3 and 5 8, 1 and 4 6, 1 and 3 4, 3 and 6 1; still
  to do 190, 178 with a mass, 12 without. Its sheets: About, Robots, Type 1, Type 2.
- **In the code (read only):** `tools/make_humanoid_register.py` writes the sheets of `TYPES_LISTED = (1, 2)`; a
  sheet's row is the robot's row of Robots, its "Taken apart as" included (`taken_apart_as()`, any type's file;
  a robot in two types' files stops the building); `in_the_run()` gives "drawn: its own parts" only for the robots of
  the type's own `TAKEN_APART`, else, while none of the type is, "not drawn: its type drawn from the workbook, none of
  its robots taken apart yet". `01_schemas.py` `types_taken_apart()` and `02_composition.py` `run()` take a type as
  taken apart when any robot of its sheet has "Taken apart as" filled, and then read its parts file
  (`parts_path()`); 01's `check_type_sheet()` counts a robot as taken apart only where all its versions are in the
  type's own file.
- **Not covered:** nothing built or run; the 190 robots' sources.

### V106. The leftovers removed ("Remove leftoveres")

- **His words:** "Remove leftoveres" (the three lists waiting for his word: C's leftovers, HANDOVER "Left behind once
  he has run them"; type 2's two former 01 pages, V85 and V94; the shared lists' backup, E9.7 open point D).
- **Before removing, each checked:** all 44 files on disk with the dates their lists give (2026-10-26 15:27 the backup;
  2026-10-29 16:38 to 16:39 type 1's old file and outputs; 2026-10-30 04:42 type 2's two pages); none tracked by git;
  no code of this repository reads any of them (01 writes `<n>_<name>_shared_lists.png` only for a type still drawn by
  its former pages, and did not rewrite type 2's in his runs of 11:53 and 13:50); no other repository in the GitHub
  folder names RAWCLICHumanoidRobots in its code; the old `figures/parts_taken_apart/sources/` held only the 18 files
  listed.
- **Removed, each by its exact name** (no pattern): `data/researched/parts_taken_apart.xlsx`,
  `data/researched/shared_lists_before_wheels_2026-10-30.xlsx`; in `data/parts_taken_apart/` elements, estimated,
  grades, materials, parts, robots (.npy and .txt each), register.txt, summary.csv; in `figures/parts_taken_apart/`
  robot_type_1_elements_1 and _2, robot_type_1_notes_1, robot_type_1_overview_1 to _5 (.png) and the 18 files of
  `sources/` (then the empty folder); in `figures/schemas/categories/` 2_full_scale_general_purpose_ai_research.png and
  2_full_scale_general_purpose_ai_research_shared_lists.png. 44 files, none left; what remains in those folders is
  the types' own folders and 01's current pages.
- **Not covered:** nothing else was looked for; the shared lists themselves are unchanged (V101).

### V105. The panels' numbers above their titles ("Yes, fix it")

- **His words:** "Yes, fix it" (V104's finding 1: on the material pages the titles of the magnets' grade classes ran
  into their "mean …").
- **The cause:** `02_composition.py` `element_panel`, which draws every panel of the element and material pages:
  its numbers were the panel's right title, on the same line as its title (left); a long title reached them.
  Matplotlib's title pad moves all of a panel's titles together, so the numbers now have an offset of their own
  above the panel: the title's pad, its lines at 1.2 times its size, the numbers' descent and 2 points
  (`PANEL_NUMBERS_GAP`).
- **Test first:** `tests/test_parts_taken_apart.py` `test_no_panel_title_runs_into_its_numbers` (every element and
  material page of types 1 and 2 at 300 draws: no panel's title box overlaps its numbers' box): failed on the old
  layout (type 1's "Nickel strips, battery"), and on a first fix that used the title's pad (which moved the title too);
  passes on the second.
- **After:** the whole suite, 395 tests, all pass (type 2's file equal to his of 13:50, V104).
- **Looked at** (sandbox, scratch, 2,000 draws): type 2's materials page 1 of 3 (the magnets' four grade classes clear
  of their numbers; "in 68 % of the draws" and the two lines under it above "Magnets, grade class H") and type 1's
  elements page 1 of 4 (short titles, the numbers above them as on the material pages); no text over another, the
  numbers clear of the row above's axis label. The bars are a little lower: the tight layout gives the numbers their
  line.
- **Not covered:** his pages on disk keep the old layout until he reruns 02; the other pages one by one.

### V104. His runs of 13:50 read back: type 2's builder, 01 and 02 with the robots on wheels

- **His words:** "I run 02, what is next".
- **Times** (files and the process, not his console, which Claude cannot see): type 2's parts file 13:50:17; 01's
  pages 13:50:37 to 13:50:38; 02 started 13:50:48, ended 13:56:42 (5 min 54 s). Its outputs: `data/consolidated/` 72
  of 72 files new (13:55:46 to 13:55:58), `figures/composition/` 19 of 19 (13:55:49 to 13:55:56),
  `data/parts_taken_apart/` 28 of 42 (13:55:59 to 13:56:23), `figures/parts_taken_apart/` 48 of 74 (13:56:13 to
  13:56:38). The older ones are the 40 files of 2026-10-29 at the top of the last two folders (C's leftovers, waiting
  for his word); none in a type's folder. The register and type 1's file of 11:52 equal their builders (V102).
- **His type 2 file against its builder, cell by cell:** 0 differences.
- **01:** "No fault found"; its overview: type 2 "96 of its 97 robots … Its draws for stock-and-flow from its parts",
  the open line on its last robot.
- **Type 2's draws for stock-and-flow** (`data/consolidated/2_full_scale_general_purpose_ai_research/`), from its 96
  robots: 200,000 draws, 84.3 kg at the mean (95 %: 37.8 to 230.1); Not allocated below zero in 0 draws; the materials
  add up to the total in every draw (to 1e-4).
- **Remainders below zero, all of type 2's frames and housings:** one, the Unitree R1-A5-D's battery housing in 1 of
  its 1,081 draws, by 1.6 g (its cells 1.055 kg, its management board 0.030 kg, its pack 1.084 kg in that draw; its
  housing 0.62 kg at the median), reported, not cut, as the Omni's 0.9 g in V94.
- **The CASBOT W1** in its 2,114 draws: cells 9.95 kg, pack 14.38 kg, housing 4.45 kg at the medians; its housing at
  least 0.14 kg; its pack 1.02 to 2.28 times its cells (E9.8).
- **Looked at:** type 2's notes page 1 of 3 (200,000 draws, its 96 robots, the robots drawn); its materials page 1 of
  3; type 1's materials page 1 of 3, for the fault below.
- **Found, on his pages:** (1) **On every material page with the magnets' grade classes, the panel title runs into
  its "mean …"** (type 2: "Magnets, grade class UH" into "mean 583 g", SH into "mean 710 g"; type 1's page the same, SH,
  UH, EH): the layout of the material pages, older than today's work. Not changed: his word first. (2) Type 2's
  "Nickel strips, battery" says "in 100 % of the draws": held in 99.9995 %, all but the one R1-A5-D draw of (above),
  where the housing's nickel strips are below zero; the share rounds to 100. Reported, not changed.
- **Not covered:** his console's lines; the other pages one by one (types 1 and 2, 02's and 01's).

### V103. 02 says each step while it runs ("Yes, build them")

- **His words:** "Information on the working of 02 is poor. What next", then "Yes, build them" (the seven lines
  proposed: reading, checking, each type drawn, every tenth robot, the draws checked, writing and pages, the whole
  time).
- **Found first:** 02 printed nothing while it read, checked and drew; its first line came after all the drawing. His
  run of 11:53:26 was silent for 6 min 57 s, then printed the fault. No run of his was going while this was built.
- **Tests first** (each failing before its code: an unknown function, an unknown argument, no such lines):
  `tests/test_composition.py` `test_its_steps_are_said_as_they_happen_with_their_times` (on the small files: the
  twelve lines found, in the order they run, the last "02 done in … s."), `test_a_fault_says_when_02_stopped` (the
  last line on stderr "02 stopped after … s: nothing is written."), `test_a_time_in_plain_words` (0.4 s, 12 s, 3 min
  40 s, 1 h 2 min); `tests/test_parts_taken_apart.py` `test_every_tenth_robot_is_said_as_it_is_drawn` (type 1: robots
  10, 20 and 30 of its 32, by name).
- **After:** the whole suite, 394 tests; 393 pass. The one that fails is type 2's builder against his file of 11:52
  (V102), until he reruns it.
- **Sandbox** (scratch, 2,000 draws, the CASBOT W1's LFP cells as they are): every line in order; type 1 drawn in 0.9 s
  (robots 10, 20, 30 of 32 said), type 2 in 1.2 s (robots 10 to 100 of 102), each type from the workbook in under
  0.1 s, its pages 4.1 s, each type's two figures about 7 s; "02 done in 26 s."; its results the same as V102's (type 2
  84.2 kg at the mean, 95 %: 37.7 to 229.5).
- **Deviations from the proposal, both small:** the robots are counted as the parts file holds them, versions apart
  ("robot 10 of 102", the line before saying "its 96 robots (102 with their versions)"); the line "200,000 draws per
  robot type, seed 1." now comes before the drawing, which it describes, not after it.
- **Not covered:** the times of a 200,000-draw run (his); matplotlib's warning "More than 20 figures", still printed
  between the lines (seen, not changed, as before).

### V102. The CASBOT W1's pack by the NMC packs' ratio (EVIDENCE E9.8, "Ratio, as recommended")

- **His words:** "Ratio, as recommended"; then, mid-turn, "02 is runing", ". Next steps".
- **His run of 11:52 to 12:00** (read from the files' times and the process, not his console): the register 11:52:43,
  type 1's file 11:52:53, type 2's 11:52:58, 01's pages 11:53:12; 02 started 11:53:26 and ended 12:00:23, with the code
  before this fix. No file in `data/consolidated/`, `data/parts_taken_apart/`, `figures/composition/` or
  `figures/parts_taken_apart/` is newer than 11:53 (0 files): it stopped before writing, as V101 foresaw; his outputs of
  09:51 are untouched. The fix was prepared in Claude's scratch folder while it ran and put in after it ended.
- **Tests first:** `tests/test_parts_taken_apart.py` `test_the_casbot_w1s_pack_by_the_nmc_packs_ratio` (at the modes
  the pack over its cells 241.5 / 164; its housing above zero in all its draws of 3,000) and the texts of its rows in
  `tests/test_make_parts_taken_apart.py` `test_lfp_cells_for_the_casbot_w1_only` (its cells over a cell of its recipe,
  its pack by the ratio, no other robot's text changed): both failed on the old code, both pass on the new.
- **After:** the whole suite, 390 tests; 389 pass. The one that fails compares type 2's builder with his file of
  11:52:58: by program, 3 cells differ, all the CASBOT W1's (sheet Parts, row 198 its pack's text and sources, row 199
  its cells' text); it passes once he reruns type 2's builder. The register and type 1's file equal his.
- **Sandbox with the CASBOT W1's LFP cells** (scratch, 2,000 draws; the register, both builders, 01, 02): 01 "No fault
  found"; 02 writes everything; type 2 over 96 robots, 84.2 kg at the mean (95 %: 37.7 to 229.5), Not allocated below
  zero in 0.0 % of the draws, no remainder of type 2 below zero. The CASBOT W1 in its 20 draws: its cells 10.16 kg, its
  pack 15.61 kg, its housing 5.59 kg at the medians, the housing at least 1.59 kg; the pack 1.18 to 2.00 times its cells.
- **Not covered:** his runs; the CASBOT W1 over many draws (20 here; the test's 3,000 draws hold about 30 of it).

### V101. The 43 robots on wheels entered (EVIDENCE E9.8): tests, the sandbox, the pages looked at, one fault left

- **His words:** "Spec the entry", "Yes, build it" (E9.7's points 1 to 13, open points A to D as recommended).
- **Tests:** `tests/test_make_parts_taken_apart.py` TestTypeTwoOnWheels (the 46 blocks against the register; the masses
  as agreed; drive wheels, hub classes, steering, casters and their heat groups; the lift columns, stated or a share,
  with their motors; the wheeled template's shares and split; the four with every joint; the batteries, the Reachy 2's
  stated pack; LFP cells for the CASBOT W1 only; no kind "Torso boards" left; every joint to a kind; the encoders of a
  hand or gripper, one each); `tests/test_parts_taken_apart.py` TestTypeTwoOnWheels (02: the wheeled template's
  share, the lift column's share less its motor, LFP only in the CASBOT W1's draws, the wheeled base drawn);
  `tests/test_schemas.py` (the wheeled fixtures of check 18: two templates, each alike within itself, the shared share
  on wheels needed; no drive wheel; a lift column and its motor together; type 2's table sections, base and ‡, after
  the robots on legs; the twelve kinds; the drawing with the base and the column, and without them for a type that has
  none); `tests/test_make_humanoid_register.py` (96 taken
  apart, none with a mass left). Shown failing before their code today: the encoder count (46 ≠ 48 for the AgiBot G1)
  and 01's two checks of point 7 (no fault found before the check).
- **Faults found during the build, and their fixes:** (1) 01 refused the lift column's steel 20 / 30 / 40 % as an
  estimate narrower than half to 1.5 times: 15 / 30 / 45 %. (2) 01 refused the grade "LFP cylindrical" of a cells row:
  `CELL_MATERIAL` may name its cells' recipe. (3) The AI Worker's 25 V × 80 Ah gave 2,000 Wh against its stated 2,040:
  25.5 V (the stated energy over the stated capacity). (4) 'Battery energy per kg of robot, on wheels' was labelled
  "S, E" with no source code: E. (5) 02's notes named the first template of the file for every robot: each its own.
  (6) Overlaps on the table pages (the battery ticks, the mass ticks, the key): measured widths, `T_WHEELS`. (7) The
  overview box said "from the workbook until all are" when all with a mass are in: conditioned on it. (8) A pair of
  hands or grippers counted as one joint for the encoders: one each, as batch 1. (9) 01's point 7 checks (a drive wheel;
  a lift column with its motor) were missing: built, tests first. (10) 01's "Open:" line still said type 2's "other
  robots": now its last robot, with no mass.
- **His shared lists against their backup, cell by cell** (`data/researched/shared_lists.xlsx` against
  `shared_lists_before_wheels_2026-10-30.xlsx`): the same six sheets; the sheet Lists 31 → 33 rows, the two agreed rows
  added and every other row the same, in the same order; About, Parts, Materials, Splits and Battery cells identical.
  Its time 11:00:27, unchanged by the sandbox's 01 (01 reads it only).
- **Type 1's file:** the builder's output against the file on disk differs in 173 cells, all the kind "Torso boards" →
  "Boards" (Parts 65, Boards 94, Sensors 14); no number differs.
- **After:** the whole suite, 389 tests; 386 pass. The three that fail compare the builders' output with the files on
  disk (the register, type 1's and type 2's parts files) and pass once he reruns the three builders.
- **Sandbox** (Claude's scratch folder, 2,000 draws): the register and both builders, then 01 and 02. **With the CASBOT
  W1's LFP cells, 02 stops** before writing: "robot type 2: Ni is below zero in 5 draws". Measured by
  `casbot_pack.py` (Claude's arithmetic of 02's battery steps for that robot, its own inputs): its energy 1,200 Wh, its
  LFP cells 9.93 kg (117.8 to 125.6 Wh/kg, the sheet Cells' three LFP cells), its pack 7.16 kg (the shared 164 Wh/kg of
  NMC packs), at the medians; the pack lighter than its cells in 98.0 % of the draws, so its housing is below zero.
  V99's arithmetic took every pack at 164 Wh/kg and did not compare the CASBOT W1's pack with its LFP cells: missed
  there. **With its cells made NMC in the scratch copy only:** 01 "No fault found"; 02 writes everything; type 2 drawn
  over 96 robots (the Xialan S0 not drawn, no mass), its stock-and-flow draws from its parts: 84.2 kg at the mean
  (95 %: 37.5 to 229.5), Not allocated below zero in 0.0 % of the draws; no frame of type 2 below zero. Per robot of
  type 2, the medians: copper 3.6 kg, aluminium 32 kg, Nd and Pr 437 g (V93, 53 robots: 3.4 kg, 25 kg, 447 g).
- **Looked at:** 01's overview 2 (type 2's box and the open line), type 2's table pages 5, 6 and 7 (the sections on
  wheels, the base column, ‡, no overlap), its robot page (the base F and the column G beside the feet, twelve kinds);
  02's type 2 page "where the critical materials sit" 1 of 5 and its elements page 1 of 2 (twelve kinds in the legend).
- **Not covered:** his runs; the CASBOT W1's pack (open, his word); type 2's table pages 1 to 4, the other pages of 02
  one by one; the materials of a hub motor taken as a geared joint's (stated in E9.6).

### V100. What the spec of the wheeled entry (EVIDENCE E9.7) rests on, checked in the code and data

- **His words:** "Spec the entry".
- **Checked in the code (read only):** 02 takes a type's draws for stock-and-flow from its parts once its robots with a
  mass not yet taken apart (`later`) are none (`02_composition.py`, the type loop and `taken_apart_notes`); one cell recipe
  for every robot taken apart (`CELL_RECIPE = 'NMC cylindrical'`); the battery rows written to the body region "Torso"
  (`tools/parts_taken_apart.py`, `robot_rows`); joints to kinds by name (`01_schemas.py` `JOINT_KIND`).
- **Checked in the data (read only):** type 2's sheet MagnetGrades: the heat groups Knees, Hips, Waist, Ankles,
  Shoulders, Elbows and wrists with their grade classes (Hips SH 0.5, UH 0.4, EH 0.1; Waist SH 0.6, UH 0.4); the kind name
  "Torso boards" in 173 cells of type 1's parts file and 326 of type 2's; in the code: 01 1, 02 1, the shared machinery
  6, type 1's builder 66, type 2's 44, the tests 5.
- **Not covered:** nothing built.

### V99. The proposal of the 43 robots on wheels (EVIDENCE E9.6) at its modes, and the table against the script

- **His words:** "Propose the numbers".
- **How:** `wheeled_modes.py` in Claude's scratch folder (Claude's arithmetic, not the model): E6.8's fit at the torques
  of the Vega's and RB-Y1's models (by script from the files of V95) and of the W-Bot's page; the makers' module masses
  (ROBOTIS's seven actuators, read on their e-manual pages; Pollen's Orbita); the template's share as the four's mean;
  the hub motor of each base by the robot's mass per driven wheel; the packs at 164 Wh per kg; the shell 11.5 % and the
  screws 0.5 kg; the frame before cables, boards and sensors the rest.
- **Results:** the four with every joint: Vega 17.83 kg (13.2 %), RB-Y1 A 18.17 kg (13.9 %), AI Worker 12.87 kg
  (14.3 %), Reachy 2 10.45 kg (20.9 %); mean 15.6 %, median 14.1 %; their split waist 20.5, shoulders 38.3, elbows and
  wrists 33.6, head 7.6 % (sum 100 %). Battery energy per kg of the 12: median 10.28, least 4.62, most 22.86 without the
  W-Bot (40.0). No frame below zero at the modes; least the AI Worker's 23.5 %.
- **The table against the script, by program:** 46 rows (43 robots, three in two versions), in the same order; each
  base's hub motor class, each battery's energy and each lift's mass equal the script's. **A fault it found first:**
  five rows written by hand with the wrong hub class (AGIBOT G1, Y1, YMBot D2: 8.5 kg instead of 3.75; Dual-Arm Lift:
  8.5 instead of 4.85; Astribot S1 a leftover); corrected, then 0 differences.
- **Not covered:** the run's draws (only the modes); cables, boards and sensors in the remainder (they take 1 to 3 kg,
  as in E8.3); the bases' material, which no source settles beyond the makers' words.

### V98. The sources of the wheeled base's parts (EVIDENCE E9.5): read first-hand

- **His words:** "Yes, start sources" (E9.4 points 5, 6, 7 and 10).
- **How:** four web-fetch reads of makers' pages (ROBOTIS's e-manual, ZLTECH's and UU Motor's hub motors, Oriental
  Motor's and Phoenix Mecano's lifting columns, Pollen's base pages), Tente's two castor pages in the built-in browser
  myself (the weight from the page's data; the cookie banner declined, "click here" not to agree), the three model
  files by script, the project's own cell sheet (`element_recipes.xlsx`, sheet Cells, read only).
- **Agreement between sources:** the Vega's driven wheels (3.7 kg) and the AI Worker's drive links (3.80 kg) in their
  makers' models fall in ZLTECH's 8" hub motors (3.40 to 3.725 kg); the Vega's casters (0.2, 0.3 kg) in Tente's 75 mm
  castors (0.18, 0.27 kg).
- **Refused or failed, not substituted:** RS, Fallshaw (403), Distrelec (empty); Honpine's steering hub motor (404);
  Pollen's blog (403); Ewellix's LIFTKIT (now a redirect to Schaeffler, not followed). Conflicts on the makers' pages
  named in E9.5 (ZLTECH's weights and voltages, UU Motor's torques, Phoenix Mecano's stroke).
- **Not opened:** two PDFs found (Oriental Motor's EL manual, RK Rose+Krieger's PowerLift catalogue).
- **Not covered:** a steering drive unit's datasheet, castors for heavy bases, a robot lift column of 300 to 900 mm
  other than the AI Worker's model, any ballast.

### V97. What the spec of the wheeled kinds of part (EVIDENCE E9.4) rests on, checked in the code and data

- **His words:** "Spec the wheeled parts".
- **Checked:** the ten kinds of part in `01_schemas.py` (`KINDS`, `KIND_HOLDS`) and their placing in `02_composition.py`
  (`KIND_PART_GROUP`, `KIND_BODY_REGION`); the shared block of a robot in `tools/parts_taken_apart.py` (`block()`, the
  parts sheet's columns: kind and body region per row); the shared lists' sheet Lists (read only): no body region for a
  base, no part group for wheels; the car sensor list's sheet Sensor Details (read only): 61 types, among them
  "ultrasonic sensor"; the wheel and base links of the three model files (V95's): AI Worker drive links 3.80 kg and
  steering links 0.76 kg each, base 35.99 kg, lift 17.9 kg; RB-Y1 wheels 1.378 kg each, base 60.08 kg; Vega driven
  wheels 3.7 kg, steering 0.358 kg, casters 0.2 and 0.3 kg, base 88.43 kg.
- **The battery energy per kg of robot** of the 12 wheeled robots whose makers state an energy (E9.1; the R1 Pro by the
  R1's guide, the RB-Y1 as its A, the TIAGo Pro one battery): 4.6 (CASBOT W1) to 40.0 Wh/kg (W-Bot), median 10.3.
- **Not covered:** nothing built; the numbers of points 5, 6, 10 and 11 wait for sources and a proposal.

### V96. The makers' datasheets read (EVIDENCE E9.3), on "Yes, all five"

- **His words:** "Yes, all five" (E9.2: point 4, the six makers' PDF datasheets, read only).
- **How:** each downloaded with its status, size and type reported, into its own new folder in Claude's scratch folder;
  the PDFs read first-hand page by page (text and the page pictures). Four are PDFs (ARI 5 pages, TIAGo Pro 2, Vega 1
  Pro 1, Feather 2; their SHA-256 in the scratch folder); Reachy 2's two answered HTTP 404 "Page not found"; the AI
  Worker drawing's link answered a ROBOTIS download page, not a PDF. The three that are not PDFs were removed from the
  scratch folder by exact name; none was read beyond its title.
- **Found:** PAL states two masses for the TIAGo Pro: 80 kg in its datasheet (4 hours, a second battery an upgrade),
  95 kg in its documentation (2 × 36 V 20 Ah, 8 to 10 hours). "Yes, all five" took 95 kg from the documentation alone;
  brought to him the same day (E9.3). ARI's datasheet gives arms of 5 DoF (the docs: 4) and no mass. Vega's and
  Feather's sheets repeat their pages; Vega states no battery.
- **Not covered:** Reachy 2's battery (not stated anywhere read); the AI Worker drawing.

### V95. The source table of type 2's 43 robots on wheels (EVIDENCE E9): read first-hand, checked against the register

- **His words:** "Yes, start sources".
- **How:** the register's sheet Type 2 read: 44 robots not yet taken apart, 43 of them on wheels (the 44th, Xialan S0,
  has no mass and waits for his word). Each maker's own page read first-hand: seven web-fetch reads (HTML only), and in
  the built-in browser myself where those got no text (AgiBot's G2 manual, W-Bot, MagicBot D1, R1 Pro, Mantis Standard,
  YMBot, Astribot). Search results only pointed to pages; none of their summaries is used as a source.
- **Model files**, fetched through GitHub's interface into Claude's scratch folder and read by script (masses summed,
  joint limits listed): `ffw_sg2.xml` (AI Worker) 94.42 kg; `model_v1.2.urdf` (RB-Y1 A) 132.22 kg, against the maker's
  131 kg; `vega_1p.urdf` (Vega 1 Pro) 141.00 kg, against the maker's 135 kg. PAL's and Pollen's models are xacro, not
  expanded.
- **Checked:** E9.1 holds exactly the register's 43 wheeled robots (by script: none missing, none extra).
- **Found against the register** (E9.2 point 1): the makers' masses of G2 Genie (185 kg, register 55), R1 Pro (126, 96),
  R1-D (30 or 32, 52), TIAGo Pro (95, 80), Honda Avatar (110, 101); A2-W no longer on AgiBot's sites.
- **Not opened:** every PDF (E9.2 point 4, for his word). The fetch tool saved PAL's two datasheet PDFs to its own folder
  unasked; they were not opened. RB-Y1's torque table in its web manual came back only as the fetch tool's summary, not
  as text: not used (its model file's limits are).
- **Not covered:** the robots no maker's source describes (12, E9.2 point 3); second-hand figures (CUE7, Mantis) are
  named as such, not used.

### V94. His runs of 09:49 read back: the register, type 2's builder, 01 and 02 with batch 2b

- **His words:** "02 run is done. What is next".
- **Times:** commit 60491dd at 09:49:13, the working tree clean since, so his runs ran the committed code. The register
  09:49:30, type 2's parts file 09:49:41, 01's pages 09:49:55 to 09:49:57, 02's outputs 09:51:09 to 09:51:59
  (`data/consolidated/`, `data/parts_taken_apart/<n>_<name>/`, `figures/composition/`,
  `figures/parts_taken_apart/<n>_<name>/`). Older in `figures/schemas/categories/`: only type 2's two former pages
  (`2_full_scale_general_purpose_ai_research.png`, `…_shared_lists.png`, 04:42), left behind as V85 says, waiting
  for his word; the third, `…_robot.png`, is now 01's page of type 2's robots.
- **The files on disk equal the builders':** the register, type 1's and type 2's parts files, cell for cell (the two
  tests that failed until his runs, V93, now pass).
- **01:** "No fault found in the inputs"; type 2 "53 of its 97 robots of the register taken apart so far …; their
  masses 31 to 96 kg. Its draws for stock-and-flow from the workbook until all are." Its table of type 2's robots on
  four pages, "(4 of 4)" looked at: labels clear, no battery label over the cells.
- **02, type 2:** 200,000 draws over its 53 robots (`register.txt`, the 53 of the register), each drawn 3,655 to 3,923
  times (200,000 / 53 = 3,774); the three robots in two versions each version 1,811 to 1,979 times (the GR-1, the
  H2-X, the Walker Tienkung). Per robot, the medians: mass 61.0 kg (95 %: 37.7 to 86.4), copper 3.35 kg, aluminium
  25.6 kg, iron 15.5 kg, nickel 0.82 kg, Nd 0.37 kg, Pr 0.070 kg, Dy 82 g, lithium 0.096 kg, cobalt 0.14 kg: as the
  sandbox of V93 at 2,000 draws (copper 3.4 kg, aluminium 25 kg, Nd and Pr 447 g against 441 g here).
- **One remainder below zero, of 868:** the X-Humanoid Omni's battery housing, in 1 of its 3,796 draws (0.026 %),
  by 0.9 g. The housing is the pack (energy over the pack's Wh per kg) less its cells (energy over the NMC cell's Wh per
  kg) and its management board; in that draw 1.71 kg less 1.67 kg less 0.041 kg. The same tail as type 1's Booster
  K1 2 Ah (1.6 % of its draws, as in V92). Reported, not cut. The sandbox of V93 drew the Omni about 38 times and could
  not show it.
- **02, type 1:** unchanged: 25 of its 416 remainders below zero in some draw, at most the Booster K1 2 Ah's housing,
  1.6 %, as in V92. Type 2's draws for stock-and-flow from the workbook (`data/consolidated/2_…/summary.csv`).
- **Looked at:** 01's faults page and overview of the six types; type 2's last table page; 02's type 2 notes page and
  first element page (copper 3.4 kg, aluminium 26 kg at the median; the kinds of part stacked).
- **Not covered:** the other pages of this run one by one; type 1's draws against the run of 08:39 (overwritten, no copy
  kept).

### V93. Batch 2b of type 2 entered (EVIDENCE E8.4): tests first, a sandbox run, the pages looked at

- **His words:** "Spec batch 2b's entry", "Yes, build it" (points 1 to 6, open points A to C).
- **Tests first** (each failing before its code): `tests/test_make_parts_taken_apart.py` TestTypeTwoBatchTwoB (10: the
  template unchanged and taken as it is; the five robots' joints by their torques, the H1's knees the M107, TALOS's
  limits, the Walker Tienkung's waist; every joint named by its body part; the masses; the batteries; hands and
  grippers; cables, TALOS's Ethernet line; the Walker Tienkung's versions; the compute modules; one motion sensor where
  none is named); the register's test (53 taken apart, the 43 left all on wheels, 307, 312, 313 on wheels); 02's test
  (53 robots each as often, the three two-version robots half as often); 01's page test (53 of 97, four pages). Two
  of batch 2's tests that collected over every robot now look at batch 2's only.
- **Faults the tests and the pages found, and their fixes:** (1) 01 refused the Tien Kung 3.0's and T1's voltage of 48 V
  labelled E at one value (an estimate spans half to 1.5 times): the Tien Kung 3.0 24 / 48 / 72 V (E) as type 1's
  Booster T1, the T1's labelled "S, E" (its stated energy only split). (2) **On the sandbox's pages**: the Walker
  Tienkung's "1584 Wh" ran into its first cell, and the makers' numbers of several robots showed as a third party's.
  The second cause: batch 2b's source codes cited but not in the sheet Sources, and batch 2's two Orin NX rows naming
  no code. **Two new tests for type 2's pages, failing first**: every stated number behind the cells names a code of
  the sheet Sources (type 1 had it, type 2 not); no battery label overlaps the cells. Fixed: the codes added, the rows
  naming their codes first, 01's battery axis with room for the label (`WH_ROOM`; type 1's ticks 0, 400, 800 as before,
  computed). Both tests pass; the pages looked at again.
- **After:** the whole suite, 368 tests; 366 pass. The two that fail compare the builders' output with the files on
  disk (the register, type 2's parts file) and pass once he reruns the two builders.
- **Sandbox:** both builders and the register into Claude's scratch folder, 01's pages of type 2 and 02 whole at 2,000
  draws; type 2 over 53 robots, 43 not yet taken apart, its stock-and-flow draws from the workbook; no frame of type 2
  below zero. Per robot of type 2, the medians: copper 3.4 kg, aluminium 25 kg, Nd and Pr 447 g.
- **Looked at:** 01's four table pages of type 2 (after the fixes: labels clear, the makers' cells blue).
- **Not covered:** his runs; the other pages of 02 one by one.

### V92. His runs of 08:39 read back: the register, type 2's builder, 01 and 02 with batch 2

- **His words:** "Read back 02 first".
- **Times:** the register 08:39:08, type 2's parts file 08:39:16, 01's pages 08:39:25 to 08:39:26, 02's outputs
  08:39:59 to 08:40:48 (`data/consolidated/`, `data/parts_taken_apart/<n>_<name>/`, `figures/composition/`,
  `figures/parts_taken_apart/<n>_<name>/`): every file of the per-type folders is of this run. Older: only C's
  leftovers at the former paths (`data/parts_taken_apart/*.npy`, `.txt`, `summary.csv`; `figures/parts_taken_apart/
  robot_type_1_*.png` and `sources/`), of 2026-10-29 16:39, waiting for his word.
- **The files on disk equal the builders':** the register, type 1's and type 2's parts files, cell for cell (the
  three tests that failed until his runs now pass).
- **01:** "No fault found in the inputs"; type 2 "29 of its 97 robots of the register taken apart so far …; their
  masses 44 to 86 kg. Its draws for stock-and-flow from the workbook until all are."
- **02, type 2:** 200,000 draws over its 29 robots (`register.txt`), each drawn 6,789 to 7,048 times (200,000 / 29 =
  6,897); the GR-1's versions 3,351 and 3,458 times, the H2-X's 3,593 and 3,455. No remainder below zero in any draw
  (495 remainders). Per robot, the medians: mass 64.2 kg (95 %: 44.7 to 84.7), copper 3.47 kg, aluminium 26.4 kg, iron
  16.1 kg, nickel 0.84 kg, Nd 0.39 kg, Pr 0.073 kg, Dy 86 g, lithium 0.10 kg, cobalt 0.15 kg: as the sandbox of V89
  at 2,000 draws (copper 3.5 kg, Nd and Pr 465 g, Dy 85 g). Its draws for stock-and-flow from the workbook
  (`data/consolidated/2_…/summary.csv`: titanium, steel not yet in the elements, as before).
- **02, type 1:** remainders below zero in a few draws, as before (at most the Booster K1 2 Ah's housing, 1.6 %; the
  PrimeBOT Q1's frame 0.37 %): reported, not cut.
- **Looked at:** 01's overview pages; type 2's first element page (the medians as above, its kinds of part stacked).
- **Seen, not changed:** 01's overview box of the register says "31 of robot type 1" and not type 2's 97.
- **Not covered:** the other pages of this run one by one; type 1's draws against the run of 05:04 (its outputs
  overwritten, no copy kept).

### V91. Batch 2b's proposal (EVIDENCE E8.3): its numbers at the modes

- **His words:** "Propose batch 2b" (and, before it, "Yes, all six" and, of the Omni, "If 2 stay, it has to be
  included"). Only `documentation/claude/EVIDENCE.md` and this report were written; his run of 02 not touched.
- **From the models** (`batch2b_inputs.py`, Claude's scratch folder, reading the model files of V90): the joint
  modules by type 2's fit: H1 21.67 kg (its page's peaks per group, the knees the M107's 1.9 kg, its model's torso),
  Qinglong 30.11 kg (31 joints), Tien Kung 2.0 24.79 kg (30), Walker Tienkung 21.00 kg (its model's 20 and its waist
  at 180 N·m) and 24.06 kg (with its neck at 15.8 and wrists at 17.3 N·m), TALOS 26.09 kg (its 30 body joints).
  TALOS's grippers 1.094 kg each and THEMIS's hands 0.463 kg each by their models' links. A first count of THEMIS's
  right hand (0.926 kg) also caught the left, "WRIST_YAW" starting "WRIST_YAW_L": counted again, 0.463 kg each. TALOS's
  file holds `<joint>` entries inside its transmissions: only the robot's own joints read.
- **At the modes** (`batch2b_modes.py`): no frame below zero; the least the H1's, 30 % of its mass; the template's
  robots without hands or stated battery 38 %. Two sentences of the proposal corrected before showing it (14 such
  robots, not 16; the T1 states its hips', knees' and ankles' torques, not a maximum only).
- **The medians the Walker Tienkung's neck and wrists take** (17.3 and 15.8 N·m): from the seven robots' joints as
  entered (V89): wrists 19 values, median 17.3; head 13 values, median 15.8; by hand.
- **Not covered:** nothing is entered or drawn; the module sizes "2070" and "275 TOPS" read as Thor and AGX Orin are my
  reading; the scratch scripts may be emptied again (their results stand here).

### V90. Batch 2b's source table (EVIDENCE E8); the scratch scripts of V87 to V89 gone

- **His words:** "Yes, start batch 2b" (the sources of the 27 robots not on wheels, nothing changed while 02 runs).
  Only `documentation/claude/EVIDENCE.md` and this report were written, with the handover's line on the next batch
  corrected earlier (27 with a mass and the Xialan S0, not 28).
- **His run checked by its files' times only (not read back):** the register 08:39:08, type 2's parts file 08:39:16,
  01's pages of type 2 08:39:25 to 08:39:26; 02 started at about 08:39:36. So this run of 02 draws batch 2.
- **The 27 against the register:** read from `data/researched/humanoid_register.xlsx` (sheet Type 2): its robots of
  form not "wheels" and "not drawn: not yet taken apart", 27, from 216 Omni to 352 H1 (the Xialan S0 "not drawn: no
  mass stated").
- **How read:** six web-fetch reads of the makers' sites (HTML text, no PDF opened); the built-in browser where they
  got no text (Robotera's script-rendered pages, Zeroth's rate limit, Tesla's refusal, PHYBOT's splash page; Westwood's
  site down, Cloudflare 522, in both); two spec pictures read myself (Tien Kung 3.0, Walker Tienkung); nine model
  files through GitHub's interface, their links' masses summed and their moving joints' limits listed by script.
- **Checked against each other:** the Walker Tienkung's model (61.76 kg, 20 joints, peak 300 N·m) fits its "Voice &
  Vision" version (about 61 kg, 21 DoF, peak 300 N·m); the L7's 65 kg without hands plus two XHAND 1 of 1.1 kg; the
  H1's "Peak Torque Density: 189N.m/Kg" is the M107's 360 N·m over 1.9 kg (E6.3).
- **Found against the register** (E8.2's questions): three robots on wheels (Torobo, VB1-I, VB2), the Omni at 135 cm,
  five robots on no list of their makers or without a site, masses that differ.
- **Claude's scratch folder emptied again** between turns (as noted on 2026-10-30, morning): the scripts behind V87 to
  V89 (`type2_template_test.py`, `type2_template_check.py`, `knee_check.py`, `batch2_modes.py`, `sandbox_batch2.py`)
  are gone; their results stand as recorded, and the entry's checks that matter are tests in `tests/` (V89).
- **Not covered:** REEM-C's model (xacro, not expanded); the PDFs linked (TALOS's datasheet); TALOS's model is a
  user's, not PAL's.

### V89. Batch 2 of type 2 entered (EVIDENCE E7.6): tests first, a sandbox run of 01 and 02, the pages looked at

- **His words:** "Spec the entry", "Yes, build it" (points 1 to 7, open points A to D with the recommendations).
- **Before:** the whole suite, 335 tests, all passing (type 1's file on disk equal to its builder's, cell for cell).
- **Tests first** (each failing before its code): `tests/test_make_parts_taken_apart.py` TestTypeTwoBatchTwo (13: the
  template's numbers; its split recomputed from the seven robots' own rows without their hands; which robots rest on
  it; the JingChu's stated knees and the template's other rows, their shares adding up to 1 less the knees'; the four
  robots' joints by the fit at their models' torques; every joint named by its body part; masses; batteries; the H2-X's
  versions differing in PC2 only; cables; hands and grippers; one motion sensor where none is named; the compute
  modules); `tests/test_schemas.py` (01's check 18: a stated joint beside the template's other shares, a hand beside the
  whole template, shares unlike the template's, stated joints of the wrong group, shares for some joints with no
  template in the file; the pages of type 2 from the builders' output, 29 of 97 robots on two pages);
  `tests/test_make_humanoid_register.py` (29 taken apart, 67 later, the three on wheels);
  `tests/test_parts_taken_apart.py` (02: 29 robots each as often, the H2-X's and GR-1's versions half as often; the
  JingChu's knees within 2 × 1.9 to 2 × 2.1 kg, its other joints 20.2 to 60.6 % of its mass over the template's shares
  it keeps; the notes in type 2's own words).
- **After:** 355 tests; 353 pass. The two that fail compare the builders' output with the files on disk (the register,
  type 2's parts file) and pass once he reruns the two builders. Type 1's file is still equal to its builder's, cell for
  cell (point C proved).
- **Deliberate faults:** the H2-X's long name put back: the page test failed on "1.725 m" over "Unitree H2-X PC2 Intel
  Core i7", then passed again with the short name. 01's new check against four planted faults (the tests above).
- **What 01 found in the new file and was corrected:** the compute modules whose size is an estimate had ± 5 %; 01 asks
  half to 1.5 times of every estimate: widened (E7.6). Then no fault.
- **Sandbox:** both builders and the register written into Claude's scratch folder, 01's pages of type 2 drawn, and 02
  run whole at 2,000 draws with every output folder redirected there; nothing of `data/` or `figures/` touched. Type 2
  drawn over 29 robots, 67 not yet taken apart, its stock-and-flow draws from the workbook; no frame of type 2 below
  zero (type 1's PrimeBOT Q1 in 1.8 %, as before). Per robot of type 2, the medians: copper 3.5 kg, aluminium 26 kg,
  Nd and Pr 465 g, dysprosium 85 g (batch 1 alone: copper 3.9 kg, Nd and Pr 0.51 kg, V84).
- **Looked at:** 01's two table pages and the robot page of type 2; 02's notes, overview 1 and notes pages of type 2.
  Found: the H2-X's long name over its height (shortened); 02's notes saying "split as batch 1's on average" for type 2
  (now from the rows' own words; type 1's notes read "split as batch 1 on average", one word fewer than before).
- **Seen, not changed:** 02 opens more than 20 figures at once (matplotlib's warning): type 1's 26 pages did before
  this entry; type 2 now opens 21.
- **Not covered:** his runs of the register's and type 2's builders, then 01 and 02 at 200,000 draws; the other
  element and material pages of type 2 not looked at one by one.

### V88. Batch 2's proposal (EVIDENCE E7.5): its numbers at the modes, and three checks

- **His words:** "Propose batch 2". Only `documentation/claude/EVIDENCE.md` and this report were written.
- **The numbers at the modes:** `batch2_modes.py` in Claude's scratch folder, reading only the makers' model files
  (`atom_wholebody.urdf`, `biped_s56.urdf`, `HU_L04_01.urdf`, `MAGICBOT.urdf`): each joint's module by type 2's fit,
  the template's 40.4 % and 14.67 Wh/kg (E7.4), the pack at 164 Wh/kg, shell 11.5 %, screws 0.5 kg × mass / 35 kg, the
  frame the remainder. No remainder below zero; the least the MagicBot's, 27 % of its mass. The JingChu's row by hand:
  26.26 − 3.70 + 4.0 = 26.56 kg of modules, the frame 23.3 kg.
- **The JingChu's stated knees against the template** (`knee_check.py`): the knees' share of the modules over E7.4's
  seven robots, 11.8 to 17.5 %, mean 14.1 %; the template gives its knees 1.85 kg each against the stated 2 kg (0.92).
  A first pass read the Kuavo-5's knees as none: its model names them `leg_l4_joint`, `leg_r4_joint` (280 N·m);
  counted by name, rerun. **For the entry:** the Kuavo-5's and the Atom's joints must be named by their place in the
  chain, or `average_joints()` will not find their groups.
- **The MagicBot's hands:** `MAGICBOT_with_hand.urdf` against `MAGICBOT.urdf`: 24 links only in the first, 1.178 kg;
  the first sums to 66.19 kg, the second to 66.40 kg (the second holds fixed hand links the first replaces).
- **Cables, boards and sensors, from his run of 02** (`data/parts_taken_apart/2_full_scale_general_purpose_ai_research/`,
  written 05:03 to 05:04; the first 20,000 draws, each robot's draws where it was drawn): the medians of the three
  added, H2 1.23, H1-2 1.42, GR-2 1.57, GR-1 1.31 kg. A sentence of E7.5 first said "about 2 kg", unchecked; corrected
  to these.
- **Not covered:** nothing is entered or drawn; the Orin-sized modules where a maker names only TOPS are my reading;
  the run of 02 itself is not yet read back (its figures and summary).

### V87. The test of a template from type 2's own robots against type 1's (EVIDENCE E7.4)

- **His words:** "for 6 test, if you can develop a method just using 2 data and see if it is different than 1 model",
  then "Yes, build the test". Only `documentation/claude/EVIDENCE.md` and this report were written.
- **How:** a script in Claude's scratch folder (`type2_template_test.py`, and `type2_template_check.py` for the check
  below), run with the project's `.venv` (scipy 1.18.1). It reads, never writes, both parts files (type 1's of 04:41,
  type 2's of 05:03) and five of the makers' model files fetched through GitHub (`biped_s56.urdf`, `HU_L04_01.urdf`,
  `MAGICBOT.urdf`, `atom_wholebody.urdf`, `atom_p3.urdf`). A two-sided Mann–Whitney test (no distribution assumed),
  different if p < 0.05.
- **Against the agreed numbers:** the script reproduces E5.17's type 1 inputs, 49.3 % (36.3 to 53.0 %) and 12.3 Wh/kg
  (6.85 to 21.3), and E5.12's joint masses for eight of its nine robots; the ninth, the RP1, 18.77 kg against the
  table's 19.2, is the difference E5.20 already gives (the RMM8463-2E at its mode 0.7 kg, not its bound 0.8). Type 2's
  batch 1 against E6.8's table: H1-2 28.3, GR-2 22.2, GR-1 18.3 kg the same; the H2 31.3 kg against "31.1" (E6.8's
  rounding of 8 × 1.93; summed by hand joint by joint, 31.31 kg).
- **Result:** the joint modules' share differs (type 2 40.4 %, type 1 49.3 %, p = 0.008); the large joints' share of
  the modules (90.0 against 65.9 %, p = 0.055) and the battery's Wh per kg (14.7 against 12.3, p = 0.25) do not.
- **Checked, a deliberate change of method:** type 1's four robots estimated at 87.3 N·m/kg recomputed by type 2's fit:
  type 1 still 49.3 %, p = 0.008; so the difference is not the method. Type 1's five robots with stated or weighed
  joints alone: 48.0 % against 40.4 %, p = 0.11, too few robots for the test to settle.
- **Not covered:** type 2's joint masses are the fit's, none stated but the M107 (the makers' modules of E7.2 lie at
  0.60 to 1.38 times the fit); seven type 2 robots for (a), so a difference of a few points would not be found; the
  Atom Max left out (a placeholder torque at its waist). Nothing entered: E7.4's proposal waits for Matthias.

### V86. Batch 2's source table (EVIDENCE E7): its robots, its arithmetic, the joint modules against the fit

- **His words:** "Yes, start batch 2": the first 27 of type 2's 55 robots not on wheels, sources only, nothing changed
  while his run of 02 goes. Only `documentation/claude/EVIDENCE.md` and this report were written; no code, data or
  figure.
- **The robots against the register:** the 27 numbers, names, heights and masses of E7.1 read from
  `data/researched/humanoid_register.xlsx` (sheet Type 2, read only) and the catalogue's rows from
  `data/raw/humanoid_guide_2026-10-28.xlsx`. By script: the sheet holds 97 robots, 37 of form "wheels" and 5 drawn
  from their own parts; of the other 55, in the sheet's order, the first 27 are E7.1's, number for number (the 28th is
  216 Omni). Where a maker's figure differs, E7.1 marks it bold and question 2 or 3 of E7.3 lists it.
- **Arithmetic** (by hand, then by script): the batteries' energies, voltage × capacity: IGRIS-C 48 × 17 = 816 Wh,
  JingChu 48 × 20 = 960 Wh, LUS2 54 × 10 = 540 Wh, Oli 14 × 3.6 × 9.5 = 479 Wh (58.8 V / 4.2 V = 14 cells), Luna 14 ×
  3.6 × 20 = 1,008 Wh, H2-X 1,152 Wh / 20 Ah = 57.6 V = 16 × 3.6 V (67.2 V / 4.2 V = 16 cells), as stated.
- **The joint modules against type 2's fit** (E7.2): 0.0689 × torque^0.566 computed for each of the eight rotary
  modules; mass / fit 0.60 to 1.38, all inside the band of half to 1.5 times. A check of the fit agreed in E6.8, not
  a change to it.
- **Leju's model files** (E7.1, Kuavo-5): every `biped_s50` to `biped_s56` file (and s200053, s300053) read through
  GitHub; the links' masses summed and the moving joints' effort limits listed by script; version 5.x by Leju's
  numbering rule (`docs/robot_version版本号说明.md`: "45" is version 4.5).
- **Not covered:** the second-hand figures (context only, none proposed as a value); Leju's parameters, read by eye
  from a picture (no text on the page); PAL's model files of the Kangaroo, not read; the datasheet PDF of the
  Astribot S1, not opened (a download). Nothing is entered; E7.3's six questions wait for Matthias.

## 2026-10-29

### V85. 01's pages of type 2 as type 1's; the H1-2's joint modules labelled E

- **His words:** "Why the hell do thw 01 figures of type 2 look like this the 1 look much better", then "Yes, as type
  1's". The cause, mine: `output.robot_types_with_pages` (1, 2) (point 6 of C) made 01 draw type 2 with its former
  pages of the workbook's anchor robot, the only pages it had for a type other than 1; I had not said so.
- **Tests first** (failed, then passed): 01 draws for type 2 its robots' table and where its kinds of part sit, named
  and titled for type 2 ("Robot type 2: 5 of its 97 robots taken apart so far, each drawn from its own parts"),
  readable fit to a screen (18 px at least), no text over another or off the page, no project words; the former pages
  only for a type with no parts file. Type 1's pages: the same functions, its titles as before.
- **Looked at:** both pages drawn from his files of 04:41 (type 2's parts file, the register). The table first put
  the H1-2 under "Joints whose masses are stated": I had labelled its large joint modules "S, E" for its two M107
  knees, though 25 of its 27 joints' masses come from their torques. Labelled E now (the knees' M107 still in its
  joints' rows and sources); drawn again, all five under "from their torques", and 02's notes page lists the H1-2
  among the robots resting most on estimates. A test holds it.
- **Left behind** (removed on his word only): `figures/schemas/categories/2_full_scale_general_purpose_ai_research.png`,
  `…_robot.png`, `…_shared_lists.png`, of his 01 run at 04:42; no longer drawn.
- **Not covered:** his runs of type 2's builder, 01 and 02 with the change.

### V84. C built: a parts file and builder per type, 02 drawing each type the same way, type 2's batch 1 entered

- **On his words:** "Yes, build C" (HANDOVER.md, the specification of C, points 1 to 8, with Q1 to Q4); "All 97 first"
  (Q2 kept: type 2's draws for stock-and-flow from the workbook until all its robots are taken apart).
- **His runs read back first:** 01 at 03:24 and 03:31:48, the register builder at 03:31:40 (`figures/schemas/`,
  `humanoid_register.xlsx`); 01 found no fault; then all 316 tests passed.
- **Type 1 unchanged, proved, not assumed:**
  - the builder split into `tools/parts_taken_apart.py` and `tools/1_compact_research_developer/
    make_parts_taken_apart.py` (moved by git): the file it writes equals the file the old builder wrote this morning,
    every sheet, every row, every column width (12 sheets, 0 differing);
  - 02 before and after, the same sandbox run (2,000 draws, seed 1, the real inputs and the register on disk): all 84
    draw arrays identical (`data/consolidated/` of all six types, type 1 part by part). The two `summary.csv` differ in
    the 16th digit for H and B; the new code run twice with two hash seeds differs in the same way: the order Python
    adds a set of kinds, not the change (seen before it, not changed).
- **Type 2 entered** (EVIDENCE E6.9): its file passes every check of 01 (0 faults); at the modes its joints weigh H2
  31.32, H2 Plus 32.97 (with hands), H1-2 28.30, GR-2 23.11, GR-1 19.18 kg. E6.8's table had 31.1 kg for the H2, computed
  with the power unrounded (0.5656); the builder follows the agreed formula (0.566).
- **Type 2 drawn in the sandbox** (2,000 draws, the register as the new builder writes it, in the scratch folder): five
  robots drawn part by part, the Xialan S0 not drawn (no mass), 91 not yet taken apart, its draws for stock-and-flow the
  workbook's (identical to before); no frame or battery housing below zero; copper 3.9 kg, Nd+Pr 0.51 kg, Dy 96 g, 66
  kg a robot at the mean. Its pages looked at: the notes page (1 of 2), the elements page 1 ("Robot type 2, 5 of its 97
  robots"), the overview page 4 (the head holds magnets in 80 % of the draws: the H1-2 has no head joints).
- **Found while building, and done within C:** type 2's file had no area for the small joint's driver board (type 1's
  is the G1's weighed board, in type 1's file only): one shared constant now, the G1's row the same values; the
  encoder's elements are written by the shared robot rows (type 1's file unchanged: it held them already).
- **Tests:** 323; all pass but `test_what_it_writes_equals_the_register_on_disk` (his run of the register builder); 7
  skipped where the files at the new paths are not yet on disk. New: the type 2 builder (its robots, the refit, the
  M107, the hands, the batteries, the cables, the GR-1's versions, the screws and titanium, the board area), 02's type 2
  (its robots and those not yet taken apart, each as often, its recipes, its cables' copper by hand), 01's sheets (a
  type partly taken apart, a robot taken apart that no sheet lists). These were written after the code, not before it;
  each was checked against a deliberate fault: the Ethernet line drawn as two signal conductors fails the hand test.
- **By hand, at the modes:** the GR-2's cables 14 m × (2 × 0.82 + 8 × 0.205) mm² × 8.96 g/cm³ = 411.4432 g and 62
  mated XT30 × 2.12 g × 0.35 × 0.62 = 28.52248 g, 439.96568 g, as 02 draws; my first figure, 411.4592 g, was my slip
  in the multiplication. The H2's 238.336 + 28.52248 = 266.85848 g.
- **01's overview with both types, drawn from the sandbox files and looked at:** the box "The robot types part by part"
  ran into the next box; its text shortened to three lines, drawn again, it fits. The test that checks the overview
  with the real files is skipped until the files at the new paths are on disk, so it did not catch this.
- **Not covered:** his runs (00, both builders, the register builder, 01, 02); type 2's pages at 200,000 draws.

### V83. The proposal for batch 1 of type 2 (EVIDENCE E6.8): its numbers recomputed

- **The fit:** least squares of log mass on log torque over the 12 makers' actuators with a stated mass (E2.8e's 3,
  E5.11's 8 with the QC060 and QC080 at the middle of their two stated masses, the M107; the RMM8463-2E's bound left
  out): mass = 0.0689 kg × torque^0.5656. Each stated mass against it: 0.794 (Q25H) to 1.330 (DM-J10010L-2EC), the
  M107 0.987. Type 1's fit gives 1.622 kg at 360 N·m, this one 1.925.
- **Checked on what the fit did not use:** the G1's weighed joints, small 0.525 kg against 0.426 to 0.515 kg at 25 to
  35 N·m, large 1.1 kg against 0.868 to 1.124 kg at 88 to 139 N·m.
- **The H1-2's arm torques:** its page's "Peak: About 21Kg" at its "685mm" arm: 21 × 9.81 × 0.685 = 141 N·m at the
  shoulder, near the page's 120 N·m, three times the model's 40 N·m.
- **At the modes, by hand:** actuators H2 31.08 kg (8 × 1.9 kg M107-class and the fit), H1-2 28.27, GR-2 22.19, GR-1
  18.28 kg; battery packs 972 / 164 = 5.93, 864 / 164 = 5.27, 950 / 164 = 5.79, 483 / 164 = 2.95 kg; shells 11.5 % of
  70, 71.65, 63, 52 kg; the frames' remainders about 22, 22, 26, 25 and 22 kg (H2, H2 Plus, H1-2, GR-2, GR-1), none
  below zero; the small parts (cables, connectors, boards, sensors, coolers) about 1 kg each, rounded.
- **Read for it:** Fourier's GR-1 page (support-old.fftai.com, its hands, the ASUS PN64 computer, the 46 V power and
  Ethernet line, one or two depth cameras); Fourier's hand models, 0.443 kg each (the left and the right).
- **Not covered:** nothing is entered or run; the run's own draws will differ from these modes.

### V82. 2026-10-30, morning: what is on disk, and the large joints' sources

- **His runs:** `data/researched/humanoid_register.xlsx` 2026-10-29 11:53:41, `figures/schemas/overview_1.png`
  16:39:07, `data/parts_taken_apart/summary.csv` 16:39:39; nothing in `data/` or `figures/` newer than 17:00. The
  register builder and 01 have not been run since the sheet Type 2 (`7515d13`, 17:07:47).
- **Committed and pushed:** `git status` clean, `main` = `origin/main` = `7515d13`.
- **Claude's scratch folder** is empty: yesterday's downloads and the backup of `element_recipes.xlsx` from before the
  440C rows are gone.
- **The large joints' sources** (EVIDENCE E6.7): each torque per kg recomputed from the stated torque and mass (M107
  360 / 1.9 = 189.5; J100-116P 315 / 2.93 = 107.5, as its maker's figure; Huayan 459 / 5.8 = 79.1 and 204 / 2.53 =
  80.6). Read in the built-in browser: Unitree's H1 page, Huayan's page, EngineAI's T800 page; Deep Robotics' page
  answered 404.
- **Not covered:** his runs; nothing was entered or run.

### V81. His run of 16:38 read back; the register's sheet Type 2 and the check of every type's sheet

- **Times, against the code's:** the builder 16:38:57, 01 16:39:07 to 16:39:08, 02 16:39:30 to 16:39:52; the code of
  all three committed at 16:36:53 (`bfdfdfc`). Every stage after its code: the run holds V80. My first edit after it
  (the register's sheet Type 2) is of 16:40:35, after his run had ended.
- **His results (200,000 draws):** copper (element) 2.042 kg at the mean (2.071 in V79: −29 g, the connectors'
  contacts now brass), zinc 0.245 kg (+15 g, the brass), bromine 51.2 g, neodymium 260.7 g; as V80's sandbox said
  (copper −45 g there at 3,000 draws, the rest chance).
- **The sheet Type 2** (on "commit and push and then to typ 2", then "Yes, as proposed", point A: "first the
  register's sheet Type 2"): `tools/make_humanoid_register.py` writes one sheet per type listed (1 and 2), each robot
  with its In the run; a type none of whose robots is taken apart yet says "not drawn: its type drawn from the
  workbook, none of its robots taken apart yet". 01's check of the sheet is now one check for every sheet "Type n"
  (it was for type 1 only).
- **Tests first** (failed, then passed): the builder writes 97 robots into Type 2, each "not drawn: its type drawn from
  the workbook"; 01 finds a robot missing from a type's sheet, one too many, and a wrong In the run, in type 2 as in
  type 1.
- **Tests:** 316; all pass but `test_what_it_writes_equals_the_register_on_disk`, which waits for his run of the
  register builder.
- **Not covered:** his run of the register builder and of 01 with the new sheet.

### V80. Type 1's last open parts entered: the X1 by its newer lists, the N1's switch, the XT30 a mated pair of brass

- **What, on his words:** "Yes, 1 to 5", then "Yes, enter all" (EVIDENCE.md E5.22). Downloaded on his yes, each into
  its own new folder of Claude's scratch area: `智元灵犀X1_BOM清单_20250108.xlsx` (17,678 bytes) and
  `智元灵犀X1总BOM.xlsx` (folder 20250307, 18,808 bytes), sizes checked. The connectors' masses read in LCSC's
  listings in the built-in browser (LCSC refuses automated reading); 440C from Carpenter's alloy page.
- **Tests first** (failed, then passed): the builder (the X1's screws split and its pins on their own, no row counting
  the pins twice; its inserts, shield, dampers and XT60; the N1's switch; every connector's contacts brass; every
  XT30 a pair of 1.9 / 2.12 / 2.3 g, the Asimov 2's × 38 / 35); 02 by hand at the modes: the G1's cables' copper
  102.144 g + 46 × 2.12 g × 0.35 × 0.62 = 21.16184 g + 2.24 g = 125.54584 g (152.684 g before). 01's check caught my
  own slip: the XT30 rows still labelled E, narrower than an estimate may be; labelled S, E as the table said (the
  count estimated, the mass stated).
- **The recipes file** `data/researched/element_recipes.xlsx`: a backup first (Claude's scratch folder,
  `backups/element_recipes_before_440C_2026-10-29.xlsx`), then the 8 rows of 440C (rows 290 to 297); nothing else
  changed.
- **Moved with it:** the test of a material held in some draws used the RP1's brass, now in every robot (the
  connectors' contacts); it uses the X1's 440C (in 3.5 % of the draws).
- **Sandbox** (the builder's file in Claude's scratch folder, 3,000 draws): no fault; the X1's new parts at their
  means as entered (pins 108.6 g, screws 420 g and 92 g, shafts 153 g, inserts 12.7 g, shield 20 g, dampers 8 g, XT60
  6.5 g), the N1's switch drawn; copper (element) 2.026 kg (his run 2.071), zinc +16 g, plastics −39 g; by hand the
  connectors' copper falls by about 30 g (from 1.05 g to 0.46 g a pair, about 50 pairs a robot), the rest the 3,000
  draws' chance. Looked at: materials page 2 ("Stainless steel 440C", "Stainless steel 17-4PH").
- **Tests:** 313; all pass but `test_what_it_writes_equals_the_data_file_on_disk`, which waits for his builder run.
- **Found, left out on his word** ("Leave it out"): the X1's docking terminal "对接端子2进8出" (2 in, 8 out) in its
  overall BOM.
- **Not covered:** his runs.

### V79. His run of 16:01 read back: type 1 wholly in its elements

- **Times, against the code's:** the builder 16:01:38 (its code 15:48:43), 01 16:01:50 (15:48:43), 02 16:02:11 to
  16:02:35 (15:57:42); 00 not run, its settings unchanged since 12:06:56 (`params.xlsx` 15:44:40). Every stage after
  its code: the run holds V76, V77 and V78.
- **Tests:** all 309 pass, the two reading his files included (the parts file now holds the boards' rest constants).
- **His results (200,000 draws):** every material of type 1 "Yes" in its elements, electronics 0.777 kg included;
  bromine 51.16 g, calcium 46.86 g, copper (element) 2.071 kg, lead 2.53 g, neodymium 260.7 g, dysprosium 59.8 g; 01
  found no fault. Looked at: his elements page 3 ("Bromine (Br)", median 49 g, mean 51 g).
- **Remainders below zero, accepted ("2 accept"):** 30 of 416 in some draws (27 before), the largest the Booster K1
  2 Ah's battery housing 1.59 %, the Noetix Bumi's frame 0.50 % (0.40 before: the coolers and parts now out of the
  frames), the PrimeBOT Q1's frame 0.31 %, the Sprout's frame 0.23 %. A first count of 44 was mine and wrong: it read the
  table of magnet classes that follows in the same file.
- **Not covered:** the open items of his "Yes, 1 to 5" (HANDOVER.md, 2026-10-29, evening).

### V78. His run of 15:44 read back; matplotlib's deprecated `vert` replaced

- **His run, read against the code's times:** the builder 15:44:31, 00 15:44:40, 01 15:44:45, 02 15:45:06 to
  15:45:32, 200,000 draws. It ran while 3b was being built: the builder's change for 3b came at 15:48:43, after it; before
  that only test files had changed. So it holds V76 and not 3b: the coolers, the RP1's auxiliary cells and cover
  magnets, the Sprout's sensors in `parts.txt`; lead 2.53 g; electronics 0.777 kg, "Partly"; no bromine.
- **Copper, measured:** 1.6077 kg before (his run of 14:34), 1.6248 kg now: +17.1 g. The new coolers by hand: the
  heat pipes of four robots (AKINCI-5, JAKA π, YMBOT E3, the T1), 4 of 31 × 0.1217 kg = 15.7 g, and the new fans'
  windings, about 1.3 g: 17 g. **My V76 said "about 25 g": wrong**, it counted the X1's and N1's heat pipes, which were
  there before.
- **The warning he saw:** "MatplotlibDeprecationWarning: vert: bool was deprecated in Matplotlib 3.11 and will be
  removed in 3.13" (the violins of the figures of where a material sits). `vert=False` replaced by
  `orientation='horizontal'`, the only use. Test (new): every page of 02 drawn with deprecation warnings as errors;
  failed first on this warning, then passed. The same violin drawn both ways: the same picture, pixel for pixel. 307
  of 309 tests pass; the two reading the parts file on disk wait for his builder run (3b's two constants).
- **Not covered:** his run of 3b.

### V77. Point 3b entered: the rest of the boards in glass fibre, bromine and epoxy; electronics wholly in the elements

- **What, on his words:** "Yes, enter them" (EVIDENCE.md E5.21): the rest of a board beyond its metals glass fibre 40 /
  55 / 70 % (E-glass), bromine 4.4 / 8.8 / 13.2 %, epoxy the remainder (Epoxy).
- **Built:** the builder's two shared constants; 01 requires them, checks that glass and bromine at their maxima leave
  the epoxy above zero, and that the recipes E-glass and Epoxy are in the element recipes; 02's `board()` gives a
  board's rest its glass, bromine and epoxy. **Two accounting faults found by the new test** (electronics wholly in the
  elements) and closed: a joint's encoders sit on its driver board, so their elements are in its mass (its rest is
  now its mass less them); a sensor whose mass no source states had its elements drawn and no mass booked (now its
  elements at least, its housing in the frame's remainder). After both, every robot's electronics equal their elements
  to the compounds' rounding (0.1 %); before, four robots were 0.13 to 0.17 % over.
- **Fault on a page caught by looking:** the bromine panel was titled "Br" (no name in 02's list); a test (new) that
  every element of the pages has its name, failed first, then "Bromine (Br)".
- **Tests (new):** by hand at the modes, the G1's head board's bromine = 8.8 % of (8.4 g less 20 % copper, its tantalum
  and its car metals over 15 cm2); type 1's electronics "Yes" in its elements; 01: maxima that leave no epoxy a
  fault; a missing recipe of the boards' rest a fault; every element named. 306 of 308 pass; the two that read the
  parts file on disk wait for his builder run.
- **Sandbox** (the builder's file in Claude's scratch folder, 3,000 draws): no fault; electronics 0.776 kg, in the
  elements "Yes" (0.776 kg); the boards' rest about 0.58 kg: bromine 51 g (none before), calcium 47 g (none), silicon
  +83 g, boron +7 g, carbon +158 g, each as the shares give it by hand; copper and gold unchanged within chance.
  Looked at: elements pages 1, 3 and 4. **Seen, not changed:** titanium is now in every draw (the glass's TiO2, 0 to
  0.8 %), a few grams, while the titanium parts of a few robots reach hundreds of grams: its panel is a peak near
  13 g with a long tail to 450 g.
- **Not covered:** his runs.

### V76. The pragmatic solutions built: plain words on the pages, the boards' other metals, the parts not entered, the sensors' housings

- **What, on his words:** "Can we go through the open items and decide pragmatic solutions", "2 accept, this is
  occuring in MC", "Yes build a pragmatic solution list", "Yes, build them" (HANDOVER.md, the list of 2026-10-29, late
  afternoon). Built in its order: 7, 5 and 6, 3a, 4, 3c; 3b waits on its source table.
- **7, plain words:** every page of 01 and 02 searched for the project words: found on 02's notes pages ("EVIDENCE.md
  E2 and E5", "(E5.17 point 1)", "(E5.12 point 4, E2.8e)", "(E)", "the register's sheet Type 1") and 01's faults
  pages ("(E)", "04_", "07_", "documentation/claude/EVIDENCE.md"); each put in plain words; the faults pages keep sheet
  names. One list of the words in 01 (`PROJECT_WORDS`), read by both tests: every page of 02 (new) and 01's faults
  pages (new; sheet names allowed). The overview's "02_composition.py" stays: the file he presses Run on.
- **5 and 6:** the notes page says where the part groups and body regions are rough, and that a robot of two types is
  drawn in full in each; METHODOLOGY and 02's comments the same.
- **3a:** `BOARD_METALS` adds aluminium, zinc, iron and lead from the car board file. Test by hand (new): the G1's hips'
  lead in the draws of ADC12 (its lead 0 at the mode) is its six large driver boards' 489.144 cm2 × 0.5 mg/cm2 =
  244.572 mg (failed first at 0). Lead is now in every draw (2.5 g at the mean, 1.4 g before); the tests that had lead
  and the torso boards' aluminium as held in some draws moved to vanadium and the head's indium.
- **4:** in the builder, a block's `cooler` (the G1's by default, the X1's for the AKINCI-5, JAKA π and YMBOT E3, both
  for the T1, the RP1's three fans from its BOM); the RP1's auxiliary battery cells, bearings and cover magnets; the
  Sprout's time-of-flight sensors (EVIDENCE.md E5.20, "Since entered"). Code: a part of battery cells follows the
  cells' recipe; a part of magnets names its grade class (01 checks the class and the sibling's sheet). Tests: three
  of the builder (every robot its cooler by its computer; the RP1's four parts; the Sprout's sensors), three of 01 (a
  magnet part's class passes; a wrong one, one in a joint, one missing from the traction motors' file each a fault),
  two by hand in 02 (the RP1's cover magnets 80 × 0.283 g × 24 % Nd = 5.4336 g in its frame, class N; its cells 480 /
  241.5 + 0.25 kg, all NMC).
- **3c:** a sensor with a mass is its elements (electronics) and its housing, aluminium a share of the rest, plastics
  the remainder. **Fault of mine caught by 01's check:** the share I proposed, 30 / 50 / 70 %, is narrower than his
  rule for estimates (at least half to 1.5 times the mode); entered as 25 / 50 / 75 %. Test by hand (new): the G1's
  head (its head board 8.4 g, four sensors 385 g at the modes): aluminium equals plastics, the three add up to
  0.3934 kg.
- **Sandbox** (the builder's new file in Claude's scratch folder, 3,000 draws): no fault; electronics 0.775 kg (0.815
  in his run), of it in the elements 0.196 kg (0.183); lead 2.5 g (1.4); aluminium +0.026 kg. **Checked, not assumed:**
  copper seemed unchanged (1.608 kg against his 1.608), where the coolers add about 25 g. Their parts are drawn and
  carry it (JAKA π: heat pipes 0.119 kg, its torso boards' copper 0.121 kg); the committed code (`20c2023`) on his
  file at the same 3,000 draws gives 1.590 kg, the new code 1.608 kg: +18 g, the 3,000 draws' chance (± 10 g), not a
  fault. Looked at: type 1's notes page 1, materials page 1 (the class N, in 3.1 % of the draws, median 22 g).
- **Tests:** 303; 301 pass. The two that fail read the parts file on disk (his builder run of 11:53): it lacks the new
  rows and the constant "Sensor housing, aluminium share", so 01 and 02 stop on it until he runs the builder first.
- **3b, the sources checked against each other** (EVIDENCE.md E5.21): the Danish EPA's "about 15%" TBBPA in an FR-4
  laminate against its own 0.42 kg/m2 in 1.6 mm: at 55 % glass and IPC-TM-650 2.3.16.2's densities (resin 1.37, E-glass
  2.59 g/cm3) the laminate weighs 2.96 kg/m2, so 0.42 kg is 14 %: the two agree. TBBPA's bromine by its formula
  C15H12Br4O2: 58.8 %. Not entered: his word first.
- **Not covered:** his runs; 3b's entry.

### V75. The overview's rows: the draws in which a kind of part holds the element, and in what share of the draws

- **What, on his words:** "Yes, do it", to the overview's rows of a kind of part that holds an element in only some
  draws (seen in V74: the torso boards' aluminium, median 0).
- **Built** (02, `ridge_panel`): each row the histogram of the draws in which the kind of part holds the element, its
  median, mean and 95 % lines of those draws; a third column "held in", in what share of all the draws (100 % where in
  every draw). The panels 0.38 of the page wide (0.42 before) and their columns at 1.01, 1.18 and 1.35 of the panel's
  width (`OVERVIEW_COLUMNS`), so that three columns fit; the figures of where a material sits keep their two
  (`NUMBER_COLUMNS`). The notes page of the figures says it, once.
- **Rows held in some draws** (real inputs, 3,000 draws): the waist 96 % (a robot without waist joints), the head 76
  to 83 %, the torso boards' aluminium 41 % (median 0.000022 kg, mean 0.019 kg: a trace in the board metals in some
  robots, a heat sink of aluminium in others), the cables' silver, gold, palladium and tantalum 10 %, the head's indium
  33 %.
- **Test (new):** on the five overview pages as 02 draws them, every row's median is that of the draws that hold it,
  its share is written, every number is within the page and clear of every other. The last check caught, after the
  first try, the torso boards' "0.000022" running into its mean; fixed by the wider columns. 291 tests pass.
- **Looked at:** overview pages 1, 2 and 5 (scratch folder).
- **Not covered:** his run. Committed and pushed on his word ("Commit and push"), after `946c0a5` (V69 to V74).

### V74. Elements 0 in some draws show the draws that hold them; the parts figures' footnotes once on a notes page

- **What, on his words:** "I told you I want to see the distribution not just the 0 value for vanadium and lead" (the
  rule of V72 had been applied to the material pages only, not the element pages: my fault), then, mid-turn, "parts
  taken apart show each a long legend, you know, what I think about this" (his rule: the notes once, on a page of
  their own).
- **Element panels** (02, `element_panel`, one copy for the element and the material pages): an element that is 0 in
  some draws shows the draws that hold it, their median, mean and 95 % interval, and above them in what share of all
  the draws it is held; one held in fewer than 2.5 % of the draws has no panel, as a material (`held`). On the real
  inputs, 3,000 draws: lead in 50 % of the draws (median 2.4 g), vanadium 3.5 % (16 g), arsenic 33 %, indium 33 %,
  tungsten 49 %; every other shown element in every draw; none below 2.5 %, so no panel is lost. The same on the
  element figure of `figures/parts_taken_apart/` (`stacked_panel`): indium in 33 % of the draws, median 14 mg (before:
  "median 0 mg"), the share right of its title.
- **Footnotes:** the grey footnote under each of the 7 pages of the two figures (2 element pages, 5 overview pages)
  removed, the panels given its space; its paragraphs once on `robot_type_1_notes_<k>.png`, the first pages of the
  folder (nothing cut, the repeated sentences once). The footnote's code (`figure_note`, `FIGURE_NOTE_WIDTH`,
  `FOOTNOTE`) went with it; nothing else read it.
- **A fault of mine found by the new test:** type 1's notes page in `figures/composition/` has run off its foot since
  V71/V72: its last paragraph (the material pages) was cut off the page, and I missed it when I looked. The notes now
  go on as many pages as they need (`notes_pages`: at most 26 lines a page, a paragraph never split, "(k of n)" in
  the title), wrapped at 140 characters instead of 120: two pages, `1_compact_research_developer_notes_1.png` and
  `_2.png`.
- **Tests:** three new (an element held in some draws on the element pages; the same on the element figure, indium;
  no footnote under a figure and the notes on their own pages) and one widened (every page's own texts within the
  page, on every page of 02, which caught the notes). 290 tests pass.
- **Looked at** (real inputs, 3,000 draws, Claude's scratch folder): elements 2 (lead and vanadium), the element
  figure's two pages, overview 1, both notes pages of type 1, the notes page of the figures.
- **Not covered:** his run. After it, his former `figures/composition/1_compact_research_developer_notes.png` is left
  behind (now `_notes_1.png` and `_notes_2.png`): for his word to remove. **Seen and not changed (not asked):** on the
  overview pages a row of a kind of part that holds an element in only some draws still shows the median of all the
  draws, 0 where it holds it in fewer than half (aluminium in the torso boards: median 0, mean 0.0077 kg).

### V73. 01's table of robot type 1's robots redone: range bars and where each robot's numbers come from

- **What, on his words:** "These table in 01 can be made better", "you are so cheap", then "Yes, build it" to the table
  proposed. Two pages (`categories/1_<name>_robots_<k>.png`): the robots grouped by what their joints rest on (weighed,
  from a robot taken apart: 2; masses stated: 6; from their torques: 7; a share of the robot's mass: 17), the lightest
  first within each group; the mass a bar from its min to its max with its mode a dot, on one kg axis for all (0 to 50
  kg), the mode written beside it; the joints (two encoders a joint), marked † where they are a share of the mass; the
  battery's energy at the modes a bar on one Wh axis (0 to 800 Wh), written beside it; five cells (mass, joints,
  battery, boards, frame and shell), each coloured by where the numbers of its rows in the parts file come from:
  weighed (label W), from the maker (S, its first source's "What it is" the manufacturer's or the actuators' maker's),
  from a third party (S, any other source), estimated (E). A heading band, every other row shaded, a heading for each
  group, the key once at the foot of each page, Paul Tol's "medium contrast" colours as published.
- **Decided where the specification was silent (to be told to him):** a cell whose rows rest on different bases shows
  each as a stripe, not only the weakest or the strongest; a stated number counts as its first named source's; a
  stated number naming no source would count as a third party's, never the maker's (the test finds none).
- **Reader:** 01 now keeps the column Source of the sheet Constants and the column "What it is" of the sheet Sources;
  the two places that unpack a constant (01's label check, 02's shared constants) take the new field. Nothing else
  reads the sheet Sources. The old table's words for the estimates (`ESTIMATE_KINDS` as a dict) and its page bottom
  (`ROBOTS_BOTTOM`) went with the old table; 02's notes page keeps its own words.
- **Tests (six, replacing one):** the rows (the G1: 1.32 m, 34 / 35 / 36 kg, 23 joints, 421 Wh; the E1's 480 Wh; the
  PrimeBOT Q1's 9.75 / 19.5 / 29.25 kg); the groups, their order and their order by mass, the mark on the shares group
  only; the cells of the G1, X1, T1, E1 and Q1; the label and source rule ('BT1b' read as itself, not as the maker's
  'BT1'; the actuators' maker counted as the maker); every stated number behind the cells names a source of the sheet
  Sources; the pages show every robot once and no text runs into another or off the page. **All 287 tests pass.**
- **Looked at** both pages (drawn into Claude's scratch folder, not into `figures/`). Fixed after looking: "720 Wh"
  nearly touched the first cell (the mass axis made wider, the battery axis narrower); the heading "Joints of the
  masses stated for them" reworded to "Joints whose masses are stated".
- **What the cells show, as the parts file stands:** the masses 17 from the maker, 14 from a third party (all 14 the
  catalogue humanoid.guide, "Not Verified" there), 1 estimated (the PrimeBOT Q1); the frame and shell estimated for
  all 32; the boards estimated for all but 10 robots (partly the maker's, the G1 and G1+ partly weighed); the G1's
  battery a third party's, because the teardown T1 is named before the maker's U1 in its capacity's sources.
- **Not covered:** his run of 01. The table now has two pages, so after his run his former third page
  `figures/schemas/categories/1_compact_research_developer_robots_3.png` (written 12:58 today) is left behind: for his
  word to remove.

### V72. The material pages: the draws that hold a material, the battery by its cells' chemistry

- **What:** Matthias: "If there is nothing then show nothing. If it is just a bit and a large 0 then show me the
  distribution. Give me NMC etc. for the batteries as materiel not nickel". A material held in fewer than 2.5 % of the
  draws still gets no panel; one that is 0 in some draws shows the draws that hold it (their median, mean and 95 %
  interval) and says in what share of the draws it is held; the battery cells by their recipe, "Battery cells, NMC
  (cylindrical)" (one panel per chemistry); the nickel strips named "Nickel strips, battery".
- **Tests:** a new one, the RP1's brass: the panel names its share of the draws and the median of the draws that hold
  it; the titles of the cells and the strips. 02's 54 tests pass.
- **Sandbox** (3,000 draws, the real inputs, outputs in the scratch folder): looked at materials 1 and 3: brass in 3 %
  of the draws (median 87 g), stainless 17-4PH in 4 % (149 g), titanium in 4 % (390 g), the magnet classes H 70 %, UH
  71 %, EH 21 %, the die-cast alloys A380 and ADC12 each in 50 % (one of them in a draw), the cells NMC 1.8 kg at the
  median. Fixed after looking: the strips' title ran into its numbers.
- **Not covered:** his runs; the element pages keep the draws at 0 in their panels (not asked).

### V71. 01's pages and overview by his rules, type 1's material pages, 04 into 02, pages of type 1 only

- **What, on his words:** "Yes, into 02" (04's two figures drawn by 02, 04 removed); "Type 1 only" (a setting,
  `output.robot_types_with_pages`, the robot types whose pages 01 and 02 draw; 02 still writes all six types' draws);
  "Yes, build it" (01's pages and the overview, the specification in HANDOVER.md); "S and P can go also Na" (added to
  `composition.elements_not_shown`); "Yes, 1 to 5" (type 1's material pages as RAWCLICDataCenters draws its materials:
  each material in one robot, the steels by grade, the aluminium by alloy, the magnets in all and by grade class, where
  each sits, the draws kept).
- **Read first:** RAWCLICDataCenters' "materials of one data center" (one distribution panel per material) and "where
  the copper comes from" (a violin per item on a logarithmic axis), figures and code (its 04).
- **How, tests first:** 02 keeps each material by its grade, alloy or magnet class (`Robot.detail`, the shares by
  `RecipeDraws.leaves`, the same draws its elements are drawn with); 04's code moved into 02 verbatim, its names given
  02's forms; the robot schema, the kinds of part, the hot joints and the estimate kinds moved into 01 (one copy, used
  by 01's robot page and 02's figure). New tests: the grades, alloys and magnet classes add up to their material in
  every draw (all 10 kinds); the material pages show copper, the magnets and their classes, each steel grade and each
  aluminium alloy, steel and aluminium never whole; by hand at the modes, 7075 25.6 % and 6061 54.4 % of the
  aluminium; grades.npy written with its columns; 02's figures and the sources figures written; every page of 01 and
  02 readable fit to 1920 × 1080 (18 px at least) and 01's 16 × 9 inches; no project words on 01's overview, notes and
  type 1 pages; type 1's table lists every robot of the parts file (the G1 34 / 35 / 36 kg, 23 joints, 421 Wh); the
  faults continue over pages; the setting refused when empty, repeated or outside 1 to 6; 02 draws no page for a type
  the setting does not name and still writes its draws.
- **Sandbox run** (the real inputs on disk, 01 and 02 with 3,000 draws, every output in the scratch folder): exit 0 for
  both; 01: overview_1 and _2, notes, faults_1 to _3, type 1's robots_1 to _3 and robot page; 02: type 1's notes,
  elements 1 to 4, materials 1 to 3, its two figures (7 pages), 17 "where it sits" figures; no page of types 2 to 6.
  Looked at: overview_1 (fixed: the sibling box over the legend; "a robot in two versions twice"), overview_2 (fixed:
  type 1's card, the last line), the robots table (fixed: it ran off its page; now as many rows a page as fit, 3
  pages), the robot page (fixed: each kind's name twice), materials_1 (fixed: two-line titles over the numbers),
  sources/Copper (the hip joints 428 g at the median, the arms 371 g, the cables 227 g), faults_1. Type 1: 33.8 kg at
  the mean (95 %: 17.2 to 42.7); copper 1.6 kg as metal, 2.1 kg as the element with the boards'; the magnets 972 g at
  the median.
- **Tests:** 281, all pass.
- **Not covered:** his runs of 01 and 02; the pages of types 2 to 6 keep their former drawing until their steps begin;
  the faults pages list the checks with the names of the sheets they check (to find a fault), the one page not held to
  the project-words test.

### V70. Type 304's chromium maximum corrected in RAWCLICVehicleTractionMotor's element workbook, on his word

- **What:** Matthias, 2026-10-29: "What the hell is with 304. Why did you not tell me and resolve it", then, choosing
  the answer offered: "Yes, correct it" (set Type 304's chromium maximum, sheet CastFeSteel, cell H17, from 0.02 to
  0.20, a backup first). The fault: V69.
- **How:** the workbook `RAWCLICVehicleTractionMotor/data/raw/10_MaterialElementDefinitions.xlsx` (not evicted by iCloud,
  no lock file, no charts or drawings, git-ignored there) copied first into Claude's scratch folder
  (`backups/10_MaterialElementDefinitions_before_304_Cr_2026-10-29.xlsx`); then written anew part by part, every part
  byte for byte as it was, the sheet's XML (`xl/worksheets/sheet6.xml`) with the one cell's value `0.02` as `0.2`.
- **Checked:** every part of the file but that sheet byte-identical to the backup, the sheet differing in that cell
  only; every cell of every sheet read against the backup: one differs, CastFeSteel H17, 0.02 to 0.2. Type 304 now
  0.18 to 0.20 (the standard's 18 to 20 %). RAWCLICVehicleTractionMotor's own code reads only the magnets' sheet for
  elements (its `src/params_schema.py`: "THE MAGNET ONLY, AND THAT IS A DECISION"), so none of its results change.
- **Tests on the real files:** 273; all pass but the six that compare with the register and the parts file on disk,
  which his builder runs write (they pass against files the builders write, V69). The 21 failures naming Type 304
  are gone.
- **A second sandbox run, 20,000 draws, the real files** (the register and the parts file built into the scratch folder,
  every output there): 02, 03 and 04 exit 0; 14 s, 1.0 GB at most in memory; `data/parts_taken_apart/` 106 MB (its
  parts 795 columns), `data/consolidated/` 32 MB. For his run of 200,000 draws, by the same measure: about 2 to 3
  minutes, 8 to 10 GB of memory (this Mac: 17 GB), about 1 GB into `data/parts_taken_apart/`. Type 1: 33.8 kg at the
  mean (95 %: 17.1 to 42.8). Remainders below zero (reported, not cut): the frames of the Noetix Bumi 0.6 %, Fauna
  Sprout 0.3 %, PrimeBOT Q1 0.2 %, TOPSTAR Xiao Tuo 0.2 % of their draws; the battery housings of the Booster K1 2 Ah
  0.6 %, Noetix Bumi, AgiBot QUESTER1 and Fauna Sprout 0.2 %. **Corrects V69:** the K1 2 Ah's "8.3 %" there came from
  about eight of its draws in 500.
- **Not covered:** his runs.

### V69. The entry of type 1's research: every robot of type 1 from its own rows

- **What:** on "Yes, build it" (the entry, HANDOVER.md, points 1 to 10 with the recommendations for A to D), and his
  two answers during the build ("only if it is exclude due to a limit given in the code": check 20 removed; the nickel
  strip "With Copper"): the register's TRON 2 not assigned (31 robots of type 1); the parts file's builder writes all
  32 (the K1 in its versions 5 Ah and 2 Ah), one block per robot (EVIDENCE.md E5.12 to E5.19); the columns Grade
  (JointParts, Parts) and "Share of the joint modules" (Joints); 01's new checks (joint shares, battery constants,
  alternatives 'A or B', `check_grades`, the sibling's steel sheets, the setting `data.traction_motor_steels`); 02
  draws each robot from its own rows, its versions each as often, its grades, its shares of its mass; the scaled
  drawing, check 20, `parts.draws`, `parts.seed` and the old page `figures/composition/1_compact_research_developer.png`
  removed (decisions C and D; nothing read them, grep of the code, tests and documents).
- **Read first-hand for the placements** (web-fetch tool): Menlo's mechanical system tour gives the Asimov 1's actuator
  at every joint (its "Full Actuator Specifications"; the page marks these tables as possibly outdated), entered as it
  gives them; ROBOTIS's pages give only the count of each actuator model for the AI Sapiens K1 and the K0, not where
  each sits: the placement is an estimate (E), written in its row (the larger actuators at the hips, knees, waist and,
  for the K1's eleven, the ankle pitch). The makers' model files on disk (E5.10) give the joints' torque limits of the
  Roboto Origin, RP1, T1, K1, PM01 and R1; the RP1's actuators by joint from RoboParty's ROMOMO introduction.
- **How, tests first:** the builder's 14 tests (every robot of the sheet Type 1 with rows, the K1's versions differing
  only in battery and computer, the G1+ the G1 with two head joints, the Asimov 2 the Asimov 1 times 38 / 35, the
  actuators of batch 1 at their modes as E5.12: Roboto Origin 17.6, Asimov 1 18.6, T1 14.9, K1 9.2, PM01 15.6, R1 14.6,
  AI Sapiens K1 14.5 kg, RP1 18.8 kg; the 17 robots without joint torques with shares adding up to 1; every steel and
  titanium part with its grade); 01's 19 new tests, each a planted fault (shares not adding up to 1, shares for some
  joints only, a module mass beside a share, the shared share missing; a voltage without its capacity; neither and no
  energy per kg; a pack with no mass without the pack energy per kg; a share of the robot without the shell share; a
  material 'Steel or Brass'; a steel part without a grade; a grade neither recipe nor steel; 'M19 or M99'; a grade on
  aluminium; a sibling steel whose maximum is below its minimum; the steels' sheet missing; the six tests of check
  20 removed with it); 02's 23 type 1 tests over
  the register's 31 robots (each drawn as often within 4 standard errors, the K1's versions each half of its draws,
  each robot within its mass range, materials and parts adding up to its mass, every remainder reported and none cut,
  each joint of a stated mass within its stated range, the joints of a robot without torques 24.5 to 73.5 % of it,
  'M19 or M27' and 'Aluminium or Plastics' each as often, and by hand at the modes: the G1's copper in its cables, gold
  and neodymium in its hips as before, its molybdenum in its hips from the grades 1.8396537 g, the E1's joints 19.6 kg,
  shell 4.6 kg, cells 1.987578 kg, housing 0.905651 kg).
- **Found by the new check, Matthias's data, not corrected here** (corrected on his word, V70): RAWCLICVehicleTractionMotor
  `data/raw/10_MaterialElementDefinitions.xlsx`, sheet CastFeSteel, rows 16 and 17 (Type 304): chromium 0.18 at its
  minimum (H16) and 0.02 at its maximum (H17); the standard's range is 18 to 20 % (E5.18). Until it is settled, 01 and
  02 report the fault and 02 draws nothing; the RP1's 304 pins and screws (39 g at the mode) are the only part that
  uses it.
- **Sandbox run** (the register and the parts file built by their builders into the scratch folder; the sibling's steels
  a scratch copy with H17 0.2, only to try the drawing; 02, 03 and 04 with 500 draws, every output in the scratch
  folder): exit 0 for all three. Type 1: 33.6 kg at the mean (95 %: 16.9 to 42.6), 31 robots drawn, none left out;
  steel, titanium and copper now in the elements, only the electronics in part. One remainder below zero: the Booster K1
  2 Ah's battery housing in 8.3 % of its draws (its 96 Wh pack against the template's battery management board of 30 /
  60 / 96 cm2; reported, not cut); no frame below zero. Pages looked at: the notes page (fixed after looking: it listed
  the G1 and G1+ under "joints' masses from their torques", and said iron was missing when nothing was), element pages
  1 and 2 (iron 10 kg, chromium 133 g, carbon 4.5 kg at the median), 04's element figure 1. The project's `data/` and
  `figures/` unchanged but the old page removed.
- **Tests:** 273. In the sandbox (the steels' copy) all pass but the six that read the register and the parts file on
  disk (written before the change); those six pass against files built by the builders (sandbox). As the project
  stands, 21 more fail, each naming the one fault above ("the steel 'Type 304': min and max not in order for Cr").
- **Not covered:** the real run (his); the files on disk until his builder runs; the joints' kinds of the 17 robots
  without torques (an average layout, one row per joint group); the head joints counted in the kind "Head", which 02's
  standard tables place in the part group Sensors (KIND_PART_GROUP, unchanged); fans, heat sinks, the RP1's 30 V
  battery, bearings outside its actuators and its magnets in the covers, and Sprout's four time-of-flight sensors (not
  in E5.14); a sensor whose mass no source gives is drawn by its elements only, its mass in the frame.

### V68. Hydrogen, nitrogen, oxygen and fluorine off the element pages of 02 and 03, kept in the draws

- **What:** on "Hydrogene and Oxygen have to go you should know this. Same for F, and N" and "Yes do it" (the four
  points written back): the setting `composition.elements_not_shown` ('H', 'N', 'O', 'F'); 02's type 1 element pages
  and the "By element" of types 2 to 6, and 03's `elements.png`, leave them out, with one function of 02
  (`shown_elements`) and a note on each page; the draws keep them; 02 stops on a symbol that is not an element.
- **Found before building:** the rule was set in RAWCLICStockAndFlow (`materials.battery_elements_not_of_interest`,
  N and F, 2026-10-05; oxygen out of its figures) and RAWCLICDataCenters 05 (oxygen); hydrogen is written nowhere.
- **How, tests first** (8 new tests; before the code: 5 failures and 3 errors): the setting listed and refused when a
  symbol repeats, is empty, or is not in a tuple; on the small files, fluorine in the draws and off the page, the note
  naming it, a symbol that is no element ('Ox') a fault of 02; on the real inputs, type 1 holding all four in its
  draws, its pages' panels without them and with copper, its notes page naming them; 03's elements without them, its
  materials as before.
- **Sandbox run** (the real inputs, the register on disk, 02 and 03 with 5,000 draws, every output in the scratch
  folder): exit 0 for both; type 1 as in V64 (31 robots, 34.0 kg at the mean); `elements.txt` still holds H, N, O, F;
  type 1's first element page starts with lithium; type 2's page by element without the four, its note naming them.
  The project's `figures/` unchanged.
- **All tests: 246, all pass.**
- **Not covered:** `params.xlsx` and PARAMETER_REFERENCE.md gain the setting at Matthias's next run of 00; the real run
  of 02 and 03 is his. The pages of types 2 to 6 show the mean alone and are not 16 × 9 inches (his rules of
  2026-10-28), as before: not changed.

### V67. 01's pages of Matthias's run (06:32:59 to 06:33:16), against his figure rules

- **What:** on "I am not so happy about the figures generated in 01. You know why!": the pages of `figures/schemas/`
  opened (the overview, type 1's robot page, type 3's shared-lists page) and 01's drawing code read.
- **Result, nothing changed:**
  - They do not show what the model does: type 1's pages show the workbook's anchor robot alone (the G1, 13 parts,
    35 kg, materials at the mode), the overview says one anchor robot "stands for the category"; 02 draws type 1 over
    the 31 robots of the sheet Type 1 (34.0 kg at the mean, 95 %: 17.3 to 42.7 kg in V64's sandbox).
  - Not readable by his rule of 2026-10-28 (16 × 9 inch pages, text 14 pt and up, 18 px at least on a 1920 × 1080
    screen): pages 19 inches wide and 10 to 20 inches high, text down to 8.5 pt at 150 dpi (17.7 px); type 3's
    shared-lists page (2850 × 3049 px) fit to the screen is 35 % of its size, its text about 6 px.
  - Notes and explanations at the foot of every page, not once on a page of their own.
  - Project words on the pages: "point 2 of SHARED_LISTS.md", "Point 5", "EVIDENCE.md E1.7j", "(E)", "sheet Splits",
    report file names.
  - Colours chosen by hand (`PART_COLOUR`, `MATERIAL_COLOUR`, `BAR` in 01), not Paul Tol's as published.
  - Single bars at the mode with the bounds; no median, mean or 95 % interval (01 draws nothing at random).
  - `figures/schemas/categories/3_industrial_logistics_warehousing_robot.png` still of 2026-10-27 09:41:11, the only
    page not rewritten by the run: not written by it, or replaced by iCloud's older copy; not found out.
- **Missed before:** V64 says faults.png was looked at with "nothing overflowing"; its readability by the rule above
  was not checked.

### V66. The three settings of 2026-10-28 in the test's list of settings

- **What:** on "Yes, add them": `data.humanoid_guide`, `data.register` and `composition.type_one_lowest_kg` added to
  `KEYS` in `tests/test_parameters.py`, the list every setting of the project must be in (V65's two failures).
- **How:** all tests, with `params.xlsx` and PARAMETER_REFERENCE.md as Matthias's run of 00 wrote them (05:14:33).
- **Result:** 242 tests, all pass.
- **Not covered:** `parts.draws` and `parts.seed`, which nothing reads since 02 draws type 1 (HANDOVER.md, waiting
  point 1), stay in `KEYS` while they stay in the settings.

### V65. Matthias's runs of 00 and of the register builder, read back

- **What:** on "I have run the two programs": what `00_parameters.py` and `tools/make_humanoid_register.py` wrote,
  against the commit they ran (39f51f1, 2026-10-29 05:14:28 +0100).
- **How:** the files' modification times; `params.xlsx`, PARAMETER_REFERENCE.md and the register opened; all tests.
- **Result:**
  - 00 at 05:14:33: `params.xlsx` (7,190 bytes) and PARAMETER_REFERENCE.md (5,409 bytes) hold the three settings of
    2026-10-28, `data.humanoid_guide`, `data.register` and `composition.type_one_lowest_kg`.
  - The builder at 05:15:02: `data/researched/humanoid_register.xlsx` (45,703 bytes), sheets About, Robots (354
    robots, 17 columns) and Type 1 (32 robots, 18 columns, the last "In the run"): 3 drawn with their own parts, 28 with
    the parts of the G1, X1 or N1 scaled to their mass, the PrimeBOT Q1 not drawn (no mass stated); the Booster T1 in.
  - The two tests that waited on the register on disk now run and pass: what the builder writes equals the file on
    disk sheet by sheet, cell by cell; the real register and its sheet Type 1 pass 01's checks 21 and 22.
  - **242 tests, 240 pass, 2 fail.** The 2 failing (`test_parameters`:
    `test_every_setting_is_listed_with_a_description`, `test_the_register_holds_every_setting`) do not wait on the
    run of 00, as HANDOVER.md (2026-10-28) and V64 said: they compare the settings with the test's own list `KEYS`,
    which was not given the three settings of 2026-10-28. They fail with or without 00's run. Not changed: adding
    the three to `KEYS` waits on Matthias's word.
- **Not covered:** 01 to 04 not run since (his runs).

### V64. The register's sheet Type 1: every robot of type 1 listed, and 02 drawing over it

- **What:** on "I want the all the know type 1 robots are integrated and included in the run", "There has to be an
  excel sheet where all the robots of the different types are fully listed. For now it has to be just all for type 1."
  and "Yes, build it" (points 1 to 5 as written back, the Booster T1 kept in type 1, the PrimeBOT Q1 listed and not
  drawn): the builder writes the sheet Type 1 into the register beside the sheet Robots, from the same decisions;
  01 reads it and checks it against the sheet Robots (check 22, `read_type_sheet`, `check_type_one`); 02 reads type 1's
  robots from it and stops without it.
- **Found before building:** `data/researched/humanoid_register.xlsx` was never written to disk (the builder ran only
  in the scratch folder of 2026-10-28), so 02 stops today with "the register is not there".
- **How, tests first** (14 new tests; before the code: 12 errors and 2 failures, as expected):
  - the builder on the real catalogue: the sheet lists exactly the robots of the sheet Robots whose types include 1,
    32, in the register's order, the Booster T1 (54) and the PrimeBOT Q1 (236) among them; 01's check finds nothing;
    "In the run": own parts for 102, 16 and 350, the parts of the G1, X1 or N1 scaled for 28, not drawn for 236 only;
  - 01 on a small register: read robot by robot with "In the run"; refused without the sheet; one fault each for a
    robot of type 1 missing, a robot not of type 1 listed, a robot listed twice, a cell not as in Robots (the mass
    mode), a robot without a mass said to be drawn, a robot with a mass said not to be drawn, a robot taken apart said
    to take other parts;
  - 02 on the small files: stops, writing nothing, without the sheet Type 1, and when it misses a robot of type 1.
- **Deliberate faults on the real register** (a copy in the scratch folder): the Booster T1's row removed, the G1's
  mass mode set to 40, the PrimeBOT Q1 said to be drawn with its own parts: three faults, each naming the robot.
- **Sandbox run** (the real inputs; the register built in the scratch folder; 01, then 02 with 5,000 draws, every
  output in the scratch folder): the builder 32 robots in the sheet Type 1; 01 no fault; 02 exit 0, type 1 drawn over
  31 robots of the sheet, not drawn 236 PrimeBOT Q1, 34.0 kg at the mean (95 %: 17.3 to 42.7), the X1's frame below
  zero in 0.2 % of its draws (reported, not cut): the same as V62. The sheet opened: 18 columns, the last "In the run".
  faults.png and type 1's notes page looked at: the new check and the sheet named, nothing overflowing. The project's
  `data/researched/` and `figures/` unchanged (their dates as before).
- **All tests: 242, 238 pass**; the 2 skipped on the register on disk (his run of the builder). The 2 failing were said
  here to wait on Matthias's run of 00, taken from HANDOVER.md without checking; that is wrong (V65).
- **Also changed:** three texts that said the Booster T1 "is out of type 1" (01's check 20 and `check_robot_types`,
  METHODOLOGY.md check 20) now say it is not taken apart and the register keeps it in type 1; METHODOLOGY.md's list of
  checks had stopped at 20: checks 21 (the register) and 22 (the sheet Type 1) written.
- **Not covered:** the real run (the builder, then 00 to 04) is Matthias's; the masses in the sheet are as the
  catalogue states them (second-hand, not checked against the makers); the 28 robots without their own parts are
  drawn with the parts of the G1, X1 or N1, scaled; the PrimeBOT Q1 waits on a mass estimate (E).

### V63. The handover checked against the disk, and the git folder attached on this Mac

- **What:** on the other Mac, on Matthias's "read them and follow them and als read the handover": the section
  "2026-10-28, late night" of HANDOVER.md against what is on disk; then, on "Yes, attach", the git folder attached and
  the working tree compared with GitHub.
- **How:**
  - the modification times (`stat`) of `params.xlsx`, PARAMETER_REFERENCE.md, the stages, `tools/`, `src/` and every
    file in `data/` and `figures/`;
  - the git folder: `git clone --bare` of https://github.com/MattRoess/RAWCLICHumanoidRobots.git into
    `$HOME/gitdirs/RAWCLICHumanoidRobots.git`, the path the project's `.git` pointer names, set up as
    RAWCLICDataCenters' (`core.bare` false, `core.worktree` the project folder, `origin` fetching every branch, `main`
    following `origin/main`); the index filled from `origin/main` by a mixed `git reset`, which writes no file in the
    project folder; then `git status` and `git log`.
- **Result:**
  - Before attaching, git refused: "Kein Git-Repository: /Users/rm/gitdirs/RAWCLICHumanoidRobots.git".
  - After: on `main`, the same as `origin/main` (b271afd, 2026-10-28 15:50:02 +0100), nothing to commit. The working
    tree equals GitHub, so it holds no uncommitted work; the handover's "committed and pushed to `main`" holds.
  - None of Matthias's six runs has been made, as the handover says: `params.xlsx` and PARAMETER_REFERENCE.md are of
    2026-10-27 09:41:06, while 01, 02 and `src/params_schema.py` changed on 2026-10-28 between 15:44 and 15:47;
    `data/researched/humanoid_register.xlsx` does not exist; `figures/composition/` holds only the six pages of
    2026-10-27 09:41, not type 1's notes and element pages.
  - Still on disk: `data/parts_taken_apart/` and `figures/parts_taken_apart/` of 2026-10-28 12:53, from 04 before its
    drawing moved into 02 (15:43 to 15:44); `data/consolidated/` of 2026-10-27 09:42, the run of 00 to 03, his to keep
    or remove; the old page `figures/composition/1_compact_research_developer.png` (2026-10-27 09:41:23), the
    handover's waiting point 1.
  - On this Mac the project lies at `/Users/rm/Documents/GitHub/RAWCLICHumanoidRobots` (`pwd -P`); the handover's run
    paths begin with `/Users/rm/Library/Mobile Documents/com~apple~CloudDocs/`.
- **Not covered:** the test suite was not run (the handover: 228 tests, 226 pass before run 1); whether the handover's
  `Mobile Documents` paths exist on this Mac (outside the GitHub folder, not looked at); whether iCloud evicted any
  file (`stat -f %Sf` not run); the statements of the older sections of the handover.

## 2026-10-28

### V62. Robot type 1 drawn in 02 over all its robots of the register; 04 draws its figures from 02's draws

- **What:** on "Yes in 02 it is all type 1 in.!" and "Yes, code it in 02": 04's drawing of robot type 1 taken apart
  moved into 02_composition.py unchanged but for the choice of robot and mass (METHODOLOGY.md "Robot type 1 over its
  robots, in 02"); 02 writes type 1 as every robot type (materials, elements, part groups, body regions, total) and
  type 1 taken apart for 04 (`data/parts_taken_apart/`, with `register.txt` and `estimated.npy`); every robot type now
  has the same element columns (0 where none is drawn); type 1's pages a notes page and its elements nine a page.
  04 reads 02's draws and draws only its two figures. A robot type is drawn from robots taken apart where its register
  robots include one (type 1 today), so 02's and 03's small-workbook tests run with a small register of their own.
- **How, tests first where new:** tests/test_parts_taken_apart.py rewritten against 02's `draw_type_one` over a
  register of the three robots taken apart and, where needed, a robot of 50 kg: each robot taken apart a third of the
  draws and its own mass; a robot of the register taking each robot taken apart's parts a third of the time and its
  own mass (49 to 51 kg); materials and parts adding up to the mass in every draw; remainders reported, not cut; a
  stated joint mass kept; type 1 as 02 writes it passing `draw_faults` with Not allocated 0; the hand calculations at
  the modes unchanged (the G1's cable copper 152.684 g, hip gold 10.50288 mg, hip neodymium 99.205152 g); the hip
  joints of the 50 kg robot drawn with the G1's parts 50 / 35 times the G1's (fans not scaled), its head the same;
  every page of 04 and 02's type 1 pages readable fit to 1920 × 1080 (18 px at least); 04's run from 02's written
  draws. **228 tests: 226 pass**; 2 wait on Matthias's run of 00 (the three new settings in `params.xlsx` and
  PARAMETER_REFERENCE.md), 2 are skipped until the register is built on disk (his run of the builder).
- **Sandbox run** (5,000 draws, the real inputs, the register built in Claude's scratch folder, every output there):
  exit 0 in 4.8 s; type 1 over 31 robots (not drawn: 236 PrimeBOT Q1, no mass), 34.0 kg at the mean (95 %: 17.3 to
  42.7), Not allocated 0; the X1's frame below zero in 0.2 % of its draws (reported, not cut); types 2 to 6 as before.
  The pages looked at (notes page; elements pages with the bars to about nine tenths of the panel).
- **Faults found and fixed on the way:** type 1's Not allocated first computed as the mass less the materials showed
  rounding noise as "below zero in 27.4 % of the draws" (now 0 by construction); the summary called the cells "not
  in the elements" because their recipe adds up to 1 only to the compounds' rounding (now compared at 0.1 %, as
  `draw_faults` allows; no other robot type changes).
- **Not covered:** the real run (200,000 draws) is Matthias's; steel, titanium and mixed parts are not yet in the
  elements (their iron, chromium, nickel are missing, as the notes page says); the grouping of type 1's kinds into
  part groups and body regions is by whole kinds.

### V61. The register of every known humanoid robot: its builder and 01's checks

- **What:** `tools/make_humanoid_register.py` writes `data/researched/humanoid_register.xlsx` from the catalogue
  (`data/raw/humanoid_guide_2026-10-28.xlsx`) and the decisions held in it (EVIDENCE.md E4 to E4.11, one line per
  robot); 01 reads it (`read_register`) and checks it (`check_register`): every number once; one or two different
  robot types of the six; an entry saying why where there are none (not assigned, or the same robot as an entry with
  types); every form known; masses all three or none, in order; no robot of type 1 below 15 kg; the robots taken apart
  in the parts file and of type 1. New settings: `data.humanoid_guide`, `data.register`,
  `composition.type_one_lowest_kg` (15 kg, Matthias: "Below 15 kg not part of the type 1").
- **How, tests first:** 19 tests of 01 on a small register, each breaking one thing (a number twice, three types, a
  type 7, a type twice, no type and no entry, a robot left out with types, an unknown entry, a second entry of a
  missing or of another second entry, an unknown form, a mass out of order or given in part, a type 1 robot of 10 kg,
  a robot taken apart not in the parts file or not of type 1, other headings), all failing before the code; the
  builder's 7 tests: what it writes passes 01's checks; 354 robots, 325 with types, 137 with two, 10 second entries, 19
  not assigned; per type 32 / 97 / 181 / 135 / 12 / 5 (V60 less the FF Nova); the three robots taken apart (102 G1, 16
  X1, 350 N1); masses as stated (G1 34 / 35 / 36, QUESTER1 20 / 25 / 30, Walker S2 72 / 73 / 74, PrimeBOT Q1 none).
- **Not covered:** the file on disk: built by Matthias's run of the builder; until then its two comparison tests skip.

### V60. The register's counts by type, computed from the proposal tables (EVIDENCE.md E4.1 to E4.9)

- **What:** the number of robots in each type, after robots listed twice were taken out, robots not assigned and
  unclear ones left aside, and the rule for two types applied (E4.6).
- **How:** a script in Claude's scratch folder (`apply_two_types.py`, then a combined count) reads the Types column of
  every proposal table in EVIDENCE.md, applies the changes listed in E4.6 to robots 1 to 250, takes out the ten
  entries listed twice and the rows without a type, and counts. The rows of batches 1 and 2 that still show a type for
  five robots later not assigned or unclear (ALLEX, Axol, Ambidex, Astra, Bimanual) are taken out by number. Each
  batch's own count was checked against its table the same way (50, 50, 50, 50, 50, 50 and 49 rows).
- **Result:** 349 entries; 10 listed twice; 10 not assigned; 11 unclear; 318 robots with a type, 136 of them with two.
  In each type, a robot with two types counted in both: 1: 32; 2: 95; 3: 178; 4: 134; 5: 11; 6: 4. By the first type
  only: 1: 27; 2: 68; 3: 125; 4: 89; 5: 6; 6: 3.
- **Not covered:** the types themselves are Claude's proposals from the catalogue's second-hand text, not checked
  against the makers for most robots; three pairs may be one robot each (E4.9) and would lower the count to 315; four
  robots the workbook names are not in the catalogue and not counted.
- **Recount after the refinement proposals** (EVIDENCE.md E4.10; HELIOS, Reachy 2 and Synthia given a type, eight
  more not assigned): 321 robots with a type, 321 different numbers (none counted twice), 136 with two types; 1: 32;
  2: 96; 3: 179; 4: 135; 5: 11; 6: 4.
- **Recount with the five robots added** (EVIDENCE.md E4.11; N1, Fuxi, H1, Walker S, PR-OMNI, numbered 350 to 354):
  326 robots with a type, 326 different numbers, 137 with two types; 1: 33; 2: 97; 3: 181; 4: 135; 5: 12; 6: 5.

### V59. The magnets' grade by each joint's heat: in 01, the builder and 04

- **What:** on Matthias's "Accept as proposed" (EVIDENCE.md E2.11): the sheet Joints' base grade class and scenarios
  replaced by a heat group (Hips, Knees, Ankles, Waist, Shoulders, Elbows and wrists, by the joint's name); a new sheet
  MagnetGrades, each group a distribution over grade classes (the accepted table); 01 reads it and checks it (check
  18: every joint's group there, known classes, each once, probabilities adding up to 1, every group used; the old
  grade columns stop the reading; check 19: every class a group can draw in RAWCLICVehicleTractionMotor's workbook); 04
  draws one draw of heat in each draw and every group's class at that point (tied), the magnets' elements of that class;
  the overview's red ring where a joint's group draws 150 °C or more in most draws; `summary.csv` the classes' shares.
  The data file's About sheet updated for the Joints and MagnetGrades sheets (its stale line on the Joints, reported on
  2026-10-28, is gone with it).
- **How, tests first:** 01: six tests on a small file (an unknown class, a joint's group not in MagnetGrades,
  probabilities not adding up to 1, a class twice in a group, a group no joint has, the old grade columns refused);
  the builder: the accepted table and every joint's group by its name; 04: every group's classes at their
  probabilities (4,000 draws, within four standard errors) and each the class at the draw's heat on its cumulative
  probabilities (tied); at the modes, the G1's knees' dysprosium equals their magnets times the drawn class's
  dysprosium (classes given different dysprosium) plus their encoders' 2 mg. All failed before the change. A
  deliberate fault in a scratch copy (each group drawn on its own, not tied) failed the tie test in all six groups.
- **Against the new data file**, built into Claude's scratch folder (not into `data/`): all 200 tests pass. In the
  project, until Matthias runs the builder, 18 of the 200 wait on it: the builder's comparison with the file on disk
  fails, and 3 tests of 01 and 14 of 04 that read the file on disk stop at its old Joints headings, by design (the old
  layout is refused).
- **Sandbox draw** (50,000 draws, the real magnets from RAWCLICVehicleTractionMotor's code, outputs in Claude's scratch
  folder): the classes drawn at their probabilities (knees SH 0.299 / UH 0.500 / EH 0.201, the others likewise);
  dysprosium in one robot median 63 g, mean 67 g, 95 % 29 to 126 g (before, with SH in the legs and waist and H in
  the arms: 52 / 55 g, 26 to 100 g); by kind, medians: hips 23.6 g, arms 17.2 g, knees 9.4 g, ankles 6.7 g, waist
  4.3 g. Copper, Nd + Pr unchanged. The pages looked at; the new footnote fits.
- **Not covered:** the grade probabilities are estimates (no maker states a joint's grade, E2.11); the real run is
  Matthias's.
- **Matthias's runs, read back** (after the commit `5d2c6b2`): the builder at 12:53:19, 04 at 12:53:40 to 12:53:46
  (code of 12:45 to 12:48), 200,000 draws (robots 0.334 / 0.333 / 0.333). **All 200 tests pass.** The classes drawn
  at the accepted shares (knees SH 0.302 / UH 0.498 / EH 0.200, the others likewise); 30 remainders, none below zero in
  any draw; dysprosium in one robot median 63 g, mean 67 g, 95 % 29 to 127 g; copper median 2.21 kg, Nd 287 g, Pr
  54 g, gold 57 mg, as in the sandbox; the seven pages written.

### V58. The X1's and N1's joints weigh their stated mass: the joint's structure the remainder, in 04

- **What:** on Matthias's "Yes, build it" (variant 2 of V57): in `04_parts_taken_apart.py` each joint whose module
  mass is stated (the X1's, the N1's) has its structure (housing, two end caps, output flange, two small bearings) as
  the explicit remainder of its drawn module mass, split in the G1's weighed proportions at their modes; the
  structures reported with the other remainders (`below_zero`, `summary.csv`); 04 checks that the four components
  exist in JointParts. The G1's joints unchanged (they have no stated module mass).
- **How, tests first:** two tests in `tests/test_parts_taken_apart.py`: the X1's and N1's joints, at the robot's own
  mass, lie between the sums of their stated minima and maxima in every draw (before: the X1's 16.9 to 23.7 kg against
  19.3 to 21.2 kg; failed); the joint structures are among the reported remainders (failed). After the change both
  pass, and the hand calculations of the G1 still do.
- **Result:** 191 tests pass. A sandbox draw (50,000 draws, the project's data and settings, outputs in Claude's scratch
  folder): 30 remainders (3 frames, 3 battery housings, 24 joint structures), none below zero in any draw. The elements
  as in V56 (copper median 2.2 kg, Nd + Pr 341 g, Dy 52 g, gold 57 mg); aluminium 95 % 6.6 to 21 kg.
- **Not covered:** the real run is Matthias's (the data file is unchanged; 04 only).
- **Then, on "Yes do it":** the G1's three hip rows of the sheet Joints, column Cooling, "two centrifugal fans per hip"
  corrected to "passive, with air from two centrifugal fans in the hip area" (Munro, T3, read again 2026-10-28: "The hip
  area uses two centrifugal fans"; Matthias: "Joints have no fans, just passive cooling"). Test first (failed, then
  passed); against the file on disk the builder now differs in exactly these three cells. 04 does not read the column,
  so no result changes. The builder's comparison with the file on disk fails until Matthias runs the builder.

### V57. Why the X1's frame falls below zero, and two remainders tested in a scratch copy (nothing changed)

- **Asked,** Matthias: "would mean that the correlations are not taken correctly, or is the uper weight limit the
  problem", then "Yes do as proposed" (test the housing as the joint's remainder in a scratch copy).
- **Measured on his run** (66,599 X1 draws): the frame below zero in 0.81 %, falling with the varied mass (1.35 % at
  30 to 35 kg, 0.67 %, 0.48 %, 0.24 % at 45 to 50 kg): not the upper limit. At its own mass the X1 leaves a median of
  about 3 kg for its frame (joints 20.6 kg, other scaled parts 7.7, fixed 1.9). Its joints come out 0.92 to 1.11 times
  AgiBot's stated module masses at their modes (95 %), against about ± 5 % stated; in the draws below zero 1.12 times
  (median). Cause: each joint's inside follows the G1's components, drawn with their own spread and scaled by a fixed
  number, so it does not add up to the drawn module mass; and those draws are shared by all 29 joints.
- **Tested** (scratch copy of 04, the project's data and settings read only, 50,000 draws, the same seed and magnets):
  1. *The housing as the explicit remainder* of each X1 and N1 joint: the joints at 0.988 to 1.012 times the stated
     masses, no frame below zero; but the housing below zero in 5.8 % of the X1's large joints' draws (5.5 % N1), 0.43 %
     of the small ones'. Rejected: the housing (about 11 % of a large joint) is too small to take the large joint's
     other components, drawn with the G1's factors of up to 3.56.
  2. *The joint's structure as the explicit remainder* (housing, two end caps, output flange, two small bearings),
     split among them in the G1's weighed proportions at their modes (fixed numbers, not the draw's own sum): no
     remainder below zero anywhere (the lightest structure 19 g, the N1's shoulder pitch); the X1's joints at 0.988 to
     1.012 times the stated masses; copper, Nd + Pr, Dy and Au unchanged to five figures; aluminium mean 13.27 kg
     (13.22 before), as the steel of the flange and bearings is now part of the remainder.
- **Not covered:** nothing changed in the project; variant 2 waits for Matthias's word.

### V56. The X1's and N1's battery packs cut at the model's own cells

- **What:** on Matthias's "Cut at the cells" (EVIDENCE.md E2.8e, "The battery packs' lower cut"): in
  `tools/make_parts_taken_apart.py` the X1's pack 1.75 / 2.2 / 3.3 kg (was 1.4), the N1's 2.26 / 2.9 / 3.2 kg (was 1.9).
- **How, tests first:** a new test in `tests/test_make_parts_taken_apart.py` computes, for every robot, the pack's
  needed lower bound from the builder's own output (largest energy over 00's `composition.nmc_wh_per_kg_min`, plus the
  largest management board over the lightest robot's mass factor, type 1's 30 kg from the workbook's Taxonomy) and
  checks the pack against it, and the two new values. Before the change it failed for the X1 (1.4 against 1.746) and
  the N1 (1.9 against 2.254), not for the G1 (2.25 against 1.999); after it, it passes.
- **Against the new data file**, written by the builder into Claude's scratch folder (not into `data/`): the 19 tests
  of the builder and of 04 all pass. A sandbox draw of 04 (50,000 draws, outputs in the scratch folder): no battery
  housing below zero; the lightest 0.38 kg (G1), 0.14 kg (X1), 0.14 kg (N1); medians 0.80, 0.97 and 0.82 kg (the X1's
  was about 0.70 kg at the modes before, its pack range now narrower from below). The X1's frame below zero in 0.78 %
  of its draws (0.68 % in Matthias's run), unchanged in kind. The elements as in V55, to their sampling spread.
- **Result in the project:** the one test failing is the builder's comparison with the data file on disk, until
  Matthias runs the builder.
- **Matthias's runs, read back:** the builder at 12:11:33 (after the change of 12:09:43), 04 at 12:11:51 to 12:11:57,
  200,000 draws (robots 0.334 / 0.333 / 0.333). No battery housing below zero: the lightest 0.330 kg (G1), 0.167 kg
  (X1), 0.133 kg (N1), medians 0.797, 0.966, 0.820 kg. The X1's frame below zero in 0.81 % of its draws, no other
  remainder. Elements as in V55 (copper median 2.21 kg, gold 57 mg, Nd 287 g, Pr 54 g, Dy 52 g). **190 tests pass.**
- **Not covered:** the housing's own mass has no source (a remainder); a minimum case mass was not researched (option 2,
  not chosen).

### V55. Matthias's real run of 04 with the pages, read back

- **What:** his run of `04_parts_taken_apart.py`, 12:02:34 to 12:02:41, 200,000 draws, with the code of 11:53:39 (the
  pages, median and mean) and the data file his builder wrote at 11:41:27.
- **How:** read from disk: `robots.npy` (200,000 rows; the G1, X1 and N1 in 0.334, 0.333 and 0.333 of the draws),
  `summary.csv`, the seven pages (each 2,400 × 1,350 pixels; looked at side by side for anything broken).
- **Result,** one robot of type 1, median / mean (95 % interval): varied mass 38.3 / 38.6 kg (31.6 to 47.4); copper
  2.21 / 2.27 kg (1.61 to 3.27); aluminium 13.1 / 13.3 kg (6.3 to 21.4); silver 432 / 472 mg (184 to 981); gold 57 / 64
  mg (29 to 127); palladium 22 / 26 mg (12 to 54); tantalum 143 / 165 mg (27 to 426); neodymium 287 / 298 g and
  praseodymium 54 / 57 g (Nd + Pr 342 / 355 g); dysprosium 52 / 55 g (26 to 100); gallium 599 / 640 mg (142 to 1,372);
  indium 9.0 / 13.5 mg (0 to 53). Within the sandbox's of V53 and V54 (2,000 draws) to their sampling spread.
  Remainders below zero: the X1's battery housing in 1.00 % of its draws, its frame in 0.68 %; the N1's battery
  housing in 0.80 %; none of the G1's.
- **Not covered:** the finding of V53 stands: the battery packs' lower cut (250 Wh/kg cells) against 00's NMC cells
  (232.5 to 256 Wh/kg).

### V54. Stage 04's figures on readable pages, with the median and the mean

- **What:** Matthias, on the first previews: "Have the overview on several pages. I can not read it. too smal, you
  should notice this before you sjhow me. Elements is an edge case. Also quite small"; then "Showing the mean is
  wrong. It is not a good measure. Use the median or show boths" (answer "Both, median first"). The element figure on
  2 pages, the overview on 5, each 16 × 9 inches with no text below 14 points; the median a solid line, the mean a
  dotted one, each with its number (METHODOLOGY.md, "What 04 draws").
- **Measured before:** fit to a 1920 × 1080 screen, scale = min(1920 / width, 1080 / height): the one-page overview
  (3,073 × 3,205 pixels, smallest text 10 points) showed its smallest text 7.0 pixels tall, the one-page element figure
  (2,997 × 1,821, 11 points) 13.6 pixels: his "can not read it" and "edge case".
- **How, tests first:** `TestReadable` draws every page and fails where its smallest text, fit to that screen, is under
  18 pixels; it failed before the change (no pages). `TestCentre` draws a panel and an overview row of skewed draws
  (lognormal) and checks that the solid line sits at the median and the dotted one at the mean; it failed before the
  change (no dotted line). Both pass after it.
- **Measured after** (sandbox, 2,000 draws): every page 2,400 × 1,350 pixels, smallest text 23.3 pixels on that screen.
  Every page opened and looked at, at screen size; fixed on the way: a two-line title where "Neodymium and
  praseodymium (Nd+Pr)" ran into the next panel, a number and its unit kept together in the footnotes, the overview's
  two number columns headed "median" and "mean" with the unit in the panel's title (the headers had run into each
  other).
- **Result:** 189 tests pass, the builder's comparison with the data file on disk included (Matthias ran the builder
  at 11:41:27).
- **Matthias's real run of 04, 2026-10-28, 11:41:44 to 11:41:50**, with the version before the pages: 200,000 draws;
  `data/parts_taken_apart/` 297 MB (elements 180.8 MB, parts 76.8, materials 36.8, robots 2.4), against the 280 MB
  extrapolated in V53; the varied mass median 38.3 kg, mean 38.6 kg. Its two one-page figures are in
  `figures/parts_taken_apart/`; the page version writes other names, so a new run leaves them beside the pages.
- **Not covered:** the pages of his data run itself (200,000 draws) are not drawn yet; the readability test checks text
  size, not overlaps, which were looked at.

### V53. Stage 04: robot type 1 taken apart, drawn, and its two figures (steps 5 to 7)

- **What:** on Matthias's "Yes, build steps 5 and 6: stage 04 and its two approved figures, tests first, tried in a
  sandbox with few draws" and his answers A to E (HANDOVER.md, 2026-10-28): `04_parts_taken_apart.py` (method in
  METHODOLOGY.md, "What 04 draws") and `tests/test_parts_taken_apart.py`.
- **How, tests first:** the 11 tests were written and run before the stage existed (they failed: no file). With the
  stage, all pass. They check: each robot drawn about a third of the time (within four standard errors, 3,000 draws);
  the varied mass within 30 to 50 kg and the own mass within each robot's range; the materials and the parts of every
  draw adding up to its varied mass (to 1e-9); the frames and battery housings reported below zero, not cut; the
  magnets' fractions from RAWCLICVehicleTractionMotor's own code adding up to 1, iron the remainder; the draws written
  at every level and both figures drawn. **Hand calculations**, every triangle at its mode and the magnets' fractions
  fixed, against the data file's modes (EVIDENCE.md E2.8, E2.8b): the G1's copper in its cables 152.684 g (102.144 g
  conductors, 48.3 g XT30, 2.24 g capacitor buffer boards); its gold in its hips 10.50288 mg (six driver boards of
  81.524 cm2 at 0.02 mg/cm2, twelve encoders at 0.06 mg); its neodymium in its hips 99.205152 g (six rotors of 76.362 g,
  90 % NdFeB, 24 % Nd, and twelve encoders at 20 mg); each robot at its modes weighing 35, 33 and 39 kg; and answer B:
  at 50 kg the G1's hip joints weigh 50 / 35 times as much, its hip fans and its head the same.
- **Deliberate faults**, in scratch copies of the stage: the encoders counted per joint kind instead of per joint (the
  gold and neodymium hand calculations failed, 3.4 % and 0.12 % off); the joints not following the varied mass (the
  scaling test failed). Both caught.
- **Against today's data file:** the builder wrote the file of V52 into Claude's scratch folder (not into `data/`); with
  it, the 15 tests of 04 and of the builder all pass, the builder's comparison with the file on disk included.
- **Sandbox run** (step 7): the project's settings, 2,000 draws, today's data file from the scratch folder, every output
  into Claude's scratch folder; 4.5 s. Means in one robot (95 %): copper 2.3 kg (1.6 to 3.3), aluminium 13 kg (6.4 to
  22), silver 469 mg, gold 63 mg (29 to 126), palladium 26 mg, tantalum 164 mg, neodymium and praseodymium 352 g (183 to
  597), dysprosium 54 g (25 to 99), gallium 639 mg, indium 13 mg (0 to 53). Order of magnitude against the G1 alone
  (E2.8c: copper 1.82 kg, gold 51 mg, Nd + Pr 312 g, Dy 49 g): higher by the heavier draws (mean about 39 kg) and the X1's
  29 joints. Gallium 639 mg against the G1's 130 mg: the magnets' gallium of the sibling's grade bands (0 to 0.1 % of
  NdFeB), not in E2.8c's table. Indium: 0 in about a third of the draws, the N1's (no camera in the standard robot).
  Remainders below zero: the X1's battery housing in 1.4 % of its draws, the X1's frame in 0.9 %, the N1's battery
  housing in 1.3 %. Both figures opened and looked at; the overview redrawn once (a mean written 9.5e-05, labels
  running into the robot, rows too far apart), then clean. `data/` and `figures/` of the project unchanged. Its cost,
  measured (`/usr/bin/time -l`): 2,000 draws 4.5 s, 0.36 GB peak memory, 2.9 MB written; 20,000 draws 4.9 s, 0.57 GB,
  28 MB; 50,000 draws 5.3 s, 0.88 GB, 71 MB. For the real run, extrapolated linearly and not measured: 200,000 draws
  about 10 s, 2.5 GB, 280 MB.
- **Result:** 186 tests; 185 pass. One fails by design until Matthias runs the builder (V52, point C).
- **Not covered:** the real run (200,000 draws) is Matthias's; the magnets' scenarios (UH, EH) are not drawn, only the
  base classes; the elements of steel, titanium and the mixed parts are not drawn; the X1's phone and the N1's network
  switch beyond the phone's board (E2.8e).
- **Found, not changed:** the X1's and N1's battery packs were cut below at 250 Wh/kg cells (E2.8e), but 00's NMC cells
  range from 232.5 to 256 Wh/kg (`composition.nmc_wh_per_kg_*`): where a light pack meets heavy cells, the housing
  falls below zero. And `.gitignore` now names `data/parts_taken_apart/` (the stage's `.txt` column lists would
  otherwise not be ignored).

### V52. The X1's and N1's masses and the G1's parts carried over to them, in the builder

- **What:** on Matthias's answers "X1 max 35.3 kg", "Encoders", "XT30 connectors", "Main board cooler" and then "Yes,
  build" (EVIDENCE.md E2.8e, "Decided, 2026-10-28"), the builder `tools/make_parts_taken_apart.py` now writes: the
  X1's mass 32 / 33 / 35.3 kg; for the X1 and N1 each, encoders (two per joint) in the sheets Parts and Sensors, XT30
  (2+2) connectors (two per joint), a main board fan and a main board heat sink of copper heat pipes and fins; two new
  sources (FW1, DY1).
- **Checked first-hand, today, before entering:** the X1's two BOMs (X1a, downloaded again on his "Yes, download"
  into Claude's scratch folder only), counted for its XT30 plugs: 19 cables with two, 12 with one, 6 terminating
  resistors and 2 to the L28 push rods, 58; AgiBot's model file (X1c), its 58 links summed in the browser: 35.323 kg;
  Fourier's N1 page (N1a): "双编码器 16bit/14bit", "体重38公斤", "净重 ≈39 kg"; Dynatron's I2 page: "199g ±5g";
  Framework's kit page: "Weight: 67.5g".
- **How, tests first:** a new test in `tests/test_make_parts_taken_apart.py` (the X1's mass; for every robot, encoders
  and XT30 connectors twice its joints in the sheet Joints, the fan's mass; the X1's and N1's heat sink, its range,
  copper, E) failed before the change (the X1's max 34.0, not 35.3) and passes after it. Deliberate faults in a
  scratch copy of the builder (the X1's encoders 56 instead of 58; the N1's heat sink aluminium instead of copper) were
  both caught. What the builder writes passes 01's checks 18 to 20 with no fault. Compared with the file on disk, it
  differs in exactly the rows decided: 8 rows added to Parts, 2 to Sensors, 2 to Sources, the X1's mass row changed in
  Constants; nothing else.
- **Result:** 175 tests, 174 pass. **One fails by design:** `test_what_it_writes_equals_the_data_file_on_disk`, until
  Matthias writes the new file by pressing Run on the builder (point C of the specification, as recommended and
  accepted); then it passes. The data file was not written: 2026-10-27 15:14:22, 28,792 bytes, before and after.
- **Not covered:** the heat sink's mass has no source of its own kind (no maker gives the mass of a mini PC's cooler):
  an estimate, with a laptop's and a server's cooler as context only; its copper is an upper bound if the mini PCs'
  fins are aluminium (point B). Whether a connector counts one half of a mated XT30 or both is still open for all three
  robots (point A). The X1's encoders rest on "two per joint" as the G1 and N1 (E): its BOM lists the actuators as
  bought-in units and names none.

### V51. The builder of the data file, rewritten into tools/

- **What:** on Matthias's "Yes, rewrite": `tools/make_parts_taken_apart.py`, the builder of
  `data/researched/parts_taken_apart.xlsx` (the first builder, in Claude's scratch folder, was lost with it; found
  empty on 2026-10-28). Its values were transcribed from the data file on disk, which the first builder had written
  from EVIDENCE.md E2.8 to E2.8e on 2026-10-27 (15:14:22, 28,792 bytes): the only exact copy left.
- **How, tests first:** `tests/test_make_parts_taken_apart.py` (written 2026-10-27) run before the builder existed:
  it failed (the file not there). Then, with the builder: what it writes into a temporary folder passes 01's checks 18
  to 20 with no fault; it equals the file on disk sheet by sheet and cell by cell (values); it writes where 00's
  `data.parts_taken_apart` says. A deliberate fault in a scratch copy of the builder (copper density 8.96 / 8.97 /
  8.98 instead of 8.96 three times) was caught: the comparison found exactly that row (Constants, row 5) and no
  other.
- **Result:** 174 tests pass, none skipped. Importing the builder (as the tests do) wrote nothing: the data file's
  time and size were the same before and after the tests (2026-10-27 15:14:22, 28,792 bytes).
- **Not covered:** cell formats (bold, fill, widths) are not compared, only values; the builder was not run into
  `data/` (pressing Run is Matthias's); the values themselves rest on E2.8 to E2.8e.
- **Found, not changed:** the file's own About sheet still says "Sheet Joints: the 12 joint kinds of the basic G1 (23
  joints)", written before the X1 and N1 went in; the builder reproduces it, as the comparison demands.

## 2026-10-27

### V50. Step 2b: the G1, X1 and N1 in one data file, and 01's checks of it

- **What:** on Matthias's "Yes, build points 1 to 8 as specified, tests first" (EVIDENCE.md E2.8e): the data file
  `data/researched/parts_taken_apart.xlsx` holds the Unitree G1, the AgiBot X1 and the Fourier N1 (sheet Robots; a
  column Robot on Joints, Parts, Boards, Sensors and Constants; module masses on Joints); 01 reads it
  (`read_parts_taken_apart`), checks it per robot (`check_parts_taken_apart`) and checks every robot against its
  type's height and mass in the workbook's sheet Taxonomy (`check_robot_types`, new; METHODOLOGY.md check 20).
- **How, tests first:** the small test file rewritten for two robots (one as the G1, without module masses; one as the
  X1, with them); 12 tests added: the one-robot layout refused; a robot not in Robots; a robot without rows on a sheet;
  a module mass given in part; a module mass out of order; a robot's own constant missing; a robot below its type's
  height (1.18 m), above its mass (57 kg), of a type the Taxonomy lacks, of a type whose limits cannot be read; the
  robots inside their type; the real robots inside type 1. Run against the code before the change: 36 errors. The new
  file built into Claude's scratch folder and checked by all three of 01's checks (0 faults each) before it replaced
  the old file (point 7: no copy).
- **Result:** 171 tests pass, none skipped. The real file: three robots; the G1 23 joints in 12 kinds, 9 large, its
  weighed joint parts 525 g and the large joint 1,011.717 g, unchanged; the X1 29 joints, 15 large, module masses at
  their modes 20.27 kg (AgiBot's own); the N1 23 joints, 11 large, 14.90 kg (the fit, as E2.8e rounds it); every robot
  inside type 1 (1.20 to 1.45 m, 30 to 50 kg); every board category, sensor type and magnet class in the sibling files.
- **Found on the way:** the test first expected the N1's joints at 14.94 kg, the fit unrounded; the accepted table
  gives 0.88 / 0.70 / 0.54 kg, so 14.90 kg; the test now checks the accepted values. A missing magnet grade class was
  reported once per joint using it (twice in the small file); it is now reported once, naming every joint that uses it.
- **Not covered:** the values themselves (E2.8e, as accepted); 01 not run (its pages are drawn when Matthias presses
  Run); stage 04, which draws the robots, not built (step 5).

### V49. The element figure of robot type 1, approved as a preview

- **What:** the scratch preview "Robot type 1 (Unitree G1): critical elements in one robot", approved by Matthias
  ("Yes, the element figure is right now"): one histogram per element of the robot's total, each bar split into the
  weight its draws hold in each of ten kinds of part (the form of RAWCLICDataCenters' `05_data_center_elements.py`,
  `_stacked_panel`), from the 20,000 draws of the G1 alone (`kinds_draws.npz`, Claude's scratch folder).
- **How:**
  - for copper, gold, aluminium and tantalum, the stacked segments of every bar summed and compared with the bar's
    share of the draws, and the grams in all bars of a part compared with that part's grams over all draws;
  - the bars' shares summed;
  - the mean weight of every part compared with the approved overview figure (robot_type_1_distributions.png);
  - the ten colours compared with Paul Tol's own file `tol_colors.py` (rainbow_discrete, lut = 10, downloaded from
    https://sronpersonalpages.nl/~pault/data/tol_colors.py on 2026-10-27), and the one swap (frame and battery pack)
    checked to leave the set of colours unchanged;
  - the figure opened and looked at after every change (nothing cut off or overlapping).
- **Result:** largest gap between a bar and its stack 9.7e-17; largest relative gap between a part's grams in the
  bars and over all draws 5.3e-16; the bars sum to 1.000000; the part means equal the overview's (copper in the hip
  joints 517 g, in the arm joints 449 g); the colours are Tol's ten, unchanged.
- **Not covered:** the draws themselves (V45, E2.8); the spread between robots of type 1 (open point G), not yet in;
  the stage that will draw the figure (step 6) is not built, so these checks are to be repeated on its output.
- **Found on the way and corrected:** a palette search of Claude's own (scratch) first left out the LMS step of OKLab
  and ranked colours on a wrong distance; corrected before use. Claude then graded Tol's published palettes with that
  home-made score; Matthias objected ("You always try to trick me"); the figure now uses Tol's set as published.

### V48. Step 4: the settings of robot type 1 taken apart, and the sibling projects' files checked

- **What:** on Matthias's "Yes" to step 4: in 00 the absolute paths of the four sibling files and of
  RAWCLICVehicleTractionMotor (`data.vehicle_pcb_composition`, `data.vehicle_sensor_composition`,
  `data.data_center_element_composition`, `data.traction_motor_magnets`, `data.traction_motor_dir`), the draws and
  seed of the stage to come (`parts.draws` 200,000, `parts.seed` 1) and its output folders (`output.parts_dir`
  `data/parts_taken_apart`, the project's own outputs until open point F is decided; `output.parts_figures_dir`
  `figures/parts_taken_apart`); in 01 `check_sibling_data` (CHECKS_DONE and METHODOLOGY.md point 19).
- **How, tests first** (`TestSiblingData`; `tests/test_parameters.py`): run failing (12), then passing. Small copies of
  the four sibling sheets are broken one at a time: a board category not there; a category without palladium; a
  sensor type not there; a magnet class missing; no tantalum row; a file not there. A relative sibling path, too few
  draws, a negative seed or an empty output folder stops 00.
- **Result:** 159 tests pass, none skipped. The real sibling files hold everything the real file names: the car board
  categories PE_HVS, ITC, BMS and VCC with gold, silver, palladium, tin and nickel; the car sensor types laser diode
  array, photodetector array, IMU, IR camera sensor, CMOS image sensor, MEMS microphone array and angle sensor; the
  tantalum row 0 / 0.0001 / 0.00045; the magnet grade classes H, SH, UH and EH.
- **Not covered:** the sibling files' numbers themselves (they are their projects'); 00 not run, so `params.xlsx` and
  `PARAMETER_REFERENCE.md` gain the new settings at the next press of Run on 00.

### V47. Step 3: 01 checks robot type 1 taken apart

- **What:** on Matthias's "Yes" to step 3: the setting `data.parts_taken_apart` (00), and in 01 the reader
  `read_parts_taken_apart`, the check `check_parts_taken_apart` (CHECKS_DONE point 18, METHODOLOGY.md point 18) and
  their call in `main()`.
- **How, tests first** (`tests/test_schemas.py`, class `TestPartsTakenApart`; `tests/test_parameters.py`): written
  before the code and run failing (19 errors and failures), then passing. A small file of the same layout is broken
  one thing at a time, and 01 must report exactly that fault: a minimum above its mode; an estimate narrower than half
  to 1.5 times its mode; a large joint's factor below 1; a group of shares without its remainder; shares leaving the
  remainder below zero; a material and a body region not on the shared lists; shares of a part that does not exist; a
  component with neither one material nor shares; joints not matching the joint modules; a joint number given twice;
  a magnet grade class that is not one; a sensor element of an unlisted sensor; a missing constant; an unknown label;
  two parts taking the robot's remainder; a missing sheet (stops the reading). A setting not ending in .xlsx stops 00.
- **Result:** 151 tests pass (were 132). The real file read with the real shared lists: 12 joint kinds, 14 components,
  18 parts, 20 shares, 7 boards, 6 sensors, no fault. The test of the real file asserts 23 joints, 9 large, the small
  joint 525.0 g and the large joint 1,011.717 g at the factors' modes.
- **Corrected on the way:** the test first expected 1,011.744 g, a slip of mine; worked by hand (154.1 g × 1.78 +
  155.2 g × 2.33 + 12.8 g × 3.56 + 11 g × 1.78 + 79.3 g × 1.39 + (23.7 + 50.8 + 38.1) g × 1.78 = 1,011.717 g), the
  file was right. Two rows of the file gained what they are computed from (the encoders, the battery pack), so that 01
  can tell they need no shares.
- **Not covered:** whether the car board categories, car sensor types and magnet grade classes are in the sibling
  projects' files (step 4); the parameter register and `PARAMETER_REFERENCE.md` are rewritten by 00, not run here
  (the next press of Run on 00 writes the new setting into them).

### V46. Step 2: the data file `data/researched/parts_taken_apart.xlsx` against EVIDENCE.md E2

- **What:** the new workbook for robot type 1 (Matthias, "Yes" to step 2), written by a one-off builder in Claude's
  scratch folder from E2.8, E2.8b and E2.8c with his decisions of step 1; ten sheets (About, Joints, JointParts, Parts,
  Shares, Boards, Sensors, SensorElements, Constants, Sources).
- **How:** the file read back with openpyxl; its numbers checked against E2.
- **Result:**
  - 23 joints in 12 kinds: 9 large, 14 small, as T1.
  - The small joint's parts add up to 525.0 g, as T1 weighed; the large joint's parts at their factors' modes to
    1,011.7 g, as E2.8 (1,012 g).
  - Every min ≤ mode ≤ max; in every part, the shares other than its remainder add up to at most 1 at their maxima
    (the joint's "Other": exactly 1, so its plastics remainder never falls below zero).
  - Every value labelled E spans at least half to 1.5 times its mode, except the rotor's NdFeB, whose maximum is cut
    at 100 % (stated, agreed).
  - Git ignores the file (`*.xlsx`, `.gitignore` line 21).
- **Not covered:** 01 does not check the file yet (step 3); nothing reads it yet.

### V45. The proposal for robot type 1 part by part (EVIDENCE.md E2.8), checked against the measured totals

- **What:** the estimates of E2.8 against the masses the sources measured and against the workbook's sheet `Material
  Composition per Cat` (robot type 1, rows 5 to 14). Nothing in the project was changed or run; the proposal is not
  entered.
- **How:** a scratch script (not in the project), 20,000 draws, seed 1, each min / mode / max drawn as a triangle,
  independently; remainders taken explicitly, never rescaled. Checked by hand: the small joint's 14 weighed parts add
  up to 525.0 g; motor 94.3 + 42.9 = 137.2 g and gearbox 8 + 25.3 + 24.1 + 74 + 23.8 = 155.2 g, as T1 states;
  46.8 V × 9 Ah = 421.2 Wh against T1's 0.42 kWh.
- **Result:**
  - **Small joint:** 497 / 525 / 552 g (2.5 % / mean / 97.5 %) against T1's 525 g.
  - **Large joint:** modes 1,012 g; draws 1,017 / 1,097 / 1,185 g against 1,100 g (T1) and 1,085.1 g (T3k). The mode
    is 8 % under T1, the mean 0.3 % under it.
  - **Battery:** cells 1.67 / 1.73 / 1.79 kg; the pack's remainder 0.67 / 0.73 / 0.80 kg; never below zero.
  - **Robot:** all estimated parts 20.2 / 21.1 / 22.1 kg (with the pack's remainder about 0.7 kg more); frame and shell,
    the remainder of 35 kg, 11.9 / 13.2 / 14.4 kg, never below zero; its aluminium 6.3 / 8.1 / 9.8 kg, never below
    zero. The materials add up to 34.2 / 35.0 / 35.8 kg.
  - **Against the workbook's materials:** aluminium agrees (12.2 against 12 kg); copper is half the workbook's (1.8
    against 3.8 kg); cables a third of row 18 (0.45 against 1.3 kg); steel higher (8.9 against 7.0 kg); magnets lower
    (1.1 against 1.5 kg); the workbook has no electrical steel (1.6 kg here).
  - **Found and fixed in the script before reporting:** the pack's 0.73 kg remainder was at first not subtracted from
    the robot, which put the materials at 35.7 kg; counted once, they add up to 35.0 kg.
  - **Rerun with the stator's copper share at 23 / 36 / 45 %** (Matthias, "Yes use this numberrs"; E2.10), in place of
    30 / 40 / 55 %: copper 1.30 / 1.57 / 1.85 kg (was 1.49 / 1.78 / 2.10), electrical steel 1.50 / 1.78 / 2.11 kg (was
    1.28 / 1.57 / 1.89); every other total unchanged; the materials still add up to 34.2 / 35.0 / 35.8 kg.
  - **Rerun with every estimate at least half to 1.5 times its mode** (Matthias, "Estimates should be larger than
    known numbers", then "Yes"; E2.8): the 13 unweighed small joints ± 50 % (was ± 20 %), the large joints' factors
    from 1.0 up, the rotor's NdFeB from 0.45, the board mass per cm² 0.28 / 0.56 / 0.84, the cables from 3 m, and the
    rest listed in E2.8. Small joint 456 / 525 / 593 g; large joint 912 / 1,034 / 1,158 g against 1,100 g (T1) and
    1,085.1 g (T3k), its mean now 6 % under T1; frame and shell 12.0 / 13.8 / 15.5 kg and its aluminium 6.1 / 8.6 /
    11.1 kg, never below zero; copper 1.17 / 1.52 / 1.90 kg; magnets 0.69 / 1.02 / 1.39 kg; the materials still add up
    to 34.2 / 35.0 / 35.8 kg.
  - **Against the workbook's parts list, rows 8 to 20** (Matthias: "Compare with already existing data"): the joints
    agree in total (16.7 against 17.6 kg) and the battery (2.5 kg); the harness is a third, the fasteners a quarter
    and the cooling about a sixth of the workbook's rows, and the frame and shell, the remainder, 4 kg above rows 16
    and 17; frame, shell, harness, fasteners and cooling together 14.9 kg here, 13.75 kg in the workbook. **Found:**
    row 14 gives the LiDAR 0.65 kg, "Direct", citing Livox (S46), whose specifications give 265 g; reported, not
    changed. Not covered: Unitree's model file was read only approximately for this check (about 13 kg).
  - **Where the materials sit** (a second scratch script reading the first one's draws): the knee cooling moved into
    the knee joints (Matthias, "Is with the joins often used"); every part split over body regions by its count of
    pieces there. Checked: the regions add up to each material's total (copper 0.83 + 0.42 + 0.08 + 0.18 = 1.52 kg);
    the materials' totals are unchanged by the move (34.2 / 35.0 / 35.8 kg). Result: the joints hold 88 % of the
    copper and all the NdFeB; their driver boards are 51 % of the boards' mass.
  - **Boards and sensors to elements** (EVIDENCE.md E2.8b; a third scratch script, 20,000 draws, seed 1, reading the
    board masses of the first and the car rows of `RAWCLICVehicleElectronics/Data/04_` and `07_`, copied to a scratch
    file, not changed). Checked by hand: Bizzo's 14 copper values average 20.03 wt% (12.5 to 28.7); the two laser
    diode arrays give 2 × (5 + 30 + 150) / 3 = 123 mg gallium at the mean, the photodetector 3.7 mg, together 127 mg as
    printed. Result: gold 35 / 51 / 73 mg, copper 0.10 / 0.16 / 0.23 kg, gallium and arsenic about 0.13 g each, all in
    the head; no germanium. Not covered: the approximation of drawing board area and mass independently.
  - **Tantalum added, silicon dropped** (Matthias): board mass × 0 / 100 / 450 ppm (DataCenters'
    `BoardsAndComponents`, its row read and quoted): 63 / 140 / 248 mg; every other element unchanged within the
    draws' noise (gold 34 / 51 / 73 mg).
  - **The complete picture** (EVIDENCE.md E2.8c; a fourth scratch script running the other three and 02's
    `RecipeDraws` on the project's recipe 'NMC cylindrical', read-only, nothing written to the project). Checked by
    hand: copper 1.52 (parts) + 0.16 (boards) + 1.744 × 8.36 % = 0.146 (cell foil) = 1.82 kg, as printed; lithium
    1.744 × 2.58 % = 0.045 kg.
  - **The magnets' elements** (a fifth scratch script, run in RAWCLICVehicleTractionMotor's own environment with its
    `magnet_element_draws`, read-only): the grade bands printed by its `magnet_chemistry` match its METHODOLOGY § 4.2
    table (Nd + Pr 0.29–0.32 in every class; Dy H 0.02–0.05 to EH 0.08–0.10). Checked by hand: Nd + Pr = 262 + 50 =
    312 g of 1,021 g of NdFeB = 30.5 %, inside 0.29–0.32. Not covered: which joints run hot is a proposal; the
    fractions use that project's fixed seed, so the scenarios share their draws.
- **Not covered:** the estimates' own bases (E2.8 names where there is none); the 23 joints' differences beyond
  small and large; the sensors' and boards' insides.

### V44. The real run: 00 to 03, 200,000 draws

- **What:** on Matthias's word "Yes, run 00 to 03 with the full 200,000 draws into data/consolidated/ and figures/,
  then tell me when the pages are there."
- **How:**
  - **The run:** 00, 01, 02 and 03 were run in order from the project folder with the project's `.venv`, each timed
    with `/usr/bin/time -l`.
  - **The outputs:**
    - every robot type's `.npy` files were loaded and their shapes checked against their `.txt` column lists;
    - materials, part groups and body regions were added up against the total, row by row;
    - each total's mean was compared with the workbook's triangle;
    - `git check-ignore` was run on the outputs.
  - **The pages:**
    - robot type 2's page and 03's page by material were opened and read;
    - 01's 20 pages were compared byte for byte with the sandbox pages read in V43.
- **Result:**
  - **00:** 200,000 draws, seed 1; every input present.
  - **01:** no fault; 20 pages in 9.3 s, at most 380 MB.
  - **02:** 9.0 s, at most 1.88 GB, almost twice the estimate of about 1 GB (HANDOVER). It wrote 42 MB per robot type,
    252 MB in all, as computed.
  - **03:** 4.0 s, at most 495 MB.
  - **The draws:**
    - every file has 200,000 rows and as many columns as its list;
    - the sums miss the total by at most 1e-7 of it, the rounding of float32;
    - the totals' means are 35.00, 71.44, 72.90, 69.34, 103.90 and 93.99 kg, each its triangle's mean;
    - robot type 2's magnesium is 6.33 kg, the mean of (4, 6, 9).
  - **The pages:** 01's are unchanged against the sandbox. Not allocated is below zero in 52.2 % of robot type 1's
    draws and 67.0 % of robot type 2's (2,000 draws: 50.8 and 67.4 %).
  - **Git:** the outputs are ignored (`data/consolidated/` and `figures/` in `.gitignore`).
- **Not covered:** of 02's and 03's ten pages, two were opened; the other eight are the same code as the preview pages
  read in V43.

### V43. Aluminium's modes rewritten and magnesium entered, and a preview of 02 and 03

- **What:** E1.1e with E1.1f (aluminium) and E1.2c with E1.2d and E1.2e (magnesium), entered on Matthias's word:
  "Yes, enter both: rewrite the aluminium modes as in E1.1e, and enter the magnesium recipe of E1.2c ... with the
  modes of E1.2d". Mid-entry, before anything was written, he added: "If the elemental analysis of a material is only
  based on university analysis, then combine them and use respective large uncertainties." Then: "Can we then
  continue with the code to describe the material compsotion of the six robot types. Furthermore I want to see these
  related figures soon."
- **How:**
  - **Tests first.** The aluminium test's expected table was set to E1.1e with E1.1f; a new magnesium test requires
    no fault, a row for robot types 2, 3, 4 and 6 (robot type 3 naming 'Magnesium AZ91D'), and E1.2e's table at the
    modes. Both failed before the entry.
  - **The second rule:** applied in a sandbox (`modes_by_rules_sandbox.py`). Every university value was checked
    against its limits before combining; none was outside.
  - **The data:** the workbook was copied to the session's scratch folder
    (`element_recipes_before_modes_and_magnesium.xlsx`) and the copy compared byte for byte. The entry script
    (`make_modes_and_magnesium_entry.py`) took the modes from the sandbox's own code, word for word:
    - 34 aluminium items rewritten in place (mode, label, basis), each checked to keep its limits;
    - 33 magnesium items and 4 rows added.
  - **01:** check 17's text names magnesium. 01 was drawn into the scratch folder before and after, and all 20 pages
    compared byte for byte.
  - **02 and 03:** run on the real inputs with 2,000 draws into the scratch folder. Robot type 4's page was read, and
    all ten pages were sent to Matthias as a preview.
- **Result:**
  - 132 tests pass, none skipped. 01 finds no fault, and of its pages only faults.png changed (check 17's text).
  - In 02, magnesium is in the elements of robot types 2, 3, 4 and 6.
  - Robot type 4's element magnesium is 6.31 kg: its 6.40 kg of magnesium alloy at about 92 % Mg, plus about 0.43 kg
    in its 28.5 kg of aluminium.
  - Its element aluminium is 26.6 kg, and its elements now cover 45.3 of its 62.7 kg of materials.
- **Not covered:**
  - The 200,000-draw run, which is Matthias's; the preview has 2,000 draws.
  - `figures/` and `data/consolidated/` were not written.

### V42. The modes set again by Matthias's rule, drawn in a sandbox

- **What:** [EVIDENCE.md](EVIDENCE.md) E1.1e (aluminium) and E1.2d (magnesium), on Matthias's "Yes, redo the modes of
  E1.2c and of the entered E1.1c by my rule".
- **How:**
  - **The sources:**
    - SAE's pages for AMS4027P, AMS4045N and AMS4490K;
    - Arconic's lot tables for SS-6061, SS-7075, KC-380, SS-380 and SS-383, in the built-in browser (a small reader
      turned each tab into its certified values; SS-380's tin was read again by hand);
    - NIST's certificate for SRM 1256b, through its text layer;
    - searches for reference materials of ADC12, AZ91D, AM60B and AM50A, and for SAE specifications of AM60B and AM50A.
  - **The modes:** each set by the rule's order (`modes_by_rule_sandbox.py` in the session's scratch folder), every
    one checked to lie within its limits.
  - **The copy:** a scratch copy of `element_recipes.xlsx` with the aluminium modes rewritten (34 items) and the
    magnesium proposal added.
  - **The checks:** 01's `check_element_recipes` and `check_material_recipes` on the copy; each robot type's recipe
    at the modes and in 20,000 draws (seed 1) with 02's `RecipeDraws`.
- **Result:**
  - 01 finds no fault.
  - Every recipe adds up to 1, at the modes and in every draw, and no element falls below zero.
  - Hand checks at the modes:
    - robot type 1's silicon: 0.2 × 9.07 + 0.8 × (0.32 × 0.160 + 0.68 × 0.60) = 2.18 %;
    - robot type 3's magnesium: 100 − (9 + 0.7 + 0.3 + 0.05 + 0.0025 + 0.015 + 0.001) = 89.93 %.
  - Both as drawn.
- **Not covered:**
  - ADC12, and the trace elements of AZ91D and AM60B, rest on the middle of the ranges (E).
  - Arconic's lab is registered to ISO 9001; whether its reference materials are accredited to ISO 17034 was not read.
  - Nothing is entered; E1.1c in the workbook is unchanged.

### V41. The proposed magnesium recipe, drawn in a sandbox

- **What:** the proposal of [EVIDENCE.md](EVIDENCE.md) E1.2c.
- **How:**
  - **The sources:** each analysis was read where it is published, and each is cited in E1.2c:
    - the PMC articles through the fetch tool;
    - the MDPI pages in the built-in browser;
    - the thesis and ICAST's datasheets through their text layer.
    - The OSTI report could not be reached.
  - **The shares:** the AM share was computed from the workbook's grade for every part.
  - **The proposal:** written into a scratch copy of `element_recipes.xlsx` (`magnesium_sandbox.py` in the session's
    scratch folder; the project unchanged).
  - **01's checks:** `check_element_recipes` and `check_material_recipes` were run on the copy.
  - **The draws:** each robot type's recipe was drawn 20,000 times (seed 1) with 02's `RecipeDraws`, and each was
    computed at the modes with 01's `element_shares`, for each AM alloy.
- **Result:**
  - 01 finds no fault.
  - Every recipe adds up to 1, at the modes and in every draw, and no element falls below zero.
  - Hand checks at the modes: robot type 2's aluminium is 0.43 × 5.71 + 0.57 × 8.56 = 7.335 %, and robot type 3's
    magnesium is 100 − 9.525 = 90.475 %, both as drawn.
- **Not covered:**
  - The AM share and the choice between AM60B and AM50A are estimates (E).
  - AM60B rests on one analysis without trace elements.
  - One of the three AZ91D analyses is not said to be the D grade.
  - Nothing is entered.

### V40. Magnesium: what the robots use, the sources and the car files

- **What:** the sources of [EVIDENCE.md](EVIDENCE.md) E1.2b, on Matthias's "Go on to magnesium: show me what the
  robots use and the sources first, verified on the web with references, and check the car composition files too."
- **How:**
  - **The project's own files:** the workbook's magnesium rows and every part naming magnesium were listed with 01's
    reader, and the reports in `documentation/sources/` were searched.
  - **The car files:** every `.xlsx` of the GitHub folder was searched for a magnesium sheet, and the five found were
    read. The two alloys' means were added up.
  - **The web:** each source was opened and read where it is published:
    - SURENA IV's full text on arXiv;
    - the JOM page and TechRadar's page in the built-in browser;
    - Magnecast, Dongrun and SMM through the fetch tool;
    - the TMS compilation rendered by PDFKit and read as images.
- **Result:**
  - Every grade a source about robots names is a casting alloy: AZ91 or AZ91D, AM60B, AM50A, and ZM5 on one
    unsourced page.
  - The producers' ingot limits (TMS) and the casting limits (ICAST, E1.2) agree as B93 against B94.
  - The car file's AZ91C-E adds up to 100.365 %, and its column "Co" is probably copper. Both were reported and not
    changed.
- **Not covered:**
  - ASTM B93 and B94 themselves.
  - Any grade from a robot maker.
  - Typical contents (analyses).
  - Nothing is proposed or entered.

### V39. The aluminium entry

- **What:** the recipe of [EVIDENCE.md](EVIDENCE.md) E1.1c, entered on Matthias's word: "Keep E1.1c as agreed and
  enter it now, as with the plastics and fibre composites."
- **How:**
  - **Tests first.** Two new tests, written before the data and the code; one failed, as it should.
    - The first reads the real workbook. It requires no fault from checks 15 and 17, and a row for every robot
      type's 'Aluminum alloys'. It also requires E1.1c's table at the modes, for each die-cast alloy, within 0.006
      percentage points, with lead only where ADC12 is chosen.
    - The second requires a plain name in 02 for every element 01 has an atomic mass for. It started guarding once
      01 had Zn, Sn and Pb, and failed until 02 named them.
  - **The data:** written by a throw-away script (`make_aluminium_entry.py` in the session's scratch folder). The
    workbook was first copied to the same folder (`element_recipes_before_aluminium.xlsx`), and the copy compared
    byte for byte. Added: 7 compounds, 65 recipe items, 6 rows.
  - **01 and 02:**
    - 01's check found that zinc, tin and lead had no atomic mass, before 01 got them (IUPAC CIAAW 2024: Zn 65.38,
      Sn 118.71, Pb 207.2);
    - check 17's text names aluminium;
    - 02 got the names zinc, tin and lead.
  - **The pages:**
    - 01 was drawn into the scratch folder before and after the entry, and all 20 pages compared byte for byte.
    - 02 and 03 were run with 2,000 draws into the scratch folder.
    - Robot type 1's page and 03's page by element were opened and read.
- **Result:**
  - 131 tests pass, none skipped. 01 finds no fault.
  - Of the 20 pages of 01, only faults.png changed: its check 17 now reads "so far aluminium, plastics and fibre
    composites", as read on the page.
  - In 02, aluminium is "In the elements: Yes" in every robot type. Robot type 1's elements now cover 21.0 of its
    35.0 kg of materials, against 9.05 before.
  - Robot type 1's Al is 11.19 kg: 11.97 kg of aluminium × about 92.9 %, plus about 0.07 kg of the cells' foils and
    tabs. Its zinc is 0.20 kg, about 1.6 % of the aluminium.
  - Robot type 5's copper is 1.21 kg: 0.87 kg of cells as before, plus 22 kg × about 1.5 %.
  - Every page fits: the 24 elements of 03 and the 24 rows of robot type 1's element chart.
- **Not covered:**
  - The real run (Matthias's).
  - The die-cast and 7075 shares stay estimates (E).
  - `figures/` was not redrawn.

### V38. The car projects' aluminium, against the registration records

- **What:** the aluminium compositions of `VehicleComposition/Data/14_…`, `15_…`, `22_…`, `34_…` and the `CastAl`
  sheet of RAWCLICVehicleTractionMotor and RAWCLICVehicleElectronics, on Matthias's "chek also there"
  ([EVIDENCE.md](EVIDENCE.md) E1.1d).
- **How:**
  - Every sheet's names were listed and every aluminium sheet was read with openpyxl, only reading.
  - The rows of 6061, 6063, 6005A, 6082, 5052, 5083, 7075, A380.0, A383.0 and A360.0 were compared, element by
    element, with the full text of the Teal and Pink Sheets read for V36.
  - The projects' `.py` and `.md` files were searched for a source of the sheets.
- **Result:**
  - All ten rows equal the records. The one exception is 6005A's condition on Mn + Cr, which the car file cannot
    hold.
  - No sheet names its source. The traction-motor project's audit names its housings "cast aluminium".
  - The aggregated compositions are envelopes over fixed mixes of alloys, not analyses.
- **Not covered:**
  - The 53 EN AC casting alloys: EN 1706 was not read.
  - The steels, cast irons, magnesium, boards, cables and magnets of the same files: listed in E1.1d, not checked.
  - Nothing in E1.1c is changed.

### V37. The proposed aluminium recipe, drawn in a sandbox

- **What:** the proposal of [EVIDENCE.md](EVIDENCE.md) E1.1c.
- **How:**
  - **The sources:** each analysis was read where it is published, and each is cited in E1.1c:
    - the Springer and journal tables in the built-in browser;
    - the PMC articles through the fetch tool;
    - the Gifu report through its text layer;
    - NIST's scanned certificate, rendered by macOS PDFKit and read as an image.
    - One site (springerprofessional.de) answered with a bot challenge and was left.
  - **The shares:** the 7075 share was computed from the workbook's grade for every part. The frames' mass against the
    aluminium rows was computed to bound the die-cast share.
  - **The proposal:** written into a scratch copy of `element_recipes.xlsx` (`aluminium_sandbox.py` in the session's
    scratch folder; the project unchanged). 01's atomic masses got Zn, Sn and Pb in the sandbox only.
  - **01's checks:** `check_element_recipes` and `check_material_recipes` were run on the copy.
  - **The draws:** each robot type's recipe was drawn 20,000 times (seed 1) with 02's `RecipeDraws`, and each was
    computed at the modes with 01's `element_shares`, for each die-cast alloy.
- **Result:**
  - 01 finds no fault.
  - Every recipe adds up to 1, at the modes and in every draw, and no element falls below zero. The tables are in
    E1.1c.
  - Hand check, robot type 1 at the modes with A380: silicon 0.2 × 9.146 + 0.8 × (0.32 × 0.18 + 0.68 × 0.66) =
    2.23 %, and zinc 0.2 × 0.60 + 0.8 × (0.32 × 5.7 + 0.68 × 0.02) = 1.59 %, as drawn.
- **Not covered:**
  - The die-cast and 7075 shares are estimates (E).
  - The elements of an alloy are drawn independently.
  - Three of the eleven analyses are of one research group (6061, two lots) or not production metal (the A380
    reference disk).
  - Nothing is entered.

### V36. Aluminium: the further alloys and their composition limits, read first-hand

- **What:** the sources of [EVIDENCE.md](EVIDENCE.md) E1.1b, for Matthias's comment that more aluminium alloys are
  used ("a more mixed approach").
- **How:**
  - **Where the alloys are used:** web searches, then each source opened and read. The three humanoid papers were
    read in their full text on arXiv (Berkeley §3.3, NING §III-A, Duke §III-A), the two manufacturers' guides on
    their pages, all through the fetch tool.
  - **The project's own files first:** the workbook's two sheets and the reports in `documentation/sources/` name
    only 6061-T6 and 7075-T6.
  - **The composition limits:** the Teal Sheets (December 2025, 5.8 MB) and the Pink Sheets (August 2025, 2.0 MB)
    were downloaded, on Matthias's yes, into the session's scratch folder, and their full text was read through
    macOS PDFKit. The rows taken: 6061, 6082, 7075, 5052, 5083; 380.0, A380.0, 383.0, A383.0, 384.0, A384.0,
    360.0, A360.0, all die castings (footnote 5). The footnotes that apply were read: 7075's footnote 10, the
    castings' footnotes 5 and 8. ADC12 was read on Yamaha Motor's page reproducing JIS H 5302:2006.
- **Result:**
  - The 6061 and 7075 rows equal those of E1.1.
  - ADC12's limits on Yamaha's page agree with those the search showed from ICAST and a Japanese bulletin.
  - Five sources name the alloys robots use: three research humanoids (machined 6061 and 7075) and two
    manufacturers' guides with a commercial interest (6082, 5052, 5083 and the die castings).
  - No anchor robot's alloy was found.
- **Not covered:**
  - The share of each alloy in each robot type: no source gives it.
  - A typical content inside each limit: the records give ranges and maxima only.
  - The standards themselves (JIS H 5302, EN 1706) were not read; JIS H 5302 through Yamaha's reproduction.
  - Nothing is proposed or entered.

### V35. The handover checked against the files and git

- **What:** the section "2026-10-26, end of the day" of HANDOVER.md, on Matthias's "Check the handover and then
  continue".
- **How:** each statement compared with what is on disk and in git:
  - `git status` and `git log`; the working tree against `origin/main`;
  - the files' modification times;
  - the folders `data/` and `figures/`;
  - the input files, and whether iCloud had evicted any (`stat -f %Sf`);
  - the test suite;
  - commit 557967b;
  - points 5 and 11 of SHARED_LISTS.md, and V23, V26 and V28;
  - the scratch folder;
  - `figures/schemas/overview.png`, opened.
- **Result:**
  - The working tree equals `origin/main` (7133c08), with nothing uncommitted.
  - 129 tests pass.
  - No output of 02 or 03 exists. The overview of 15:07 still says "Next … Not built yet", as stated.
  - Two statements were corrected:
    - "last commit 9a14f83" had been written before the handover's own commit;
    - the backups "may be gone": they are gone, because the scratch folder was empty.
- **Not covered:** the older sections of the handover, which are kept as they were written.

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
