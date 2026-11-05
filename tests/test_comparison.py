"""
Tests of 03_comparison.py: the six robot types side by side, each page one item, its six types in six panels of 02's
form, from the draws 02_composition.py wrote.

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

Matthias, 2026-11-04: "Yes, agree E29" (documentation/claude/EVIDENCE.md E29: the form of 02's pages, "the different
contributions to the overall", each item a page) and "Yes, build 03". The tests write six robot types' draws in 02's
own files (its tables of `data/consolidated/` and of `data/parts_taken_apart/`, each adding up as 02's do) into a
temporary folder, few draws, then run 03 on them: press Run, nothing in the project is changed.
"""

import importlib.util
import os
import sys
import tempfile
import unittest

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

_spec = importlib.util.spec_from_file_location('comparison', os.path.join(ROOT, '03_comparison.py'))
comparison = importlib.util.module_from_spec(_spec)
sys.modules['comparison'] = comparison  # the dataclasses of 03 look their module up here while it loads
_spec.loader.exec_module(comparison)

composition = comparison.composition
schemas = composition.schemas
from src.params_schema import Params, absolute  # noqa: E402

N = 400
ELEMENTS = ['Li', 'B', 'Mg', 'Al', 'Ti', 'Mn', 'Co', 'Ni', 'Cu', 'Sn', 'Pb', 'Ag', 'Au', 'Dy', 'Ga', 'In', 'Nb', 'Nd',
            'Pd', 'Pr', 'Ta', 'Tb']
PART_GROUPS = ['Joint drives', 'Hands', 'Battery', 'Computer', 'Sensors', 'Frame', 'Shell and armour', 'Cables',
               'Cooling', 'Screws and bearings', 'Wheels and wheel drives', 'Mixed']
BODY_REGIONS = ['Legs', 'Arms', 'Hands', 'Torso', 'Head', 'Base', 'Whole body']
MATERIALS = list(composition.MATERIAL_ORDER) + [composition.NOT_ALLOCATED]
NOT_HELD = 'Ceramics'          # held by no robot type: no page
LACKING = (1, 'Tb')            # robot type 1 holds no terbium: no panel on its page


def save(folder: str, table: str, columns: list, draws: np.ndarray) -> None:
    """One table as 02 writes it: <table>.npy (float32, a column each) and its columns in <table>.txt."""
    os.makedirs(folder, exist_ok=True)
    np.save(os.path.join(folder, f'{table}.npy'), np.asarray(draws, dtype=np.float32))
    with open(os.path.join(folder, f'{table}.txt'), 'w', encoding='utf-8') as file:
        file.write('\n'.join(columns) + '\n')


