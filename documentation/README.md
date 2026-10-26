# Documentation

Two folders, so that one sees who contributed what:

- **[`sources/`](sources/)**: Matthias's sources, copied in by him or on his word. Not written for this project,
  and not covered by its licence.
- **[`claude/`](claude/)**: written by Claude for this project: how the model works, where the work stands, the
  check of every step, the settings.

**New here? Start with [`claude/METHODOLOGY.md`](claude/METHODOLOGY.md)**, then open the numbered scripts at the
top of the project in order.

## `claude/`: written by Claude

| File | What it is |
|---|---|
| [METHODOLOGY.md](claude/METHODOLOGY.md) | The model step by step: the stages, the workbook, the six categories, the checks, what the schemas show. |
| [HANDOVER.md](claude/HANDOVER.md) | Where the work stands, newest first: the decisions, who made them, what is open. |
| [EVIDENCE.md](claude/EVIDENCE.md) | The check of the inputs against sources outside the project: every web source with its URL, its kind, what was read and what it says. E1: the element recipes of the materials. |
| [VERIFICATION.md](claude/VERIFICATION.md) | Every verification and validation: what, how, against what, the result, the date, what it does not cover. |
| [PARAMETER_REFERENCE.md](claude/PARAMETER_REFERENCE.md) | Every setting and what it does. **Generated** by `00_parameters.py` from `src/params_schema.py`; do not edit. |
| [SHARED_LISTS.md](claude/SHARED_LISTS.md) | The shared part groups, body regions and materials that make the six robots comparable, with where each of the 68 parts and 35 material names goes. Decided by Matthias on 2026-10-26, point by point. The placements themselves are in `data/researched/shared_lists.xlsx`. |

## `sources/`: Matthias's sources

The workbook the stages read is not here. It is in `data/raw/humanoid_robots_2040_workbook.xlsx`, because a file
the code opens lives in `data/raw/`.

**The research of 2026 to 2040: six categories.** These were in the project folder before 2026-10-26. The overview
report names six categories; categories 1 to 4 have a report of their own, and categories 5 and 6 do not.

| File | What it is |
|---|---|
| `00_overview_categories_market_shares_2040.md`, `.pdf` | The six categories, their anchor robots, component and material trends, market outlook to 2040. |
| `01_category_compact_research_developer_components_materials_2040.md`, `.pdf` | Category 1, Compact Research & Developer. |
| `02_category_full_scale_general_purpose_ai_research_components_materials_2040.md`, `.pdf` | Category 2, Full-Scale General-Purpose / AI Research. |
| `03_category_industrial_logistics_warehousing_components_materials_2040.md`, `.pdf` | Category 3, Industrial Logistics & Warehousing. |
| `04_category_service_healthcare_interaction_components_materials_2040.md`, `.pdf` | Category 4, Service / Healthcare / Interaction. |

**The earlier research: four robot classes, HRC-1 to HRC-4.** Copied on 2026-10-26 from
`Empa/RAWCLIC/Robots/HumanoidRobots/humanoid_robot_research/`, dated 2026-04-20 to 2026-05-07. Most reports come
as `.md`, `.pdf` and `*_original.md`.

| File | What it is |
|---|---|
| `01_robot_classes_and_comparison` | The four classes and how they compare. |
| `02_architecture_materials_actuators_dof_hands` | Architecture, materials, actuators, degrees of freedom, hands. |
| `03_batteries_controllers_sensors_lifetime` | Batteries, controllers, sensors, lifetime. |
| `04_global_landscape_europe_policy_market` | Global landscape, Europe, policy, market. |
| `classification_and_material_weights` | The classification and the material weights. |
| `detailed_motors_sensors_controllers_materials` | Motors, sensors and controllers in detail. |
| `humanoid_robot_materials_and_components_report` | The materials and components report. |
| `humanoid_robot_material_weights.xlsx` | Workbook: material weights by class. |
| `humanoid_robots_comprehensive_workbook.xlsx` | Workbook: components and materials of the four classes. |

**The diagram.** Copied on 2026-10-26 from `Empa/RAWCLIC/_robots/`.

| File | What it is |
|---|---|
| `ComponentHumanoidRobots.png`, `.graffle` | The component diagram of a humanoid robot, and its OmniGraffle source. |
