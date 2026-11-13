"""
tests/test_memory.py
====================
**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

The memory of the stages at the size of the real run. Matthias, 2026-11-13, after his run of 02 held 43 GB on his
16 GB computer, swapped for 48 minutes and wrote nothing: "This is very very bad designe!!!", "Damit it is always MC.
Wrtite done those rules, that you have to test and optimize!!!!", "Fix it damit and this never ever happens again. We
always do Monte Carlo Get this damit.", "It must adopte, so if data are added, it still works!!!" (the rule in the
GitHub folder's CLAUDE.md §4):

1. 02 holds each robot's parts over its own draws only (PartBlocks): their memory grows with the draws, not with the
   number of robots; parts.npy is written from them byte for byte as numpy writes the whole matrix.
2. 02's own check before a run (memory_needed): the run at the settings' draws below MEMORY_SHARE of the memory.
3. The stages 02, 03 and 04, each in a process of its own at 20,000 and 50,000 runs on his real inputs (its outputs in
   a temporary folder), their peak memory measured by the system; extrapolated in a straight line to the settings'
   draws (which overestimates 02: measured 4.6 GB at 100,000 against 6.2 extrapolated), each below the line where the
   computer would begin to swap (MEMORY_SHARE of its memory). Slow (some ten minutes): it runs the stages.

Run: ./.venv/bin/python -m unittest tests.test_memory
"""
import importlib.util
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from src.params_schema import absolute, current  # noqa: E402

_spec = importlib.util.spec_from_file_location('composition', os.path.join(ROOT, '02_composition.py'))
composition = importlib.util.module_from_spec(_spec)
sys.modules['composition'] = composition
_spec.loader.exec_module(composition)

LIMIT = composition.MEMORY_SHARE * os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')   # bytes
# The two numbers of runs each stage is measured at (test 3).
LOW, HIGH = 20000, 50000   # Matthias: "I do not want that you go beyond 50 000 runs"
STAGES = ('02_composition', '03_comparison', '04_stock_and_flow')   # "have it done for 02, 03 and 04"
# A stage run as by pressing Run, its outputs moved into a temporary folder, `runs` draws of each robot type, 05 on the
# first `runs` draws of the data centres' copy (sandbox settings of tests/test_all_figures.py, with its own runs).
RUNNER = '''
import os, sys
from dataclasses import fields, replace
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
sys.path.insert(0, {root!r}); sys.path.insert(0, os.path.join({root!r}, "tests"))
import numpy as np
import figure_tests as ft
import src.params_schema as ps
folder, runs, stage = Path(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
real = ps.current()
moved = {{f.name: str(folder / getattr(real.output, f.name)) for f in fields(real.output) if f.name.endswith("_dir")}}
copy = folder / "data_center_draws"
if not copy.exists():
    copy.mkdir(parents=True)
    source = ps.absolute(real.data.data_center_draws_dir)
    np.save(copy / "element_draws.npy", np.ascontiguousarray(np.load(os.path.join(source, "element_draws.npy"),
                                                                     mmap_mode="r")[:, :runs]))
    for name in ("elements.txt", "source.txt"):
        (copy / name).write_bytes(Path(source, name).read_bytes())
settings = replace(real, output=replace(real.output, **moved), composition=replace(real.composition, draws=runs),
                   data=replace(real.data, data_center_draws_dir=str(copy)))
ps.current = lambda: settings
error = ft.run_main(Path({root!r}) / (stage + ".py"), "memory_" + stage)
sys.exit(0 if error is None else error[-2000:])
'''


def peak_bytes(folder: str, runs: int, stage: str) -> float:
    """The peak memory of `stage` run at `runs` draws in its own process, as the system measures it (/usr/bin/time -l:
    its peak memory footprint). Raises AssertionError where the stage stopped."""
    run = subprocess.run(['/usr/bin/time', '-l', sys.executable, '-c', RUNNER.format(root=ROOT), folder, str(runs),
                          stage], capture_output=True, text=True, env={**os.environ, 'MPLBACKEND': 'Agg'})
    if run.returncode != 0:
        raise AssertionError(f'{stage} at {runs:,} runs stopped: {run.stderr[-1500:]}')
    found = re.search(r'(\d+)\s+peak memory footprint', run.stderr)
    return float(found.group(1))


