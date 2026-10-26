"""
Tests of 01_schemas.py, the schema of each category of humanoid robot.

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

Matthias, 2026-10-26: "Draw a repective schema and the we will go through and do separate code for each
of the different categories."

Most tests build a small workbook of their own, in the layout of
data/raw/humanoid_robots_2040_workbook.xlsx (two categories, three parts), break one thing in it and
check that 01 reports exactly that fault: a check is only trusted once it has been seen to catch what it
guards. One test reads the real workbook and is skipped without it. Everything is written into temporary
folders: press Run, nothing in the project is changed.
"""

import glob
import importlib.util
import os
import re
import sys
import tempfile
import unittest

from openpyxl import Workbook
from openpyxl.styles import PatternFill

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
_spec = importlib.util.spec_from_file_location('schemas', os.path.join(ROOT, '01_schemas.py'))
schemas = importlib.util.module_from_spec(_spec)
sys.modules['schemas'] = schemas  # the dataclasses of 01 look their module up here while it loads
_spec.loader.exec_module(schemas)

from src.params_schema import Params, absolute  # noqa: E402

HEADER = ['Category', 'BOM Anchor Robot', 'Subsystem', 'Component', 'Location / Joint', 'Qty',
          'Per-Unit Min (kg)', 'Per-Unit Mode (kg)', 'Per-Unit Max (kg)', 'Total Min (kg)', 'Total Mode (kg)',
          'Total Max (kg)', 'Primary Material Grade', 'Secondary / Mixed Material', 'EU Critical Raw Material',
          'Evidence', 'Source Reference']
D = '—'  # the workbook's dash for "not applicable"

# The small workbook: (category, anchor, subsystem, component, location, quantity, mass of one min/mode/max,
# mass of all min/mode/max, material, evidence). Category 1: two parts; category 2: one part, and an anchor
# robot that is 1 kg lighter than its parts. The header is row 3, so the rows below are rows 4 to 12.
ROWS = [
    ('1. Small', 'Robot A', 'Actuation', 'Knee actuator', 'Knees', 2, 1, 2, 3, 2, 4, 6, 'Aluminium', 'Estimate'),
    ('1. Small', 'Robot A', 'Structure', 'Frame', 'Torso', 1, 0.5, 1, 1.5, 0.5, 1, 1.5, 'Steel', 'Direct'),
    ('1. Small', 'Robot A', 'CATEGORY SUBTOTAL', 'Subtotal', 'All', 3, D, D, D, 2.5, 5, 7.5, 'Sum', 'Derived'),
    ('1. Small', 'Robot A', 'REPORTED ANCHOR MASS', 'Stated mass', 'Robot', 1, D, 5, D, D, 5, D, 'Spec', 'Direct'),
    ('1. Small', 'Robot A', 'RECONCILIATION CHECK', 'Difference', 'Check', D, D, D, D, D, 0, 0, 'K, L', 'Derived'),
    ('2. Large', "Notional 'B'", 'Energy', 'Battery', 'Torso', 4, 1, 1.5, 2, 4, 6, 8, 'Lithium cells', 'Derived'),
    ('2. Large', "Notional 'B'", 'CATEGORY SUBTOTAL', 'Subtotal', 'All', 4, D, D, D, 4, 6, 8, 'Sum', 'Derived'),
    ('2. Large', "Notional 'B'", 'REPORTED ANCHOR MASS', 'Stated mass', 'Robot', 1, D, 5, D, D, 5, D, 'Spec',
     'Estimate'),
    ('2. Large', "Notional 'B'", 'RECONCILIATION CHECK', 'Difference', 'Check', D, D, D, D, D, 1, 0.2, 'K, L',
     'Derived'),
]
GRAND = ('ALL 2 CATEGORIES', '2 robots', 'GRAND TOTAL (SUM OF 2 ANCHORS)', 'Sum', 'All', 7, D, D, D, 6.5, 11,
         15.5, 'Sum', 'Derived')
FILLS = {'Derived': 'FFFFF2CC', 'Estimate': 'FFFCE4D6'}   # Direct has no fill, as in the workbook's key
COLUMN = {name: i + 1 for i, name in enumerate(HEADER)}

# The materials of the small workbook, in the layout of 'Material Composition per Cat': (category, anchor, family,
# grade, minimum, mode, maximum, share, evidence). Category 1: 5 kg at the mode, all of its parts list; category
# 2: 4 kg, which leaves 2 kg of its 6 kg parts list and 1 kg of its 5 kg stated mass unallocated. The header is
# row 3, so the rows below are rows 4 to 10.
MATERIAL_HEADER = ['Category', 'BOM Anchor Robot', 'Material Family', 'Proposed Grade / Specification',
                   'Principal Allocation / Subsystem Role', 'Min (kg)', 'Mode (kg)', 'Max (kg)',
                   'Share of Category Material Mode (%)', 'Evidence', 'Source Reference']
