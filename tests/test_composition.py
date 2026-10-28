"""
Tests of 02_composition.py: what each robot type is made of, drawn at random (Monte Carlo).

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

Matthias, 2026-10-26: "I agree with the specification of 02_composition.py and 03_comparison.py and with the
recommendations a to g. Build it step by step, tests first, and test with few draws only." The specification is in
documentation/claude/HANDOVER.md; these tests are its points 12 and 13.

The tests draw the small workbook of tests/test_schemas.py (robot type 1: two parts and two materials; robot type 2: a
battery built from two cells), with its shared lists and element recipes, 2,000 times, into temporary folders: press
Run, nothing in the project is changed. A mean is compared with the triangle's mean within four standard errors, and a
frequency with its probability the same way; the seed is fixed, so a test that passes keeps passing.
"""

import csv
import importlib.util
import math
import os
import sys
import tempfile
import unittest

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)

import test_schemas as small  # noqa: E402  the small workbook, its shared lists and recipes; it loads 01 as `schemas`

_spec = importlib.util.spec_from_file_location('composition', os.path.join(ROOT, '02_composition.py'))
composition = importlib.util.module_from_spec(_spec)
sys.modules['composition'] = composition  # the dataclasses of 02 look their module up here while it loads
_spec.loader.exec_module(composition)

from src.params_schema import Params  # noqa: E402

DRAWS = 2000
# Robot type 1's two materials follow the small recipe 'Outer': its 'Iron part' 30 / 40 / 50 %, 'Inner' the rest.
RECIPE_ROWS = [(1, 'Aluminum alloys', 'Aluminium', 'Outer', 'For the tests.'),
               (1, 'Copper conductors', 'Copper', 'Outer', 'For the tests.')]
# The energy per kg of the small cells, Wh/kg: Cell A 3.6 V × 2 Ah / 50 g, Cell B 3.6 V × 4 Ah / 90 g.
WH_PER_KG = (3.6 * 2 / 0.050, 3.6 * 4 / 0.090)
# The mass share of phosphorus in LiPF6, from the atomic masses of IUPAC 2024 (Li 6.94, P 30.974, F 18.998): the only
# compound of the small recipes that holds phosphorus, and only in the item 'Salt', which follows the cell's energy.
P_IN_LIPF6 = 30.974 / (6.94 + 30.974 + 6 * 18.998)
SALT = 0.1   # the mode of the item 'Salt' in the small 'Test recipe'
# The small register of the runs: two robots, neither taken apart (01's test register without its robot taken apart).
SMALL_REGISTER = [(1, 'Robot A', 34, 35, 36, '1', 'legs', '', ''), (2, 'Robot B', 59, 60, 61, '2', 'wheels', '', '')]


def triangle_mean(low: float, mode: float, high: float) -> float:
    """The mean of a triangular distribution."""
    return (low + mode + high) / 3


def triangle_sd(low: float, mode: float, high: float) -> float:
    """The standard deviation of a triangular distribution."""
    return math.sqrt((low * low + mode * mode + high * high - low * mode - low * high - mode * high) / 18)


