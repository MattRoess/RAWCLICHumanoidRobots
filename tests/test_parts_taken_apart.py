"""
Tests of 02_composition.py's robot type 1 part by part: its drawing over its robots, its element and material pages,
its two figures of where its critical elements sit and its figures of where each material sits (04_parts_taken_apart.py
until 2026-10-29: "Yes, into 02").

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

Matthias, 2026-10-28: "Yes, build steps 5 and 6: stage 04 and its two approved figures, tests first, tried in a
sandbox with few draws", with his answers A to E (documentation/claude/HANDOVER.md, 2026-10-28); then, the same day,
"Yes in 02 it is all type 1 in.!" and "Yes, code it in 02": the drawing moved to 02, over all the register's robots of
type 1; 2026-10-29, "Yes, build it": every robot of type 1 drawn from its own rows. The tests draw what the parts
file's builder writes (tools/1_compact_research_developer/make_parts_taken_apart.py, into a temporary folder) and the
sibling projects' files where they lie, a few hundred times, over the register's robots of type 1 and their versions
(the register's builder, tools/make_humanoid_register.py), into temporary folders: press Run, nothing in the project is
changed. Since 2026-10-30 also robot type 2, from its own builder's file. Where a file is not on disk, the test that
needs it is skipped and says so; where the inputs have a fault, it fails and names it.

The hand calculations draw every triangle at its mode (the test replaces 02's `triangle` by one that returns the mode)
and give the magnets fixed element fractions, so that one robot can be added up by hand from the data file's modes
(EVIDENCE.md E2.8, E2.8b, E5).
"""

import csv
import importlib.util
import os
import sys
import tempfile
import types
import unittest
from unittest import mock

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

from src.params_schema import Params, absolute  # noqa: E402


def load(name: str, file: str):
    """A stage of the project as a module (its name starts with a digit); only once, as the stages share 01 and 02."""
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, file))
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


composition = load('composition', '02_composition.py')
schemas = composition.schemas

# The parts file as its builder writes it, built once into a temporary folder for all the tests here; and the register's
# robots of type 1, every version of each, as the register's builder names them ("Taken apart as").
PARTS_BUILDER = load('make_parts_taken_apart', os.path.join('tools', '1_compact_research_developer',
                                                             'make_parts_taken_apart.py'))
REGISTER_BUILDER = load('make_humanoid_register', os.path.join('tools', 'make_humanoid_register.py'))
FOLDER = tempfile.TemporaryDirectory()
# In its type's folder, as 00's setting names it (data/researched/{folder}/parts_taken_apart.xlsx, since 2026-10-30).
PARTS_PATTERN = os.path.join(FOLDER.name, '{folder}', 'parts_taken_apart.xlsx')
PARTS_FILE = PARTS_PATTERN.format(folder='1_compact_research_developer')
PARTS_BUILDER.build(PARTS_FILE)
# Type 2's (2026-10-30, "Yes, build C"): its builder's file beside type 1's, in its own folder.
PARTS_BUILDER_TWO = load('make_parts_taken_apart_2', os.path.join('tools', '2_full_scale_general_purpose_ai_research',
                                                                 'make_parts_taken_apart.py'))
PARTS_BUILDER_TWO.build(PARTS_PATTERN.format(folder='2_full_scale_general_purpose_ai_research'))

# The magnets' element fractions the hand calculations use, the same for every grade class: neodymium 0.24,
# praseodymium 0.06, dysprosium 0.05, boron 0.01, iron the remainder.
FIXED_MAGNET = {'Nd': 0.24, 'Pr': 0.06, 'Dy': 0.05, 'B': 0.01, 'Fe': 0.64}


def inputs_or_skip(test: unittest.TestCase, params: Params):
    """02's inputs of robot type 1, from the parts file as its builder writes it, over the register's robots of type 1
    (each with its versions, its mass the parts file's, as its own); or the test skipped where a file is not on disk,
    failed where the inputs have a fault (01's checks and 02's)."""
    params.data.parts_taken_apart = PARTS_PATTERN
    files = [absolute(params.data.workbook), absolute(params.data.shared_lists), absolute(params.data.element_recipes),
             params.data.vehicle_pcb_composition, params.data.vehicle_sensor_composition,
             params.data.data_center_element_composition, params.data.traction_motor_steels]
    missing = [f for f in files if not os.path.exists(f)]
    if missing:
        test.skipTest(f'not on disk: {", ".join(missing)}')
    base = composition.read_inputs(params)
    parts = schemas.read_parts_taken_apart(PARTS_FILE)
    register = [schemas.RegisterRobot(row=0, number=number, name=names, maker='', types=(1,), types_text='1',
                                      mass=parts.constants[schemas.versions(names)[0]][composition.ROBOT_MASS][1],
                                      form='legs', entry='', taken_apart=names)
                for number, names in sorted(REGISTER_BUILDER.TAKEN_APART[1].items())]
    category = next(c for c in base.book.categories if c.number == 1)
    inputs = composition.read_apart_inputs(params, base, register, category)
    faults = composition.apart_faults(inputs, params)
    if faults:
        test.fail('faults in the inputs: ' + '; '.join(f'{f.sheet} {f.row}: {f.text}' for f in faults))
    return inputs


def draw(inputs, params: Params, magnets: dict):
    """Robot type 1 drawn by 02 over the register of `inputs`."""
    return composition.draw_taken_apart(inputs, params, magnets)


def fixed_magnets(inputs, n: int) -> dict:
    """FIXED_MAGNET for every grade class the joints use, in every draw."""
    names = list(FIXED_MAGNET)
    row = np.array([FIXED_MAGNET[e] for e in names])
    return {klass: (names, np.tile(row, (n, 1))) for klass in composition.grade_classes(inputs)}


def at_mode(rng, low, mode, high, n):
    """A triangle drawn at its mode in every draw (the varied mass: the robot's own)."""
    return np.broadcast_to(np.asarray(mode, dtype=float), (n,)).copy()


class TestDraws(unittest.TestCase):
    """Each draw one robot of the register's type 1, its mass, everything adding up; robot type 1 as 02 writes every
    robot type."""

    @classmethod
    def setUpClass(cls):
        cls.params = Params()
        cls.params.composition.draws = 3000

    def drawn(self):
        inputs = inputs_or_skip(self, self.params)
        return inputs, draw(inputs, self.params, fixed_magnets(inputs, self.params.composition.draws))

    def test_every_tenth_robot_is_said_as_it_is_drawn(self):
        # Matthias, 2026-10-30: "Information on the working of 02 is poor", "Yes, build them" (point 4): while a type
        # taken apart is drawn, every tenth robot of its parts file is said (the versions counted apart, as drawn).
        inputs = inputs_or_skip(self, self.params)
        said = []
        composition.draw_taken_apart(inputs, self.params, fixed_magnets(inputs, self.params.composition.draws),
                                     say=lambda done, of, name: said.append((done, of, name)))
        names = list(inputs.apart.robots)
        self.assertEqual(said, [(k, len(names), names[k - 1]) for k in range(10, len(names) + 1, 10)])

    def test_each_robot_of_the_register_is_drawn_equally_often(self):
        inputs, d = self.drawn()
        # Since 2026-11-01 (E12.6 point 4) the PrimeBOT Q1 listed only, no mass stated: 30 robots, the K1 in two.
        self.assertEqual(len(d.register), 30)
        self.assertEqual(len(d.robots), 31)
        p = 1 / len(d.register)
        for share in np.bincount(d.register_robot, minlength=len(d.register)) / d.n:
            self.assertAlmostEqual(share, p, delta=4 * np.sqrt(p * (1 - p) / d.n))
        # Every draw takes the rows of a version of its robot of the register.
        for k, r in enumerate(inputs.robots):
            versions = {d.robots.index(v) for v in schemas.versions(r.taken_apart)}
            self.assertTrue(set(d.robot[d.register_robot == k]) <= versions, msg=r.name)

    def test_a_robot_in_two_versions_draws_each_as_often(self):
        # The entry, decision B: the K1's 5 Ah and 2 Ah, each as often (a discrete state, never blended).
        inputs, d = self.drawn()
        k1 = next(k for k, r in enumerate(inputs.robots) if 'Booster K1 5 Ah' in r.taken_apart)
        rows = d.register_robot == k1
        five = (d.robot[rows] == d.robots.index('Booster K1 5 Ah')).mean()
        self.assertAlmostEqual(five, 0.5, delta=4 * np.sqrt(0.25 / rows.sum()))

    def test_each_robot_weighs_its_own_mass_within_its_range(self):
        inputs, d = self.drawn()
        for k, name in enumerate(d.robots):
            low, _, high = inputs.apart.constants[name][composition.ROBOT_MASS][1]
            mass = d.mass[d.robot == k]
            self.assertTrue(np.all((mass >= low) & (mass <= high)), msg=name)

    def test_the_materials_and_the_parts_of_every_draw_add_up_to_its_mass(self):
        _, d = self.drawn()
        for columns, draws in (d.materials, d.parts):
            np.testing.assert_allclose(draws.sum(axis=1), d.mass, rtol=1e-9)

    def test_nothing_is_cut_where_a_remainder_falls_below_zero(self):
        # The frame, the battery housing and the joints' structure (where a joint's mass is stated, or its share of the
        # robot) are remainders: below zero they are reported, never cut (point 2).
        inputs, d = self.drawn()
        below = composition.below_zero(d)
        expected = {f'{p.robot}: {p.name}' for p in inputs.apart.parts
                    if p.computed.startswith((composition.FRAME, composition.HOUSING))}
        expected |= {f'{j.robot}: {j.name} structure' for j in inputs.apart.joints
                     if None not in j.module_mass or j.share is not None}
        self.assertEqual(set(below), expected)
        for share in below.values():
            self.assertTrue(0 <= share <= 1)

    def test_a_joint_whose_mass_is_stated_weighs_that_mass(self):
        # Matthias, 2026-10-28: "Yes, build it" (VERIFICATION.md V57): each joint whose module mass is given adds up to
        # its drawn module mass, its structure the explicit remainder; so its robot's joints lie between the sums of
        # their stated minima and maxima in every draw.
        inputs, d = self.drawn()
        columns, draws = d.parts
        for k, robot in enumerate(d.robots):
            stated = [j for j in inputs.apart.joints if j.robot == robot]
            if any(None in j.module_mass for j in stated):
                continue
            rows = d.robot == k
            joints = sum(draws[rows, i] for i, c in enumerate(columns) if c.startswith(robot + ':')
                         and c.endswith('joints)'))
            low = sum(j.count * j.module_mass[0] for j in stated)
            high = sum(j.count * j.module_mass[2] for j in stated)
            with self.subTest(robot=robot):
                self.assertTrue(np.all((joints >= low - 1e-9) & (joints <= high + 1e-9)),
                                msg=f'{joints.min():.3f} to {joints.max():.3f} kg against {low:.3f} to {high:.3f}')

    def test_joints_that_are_a_share_of_the_robot_weigh_that_share(self):
        # E5.17 point 1: the joint modules 24.5 / 49 / 73.5 % of the robot's mass, split by fixed shares.
        inputs, d = self.drawn()
        columns, draws = d.parts
        low, _, high = inputs.apart.constants[schemas.ALL_ROBOTS][composition.JOINT_SHARE][1]
        shared = [r for r in d.robots if any(j.share is not None for j in inputs.apart.joints if j.robot == r)]
        # 13: the PrimeBOT Q1 out since 2026-11-01 (E12.6); the Booster T2, Noetix Bumi and E1 their makers' joints
        # since E14 (E14.6 point 1).
        self.assertEqual(len(shared), 13)
        for robot in shared:
            rows = d.robot == d.robots.index(robot)
            joints = sum(draws[rows, i] for i, c in enumerate(columns) if c.startswith(robot + ':')
                         and c.endswith(')') and 'joints)' in c)
            with self.subTest(robot=robot):
                share = joints / d.mass[rows]
                self.assertTrue(np.all((share >= low - 1e-9) & (share <= high + 1e-9)))

    def test_robot_type_1_as_02_writes_every_robot_type_adds_up(self):
        # Its materials (Not allocated 0), part groups and body regions add up to its mass, its elements to the
        # kilograms of the materials they come from, nothing below zero but where 02 allows it (draw_faults).
        inputs, d = self.drawn()
        category = next(c for c in inputs.base.book.categories if c.number == 1)
        c = composition.compose_taken_apart(category, d, inputs.base.lists)
        self.assertEqual(composition.draw_faults(c), [])
        self.assertFalse(c.column('materials', schemas.NOT_ALLOCATED).any())
        np.testing.assert_allclose(c.column('total', 'Total'), d.mass)

    def test_either_of_two_grades_or_materials_each_as_often(self):
        # E5.18, E5.19: the electrical steel M19 or M27, the battery housing aluminium or plastics, each as often.
        inputs, d = self.drawn()
        shared = composition.Shared(inputs, self.params, fixed_magnets(inputs, d.n), np.random.default_rng(5), d.n)
        for written in ('M19 or M27', 'Aluminium or Plastics'):
            first = (shared.state(written) == 0).mean()
            self.assertAlmostEqual(first, 0.5, delta=4 * np.sqrt(0.25 / d.n), msg=written)


