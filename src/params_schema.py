"""
src/params_schema.py
====================

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

**EVERY SETTING FOR THIS PROJECT IS IN THIS FILE.** Open it, change a value, press Run on
`00_parameters.py`, then on the stages in order. Nothing is passed on a command line: no stage takes an
argument, because a switch that only exists on a command line is a switch the person running this never
sees.

`params.xlsx` and `documentation/claude/PARAMETER_REFERENCE.md` are OUTPUTS of this file. Editing either
of them changes nothing.

WHAT THIS PROJECT IS
--------------------
What a humanoid robot is made of, by category of humanoid robot, through 2040. The research of 2026
(`documentation/sources/00_overview_categories_market_shares_2040.md` and the category reports) defines
six categories, each with one anchor robot whose parts list stands for the category. Two stages exist:

  00_parameters.py     checks the settings in this file and writes the register of them.

  01_schemas.py        draws what the workbook defines, before anything is drawn at random: an
                       overview, per category its page, its page in the shared lists and its robot in one
                       view, and the faults found, into `figures/schemas/`.

The stages that compute the materials of each category are not built yet. Matthias, 2026-10-26: "Draw a
repective schema and the we will go through and do separate code for each of the different categories".

WHAT IS IN THIS FILE
--------------------
One small class per group of settings (`DataParams`, `CheckParams`, `OutputParams`), gathered in `Params`.
Each setting carries, in `metadata['doc']`, the one-line description that the register shows. `current()`
returns the settings in force after checking them; `flatten()` lists them for the register;
`source_status()` says which of the input files are on disk.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field, fields

# The project root: the folder above src/. Every relative path below is read from here, whatever the
# working folder of the run happens to be.
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class ParameterError(ValueError):
    """Raised when a setting in this file cannot be used as written."""


@dataclass
class DataParams:
    """The files the stages read. Paths are relative to the project root."""

    # The workbook of the 2026 research. Sheet 'Taxonomy' defines the six categories (what each is for, its
    # height, mass, joints and payload, its anchor robot); sheet 'Components & Materials' holds the parts
    # list of each anchor robot (per part the quantity, the mass of one unit and of all units as minimum,
    # mode and maximum in kg, the main material, the evidence). Matthias's workbook: read, never changed.
    # SAFE TO CHANGE: yes, when a newer workbook with the same sheets arrives under another name.
    workbook: str = field(
        default=os.path.join('data', 'raw', 'humanoid_robots_2040_workbook.xlsx'),
        metadata={'doc': 'The workbook of the 2026 research: the six categories and the parts list of '
                         'each anchor robot. Read, never changed.'})

    # The sheet of the workbook that defines the categories. Its first row is the header; one row per
    # category follows, numbered "1." to "6.".
    taxonomy_sheet: str = field(
        default='Taxonomy',
        metadata={'doc': 'The sheet that defines each category: what it is for, height, mass, joints, '
                         'payload, anchor robot.'})

    # The sheet of the workbook with the parts lists. Its header row starts with 'Category'; each
    # category's parts are closed by three rows: the sum of the parts, the stated mass of the anchor robot
    # and the difference between the two.
    components_sheet: str = field(
        default='Components & Materials',
        metadata={'doc': 'The sheet with the parts list of each anchor robot, closed per category by its '
                         'sum, the stated mass and their difference.'})

    # The sheet of the workbook with the materials of each anchor robot: per material its grade, minimum, mode and
    # maximum in kg, its share of the category and its evidence. Each category's materials are closed by their sum
    # and by the kilograms they leave unallocated against the parts list and against the stated mass.
    materials_sheet: str = field(
        default='Material Composition per Cat',
        metadata={'doc': 'The sheet with the materials of each anchor robot, closed per category by their sum '
                         'and the kilograms left unallocated.'})

    # Matthias's sources. 01_schemas.py looks here for the report of each category (a file whose name
    # starts with the category's number, as in 01_category_..., 02_category_...) and says on the category's
    # page whether there is one.
    # SAFE TO CHANGE: only if the sources move.
    sources_dir: str = field(
        default=os.path.join('documentation', 'sources'),
        metadata={'doc': "Matthias's sources; the schema looks here for each category's own report."})

    # Where every part and every material name of the workbook goes in the shared lists (part groups, body regions,
    # materials) that make the six robot types comparable. Decided by Matthias on 2026-10-26, point by point
    # (documentation/claude/SHARED_LISTS.md); written by Claude, to be corrected by Matthias in Excel.
    # 01_schemas.py checks every placement and draws one page per robot type from it.
    # SAFE TO CHANGE: only if the file moves.
    shared_lists: str = field(
        default=os.path.join('data', 'researched', 'shared_lists.xlsx'),
        metadata={'doc': 'Where every part and material name goes in the shared part groups, body regions and '
                         'materials.'})


@dataclass
class CheckParams:
    """How strictly the workbook is checked before it is drawn."""

    # Two numbers that should be equal (the mass of all units and the number times the mass of one; a sum
    # row and the sum of its parts) may differ by this much, in kg, before it counts as a fault. The
    # workbook stores some masses of one unit as long fractions (0.4090909... kg = 9 kg / 22), so a product
    # is exact only to about 0.00000001 kg. 0.001 kg (1 g) is far above that, and far below the lightest
    # part of the workbook (the depth camera of category 1, 0.08 kg at its minimum).
    # SAFE TO CHANGE: yes, within the limits that `current()` enforces (above 0, at most 0.01 kg).
    tolerance_kg: float = field(
        default=0.001,
        metadata={'doc': 'How far apart, in kg, two numbers that should be equal may be before the '
                         'schema reports a fault.'})


@dataclass
class OutputParams:
    """Where the stages write. Paths are relative to the project root."""

    # The pages of 01_schemas.py: overview.png, faults.png and categories/<n>_<name>.png.
    schemas_dir: str = field(
        default=os.path.join('figures', 'schemas'),
        metadata={'doc': 'Where 01_schemas.py draws the overview, one page per category and the '
                         'faults.'})

    # The resolution of every figure, in dots per inch. 150 keeps the text of a page sharp on a screen
    # and a page small enough to open quickly.
    dpi: int = field(
        default=150,
        metadata={'doc': 'Resolution of the figures in dots per inch.'})


@dataclass
class Params:
    """All settings of the project, one group per stage concern."""

    data: DataParams = field(default_factory=DataParams)
    checks: CheckParams = field(default_factory=CheckParams)
    output: OutputParams = field(default_factory=OutputParams)


def absolute(path: str) -> str:
    """A path of this file, relative to the project root, as an absolute path."""
    return os.path.join(ROOT, path)


def validate(params: Params) -> None:
    """Stop with a ParameterError, in plain words, when a setting cannot be used as written."""
    data = params.data
    for name in ('workbook', 'shared_lists'):
        if not getattr(data, name).lower().endswith('.xlsx'):
            raise ParameterError(f'data.{name} must be an .xlsx workbook, not {getattr(data, name)!r}.')
    for name in ('taxonomy_sheet', 'components_sheet', 'materials_sheet', 'sources_dir'):
        if not str(getattr(data, name)).strip():
            raise ParameterError(f'data.{name} is empty.')

    # Above 0, or every rounding difference would count as a fault; at most 0.01 kg, an eighth of the
    # lightest part (0.08 kg), so that a tolerance can never hide a whole part.
    tolerance = params.checks.tolerance_kg
    if not 0 < tolerance <= 0.01:
        raise ParameterError(f'checks.tolerance_kg must be above 0 and at most 0.01 kg, not {tolerance}.')

    if not str(params.output.schemas_dir).strip():
        raise ParameterError('output.schemas_dir is empty.')
    # Below 50 dpi the small print of a page cannot be read; above 600 a page takes megabytes and
    # seconds to open, for nothing a screen can show.
    if not 50 <= params.output.dpi <= 600:
        raise ParameterError(f'output.dpi must be between 50 and 600, not {params.output.dpi}.')


def current() -> Params:
    """The settings in force: the values written in this file, checked."""
    params = Params()
    validate(params)
    return params


def flatten(params: Params) -> list[tuple[str, str, str, object]]:
    """Every setting as (name, description, key, value), in the order of this file, for the register."""
    rows = []
    for section in fields(params):
        group = getattr(params, section.name)
        for item in fields(group):
            rows.append((item.name, item.metadata.get('doc', ''), f'{section.name}.{item.name}',
                         getattr(group, item.name)))
    return rows


def source_status(params: Params) -> str:
    """Which of the input files and folders are on disk, one line each."""
    lines = []
    for label, path in (('workbook', params.data.workbook), ('shared lists', params.data.shared_lists),
                        ('sources', params.data.sources_dir)):
        state = 'present' if os.path.exists(absolute(path)) else 'MISSING'
        lines.append(f'{label:<13} {path}: {state}')
    return '\n  '.join(lines)
