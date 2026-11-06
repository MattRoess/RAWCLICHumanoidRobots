"""
Tests of 04_stock_and_flow.py: the humanoid robots in the world, their joint sets and battery packs, quarter by
quarter as RAWCLICDataCenters' 07, and the elements in them, each robot one of 02's draws of its robot type.

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

Matthias, 2026-11-06: "Use the numbers in the article", "Do exactly what has been done for the datacenter", "I want the
same figures as for the datacenters, but expand them all the essential critcial and statigic elements. Also have real
lifetimes not something fixed like this. I want to see uncerttainites", "Add also the limit in stock and production like
for the data centers", "Yes, build it", "Have at least so many battery packs ready for use as it is needed to have them
for 1 day to switch", "Yes, replace joints" (documentation/claude/EVIDENCE.md E39 to E43). The hand calculations are
written beside each test; the faults are made on purpose. 02's draws are made up for the run (four elements, 40 draws),
so that every kg can be counted by hand. Everything is written into temporary folders: press Run, nothing in the
project is changed.
"""

import dataclasses
import importlib.util
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)

_spec = importlib.util.spec_from_file_location('stock_and_flow', os.path.join(ROOT, '04_stock_and_flow.py'))
stock_and_flow = importlib.util.module_from_spec(_spec)
sys.modules['stock_and_flow'] = stock_and_flow
_spec.loader.exec_module(stock_and_flow)

from src.params_schema import ParameterError, Params, absolute, validate  # noqa: E402

S = stock_and_flow
# The article's robots in the world, Plan A, at 1 January (its economics explorer, preset "AI 2040 Plan A Scenario",
# Input Table, row "Robots"; EVIDENCE.md E40), as the article writes them.
ARTICLE = {2025: 10e6, 2026: 11.6e6, 2027: 13.3e6, 2028: 15.3e6, 2029: 18.2e6, 2030: 23e6, 2031: 35.7e6, 2032: 72e6,
           2033: 170e6, 2034: 423e6, 2035: 1.0e9, 2036: 2.26e9, 2037: 5.28e9, 2038: 12.5e9, 2039: 29.7e9, 2040: 70e9}


def changed(**settings) -> Params:
    """The settings in force with some of `stock_and_flow` changed."""
    params = Params()
    params.stock_and_flow = dataclasses.replace(params.stock_and_flow, **settings)
    return params


class TestTheSettings(unittest.TestCase):
    """The settings hold the agreed table (EVIDENCE.md E42, E43) and refuse what cannot be counted."""

    def test_the_agreed_table(self):
        flow = Params().stock_and_flow
        self.assertEqual(dict(flow.robots), ARTICLE)
        self.assertEqual(flow.robot_lifetime_years, (5.0, 7.0, 10.0))
        self.assertEqual(flow.hours_a_day, 24.0)
        self.assertEqual(flow.joint_life_hours, (7000.0, 10000.0, 30000.0))
        self.assertEqual(flow.battery_cycles_to_80, (500.0, 800.0, 1000.0))
        self.assertEqual(flow.battery_replaced_below, (0.75, 0.80, 0.85))         # "80% +-5%"
        self.assertEqual(dict(flow.runtime_2025_hours), {1: 2.0, 3: 2.0, 5: 4.0})
        self.assertEqual(flow.research_share_2025, (0.05, 0.10, 0.15))           # "around 10% within -+5%"
        self.assertEqual(flow.research_share_2040, (0.025, 0.05, 0.075))
        self.assertFalse(hasattr(flow, 'robot_depreciation'))                     # the first 04's, gone

    def test_what_cannot_be_counted_is_refused(self):
        for settings in ({'robots': ((2025, 10e6), (2027, 13.3e6))},             # a year missing
                         {'robots': ((2025, 10e6), (2026, 0.0))},                # no robots
                         {'robots': ((2025, 10e6),)},                            # one year has no flow
                         {'robot_lifetime_years': (7.0, 5.0, 10.0)},             # out of order
                         {'joint_life_hours': (0.0, 10000.0, 30000.0)},          # 0
                         {'battery_cycles_to_80': (800.0, 800.0, 800.0)},        # a single number, no triangle
                         {'battery_replaced_below': (0.75, 0.80, 1.0)},          # a capacity of 100 %
                         {'research_share_2040': (0.5, 1.0, 1.5)},               # a share above 1
                         {'hours_a_day': 25.0}, {'hours_a_day': 0.0},
                         {'runtime_2025_hours': ((1, 2.0), (3, 2.0))},           # type 5 missing
                         {'runtime_2025_hours': ((1, 2.0), (3, 0.0), (5, 4.0))}):
            with self.assertRaises(ParameterError, msg=settings):
                validate(changed(**settings))