class TestHandCalculations(unittest.TestCase):
    """Point 6: one robot at its modes, added up by hand from the data file (EVIDENCE.md E2.8, E2.8b, E5)."""

    @classmethod
    def setUpClass(cls):
        cls.params = Params()
        cls.params.composition.draws = 300

    def at(self):
        inputs = inputs_or_skip(self, self.params)
        with mock.patch.object(composition, 'triangle', at_mode):
            return draw(inputs, self.params, fixed_magnets(inputs, self.params.composition.draws))

    def element(self, d, robot: str, kind: str, element: str) -> np.ndarray:
        return d.elements.get((kind, element), np.zeros(d.n))[d.robot == d.robots.index(robot)]

    def recipe_element(self, d, robot: str, kind: str, element: str) -> np.ndarray:
        """An element by the recipes, fractions and sibling files, those not of interest too (E19 point 3)."""
        return d.recipe_elements.get((kind, element), np.zeros(d.n))[d.robot == d.robots.index(robot)]

    def part(self, d, column: str) -> np.ndarray:
        columns, draws = d.parts
        robot = column.split(': ')[0]
        return draws[d.robot == d.robots.index(robot), columns.index(column)]

    def test_the_g1s_copper_in_its_cables(self):
        d = self.at()
        # Cables: 6 m × (2 × 0.82 + 2 × 0.13) mm2 × 8.96 g/cm3 = 102.144 g; 46 mated XT30 (2+2) × 2.12 g × 0.35 of
        # contacts × 0.62 copper of their brass = 21.16184 g (2026-10-29, "Yes, enter all", EVIDENCE.md E5.22: the pair
        # 1.1224 g + 1 g, its contacts brass); 4 capacitor buffer boards × 5 cm2 × 0.56 g/cm2 × 0.20 = 2.24 g. The
        # element copper is the copper and the boards' copper, 104.384 g; the brass stays a material, its copper bound
        # in it (EVIDENCE.md E19 point 3, question 3), so it is in the recipes' copper only.
        np.testing.assert_allclose(self.element(d, 'Unitree G1', 'cables', 'Cu'), 0.104384, rtol=1e-9)
        np.testing.assert_allclose(self.recipe_element(d, 'Unitree G1', 'cables', 'Cu'), 0.12554584, rtol=1e-9)

    def test_the_g1s_gold_in_its_hips(self):
        d = self.at()
        # Six hip joints, large: a driver board of 22.9 cm2 × 3.56 = 81.524 cm2 × 0.02 mg/cm2 (car PE_HVS) each,
        # 9.78288 mg; two encoders each, 12 × 0.06 mg (car angle sensor) = 0.72 mg.
        np.testing.assert_allclose(self.element(d, 'Unitree G1', 'hips', 'Au'), 10.50288e-6, rtol=1e-9)

    def test_the_g1s_lead_in_its_hips_from_its_driver_boards(self):
        # 2026-10-29, "Yes, build them", point 3a: the boards' aluminium, zinc, iron and lead from the car board file,
        # as its other metals. Six hip joints, large: a driver board of 22.9 cm2 × 3.56 = 81.524 cm2 each, 489.144 cm2
        # × 0.5 mg/cm2 (car PE_HVS, the mode) = 244.572 mg. The die-cast alloy, A380 or ADC12, is drawn: in the draws
        # of ADC12 (its lead 0 at the mode) the boards' lead is all the hips hold.
        d = self.at()
        np.testing.assert_allclose(self.element(d, 'Unitree G1', 'hips', 'Pb').min(), 244.572e-6, rtol=1e-9)

    def material(self, d, robot: str, kind: str, material: str) -> np.ndarray:
        columns, draws = d.materials
        return draws[d.robot == d.robots.index(robot), columns.index((kind, material))]

    def test_the_rp1s_magnets_in_its_covers_of_their_stated_class(self):
        # 2026-10-29, "Yes, build them", point 4: 80 magnets of 0.283 g at the mode, NdFeB of the class N they name
        # (N52), neodymium 24 % (FIXED_MAGNET): 5.4336 g in its frame and shell, which holds no other magnet.
        d = self.at()
        np.testing.assert_allclose(self.element(d, 'RoboParty RP1', 'frame', 'Nd'), 80 * 0.000283 * 0.24, rtol=1e-9)
        rows = d.robot == d.robots.index('RoboParty RP1')
        np.testing.assert_allclose(d.details[('frame', composition.MAGNETS, 'N')][rows], 80 * 0.000283, rtol=1e-9)

    def test_the_rp1s_auxiliary_battery_is_cells_as_its_main_pack(self):
        # Point 4: its main cells 48 V × 10 Ah = 480 Wh over 241.5 Wh/kg, and its auxiliary cells 0.25 kg at the mode,
        # both battery cells by the NMC recipe.
        d = self.at()
        cells = 480 / 241.5 + 0.25
        np.testing.assert_allclose(self.material(d, 'RoboParty RP1', 'battery', composition.CELL_MATERIAL), cells,
                                   rtol=1e-9)
        rows = d.robot == d.robots.index('RoboParty RP1')
        key = ('battery', composition.CELL_MATERIAL, composition.CELL_RECIPE)
        np.testing.assert_allclose(d.details[key][rows], cells, rtol=1e-9)

    def test_the_g1s_head_sensors_are_their_elements_and_their_housings(self):
        # Point 3c: the head holds the head control board (15 cm2 × 0.56 g/cm2 = 8.4 g) and four sensors with masses
        # (265 + 75 + 10 + 35 = 385 g). Each sensor its car elements (electronics) and its housing, the rest of its
        # mass: aluminium 50 % of it at the mode, plastics the remainder.
        d = self.at()
        aluminium, plastics, electronics = (self.material(d, 'Unitree G1', 'head', m)
                                            for m in (composition.ALUMINIUM, 'Plastics', composition.ELECTRONICS))
        np.testing.assert_allclose(aluminium, plastics, rtol=1e-9)
        np.testing.assert_allclose(aluminium + plastics + electronics, 0.385 + 0.0084, rtol=1e-9)
        self.assertTrue((electronics > 0.0084).all() and (aluminium < 0.385 / 2).all())   # the elements in electronics

    def test_the_g1s_head_board_holds_its_bromine_in_the_rest_beyond_its_metals(self):
        # 2026-10-29, "Yes, enter them" (point 3b, EVIDENCE.md E5.21): the rest of a board beyond its metals 55 % glass
        # fibre, 8.8 % bromine, epoxy the remainder, at the modes. The G1's head control board: 15 cm2 × 0.56 g/cm2 =
        # 8.4 g, less its copper (20 %), its tantalum (the data centres' share) and its car metals (VCC, mg per cm2).
        inputs = inputs_or_skip(self, self.params)
        d = self.at()
        metals = 15 * sum(inputs.pcb['VCC'][m][1] for m in schemas.BOARD_METALS) / 1e6
        rest = 0.0084 * (1 - 0.2 - inputs.tantalum[1]) - metals
        np.testing.assert_allclose(self.recipe_element(d, 'Unitree G1', 'head', 'Br'), 0.088 * rest, rtol=1e-9)
        self.assertNotIn(('head', 'Br'), d.elements)   # the laminate's: no element of interest (E19 point 3)

    def test_type_1s_electronics_wholly_drawn_and_their_metals_of_interest_declared(self):
        # Point 3b: the boards' rest in the elements, the sensors' housings their own materials (point 3c), a joint's
        # encoders inside its driver board: every robot's electronics are drawn as elements whole, to the compounds'
        # rounding. Of them, the metals of interest are its elements (E19 point 3), not the laminate's glass, epoxy and
        # bromine, nor zinc and iron: in part.
        inputs = inputs_or_skip(self, self.params)
        d = self.at()
        category = next(c for c in inputs.base.book.categories if c.number == 1)
        c = composition.compose_taken_apart(category, d, inputs.base.lists)
        at = c.tables['materials'][0].index(composition.ELECTRONICS)
        np.testing.assert_allclose(c.in_recipes[:, at], c.tables['materials'][1][:, at],
                                   rtol=composition.COMPOUND_TOLERANCE)
        rows = {r['Name']: r for r in composition.summary(c) if r['Kind'] == 'Material'}
        self.assertEqual(rows[composition.ELECTRONICS]['In the elements'], 'Partly')

    def test_the_g1s_neodymium_in_its_hips(self):
        d = self.at()
        # Six rotors of 42.9 g × 1.78 (the large joint), 90 % NdFeB, 24 % Nd: 98.965152 g; twelve encoders × 20 mg.
        np.testing.assert_allclose(self.element(d, 'Unitree G1', 'hips', 'Nd'), 0.099205152, rtol=1e-9)

    def test_the_g1s_molybdenum_in_its_hips_from_the_grades(self):
        # E5.18, every share at its mode. One large joint: the output flange 50.8 g × 1.78 = 90.424 g of 42CrMo4,
        # Mo 0.225 %: 0.203454 g; the "Other" 38.1 g × 1.78 = 67.818 g, 40 % 42CrMo4: 0.0610362 g; the small bearings
        # 11 g × 1.78 = 19.58 g of GCr15, Mo 0.05 %: 0.00979 g; the gear stage 2 74 g × 2.33 = 172.42 g, 75 % steel,
        # half of it GCr15: 64.6575 g, 0.0323288 g. Six hip joints: 1.8396537 g. No other material of the hips holds
        # Mo.
        d = self.at()
        np.testing.assert_allclose(self.recipe_element(d, 'Unitree G1', 'hips', 'Mo'), 1.8396537e-3, rtol=1e-6)
        self.assertNotIn(('hips', 'Mo'), d.elements)   # it stays in its steel (E19 point 3)

    def test_each_robot_at_its_modes_weighs_its_own_mass(self):
        inputs = inputs_or_skip(self, self.params)
        d = self.at()
        for k, robot in enumerate(d.robots):
            mass = inputs.apart.constants[robot][composition.ROBOT_MASS][1][1]
            np.testing.assert_allclose(d.mass[d.robot == k], mass, rtol=1e-12, err_msg=robot)

    def test_a_robot_without_joint_torques_and_battery_data_at_its_modes(self):
        # The Nori L3, 40 kg (E5.17; the Noetix E1 before, its joints its maker's since E14): its joint modules 49 % of
        # it, 19.6 kg; its shell 11.5 %, 4.6 kg; its battery 12 Wh per kg of robot, 480 Wh: cells 480 / 241.5 = 1.987578
        # kg, its pack weighed by no source, so its housing 0.414 of its cells (EVIDENCE.md E20): 0.822857 kg.
        d = self.at()
        columns, draws = d.parts
        rows = d.robot == d.robots.index('Nori L3')
        joints = sum(draws[rows, i] for i, c in enumerate(columns) if c.startswith('Nori L3:') and 'joints)' in c)
        np.testing.assert_allclose(joints, 19.6, rtol=1e-9)
        np.testing.assert_allclose(self.part(d, 'Nori L3: Shell: engineering plastics'), 4.6, rtol=1e-9)
        np.testing.assert_allclose(self.part(d, 'Nori L3: Battery cells'), 480 / 241.5, rtol=1e-9)
        np.testing.assert_allclose(self.part(d, 'Nori L3: Battery housing, busbars and wires'),
                                   480 / 241.5 * 0.414, rtol=1e-9)


class TestGradesByHeat(unittest.TestCase):
    """Matthias, 2026-10-28: "Heat has to matter and so the distribution will be different depending on the joint",
    then "Accept as proposed" (EVIDENCE.md E2.11): each heat group's grade class drawn by its probabilities, the classes
    tied within a draw (one draw decides how hot the robot is built for, every joint takes its class at that point)."""

    # Dysprosium by class, different for each, so that a joint's dysprosium tells which class it drew.
    DY = {'N': 0.0, 'H': 0.03, 'SH': 0.05, 'UH': 0.07, 'EH': 0.09}   # N: the RP1's cover magnets (point 4), no Dy

    def graded_magnets(self, inputs, n):
        names = ['Nd', 'Pr', 'Dy', 'B', 'Fe']
        return {k: (names, np.tile([0.24, 0.06, self.DY[k], 0.01, 0.69 - self.DY[k]], (n, 1)))
                for k in composition.grade_classes(inputs)}

    def test_each_heat_group_draws_its_classes_by_their_probabilities_tied_within_a_draw(self):
        params = Params()
        params.composition.draws = 4000
        inputs = inputs_or_skip(self, params)
        d = draw(inputs, params, self.graded_magnets(inputs, params.composition.draws))
        order = list(schemas.MAGNET_CLASSES)
        groups: dict = {}
        for g in inputs.apart.grades:
            groups.setdefault(g.group, []).append((order.index(g.klass), g.klass, g.probability))
        for group, classes in groups.items():
            classes.sort()
            drawn = d.grades[group]
            with self.subTest(group=group):
                for _, klass, p in classes:
                    share = (drawn == klass).mean()
                    self.assertAlmostEqual(share, p, delta=4 * np.sqrt(p * (1 - p) / d.n) + 1e-12, msg=klass)
                # Tied: the class is the one at the draw's heat on the group's cumulative probabilities.
                edges = np.cumsum([p for _, _, p in classes])
                at = np.minimum(np.searchsorted(edges, d.heat, side='right'), len(classes) - 1)
                self.assertTrue(np.array_equal(drawn, np.array([k for _, k, _ in classes])[at]))

    def test_a_joints_dysprosium_follows_the_class_it_drew(self):
        # Every triangle at its mode: the G1's two knees' magnets, times the dysprosium of the class each draw gave
        # the knees, plus their four encoders' 0.5 mg (car angle sensor).
        params = Params()
        params.composition.draws = 2000
        inputs = inputs_or_skip(self, params)
        with mock.patch.object(composition, 'triangle', at_mode):
            d = draw(inputs, params, self.graded_magnets(inputs, params.composition.draws))
        g1 = d.robot == d.robots.index('Unitree G1')
        columns, materials = d.materials
        magnets = materials[g1, columns.index(('knees', composition.MAGNETS))]
        expected = magnets * np.array([self.DY[k] for k in d.grades['Knees'][g1]]) + 4 * 0.5e-6
        np.testing.assert_allclose(d.elements[('knees', 'Dy')][g1], expected, rtol=1e-9)
        self.assertGreater(len(set(d.grades['Knees'][g1])), 1)


class TestMagnets(unittest.TestCase):
    """Answer C: the magnets' elements from RAWCLICVehicleTractionMotor's own code, run where it lies."""

    def test_its_fractions_add_up_to_one_with_iron_the_remainder(self):
        params = Params()
        python = os.path.join(params.data.traction_motor_dir, '.venv', 'bin', 'python')
        if not os.path.exists(python):
            self.skipTest(f'not on disk: {python}')
        fractions = composition.magnet_fractions(params, ['SH', 'H'], 50)
        for klass, (names, drawn) in fractions.items():
            self.assertEqual(drawn.shape, (50, len(names)))
            np.testing.assert_allclose(drawn.sum(axis=1), 1.0, rtol=1e-12, err_msg=klass)
            self.assertIn('Fe', names)
            self.assertTrue(np.all(drawn[:, names.index('Nd')] > 0.2), msg=klass)


