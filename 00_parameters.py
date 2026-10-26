"""
00_parameters.py
================

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

The first stage. Checks the settings in `src/params_schema.py`, prints them and says which input files
are on disk, then writes the register of them: `params.xlsx` and
`documentation/claude/PARAMETER_REFERENCE.md`. Press Run.

**To change a setting, edit `src/params_schema.py`**, then press Run here to refresh the register. The
spreadsheet and the Markdown reference are OUTPUTS: editing either of them changes nothing, because
nothing reads them.

NO ARGUMENTS, AND NOT BY OVERSIGHT. This project is run by pressing Run on the numbered stages; a switch
that only exists on a command line is a switch the person running this never sees.

Where it sits: first; next is `01_schemas.py`. This file is intentionally thin: every setting, its value
and its description live in `src/params_schema.py`, the writing lives in `src/params_io.py`.
"""

from __future__ import annotations

import os
import sys

# Run from anywhere, and put the project root on the path. Must come before any import of src.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.params_io import PARAMS_FILE, reference, save  # noqa: E402
from src.params_schema import ParameterError, absolute, current, flatten, source_status  # noqa: E402

# The Markdown copy of the register, with the documents Claude writes for this project.
REFERENCE_FILE = absolute(os.path.join('documentation', 'claude', 'PARAMETER_REFERENCE.md'))


def main() -> int:
    """Check the settings, print them and the input files, write the register."""
    try:
        params = current()
    except ParameterError as error:
        print(error, file=sys.stderr)
        return 1

    rows = flatten(params)

    print('src/params_schema.py is valid. Values in force:')
    width = max(len(key) for _, _, key, _ in rows)
    for _, _, key, value in rows:
        print(f'  {key:<{width}} {value}')

    # Data files are not part of the code, so the first thing worth knowing on another computer is
    # whether the workbook the stages read is actually here.
    print(f'\nInput files\n  {source_status(params)}\n')

    save(params, PARAMS_FILE)
    print(f'{os.path.relpath(PARAMS_FILE, absolute(""))}: regenerated ({len(rows)} settings)')

    os.makedirs(os.path.dirname(REFERENCE_FILE), exist_ok=True)
    with open(REFERENCE_FILE, 'w') as handle:
        handle.write(reference(params))
    print(f'{os.path.relpath(REFERENCE_FILE, absolute(""))}: regenerated')
    print('\nNext: press Run on 01_schemas.py, the schemas of what the workbook defines.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
