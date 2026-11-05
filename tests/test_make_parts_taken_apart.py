"""
Tests of the builders of the parts files: tools/1_compact_research_developer/make_parts_taken_apart.py (type 1's,
data/researched/1_compact_research_developer/parts_taken_apart.xlsx) and
tools/2_full_scale_general_purpose_ai_research/make_parts_taken_apart.py (type 2's), with the machinery they share,
tools/parts_taken_apart.py.

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

Matthias, 2026-10-27: "Yes, put the builder in tools/make_parts_taken_apart.py as proposed, with its test and
documents"; 2026-10-29: "Yes, build it" (every robot of type 1 its own rows). The builder is the master of the data
file: what it writes must pass every check 01 makes of the file, hold every robot of type 1 as agreed (EVIDENCE.md E5),
and, while nobody has changed it, equal the file on disk cell by cell. Type 2's builder (2026-10-30, "Yes, build C")
writes its batch 1 as agreed in EVIDENCE.md E6.8. Everything is written into temporary folders: press Run, nothing in
the project is changed.
"""
import importlib.util
import os
import re
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
builder = load('make_parts_taken_apart', os.path.join('tools', '1_compact_research_developer',
                                                       'make_parts_taken_apart.py'))
builder_two = load('make_parts_taken_apart_2', os.path.join('tools', '2_full_scale_general_purpose_ai_research',
                                                           'make_parts_taken_apart.py'))
from src.params_schema import Params, absolute  # noqa: E402


# The robots the register's sheet Type 1 names in its column "Taken apart as", every version once (its builder).
REGISTER = load('make_humanoid_register', os.path.join('tools', 'make_humanoid_register.py'))
TYPE_ONE = [name for names in REGISTER.TAKEN_APART[1].values() for name in schemas.versions(names)]
TYPE_TWO = [name for names in REGISTER.TAKEN_APART[2].values() for name in schemas.versions(names)]
# Type 2's batch 1 (EVIDENCE.md E6.8), the GR-1 in two versions; batch 2 since 2026-10-30 (E7.5), TestTypeTwoBatchTwo.
BATCH_ONE_TWO = ['Fourier GR-1 one camera', 'Fourier GR-1 two cameras', 'Fourier GR-2', 'Unitree H1-2', 'Unitree H2',
                 'Unitree H2 Plus']


def written(which=None):
    """What a builder writes (type 1's unless `which` is another), read with 01's reader, from a temporary folder."""
    with tempfile.TemporaryDirectory() as folder:
        path = os.path.join(folder, 'parts_taken_apart.xlsx')
        (which or builder).build(path)
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
        self.assertEqual(len(self.apart.robots), 31)   # 30 robots, the K1 in two; the PrimeBOT Q1 out (E12.6)
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
        # 13: the PrimeBOT Q1 listed only since 2026-11-01 (E12.6); the Booster T2, Noetix Bumi and E1 their makers'
        # joints since E14 (E14.6 point 1).
        self.assertEqual(len(shared), 13)
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
            if p.material in ('Steel', 'Stainless steel', 'Electrical steel', 'Titanium alloy', 'Brass', 'Nickel'):
                self.assertTrue(p.grade, msg=f'{p.robot}, {p.name}')
        for s in self.apart.shares:
            if s.material in ('Steel', 'Stainless steel', 'Electrical steel', 'Titanium alloy', 'Brass', 'Nickel'):
                self.assertTrue(s.grade, msg=s.item)
        stator = {s.material: s.grade for s in self.apart.shares if s.item == 'Motor stator'}
        self.assertEqual(stator['Electrical steel'], 'M19 or M27')

    def test_what_it_writes_equals_the_data_file_on_disk(self):
        on_disk = builder.output_path()
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
        # In its type's folder, the folder the builder sits in (2026-10-30, "Yes, build C", Q1).
        self.assertEqual(builder.output_path(), absolute(Params().data.parts_taken_apart.format(
            folder='1_compact_research_developer')))
        self.assertEqual(builder_two.output_path(), absolute(Params().data.parts_taken_apart.format(
            folder='2_full_scale_general_purpose_ai_research')))

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
                pair = (0.0019, 0.00212, 0.0023)   # one mated pair (EVIDENCE.md E5.22); the Asimov 2's to four decimals
                self.assertEqual(xt30.bounds, pair if factor == 1 else tuple(round(kg * factor, 4) for kg in pair))
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
                    self.assertEqual(parts[sink].material, 'Aluminium alloys')
                    self.assertEqual(parts[pipes].material, 'Copper')
                else:
                    self.assertEqual((parts[sink].bounds, parts[sink].material),
                                     (tuple(round(kg * factor, 4) for kg in (0.05, 0.1, 0.2)), 'Aluminium alloys'))
                    self.assertNotIn(pipes, parts)

    def test_the_rp1s_fans_its_auxiliary_battery_bearings_and_cover_magnets(self):
        parts = self.parts('RoboParty RP1')
        self.assertEqual(parts['Waist fan'].count, 2)            # its BOM: two waist fans and a main-board fan
        battery = parts['Auxiliary battery cells (30 V)']
        self.assertEqual((battery.bounds, battery.material, battery.kind), ((0.12, 0.25, 0.5), 'Battery cells',
                                                                            'Battery pack'))
        bearings = parts['Bearings outside the actuators (9)']
        self.assertEqual((bearings.count, bearings.material, bearings.grade), (9, 'Steel', 'GCr15'))
        self.assertAlmostEqual(9 * bearings.bounds[1], 0.8 / 21 * 9, places=3)   # each as the X1's average
        magnets = parts['Magnets in the covers, N52 (80)']
        self.assertEqual((magnets.count, magnets.material, magnets.grade), (80, 'NdFeB magnets', 'N'))
        # 4 × 2 mm and 4 × 4 mm discs of NdFeB, 7.5 g/cm3: 0.188 g and 0.377 g each.
        self.assertEqual(magnets.bounds, (0.000188, 0.000283, 0.000377))

    def test_the_sprouts_time_of_flight_sensors(self):
        sensors = {e.name: e for e in self.apart.sensors if e.robot == 'Fauna Sprout'}
        tof = sensors['Time-of-flight sensor']
        self.assertEqual((tof.count, tof.bounds), (4, (5, 10, 20)))
        units = {(t, u) for _, sensor, t, u in self.apart.elements if sensor == 'Time-of-flight sensor'}
        self.assertEqual(units, {('laser diode array', 1), ('photodetector array', 1)})


class TestTheLastOpenParts(unittest.TestCase):
    """Matthias, 2026-10-29, "Yes, enter all" (EVIDENCE.md E5.22): the X1's parts by its newer parts list (its screws
    split, its 90 pins of 440C on their own, no longer counted twice), the parts found in its lists (brass inserts,
    sensor shield, silicone dampers, an XT60), the N1's network switch, and every robot's XT30 a mated pair of 2.12 g
    with brass contacts."""

    @classmethod
    def setUpClass(cls):
        cls.apart, _ = written()

    def parts(self, robot: str) -> dict:
        return {p.name: p for p in self.apart.parts if p.robot == robot}

    def test_the_x1s_screws_and_pins_by_its_newer_list(self):
        parts = self.parts('AgiBot X1')
        self.assertNotIn('Screws (about 980)', parts)
        self.assertNotIn('Stainless 17-4PH shafts and crosses; steel pins (about 115)', parts)
        carbon, stainless = parts['Screws, class 12.9 and 10.9 (677)'], parts['Screws, stainless 304 (150)']
        self.assertEqual((carbon.bounds, carbon.grade), ((0.207, 0.4145, 0.622), '42CrMo4'))
        self.assertEqual((stainless.bounds, stainless.grade), ((0.0459, 0.0918, 0.1377), 'Type 304'))
        self.assertAlmostEqual(carbon.bounds[1] + stainless.bounds[1], 0.6 * 827 / 980, places=3)   # by number
        pins = parts['Pins, SUS440C (90)']
        self.assertEqual((pins.bounds, pins.material, pins.grade, pins.label), ((0.105, 0.1086, 0.112), 'Stainless steel', '440C',
                                                                               'S'))
        shafts = parts['Stainless 17-4PH shafts and crosses']
        self.assertEqual((shafts.bounds, shafts.material, shafts.grade), ((0.075, 0.15, 0.225), 'Stainless steel', '17-4PH'))
        self.assertFalse([s for s in self.apart.shares if s.item.startswith('Stainless 17-4PH shafts and crosses;')])

    def test_the_x1s_parts_found_in_its_lists(self):
        parts = self.parts('AgiBot X1')
        inserts = parts['Brass threaded inserts, M3 (12) and M4 (4)']
        self.assertEqual((inserts.bounds, inserts.material, inserts.grade),
                         ((0.0065, 0.013, 0.0195), 'Brass', 'Brass'))
        shield = parts['Sensor shield, stainless 304']
        self.assertEqual((shield.bounds, shield.grade), ((0.01, 0.02, 0.03), 'Type 304'))
        dampers = parts['Silicone dampers (4)']
        self.assertEqual((dampers.count, dampers.bounds, dampers.material), (4, (0.001, 0.002, 0.003), 'Plastics'))
        xt60 = parts['XT60 connector, mated pair']
        self.assertEqual((xt60.count, xt60.bounds), (1, (0.0059, 0.0065, 0.0072)))

    def test_the_n1s_network_switch(self):
        boards = {b.name: b for b in self.apart.boards if b.robot == 'Fourier N1'}
        switch = boards['Network switch board']
        self.assertEqual((switch.bounds, switch.category, switch.label), ((30, 60, 90), 'ITC', 'E'))

    def test_every_connectors_contacts_are_brass(self):
        for item in ('XT30 (2+2) connectors (two per joint)', 'XT60 connector, mated pair'):
            contacts = [s for s in self.apart.shares if s.item == item and s.material == 'Brass']   # E19: brass its own
            self.assertEqual([(s.grade, s.share) for s in contacts], [('Brass', (0.175, 0.35, 0.525))], msg=item)


class TestTypeTwo(unittest.TestCase):
    """Type 2's builder (Matthias, 2026-10-30: "Yes, agree E6.8", "Yes, build C"): what it writes passes every check of
    01, holds the five robots of batch 1 as the register names them (the GR-1 in two versions), and each number as
    E6.8 agreed it."""

    @classmethod
    def setUpClass(cls):
        cls.apart, cls.book = written(builder_two)

    def parts(self, robot: str) -> dict:
        return {p.name: p for p in self.apart.parts if p.robot == robot}

    def constant(self, robot: str, quantity: str) -> tuple:
        return self.apart.constants[robot][quantity][1]

    def test_what_it_writes_passes_every_check_of_01(self):
        params = Params()
        lists_path, recipes_path = absolute(params.data.shared_lists), absolute(params.data.element_recipes)
        if not all(os.path.exists(p) for p in (lists_path, recipes_path)):
            self.skipTest('the shared lists or the element recipes are not on disk')
        lists, recipes = schemas.read_shared_lists(lists_path), schemas.read_element_recipes(recipes_path)
        faults = (schemas.check_parts_taken_apart(self.apart, lists, params)
                  + schemas.check_sibling_data(self.apart, params) + schemas.check_grades(self.apart, recipes, params))
        self.assertEqual([f.text for f in faults], [])

    def test_its_robots_are_those_the_register_names(self):
        self.assertEqual(sorted(self.apart.robots), sorted(TYPE_TWO))
        self.assertEqual({r.type for r in self.apart.robots.values()}, {2})
        # Batch 1, five robots (the GR-1 in two versions), batch 2, 24 (the H2-X in two versions; E7.5), and batch 2b,
        # 24 (the Walker Tienkung in two versions; E8.3).
        self.assertEqual(len(TYPE_TWO), 56 + 46)   # since 2026-10-30, the robots on wheels (E9.6)
        self.assertTrue(set(BATCH_ONE_TWO) <= set(TYPE_TWO))

    def test_the_joints_masses_by_the_refit_and_the_m107(self):
        # E6.8 point 1: 0.0689 kg × torque^0.566, half to 1.5 times; the H1-2's knees the M107, 1.9 kg ± 5 %.
        joints = {(j.robot, j.name): j for j in self.apart.joints}
        hip = joints[('Unitree H2', 'Hip pitch')]
        mode = 0.0689 * 360 ** 0.566
        self.assertEqual(hip.module_mass, tuple(round(f * mode, 4) for f in (0.5, 1, 1.5)))
        self.assertAlmostEqual(hip.module_mass[1], 1.928, places=3)
        self.assertEqual(joints[('Unitree H1-2', 'Knee')].module_mass, (1.805, 1.9, 1.995))
        # Its joint modules E: 25 of its 27 joints from their torques, so 01's table and 02's notes say so.
        modules = {p.name: p.label for p in self.apart.parts if p.robot == 'Unitree H1-2'
                   and p.name.startswith('Joint module')}
        self.assertEqual(set(modules.values()), {'E'})
        self.assertIn('joint torques', schemas.estimate_kinds(self.apart, 'Unitree H1-2'))
        self.assertEqual(joints[('Unitree H1-2', 'Hip pitch')].torque, 220)           # its page's peak (point 2)
        self.assertEqual(joints[('Fourier GR-1 one camera', 'Knee')].torque, 225)     # GR1T2.urdf (decided)
        self.assertEqual(joints[('Fourier GR-1 one camera', 'Shoulder pitch')].torque, 38.46)   # gr1t2.urdf
        counts = {r: sum(j.count for j in self.apart.joints if j.robot == r) for r in BATCH_ONE_TWO}
        self.assertEqual(counts, {'Fourier GR-1 one camera': 34, 'Fourier GR-1 two cameras': 34, 'Fourier GR-2': 31,
                                  'Unitree H1-2': 27, 'Unitree H2': 31, 'Unitree H2 Plus': 33})

    def test_the_hands(self):
        # E6.8 point 4: the H2 Plus's two hands 1.65 kg for both (decided), the Fourier hands their model's 0.443 kg.
        hands = {j.robot: j for j in self.apart.joints if j.name.startswith('Hand') and j.robot in BATCH_ONE_TWO}
        self.assertEqual(set(hands), {'Unitree H2 Plus', 'Fourier GR-2', 'Fourier GR-1 one camera',
                                      'Fourier GR-1 two cameras'})
        self.assertEqual(hands['Unitree H2 Plus'].module_mass, (0.4125, 0.825, 1.2375))
        self.assertEqual(hands['Fourier GR-2'].module_mass, (0.2215, 0.443, 0.6645))
        self.assertEqual({j.module for j in hands.values()}, {'small'})

    def test_the_batteries_by_voltage_and_capacity(self):
        # E6.8 point 6: 972, 864, 950 and 483 Wh at the modes; the GR-2's pack cut at its stated 9 kg.
        wh = {r: self.constant(r, 'Battery voltage')[1] * self.constant(r, 'Battery capacity')[1]
              for r in BATCH_ONE_TWO}
        for robot, energy in (('Unitree H2', 972), ('Unitree H2 Plus', 972), ('Unitree H1-2', 864),
                              ('Fourier GR-2', 950), ('Fourier GR-1 one camera', 483)):
            self.assertAlmostEqual(wh[robot], energy, places=1, msg=robot)
        self.assertEqual(self.parts('Fourier GR-2')['Battery pack'].bounds, (4.33, 5.79, 9))

    def test_the_cables_by_height_and_the_fourier_robots_ethernet_line(self):
        # E6.8 point 9: 7 / 14 / 21 m (the GR-1 6.5 / 13 / 19.5 m); the Fourier robots two power conductors and an
        # Ethernet line of eight.
        for robot in BATCH_ONE_TWO:
            own = self.apart.constants[robot]
            cable = schemas.CABLE_ETHERNET if robot.startswith('Fourier') else schemas.CABLE_FOUR
            self.assertIn(cable, own, msg=robot)
            self.assertEqual(own[cable][1], (6.5, 13, 19.5) if 'GR-1' in robot else (7, 14, 21), msg=robot)
        self.assertEqual(self.apart.constants['all'][schemas.ETHERNET_CS][1], (0.1, 0.205, 0.326))

    def test_the_gr1s_two_versions_differ_in_their_cameras_only(self):
        one, two = 'Fourier GR-1 one camera', 'Fourier GR-1 two cameras'

        def rows(robot, items):
            return sorted((p.name, p.count, p.bounds) for p in items if p.robot == robot)

        self.assertEqual(rows(one, self.apart.parts), rows(two, self.apart.parts))
        self.assertEqual(rows(one, self.apart.boards), rows(two, self.apart.boards))
        cameras = {p.robot: p.count for p in self.apart.sensors if p.name.startswith('Depth camera')}
        self.assertEqual((cameras[one], cameras[two]), (1, 2))

    def test_screws_by_mass_and_the_h2s_titanium(self):
        # E6.8 points 11 and 12.
        self.assertEqual(self.parts('Unitree H2')['Screws'].bounds, (0.4, 1.0, 2.0))
        self.assertEqual(self.parts('Fourier GR-2')['Screws'].bounds, (0.36, 0.9, 1.8))
        titanium = self.parts('Unitree H2')['Titanium alloy parts']
        self.assertEqual((titanium.bounds, titanium.material, titanium.grade),
                         ((0.42, 0.84, 1.26), 'Titanium alloy', 'Ti-6Al-4V'))
        self.assertNotIn('Titanium alloy parts', self.parts('Fourier GR-2'))

    def test_the_small_joints_driver_board_area_as_type_1s(self):
        # The G1's weighed board, the area every joint's board is scaled from: one copy, in both files.
        self.assertEqual(self.apart.constants['all'][schemas.DRIVER_AREA][1], (11.5, 22.9, 28.3))
        one, _ = written()
        g1 = next(b for b in one.boards if b.robot == 'Unitree G1' and b.name == 'Driver board, small joint')
        self.assertEqual(g1.bounds, (11.5, 22.9, 28.3))

    def test_what_it_writes_equals_the_data_file_on_disk(self):
        on_disk = builder_two.output_path()
        if not os.path.exists(on_disk):
            self.skipTest('the data file is not on disk')
        present = load_workbook(on_disk)
        for name in self.book.sheetnames:
            rows = [list(r) for r in self.book[name].iter_rows(values_only=True)]
            self.assertEqual(rows, [list(r) for r in present[name].iter_rows(values_only=True)], msg=name)


def fitted(torque: float) -> tuple:
    """Type 2's fit at a torque, half to 1.5 times, to four decimals (EVIDENCE.md E6.8 point 1)."""
    mode = 0.0689 * torque ** 0.566
    return tuple(round(f * mode, 4) for f in (0.5, 1, 1.5))


def half_to_one_and_a_half(mode: float) -> tuple:
    return tuple(round(f * mode, 4) for f in (0.5, 1, 1.5))


