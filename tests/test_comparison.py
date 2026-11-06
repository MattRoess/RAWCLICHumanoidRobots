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

Since 2026-11-06 (Matthias: "Relabel and page check"; EVIDENCE.md E37) `TestEveryPageOfTheSixTypes` also runs
02_composition.py itself for the six robot types from the project's own inputs, 1,000 draws a type, into a temporary
folder, then 03 on those draws, and checks every page of both as it is saved (`page_problems`): its legends, colours and
texts within Matthias's rules, no median pressed into the first 5 % of a panel's bars. No page is written.
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
# The elements of the magnets the sensors hold too, as in 02's draws (E38 point 5): from the NdFeB magnets and the
# cameras and other sensors alone.
MAGNETS_AND_SENSORS = ('Dy', 'Ga', 'Nd')


def save(folder: str, table: str, columns: list, draws: np.ndarray) -> None:
    """One table as 02 writes it: <table>.npy (float32, a column each) and its columns in <table>.txt."""
    os.makedirs(folder, exist_ok=True)
    np.save(os.path.join(folder, f'{table}.npy'), np.asarray(draws, dtype=np.float32))
    with open(os.path.join(folder, f'{table}.txt'), 'w', encoding='utf-8') as file:
        file.write('\n'.join(columns) + '\n')


