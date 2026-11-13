"""
test_all_figures.py -- every figure of every stage, checked against every rule of the shared figure tests (FigureTests,
installed as the package figure_tests, pinned in requirements.txt).

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

Matthias, 2026-11-13: "There is now the package for figure testing. I want that you intergate the new results with the
robots and als test all the figures", "Yes, 1 to 7" (step 1: install the package pinned and one test file of this
project, built like RAWCLICDataCenters' tests/test_all_figures.py). The rules are those of the data-centre pages
(FigureTests' README; Matthias, 2026-11-12: "yes, 1 to 11"), and this project's figures follow the data-centre pages
(his rule "Robots exactly as the data centres").

What is tested, and why:
  TestEachRuleCatchesItsFault  imported from figure_tests.proofs: every rule on a figure drawn with its fault (it must be
                               caught) and on the same figure without it (it must pass), with the version installed here.
  TestTheInstalledVersion      the version installed is the one requirements.txt pins (a rule added or changed in
                               FigureTests reaches this project only with its pin raised, and then is checked here).
  TestEveryFigureOfEveryStage  every numbered stage from 01 on (figure_tests.numbered_stages: found by its file name, so a
                               new stage is included without a change here; 00 the settings draws no figure) run as by
                               pressing Run, its own main() (figure_tests.run_main), in order, on Matthias's workbooks
                               with FEW_RUNS runs of each robot type, every output folder of the settings moved into a
                               temporary folder (sandbox_settings, this project's own part). 05 reads the first FEW_RUNS
                               runs of this project's copy of the data centres' runs (data/raw/, written by
                               tools/copy_data_center_draws.py), copied into the temporary folder. Every figure is checked
                               against every rule at the moment it is saved (figure_tests.FigureCheck), with this
                               project's SETTINGS. One test per stage: it ran, it saved figures, none breaks a rule. And
                               one test that nothing was written into the repository's data/ or figures/.

A fault Matthias finds in a figure that no rule catches becomes a new rule in FigureTests the same day, with its proof
there first; then FigureTests' version, this project's pin, and its documents are updated (FigureTests' README, "When a
rule is added or changed").

Press Run on this file. The proofs draw their own small figures. The stages read his workbooks and write only into a
temporary folder. The figures of the last run stay in that folder (its path is printed) so that they can be opened.
"""

import os
import re
import shutil
import sys
import tempfile
import time
import unittest
from dataclasses import fields, replace
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import figure_tests as ft  # noqa: E402
from figure_tests.proofs import TestEachRuleCatchesItsFault  # noqa: E402,F401  (the proofs run here too)

import src.params_schema as ps  # noqa: E402

FEW_RUNS = 200          # runs of each robot type in the sandbox: enough for every kind of panel, minutes in all

# The copy of the data centres' runs that 05 reads (tools/copy_data_center_draws.py writes it; not in git)
COPY_FILES = ("element_draws.npy", "elements.txt", "source.txt")

def proper_names() -> tuple:
    """The names Matthias's register and workbook write together, robots and makers (AgiBot, CyberOne, TianGong ...):
    proper names, not code names (FigureTests' rule words), read from his files each time so that a robot added to the
    register needs no change here; a file name (with a full stop) is not a name."""
    import openpyxl
    real = ps.current()
    code = re.compile(r"[a-z]{2,}[A-Z][a-z]|[A-Z]{2,}[A-Z][a-z]{2,}|[0-9][A-Z][a-z]{2,}")   # FigureTests' CODE_NAME
    names = set()
    for path in (real.data.register, real.data.workbook):
        book = openpyxl.load_workbook(ps.absolute(path), read_only=True, data_only=True)
        for sheet in book.worksheets:
            for row in sheet.iter_rows(values_only=True):
                for cell in row:
                    if isinstance(cell, str):
                        names |= {w for w in re.findall(r"[\w\-]+", cell) if code.search(w)}
        book.close()
    return tuple(sorted(names, key=len, reverse=True))          # the longest first: 'RealBot-L2' before 'RealBot'


# What is particular to this project's figures (figure_tests.Settings):
#   proper_names    the names of the robots and their makers written together (proper_names, from his register)
#   schema_folders  01 saves its schema pages in figures/schemas/: they may name the stages, sheets and settings
#   extra_words     the jargon of the data-centre pages, which this project's pages follow (Matthias, 2026-11-10:
#                   "NOBODY can understand it"): inflow, outflow; "Plan A" (the ai-2040 article's name of its scenario:
#                   not a scientist's word, rule 2 of 2026-11-12)
#   text_pages      the notes pages of 02 and 03 ("how to read its pages", <...>_notes_<k>.png): pages of text, with no
#                   foot of three sentences to keep, and "average" may name an input there, as his workbook does
#                   (Matthias, 2026-11-13: "Yes, both"); every other rule holds on them
SETTINGS = ft.Settings(proper_names=proper_names(), schema_folders=("schemas",),
                       extra_words=(r"\binflows?\b", r"\boutflows?\b", r"\bPlan A\b"),
                       text_pages=(r"_notes_\d+\.png$",))


