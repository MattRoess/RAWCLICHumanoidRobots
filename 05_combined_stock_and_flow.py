"""
05_combined_stock_and_flow.py
=============================
**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

The elements in all AI data centres and all humanoid robots of the world together, 2025 to 2040, with their
distributions. Matthias, 2026-11-08: "The distributions have to be combines 07 and 04 output", "Both have to be exactly
the same, as we have to combine both data!!!", "write 05 combination of results of 04 and 07 with the distributions",
the specification's rows 1 to 8, "Yes, build it" (documentation/claude/EVIDENCE.md E52). Press Run. No arguments; every
setting is in `src/params_schema.py`.

WHAT IT DOES
------------
For each scenario of RAWCLICDataCenters' 07 (A, B, C) and each element of either model, in every draw and year: the
kilograms in all AI data centres (07's draw i) and in all humanoid robots (04's draw i) added up, the stock at the end
of the year, the inflow and the outflow of the calendar year, 2025 to 2040 (both models count so: 04 exactly as 07).
The two models are independent; draw i of one is added to draw i of the other, on the raw draws, before any statistic.
An element only one model holds (magnesium, titanium, indium only the robots; strontium only the data centres) is that
model's alone. 07's "collected" is left out: 04 has none yet.

WHAT IT READS
-------------
- `data.data_center_draws_dir` (data/raw/data_center_stock_and_flow/): the copy of 07's element draws that
  tools/copy_data_center_draws.py made (element_draws.npy, elements.txt, source.txt); nothing of RAWCLICDataCenters
  itself (GitHub/CLAUDE.md §6).
- `output.stock_and_flow_dir` (data/stock_and_flow/): 04's elements_in, elements_stock, elements_out (draw × year × part
  of how a robot is taken apart × element), its elements those of 02 (`output.composition_dir`, elements.txt).
- The world's mine production and reserves of each element, as 04 reads them (04's `references`).

WHAT IT WRITES
--------------
Into `output.combined_dir` (data/combined_stock_and_flow/; not in git), the draws of every level ("keep the distribution
on all levels"): for each scenario a folder <scenario>/ with elements_in.npy, elements_stock.npy and elements_out.npy
(float32, draw × year 2025 to 2040 × element, kg, the data centres and the robots together; each model's own draws stay
in 04's files and the copy of 07's), elements.txt; and summary.csv: for each scenario, element, source (AI data centres,
humanoid robots, together), flow and year, the mean and the 2.5 % and 97.5 % percentiles over the draws above 0 and the
share of the draws above 0 ("A 0 is not part of a distribution").
Into `output.combined_figures_dir` (figures/combined_stock_and_flow/; not in git), for each scenario <scenario>/:
  elements/<Element>.png          its stock, its inflow and its outflow, each a panel with three lines: the AI data
                                  centres, the humanoid robots and both together, each the mean of its draws above 0 and
                                  95 % of them as a band; logarithmic axes; the world's reserves and mine production
                                  dashed (as 04 and 07)
  distributions/elements_<year>.png
                                  2025, 2030, 2035 and 2040: exactly as RAWCLICDataCenters' 05 draws the elements of one
                                  data centre (04's split_elements_page, one copy): a panel per element held, its draws'
                                  distribution, each bar split into the data centres and the humanoid robots, the mean
                                  a line with its number, 95 % dashed
Every figure a result of the runs, never an input (GitHub/CLAUDE.md §5).

WHAT IT CHECKS
--------------
That the two models' draws belong together before anything is written: the same number of draws, the years 2025 to 2040
in both, 07's three flows in the copy, 04's 14 parts; the copy's source named (source.txt). Any problem stops it.

WHERE IT SITS
-------------
After 04_stock_and_flow.py and tools/copy_data_center_draws.py (which needs RAWCLICDataCenters' 07 to have run). Run
04 and the tool first; their outputs are read as they are.
"""

from __future__ import annotations

