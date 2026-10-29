# Verification and validation

Every check made on this project: what, how, against what, the result, the date, and what it does not cover. Written
by Claude, newest first.

## 2026-10-29

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
