"""
Tests of 05_combined_stock_and_flow.py and tools/copy_data_center_draws.py: the AI data centres of RAWCLICDataCenters'
07 and the humanoid robots of 04 together, with their distributions.

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

Matthias, 2026-11-08: "write 05 combination of results of 04 and 07 with the distributions", rows 1 to 8, "Yes, build
it" (documentation/claude/EVIDENCE.md E52). Made-up draws in temporary folders, every kilogram by hand: the copy of a
made-up file in 07's form; 05 on made-up draws of 07 and 04; its checks, each with a deliberate fault. Nothing in data/
or figures/ is touched.
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


def load(name: str, path: str):
    """A file of the project whose name starts with a digit or lies outside a package, as a module."""
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, path))
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


C = load('combined_stock_and_flow', '05_combined_stock_and_flow.py')
T = load('copy_data_center_draws', os.path.join('tools', 'copy_data_center_draws.py'))
from src.params_schema import Params, absolute  # noqa: E402

N = 30
ROBOT_ELEMENTS = ['Li', 'Al', 'Cu', 'Nd']          # 04's (made up): neodymium 0 in every draw
CENTRE_ELEMENTS = ['Cu', 'Al', 'Sr']               # 07's (made up): strontium the data centres' only
YEARS = 16


def centre_value(s, d, y, f, e):
    """A made-up kg of 07's copy: scenario s, draw d, year y, flow f, element e (07's order)."""
    return (s + 1) * (1 + d / N) * (y + 1) * (f + 1) * (e + 1) * 1e3


def robot_value(d, y, p, e):
    """A made-up kg of 04: draw d, year y, part p, element e (04's order); neodymium 0."""
    return 0.0 if ROBOT_ELEMENTS[e] == 'Nd' else (1 + d) * (y + 1) * (p + 1) * (e + 1) * 10.0


def write_inputs(params: Params, draws: int = N, years: int = YEARS) -> None:
    """The made-up copy of 07's draws and 04's draws where 05 reads them (params' folders)."""
    copy = absolute(params.data.data_center_draws_dir)
    os.makedirs(copy)
    s, d, y, f, e = np.meshgrid(*(np.arange(k) for k in (3, draws, years, 3, len(CENTRE_ELEMENTS))), indexing='ij')
    np.save(os.path.join(copy, C.COPY_DRAWS), centre_value(s, d, y, f, e).astype(np.float32))
    with open(os.path.join(copy, C.COPY_ELEMENTS), 'w', encoding='utf-8') as handle:
        handle.write('\n'.join(CENTRE_ELEMENTS) + '\n')
    with open(os.path.join(copy, C.COPY_SOURCE), 'w', encoding='utf-8') as handle:
        handle.write('source: /made/up/stock_flow_draws.csv\nmodified: 2026-10-23 14:38:00\ncopied: 2026-11-08 18:00:00\n')
    flows = absolute(params.output.stock_and_flow_dir)
    os.makedirs(flows)
    d, y, p, e = np.meshgrid(*(np.arange(k) for k in (N, YEARS, len(C.flow.PARTS), len(ROBOT_ELEMENTS))),
                             indexing='ij')
    for k, name in enumerate(C.flow.ELEMENT_FILES):
        np.save(os.path.join(flows, f'{name}.npy'), ((k + 1) * np.vectorize(robot_value)(d, y, p, e))
                .astype(np.float32))
    book = C.schemas.read_workbook(absolute(params.data.workbook), params)
    consolidated = os.path.join(absolute(params.output.composition_dir), C.composition.folder_name(book.categories[0]))
    os.makedirs(consolidated)
    with open(os.path.join(consolidated, 'elements.txt'), 'w', encoding='utf-8') as handle:
        handle.write('\n'.join(ROBOT_ELEMENTS) + '\n')


def settings(folder: str) -> Params:
    """The settings of a run into `folder`: every input and output there."""
    params = Params()
    where = lambda name: os.path.join(folder, name)                       # noqa: E731
    params.data = dataclasses.replace(params.data, data_center_draws_dir=where('copy'))
    params.output = dataclasses.replace(params.output, composition_dir=where('consolidated'),
                                        stock_and_flow_dir=where('flows'), combined_dir=where('combined'),
                                        combined_figures_dir=where('figures'))
    return params


class TestTheCopy(unittest.TestCase):
    """tools/copy_data_center_draws.py on a made-up file in 07's form: every number copied, 2022 to 2024 and the
    collected left out; a missing or doubled row stops it."""

    def write_csv(self, path: str, rows_left_out=(), row_twice=None) -> None:
        elements = ['Cu', 'Al']
        header = ['scenario', 'draw', 'year', 'twh'] + [f'{e}_kg_{f}' for e in elements
                                                        for f in ('in', 'stock', 'out', 'collected')]
        with open(path, 'w', encoding='utf-8') as handle:
            handle.write(','.join(header) + '\n')
            for s, name in enumerate(T.SCENARIOS):
                for d in range(4):
                    for year in range(2022, 2041):
                        if (name, d, year) in rows_left_out:
                            continue
                        values = [f'{(s + 1) * 100 + d * 10 + (year - 2022) + k / 10:g}'
                                  for k in range(len(elements) * 4)]
                        line = ','.join([name, str(d), str(year), '1.5'] + values) + '\n'
                        handle.write(line)
                        if row_twice == (name, d, year):
                            handle.write(line)

    def test_every_number_copied(self):
        with tempfile.TemporaryDirectory() as folder:
            source = os.path.join(folder, 'stock_flow_draws.csv')
            self.write_csv(source)
            path = T.copy(source, os.path.join(folder, 'copy'))
            draws = np.load(path)
            self.assertEqual(draws.shape, (3, 4, 16, 3, 2))
            # Scenario B (1), draw 2, 2030 (year 8 of the copy, 2030 - 2022 = 8 of the file), Al (element 1), out
            # (flow 2): its column k = 1 × 4 + 2 = 6 of the file's element columns.
            self.assertAlmostEqual(float(draws[1, 2, 2030 - 2025, 2, 1]), 2 * 100 + 2 * 10 + 8 + 0.6, places=3)
            self.assertAlmostEqual(float(draws[0, 0, 0, 0, 0]), 100 + 3 + 0.0, places=3)   # A, 0, 2025, in, Cu
            with open(os.path.join(folder, 'copy', T.ELEMENTS_FILE), encoding='utf-8') as handle:
                self.assertEqual(handle.read().split(), ['Cu', 'Al'])
            with open(os.path.join(folder, 'copy', T.SOURCE_FILE), encoding='utf-8') as handle:
                words = handle.read()
            self.assertIn(f'source: {source}', words)
            self.assertIn('draws: 4', words)
            self.assertIn('years: 2025 to 2040', words)

    def test_a_missing_or_doubled_row_stops_it(self):
        for kwargs in ({'rows_left_out': {('C', 3, 2031)}}, {'row_twice': ('A', 1, 2026)}):
            with tempfile.TemporaryDirectory() as folder:
                source = os.path.join(folder, 'stock_flow_draws.csv')
                self.write_csv(source, **kwargs)
                with self.assertRaises(ValueError, msg=kwargs):
                    T.copy(source, os.path.join(folder, 'copy'))
                self.assertFalse(os.path.exists(os.path.join(folder, 'copy', T.SOURCE_FILE)))
        # A row before 2025 left out does not matter: only 2025 to 2040 is copied.
        with tempfile.TemporaryDirectory() as folder:
            source = os.path.join(folder, 'stock_flow_draws.csv')
            self.write_csv(source, rows_left_out={('B', 0, 2023)})
            self.assertTrue(os.path.exists(T.copy(source, os.path.join(folder, 'copy'))))


class TestTheCombination(unittest.TestCase):
    """05 on made-up draws: every kilogram by hand, draw i with draw i; the summary; the pages."""

    @classmethod
    def setUpClass(cls):
        from matplotlib.figure import Figure
        from unittest import mock
        from test_comparison import page_problems
        cls.folder = tempfile.TemporaryDirectory()
        cls.params = settings(cls.folder.name)
        write_inputs(cls.params)
        cls.saved, cls.problems, cls.legends = [], [], {}
        save = Figure.savefig

        def checked(figure, path, *args, **kwargs):
            name = os.path.relpath(str(path), cls.params.output.combined_figures_dir)
            cls.saved.append(name)
            cls.problems += page_problems(figure, os.path.basename(name), kwargs.get('dpi'))
            cls.legends[name] = [t.get_text() for legend in figure.legends for t in legend.get_texts()]
            save(figure, path, *args, **kwargs)

        out = StringIO()
        with mock.patch.object(Figure, 'savefig', checked), redirect_stdout(out):
            cls.code = C.run(cls.params)
        cls.printed = out.getvalue()

    @classmethod
    def tearDownClass(cls):
        cls.folder.cleanup()

    def test_it_runs(self):
        self.assertEqual(self.code, 0, self.printed)

    def test_every_kg_by_hand(self):
        elements = C.composition.element_order(set(ROBOT_ELEMENTS) | set(CENTRE_ELEMENTS))
        for s, scenario in enumerate(C.SCENARIOS):
            folder = os.path.join(self.params.output.combined_dir, scenario)
            with open(os.path.join(folder, 'elements.txt'), encoding='utf-8') as handle:
                self.assertEqual(handle.read().split(), elements)
            for f, name in enumerate(C.flow.ELEMENT_FILES):
                together = np.load(os.path.join(folder, f'{name}.npy')).astype(np.float64)
                self.assertEqual(together.shape, (N, YEARS, len(elements)))
                for k, symbol in enumerate(elements):
                    expected = np.zeros((N, YEARS))
                    for d in range(N):
                        for y in range(YEARS):
                            if symbol in CENTRE_ELEMENTS:
                                expected[d, y] += centre_value(s, d, y, f, CENTRE_ELEMENTS.index(symbol))
                            if symbol in ROBOT_ELEMENTS:
                                expected[d, y] += (f + 1) * sum(robot_value(d, y, p, ROBOT_ELEMENTS.index(symbol))
                                                                for p in range(len(C.flow.PARTS)))
                    np.testing.assert_allclose(together[:, :, k], expected, rtol=1e-6,
                                               err_msg=(scenario, name, symbol))

    def test_its_summary(self):
        import csv
        with open(os.path.join(self.params.output.combined_dir, C.SUMMARY), newline='', encoding='utf-8') as handle:
            rows = list(csv.DictReader(handle))
        # Scenario B, copper, together, stock, 2030: the mean, 2.5 % and 97.5 % of the draws by hand.
        values = np.array([centre_value(1, d, 5, 1, 0) + 2 * sum(robot_value(d, 5, p, 2)
                                                                 for p in range(len(C.flow.PARTS)))
                           for d in range(N)])
        row = next(r for r in rows if r['scenario'] == 'B' and r['element'] == 'Copper' and r['source'] == 'together'
                   and r['flow'] == 'stock' and r['year'] == '2030')
        self.assertAlmostEqual(float(row['mean']) / values.mean(), 1, places=5)
        low, high = np.percentile(values, (2.5, 97.5))
        self.assertAlmostEqual(float(row['2.5 %']) / low, 1, places=5)
        self.assertAlmostEqual(float(row['97.5 %']) / high, 1, places=5)
        # Strontium the data centres' alone; lithium the robots' alone; neodymium in no draw: '–', held 0.
        sr = next(r for r in rows if r['element'] == 'Strontium' and r['source'] == C.ROBOTS and r['flow'] == 'in')
        self.assertEqual((sr['mean'], sr['held in % of the draws']), ('–', '0.0'))
        li = next(r for r in rows if r['element'] == 'Lithium' and r['source'] == C.DATA_CENTRES and r['flow'] == 'in')
        self.assertEqual(li['mean'], '–')
        nd = [r for r in rows if r['element'] == 'Neodymium']
        self.assertTrue(nd and all(r['mean'] == '–' for r in nd))

    def test_its_pages(self):
        held = ['Lithium', 'Aluminium', 'Copper', 'Strontium']
        expected = sorted([os.path.join(s, C.ELEMENTS_DIR, f'{e}.png') for s in C.SCENARIOS for e in held]
                          + [os.path.join(s, C.DISTRIBUTIONS_DIR, f'elements_{y}.png') for s in C.SCENARIOS
                             for y in (2025, 2030, 2035, 2040)])
        self.assertEqual(sorted(self.saved), expected)
        self.assertEqual(self.problems, [])
        self.assertIn('Neodymium: no numbers, 0 kg in every draw; no page.', self.printed)
        self.assertEqual(self.legends[os.path.join('B', C.DISTRIBUTIONS_DIR, 'elements_2040.png')],
                         [C.DATA_CENTRES, C.ROBOTS])


class TestItsChecks(unittest.TestCase):
    """05 stops, writing nothing, where the two models' draws do not belong together: each a deliberate fault."""

    def run_on(self, **kwargs) -> tuple:
        with tempfile.TemporaryDirectory() as folder:
            params = settings(folder)
            write_inputs(params, **kwargs)
            out = StringIO()
            with redirect_stdout(out):
                code = C.run(params)
            return code, out.getvalue(), os.path.exists(params.output.combined_dir)

    def test_other_numbers_of_draws_or_years(self):
        for kwargs, words in (({'draws': N + 1}, 'do not pair draw by draw'), ({'years': YEARS - 1}, 'the years')):
            code, printed, written = self.run_on(**kwargs)
            self.assertEqual(code, 1, printed)
            self.assertIn('05 stopped', printed)
            self.assertIn(words, printed)
            self.assertFalse(written)

    def test_no_copy_of_07(self):
        with tempfile.TemporaryDirectory() as folder:
            params = settings(folder)
            out = StringIO()
            with redirect_stdout(out):
                self.assertEqual(C.run(params), 1)
            self.assertIn('tools/copy_data_center_draws.py', out.getvalue())


if __name__ == '__main__':
    unittest.main()