class TestTypeTwoBatchTwo(unittest.TestCase):
    """Type 2's batch 2 entered (Matthias, 2026-10-30: "Yes, all six" (E7.3), "Yes, agree E7.4", "Yes, agree E7.5",
    "Spec the entry", "Yes, build it"): its 24 robots as E7.5 agreed them, the H2-X in two versions; type 2's own
    template where a maker gives no joint torques (E7.4); the JingChu's stated knees beside the template's other
    joints (open point A); every joint named by its body part (D)."""

    # The seven robots whose joints give type 2's template (E7.4: every joint's torque; each robot once, the GR-1's
    # first version; their hands left out).
    SEVEN = ['Unitree H2', 'Unitree H1-2', 'Fourier GR-2', 'Fourier GR-1 one camera', 'Leju Kuavo 5', 'LimX Luna',
             'MagicLab MagicBot Gen1']
    # The robots whose joint modules are a share of their mass (E7.5 point 2), the H2-X in both versions.
    TEMPLATE = ['AeiROBOT ALICE 4', 'MirrorMe Bolt', 'Xiaomi CyberOne', 'Deep Robotics DR01', 'Figure AI Figure 03',
                'Unitree H2-X Core i7', 'Unitree H2-X Orin NX', 'HONOR D1', 'Simplexity I-Series',
                'ROBROS IGRIS-C', 'JCBOT JingChu', 'KAIST Humanoid', 'PAL Kangaroo', 'Kepler K1', 'Kepler K2',
                'LimX CL', 'LimX Oli', 'Lumos LUS2', 'VinMotion Motion 2', 'Zhejiang NAVAI-I3', 'Digit Nezha P01']
    GROUP = {'hip': 'Hip joints', 'knee': 'Knee joints', 'ankle': 'Ankle joints', 'waist': 'Waist joints',
             'shoulder': 'Shoulder joints', 'elbow': 'Elbow and wrist joints', 'wrist': 'Elbow and wrist joints',
             'head': 'Head joints'}
    LABEL = "as type 2's seven robots with every joint's torque on average"
    # Batch 2's robots (since batch 2b, 2026-10-30, the file holds more).
    BATCH_TWO = set(TEMPLATE) | {'DOBOT Atom', 'Leju Kuavo 5', 'LimX Luna', 'MagicLab MagicBot Gen1'}

    @classmethod
    def setUpClass(cls):
        cls.apart, cls.book = written(builder_two)

    def joints(self, robot: str) -> list:
        return [j for j in self.apart.joints if j.robot == robot]

    def constant(self, robot: str, quantity: str) -> tuple:
        return self.apart.constants[robot][quantity][1]

    def test_type_2s_template_numbers(self):
        # E7.4: the joint modules 20.2 / 40.4 / 60.6 % of the robot's mass; the battery 14.67 Wh per kg (type 2's
        # median), half to 1.5 times.
        shared = self.apart.constants['all']
        self.assertEqual(shared[schemas.JOINT_SHARE][1], (0.202, 0.404, 0.606))
        self.assertEqual(shared[schemas.ENERGY_PER_KG][1], (7.335, 14.67, 22.005))

    def test_the_template_split_is_the_seven_robots_without_their_hands(self):
        # Recomputed here from the seven robots' own rows: each group and class its share of the body's joint modules
        # at the modes, averaged over the seven; the rows named for it (open point B).
        expected: dict = {}
        for robot in self.SEVEN:
            body = [j for j in self.joints(robot) if not j.name.startswith('Hand')]
            total = sum(j.count * j.module_mass[1] for j in body)
            for j in body:
                key = (self.GROUP[j.name.split()[0].lower()], j.module)
                expected[key] = expected.get(key, 0) + j.count * j.module_mass[1] / total / len(self.SEVEN)
        rows = [j for j in self.joints('LimX CL')]
        got = {(j.name.split(',')[0], j.module): j.share for j in rows}
        self.assertEqual(set(got), set(expected))
        for key, share in expected.items():
            self.assertAlmostEqual(got[key], share, places=6, msg=key)
        self.assertAlmostEqual(sum(got.values()), 1, places=9)
        for j in rows:
            self.assertTrue(j.name.endswith(f'({self.LABEL})'), j.name)

    def test_which_robots_rest_on_the_template(self):
        # Since E14 (E14.6 point 2) the H2-X and the Oli take their joints from their makers' models.
        template = [r for r in self.TEMPLATE if r not in E14_OWN]
        shared = {j.robot for j in self.apart.joints if j.share is not None and j.robot in self.BATCH_TWO}
        self.assertEqual(shared, set(template))
        for robot in template:
            self.assertIn('joint shares', schemas.estimate_kinds(self.apart, robot), msg=robot)

    def test_the_jingchus_knees_stated_its_other_joints_the_template(self):
        # E7.5 point 2: "关节重量：2kg" each, ± 5 % (S); the template's knee rows left out, its others as for every robot
        # of the template; nothing rescaled.
        template = {(j.name, j.module): j.share for j in self.joints('LimX CL')}
        mine = self.joints('JCBOT JingChu')
        knees = [j for j in mine if j.name.split()[0] == 'Knee']
        self.assertEqual([(j.count, j.module, j.module_mass, j.share) for j in knees],
                         [(2, 'large', (1.9, 2.0, 2.1), None)])
        shares = {(j.name, j.module): j.share for j in mine if j.share is not None}
        knee_rows = {k: v for k, v in template.items() if k[0].startswith('Knee joints')}
        self.assertTrue(knee_rows)
        self.assertEqual(shares, {k: v for k, v in template.items() if k not in knee_rows})
        self.assertAlmostEqual(sum(shares.values()), 1 - sum(knee_rows.values()), places=9)
        hands = [j for j in mine if j.name.startswith('Hand')]
        self.assertEqual([(j.count, j.module_mass) for j in hands], [(2, (0.2215, 0.443, 0.6645))])

    def test_the_four_robots_with_every_joints_torque(self):
        # E7.5 point 1: type 2's fit at each joint's torque of the maker's model; the joints named by their axes (D).
        kuavo = {'Hip roll': 127, 'Hip yaw': 71, 'Hip pitch': 132, 'Knee': 280, 'Ankle pitch': 91.6,
                 'Ankle roll': 68.4, 'Waist yaw': 102, 'Shoulder pitch': 66, 'Shoulder roll': 75, 'Shoulder yaw': 57,
                 'Elbow': 75, 'Wrist yaw': 14.1, 'Wrist roll': 14.1, 'Wrist pitch': 14.1, 'Head yaw': 1.5,
                 'Head pitch': 12}
        atom = {'Hip pitch': 207.76, 'Hip roll': 241.42, 'Hip yaw': 104.16, 'Knee': 213.8, 'Ankle pitch': 89.896,
                'Ankle roll': 89.896, 'Waist yaw': 104.16, 'Shoulder pitch': 56, 'Shoulder roll': 36,
                'Shoulder yaw': 36, 'Elbow pitch': 36, 'Elbow roll': 18.6, 'Wrist pitch': 18.6, 'Wrist yaw': 18.6,
                'Head yaw': 12, 'Head pitch': 12}
        for robot, torques, body, modules in (('Leju Kuavo 5', kuavo, 29, 21.66), ('DOBOT Atom', atom, 29, 22.37),
                                              ('LimX Luna', None, 27, 23.24), ('MagicLab MagicBot Gen1', None, 30,
                                                                               32.59)):
            rows = [j for j in self.joints(robot) if not j.name.startswith('Hand')]
            with self.subTest(robot=robot):
                self.assertEqual(sum(j.count for j in rows), body)
                for j in rows:
                    self.assertEqual(j.module_mass, fitted(j.torque), msg=j.name)
                    if torques:
                        self.assertEqual(j.torque, torques[j.name], msg=j.name)
                self.assertAlmostEqual(sum(j.count * j.module_mass[1] for j in rows), modules, places=1)
        # The Atom's waist (DOBOT's file a placeholder of 1000 N·m) its own hip yaw's, E (E7.5 point 1).
        self.assertNotIn(1000, [j.torque for j in self.joints('DOBOT Atom')])

    def test_every_joint_named_by_its_body_part(self):
        for j in self.apart.joints:
            self.assertIn(j.name.split()[0].lower(), schemas.JOINT_KIND, msg=f'{j.robot}, {j.name}')

    def test_the_masses_as_agreed(self):
        # E7.5 point 5 and its table: the maker's where stated (E7.3, 2), else the register's.
        masses = {'AeiROBOT ALICE 4': (44, 45, 46), 'DOBOT Atom': (57.91, 58.91, 61.81), 'MirrorMe Bolt': (74, 75, 76),
                  'Xiaomi CyberOne': (51, 52, 53), 'Deep Robotics DR01': (79, 80, 81),
                  'Figure AI Figure 03': (60, 61, 62), 'Unitree H2-X Core i7': (65, 66, 70),
                  'Unitree H2-X Orin NX': (65, 66, 70), 'HONOR D1': (44, 45, 46),
                  'Simplexity I-Series': (59, 60, 61), 'ROBROS IGRIS-C': (55, 56, 57), 'JCBOT JingChu': (64, 65, 66),
                  'KAIST Humanoid': (74, 75, 76), 'PAL Kangaroo': (50, 57.5, 65), 'Kepler K1': (84, 85, 86),
                  'Kepler K2': (74, 75, 76), 'Leju Kuavo 5': (62.5, 63.5, 69.44), 'LimX CL': (44, 45, 46),
                  'LimX Oli': (54, 55, 55), 'LimX Luna': (55, 56, 57), 'Lumos LUS2': (56, 57, 58),
                  'MagicLab MagicBot Gen1': (66.4, 70, 71), 'VinMotion Motion 2': (60, 67.5, 75),
                  'Zhejiang NAVAI-I3': (69, 70, 71), 'Digit Nezha P01': (64, 65, 66)}
        for robot, mass in masses.items():
            self.assertEqual(self.constant(robot, 'Robot mass, with battery'), mass, msg=robot)

    def test_the_batteries(self):
        # E7.5 point 6: the maker's energy where stated (voltage × capacity at the modes); else no voltage, the energy
        # per kg of the template.
        stated = {'Unitree H2-X Core i7': 1152, 'Unitree H2-X Orin NX': 1152, 'ROBROS IGRIS-C': 816,
                  'JCBOT JingChu': 960, 'PAL Kangaroo': 976, 'LimX Oli': 478.8, 'LimX Luna': 1008, 'Lumos LUS2': 540,
                  'MagicLab MagicBot Gen1': 1350}
        for robot in set(self.TEMPLATE) | {'DOBOT Atom', 'Leju Kuavo 5', 'LimX Luna', 'MagicLab MagicBot Gen1'}:
            own = self.apart.constants[robot]
            with self.subTest(robot=robot):
                if robot in stated:
                    wh = own['Battery voltage'][1][1] * own['Battery capacity'][1][1]
                    self.assertAlmostEqual(wh, stated[robot], places=1)
                else:
                    self.assertNotIn('Battery voltage', own)
        cells = {p.robot: p.label for p in self.apart.parts if p.name == 'Battery cells'}
        self.assertEqual(cells['Lumos LUS2'], 'S')   # "Ternary lithium battery"

    def test_the_h2x_two_versions_differ_in_pc2_only(self):
        intel, orin = 'Unitree H2-X Core i7', 'Unitree H2-X Orin NX'

        def rows(robot, items, leave=()):
            return sorted((p.name, p.count, p.bounds) for p in items if p.robot == robot and p.name not in leave)

        coolers = ('Main board heat sink', 'Main board heat sink: heat pipes and fins')
        self.assertEqual(rows(intel, self.apart.parts, coolers), rows(orin, self.apart.parts, coolers))
        self.assertEqual(rows(intel, self.apart.sensors), rows(orin, self.apart.sensors))
        boards = {r: {b.name: b.bounds for b in self.apart.boards if b.robot == r} for r in (intel, orin)}
        self.assertEqual(boards[intel]['Computer board PC2, Intel Core i7'], (60, 120, 180))
        self.assertEqual(boards[orin]['Compute module PC2, NVIDIA Jetson Orin NX'], (29.74, 31.3, 32.87))
        self.assertEqual(boards[orin]['Carrier board of the Orin NX'], (60, 120, 180))
        self.assertEqual({k: v for k, v in boards[intel].items() if 'PC2' not in k},
                         {k: v for k, v in boards[orin].items() if 'PC2' not in k and 'Carrier' not in k})

    def test_the_cables_by_height_and_the_kangaroos_ethernet_line(self):
        # E7.5 point 9: 8 m per metre of height, to the half metre, half to 1.5 times; the Kangaroo's EtherCAT.
        modes = {'AeiROBOT ALICE 4': 13, 'DOBOT Atom': 13.5, 'MirrorMe Bolt': 14, 'Xiaomi CyberOne': 14,
                 'Deep Robotics DR01': 13.5, 'Figure AI Figure 03': 14, 'Unitree H2-X Core i7': 14,
                 'Unitree H2-X Orin NX': 14, 'HONOR D1': 13.5, 'Simplexity I-Series': 14, 'ROBROS IGRIS-C': 12.5,
                 'JCBOT JingChu': 13.5, 'KAIST Humanoid': 13, 'PAL Kangaroo': 13, 'Kepler K1': 14, 'Kepler K2': 14,
                 'Leju Kuavo 5': 14, 'LimX CL': 13, 'LimX Oli': 13, 'LimX Luna': 13, 'Lumos LUS2': 13,
                 'MagicLab MagicBot Gen1': 14, 'VinMotion Motion 2': 13, 'Zhejiang NAVAI-I3': 14.5,
                 'Digit Nezha P01': 11.5}
        for robot, mode in modes.items():
            own = self.apart.constants[robot]
            cable = schemas.CABLE_ETHERNET if robot == 'PAL Kangaroo' else schemas.CABLE_FOUR
            self.assertEqual(own[cable][1], half_to_one_and_a_half(mode), msg=robot)

    def test_the_hands_and_grippers_of_batch_2(self):
        # E7.5 point 4.
        six = half_to_one_and_a_half(0.443)
        eleven = half_to_one_and_a_half(0.443 * 11 / 6)
        expected = {'Leju Kuavo 5': six, 'ROBROS IGRIS-C': six, 'JCBOT JingChu': six, 'Kepler K1': eleven,
                    'Kepler K2': eleven, 'MagicLab MagicBot Gen1': half_to_one_and_a_half(1.178 / 2),
                    'Figure AI Figure 03': (0.4125, 0.825, 1.2375), 'LimX Oli': (0.41, 0.43, 0.45)}
        got = {}
        for j in self.apart.joints:
            if j.robot in self.BATCH_TWO and j.name.split()[0] in ('Hand', 'Gripper'):
                got[j.robot] = (j.count, j.module, j.module_mass)
        self.assertEqual(got, {r: (2, 'small', m) for r, m in expected.items()})

    def test_one_motion_sensor_where_the_maker_names_no_sensor(self):
        # E7.5 point 8. The block's own sensors: since 2026-11-05 the cameras of E31 beside them (their sources E31's),
        # TestCamerasE31.
        for robot in ('DOBOT Atom', 'MirrorMe Bolt', 'Deep Robotics DR01', 'HONOR D1', 'Simplexity I-Series',
                      'KAIST Humanoid', 'LimX CL', 'VinMotion Motion 2', 'Zhejiang NAVAI-I3', 'Digit Nezha P01'):
            sensors = [(p.name, p.count) for p in self.apart.sensors if p.robot == robot and p.name != 'Encoder'
                       and not p.sources.startswith('E31')]
            self.assertEqual(sensors, [('Motion sensor (IMU)', 1)], msg=robot)

    def test_a_compute_module_where_the_maker_names_only_its_power(self):
        # E7.5 point 7: an Orin NX-sized module and its carrier, estimates, so half to 1.5 times the Orin NX's 31.3 cm2.
        for robot in ('JCBOT JingChu', 'Kepler K1', 'Kepler K2', 'Leju Kuavo 5', 'MagicLab MagicBot Gen1'):
            boards = [b for b in self.apart.boards if b.robot == robot and b.kind == 'Boards']
            modules = [b for b in boards if b.name.startswith('Compute module')]
            carriers = [b for b in boards if b.name.startswith('Carrier board')]
            self.assertEqual([b.bounds for b in modules], [(15.65, 31.3, 46.95)], msg=robot)
            self.assertEqual([b.bounds for b in carriers], [(60, 120, 180)], msg=robot)


class TestTypeTwoBatchTwoB(unittest.TestCase):
    """Type 2's batch 2b entered (Matthias, 2026-10-30: "Yes, all six" (E8.2), the Omni "has to be included", "Yes, agree
    E8.3", "Yes, build it" with the spec's open points A to C): its 24 robots as E8.3 agreed them, the Walker Tienkung in
    two versions; the template of E7.4 unchanged (A); Qinglong's and TALOS's joints named by their place and axis (B)."""

    TORQUES = {'Unitree H1': (19, 21.67), 'OpenLoong Qinglong': (31, 30.11), 'X-Humanoid Tien Kung 2.0': (30, 24.79),
               'Walker Tienkung Vision': (21, 21.00), 'Walker Tienkung Embodied': (30, 24.06), 'PAL TALOS': (30, 26.09)}
    TEMPLATE = ['X-Humanoid Omni', 'Tesla Optimus Gen 3', 'Tesla Optimus Gen 2', 'Tesla Optimus V2.5',
                'Cyan Robotics Orca', 'Sanctuary Phoenix', 'PHYBOT M1', 'PAL REEM-C', 'Robotera L7', 'EngineAI SE01',
                'Zeroth Sean', 'Siasun Songxing', 'Unitree Superman', 'Westwood THEMIS', 'X-Humanoid TianGong Ultra',
                'Tlibot Tianzhen Z1', 'X-Humanoid Tien Kung 3.0', 'Tlibot T1', 'DroidUp Walker II']

    @classmethod
    def setUpClass(cls):
        cls.apart, _ = written(builder_two)

    def joints(self, robot: str) -> list:
        return [j for j in self.apart.joints if j.robot == robot]

    def test_the_template_unchanged(self):
        # Open point A: E7.4's numbers and its seven robots; batch 2b's robots of the template take its rows as they are.
        shared = self.apart.constants['all']
        self.assertEqual(shared[schemas.JOINT_SHARE][1], (0.202, 0.404, 0.606))
        rows = {(j.name, j.share) for j in self.joints('LimX CL')}
        for robot in self.TEMPLATE:
            if robot in E14_OWN:   # its maker's joints since E14 (E14.6 point 2)
                continue
            self.assertEqual({(j.name, j.share) for j in self.joints(robot) if j.share is not None}, rows, msg=robot)

    def test_the_robots_with_every_joints_torque(self):
        for robot, (count, modules) in self.TORQUES.items():
            body = [j for j in self.joints(robot) if j.name.split()[0] not in ('Hand', 'Gripper')]
            with self.subTest(robot=robot):
                self.assertEqual(sum(j.count for j in body), count)
                self.assertAlmostEqual(sum(j.count * j.module_mass[1] for j in body), modules, places=1)
                self.assertTrue(all(j.share is None for j in self.joints(robot)))
        knees = [j for j in self.joints('Unitree H1') if j.name.startswith('Knee')]
        self.assertEqual([(j.count, j.module_mass) for j in knees], [(2, (1.805, 1.9, 1.995))])   # the M107 (E8.3, 1)
        self.assertEqual(max(j.torque for j in self.joints('PAL TALOS') if j.torque), 300)          # LAAS's model
        waist = [j for j in self.joints('Walker Tienkung Vision') if j.name.startswith('Waist')]
        self.assertEqual([(j.torque, j.module_mass) for j in waist], [(180, fitted(180))])       # E: its hip roll's

    def test_every_joint_named_by_its_body_part(self):
        for j in self.apart.joints:
            self.assertIn(j.name.split()[0].lower(), schemas.JOINT_KIND, msg=f'{j.robot}, {j.name}')

    def test_the_masses_as_agreed(self):
        masses = {'X-Humanoid Omni': (38.5, 39.5, 40.5), 'Tesla Optimus Gen 3': (51, 52, 53),
                  'Tesla Optimus Gen 2': (55, 56, 57), 'Tesla Optimus V2.5': (54, 55, 56), 'Cyan Robotics Orca': (49, 50, 51),
                  'Sanctuary Phoenix': (69, 70, 71), 'PHYBOT M1': (59, 60, 61), 'OpenLoong Qinglong': (85.14, 86.14, 87.14),
                  'PAL REEM-C': (79, 80, 81), 'Robotera L7': (66.2, 67.2, 68.2), 'EngineAI SE01': (79, 80, 81),
                  'Zeroth Sean': (44, 45, 46), 'Siasun Songxing': (84, 85, 86), 'Unitree Superman': (44, 45, 46),
                  'PAL TALOS': (93.34, 95, 96), 'Westwood THEMIS': (35.5, 36.5, 37.92),
                  'X-Humanoid TianGong Ultra': (54, 55, 56), 'Tlibot Tianzhen Z1': (44, 45, 46),
                  'X-Humanoid Tien Kung 2.0': (66.96, 67.96, 68.96), 'X-Humanoid Tien Kung 3.0': (63.5, 64.5, 65.5),
                  'Tlibot T1': (42, 43, 44), 'DroidUp Walker II': (31, 32, 33), 'Walker Tienkung Vision': (60, 61, 62),
                  'Walker Tienkung Embodied': (72, 73, 74), 'Unitree H1': (46, 47, 59.34)}
        for robot, mass in masses.items():
            self.assertEqual(self.apart.constants[robot]['Robot mass, with battery'][1], mass, msg=robot)

    def test_the_batteries(self):
        stated = {'Unitree H1': 864, 'Robotera L7': 900, 'Walker Tienkung Vision': 1584, 'Walker Tienkung Embodied': 1584,
                  'Tlibot T1': 1110, 'X-Humanoid Tien Kung 3.0': 864,
                  'Westwood THEMIS': 518.4}   # its brochure's "Dual 259.2 Wh" since E14 (E14.5 point B)
        for robot in self.TEMPLATE + list(self.TORQUES):
            own = self.apart.constants[robot]
            with self.subTest(robot=robot):
                if robot in stated:
                    self.assertAlmostEqual(own['Battery voltage'][1][1] * own['Battery capacity'][1][1], stated[robot],
                                           places=1)
                else:
                    self.assertNotIn('Battery voltage', own)

    def test_hands_and_grippers(self):
        expected = {'Robotera L7': (1.045, 1.1, 1.155), 'EngineAI SE01': half_to_one_and_a_half(0.443),
                    'Walker Tienkung Embodied': half_to_one_and_a_half(0.443),
                    'Westwood THEMIS': half_to_one_and_a_half(0.463), 'PAL TALOS': half_to_one_and_a_half(1.094)}
        got = {j.robot: j.module_mass for j in self.apart.joints if j.robot in self.TEMPLATE + list(self.TORQUES)
               and j.name.split()[0] in ('Hand', 'Gripper')}
        self.assertEqual(got, expected)

    def test_the_cables_by_height_and_talos_ethernet_line(self):
        modes = {'X-Humanoid Omni': 11, 'Unitree H1': 14.5, 'PAL TALOS': 14, 'Walker Tienkung Vision': 14,
                 'Robotera L7': 13.5, 'Zeroth Sean': 12.5}
        for robot, mode in modes.items():
            cable = schemas.CABLE_ETHERNET if robot == 'PAL TALOS' else schemas.CABLE_FOUR
            self.assertEqual(self.apart.constants[robot][cable][1], half_to_one_and_a_half(mode), msg=robot)

    def test_the_walker_tienkungs_two_versions(self):
        vision, embodied = 'Walker Tienkung Vision', 'Walker Tienkung Embodied'
        boards = {r: {b.name: b.count for b in self.apart.boards if b.robot == r and b.kind == 'Boards'}
                  for r in (vision, embodied)}
        self.assertEqual(boards[vision]['Compute module, NVIDIA Jetson AGX Orin'], 1)
        self.assertEqual(boards[embodied]['Compute module, NVIDIA Jetson AGX Orin'], 2)
        extra = {j.name for j in self.joints(embodied)} - {j.name for j in self.joints(vision)}
        self.assertEqual({n.split()[0] for n in extra}, {'Head', 'Wrist', 'Hand'})

    def test_the_compute_modules_read_from_their_power(self):
        # E8.3 point 7: a "2070" controller as the H2 Plus's Thor, the L7's "275 TOPS" Orin as an AGX Orin (E).
        for robot in ('X-Humanoid Omni', 'X-Humanoid Tien Kung 3.0', 'Robotera L7'):
            modules = [b.bounds for b in self.apart.boards if b.robot == robot and b.name.startswith('Compute module')]
            self.assertEqual(modules, [(43.5, 87, 130.5)], msg=robot)

    def test_one_motion_sensor_where_the_maker_names_none(self):
        # The block's own sensors: since 2026-11-05 the cameras of E31 beside them (their sources E31's), TestCamerasE31.
        for robot in ('Tesla Optimus Gen 3', 'Cyan Robotics Orca', 'Sanctuary Phoenix', 'PHYBOT M1', 'PAL REEM-C',
                      'Zeroth Sean', 'Siasun Songxing', 'Unitree Superman',   # THEMIS: its brochure's, since E14
                      'X-Humanoid TianGong Ultra', 'Tlibot Tianzhen Z1', 'Tlibot T1', 'OpenLoong Qinglong',
                      'X-Humanoid Tien Kung 2.0'):
            sensors = [(p.name, p.count) for p in self.apart.sensors if p.robot == robot and p.name != 'Encoder'
                       and not p.sources.startswith('E31')]
            self.assertEqual(sensors, [('Motion sensor (IMU)', 1)], msg=robot)