MATERIAL_ROWS = [
    ('1. Small', 'Robot A', 'Aluminum alloys', 'Al 6061', 2, 3, 4.5, 0.6, 'Estimate'),
    ('1. Small', 'Robot A', 'Copper conductors', 'Copper', 1, 2, 3, 0.4, 'Estimate'),
    ('1. Small', 'Robot A', 'CATEGORY MATERIAL SUBTOTAL', 'Sum', 3, 5, 7.5, 1, 'Derived'),
    ('1. Small', 'Robot A', 'UNALLOCATED MATERIAL RESIDUAL', 'Gap', D, 0, 0, 1, 'Derived'),
    ('2. Large', "Notional 'B'", 'Battery materials', 'NMC', 3, 4, 5, 1, 'Estimate'),
    ('2. Large', "Notional 'B'", 'CATEGORY MATERIAL SUBTOTAL', 'Sum', 3, 4, 5, 1, 'Derived'),
    ('2. Large', "Notional 'B'", 'UNALLOCATED MATERIAL RESIDUAL', 'Gap', D, 2, 1, 1, 'Derived'),
]
MATERIAL_COLUMN = {name: i + 1 for i, name in enumerate(MATERIAL_HEADER)}

# The shared lists of the small workbook, in the layout of data/researched/shared_lists.xlsx.
LISTS = [('Part group', 'Joint drives'), ('Part group', 'Frame'), ('Part group', 'Battery'),
         ('Part group', 'Mixed'), ('Body region', 'Legs'), ('Body region', 'Torso'), ('Body region', 'Whole body'),
         ('Material', 'Aluminium'), ('Material', 'Copper'), ('Material', 'Battery materials'),
         ('Material', 'Mixed'), ('Material', 'Not allocated')]
PLACED_PARTS = [(1, 4, 'Knee actuator', 'Joint drives', 'Legs', '', 2, 'The location names one region.'),
                (1, 5, 'Frame', 'Frame', 'Whole body', '', 0, 'Spread over the body.'),
                (2, 9, 'Battery', 'Battery', 'Torso', '', 0, 'The location names one region.')]
PLACED_MATERIALS = [('Aluminum alloys', 'Aluminium', 'The name says the material.'),
                    ('Copper conductors', 'Copper', 'The name says the material.'),
                    ('Battery materials', 'Battery materials', 'The name says the material.')]


def build_lists(path, parts=None, materials=None, lists=None, splits=None):
    """Write small shared lists to `path`: the rows of LISTS, PLACED_PARTS and PLACED_MATERIALS, or the ones
    given instead, and a sheet Splits with the rows of `splits` when it is given."""
    book = Workbook()
    sheet = book.active
    sheet.title = 'Lists'
    sheet.append(['List', 'Name', 'What it holds'])
    for kind, name in LISTS if lists is None else lists:
        sheet.append([kind, name, 'For the tests.'])
    sheet = book.create_sheet('Parts')
    sheet.append(['Robot type', 'Row', 'Part', 'Part group', 'Body region', 'Split by units', 'Motors', 'Why'])
    for row in PLACED_PARTS if parts is None else parts:
        sheet.append(list(row))
    sheet = book.create_sheet('Materials')
    sheet.append(['Material name in the workbook', 'Shared material', 'Why'])
    for row in PLACED_MATERIALS if materials is None else materials:
        sheet.append(list(row))
    if splits is not None:
        sheet = book.create_sheet('Splits')
        sheet.append(['Robot type', 'Material name in the workbook', 'Shared material', 'Share min', 'Share mode',
                      'Share max', 'Remainder', 'Label', 'Basis', 'Decided'])
        for row in splits:
            sheet.append(list(row))
    book.save(path)