def median_along_bars(axes) -> float:
    """Where a panel's median (its panel_numbers) sits along its bars: 0 at the left edge of its first bar (its smallest
    draw), 1 at the right edge of its last (its axis's end), on the axis's own scale, linear or logarithmic; the axis's
    margins left out, as the rule measures (02's logarithmic; as in test_parts_taken_apart.py)."""
    median = axes.panel_numbers[2]
    low = min(p.get_x() for p in axes.patches)
    high = max(p.get_x() + p.get_width() for p in axes.patches)
    if axes.get_xscale() == 'log':
        return float((np.log10(median) - np.log10(low)) / (np.log10(high) - np.log10(low)))
    return float((median - low) / (high - low))


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
            # A light alloy's metal from its own alloy (E24, E33), every other element from the aluminium alloys; the
            # titanium beside its alloy in the sensors, the cameras and the other sensors (02's components, E32).
            electronics = ([(composition.component_label(composition.CAMERAS), 0.7 * (1 - share)),
                            (composition.component_label(composition.OTHER_SENSORS), 0.3 * (1 - share))]
                           if e in composition.SENSORS_OF or e in MAGNETS_AND_SENSORS
                           else [('Boards and components', 1 - share)])
            # Copper and nickel from their own metal (02's WHOLE), as 02's draws give them.
            own = {element: material for material, element in composition.WHOLE.items()}
            holder = (composition.MAGNETS if e in MAGNETS_AND_SENSORS
                      else composition.ALLOY_OF.get(e) or own.get(e, 'Aluminium alloys'))
            for m, f in [(holder, share), *electronics]:
                by_material_columns.append(f'{e}: {m}')
                by_material.append(elements[:, k] * f)
        by_material_columns.append(f'Cu: Brass{composition.FIXED_MARK}')
        by_material.append(fixed)
        save(parts, 'by_material', by_material_columns, np.column_stack(by_material))
        # The robots of the register drawn, '<number> <name>', as 02 writes them (none an outlier).
        with open(os.path.join(parts, 'register.txt'), 'w', encoding='utf-8') as file:
            file.write(f'{t}00 Robot A of type {t}\n{t}01 Robot B of type {t}\n')


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
        # Each element a page, the titanium also its sensors' (2026-11-05, "Yes, add it").
        pages_of_elements = len(ELEMENTS) + len([e for e in ELEMENTS if e in composition.SENSORS_OF
                                                 or e in MAGNETS_AND_SENSORS])
        expected = (['comparison_body_regions_1.png', 'comparison_copper_1.png']
                    + [f'comparison_elements_{k}.png' for k in range(1, pages_of_elements + 1)]
                    + [f'comparison_materials_{k}.png' for k in range(1, len(materials) + 1)]
                    + ['comparison_part_groups_1.png', 'comparison_total_1.png'])
        # Each page of panels followed by the page of its numbers (E34).
        expected += [f'comparison_numbers_{k}.png' for k in range(1, len(expected) + 1)]
        notes = [w for w in written if w.startswith('comparison_notes_')]
        self.assertTrue(notes)
        self.assertEqual(sorted(set(written) - set(notes)), sorted(expected))

    def test_the_sensors_titanium_a_page_of_its_own(self):
        # Matthias, 2026-11-05: "where the hell is titanium in the sensor … I only see titanium alloy the heavy stuff",
        # "Yes, add it": beside the page of the alloy's titanium, a page of the sensors' titanium, the cameras and the
        # other sensors, its own scale.
        robots = comparison.read_draws(self.params)
        pages = dict(comparison.pages(robots, self.params))
        titles = {n: f._suptitle.get_text() for n, f in pages.items() if f._suptitle}
        name = next(n for n, t in titles.items() if t == 'Titanium (Ti) in the sensors of one robot of each robot type')
        labels = {t.get_text() for legend in pages[name].legends for t in legend.get_texts()}
        self.assertEqual(labels, {composition.shown_name(composition.component_label(composition.CAMERAS)),
                                  composition.shown_name(composition.component_label(composition.OTHER_SENSORS))})
        self.assertIn('Titanium (Ti) held in the titanium alloy of one robot of each robot type', titles.values())
        for figure in pages.values():
            composition.plt.close(figure)

    def test_copper_and_nickel_by_what_they_are_on_the_element_pages(self):
        # Matthias, 2026-11-05: "copper in copper does not make any sense", "Yes, relabel"; 2026-11-06: "Relabel and
        # page check" (E37): on 03's element pages 02's element_page_name; the page of the mass by material as it was.
        robots = comparison.read_draws(self.params)
        legends = {}
        for name, figure in comparison.pages(robots, self.params):
            if figure._suptitle:
                legends[figure._suptitle.get_text()] = {t.get_text() for g in figure.legends for t in g.get_texts()}
            composition.plt.close(figure)
        copper = next(v for k, v in legends.items() if k.startswith('Copper (Cu) in one robot'))
        nickel = next(v for k, v in legends.items() if k.startswith('Nickel (Ni) in one robot'))
        self.assertIn(composition.ELEMENT_PAGE_NAMES[composition.COPPER], copper)
        self.assertIn(composition.ELEMENT_PAGE_NAMES['Nickel'], nickel)
        self.assertFalse({composition.COPPER, 'Nickel'} & (copper | nickel))
        total = legends['The mass of one robot of each robot type, by material']
        self.assertTrue({composition.COPPER, 'Nickel'} <= total, sorted(total))
        self.assertFalse(set(composition.ELEMENT_PAGE_NAMES.values()) & total)

    def test_the_magnets_and_the_sensors_apart(self):
        # Matthias, 2026-11-06: "Gallium apart", "Yes do it like this. Nd etc. are then similar as Ga in elements in
        # Magnets" (E38 point 5): an element of the magnets and the sensors alone on two pages, the magnets' without a
        # legend (one colour, the title naming it), the sensors' with the cameras and the other sensors.
        robots = comparison.read_draws(self.params)
        titles = {}
        for name, figure in comparison.pages(robots, self.params):
            if figure._suptitle:
                titles[figure._suptitle.get_text()] = {t.get_text() for g in figure.legends for t in g.get_texts()}
            composition.plt.close(figure)
        for e in MAGNETS_AND_SENSORS:
            label = composition.element_label(e)
            self.assertEqual(titles[f'{label} in the magnets of one robot of each robot type'], set())
            self.assertEqual(titles[f'{label} in the sensors of one robot of each robot type'],
                             {composition.shown_name(composition.component_label(c))
                              for c in (composition.CAMERAS, composition.OTHER_SENSORS)})
            self.assertFalse([t for t in titles if t.startswith(f'{label} in one robot')], label)
        self.assertTrue([t for t in titles if t.startswith('Cobalt (Co) in one robot')])   # one page, as before

    def test_no_median_in_the_first_part_of_its_axis(self):
        # Matthias, 2026-11-05: "Titanium in sensors the x axis is not good, You know this", then "Yes, build it" (E36,
        # 02's rule, one copy): type 2's sensors' titanium spread as in V186 (96 % of the draws 1 to 10 mg from the
        # cameras, 4 % 100 to 470 mg from the PZT of ultrasonic sensors), its panel on a logarithmic axis; no panel of
        # 03's pages with its median in the first LOG_BELOW of its bars.
        path = self.table_path(2, 'parts_dir', 'by_material')
        with open(path[:-len('.npy')] + '.txt', encoding='utf-8') as file:
            columns = file.read().split('\n')[:-1]
        draws = np.load(path).astype(float)
        rng = np.random.default_rng(2)
        ultrasonic = rng.random(len(draws)) < 0.04
        draws[:, columns.index(f'Ti: {composition.component_label(composition.CAMERAS)}')] = (
            rng.uniform(1, 10, len(draws)) * 1e-6)
        draws[:, columns.index(f'Ti: {composition.component_label(composition.OTHER_SENSORS)}')] = np.where(
            ultrasonic, rng.uniform(100, 470, len(draws)), rng.uniform(0.1, 1, len(draws))) * 1e-6
        save(os.path.dirname(path), 'by_material', columns, draws)
        robots = comparison.read_draws(self.params)
        checked, sensors = 0, None
        for name, figure in comparison.pages(robots, self.params):
            panels = [a for a in figure.axes if getattr(a, 'panel_numbers', None) is not None]
            if figure._suptitle and figure._suptitle.get_text() == ('Titanium (Ti) in the sensors of one robot of '
                                                                    'each robot type'):
                sensors = [a.get_xscale() for a in panels]
            for axes in panels:
                checked += 1
                self.assertGreaterEqual(median_along_bars(axes), composition.LOG_BELOW,
                                        msg=(name, axes.panel_numbers[0]))
            composition.plt.close(figure)
        self.assertEqual(sensors, ['linear', 'log', 'linear', 'linear', 'linear', 'linear'])
        self.assertGreater(checked, 100)

    def test_it_stops_where_the_draws_hold_an_outlier(self):
        # Matthias, 2026-11-05, "Yes, all ten" (open item 5): older draws on disk may hold a robot set as an outlier
        # since (the Neo1, E30), and 03's notes page would then name it "not drawn". 03 stops before drawing and says
        # which type's draws hold it.
        path = absolute(self.params.data.register)
        if not os.path.exists(path):
            self.skipTest('the register is not on disk')
        outlier = schemas.outlier_robots(schemas.read_register(path), self.params)[0]
        self.assertEqual(comparison.outliers_in_draws(self.params, [outlier]), [])
        register = os.path.join(os.path.dirname(self.table_path(3, 'parts_dir', 'by_material')), 'register.txt')
        with open(register, 'a', encoding='utf-8') as file:
            file.write(f'{outlier.number} {outlier.name}\n')
        found = comparison.outliers_in_draws(self.params, [outlier])
        self.assertEqual(len(found), 1, found)
        self.assertIn(f'robot type 3: its draws hold {outlier.number} {outlier.name}', found[0])
        self.assertEqual(comparison.run(self.params), 1)
        self.assertFalse(os.path.exists(self.params.output.comparison_dir)
                         and os.listdir(self.params.output.comparison_dir))

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

    def test_the_numbers_on_a_page_of_their_own(self):
        # Matthias, 2026-11-05: "Do we really need all this text in the figure. It might be better to have it separate",
        # "Yes" (EVIDENCE.md E34): no number over a panel of 03; after each page of panels a page of its numbers.
        pages = list(comparison.pages(comparison.read_draws(self.params), self.params))
        names = [name for name, _ in pages]
        figures = dict(pages)
        drawn = [n for n in names if '_notes_' not in n and '_numbers_' not in n]
        self.assertEqual(len([n for n in names if '_numbers_' in n]), len(drawn))
        for name in drawn:
            following = names[names.index(name) + 1]
            self.assertIn('_numbers_', following, msg=name)
            self.assertFalse([a.get_title(loc='right') for a in figures[name].axes if a.get_title(loc='right')],
                             msg=name)
            words = ' '.join(t.get_text() for t in figures[following].texts).replace('\n', ' ')
            for row in composition.panel_rows(figures[name]):
                self.assertIn(row[0], words, msg=(name, row))
        for figure in figures.values():
            composition.plt.close(figure)

    def test_a_light_alloys_metal_its_alloy_drawn_alone(self):
        # Matthias, 2026-11-05, "Work out a pragmatic solution", "Yes", "Yes, relabel", "A figure is a figure and not
        # text" (EVIDENCE.md E33): on 03's pages of aluminium, magnesium and titanium each type's panel draws the metal
        # its alloys hold, the page titled so, no legend, nothing written beside it; a type without the alloy has no
        # panel, its place naming the alloy.
        path = self.table_path(4, 'parts_dir', 'by_material')
        columns = open(path[:-4] + '.txt').read().split('\n')
        draws = np.load(path)
        draws[:, columns.index('Ti: Titanium alloy')] = 0   # type 4 without titanium alloy
        np.save(path, draws)
        robots = comparison.read_draws(self.params)
        pages = dict(comparison.pages(robots, self.params))
        for symbol, words in (('Al', 'Aluminium (Al) held in the aluminium alloys of one robot of each robot type'),
                              ('Ti', 'Titanium (Ti) held in the titanium alloy of one robot of each robot type')):
            name = next(n for n, f in pages.items() if f._suptitle and f._suptitle.get_text() == words)
            figure = pages[name]
            self.assertEqual(figure.legends, [], msg=name)
            rights = [a.get_title(loc='right') for a in figure.axes if a.axison]
            self.assertTrue(rights and not any('outside' in r or 'electronics' in r for r in rights), (name, rights))
            if symbol == 'Ti':
                places = [t.get_text() for a in figure.axes if not a.axison for t in a.texts]
                self.assertIn('Titanium alloy: none in this robot type', places)
        notes = ' '.join(comparison.notes(robots, [], self.params))
        self.assertIn('held in the alloys', notes)
        for figure in pages.values():
            composition.plt.close(figure)

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
        # Titanium twice since 2026-11-05 ("Yes, add it"): its alloy's page, then its sensors' right after it.
        expected = [name for name in sorted(composition.ELEMENT_NAMES[e] for e in ELEMENTS)
                    for _ in range(2 if name in {composition.ELEMENT_NAMES[e] for e in
                                                 (*composition.SENSORS_OF, *MAGNETS_AND_SENSORS)} else 1)]
        self.assertEqual(names, expected)
        self.assertEqual(names[0], 'Aluminium')
        self.assertEqual(names[-1], 'Titanium')
        self.assertEqual(materials, [m for m in composition.MATERIAL_ORDER if m != NOT_HELD])

    def test_each_page_six_panels_of_02s_form_no_text_over_data_readable(self):
        # 02's form (E29): a panel per type holding the item; no text over a chart's data (E26's rule); text 14 pt and
        # up on a 16 × 9 inch page.
        from matplotlib.text import Text
        robots = comparison.read_draws(self.params)
        for name, figure in comparison.pages(robots, self.params):
            if '_notes_' in name or '_numbers_' in name:   # a page of text (E34: the numbers apart)
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
            if '_numbers_' not in name and any('Terbium' in t for t in [figure._suptitle.get_text()
                                                                        if figure._suptitle else '']):
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


