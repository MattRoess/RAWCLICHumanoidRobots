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

import importlib.util
import os
import sys
import tempfile
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


def modes(rng, low, mode, high):
    """02's triangles of the register's masses, each at its mode."""
    return np.asarray(mode, dtype=float).copy()


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

    def test_each_robot_of_the_register_is_drawn_equally_often(self):
        inputs, d = self.drawn()
        self.assertEqual(len(d.register), 31)
        self.assertEqual(len(d.robots), 32)
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
        self.assertEqual(len(shared), 17)
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
        with mock.patch.object(composition, 'triangle', at_mode), mock.patch.object(composition, 'triangles', modes):
            return draw(inputs, self.params, fixed_magnets(inputs, self.params.composition.draws))

    def element(self, d, robot: str, kind: str, element: str) -> np.ndarray:
        return d.elements.get((kind, element), np.zeros(d.n))[d.robot == d.robots.index(robot)]

    def part(self, d, column: str) -> np.ndarray:
        columns, draws = d.parts
        robot = column.split(': ')[0]
        return draws[d.robot == d.robots.index(robot), columns.index(column)]

    def test_the_g1s_copper_in_its_cables(self):
        d = self.at()
        # Cables: 6 m × (2 × 0.82 + 2 × 0.13) mm2 × 8.96 g/cm3 = 102.144 g; 46 mated XT30 (2+2) × 2.12 g × 0.35 of
        # contacts × 0.62 copper of their brass = 21.16184 g (2026-10-29, "Yes, enter all", EVIDENCE.md E5.22: the pair
        # 1.1224 g + 1 g, its contacts brass); 4 capacitor buffer boards × 5 cm2 × 0.56 g/cm2 × 0.20 = 2.24 g.
        np.testing.assert_allclose(self.element(d, 'Unitree G1', 'cables', 'Cu'), 0.12554584, rtol=1e-9)

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
                                            for m in ('Aluminium', 'Plastics', composition.ELECTRONICS))
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
        np.testing.assert_allclose(self.element(d, 'Unitree G1', 'head', 'Br'), 0.088 * rest, rtol=1e-9)

    def test_type_1s_electronics_wholly_in_its_elements(self):
        # Point 3b: the boards' rest in the elements, the sensors' housings their own materials (point 3c), a joint's
        # encoders inside its driver board: every robot's electronics are in the elements, to the compounds' rounding.
        inputs = inputs_or_skip(self, self.params)
        d = self.at()
        category = next(c for c in inputs.base.book.categories if c.number == 1)
        c = composition.compose_taken_apart(category, d, inputs.base.lists)
        rows = {r['Name']: r for r in composition.summary(c) if r['Kind'] == 'Material'}
        self.assertEqual(rows[composition.ELECTRONICS]['In the elements'], 'Yes')

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
        np.testing.assert_allclose(self.element(d, 'Unitree G1', 'hips', 'Mo'), 1.8396537e-3, rtol=1e-6)

    def test_each_robot_at_its_modes_weighs_its_own_mass(self):
        inputs = inputs_or_skip(self, self.params)
        d = self.at()
        for k, robot in enumerate(d.robots):
            mass = inputs.apart.constants[robot][composition.ROBOT_MASS][1][1]
            np.testing.assert_allclose(d.mass[d.robot == k], mass, rtol=1e-12, err_msg=robot)

    def test_a_robot_without_joint_torques_and_battery_data_at_its_modes(self):
        # The Noetix E1, 40 kg (E5.17): its joint modules 49 % of it, 19.6 kg; its shell 11.5 %, 4.6 kg; its battery
        # 12 Wh per kg of robot, 480 Wh: cells 480 / 241.5 = 1.987578 kg, the pack 480 / 164 = 2.926829 kg, its housing
        # the pack less the cells and its management board (60 cm2 × 0.56 g/cm2 = 33.6 g): 0.905651 kg.
        d = self.at()
        columns, draws = d.parts
        rows = d.robot == d.robots.index('Noetix E1')
        joints = sum(draws[rows, i] for i, c in enumerate(columns) if c.startswith('Noetix E1:') and 'joints)' in c)
        np.testing.assert_allclose(joints, 19.6, rtol=1e-9)
        np.testing.assert_allclose(self.part(d, 'Noetix E1: Shell: plastics'), 4.6, rtol=1e-9)
        np.testing.assert_allclose(self.part(d, 'Noetix E1: Battery cells'), 480 / 241.5, rtol=1e-9)
        np.testing.assert_allclose(self.part(d, 'Noetix E1: Battery housing, busbars and wires'),
                                   480 / 164 - 480 / 241.5 - 0.0336, rtol=1e-9)


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
        magnets = materials[g1, columns.index(('knees', 'Magnets (NdFeB)'))]
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
        import matplotlib.image
        from matplotlib.text import Text
        params = Params()
        params.composition.draws = 300
        inputs = inputs_or_skip(self, params)
        d = draw(inputs, params, fixed_magnets(inputs, params.composition.draws))
        category = next(c for c in inputs.base.book.categories if c.number == 1)
        c = composition.compose_taken_apart(category, d, inputs.base.lists)
        with tempfile.TemporaryDirectory() as folder:
            params.output.parts_dir = os.path.join(folder, 'data')
            pages = composition.parts_figure_pages(d)
            self.assertEqual([name for name, _ in pages if '_notes_' not in name], list(composition.parts_figures(1)))
            # 02's pages of robot type 1: its notes, its elements and its materials nine a page; where each material
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