def build(path, changes=None, taxonomy=None, coverage=3, material_changes=None):
    """Write the small workbook to `path`; `changes` maps (row, heading) of the parts to a value that replaces
    the one of ROWS, or to ('fill', ARGB) to recolour the row; `material_changes` does the same for
    MATERIAL_ROWS."""
    changes = changes or {}
    book = Workbook()
    sheet = book.active
    sheet.title = 'Taxonomy'
    sheet.append(['Category', 'Dominant Requirement & Definition', 'Working Boundary (Height & Mass)',
                  'Articulation (DoF) & Payload', 'BOM Anchor Robot'])
    for row in taxonomy or [('1. Small', 'For the tests.', 'Height: 1 m', 'DoF: 20', 'Robot A'),
                            ('2. Large', 'For the tests.', 'Height: 2 m', 'DoF: 40', "Notional 'B'")]:
        sheet.append(list(row))
    parts = book.create_sheet('Components & Materials')
    parts.append(['COMPONENT & MATERIAL BREAKDOWN'])
    parts.append([f'COVERAGE: {coverage} leaf component assemblies'])
    parts.append(HEADER)
    for values in ROWS + [GRAND]:
        cells = list(values[:13]) + ['', 'Yes', values[13], '[S01]']
        parts.append(cells)
        r = parts.max_row
        fill = FILLS.get(values[13])
        for (row, heading), value in changes.items():
            if row != r:
                continue
            if isinstance(value, tuple) and value[0] == 'fill':
                fill = value[1]
            else:
                parts.cell(row=r, column=COLUMN[heading], value=value)
        if fill:
            parts.cell(row=r, column=COLUMN['Component']).fill = PatternFill('solid', fgColor=fill)

    sheet = book.create_sheet('Material Composition per Cat')
    sheet.append(['MATERIAL COMPOSITION PER CATEGORY'])
    sheet.append(['NOTE: for the tests.'])
    sheet.append(MATERIAL_HEADER)
    for values in MATERIAL_ROWS:
        sheet.append(list(values[:4]) + ['For the tests.'] + list(values[4:]) + ['[S01]'])
        r = sheet.max_row
        fill = FILLS.get(values[8])
        for (row, heading), value in (material_changes or {}).items():
            if row != r:
                continue
            if isinstance(value, tuple) and value[0] == 'fill':
                fill = value[1]
            else:
                sheet.cell(row=r, column=MATERIAL_COLUMN[heading], value=value)
        sheet.cell(row=r, column=MATERIAL_COLUMN['Material Family']).fill = PatternFill('solid', fgColor=fill)
    book.save(path)


class Small(unittest.TestCase):
    """Builds, reads and checks the small workbook; each test changes one thing."""

    def faults(self, changes=None, **options):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, 'small.xlsx')
            build(path, changes, **options)
            self.book = schemas.read_workbook(path, Params())
        return schemas.check_workbook(self.book, Params())

    def assertOneFault(self, faults, row, words):
        self.assertEqual(len(faults), 1, [f.text for f in faults])
        self.assertEqual(faults[0].row, row)
        self.assertIn(words, faults[0].text)


class TestReading(Small):

    def test_the_small_workbook_is_read_without_fault(self):
        self.assertEqual(self.faults(), [])
        self.assertEqual([c.number for c in self.book.categories], [1, 2])
        self.assertEqual([len(pl.parts) for pl in self.book.parts_lists.values()], [2, 1])
        small = self.book.parts_lists[1]
        self.assertEqual((small.sum_row, small.stated_row, small.difference_row), (6, 7, 8))
        self.assertEqual(small.parts[0].total_kg, (2, 4, 6))
        self.assertEqual(self.book.parts_lists[2].difference_share, 0.2)

    def test_the_notional_anchor_is_recognised(self):
        self.faults()
        self.assertTrue(schemas.is_notional(self.book.categories[1].anchor))
        self.assertFalse(schemas.is_notional(self.book.categories[0].anchor))