class Drawn(unittest.TestCase):
    """Writes the small workbook, its shared lists and its element recipes into a temporary folder, and draws them."""

    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)

    def write(self, battery=small.BATTERY, rows=RECIPE_ROWS, parts=None, materials=None, lists=None, splits=None,
              cells=None, changes=None, seed=1) -> Params:
        """The settings of a run on the small files, with every input and output in the temporary folder."""
        folder = self.folder.name
        params = Params()
        params.data.workbook = os.path.join(folder, 'small.xlsx')
        params.data.shared_lists = os.path.join(folder, 'lists.xlsx')
        params.data.element_recipes = os.path.join(folder, 'recipes.xlsx')
        params.composition.draws = DRAWS
        params.composition.seed = seed
        params.output.composition_dir = os.path.join(folder, 'consolidated')
        params.output.composition_figures_dir = os.path.join(folder, 'figures', 'composition')
        params.output.comparison_dir = os.path.join(folder, 'figures', 'comparison')
        small.build(params.data.workbook, changes)
        small.build_lists(params.data.shared_lists, parts, materials, lists, splits, battery)
        small.build_recipes(params.data.element_recipes, cells, recipe=small.RECIPE + small.NESTED, rows=rows)
        # A small register without a robot taken apart: every robot type of the small workbook is drawn from it.
        params.data.register = os.path.join(folder, 'register.xlsx')
        small.build_register(params.data.register, rows=SMALL_REGISTER)
        return params

    def compose(self, **inputs) -> dict:
        """Each robot type of the small workbook drawn: its number -> its Composition."""
        params = self.write(**inputs)
        read = composition.read_inputs(params)
        self.assertEqual(composition.all_faults(read, params), [])
        return {c.number: composition.compose(c, read, params) for c in read.book.categories}

    def assertMean(self, draws, low, mode, high, msg=None):
        """The draws' mean within four standard errors of the triangle's mean, and every draw within its bounds."""
        self.assertAlmostEqual(draws.mean(), triangle_mean(low, mode, high),
                               delta=4 * triangle_sd(low, mode, high) / math.sqrt(len(draws)), msg=msg)
        self.assertGreaterEqual(draws.min(), low - 1e-12, msg)
        self.assertLessEqual(draws.max(), high + 1e-12, msg)


class TestDraws(Drawn):
    """Point 13: the same seed gives the same draws; the means agree with the triangles'; a discrete state is drawn
    about as often as its probability."""

    def test_the_same_seed_gives_the_same_draws(self):
        one, again, other = (self.compose(seed=seed) for seed in (7, 7, 8))
        for n in (1, 2):
            for table in composition.TABLES:
                np.testing.assert_array_equal(one[n].tables[table][1], again[n].tables[table][1])
            self.assertFalse(np.array_equal(one[n].column('total', 'Total'), other[n].column('total', 'Total')))

    def test_a_part_and_a_material_have_their_triangles_mean(self):
        one = self.compose()[1]
        self.assertMean(one.column('part_groups', 'Joint drives'), 2, 4, 6)
        self.assertMean(one.column('body_regions', 'Whole body'), 0.5, 1, 1.5)
        self.assertMean(one.column('materials', 'Aluminium'), 2, 3, 4.5)

    def test_a_part_split_by_units_gives_each_region_its_units(self):
        # The knee actuator's two units, one in the legs and one in the torso: each region half of the part.
        parts = [(1, 4, 'Knee actuator', 'Joint drives', '', 'Legs 1; Torso 1', 2, 'Split.')] + small.PLACED_PARTS[1:]
        one = self.compose(parts=parts)[1]
        np.testing.assert_allclose(one.column('body_regions', 'Legs'), one.column('body_regions', 'Torso'), rtol=1e-12)
        np.testing.assert_allclose(one.column('body_regions', 'Legs') * 2, one.column('part_groups', 'Joint drives'),
                                   rtol=1e-12)
        self.assertEqual(composition.draw_faults(one), [])

    def test_every_build_is_drawn_about_equally_often(self):
        two = self.compose()[2]
        self.assertEqual(set(two.build), {0, 1})
        self.assertAlmostEqual((two.build == 0).mean(), 0.5, delta=4 * math.sqrt(0.25 / DRAWS))

    def test_an_alternative_is_drawn_about_as_often_as_its_probability(self):
        # The can of the small recipe is plain iron or nickel-plated, half and half: nickel only in a plated can.
        plated = self.compose()[2].column('elements', 'Ni') > 0
        self.assertAlmostEqual(plated.mean(), 0.5, delta=4 * math.sqrt(0.25 / DRAWS))

    def test_a_recipe_used_twice_is_drawn_once_in_each_draw(self):
        # Robot type 1's aluminium and copper both follow 'Outer'. Its iron share is one quantity, drawn once per draw,
        # so the iron of both over their kilograms is the triangle 30 / 40 / 50 % itself. Drawn for each row on its
        # own, it would be a weighted mean of two draws, with a standard deviation near 0.030 instead of 0.041.
        one = self.compose()[1]
        iron = one.column('elements', 'Fe') / (one.column('materials', 'Aluminium') + one.column('materials', 'Copper'))
        self.assertMean(iron, 0.3, 0.4, 0.5)
        self.assertAlmostEqual(iron.std(), triangle_sd(0.3, 0.4, 0.5), delta=0.003)