class TestReadable(unittest.TestCase):
    """Matthias, 2026-10-28: "Have the overview on several pages. I can not read it. too smal, you should notice this
    before you sjhow me. Elements is an edge case. Also quite small". He looks at a page fit to his screen: every page,
    fit to a 1920 × 1080 screen, shows its smallest text at least 18 pixels tall."""

    SCREEN = (1920, 1080)
    SMALLEST_PX = 18

    def test_every_page_is_readable_fit_to_a_screen(self):
        # Type 1's pages, and since 2026-10-30 ("Yes, build it", EVIDENCE.md E11.7 open point B) types 3 and 4's, each
        # over its robots of every parts file (type 2's in TestTypeTwo).
        # Type 5's since its pages were previewed (E19, 2026-11-02): its name the longest of the six.
        for robot_type in (1, 3, 4, 5):
            with self.subTest(robot_type=robot_type):
                self.readable(robot_type)

    def readable(self, robot_type: int) -> None:
        """02's pages of one robot type, each readable fit to a screen, no text of the page running off it."""
        import matplotlib.image
        from matplotlib.text import Text
        params = Params()
        params.composition.draws = 300
        inputs = inputs_or_skip(self, params) if robot_type == 1 else type_inputs_or_skip(self, params, robot_type)
        d = draw(inputs, params, fixed_magnets(inputs, params.composition.draws))
        category = next(c for c in inputs.base.book.categories if c.number == robot_type)
        c = composition.compose_taken_apart(category, d, inputs.base.lists)
        with tempfile.TemporaryDirectory() as folder:
            params.output.parts_dir = os.path.join(folder, 'data')
            pages = composition.parts_figure_pages(d)
            self.assertEqual([name for name, _ in pages if '_notes_' not in name],
                             list(composition.parts_figures(robot_type)))
            # 02's pages of the robot type: its notes, its elements and its materials nine a page; where each material
            # sits.
            pages += composition.taken_apart_pages(c, d, [], params) + composition.sources_pages(d)
            for name, figure in pages:
                figure.canvas.draw()
                sizes = [t.get_fontsize() for t in figure.findobj(Text) if t.get_visible() and t.get_text().strip()]
                # No text of the page itself (its title, a notes page's notes, which grow with them) runs off it.
                page = figure.bbox
                within = lambda t: all(page.contains(*corner) for corner in t.get_window_extent().get_points())  # noqa
                outside = [t.get_text()[:60] for t in figure.texts if t.get_text().strip() and not within(t)]
                path = os.path.join(folder, name)
                os.makedirs(os.path.dirname(path), exist_ok=True)
                figure.savefig(path, dpi=params.output.dpi, facecolor='white')
                composition.plt.close(figure)
                height, width = matplotlib.image.imread(path).shape[:2]
                scale = min(self.SCREEN[0] / width, self.SCREEN[1] / height)
                smallest = min(sizes) * params.output.dpi / 72 * scale
                self.assertEqual(outside, [], msg=name)
                self.assertGreaterEqual(smallest, self.SMALLEST_PX,
                                        msg=f'{name}: {width} × {height} px, smallest text {smallest:.1f} px')

    def test_no_panel_title_runs_into_its_numbers(self):
        # Matthias, 2026-10-30, "Yes, fix it" (V104: "Magnets, grade class UH" ran into its "mean 583 g"): on the element
        # and material pages of types 1 and 2, a panel's title (left) and its share, median and mean (right) never
        # overlap; the numbers sit above the title's line.
        params = Params()
        params.composition.draws = 300
        # Types 3 and 4 since 2026-10-30 (E11.7 open point B), over their robots of every parts file.
        for robot_type, inputs_of in ((1, inputs_or_skip), (2, type_two_inputs_or_skip),
                                      (3, lambda t, p: type_inputs_or_skip(t, p, 3)),
                                      (4, lambda t, p: type_inputs_or_skip(t, p, 4))):
            inputs = inputs_of(self, params)
            d = draw(inputs, params, fixed_magnets(inputs, params.composition.draws))
            category = next(c for c in inputs.base.book.categories if c.number == robot_type)
            c = composition.compose_taken_apart(category, d, inputs.base.lists)
            for name, figure in composition.taken_apart_pages(c, d, [], params):
                figure.canvas.draw()
                renderer = figure.canvas.get_renderer()
                for axes in figure.axes:
                    left, right = axes._left_title, axes._right_title
                    if left.get_text().strip() and right.get_text().strip():
                        self.assertFalse(left.get_window_extent(renderer).overlaps(right.get_window_extent(renderer)),
                                         msg=f'{name}: {left.get_text()!r} over {right.get_text()!r}')
                composition.plt.close(figure)


class TestProjectWords(unittest.TestCase):
    """Matthias's figure rule: no code names and no project jargon on a page; 2026-10-29, "Yes, build them", point 7:
    every page of 02 in plain words (01's PROJECT_WORDS)."""

    def test_no_project_words_on_any_page_of_02(self):
        from matplotlib.text import Text
        params = Params()
        params.composition.draws = 300
        inputs = inputs_or_skip(self, params)
        d = draw(inputs, params, fixed_magnets(inputs, params.composition.draws))
        category = next(c for c in inputs.base.book.categories if c.number == 1)
        c = composition.compose_taken_apart(category, d, inputs.base.lists)
        pages = (composition.taken_apart_pages(c, d, [], params) + composition.parts_figure_pages(d)
                 + composition.sources_pages(d))
        for name, figure in pages:
            words = ' '.join(' '.join(t.get_text() for t in figure.findobj(Text)).split())
            composition.plt.close(figure)
            for word in schemas.PROJECT_WORDS:
                self.assertNotIn(word, words, msg=name)


class TestNoDeprecatedCalls(unittest.TestCase):
    """Matthias, 2026-10-29, from his run of 02: "MatplotlibDeprecationWarning: vert: bool was deprecated in Matplotlib
    3.11 and will be removed in 3.13". Every page of 02 drawn with the pinned matplotlib without a deprecated call, so
    that a later matplotlib draws them the same."""

    def test_the_pages_of_02_call_nothing_deprecated(self):
        import warnings
        from matplotlib import MatplotlibDeprecationWarning
        params = Params()
        params.composition.draws = 300
        inputs = inputs_or_skip(self, params)
        d = draw(inputs, params, fixed_magnets(inputs, params.composition.draws))
        category = next(c for c in inputs.base.book.categories if c.number == 1)
        c = composition.compose_taken_apart(category, d, inputs.base.lists)
        with warnings.catch_warnings():
            warnings.simplefilter('error', MatplotlibDeprecationWarning)
            pages = (composition.taken_apart_pages(c, d, [], params) + composition.parts_figure_pages(d)
                     + composition.sources_pages(d))
        for _, figure in pages:
            composition.plt.close(figure)


class TestElementTitles(unittest.TestCase):
    """Matthias's figure rule, plain words on every figure: every element of robot type 1's element pages by its name
    and its symbol, "Bromine (Br)", never the symbol alone (2026-10-29: the boards' bromine, point 3b, came without)."""

    def test_every_element_on_the_pages_has_its_name(self):
        params = Params()
        params.composition.draws = 300
        inputs = inputs_or_skip(self, params)
        d = draw(inputs, params, fixed_magnets(inputs, params.composition.draws))
        category = next(c for c in inputs.base.book.categories if c.number == 1)
        c = composition.compose_taken_apart(category, d, inputs.base.lists)
        for symbol in c.tables['elements'][0]:
            self.assertIn(symbol, composition.ELEMENT_NAMES, msg=symbol)
            self.assertEqual(composition.element_label(symbol), f'{composition.ELEMENT_NAMES[symbol]} ({symbol})')


class TestPartsNotes(unittest.TestCase):
    """Matthias, 2026-10-29: "parts taken apart show each a long legend, you know, what I think about this": his rule,
    the notes once, on a page of their own. The two figures of where the critical elements sit carry no footnote; their
    notes are on one page, the first of the folder."""

    def test_the_notes_once_on_their_own_page_and_no_footnote_on_a_figure(self):
        params = Params()
        params.composition.draws = 300
        inputs = inputs_or_skip(self, params)
        d = draw(inputs, params, fixed_magnets(inputs, params.composition.draws))
        pages = composition.parts_figure_pages(d)
        notes = [figure for name, figure in pages if '_notes_' in name]
        figures = [(name, figure) for name, figure in pages if '_notes_' not in name]
        self.assertEqual([name for name, _ in pages][:len(notes)],
                         [f'robot_type_1_notes_{k}.png' for k in range(1, len(notes) + 1)])   # first in the folder
        for name, figure in figures:
            footnotes = [t.get_text() for t in figure.texts if t.get_text() != figure.get_suptitle()]   # its title
            self.assertEqual(footnotes, [], msg=name)
            composition.plt.close(figure)
        text = ' '.join(' '.join(t.get_text() for figure in notes for t in figure.texts).split())
        for figure in notes:
            composition.plt.close(figure)
        for words in ('the element pages', 'the overview pages', 'hatched', 'fewer than 2.5 % of the draws',
                      f'{d.n:,} draws', "the magnets' grade class"):
            self.assertIn(words, text.lower())


class TestElementPages(unittest.TestCase):
    """Matthias, 2026-10-29: "I told you I want to see the distribution not just the 0 value for vanadium and lead": an
    element that is 0 in some draws (a robot or a version without it) shows the draws that hold it and in what share of
    the draws it is held, as the material pages do ("If there is nothing then show nothing. If it is just a bit and a
    large 0 then show me the distribution")."""

    @classmethod
    def setUpClass(cls):
        cls.params = Params()
        cls.params.composition.draws = 3000

    def test_an_element_held_in_some_draws_shows_the_draws_that_hold_it(self):
        inputs = inputs_or_skip(self, self.params)
        d = draw(inputs, self.params, fixed_magnets(inputs, self.params.composition.draws))
        category = next(c for c in inputs.base.book.categories if c.number == 1)
        c = composition.compose_taken_apart(category, d, inputs.base.lists)
        pages = composition.taken_apart_pages(c, d, [], self.params)
        panels = {axes.get_title(loc='left'): axes.get_title(loc='right')
                  for name, figure in pages if '_elements_' in name for axes in figure.axes}
        for _, figure in pages:
            composition.plt.close(figure)
        partly = []
        for symbol in c.tables['elements'][0]:
            kg = c.column('elements', symbol)
            held = kg > 0
            label = composition.element_label(symbol)
            label = label + ', inflow' if label + ', inflow' in panels else label   # copper since E25
            if held.mean() < composition.HELD_SHARE:   # nothing, or nearly: no panel
                self.assertNotIn(label, panels)
                continue
            numbers = panels[label]
            self.assertNotIn('median 0 ', numbers, msg=symbol)
            if held.all():
                self.assertNotIn('of the draws', numbers, msg=symbol)
                continue
            partly.append(symbol)
            per, unit = composition.panel_unit(kg[held])
            self.assertIn(f'in {composition.panel_number(100 * held.mean())} % of the draws', numbers)
            self.assertIn(f'median {composition.panel_number(np.median(kg[held]) / per)} {unit}', numbers)
        self.assertIn('Ti', partly)      # the titanium alloy, in some robots only (E19 point 3: Ti whole)
        self.assertNotIn('Pb', partly)   # since point 3a in every robot's boards, so in every draw

    def test_a_critical_element_held_in_some_draws_shows_the_draws_that_hold_it(self):
        # The same on the pages of where the critical elements sit: indium, in the head of some robots only.
        inputs = inputs_or_skip(self, self.params)
        d = draw(inputs, self.params, fixed_magnets(inputs, self.params.composition.draws))
        partly = []
        for symbol, name in composition.FIGURE_ELEMENTS:
            kinds = composition.by_kind(d, symbol)
            total = sum(kinds.values())
            figure, axes = composition.plt.subplots()
            composition.stacked_panel(axes, kinds, name, True)
            texts = share = axes.get_title(loc='right')   # the numbers above the panel since 2026-11-02
            composition.plt.close(figure)
            self.assertNotIn('median 0\u00a0', texts, msg=symbol)
            held = total > 0
            if held.all():   # since 2026-11-01 the right may say what lies beyond the axis (TestAxisEnd), never a share
                self.assertNotIn('of the draws', share, msg=symbol)
                continue
            partly.append(symbol)
            self.assertEqual(share.split('\n')[0], f'in {composition.panel_number(100 * held.mean())} % of the draws')
            per, unit = composition.panel_unit(total[held])
            self.assertIn(f'median {composition.panel_number(np.median(total[held]) / per)}\u00a0{unit}', texts)
        self.assertIn('In', partly)

    def test_an_overview_row_held_in_some_draws_shows_the_draws_that_hold_it(self):
        # Matthias, 2026-10-29, "Yes, do it": the same for the overview's rows, a kind of part holding the element in
        # only some draws (aluminium in the torso boards: median 0 before). Its median and mean those of the draws that
        # hold it; in what share of the draws, a third column; every number within the page.
        inputs = inputs_or_skip(self, self.params)
        d = draw(inputs, self.params, fixed_magnets(inputs, self.params.composition.draws))
        partly, panels = [], []
        for number, elements in enumerate(composition.OVERVIEW_PAGES, 1):   # the pages as 02 draws them
            figure = composition.overview_page(d, elements, number)
            figure.canvas.draw()
            page = figure.bbox
            for (symbol, _), axes in zip(elements, figure.axes[1:]):       # the robot first, then the panels
                boxes = []
                for t in axes.texts:   # every number within the page and clear of every other
                    box = t.get_window_extent()
                    self.assertTrue(all(page.contains(*c) for c in box.get_points()), msg=f'{symbol}: {t.get_text()}')
                    for other, seen in boxes:
                        self.assertFalse(box.overlaps(seen), msg=f'{symbol}: {t.get_text()} on {other}')
                    boxes.append((t.get_text(), box))
                panels.append((symbol, {(round(t.get_position()[0], 3), round(t.get_position()[1], 2)): t.get_text()
                                        for t in axes.texts}))
            composition.plt.close(figure)
        for symbol, at in panels:
            kinds = composition.by_kind(d, symbol)
            shown = [k for k in composition.KINDS if k in kinds and composition.held(kinds[k])]
            if not shown:
                continue
            per, _ = composition.panel_unit(sum(kinds[k] for k in shown))
            median_x, mean_x, share_x = (round(x, 3) for x in composition.OVERVIEW_COLUMNS)
            for row, kind in enumerate(reversed(shown)):
                held = kinds[kind] > 0
                y = round(row + 0.45, 2)
                self.assertEqual(at[(share_x, y)], f'{composition.panel_number(100 * held.mean())} %')
                self.assertEqual(at[(median_x, y)], composition.panel_number(np.median(kinds[kind][held]) / per))
                if not held.all():
                    partly.append((symbol, kind))
        self.assertIn(('In', 'head'), partly)   # the torso boards' aluminium in every draw since point 3a