class TestFaults(Small):
    """Each check, seen to catch the fault it guards and nothing else."""

    def test_a_minimum_above_the_mode(self):
        faults = self.faults({(4, 'Per-Unit Min (kg)'): 2.5, (4, 'Total Min (kg)'): 5,
                              (6, 'Total Min (kg)'): 5.5, (13, 'Total Min (kg)'): 9.5})
        self.assertEqual(len(faults), 2, [f.text for f in faults])
        self.assertTrue(all(f.row == 4 and 'not in order' in f.text for f in faults))

    def test_a_mass_of_all_units_that_is_not_the_number_times_one(self):
        faults = self.faults({(4, 'Total Max (kg)'): 7, (6, 'Total Max (kg)'): 8.5, (13, 'Total Max (kg)'): 16.5})
        self.assertOneFault(faults, 4, 'is not the number 2 times the mass of one, 3 kg')

    def test_a_missing_mass(self):
        faults = self.faults({(5, 'Per-Unit Mode (kg)'): D})
        self.assertOneFault(faults, 5, 'the mode of the mass of one unit is missing')

    def test_a_sum_row_that_disagrees_with_its_parts(self):
        # The materials' unallocated row is measured against the sum row, so it moves with it.
        faults = self.faults({(6, 'Total Mode (kg)'): 5.5, (8, 'Total Mode (kg)'): 0.5, (13, 'Total Mode (kg)'): 11.5,
                              (8, 'Total Max (kg)'): 0.1}, material_changes={(7, 'Mode (kg)'): 0.5})
        self.assertOneFault(faults, 6, 'the mode of the parts adds up to 5 kg, but the sum row says 5.5 kg')

    def test_a_sum_row_with_the_wrong_number_of_units(self):
        faults = self.faults({(6, 'Qty'): 4, (13, 'Qty'): 8})
        self.assertOneFault(faults, 6, 'the parts add up to 3 units, but the sum row says 4')

    def test_a_difference_row_that_disagrees(self):
        faults = self.faults({(12, 'Total Mode (kg)'): 2})
        self.assertOneFault(faults, 12, 'the difference row says 2 kg')

    def test_a_difference_share_that_disagrees(self):
        faults = self.faults({(12, 'Total Max (kg)'): 0.25})
        self.assertOneFault(faults, 12, 'the difference row says 25.00% of the stated mass')

    def test_a_row_coloured_against_its_evidence(self):
        faults = self.faults({(5, 'Component'): ('fill', 'FFFCE4D6')})
        self.assertOneFault(faults, 5, 'its evidence, Direct, is coloured without fill')

    def test_an_evidence_that_is_not_in_the_key(self):
        faults = self.faults({(5, 'Evidence'): 'Measured'})
        self.assertOneFault(faults, 5, "the evidence 'Measured' is not one of")

    def test_a_last_row_that_disagrees_with_the_sum_rows(self):
        faults = self.faults({(13, 'Total Max (kg)'): 15})
        self.assertOneFault(faults, 13, 'the maximum of the sum rows adds up to 15.5 kg')

    def test_a_stated_number_of_parts_that_disagrees(self):
        faults = self.faults(coverage=4)
        self.assertOneFault(faults, 0, 'states 4 parts, but the sheet lists 3')

    def test_a_category_named_differently_in_the_two_sheets(self):
        # Once for the parts and once for the materials: both sheets name the category.
        faults = self.faults(taxonomy=[('1. Smaller', 'x', 'x', 'x', 'Robot A'),
                                       ('2. Large', 'x', 'x', 'x', "Notional 'B'")])
        self.assertEqual(sorted(f.sheet for f in faults), ['Components & Materials', 'Material Composition per Cat'])
        self.assertTrue(all("category 1 is called 'Smaller'" in f.text for f in faults))

    def test_a_category_without_a_parts_list(self):
        faults = self.faults(taxonomy=[('1. Small', 'x', 'x', 'x', 'A'), ('2. Large', 'x', 'x', 'x', 'B'),
                                       ('3. Extra', 'x', 'x', 'x', 'C')])
        self.assertEqual(len(faults), 2, [f.text for f in faults])
        self.assertIn('category 3 is in this sheet but has no parts list', faults[0].text)
        self.assertIn('category 3 is in this sheet but has no materials', faults[1].text)


class TestPages(Small):

    def test_every_page_is_drawn_also_with_a_fault(self):
        faults = self.faults({(4, 'Total Max (kg)'): 7, (6, 'Total Max (kg)'): 8.5, (13, 'Total Max (kg)'): 16.5})
        params = Params()
        with tempfile.TemporaryDirectory() as folder:
            reports = {1: '01_category_small_components.md', 2: None}
            schemas.draw_overview(self.book, faults, reports, os.path.join(folder, 'overview.png'), params)
            for category in self.book.categories:
                schemas.draw_category(category, self.book.parts_lists[category.number], reports[category.number],
                                      faults, os.path.join(folder, 'categories', schemas.file_name(category)),
                                      params)
            schemas.draw_faults(faults, os.path.join(folder, 'faults.png'), params)
            drawn = sorted(os.path.relpath(p, folder) for p in glob.glob(os.path.join(folder, '**', '*.png'),
                                                                         recursive=True))
        self.assertEqual(drawn, ['categories/1_small.png', 'categories/2_large.png', 'faults.png',
                                 'overview.png'])

    def test_a_subsystem_split_in_the_sheet_is_shown_once(self):
        part = lambda row, subsystem: schemas.Part(row, subsystem, f'part {row}', '', 1, (1, 1, 1), (1, 1, 1),  # noqa: E731
                                                   '', 'Direct', None, '')
        groups = schemas.by_subsystem([part(1, 'Structure'), part(2, 'Energy'), part(3, 'Structure')])
        self.assertEqual([(name, [p.row for p in members]) for name, members in groups],
                         [('Structure', [1, 3]), ('Energy', [2])])

    def test_a_long_file_name_is_broken_after_underscores(self):
        lines = schemas.wrap_name('Report: ', '01_category_compact_research_developer_components_2040.md', 30)
        self.assertEqual(''.join(lines).replace('Report: ', ''), '01_category_compact_research_developer_'
                                                                  'components_2040.md')
        self.assertTrue(all(len(line) <= 30 for line in lines))
        self.assertTrue(all(line.endswith('_') for line in lines[:-1]))

    def test_the_overview_names_every_stage_of_the_project(self):
        files = sorted(os.path.basename(p) for p in glob.glob(os.path.join(ROOT, '[0-9][0-9]_*.py')))
        self.assertEqual([name for name, _ in schemas.STAGES], files)


