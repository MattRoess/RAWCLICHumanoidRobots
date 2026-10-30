# RAWCLICHumanoidRobots

What a humanoid robot is made of, by category of humanoid robot, through 2040. The research of 2026 defines six
categories, from compact research robots to defense and public safety. Each category has one anchor robot, and
that robot's parts list stands for the category. Every mass in a parts list has a minimum, a mode and a maximum.

**New here? Start with [`documentation/claude/METHODOLOGY.md`](documentation/claude/METHODOLOGY.md)**, then open
the numbered scripts at the top of the project in order. Where the work stands is in
[`documentation/claude/HANDOVER.md`](documentation/claude/HANDOVER.md).

## Running it

Open the folder `RAWCLICHumanoidRobots` itself in Positron (File → Open Folder), not the GitHub folder above it,
so that the project's `.venv` is used. Then press Run on each stage, in order. None takes an argument; every
setting is in `src/params_schema.py`.

| Stage | Full path | What it does |
|---|---|---|
| 00 | `…/GitHub/RAWCLICHumanoidRobots/00_parameters.py` | Checks the settings, says which input files are on disk, writes `params.xlsx` and `documentation/claude/PARAMETER_REFERENCE.md`. |
| 01 | `…/GitHub/RAWCLICHumanoidRobots/01_schemas.py` | Reads and checks every input (the workbook, the shared lists, the element recipes, the register, each robot type's parts file, the sibling projects' files) and draws into `figures/schemas/`, every page 16 × 9 inches: the overview (how the model works; the six robot types), a notes page, the faults and checks, and for each robot type taken apart its robots and where its kinds of part sit (types 1 and 2 since 2026-10-30). Pages only of the robot types `output.robot_types_with_pages` names (types 1 and 2). |
| 02 | `…/GitHub/RAWCLICHumanoidRobots/02_composition.py` | Draws what each robot type is made of, `composition.draws` times (200,000; Monte Carlo): its materials, elements, part groups and body regions. A robot type some of whose robots are taken apart is drawn part by part over them (each draw one of them, a robot in two versions each as often, each from its own parts in its type's parts file): type 1 over all its robots, type 2 over the 53 of its batches 1, 2 and 2b. A type's draws for stock-and-flow come from its parts once every robot of it with a mass is taken apart (type 1), from the workbook until then (type 2) and for the other types. Writes each robot type's draws and summary into `data/consolidated/<n>_<name>/` for stock-and-flow and each type taken apart part by part into `data/parts_taken_apart/<n>_<name>/`. Draws, for the robot types `output.robot_types_with_pages` names (types 1 and 2): into `figures/composition/` a type taken apart its notes pages, its elements and its materials nine a page (the steels by grade, the aluminium by alloy, the magnets in all and by grade class; hydrogen, nitrogen, oxygen, fluorine, sodium, phosphorus and sulfur left off the element pages and kept in the draws, setting `composition.elements_not_shown`); into `figures/parts_taken_apart/<n>_<name>/` its two figures of where its critical elements sit, their notes once on pages of their own, and, in `sources/`, where copper, the magnets, each steel and each aluminium alloy sit. Stops on any fault of the inputs, before writing anything. |
| 03 | `…/GitHub/RAWCLICHumanoidRobots/03_comparison.py` | Reads the draws of 02 and draws the robot types side by side into `figures/comparison/`: by material, element (without the elements 02 leaves off), part group and body region. After robot type 6 (Matthias, 2026-10-29). |

`…` is `/Users/rm/Library/Mobile Documents/com~apple~CloudDocs/Documents`. Several projects have numbered files
with the same numbers: check that the file in front of you is in `RAWCLICHumanoidRobots` before pressing Run.

The tests run from a terminal in the project folder:

```bash
./.venv/bin/python -m unittest discover -s tests
```

## Layout

| Path | What it holds |
|---|---|
| `00_parameters.py` to `03_comparison.py` | The stages. Each says at its top what it reads, what it writes and where it sits. |
| `src/params_schema.py` | Every setting of the project, with what it does and why it has its value. |
| `src/params_io.py` | Writes the register of the settings. |
| `tools/make_humanoid_register.py` | Writes `data/researched/humanoid_register.xlsx`, the register of every known humanoid robot with its one or two robot types (sheet Robots), and every robot of types 1 and 2 with what 02's run does with it (sheets Type 1 and Type 2), from the catalogue in `data/raw/` and the decisions held in it (EVIDENCE.md E4 to E4.11). Not a stage. Press Run, no arguments; it replaces the file. A change to a decision is made in it, not in the `.xlsx`. |
| `tools/1_compact_research_developer/make_parts_taken_apart.py` | Writes `data/researched/1_compact_research_developer/parts_taken_apart.xlsx` with the values agreed in EVIDENCE.md E2.8 to E2.8e and E5 (every robot of type 1, one block each). Not a stage: it writes an input, not a result. Press Run, no arguments; it replaces the file. A change to the values is made in it, not in the `.xlsx`. |
| `tools/2_full_scale_general_purpose_ai_research/make_parts_taken_apart.py` | Writes `data/researched/2_full_scale_general_purpose_ai_research/parts_taken_apart.xlsx` with the values agreed in EVIDENCE.md E6.8, E7.5 and E8.3 (type 2's batch 1, five robots, the GR-1 in two versions; its batch 2, 24 robots, the H2-X in two versions; its batch 2b, 24 robots, the Walker Tienkung in two versions; one block each), and type 2's own template where a maker gives no joint torques (E7.4). As type 1's builder. |
| `tools/parts_taken_apart.py` | What the builders of the parts files share (one copy): the sheets' first rows, the sheets that are one set for all robots (MagnetGrades, the G1's weighed joint, Shares), the shared numbers and sources, the template where a source stops (with the function for a robot without joint torques, each type binding its own texts), and the functions that write a robot's block into its rows and the rows into a file. Not run by itself. |
| `tests/` | The tests of 00 to 03, and of the builders in `tools/`. |
| `data/raw/humanoid_robots_2040_workbook.xlsx` | The workbook the stages read. Matthias's, never changed. |
| `data/raw/humanoid_guide_2026-10-28.xlsx` | The humanoid.guide catalogue as read on 2026-10-28: 349 robots with their attribute tables, numbered in the order they were read. Second-hand; read, never changed. |
| `data/researched/humanoid_register.xlsx` | The register. Sheet Robots: every known humanoid robot (354), each with its robot types (at most two), its form, its mass as min, mode and max, or why it has no type. Sheet Type 1: every robot of type 1 (31), with every cell of its row in Robots and "In the run": drawn with its own parts. Sheet Type 2: every robot of type 2 (97): 53 "drawn: its own parts", 43 "not drawn: not yet taken apart" (all on wheels), one "not drawn: no mass stated". Written by `tools/make_humanoid_register.py`; 01 checks it; 02 draws each type taken apart over the robots of its sheet. |
| `data/researched/shared_lists.xlsx` | Where every part and material name goes in the shared part groups, body regions and materials, decided by Matthias on 2026-10-26. Corrected in Excel; 01 checks it. Its sheet Battery cells gives each robot type's battery as cells only. |
| `data/researched/element_recipes.xlsx` | The element recipes: the datasheets of the cells, the compounds, the NMC and LFP cylindrical cells, the plastics, the fibre composites, the aluminium and the magnesium alloys down to their elements, and which recipe each workbook row follows. Agreed by Matthias on 2026-10-26 and 2026-10-27; 01 checks it. |
| `data/researched/<n>_<name>/parts_taken_apart.xlsx` | Each robot type's robots part by part, in the type's folder (`data.parts_taken_apart`), each robot in its own rows (sheet Robots, column Robot): their joints and where they sit, the joint module part by part as China Post Securities weighed the G1's (scaled to each joint's mass), every other part, their materials and grades, boards and sensors. Type 1 (`1_compact_research_developer/`): its 31 robots of the register (the Booster K1 in two versions, 32 in all), the G1, X1 and N1 agreed by Matthias on 2026-10-27 (EVIDENCE.md E2.8 to E2.8e), the others on 2026-10-29 (E5). Type 2 (`2_full_scale_general_purpose_ai_research/`): its batch 1, five robots (the GR-1 in two versions), agreed on 2026-10-30 (E6.8), its batch 2, 24 robots (the H2-X in two versions), agreed the same day (E7.5), and its batch 2b, 24 robots (the Walker Tienkung in two versions; E8.3): 56 in all. Each written by its type's builder in `tools/<n>_<name>/`; 01 checks it, and its grades. |
| `data/consolidated/<n>_<name>/` | What 02 writes for each robot type, for stock-and-flow: the draws (`.npy`, float32, one row per draw, with their columns in `.txt`) and the summary. Outputs: rewritten by every run. |
| `figures/schemas/` | The pages 01 draws: the overview, the notes, the faults and checks, robot type 1's robots and robot page (a robot type whose steps have not begun, when named in `output.robot_types_with_pages`: its workbook page, its page in the shared lists and its robot in one view). Outputs: redrawn by every run. |
| `figures/composition/`, `figures/comparison/` | The pages of 02 (one per robot type) and of 03 (one per view). Outputs: redrawn by every run. |
| `data/parts_taken_apart/<n>_<name>/`, `figures/parts_taken_apart/<n>_<name>/` | What 02 writes of each robot type taken apart, part by part (`.npy`, float32, with their columns in `.txt`: the robots drawn, parts, materials, materials by grade, elements; a summary), and its figures of where the critical elements and each material sit. Outputs: rewritten by every run. |
| `params.xlsx` | The register of the settings. An output: editing it changes nothing. |
| `documentation/sources/` | Matthias's sources: the research reports, the earlier workbooks, the component diagram. |
| `documentation/claude/` | Written by Claude: how the model works, where the work stands, every check made. |
| `HumanoidRobotsMC/`, `data/02_HumanoidlRobots.xlsx` | The earlier Monte Carlo model of four robot classes, copied from the Empa folder on 2026-10-26. Not part of the stages; see the handover. |