class TestCentre(unittest.TestCase):
    """Matthias, 2026-10-28: "Showing the mean is wrong. It is not a good measure. Use the median or show boths", and
    his answer "Both, median first": the median a solid line, the mean a dotted one, each with its number."""

    VALUES = np.random.default_rng(3).lognormal(0.0, 1.0, 5000)   # kg, skewed: its mean well above its median

    def lines(self, axes, style: str) -> list:
        return [line for line in axes.get_lines() if line.get_linestyle() == style]

    def test_the_element_panel_marks_the_median_solid_and_the_mean_dotted(self):
        import matplotlib.pyplot as plt
        figure, axes = plt.subplots()
        composition.stacked_panel(axes, {'hips': self.VALUES}, 'Copper (Cu)', True)
        solid, dotted = self.lines(axes, '-'), self.lines(axes, ':')
        self.assertEqual(len(solid), 1)
        self.assertEqual(len(dotted), 1)
        self.assertAlmostEqual(solid[0].get_xdata()[0], np.median(self.VALUES))
        self.assertAlmostEqual(dotted[0].get_xdata()[0], self.VALUES.mean())
        # Their numbers above the panel, right, not over its bars (Matthias, 2026-11-02: "The figure is first").
        above = axes.get_title(loc='right')
        self.assertTrue('median' in above and 'mean' in above, msg=above)
        self.assertEqual([t.get_text() for t in axes.texts], [])
        plt.close(figure)

    def test_the_overview_row_marks_the_median_solid_and_the_mean_dotted(self):
        import matplotlib.pyplot as plt
        figure, axes = plt.subplots()
        composition.ridge_panel(axes, {'hips': self.VALUES}, {'hips': np.zeros(self.VALUES.size)}, 'Copper (Cu)')
        solid, dotted = self.lines(axes, '-'), self.lines(axes, ':')
        self.assertEqual(len(solid), 1)
        self.assertEqual(len(dotted), 1)
        self.assertAlmostEqual(solid[0].get_xdata()[0], np.median(self.VALUES))
        self.assertAlmostEqual(dotted[0].get_xdata()[0], self.VALUES.mean())
        plt.close(figure)


class TestMaterialPages(unittest.TestCase):
    """Matthias, 2026-10-29: "There are only figures on the element level I want to see, how much Copper and especially
    permanent magnets. The different steels and aluminum alyoys. We had this differently in datacenters", then "Yes, 1
    to 5": the materials of one robot, the steels by grade, the aluminium by its alloys, the magnets in all and by grade
    class, where each sits, the draws behind them kept."""

    @classmethod
    def setUpClass(cls):
        cls.params = Params()
        cls.params.composition.draws = 3000

    def drawn(self):
        inputs = inputs_or_skip(self, self.params)
        return inputs, draw(inputs, self.params, fixed_magnets(inputs, self.params.composition.draws))

    def test_the_grades_alloys_and_magnet_classes_add_up_to_their_material_in_every_draw(self):
        _, d = self.drawn()
        columns, draws = d.materials
        for k, (kind, material) in enumerate(columns):
            parts = sum(kg for (x, m, _), kg in d.details.items() if x == kind and m == material)
            np.testing.assert_allclose(parts, draws[:, k], rtol=1e-9, atol=1e-15, err_msg=f'{kind}, {material}')

    def test_the_panels_by_grade_each_material_then_its_grades(self):
        # EVIDENCE.md E19 point 7 and his yes to the preview of type 5 ("Yes, build them", 2026-11-02): each material of
        # the one list, in its order, then its grades, alloys or magnet classes, each under its material; a material of
        # one grade that grade in its title. Since the same day the material pages show the steels and the aluminium
        # alloys whole (material_page_panels, below); these panels by grade give the pages of where each sits.
        _, d = self.drawn()
        titles = [title for title, *_ in composition.material_panels(d)]
        wanted = ['Copper', 'Nickel: strips of the battery', 'Aluminium alloys', 'Aluminium alloys: 6061 (wrought)',
                  'Aluminium alloys: 7075 (wrought)', 'Steel', 'Steel: gear steel 20CrMnTi', 'Steel: alloy steel 42CrMo4',
                  'Steel: bearing steel GCr15', 'Electrical steel', 'Electrical steel: M19', 'Electrical steel: M27',
                  'NdFeB magnets', 'NdFeB magnets: grade class SH', 'Battery cells: NMC (cylindrical)', 'Plastics']
        for title in wanted:
            self.assertIn(title, titles)
        self.assertEqual([t for t in titles if t in wanted], wanted)   # in the order of the one list
        self.assertNotIn('Permanent magnets', titles)
        # Where copper, the magnets in all, each steel and each aluminium alloy sit, named as before but the magnets.
        sources = [name for name, _ in composition.sources_pages(d)]
        # Each steel also since the stainless and electrical steels are materials of their own (E19 step 1).
        for name in ('Copper', 'NdFeB_magnets', 'Gear_steel_20CrMnTi', 'Aluminium_7075', 'Stainless_steel_440C',
                     'Electrical_steel_M19'):
            self.assertIn(os.path.join(composition.SOURCES_FOLDER, f'{name}.png'), sources)
        self.assertFalse(any('grade_class' in name for name in sources))   # the classes on the pages only
        self.assertNotIn(os.path.join(composition.SOURCES_FOLDER, 'Steel.png'), sources)   # the steels by grade
        figure = dict(composition.sources_pages(d))[os.path.join(composition.SOURCES_FOLDER, 'NdFeB_magnets.png')]
        self.assertTrue(figure.get_suptitle().endswith('where its NdFeB magnets sit'), msg=figure.get_suptitle())
        composition.plt.close('all')

    def test_the_material_pages_show_the_steels_and_the_aluminium_alloys_whole(self):
        # Matthias, 2026-11-02: "There are far to many different types of steels. Can we have this in separate plots and
        # in the overview just steel", "It is the same with aluminum alloys", "We have the parts for each alloy. This is
        # good. But the material is much too detailed", then "Yes, build it": on the material pages the three steels
        # and the aluminium alloys as their material only, each the sum of its grades; the other materials as before;
        # their grades still on the pages of where each sits and in the alloys table.
        _, d = self.drawn()
        panels = composition.material_page_panels(d)
        titles = [title for title, *_ in panels]
        for whole in ('Steel', 'Stainless steel', 'Electrical steel', 'Aluminium alloys'):
            self.assertIn(whole, titles)
            self.assertFalse(any(t.startswith(whole + ':') for t in titles), msg=whole)
            kinds = next(p[3] for p in panels if p[0] == whole)
            grades = sum(kg for (_, m, _), kg in d.details.items() if m == whole)
            np.testing.assert_allclose(sum(kinds.values()), grades, rtol=1e-12, err_msg=whole)
        for kept in ('NdFeB magnets: grade class SH', 'Battery cells: NMC (cylindrical)', 'Nickel: strips of the battery'):
            self.assertIn(kept, titles)
        sources = [name for name, _ in composition.sources_pages(d)]
        for name in ('Gear_steel_20CrMnTi', 'Aluminium_7075', 'Stainless_steel_440C', 'Electrical_steel_M19'):
            self.assertIn(os.path.join(composition.SOURCES_FOLDER, f'{name}.png'), sources)
        composition.plt.close('all')
        alloys = [row[0] for row in composition.alloy_rows(d)]
        self.assertIn('gear steel 20crmnti', ' '.join(alloys).lower())   # the alloys table keeps the grades

    def test_a_material_held_in_some_draws_shows_the_draws_that_hold_it(self):
        # Matthias, 2026-10-29: "If there is nothing then show nothing. If it is just a bit and a large 0 then show me
        # the distribution": the 440C of the X1's pins alone, held in about 1 of 31 draws (since 2026-10-29, "Yes,
        # enter all", every robot holds brass, the contacts of its connectors).
        import matplotlib.pyplot as plt
        _, d = self.drawn()
        title, _, _, kinds = next(p for p in composition.material_panels(d) if p[0] == 'Stainless steel: 440C')
        kg = sum(kinds.values())
        figure, axes = plt.subplots()
        composition.material_panel(axes, kg, title, True)
        numbers = axes.get_title(loc='right')
        share = 100 * (kg > 0).mean()
        self.assertIn(f'in {composition.panel_number(share)} % of the draws', numbers)
        median = np.median(kg[kg > 0]) * 1000
        self.assertIn(f'median {composition.panel_number(median)}', numbers)   # of the draws that hold it, in g
        plt.close(figure)

    def test_the_aluminium_alloys_at_the_modes_of_type_1s_recipe(self):
        # Every triangle at its mode: die-cast 20 % of the aluminium, of the wrought rest 7075 32 % (25.6 %) and 6061
        # the remainder (54.4 %), in every kind of part.
        inputs = inputs_or_skip(self, self.params)
        with mock.patch.object(composition, 'triangle', at_mode):
            d = draw(inputs, self.params, fixed_magnets(inputs, self.params.composition.draws))
        aluminium = sum(kg for (_, m, _), kg in d.details.items() if m == composition.ALUMINIUM)
        alloy = lambda name: sum(kg for (_, m, x), kg in d.details.items() if m == composition.ALUMINIUM and x == name)  # noqa
        np.testing.assert_allclose(alloy('Aluminium 7075'), 0.256 * aluminium, rtol=1e-9)
        np.testing.assert_allclose(alloy('Aluminium 6061'), 0.544 * aluminium, rtol=1e-9)

    def test_the_draws_behind_the_pages_are_written(self):
        _, d = self.drawn()
        with tempfile.TemporaryDirectory() as folder:
            composition.write_taken_apart(d, folder)
            with open(os.path.join(folder, 'grades.txt'), encoding='utf-8') as file:
                columns = file.read().splitlines()
            draws = np.load(os.path.join(folder, 'grades.npy'))
        self.assertEqual(draws.shape, (d.n, len(columns)))
        self.assertIn('Hip joints: Steel: 20CrMnTi', columns)
        self.assertIn('Frame and shell: Aluminium alloys: Aluminium 6061', columns)
        self.assertIn('Knee joints: NdFeB magnets: UH', columns)


class TestPagesByMaterial(unittest.TestCase):
    """EVIDENCE.md E19 point 7, the preview of type 5 approved ("Yes, build them", 2026-11-02): each element's panel
    split by the material it comes from, stacked to the total, as RAWCLICDataCenters 05, six panels a page, each
    material's mean written in the panel, one legend of the page's materials; the material pages each material then its
    grades; then the table of the alloys and grades, what each holds by its recipe and its kg in one robot (point 4)."""

    @classmethod
    def setUpClass(cls):
        cls.params = Params()
        cls.params.composition.draws = 1000

    def drawn(self, robot_type: int = 1):
        inputs = (inputs_or_skip(self, self.params) if robot_type == 1
                  else type_inputs_or_skip(self, self.params, robot_type))
        d = draw(inputs, self.params, fixed_magnets(inputs, self.params.composition.draws))
        category = next(c for c in inputs.base.book.categories if c.number == robot_type)
        return d, composition.compose_taken_apart(category, d, inputs.base.lists)

    def test_each_element_by_the_material_it_comes_from_adds_up_in_every_draw(self):
        d, _ = self.drawn()
        self.assertTrue({m for m, _ in d.by_material} <= set(composition.MATERIAL_COLOURS))
        for element in {e for _, e in d.elements}:
            by_kind = sum(kg for (_, e), kg in d.elements.items() if e == element)
            by_material = sum(kg for (_, e), kg in d.by_material.items() if e == element)
            np.testing.assert_allclose(by_material, by_kind, rtol=1e-12, atol=1e-18, err_msg=element)
        copper = {m for m, e in d.by_material if e == 'Cu'}
        self.assertEqual(copper, {'Copper', 'Battery cells', 'Boards and components'})

    def test_six_panels_a_page_with_the_legend_and_the_means_of_its_materials(self):
        d, c = self.drawn()
        pages = composition.taken_apart_pages(c, d, [], self.params)
        names = [name for name, _ in pages]
        kinds = [name.rsplit('_', 2)[-2] for name in names]
        self.assertEqual(kinds, sorted(kinds, key=['notes', 'elements', 'means', 'materials', 'alloys'].index))
        seen = False
        for name, figure in pages:
            if '_elements_' in name:
                panels = [axes for axes in figure.axes if axes.get_title(loc='left')]
                self.assertLessEqual(len(panels), 6, msg=name)
                legend = [t.get_text() for t in figure.legends[0].get_texts()]
                self.assertEqual(legend, [m for m in composition.MATERIAL_COLOURS if m in legend], msg=name)
                for axes in panels:
                    if axes.get_title(loc='left').startswith('Copper (Cu)'):   # ', inflow' since E25
                        seen = True
                        self.assertEqual([t.get_text() for t in axes.texts], [])   # no text over its bars
                        for material in ('Copper', 'Battery cells', 'Boards and components'):
                            self.assertIn(material, legend)
            if '_means_' in name:   # each element's mean by material, on pages of their own (2026-11-02)
                words = ' '.join(t.get_text() for t in figure.texts)
                if 'Copper (Cu), inflow' in words:
                    for material in ('Copper', 'Battery cells', 'Boards and components'):
                        self.assertIn(f'{material} ', words)
            composition.plt.close(figure)
        self.assertTrue(seen)

    def test_each_alloy_and_grade_with_what_it_holds_and_its_kg(self):
        d, _ = self.drawn()
        rows = {(label, material): (holds, kg) for label, material, holds, kg in composition.alloy_rows(d)}
        holds, kg = rows[('Gear steel 20CrMnTi', 'Steel')]
        self.assertTrue(holds.startswith('Cr 1\u20131.3, Mn 0.8\u20131.1'), msg=holds)
        self.assertTrue(holds.endswith('; Fe the rest'), msg=holds)
        self.assertTrue(rows[('7075 (wrought)', 'Aluminium alloys')][0].startswith(
            'Zn 5.1\u20136.1, Mg 2.1\u20132.9, Cu 1.2\u20132'))
        self.assertEqual(rows[('Brass', 'Brass')][0], 'Cu 58\u201365; Zn the rest')
        self.assertEqual(rows[('Strips of the battery', 'Nickel')][0], 'Ni 100')
        magnets = [h for (label, m), (h, _) in rows.items() if m == 'NdFeB magnets']
        self.assertTrue(magnets and all(h.startswith('Nd ') and h.endswith('; Fe the rest') for h in magnets))
        self.assertFalse({m for _, m in rows} & {'Copper', 'Battery cells', 'Boards and components', 'Plastics'})
        steel = sum(v for (_, m, x), v in d.details.items() if m == 'Steel' and x == '20CrMnTi')
        stats = composition.statistics_of(steel)
        per, unit = composition.panel_unit(steel[steel != 0])
        self.assertTrue(kg.startswith(f"{composition.panel_number(stats['Median (kg)'] / per)} {unit} ("), msg=kg)

    def test_magnesium_by_its_alloys_as_the_aluminium(self):
        # Type 4's magnesium recipe is AM magnesium (AM50A or AM60B) and AZ91D: each its own row, also an alloy held
        # in fewer than 2.5 % of the draws (no panel for it; the table lists every alloy the type holds, with its
        # share of the draws). An element below the table's precision, 0.005 %, is left out (AZ91D's nickel, 0.002 %).
        d, _ = self.drawn(4)
        rows = {label: holds for label, material, holds, _ in composition.alloy_rows(d) if material == 'Magnesium alloys'}
        self.assertEqual(set(rows), {'AM50A', 'AM60B', 'AZ91D'})
        self.assertEqual(rows['AZ91D'], 'Al 8.3\u20139.7, Zn 0.35\u20131, Mn 0.15\u20130.5, Si 0\u20130.1, '
                                        'Cu 0\u20130.03, Fe 0\u20130.005; Mg the rest')
        titles = [title for title, *_ in composition.every_material_panel(d)]   # in fewer than 2.5 % of the draws
        self.assertTrue(any(t.startswith('Magnesium alloys: ') for t in titles), msg=titles)

    def test_the_notes_say_how_to_read_them(self):
        d, c = self.drawn()
        pages = composition.taken_apart_pages(c, d, [], self.params)
        notes = ' '.join(' '.join(t.get_text() for name, figure in pages if '_notes_' in name
                                  for t in figure.texts).split()).lower()
        for _, figure in pages:
            composition.plt.close(figure)
        for words in ('split into the kg its draws hold from each material', 'elements of interest',
                      'what each holds by its recipe', 'stay materials'):
            self.assertIn(words, notes)
        self.assertNotIn('not yet in the elements', notes)