class TestTheLifetimes(unittest.TestCase):
    """A lifetime spread among the units as a triangle (07's survival), and a draw's value of a triangle."""

    def test_by_hand(self):
        life = (5.0, 7.0, 10.0)
        self.assertEqual(float(S.survival(4.9, life)), 1.0)                  # none has gone before 5 years
        self.assertAlmostEqual(float(S.survival(7.0, life)), 0.6)            # 1 − (7 − 5)² / ((10 − 5)(7 − 5)) = 0.6
        self.assertAlmostEqual(float(S.survival(8.5, life)), 0.15)           # (10 − 8.5)² / ((10 − 5)(10 − 7)) = 0.15
        self.assertEqual(float(S.survival(10.0, life)), 0.0)
        self.assertAlmostEqual(float(S.triangle_ppf(0.1, *life)), 6.0)       # 5 + √(0.1 × 5 × 2) = 6
        self.assertAlmostEqual(float(S.triangle_ppf(0.4, *life)), 7.0)       # the mode lies at 2 / 5
        self.assertAlmostEqual(float(S.triangle_ppf(0.5, 0.05, 0.10, 0.15)), 0.10)

    def test_a_joint_set_and_a_pack(self):
        hours = 10000 / (24 * 365.25)                                            # 10,000 hours at 24 h a day
        self.assertAlmostEqual(float(S.joint_survival(hours, 24.0, (7000.0, 10000.0, 30000.0))),
                               1 - 3000 ** 2 / (23000 * 3000))                  # 0.870
        cycles = (500.0, 800.0, 1000.0)
        # At 80 % its life is its charges to 80 %; at 800 charges 1 − 300² / (500 × 300) = 0.4 are left.
        self.assertAlmostEqual(float(S.pack_survival(np.array([800 / 365.25]), 0.80, cycles)[0, 0]), 0.4)
        # At 75 % it lasts 1.25 times as long: at 1,000 charges as many left as at 800 charges at 80 %.
        self.assertAlmostEqual(float(S.pack_survival(np.array([1000 / 365.25]), 0.75, cycles)[0, 0]), 0.4)
        both = S.pack_survival(np.array([1000 / 365.25]), np.array([0.75, 0.80]), cycles)
        self.assertEqual(both.shape, (2, 1))                                     # one row a draw
        self.assertLess(both[1, 0], both[0, 0])


