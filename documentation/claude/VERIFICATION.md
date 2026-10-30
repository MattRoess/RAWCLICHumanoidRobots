# Verification and validation

Every check made on this project: what, how, against what, the result, the date, and what it does not cover. Written
by Claude, newest first.

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