class TestSums(Drawn):
    """Point 12, in every draw: materials plus Not allocated equal the parts' sum; the elements add up to the materials
    that have recipes; cells plus rest equal the battery row; no mass below zero except Not allocated."""

    def test_every_draw_adds_up(self):
        for c in self.compose().values():
            self.assertEqual(composition.draw_faults(c), [], c.number)
            total = c.column('total', 'Total')
            for table in ('materials', 'part_groups', 'body_regions'):
                np.testing.assert_allclose(c.tables[table][1].sum(axis=1), total, rtol=1e-12, err_msg=table)
            np.testing.assert_allclose(c.tables['elements'][1].sum(axis=1), c.in_elements.sum(axis=1), rtol=1e-9)

    def test_a_draw_that_does_not_add_up_is_caught(self):
        # A check is only trusted once it has been seen to catch what it guards: each sum of point 12, broken in one
        # draw, and a mass below zero.
        for robot, table, column, change, words in (
                (1, 'materials', 0, 0.1, 'the materials and Not allocated do not add up to the parts in 1 draw'),
                (1, 'part_groups', 0, 0.1, 'the part groups do not add up to the parts in 1 draw'),
                (1, 'body_regions', 0, 0.1, 'the body regions do not add up to the parts in 1 draw'),
                (1, 'elements', 0, 0.1, 'the elements do not add up to the materials that have recipes in 1 draw'),
                (2, 'battery', 'rest', 0.1, 'the cells and the rest do not add up to the battery row in 1 draw')):
            c = self.compose()[robot]
            if table == 'battery':
                c.battery[column][5] += change
            else:
                c.tables[table][1][5, column] += change
            self.assertEqual(composition.draw_faults(c), [f'robot type {robot}: {words}.'], table)
        one = self.compose()[1]
        one.tables['part_groups'][1][5, 0] *= -1
        one.tables['part_groups'][1][5, 1] -= 2 * one.tables['part_groups'][1][5, 0]
        self.assertEqual(composition.draw_faults(one), ['robot type 1: Joint drives is below zero in 1 draw.'])

    def test_the_cells_and_the_rest_add_up_to_the_battery_row(self):
        two = self.compose()[2]
        np.testing.assert_allclose(two.battery['cells'] + two.battery['rest'], two.battery['row'], rtol=1e-12)
        # Cell A: 10 in series × 2 in parallel × 50 g = 1.0 kg; Cell B: 10 × 1 × 90 g = 0.9 kg.
        np.testing.assert_allclose(two.battery['cells'], np.where(two.build == 0, 1.0, 0.9), rtol=1e-12)
        np.testing.assert_allclose(two.column('materials', 'Battery materials'), two.battery['cells'], rtol=1e-12)
        self.assertMean(two.battery['row'], 3, 4, 5)
        # The rest goes to Not allocated; the battery is the robot's one part (4 / 6 / 8 kg) and its one material.
        np.testing.assert_allclose(two.column('materials', 'Not allocated'),
                                   two.column('total', 'Total') - two.battery['cells'], rtol=1e-12)

    def test_not_allocated_may_fall_below_zero_and_is_reported(self):
        # Robot type 1: the parts 2.5 / 5 / 7.5 kg and the materials 3 / 5 / 7.5 kg, drawn independently, so the
        # materials exceed the parts in about half of the draws (recommendation b).
        one = self.compose()[1]
        below = one.column('materials', 'Not allocated') < 0
        self.assertGreater(below.mean(), 0.2)
        row = next(r for r in composition.summary(one) if r['Name'] == composition.NOT_ALLOCATED)
        self.assertAlmostEqual(row['Draws below zero (%)'], below.mean() * 100)
        for table in ('materials', 'elements', 'part_groups', 'body_regions'):
            columns, array = one.tables[table]
            kept = [i for i, name in enumerate(columns) if name != composition.NOT_ALLOCATED]
            self.assertGreaterEqual(array[:, kept].min(), 0, table)


