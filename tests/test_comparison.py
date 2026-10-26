"""
Tests of 03_comparison.py: the robot types side by side, from the draws of 02_composition.py.

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

Point 15 of the specification (documentation/claude/HANDOVER.md): "03 reads the six robot types' draws from 02, never
re-deriving them, and draws them side by side: by material, by element, by part group and body region, each with its
95 % interval." The tests draw the small workbook of tests/test_schemas.py with 02 (2,000 draws, into a temporary
folder), then run 03 on what 02 wrote: press Run, nothing in the project is changed.
"""

import csv
import importlib.util
import os
import sys
import unittest

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)

import test_composition as drawn_tests  # noqa: E402  the small files, and 02 loaded as `composition`

_spec = importlib.util.spec_from_file_location('comparison', os.path.join(ROOT, '03_comparison.py'))
comparison = importlib.util.module_from_spec(_spec)
sys.modules['comparison'] = comparison  # the dataclasses of 03 look their module up here while it loads
_spec.loader.exec_module(comparison)

composition = drawn_tests.composition
FOLDERS = ('1_small', '2_large')


class Compared(drawn_tests.Drawn):
    """Writes the small files, draws them with 02, and gives the settings 03 runs with."""

    def drawn(self, **inputs):
        params = self.write(**inputs)
        self.assertEqual(composition.run(params), 0)
        return params


class TestComparison(Compared):

    def test_it_reads_the_draws_of_02_as_they_are(self):
        params = self.drawn()
        robots = comparison.read_draws(params)
        self.assertEqual([r.number for r in robots], [1, 2])
        for robot, folder in zip(robots, FOLDERS):
            for table in composition.TABLES:
                written = np.load(os.path.join(params.output.composition_dir, folder, f'{table}.npy'))
                np.testing.assert_array_equal(robot.tables[table][1], written)

    def test_its_statistics_agree_with_the_summary_of_02(self):
        # 02 computes its summary from its own draws before writing them as float32; 03 from the written draws.
        params = self.drawn()
        robots = comparison.read_draws(params)
        for robot, folder in zip(robots, FOLDERS):
            with open(os.path.join(params.output.composition_dir, folder, 'summary.csv'), encoding='utf-8',
                      newline='') as file:
                summary = {(r['Kind'], r['Name']): r for r in csv.DictReader(file)}
            for kind, table in (('Material', 'materials'), ('Element', 'elements')):
                for name in robot.tables[table][0]:
                    present, mean, low, high = comparison.statistics(robot.column(table, name))
                    row = summary[(kind, name)]
                    for got, heading in ((mean, 'Mean (kg)'), (low, '2.5 % (kg)'), (high, '97.5 % (kg)')):
                        self.assertAlmostEqual(got, float(row[heading]), delta=1e-5 * max(1, abs(got)),
                                               msg=f'{folder}, {name}, {heading}')

    def test_a_page_is_drawn_for_each_view(self):
        params = self.drawn()
        self.assertEqual(comparison.run(params), 0)
        for view in comparison.VIEWS:
            self.assertGreater(os.path.getsize(os.path.join(params.output.comparison_dir, f'{view}.png')), 0)

    def test_without_the_draws_of_02_it_stops(self):
        params = self.write()
        self.assertEqual(comparison.run(params), 1)
        self.assertFalse(os.path.exists(params.output.comparison_dir))

    def test_draws_that_do_not_belong_together_stop(self):
        # A check is only trusted once it has been seen to catch what it guards.
        for folder, table, change, words in (
                ('2_large', 'total', lambda a: a[:-1], 'robot type 2: total has 1999 draws, not 2000'),
                ('1_small', 'materials', lambda a: a * 1.01, 'robot type 1: the materials do not add up to the total'),
                ('2_large', 'body_regions', lambda a: a[:, ::-1], None)):
            params = self.drawn()
            path = os.path.join(params.output.composition_dir, folder, f'{table}.npy')
            np.save(path, change(np.load(path)))
            if words is None:
                # The columns read in another order: the names no longer match the draws, but every sum still
                # holds; the order of the columns is checked against the other robot types instead.
                with open(os.path.join(params.output.composition_dir, folder, f'{table}.txt'), encoding='utf-8') as f:
                    columns = f.read().splitlines()
                with open(os.path.join(params.output.composition_dir, folder, f'{table}.txt'), 'w',
                          encoding='utf-8') as f:
                    f.write(''.join(f'{c}\n' for c in columns[::-1]))
                words = 'robot type 2: the columns of body_regions are not those of robot type 1'
            problems = comparison.problems(comparison.read_draws(params))
            self.assertEqual(len(problems), 1, problems)
            self.assertIn(words, problems[0])
            self.assertEqual(comparison.run(params), 1)


if __name__ == '__main__':
    unittest.main()
