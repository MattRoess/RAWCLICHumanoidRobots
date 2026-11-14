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
2. 02's own check before a run (memory_needed, run_memory): the run at the settings' draws in half the memory.
3. The stages 02, 03 and 04, each in a process of its own at 5,000, 10,000 and 20,000 runs on his real inputs (its
   outputs in a temporary folder), their peak memory measured by the system (02: its own process and the largest process of a robot
   type, which it says); extrapolated on the safe side, the rule of 2026-11-14 (Matthias: "For MC you want currently
   to test with up to 50 000 runs. I do NOT want this. 20 000 is enough. But you have to choose a conservative
   approach, which means have enough safety margins."): along the straight line through the two largest measurements
   to the settings' draws, raised by half (MARGIN), in half the computer's memory; and 02's check never below what is
   measured. Slow (some ten minutes): it runs the stages.

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
# The growing numbers of runs each stage is measured at (test 3), 20,000 at most (Matthias, 2026-11-14: "20 000 is
# enough"); the straight line through the two largest; and the safety margin on the extrapolated peak ("enough safety
# margins": the GitHub folder's CLAUDE.md §4, "raised by half (× 1.5)").
SIZES = (5000, 10000, 20000)
LOW, HIGH = SIZES[-2:]
MARGIN = 1.5
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


def peak_bytes(folder: str, runs: int, stage: str) -> tuple:
    """(the peak memory of `stage` run at `runs` draws, bytes; for 02 its peak while drawing, else the same; the
    estimate of 02's own check or None), as the system measures it (/usr/bin/time -l: the peak memory footprint of the
    stage's process), and for 02 the largest process of a robot type added, which 02 says ("The largest process of a
    robot type held at most ... GB, while drawing at most ... GB"): the two run at the same time. The peak while
    drawing grows with the draws faster than the peak of the pages, and takes over at more draws (VERIFICATION V237).
    Raises AssertionError where the stage stopped."""
    run = subprocess.run(['/usr/bin/time', '-l', sys.executable, '-c', RUNNER.format(root=ROOT), folder, str(runs),
                          stage], capture_output=True, text=True, env={**os.environ, 'MPLBACKEND': 'Agg'})
    if run.returncode != 0:
        raise AssertionError(f'{stage} at {runs:,} runs stopped: {run.stderr[-1500:]}')
    peak = float(re.search(r'(\d+)\s+peak memory footprint', run.stderr).group(1))
    largest = re.search(r'The largest process of a robot type held at most ([\d.]+) GB, while drawing at most '
                        r'([\d.]+) GB', run.stdout)
    check = re.search(r'the run at most about ([\d.]+) GB', run.stdout)
    if largest:
        return (peak + float(largest.group(1)) * 1e9, peak + float(largest.group(2)) * 1e9,
                float(check.group(1)) * 1e9)
    return peak, peak, None


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
        total = composition.run_memory(dict(enumerate(needs)))
        self.assertLessEqual(total, LIMIT, msg=f'{total / 1e9:.1f} GB at {params.composition.draws:,} draws')


class TestEveryStageFits(unittest.TestCase):
    """3. Every stage at the settings' draws, extrapolated from its measured peak at LOW and HIGH runs along the straight
    line and raised by MARGIN, in half this computer's memory; 02's check not below its measured peak."""

    @classmethod
    def setUpClass(cls):
        if not os.path.exists('/usr/bin/time'):
            raise unittest.SkipTest('/usr/bin/time is not on this computer')
        cls.folders = {runs: tempfile.mkdtemp(prefix=f'memory_{runs}_') for runs in SIZES}
        cls.peaks, cls.drawing, cls.checks = {}, {}, {}
        for stage in STAGES:                 # in order: each stage reads what the stages before it wrote
            for runs, folder in cls.folders.items():
                cls.peaks[(stage, runs)], cls.drawing[(stage, runs)], cls.checks[(stage, runs)] = \
                    peak_bytes(folder, runs, stage)

    @classmethod
    def tearDownClass(cls):
        for folder in getattr(cls, 'folders', {}).values():
            shutil.rmtree(folder, ignore_errors=True)

    def test_each_stage_at_the_settings_draws(self):
        draws = current().composition.draws
        for stage in STAGES:
            def line(peaks: dict) -> float:
                """The straight line through the two largest measurements, at the settings' draws, never falling."""
                low, high = peaks[(stage, LOW)], peaks[(stage, HIGH)]
                return high + max(high - low, 0.0) / (HIGH - LOW) * (draws - HIGH)
            at_draws = MARGIN * max(line(self.peaks), line(self.drawing))   # the larger: the pages' or the drawing's
            measured = ', '.join(f'{self.peaks[(stage, runs)] / 1e9:.2f} GB at {runs:,}' for runs in SIZES)
            if stage == '02_composition':
                measured += ' (while drawing ' + ', '.join(f'{self.drawing[(stage, runs)] / 1e9:.2f}' for runs in SIZES) + ')'

            print(f'  {stage}: {measured} runs; about {at_draws / 1e9:.1f} GB at {draws:,} with the margin (half the '
                  f'memory: {LIMIT / 1e9:.1f} GB)', flush=True)
            self.assertLessEqual(at_draws, LIMIT, msg=stage)
            for runs in SIZES:
                if self.checks[(stage, runs)] is not None:      # 02's check: never below what the run holds
                    self.assertGreaterEqual(self.checks[(stage, runs)], self.peaks[(stage, runs)], msg=(stage, runs))


if __name__ == '__main__':
    unittest.main()
