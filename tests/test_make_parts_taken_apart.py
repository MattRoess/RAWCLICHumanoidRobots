"""
Tests of tools/make_parts_taken_apart.py, the builder of data/researched/parts_taken_apart.xlsx.

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

Matthias, 2026-10-27: "Yes, put the builder in tools/make_parts_taken_apart.py as proposed, with its test and
documents." The builder is the master of the data file: what it writes must pass every check 01 makes of the file,
and, while nobody has changed it, equal the file on disk cell by cell. Everything is written into temporary folders:
press Run, nothing in the project is changed.
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
builder = load('make_parts_taken_apart', os.path.join('tools', 'make_parts_taken_apart.py'))
from src.params_schema import Params, absolute  # noqa: E402


class TestMakePartsTakenApart(unittest.TestCase):
    """What the builder writes holds together as 01 checks it, and equals the data file on disk."""

    def test_what_it_writes_passes_every_check_of_01(self):
        params = Params()
        lists_path, workbook_path = absolute(params.data.shared_lists), absolute(params.data.workbook)
        if not all(os.path.exists(p) for p in (lists_path, workbook_path)):
            self.skipTest('the shared lists or the workbook are not on disk')
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, 'parts_taken_apart.xlsx')
            builder.build(path)
            apart = schemas.read_parts_taken_apart(path)
        lists = schemas.read_shared_lists(lists_path)
        book = schemas.read_workbook(workbook_path, params)
        faults = (schemas.check_parts_taken_apart(apart, lists, params) + schemas.check_sibling_data(apart, params)
                  + schemas.check_robot_types(apart, book.categories))
        self.assertEqual([f.text for f in faults], [])
        self.assertEqual(sorted(apart.robots), ['AgiBot X1', 'Fourier N1', 'Unitree G1'])

    def test_what_it_writes_equals_the_data_file_on_disk(self):
        on_disk = absolute(Params().data.parts_taken_apart)
        if not os.path.exists(on_disk):
            self.skipTest('the data file is not on disk')
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, 'parts_taken_apart.xlsx')
            builder.build(path)
            written, present = load_workbook(path), load_workbook(on_disk)
            self.assertEqual(written.sheetnames, present.sheetnames)
            for name in written.sheetnames:
                rows = [list(r) for r in written[name].iter_rows(values_only=True)]
                self.assertEqual(rows, [list(r) for r in present[name].iter_rows(values_only=True)], msg=name)

    def test_every_battery_pack_holds_its_heaviest_cells_and_board(self):
        """Matthias, 2026-10-28, "Cut at the cells": a pack's lower bound holds its heaviest cells (its largest energy
        over the NMC cells' lowest energy per kg, 00's composition.nmc_wh_per_kg_min) and its largest management board,
        in the lightest robot of type 1 (where pack and cells shrink with the mass and the board does not), so that the
        battery housing, the pack's remainder, never falls below zero. The X1's 1.75 kg and the N1's 2.26 kg."""
        params = Params()
        workbook = absolute(params.data.workbook)
        if not os.path.exists(workbook):
            self.skipTest('the workbook is not on disk')
        (_, _), (lightest, _) = schemas.type_limits(next(c for c in schemas.read_workbook(workbook, params).categories
                                                         if c.number == 1))
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, 'parts_taken_apart.xlsx')
            builder.build(path)
            apart = schemas.read_parts_taken_apart(path)
        g_per_cm2 = apart.constants[schemas.ALL_ROBOTS]['Board mass per cm2 (boards not weighed)'][1][2]
        for robot in apart.robots:
            constants = apart.constants[robot]
            wh = constants['Battery voltage'][1][2] * constants['Battery capacity'][1][2]
            cells = wh / params.composition.nmc_wh_per_kg_min
            board = max(b.bounds[2] * b.count for b in apart.boards if b.robot == robot and b.kind == 'Battery pack')
            factor = lightest / constants['Robot mass, with battery'][1][2]
            needed = cells + board * g_per_cm2 / 1000 / factor
            pack = next(p for p in apart.parts if p.robot == robot and p.name == 'Battery pack')
            with self.subTest(robot=robot):
                self.assertGreaterEqual(pack.bounds[0], needed - 1e-9)
        packs = {p.robot: p.bounds for p in apart.parts if p.name == 'Battery pack'}
        self.assertEqual((packs['AgiBot X1'], packs['Fourier N1']), ((1.75, 2.2, 3.3), (2.26, 2.9, 3.2)))

    def test_it_takes_no_arguments_and_writes_where_00_says(self):
        self.assertEqual(builder.output_path(), absolute(Params().data.parts_taken_apart))

    def test_it_carries_the_masses_and_parts_decided_on_2026_10_28(self):
        """Matthias, 2026-10-28, on the X1's and N1's masses and the G1's parts not carried over: "X1 max 35.3 kg",
        "Encoders", "XT30 connectors", "Main board cooler", then "Yes, build" (EVIDENCE.md E2.8e). Every robot has two
        encoders and two XT30 connectors per joint, and a main board fan and heat sink of its own."""
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, 'parts_taken_apart.xlsx')
            builder.build(path)
            apart = schemas.read_parts_taken_apart(path)
        # The X1's mass reaches up to its model file's 35.32 kg (X1c); the G1's and N1's stay as they were.
        masses = {robot: given['Robot mass, with battery'][1] for robot, given in apart.constants.items()
                  if robot != schemas.ALL_ROBOTS}
        self.assertEqual(masses, {'Unitree G1': (34, 35, 36), 'AgiBot X1': (32, 33, 35.3),
                                  'Fourier N1': (38, 39, 40)})
        for robot in apart.robots:
            parts = {p.name: p for p in apart.parts if p.robot == robot}
            sensors = {p.name: p for p in apart.sensors if p.robot == robot}
            joints = sum(j.count for j in apart.joints if j.robot == robot)
            with self.subTest(robot=robot):
                # Two encoders per joint, in the sheet Parts (their mass inside the joints) and in the sheet Sensors
                # (their elements).
                self.assertEqual(parts['Encoders (two per joint)'].count, 2 * joints)
                self.assertEqual(sensors['Encoder'].count, 2 * joints)
                # Two XT30 connectors per joint, each of the G1's mass.
                xt30 = parts['XT30 (2+2) connectors (two per joint)']
                self.assertEqual(xt30.count, 2 * joints)
                self.assertEqual(xt30.bounds, (0.0015, 0.003, 0.0045))
                # The main board's fan, as the G1's.
                self.assertEqual(parts['Main board fan'].bounds, (0.005, 0.01, 0.02))
        # The X1's and N1's main board heat sink: copper heat pipes and fins (E; the G1's is its aluminium one).
        for robot in ('AgiBot X1', 'Fourier N1'):
            sink = {p.name: p for p in apart.parts if p.robot == robot}['Main board heat sink: heat pipes and fins']
            self.assertEqual((sink.bounds, sink.material, sink.label), ((0.055, 0.12, 0.19), 'Copper', 'E'))


if __name__ == '__main__':
    unittest.main()