# Type 2's robots on wheels (EVIDENCE.md E9.6, agreed 2026-10-30, "Yes, agree E9.6"; entered on "Yes, build it", E9.7):
# each as (its mass, its driven wheels and the hub motor's mode in kg, its steered wheels, its casters, its lift column
# ('stated', a share of its mass, or none), its battery's energy in Wh where stated or derived, else None).
ON_WHEELS = {
    'AgiBot A2-W': ((229, 230, 231), 2, 8.5, 0, 2, None, None),
    'AgiBot G1': ((149, 150, 151), 2, 3.75, 0, 2, None, None),
    'ROBOTIS AI Worker': ((89, 90, 94.42), 3, 3.8, 3, 0, 'stated', 2040),
    'Flexiv AICO 2-4': ((280, 281, 282), 2, 8.5, 0, 2, None, None),
    'Flexiv AICO 2-10': ((394, 395, 396), 2, 8.5, 0, 2, None, None),
    'PAL ARI': ((59, 60, 61), 2, 1.4, 0, 2, None, 960),
    'KIT ARMAR-7': ((119, 120, 121), 3, 3.75, 0, 0, None, None),
    'Astribot S1': ((79, 80, 81), 2, 3.75, 0, 2, None, None),
    'Astribot T1': ((65, 66, 67), 2, 1.4, 0, 2, None, None),
    'ELU.AI AstroDroid AD-01': ((119, 120, 121), 2, 3.75, 0, 2, None, None),
    'Honda Avatar': ((109, 110, 111), 2, 3.75, 0, 2, None, None),
    'CASBOT W1': ((259, 260, 261), 2, 8.5, 0, 4, 'share', 1200),
    'Toyota CUE7': ((73, 74, 75), 2, 3.75, 0, 0, None, None),
    'RealMan Dual-Arm Lift': ((156, 157, 158), 2, 4.85, 0, 2, 'share', None),
    'Tangible Robots Eggie': ((44, 45, 46), 2, 1.4, 0, 2, None, None),
    'Feather Robotics Feather': ((104, 105, 106), 3, 1.4, 3, 0, 'share', 2400),
    'Unitree G1-D Ultimate': ((89, 90, 91), 2, 3.75, 0, 2, 'share', 1872),
    'AgiBot G2': ((184, 185, 186), 4, 3.75, 4, 0, None, 1652),
    'Unitree H2-D Flagship': ((119, 120, 121), 2, 3.75, 0, 2, 'share', 1440),
    'MagicLab MagicBot D1': ((149, 150, 151), 4, 3.75, 4, 0, None, 1652),
    'Blue Worm Mantis Standard': ((49, 50, 51), 4, 1.4, 0, 0, 'share', None),
    'Spirit AI Moz1': ((69, 70, 71), 4, 1.4, 0, 0, None, None),
    'Sanctuary Phoenix Gen 8': ((69, 70, 71), 2, 1.4, 0, 2, None, None),
    'Galaxea R1 Pro': ((125, 126, 127), 3, 3.75, 3, 0, None, 1680),
    'Unitree R1-A5-D': ((29, 30, 31), 4, 1.4, 0, 0, None, None),
    'Unitree R1-A7-D': ((31, 32, 33), 4, 1.4, 0, 0, None, None),
    'Rainbow Robotics RB-Y1 A': ((130, 131, 132.22), 2, 3.75, 0, 2, None, 1250),
    'Rainbow Robotics RB-Y1 M': ((169, 170, 171), 4, 3.75, 0, 0, None, 2500),
    'Pollen Robotics Reachy 2': ((49, 50, 51), 3, 2.9, 0, 0, None, 840),
    'RealMan RealBot-01': ((124, 125, 126), 2, 3.75, 0, 2, None, 1920),
    'RealMan RealBot-L2': ((119, 120, 121), 2, 3.75, 0, 2, 'share', 960),
    'RealMan RealBot-S2': ((124, 125, 126), 4, 1.4, 4, 0, None, 960),
    'PAL TIAGo Pro': ((79, 80, 95), 4, 1.4, 0, 0, 'share', 720),
    'Tokyo Robotics Torobo': ((119, 120, 121), 4, 1.4, 0, 0, None, None),
    'Lanxin VB1-I': ((60, 65, 70), 2, 1.4, 0, 2, None, None),
    'Lanxin VB2': ((65, 70, 75), 4, 1.4, 0, 0, None, None),
    'Dexmate Vega 1 Pro': ((134, 135, 141.0), 2, 3.7, 2, 2, None, None),
    'Lanxin VersaBot VB-1': ((74, 75, 76), 4, 1.4, 0, 0, None, None),
    'Yue Quan Bionics W-Bot': ((59, 60, 61), 2, 1.4, 0, 2, None, 2400),
    'Tlibot Y1': ((149, 150, 151), 2, 3.75, 0, 2, None, None),
    'Tlibot Y2-B': ((84, 85, 86), 2, 3.75, 0, 2, None, None),
    'Tlibot Y2-P': ((94, 95, 96), 2, 3.75, 0, 2, None, None),
    'Yunmu YMBot D': ((99, 100, 101), 2, 3.75, 0, 2, None, None),
    'Yunmu YMBot D2': ((149, 150, 151), 2, 3.75, 0, 2, None, None),
    'Yunmu YMBot D4': ((99, 100, 101), 2, 3.75, 0, 2, None, None),
    'PsiBot ψ-SynRobot': ((64, 65, 66), 2, 1.4, 0, 2, None, None),
}
# The four robots on wheels whose makers give every joint (E9.6 point 2), their body joints' modules at the modes (kg),
# the template's source; and the W-Bot, by its page's torques.
OWN_ON_WHEELS = {'Dexmate Vega 1 Pro': 17.83, 'Rainbow Robotics RB-Y1 A': 18.17, 'Rainbow Robotics RB-Y1 M': 18.17,
                 'ROBOTIS AI Worker': 12.867, 'Pollen Robotics Reachy 2': 10.45, 'Yue Quan Bionics W-Bot': 18.72}
OUTSIDE_THE_BODY = ('Wheel', 'Steering', 'Lift', 'Hand', 'Gripper')


class TestTypeTwoOnWheels(unittest.TestCase):
    """Type 2's 43 robots on wheels entered (Matthias, 2026-10-30: "Yes, agree E9.4", "Yes, agree E9.6", "Spec the
    entry", "Yes, build it" with the spec's open points A to D as recommended): 46 blocks with the AICO 2, the RB-Y1 and
    the R1-D in two versions; their drive wheels, steering, casters and lift columns; the wheeled template; the CASBOT
    W1's LFP cells; the kind "Torso boards" renamed "Boards"."""

    @classmethod
    def setUpClass(cls):
        cls.apart, _ = written(builder_two)

    def joints(self, robot: str) -> list:
        return [j for j in self.apart.joints if j.robot == robot]

    def test_the_46_are_the_registers(self):
        self.assertTrue(set(ON_WHEELS) <= set(self.apart.robots))
        self.assertTrue(set(ON_WHEELS) <= set(TYPE_TWO))
        self.assertEqual(len(TYPE_TWO), 56 + 46)

    def test_the_masses_as_agreed(self):
        for robot, (mass, *_rest) in ON_WHEELS.items():
            self.assertEqual(self.apart.constants[robot]['Robot mass, with battery'][1], mass, msg=robot)

    def test_drive_wheels_steering_and_casters(self):
        for robot, (_m, driven, hub, steered, casters, _l, _w) in ON_WHEELS.items():
            with self.subTest(robot=robot):
                wheels = [j for j in self.joints(robot) if j.name.startswith('Wheel')]
                self.assertEqual(sum(j.count for j in wheels), driven)
                self.assertEqual({j.module_mass[1] for j in wheels}, {hub})
                self.assertEqual({(j.heat_group, j.region) for j in wheels}, {('Hips', 'Base')})   # open point A
                steering = [j for j in self.joints(robot) if j.name.startswith('Steering')]
                self.assertEqual(sum(j.count for j in steering), steered)
                self.assertTrue(all(j.heat_group == 'Waist' for j in steering))
                found = [p for p in self.apart.parts if p.robot == robot and p.name == 'Casters']
                self.assertEqual(sum(p.count for p in found), casters)
                self.assertTrue(all(p.kind == 'Wheeled base' and p.region == 'Base' for p in found))

    def test_the_lift_columns(self):
        shared = self.apart.constants['all']
        self.assertEqual(shared['Lift column, share of the robot mass, on wheels'][1], (0.0995, 0.199, 0.2985))
        for robot, (*_x, lift, _w) in ON_WHEELS.items():
            with self.subTest(robot=robot):
                column = [p for p in self.apart.parts if p.robot == robot and p.kind == 'Lift column']
                motor = [j for j in self.joints(robot) if j.name.startswith('Lift')]
                self.assertEqual(len(column), 0 if lift is None else 1)
                self.assertEqual(sum(j.count for j in motor), 0 if lift is None else 1)
                if lift == 'stated':
                    self.assertEqual(column[0].bounds, half_to_one_and_a_half(17.01))
                elif lift == 'share':
                    self.assertTrue(column[0].computed.startswith(schemas.ROBOT_SHARE))
                    self.assertIn('Lift column, share of the robot mass, on wheels', column[0].computed)

    def test_the_wheeled_template(self):
        shared = self.apart.constants['all']
        self.assertEqual(shared['Joint modules, share of the robot mass, on wheels'][1], (0.078, 0.156, 0.234))
        self.assertEqual(shared['Battery energy per kg of robot, on wheels'][1], (4.62, 10.28, 22.86))
        # Since E14 (E14.6 point 2) seven of them take every joint from their makers, the G2 and the RealBots their arms.
        template = [r for r in ON_WHEELS if r not in OWN_ON_WHEELS and r not in E14_OWN and r not in E14_ARMS_ONLY
                    and r != 'RealMan Dual-Arm Lift']
        first = {(j.name, j.share) for j in self.joints(template[0]) if j.share is not None}
        groups: dict = {}
        for name, share in first:
            groups[name.split(',')[0]] = groups.get(name.split(',')[0], 0) + share
            self.assertIn("type 2's four robots on wheels", name)
        self.assertAlmostEqual(sum(groups.values()), 1, places=9)
        for group, share in {'Waist joints': 0.205, 'Shoulder joints': 0.383, 'Elbow and wrist joints': 0.336,
                             'Head joints': 0.076}.items():
            self.assertAlmostEqual(groups[group], share, delta=0.002, msg=group)
        for robot in template:
            self.assertEqual({(j.name, j.share) for j in self.joints(robot) if j.share is not None}, first, msg=robot)

    def test_the_robots_with_every_joint(self):
        for robot, modules in OWN_ON_WHEELS.items():
            body = [j for j in self.joints(robot) if not j.name.startswith(OUTSIDE_THE_BODY)]
            with self.subTest(robot=robot):
                self.assertTrue(all(j.share is None for j in self.joints(robot)))
                self.assertAlmostEqual(sum(j.count * j.module_mass[1] for j in body), modules, delta=0.01)

    def test_the_batteries(self):
        for robot, (*_x, wh) in ON_WHEELS.items():
            own = self.apart.constants[robot]
            with self.subTest(robot=robot):
                if wh is None:
                    self.assertNotIn('Battery voltage', own)
                else:
                    self.assertAlmostEqual(own['Battery voltage'][1][1] * own['Battery capacity'][1][1], wh, places=0)
                packs = [p for p in self.apart.parts if p.robot == robot and p.kind == 'Battery pack']
                self.assertEqual({p.region for p in packs}, {'Base'})
        reachy = [p for p in self.apart.parts if p.robot == 'Pollen Robotics Reachy 2' and p.name == 'Battery pack']
        self.assertEqual(reachy[0].bounds, (6.175, 6.5, 6.825))   # the 2021 base's "6.5kg", ± 5 %

    def test_encoders_count_each_hand_and_wheel(self):
        # Two encoders per joint, its hands or grippers one each, as batch 1's (template()): the AgiBot G1's "20 DoF", two
        # hands and two drive wheels; the Honda Avatar's 22 body joints, two hands and two wheels; the CASBOT W1's 17
        # body joints, two grippers, two drive wheels and its lift.
        for robot, joints in (('AgiBot G1', 20 + 2 + 2), ('Honda Avatar', 22 + 2 + 2), ('CASBOT W1', 17 + 2 + 2 + 1)):
            encoders = [p for p in self.apart.parts if p.robot == robot and p.name == 'Encoders (two per joint)']
            self.assertEqual(encoders[0].count, 2 * joints, msg=robot)

    def test_lfp_cells_for_the_casbot_w1_only(self):
        cells = {p.robot: p.grade for p in self.apart.parts if p.name == 'Battery cells'}
        self.assertEqual({r for r, g in cells.items() if g}, {'CASBOT W1'})
        self.assertEqual(cells['CASBOT W1'], 'LFP cylindrical')
        # Its rows say how 02 draws them (Matthias, 2026-10-30, "Ratio, as recommended", E9.8): its cells over a cell of
        # their recipe; its housing, as an NMC pack's in proportion to its cells, since 2026-11-02 a share of its cells
        # as every pack no source weighs ("A, as recommended", E20); every other robot's cells over the NMC cell's.
        rows = {(p.robot, p.name): p.computed for p in self.apart.parts}
        self.assertIn('a cell of its recipe', rows[('CASBOT W1', 'Battery cells')])
        self.assertTrue(rows[('CASBOT W1', 'Battery housing, busbars and wires')].startswith(schemas.CELLS_SHARE))
        others = {(robot, name): text for (robot, name), text in rows.items() if robot != 'CASBOT W1'}
        self.assertTrue(all("NMC cell's Wh/kg" in text for (_, name), text in others.items() if name == 'Battery cells'))
        self.assertFalse(any('pack-to-cell' in text for text in rows.values()))

    def test_no_kind_torso_boards_left(self):
        for which in (builder, builder_two):
            apart, _ = written(which)
            kinds = {p.kind for p in apart.parts + apart.boards + apart.sensors}
            self.assertNotIn('Torso boards', kinds)
            self.assertIn('Boards', kinds)

    def test_every_joint_goes_to_a_kind(self):
        for j in self.apart.joints:
            self.assertIn(j.name.split()[0].lower(), schemas.JOINT_KIND, msg=f'{j.robot}, {j.name}')


# Types 3 and 4's builders (Matthias, 2026-10-30, "Yes, build it": EVIDENCE.md E11.7, open points A to C as
# recommended): batch 1's 27 robots, each in the file of its first type among 3 and 4.
builder_three = load('make_parts_taken_apart_3', os.path.join('tools', '3_industrial_logistics_warehousing',
                                                             'make_parts_taken_apart.py'))
builder_four = load('make_parts_taken_apart_4', os.path.join('tools', '4_service_healthcare_interaction',
                                                            'make_parts_taken_apart.py'))
TYPE_THREE_BATCH_1 = {
    'NEURA 4NE1 Gen 3': (79, 80, 81), 'NEURA 4NE1 Gen 3.5': (79, 80, 81), 'NEURA 4NE1 Gen 4': (63, 64, 65),
    'AgiBot A2 Max': (84, 85, 86), 'PNDbotics Adam Lite': (58.48, 60, 61), 'PNDbotics Adam SP': (60.25, 62, 63),
    'Hexagon AEON': (59, 60, 61), 'Agile Robots Agile One': (68, 69, 70), 'AIDOL Lab AIDOL': (94, 95, 96),
    'AeiROBOT ALICE M1': (96, 97, 98), 'TeknTrash ALPHA': (89, 90, 91), 'AI² Robotics AlphaBot 2': (134, 135, 136),
    'Anigon': (119, 120, 121), 'Apptronik Apollo': (71, 72, 73), 'Apptronik Apollo 2': (74, 75, 76),
    'Boston Dynamics Atlas': (89, 90, 91), 'NEUBILITY Billi': (109, 110, 111), 'Borg Robotics Borg 01': (61, 62, 63),
    'Wandercraft CALVIN-40': (79, 80, 81)}
