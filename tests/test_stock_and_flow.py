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
for 1 day to switch", "Yes, replace joints"; 2026-11-07, on the robot types: "Have them from 10% to 30%", "All types
have to have the same uncertainty!!!", "The summ of the total has to be correct", "Check all the privous code", and to
RAWCLICRecoveryModel's conditioning "Conditioning", then "I want that you developt an algorthym that has for all 6 types
around 10% +- in 2025 and 30%+- in 2040", "NO type 3 is not triangular!!" and to the rearrangement "Yes, build it"; on the
lifetimes "30% short and 20% longer. Also with the batteries"
(documentation/claude/EVIDENCE.md E39 to E45). The hand calculations are written beside each test; the faults are made on purpose. 02's draws are made up for the run (four elements, 40 draws),
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
# The article's robots in the world, Plan A, each at the end of its year (2026-11-08: "Follow the artcile!! 70 x 10E9") (its economics explorer, preset "AI 2040 Plan A Scenario",
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
        self.assertEqual(flow.research_share, ((2025, 0.10), (2040, 0.05)))      # its mode: "around 10%", "decrease"
        self.assertEqual(flow.type_share_spread, ((2025, 0.10), (2040, 0.30)))   # "10% in 2025 and 30% in 2040"
        self.assertEqual(flow.lifetime_factor, (0.70, 1.0, 1.20))                # "30% short and 20% longer"
        self.assertFalse(hasattr(flow, 'robots_2041'))                          # "Follow the artcile!! 70 x 10E9"
        for gone in ('robot_depreciation', 'research_share_2025', 'research_share_2040'):   # the earlier ones, gone
            self.assertFalse(hasattr(flow, gone), gone)

    def test_what_cannot_be_counted_is_refused(self):
        for settings in ({'robots': ((2025, 10e6), (2027, 13.3e6))},             # a year missing
                         {'robots': ((2025, 10e6), (2026, 0.0))},                # no robots
                         {'robots': ((2025, 10e6),)},                            # one year has no flow
                         {'robot_lifetime_years': (7.0, 5.0, 10.0)},             # out of order
                         {'joint_life_hours': (0.0, 10000.0, 30000.0)},          # 0
                         {'battery_cycles_to_80': (800.0, 800.0, 800.0)},        # a single number, no triangle
                         {'battery_replaced_below': (0.75, 0.80, 1.0)},          # a capacity of 100 %
                         {'research_share': ((2025, 0.10), (2040, 1.0))},        # a share of 1
                         {'research_share': ((2025, 0.0), (2040, 0.05))},        # a share of 0
                         {'research_share': ((2025, 0.10), (2035, 0.05))},       # not 2025 and 2040
                         {'type_share_spread': ((2025, 0.0), (2040, 0.15))},     # no spread: a single number
                         {'type_share_spread': ((2025, 0.05), (2040, 1.0))},     # a min of 0
                         {'type_share_spread': ((2025, 0.10), (2040, 0.8))},     # the foot below 0: 0.8 / 0.7764 > 1
                         {'type_share_spread': ((2025, 0.05),)},                 # one year only
                         {'lifetime_factor': (1.0, 1.0, 1.0)},                   # no uncertainty: a single number
                         {'lifetime_factor': (0.0, 1.0, 1.2)},                   # a lifetime of 0
                         {'lifetime_factor': (0.7, 1.3, 1.2)},                   # out of order
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

    def test_the_lifetime_of_a_draw(self):
        # A draw's factor scales the lifetime of all its robots: at 0.7 the robots live 3.5 / 4.9 / 7 years, so at 4.9
        # years as many are left as at 7 years with the factor 1 (0.6); at 1.2, 6 / 8.4 / 12 years.
        life = (5.0, 7.0, 10.0)
        got = S.robot_survival(np.array([4.9, 8.4, 3.4, 12.0]), np.array([0.7, 1.2]), life)
        self.assertEqual(got.shape, (2, 4))                                       # one row a draw
        self.assertAlmostEqual(got[0, 0], 0.6)
        self.assertAlmostEqual(got[1, 1], 0.6)
        self.assertEqual(got[0, 2], 1.0)                                          # none gone before 3.5 years
        self.assertEqual(got[1, 3], 0.0)                                          # all gone at 12 years
        # The packs: the factor scales the charges to 80 %; at 80 % and 0.7, 560 charges leave as many as 800 at 1.
        cycles = (500.0, 800.0, 1000.0)
        packs = S.pack_survival(np.array([560 / 365.25]), np.array([0.80]), cycles, np.array([0.7]))
        self.assertAlmostEqual(float(packs[0, 0]), 0.4)
        # The joints: the factor scales their life in hours; at 1.2, 12,000 hours leave as many as 10,000 at 1.
        joints = S.joint_survival(np.array([12000 / (24 * 365.25)]), 24.0, (7000.0, 10000.0, 30000.0),
                                  np.array([1.2, 1.0]))
        self.assertEqual(joints.shape, (2, 1))
        self.assertAlmostEqual(float(joints[0, 0]), 1 - 3000 ** 2 / (23000 * 3000))

    def test_a_joint_set_and_a_pack(self):
        hours = 10000 / (24 * 365.25)                                            # 10,000 hours at 24 h a day
        self.assertAlmostEqual(float(S.joint_survival(np.array([hours]), 24.0, (7000.0, 10000.0, 30000.0))[0, 0]),
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
        # 2025 Q1 to 2040 Q4 (07's quarters), each of the article's values at the end of its year (Matthias,
        # 2026-11-08: "Follow the artcile!! 70 x 10E9"); 1 January 2025 its 10 M less one year of its own growth,
        # 10 M / 1.16 = 8.62 M (E42's growth).
        quarters = S.targets(ARTICLE)
        self.assertEqual(quarters.shape, (64,))
        self.assertAlmostEqual(S.start_robots(ARTICLE), 10e6 / 1.16)
        self.assertAlmostEqual(quarters[3], 10e6)                                # the end of 2025
        self.assertAlmostEqual(quarters[1], (10e6 / 1.16 * 10e6) ** 0.5)          # half way through 2025, geometric
        self.assertAlmostEqual(quarters[7], 11.6e6)                              # the end of 2026
        self.assertAlmostEqual(quarters[63], 70e9)                               # the end of 2040: the article's

    def test_units_living_one_year_by_hand(self):
        # Every unit lives 4 quarters (ages 0.125 to 0.875 years in use, 1.125 gone); 100 in use, no growth: 25 arrive
        # in each quarter before 2025, and 25 arrive and 25 leave in every quarter after.
        span = 8 + 64
        survive = np.where(np.arange(span) < 4, 1.0, 0.0)
        f = S.cohorts(survive, 100.0, 1.0, target=np.full((2, 64), 100.0))
        np.testing.assert_allclose(f.past, 25.0)
        np.testing.assert_allclose(f.built, 25.0)
        np.testing.assert_allclose(f.gone, 25.0)
        np.testing.assert_allclose(f.stock, 100.0)
        np.testing.assert_allclose(f.start, 100.0)

    def test_a_falling_target_never_takes_a_unit_out(self):
        span = 8 + 64
        survive = np.where(np.arange(span) < 4, 1.0, 0.0)
        target = np.full((1, 64), 100.0)
        target[0, 10:] = 40.0                                                    # 60 fewer needed from quarter 10
        f = S.cohorts(survive, 100.0, 1.0, target=target)
        self.assertEqual(f.built[0, 10], 0.0)                                    # never below 0
        self.assertAlmostEqual(f.stock[0, 10], 75.0)                             # what is left, above the target
        self.assertAlmostEqual(f.gone[0, 10], 25.0)                              # the oldest quarter's leave
        self.assertAlmostEqual(f.stock[0, 13], 40.0)                             # back on the target

    def test_the_robots_of_1_january_2025(self):
        # The robots of 1 January 2025, 10 M / 1.16 = 8.62 M, built in the quarters before at the article's own growth.
        params = Params()
        age = S.ages(41 + 64)
        first = S.start_robots(ARTICLE)
        f = S.cohorts(S.survival(age, params.stock_and_flow.robot_lifetime_years), first, 1.16,
                      target=np.broadcast_to(S.targets(ARTICLE), (1, 64)))
        p = np.arange(41, 0, -1)
        self.assertAlmostEqual(float((f.past[0] * S.survival(S.ages(41)[p - 1], (5.0, 7.0, 10.0))).sum()), first,
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

    def test_the_modes_by_hand(self):
        # Type 1 his 10 % falling to 5 %; types 2 to 6 the workbook's shares, taking what type 1 leaves in proportion,
        # so that the six modes add up to 1 (2025: the workbook's 20, 35, 10, 5, 5 % of 75 % times 90 %).
        modes = S.type_modes(self.params, self.shares, np.array([2025.0, 2032.5, 2040.0]))
        np.testing.assert_allclose(modes[:, 0], [0.10, 0.24, 0.42, 0.12, 0.06, 0.06])
        # 2032.5: type 1 half way, 7.5 %; the workbook's types 2 to 6 half way between 2030 and 2035: 26.5, 37.5,
        # 15, 5, 4.5 % (88.5 %), each times 92.5 / 88.5
        others = np.array([0.265, 0.375, 0.15, 0.05, 0.045])
        np.testing.assert_allclose(modes[:, 1], [0.075, *(others * 0.925 / 0.885)])
        np.testing.assert_allclose(modes[:, 2], [0.05, 0.25, 0.30, 0.30, 0.05, 0.05])
        np.testing.assert_allclose(S.type_modes(self.params, self.shares, S.mid_times()).sum(axis=0), 1.0)

    def test_the_spread_widens(self):
        np.testing.assert_allclose(S.type_spread(self.params, np.array([2025.0, 2032.5, 2040.0])), [0.10, 0.20, 0.30])

    def test_the_shares_by_hand(self):
        # Types 1, 2, 4, 5 and 6 at a point h of the unit triangle −1 / 0 / 1: mode × (1 + h × end), the end the spread
        # over 0.7764 (95 % of a triangle lies within 0.7764 of its half-width, 1 − √0.05), so that 95 % of the draws
        # lie within ±10 % in 2025, ±20 % in 2032.5, ±30 % in 2040: the ends 12.88 %, 25.76 %, 38.64 %. Type 3 1 minus
        # them, so that the six add up to the article's robots in every draw; nothing divided.
        times = np.array([2025.0, 2032.5, 2040.0])
        modes = S.type_modes(self.params, self.shares, times)
        others = [k for k, t in enumerate(S.TYPES) if t != S.BALANCING_TYPE]
        rest = S.TYPES.index(S.BALANCING_TYPE)
        ends = np.array([0.10, 0.20, 0.30]) / (1 - np.sqrt(0.05))
        np.testing.assert_allclose(S.type_ends(self.params, times), ends)
        np.testing.assert_allclose(ends, [0.12880, 0.25760, 0.38640], atol=1e-5)
        for h in (0.0, -1.0, 1.0, 0.5):
            got = S.type_shares(self.params, self.shares, np.full((1, 3, 5), h), times)[0]      # times × 6
            np.testing.assert_allclose(got[:, others], modes[others].T * (1 + h * ends)[:, None], err_msg=h)
            np.testing.assert_allclose(got[:, rest], 1 - got[:, others].sum(axis=1), err_msg=h)
        # At h = 0 the modes of 2025: 10, 24, 42, 12, 6, 6 %; the other five at their top: type 3 1 − 1.1288 × 58 %.
        middle = S.type_shares(self.params, self.shares, np.zeros((1, 1, 5)), np.array([2025.0]))[0, 0]
        np.testing.assert_allclose(middle, [0.10, 0.24, 0.42, 0.12, 0.06, 0.06])
        top = S.type_shares(self.params, self.shares, np.ones((1, 1, 5)), np.array([2025.0]))[0, 0]
        self.assertAlmostEqual(top[rest], 1 - 1.12880 * 0.58, places=5)

    def test_every_type_its_own_triangle_and_the_sum_one_number(self):
        # 20,000 draws as the run makes them (Matthias, 2026-11-07: "I want that you developt an algorthym that has for
        # all 6 types around 10% +- in 2025 and 30%+- in 2040", "NO type 3 is not triangular!!", "Yes, build it"):
        # each type's share in 2025 and in every quarter.
        rng = np.random.default_rng(5)
        n = 20000
        points, corrected = S.type_points(self.params, self.shares, rng.random((n, 5)), rng.random(n))
        self.assertEqual(points.shape, (n, S.SHARE_TIMES.size, 5))
        got = S.type_shares(self.params, self.shares, points, S.SHARE_TIMES)     # draws × times × 6
        modes = S.type_modes(self.params, self.shares, S.SHARE_TIMES)
        spread, ends = S.type_spread(self.params, S.SHARE_TIMES), S.type_ends(self.params, S.SHARE_TIMES)
        rest = S.TYPES.index(S.BALANCING_TYPE)
        np.testing.assert_allclose(got.sum(axis=2), 1.0, atol=1e-12)            # one number: the article's robots
        self.assertTrue((got > 0).all())
        self.assertLess(corrected, 0.01)       # type 3 off its own draws by under 1 % of its half-width (0.14 % at 200,000)
        for i in range(S.SHARE_TIMES.size):
            for k in range(len(S.TYPES)):
                x = np.sort(got[:, i, k])
                triangle = (modes[k, i] * (1 - ends[i]), modes[k, i], modes[k, i] * (1 + ends[i]))
                gap = np.abs(S.triangle_cdf(x, *triangle) - (np.arange(1, n + 1) - 0.5) / n).max()
                self.assertLess(gap, 1.63 / np.sqrt(n), (S.TYPES[k], S.SHARE_TIMES[i]))   # its triangle (Kolmogorov, 99 %)
                if i in (0, S.SHARE_TIMES.size - 1):                             # 2025; the last quarter of 2039
                    half = (np.percentile(x, 97.5) - np.percentile(x, 2.5)) / 2 / modes[k, i]
                    self.assertAlmostEqual(half / spread[i], 1.0, delta=0.03)   # 95 % within ±10 %, ±29.8 %
            np.testing.assert_allclose(got[:, i].mean(axis=0), modes[:, i], rtol=0.005)   # the means at the modes
        correlations = np.corrcoef(got[:, 0].T)[rest]
        self.assertTrue(all(correlations[k] < 0 for k in range(6) if k != rest))   # 2025: type 3 against each other
        # One world over the years: each type's point from one quarter to the next.
        h = (got / modes.T[None] - 1) / ends[None, :, None]
        for i in range(S.SHARE_TIMES.size - 1):
            self.assertTrue(all(np.corrcoef(h[:, i, k], h[:, i + 1, k])[0, 1] > 0.99 for k in range(6)), i)

    def test_the_years_as_the_data_centres(self):
        # Matthias, 2026-11-08: "Both have to be exactly the same, as we have to combine both data!!!", "Both have to be
        # on the same x axis scale!!", "Yes!!": the quarters and years of RAWCLICDataCenters' 07, 2025 Q1 to 2040 Q4,
        # the workbook's years and the settings at 1 January.
        self.assertEqual(S.QUARTERS, 64)
        self.assertAlmostEqual(S.mid_times()[0], 2025.125)                       # the middle of 2025 Q1
        self.assertAlmostEqual(S.end_times()[-1], 2041.0)                        # the end of 2040
        self.assertAlmostEqual(S.SHARE_TIMES[0], 2025.0)
        self.assertEqual(S.SHARE_TIMES.size, 65)
        self.assertAlmostEqual(float(S.along(np.array([2030.0]), (1.0, 2.0, 3.0, 4.0))[0]), 2.0)
        self.assertAlmostEqual(float(S.along(np.array([2027.5]), (1.0, 2.0, 3.0, 4.0))[0]), 1.5)
        np.testing.assert_allclose(S.between(((2025, 0.1), (2040, 0.3)), np.array([2025.0, 2032.5, 2040.0])),
                                   [0.1, 0.2, 0.3])

    def test_the_packs_a_robot_holds(self):
        packs = S.packs_per_robot(self.params, self.trajectories, np.array([2025.0, 2040.0]))
        # 2025: 24 h / 2, 3.5, 2, 2, 4, 1 h, rounded up
        np.testing.assert_array_equal(packs[:, 0], [12, 7, 12, 12, 6, 24])
        # 2040: type 1 2 h × 550 / 220 = 5 h; type 3 2 h × 700 / 180 = 7.8 h; type 5 4 h × 700 / 250 = 11.2 h;
        # type 6 held at its 4 h of 2030
        np.testing.assert_array_equal(packs[:, 1], [5, 1, 4, 3, 3, 6])
        self.assertAlmostEqual(float(S.runtimes(self.params, self.trajectories, np.array([2040.0]))[2, 0]),
                               2 * 700 / 180)


class TestTheRearrangement(unittest.TestCase):
    """The robot types' draws: each type its own triangle, linked to start from (one correlation a year), then put together
    by the rearrangement algorithm (Puccetti & Rüschendorf 2012) so that the six add up to 1 (Matthias, 2026-11-07: "Yes,
    build it"). By hand."""

    def test_the_unit_triangle_by_hand(self):
        # −1 + √(2u) below the middle, 1 − √(2 (1 − u)) above it; 95 % of it within ±(1 − √0.05) = ±0.7764.
        np.testing.assert_allclose(S.unit_triangle(np.array([0.0, 0.125, 0.5, 0.875, 1.0])), [-1, -0.5, 0, 0.5, 1])
        self.assertAlmostEqual(S.HALF95, 0.776393, places=6)
        self.assertAlmostEqual(1 - (1 - S.HALF95) ** 2, 0.95)

    def test_the_link_by_hand(self):
        # The correlation that gives type 3's start the spread of a type of its own: (m3² − Σm²) / ((Σm)² − Σm²) over
        # the other five. 2025: (0.1764 − 0.0892) / (0.3364 − 0.0892) = 0.35275; 2040: (0.09 − 0.16) / (0.49 − 0.16)
        # = −0.21212.
        modes = np.array([[0.10, 0.05], [0.24, 0.25], [0.42, 0.30], [0.12, 0.30], [0.06, 0.05], [0.06, 0.05]])
        np.testing.assert_allclose(S.link_correlation(modes), [0.0872 / 0.2472, -0.07 / 0.33])
        too_large = np.array([[0.05], [0.05], [0.80], [0.05], [0.03], [0.02]])     # made up: type 3 80 %
        with self.assertRaisesRegex(ValueError, 'robot type 3'):
            S.link_correlation(too_large)

    def test_the_linked_scores(self):
        # Five normal scores a draw, any two correlated by the year's correlation, each with variance 1.
        eps = np.random.default_rng(7).standard_normal((200000, 5))
        x = S.linked_scores(eps, np.array([0.0, 0.35, -0.21]))
        np.testing.assert_allclose(x[:, 0, :], eps, atol=1e-12)                 # no link: the scores themselves
        for i, rho in ((1, 0.35), (2, -0.21)):
            c = np.corrcoef(x[:, i, :].T)
            np.testing.assert_allclose(c[np.triu_indices(5, 1)], rho, atol=0.01)
            np.testing.assert_allclose(x[:, i, :].std(axis=0), 1.0, atol=0.01)

    def test_rearranged_by_hand(self):
        # Two types, weights 1 and 1, draws (1, 1) and (−1, −1): the first type's draws put in the opposite order of
        # the second's, (−1, 1) and (1, −1): both draws add up to 0.
        h = np.array([[1.0, 1.0], [-1.0, -1.0]])
        S.rearrange(h, np.array([1.0, 1.0]), [np.array([1.0, -1.0]), np.array([1.0, -1.0])])
        np.testing.assert_array_equal(h, [[-1.0, 1.0], [1.0, -1.0]])

    def test_type_3_its_own_random_number(self):
        # Type 3 has its own draws from its own random number: other random numbers for type 3 alone change the draws.
        params = Params()
        shares, _ = S.workbook_rows(params)
        rng = np.random.default_rng(9)
        z, u, other = rng.random((500, 5)), rng.random(500), rng.random(500)
        first, _ = S.type_points(params, shares, z, u)
        second, _ = S.type_points(params, shares, z, other)
        self.assertFalse(np.array_equal(first, second))
        np.testing.assert_array_equal(first, S.type_points(params, shares, z, u)[0])    # the same numbers, the same

    def test_only_put_together_never_changed(self):
        # Each type keeps exactly its own draws (sorted, the same before and after); only the draws put together in
        # one row change, and the six then add up far better.
        h = S.unit_triangle(np.random.default_rng(8).random((1000, 6)))
        weights = np.array([0.10, 0.24, 0.42, 0.12, 0.06, 0.06])
        before = h.copy()
        S.rearrange(h, weights, [np.sort(h[:, k])[::-1] for k in range(6)])
        np.testing.assert_array_equal(np.sort(h, axis=0), np.sort(before, axis=0))
        self.assertLess(np.abs(h @ weights).max(), 0.05 * np.abs(before @ weights).max())


class TestTheCount(unittest.TestCase):
    """One chunk of draws with the settings in force: its check passes, and catches each fault made on purpose."""

    @classmethod
    def setUpClass(cls):
        cls.params = Params()
        shares, trajectories = S.workbook_rows(cls.params)
        rng = np.random.default_rng(3)
        n = 30
        points, _ = S.type_points(cls.params, shares, rng.random((n, 5)), rng.random(n))
        cls.counted, cls.needs = S.count(cls.params, shares, trajectories, points,
                                         S.triangle_ppf(rng.random(n), 0.75, 0.80, 0.85),
                                         S.triangle_ppf(rng.random(n), 0.7, 1.0, 1.2),
                                         S.triangle_ppf(rng.random(n), 0.7, 1.0, 1.2),
                                         S.triangle_ppf(rng.random(n), 0.7, 1.0, 1.2))

    def test_it_adds_up(self):
        self.assertEqual(S.check(self.params, self.counted, self.needs), [])
        article = self.counted[('article', 0)]                                    # the article's robots, the frame
        np.testing.assert_allclose(article.stock[:, 3::4],                        # the end of 2025 to 2040
                                   np.broadcast_to([ARTICLE[y] for y in range(2025, 2041)], (30, 16)), rtol=1e-12)
        np.testing.assert_allclose(article.start, 10e6 / 1.16, rtol=1e-12)        # 1 January 2025
        # The six types add up to the article's robots in every draw: one number.
        types = sum(self.counted[('robots', t)].stock for t in S.TYPES)
        np.testing.assert_allclose(types, article.stock, rtol=1e-9)
        for t in S.TYPES:
            np.testing.assert_allclose(self.counted[('joint sets', t)].stock, self.counted[('robots', t)].stock,
                                       rtol=1e-9)
            self.assertTrue((self.counted[('battery packs', t)].stock >= self.needs[t] * (1 - 1e-9)).all())

    def test_the_robots_built_and_retired_have_a_band(self):
        # The lifetime of a draw (2026-11-07: "30% short and 20% longer"): the article's robots built and retired differ
        # from draw to draw, though its robots in use are the same in every draw.
        built, _, gone = S.years_of(self.counted[('article', 0)])
        self.assertGreater(np.ptp(built[:, 0]), 0)
        self.assertGreater(np.ptp(gone[:, 5]), 0)
        self.assertGreater(np.ptp(S.years_of(self.counted[('battery packs', 3)])[2][:, 5]), 0)
        joints_built, _, joints_gone = S.years_of(self.counted[('joint sets', 3)])
        self.assertGreater(np.ptp(joints_built[:, 5]), 0)
        self.assertGreater(np.ptp(joints_gone[:, 5]), 0)

    def test_every_type_has_a_band(self):
        # Every type's robots differ from draw to draw (2026-11-07: "also the rest has to be done with MonteCarlo").
        for t in S.TYPES:
            self.assertGreater(np.ptp(self.counted[('robots', t)].stock[:, -1]), 0, t)

    def test_the_robots_of_2025_by_hand(self):
        # The article's 2025 at the end of 2025, its start 8.62 M; with the lifetimes 5 / 7 / 10 years a young fleet
        # growing by 16 % a year; the stock of 2025 its end, as 07.
        article = self.counted[('article', 0)]
        built, stock, gone = S.years_of(article)
        self.assertAlmostEqual(stock[0, 0], 10e6, delta=1e-3)
        self.assertAlmostEqual(article.start[0] + built[0, 0] - gone[0, 0], 10e6, delta=1e-3)
        self.assertGreater(gone[0, 0], 0.5e6)
        self.assertLess(gone[0, 0], 1.2e6)

    def faults_of(self, key, field, change):
        """check() of the chunk with one array of one stock changed."""
        counted = dict(self.counted)
        values = getattr(counted[key], field).copy()
        change(values)
        counted[key] = counted[key]._replace(**{field: values})
        return S.check(self.params, counted, self.needs)

    def test_a_wrong_start_is_caught(self):
        def other(values):
            values *= 1.01                                                        # not 10 M / 1.16
        self.assertTrue(any('1 January 2025' in f for f in self.faults_of(('article', 0), 'start', other)))

    def test_each_fault_is_caught(self):
        def more(values):
            values[:, 7] *= 1.001
        self.assertTrue(any('stock before + inflow' in f
                            for f in self.faults_of(('battery packs', 4), 'gone', more)))
        self.assertTrue(any("not the article's" in f for f in self.faults_of(('article', 0), 'stock', more)))
        self.assertTrue(any('do not add up' in f for f in self.faults_of(('robots', 2), 'stock', more)))
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


class TestTheDistributionPanels(unittest.TestCase):
    """The units the distribution pages write in, and a triangle's share of the draws in each bar, by hand."""

    def test_the_units_by_hand(self):
        self.assertEqual(S.count_unit(np.array([600e3])), (1e3, 'thousand robots'))
        self.assertEqual(S.count_unit(np.array([2.4e6])), (1e6, 'million robots'))
        self.assertEqual(S.count_unit(np.array([3.8e9, 0.0])), (1e9, 'billion robots'))   # over the draws above 0
        self.assertEqual(S.mass_unit(np.array([2.5e8])), (1e6, 'kt'))
        self.assertEqual(S.mass_unit(np.array([1.2e9])), (1e9, 'Mt'))
        self.assertEqual(S.mass_unit(np.array([500.0])), (1.0, 'kg'))
        self.assertEqual(S.mass_unit(np.array([0.5])), (1e-3, 'g'))


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
        # Each element by its kind and its part of how a robot is taken apart, as 02 writes them (taken_apart): the
        # frame's aluminium, the computer's copper (a PCB), the joints' motors' copper and their driver boards' (small
        # PCBs, in the joint sets), the cells' lithium and the battery management board's copper (a small PCB, in the
        # packs): the electronics in three units, each with its own lifetime.
        columns = ['Frame and shell: Frame: Al', 'Boards and computers: PCB: Cu',
                   'Hip joints: Motor windings and steel: Cu', 'Hip joints: Small PCB: Cu',
                   'Arm joints and hands: Motor windings and steel: Cu', 'Battery pack: Cells: Li',
                   'Battery pack: Small PCB: Cu']
        draw = np.arange(N) / N
        values = np.column_stack([t * (1 + draw), np.full(N, 0.25), np.ones(N), np.full(N, 0.2), np.full(N, 0.5),
                                  np.full(N, 2.0), np.full(N, 0.1)])
        with open(os.path.join(apart, 'taken_apart.txt'), 'w', encoding='utf-8') as handle:
            handle.write('\n'.join(columns) + '\n')
        np.save(os.path.join(apart, 'taken_apart.npy'), values.astype(np.float32))


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
        cls.params, cls.problems, cls.saved, cls.covered, cls.titles = params, [], [], [], []
        cls.panels, cls.texts, cls.figure_legends, cls.type_numbers, cls.limits, cls.rows = {}, {}, {}, {}, {}, {}
        cls.element_numbers = {}
        save = Figure.savefig

        def checked(figure, path, *args, **kwargs):
            name = os.path.basename(str(path))
            cls.problems += page_problems(figure, name, kwargs.get('dpi'))
            renderer = figure.canvas.get_renderer()
            cls.covered += [(name, axes.get_title()) for axes in figure.axes if axes.get_legend() is not None
                            and S.lines_under(axes, axes.get_legend().get_window_extent(renderer), renderer)]
            cls.saved.append(str(path))
            where = os.path.relpath(str(path), params.output.stock_and_flow_figures_dir)
            cls.panels[where] = [a.panel_numbers for a in figure.axes if getattr(a, 'panel_numbers', None) is not None]
            cls.texts[where] = [t.get_text() for t in figure.texts]
            cls.figure_legends[where] = [t.get_text() for legend in figure.legends for t in legend.get_texts()]
            cls.element_numbers[where] = [a.element_numbers for a in figure.axes if getattr(a, 'element_numbers', None)]
            cls.type_numbers[where] = [a.type_numbers for a in figure.axes if getattr(a, 'type_numbers', None)]
            cls.limits[where] = [(a.get_title(loc='left'), a.get_xlim()) for a in figure.axes if a.axison]
            from matplotlib.colors import to_hex
            cls.rows[where] = [({to_hex(p.get_facecolor()): p.get_y() for p in a.patches},
                                {t.get_text(): y for t, y in zip(a.get_yticklabels(), a.get_yticks())},
                                {c: (min(p.get_x() for p in a.patches if to_hex(p.get_facecolor()) == c),
                                     max(p.get_x() + p.get_width() for p in a.patches if to_hex(p.get_facecolor()) == c))
                                 for c in {to_hex(p.get_facecolor()) for p in a.patches}})
                               for a in figure.axes if getattr(a, 'type_numbers', None)]
            cls.legends = getattr(cls, 'legends', []) + [
                (name, [t.get_text() for t in a.get_legend().get_texts()]) for a in figure.axes
                if not a.axison and a.get_legend() is not None]
            # Each pair of neighbours on a row of panels, by their titles (the overview's 'beside').
            panels = sorted((a for a in figure.axes if a.get_visible() and a.axison and a.get_title()),
                            key=lambda a: (-round(a.get_position().y0, 2), a.get_position().x0))
            cls.titles += [(a.get_title().replace('\n', ' '), b.get_title().replace('\n', ' '))
                           for a, b in zip(panels, panels[1:])
                           if round(a.get_position().y0, 2) == round(b.get_position().y0, 2)]
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
        self.assertRegex(self.printed, r'type 3 off its own draws by at most \d+\.\d+ % of its half-width')
        self.assertEqual(self.files['units_stock'].shape, (N, 16, 3, 6))       # the end of 2025 to the end of 2040
        self.assertEqual(self.files['units_in'].shape, (N, 16, 3, 6))          # 2025 to 2040
        self.assertEqual(self.files['elements_stock'].shape, (N, 16, 14, 4))   # the 14 parts of how it is taken apart

    def test_the_robots_as_the_article(self):
        # The robots in use at the end of each year, as 07 reports its stocks: the article's value of the year, 10 M
        # (2025) to 70 × 10⁹ (2040) ("Follow the artcile!! 70 x 10E9"); the types each their own share of it.
        robots = np.load(os.path.join(self.params.output.stock_and_flow_dir, 'article_stock.npy'))
        np.testing.assert_allclose(robots, np.broadcast_to([ARTICLE[y] for y in range(2025, 2041)], (N, 16)),
                                   rtol=1e-6)                                    # float32: 7 digits
        types = self.files['units_stock'][:, :, 0, :].sum(axis=2)
        np.testing.assert_allclose(types, robots, rtol=1e-6)                      # one number in every draw

    def test_every_type_inside_its_own_triangle(self):
        # Each type's share of each year's robots built lies in every draw between the lowest foot and the highest top
        # of its triangle in the year's four quarters (step 2); type 3 within what the run says it lies off its own
        # draws (40 draws cannot be put together exactly: 23 % of its half-width here; 0.14 % at 200,000 draws).
        import re
        off = float(re.search(r'off its own draws by at most (\d+\.\d+) %', self.printed).group(1)) / 100
        built = self.files['units_in'][:, :, 0, :].astype(np.float64)
        article = np.load(os.path.join(self.params.output.stock_and_flow_dir, 'article_in.npy')).astype(np.float64)
        shares, _ = S.workbook_rows(self.params)
        times = S.mid_times()
        modes, ends = S.type_modes(self.params, shares, times), S.type_ends(self.params, times)
        for k in range(len(S.TYPES)):
            low = (modes[k] * (1 - ends)).reshape(16, 4).min(axis=1)
            high = (modes[k] * (1 + ends)).reshape(16, 4).max(axis=1)
            slack = 1e-5 + (off * (modes[k] * ends).max() if S.TYPES[k] == S.BALANCING_TYPE else 0.0)
            share = built[:, :, k] / article
            self.assertTrue((share >= low - slack).all() and (share <= high + slack).all(), S.TYPES[k])

    def test_every_kg_by_hand(self):
        # Every part by hand, in the stock, the inflow and the outflow: each part's kg of one robot of type t in draw i
        # times the units of type t that carry it (the robots, the joint sets, the packs), added over the types.
        al, cu, li = ELEMENTS.index('Al'), ELEMENTS.index('Cu'), ELEMENTS.index('Li')
        part = {name: S.PARTS.index(name) for name in ('Frame', 'PCB', 'Motor windings and steel', 'Small PCB',
                                                       'Cells')}
        frame = np.array(S.TYPES)[None, :] * (1 + np.arange(N) / N)[:, None]    # draw i, type t
        for units_name, element_name in zip(S.UNIT_FILES, S.ELEMENT_FILES):
            units, kg = self.files[units_name].astype(np.float64), self.files[element_name].astype(np.float64)
            robots, joints, packs = (units[:, :, j, :] for j in range(3))
            expected = {
                ('Frame', al): (robots * frame[:, None, :]).sum(axis=2),                  # the pairing of draw i
                ('PCB', cu): robots.sum(axis=2) * 0.25,
                ('Motor windings and steel', cu): joints.sum(axis=2) * 1.5,
                # The electronics in the joints with the joint sets, in the packs with the packs: their own lifetimes.
                ('Small PCB', cu): joints.sum(axis=2) * 0.2 + packs.sum(axis=2) * 0.1,
                ('Cells', li): packs.sum(axis=2) * 2.0}
            for (name, e), values in expected.items():
                np.testing.assert_allclose(kg[:, :, part[name], e], values, rtol=1e-5, err_msg=(element_name, name))
            # Nothing anywhere else: every other part and element 0.
            rest = kg.copy()
            for (name, e) in expected:
                rest[:, :, part[name], e] = 0
            self.assertEqual(rest.max(), 0.0, element_name)
        # The groups add up from their parts: the electronics' copper the PCB's and the small PCBs'.
        electronics = [S.PARTS.index(p) for p in S.PARTS if S.schemas.TAKEN_GROUP[p] == 'Electronics']
        kg = self.files['elements_stock'].astype(np.float64)
        np.testing.assert_allclose(kg[:, :, electronics, cu].sum(axis=2),
                                   kg[:, :, part['PCB'], cu] + kg[:, :, part['Small PCB'], cu], rtol=1e-12)

    def test_its_summary(self):
        import csv
        with open(os.path.join(self.params.output.stock_and_flow_dir, S.SUMMARY), newline='',
                  encoding='utf-8') as handle:
            rows = list(csv.DictReader(handle))
        first = next(r for r in rows if r['quantity'] == 'robots' and r['robot type'] == 'all'
                     and r['flow'] == 'stock' and r['year'] == '2025')
        self.assertAlmostEqual(float(first['mean']), 10e6, delta=10)            # the end of 2025: the article's
        neodymium = [r for r in rows if r['quantity'] == 'Neodymium']
        self.assertTrue(neodymium and all(r['mean'] == '–' and r['held in % of the draws'] == '0.0'
                                          for r in neodymium))
        # Each type's share of the robots built in a year, % (2026-11-07, "Add it beside"): from the draws, draw by
        # draw, its built over the article's built, its own drawn share.
        built = self.files['units_in'][:, :, 0, :].astype(np.float64)
        article = np.load(os.path.join(self.params.output.stock_and_flow_dir, 'article_in.npy')).astype(np.float64)
        shares = 100 * built / article[:, :, None]
        for t in S.TYPES:
            got = [float(r['mean']) for r in rows if r['quantity'] == S.SHARE_QUANTITY and r['robot type'] == str(t)]
            np.testing.assert_allclose(got, shares[:, :, t - 1].mean(axis=0), rtol=1e-5, err_msg=t)

    def test_the_overview_has_the_share_panel_beside_the_types(self):
        self.assertIn(('Robots in use by robot type', 'Share of the robots built by robot type'), self.titles)
        # The robot types' legend in the eighth place, its six entries (found 2026-11-07: it came out empty).
        self.assertIn((S.OVERVIEW, [f'robot type {t}' for t in S.TYPES]), self.legends)

    def test_its_pages(self):
        names = sorted(os.path.relpath(p, self.params.output.stock_and_flow_figures_dir) for p in self.saved)
        held = ('Lithium', 'Aluminium', 'Copper')
        D = S.DISTRIBUTIONS_DIR
        self.assertEqual(names, sorted([S.OVERVIEW] + [os.path.join(S.ELEMENTS_DIR, f'{e}.png') for e in held]
                                       + [os.path.join(D, f) for f in ('robots_in_use.png', 'robots_in_use_numbers.png')]
                                       + [os.path.join(D, f'elements_{y}.png') for y in (2025, 2030, 2035, 2040)]
                                       + [os.path.join(D, f'parts_{y}_1.png') for y in (2025, 2030, 2035, 2040)]))
        self.assertTrue(all(os.path.exists(p) for p in self.saved))
        self.assertEqual(self.problems, [])
        self.assertEqual(self.covered, [])                     # no line and no written value under a legend
        self.assertIn('Neodymium: no numbers, 0 kg in every draw; no page.', self.printed)

    def test_the_distribution_pages(self):
        # Matthias, 2026-11-07: "I also want the distributions"; 2026-11-08: "can you not combine the 6 types to 1", "I
        # want to see at the end how many robots there are", "it is 2025, 2030, 2035 and 2040!!", the years as 07's
        # ("Yes!!"): one page of the robots in use at the end of 2025, 2030, 2035, 2040, a panel a year, the six types
        # one above the other, the robots in all in its title; every draw on its axis (why is the largest part of the
        # triangal cut off?); the numbers on the page after. Each element in use at the four year ends, split by part,
        # its numbers after it.
        D, E = S.DISTRIBUTIONS_DIR, os.path.join(S.DISTRIBUTIONS_DIR, S.ELEMENTS_DIR)
        page = os.path.join(D, 'robots_in_use.png')
        panels = self.type_numbers[page]
        self.assertEqual(len(panels), 4)
        self.assertTrue(all(len(rows) == 6 for rows in panels))
        titles = [title for title, _ in self.limits[page]]
        # The year alone (Matthias, 2026-11-08: "Sorry end of goes away. This is not needed").
        self.assertEqual(titles, [f'{y}: {ARTICLE[y]:,.0f} robots' for y in (2025, 2030, 2035, 2040)])
        # By hand: robot type 3 at the end of 2040, in its panel's unit.
        values = self.files['units_stock'][:, 15, 0, 2].astype(np.float64)
        everything = self.files['units_stock'][:, 15, 0, :].astype(np.float64)
        per, word = S.count_unit(everything.max(axis=1))
        name, median, mean, low, high, unit = panels[3][2]
        self.assertEqual((name, unit), ('Robot type 3, 2040', word))
        self.assertAlmostEqual(median, np.median(values) / per, places=6)
        self.assertAlmostEqual(mean, values.mean() / per, places=6)
        np.testing.assert_allclose([low, high], np.percentile(values, (2.5, 97.5)) / per, rtol=1e-9)
        # Type 1's row at the top, type 6's at the bottom, each labelled where its bars stand.
        for bottoms, labels, _ in self.rows[page]:
            for k, t in enumerate(S.TYPES):
                self.assertEqual(bottoms[S.TYPE_COLOURS[k].lower()], 5 - k)
                self.assertAlmostEqual(labels[f'robot type {t}'], 5 - k + 0.4)
        # Nothing cut: type 3's bars of 2040 run from its smallest to its largest draw.
        left, right = self.rows[page][3][2][S.TYPE_COLOURS[2].lower()]
        self.assertAlmostEqual(left, values.min() / per, places=9)
        self.assertAlmostEqual(right, values.max() / per, places=9)
        # Nothing cut: the axis holds the smallest and the largest draw of all six types.
        left, right = self.limits[page][3][1]
        self.assertLessEqual(left, everything.min() / per + 1e-12)
        self.assertGreaterEqual(right, everything.max() / per - 1e-12)
        words = ' '.join(self.texts[os.path.join(D, 'robots_in_use_numbers.png')])
        for rows in panels:
            for row in rows:
                self.assertIn(row[0], words)
        # The elements in all robots in use, a page a year, exactly as RAWCLICDataCenters' 05 draws a data centre's
        # elements (Matthias, 2026-11-08: "I also want finally see the distribution. Exactkly the figures we have
        # worked out for the data centers!!!"): a panel per element held, each bar split by part, its mean with its
        # number, 95 % dashed. By hand: copper in 2040, all parts added up, in its unit.
        page = os.path.join(D, 'elements_2040.png')
        panels = self.element_numbers[page]
        self.assertEqual([p[0] for p in panels], ['Lithium (Li)', 'Aluminium (Al)', 'Copper (Cu)'])
        total = self.files['elements_stock'][:, 15, :, ELEMENTS.index('Cu')].astype(np.float64).sum(axis=1)
        per, unit = S.mass_unit(total)
        title, mean, low, high, written = next(p for p in panels if p[0] == 'Copper (Cu)')
        self.assertEqual(written, unit)
        self.assertAlmostEqual(mean, total.mean() / per, places=6)
        np.testing.assert_allclose([low, high], np.percentile(total, (2.5, 97.5)) / per, rtol=1e-9)
        # Its legend the groups drawn on the page, in their order: aluminium in the body, lithium in the battery,
        # copper in the joints and the electronics.
        self.assertEqual(self.figure_legends[page], ['Joints', 'Battery', 'Electronics', 'Body'])
        self.assertEqual(len(self.element_numbers[os.path.join(D, 'elements_2025.png')]), 3)

    def test_an_element_held_in_some_draws(self):
        # "A 0 is not part of a distribution": copper held in half the draws, in the frame only; lithium in no
        # draw. The page: copper's mean and 95 % over the draws that hold it, "held in 50 % of the draws" written,
        # no panel for lithium, and a legend of the one part drawn.
        from matplotlib.figure import Figure
        from unittest import mock
        rng = np.random.default_rng(7)
        kg = np.zeros((400, len(S.PARTS), 2))
        kg[::2, S.PARTS.index('Frame'), 0] = rng.uniform(1e3, 2e3, 200)
        seen = {}

        def record(figure, path, *args, **kwargs):
            seen['numbers'] = [a.element_numbers for a in figure.axes if getattr(a, 'element_numbers', None)]
            seen['words'] = [t.get_text() for a in figure.axes for t in a.texts]
            seen['legend'] = [t.get_text() for legend in figure.legends for t in legend.get_texts()]

        with tempfile.TemporaryDirectory() as folder, mock.patch.object(Figure, 'savefig', record):
            S.elements_page(2040, kg, ['Cu', 'Li'], 400, os.path.join(folder, 'elements_2040.png'), 50)
        held = kg[::2, S.PARTS.index('Frame'), 0]
        per, unit = S.mass_unit(held)
        [(title, mean, low, high, written)] = seen['numbers']
        self.assertEqual(title, 'Copper (Cu)')
        self.assertAlmostEqual(mean, held.mean() / per, places=9)
        np.testing.assert_allclose([low, high], np.percentile(held, (2.5, 97.5)) / per, rtol=1e-9)
        self.assertTrue(any('held in 50 % of the draws' in w for w in seen['words']))
        self.assertEqual(seen['legend'], ['Body'])

    def test_the_list_part_by_part(self):
        # Matthias, 2026-11-08: "I want a detailed list of the component ... to know how to take it apart!!!": after
        # each year's page of the elements, the list of every element in each part that holds it, by hand: the small
        # PCBs' copper at the end of 2040 the joint sets' 0.2 kg and the packs' 0.1 kg; no row for a part that holds
        # none (the cells' copper); every row once; the page shows the rows.
        stock = self.files['elements_stock'][:, 15].astype(np.float64)
        rows = S.parts_rows(stock, ELEMENTS)
        self.assertEqual([tuple(r[:3]) for r in rows], [
            ('Lithium', 'Battery', 'Cells'), ('Aluminium', 'Body', 'Frame'),
            ('Copper', 'Joints', 'Motor windings and steel'), ('Copper', 'Electronics', 'PCB'),
            ('Copper', 'Electronics', 'Small PCB')])
        units = self.files['units_stock'][:, 15].astype(np.float64).sum(axis=2)
        small = 0.2 * units[:, 1] + 0.1 * units[:, 2]
        per, unit = S.mass_unit(small)
        row = next(r for r in rows if r[2] == 'Small PCB')
        self.assertEqual(row[3], 'all draws')
        self.assertEqual(row[5], f'{S.composition.panel_number(small.mean() / per)} {unit}')
        low, high = np.percentile(small / per, (2.5, 97.5))
        self.assertEqual(row[6], f'{S.composition.panel_number(low)} to {S.composition.panel_number(high)} {unit}')
        page = os.path.join(S.DISTRIBUTIONS_DIR, 'parts_2040_1.png')
        for r in rows:
            self.assertIn(r[5], self.texts[page])
        self.assertEqual(self.texts[page].count('Small PCB'), 1)

    def test_the_list_over_the_draws_that_hold_it(self):
        # "A 0 is not part of a distribution": copper in the small PCBs in half of 400 draws, in the frame in all; the
        # list's row of the small PCBs held in 50 %, its median, mean and 95 % over the 200 draws that hold it.
        rng = np.random.default_rng(11)
        kg = np.zeros((400, len(S.PARTS), 1))
        kg[::2, S.PARTS.index('Small PCB'), 0] = rng.uniform(10.0, 30.0, 200)
        kg[:, S.PARTS.index('Frame'), 0] = rng.uniform(1.0, 2.0, 400)
        rows = {r[2]: r for r in S.parts_rows(kg, ['Cu'])}
        self.assertEqual(sorted(rows), ['Frame', 'Small PCB'])
        held = kg[::2, S.PARTS.index('Small PCB'), 0]
        per, unit = S.mass_unit(held)
        low, median, high = np.percentile(held / per, (2.5, 50, 97.5))
        n = S.composition.panel_number
        self.assertEqual(rows['Small PCB'][3:], ['50 %', f'{n(median)}\u00a0{unit}', f'{n(held.mean() / per)}\u00a0{unit}',
                                                 f'{n(low)} to {n(high)}\u00a0{unit}'])
        self.assertEqual(rows['Frame'][3], 'all draws')

    def test_the_years_of_the_summary(self):
        # As 07: the stocks at the end of 2025 to 2040, the flows of the calendar years 2025 to 2040.
        import csv
        with open(os.path.join(self.params.output.stock_and_flow_dir, S.SUMMARY), newline='',
                  encoding='utf-8') as handle:
            rows = list(csv.DictReader(handle))
        stock = [r['year'] for r in rows if r['quantity'] == 'robots' and r['robot type'] == 'all' and r['flow'] == 'stock']
        built = [r['year'] for r in rows if r['quantity'] == 'robots' and r['robot type'] == 'all' and r['flow'] == 'in']
        self.assertEqual(stock, [str(y) for y in range(2025, 2041)])
        self.assertEqual(built, [str(y) for y in range(2025, 2041)])

    def test_the_summary_by_group_and_part(self):
        # Each element by group ('Copper, Electronics') and by part ('Copper, Electronics: Small PCB'), each over its
        # draws above 0, every flow, every year; a part or group that holds none of it '–'.
        import csv
        with open(os.path.join(self.params.output.stock_and_flow_dir, S.SUMMARY), newline='',
                  encoding='utf-8') as handle:
            rows = list(csv.DictReader(handle))
        cu = ELEMENTS.index('Cu')
        for element_name, flow in zip(S.ELEMENT_FILES, S.FLOWS):
            kg = self.files[element_name].astype(np.float64)
            for j, part in enumerate(S.PARTS):
                group = S.schemas.TAKEN_GROUP[part]
                got = [r for r in rows if r['quantity'] == f'Copper, {group}: {part}' and r['flow'] == flow]
                self.assertEqual(len(got), 16, part)
                values = kg[:, 5, j, cu]
                row = next(r for r in got if r['year'] == '2030')
                if (values > 0).any():
                    above = values[values > 0]
                    self.assertAlmostEqual(float(row['mean']) / above.mean(), 1.0, places=5)
                    low, high = np.percentile(above, (2.5, 97.5))
                    self.assertAlmostEqual(float(row['2.5 %']) / low, 1.0, places=5)
                    self.assertAlmostEqual(float(row['97.5 %']) / high, 1.0, places=5)
                else:
                    self.assertEqual(row['mean'], '–')                             # the cells hold no copper
            for group in S.GROUPS:
                values = kg[:, 5, [S.PARTS.index(p) for p in S.PARTS if S.schemas.TAKEN_GROUP[p] == group],
                            cu].sum(axis=1)
                row = next(r for r in rows if r['quantity'] == f'Copper, {group}' and r['flow'] == flow
                           and r['year'] == '2030')
                if (values > 0).any():
                    self.assertAlmostEqual(float(row['mean']) / values[values > 0].mean(), 1.0, places=5)
                else:
                    self.assertEqual(row['mean'], '–')                             # the battery's copper is a PCB's
        # By hand: the small PCBs' copper in use at the end of 2025, the joint sets' 0.2 kg and the packs' 0.1 kg.
        small = next(r for r in rows if r['quantity'] == 'Copper, Electronics: Small PCB' and r['flow'] == 'stock'
                     and r['year'] == '2025')
        units = self.files['units_stock'][:, 0, :, :].astype(np.float64).sum(axis=2)
        self.assertAlmostEqual(float(small['mean']) / (0.2 * units[:, 1] + 0.1 * units[:, 2]).mean(), 1.0, places=5)

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
                                'taken_apart.txt')
            with open(text, encoding='utf-8') as handle:
                written = handle.read()
            for wrong, words in (('Wings: Frame: Al', "'Wings: Frame: Al' of 02 is no kind"),
                                 ('Frame and shell: Gizmo: Al', "'Frame and shell: Gizmo: Al' of 02 is no kind")):
                with open(text, 'w', encoding='utf-8') as handle:
                    handle.write(written.replace('Frame and shell: Frame: Al', wrong))
                with self.assertRaisesRegex(ValueError, words):
                    S.robot_parts(params)


if __name__ == '__main__':
    unittest.main()