class TestMaterialFaults(Small):
    """The checks of the sheet 'Material Composition per Cat', each seen to catch the fault it guards."""

    def test_a_materials_sum_row_that_disagrees(self):
        faults = self.faults(material_changes={(6, 'Max (kg)'): 8})
        self.assertOneFault(faults, 6, 'the maximum of the materials adds up to 7.5 kg, but the sum row says 8 kg')

    def test_a_share_that_disagrees(self):
        faults = self.faults(material_changes={(4, 'Share of Category Material Mode (%)'): 0.5})
        self.assertOneFault(faults, 4, 'Aluminum alloys: the share says 50.00%, but its mode is 60.00% of the sum')

    def test_an_unallocated_row_that_disagrees_with_the_parts(self):
        faults = self.faults(material_changes={(10, 'Mode (kg)'): 3})
        self.assertOneFault(faults, 10, "the unallocated row says 3 kg against the parts' sum")

    def test_an_unallocated_row_that_disagrees_with_the_stated_mass(self):
        faults = self.faults(material_changes={(10, 'Max (kg)'): 2})
        self.assertOneFault(faults, 10, 'the unallocated row says 2 kg against the stated mass')

    def test_a_material_out_of_order(self):
        faults = self.faults(material_changes={(5, 'Min (kg)'): 2.5, (6, 'Min (kg)'): 4.5})
        self.assertOneFault(faults, 5, 'Copper conductors: not in order')

    def test_a_material_coloured_against_its_evidence(self):
        faults = self.faults(material_changes={(4, 'Material Family'): ('fill', 'FFFFF2CC')})
        self.assertOneFault(faults, 4, 'its evidence, Estimate, is coloured FFFCE4D6')


class SmallLists(Small):
    """Builds the small workbook and its shared lists, and checks both."""

    def lists_faults(self, parts=None, materials=None, lists=None, splits=None):
        with tempfile.TemporaryDirectory() as folder:
            build(os.path.join(folder, 'small.xlsx'))
            build_lists(os.path.join(folder, 'lists.xlsx'), parts, materials, lists, splits)
            self.book = schemas.read_workbook(os.path.join(folder, 'small.xlsx'), Params())
            self.lists = schemas.read_shared_lists(os.path.join(folder, 'lists.xlsx'))
        return schemas.check_workbook(self.book, Params()) + schemas.check_shared_lists(self.book, self.lists,
                                                                                         Params())

    def assertFaultSays(self, faults, words):
        self.assertEqual(len(faults), 1, [f.text for f in faults])
        self.assertIn(words, faults[0].text)