TYPE_FOUR_BATCH_1 = {
    '1X NEO': (28.9, 29.9, 30.9), 'AgiBot A2': (68, 69, 70), 'AgiBot A3 Ultra': (59, 60, 61),
    'Andromeda Abi': (49, 50, 51), 'AgiBot A3': (54, 55, 56), 'AgiBot X2': (34, 35, 36),
    'AgiBot X2 Ultra': (38, 39, 40), 'DOBOT Atom 153 cm': (57.91, 58.91, 61.81), 'Vbot ATOM': (49, 50, 51)}
TYPES_34_ON_WHEELS = {'Andromeda Abi', 'AeiROBOT ALICE M1', 'AI² Robotics AlphaBot 2', 'Anigon', 'NEUBILITY Billi'}
# Batch 2 (E12.5 agreed, "Yes, agree E12.5"; E12.6, "Yes, build it"): each robot in the file of its first type among 3
# and 4, in the register's order; its mass as E12.5's table (the makers' ± 1 kg; the internet's; the sources' spread).
TYPE_THREE_BATCH_2 = {
    'Elite Robots Centaur-G1': (85, 260, 261), 'Donut Cinnamon 1': (69, 70, 71),
    'UBTECH Cruzr S2': (149, 150, 151), 'UBTECH Cruzr Y1': (89, 90, 91),
    'CYBORG RO1 SE': (74, 75, 76), 'CYBORG RO1 PRO': (79, 80, 81),
    'CYBORG WO1': (169, 170, 171), 'Sharpa D01': (57.5, 75, 92.5),
    'Richtech Robotics Dex': (59, 60, 61), 'BOSHIAC DexBot': (57, 58, 80), 'Agility Digit': (62.5, 63.5, 76),
    'Agility Digit 5': (128, 129, 130), 'DEEP Robotics DR02': (67, 68, 69),
    'DEEP Robotics DR02 Pro': (77, 78, 79), 'Duatic Alpha': (89, 90, 91), 'Siasun DUCO': (90, 100, 110),
    'Addverb Elixis': (74, 75, 76), 'Addverb Elixis-W': (209, 210, 211), 'Genesis AI Eno': (119, 120, 121),
    'AVIC Fengxing-001': (79, 80, 81)}
TYPE_FOUR_BATCH_2 = {
    'CASBOT 02': (49, 50, 51), 'CASBOT 02 EDU': (51, 52, 53), 'CasiVision CASIVIBOT': (54, 55, 56),
    'LG CLOiD': (60, 65, 70), 'XYZ DEUX': (59, 60, 61), 'Noetix Dora': (19, 20, 21), 'Realbotix F-Series': (49, 50, 51),
    'FF Futurist': (68, 69, 70), 'FF Master Classic Edu': (34, 35, 36),
    'FF Master Classic Ultra': (38, 39, 40)}
TYPES_34_ON_WHEELS_2 = {'Elite Robots Centaur-G1', 'UBTECH Cruzr S2', 'UBTECH Cruzr Y1', 'CYBORG WO1',
                        'Sharpa D01', 'Richtech Robotics Dex', 'Duatic Alpha', 'Siasun DUCO', 'Addverb Elixis-W',
                        'Genesis AI Eno', 'CasiVision CASIVIBOT', 'LG CLOiD', 'XYZ DEUX', 'Realbotix F-Series'}
TYPES_34_LIFTS_2 = {'UBTECH Cruzr S2', 'UBTECH Cruzr Y1', 'Siasun DUCO', 'Genesis AI Eno', 'XYZ DEUX'}
# Joints from a stated joint (E12.5 point 2): the block, its stated torque (N·m), and the joint it is (on legs the knee,
# on wheels the waist).
FROM_A_STATED_JOINT = {'CASBOT 02': (150, 'Knee'), 'CASBOT 02 EDU': (150, 'Knee'),
                       'CYBORG RO1 SE': (400, 'Knee'), 'CYBORG RO1 PRO': (400, 'Knee'),
                       'CYBORG WO1': (562, 'Waist'), 'FF Futurist': (270, 'Knee'),
                       'FF Master Classic Edu': (120, 'Knee'),
                       'FF Master Classic Ultra': (120, 'Knee')}
# The ratios by program from the robots with every joint (E12.5 point 2, corrected in E12.7: on legs over the knee the
# elbow 0.17; on wheels the second waist joint the median of the Vega's 0.54 and the RB-Y1's 1.00), to two decimals.
LEG_RATIOS = {'Hip pitch': 1.00, 'Hip roll': 1.00, 'Hip yaw': 0.25, 'Knee': 1.00, 'Ankle pitch': 0.33,
              'Ankle roll': 0.24, 'Waist': 0.36, 'Shoulder': 0.27, 'Elbow': 0.17, 'Wrist': 0.08, 'Head': 0.08}
WHEEL_RATIOS = {'Waist': 1.00, 'Second waist': 0.77, 'Shoulder': 0.24, 'Elbow': 0.13, 'Wrist': 0.04, 'Head': 0.06}


class TestTypesThreeAndFour(unittest.TestCase):
    """Types 3 and 4's batch 1 entered (E11.6 agreed, "Yes, agree E11.6"; E11.7, "Yes, build it")."""

    @classmethod
    def setUpClass(cls):
        cls.three, _ = written(builder_three)
        cls.four, _ = written(builder_four)

    def test_each_robot_in_the_file_of_its_first_type_among_3_and_4(self):
        # Since types 5 and 6's entry (E16.6): batch 3's robots of types 5 and 6 whose first type among 3 and 4 is 3;
        # since batch 3 (E15.7) every robot of it, E16.6's three in their places of the register's order.
        self.assertEqual(list(self.three.robots), list(TYPE_THREE_BATCH_1) + list(TYPE_THREE_BATCH_2)
                         + TYPE_THREE_ORDER_3)
        self.assertEqual(list(self.four.robots), list(TYPE_FOUR_BATCH_1) + list(TYPE_FOUR_BATCH_2)
                         + list(TYPE_FOUR_BATCH_3))
        self.assertEqual({r.type for r in self.three.robots.values()}, {3})
        self.assertEqual({r.type for r in self.four.robots.values()}, {4})
        self.assertFalse(set(self.three.robots) & set(self.four.robots))
        two, _ = written(builder_two)
        self.assertFalse((set(self.three.robots) | set(self.four.robots))
                         & (set(two.robots) | set(written()[0].robots)))

    def test_what_they_write_passes_every_check_of_01(self):
        lists = schemas.read_shared_lists(absolute(Params().data.shared_lists))
        for apart in (self.three, self.four):
            self.assertEqual([f.text for f in schemas.check_parts_taken_apart(apart, lists, Params())], [])

    def test_the_masses_as_decided(self):
        for apart, masses in ((self.three, {**TYPE_THREE_BATCH_1, **TYPE_THREE_BATCH_2}),
                              (self.four, {**TYPE_FOUR_BATCH_1, **TYPE_FOUR_BATCH_2})):
            for robot, mass in masses.items():
                self.assertEqual(apart.constants[robot]['Robot mass, with battery'][1], mass, msg=robot)
        self.assertEqual(self.three.constants['NEURA 4NE1 Gen 4']['Robot mass, with battery'][3], 'S, E')

    def test_their_templates_under_names_of_their_own(self):
        for apart in (self.three, self.four):
            shared = apart.constants['all']
            self.assertEqual(shared['Joint modules, share of the robot mass, types 3 and 4'][1],
                             (0.2235, 0.447, 0.6705))
            self.assertEqual(shared['Joint modules, share of the robot mass, types 3 and 4, on wheels'][1],
                             (0.0695, 0.139, 0.2085))
            self.assertEqual(shared['Battery energy per kg of robot, types 3 and 4'][1], (7.335, 14.67, 22.005))
            self.assertEqual(shared['Battery energy per kg of robot, types 3 and 4, on wheels'][1],
                             (5.42, 10.84, 16.26))
            self.assertNotIn('Joint modules, share of the robot mass', shared)
        # The median of the seven robots on legs, at the modes, is the template's mode (E11.6 point 1).
        module = sys.modules[builder_three.SHARED.__name__]
        from statistics import median
        shares = [sum(j[1] * j[4][1] for j in module.body(b)) / b['mass'][0][1] for b in module.SEVEN]
        self.assertAlmostEqual(median(shares), 0.447, delta=0.0005)

    def test_the_adam_by_its_actuators_and_the_atom_as_type_twos(self):
        knee = [j for j in self.three.joints if j.robot == 'PNDbotics Adam Lite' and j.name == 'Knee']
        self.assertEqual(knee[0].module_mass, (3.8, 4.0, 4.2))
        shoulder = [j for j in self.three.joints if j.robot == 'PNDbotics Adam Lite' and j.name == 'Shoulder pitch']
        self.assertAlmostEqual(shoulder[0].module_mass[1], 0.0689 * 60 ** 0.566, places=3)
        mine = [(j.name, j.count, j.torque) for j in self.four.joints if j.robot == 'DOBOT Atom 153 cm']
        two, _ = written(builder_two)
        self.assertEqual(mine, [(j.name, j.count, j.torque) for j in two.joints if j.robot == 'DOBOT Atom'])

    def test_the_batteries(self):
        def wh(apart, robot):
            own = apart.constants[robot]
            return own['Battery voltage'][1][1] * own['Battery capacity'][1][1]
        for apart, robot, energy in ((self.four, '1X NEO', 842), (self.four, 'AgiBot A2', 700),
                                     (self.four, 'AgiBot A3', 1152), (self.four, 'AgiBot A3 Ultra', 1152),
                                     (self.four, 'AgiBot X2', 500), (self.three, 'PNDbotics Adam Lite', 1172),
                                     (self.three, 'AI² Robotics AlphaBot 2', 1440)):
            self.assertAlmostEqual(wh(apart, robot), energy, delta=1, msg=robot)
        self.assertNotIn('Battery voltage', self.three.constants['Boston Dynamics Atlas'])

    def test_on_wheels_and_the_magnesium_frames(self):
        both = {**{n: self.three for n in self.three.robots}, **{n: self.four for n in self.four.robots}}
        wheeled = {n for n, a in both.items() if schemas.on_wheels(a, n)}
        self.assertEqual(wheeled, TYPES_34_ON_WHEELS | TYPES_34_ON_WHEELS_2 | TYPES_34_ON_WHEELS_3)   # batch 3: E15.7
        self.assertTrue(any(p.robot == 'Anigon' and p.kind == 'Lift column' for p in self.three.parts))
        frames = {p.robot: p.material for p in self.four.parts if p.name == 'Frame'}
        self.assertEqual((frames['AgiBot A3'], frames['AgiBot A3 Ultra']), ('Magnesium alloys', 'Magnesium alloys'))


def template_spans(constants: dict) -> list:
    """E13 rule 1: the shared quantities that are a share of a robot's mass or an energy per kg of it (the templates,
    resting on its mass) whose min is above half their mode or whose max below 1.5 times it."""
    narrow = []
    for quantity, (_, (low, mode, high), *_) in constants.items():
        if ('share of the robot mass' in quantity or 'per kg of robot' in quantity) and mode:
            if low > 0.5 * mode + 1e-9 or high < 1.5 * mode - 1e-9:
                narrow.append(quantity)
    return narrow


class TestTemplatesWiderThanData(unittest.TestCase):
    """E13 rule 1 (Matthias, 2026-11-01, "Yes, agree E13"): a template, a robot's part estimated from its mass, spans at
    least half to 1.5 times its mode in every parts file, so that it is never narrower than a robot's own data."""

    def test_every_template_of_every_parts_file_spans_half_to_one_and_a_half(self):
        for builder in (None, builder_two, builder_three, builder_four):
            apart = written(builder)[0] if builder else written()[0]
            self.assertEqual(template_spans(apart.constants['all']), [], msg=apart.source)

    def test_a_narrowed_template_is_caught(self):
        apart = written(builder_three)[0]
        narrowed = dict(apart.constants['all'])
        name = 'Battery energy per kg of robot, types 3 and 4'
        row = narrowed[name]
        narrowed[name] = (row[0], (10.0, 14.67, 20.0)) + tuple(row[2:])
        self.assertEqual(template_spans(narrowed), [name])


class TestTypesThreeAndFourBatchTwo(unittest.TestCase):
    """Types 3 and 4's batch 2 entered (E12.5 agreed; E12.6, "Yes, build it"): joints from a stated joint, the stated
    batteries by their chemistry, the robots on wheels and their lifts; the Clone Alpha and the PrimeBOT Q1 listed only
    (E12.4, "A stated mass")."""

    @classmethod
    def setUpClass(cls):
        cls.three, _ = written(builder_three)
        cls.four, _ = written(builder_four)
        cls.both = {**{n: cls.three for n in cls.three.robots}, **{n: cls.four for n in cls.four.robots}}
        cls.module = sys.modules[builder_three.SHARED.__name__]

    def test_the_ratios_from_the_robots_with_every_joint(self):
        for ratios, expected in ((self.module.LEG_RATIOS, LEG_RATIOS), (self.module.WHEEL_RATIOS, WHEEL_RATIOS)):
            self.assertEqual(set(ratios), set(expected))
            for kind, value in expected.items():
                low, mid, high = ratios[kind]
                self.assertAlmostEqual(mid, value, delta=0.005, msg=kind)
                self.assertLessEqual(low, mid, msg=kind)
                self.assertLessEqual(mid, high, msg=kind)

    def test_joints_from_a_stated_joint(self):
        fit = lambda t: 0.0689 * t ** 0.566  # noqa: E731   (E6.8's fit, kg at a torque)
        for robot, (torque, kind) in FROM_A_STATED_JOINT.items():
            body = [j for j in self.both[robot].joints if j.robot == robot
                    and not j.name.startswith(('Hand', 'Gripper', 'Wheel', 'Steering', 'Lift'))]
            self.assertTrue(body, msg=robot)
            self.assertTrue(all(j.share is None for j in body), msg=robot)             # not the template
            self.assertEqual(max(j.torque for j in body), torque, msg=robot)
            stated = next(j for j in body if j.name == kind)
            self.assertAlmostEqual(stated.module_mass[1], fit(torque), places=3, msg=robot)
            for j in body:   # each module half to 1.5 times the fit at its kind's least and most ratio, or wider
                self.assertLessEqual(j.module_mass[0], 0.5 * fit(j.torque) + 1e-3, msg=(robot, j.name))
                self.assertGreaterEqual(j.module_mass[2], 1.5 * fit(j.torque) - 1e-3, msg=(robot, j.name))
        hip_yaw = next(j for j in self.four.joints if j.robot == 'CASBOT 02' and j.name == 'Hip yaw')
        self.assertAlmostEqual(hip_yaw.torque, 150 * LEG_RATIOS['Hip yaw'], delta=1)
        # The Dora's second-hand 120 N·m not used: the template (E12.5 point 2).
        self.assertTrue(any(j.share is not None for j in self.four.joints if j.robot == 'Noetix Dora'))

    def test_the_hands_and_the_batteries(self):
        hand = next(j for j in self.three.joints
                    if j.robot == 'CYBORG WO1' and j.name.startswith('Hand'))
        self.assertEqual((hand.count, hand.module_mass), (2, (0.7125, 0.75, 0.7875)))      # "重量 750g", ± 5 % (S)

        def wh(robot):
            own = self.both[robot].constants[robot]
            return own['Battery voltage'][1][1] * own['Battery capacity'][1][1]
        for robot, energy in (('CASBOT 02', 480), ('Elite Robots Centaur-G1', 1920),
                              ('CYBORG RO1 SE', 888), ('CYBORG RO1 PRO', 1608),
                              ('XYZ DEUX', 1440), ('DEEP Robotics DR02', 1440), ('DEEP Robotics DR02 Pro', 1440),
                              ('FF Futurist', 690)):
            self.assertAlmostEqual(wh(robot), energy, delta=1, msg=robot)
        self.assertNotIn('Battery voltage', self.three.constants['CYBORG WO1'])   # a runtime only

    def test_on_wheels_and_their_lifts(self):
        lifts = {p.robot for a in (self.three, self.four) for p in a.parts if p.kind == 'Lift column'}
        self.assertEqual(lifts & set(TYPE_THREE_BATCH_2) | lifts & set(TYPE_FOUR_BATCH_2), TYPES_34_LIFTS_2)
        steering = [j for j in self.four.joints if j.robot == 'XYZ DEUX' and j.name == 'Steering motor']
        self.assertEqual(steering[0].count, 2)

    def test_the_robots_listed_only_have_no_rows(self):
        one, _ = written()
        self.assertNotIn('PrimeBOT Q1', one.robots)
        for apart in (one, written(builder_two)[0], self.three, self.four):
            self.assertFalse([r for r in apart.robots if 'Clone Alpha' in r], msg=apart.source)


def type_one_rule(torque: float) -> tuple:
    """Type 1's module at a torque: the torque over 87.3 N·m/kg, half to 1.5 times (EVIDENCE.md E5.12 point 4)."""
    return tuple(round(f * torque / 87.3, 4) for f in (0.5, 1, 1.5))


# E14.6 (Matthias, 2026-11-01: "Yes, agree E14", "Yes, build it"): each robot's body joints as its maker's model file
# gives them (EVIDENCE.md E14.1, read first-hand: V123, V130), in order, (name, count, torque N·m); its modules by its
# type's rule (type 1's, else type 2's fit). The X2's arms the first five of the X2 files' seven, the R1-A5-D's upper
# body the R1-A5's, the REEM-C's legs v0, the ARI's fifth arm joint (its datasheet's wrist, not in the model) at its
# elbow's 5 N·m (E). Its hands, grippers, wheels, steering and lift as entered before.
X2_LEGS_WAIST = [('Hip pitch', 2, 120), ('Hip roll', 2, 120), ('Hip yaw', 2, 120), ('Knee', 2, 120),
                 ('Ankle pitch', 2, 60), ('Ankle roll', 2, 36), ('Waist yaw', 1, 120), ('Waist pitch', 1, 36),
                 ('Waist roll', 1, 36)]
A3_BODY = [('Waist yaw', 1, 220), ('Waist roll', 1, 46), ('Waist pitch', 1, 118), ('Head yaw', 1, 6),
           ('Head pitch', 1, 6), ('Shoulder pitch', 2, 60), ('Shoulder roll', 2, 60), ('Shoulder yaw', 2, 24),
           ('Elbow', 2, 24), ('Wrist roll', 2, 24), ('Wrist pitch', 2, 6), ('Wrist yaw', 2, 6), ('Hip pitch', 2, 220),
           ('Hip roll', 2, 220), ('Hip yaw', 2, 220), ('Knee', 2, 320), ('Ankle pitch', 2, 118.2),
           ('Ankle roll', 2, 54.75)]
H2X_BODY = [('Hip pitch', 2, 220), ('Hip roll', 2, 248.18), ('Hip yaw', 2, 248.18), ('Knee', 2, 248.18),
            ('Ankle pitch', 2, 100), ('Ankle roll', 2, 100), ('Waist yaw', 1, 111), ('Waist roll', 1, 180),
            ('Waist pitch', 1, 180), ('Head pitch', 1, 24.8), ('Head yaw', 1, 24.8), ('Shoulder pitch', 2, 111),
            ('Shoulder roll', 2, 53.7), ('Shoulder yaw', 2, 53.7), ('Elbow', 2, 53.7), ('Wrist roll', 2, 53.7),
            ('Wrist pitch', 2, 24.8), ('Wrist yaw', 2, 24.8)]
R1_UPPER = [('Waist yaw', 1, 60), ('Shoulder pitch', 2, 60), ('Shoulder roll', 2, 60), ('Shoulder yaw', 2, 33),
            ('Elbow', 2, 33), ('Wrist roll', 2, 33)]
