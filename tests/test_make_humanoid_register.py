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
parts_builder = load('make_parts_taken_apart', os.path.join('tools', 'make_parts_taken_apart.py'))
# The robots of the parts file, as its builder writes them: the names the register's "Taken apart as" must use.
APART = [row[0] for row in parts_builder.ROBOTS_ROWS]
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
        self.assertEqual([f.text for f in schemas.check_register(self.register, Params(), APART)], [])

    def test_every_robot_once_as_decided(self):
        # EVIDENCE.md E4.9 to E4.11 and V60: 349 entries of the catalogue and 5 added; 10 second entries of one robot;
        # 18 not assigned, the FF Nova below 15 kg (decided 2026-10-28) and the TRON 2, sold in no form with legs and
        # arms (E5.17, agreed 2026-10-29); 324 robots with a type, 137 with two.
        self.assertEqual([r.number for r in self.register], list(range(1, 355)))
        typed = [r for r in self.register if r.types]
        self.assertEqual(len(typed), 324)
        self.assertEqual(sum(len(r.types) == 2 for r in typed), 137)
        self.assertEqual(sum(r.entry.startswith(schemas.SAME_ROBOT) for r in self.register), 10)
        self.assertEqual(sum(r.entry.startswith(schemas.NOT_ASSIGNED) for r in self.register), 20)
        tron = next(r for r in self.register if r.number == 309)
        self.assertEqual(tron.entry, 'not assigned: no form with legs and arms')

    def test_the_robots_in_each_type(self):
        # V60's recount with the five added (1: 33 ...), less the FF Nova and the TRON 2, which leave type 1.
        counts = {t: sum(t in r.types for r in self.register) for t in range(1, 7)}
        self.assertEqual(counts, {1: 31, 2: 97, 3: 181, 4: 135, 5: 12, 6: 5})

    def test_every_robot_of_type_1_has_its_own_rows_in_the_parts_file(self):
        # Matthias, 2026-10-29: "Yes, build it" (the entry, point 2): every robot of type 1 its own rows; the K1 in its
        # two versions, each drawn as often (point 3).
        apart = {r.number: r.taken_apart for r in self.register if r.taken_apart}
        self.assertEqual(set(apart), {r.number for r in self.register if 1 in r.types})
        self.assertEqual(apart[102], 'Unitree G1')
        self.assertEqual(apart[148], 'Booster K1 5 Ah; Booster K1 2 Ah')
        names = [n for v in apart.values() for n in v.split('; ')]
        self.assertEqual(len(names), len(set(names)))
        for name in names:
            self.assertFalse(set('(),') & set(name), msg=name)   # 04 reads the names between brackets, by commas

    def test_masses_as_stated(self):
        by_number = {r.number: r for r in self.register}
        self.assertEqual(by_number[102].mass, (34, 35, 36))          # G1: "35", +- 1 kg
        self.assertEqual(by_number[246].mass, (20, 25, 30))          # QUESTER1: "~20–30", the range
        self.assertEqual(by_number[325].mass, (72, 73, 74))          # Walker S2: "43, 73", the larger
        self.assertEqual(by_number[236].mass, (9.75, 19.5, 29.25))   # PrimeBOT Q1: none stated, E5.17 point 6

    def test_the_sheet_type_1_lists_every_robot_of_type_1_as_in_the_sheet_robots(self):
        # Matthias, 2026-10-29: "There has to be an excel sheet where all the robots of the different types are fully
        # listed. For now it has to be just all for type 1." Every robot whose types include 1, leading or second, in
        # the order of the register, every cell as in the sheet Robots, and 01's check of it finds nothing.
        listed = schemas.read_type_sheet(self.path, 1)
        self.assertEqual([r.number for r in listed], [r.number for r in self.register if 1 in r.types])
        self.assertEqual(len(listed), 31)
        self.assertIn(54, [r.number for r in listed])    # the Booster T1, 1.18 m: kept in type 1 (2026-10-29)
        self.assertIn(236, [r.number for r in listed])   # the PrimeBOT Q1, its mass an estimate (E5.17)
        self.assertEqual([f.text for f in schemas.check_type_sheet(self.register, listed, 1, Params())], [])

    def test_the_sheet_type_2_lists_every_robot_of_type_2_drawn_from_the_workbook_for_now(self):
        # Matthias, 2026-10-29, "Yes, as proposed" (type 2 as type 1, step 5: its robots all listed): every robot whose
        # types include 2, leading or second; none of them taken apart yet, so 02 draws type 2 from the workbook, and
        # the sheet says so of each.
        listed = schemas.read_type_sheet(self.path, 2)
        self.assertEqual([r.number for r in listed], [r.number for r in self.register if 2 in r.types])
        self.assertEqual(len(listed), 97)
        self.assertEqual({r.in_run for r in listed}, {schemas.IN_RUN_WORKBOOK})
        self.assertEqual([f.text for f in schemas.check_type_sheet(self.register, listed, 2, Params())], [])

    def test_the_sheet_type_1_says_what_the_run_does_with_each_robot(self):
        listed = {r.number: r.in_run for r in schemas.read_type_sheet(self.path, 1)}
        self.assertEqual(set(listed.values()), {'drawn: its own parts'})

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