class TestBattery(Drawn):
    """The battery as cells (E1.7j, E1.7k) and the NMC cell's parts that follow its energy per kg (E1.7i)."""

    def test_the_cells_follow_the_drawn_build_and_its_energy(self):
        # The salt follows the energy: its share is its mode × the drawn cell's Wh/kg over the mode of the NMC cells.
        two = self.compose()[2]
        f = np.where(two.build == 0, WH_PER_KG[0], WH_PER_KG[1]) / Params().composition.nmc_wh_per_kg_mode
        np.testing.assert_allclose(two.column('elements', 'P'), two.battery['cells'] * SALT * f * P_IN_LIPF6,
                                   rtol=1e-9)

    def test_a_kept_battery_follows_its_recipe_with_the_energy_drawn(self):
        # Recommendation f: where the battery row is kept, the energy per kg is drawn from the NMC triangle.
        two = self.compose(battery=[small.battery_row('Kept', 'Test recipe')])[2]
        self.assertIsNone(two.build)
        row = two.column('materials', 'Battery materials')
        self.assertMean(row, 3, 4, 5)
        settings = Params().composition
        low, mode, high = settings.nmc_wh_per_kg_min, settings.nmc_wh_per_kg_mode, settings.nmc_wh_per_kg_max
        self.assertMean(two.column('elements', 'P') / (row * SALT * P_IN_LIPF6) * mode, low, mode, high)
        np.testing.assert_allclose(two.column('materials', 'Not allocated'), two.column('total', 'Total') - row,
                                   rtol=1e-12)

    def test_a_rest_split_among_materials_adds_back_to_the_row(self):
        rest = [small.battery_row('Rest', 'Copper', share=(0.1, 0.2, 0.3)),
                small.battery_row('Rest', 'Aluminium', remainder='Yes')]
        two = self.compose(battery=small.BATTERY[:2] + rest, rows=None)[2]
        copper, aluminium = two.column('materials', 'Copper'), two.column('materials', 'Aluminium')
        np.testing.assert_allclose(copper + aluminium, two.battery['row'] - two.battery['cells'], rtol=1e-12)
        self.assertMean(copper / (copper + aluminium), 0.1, 0.2, 0.3)
        self.assertGreater(aluminium.min(), 0)


class TestSplits(Drawn):
    """A material name split by an estimate (sheet Splits): robot type 1's 'Copper conductors' (1 / 2 / 3 kg) into
    electronics (10 / 20 / 30 %) and copper as the remainder."""

    def test_a_split_adds_back_to_its_row(self):
        one = self.compose(lists=small.TestSplits.LISTS, materials=small.TestSplits.MATERIALS,
                           splits=small.TestSplits.SPLIT, rows=None)[1]
        electronics, copper = one.column('materials', 'Electronics'), one.column('materials', 'Copper')
        self.assertMean(electronics + copper, 1, 2, 3)
        self.assertMean(electronics / (electronics + copper), 0.1, 0.2, 0.3)