E14_OWN = {
    # The Booster T2 by type 2's fit (Matthias, 2026-11-01, "Yes, agree": type 1's rule put 71 % of its mass in its
    # joints and its frame below zero in 4.1 % of its draws; E14.7 point 6).
    'Booster T2': (2, [('Head yaw', 1, 22), ('Head pitch', 1, 22), ('Shoulder pitch', 2, 74), ('Shoulder roll', 2, 60),
                       ('Elbow pitch', 2, 60), ('Elbow yaw', 2, 60), ('Wrist pitch', 2, 22), ('Wrist yaw', 2, 22),
                       ('Wrist roll', 2, 22), ('Waist pitch', 1, 138), ('Waist roll', 1, 144), ('Waist yaw', 1, 135),
                       ('Hip pitch', 2, 135), ('Hip roll', 2, 135), ('Hip yaw', 2, 135), ('Knee', 2, 135),
                       ('Ankle pitch', 2, 132), ('Ankle roll', 2, 72)]),
    'Unitree H2-X Core i7': (2, H2X_BODY), 'Unitree H2-X Orin NX': (2, H2X_BODY),
    'Unitree H2-D Flagship': (2, [('Waist pitch', 1, 200), ('Shoulder pitch', 2, 130), ('Shoulder roll', 2, 60),
                                  ('Shoulder yaw', 2, 60), ('Elbow', 2, 60), ('Wrist roll', 2, 60),
                                  ('Wrist pitch', 2, 10), ('Wrist yaw', 2, 10), ('Head pitch', 1, 50),
                                  ('Head yaw', 1, 50)]),
    'Unitree G1-D Ultimate': (2, [('Waist yaw', 1, 80), ('Waist pitch', 1, 30), ('Shoulder pitch', 2, 25),
                                  ('Shoulder roll', 2, 25), ('Shoulder yaw', 2, 25), ('Elbow', 2, 25),
                                  ('Wrist roll', 2, 25), ('Wrist pitch', 2, 5), ('Wrist yaw', 2, 5)]),
    'Unitree R1-A7-D': (2, R1_UPPER + [('Wrist pitch', 2, 10), ('Wrist yaw', 2, 10), ('Head pitch', 1, 33),
                                       ('Head yaw', 1, 0.86)]),
    'Unitree R1-A5-D': (2, R1_UPPER + [('Head pitch', 1, 33), ('Head yaw', 1, 0.86)]),
    'Galaxea R1 Pro': (2, [('Waist 1', 1, 100), ('Waist 2', 1, 100), ('Waist 3', 1, 100), ('Waist 4', 1, 100),
                           ('Shoulder 1', 2, 55), ('Shoulder 2', 2, 55), ('Shoulder 3', 2, 25), ('Elbow', 2, 25),
                           ('Wrist 1', 2, 18), ('Wrist 2', 2, 18), ('Wrist 3', 2, 18)]),
    'X-Humanoid Tien Kung 3.0': (2, [('Hip pitch', 2, 235), ('Hip roll', 2, 235), ('Hip yaw', 2, 150),
                                     ('Knee', 2, 400), ('Ankle pitch', 2, 55), ('Ankle roll', 2, 55),
                                     ('Waist yaw', 1, 200), ('Waist roll', 1, 150), ('Waist pitch', 1, 150),
                                     ('Head yaw', 1, 6.3), ('Head pitch', 1, 6.3), ('Shoulder pitch', 2, 90),
                                     ('Shoulder roll', 2, 90), ('Shoulder yaw', 2, 50), ('Elbow pitch', 2, 50),
                                     ('Elbow yaw', 2, 40), ('Wrist pitch', 2, 40), ('Wrist roll', 2, 40)]),
    'LimX Oli': (2, [('Hip pitch', 2, 140), ('Hip roll', 2, 140), ('Hip yaw', 2, 140), ('Knee', 2, 140),
                     ('Ankle pitch', 2, 42), ('Ankle roll', 2, 42), ('Waist yaw', 1, 42), ('Waist roll', 1, 42),
                     ('Waist pitch', 1, 42), ('Shoulder pitch', 2, 42), ('Shoulder roll', 2, 42),
                     ('Shoulder yaw', 2, 42), ('Elbow', 2, 42), ('Wrist yaw', 2, 19), ('Wrist pitch', 2, 19),
                     ('Wrist roll', 2, 19), ('Head yaw', 1, 19), ('Head pitch', 1, 19)]),
    'PAL REEM-C': (2, [('Hip yaw', 2, 42.7), ('Hip roll', 2, 64), ('Hip pitch', 2, 55.7), ('Knee', 2, 138.3),
                       ('Ankle pitch', 2, 80.9), ('Ankle roll', 2, 64), ('Waist 1', 1, 78), ('Waist 2', 1, 78),
                       ('Shoulder 1', 2, 44.64), ('Shoulder 2', 2, 22.32), ('Shoulder 3', 2, 17.86),
                       ('Elbow', 2, 17.86), ('Wrist 1', 2, 3), ('Wrist 2', 2, 6.6), ('Wrist 3', 2, 6.6),
                       ('Head 1', 1, 3.4), ('Head 2', 1, 3.26)]),
    'PAL TIAGo Pro': (2, [('Shoulder 1', 2, 43), ('Shoulder 2', 2, 43), ('Shoulder 3', 2, 26), ('Elbow', 2, 26),
                          ('Wrist 1', 2, 26), ('Wrist 2', 2, 26), ('Wrist 3', 2, 26), ('Head 1', 1, 5.197),
                          ('Head 2', 1, 2.77)]),
    'PAL ARI': (2, [('Shoulder 1', 2, 10), ('Shoulder 2', 2, 10), ('Shoulder 3', 2, 5), ('Elbow', 2, 5),
                    ('Wrist', 2, 5), ('Head 1', 1, 3.4), ('Head 2', 1, 3.26)]),
    'AgiBot X2 Ultra': (2, X2_LEGS_WAIST + [('Head yaw', 1, 3.13), ('Head pitch', 1, 2), ('Shoulder pitch', 2, 60),
                                            ('Shoulder roll', 2, 60), ('Shoulder yaw', 2, 36), ('Elbow', 2, 36),
                                            ('Wrist yaw', 2, 36), ('Wrist pitch', 2, 6), ('Wrist roll', 2, 6)]),
    'AgiBot X2': (2, X2_LEGS_WAIST + [('Shoulder pitch', 2, 60), ('Shoulder roll', 2, 60), ('Shoulder yaw', 2, 36),
                                      ('Elbow', 2, 36), ('Wrist yaw', 2, 36)]),
    'AgiBot A3': (2, A3_BODY), 'AgiBot A3 Ultra': (2, A3_BODY),
}
# RealMan's own modules (E14.5 point A; RMs page 5: "1040", "750", "425" g at 60, 30, 10 N·m), ± 5 % (S).
WHJ60, WHJ30, WHJ10_N = (tuple(round(f * kg, 4) for f in (0.95, 1, 1.05)) for kg in (1.04, 0.75, 0.425))
RM65_ARM = [('Shoulder 1', 2, 60, WHJ60), ('Shoulder 2', 2, 60, WHJ60), ('Elbow', 2, 30, WHJ30),
            ('Wrist 1', 2, 10, WHJ10_N), ('Wrist 2', 2, 10, WHJ10_N), ('Wrist 3', 2, 10, WHJ10_N)]
RM75_ARM = [('Shoulder 1', 2, 60, WHJ60), ('Shoulder 2', 2, 60, WHJ60), ('Shoulder 3', 2, 30, WHJ30),
            ('Elbow', 2, 30, WHJ30), ('Wrist 1', 2, 10, WHJ10_N), ('Wrist 2', 2, 10, WHJ10_N),
            ('Wrist 3', 2, 10, WHJ10_N)]
# Robots whose arms only are now their maker's; their other body joints stay on the template (E14.2, E14.5 point A).
E14_ARMS_ONLY = {'AgiBot G2': [(n, c, t, fitted(t)) for n, c, t in
                               (('Shoulder 1', 2, 108), ('Shoulder 2', 2, 108), ('Shoulder 3', 2, 35), ('Elbow', 2, 35),
                                ('Wrist 1', 2, 35), ('Wrist 2', 2, 18), ('Wrist 3', 2, 18))],
                 'RealMan RealBot-01': RM75_ARM, 'RealMan RealBot-L2': RM75_ARM, 'RealMan RealBot-S2': RM75_ARM}


class TestE14Entry(unittest.TestCase):
    """E14's entry (Matthias, 2026-11-01: "Yes, start research", "Yes, agree E14", "download what ever is possibel",
    "Yes, build it"): the robots on the joint template whose makers publish their joints, each joint as its maker's
    model or page; RealMan's arms by RealMan's own modules; THEMIS's mass and battery from its brochure."""

    NOT_BODY = ('Hand', 'Gripper', 'Wheel', 'Steering', 'Lift')

    @classmethod
    def setUpClass(cls):
        cls.files = {1: written(builder)[0], 2: written(builder_two)[0], 3: written(builder_three)[0],
                     4: written(builder_four)[0]}

    def joints(self, robot: str) -> list:
        apart = next(a for a in self.files.values() if robot in a.robots)
        return [j for j in apart.joints if j.robot == robot]

    def constants(self, robot: str) -> dict:
        return next(a for a in self.files.values() if robot in a.robots).constants[robot]

    def test_every_joint_from_its_makers_file(self):
        for robot, (rule, expected) in E14_OWN.items():
            body = [j for j in self.joints(robot) if not j.name.startswith(self.NOT_BODY)]
            self.assertEqual([(j.name, j.count, j.torque) for j in body], expected, msg=robot)
            self.assertTrue(all(j.share is None for j in self.joints(robot)), msg=robot)   # off the template
            for j in body:
                self.assertEqual(j.module_mass, type_one_rule(j.torque) if rule == 1 else fitted(j.torque),
                                 msg=(robot, j.name))

    def test_realmans_arms_by_its_own_modules(self):
        body = [j for j in self.joints('RealMan Dual-Arm Lift') if not j.name.startswith(self.NOT_BODY)]
        self.assertEqual([(j.name, j.count, j.torque, j.module_mass) for j in body], RM65_ARM)
        self.assertTrue(all(j.share is None for j in self.joints('RealMan Dual-Arm Lift')))

    def test_the_arms_alone_and_the_rest_on_the_template(self):
        for robot, arms in E14_ARMS_ONLY.items():
            rows = self.joints(robot)
            stated = [(j.name, j.count, j.torque, j.module_mass) for j in rows if j.share is None
                      and not j.name.startswith(self.NOT_BODY)]
            self.assertEqual(stated, arms, msg=robot)
            self.assertTrue(any(j.share is not None for j in rows), msg=robot)                # its other joints
            self.assertFalse(any(j.share is not None and j.name.startswith(('Shoulder', 'Elbow and wrist'))
                                 for j in rows), msg=robot)

    def test_joints_from_a_stated_joint_by_type_1s_rule(self):
        for robot, torque, joints in (('Noetix Bumi', 70, 21), ('Noetix E1', 150, 26)):
            body = [j for j in self.joints(robot) if not j.name.startswith(self.NOT_BODY)]
            self.assertEqual(sum(j.count for j in body), joints, msg=robot)
            self.assertTrue(all(j.share is None for j in body), msg=robot)
            self.assertEqual(max(j.torque for j in body), torque, msg=robot)
            knee = next(j for j in body if j.name == 'Knee')
            self.assertEqual(knee.module_mass[1], round(torque / 87.3, 4), msg=robot)
        own = self.constants('Noetix Bumi')
        self.assertAlmostEqual(own['Battery voltage'][1][1] * own['Battery capacity'][1][1], 48 * 5.1, places=6)

    def test_the_agibot_a2_from_its_knee(self):
        body = [j for j in self.joints('AgiBot A2') if not j.name.startswith(self.NOT_BODY)]
        self.assertEqual(sum(j.count for j in body), 28)
        self.assertEqual(max(j.torque for j in body), 270)
        self.assertTrue(all(j.share is None for j in self.joints('AgiBot A2')))

    def test_themis_from_its_brochure(self):
        own = self.constants('Westwood THEMIS')
        self.assertEqual(own['Robot mass, with battery'][1], (35.5, 36.5, 37.92))
        self.assertAlmostEqual(own['Battery voltage'][1][1] * own['Battery capacity'][1][1], 518.4, places=6)
        boards = [b.name for b in self.files[2].boards if b.robot == 'Westwood THEMIS']
        self.assertTrue(any('Ryzen' in b for b in boards), boards)
        self.assertEqual(sum(1 for b in boards if b.startswith('Compute module, NVIDIA Jetson Orin NX')), 1)
        self.assertEqual(next(b.count for b in self.files[2].boards if b.robot == 'Westwood THEMIS'
                              and b.name.startswith('Compute module, NVIDIA Jetson Orin NX')), 2)


# --- Types 5 and 6 (EVIDENCE.md E16.6; Matthias, 2026-11-01: "Yes, agree both", "Find all the data for 5 and 6 and
# then fill in the data in the respective sheets") ---------------------------------------------------------------------
builder_five = load('make_parts_taken_apart_5', os.path.join('tools', '5_heavy_duty_high_performance_hazardous_'
                                                            'environment', 'make_parts_taken_apart.py'))
builder_six = load('make_parts_taken_apart_6', os.path.join('tools', '6_defense_public_safety',
                                                           'make_parts_taken_apart.py'))


def stated(mode: float) -> tuple:
    """A mass stated once, ± 5 %, to four decimals."""
    return tuple(round(f * mode, 4) for f in (0.95, 1, 1.05))


# EngineAI's T800 (its developer documents 05/05, 05/02; its model files' efforts): each joint its stated motor.
T800_BODY = [('Hip pitch', 2, 415, stated(2.6)), ('Hip roll', 2, 370, stated(2.1)), ('Hip yaw', 2, 222, stated(1.65)),
             ('Knee', 2, 415, stated(2.6)), ('Ankle pitch', 2, 160, stated(0.95)), ('Ankle roll', 2, 160, stated(0.95)),
             ('Waist yaw', 1, 222, stated(1.65)), ('Shoulder pitch', 2, 160, stated(0.95)),
             ('Shoulder roll', 2, 160, stated(0.95)), ('Shoulder yaw', 2, 160, stated(0.95)),
             ('Elbow pitch', 2, 160, stated(0.95)), ('Elbow yaw', 2, 52, stated(0.5)), ('Head pitch', 1, 52, stated(0.5)),
             ('Head yaw', 1, 52, stated(0.5))]
T800_PRO_WRISTS = [('Wrist pitch', 2, 5, fitted(5)), ('Wrist roll', 2, 5, fitted(5))]
# DEEP Robotics' model files (DR02-pro.urdf, DR02-std.urdf): every joint's effort, its module the fit.
DR02_LEGS = [('Hip pitch', 2, 363), ('Hip roll', 2, 363), ('Hip yaw', 2, 137), ('Knee', 2, 363), ('Ankle pitch', 2, 137),
             ('Ankle roll', 2, 50)]
DR02_PRO_BODY = DR02_LEGS + [('Waist pitch', 1, 363), ('Waist yaw', 1, 137), ('Waist roll', 1, 137),
                             ('Shoulder pitch', 2, 137), ('Shoulder roll', 2, 137), ('Shoulder yaw', 2, 137),
                             ('Elbow', 2, 137), ('Wrist yaw', 2, 50), ('Wrist pitch', 2, 50), ('Wrist roll', 2, 50),
                             ('Head yaw', 1, 50), ('Head pitch', 1, 50)]
DR02_BODY = DR02_LEGS + [('Waist yaw', 1, 137), ('Shoulder pitch', 2, 137), ('Shoulder roll', 2, 137),
                         ('Shoulder yaw', 2, 137), ('Elbow', 2, 137)]
# Alex's arms as Nadia's cycloidal arm actuators (IHMC, arXiv 2409.04639 Fig. 4; E16.5 question 1), the fit.
ALEX_ARMS = [('Shoulder pitch', 2, 158, fitted(158)), ('Shoulder roll', 2, 158, fitted(158)),
             ('Shoulder yaw', 2, 79, fitted(79)), ('Elbow', 2, 79, fitted(79)), ('Wrist yaw', 2, 19, fitted(19)),
             ('Wrist pitch', 2, 19, fitted(19)), ('Wrist roll', 2, 19, fitted(19))]


class TestTypesFiveAndSix(unittest.TestCase):
    """Types 5 and 6's entry (E16.6): their own robots in their own files, the DR02 from its model files, the Atlas with
    its 13-DoF hands and its Jetson Thor, and the Kaleido 9, the Moby and the Phantom MK1 in type 3's file (E15)."""

    NOT_BODY = ('Hand', 'Gripper', 'Wheel', 'Steering', 'Lift')

    @classmethod
    def setUpClass(cls):
        cls.files = {3: written(builder_three)[0], 5: written(builder_five)[0], 6: written(builder_six)[0]}

    def apart(self, robot: str):
        return next(a for a in self.files.values() if robot in a.robots)

    def joints(self, robot: str) -> list:
        return [j for j in self.apart(robot).joints if j.robot == robot]

    def body(self, robot: str) -> list:
        return [j for j in self.joints(robot) if not j.name.startswith(self.NOT_BODY)]

    def parts(self, robot: str) -> dict:
        return {p.name: p for p in self.apart(robot).parts if p.robot == robot}

    def mass(self, robot: str) -> tuple:
        return self.apart(robot).constants[robot]['Robot mass, with battery'][1]

    def test_each_file_holds_its_own_robots(self):
        # Since E27.7 (2026-11-04) the hydraulic Atlas (old) and Nadia, each in two versions (TestHydraulicRobots).
        self.assertEqual(set(self.files[5].robots), {'EngineAI T800 Dev', 'EngineAI T800 PRO', 'Mirsee MH3', *ATLAS_OLD})
        self.assertEqual(set(self.files[6].robots), {'IHMC Alex', 'NORINCO Fuxi on legs', 'NORINCO Fuxi on wheels',
                                                     *NADIA})
        for name in ('Kawasaki Kaleido 9', 'Noble Machines Moby', 'Foundation Phantom MK1'):
            self.assertIn(name, self.files[3].robots)
        names = {n for t in (3, 5, 6) for n in REGISTER.TAKEN_APART[t].values() for n in schemas.versions(n)}
        self.assertTrue(set(self.files[5].robots) | set(self.files[6].robots) <= names)

    def test_the_t800_every_joint_its_stated_motor(self):
        self.assertEqual([(j.name, j.count, j.torque, j.module_mass) for j in self.body('EngineAI T800 Dev')],
                         T800_BODY)
        self.assertEqual([(j.name, j.count, j.torque, j.module_mass) for j in self.body('EngineAI T800 PRO')],
                         T800_BODY + T800_PRO_WRISTS)
        self.assertTrue(all(j.share is None for name in ('EngineAI T800 Dev', 'EngineAI T800 PRO')
                            for j in self.joints(name)))
        hands = [j for j in self.joints('EngineAI T800 PRO') if j.name.startswith('Hand')]
        self.assertEqual([(j.count, j.module_mass) for j in hands], [(2, stated(0.74))])
        self.assertFalse([j for j in self.joints('EngineAI T800 Dev') if j.name.startswith('Hand')])
        self.assertEqual(self.mass('EngineAI T800 Dev'), (83.5, 84.5, 85.5))
        self.assertEqual(self.mass('EngineAI T800 PRO'), (84.3, 85.3, 86.3))
        for name in ('EngineAI T800 Dev', 'EngineAI T800 PRO'):
            own = self.apart(name).constants[name]
            self.assertAlmostEqual(own['Battery voltage'][1][1] * own['Battery capacity'][1][1], 61.2 * 20, places=6)
            self.assertEqual(self.parts(name)['Battery pack'].bounds, stated(7.2))

    def test_the_dr02_from_its_model_files(self):
        for name, expected in (('DEEP Robotics DR02', DR02_BODY), ('DEEP Robotics DR02 Pro', DR02_PRO_BODY)):
            self.assertEqual([(j.name, j.count, j.torque) for j in self.body(name)], expected, msg=name)
            self.assertTrue(all(j.share is None for j in self.joints(name)), msg=name)
            self.assertTrue(all(j.module_mass == fitted(j.torque) for j in self.body(name)), msg=name)

    def test_alex_its_arms_as_nadias_the_rest_on_the_template(self):
        rows = self.joints('IHMC Alex')
        arms = [(j.name, j.count, j.torque, j.module_mass) for j in rows if j.share is None
                and not j.name.startswith(self.NOT_BODY)]
        self.assertEqual(arms, ALEX_ARMS)
        self.assertTrue(any(j.share is not None for j in rows))
        hands = [j for j in rows if j.name.startswith('Hand')]
        self.assertEqual([(j.count, j.module_mass) for j in hands], [(2, stated(0.49))])
        self.assertEqual(self.mass('IHMC Alex'), (84, 85, 86))

    def test_mh3_and_fuxi(self):
        self.assertEqual(self.mass('Mirsee MH3'), (124, 125, 126))
        wheels = [j for j in self.joints('Mirsee MH3') if j.name.startswith('Wheel')]
        self.assertEqual([j.count for j in wheels], [4])
        for name in ('NORINCO Fuxi on legs', 'NORINCO Fuxi on wheels'):
            self.assertEqual(self.mass(name), (84, 85, 86), msg=name)
        self.assertFalse([j for j in self.joints('NORINCO Fuxi on legs') if j.name.startswith('Wheel')])
        self.assertTrue([j for j in self.joints('NORINCO Fuxi on wheels') if j.name.startswith('Wheel')])

    def test_the_atlas_its_hands_and_its_thor(self):
        hands = [j for j in self.joints('Boston Dynamics Atlas') if j.name.startswith('Hand')]
        self.assertEqual([(j.name, j.count) for j in hands], [('Hand (13 joints)', 2)])
        boards = {b.name for b in self.apart('Boston Dynamics Atlas').boards if b.robot == 'Boston Dynamics Atlas'}
        self.assertIn('Compute module, NVIDIA Jetson AGX Thor', boards)

    def test_e15s_three_robots_of_types_5_and_6(self):
        self.assertEqual(self.mass('Noble Machines Moby'), (71, 72, 73))
        self.assertEqual(self.mass('Kawasaki Kaleido 9'), (98, 99, 100))
        self.assertEqual(self.parts('Kawasaki Kaleido 9')['Frame'].material, 'Magnesium alloys')
        phantom = self.parts('Foundation Phantom MK1')
        self.assertFalse([p for p in phantom if p.startswith('Battery')])     # "lacks a battery"
        body = {j.name: j.torque for j in self.body('Foundation Phantom MK1')}
        self.assertEqual((body['Knee'], body['Shoulder'], body['Wrist']), (160, 119, 20))

    def test_types_5_and_6_take_types_3_and_4s_templates(self):
        # Types 5 and 6 have no template of their own (E16.6): their files' robots take types 3 and 4's shared numbers.
        for name, quantity in (('NORINCO Fuxi on wheels', 'Battery energy per kg of robot, types 3 and 4, on wheels'),
                               ('NORINCO Fuxi on legs', 'Joint modules, share of the robot mass, types 3 and 4')):
            apart = self.apart(name)
            asked = quantity.split(', types')[0]
            self.assertEqual(schemas.template_quantity(apart, name, asked), quantity, msg=name)
            self.assertIn(quantity, apart.constants[schemas.ALL_ROBOTS])

    def test_01s_table_gives_a_robot_without_a_battery_none(self):
        # The Phantom MK1 "lacks a battery" (E16.2): 01's table of its type draws no battery bar and no battery cell.
        rows = {r.name: r for r in schemas.robots_table_rows(self.files[3])}
        self.assertIsNone(rows['Foundation Phantom MK1'].battery_wh)
        self.assertEqual(rows['Foundation Phantom MK1'].bases['Battery'], ())
        self.assertGreater(rows['Noble Machines Moby'].battery_wh, 0)

    def test_the_makers_own_numbers_count_as_the_makers(self):
        # IHMC's page gives the Alex's mass, EngineAI's documents the T800's: from the maker in 01's table.
        for t, name in ((6, 'IHMC Alex'), (5, 'EngineAI T800 Dev')):
            table = {r.name: r for r in schemas.robots_table_rows(self.files[t])}
            self.assertEqual(table[name].bases['Mass'], ('maker',), msg=name)


