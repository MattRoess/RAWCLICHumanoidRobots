"""
Tests of 00_parameters.py and the settings in src/params_schema.py.

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein
**Licence:** CC BY 4.0, Creative Commons Attribution 4.0 International; the full text is in `LICENSE`
at the root of the repository.

The settings as written must pass their own checks, a setting that cannot be used must stop with a
ParameterError, and the register must list every setting. Press Run: the register is written into a
temporary folder, nothing in the project is changed.
"""

import os
import sys
import tempfile
import unittest

import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from src.params_io import reference, save  # noqa: E402
from src.params_schema import ParameterError, Params, current, flatten, validate  # noqa: E402

# Every setting the project has; a new one must be added here, so that its arrival is a decision.
KEYS = {'data.workbook', 'data.taxonomy_sheet', 'data.components_sheet', 'data.materials_sheet',
        'data.sources_dir', 'data.shared_lists', 'data.element_recipes', 'checks.tolerance_kg', 'composition.draws',
        'composition.seed', 'composition.nmc_wh_per_kg_min', 'composition.nmc_wh_per_kg_mode',
        'composition.nmc_wh_per_kg_max', 'output.schemas_dir', 'output.composition_dir',
        'output.composition_figures_dir', 'output.comparison_dir', 'output.dpi'}


class TestSettings(unittest.TestCase):

    def test_the_settings_as_written_are_valid(self):
        self.assertIsInstance(current(), Params)

    def test_every_setting_is_listed_with_a_description(self):
        rows = flatten(current())
        self.assertEqual({key for _, _, key, _ in rows}, KEYS)
        for name, description, key, _ in rows:
            self.assertTrue(description.strip(), f'{key} has no description')

    def test_a_setting_that_cannot_be_used_stops(self):
        for section, name, value in (('data', 'workbook', 'workbook.csv'),
                                     ('data', 'shared_lists', 'lists.csv'),
                                     ('data', 'element_recipes', 'recipes.csv'),
                                     ('data', 'components_sheet', ' '),
                                     ('data', 'materials_sheet', ''),
                                     ('checks', 'tolerance_kg', 0),
                                     ('checks', 'tolerance_kg', 0.08),
                                     ('composition', 'draws', 50),
                                     ('composition', 'draws', 2_000_000),
                                     ('composition', 'seed', -1),
                                     ('composition', 'nmc_wh_per_kg_mode', 300.0),
                                     ('output', 'composition_dir', ' '),
                                     ('output', 'dpi', 10)):
            params = Params()
            setattr(getattr(params, section), name, value)
            with self.assertRaises(ParameterError, msg=f'{section}.{name} = {value!r}'):
                validate(params)


class TestRegister(unittest.TestCase):

    def test_the_register_holds_every_setting(self):
        params = current()
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, 'params.xlsx')
            save(params, path)
            frame = pd.read_excel(path)
        self.assertEqual(set(frame['key']), KEYS)

    def test_the_markdown_reference_names_every_setting(self):
        text = reference(current())
        for key in KEYS:
            self.assertIn(f'`{key}`', text)


if __name__ == '__main__':
    unittest.main()