class TestSharedLists(SmallLists):

    def test_the_small_lists_are_read_without_fault_and_add_up(self):
        self.assertEqual(self.lists_faults(), [])
        one, two = self.book.parts_lists[1], self.book.parts_lists[2]
        self.assertEqual(schemas.by_view(one, self.lists, 'group'), {'Joint drives': 4, 'Frame': 1})
        self.assertEqual(schemas.by_view(one, self.lists, 'region'), {'Legs': 4, 'Whole body': 1})
        self.assertEqual(schemas.by_material(self.book.materials_lists[1], self.lists), {'Aluminium': 3, 'Copper': 2})
        self.assertEqual(schemas.by_material(self.book.materials_lists[2], self.lists),
                         {'Battery materials': 4, 'Not allocated': 2})
        self.assertEqual(schemas.motors_of(one, self.lists), 2)
        self.assertEqual(schemas.motors_of(two, self.lists), 0)

    def test_a_split_counts_the_mass_of_one_unit_per_unit(self):
        parts = [(1, 4, 'Knee actuator', 'Joint drives', '', 'Legs 1; Torso 1', 2, 'Split.')] + PLACED_PARTS[1:]
        self.assertEqual(self.lists_faults(parts), [])
        regions = schemas.by_view(self.book.parts_lists[1], self.lists, 'region')
        self.assertEqual(regions, {'Legs': 2, 'Torso': 2, 'Whole body': 1})

    def test_a_part_not_placed(self):
        self.assertFaultSays(self.lists_faults(PLACED_PARTS[:1] + PLACED_PARTS[2:]), 'Frame (row 5')

    def test_a_part_placed_twice(self):
        self.assertFaultSays(self.lists_faults(PLACED_PARTS + PLACED_PARTS[:1]), 'placed a second time')

    def test_a_part_under_another_name(self):
        parts = [(1, 4, 'Knee motor', 'Joint drives', 'Legs', '', 2, '')] + PLACED_PARTS[1:]
        self.assertFaultSays(self.lists_faults(parts), "row 4 is 'Knee actuator' in the workbook, not 'Knee motor'")

    def test_a_part_under_another_robot_type(self):
        parts = [(2, 4, 'Knee actuator', 'Joint drives', 'Legs', '', 2, '')] + PLACED_PARTS[1:]
        self.assertFaultSays(self.lists_faults(parts), 'robot type 2, but the workbook has it in 1')

    def test_a_part_group_not_in_the_lists(self):
        parts = [(1, 4, 'Knee actuator', 'Motors', 'Legs', '', 2, '')] + PLACED_PARTS[1:]
        self.assertFaultSays(self.lists_faults(parts), "the part group 'Motors' is not in the sheet Lists")

    def test_a_body_region_not_in_the_lists(self):
        parts = [(1, 4, 'Knee actuator', 'Joint drives', 'Feet', '', 2, '')] + PLACED_PARTS[1:]
        self.assertFaultSays(self.lists_faults(parts), "the body region 'Feet' is not in the sheet Lists")

    def test_a_region_and_a_split_at_once(self):
        parts = [(1, 4, 'Knee actuator', 'Joint drives', 'Legs', 'Legs 2', 2, '')] + PLACED_PARTS[1:]
        self.assertFaultSays(self.lists_faults(parts), 'give either one body region or a split by units')

    def test_a_split_that_does_not_add_up(self):
        parts = [(1, 4, 'Knee actuator', 'Joint drives', '', 'Legs 1; Torso 2', 2, '')] + PLACED_PARTS[1:]
        self.assertFaultSays(self.lists_faults(parts), 'the split adds up to 3 units, but the part has 2')

    def test_more_motors_than_units(self):
        parts = [(1, 4, 'Knee actuator', 'Joint drives', 'Legs', '', 3, '')] + PLACED_PARTS[1:]
        self.assertFaultSays(self.lists_faults(parts), 'the number of motors must be a whole number from 0 to its 2')

    def test_a_material_name_not_placed(self):
        self.assertFaultSays(self.lists_faults(materials=PLACED_MATERIALS[:1] + PLACED_MATERIALS[2:]),
                             "'Copper conductors'")

    def test_a_shared_material_not_in_the_lists(self):
        materials = [('Aluminum alloys', 'Brass', '')] + PLACED_MATERIALS[1:]
        self.assertFaultSays(self.lists_faults(materials=materials), "the shared material 'Brass' is not")

    def test_a_material_placed_in_not_allocated(self):
        materials = [('Aluminum alloys', 'Not allocated', '')] + PLACED_MATERIALS[1:]
        self.assertFaultSays(self.lists_faults(materials=materials), "the shared material 'Not allocated'")

    def test_a_material_name_the_workbook_does_not_have(self):
        materials = PLACED_MATERIALS + [('Gold', 'Copper', '')]
        self.assertFaultSays(self.lists_faults(materials=materials), "'Gold' is not a material name of the workbook")

    def test_the_page_of_a_robot_type_is_drawn(self):
        self.lists_faults()
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, 'categories', '1_small_shared_lists.png')
            schemas.draw_shared_lists(self.book.categories[0], self.book.parts_lists[1],
                                      self.book.materials_lists[1], self.lists, [], path, Params())
            self.assertTrue(os.path.exists(path))