def write_six(params: Params, rng: np.random.Generator) -> None:
    """Six robot types' draws in 02's files, each adding up as 02's do: the materials, part groups and body regions to
    the total; each material by kind of part to the material; each element by material to the element, its copper
    fixed in alloys beside it; the copper recycled as copper the element Cu, its inflow the two together."""
    book = schemas.read_workbook(absolute(params.data.workbook), params)
    for category in book.categories:
        t = category.number
        name = composition.folder_name(category)
        materials = np.column_stack([np.zeros(N) if m in (NOT_HELD, composition.NOT_ALLOCATED)
                                     else rng.gamma(4, t + k % 5, N) for k, m in enumerate(MATERIALS)])
        total = materials.sum(axis=1)
        groups = rng.dirichlet(np.ones(len(PART_GROUPS)), N) * total[:, None]
        regions = rng.dirichlet(np.ones(len(BODY_REGIONS)), N) * total[:, None]
        elements = np.column_stack([np.zeros(N) if (t, e) == LACKING else rng.gamma(3, 0.01 * (k + 1), N)
                                    for k, e in enumerate(ELEMENTS)])
        cu = elements[:, ELEMENTS.index('Cu')]
        fixed = rng.gamma(2, 0.1, N)
        consolidated = os.path.join(absolute(params.output.composition_dir), name)
        save(consolidated, 'total', ['Total'], total[:, None])
        save(consolidated, 'materials', MATERIALS, materials)
        save(consolidated, 'elements', ELEMENTS, elements)
        save(consolidated, 'part_groups', PART_GROUPS, groups)
        save(consolidated, 'body_regions', BODY_REGIONS, regions)
        save(consolidated, 'copper', list(composition.COPPER_COLUMNS), np.column_stack([cu, fixed, cu + fixed]))
        parts = os.path.join(absolute(params.output.parts_dir), name)
        share = rng.uniform(0.2, 0.8, N)
        by_kind_columns, by_kind = [], []
        for k, m in enumerate(MATERIALS):
            for kind, f in (('Hip joints', share), ('Frame and shell', 1 - share)):
                by_kind_columns.append(f'{kind}: {m}')
                by_kind.append(materials[:, k] * f)
        save(parts, 'materials', by_kind_columns, np.column_stack(by_kind))
        by_material_columns, by_material = [], []
        for k, e in enumerate(ELEMENTS):
            for m, f in (('Aluminium alloys', share), ('Boards and components', 1 - share)):
                by_material_columns.append(f'{e}: {m}')
                by_material.append(elements[:, k] * f)
        by_material_columns.append(f'Cu: Brass{composition.FIXED_MARK}')
        by_material.append(fixed)
        save(parts, 'by_material', by_material_columns, np.column_stack(by_material))


class Compared(unittest.TestCase):
    """Six robot types' draws written as 02 writes them, into a temporary folder; the settings 03 runs with."""

    def setUp(self):
        params = Params()
        if not os.path.exists(absolute(params.data.workbook)):
            self.skipTest('the workbook is not on disk')
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        params.output.composition_dir = os.path.join(self.folder.name, 'consolidated')
        params.output.parts_dir = os.path.join(self.folder.name, 'parts_taken_apart')
        params.output.comparison_dir = os.path.join(self.folder.name, 'figures', 'comparison')
        write_six(params, np.random.default_rng(1))
        self.params = params

    def table_path(self, number: int, folder_setting: str, table: str) -> str:
        book = schemas.read_workbook(absolute(self.params.data.workbook), self.params)
        category = next(c for c in book.categories if c.number == number)
        return os.path.join(getattr(self.params.output, folder_setting), composition.folder_name(category),
                            f'{table}.npy')