class TestTheInstalledVersion(unittest.TestCase):

    def test_the_version_installed_is_the_one_pinned(self):
        text = (ROOT / "requirements.txt").read_text(encoding="utf-8")
        pinned = re.search(r"^figure-tests @ git\+\S+@v(\S+)$", text, flags=re.MULTILINE)
        self.assertIsNotNone(pinned, "requirements.txt pins no version of figure-tests")
        self.assertEqual(ft.__version__, pinned.group(1),
                         "the figure tests installed are not the version requirements.txt pins: install the pinned one")


def few_runs_of_the_copy(real, folder: Path) -> str:
    """The first FEW_RUNS runs of this project's copy of the data centres' runs (data/raw/, its element_draws.npy:
    scenario × run × year × flow × element), with its elements.txt and source.txt, into folder/data_center_draws, so that
    05 pairs run i with run i of the sandbox's FEW_RUNS runs of 04. Returns the folder; where the copy is not here, the
    folder stays empty and 05 stops, saying to run the copy tool."""
    source, target = Path(ps.absolute(real.data.data_center_draws_dir)), folder / "data_center_draws"
    target.mkdir(parents=True, exist_ok=True)
    if all((source / name).is_file() for name in COPY_FILES):
        runs = np.load(source / COPY_FILES[0], mmap_mode="r")
        np.save(target / COPY_FILES[0], np.ascontiguousarray(runs[:, :FEW_RUNS]))
        for name in COPY_FILES[1:]:
            shutil.copy2(source / name, target / name)
    return str(target)


def sandbox_settings(real, folder: Path):
    """The settings of src/params_schema.py with every output folder moved into `folder` (a setting ending in _dir), few
    runs of each robot type, and 05's copy of the data centres' runs cut to the same few runs. The inputs are his."""
    moved = {f.name: str(folder / getattr(real.output, f.name)) for f in fields(real.output) if f.name.endswith("_dir")}
    return replace(real, output=replace(real.output, **moved),
                   composition=replace(real.composition, draws=FEW_RUNS),
                   data=replace(real.data, data_center_draws_dir=few_runs_of_the_copy(real, folder)))


class TestEveryFigureOfEveryStage(unittest.TestCase):
    """Runs once for the class; one test per stage reads what its run found."""

    ran = {}            # stage file name -> None, or the error it stopped with
    check = None        # the FigureCheck: figures and faults per stage
    folder = None

    @classmethod
    def setUpClass(cls):
        real = ps.current()
        cls.folder = Path(tempfile.mkdtemp(prefix="all_figures_"))
        cls.before = {name: ft.files_and_times(ROOT / name) for name in ("data", "figures")}
        settings = sandbox_settings(real, cls.folder)
        original_current = ps.current
        ps.current = lambda: settings                    # each stage reads its settings anew when it is loaded
        try:
            with ft.FigureCheck(SETTINGS, root=cls.folder) as cls.check:
                for path in ft.numbered_stages(ROOT):
                    cls.check.stage(path.name)
                    start = time.perf_counter()
                    cls.ran[path.name] = ft.run_main(path, f"all_figures_{path.stem}")
                    plt.close("all")
                    print(f"{path.name}: {time.perf_counter() - start:.0f} s, {len(cls.check.figures[path.name])} "
                          f"figures, {len(cls.check.faults[path.name])} faults", flush=True)
        finally:
            ps.current = original_current
        cls.after = {name: ft.files_and_times(ROOT / name) for name in ("data", "figures")}
        print(f"The figures of this run: {cls.folder}", flush=True)

    def test_nothing_written_into_the_repository(self):
        """The sandbox wrote nothing into the repository's data/ or figures/ (his runs' folders)."""
        self.assertEqual(self.before, self.after)

    def test_every_stage_was_run(self):
        """Every numbered stage from 01 on is in the run (a new stage is found without a change here)."""
        self.assertEqual(sorted(self.ran), [p.name for p in ft.numbered_stages(ROOT)])


def _stage_test(name):
    def test(self):
        self.assertIsNone(self.ran.get(name), f"{name} stopped:\n{self.ran.get(name)}")
        self.assertTrue(self.check.figures.get(name), f"{name} saved no figure")
        faults = self.check.faults.get(name, [])
        self.assertEqual(faults, [], f"{len(faults)} faults in the figures of {name}:\n{ft.fault_report(faults)}")
    test.__doc__ = f"{name}: it ran, it saved figures, and none breaks a rule of the figure tests."
    return test


for _path in ft.numbered_stages(ROOT):
    setattr(TestEveryFigureOfEveryStage, f"test_{_path.stem}", _stage_test(_path.name))


if __name__ == "__main__":
    unittest.main()