# --- Batch 3 of types 3 and 4 (EVIDENCE.md E15.7; Matthias, 2026-11-02: "E15's entry", "Yes, build it") ---------------
# Each block as E15.3's row: (mass (min, mode, max) kg, on wheels, hands, battery Wh). Hands: 0 none, 'G' two grippers,
# an int the joints of each of its two hands (Fourier's six-joint hand per joint), a float a stated hand's kg (each of
# two). Battery: its energy, voltage × capacity at the modes, or None for the template's (no voltage of its own). The
# seven robots of no stated form on legs and on wheels (E15.6 question 2), each the same row. In the register's order.
BOTH_FORMS = ('on legs', 'on wheels')
TYPE_THREE_BATCH_3 = {
    'Figure AI Figure 02': ((69, 70, 71), False, 16, 2250), 'Holiday Robotics Friday': ((114, 115, 116), True, 0.5, None),
    'AgiBot G2 Max': ((184, 185, 186), True, 0, None), 'Galbot G1': ((91.5, 92.5, 93.5), True, 'G', 1440),
    'Galbot ET1': ((31, 32, 33), False, 0, None), 'Galbot S1': ((319, 320, 321), True, 'G', 2880),
    'Persona AI Gen 1': ((69, 70, 85), False, 10, None), 'Generative Bionics GENE.01': ((60, 79.7, 80.7), False, 21, None),
    'Gento Luna': ((89, 90, 91), True, 'G', 1651.2), 'Geek+ Gino 1': ((62, 63, 64), True, 7, None),
    'GAC GoMate': ((44, 45, 46), True, 5, None), 'GAC GoMate Mini': ((59, 60, 61), True, 0, None),
    'Humanoid HMND 01 Bipedal': ((89, 90, 91), False, 'G', None),
    'Huashu HSR-ER-HR705': ((199, 200, 201), True, 'G', None), 'XPENG IRON 2025': ((69, 70, 90), False, 22, None),
    'JAKA K1': ((39, 40, 41), False, 0, None), 'JAKA Kargo': ((179, 180, 200), True, 0, None),
    'Zeroth Jupiter': ((57, 58, 60), False, 10, None), 'LG KAPEX': ((60, 65, 70), False, 0, None),
    'Galaxea Kengo': ((39, 40, 65), False, 6, None), 'Kinisi KR1': ((99, 100, 101), True, 'G', None),
    'Moon Dynamics L1': ((59, 60, 61), True, 'G', None), 'Glroad Laborer M1': ((85, 86, 87), False, 0, None),
    'MagicLab MagicBot X1': ((69, 70, 71), False, 0, None),
    'Matrix Robotics Matrix-1': ((66, 67, 68), False, 22, 2280), 'Mentee MenteeBot 2024': ((69, 70, 71), False, 0, None),
    'Mentee MenteeBot V3': ((65, 70, 71), False, 0, None), 'O-ID Modular': ((69, 70, 71), True, 'G', None),
    'Zhejiang Navigator 2': ((59, 60, 61), False, 0.6, None), 'Galaxea NEXO': ((78, 85, 86), True, 0, None),
    'Sharpa North': ((59, 60, 90), True, 22, None), 'ugo Nova': ((99, 100, 101), True, 'G', 1113.2),
    'Pink Robotics P0': ((81, 82, 83), False, 'G', None), 'PsiBot Psi V1': ((149, 150, 151), True, 0, None),
    'Pudu D9': ((64, 65, 66), False, 0.5, 720), 'XPENG PX5': ((108, 109, 110), False, 0.43, None),
    'X Square QUANTA X2': ((94, 95, 96), True, 20, None), 'AgiBot RAISE A1': ((54, 55, 56), False, 12, None),
    'NineRay RayNex G3': ((59, 60, 61), False, 6, None), 'RoboScience REX G1': ((79, 80, 81), True, 0, None),
    'Oversonic RoBee': ((179, 180, 293), True, 'G', None), 'Roboligent Robin': ((104, 105, 106), True, 'G', None),
    'Robo Robotics ROBO-T1': ((45, 50, 60), True, 'G', None), 'Ati Sherpa Mecha': ((179, 180, 181), True, 0, None),
    'EIR SkyWalker 2 on legs': ((54, 55, 56), False, 6, None), 'EIR SkyWalker 2 on wheels': ((54, 55, 56), True, 6, None),
    'Muks Spaceo Pro': ((59, 60, 61), True, 'G', 1152), 'Robotera Star1': ((62, 63, 64), False, 12, None),
    'WorkFar Syntro': ((107, 108, 109), True, 12, 1200),
    'PaXini Tora DoubleOne P': ((69, 70, 71), True, 18, 1214.01),
    'PaXini Tora DoubleOne X': ((72, 73, 74), True, 18, 1214.01), 'DexForce W1 Pro': ((109, 110, 111), True, 6, None),
    'Walden Robotics Walden': ((89, 90, 91), True, 'G', None), 'UBTECH Walker S2': ((69, 70, 71), False, 11, 2300),
    'PL-Universe Zeus 1': ((299, 300, 301), True, 0, 1920), 'Perceptyne PR-OMNI': ((119, 120, 121), True, 'G', 3000)}
TYPE_FOUR_BATCH_3 = {
    'Pudu FlashBot Arm': ((69, 70, 71), True, 6, None), 'Futuring 2 on legs': ((69, 70, 71), False, 'G', None),
    'Futuring 2 on wheels': ((69, 70, 71), True, 'G', None), 'Fourier GR-3': ((70, 71, 72), False, 6, 936),
    'Haier HIVA Haiwa': ((69, 70, 71), True, 6, None), 'Noetix Hobbs W1': ((74, 75, 76), True, 6, 828.8),
    'HONOR': ((79, 80, 81), False, 0, None), 'HONOR A1': ((39, 40, 41), False, 0, None),
    'XPENG IRON 2024': ((69, 70, 71), False, 15, None), 'Weave Isaac 1': ((39, 40, 45), True, 'G', None),
    'Jingchu Elf': ((69, 70, 80), True, 0, None), 'KinetixAI KAI on legs': ((69, 70, 71), False, 0.75, 1700),
    'KinetixAI KAI on wheels': ((69, 70, 71), True, 0.75, 1700), 'Keenon XMAN-R1': ((109, 110, 111), True, 0, None),
    'Knowin-X1': ((49, 50, 51), True, 0, None), 'Leju KUAVO 5-W': ((155, 156, 157), True, 6, None),
    'Leju Kuavo-my': ((44, 45, 46), False, 0, None), 'Glroad Laborer C1': ((37, 38, 39), False, 0, None),
    'HECbot Lumen H1': ((68, 69, 70), False, 6, 700), 'HECbot Lumen S1 on legs': ((34, 35, 36), False, 0, None),
    'HECbot Lumen S1 on wheels': ((34, 35, 36), True, 0, None), 'MagicLab MagicBot': ((54, 70, 71), False, 6, 1350),
    'MagicLab MagicBot Z1': ((39, 40, 41), False, 0, 555), 'GigaAI Maker H01': ((63, 64, 65), True, 7, None),
    'UniX Martian': ((39, 40, 41), False, 11, 432), 'Sunday MEMO': ((76.1, 77.1, 78.1), True, 4, None),
    'Enchanted Tools Mirokaï': ((26, 29, 30), True, 2, None), 'AiMOGA Mornine': ((65, 70, 71), False, 12, 700),
    'Noetix N2': ((29, 30, 31), False, 0, None), 'GENISOM NE01': ((39, 40, 41), False, 0, None),
    '1X NEO Beta': ((29, 30, 31), False, 0, None), '1X NEO Gamma': ((34, 35, 36), False, 0, None),
    'Lumos NIX': ((18, 25.41, 26.41), False, 0, 282), 'SwitchBot Onero H1': ((35, 68, 69), True, 0, None),
    'PrimeBOT T1': ((8, 8.5, 9), True, 0, None), 'PL-Universe ProWhite': ((399, 400, 401), True, 'G', 4000),
    'Pudu D7 2024': ((44, 45, 46), True, 0, 1000), 'Pudu D7 2026': ((139, 140, 141), True, 0, None),
    'Robot.com RNoid': ((89, 90, 91), True, 'G', None), 'Robbyant R1': ((109, 110, 111), True, 0, None),
    'ROBOTERA Q5': ((69, 70, 71), True, 11, None), 'EngineAI SA02 on legs': ((24, 25, 26), False, 0, None),
    'EngineAI SA02 on wheels': ((24, 25, 26), True, 0, None), 'Muks Spaceo M1': ((44, 45, 46), True, 'G', 1152),
    'StarBot Nova': ((30.8, 31.8, 32.8), True, 0, None), 'Sulu.be Steve on legs': ((99, 100, 140), False, 0, None),
    'Sulu.be Steve on wheels': ((99, 100, 140), True, 0, None), 'Syntheva Synthia': ((9.8, 10.9, 12.0), False, 0, None),
    'iHub TARA GEN1': ((74, 75, 76), True, 0, None), 'Tau Robotics Tau Humanoid': ((34, 35, 36), False, 'G', 421.2),
    'UBTECH U1 Pro male': ((41, 42, 43), False, 0, None), 'UBTECH U1 Pro female': ((34.2, 35.2, 36.2), False, 0, None),
    'Tuesday Labs Voxel': ((44, 45, 46), False, 'G', None), 'UBTECH Walker C': ((42, 43, 44), False, 0, 720),
    'UBTECH Walker C1': ((54, 55, 56), False, 0, None), 'UBTECH Walker S1': ((75, 76, 77), False, 6, None),
    'Yue Quan X-Bot': ((59, 60, 61), False, 0, None), 'BYD Xiao Di': ((57.5, 58.5, 59.5), False, 0, None),
    'Tencent Xiao Liu on legs': ((55, 70, 71), False, 0, None), 'Tencent Xiao Liu on wheels': ((55, 70, 71), True, 0, None),
    'Digit XiaQi': ((68, 69, 69), False, 0, 700), 'Leju XTRON KUAVO-MY': ((50, 55, 56), False, 0, None),
    'Yunmu YMBot C': ((74, 75, 76), False, 0, None), 'Yunmu YMBot H': ((74, 75, 76), True, 0, None),
    'Zerith H1': ((54, 55, 56), True, 0, None), 'Zerith Z1': ((32, 33, 34), False, 0, None)}
# Type 3's file in the register's order: batch 3 with E16.6's three in their places (E11.7 point 1).
TYPE_THREE_ORDER_3 = (list(TYPE_THREE_BATCH_3)[:18] + ['Kawasaki Kaleido 9'] + list(TYPE_THREE_BATCH_3)[18:27]
                      + ['Noble Machines Moby'] + list(TYPE_THREE_BATCH_3)[27:29]
                      + ['NeodraDynamics Neo1']                        # since E27.7, after the Navigator 2 (204)
                      + list(TYPE_THREE_BATCH_3)[29:33] + ['Foundation Phantom MK1'] + list(TYPE_THREE_BATCH_3)[33:])
TYPES_34_ON_WHEELS_3 = {n for d in (TYPE_THREE_BATCH_3, TYPE_FOUR_BATCH_3) for n, row in d.items() if row[1]}
# The 17 blocks with joints from a stated joint (E15.7 point 2): its torque (N·m), the joint it is, and E15.3's body
# joint modules at the modes (kg), batch3_plan.py's arithmetic (its ratios before E12.7's elbow 0.17 and second waist
# 0.77: within 5 %). The Spaceo Pro its shoulders' "66 Nm" as stated beside its waist's 90 (E15.3's 4.7 kg left them out).
FROM_A_STATED_JOINT_3 = {
    'Galaxea Kengo': (130, 'Knee', 16.1), 'Glroad Laborer C1': (150, 'Knee', 15.2),
    'Glroad Laborer M1': (430, 'Knee', 30.0), 'HECbot Lumen H1': (512, 'Knee', 33.7),
    'MagicLab MagicBot': (350, 'Knee', 29.3), 'MagicLab MagicBot X1': (350, 'Knee', 30.4),
    'MagicLab MagicBot Z1': (100, 'Knee', 12.8), 'UniX Martian': (150, 'Knee', 18.8), 'Noetix N2': (150, 'Knee', 13.5),
    'Pudu D9': (352, 'Knee', 29.4), 'AgiBot RAISE A1': (350, 'Knee', 26.4), 'Muks Spaceo M1': (15.7, 'Shoulder', 2.7),
    'Muks Spaceo Pro': (90, 'Waist', None), 'PaXini Tora DoubleOne P': (207, 'Waist', 11.4),
    'PaXini Tora DoubleOne X': (207, 'Waist', 11.4), 'UBTECH Walker S1': (250, 'Knee', 25.1),
    'Zerith Z1': (150, 'Knee', 15.2)}
# Every body joint from its maker's model file (E15.7 point 2, E14's way): (name, count, torque N·m), as read (V134).
GR3_BODY = [('Hip pitch', 2, 366), ('Hip roll', 2, 140.4), ('Hip yaw', 2, 140.4), ('Knee', 2, 366),
            ('Ankle pitch', 2, 59.4), ('Ankle roll', 2, 59.4), ('Waist yaw', 1, 140.4), ('Waist roll', 1, 108.6),
            ('Waist pitch', 1, 108.6), ('Head yaw', 1, 17.4), ('Head pitch', 1, 17.4), ('Shoulder pitch', 2, 74.4),
            ('Shoulder roll', 2, 74.4), ('Shoulder yaw', 2, 42.9), ('Elbow', 2, 42.9), ('Wrist yaw', 2, 42.9),
            ('Wrist pitch', 2, 17.4), ('Wrist roll', 2, 17.4)]
STAR1_BODY = [('Head yaw', 1, 35), ('Head pitch', 1, 35), ('Shoulder pitch', 2, 110), ('Shoulder roll', 2, 110),
              ('Shoulder yaw', 2, 110), ('Elbow pitch', 2, 110), ('Elbow yaw', 2, 35), ('Wrist pitch', 2, 35),
              ('Wrist roll', 2, 35), ('Waist pitch', 1, 220), ('Waist roll', 1, 220), ('Waist yaw', 1, 110),
              ('Hip roll', 2, 255), ('Hip yaw', 2, 100), ('Hip pitch', 2, 400), ('Knee', 2, 400),
              ('Ankle pitch', 2, 100), ('Ankle roll', 2, 100)]
# The seven of E15.4: no stated mass, listed only (E15.7 point 5).
LISTED_ONLY_3 = {124: 'HELIOS', 214: 'Northstar', 282: 'StarBot Flex', 292: 'TARS', 304: 'Tobi', 316: 'Vesoma 1',
                 345: 'Yogi'}