## Setup

Python 3.14.4 from pyenv, in a virtual environment in the project folder. No conda.

```bash
~/.pyenv/versions/3.14.4/bin/python3 -m venv .venv
```

```bash
./.venv/bin/pip install -r requirements.txt
```

`.vscode/settings.json` makes `.venv` Positron's interpreter and activates it in every terminal. The versions in
`requirements.txt` are pinned; do not change them without asking.

## What is on GitHub

https://github.com/MattRoess/RAWCLICHumanoidRobots, public, branch `main`. It holds the code and the documents
only. Not in the repository, by `.gitignore`: the workbooks and every other `.xlsx`, everything the stages write
(the figures, the draws in `data/consolidated/` and `data/parts_taken_apart/`, `params.xlsx`, `documentation/claude/PARAMETER_REFERENCE.md`), and
the earlier model `HumanoidRobotsMC/`. A fresh clone cannot run 01 to 03 until `data/raw/humanoid_robots_2040_workbook.xlsx`,
`data/researched/shared_lists.xlsx` and `data/researched/element_recipes.xlsx` are supplied separately, and
each `data/researched/<n>_<name>/parts_taken_apart.xlsx` is written by pressing Run on its type's builder, `tools/<n>_<name>/make_parts_taken_apart.py`.

## Licence

Code and documentation: CC BY 4.0, Creative Commons Attribution 4.0 International. The full text is in
[`LICENSE`](LICENSE). Copyright © 2026 Empa, Matthias Roesslein. The licence does not cover the sources in
`documentation/sources/`, which were not written for this project.
