"""
Tests of robot type 1 taken apart: its drawing over its robots in 02_composition.py, and the two figures of
04_parts_taken_apart.py drawn from what 02 writes.

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

Matthias, 2026-10-28: "Yes, build steps 5 and 6: stage 04 and its two approved figures, tests first, tried in a
sandbox with few draws", with his answers A to E (documentation/claude/HANDOVER.md, 2026-10-28); then, the same day,
"Yes in 02 it is all type 1 in.!" and "Yes, code it in 02": the drawing moved to 02, over all the register's robots of
type 1. The tests draw the real parts file and the sibling projects' files where they lie, a few hundred times, over a
register of the three robots taken apart (and, where a test needs it, one robot of 50 kg), into temporary folders:
press Run, nothing in the project is changed. Where a file is not on disk, the test that needs it is skipped and says
so.

The hand calculations draw every triangle at its mode (the test replaces 02's `triangle` by one that returns the mode)
and give the magnets fixed element fractions, so that one robot can be added up by hand from the data file's modes
(EVIDENCE.md E2.8 and E2.8b).
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


apart = load('parts_taken_apart', '04_parts_taken_apart.py')
composition = sys.modules['composition']
schemas = composition.schemas

# A robot of the register of type 1 that is not taken apart, of 50 kg (49 to 51): drawn with the parts of one of the
# three robots taken apart, scaled to its mass.
HEAVY = schemas.RegisterRobot(row=0, number=900, name='Heavy robot', maker='Tests', mass=(49.0, 50.0, 51.0), types=(1,),
                              types_text='1', form='legs', entry='', taken_apart='')

# The magnets' element fractions the hand calculations use, the same for every grade class: neodymium 0.24,
# praseodymium 0.06, dysprosium 0.05, boron 0.01, iron the remainder.
FIXED_MAGNET = {'Nd': 0.24, 'Pr': 0.06, 'Dy': 0.05, 'B': 0.01, 'Fe': 0.64}


def inputs_or_skip(test: unittest.TestCase, params: Params, extra: tuple = ()):
    """02's inputs of robot type 1 taken apart, over a register of the three robots taken apart (each its own mass
    range) and `extra`; or the test skipped where a file is not on disk."""
    files = [absolute(params.data.workbook), absolute(params.data.shared_lists), absolute(params.data.element_recipes),
             absolute(params.data.parts_taken_apart), params.data.vehicle_pcb_composition,
             params.data.vehicle_sensor_composition, params.data.data_center_element_composition]
    missing = [f for f in files if not os.path.exists(f)]
    if missing:
        test.skipTest(f'not on disk: {", ".join(missing)}')
    base = composition.read_inputs(params)
    parts = schemas.read_parts_taken_apart(absolute(params.data.parts_taken_apart))
    register = [schemas.RegisterRobot(row=0, number=k + 1, name=name, maker=robot.maker,
                                      mass=parts.constants[name][composition.ROBOT_MASS][1], types=(1,),
                                      types_text='1', form='legs', entry='', taken_apart=name)
                for k, (name, robot) in enumerate(parts.robots.items())]
    return composition.read_apart_inputs(params, base, register + list(extra))


def draw(inputs, params: Params, magnets: dict):
    """Robot type 1 drawn by 02 over the register of `inputs`."""
    return composition.draw_type_one(inputs, params, magnets)


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

    def drawn(self, extra=()):
        inputs = inputs_or_skip(self, self.params, extra)
        return inputs, draw(inputs, self.params, fixed_magnets(inputs, self.params.composition.draws))

    def test_each_robot_is_drawn_about_a_third_of_the_time(self):
        _, d = self.drawn()
        self.assertEqual(d.robots, ['Unitree G1', 'AgiBot X1', 'Fourier N1'])
        self.assertEqual(d.register, ['1 Unitree G1', '2 AgiBot X1', '3 Fourier N1'])
        shares = np.bincount(d.robot, minlength=3) / d.n
        # Four standard errors of a share of 1/3 in 3,000 draws: 0.034.
        for share in shares:
            self.assertAlmostEqual(share, 1 / 3, delta=4 * np.sqrt(1 / 3 * 2 / 3 / d.n))
        np.testing.assert_array_equal(d.register_robot, d.robot)   # each robot taken apart takes its own parts

    def test_a_robot_taken_apart_weighs_its_own_mass_within_its_range(self):
        _, d = self.drawn()
        np.testing.assert_array_equal(d.varied, d.own)
        ranges = {'Unitree G1': (34, 36), 'AgiBot X1': (32, 35.3), 'Fourier N1': (38, 40)}
        for k, name in enumerate(d.robots):
            own = d.own[d.robot == k]
            self.assertTrue(np.all((own >= ranges[name][0]) & (own <= ranges[name][1])), msg=name)

    def test_a_robot_of_the_register_takes_the_parts_of_each_robot_taken_apart_and_its_own_mass(self):
        _, d = self.drawn((HEAVY,))
        heavy = d.register_robot == 3
        self.assertAlmostEqual(heavy.mean(), 1 / 4, delta=4 * np.sqrt(1 / 4 * 3 / 4 / d.n))
        self.assertTrue(np.all((d.varied[heavy] >= 49) & (d.varied[heavy] <= 51)))
        shares = np.bincount(d.robot[heavy], minlength=3) / heavy.sum()
        for share in shares:
            self.assertAlmostEqual(share, 1 / 3, delta=4 * np.sqrt(1 / 3 * 2 / 3 / heavy.sum()))

    def test_the_materials_of_every_draw_add_up_to_its_mass(self):
        _, d = self.drawn((HEAVY,))
        columns, draws = d.materials
        np.testing.assert_allclose(draws.sum(axis=1), d.varied, rtol=1e-9)
        columns, draws = d.parts
        np.testing.assert_allclose(draws.sum(axis=1), d.varied, rtol=1e-9)

    def test_nothing_is_cut_where_a_remainder_falls_below_zero(self):
        # The frame, the battery housing and the joints' structure (where a joint's mass is stated) are remainders:
        # below zero they are reported, never cut (point 2).
        inputs, d = self.drawn()
        below = composition.below_zero(d)
        expected = {f'{r}: {p}' for r in d.robots for p in ('Frame', 'Battery housing, busbars and wires')}
        expected |= {f'{j.robot}: {j.name} structure' for j in inputs.apart.joints if None not in j.module_mass}
        self.assertEqual(set(below), expected)
        for share in below.values():
            self.assertTrue(0 <= share <= 1)

    def test_a_joint_whose_mass_is_stated_weighs_that_mass(self):
        # Matthias, 2026-10-28: "Yes, build it" (VERIFICATION.md V57): each X1 and N1 joint adds up to its drawn module
        # mass, its structure the explicit remainder. So, at the robot's own mass, its joints lie between the sums of
        # their stated minima and maxima in every draw (before, the X1's reached 1.11 times its stated modes).
        inputs, d = self.drawn((HEAVY,))
        columns, draws = d.parts
        for k, robot in enumerate(d.robots):
            stated = [j for j in inputs.apart.joints if j.robot == robot]
            if any(None in j.module_mass for j in stated):
                continue
            rows = d.robot == k
            joints = sum(draws[rows, i] for i, c in enumerate(columns) if c.startswith(robot) and c.endswith('joints)'))
            at_own = joints / (d.varied[rows] / d.own[rows])
            low = sum(j.count * j.module_mass[0] for j in stated)
            high = sum(j.count * j.module_mass[2] for j in stated)
            with self.subTest(robot=robot):
                self.assertTrue(np.all((at_own >= low - 1e-9) & (at_own <= high + 1e-9)),
                                msg=f'{at_own.min():.3f} to {at_own.max():.3f} kg against {low:.3f} to {high:.3f}')

    def test_robot_type_1_as_02_writes_every_robot_type_adds_up(self):
        # Its materials (Not allocated 0), part groups and body regions add up to its mass, its elements to the
        # kilograms of the materials they come from, nothing below zero but where 02 allows it (draw_faults).
        inputs, d = self.drawn((HEAVY,))
        category = next(c for c in inputs.base.book.categories if c.number == 1)
        c = composition.compose_type_one(category, d, inputs.base.lists)
        self.assertEqual(composition.draw_faults(c), [])
        self.assertFalse(c.column('materials', schemas.NOT_ALLOCATED).any())
        np.testing.assert_allclose(c.column('total', 'Total'), d.varied)


class TestHandCalculations(unittest.TestCase):
    """Point 6: one robot at its modes, added up by hand from the data file (EVIDENCE.md E2.8, E2.8b)."""

    @classmethod
    def setUpClass(cls):
        cls.params = Params()
        cls.params.composition.draws = 300

    def at(self, extra=()):
        inputs = inputs_or_skip(self, self.params, extra)
        with mock.patch.object(composition, 'triangle', at_mode), mock.patch.object(composition, 'triangles', modes):
            return draw(inputs, self.params, fixed_magnets(inputs, self.params.composition.draws))

    def element(self, d, robot: str, kind: str, element: str) -> np.ndarray:
        return d.elements.get((kind, element), np.zeros(d.n))[d.robot == d.robots.index(robot)]

    def test_the_g1s_copper_in_its_cables(self):
        d = self.at()
        # Cables: 6 m × (2 × 0.82 + 2 × 0.13) mm2 × 8.96 g/cm3 = 102.144 g; 46 XT30 × 3 g × 0.35 = 48.3 g;
        # 4 capacitor buffer boards × 5 cm2 × 0.56 g/cm2 × 0.20 = 2.24 g.
        np.testing.assert_allclose(self.element(d, 'Unitree G1', 'cables', 'Cu'), 0.152684, rtol=1e-9)

    def test_the_g1s_gold_in_its_hips(self):
        d = self.at()
        # Six hip joints, large: a driver board of 22.9 cm2 × 3.56 = 81.524 cm2 × 0.02 mg/cm2 (car PE_HVS) each,
        # 9.78288 mg; two encoders each, 12 × 0.06 mg (car angle sensor) = 0.72 mg.
        np.testing.assert_allclose(self.element(d, 'Unitree G1', 'hips', 'Au'), 10.50288e-6, rtol=1e-9)

    def test_the_g1s_neodymium_in_its_hips(self):
        d = self.at()
        # Six rotors of 42.9 g × 1.78 (the large joint), 90 % NdFeB, 24 % Nd: 98.965152 g; twelve encoders × 20 mg.
        np.testing.assert_allclose(self.element(d, 'Unitree G1', 'hips', 'Nd'), 0.099205152, rtol=1e-9)

    def test_a_robot_at_its_modes_weighs_its_own_mass(self):
        d = self.at()
        for k, mass in enumerate((35, 33, 39)):
            np.testing.assert_allclose(d.varied[d.robot == k], mass, rtol=1e-12)

    def test_what_follows_mass_is_scaled_and_the_rest_is_not(self):
        # Answer B, "Joints whole, as listed": a robot of the register of 50 kg drawn with the G1's parts has the G1's
        # hip joints (whole) 50 / 35 times as heavy, its two hip fans (2 × 0.01 kg, not scaled) the same; its head
        # (sensors and a board) the same.
        d = self.at((HEAVY,))
        g1 = d.robots.index('Unitree G1')
        itself, heavy = (d.robot == g1) & (d.register_robot == g1), (d.robot == g1) & (d.register_robot == 3)
        self.assertTrue(itself.any() and heavy.any())
        fans = 2 * 0.01
        hips, head = composition.kind_kg(d, 'hips'), composition.kind_kg(d, 'head')
        np.testing.assert_allclose(hips[heavy], (hips[itself][0] - fans) * 50 / 35 + fans, rtol=1e-9)
        np.testing.assert_allclose(head[heavy], head[itself][0], rtol=1e-9)


class TestGradesByHeat(unittest.TestCase):
    """Matthias, 2026-10-28: "Heat has to matter and so the distribution will be different depending on the joint",
    then "Accept as proposed" (EVIDENCE.md E2.11): each heat group's grade class drawn by its probabilities, the classes
    tied within a draw (one draw decides how hot the robot is built for, every joint takes its class at that point)."""

    # Dysprosium by class, different for each, so that a joint's dysprosium tells which class it drew.
    DY = {'H': 0.03, 'SH': 0.05, 'UH': 0.07, 'EH': 0.09}

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
        inputs = inputs_or_skip(self, params, (HEAVY,))
        d = draw(inputs, params, fixed_magnets(inputs, params.composition.draws))
        category = next(c for c in inputs.base.book.categories if c.number == 1)
        c = composition.compose_type_one(category, d, inputs.base.lists)
        with tempfile.TemporaryDirectory() as folder:
            params.output.parts_dir = os.path.join(folder, 'data')
            composition.write_taken_apart(d, params.output.parts_dir)
            pages = apart.figure_pages(apart.read_taken(params))
            self.assertEqual([name for name, _ in pages], list(apart.FIGURES))
            # 02's pages of robot type 1: its notes, then its elements nine a page.
            pages += composition.type_one_pages(c, d, [], params)
            for name, figure in pages:
                figure.canvas.draw()
                sizes = [t.get_fontsize() for t in figure.findobj(Text) if t.get_visible() and t.get_text().strip()]
                path = os.path.join(folder, name)
                figure.savefig(path, dpi=params.output.dpi, facecolor='white')
                apart.plt.close(figure)
                height, width = matplotlib.image.imread(path).shape[:2]
                scale = min(self.SCREEN[0] / width, self.SCREEN[1] / height)
                smallest = min(sizes) * params.output.dpi / 72 * scale
                self.assertGreaterEqual(smallest, self.SMALLEST_PX,
                                        msg=f'{name}: {width} × {height} px, smallest text {smallest:.1f} px')


class TestElementsNotShown(unittest.TestCase):
    """Matthias, 2026-10-29: "Hydrogene and Oxygen have to go you should know this. Same for F, and N": type 1's
    element pages leave them out, its draws keep them."""

    def test_type_1s_pages_leave_out_hydrogen_nitrogen_oxygen_and_fluorine(self):
        params = Params()
        params.composition.draws = 300
        inputs = inputs_or_skip(self, params)
        d = draw(inputs, params, fixed_magnets(inputs, params.composition.draws))
        category = next(c for c in inputs.base.book.categories if c.number == 1)
        c = composition.compose_type_one(category, d, inputs.base.lists)
        for symbol in ('H', 'N', 'O', 'F'):
            self.assertTrue(c.column('elements', symbol).any(), msg=symbol)   # in the draws
        pages = composition.type_one_pages(c, d, [], params)
        titles = [axes.get_title(loc='left') for _, figure in pages[1:] for axes in figure.axes]
        notes = ' '.join(t.get_text() for t in pages[0][1].texts)
        for _, figure in pages:
            apart.plt.close(figure)
        for name in ('Hydrogen (H)', 'Nitrogen (N)', 'Oxygen (O)', 'Fluorine (F)'):
            self.assertNotIn(name, titles)
        self.assertIn('Copper (Cu)', titles)
        self.assertIn('hydrogen, nitrogen, oxygen and fluorine are not shown', ' '.join(notes.split()).lower())


class TestCentre(unittest.TestCase):
    """Matthias, 2026-10-28: "Showing the mean is wrong. It is not a good measure. Use the median or show boths", and
    his answer "Both, median first": the median a solid line, the mean a dotted one, each with its number."""

    VALUES = np.random.default_rng(3).lognormal(0.0, 1.0, 5000)   # kg, skewed: its mean well above its median

    def lines(self, axes, style: str) -> list:
        return [line for line in axes.get_lines() if line.get_linestyle() == style]

    def test_the_element_panel_marks_the_median_solid_and_the_mean_dotted(self):
        import matplotlib.pyplot as plt
        figure, axes = plt.subplots()
        apart.stacked_panel(axes, {'hips': self.VALUES}, 'Copper (Cu)', True)
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
        apart.ridge_panel(axes, {'hips': self.VALUES}, {'hips': np.zeros(self.VALUES.size)}, 'Copper (Cu)')
        solid, dotted = self.lines(axes, '-'), self.lines(axes, ':')
        self.assertEqual(len(solid), 1)
        self.assertEqual(len(dotted), 1)
        self.assertAlmostEqual(solid[0].get_xdata()[0], np.median(self.VALUES))
        self.assertAlmostEqual(dotted[0].get_xdata()[0], self.VALUES.mean())
        plt.close(figure)


class TestRun(unittest.TestCase):
    """02 writes robot type 1 taken apart at every level, and 04 draws its two figures from it, all into temporary
    folders."""

    def test_02_writes_the_draws_and_04_draws_both_figures(self):
        params = Params()
        params.composition.draws = 300
        inputs = inputs_or_skip(self, params, (HEAVY,))
        with tempfile.TemporaryDirectory() as folder:
            params.output.parts_dir = os.path.join(folder, 'data')
            params.output.parts_figures_dir = os.path.join(folder, 'figures')
            d = draw(inputs, params, fixed_magnets(inputs, params.composition.draws))
            composition.write_taken_apart(d, params.output.parts_dir)
            self.assertEqual(apart.run(params), 0)
            with open(os.path.join(params.output.parts_dir, 'register.txt'), encoding='utf-8') as file:
                self.assertEqual(file.read().splitlines(), d.register)
            for table in composition.APART_TABLES:
                draws = np.load(os.path.join(params.output.parts_dir, f'{table}.npy'))
                with open(os.path.join(params.output.parts_dir, f'{table}.txt'), encoding='utf-8') as file:
                    columns = file.read().splitlines()
                self.assertEqual(draws.shape, (300, len(columns)), msg=table)
            self.assertTrue(os.path.exists(os.path.join(params.output.parts_dir, 'summary.csv')))
            for name in apart.FIGURES:
                self.assertGreater(os.path.getsize(os.path.join(params.output.parts_figures_dir, name)), 10_000,
                                   msg=name)


if __name__ == '__main__':
    unittest.main()
