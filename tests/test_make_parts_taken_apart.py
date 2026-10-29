"""
Tests of tools/make_parts_taken_apart.py, the builder of data/researched/parts_taken_apart.xlsx.

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

Matthias, 2026-10-27: "Yes, put the builder in tools/make_parts_taken_apart.py as proposed, with its test and
documents"; 2026-10-29: "Yes, build it" (every robot of type 1 its own rows). The builder is the master of the data
file: what it writes must pass every check 01 makes of the file, hold every robot of type 1 as agreed (EVIDENCE.md E5),
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


# The robots the register's sheet Type 1 names in its column "Taken apart as", every version once (its builder).
REGISTER = load('make_humanoid_register', os.path.join('tools', 'make_humanoid_register.py'))
TYPE_ONE = [name for names in REGISTER.TAKEN_APART.values() for name in schemas.versions(names)]


def written():
    """What the builder writes, read with 01's reader, from a temporary folder."""
    with tempfile.TemporaryDirectory() as folder:
        path = os.path.join(folder, 'parts_taken_apart.xlsx')
        builder.build(path)
        return schemas.read_parts_taken_apart(path), load_workbook(path)


class TestMakePartsTakenApart(unittest.TestCase):
    """What the builder writes holds together as 01 checks it, holds every robot of type 1 as agreed, and equals the
    data file on disk."""

    @classmethod
    def setUpClass(cls):
        cls.apart, cls.book = written()

    def test_what_it_writes_passes_every_check_of_01(self):
        params = Params()
        lists_path, recipes_path = absolute(params.data.shared_lists), absolute(params.data.element_recipes)
        if not all(os.path.exists(p) for p in (lists_path, recipes_path)):
            self.skipTest('the shared lists or the element recipes are not on disk')
        lists = schemas.read_shared_lists(lists_path)
        recipes = schemas.read_element_recipes(recipes_path)
        faults = (schemas.check_parts_taken_apart(self.apart, lists, params)
                  + schemas.check_sibling_data(self.apart, params)
                  + schemas.check_grades(self.apart, recipes, params))
        self.assertEqual([f.text for f in faults], [])

    def test_every_robot_of_type_1_has_its_own_rows(self):
        # Matthias, 2026-10-29: "Yes, build it" (the entry, point 2: every robot of the sheet Type 1 its own rows;
        # point 3: the K1 in its two versions).
        self.assertEqual(sorted(self.apart.robots), sorted(TYPE_ONE))
        self.assertEqual(len(self.apart.robots), 32)
        self.assertIn('Booster K1 5 Ah', self.apart.robots)
        self.assertIn('Booster K1 2 Ah', self.apart.robots)

    def test_the_k1_in_its_two_versions_differs_in_its_battery_and_computer_only(self):
        # E5.14 point 2: 5 Ah (Education, Professional) or 2 Ah (Geek), each drawn as often.
        five, two = 'Booster K1 5 Ah', 'Booster K1 2 Ah'
        joints = lambda robot: [(j.name, j.count, j.module, j.module_mass) for j in self.apart.joints  # noqa: E731
                                if j.robot == robot]
        self.assertEqual(joints(five), joints(two))
        self.assertEqual(self.apart.constants[five]['Battery capacity'][1], (4.75, 5, 5.25))
        self.assertEqual(self.apart.constants[two]['Battery capacity'][1], (1.9, 2, 2.1))

    def test_the_g1_plus_is_the_g1_with_two_head_joints(self):
        # E5.17 point 5: the G1's own parts as taken apart, and its two head joints as two small joints.
        g1 = [(j.name, j.count, j.module) for j in self.apart.joints if j.robot == 'Unitree G1']
        plus = [(j.name, j.count, j.module) for j in self.apart.joints if j.robot == 'Unitree G1+']
        self.assertEqual(plus, g1 + [('Head (yaw and pitch)', 2, 'small')])
        parts = {p.name: p for p in self.apart.parts if p.robot == 'Unitree G1+'}
        self.assertEqual(parts['Joint module, small'].count, 16)
        self.assertEqual({p.name for p in self.apart.parts if p.robot == 'Unitree G1'}, set(parts))

    def test_the_asimov_2_is_the_asimov_1_scaled_to_38_kg(self):
        # E5.17 point 7: every mass of the Asimov 1 times 38 / 35.
        one = {j.name: j.module_mass for j in self.apart.joints if j.robot == 'Menlo Asimov 1'}
        two = {j.name: j.module_mass for j in self.apart.joints if j.robot == 'Menlo Asimov 2'}
        self.assertEqual(set(one), set(two))
        for name in one:
            for a, b in zip(one[name], two[name]):
                self.assertAlmostEqual(b, a * 38 / 35, places=3, msg=name)
        self.assertEqual(self.apart.constants['Menlo Asimov 2']['Robot mass, with battery'][1], (37, 38, 39))

    def test_the_actuators_of_batch_1_at_their_modes_as_agreed(self):
        # E5.12, agreed 2026-10-29: the actuators' kg at the modes. The RP1's 18.8 kg holds the RMM8463-2E at its
        # agreed mode, 0.7 kg (point 3); E5.12's table gave 19.2 kg with it at its bound, 0.8 kg.
        agreed = {'RoboParty Roboto Origin': 17.6, 'RoboParty RP1': 18.8, 'EngineAI PM01': 15.6,
                  'ROBOTIS AI Sapiens K1': 14.5, 'Menlo Asimov 1': 18.6, 'Booster T1': 14.9, 'Booster K1 5 Ah': 9.2,
                  'Unitree R1': 14.6}
        for robot, kg in agreed.items():
            total = sum(j.count * j.module_mass[1] for j in self.apart.joints if j.robot == robot)
            self.assertAlmostEqual(total, kg, delta=0.05, msg=robot)

    def test_a_robot_without_joint_torques_has_its_joints_as_shares_adding_up_to_1(self):
        # E5.17 point 1: the joint modules a share of the robot's mass, split as batch 1's are on average.
        shared = [r for r in self.apart.robots
                  if any(j.share is not None for j in self.apart.joints if j.robot == r)]
        self.assertEqual(len(shared), 17)
        for robot in shared:
            shares = [j.share for j in self.apart.joints if j.robot == robot]
            self.assertNotIn(None, shares, msg=robot)
            self.assertAlmostEqual(sum(shares), 1, places=12, msg=robot)

    def test_every_steel_and_titanium_part_has_its_grade(self):
        # E5.18, agreed 2026-10-29: each steel part takes the grade of its use.
        grades = {c.name: c.grade for c in self.apart.joint_parts if c.material == 'Steel'}
        self.assertEqual(grades, {'Gear stage 1, sun gear': '20CrMnTi',
                                  'Gear stage 1, planets and carrier with stage 2 sun gear': '20CrMnTi',
                                  'Gear stage 1, ring gear': '20CrMnTi', 'Gear stage 2, ring gear': '20CrMnTi',
                                  'Two small bearings': 'GCr15', 'Output flange': '42CrMo4'})
        for p in self.apart.parts:
            if p.material in ('Steel', 'Titanium'):
                self.assertTrue(p.grade, msg=f'{p.robot}, {p.name}')
        for s in self.apart.shares:
            if s.material in ('Steel', 'Titanium'):
                self.assertTrue(s.grade, msg=s.item)
        stator = {s.material: s.grade for s in self.apart.shares if s.item == 'Motor stator'}
        self.assertEqual(stator['Steel'], 'M19 or M27')

    def test_what_it_writes_equals_the_data_file_on_disk(self):
        on_disk = absolute(Params().data.parts_taken_apart)
        if not os.path.exists(on_disk):
            self.skipTest('the data file is not on disk')
        present = load_workbook(on_disk)
        self.assertEqual(self.book.sheetnames, present.sheetnames)
        for name in self.book.sheetnames:
            rows = [list(r) for r in self.book[name].iter_rows(values_only=True)]
            self.assertEqual(rows, [list(r) for r in present[name].iter_rows(values_only=True)], msg=name)

    def test_every_stated_battery_pack_holds_its_heaviest_cells_and_board(self):
        """Matthias, 2026-10-28, "Cut at the cells": a pack whose mass is given has at its lower bound room for its
        heaviest cells (its largest energy over the NMC cells' lowest energy per kg, 00's composition.nmc_wh_per_kg_min)
        and its largest management board, so that the battery housing, the pack's remainder, never falls below zero.
        Each robot is drawn at its own mass (no scaling since 2026-10-29). A pack drawn from its energy is never lighter
        than its cells: its highest energy per kg is the cells' lowest."""
        params = Params()
        g_per_cm2 = self.apart.constants[schemas.ALL_ROBOTS]['Board mass per cm2 (boards not weighed)'][1][2]
        for robot in self.apart.robots:
            pack = next(p for p in self.apart.parts if p.robot == robot and p.name == 'Battery pack')
            if None in pack.bounds:
                continue
            constants = self.apart.constants[robot]
            cells = constants['Battery voltage'][1][2] * constants['Battery capacity'][1][2] / \
                params.composition.nmc_wh_per_kg_min
            board = max(b.bounds[2] * b.count for b in self.apart.boards
                        if b.robot == robot and b.kind == 'Battery pack')
            with self.subTest(robot=robot):
                self.assertGreaterEqual(pack.bounds[0], cells + board * g_per_cm2 / 1000 - 1e-9)
        packs = {p.robot: p.bounds for p in self.apart.parts if p.name == 'Battery pack'}
        self.assertEqual((packs['AgiBot X1'], packs['Fourier N1']), ((1.75, 2.2, 3.3), (2.26, 2.9, 3.2)))
        pack_wh_per_kg = self.apart.constants[schemas.ALL_ROBOTS]['Battery pack, Wh per kg (packs not weighed)'][1]
        self.assertLessEqual(pack_wh_per_kg[2], params.composition.nmc_wh_per_kg_min)

    def test_the_g1s_hips_are_cooled_passively_with_air_from_the_hip_area(self):
        """Matthias, 2026-10-28: "Joints have no fans, just passive cooling"; Munro (T3): "The hip area uses two
        centrifugal fans" for the whole robot, blowing air around the actuators, not two per hip."""
        heading = [c.value for c in self.book['Joints'][1]].index('Cooling')
        rows = [r for r in self.book['Joints'].iter_rows(min_row=2, values_only=True) if r[0] == 'Unitree G1'
                and str(r[2]).startswith('Hip')]
        self.assertEqual(len(rows), 3)
        for row in rows:
            self.assertEqual(row[heading], 'passive, with air from two centrifugal fans in the hip area', msg=row[2])

    def test_the_magnets_grade_by_each_joints_heat(self):
        """Matthias, 2026-10-28: "Heat has to matter and so the distribution will be different depending on the joint",
        then "Accept as proposed" (EVIDENCE.md E2.11): every joint in a heat group by its name, each group a
        distribution over grade classes. The head joints and the X1's grippers are cool (the entry, point 5)."""
        grades = {}
        for g in self.apart.grades:
            grades.setdefault(g.group, {})[g.klass] = g.probability
        self.assertEqual(grades, {'Knees': {'SH': 0.3, 'UH': 0.5, 'EH': 0.2},
                                  'Hips': {'SH': 0.5, 'UH': 0.4, 'EH': 0.1},
                                  'Waist': {'SH': 0.6, 'UH': 0.4},
                                  'Ankles': {'SH': 0.6, 'UH': 0.4},
                                  'Shoulders': {'H': 0.5, 'SH': 0.5},
                                  'Elbows and wrists': {'H': 0.7, 'SH': 0.3}})
        group_of = {'hip': 'Hips', 'knee': 'Knees', 'ankle': 'Ankles', 'waist': 'Waist', 'shoulder': 'Shoulders',
                    'elbow': 'Elbows and wrists', 'wrist': 'Elbows and wrists', 'head': 'Elbows and wrists',
                    'neck': 'Elbows and wrists', 'gripper': 'Elbows and wrists'}
        for j in self.apart.joints:
            self.assertEqual(j.heat_group, group_of[j.name.split()[0].lower()], msg=f'{j.robot}, {j.name}')

    def test_it_takes_no_arguments_and_writes_where_00_says(self):
        self.assertEqual(builder.output_path(), absolute(Params().data.parts_taken_apart))

    def test_it_carries_the_masses_and_parts_decided_on_2026_10_28(self):
        """Matthias, 2026-10-28, on the X1's and N1's masses and the G1's parts not carried over: "X1 max 35.3 kg",
        "Encoders", "XT30 connectors", "Main board cooler", then "Yes, build" (EVIDENCE.md E2.8e). Every robot has two
        encoders and two XT30 connectors per joint (a robot whose joints are shares: per joint its sources state); the
        G1, X1 and N1 a main board fan and heat sink of their own."""
        masses = {robot: self.apart.constants[robot]['Robot mass, with battery'][1]
                  for robot in ('Unitree G1', 'AgiBot X1', 'Fourier N1')}
        self.assertEqual(masses, {'Unitree G1': (34, 35, 36), 'AgiBot X1': (32, 33, 35.3),
                                  'Fourier N1': (38, 39, 40)})
        stated = {b['name']: b['joints_stated'] for b in vars(builder).values()
                  if isinstance(b, dict) and b.get('joints') == builder.AVERAGE}
        for robot in self.apart.robots:
            parts = {p.name: p for p in self.apart.parts if p.robot == robot}
            sensors = {p.name: p for p in self.apart.sensors if p.robot == robot}
            joints = stated.get(robot) or sum(j.count for j in self.apart.joints if j.robot == robot)
            with self.subTest(robot=robot):
                self.assertEqual(parts['Encoders (two per joint)'].count, 2 * joints)
                self.assertEqual(sensors['Encoder'].count, 2 * joints)
                xt30 = parts['XT30 (2+2) connectors (two per joint)']
                self.assertEqual(xt30.count, 2 * joints)
                # Each of the G1's mass; the Asimov 2's, as all of its composition, the Asimov 1's times 38 / 35.
                factor = 38 / 35 if robot == 'Menlo Asimov 2' else 1
                self.assertEqual(xt30.bounds, tuple(round(kg * factor, 4) for kg in (0.0015, 0.003, 0.0045)))
        for robot in ('Unitree G1', 'AgiBot X1', 'Fourier N1'):
            parts = {p.name: p for p in self.apart.parts if p.robot == robot}
            self.assertEqual(parts['Main board fan'].bounds, (0.005, 0.01, 0.02))
        for robot in ('AgiBot X1', 'Fourier N1'):
            parts = {p.name: p for p in self.apart.parts if p.robot == robot}
            sink = parts['Main board heat sink: heat pipes and fins']
            self.assertEqual((sink.bounds, sink.material, sink.label), ((0.055, 0.12, 0.19), 'Copper', 'E'))