class TestRun(unittest.TestCase):
    """02 writes robot type 1 part by part at every level, and draws its two figures and where each material sits, all
    into temporary folders."""

    def test_02_writes_the_draws_and_draws_both_figures_and_where_each_material_sits(self):
        params = Params()
        params.composition.draws = 300
        inputs = inputs_or_skip(self, params)
        with tempfile.TemporaryDirectory() as folder:
            params.output.parts_dir = os.path.join(folder, 'data')
            params.output.parts_figures_dir = os.path.join(folder, 'figures')
            d = draw(inputs, params, fixed_magnets(inputs, params.composition.draws))
            composition.write_taken_apart(d, params.output.parts_dir)
            composition.draw_parts_figures(d, params, params.output.parts_figures_dir)
            with open(os.path.join(params.output.parts_dir, 'register.txt'), encoding='utf-8') as file:
                self.assertEqual(file.read().splitlines(), d.register)
            for table in composition.APART_TABLES:
                draws = np.load(os.path.join(params.output.parts_dir, f'{table}.npy'))
                with open(os.path.join(params.output.parts_dir, f'{table}.txt'), encoding='utf-8') as file:
                    columns = file.read().splitlines()
                self.assertEqual(draws.shape, (300, len(columns)), msg=table)
            self.assertTrue(os.path.exists(os.path.join(params.output.parts_dir, 'summary.csv')))
            for name in list(composition.parts_figures(1)) + [n for n, _ in composition.sources_pages(d)]:
                self.assertGreater(os.path.getsize(os.path.join(params.output.parts_figures_dir, name)), 10_000,
                                   msg=name)



def type_two_inputs_or_skip(test: unittest.TestCase, params: Params):
    """02's inputs of robot type 2, from its parts file as its builder writes it, over the register's sheet Type 2 as
    the register's builder writes it (its five robots taken apart, the others not yet); skipped where a file is not on
    disk, failed where the inputs have a fault."""
    params.data.parts_taken_apart = PARTS_PATTERN
    files = [absolute(params.data.workbook), absolute(params.data.shared_lists), absolute(params.data.element_recipes),
             absolute(params.data.humanoid_guide), params.data.vehicle_pcb_composition,
             params.data.vehicle_sensor_composition, params.data.data_center_element_composition,
             params.data.traction_motor_steels]
    missing = [f for f in files if not os.path.exists(f)]
    if missing:
        test.skipTest(f'not on disk: {", ".join(missing)}')
    base = composition.read_inputs(params)
    with tempfile.TemporaryDirectory() as folder:
        path = os.path.join(folder, 'register.xlsx')
        REGISTER_BUILDER.build(path, params)
        listed = schemas.read_type_sheet(path, 2)
    category = next(c for c in base.book.categories if c.number == 2)
    inputs = composition.read_apart_inputs(params, base, listed, category)
    faults = composition.apart_faults(inputs, params)
    if faults:
        test.fail('faults in the inputs: ' + '; '.join(f'{f.sheet} {f.row}: {f.text}' for f in faults))
    return inputs


class TestTypeTwo(unittest.TestCase):
    """Robot type 2 drawn by 02 part by part (Matthias, 2026-10-30, "Yes, build C"): over its robots taken apart (batch
    1's five, the GR-1 in two versions; since "Yes, build it" batch 2's 24, the H2-X in two versions), by type 2's own
    recipes, the Fourier robots' Ethernet line by hand; the robots not yet taken apart counted, so that its draws come
    from the workbook until all are (Q2, Q4)."""
    BATCHES = [25, 47, 53, 69, 80, 98, 116, 117, 119, 120, 121, 123, 132, 134, 135, 144, 151, 153, 157, 158, 163, 170,
               171, 176, 177, 180, 199, 203, 210, 216, 221, 222, 223, 224, 229, 232, 244, 256, 265, 271, 272, 276, 285, 290,
               294, 297, 298, 299, 300, 302, 323, 326, 352]
    # The 43 on wheels (2026-10-30, "Yes, agree E9.6", "Yes, build it"): with them every robot of type 2 with a mass.
    ON_WHEELS = [13, 15, 20, 21, 34, 35, 40, 41, 42, 49, 60, 68, 82, 86, 92, 104, 105, 122, 179, 184, 200, 230, 247, 248,
                 251, 252, 253, 254, 255, 295, 307, 312, 313, 314, 315, 318, 335, 336, 337, 340, 341, 342, 349]

    @classmethod
    def setUpClass(cls):
        cls.params = Params()
        cls.params.composition.draws = 3000

    def test_its_robots_and_those_not_yet_taken_apart(self):
        inputs = type_two_inputs_or_skip(self, self.params)
        self.assertEqual([r.number for r in inputs.robots], sorted(self.BATCHES + self.ON_WHEELS))
        self.assertEqual([r.number for r in inputs.left_out], [329])       # the Xialan S0, no mass stated
        # None with a mass left: type 2's draws from its parts now (Q2). Its robots with a mass, 96:
        # one without is not in the evaluation and not counted (2026-10-30, E10.1 point 4).
        self.assertEqual((len(inputs.later), inputs.listed, inputs.robot_type), (0, 96, 2))

    def test_drawn_over_its_robots_each_as_often(self):
        inputs = type_two_inputs_or_skip(self, self.params)
        d = draw(inputs, self.params, fixed_magnets(inputs, self.params.composition.draws))
        self.assertEqual((d.robot_type, composition.lead(d)), (2, 'Robot type 2, all its 96 robots'))   # E10.1 point 4
        n, p = d.n, 1 / 96
        tolerance = 4 * np.sqrt(p * (1 - p) / n)
        for k in range(96):
            self.assertAlmostEqual((d.register_robot == k).mean(), p, delta=tolerance, msg=d.register[k])
        for version in ('Fourier GR-1 one camera', 'Fourier GR-1 two cameras', 'Unitree H2-X Core i7',
                        'Unitree H2-X Orin NX', 'Walker Tienkung Vision', 'Walker Tienkung Embodied',
                        'Flexiv AICO 2-4', 'Flexiv AICO 2-10', 'Rainbow Robotics RB-Y1 A', 'Rainbow Robotics RB-Y1 M',
                        'Unitree R1-A5-D', 'Unitree R1-A7-D'):
            self.assertAlmostEqual((d.robot == d.robots.index(version)).mean(), p / 2,
                                   delta=4 * np.sqrt(p / 2 * (1 - p / 2) / n))

    def test_its_notes_name_its_own_template(self):
        # Open point B: the template's rows name what they average, and the notes page says it in their words, type
        # 2's seven robots for type 2, batch 1 for type 1; never the other type's.
        inputs = type_two_inputs_or_skip(self, self.params)
        words = list(composition.on_estimates(inputs.apart, ['LimX CL']))
        self.assertEqual(words, ["the joint modules a share of the robot's mass, split as type 2's seven robots with "
                                 "every joint's torque on average", "the battery's energy a share of the robot's mass"])
        one = schemas.read_parts_taken_apart(PARTS_FILE)
        self.assertIn("the joint modules a share of the robot's mass, split as batch 1 on average",
                      composition.on_estimates(one, ['JAKA π']))

    def test_the_jingchus_knees_drawn_from_their_stated_mass_its_other_joints_a_share(self):
        # E7.5 point 2 (open point A): its two knees each 1.9 / 2 / 2.1 kg; its other joints the template's shares of
        # one drawn total, 20.2 / 40.4 / 60.6 % of its mass, the knees' share left out: nothing rescaled.
        inputs = type_two_inputs_or_skip(self, self.params)
        d = draw(inputs, self.params, fixed_magnets(inputs, self.params.composition.draws))
        columns, draws = d.parts
        robot = 'JCBOT JingChu'
        rows = d.robot == d.robots.index(robot)
        knees = sum(draws[rows, i] for i, c in enumerate(columns) if c.startswith(robot + ': Knee ('))
        others = sum(draws[rows, i] for i, c in enumerate(columns) if c.startswith(robot + ':')
                     and c.endswith('joints)') and not c.startswith(robot + ': Knee (') and ': Hand' not in c)
        self.assertTrue(np.all((knees >= 2 * 1.9 - 1e-9) & (knees <= 2 * 2.1 + 1e-9)))
        left = sum(j.share for j in inputs.apart.joints if j.robot == robot and j.share is not None)
        share = others / d.mass[rows] / left
        self.assertTrue(np.all((share >= 0.202 - 1e-9) & (share <= 0.606 + 1e-9)))
        self.assertLess(left, 1)

    def test_its_own_recipes_of_aluminium_and_plastics(self):
        # Q3: type 2's own rows of the element recipes; since E17 (2026-11-02) its copper by the recipe Copper metal.
        inputs = type_two_inputs_or_skip(self, self.params)
        shared = composition.Shared(inputs, self.params, fixed_magnets(inputs, 10), np.random.default_rng(5), 10)
        self.assertEqual(shared.recipe_name, {'Aluminium alloys': 'Aluminium, robot type 2, Aluminum alloys',
                                              'Plastics': 'Plastics, robot type 2, Engineering plastics',
                                              'Copper': 'Copper metal'})
        d = draw(inputs, self.params, fixed_magnets(inputs, self.params.composition.draws))
        self.assertEqual(d.aluminium, 'die-cast 0 to 40 %, of the wrought rest 7075 39 to 97 % and 6061')

    def test_the_copper_of_its_cables_by_hand(self):
        inputs = type_two_inputs_or_skip(self, self.params)
        with mock.patch.object(composition, 'triangle', at_mode):
            d = draw(inputs, self.params, fixed_magnets(inputs, self.params.composition.draws))

        def copper(robot, table='elements'):
            return getattr(d, table)[('cables', 'Cu')][d.robot == d.robots.index(robot)]

        # The GR-2: 14 m × (2 × 0.82 + 8 × 0.205) mm2 × 8.96 g/cm3 = 411.4432 g, two power conductors and an Ethernet
        # line of eight (E6.8 point 9); 62 mated XT30 × 2.12 g × 0.35 of contacts × 0.62 copper of their brass =
        # 28.52248 g. The H2: 14 m × (2 × 0.82 + 2 × 0.13) mm2 × 8.96 = 238.336 g, and the same 28.52248 g. The element
        # copper is the conductors' alone; the brass's copper stays bound in it (E19 point 3, question 3).
        np.testing.assert_allclose(copper('Fourier GR-2'), 0.4114432, rtol=1e-9)
        np.testing.assert_allclose(copper('Unitree H2'), 0.238336, rtol=1e-9)
        np.testing.assert_allclose(copper('Fourier GR-2', 'recipe_elements'), 0.43996568, rtol=1e-9)
        np.testing.assert_allclose(copper('Unitree H2', 'recipe_elements'), 0.26685848, rtol=1e-9)


class TestTypeTwoOnWheels(unittest.TestCase):
    """Type 2's robots on wheels drawn by 02 (Matthias, 2026-10-30, "Yes, agree E9.6", "Yes, build it", E9.7 points 3
    and 5): the wheeled template's joint share and energy for a robot on wheels of the template, its lift column a share
    of its mass (its structure the share less its motor), the CASBOT W1's cells LFP and no other robot's; the two new
    kinds of part drawn."""

    @classmethod
    def setUpClass(cls):
        cls.params = Params()
        cls.params.composition.draws = 3000

    def drawn(self):
        inputs = type_two_inputs_or_skip(self, self.params)
        return inputs, draw(inputs, self.params, fixed_magnets(inputs, self.params.composition.draws))

    def kind_kg(self, d, robot: str, kind: str):
        columns, draws = d.materials
        rows = d.robot == d.robots.index(robot)
        return sum(draws[rows, i] for i, (k, _) in enumerate(columns) if k == kind)

    def test_the_wheeled_template_share_for_a_robot_of_it(self):
        inputs, d = self.drawn()
        columns, draws = d.parts
        robot = 'Toyota CUE7'
        rows = d.robot == d.robots.index(robot)
        body = sum(draws[rows, i] for i, c in enumerate(columns) if c.startswith(robot + ':') and c.endswith('joints)')
                   and not c.startswith((robot + ': Wheel', robot + ': Steering', robot + ': Lift')))
        share = body / d.mass[rows]
        self.assertTrue(np.all((share >= 0.078 - 1e-9) & (share <= 0.234 + 1e-9)))

    def test_the_lift_column_a_share_of_the_robot_mass(self):
        inputs, d = self.drawn()
        rows = d.robot == d.robots.index('Unitree H2-D Flagship')
        share = self.kind_kg(d, 'Unitree H2-D Flagship', 'lift') / d.mass[rows]
        self.assertTrue(np.all((share >= 0.0995 - 1e-9) & (share <= 0.2985 + 1e-9)))
        self.assertTrue(np.all(self.kind_kg(d, 'Toyota CUE7', 'lift') == 0))

    def test_lfp_cells_only_in_the_casbot_w1(self):
        inputs, d = self.drawn()
        key = ('battery', composition.CELL_MATERIAL, 'LFP cylindrical')
        lfp = d.details[key]
        casbot = d.robot == d.robots.index('CASBOT W1')
        self.assertTrue(np.all(lfp[casbot] > 0))
        self.assertTrue(np.all(lfp[~casbot] == 0))
        nmc = d.details[('battery', composition.CELL_MATERIAL, 'NMC cylindrical')]
        self.assertTrue(np.all(nmc[casbot] == 0))

    def test_the_casbot_w1s_housing_a_share_of_its_cells(self):
        # Matthias, 2026-10-30, "Ratio, as recommended" (EVIDENCE.md E9.8): its pack has no mass from its maker and its
        # cells are LFP, so its housing is an NMC pack's in proportion to its cells; since 2026-11-02 ("A, as
        # recommended", E20) every pack no source weighs is so: its housing 0.414 of its cells at the modes, above zero
        # in every draw.
        inputs = type_two_inputs_or_skip(self, self.params)
        with mock.patch.object(composition, 'triangle', at_mode):
            d = draw(inputs, self.params, fixed_magnets(inputs, self.params.composition.draws))
        columns, draws = d.parts
        rows = d.robot == d.robots.index('CASBOT W1')

        def part(name):
            return draws[rows, columns.index(f'CASBOT W1: {name}')]

        cells, housing = part('Battery cells'), part('Battery housing, busbars and wires')
        np.testing.assert_allclose(housing / cells, 0.414, rtol=1e-9)
        _, d = self.drawn()
        columns, draws = d.parts
        rows = d.robot == d.robots.index('CASBOT W1')
        self.assertTrue(np.all(draws[rows, columns.index('CASBOT W1: Battery housing, busbars and wires')] > 0))

    def test_the_wheeled_base_drawn(self):
        inputs, d = self.drawn()
        self.assertTrue(np.all(self.kind_kg(d, 'Toyota CUE7', 'base') > 0))
        self.assertTrue(np.all(self.kind_kg(d, 'Unitree H2', 'base') == 0))
        self.assertIn('base', {k for k, _ in d.materials[0]})