def page_problems(figure, name: str) -> list:
    """What breaks Matthias's figure rules on one page as it is saved (VERIFICATION.md V186, V188): a legend beyond the
    page; on a page with a legend, a colour a panel draws that the legend does not name; a panel or a text beyond the
    page; a panel whose median lies in the first LOG_BELOW of its bars (02's logarithmic axis, E36). [] where none."""
    from matplotlib.colors import to_hex
    from matplotlib.patches import Rectangle
    figure.canvas.draw()   # the page laid out as it is saved
    renderer = figure.canvas.get_renderer()
    width, height = figure.bbox.width, figure.bbox.height
    inside = lambda box: box.x0 >= -2 and box.x1 <= width + 2 and box.y0 >= -2 and box.y1 <= height + 2  # noqa: E731
    problems = [(name, 'a legend beyond the page') for legend in figure.legends
                if not inside(legend.get_window_extent(renderer))]
    named = {to_hex(h.get_facecolor()) for legend in figure.legends for h in legend.legend_handles}
    for axes in figure.axes:
        title = axes.get_title(loc='left')[:40]
        if axes.get_visible() and axes.axison and not inside(axes.get_tightbbox(renderer)):
            problems.append((name, 'a panel beyond the page', title))
        if figure.legends:
            drawn = {to_hex(p.get_facecolor()) for p in axes.patches if isinstance(p, Rectangle)
                     and p.get_height() > 0 and p.get_width() > 0 and p.get_facecolor()[3] > 0}
            if drawn - named:
                problems.append((name, 'a colour drawn, not in the legend', title, sorted(drawn - named)))
        if getattr(axes, 'panel_numbers', None) is not None and axes.patches:
            where = median_along_bars(axes)
            if where < composition.LOG_BELOW:
                problems.append((name, 'its median in the first 5 % of its bars', title, round(where, 4)))
    texts = [figure._suptitle, *figure.texts] + [t for axes in figure.axes if not axes.axison for t in axes.texts]
    problems += [(name, 'a text beyond the page', t.get_text()[:40]) for t in texts
                 if t is not None and t.get_visible() and t.get_text().strip()
                 and not inside(t.get_window_extent(renderer))]
    return problems


