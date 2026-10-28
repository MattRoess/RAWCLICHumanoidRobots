"""
Tests of tools/make_humanoid_register.py, the builder of data/researched/humanoid_register.xlsx.

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

Matthias, 2026-10-28: "Yes, code it in 02", on the plan whose first step is the register as a data file built in
tools/ with its test. The builder is the master of the register: what it writes must pass every check 01 makes of it,
hold the decisions of EVIDENCE.md E4 to E4.11 as counted there (VERIFICATION.md V60), and, while nobody has changed it,
equal the file on disk cell by cell. Everything is written into temporary folders: press Run, nothing in the project
is changed.
"""
import importlib.util
import os
import sys
import tempfile
import unittest

from openpyxl import load_workbook

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)


def load(name: str, path: str):
    """Import a file of the project whose name starts with a digit or lies outside a package."""
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, path))
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


schemas = load('schemas', '01_schemas.py')
builder = load('make_humanoid_register', os.path.join('tools', 'make_humanoid_register.py'))
from src.params_schema import Params, absolute  # noqa: E402


class TestMakeHumanoidRegister(unittest.TestCase):
    """What the builder writes holds together as 01 checks it, counts as decided, and equals the file on disk."""

    @classmethod
    def setUpClass(cls):
        params = Params()
        if not os.path.exists(absolute(params.data.humanoid_guide)):
            raise unittest.SkipTest('the catalogue is not on disk')
        cls.folder = tempfile.TemporaryDirectory()
        cls.path = os.path.join(cls.folder.name, 'humanoid_register.xlsx')
        builder.build(cls.path, params)
        cls.register = schemas.read_register(cls.path)

    @classmethod
    def tearDownClass(cls):
        cls.folder.cleanup()

    def test_what_it_writes_passes_every_check_of_01(self):
        apart = ['Unitree G1', 'AgiBot X1', 'Fourier N1']
        self.assertEqual([f.text for f in schemas.check_register(self.register, Params(), apart)], [])

    def test_every_robot_once_as_decided(self):
        # EVIDENCE.md E4.9 to E4.11 and V60: 349 entries of the catalogue and 5 added; 10 second entries of one robot;
        # 18 not assigned, and the FF Nova below 15 kg (decided 2026-10-28); 325 robots with a type, 137 with two.
        self.assertEqual([r.number for r in self.register], list(range(1, 355)))
        typed = [r for r in self.register if r.types]
        self.assertEqual(len(typed), 325)
        self.assertEqual(sum(len(r.types) == 2 for r in typed), 137)
        self.assertEqual(sum(r.entry.startswith(schemas.SAME_ROBOT) for r in self.register), 10)
        self.assertEqual(sum(r.entry.startswith(schemas.NOT_ASSIGNED) for r in self.register), 19)

    def test_the_robots_in_each_type(self):
        # V60's recount with the five added (1: 33 ...), less the FF Nova, which leaves type 1.
        counts = {t: sum(t in r.types for r in self.register) for t in range(1, 7)}
        self.assertEqual(counts, {1: 32, 2: 97, 3: 181, 4: 135, 5: 12, 6: 5})

    def test_the_three_robots_taken_apart(self):
        apart = {r.taken_apart: r.number for r in self.register if r.taken_apart}
        self.assertEqual(apart, {'Unitree G1': 102, 'AgiBot X1': 16, 'Fourier N1': 350})

    def test_masses_as_stated(self):
        by_number = {r.number: r for r in self.register}
        self.assertEqual(by_number[102].mass, (34, 35, 36))          # G1: "35", +- 1 kg
        self.assertEqual(by_number[246].mass, (20, 25, 30))          # QUESTER1: "~20–30", the range
        self.assertEqual(by_number[325].mass, (72, 73, 74))          # Walker S2: "43, 73", the larger
        self.assertEqual(by_number[236].mass, (None, None, None))    # PrimeBOT Q1: none stated

    def test_it_writes_where_00_says(self):
        self.assertEqual(builder.output_path(Params()), absolute(Params().data.register))

    def test_what_it_writes_equals_the_register_on_disk(self):
        on_disk = absolute(Params().data.register)
        if not os.path.exists(on_disk):
            self.skipTest('the register is not on disk')
        written, present = load_workbook(self.path), load_workbook(on_disk)
        self.assertEqual(written.sheetnames, present.sheetnames)
        for name in written.sheetnames:
            rows = [list(r) for r in written[name].iter_rows(values_only=True)]
            self.assertEqual(rows, [list(r) for r in present[name].iter_rows(values_only=True)], msg=name)


if __name__ == '__main__':
    unittest.main()