# Types 3 and 4's builders (2026-10-30, E11.7): their files beside types 1's and 2's, each in its own folder.
PARTS_BUILDER_THREE = load('make_parts_taken_apart_3', os.path.join('tools', '3_industrial_logistics_warehousing',
                                                                   'make_parts_taken_apart.py'))
PARTS_BUILDER_THREE.build(PARTS_PATTERN.format(folder='3_industrial_logistics_warehousing'))
PARTS_BUILDER_FOUR = load('make_parts_taken_apart_4', os.path.join('tools', '4_service_healthcare_interaction',
                                                                  'make_parts_taken_apart.py'))
PARTS_BUILDER_FOUR.build(PARTS_PATTERN.format(folder='4_service_healthcare_interaction'))
# Types 5 and 6's (E16.6; since E27.7 the hydraulic Atlas (old) and Nadia): their files too, each in its own folder.
PARTS_BUILDER_FIVE = load('make_parts_taken_apart_5', os.path.join('tools', '5_heavy_duty_high_performance_hazardous_'
                                                                  'environment', 'make_parts_taken_apart.py'))
PARTS_BUILDER_FIVE.build(PARTS_PATTERN.format(folder='5_heavy_duty_high_performance_hazardous_environment'))
PARTS_BUILDER_SIX = load('make_parts_taken_apart_6', os.path.join('tools', '6_defense_public_safety',
                                                                 'make_parts_taken_apart.py'))
PARTS_BUILDER_SIX.build(PARTS_PATTERN.format(folder='6_defense_public_safety'))


def type_inputs_or_skip(test: unittest.TestCase, params: Params, robot_type: int):
    """02's inputs of `robot_type` over every parts file as the builders write them (E11.7 point 4), over the register's
    sheet of the type as its builder writes it; skipped where a file is not on disk, failed where they have a fault."""
    params.data.parts_taken_apart = PARTS_PATTERN
    if not os.path.exists(absolute(params.data.humanoid_guide)):
        test.skipTest('the catalogue is not on disk')
    base = composition.read_inputs(params)
    with tempfile.TemporaryDirectory() as folder:
        path = os.path.join(folder, 'register.xlsx')
        REGISTER_BUILDER.build(path, params)
        listed = schemas.read_type_sheet(path, robot_type)
    files = composition.read_parts_files(params, base)
    category = next(c for c in base.book.categories if c.number == robot_type)
    inputs = composition.read_apart_inputs(params, base, listed, category, files)
    faults = [f for t, file in files.items() for f in composition.apart_faults(composition.file_inputs(inputs, t, file),
                                                                               params)]
    if faults:
        test.fail('faults in the inputs: ' + '; '.join(f'{f.sheet} {f.row}: {f.text}' for f in faults))
    return inputs


class TestTypesThreeAndFour(unittest.TestCase):
    """Types 3 and 4 drawn part by part over the robots of every file that holds one (E11.7 point 4): each robot from
    its own rows with its own file's shared values; types 1 and 2 from their own file, as before."""

    @classmethod
    def setUpClass(cls):
        cls.params = Params()
        cls.params.composition.draws = 3000

    def test_type_3_over_its_72_and_type_4_over_its_33(self):
        # Versions: type 3's robots and the AgiBot X2, the Flexiv AICO 2, the Rainbow RB-Y1 and since batch 2 (E12.6)
        # the CYBORG RO1 and the DR02 in two each; type 4's and the X2, the CASBOT 02 and the FF Master in two. Since
        # batch 2: type 3 91 robots, type 4 47 (the PrimeBOT Q1 out); since types 5 and 6's entry (E16.6) type 3 94: the
        # Kaleido 9, the Moby and the Phantom MK1; since batch 3 (E15.7) type 3 163 robots in 172 versions (Neo1 the
        # one not taken apart), type 4 124 in 137 (each of its robots with a mass); since E27.7 (2026-11-04) type 3 164
        # in 173, Neo1 too; since E30 (2026-11-05, "Yes, 3 to 5") 163 in 172, Neo1 an outlier, not drawn.
        for robot_type, count, versions in ((3, 163, 172), (4, 124, 137)):
            inputs = type_inputs_or_skip(self, self.params, robot_type)
            self.assertEqual(len(inputs.robots), count, msg=robot_type)
            self.assertGreater(len(inputs.files), 1)
            d = draw(inputs, self.params, fixed_magnets(inputs, self.params.composition.draws))
            self.assertEqual(len(d.register), count)
            self.assertEqual(len(d.robots), versions, msg=robot_type)

    def test_the_neo1_an_outlier_not_drawn_in_types_3_and_5_and_named_on_their_notes(self):
        # Matthias, 2026-11-04: "So kick it out of the statistics and just hae it mentioned or in as the outlier", "Ok
        # it is neo. It should be out. Mark it as outlier."; 2026-11-05, "Yes, 3 to 5" (EVIDENCE.md E30): 02 no longer
        # draws it (point 1), in either of its types; it stays in type 3's parts file (point 2); the notes pages of
        # types 3 and 5 name it, not a page of its own (point 4); the other robots drawn as before.
        words = 'Not drawn, an outlier: 208 NeodraDynamics Neo1, 1,200 kg, built as a few, never in large numbers.'
        for robot_type, listed in ((3, 163), (5, 10)):
            inputs = type_inputs_or_skip(self, self.params, robot_type)
            self.assertEqual([r.number for r in inputs.outliers], [208], msg=robot_type)
            self.assertNotIn(208, [r.number for r in inputs.robots])
            self.assertNotIn('NeodraDynamics Neo1', inputs.apart.robots)
            self.assertFalse([x for x in inputs.apart.joints + inputs.apart.parts + inputs.apart.boards
                              + inputs.apart.sensors if x.robot == 'NeodraDynamics Neo1'], msg=robot_type)
            self.assertIn('NeodraDynamics Neo1', inputs.files[3].robots)       # its rows stay in type 3's file
            self.assertEqual((inputs.listed, inputs.later), (listed, []), msg=robot_type)
            self.assertEqual(composition.outlier_words(inputs.outliers, self.params), words)
        params = Params()
        params.composition.draws = 300
        inputs = type_inputs_or_skip(self, params, 5)
        d = draw(inputs, params, fixed_magnets(inputs, params.composition.draws))
        self.assertNotIn('208 Neo1', d.register)
        self.assertNotIn('NeodraDynamics Neo1', d.robots)
        self.assertEqual(composition.lead(d), 'Robot type 5, all its 10 robots')
        category = next(c for c in inputs.base.book.categories if c.number == 5)
        c = composition.compose_taken_apart(category, d, inputs.base.lists)
        notes = composition.taken_apart_notes(c, d, inputs.left_out, params, inputs.later, inputs.outliers)
        self.assertIn(words, notes)
        self.assertNotIn('Neo1', ' '.join(n for n in notes if n != words))
        # A type without an outlier: no such sentence.
        self.assertEqual(composition.outlier_words([], params), '')

    def test_a_robot_of_another_file_drawn_from_its_own_rows(self):
        inputs = type_inputs_or_skip(self, self.params, 3)
        self.assertIn('Unitree H2', inputs.apart.robots)
        self.assertIs(inputs.apart.origin['Unitree H2'], inputs.files[2])
        self.assertEqual(len([j for j in inputs.apart.joints if j.robot == 'Unitree H2']),
                         len([j for j in inputs.files[2].joints if j.robot == 'Unitree H2']))

    def test_each_robot_drawn_with_its_own_files_shared_numbers(self):
        # The robots of type 3 come from the files of types 1 to 4; each is drawn with the shared numbers (the joints'
        # parts, the shares, the constants for all robots) of the file its rows stand in, never of another file.
        inputs = type_inputs_or_skip(self, self.params, 3)
        seen = {}
        robot = composition.Robot

        def recording(name, rows, shared, mass):
            seen[name] = shared.apart
            return robot(name, rows, shared, mass)
        shared = composition.Shared

        def keeping(inputs, *args):
            s = shared(inputs, *args)
            s.apart = inputs.apart
            return s
        with mock.patch.object(composition, 'Robot', recording), mock.patch.object(composition, 'Shared', keeping):
            draw(inputs, self.params, fixed_magnets(inputs, self.params.composition.draws))
        self.assertEqual(set(seen), set(inputs.apart.robots))
        file_of = {id(f): t for t, f in inputs.files.items()}     # a file by the type it is the parts file of
        for name, apart in seen.items():
            self.assertEqual(file_of[id(apart)], file_of[id(inputs.apart.origin[name])], msg=name)

    def test_its_notes_say_how_many_rest_on_templates(self):
        # E13 rules 2 and 4 (E12.6 point 6): 02's notes page of a type says, in 01's words, how many of its robots rest
        # on the templates, and "most" where above half.
        params = Params()
        params.composition.draws = 300
        for robot_type in (3, 4):
            inputs = type_inputs_or_skip(self, params, robot_type)
            d = draw(inputs, params, fixed_magnets(inputs, params.composition.draws))
            self.assertEqual(d.templates, schemas.template_words(inputs.apart))
            category = next(c for c in inputs.base.book.categories if c.number == robot_type)
            c = composition.compose_taken_apart(category, d, inputs.base.lists)
            self.assertIn(d.templates, composition.taken_apart_notes(c, d, [], params, inputs.later))
            self.assertTrue(d.templates.startswith('Most of its robots rest on templates'))

    def test_types_1_and_2_from_their_own_file_only(self):
        for robot_type in (1, 2):
            inputs = type_inputs_or_skip(self, self.params, robot_type)
            self.assertIs(inputs.apart, inputs.files[robot_type])


if __name__ == '__main__':
    unittest.main()


class TestZeroNotInDistribution(unittest.TestCase):
    """Matthias, 2026-11-01: "It can not be that median is 0. If a value is 0 then it is NOT part of the distribution",
    "Check for all with 0 values. There needs to be a rule" (CLAUDE.md §7): the pages of where a material sits and the
    summary of a type taken apart over the draws that are not 0, each with the share of the draws that hold it. Type 2,
    whose wheeled base and lift column are in some draws only (its robots on wheels), and whose legs in others."""

    @classmethod
    def setUpClass(cls):
        cls.params = Params()
        cls.params.composition.draws = 3000

    def drawn(self):
        inputs = type_two_inputs_or_skip(self, self.params)
        return draw(inputs, self.params, fixed_magnets(inputs, self.params.composition.draws))

    def test_where_a_material_sits_over_the_draws_that_hold_it(self):
        d = self.drawn()
        partly = []
        for name, figure in composition.sources_pages(d):
            figure.canvas.draw()
            page = figure.bbox
            axes = figure.axes[0]
            for t in axes.texts:   # every number within the page
                box = t.get_window_extent()
                self.assertTrue(all(page.contains(*c) for c in box.get_points()), msg=f'{name}: {t.get_text()}')
            at = {(round(t.get_position()[0], 3), round(t.get_position()[1], 2)): t.get_text() for t in axes.texts}
            labels = [t.get_text() for t in axes.get_yticklabels()]
            composition.plt.close(figure)
            title = next(p for p in composition.material_panels(d) if composition.source_file(p[1], p[2]) == name)
            kinds = title[3]
            by_label = {composition.KINDS[k][0]: k for k in kinds}
            medians = []
            for row, label in enumerate(labels):
                kg = kinds[by_label[label]]
                held = kg != 0
                median_x, mean_x, share_x = (round(x, 3) for x in composition.NUMBER_COLUMNS)
                for x, value in ((median_x, np.median(kg[held])), (mean_x, kg[held].mean())):
                    per, unit = composition.panel_unit(np.array([value]))
                    self.assertEqual(at[(x, row)], f'{composition.panel_number(value / per)}\u00a0{unit}',
                                     msg=f'{name}, {label}')
                self.assertEqual(at[(share_x, row)], f'{composition.panel_number(100 * held.mean())} %')
                medians.append(np.median(kg[held]))
                if not held.all():
                    partly.append((name, label))
            self.assertEqual(medians, sorted(medians), msg=name)   # the largest median on top, of the held draws
        self.assertIn((os.path.join(composition.SOURCES_FOLDER, 'Copper.png'), 'Wheeled base'), partly)

    def test_its_summary_over_the_draws_that_hold_it(self):
        d = self.drawn()
        with tempfile.TemporaryDirectory() as folder:
            composition.write_taken_apart(d, folder)
            with open(os.path.join(folder, 'summary.csv'), encoding='utf-8', newline='') as file:
                lines = list(csv.reader(file))
        heading, rows = lines[0], [r for r in lines[1:] if r and r[1:2] and r[0] != 'Remainder'][:]
        self.assertEqual(heading, ['Element', 'Kind of part', 'Mean (kg)', 'Median (kg)', '2.5 % (kg)', '97.5 % (kg)',
                                   'Held in (% of the draws)'])
        by_name = {(kind, e): v for (kind, e), v in d.elements.items()}
        names = {composition.KINDS[k][0]: k for k in composition.KINDS}
        partly = 0
        for row in rows:
            if len(row) < 7 or row[1] not in names:
                continue
            kg = by_name[(names[row[1]], row[0])]
            held = kg != 0
            self.assertAlmostEqual(float(row[6]), 100 * held.mean(), places=6, msg=row[:2])
            if not held.any():
                self.assertEqual(row[2:6], [''] * 4, msg=row[:2])
                continue
            self.assertAlmostEqual(float(row[3]), float(np.median(kg[held])), places=9, msg=row[:2])
            self.assertGreater(float(row[3]), 0, msg=row[:2])
            self.assertGreater(float(row[4]), 0, msg=row[:2])
            partly += not held.all()
        self.assertGreater(partly, 0)