import csv
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)   # so that `src` imports, from anywhere

import numpy as np  # noqa: E402

from src.params_schema import ParameterError, Params, absolute, current  # noqa: E402


def load_stock_and_flow():
    """04_stock_and_flow.py as a module, for its years, its statistics, its panels and pages (one copy of the code), and
    through it 02 (`composition`) and 01 (`schemas`). Loaded once; where the tests have loaded it, that module is used."""
    path = os.path.join(HERE, '04_stock_and_flow.py')
    loaded = sys.modules.get('stock_and_flow')
    if loaded is not None and os.path.samefile(getattr(loaded, '__file__', path), path):
        return loaded
    spec = importlib.util.spec_from_file_location('stock_and_flow', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules['stock_and_flow'] = module
    spec.loader.exec_module(module)
    return module


flow = load_stock_and_flow()
composition, schemas, plt = flow.composition, flow.schemas, flow.plt

# ------------------------------------------------------------------------------------------------------
# What it combines
# ------------------------------------------------------------------------------------------------------

SCENARIOS = ('A', 'B', 'C')                      # 07's scenarios, in the order of the copy
FLOWS = flow.FLOWS                               # ('in', 'stock', 'out'): the copy's flows, 04's files, in one order
YEARS = flow.LAST - flow.FIRST + 1               # 2025 to 2040: 16
DATA_CENTRES, ROBOTS, TOGETHER = 'AI data centres', 'Humanoid robots', 'together'
SOURCES = (DATA_CENTRES, ROBOTS, TOGETHER)
# The colours of the two models and of both together (Paul Tol's "bright" scheme, as published, its red and its blue;
# both together black), on the element pages and the distribution pages.
COLOURS = {DATA_CENTRES: '#EE6677', ROBOTS: '#4477AA', TOGETHER: '#222222'}
COPY_DRAWS, COPY_ELEMENTS, COPY_SOURCE = 'element_draws.npy', 'elements.txt', 'source.txt'
SUMMARY = 'summary.csv'
ELEMENTS_DIR, DISTRIBUTIONS_DIR = 'elements', 'distributions'


def read_inputs(params: Params) -> tuple:
    """The copy of 07's element draws and 04's: (the copy, scenario × draw × year × flow × element; its elements; its
    source in words; 04's three files {flow: draw × year × part × element}; 04's elements). Raises FileNotFoundError
    where a file is missing, ValueError where they do not belong together (WHAT IT CHECKS)."""
    folder = absolute(params.data.data_center_draws_dir)
    for name in (COPY_DRAWS, COPY_ELEMENTS, COPY_SOURCE):
        if not os.path.exists(os.path.join(folder, name)):
            raise FileNotFoundError(f'{os.path.join(folder, name)} is not there: run tools/copy_data_center_draws.py '
                                    'first.')
    centres = np.load(os.path.join(folder, COPY_DRAWS), mmap_mode='r')
    with open(os.path.join(folder, COPY_ELEMENTS), encoding='utf-8') as handle:
        centre_elements = handle.read().split()
    with open(os.path.join(folder, COPY_SOURCE), encoding='utf-8') as handle:
        source = handle.read()
    book = schemas.read_workbook(absolute(params.data.workbook), params)
    first = composition.folder_name(book.categories[0])
    with open(os.path.join(absolute(params.output.composition_dir), first, 'elements.txt'), encoding='utf-8') as handle:
        robot_elements = handle.read().split()
    robots = {}
    for name, flow_name in zip(flow.ELEMENT_FILES, FLOWS):
        path = os.path.join(absolute(params.output.stock_and_flow_dir), f'{name}.npy')
        if not os.path.exists(path):
            raise FileNotFoundError(f'{path} is not there: run 04_stock_and_flow.py first.')
        robots[flow_name] = np.load(path, mmap_mode='r')
    shape = robots[FLOWS[0]].shape
    if centres.ndim != 5 or centres.shape[0] != len(SCENARIOS) or centres.shape[3] != len(FLOWS):
        raise ValueError(f"the copy of 07's draws is {centres.shape}, not scenario × draw × year × flow × element.")
    if centres.shape[4] != len(centre_elements):
        raise ValueError(f"the copy of 07's draws holds {centres.shape[4]} elements, its list {len(centre_elements)}.")
    if any(robots[f].shape != shape for f in FLOWS) or shape[2] != len(flow.PARTS) or shape[3] != len(robot_elements):
        raise ValueError(f"04's element files are {shape}, not draw × year × its {len(flow.PARTS)} parts × "
                         f'{len(robot_elements)} elements.')
    if centres.shape[1] != shape[0]:
        raise ValueError(f"07's copy holds {centres.shape[1]:,} draws, 04 {shape[0]:,}: the two do not pair draw by "
                         'draw; run both with the same number of draws.')
    if centres.shape[2] != YEARS or shape[1] != YEARS:
        raise ValueError(f"the years: 07's copy {centres.shape[2]}, 04's {shape[1]}, not {YEARS} ({flow.FIRST} to "
                         f'{flow.LAST}).')
    return centres, centre_elements, source, robots, robot_elements


def columns_of(elements: list, own: list) -> tuple:
    """Where each of `elements` stands in a model's own list `own`: (its places in `elements`, its places in `own`),
    an element the model does not hold left out (it adds 0)."""
    here = [k for k, e in enumerate(elements) if e in own]
    return here, [own.index(elements[k]) for k in here]


def stats_columns(values: np.ndarray) -> tuple:
    """04's column_stats (one copy): the mean, 2.5 % and 97.5 % over the draws above 0, the share above 0."""
    return flow.column_stats(values)


def combine(params: Params, centres, centre_elements: list, robots: dict, robot_elements: list, folder: str,
            figures: str) -> tuple:
    """Add the data centres and the humanoid robots draw by draw for every scenario, flow and year; write the combined
    draws; draw the distribution pages of the year ends of DISTRIBUTION_YEARS; return (the elements, the statistics:
    {(scenario, source, flow): {'mean', 'low', 'high', 'held'} each year × element})."""
    elements = composition.element_order(set(centre_elements) | set(robot_elements))
    n, e = centres.shape[1], len(elements)
    at_c, from_c = columns_of(elements, centre_elements)
    at_r, from_r = columns_of(elements, robot_elements)
    stats = {(s, source, f): {key: np.full((YEARS, e), np.nan) for key in ('mean', 'low', 'high')}
             for s in SCENARIOS for source in SOURCES for f in FLOWS}
    for value in stats.values():
        value['held'] = np.zeros((YEARS, e))
    files = {}
    for s in SCENARIOS:
        os.makedirs(os.path.join(folder, s), exist_ok=True)
        with open(os.path.join(folder, s, 'elements.txt'), 'w', encoding='utf-8') as handle:
            handle.write('\n'.join(elements) + '\n')
        for name, f in zip(flow.ELEMENT_FILES, FLOWS):
            files[(s, f)] = np.lib.format.open_memmap(os.path.join(folder, s, f'{name}.npy'), mode='w+',
                                                      dtype=np.float32, shape=(n, YEARS, e))
    for k, f in enumerate(FLOWS):
        for y in range(YEARS):
            # The humanoid robots: all their parts of how a robot is taken apart added up, draw by draw.
            robot = np.zeros((n, e))
            robot[:, at_r] = np.asarray(robots[f][:, y], dtype=np.float64).sum(axis=1)[:, from_r]
            for s_index, s in enumerate(SCENARIOS):
                centre = np.zeros((n, e))
                centre[:, at_c] = np.asarray(centres[s_index, :, y, k, :], dtype=np.float64)[:, from_c]
                together = centre + robot                                   # draw i with draw i, the raw draws
                files[(s, f)][:, y] = together
                for source, values in ((DATA_CENTRES, centre), (ROBOTS, robot), (TOGETHER, together)):
                    for key, column in zip(('mean', 'low', 'high', 'held'), stats_columns(values)):
                        stats[(s, source, f)][key][y] = column
                year = flow.FIRST + y
                if f == 'stock' and year in flow.DISTRIBUTION_YEARS:
                    distribution_page(s, year, centre, robot, elements, n,
                                      os.path.join(figures, s, DISTRIBUTIONS_DIR, f'elements_{year}.png'),
                                      params.output.dpi)
    for array in files.values():
        array.flush()
    return elements, stats


def distribution_page(scenario: str, year: int, centre: np.ndarray, robot: np.ndarray, elements: list, draws: int,
                      path: str, dpi: int) -> str:
    """The elements in all AI data centres and humanoid robots in use at the end of `year`, exactly as
    RAWCLICDataCenters' 05 draws the elements of one data centre (04's split_elements_page): each bar split into the
    data centres and the humanoid robots."""
    note = (f'bars: the draws ({draws:,}), the height the share of the draws; solid line and number: the mean; dashed '
            'lines: 2.5th and 97.5th percentile (the 95% interval);\neach panel on its own scale and unit; each bar split '
            f"into the kg of its draws in the AI data centres (RAWCLICDataCenters' 07, scenario {scenario}) and in the "
            'humanoid robots (04), draw i with draw i; an element held in fewer than 2.5% of the draws is not drawn')
    return flow.split_elements_page(f'{year}: elements in all AI data centres (scenario {scenario}) and humanoid '
                                    'robots in use', {DATA_CENTRES: centre, ROBOTS: robot},
                                    {name: COLOURS[name] for name in (DATA_CENTRES, ROBOTS)}, elements, note, path,
                                    dpi)


def per_element(stats: dict, k: int) -> dict:
    """One element's statistics over the years, {'mean', 'low', 'high', 'held'}, as 04's log_panel takes them."""
    return {key: stats[key][:, k] for key in ('mean', 'low', 'high', 'held')}


def element_page(scenario: str, symbol: str, k: int, stats: dict, world: dict, notes: list, draws: int, source: str,
                 path: str, dpi: int) -> str:
    """One element of one scenario: its stock beside the world's reserves, its inflow beside the world's mine
    production in 2025, its outflow; each panel the data centres, the humanoid robots and both together (04's
    log_panel, world_reference and save_figure: one copy)."""
    years = np.arange(flow.FIRST, flow.LAST + 1)
    figure, panels = plt.subplots(1, 3, figsize=flow.A4_LANDSCAPE)
    for axes, f, title, word in zip(panels, FLOWS, ('Inflow', 'Stock', 'Outflow'),
                                    ('per year', '', 'per year')):
        series = [(years, per_element(stats[(scenario, source, f)], k), source if source != TOGETHER else 'both together',
                   COLOURS[source]) for source in SOURCES]
        if flow.log_panel(axes, series, word, flow.mass_label):
            axes.set_title(title)
            if f == 'stock':
                flow.world_reference(axes, world.get('reserves'), 'World reserves', per_year=False)
            if f == 'in':
                flow.world_reference(axes, world.get('production'), 'World production 2025', per_year=True)
            axes.legend(loc='upper left')
    figure.suptitle(f'{composition.ELEMENT_NAMES.get(symbol, symbol)}: AI data centres (scenario {scenario}) and '
                    'humanoid robots')
    note = (f'Lines: the mean of the draws above 0 of {draws:,} draws; bands: 95 % of them (2.5 % to 97.5 %); flows per '
            "calendar year, stocks at the end of the year, as RAWCLICDataCenters' 07; logarithmic axes. AI data centres: "
            f"RAWCLICDataCenters' 07, scenario {scenario}, its draws as copied ({copied_words(source)}); humanoid robots: "
            "04; both together: added draw by draw.")
    if world:
        note += (" Dashed: the world's mine production in 2025 (inflow) and reserves (stock), " + flow.WORLD_SOURCE
                 + ('; ' + '; '.join(notes) if notes else '') + '; a value outside the scale is written in the panel.')
    else:
        note += ' No world production or reserves for it in the sources read.'
    return flow.save_figure(figure, path, note, dpi)


def copied_words(source: str) -> str:
    """The copy's source in words, from its source.txt: '<file> of <its modification time>, copied <when>'."""
    lines = dict(line.split(': ', 1) for line in source.splitlines() if ': ' in line)
    return (f"{os.path.basename(lines.get('source', '?'))} of {lines.get('modified', '?')}, copied "
            f"{lines.get('copied', '?')}")


def write_summary(path: str, elements: list, stats: dict) -> None:
    """summary.csv: a row for each scenario, element, source, flow and year; '–' where no draw is above 0."""
    with open(path, 'w', newline='', encoding='utf-8') as handle:
        writer = csv.writer(handle)
        writer.writerow(('scenario', 'element', 'source', 'flow', 'year', 'mean', '2.5 %', '97.5 %',
                         'held in % of the draws'))
        for (s, source, f), value in stats.items():
            for k, symbol in enumerate(elements):
                for y in range(YEARS):
                    cells = [f'{value[key][y, k]:.6g}' if np.isfinite(value[key][y, k]) else '–'
                             for key in ('mean', 'low', 'high')]
                    writer.writerow((s, composition.ELEMENT_NAMES.get(symbol, symbol), source, f, flow.FIRST + y,
                                     *cells, f"{100 * value['held'][y, k]:.1f}"))


def run(params: Params) -> int:
    """Read, check, combine, write the draws and the summary, draw the pages. 0 when done; 1 when an input is missing or
    the draws do not belong together (then nothing is written)."""
    try:
        centres, centre_elements, source, robots, robot_elements = read_inputs(params)
    except (FileNotFoundError, ValueError, schemas.WorkbookError) as error:
        print(f'05 stopped: {error}')
        return 1
    n = centres.shape[1]
    print(f"05: AI data centres, 07's draws as copied ({copied_words(source)}); humanoid robots, 04's; {n:,} draws, "
          f'scenarios {", ".join(SCENARIOS)} …', flush=True)
    folder, figures = absolute(params.output.combined_dir), absolute(params.output.combined_figures_dir)
    os.makedirs(folder, exist_ok=True)
    with plt.rc_context(flow.PRINT_STYLE):
        elements, stats = combine(params, centres, centre_elements, robots, robot_elements, folder, figures)
    write_summary(os.path.join(folder, SUMMARY), elements, stats)
    world, notes = flow.references(params)
    pages = 0
    with plt.rc_context(flow.PRINT_STYLE):
        for s in SCENARIOS:
            for k, symbol in enumerate(elements):
                if not any(stats[(s, TOGETHER, f)]['held'][:, k].max() > 0 for f in FLOWS):
                    print(f'05: {composition.ELEMENT_NAMES.get(symbol, symbol)}: no numbers, 0 kg in every draw; no '
                          'page.')
                    continue
                element_page(s, symbol, k, stats, world.get(symbol, {}), notes.get(symbol, []), n, source,
                             os.path.join(figures, s, ELEMENTS_DIR, flow.element_file(symbol)), params.output.dpi)
                pages += 1
    print(f'05 done: {n:,} draws, {len(elements)} elements, scenarios {", ".join(SCENARIOS)}; {pages} element pages and '
          f'{len(SCENARIOS) * len(flow.DISTRIBUTION_YEARS)} distribution pages in {figures}; the draws and {SUMMARY} in '
          f'{folder}.')
    return 0


def main() -> int:
    """Press Run: the settings in force, then run()."""
    try:
        params = current()
    except ParameterError as error:
        print(error, file=sys.stderr)
        return 1
    return run(params)


if __name__ == '__main__':
    raise SystemExit(main())