class TestTypesThreeAndFourBatchThree(unittest.TestCase):
    """Batch 3 of types 3 and 4 entered (E15.7; Matthias, 2026-11-02, "Yes, build it"): every block as E15.3's row, the
    17 from a stated joint, the GR-3 and the Star1 from their models, the Tau Humanoid with the Unitree G1's joints and
    battery, the stated batteries and computers, the seven of E15.4 listed only."""

    NOT_BODY = ('Hand', 'Gripper', 'Wheel', 'Steering', 'Lift')

    @classmethod
    def setUpClass(cls):
        cls.three, _ = written(builder_three)
        cls.four, _ = written(builder_four)
        cls.both = {**{n: cls.three for n in cls.three.robots}, **{n: cls.four for n in cls.four.robots}}

    def joints(self, robot: str) -> list:
        return [j for j in self.both[robot].joints if j.robot == robot]

    def body(self, robot: str) -> list:
        return [j for j in self.joints(robot) if not j.name.startswith(self.NOT_BODY)]

    def test_each_block_in_the_file_of_its_first_type(self):
        self.assertTrue(set(TYPE_THREE_BATCH_3) <= set(self.three.robots))
        self.assertTrue(set(TYPE_FOUR_BATCH_3) <= set(self.four.robots))
        self.assertEqual((len(TYPE_THREE_BATCH_3), len(TYPE_FOUR_BATCH_3)), (56, 66))

    def test_every_block_as_e15_3(self):
        for rows in (TYPE_THREE_BATCH_3, TYPE_FOUR_BATCH_3):
            for robot, (mass, wheels, hands, energy) in rows.items():
                apart, own = self.both[robot], self.both[robot].constants[robot]
                self.assertEqual(own['Robot mass, with battery'][1], mass, msg=robot)
                self.assertEqual(schemas.on_wheels(apart, robot), wheels, msg=robot)
                hand = [j for j in self.joints(robot) if j.name.startswith(('Hand', 'Gripper'))]
                if hands == 0:
                    self.assertEqual(hand, [], msg=robot)
                elif hands == 'G':
                    self.assertEqual([(j.name, j.count) for j in hand], [('Gripper', 2)], msg=robot)
                elif isinstance(hands, int):
                    self.assertEqual([(j.name, j.count, j.module_mass) for j in hand],
                                     [(f'Hand ({hands} joints)', 2, half_to_one_and_a_half(0.443 * hands / 6))],
                                     msg=robot)
                else:
                    self.assertEqual([(j.count, j.module_mass[1]) for j in hand], [(2, hands)], msg=robot)
                if energy is None:
                    self.assertNotIn('Battery voltage', own, msg=robot)
                else:
                    self.assertAlmostEqual(own['Battery voltage'][1][1] * own['Battery capacity'][1][1], energy,
                                           delta=0.5, msg=robot)

    def test_what_they_write_passes_every_check_of_01(self):
        lists = schemas.read_shared_lists(absolute(Params().data.shared_lists))
        for apart in (self.three, self.four):
            self.assertEqual([f.text for f in schemas.check_parts_taken_apart(apart, lists, Params())], [])

    def test_the_seventeen_from_a_stated_joint(self):
        for robot, (torque, kind, kg) in FROM_A_STATED_JOINT_3.items():
            body = self.body(robot)
            self.assertTrue(all(j.share is None for j in self.joints(robot)), msg=robot)   # off the template
            stated = next(j for j in body if j.name == kind)
            self.assertAlmostEqual(stated.torque, torque, places=2, msg=robot)
            self.assertAlmostEqual(stated.module_mass[1], fitted(torque)[1], places=3, msg=robot)
            total = sum(j.count * j.module_mass[1] for j in body)
            if kg is not None:
                self.assertAlmostEqual(total, kg, delta=0.05 * kg, msg=robot)
        pro = {j.name: j for j in self.body('Muks Spaceo Pro')}
        self.assertEqual((pro['Shoulder'].torque, pro['Shoulder'].module_mass), (66, fitted(66)))
        self.assertEqual(max(j.torque for j in self.body('Muks Spaceo M1')), 15.7)
        tora = {j.name: j.count for j in self.body('PaXini Tora DoubleOne P')}
        self.assertEqual(tora, {'Waist': 2, 'Waist 2': 2, 'Shoulder': 6, 'Elbow': 2, 'Wrist': 6, 'Head': 2})

    def test_the_gr3_and_the_star1_from_their_models(self):
        for robot, rows, kg in (('Fourier GR-3', GR3_BODY, 26.9), ('Robotera Star1', STAR1_BODY, 32.9)):
            body = self.body(robot)
            self.assertEqual([(j.name, j.count, j.torque) for j in body], rows, msg=robot)
            self.assertTrue(all(j.module_mass == fitted(j.torque) for j in body), msg=robot)
            self.assertAlmostEqual(sum(j.count * j.module_mass[1] for j in body), kg, delta=0.1, msg=robot)
            self.assertTrue(all(j.share is None for j in self.joints(robot)), msg=robot)

    def test_the_tau_humanoid_takes_the_unitree_g1s_joints_and_battery(self):
        one, _ = written()
        g1 = [(j.name, j.count, j.module, j.torque) for j in one.joints if j.robot == 'Unitree G1']
        tau = self.body('Tau Robotics Tau Humanoid')
        self.assertEqual([(j.name, j.count, j.module, j.torque) for j in tau], g1)
        self.assertTrue(all(None in j.module_mass for j in tau))                    # inside as the G1's, unscaled
        own = self.four.constants['Tau Robotics Tau Humanoid']
        self.assertEqual((own['Battery voltage'][1], own['Battery capacity'][1]),
                         ((46.8, 46.8, 46.8), (8.55, 9, 9.45)))
        pack = next(p for p in self.four.parts if p.robot == 'Tau Robotics Tau Humanoid' and p.name == 'Battery pack')
        self.assertEqual(pack.bounds, (2.25, 2.5, 2.75))

    def test_the_named_computers(self):
        boards = lambda robot: {b.name for b in self.both[robot].boards if b.robot == robot}  # noqa: E731
        for robot, names in (('Galbot G1', {'Compute module, NVIDIA Jetson AGX Orin'}),
                             ('Geek+ Gino 1', {'Compute module, NVIDIA Jetson AGX Thor'}),
                             ('Fourier GR-3', {'Computer board, AMD Ryzen 7 8845HS'}),
                             ('Humanoid HMND 01 Bipedal', {'Compute module, NVIDIA Jetson AGX Orin',
                                                                 'Computer board, Intel i9'}),
                             ('Noetix Hobbs W1', {'Compute module, Rockchip RK3588', 'Computer board, Intel J1900'}),
                             ('Glroad Laborer C1', {'Compute module, NVIDIA Jetson Orin NX'}),
                             ('Robot.com RNoid', {'Computer board, AMD Ryzen 5 7640HS',
                                                  'Compute module, NVIDIA Jetson AGX Orin'}),
                             ('UBTECH Walker C1', {'Compute module, NVIDIA Jetson AGX Thor'}),
                             ('Syntheva Synthia', {'Computer board, BCM2712'})):
            self.assertTrue(names <= boards(robot), msg=(robot, boards(robot)))
        mentee = [b for b in self.three.boards if b.robot == 'Mentee MenteeBot V3'
                  and b.name == 'Compute module, NVIDIA Jetson AGX Orin']
        self.assertEqual([b.count for b in mentee], [2])

    def test_lfp_cells_where_their_makers_say_so(self):
        for robot in ('Gento Luna', 'ugo Nova', 'Muks Spaceo M1', 'Muks Spaceo Pro'):
            cells = next(p for p in self.both[robot].parts if p.robot == robot and p.name == 'Battery cells')
            self.assertEqual(cells.grade, 'LFP cylindrical', msg=robot)

    def test_steered_wheels_and_lifts(self):
        steering = {j.robot: j.count for a in (self.three, self.four) for j in a.joints if j.name == 'Steering motor'}
        self.assertTrue({'AgiBot G2 Max': 4, 'Galbot S1': 4, 'PaXini Tora DoubleOne P': 4}.items() <= steering.items())
        lifts = {p.robot for a in (self.three, self.four) for p in a.parts if p.kind == 'Lift column'}
        self.assertTrue({'Galbot S1', 'JAKA Kargo', 'Weave Isaac 1', 'Sunday MEMO', 'PL-Universe ProWhite',
                         'RoboScience REX G1', 'Oversonic RoBee', 'Roboligent Robin', 'Ati Sherpa Mecha',
                         'Muks Spaceo Pro', 'PaXini Tora DoubleOne P', 'PaXini Tora DoubleOne X', 'PL-Universe Zeus 1',
                         'Perceptyne PR-OMNI'} <= lifts)

    def test_the_seven_listed_only_have_no_rows(self):
        for name in LISTED_ONLY_3.values():
            self.assertFalse([r for r in self.both if name in r], msg=name)
        self.assertTrue(set(LISTED_ONLY_3) <= set(REGISTER.NO_MASS_STATED))

    def test_no_source_row_from_a_robots_name(self):
        # A robot's name holding a source code ("Moon Dynamics L1", "Robo Robotics ROBO-T1") brings no row of that
        # code into the sheet Sources: only the codes its rows' texts cite.
        self.assertNotIn('L1', self.three.sources)
        self.assertNotIn('T1', self.three.sources)


# --- E19 (Matthias, 2026-11-02, "Yes, agree E19"): the one fixed list of materials, each name what it is --------------
E19_MATERIALS = ['Copper', 'Brass', 'Nickel', 'Aluminium alloys', 'Magnesium alloys', 'Titanium alloy', 'Steel',
                 'Stainless steel', 'Electrical steel', 'NdFeB magnets', 'Battery cells', 'Boards and components',
                 'Plastics', 'Fibre composites', 'Ceramics', 'Other', 'Not allocated']
# The grades that name a material of their own (E19 point 2): a stainless or electrical steel, brass, the nickel strip.
E19_GRADE_MATERIAL = {'17-4PH': 'Stainless steel', '440C': 'Stainless steel', 'Type 304': 'Stainless steel',
                      'M19': 'Electrical steel', 'M27': 'Electrical steel', 'M19 or M27': 'Electrical steel',
                      'Brass': 'Brass', 'Nickel strip': 'Nickel'}


class TestE19Materials(unittest.TestCase):
    """Every parts file names its materials from E19's one list, a stainless or electrical steel, brass and the nickel
    strip each under a material of its own (EVIDENCE.md E19 point 2)."""

    def test_every_file_names_its_materials_from_the_list(self):
        five = load('make_parts_taken_apart_5', os.path.join('tools', '5_heavy_duty_high_performance_hazardous_'
                                                            'environment', 'make_parts_taken_apart.py'))
        six = load('make_parts_taken_apart_6', os.path.join('tools', '6_defense_public_safety',
                                                           'make_parts_taken_apart.py'))
        for which in (None, builder_two, builder_three, builder_four, five, six):
            apart = written(which)[0] if which else written()[0]
            rows = ([(c.material, c.grade) for c in apart.joint_parts] + [(p.material, p.grade) for p in apart.parts]
                    + [(s.material, s.grade) for s in apart.shares])
            for material, grade in rows:
                if not material:
                    continue
                for one in schemas.alternatives(material):
                    self.assertIn(one, E19_MATERIALS, msg=(apart.source, material, grade))
                for g in schemas.alternatives(grade):
                    if g in E19_GRADE_MATERIAL:
                        self.assertEqual(material, E19_GRADE_MATERIAL[g], msg=(apart.source, grade))


class TestHousingShareOfCells(unittest.TestCase):
    """Matthias, 2026-11-02: "A, as recommended" (EVIDENCE.md E20): in every parts file a battery pack no source weighs
    is its cells, its management board and its housing, the housing a share of its cells by one shared row (0.207 /
    0.414 / 0.859: the median of the packs their makers weigh, the G1's, the PM01's and the T800's; half of it; the
    Reachy 2's), so that it never falls below zero; a weighed pack's housing stays the pack's remainder."""

    def test_every_file_holds_the_share_and_every_pack_not_weighed_takes_it(self):
        for which in (None, builder_two, builder_three, builder_four, builder_five, builder_six):
            apart = written(which)[0]
            with self.subTest(file=apart.source):
                self.assertEqual(apart.constants[schemas.ALL_ROBOTS][schemas.HOUSING_SHARE][1], (0.207, 0.414, 0.859))
                for pack in (p for p in apart.parts if p.name == 'Battery pack'):
                    housings = [p.computed for p in apart.parts if p.robot == pack.robot
                                and p.computed.startswith((schemas.PACK_REMAINDER, schemas.CELLS_SHARE))]
                    want = (f"{schemas.CELLS_SHARE}: Constants' {schemas.HOUSING_SHARE}" if None in pack.bounds
                            else schemas.PACK_REMAINDER)
                    for computed in housings:
                        self.assertTrue(computed.startswith(want), msg=(pack.robot, computed))

    def test_type_one_has_both(self):
        apart = written()[0]
        housing = {p.robot: p.computed for p in apart.parts if p.name == 'Battery housing, busbars and wires'}
        self.assertTrue(housing['Unitree G1'].startswith(schemas.PACK_REMAINDER))
        self.assertTrue(housing['Booster K1 2 Ah'].startswith(schemas.CELLS_SHARE))


# The hydraulic robots (EVIDENCE.md E27.7; Matthias, 2026-11-04, "Yes, agree E27.7", "Yes, build it"): each hydraulic
# joint an actuator in its place's row, its valve, board and sensors drawn and its body the remainder; the power unit,
# its manifold, oil and hoses the new kind "Hydraulics".
# Matthias, 2026-11-04, "Yes, knees only" (E27.8): the Atlas (old)'s 1.6 kg actuators at its knees only, as HyQReal's;
# "Yes, fix both" (V167): its names short enough for the robots table, the guide's "Atlas HD, or hydraulic".
ATLAS_OLD = ('Atlas HD ISA v2', 'Atlas HD ISA v5 knees')
NADIA = ('IHMC Nadia ISA v2', 'IHMC Nadia ISA v5')
NEO1 = 'NeodraDynamics Neo1'
ISA_KG = {'v2': 0.92, 'v5': 1.6}
# Point 4.2: Atlas (old)'s 28 by the seven template robots' joints by place (42, 14, 28, 16, 10, 90 of 200), the largest
# remainders; point 3.2: Nadia's 12 as IHMC names them; point 5.2: Neo1's 39 as 上海证券报 counts them.
ATLAS_PLACES = {'hips': 6, 'knees': 2, 'ankles': 4, 'waist': 2, 'head': 1, 'arms': 13}
NADIA_PLACES = {'hips': 4, 'knees': 2, 'ankles': 4, 'waist': 2}
NEO1_PLACES = {'arms': 22, 'hips': 6, 'knees': 2, 'ankles': 4, 'waist': 3, 'head': 2}