class TestTheCohorts(unittest.TestCase):
    """The robots in use quarter by quarter (07's compute path and follow_target), checked by hand."""

    def test_the_quarters_between_the_articles_years(self):
        quarters = S.targets(ARTICLE)
        self.assertEqual(quarters.shape, (60,))
        self.assertAlmostEqual(quarters[3], 11.6e6)                              # the end of 2025 Q4: 1 January 2026
        self.assertAlmostEqual(quarters[1], (10e6 * 11.6e6) ** 0.5)              # half way, geometric: 10.77 M
        self.assertAlmostEqual(quarters[-1], 70e9)

    def test_units_living_one_year_by_hand(self):
        # Every unit lives 4 quarters (ages 0.125 to 0.875 years in use, 1.125 gone); 100 in use, no growth: 25 arrive
        # in each quarter before 2025, and 25 arrive and 25 leave in every quarter after.
        span = 8 + 60
        survive = np.where(np.arange(span) < 4, 1.0, 0.0)
        f = S.cohorts(survive, 100.0, 1.0, target=np.full((2, 60), 100.0))
        np.testing.assert_allclose(f.past, 25.0)
        np.testing.assert_allclose(f.built, 25.0)
        np.testing.assert_allclose(f.gone, 25.0)
        np.testing.assert_allclose(f.stock, 100.0)
        np.testing.assert_allclose(f.start, 100.0)

    def test_a_falling_target_never_takes_a_unit_out(self):
        span = 8 + 60
        survive = np.where(np.arange(span) < 4, 1.0, 0.0)
        target = np.full((1, 60), 100.0)
        target[0, 10:] = 40.0                                                    # 60 fewer needed from quarter 10
        f = S.cohorts(survive, 100.0, 1.0, target=target)
        self.assertEqual(f.built[0, 10], 0.0)                                    # never below 0
        self.assertAlmostEqual(f.stock[0, 10], 75.0)                             # what is left, above the target
        self.assertAlmostEqual(f.gone[0, 10], 25.0)                              # the oldest quarter's leave
        self.assertAlmostEqual(f.stock[0, 13], 40.0)                             # back on the target

    def test_the_robots_of_1_january_2025(self):
        # The robots of 1 January 2025, built in the quarters before at the article's own growth, hold its 10 M.
        params = Params()
        age = S.ages(41 + 60)
        f = S.cohorts(S.survival(age, params.stock_and_flow.robot_lifetime_years), 10e6, 1.16,
                      target=np.broadcast_to(S.targets(ARTICLE), (1, 60)))
        p = np.arange(41, 0, -1)
        self.assertAlmostEqual(float((f.past[0] * S.survival(S.ages(41)[p - 1], (5.0, 7.0, 10.0))).sum()), 10e6,
                               delta=1e-3)
        np.testing.assert_allclose(f.past[0, 1:] / f.past[0, :-1], 1.16 ** 0.25)  # growing by the article's 16 %
        self.assertTrue((f.built > 0).all())


class TestTheWorkbook(unittest.TestCase):
    """The robot types' shares, runtimes and packs from his workbook, by hand."""

    @classmethod
    def setUpClass(cls):
        cls.params = Params()
        cls.shares, cls.trajectories = S.workbook_rows(cls.params)

    def test_his_numbers_read(self):
        self.assertEqual(self.shares[2], (0.20, 0.25, 0.28, 0.25))
        self.assertEqual(self.shares[6], (0.05, 0.05, 0.04, 0.05))
        self.assertEqual(self.trajectories[2], (S.RUNTIME_ROW, (3.5, 9.0, 14.0, 24.0)))
        self.assertEqual(self.trajectories[6], (S.RUNTIME_ROW, (1.0, 4.0, None, None)))   # '—' after 2030
        self.assertEqual(self.trajectories[3], (S.DENSITY_ROW, (180.0, 350.0, 500.0, 700.0)))

    def test_the_shares_by_hand(self):
        u = np.array([0.5])                                                      # the research share at its mode
        times = np.array([2025.0, 2032.5, 2040.0])
        got = S.type_shares(self.params, self.shares, u, times)[0]
        np.testing.assert_allclose(got[0], [0.10, 0.20, 0.50, 0.10, 0.05, 0.05])  # type 3: 1 − 0.50
        # 2032.5: type 1 half way, 0.075; type 2 (0.25 + 0.28) / 2; type 4 (0.10 + 0.20) / 2; type 6 (0.05 + 0.04) / 2
        np.testing.assert_allclose(got[1], [0.075, 0.265, 0.415, 0.15, 0.05, 0.045])
        np.testing.assert_allclose(got[2], [0.05, 0.25, 0.30, 0.30, 0.05, 0.05])
        many = S.type_shares(self.params, self.shares, np.linspace(0, 1, 11), S.mid_times())
        np.testing.assert_allclose(many.sum(axis=2), 1.0)
        self.assertTrue((many >= 0).all())

    def test_a_remainder_below_0_stops(self):
        shares = dict(self.shares)
        shares[2] = (0.90, 0.90, 0.90, 0.90)                                     # made up: the others above 1
        with self.assertRaisesRegex(ValueError, 'remainder'):
            S.type_shares(self.params, shares, np.array([0.5]), np.array([2025.0]))

    def test_the_packs_a_robot_holds(self):
        packs = S.packs_per_robot(self.params, self.trajectories, np.array([2025.0, 2040.0]))
        # 2025: 24 h / 2, 3.5, 2, 2, 4, 1 h, rounded up
        np.testing.assert_array_equal(packs[:, 0], [12, 7, 12, 12, 6, 24])
        # 2040: type 1 2 h × 550 / 220 = 5 h; type 3 2 h × 700 / 180 = 7.8 h; type 5 4 h × 700 / 250 = 11.2 h;
        # type 6 held at its 4 h of 2030
        np.testing.assert_array_equal(packs[:, 1], [5, 1, 4, 3, 3, 6])
        self.assertAlmostEqual(float(S.runtimes(self.params, self.trajectories, np.array([2040.0]))[2, 0]),
                               2 * 700 / 180)