class TestComparison(Compared):

    def test_it_reads_the_draws_of_02_as_they_are(self):
        robots = comparison.read_draws(self.params)
        self.assertEqual([r.number for r in robots], [1, 2, 3, 4, 5, 6])
        for robot in robots:
            for table, setting in [(t, 'composition_dir') for t in composition.TABLES] + [
                    (t, 'parts_dir') for t in comparison.PARTS_TABLES]:
                read = robot.tables[table][1] if setting == 'composition_dir' else robot.parts[table][1]
                np.testing.assert_array_equal(read, np.load(self.table_path(robot.number, setting, table)))

    def test_every_page_of_e29(self):
        # E29: the notes once, the total, each material held by any type, each element held by any type, the part
        # groups, the body regions, copper three ways; one item a page.
        self.assertEqual(comparison.run(self.params), 0)
        written = sorted(os.listdir(self.params.output.comparison_dir))
        materials = [m for m in MATERIALS if m not in (NOT_HELD, composition.NOT_ALLOCATED)]
        expected = (['comparison_body_regions_1.png', 'comparison_copper_1.png']
                    + [f'comparison_elements_{k}.png' for k in range(1, len(ELEMENTS) + 1)]
                    + [f'comparison_materials_{k}.png' for k in range(1, len(materials) + 1)]
                    + ['comparison_part_groups_1.png', 'comparison_total_1.png'])
        notes = [w for w in written if w.startswith('comparison_notes_')]
        self.assertTrue(notes)
        self.assertEqual(sorted(set(written) - set(notes)), sorted(expected))

    def test_its_notes_name_the_outlier_not_drawn(self):
        # Matthias, 2026-11-04: "Mark it as outlier"; 2026-11-05, "Yes, 3 to 5" (EVIDENCE.md E30 point 4): 03's notes
        # page names the Neo1, not drawn, an outlier, in its types; the paragraph on each panel's own scale no longer
        # gives it as the reason.
        path = absolute(self.params.data.register)
        if not os.path.exists(path):
            self.skipTest('the register is not on disk')
        outliers = schemas.outlier_robots(schemas.read_register(path), self.params)
        notes = comparison.notes(comparison.read_draws(self.params), outliers, self.params)
        self.assertIn('Not drawn, an outlier: 208 NeodraDynamics Neo1, 1,200 kg, built as a few, never in large '
                      'numbers (robot types 3 and 5).', notes)
        scale = next(n for n in notes if n.startswith('Each panel on its own scale'))
        self.assertNotIn('Neo1', scale)
        self.assertEqual([n for n in comparison.notes(comparison.read_draws(self.params), [], self.params)
                          if 'outlier' in n], [])

    def test_the_element_pages_in_alphabetical_order_of_their_names(self):
        # Matthias, 2026-11-04: "Alphabtetic is easier to find", "Elements only": comparison_elements_1.png Aluminium (Al)
        # … the last Titanium (Ti), by the element's name, as its page's title begins; the material pages keep 02's order.
        robots = comparison.read_draws(self.params)
        elements, materials = [], []
        for name, figure in comparison.pages(robots, self.params):
            heading = figure._suptitle.get_text() if figure._suptitle else ''
            if '_elements_' in name:
                elements.append((int(name.rsplit('_', 1)[1].split('.')[0]), heading.split(' (')[0]))
            if '_materials_' in name:
                materials.append(heading.split(' in one robot')[0])
            composition.plt.close(figure)
        names = [n for _, n in sorted(elements)]
        self.assertEqual(names, sorted(composition.ELEMENT_NAMES[e] for e in ELEMENTS))
        self.assertEqual(names[0], 'Aluminium')
        self.assertEqual(names[-1], 'Titanium')
        self.assertEqual(materials, [m for m in composition.MATERIAL_ORDER if m != NOT_HELD])

    def test_each_page_six_panels_of_02s_form_no_text_over_data_readable(self):
        # 02's form (E29): a panel per type holding the item; no text over a chart's data (E26's rule); text 14 pt and
        # up on a 16 × 9 inch page.
        from matplotlib.text import Text
        robots = comparison.read_draws(self.params)
        for name, figure in comparison.pages(robots, self.params):
            if '_notes_' in name:
                composition.plt.close(figure)
                continue
            charts = [a for a in figure.axes if a.axison]
            self.assertTrue(1 <= len(charts) <= 6, msg=name)
            self.assertEqual(composition.texts_over_data(figure), [], msg=name)
            self.assertEqual(tuple(figure.get_size_inches()), tuple(composition.APART_PAGE), msg=name)
            # (A place without a panel has its axis switched off: its tick labels are not drawn.)
            hidden = {id(t) for a in figure.axes if not a.axison for t in a.xaxis.findobj(Text) + a.yaxis.findobj(Text)}
            small = [t.get_text() for t in figure.findobj(Text) if t.get_text().strip() and t.get_fontsize() < 14
                     and id(t) not in hidden]
            self.assertEqual(small, [], msg=name)
            # Nothing drawn runs off the page (CLAUDE.md §5: "nothing overflowing its panel"): each panel with its title,
            # numbers and axes' labels as drawn (a tick label matplotlib keeps outside the axis's range is not drawn),
            # the legend of the sixteen materials in its rows, the page's title.
            page = figure.bbox
            renderer = figure.canvas.get_renderer()
            boxes = [(a.get_title(loc='left') or 'a place', a.get_tightbbox(renderer)) for a in figure.axes]
            boxes += [('legend', legend.get_window_extent(renderer)) for legend in figure.legends]
            boxes += [(t.get_text(), t.get_window_extent(renderer)) for t in figure.texts if t.get_text().strip()]
            if figure._suptitle is not None:
                boxes.append((figure._suptitle.get_text(), figure._suptitle.get_window_extent(renderer)))
            off = [what for what, box in boxes if not (page.x0 - 1 <= box.x0 and box.x1 <= page.x1 + 1
                                                       and page.y0 - 1 <= box.y0 and box.y1 <= page.y1 + 1)]
            self.assertEqual(off, [], msg=name)
            composition.plt.close(figure)

    def test_a_type_without_the_item_has_no_panel(self):
        # A 0 is not part of a distribution (CLAUDE.md §7): robot type 1 holds no terbium, its place on the page says
        # so, with no chart.
        robots = comparison.read_draws(self.params)
        found = False
        for name, figure in comparison.pages(robots, self.params):
            titles = [a.get_title(loc='left') for a in figure.axes if a.axison]
            if any('Terbium' in t for t in [figure._suptitle.get_text() if figure._suptitle else '']):
                found = True
                self.assertEqual(len(titles), 5, msg=titles)
                self.assertFalse(any(t.startswith('1 ') for t in titles), msg=titles)
                # The first panel drawn in a row has the scale of the share of the draws: type 2's in the first row.
                labelled = [a.get_title(loc='left') for a in figure.axes if a.axison and a.get_ylabel()]
                self.assertEqual([t.split()[0] for t in labelled], ['2', '4'])
            composition.plt.close(figure)
        self.assertTrue(found)

    def test_the_old_pages_and_the_pages_not_drawn_removed_by_name(self):
        # E29: 03's four pages of the old form removed by their exact names; a numbered page beyond those drawn too;
        # nothing else in the folder touched.
        out = self.params.output.comparison_dir
        os.makedirs(out, exist_ok=True)
        old = list(comparison.OLD_PAGES) + ['comparison_materials_99.png']
        for name in old + ['keep.txt']:
            with open(os.path.join(out, name), 'w') as file:
                file.write('x')
        self.assertEqual(comparison.run(self.params), 0)
        left = set(os.listdir(out))
        self.assertFalse(set(old) & left)
        self.assertIn('keep.txt', left)

    def test_without_the_draws_of_02_it_stops(self):
        path = self.table_path(3, 'parts_dir', 'by_material')
        os.remove(path)
        self.assertEqual(comparison.run(self.params), 1)
        self.assertFalse(os.path.exists(self.params.output.comparison_dir))

    def test_draws_that_do_not_belong_together_stop(self):
        # A check is only trusted once it has been seen to catch what it guards.
        cases = (
            (2, 'composition_dir', 'total', lambda a: a[:-1], f'robot type 2: total has {N - 1} draws, not {N}'),
            (1, 'composition_dir', 'materials', lambda a: a * 1.01,
             'robot type 1: the materials do not add up to the total'),
            (4, 'parts_dir', 'materials', lambda a: a * 1.01,
             'robot type 4: its materials by kind of part do not add up to its materials'),
            (5, 'parts_dir', 'by_material', lambda a: a * 1.01,
             'robot type 5: its elements by material do not add up to its elements'),
        )
        for number, setting, table, change, words in cases:
            with self.subTest(table=table, setting=setting):
                self.setUp()
                path = self.table_path(number, setting, table)
                np.save(path, change(np.load(path)))
                found = comparison.problems(comparison.read_draws(self.params))
                self.assertTrue(any(words in p for p in found), found)
                self.assertEqual(comparison.run(self.params), 1)


if __name__ == '__main__':
    unittest.main()