class TestHydraulicRobots(unittest.TestCase):
    """E27.7 points 1 to 7: the hydraulic Atlas (old) and Nadia in two versions each, their actuators as Moog's ISA,
    and Neo1, its digital hydraulic actuators, each in its file and in the register."""

    @classmethod
    def setUpClass(cls):
        cls.files = {3: written(builder_three)[0], 5: written(builder_five)[0], 6: written(builder_six)[0]}

    def apart(self, robot: str):
        return next(a for a in self.files.values() if robot in a.robots)

    def parts(self, robot: str) -> dict:
        return {p.name: p for p in self.apart(robot).parts if p.robot == robot}

    def own(self, robot: str) -> dict:
        return self.apart(robot).constants[robot]

    def shares(self, robot: str, item: str) -> dict:
        return {s.material: (s.grade, s.share, s.remainder) for s in self.apart(robot).shares if s.item == item}

    def test_the_register_takes_them_apart(self):
        self.assertEqual(REGISTER.TAKEN_APART[5][44], '; '.join(ATLAS_OLD))
        self.assertEqual(REGISTER.TAKEN_APART[6][202], '; '.join(NADIA))
        self.assertEqual(REGISTER.TAKEN_APART[3][208], NEO1)
        self.assertTrue(set(ATLAS_OLD) <= set(self.files[5].robots))
        self.assertTrue(set(NADIA) <= set(self.files[6].robots))
        self.assertIn(NEO1, self.files[3].robots)

    def test_every_file_passes_every_check_of_01(self):
        params = Params()
        lists_path, recipes_path = absolute(params.data.shared_lists), absolute(params.data.element_recipes)
        if not all(os.path.exists(p) for p in (lists_path, recipes_path)):
            self.skipTest('the shared lists or the element recipes are not on disk')
        lists, recipes = schemas.read_shared_lists(lists_path), schemas.read_element_recipes(recipes_path)
        for robot_type, apart in self.files.items():
            faults = (schemas.check_parts_taken_apart(apart, lists, params) + schemas.check_sibling_data(apart, params)
                      + schemas.check_grades(apart, recipes, params))
            self.assertEqual([f.text for f in faults], [], msg=robot_type)

    def test_moogs_actuators_of_atlas_old_and_nadia(self):
        # Points 2.1 to 2.5: the actuator as weighed ± 5 %, its valve 95 g ± 5 %, its board as the small joint's driver
        # board, a position and two pressure sensors, its body the remainder.
        for robots, places in ((ATLAS_OLD, ATLAS_PLACES), (NADIA, NADIA_PLACES)):
            for robot in robots:
                # The version of each place: Nadia's either all v2 or all v5; the Atlas (old)'s all v2, or the v5 at its
                # knees only and the v2 at its other places.
                at_knees = robot.endswith(' knees')
                parts = self.parts(robot)
                boards = {b.name: b for b in self.apart(robot).boards if b.robot == robot}
                sensors = {e.name: e for e in self.apart(robot).sensors if e.robot == robot}
                found = {name.rsplit(', ', 1)[1]: p.count for name, p in parts.items()
                         if name.startswith('Hydraulic actuators, ')}
                self.assertEqual(found, places, msg=robot)
                for place, count in places.items():
                    version = (('v5' if place == 'knees' else 'v2') if at_knees
                               else robot.rsplit(' ', 1)[1])
                    whole = parts[f'Hydraulic actuators, {place}']
                    self.assertEqual(whole.bounds, stated(ISA_KG[version]), msg=(robot, place))
                    self.assertTrue(whole.computed.startswith(schemas.ACTUATORS_WHOLE), msg=robot)
                    self.assertEqual((parts[f'Servo valves, {place}'].count, parts[f'Servo valves, {place}'].bounds),
                                     (count, stated(0.095)), msg=robot)
                    self.assertEqual((boards[f'Actuator boards, {place}'].count,
                                      boards[f'Actuator boards, {place}'].bounds), (count, (11.5, 22.9, 28.3)))
                    self.assertEqual(sensors[f'Actuator position sensors, {place}'].count, count)
                    self.assertEqual(sensors[f'Actuator pressure sensors, {place}'].count, 2 * count)
                    body = parts[f'Actuator bodies, rods and seals, {place}']
                    self.assertTrue(body.computed.startswith(schemas.ACTUATOR_REST), msg=robot)
                    self.assertEqual(body.count, count)
                    self.assertEqual(self.shares(robot, f'Servo valves, {place}'),
                                     {'Copper': ('', (0.05, 0.1, 0.15), False),
                                      'Other': ('', (0.1, 0.2, 0.3), False),
                                      'Aluminium alloys': ('', (0.025, 0.05, 0.075), False),
                                      'Stainless steel': ('17-4PH', (None, None, None), True)})
                    self.assertEqual(self.shares(robot, f'Actuator bodies, rods and seals, {place}'),
                                     {'Steel': ('C45', (0.06, 0.12, 0.18), False),
                                      'Plastics': ('', (0.005, 0.01, 0.015), False),
                                      'Titanium alloy': ('Ti-6Al-4V', (None, None, None), True)})

    def test_nadia(self):
        # Point 3: its mass, its electric arms as the Alex's and pelvis on the template, grippers, no battery, power unit
        # or computer, no plastics shell, its carbon-fibre frame and shell, hoses and oil.
        for robot in NADIA:
            self.assertEqual(self.own(robot)['Robot mass, with battery'][1], (99, 100, 101))
            joints = [j for j in self.apart(robot).joints if j.robot == robot]
            arms = [(j.name, j.count, j.torque, j.module_mass) for j in joints
                    if j.name.startswith(('Shoulder', 'Elbow', 'Wrist'))]
            self.assertEqual(arms, ALEX_ARMS)
            self.assertTrue(all(j.share is None for j in joints))   # module masses, no shares (01's rule)
            pelvis = {j.name: (j.count, j.module) for j in joints if j.name in ('Hip yaw', 'Waist yaw (spine)')}
            self.assertEqual(pelvis, {'Hip yaw': (2, 'large'), 'Waist yaw (spine)': (1, 'large')})
            for j in joints:
                if j.name in pelvis:   # the template's per joint at its mode, its own spread: half to 1.5 times
                    self.assertEqual(j.module_mass, half_to_one_and_a_half(j.module_mass[1]), msg=j.name)
            grippers = [(j.count, j.module_mass) for j in joints if j.name.startswith('Gripper')]
            self.assertEqual(grippers, [(2, stated(0.4))])
            parts = self.parts(robot)
            self.assertFalse([p for p in parts if p.startswith('Battery')], msg=robot)
            self.assertNotIn('Hydraulic power unit', parts)
            self.assertFalse([p for p in parts if p.startswith('Shell')], msg=robot)
            frame = [p for p in parts.values() if p.computed.startswith(schemas.ROBOT_REMAINDER)]
            self.assertEqual([(p.name, p.material) for p in frame],
                             [('Frame and shell: carbon-fibre exoskeleton', 'Fibre composites')])
            boards = {b.name for b in self.apart(robot).boards if b.robot == robot and b.kind == 'Boards'}
            self.assertEqual(boards, {'Power distribution board'})
            hoses = parts['Hydraulic hoses']
            self.assertEqual((hoses.bounds, hoses.material, hoses.kind), ((0.5, 1, 1.5), 'Plastics', 'Hydraulics'))
            self.assertEqual(self.own(robot)[schemas.OIL_VOLUME][1], (0.25, 0.5, 0.75))
            self.assertTrue(parts['Hydraulic oil'].computed.startswith(schemas.OIL_FROM))
            self.assertEqual(parts['Hydraulic oil'].material, 'Other')

    def test_atlas_old(self):
        # Point 4: its mass Boston Dynamics', no electric joint, its manifold, power unit, battery, frame of titanium and
        # aluminium, oil; its lines in its frame (no hoses apart).
        for robot in ATLAS_OLD:
            self.assertEqual(self.own(robot)['Robot mass, with battery'][1], (80, 81.6, 86.2))
            self.assertFalse([j for j in self.apart(robot).joints if j.robot == robot])
            parts = self.parts(robot)
            self.assertFalse([p for p in parts if p.startswith(('Encoders', 'XT30'))], msg=robot)
            manifold = parts['Hydraulic manifold']
            self.assertEqual((manifold.bounds, manifold.material, manifold.grade, manifold.kind),
                             ((1.05, 2.1, 3.15), 'Titanium alloy or Aluminium alloys', 'Ti-6Al-4V', 'Hydraulics'))
            unit = parts['Hydraulic power unit']
            self.assertEqual((unit.bounds, unit.material, unit.kind), ((2.5, 5, 12), '', 'Hydraulics'))
            self.assertEqual(self.shares(robot, 'Hydraulic power unit'),
                             {'Steel': ('42CrMo4', (0.1, 0.2, 0.3), False),
                              # its motor 11 % of it, 22, 39 and 25 % of the motor copper, electrical steel and magnets
                              # (E27.7 point 4.4, there rounded), half to 1.5 times
                              'Copper': ('', (0.0121, 0.0242, 0.0363), False),
                              'Electrical steel': ('M19 or M27', (0.02145, 0.0429, 0.06435), False),
                              'NdFeB magnets': ('SH', (0.01375, 0.0275, 0.04125), False),
                              'Titanium alloy or Aluminium alloys': ('Ti-6Al-4V', (None, None, None), True)})
            own = self.own(robot)
            # its capacity 1400 / 48 V to four decimals
            self.assertAlmostEqual(own['Battery voltage'][1][1] * own['Battery capacity'][1][1], 1400, delta=0.01)
            self.assertEqual(own[schemas.OIL_VOLUME][1], (1, 2, 4))
            self.assertNotIn('Hydraulic hoses', parts)
            frame = [p for p in parts.values() if p.computed.startswith(schemas.ROBOT_REMAINDER)]
            self.assertEqual([p.name for p in frame], ['Frame: titanium and aluminium'])
            self.assertEqual(self.shares(robot, 'Frame: titanium and aluminium'),
                             {'Titanium alloy': ('Ti-6Al-4V', (0.25, 0.5, 0.75), False),
                              'Aluminium alloys': ('', (None, None, None), True)})
            boards = {b.name: b.count for b in self.apart(robot).boards if b.robot == robot and b.kind == 'Boards'}
            self.assertEqual(boards, {'Computer board (not named)': 3, 'Power distribution board': 1})

    def test_neo1(self):
        # Point 5: its mass the maker's, its 39 digital hydraulic actuators by place, their insides as shares, its two
        # electric forearm joints, no battery or power unit, its steel frame, no sensors, hoses and oil.
        self.assertEqual(self.own(NEO1)['Robot mass, with battery'][1], (1199, 1200, 1201))
        parts = self.parts(NEO1)
        found = {name.rsplit(', ', 1)[1]: p.count for name, p in parts.items()
                 if name.startswith('Digital hydraulic actuators, ')}
        self.assertEqual(found, NEO1_PLACES)
        self.assertEqual(sum(found.values()), 39)
        for place in NEO1_PLACES:
            self.assertEqual(parts[f'Digital hydraulic actuators, {place}'].bounds, (1.0, 1.1, 1.65))
            self.assertEqual(self.shares(NEO1, f'Digital hydraulic actuators, {place}'),
                             {'Copper': ('', (0.022, 0.044, 0.066), False),
                              'Electrical steel': ('M19 or M27', (0.039, 0.078, 0.117), False),
                              'NdFeB magnets': ('H or SH', (0.025, 0.05, 0.075), False),
                              'Steel': ('C45', (0.15, 0.3, 0.45), False),
                              'Plastics': ('', (0.005, 0.01, 0.015), False),
                              'Titanium alloy': ('Ti-6Al-4V', (None, None, None), True)})
        joints = [(j.name, j.count, j.module, j.module_mass) for j in self.apart(NEO1).joints if j.robot == NEO1]
        self.assertEqual(joints, [('Elbow yaw (forearm rotation)', 2, 'large', (1.3, 2.6, 3.9))])
        self.assertFalse([p for p in parts if p.startswith('Battery')])
        self.assertNotIn('Hydraulic power unit', parts)
        frame = [p for p in parts.values() if p.computed.startswith(schemas.ROBOT_REMAINDER)]
        self.assertEqual([(p.material, p.grade) for p in frame], [('Steel', 'C45')])
        self.assertFalse([e for e in self.apart(NEO1).sensors if e.robot == NEO1 and e.kind != 'In the joints'])
        self.assertEqual(parts['Hydraulic hoses'].bounds, (4, 8, 12))
        self.assertEqual(self.own(NEO1)[schemas.OIL_VOLUME][1], (1, 2, 3))

    def test_the_oil_density_in_the_files_of_the_hydraulic_robots_only(self):
        for robot_type, apart in self.files.items():
            self.assertEqual(apart.constants[schemas.ALL_ROBOTS][schemas.OIL_DENSITY][1], (0.86, 0.87, 0.88),
                             msg=robot_type)
        for which in (None, builder_two, builder_four):
            apart = written(which)[0] if which else written()[0]
            self.assertNotIn(schemas.OIL_DENSITY, apart.constants[schemas.ALL_ROBOTS], msg=apart.source)

    def test_atlas_olds_places_by_the_seven(self):
        self.assertEqual(builder_three.SHARED.places_of(28), ATLAS_PLACES)

    def faults_of(self, apart) -> list:
        params = Params()
        lists_path = absolute(params.data.shared_lists)
        if not os.path.exists(lists_path):
            self.skipTest('the shared lists are not on disk')
        return [f.text for f in schemas.check_parts_taken_apart(apart, schemas.read_shared_lists(lists_path), params)]

    def test_01_faults_a_body_without_its_actuators(self):
        import dataclasses
        apart = self.files[6]
        parts = [p for p in apart.parts if not (p.robot == NADIA[0] and p.name == 'Hydraulic actuators, hips')]
        faults = self.faults_of(dataclasses.replace(apart, parts=parts))
        self.assertTrue(any('Actuator bodies, rods and seals, hips' in f and 'no row' in f for f in faults),
                        msg=faults)

    def test_01_faults_oil_without_its_volume(self):
        import dataclasses
        apart = self.files[6]
        constants = dict(apart.constants)
        constants[NADIA[0]] = {q: v for q, v in constants[NADIA[0]].items() if q != schemas.OIL_VOLUME}
        faults = self.faults_of(dataclasses.replace(apart, constants=constants))
        self.assertTrue(any(schemas.OIL_VOLUME in f for f in faults), msg=faults)

    def test_01_faults_an_actuator_whose_lightest_cannot_hold_its_valve_and_board(self):
        import dataclasses
        apart = self.files[6]
        parts = [dataclasses.replace(p, bounds=(0.1, 0.92, 0.966))
                 if p.robot == NADIA[0] and p.name == 'Hydraulic actuators, hips' else p for p in apart.parts]
        faults = self.faults_of(dataclasses.replace(apart, parts=parts))
        self.assertTrue(any('Hydraulic actuators, hips' in f and 'below zero' in f for f in faults), msg=faults)


class TestNoBatteryNoBatteryEstimate(unittest.TestCase):
    """Matthias, 2026-11-04, "Yes, fix it" (VERIFICATION.md V163): a robot that carries no battery (the Phantom MK1,
    Nadia, Neo1) rests on no estimate of its battery's energy; 02's notes pages listed it under "the battery's energy a
    share of the robot's mass" (type 5's said "the battery of 5" and named six)."""

    @classmethod
    def setUpClass(cls):
        cls.files = {3: written(builder_three)[0], 5: written(builder_five)[0], 6: written(builder_six)[0]}

    def apart(self, robot: str):
        return next(a for a in self.files.values() if robot in a.robots)

    def test_no_battery_no_battery_estimate(self):
        for robot in (*NADIA, NEO1, 'Foundation Phantom MK1'):
            self.assertFalse(schemas.has_battery(self.apart(robot), robot), msg=robot)
            self.assertNotIn('battery per kg', schemas.estimate_kinds(self.apart(robot), robot), msg=robot)

    def test_a_battery_from_the_energy_per_kg_still_listed(self):
        for robot in ('IHMC Alex', 'Kawasaki Kaleido 9', 'Mirsee MH3'):
            self.assertIn('battery per kg', schemas.estimate_kinds(self.apart(robot), robot), msg=robot)

    def test_the_kinds_of_joint_estimate(self):
        # Matthias, 2026-11-04, "Yes, do the package": an estimated body joint with a stated torque, "joint torques";
        # one without, "joint estimates"; 01's table of robots groups both as before (its group 'torques').
        self.assertEqual([k for k in schemas.estimate_kinds(self.apart(NEO1), NEO1) if k.startswith('joint')],
                         ['joint estimates'])
        for robot in NADIA:
            self.assertEqual([k for k in schemas.estimate_kinds(self.apart(robot), robot) if k.startswith('joint')],
                             ['joint torques', 'joint estimates'], msg=robot)
        self.assertEqual([k for k in schemas.estimate_kinds(self.apart('DEEP Robotics DR02'), 'DEEP Robotics DR02')
                          if k.startswith('joint')], ['joint torques'])
        groups = {r.name: r.group for a in self.files.values() for r in schemas.robots_table_rows(a)}
        for robot in (NEO1, *NADIA, 'DEEP Robotics DR02'):
            self.assertEqual(groups[robot], 'torques', msg=robot)


class TestRobotsTablesOfTheHydraulicRobots(unittest.TestCase):
    """Matthias, 2026-11-04, "Yes, fix both" (V166): in 01's tables of each type's robots no text lies over another (the
    Atlas (old)'s names ran over its height), and a hydraulic robot's joints count its hydraulic actuators (the Atlas
    (old) 28, not 0; Neo1 41, not 2; Nadia 31)."""

    @classmethod
    def setUpClass(cls):
        folders = {1: builder, 2: builder_two, 3: builder_three, 4: builder_four, 5: builder_five, 6: builder_six}
        cls.files = {n: written(b if n > 1 else None)[0] for n, b in folders.items()}
        params = Params()
        if not os.path.exists(absolute(params.data.humanoid_guide)):
            raise unittest.SkipTest('the catalogue is not on disk')
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, 'register.xlsx')
            REGISTER.build(path, params)
            cls.register = schemas.read_register(path)

    def test_no_text_over_text_in_any_robots_table(self):
        from matplotlib.text import Text
        for n in self.files:
            for k, figure in enumerate(schemas.robots_table_pages(schemas.type_parts(self.files, self.register, n), n)):
                figure.canvas.draw()
                renderer = figure.canvas.get_renderer()
                texts = [(t.get_text(), t.get_window_extent(renderer)) for t in figure.findobj(Text)
                         if t.get_text().strip()]
                for i, (one, a) in enumerate(texts):
                    for other, b in texts[i + 1:]:
                        over = (min(a.x1, b.x1) - max(a.x0, b.x0) > 1 and min(a.y1, b.y1) - max(a.y0, b.y0) > 1)
                        self.assertFalse(over, msg=(n, k + 1, one[:40], other[:40]))
                schemas.plt.close(figure)

    def test_a_hydraulic_robots_joints_count_its_actuators(self):
        joints = {r.name: r.joints for a in self.files.values() for r in schemas.robots_table_rows(a)}
        self.assertEqual({robot: joints[robot] for robot in ATLAS_OLD}, {robot: 28 for robot in ATLAS_OLD})
        self.assertEqual(joints[NEO1], 41)
        self.assertEqual({robot: joints[robot] for robot in NADIA}, {robot: 31 for robot in NADIA})
        self.assertEqual(joints['EngineAI T800 Dev'], 25)   # an electric robot as before
        # Written as whole numbers ("28", not "28.0": the sandbox's preview, V167).
        self.assertTrue(all(type(v) is int for v in joints.values()), msg=[k for k, v in joints.items() if type(v) is not int])



# --- The cameras of the robots whose parts named none (EVIDENCE.md E31; Matthias, 2026-11-05, "Yes, build 1 to 5",
# "Yes, those first", "Yes, A to H"). 144 robots of the six parts files listed no camera and no microphone; their makers'
# pages and, where those say nothing, third parties were searched twice. Point 1 and 2: the robots whose source states
# their cameras hold them as it states, each source read first-hand (VERIFICATION.md V181); point 3: those whose
# cameras no source counts an estimate, a row without a number and its drawn number 1 / 3 / 12 (E), and a microphone
# array of four where a source names a microphone or voice; point 4: the makers who sell the camera only as an option,
# none. The numbers below are the image sensors each robot holds (a camera one, a stereo camera two, a depth camera
# one colour and two infrared, as the D435's) and its microphones, counted by hand from E31's sources.
E31_STATED = {
    'Foundation Phantom MK1': (8, 0), 'PAL TALOS': (3, 0), 'PAL REEM-C': (3, 4), 'AgiBot A2': (6, 4),
    'DOBOT Atom': (4, 0), 'Keenon XMAN-R1': (16, 4), 'UBTECH U1 Pro male': (2, 6), 'UBTECH U1 Pro female': (2, 6),
    'Yunmu YMBot D': (3, 4), 'NEURA 4NE1 Gen 3': (7, 4), 'AIDOL Lab AIDOL': (4, 7), 'Mentee MenteeBot V3': (5, 4),
    'Apptronik Apollo': (1, 0), 'PrimeBOT T1': (1, 4), 'Agility Digit': (3, 0), 'Astribot S1': (14, 0),
    'Noetix Dora': (9, 6), 'JAKA Kargo': (2, 0), 'JAKA π': (1, 4), 'Spirit AI Moz1': (9, 0),
    'X-Humanoid Tien Kung 2.0': (9, 0), 'Tlibot Y1': (5, 4), 'Yunmu YMBot D4': (6, 4), 'Toyota CUE7': (3, 0)}
# Point 3, by the register's numbers; those whose sources name a microphone or voice (E31's table of point 3).
E31_ESTIMATED = [4, 5, 7, 9, 13, 19, 21, 23, 28, 31, 33, 41, 42, 43, 46, 51, 53, 56, 57, 58, 61, 63, 73, 74, 76, 78, 80, 83,
                 85, 86, 90, 93, 100, 101, 106, 110, 112, 114, 115, 125, 131, 132, 134, 136, 137, 139, 141, 146, 147, 150,
                 151, 154, 156, 164, 165, 167, 170, 175, 183, 184, 188, 189, 197, 199, 203, 204, 205, 206, 209, 210, 213,
                 221, 222, 223, 224, 226, 229, 230, 232, 238, 240, 242, 244, 246, 250, 258, 261, 263, 264, 272, 275, 276,
                 280, 281, 284, 285, 291, 293, 297, 298, 302, 308, 320, 330, 331, 333, 336, 337, 339, 341, 343, 344, 348,
                 351]
E31_MICROPHONES = [4, 5, 9, 33, 57, 74, 76, 85, 101, 114, 131, 132, 136, 137, 150, 175, 188, 189, 223, 224, 240, 244, 250,
                   261, 275, 291, 293, 330, 333, 339, 344]
# Point 4: none, as the maker states (the RB-Y1 "The vision camera is not provided.", the Adam Lite without head).
E31_NONE = [10, 251, 260, 268, 269, 307, 350]
IMAGE_SENSORS = ('CMOS image sensor', 'IR camera sensor')


def names_of(numbers: list) -> list:
    """The parts files' names of the register's robots `numbers`, every version once."""
    taken = {n: names for d in REGISTER.TAKEN_APART.values() for n, names in d.items()}
    return [name for n in numbers for name in schemas.versions(taken[n])]


class TestCamerasE31(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.files = [written(b)[0] for b in (builder, builder_two, builder_three, builder_four, builder_five,
                                             builder_six)]

    def apart(self, robot: str):
        return next(a for a in self.files if robot in a.robots)

    def held(self, robot: str, car_types) -> float:
        """How many units of `car_types` the robot's sensors hold (a sensor without a number not counted)."""
        apart = self.apart(robot)
        units = {}
        for _, sensor, car_type, n in apart.elements:
            units.setdefault(sensor, {})[car_type] = n
        return sum((s.count or 0) * units.get(s.name, {}).get(t, 0) for s in apart.sensors if s.robot == robot
                   for t in car_types)

    def test_the_144_robots_each_in_one_point(self):
        stated = set(E31_STATED)
        self.assertEqual(len(set(names_of(E31_ESTIMATED)) | set(names_of(E31_NONE)) | stated),
                         len(names_of(E31_ESTIMATED)) + len(names_of(E31_NONE)) + len(stated))
        self.assertEqual(len(E31_ESTIMATED) + len(E31_NONE) + len(stated) - 1, 144)   # the U1 Pro in two versions

    def test_points_1_and_2_the_cameras_and_microphones_as_their_sources_state(self):
        for robot, (sensors, microphones) in E31_STATED.items():
            self.assertEqual(self.held(robot, IMAGE_SENSORS), sensors, msg=robot)
            self.assertEqual(self.held(robot, ('MEMS microphone array',)), microphones, msg=robot)

    def test_point_3_a_drawn_number_of_cameras_and_a_microphone_array_where_named(self):
        for robot in names_of(E31_ESTIMATED):
            apart = self.apart(robot)
            rows = [s for s in apart.sensors if s.robot == robot and s.name == builder.ESTIMATED_CAMERAS]
            self.assertEqual([(s.count, s.kind, s.label) for s in rows], [(None, 'Head', 'E')], msg=robot)
            row, values, unit, label, _ = apart.constants[robot][schemas.NUMBER_OF + builder.ESTIMATED_CAMERAS]
            self.assertEqual((values, label), ((1, 3, 12), 'E'), msg=robot)
            self.assertEqual(self.held(robot, IMAGE_SENSORS), 0, msg=robot)   # none counted beside the drawn ones
        mics = set(names_of(E31_MICROPHONES))
        for robot in names_of(E31_ESTIMATED):
            self.assertEqual(self.held(robot, ('MEMS microphone array',)), 4 if robot in mics else 0, msg=robot)

    def test_point_4_no_camera(self):
        for robot in names_of(E31_NONE):
            self.assertEqual(self.held(robot, IMAGE_SENSORS), 0, msg=robot)
            self.assertFalse(any(s.robot == robot and s.name == builder.ESTIMATED_CAMERAS
                                 for s in self.apart(robot).sensors), msg=robot)

    def test_the_phantom_without_battery_its_source_the_bbc(self):
        apart = self.apart('Foundation Phantom MK1')
        self.assertFalse(any(p.robot == 'Foundation Phantom MK1' and p.kind == 'Battery pack' for p in apart.parts))
        self.assertIn('E31-BBC', apart.robots['Foundation Phantom MK1'].sources)
        self.assertNotIn('TBS', apart.sources)
        self.assertIn('bbc.com/news/articles/cedpxwe26l1o', apart.sources['E31-BBC'][2])

    def test_every_source_a_camera_cites_on_the_sheet_sources(self):
        for apart in self.files:
            for s in apart.sensors:
                for code in re.findall(r'E31-\w+', s.sources):
                    self.assertIn(code, apart.sources, msg=(s.robot, s.name))

    def test_the_number_prefix_is_01s(self):
        self.assertEqual(builder.NUMBER_OF, schemas.NUMBER_OF)

    def test_what_they_write_passes_every_check_of_01(self):
        lists = schemas.read_shared_lists(absolute(Params().data.shared_lists))
        for apart in self.files:
            self.assertEqual([f.text for f in schemas.check_parts_taken_apart(apart, lists, Params())], [])