class TestSplits(SmallLists):
    """A material name split by an estimate (point 9 of SHARED_LISTS.md). In the small workbook, robot type 1's
    'Copper conductors' (1 / 2 / 3 kg) is split into electronics (10 / 20 / 30 %) and copper as the remainder."""

    LISTS = LISTS + [('Material', 'Electronics')]
    MATERIALS = [PLACED_MATERIALS[0], ('Copper conductors', 'Split', 'Point 9.'), PLACED_MATERIALS[2]]
    SPLIT = [(1, 'Copper conductors', 'Electronics', 0.1, 0.2, 0.3, '', 'E', 'Basis.', 'Decided.'),
             (1, 'Copper conductors', 'Copper', None, None, None, 'Yes', 'E', 'The rest.', 'Decided.')]

    def split_faults(self, splits=None, materials=None):
        return self.lists_faults(materials=self.MATERIALS if materials is None else materials, lists=self.LISTS,
                                 splits=self.SPLIT if splits is None else splits)

    def test_a_split_is_read_and_adds_back_to_the_material(self):
        self.assertEqual(self.split_faults(), [])
        materials = self.book.materials_lists[1]
        totals = schemas.by_material(materials, self.lists)
        self.assertEqual(set(totals), {'Aluminium', 'Copper', 'Electronics'})
        self.assertAlmostEqual(totals['Electronics'], 0.4)
        self.assertAlmostEqual(totals['Copper'], 1.6)
        self.assertAlmostEqual(sum(totals.values()), 5)
        rows = schemas.material_rows(materials, self.lists)
        for name, expected in (('Electronics', (0.1, 0.4, 0.9)), ('Copper', (0.7, 1.6, 2.7))):
            for got, want in zip(rows[name][0], expected):
                self.assertAlmostEqual(got, want, msg=name)

    def test_a_split_without_a_remainder(self):
        self.assertFaultSays(self.split_faults(self.SPLIT[:1]), 'exactly one remainder, not 0')

    def test_a_split_with_two_remainders(self):
        two = [self.SPLIT[1], (1, 'Copper conductors', 'Electronics', None, None, None, 'Yes', 'E', '', '')]
        self.assertFaultSays(self.split_faults(two), 'exactly one remainder, not 2')

    def test_shares_out_of_order(self):
        rows = [(1, 'Copper conductors', 'Electronics', 0.3, 0.2, 0.4, '', 'E', '', ''), self.SPLIT[1]]
        self.assertFaultSays(self.split_faults(rows), 'the shares must be in order between 0 and 1')

    def test_shares_that_leave_the_remainder_below_zero(self):
        rows = [(1, 'Copper conductors', 'Electronics', 0.5, 0.8, 1.0, '', 'E', '', ''),
                (1, 'Copper conductors', 'Aluminium', 0.1, 0.1, 0.2, '', 'E', '', ''), self.SPLIT[1]]
        self.assertFaultSays(self.split_faults(rows), 'the largest shares add up to 1.2')

    def test_a_split_not_labelled_as_an_estimate(self):
        rows = [(1, 'Copper conductors', 'Electronics', 0.1, 0.2, 0.3, '', 'Direct', '', ''), self.SPLIT[1]]
        self.assertFaultSays(self.split_faults(rows), "labelled 'E', not 'Direct'")

    def test_a_piece_in_mixed(self):
        rows = [(1, 'Copper conductors', 'Mixed', 0.1, 0.2, 0.3, '', 'E', '', ''), self.SPLIT[1]]
        self.assertFaultSays(self.split_faults(rows), "the piece 'Mixed' is not a material")

    def test_a_split_whose_material_row_does_not_say_split(self):
        self.assertFaultSays(self.split_faults(materials=PLACED_MATERIALS), "does not say 'Split'")

    def test_a_material_row_saying_split_without_a_split(self):
        self.assertFaultSays(self.split_faults(splits=[]), "it says 'Split', but the sheet Splits has no rows")

    def test_the_pages_show_the_split(self):
        self.split_faults()
        with tempfile.TemporaryDirectory() as folder:
            for draw, name in ((schemas.draw_shared_lists, 'lists.png'), (schemas.draw_robot, 'robot.png')):
                path = os.path.join(folder, name)
                args = (self.book.categories[0], self.book.parts_lists[1], self.book.materials_lists[1], self.lists)
                draw(*args, [], path, Params()) if draw is schemas.draw_shared_lists else draw(*args, path, Params())
                self.assertTrue(os.path.exists(path))