class TestTheCount(unittest.TestCase):
    """One chunk of draws with the settings in force: its check passes, and catches each fault made on purpose."""

    @classmethod
    def setUpClass(cls):
        cls.params = Params()
        shares, trajectories = S.workbook_rows(cls.params)
        rng = np.random.default_rng(3)
        n = 30
        cls.counted, cls.needs = S.count(cls.params, shares, trajectories, rng.random(n),
                                         S.triangle_ppf(rng.random(n), 0.75, 0.80, 0.85))

    def test_it_adds_up(self):
        self.assertEqual(S.check(self.params, self.counted, self.needs), [])
        total = self.counted[('robots', 0)]
        np.testing.assert_allclose(total.stock[:, 3::4], np.broadcast_to([ARTICLE[y] for y in range(2026, 2041)],
                                                                         (30, 15)), rtol=1e-12)
        for t in S.TYPES:
            np.testing.assert_allclose(self.counted[('joint sets', t)].stock, self.counted[('robots', t)].stock,
                                       rtol=1e-9)
            self.assertTrue((self.counted[('battery packs', t)].stock >= self.needs[t] * (1 - 1e-9)).all())

    def test_the_robots_of_2025_by_hand(self):
        # The article's 2025 and 2026 with the lifetimes 5 / 7 / 10 years: built 2.43 M, retired 0.83 M (none of
        # them below 5 years old, a young fleet growing by 16 % a year).
        built, stock, gone = S.years_of(self.counted[('robots', 0)])
        self.assertAlmostEqual(stock[0, 0] + built[0, 0] - gone[0, 0], 11.6e6, delta=1e-3)
        self.assertGreater(gone[0, 0], 0.5e6)
        self.assertLess(gone[0, 0], 1.2e6)

    def faults_of(self, key, field, change):
        """check() of the chunk with one array of one stock changed."""
        counted = dict(self.counted)
        values = getattr(counted[key], field).copy()
        change(values)
        counted[key] = counted[key]._replace(**{field: values})
        return S.check(self.params, counted, self.needs)

    def test_each_fault_is_caught(self):
        def more(values):
            values[:, 7] *= 1.001
        self.assertTrue(any('stock before + inflow' in f
                            for f in self.faults_of(('battery packs', 4), 'gone', more)))
        self.assertTrue(any("not the article's" in f for f in self.faults_of(('robots', 0), 'stock', more)))
        self.assertTrue(any('do not add up to all robots' in f for f in self.faults_of(('robots', 2), 'stock', more)))
        self.assertTrue(any('joint sets in use are not' in f for f in self.faults_of(('joint sets', 3), 'stock', more)))

        def fewer(values):
            values[:, 20] *= 0.99
        self.assertTrue(any('fewer battery packs' in f for f in self.faults_of(('battery packs', 6), 'stock', fewer)))

        def below(values):
            values[:, 5] = -1.0
        self.assertTrue(any('below 0' in f for f in self.faults_of(('joint sets', 1), 'built', below)))