class TestPartsHeldRobotByRobot(unittest.TestCase):
    """1. The parts of every robot over its own draws only, and parts.npy byte for byte as before."""

    def setUp(self):
        rng = np.random.default_rng(7)
        n, self.columns = 600, ['A: frame', 'A: shell', 'B: frame', 'B: cells', 'B: wires', 'C: frame']
        robot = rng.integers(3, size=n)
        firsts, sizes = (0, 2, 5), (2, 3, 1)
        blocks = []
        for k in range(3):
            rows = np.flatnonzero(robot == k)
            blocks.append((rows, firsts[k], rng.random((rows.size, sizes[k])) * 10 - 1))
        self.n, self.robot, self.blocks = n, robot, blocks
        self.parts = composition.PartBlocks(n, self.columns, blocks)

    def test_only_each_robots_own_draws_are_held(self):
        held = composition.held_bytes(self.parts)
        self.assertEqual(held, sum(rows.nbytes + kg.nbytes for rows, _, kg in self.blocks))   # its draws and kg
        self.assertLess(held, self.n * len(self.columns) * 8 / 2)    # the whole matrix would be N × all columns

    def test_its_matrix_and_its_columns(self):
        dense = self.parts.dense()
        for k, (rows, first, kg) in enumerate(self.blocks):
            others = np.flatnonzero(self.robot != k)
            self.assertTrue(np.array_equal(dense[rows, first:first + kg.shape[1]], kg))
            self.assertFalse(dense[others, first:first + kg.shape[1]].any())     # 0 in every other robot's draws
        for c, name in enumerate(self.columns):
            self.assertTrue(np.array_equal(self.parts.column(name), dense[:, c]))
        self.assertTrue(np.array_equal(self.parts.robot_column('B: wires'), self.blocks[1][2][:, 2]))

    def test_its_file_byte_for_byte_as_numpy_writes_the_matrix(self):
        with tempfile.TemporaryDirectory() as folder:
            mine, numpys = os.path.join(folder, 'parts.npy'), os.path.join(folder, 'whole.npy')
            self.parts.save(mine)
            np.save(numpys, np.asarray(self.parts.dense(), dtype=np.float32))
            with open(mine, 'rb') as a, open(numpys, 'rb') as b:
                self.assertEqual(a.read(), b.read())


class TestTheCheckBeforeARun(unittest.TestCase):
    """2. 02's own check: the run at the settings' draws fits in half this computer's memory."""

    def test_every_robot_type_and_the_run_fit(self):
        params = current()
        paths = [absolute(params.data.register), absolute(params.data.workbook)]
        if not all(os.path.exists(p) for p in paths):
            self.skipTest('the register or the workbook is not on disk')
        inputs = composition.read_inputs(params)
        register = absolute(params.data.register)
        sheets = {n: composition.schemas.read_type_sheet(register, n)
                  for n in composition.schemas.type_sheet_numbers(register)}
        files = composition.read_parts_files(params, inputs)
        needs = []
        for category in inputs.book.categories:
            if category.number in sheets and composition.schemas.drawn_part_by_part(sheets[category.number]):
                a = composition.read_apart_inputs(params, inputs, sheets[category.number], category, files)
                needs.append(composition.memory_needed(a, category, inputs.lists, params))
        self.assertTrue(needs)
        total = (composition.memory_in_use() + sum(kept for _, kept in needs) + max(peak for peak, _ in needs)
                 + composition.PAGES_MEMORY)
        self.assertLessEqual(total, LIMIT, msg=f'{total / 1e9:.1f} GB at {params.composition.draws:,} draws')


class TestEveryStageFits(unittest.TestCase):
    """3. Every stage at the settings' draws, extrapolated from its measured peak at LOW and HIGH runs, in half this
    computer's memory."""

    @classmethod
    def setUpClass(cls):
        if not os.path.exists('/usr/bin/time'):
            raise unittest.SkipTest('/usr/bin/time is not on this computer')
        cls.folders = {runs: tempfile.mkdtemp(prefix=f'memory_{runs}_') for runs in (LOW, HIGH)}
        cls.peaks = {}
        for stage in STAGES:                 # in order: each stage reads what the stages before it wrote
            for runs, folder in cls.folders.items():
                cls.peaks[(stage, runs)] = peak_bytes(folder, runs, stage)

    @classmethod
    def tearDownClass(cls):
        for folder in getattr(cls, 'folders', {}).values():
            shutil.rmtree(folder, ignore_errors=True)

    def test_each_stage_at_the_settings_draws(self):
        draws = current().composition.draws
        for stage in STAGES:
            low, high = self.peaks[(stage, LOW)], self.peaks[(stage, HIGH)]
            at_draws = high + max(high - low, 0.0) / (HIGH - LOW) * (draws - HIGH)
            print(f'  {stage}: {low / 1e9:.2f} GB at {LOW:,} runs, {high / 1e9:.2f} GB at {HIGH:,}, about '
                  f'{at_draws / 1e9:.1f} GB at {draws:,} (the limit: {LIMIT / 1e9:.1f} GB)', flush=True)
            self.assertLessEqual(at_draws, LIMIT, msg=stage)


if __name__ == '__main__':
    unittest.main()