class TestRecipes(Drawn):
    """Which materials are in the elements, and where an item that follows the energy may sit."""

    def test_materials_without_a_recipe_are_named(self):
        # Point 9: without the sheet Rows, robot type 1's materials have no recipe; their kilograms are drawn, their
        # elements are not, and the summary says so.
        drawn = self.compose(rows=None)
        rows = {r['Name']: r for r in composition.summary(drawn[1]) if r['Kind'] == 'Material'}
        self.assertEqual((rows['Aluminium']['In the elements'], rows['Copper']['In the elements']), ('No', 'No'))
        self.assertEqual(drawn[1].tables['elements'][1].sum(), 0)
        rows = {r['Name']: r for r in composition.summary(drawn[2]) if r['Kind'] == 'Material'}
        self.assertEqual(rows['Battery materials']['In the elements'], 'Yes')
        self.assertEqual(rows[composition.NOT_ALLOCATED]['In the elements'], 'No')

    def test_a_cell_recipe_that_follows_the_energy_of_cells_other_than_nmc_stops(self):
        cells = [small.CELLS[0], ('Cell B', 'LFP') + small.CELLS[1][2:]]
        params = self.write(cells=cells)
        faults = composition.all_faults(composition.read_inputs(params), params)
        self.assertEqual(len(faults), 1, [f.text for f in faults])
        self.assertIn("Cell B: its recipe 'Test recipe' follows the energy per kg of NMC cells", faults[0].text)

    def test_a_row_whose_recipe_follows_the_energy_stops(self):
        params = self.write(rows=[(1, 'Copper conductors', 'Copper', 'Test recipe', '')])
        faults = composition.all_faults(composition.read_inputs(params), params)
        self.assertEqual(len(faults), 1, [f.text for f in faults])
        self.assertIn("'Test recipe' follows the energy of a cell", faults[0].text)


class TestRun(Drawn):
    """Point 10, 11 and 16: 02 run as by pressing Run, on the small files."""

    def test_each_robot_type_is_written_for_stock_and_flow(self):
        params = self.write()
        self.assertEqual(composition.run(params), 0)
        for folder in ('1_small', '2_large'):
            path = os.path.join(params.output.composition_dir, folder)
            arrays = {}
            for table in composition.TABLES:
                arrays[table] = np.load(os.path.join(path, f'{table}.npy'))
                with open(os.path.join(path, f'{table}.txt'), encoding='utf-8') as file:
                    columns = file.read().splitlines()
                self.assertEqual(arrays[table].dtype, np.float32, table)
                self.assertEqual(arrays[table].shape, (DRAWS, len(columns)), table)
            # Row i is the same draw in every array.
            for table in ('materials', 'part_groups', 'body_regions'):
                np.testing.assert_allclose(arrays[table].sum(axis=1), arrays['total'][:, 0], rtol=1e-5)
            with open(os.path.join(path, 'summary.csv'), encoding='utf-8', newline='') as file:
                rows = list(csv.DictReader(file))
            self.assertEqual(rows[0].keys(), set(composition.SUMMARY_HEADINGS))
            self.assertEqual({r['Kind'] for r in rows}, {'Material', 'Element'})
            self.assertTrue(os.path.exists(os.path.join(path, 'summary.xlsx')))

    def test_a_page_is_drawn_for_each_robot_type(self):
        # Point 14: kg by material and kg by element, each with its 95 % interval.
        params = self.write()
        self.assertEqual(composition.run(params), 0)
        for name in ('1_small.png', '2_large.png'):
            self.assertGreater(os.path.getsize(os.path.join(params.output.composition_figures_dir, name)), 0)

    def test_small_masses_keep_three_significant_figures(self):
        # An element of a few grams or less must not be printed as 0 kg.
        values = (104.04, 11.97, 6.114, 0.04789, 0.15, 0.4599996, 0.014, 0.000474, 0.0000474, -0.0312, 0)
        self.assertEqual([composition.mass(value) for value in values],
                         ['104', '12.0', '6.11', '0.0479', '0.150', '0.460', '0.0140', '0.000474', '0.0000474',
                          '-0.0312', '0'])

    def test_every_element_has_its_plain_name(self):
        # Every element the recipes can name (01's atomic masses) is written in plain words on the pages.
        for symbol in composition.schemas.ATOMIC_MASS:
            self.assertIn(symbol, composition.ELEMENT_NAMES, symbol)

    def test_a_fault_stops_before_anything_is_written(self):
        params = self.write(changes={(5, 'Evidence'): 'Measured'})
        self.assertEqual(composition.run(params), 1)
        self.assertFalse(os.path.exists(params.output.composition_dir))
        self.assertFalse(os.path.exists(params.output.composition_figures_dir))


if __name__ == '__main__':
    unittest.main()