class TestTheStatistics(unittest.TestCase):
    """Over the draws above 0 ("A 0 is not part of a distribution"), and the words and units of the figures."""

    def test_a_0_is_not_part_of_the_distribution(self):
        stats = S.stats_of(np.array([[0.0, 0.0], [1.0, 0.0], [3.0, 0.0]]))
        self.assertEqual(stats['mean'][0], 2.0)                                  # over 1 and 3, not 0, 1 and 3
        self.assertAlmostEqual(stats['held'][0], 2 / 3)
        self.assertTrue(np.isnan(stats['mean'][1]))                              # 0 in every draw: no number
        self.assertEqual(stats['held'][1], 0.0)
        self.assertEqual(S.held_words(np.array([1.0, 1.0])), '')
        self.assertEqual(S.held_words(np.array([0.999, 1.0])), ', held in 99 % to 100 % of the draws')
        self.assertEqual(S.held_words(np.array([0.0, 0.56, 0.56])), ', held in 56 % of the draws')

    def test_masses_written_as_07(self):
        self.assertEqual(S.mass_label(1e6), '1 kt')
        self.assertEqual(S.mass_label(100.0), '100 kg')
        self.assertEqual(S.mass_label(1e12), '1,000 Mt')
        self.assertEqual(S.mass_text(9.8e11), '980 Mt')
        self.assertEqual(S.mass_text(7.25e12), '7,250 Mt')                     # "4000 not 4k"
        self.assertEqual(S.mass_text(5.5e7), '55 kt')


class TestTheLegends(unittest.TestCase):
    """A legend at the upper left, as 07's, unless a line runs under it or a value is written there (found 2026-11-06:
    indium's world production ran under the legend)."""

    def test_a_legend_leaves_lines_and_written_values_free(self):
        figure, axes = S.plt.subplots()
        axes.plot([0, 1], [0.95, 0.95], label='a line along the top')            # the upper corners taken
        axes.plot([0, 1], [0.5, 0.5], label='a line in the middle')
        axes.set_ylim(0, 1)
        axes.text(0.98, 0.03, 'a value below the scale', transform=axes.transAxes, ha='right', va='bottom')
        axes.legend(loc='upper left')
        S.place_legends(figure)
        renderer = figure.canvas.get_renderer()
        legend = axes.get_legend()
        self.assertFalse(S.lines_under(axes, legend.get_window_extent(renderer), renderer))
        self.assertEqual(legend._loc, 3)                                          # the lower left, the one corner free
        S.plt.close(figure)


@unittest.skipUnless(os.path.exists(Params().data.data_center_scenarios)
                     and os.path.exists(Params().data.usgs_commodities),
                     "RAWCLICDataCenters' workbook or USGS's data file is not on this computer")
class TestTheWorldsProductionAndReserves(unittest.TestCase):
    """The dashed lines: RAWCLICDataCenters' sheet ElementReference, and USGS's data file for Mg, Ti and In."""

    def test_read_as_written(self):
        values, notes = S.references(Params())
        self.assertEqual(values['Cu']['production'], (23e9, 23e9, 23e9, False))   # 23,000,000 t
        self.assertEqual(values['Pd']['reserves'][3], True)                       # "at least"
        mg = 1100 * 1e6                                                           # 1,100 thousand t of metal
        self.assertAlmostEqual(values['Mg']['production'][1], mg)
        self.assertAlmostEqual(values['Mg']['reserves'][1], 7.8e6 * 1e6 * 24.305 / 84.313, delta=1)
        self.assertAlmostEqual(values['Ti']['reserves'][1], 540000 * 1e6 * 47.867 / 79.866, delta=1)
        self.assertTrue(values['Ti']['reserves'][3])                              # USGS writes ">540,000"
        self.assertAlmostEqual(values['In']['production'][1], 1100 * 1e3)       # 1,100 t refined
        self.assertNotIn('reserves', values['In'])
        self.assertNotIn('Dy', values)
        self.assertNotIn('Tb', values)
        self.assertTrue(any('estimate' in n for n in notes['Mg']))


# Made-up draws of 02 (N draws), one robot of type t in draw i: its frame t × (1 + i / N) kg of aluminium, its boards
# 0.25 kg of copper, its hip joints 1 kg and its arm joints 0.5 kg of copper, its battery pack 2 kg of lithium; no
# neodymium in any draw.
N = 40
ELEMENTS = ['Li', 'Al', 'Cu', 'Nd']