class TestElementsNotShown(unittest.TestCase):
    """Matthias, 2026-10-29: "Hydrogene and Oxygen have to go you should know this. Same for F, and N", then "S and P
    can go also Na": type 1's element pages leave them out, its draws keep them."""

    def test_type_1s_pages_leave_out_hydrogen_nitrogen_oxygen_and_fluorine(self):
        params = Params()
        params.composition.draws = 300
        inputs = inputs_or_skip(self, params)
        d = draw(inputs, params, fixed_magnets(inputs, params.composition.draws))
        category = next(c for c in inputs.base.book.categories if c.number == 1)
        c = composition.compose_taken_apart(category, d, inputs.base.lists)
        for symbol in ('H', 'N', 'O', 'F', 'Na', 'P', 'S'):
            self.assertTrue(c.column('elements', symbol).any(), msg=symbol)   # in the draws
        pages = composition.taken_apart_pages(c, d, [], params)
        titles = [axes.get_title(loc='left') for _, figure in pages for axes in figure.axes]
        notes = ' '.join(t.get_text() for name, figure in pages if '_notes_' in name for t in figure.texts)
        for _, figure in pages:
            composition.plt.close(figure)
        for name in ('Hydrogen (H)', 'Nitrogen (N)', 'Oxygen (O)', 'Fluorine (F)', 'Sodium (Na)', 'Phosphorus (P)',
                     'Sulfur (S)'):
            self.assertNotIn(name, titles)
        self.assertIn('Copper (Cu)', titles)
        self.assertIn('hydrogen, nitrogen, oxygen, fluorine, sodium, phosphorus and sulfur are not shown',
                      ' '.join(notes.split()).lower())


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
        for symbol in composition.shown_elements(c.tables['elements'][0], params):
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
        for symbol in composition.shown_elements(c.tables['elements'][0], self.params):
            kg = c.column('elements', symbol)
            held = kg > 0
            label = composition.element_label(symbol)
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
        self.assertIn('V', partly)
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
            texts = ' '.join(t.get_text() for t in axes.texts)
            share = axes.get_title(loc='right')
            composition.plt.close(figure)
            self.assertNotIn(' median 0 ', texts, msg=symbol)
            held = total > 0
            if held.all():
                self.assertEqual(share, '', msg=symbol)
                continue
            partly.append(symbol)
            self.assertEqual(share, f'in {composition.panel_number(100 * held.mean())} % of the draws')
            per, unit = composition.panel_unit(total[held])
            self.assertIn(f' median {composition.panel_number(np.median(total[held]) / per)} {unit}', texts)
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
        texts = [t.get_text() for t in axes.texts]
        self.assertTrue(any('median' in t for t in texts) and any('mean' in t for t in texts), msg=texts)
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

    def test_the_pages_show_copper_the_magnets_each_steel_and_each_aluminium_alloy(self):
        _, d = self.drawn()
        titles = [title for title, *_ in composition.material_panels(d)]
        for wanted in ('Copper', 'Permanent magnets', 'Magnets, grade class SH',
                       'Gear steel 20CrMnTi', 'Bearing steel GCr15', 'Alloy steel 42CrMo4', 'Electrical steel M19',
                       'Electrical steel M27', 'Aluminium 6061', 'Aluminium 7075', 'Plastics',
                       'Battery cells, NMC (cylindrical)', 'Nickel strips, battery'):
            self.assertIn(wanted, titles)
        self.assertNotIn('Steel', titles)        # steel only by its grades
        self.assertNotIn('Aluminium', titles)    # aluminium only by its alloys
        sources = [name for name, _ in composition.sources_pages(d)]
        for name in ('Copper', 'Permanent_magnets', 'Gear_steel_20CrMnTi', 'Aluminium_7075'):
            self.assertIn(os.path.join(composition.SOURCES_FOLDER, f'{name}.png'), sources)
        self.assertFalse(any('grade_class' in name for name in sources))   # the classes on the pages only

    def test_a_material_held_in_some_draws_shows_the_draws_that_hold_it(self):
        # Matthias, 2026-10-29: "If there is nothing then show nothing. If it is just a bit and a large 0 then show me
        # the distribution": the 440C of the X1's pins alone, held in about 1 of 31 draws (since 2026-10-29, "Yes,
        # enter all", every robot holds brass, the contacts of its connectors).
        import matplotlib.pyplot as plt
        _, d = self.drawn()
        title, _, _, kinds = next(p for p in composition.material_panels(d) if p[0] == 'Stainless steel 440C')
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
        with mock.patch.object(composition, 'triangle', at_mode), mock.patch.object(composition, 'triangles', modes):
            d = draw(inputs, self.params, fixed_magnets(inputs, self.params.composition.draws))
        aluminium = sum(kg for (_, m, _), kg in d.details.items() if m == 'Aluminium')
        alloy = lambda name: sum(kg for (_, m, x), kg in d.details.items() if m == 'Aluminium' and x == name)  # noqa
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
        self.assertIn('Frame and shell: Aluminium: Aluminium 6061', columns)
        self.assertIn('Knee joints: Magnets (NdFeB): UH', columns)


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
    recipes, the Fourier robots' Ethernet line by hand; the robots not yet taken apart counted, so that its draws for
    stock-and-flow come from the workbook until all are (Q2, Q4)."""
    BATCHES = [25, 47, 53, 69, 80, 98, 116, 117, 119, 120, 121, 123, 132, 134, 135, 144, 151, 153, 157, 158, 163, 170,
               171, 176, 177, 180, 199, 203, 210, 216, 221, 222, 223, 224, 229, 232, 244, 256, 265, 271, 272, 276, 285, 290,
               294, 297, 298, 299, 300, 302, 323, 326, 352]

    @classmethod
    def setUpClass(cls):
        cls.params = Params()
        cls.params.composition.draws = 3000

    def test_its_robots_and_those_not_yet_taken_apart(self):
        inputs = type_two_inputs_or_skip(self, self.params)
        self.assertEqual([r.number for r in inputs.robots], self.BATCHES)
        self.assertEqual([r.number for r in inputs.left_out], [329])       # the Xialan S0, no mass stated
        self.assertEqual((len(inputs.later), inputs.listed, inputs.robot_type), (43, 97, 2))

    def test_drawn_over_its_robots_each_as_often(self):
        inputs = type_two_inputs_or_skip(self, self.params)
        d = draw(inputs, self.params, fixed_magnets(inputs, self.params.composition.draws))
        self.assertEqual((d.robot_type, composition.lead(d)), (2, 'Robot type 2, 53 of its 97 robots'))
        n, p = d.n, 1 / 53
        tolerance = 4 * np.sqrt(p * (1 - p) / n)
        for k in range(53):
            self.assertAlmostEqual((d.register_robot == k).mean(), p, delta=tolerance, msg=d.register[k])
        for version in ('Fourier GR-1 one camera', 'Fourier GR-1 two cameras', 'Unitree H2-X Core i7',
                        'Unitree H2-X Orin NX', 'Walker Tienkung Vision', 'Walker Tienkung Embodied'):
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
        # Q3: type 2's own rows of the element recipes.
        inputs = type_two_inputs_or_skip(self, self.params)
        shared = composition.Shared(inputs, self.params, fixed_magnets(inputs, 10), np.random.default_rng(5), 10)
        self.assertEqual(shared.recipe_name, {'Aluminium': 'Aluminium, robot type 2, Aluminum alloys',
                                              'Plastics': 'Plastics, robot type 2, Engineering plastics'})
        d = draw(inputs, self.params, fixed_magnets(inputs, self.params.composition.draws))
        self.assertEqual(d.aluminium, 'die-cast 0 to 40 %, of the wrought rest 7075 39 to 97 % and 6061')

    def test_the_copper_of_its_cables_by_hand(self):
        inputs = type_two_inputs_or_skip(self, self.params)
        with mock.patch.object(composition, 'triangle', at_mode), mock.patch.object(composition, 'triangles', modes):
            d = draw(inputs, self.params, fixed_magnets(inputs, self.params.composition.draws))

        def copper(robot):
            return d.elements[('cables', 'Cu')][d.robot == d.robots.index(robot)]

        # The GR-2: 14 m × (2 × 0.82 + 8 × 0.205) mm2 × 8.96 g/cm3 = 411.4432 g, two power conductors and an Ethernet
        # line of eight (E6.8 point 9); 62 mated XT30 × 2.12 g × 0.35 of contacts × 0.62 copper of their brass =
        # 28.52248 g. The H2: 14 m × (2 × 0.82 + 2 × 0.13) mm2 × 8.96 = 238.336 g, and the same 28.52248 g.
        np.testing.assert_allclose(copper('Fourier GR-2'), 0.43996568, rtol=1e-9)
        np.testing.assert_allclose(copper('Unitree H2'), 0.26685848, rtol=1e-9)


if __name__ == '__main__':
    unittest.main()