class TestRobotPage(SmallLists):
    """The one-view schema of a robot type: Matthias, 2026-10-26, "I want theat one can understand the robot and
    its compostion and parts in one vew"."""

    def category(self, anchor, height_and_mass):
        return schemas.Category(1, 'Small', '', height_and_mass, '', anchor, 2)

    def test_the_height_of_the_anchor_robot_where_the_workbook_gives_it(self):
        height, note = schemas.robot_height(self.category('Unitree G1 (China)\n1.32 m | 35.0 kg', 'Height: 1–2 m'))
        self.assertEqual((height, note), (1.32, ''))

    def test_otherwise_the_middle_of_the_category_range_said_on_the_page(self):
        height, note = schemas.robot_height(self.category('Atlas (US)', 'Height: ~1.73–1.85 m\nMass: 73–90 kg'))
        self.assertAlmostEqual(height, 1.79)
        self.assertIn('middle of the category\'s height range, 1.73–1.85 m', note)

    def test_without_any_height_the_tallest(self):
        height, note = schemas.robot_height(self.category('Robot', 'Mass: 50 kg'))
        self.assertEqual(height, schemas.TALLEST)
        self.assertTrue(note)

    def test_labels_keep_their_order_and_their_distance(self):
        placed = schemas.spread([5.0, 1.0, 1.1, 1.15], 0.5, 1.0, 6.0)
        self.assertEqual(placed[1:], [1.0, 1.5, 2.0])
        self.assertEqual(placed[0], 5.0)
        crowded = schemas.spread([5.9, 5.95, 6.0], 0.5, 1.0, 6.0)
        self.assertEqual(crowded, [5.0, 5.5, 6.0])

    def test_the_motors_of_a_split_part_follow_its_units(self):
        parts = [(1, 4, 'Knee actuator', 'Joint drives', '', 'Legs 1; Torso 1', 2, 'Split.')] + PLACED_PARTS[1:]
        self.lists_faults(parts)
        self.assertEqual(schemas.motors_by_region(self.book.parts_lists[1], self.lists), {'Legs': 1, 'Torso': 1})

    def test_bounds_add_up_the_minimums_and_the_maximums(self):
        self.assertEqual(schemas.bounds([(1, 2, 3), (0.5, 1, 1.5), (None, 4, None)]), (1.5, 4.5))

    def test_the_page_is_drawn(self):
        self.lists_faults()
        with tempfile.TemporaryDirectory() as folder:
            for n in (1, 2):
                path = os.path.join(folder, 'categories', f'{n}_robot.png')
                schemas.draw_robot(self.book.categories[n - 1], self.book.parts_lists[n],
                                   self.book.materials_lists[n], self.lists, path, Params())
                self.assertTrue(os.path.exists(path))


class TestTheWorkbook(unittest.TestCase):
    """The real workbook, as 01 reads it; skipped where the workbook is not on disk."""

    def test_six_categories_68_parts_and_no_fault(self):
        params = Params()
        path = absolute(params.data.workbook)
        if not os.path.exists(path):
            self.skipTest(f'{params.data.workbook} is not on disk')
        book = schemas.read_workbook(path, params)
        self.assertEqual([c.number for c in book.categories], [1, 2, 3, 4, 5, 6])
        self.assertEqual(sum(len(pl.parts) for pl in book.parts_lists.values()), 68)
        self.assertEqual(schemas.check_workbook(book, params), [])
        # The two numbers the overview leans on, read by hand from the workbook (rows 77 and 78).
        heavy = book.parts_lists[5]
        self.assertEqual((heavy.sum_kg[1], heavy.stated_mass_kg), (103.4, 90.0))
        self.assertTrue(re.match(r'Notional', book.categories[5].anchor))
        self.assertEqual(sum(len(ml.materials) for ml in book.materials_lists.values()), 59)

    def test_the_shared_lists_place_everything_and_add_up(self):
        params = Params()
        if not (os.path.exists(absolute(params.data.workbook)) and os.path.exists(absolute(params.data.shared_lists))):
            self.skipTest('the workbook or the shared lists are not on disk')
        book = schemas.read_workbook(absolute(params.data.workbook), params)
        lists = schemas.read_shared_lists(absolute(params.data.shared_lists))
        self.assertEqual(schemas.check_shared_lists(book, lists, params), [])
        self.assertEqual((len(lists.parts), len(lists.materials)), (68, 35))
        for n, parts_list in book.parts_lists.items():
            mode = parts_list.sum_kg[1]
            for totals in (schemas.by_view(parts_list, lists, 'group'), schemas.by_view(parts_list, lists, 'region'),
                           schemas.by_material(book.materials_lists[n], lists)):
                self.assertAlmostEqual(sum(totals.values()), mode, places=6, msg=f'robot type {n}')
        self.assertEqual([schemas.motors_of(book.parts_lists[n], lists) for n in range(1, 7)], [23, 31, 52, 30, 28, 14])
        # Point 9: robot type 3's 'Electrical & magnetics group' (4.2 kg at the mode), split by the shares of robot
        # types 2, 4 and 5: magnets 30 %, electronics 20 %, copper the remaining 50 %.
        three = schemas.by_material(book.materials_lists[3], lists)
        for name, mode in (('Magnets (NdFeB)', 1.26), ('Electronics', 0.84), ('Copper', 2.1), ('Mixed', 2.3)):
            self.assertAlmostEqual(three[name], mode, places=6, msg=name)


if __name__ == '__main__':
    unittest.main()
