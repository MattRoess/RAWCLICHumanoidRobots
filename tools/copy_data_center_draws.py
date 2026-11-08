"""
tools/copy_data_center_draws.py
===============================
**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

Copies the element draws of RAWCLICDataCenters' stock and flow (its stage 07) into this project, so that 05 reads its
data from its own folder (GitHub/CLAUDE.md §6: "They have to be here in this project as raw data. This is essential so
the project is independet"). Matthias, 2026-11-08: "write 05 combination of results of 04 and 07 with the
distributions", the specification's row 7 ("A small tool here makes the copy, run by you once and again whenever 07 is
rerun"), "Yes, build it" (documentation/claude/EVIDENCE.md E52).

WHAT IT READS
-------------
07's draws, the setting `data.data_center_stock_and_flow_source` (RAWCLICDataCenters'
data/data_center_stock_and_flow/stock_flow_draws.csv, about 9 GB): a row for each scenario (A, B, C), draw and year
(2022 to 2040), with the kilograms of each element in, in stock, out and collected. Only this tool reads it.

WHAT IT WRITES
--------------
Into the setting `data.data_center_draws_dir` (data/raw/data_center_stock_and_flow/, not in git):
  element_draws.npy   float32, scenario (A, B, C) × draw × year (2025 to 2040, as 04 counts them: the flows of the
                      calendar year, the stock at its end, as 07 writes them) × flow (in, stock, out) × element, kg;
                      07's numbers as they are, nothing computed (its "collected" left out: 04 has none yet)
  elements.txt        the elements, one a line, in 07's order
  source.txt          where the copy comes from: the source file, its size and modification time, when it was copied,
                      the scenarios, draws, years and flows copied
It stops, writing no source.txt, where a scenario, draw or year of 2025 to 2040 is missing or comes twice.

HOW TO RUN IT
-------------
Press Run, with no arguments, after 07 has run in RAWCLICDataCenters, and again whenever 07 has run again. Reading the
9 GB takes some minutes; it is Matthias's run.

WHERE IT SITS
-------------
Before 05_combined_stock_and_flow.py, which reads its copy and nothing of RAWCLICDataCenters.
"""

from __future__ import annotations

import datetime
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)   # so that `src` imports

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from src.params_schema import ParameterError, absolute, current  # noqa: E402

FIRST, LAST = 2025, 2040                  # the years copied: 04's, as 07 counts them
SCENARIOS = ('A', 'B', 'C')               # 07's scenarios, in its order
FLOWS = ('in', 'stock', 'out')            # the flows copied; 07's "collected" left out (04 has none yet)
DRAWS_FILE, ELEMENTS_FILE, SOURCE_FILE = 'element_draws.npy', 'elements.txt', 'source.txt'
CHUNK_ROWS = 400_000                      # rows of 07's file read at once (memory: about 0.5 GB a chunk)


def elements_of(header: list) -> list:
    """The elements of 07's file, in its order: the columns '<symbol>_kg_in'."""
    return [column[:-len('_kg_in')] for column in header if column.endswith('_kg_in')]


def draws_of(source: str) -> int:
    """How many draws 07 wrote: its last row's draw + 1 (07 writes scenario by scenario, draw by draw, year by year);
    every draw below it is checked to be there when the copy is made."""
    with open(source, 'rb') as handle:
        handle.seek(0, os.SEEK_END)
        position = max(handle.tell() - 4096, 0)
        handle.seek(position)
        last = handle.read().decode('utf-8').rstrip('\n').rsplit('\n', 1)[-1]
    return int(last.split(',')[1]) + 1