def made_up_draws(params: Params) -> None:
    """Write the made-up draws of the six types where 02 writes its own (params' folders)."""
    book = S.schemas.read_workbook(absolute(params.data.workbook), params)
    for category in book.categories:
        t, folder = category.number, S.composition.folder_name(category)
        consolidated = os.path.join(params.output.composition_dir, folder)
        apart = os.path.join(params.output.parts_dir, folder)
        os.makedirs(consolidated)
        os.makedirs(apart)
        with open(os.path.join(consolidated, 'elements.txt'), 'w', encoding='utf-8') as handle:
            handle.write('\n'.join(ELEMENTS) + '\n')
        columns = ['Frame and shell: Al', 'Boards and computers: Cu', 'Hip joints: Cu', 'Arm joints and hands: Cu',
                   'Battery pack: Li']
        draw = np.arange(N) / N
        values = np.column_stack([t * (1 + draw), np.full(N, 0.25), np.ones(N), np.full(N, 0.5), np.full(N, 2.0)])
        with open(os.path.join(apart, 'elements.txt'), 'w', encoding='utf-8') as handle:
            handle.write('\n'.join(columns) + '\n')
        np.save(os.path.join(apart, 'elements.npy'), values.astype(np.float32))


class TestTheRun(unittest.TestCase):
    """04 run on the made-up draws into a temporary folder: every kg by hand, the files, the pages."""

    @classmethod
    def setUpClass(cls):
        from matplotlib.figure import Figure
        from unittest import mock
        from test_comparison import page_problems
        cls.folder = tempfile.TemporaryDirectory()
        params = Params()
        where = lambda name: os.path.join(cls.folder.name, name)                 # noqa: E731
        params.output = dataclasses.replace(
            params.output, composition_dir=where('consolidated'), parts_dir=where('parts_taken_apart'),
            stock_and_flow_dir=where('data'), stock_and_flow_figures_dir=where('figures'))
        made_up_draws(params)
        cls.params, cls.problems, cls.saved, cls.covered = params, [], [], []
        save = Figure.savefig

        def checked(figure, path, *args, **kwargs):
            name = os.path.basename(str(path))
            cls.problems += page_problems(figure, name)
            renderer = figure.canvas.get_renderer()
            cls.covered += [(name, axes.get_title()) for axes in figure.axes if axes.get_legend() is not None
                            and S.lines_under(axes, axes.get_legend().get_window_extent(renderer), renderer)]
            cls.saved.append(str(path))
            save(figure, path, *args, **kwargs)

        out = StringIO()
        with mock.patch.object(Figure, 'savefig', checked), redirect_stdout(out):
            cls.code = S.run(params)
        cls.printed = out.getvalue()
        data = params.output.stock_and_flow_dir
        cls.files = {name: np.load(os.path.join(data, f'{name}.npy')) for name in S.UNIT_FILES + S.ELEMENT_FILES}

    @classmethod
    def tearDownClass(cls):
        cls.folder.cleanup()

    def test_it_runs(self):
        self.assertEqual(self.code, 0, self.printed)
        self.assertEqual(self.files['units_stock'].shape, (N, 16, 3, 6))
        self.assertEqual(self.files['units_in'].shape, (N, 15, 3, 6))
        self.assertEqual(self.files['elements_stock'].shape, (N, 16, 3, 4))

    def test_the_robots_as_the_article(self):
        robots = self.files['units_stock'][:, :, 0, :].sum(axis=2)
        np.testing.assert_allclose(robots, np.broadcast_to([ARTICLE[y] for y in range(2025, 2041)], (N, 16)),
                                   rtol=1e-6)                                    # float32: 7 digits

    def test_every_kg_by_hand(self):
        units, kg = self.files['units_stock'].astype(np.float64), self.files['elements_stock'].astype(np.float64)
        al, cu, li = ELEMENTS.index('Al'), ELEMENTS.index('Cu'), ELEMENTS.index('Li')
        frame = np.array(S.TYPES)[None, :] * (1 + np.arange(N) / N)[:, None]    # draw i, type t
        # The bodies: each type's robots × its frame of draw i, added over the types (the pairing of draw i).
        np.testing.assert_allclose(kg[:, :, 0, al], (units[:, :, 0, :] * frame[:, None, :]).sum(axis=2), rtol=1e-5)
        np.testing.assert_allclose(kg[:, :, 0, cu], units[:, :, 0, :].sum(axis=2) * 0.25, rtol=1e-5)
        # The joint sets: 1 + 0.5 kg of copper each; the packs: 2 kg of lithium each; nothing else in them.
        np.testing.assert_allclose(kg[:, :, 1, cu], units[:, :, 1, :].sum(axis=2) * 1.5, rtol=1e-5)
        np.testing.assert_allclose(kg[:, :, 2, li], units[:, :, 2, :].sum(axis=2) * 2.0, rtol=1e-5)
        self.assertEqual(kg[:, :, 1, al].max(), 0.0)
        self.assertEqual(kg[:, :, 0, li].max(), 0.0)
        self.assertEqual(kg[:, :, :, ELEMENTS.index('Nd')].max(), 0.0)
        flows = self.files['elements_in'].astype(np.float64)
        np.testing.assert_allclose(flows[:, :, 2, li], self.files['units_in'][:, :, 2, :].sum(axis=2) * 2.0,
                                   rtol=1e-5)

    def test_its_summary(self):
        import csv
        with open(os.path.join(self.params.output.stock_and_flow_dir, S.SUMMARY), newline='',
                  encoding='utf-8') as handle:
            rows = list(csv.DictReader(handle))
        first = next(r for r in rows if r['quantity'] == 'robots' and r['robot type'] == 'all'
                     and r['flow'] == 'stock' and r['year'] == '2025')
        self.assertAlmostEqual(float(first['mean']), 10e6, delta=10)
        neodymium = [r for r in rows if r['quantity'] == 'Neodymium']
        self.assertTrue(neodymium and all(r['mean'] == '–' and r['held in % of the draws'] == '0.0'
                                          for r in neodymium))

    def test_its_pages(self):
        names = sorted(os.path.relpath(p, self.params.output.stock_and_flow_figures_dir) for p in self.saved)
        self.assertEqual(names, sorted([S.OVERVIEW] + [os.path.join(S.ELEMENTS_DIR, f) for f in
                                                       ('Lithium.png', 'Aluminium.png', 'Copper.png')]))
        self.assertTrue(all(os.path.exists(p) for p in self.saved))
        self.assertEqual(self.problems, [])
        self.assertEqual(self.covered, [])                     # no line and no written value under a legend
        self.assertIn('Neodymium: no numbers, 0 kg in every draw; no page.', self.printed)

    def test_without_02_it_stops(self):
        params = dataclasses.replace(self.params)
        params.output = dataclasses.replace(self.params.output, parts_dir=os.path.join(self.folder.name, 'none'))
        out = StringIO()
        with redirect_stdout(out):
            self.assertEqual(S.run(params), 1)
        self.assertIn('04 stopped', out.getvalue())

    def test_a_column_of_02_that_is_no_kind_stops(self):
        with tempfile.TemporaryDirectory() as other:
            params = dataclasses.replace(self.params)
            params.output = dataclasses.replace(self.params.output,
                                                composition_dir=os.path.join(other, 'consolidated'),
                                                parts_dir=os.path.join(other, 'parts_taken_apart'))
            made_up_draws(params)
            book = S.schemas.read_workbook(absolute(params.data.workbook), params)
            text = os.path.join(params.output.parts_dir, S.composition.folder_name(book.categories[2]),
                                'elements.txt')
            with open(text, encoding='utf-8') as handle:
                columns = handle.read().replace('Frame and shell: Al', 'Wings: Al')
            with open(text, 'w', encoding='utf-8') as handle:
                handle.write(columns)
            with self.assertRaisesRegex(ValueError, "'Wings: Al' of 02 is no kind"):
                S.robot_parts(params)


if __name__ == '__main__':
    unittest.main()