class TestAxisEnd(unittest.TestCase):
    """Matthias, 2026-11-01: "The distribution figures show the distribution pressed to the left side. You give away
    have of the x axis. This can be done much better", then "Yes, build it" (VERIFICATION V124): each distribution
    panel's axis ends at the 99.5th percentile of its draws, its 70 bars up to there, their heights still the share of
    all the panel's draws (nothing rescaled); the draws beyond are not drawn, and the panel says how many and the
    largest; on the overview nothing piled into the last bar. On draws with a long tail (a lognormal), as type 2's."""

    def setUp(self):
        rng = np.random.default_rng(7)
        self.kg = rng.lognormal(0.8, 0.6, 20_000)           # kg, a long right tail
        self.end = np.percentile(self.kg, composition.AXIS_END)
        self.beyond = f'{composition.panel_number(100 * (self.kg > self.end).mean())} % beyond the axis, up to ' \
                      f'{composition.panel_number(self.kg.max())} kg'

    def bars(self, axes):
        return [p for p in axes.patches if p.get_width() > 0]

    def test_the_setting(self):
        self.assertEqual(composition.AXIS_END, 99.5)

    def test_an_element_panel_ends_at_its_99_5th_percentile(self):
        figure, axes = composition.plt.subplots()
        composition.element_panel(axes, self.kg, 'Copper (Cu)', True)
        bars = self.bars(axes)
        right = max(p.get_x() + p.get_width() for p in bars)
        numbers = axes.get_title(loc='right')
        limit = axes.get_xlim()[1]
        composition.plt.close(figure)
        self.assertEqual(len(bars), composition.APART_BINS)
        self.assertAlmostEqual(right, self.end, places=9)
        self.assertLess(limit, 1.1 * self.end)                     # not to the largest draw
        self.assertAlmostEqual(sum(p.get_height() for p in bars), (self.kg <= self.end).mean(), places=9)
        self.assertIn(self.beyond, numbers)

    def test_a_critical_element_panel_ends_at_its_99_5th_percentile(self):
        kinds = dict(zip(list(composition.KINDS)[:2], (0.3 * self.kg, 0.7 * self.kg)))
        figure, axes = composition.plt.subplots()
        composition.stacked_panel(axes, kinds, 'Copper (Cu)', True)
        bars = self.bars(axes)
        right = max(p.get_x() + p.get_width() for p in bars)
        heights = sum(p.get_height() for p in bars)
        numbers = axes.get_title(loc='right')
        limit = axes.get_xlim()[1]
        composition.plt.close(figure)
        self.assertAlmostEqual(right, self.end, places=9)
        self.assertLess(limit, 1.1 * self.end)
        self.assertAlmostEqual(heights, (self.kg <= self.end).mean(), places=9)   # both kinds' bars together
        self.assertIn(self.beyond, numbers)

    def test_an_overview_panel_ends_at_its_largest_rows_99_5th_percentile_nothing_piled(self):
        first, second = list(composition.KINDS)[:2]
        kinds = {first: self.kg, second: 0.1 * self.kg}
        estimated = {k: np.zeros_like(v) for k, v in kinds.items()}
        figure, axes = composition.plt.subplots()
        composition.ridge_panel(axes, kinds, estimated, 'Copper (Cu)')
        label = axes.get_xlabel()
        limit = axes.get_xlim()[1]
        # The rows from the bottom in the reverse order of KINDS: the first kind's bars stand on row 1 (at 1.05).
        heights = [p.get_height() for p in self.bars(axes) if abs(p.get_y() - 1.05) < 1e-9]
        composition.plt.close(figure)
        self.assertAlmostEqual(limit, self.end, places=9)
        # The first kind's row: the draws beyond are left out, not piled into the last bar.
        edges = np.linspace(0, self.end, 51)
        counts, _ = np.histogram(self.kg[self.kg <= self.end], bins=edges)
        self.assertEqual(len(heights), 50)
        self.assertAlmostEqual(heights[-1] / max(heights), counts[-1] / counts.max(), places=9)
        self.assertIn('beyond the axis', label)

    def test_no_words_where_nothing_lies_beyond(self):
        kg = np.repeat([1.0, 2.0, 3.0], 1000)                     # its 99.5th percentile its largest draw
        figure, axes = composition.plt.subplots()
        composition.element_panel(axes, kg, 'Copper (Cu)', True)
        numbers = axes.get_title(loc='right')
        composition.plt.close(figure)
        self.assertNotIn('beyond', numbers)

    def test_no_critical_element_title_runs_into_its_numbers(self):
        # As the element and material pages (test_no_panel_title_runs_into_its_numbers): the share held and the words
        # on the axis's end above the title's line, never over a long title.
        kinds = dict(zip(list(composition.KINDS)[:2], (np.r_[np.zeros(5000), 0.3 * self.kg],
                                                       np.r_[np.zeros(5000), 0.7 * self.kg])))
        figure, axes = composition.plt.subplots(figsize=(5.3, 4))
        composition.stacked_panel(axes, kinds, 'Neodymium and praseodymium (Nd+Pr)', True)
        figure.canvas.draw()
        renderer = figure.canvas.get_renderer()
        left, right = axes._left_title, axes._right_title
        overlap = left.get_window_extent(renderer).overlaps(right.get_window_extent(renderer))
        text = right.get_text()
        composition.plt.close(figure)
        self.assertIn('% of the draws', text)
        self.assertIn('beyond the axis', text)
        self.assertFalse(overlap)


class TestDrawsBelowZero(unittest.TestCase):
    """2026-11-01: his 02 run at 200,000 draws stopped on type 1's pages of where a material sits ("Axis limits cannot
    be NaN or Inf"): its frame's aluminium below zero in 72 of 200,000 draws (a remainder, reported, not cut), and since
    V126 those pages took the draws that are not 0, so a logarithm of a negative mass. At 2,000 draws there were none.
    Here every page that draws a distribution is drawn with such draws in it: a logarithmic axis shows the draws above
    0 only (its numbers of those draws), the linear panels as before."""

    def setUp(self):
        rng = np.random.default_rng(3)
        self.first, self.second = list(composition.KINDS)[:2]
        # The kind with the draws below zero has the smaller median, so it is the page's first row (its lowest draw
        # then first in the axis's limits), and 2 % of its draws are below zero, so that its share held shows them.
        frame = rng.triangular(0.05, 0.1, 0.2, 20_000)
        frame[:400] = -np.linspace(0.01, 1.8, 400)                 # a remainder below zero in 400 draws
        self.kinds = {self.first: frame, self.second: rng.triangular(0.5, 2.0, 4.0, 20_000)}
        self.d = types.SimpleNamespace(robot_type=1, register=['1 Robot'], listed=1)

    def test_where_a_material_sits_over_the_draws_above_0(self):
        figure = composition.sources_figure(composition.ALUMINIUM, self.kinds, self.d)
        axes = figure.axes[0]
        labels = [t.get_text() for t in axes.get_yticklabels()]
        at = {(round(t.get_position()[0], 3), round(t.get_position()[1], 2)): t.get_text() for t in axes.texts}
        limits = axes.get_xlim()
        composition.plt.close(figure)
        self.assertTrue(np.isfinite(limits).all())
        row = labels.index(composition.KINDS[self.first][0])
        self.assertEqual(row, 0)
        frame = self.kinds[self.first]
        above = frame[frame > 0]
        per, unit = composition.panel_unit(np.array([np.median(above)]))
        self.assertEqual(at[(round(composition.NUMBER_COLUMNS[0], 3), row)],
                         f'{composition.panel_number(np.median(above) / per)} {unit}')
        self.assertEqual(at[(round(composition.NUMBER_COLUMNS[2], 3), row)],
                         f'{composition.panel_number(100 * above.size / frame.size)} %')

    def test_the_linear_panels_draw_with_them(self):
        for draw_panel in (lambda a: composition.element_panel(a, self.kinds[self.first], 'Aluminium', True),
                           lambda a: composition.stacked_panel(a, self.kinds, 'Aluminium (Al)', True),
                           lambda a: composition.ridge_panel(a, self.kinds, {k: np.zeros_like(v)
                                                                             for k, v in self.kinds.items()},
                                                             'Aluminium (Al)')):
            figure, axes = composition.plt.subplots()
            draw_panel(axes)
            figure.canvas.draw()
            self.assertTrue(np.isfinite(axes.get_xlim()).all())
            composition.plt.close(figure)


class TestElementsOfInterest(unittest.TestCase):
    """EVIDENCE.md E19 point 3 (Matthias, 2026-11-02, "Yes, agree E19"), robot type 2 part by part: only the elements of
    interest; copper, nickel and the light alloys each their element whole, kind of part by kind of part; no iron,
    chromium, molybdenum, vanadium, zinc, carbon, oxygen or silicon (they stay in their steel, alloy or plastics)."""

    INTEREST = ('Li', 'B', 'Mg', 'Al', 'Ti', 'Mn', 'Co', 'Ni', 'Cu', 'Ga', 'Sr', 'Nb', 'Pd', 'Ag', 'In', 'Sn', 'Ta', 'Au',
                'Pb', 'Nd', 'Pr', 'Dy', 'Tb')

    def test_kind_by_kind(self):
        params = Params()
        params.composition.draws = 2000
        inputs = type_two_inputs_or_skip(self, params)
        d = draw(inputs, params, fixed_magnets(inputs, params.composition.draws))
        self.assertTrue({e for _, e in d.elements} <= set(self.INTEREST), {e for _, e in d.elements})
        columns, draws = d.materials
        kg = lambda kind, m: (draws[:, columns.index((kind, m))] if (kind, m) in columns  # noqa: E731
                              else np.zeros(d.n))
        for kind in composition.KINDS:
            for material, element in (('Copper', 'Cu'), ('Nickel', 'Ni')):
                own = d.elements.get((kind, element), np.zeros(d.n))
                self.assertTrue((own >= kg(kind, material) - 1e-12).all(), msg=(kind, material))
        self.assertTrue(d.elements[('battery', 'Li')].any())
        self.assertTrue(d.elements[('knees', 'Nd')].any())


class TestHousingShareOfCells(unittest.TestCase):
    """Matthias, 2026-11-02: "A, as recommended" (EVIDENCE.md E20): a battery pack no source weighs is its cells, its
    management board and its housing, the housing a share of its cells (0.207 / 0.414 / 0.859), so that it never falls
    below zero; a weighed pack's housing stays its remainder. His run of 1 November had the Booster K1 2 Ah's housing
    below zero in 44 of its draws, the Unitree R1's in 13 (VERIFICATION.md V145)."""

    @classmethod
    def setUpClass(cls):
        cls.params = Params()
        cls.params.composition.draws = 3000

    def test_every_housing_of_a_pack_not_weighed_a_share_of_its_cells_in_every_draw(self):
        inputs = inputs_or_skip(self, self.params)
        d = draw(inputs, self.params, fixed_magnets(inputs, self.params.composition.draws))
        columns, draws = d.parts
        not_weighed = {p.robot for p in inputs.apart.parts if p.name == 'Battery pack' and None in p.bounds}
        checked = []
        for robot in d.robots:
            housing = f'{robot}: Battery housing, busbars and wires'
            if robot not in not_weighed or housing not in columns:
                continue
            rows = d.robot == d.robots.index(robot)
            share = draws[rows, columns.index(housing)] / draws[rows, columns.index(f'{robot}: Battery cells')]
            self.assertTrue(np.all((share >= 0.207 - 1e-12) & (share <= 0.859 + 1e-12)), msg=robot)
            checked.append(robot)
        self.assertIn('Booster K1 2 Ah', checked)
        self.assertIn('Unitree R1', checked)

    def test_only_a_weighed_packs_housing_is_a_remainder(self):
        inputs = inputs_or_skip(self, self.params)
        d = draw(inputs, self.params, fixed_magnets(inputs, self.params.composition.draws))
        self.assertIn('Unitree G1: Battery housing, busbars and wires', d.remainders)
        self.assertNotIn('Booster K1 2 Ah: Battery housing, busbars and wires', d.remainders)


class TestRemainderBelowZeroReported(unittest.TestCase):
    """Matthias, 2026-11-02: "A, as recommended" (EVIDENCE.md E21): a robot type drawn part by part marks the draws in
    which a remainder of the robot drawn (its frame, a weighed pack's housing, a joint's structure) is below zero; 02
    reports what falls below zero with it, on the type's notes page, instead of stopping."""

    @classmethod
    def setUpClass(cls):
        cls.params = Params()
        cls.params.composition.draws = 3000

    def composed(self):
        inputs = inputs_or_skip(self, self.params)
        d = draw(inputs, self.params, fixed_magnets(inputs, self.params.composition.draws))
        category = next(c for c in inputs.base.book.categories if c.number == 1)
        return d, composition.compose_taken_apart(category, d, inputs.base.lists)

    def test_the_draws_whose_remainder_is_below_zero_are_marked(self):
        d, c = self.composed()
        columns, draws = d.parts
        expected = np.zeros(d.n, dtype=bool)
        for column in d.remainders:
            expected |= draws[:, columns.index(column)] < 0
        for values in d.structures.values():
            expected |= values < 0
        np.testing.assert_array_equal(c.remainder_below, expected)

    def test_the_notes_page_names_what_is_below_zero_with_a_remainder(self):
        d, c = self.composed()
        self.assertFalse(any('where a remainder of the robot drawn is below zero' in note
                             for note in composition.taken_apart_notes(c, d, [], self.params)
                             if not c.remainder_below.any()))
        groups = c.tables['part_groups'][1]
        frame = c.tables['part_groups'][0].index('Frame')
        groups[7, frame] = -0.1
        c.remainder_below[7] = True
        notes = ' '.join(composition.taken_apart_notes(c, d, [], self.params))
        self.assertIn('the part group Frame is below zero in', notes)
        self.assertIn('reported, not cut', notes)