if __name__ == '__main__':
    unittest.main()


class TestPartsNotEntered(unittest.TestCase):
    """Matthias, 2026-10-29, "Yes, build them", point 4: the parts the research found and the entry left out
    (EVIDENCE.md E5.20, "Not entered") entered, each out of its robot's frame: the computer's cooler of every robot
    without one, by its computer; the RP1's 30 V auxiliary battery, its bearings outside the actuators and its 80
    magnets in the covers; the Sprout's four time-of-flight sensors."""

    # The robots whose computer has an Intel or AMD laptop-class processor: cooled as the X1's and N1's mini PCs.
    X86 = {'AKINROBOTICS AKINCI-5', 'JAKA π', 'YMBOT E3'}

    @classmethod
    def setUpClass(cls):
        cls.apart, _ = written()

    def parts(self, robot: str) -> dict:
        return {p.name: p for p in self.apart.parts if p.robot == robot}

    def test_every_robot_has_its_computers_cooler(self):
        pipes, sink = 'Main board heat sink: heat pipes and fins', 'Main board heat sink'
        for robot in self.apart.robots:
            parts = self.parts(robot)
            factor = 38 / 35 if robot == 'Menlo Asimov 2' else 1   # the Asimov 1's masses times 38 / 35
            with self.subTest(robot=robot):
                self.assertIn('Main board fan', parts)
                self.assertEqual(parts['Main board fan'].bounds, tuple(round(kg * factor, 4) for kg in
                                                                       (0.005, 0.01, 0.02)))
                if robot in self.X86 | {'AgiBot X1', 'Fourier N1'}:
                    self.assertEqual((parts[pipes].bounds, parts[pipes].material), ((0.055, 0.12, 0.19), 'Copper'))
                    self.assertNotIn(sink, parts)
                elif robot == 'Booster T1':   # a Jetson AGX Orin and an Express-i7: both coolers, two fans
                    self.assertEqual(parts['Main board fan'].count, 2)
                    self.assertEqual(parts[sink].material, 'Aluminium')
                    self.assertEqual(parts[pipes].material, 'Copper')
                else:
                    self.assertEqual((parts[sink].bounds, parts[sink].material),
                                     (tuple(round(kg * factor, 4) for kg in (0.05, 0.1, 0.2)), 'Aluminium'))
                    self.assertNotIn(pipes, parts)

    def test_the_rp1s_fans_its_auxiliary_battery_bearings_and_cover_magnets(self):
        parts = self.parts('RoboParty RP1')
        self.assertEqual(parts['Waist fan'].count, 2)            # its BOM: two waist fans and a main-board fan
        battery = parts['Auxiliary battery cells (30 V)']
        self.assertEqual((battery.bounds, battery.material, battery.kind), ((0.12, 0.25, 0.5), 'Battery materials',
                                                                            'Battery pack'))
        bearings = parts['Bearings outside the actuators (9)']
        self.assertEqual((bearings.count, bearings.material, bearings.grade), (9, 'Steel', 'GCr15'))
        self.assertAlmostEqual(9 * bearings.bounds[1], 0.8 / 21 * 9, places=3)   # each as the X1's average
        magnets = parts['Magnets in the covers, N52 (80)']
        self.assertEqual((magnets.count, magnets.material, magnets.grade), (80, 'Magnets (NdFeB)', 'N'))
        # 4 × 2 mm and 4 × 4 mm discs of NdFeB, 7.5 g/cm3: 0.188 g and 0.377 g each.
        self.assertEqual(magnets.bounds, (0.000188, 0.000283, 0.000377))

    def test_the_sprouts_time_of_flight_sensors(self):
        sensors = {e.name: e for e in self.apart.sensors if e.robot == 'Fauna Sprout'}
        tof = sensors['Time-of-flight sensor']
        self.assertEqual((tof.count, tof.bounds), (4, (5, 10, 20)))
        units = {(t, u) for _, sensor, t, u in self.apart.elements if sensor == 'Time-of-flight sensor'}
        self.assertEqual(units, {('laser diode array', 1), ('photodetector array', 1)})