class TestEveryPageOfTheSixTypes(unittest.TestCase):
    """Matthias, 2026-11-06: "I want that everything is verifyed", then "Relabel and page check": every page 02 draws for
    the six robot types and every page 03 draws, from the project's own inputs, checked as it is saved (page_problems).
    02 runs with 1,000 draws a type into a temporary folder, then 03 on those draws; no page is written, nothing in
    data/ or figures/ is touched. Until 2026-11-06 this check was a scratch script (V186), lost overnight."""

    @classmethod
    def setUpClass(cls):
        from contextlib import redirect_stdout
        from io import StringIO
        from unittest import mock
        from matplotlib.figure import Figure
        params = Params()
        files = [absolute(params.data.workbook), absolute(params.data.register), params.data.vehicle_sensor_composition]
        if not all(os.path.exists(f) for f in files):
            raise unittest.SkipTest('the inputs are not on disk')
        cls.folder = tempfile.TemporaryDirectory()
        params.composition.draws = 1000
        for setting in ('schemas_dir', 'composition_dir', 'composition_figures_dir', 'comparison_dir', 'parts_dir',
                        'parts_figures_dir'):
            setattr(params.output, setting, os.path.join(cls.folder.name, setting))
        cls.pages, cls.problems, cls.codes = {}, {}, {}
        stage = []

        def checked(figure, path, *args, **kwargs):   # in place of Figure.savefig: check the page, write nothing
            cls.pages[stage[-1]] += 1
            cls.problems[stage[-1]] += page_problems(figure, os.path.basename(str(path)))

        with mock.patch.object(Figure, 'savefig', checked), redirect_stdout(StringIO()):
            for name, module in (('02', composition), ('03', comparison)):
                stage.append(name)
                cls.pages[name], cls.problems[name] = 0, []
                cls.codes[name] = module.run(params)

    @classmethod
    def tearDownClass(cls):
        cls.folder.cleanup()

    def test_02_every_page_by_the_rules(self):
        self.assertEqual(self.codes['02'], 0)
        self.assertGreater(self.pages['02'], 200)   # 263 pages at V186
        self.assertEqual(self.problems['02'], [])

    def test_03_every_page_by_the_rules(self):
        self.assertEqual(self.codes['03'], 0)
        self.assertGreater(self.pages['03'], 80)    # 86 pages at V186
        self.assertEqual(self.problems['03'], [])
