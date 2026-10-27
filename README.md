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
| 01 | `…/GitHub/RAWCLICHumanoidRobots/01_schemas.py` | Reads and checks the workbook and the shared lists, and draws into `figures/schemas/`: the overview, three pages per robot type (workbook, shared lists, the robot in one view) and the faults. |
| 02 | `…/GitHub/RAWCLICHumanoidRobots/02_composition.py` | Draws what each robot type is made of, `composition.draws` times (200,000; Monte Carlo): its materials, elements, part groups and body regions. Writes each robot type's draws and summary into `data/consolidated/<n>_<name>/` for stock-and-flow, and a page per robot type into `figures/composition/`. Stops on any fault of the inputs, before writing anything. |
| 03 | `…/GitHub/RAWCLICHumanoidRobots/03_comparison.py` | Reads the draws of 02 and draws the robot types side by side into `figures/comparison/`: by material, element, part group and body region. |

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
| `tests/` | The tests of 00 to 03. |
| `data/raw/humanoid_robots_2040_workbook.xlsx` | The workbook the stages read. Matthias's, never changed. |
| `data/researched/shared_lists.xlsx` | Where every part and material name goes in the shared part groups, body regions and materials, decided by Matthias on 2026-10-26. Corrected in Excel; 01 checks it. Its sheet Battery cells gives each robot type's battery as cells only. |
| `data/researched/element_recipes.xlsx` | The element recipes: the datasheets of the cells, the compounds, the NMC and LFP cylindrical cells, the plastics, the fibre composites and the aluminium alloys down to their elements, and which recipe each workbook row follows. Agreed by Matthias on 2026-10-26 and 2026-10-27; 01 checks it. |
| `data/consolidated/<n>_<name>/` | What 02 writes for each robot type, for stock-and-flow: the draws (`.npy`, float32, one row per draw, with their columns in `.txt`) and the summary. Outputs: rewritten by every run. |
| `figures/schemas/` | The pages 01 draws: the overview, per robot type its workbook page, its page in the shared lists and its robot in one view, and the faults. Outputs: redrawn by every run. |
| `figures/composition/`, `figures/comparison/` | The pages of 02 (one per robot type) and of 03 (one per view). Outputs: redrawn by every run. |
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
(the figures, the draws in `data/consolidated/`, `params.xlsx`, `documentation/claude/PARAMETER_REFERENCE.md`), and
the earlier model `HumanoidRobotsMC/`. A fresh clone cannot run 01 to 03 until `data/raw/humanoid_robots_2040_workbook.xlsx`,
`data/researched/shared_lists.xlsx` and `data/researched/element_recipes.xlsx` are supplied separately.

## Licence

Code and documentation: CC BY 4.0, Creative Commons Attribution 4.0 International. The full text is in
[`LICENSE`](LICENSE). Copyright © 2026 Empa, Matthias Roesslein. The licence does not cover the sources in
`documentation/sources/`, which were not written for this project.