class TestPagesNoLongerDrawn(unittest.TestCase):
    """Matthias, 2026-11-02: "02 removes them itself": a numbered page of a robot type that 02 no longer draws (its
    third and fourth material pages, when it now has two) is removed by its exact name; nothing else in the folder."""

    def test_the_pages_beyond_those_written_are_removed_by_name(self):
        with tempfile.TemporaryDirectory() as folder:
            names = ['t_materials_1.png', 't_materials_2.png', 't_materials_3.png', 't_materials_4.png',
                     't_alloys_1.png', 't_notes_1.png', 'u_materials_3.png', 't_materials_x.png', 'other.png']
            for name in names:
                open(os.path.join(folder, name), 'w').close()
            written = ['t_materials_1.png', 't_materials_2.png', 't_notes_1.png']
            removed = composition.remove_pages_not_drawn(folder, 't', ('notes', 'materials', 'alloys'), written)
            self.assertEqual(sorted(removed), ['t_alloys_1.png', 't_materials_3.png', 't_materials_4.png'])
            self.assertEqual(sorted(os.listdir(folder)), sorted(['t_materials_1.png', 't_materials_2.png',
                                                                 't_notes_1.png', 'u_materials_3.png',
                                                                 't_materials_x.png', 'other.png']))

    def test_02s_figures_leave_no_page_of_an_earlier_run(self):
        params = Params()
        params.composition.draws = 300
        inputs = inputs_or_skip(self, params)
        with tempfile.TemporaryDirectory() as folder:
            stale = os.path.join(folder, 'robot_type_1_overview_9.png')
            open(stale, 'w').close()
            d = draw(inputs, params, fixed_magnets(inputs, params.composition.draws))
            composition.draw_parts_figures(d, params, folder)
            self.assertFalse(os.path.exists(stale))
            self.assertTrue(os.path.exists(os.path.join(folder, 'robot_type_1_overview_1.png')))


class TestLightAlloysTheirMetal(unittest.TestCase):
    """Matthias, 2026-11-02: "I need both alloy mass and then also the Al mass. The first for the total weight and the
    last for the inflow needs", then "Yes do it as writen in A" (EVIDENCE.md E24): the aluminium, magnesium and
    titanium alloys keep their whole mass as materials; their elements Al, Mg and Ti are the metal their recipes hold,
    in every draw less than the alloy (the aluminium alloys 6061, 7075, A380, ADC12, Ti-6Al-4V: 75 to 99.9 %)."""

    def check(self, d, material, element):
        columns, draws = d.materials
        alloy = sum(draws[:, k] for k, (_, m) in enumerate(columns) if m == material)
        metal = d.by_material[(material, element)]
        held = alloy > 0
        self.assertTrue(held.any(), msg=material)
        share = metal[held] / alloy[held]
        self.assertTrue(((share > 0.75) & (share < 0.999)).all(), msg=(material, share.min(), share.max()))

    def test_type_1s_aluminium_and_titanium(self):
        params = Params()
        params.composition.draws = 3000
        inputs = inputs_or_skip(self, params)
        d = draw(inputs, params, fixed_magnets(inputs, params.composition.draws))
        self.check(d, 'Aluminium alloys', 'Al')
        self.check(d, 'Titanium alloy', 'Ti')

    def test_type_4s_magnesium(self):
        params = Params()
        params.composition.draws = 3000
        inputs = type_inputs_or_skip(self, params, 4)
        d = draw(inputs, params, fixed_magnets(inputs, params.composition.draws))
        self.check(d, 'Magnesium alloys', 'Mg')


class TestCopperSplit(unittest.TestCase):
    """Matthias, 2026-11-02: "So we have to add it to the inflow cupper, but we have to destiguish, what is fixed in
    alloys like Al aalloysa nd brass", "and what can be recycled as elemental Cu", then "Yes, build it" (EVIDENCE.md E25,
    A and B as recommended): copper recycled as copper (the element Cu), copper fixed in alloys (the aluminium alloys,
    brass, the steels, the magnets, the magnesium alloys) and the inflow, both, in every draw."""

    @classmethod
    def setUpClass(cls):
        cls.params = Params()
        cls.params.composition.draws = 2000

    def composed(self):
        inputs = inputs_or_skip(self, self.params)
        d = draw(inputs, self.params, fixed_magnets(inputs, self.params.composition.draws))
        category = next(c for c in inputs.base.book.categories if c.number == 1)
        return d, composition.compose_taken_apart(category, d, inputs.base.lists)

    def test_recycled_and_fixed_add_up_to_the_inflow_all_the_copper(self):
        d, c = self.composed()
        columns, draws = c.tables['copper']
        self.assertEqual(columns, list(composition.COPPER_COLUMNS))
        recycled, fixed, inflow = (draws[:, k] for k in range(3))
        np.testing.assert_allclose(recycled, c.column('elements', 'Cu'), rtol=1e-12)
        np.testing.assert_allclose(recycled + fixed, inflow, rtol=1e-12)
        self.assertTrue((fixed > 0).all())   # every robot's connectors hold brass, its frame an aluminium alloy
        every = sum(kg for (_, e), kg in d.recipe_elements.items() if e == 'Cu')
        np.testing.assert_allclose(inflow, every, rtol=2e-3)   # the copper's own traces: Copper counts whole
        in_alloys = sum(kg for (m, e), kg in d.fixed.items() if e == 'Cu')
        np.testing.assert_allclose(fixed, in_alloys, rtol=1e-12)
        self.assertEqual({m for m, e in d.fixed if e == 'Cu'} - set(composition.FIXED_IN_ALLOYS['Cu']), set())
        self.assertEqual(composition.draw_faults(c), [])

    def test_the_summary_and_the_cu_panel_say_so(self):
        d, c = self.composed()
        rows = [r['Name'] for r in composition.summary(c) if r['Kind'] == 'Copper']
        self.assertEqual(rows, list(composition.COPPER_COLUMNS))
        pages = composition.taken_apart_pages(c, d, [], self.params)
        texts = []
        titles = []
        for name, figure in pages:
            if '_elements_' in name:
                titles += [a.get_title(loc='left') for a in figure.axes]
            if '_means_' in name:   # the means by material on pages of their own (2026-11-02)
                texts += [t.get_text().replace('\n', ' ') for t in figure.texts]
            composition.plt.close(figure)
        self.assertIn('Copper (Cu), inflow', titles)
        self.assertTrue(any('Aluminium alloys (fixed)' in t for t in texts))
        self.assertTrue(any('Brass (fixed)' in t for t in texts))

    def test_02_writes_each_element_by_the_material_it_comes_from(self):
        # EVIDENCE.md E29 question 2 (Matthias, 2026-11-04, "Yes, agree E29", "Yes, build 03"): the split of an element
        # by the material it comes from, which 02's element pages draw, written as a table of its own for 03,
        # 'by_material', '<element>: <material>', the copper fixed in an alloy '<element>: <material> (fixed in
        # alloys)'. Each element's columns add up to it, the copper's fixed ones to the copper fixed in alloys.
        d, c = self.composed()
        with tempfile.TemporaryDirectory() as folder:
            composition.write_taken_apart(d, folder)
            draws = np.load(os.path.join(folder, 'by_material.npy')).astype(np.float64)
            with open(os.path.join(folder, 'by_material.txt'), encoding='utf-8') as file:
                columns = file.read().splitlines()
        self.assertIn('by_material', composition.APART_TABLES)
        self.assertEqual(draws.shape, (self.params.composition.draws, len(columns)))
        mark = composition.FIXED_MARK
        recovered = [k for k, name in enumerate(columns) if not name.endswith(mark)]
        fixed = [k for k, name in enumerate(columns) if name.endswith(mark)]
        self.assertTrue(fixed)
        for symbol in c.tables['elements'][0]:
            own = [k for k in recovered if columns[k].split(': ', 1)[0] == symbol]
            np.testing.assert_allclose(draws[:, own].sum(axis=1), c.column('elements', symbol), rtol=1e-5, atol=1e-9,
                                       err_msg=symbol)
        self.assertEqual({columns[k].split(': ', 1)[0] for k in fixed}, {'Cu'})
        np.testing.assert_allclose(draws[:, fixed].sum(axis=1), c.column('copper', 'Cu fixed in alloys'), rtol=1e-5)
        self.assertIn(f'Cu: Brass{mark}', columns)
        self.assertIn('Cu: Copper', columns)


class TestNoTextOverData(unittest.TestCase):
    """Matthias, 2026-11-02: "Cupper is bad. Text over the figures. Build a rule, which prevents this. The figure is
    first and not the text Tex can go to other places": on every page 02 draws of a robot type taken apart (its notes,
    element, material and alloys pages, its two figures of where its critical elements sit, where each material sits),
    no text inside a chart lies over its bars or lines (texts_over_data)."""

    def test_no_page_has_text_over_its_data(self):
        params = Params()
        params.composition.draws = 2000
        inputs = inputs_or_skip(self, params)
        d = draw(inputs, params, fixed_magnets(inputs, params.composition.draws))
        category = next(c for c in inputs.base.book.categories if c.number == 1)
        c = composition.compose_taken_apart(category, d, inputs.base.lists)
        found = []
        for name, figure in (composition.taken_apart_pages(c, d, [], params) + composition.parts_figure_pages(d)
                             + composition.sources_pages(d)):
            found += [f'{name}: {text}' for text in composition.texts_over_data(figure)]
            composition.plt.close(figure)
        self.assertEqual(found, [])


class TestHydraulicActuators(unittest.TestCase):
    """EVIDENCE.md E27.7 (Matthias, 2026-11-04, "Yes, agree E27.7", "Yes, build it"): a hydraulic actuator's body, rod
    and seals the remainder of its place's actuators less their valves, boards and sensors, in every draw, as the
    battery housing is the pack's; the oil its volume times its density; a robot without an electric joint drawn."""

    @classmethod
    def setUpClass(cls):
        cls.params = Params()
        cls.params.composition.draws = 3000

    def drawn(self, robot_type: int):
        inputs = type_inputs_or_skip(self, self.params, robot_type)
        return inputs, draw(inputs, self.params, fixed_magnets(inputs, self.params.composition.draws))

    def test_the_body_the_actuators_less_their_valves_boards_and_sensors(self):
        for robot_type, robot in ((6, 'IHMC Nadia ISA v2'), (6, 'IHMC Nadia ISA v5'),
                                  (5, 'Atlas HD ISA v2'),
                                  (5, 'Atlas HD ISA v5 knees')):
            inputs, d = self.drawn(robot_type)
            columns, draws = d.parts
            rows = d.robot == d.robots.index(robot)
            whole = {p.name.rsplit(', ', 1)[1]: p for p in inputs.apart.parts
                     if p.robot == robot and p.computed.startswith(schemas.ACTUATORS_WHOLE)}
            self.assertTrue(whole, msg=robot)
            for place, p in whole.items():
                body = f'{robot}: Actuator bodies, rods and seals, {place}'
                inside = [f'{robot}: {name}, {place}' for name in ('Servo valves', 'Actuator boards',
                                                                   'Actuator position sensors',
                                                                   'Actuator pressure sensors')]
                total = draws[rows, columns.index(body)] + sum(draws[rows, columns.index(c)] for c in inside)
                low, high = p.count * p.bounds[0], p.count * p.bounds[2]
                self.assertTrue(np.all((total >= low - 1e-9) & (total <= high + 1e-9)), msg=(robot, place))
                self.assertTrue(np.all(draws[rows, columns.index(body)] > 0), msg=(robot, place))
                self.assertIn(body, d.remainders)

    def test_the_oil_its_volume_times_its_density(self):
        inputs, d = self.drawn(6)
        columns, draws = d.parts
        for robot in ('IHMC Nadia ISA v2', 'IHMC Nadia ISA v5'):
            oil = draws[d.robot == d.robots.index(robot), columns.index(f'{robot}: Hydraulic oil')]
            self.assertTrue(np.all((oil >= 0.25 * 0.86 - 1e-12) & (oil <= 0.75 * 0.88 + 1e-12)), msg=robot)

    def test_a_robot_without_an_electric_joint_drawn(self):
        inputs, d = self.drawn(5)
        robot = 'Atlas HD ISA v5 knees'
        self.assertFalse([j for j in inputs.apart.joints if j.robot == robot])
        columns, draws = d.parts
        rows = d.robot == d.robots.index(robot)
        self.assertTrue(np.all(np.abs(draws[rows].sum(axis=1) - d.mass[rows]) < 1e-9 * d.mass[rows]))
        self.assertIn(f'{robot}: Hydraulic power unit', columns)

    def test_the_atlas_olds_frame_never_below_zero(self):
        # Matthias, 2026-11-04, "Yes, knees only" (EVIDENCE.md E27.8): with the 1.6 kg actuators at all 28 joints its
        # frame fell below zero in 2.1 % of its draws (V161); at its knees only, in none.
        inputs, d = self.drawn(5)
        columns, draws = d.parts
        for robot in ('Atlas HD ISA v2', 'Atlas HD ISA v5 knees'):
            frame = draws[d.robot == d.robots.index(robot), columns.index(f'{robot}: Frame: titanium and aluminium')]
            self.assertTrue(np.all(frame > 0), msg=robot)


class TestJointsEstimatedWithoutTorque(unittest.TestCase):
    """Matthias, 2026-11-04, "Yes, do the package" (V163): the notes pages name a robot under "the joints' masses from
    their torques" only where an estimated body joint has a stated torque; one whose estimated body joints have none
    (Neo1's forearms, Nadia's pelvis) under "the joints' masses estimated, no torque stated"."""

    TORQUES = "the joints' masses from their torques"
    NO_TORQUE = "the joints' masses estimated, no torque stated"

    def test_the_notes_of_types_5_and_6(self):
        params = Params()
        params.composition.draws = 300
        for robot_type, robots in ((6, ['IHMC Nadia ISA v2', 'IHMC Nadia ISA v5']),):
            inputs = type_inputs_or_skip(self, params, robot_type)
            drawn = [v for r in inputs.robots for v in schemas.versions(r.taken_apart)]
            said = composition.on_estimates(inputs.apart, drawn)
            for robot in robots:
                self.assertIn(robot, said.get(self.NO_TORQUE, []), msg=robot)
        # Neo1, since E30 (2026-11-05) an outlier and not drawn: the words for its rows, in type 3's file, where they
        # stay.
        said = composition.on_estimates(type_inputs_or_skip(self, params, 5).files[3], ['NeodraDynamics Neo1'])
        self.assertIn('NeodraDynamics Neo1', said.get(self.NO_TORQUE, []))
        self.assertNotIn('NeodraDynamics Neo1', said.get(self.TORQUES, []))
        self.assertIn('DEEP Robotics DR02', composition.on_estimates(
            type_inputs_or_skip(self, params, 5).apart, ['DEEP Robotics DR02']).get(self.TORQUES, []))