def copy(source: str, folder: str) -> str:
    """Copy the element draws of 07's file `source` into `folder` (WHAT IT WRITES); returns the path of the draws.
    Raises ValueError where a scenario, draw or year of FIRST to LAST is missing or comes twice."""
    header = pd.read_csv(source, nrows=0).columns.tolist()
    elements = elements_of(header)
    columns = [f'{e}_kg_{f}' for f in FLOWS for e in elements]           # flow by flow, each its elements
    missing = [c for c in ['scenario', 'draw', 'year'] + columns if c not in header]
    if missing:
        raise ValueError(f'{source}: no column {", ".join(missing)}.')
    n, years = draws_of(source), LAST - FIRST + 1
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, DRAWS_FILE)
    out = np.lib.format.open_memmap(path, mode='w+', dtype=np.float32,
                                    shape=(len(SCENARIOS), n, years, len(FLOWS), len(elements)))
    seen = np.zeros((len(SCENARIOS), n, years), dtype=np.uint8)            # how often each cell was written
    for chunk in pd.read_csv(source, usecols=['scenario', 'draw', 'year'] + columns, chunksize=CHUNK_ROWS):
        chunk = chunk[(chunk['year'] >= FIRST) & (chunk['year'] <= LAST)]
        if chunk.empty:
            continue
        unknown = set(chunk['scenario']) - set(SCENARIOS)
        if unknown:
            raise ValueError(f'{source}: scenario {", ".join(sorted(unknown))} is none of {", ".join(SCENARIOS)}.')
        s = chunk['scenario'].map({name: k for k, name in enumerate(SCENARIOS)}).to_numpy()
        d, y = chunk['draw'].to_numpy(), chunk['year'].to_numpy() - FIRST
        if (d < 0).any() or (d >= n).any():
            raise ValueError(f'{source}: a draw outside 0 to {n - 1}.')
        values = chunk[columns].to_numpy(dtype=np.float32).reshape(len(chunk), len(FLOWS), len(elements))
        out[s, d, y] = values
        np.add.at(seen, (s, d, y), 1)
    out.flush()
    if (seen != 1).any():
        count = int((seen == 0).sum())
        twice = int((seen > 1).sum())
        raise ValueError(f'{source}: {count} scenario-draw-years of {FIRST} to {LAST} missing, {twice} written more '
                         'than once; the copy is incomplete.')
    with open(os.path.join(folder, ELEMENTS_FILE), 'w', encoding='utf-8') as handle:
        handle.write('\n'.join(elements) + '\n')
    status = os.stat(source)
    with open(os.path.join(folder, SOURCE_FILE), 'w', encoding='utf-8') as handle:
        handle.write(f'source: {source}\n')
        handle.write(f'size (bytes): {status.st_size}\n')
        handle.write(f'modified: {datetime.datetime.fromtimestamp(status.st_mtime):%Y-%m-%d %H:%M:%S}\n')
        handle.write(f'copied: {datetime.datetime.now():%Y-%m-%d %H:%M:%S}\n')
        handle.write(f'scenarios: {", ".join(SCENARIOS)}\n')
        handle.write(f'draws: {n}\n')
        handle.write(f'years: {FIRST} to {LAST} (in, out: the calendar year; stock: its end)\n')
        handle.write(f'flows: {", ".join(FLOWS)}\n')
        handle.write(f'axes of {DRAWS_FILE}: scenario × draw × year × flow × element (as {ELEMENTS_FILE}), kg\n')
    return path


def main() -> int:
    """Press Run: copy 07's element draws where the settings say, and say what was copied."""
    try:
        params = current()
    except ParameterError as error:
        print(error, file=sys.stderr)
        return 1
    source, folder = params.data.data_center_stock_and_flow_source, absolute(params.data.data_center_draws_dir)
    if not os.path.exists(source):
        print(f'{source}: not there; run 07 in RAWCLICDataCenters first.', file=sys.stderr)
        return 1
    print(f'Copying the element draws of {source} into {folder} …', flush=True)
    try:
        path = copy(source, folder)
    except ValueError as error:
        print(f'Stopped: {error}', file=sys.stderr)
        return 1
    print(f'Written: {path}, with {ELEMENTS_FILE} and {SOURCE_FILE}.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
