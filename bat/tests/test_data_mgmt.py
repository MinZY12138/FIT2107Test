import unittest
from .dummy_patron import DummyPatron
from .dummy_item import DummyItem

# --- Patch config paths BEFORE importing DataManager ---
import src.config as config
config.PATRON_DATA = "tests/tmp_patrons.json"
config.CATALOGUE_DATA = "tests/tmp_catalogue.json"

from tests.dummy_patron import DummyPatron
from tests.dummy_item import DummyItem

import src.data_mgmt as dm
dm.Patron = DummyPatron          # monkey patch to use dummies
dm.BorrowableItem = DummyItem

from src.data_mgmt import DataManager


class TestDataManager(unittest.TestCase):
    """Unit tests for DataManager. One assert per test method where feasible."""

    def setUp(self):
        # Prepare minimal valid JSON files
        with open(config.CATALOGUE_DATA, "w", encoding="utf-8") as f:
            json.dump([{"item_id": 1}], f)
        with open(config.PATRON_DATA, "w", encoding="utf-8") as f:
            json.dump([{
                "patron_id": 1, "name": "Test", "age": 20,
                "outstanding_fees": 0.0,
                "gardening_tool_training": True,
                "carpentry_tool_training": False,
                "makerspace_training": True,
                "loans": []
            }], f)

    def tearDown(self):
        # Clean up tmp files
        for p in (config.CATALOGUE_DATA, config.PATRON_DATA):
            try:
                os.remove(p)
            except FileNotFoundError:
                pass
        # Reset paths (in case tests changed them)
        config.PATRON_DATA = "tests/tmp_patrons.json"
        config.CATALOGUE_DATA = "tests/tmp_catalogue.json"

    # -------- init loads --------

    def test_init_loads_catalogue_as_dummyitem(self):
        mgr = DataManager()
        self.assertIsInstance(mgr._catalogue_data[0], DummyItem)

    def test_init_loads_patrons_as_dummypatron(self):
        mgr = DataManager()
        self.assertIsInstance(mgr._patron_data[0], DummyPatron)

    # -------- register_patron --------

    def test_register_patron_increments_count(self):
        mgr = DataManager()
        before = len(mgr._patron_data)
        mgr.register_patron("Eve", 25)
        self.assertEqual(len(mgr._patron_data), before + 1)

    def test_register_patron_appends_name_eve(self):
        mgr = DataManager()
        mgr.register_patron("Eve", 25)
        self.assertTrue(any(p._name == "Eve" for p in mgr._patron_data))

    # -------- save_* writes --------

    def test_save_patrons_writes_patron_id_key(self):
        mgr = DataManager()
        mgr.save_patrons()
        with open(config.PATRON_DATA, encoding="utf-8") as f:
            content = f.read()
        self.assertIn("patron_id", content)

    def test_save_catalogue_writes_item_id_key(self):
        mgr = DataManager()
        mgr.save_catalogue()
        with open(config.CATALOGUE_DATA, encoding="utf-8") as f:
            content = f.read()
        self.assertIn("item_id", content)

    # -------- load failures --------

    def test_load_patrons_missing_file_exits(self):
        mgr = DataManager()
        config.PATRON_DATA = "tests/does_not_exist.json"
        with self.assertRaises(SystemExit):
            mgr.load_patrons()

    def test_load_catalogue_missing_file_exits(self):
        config.CATALOGUE_DATA = "tests/missing.json"
        with self.assertRaises(SystemExit):
            DataManager().load_catalogue()

    # -------- encoders: Patron --------

    def test_patron_encoder_has_patron_id_key(self):
        result = DataManager.PatronEncoder().default(DummyPatron())
        self.assertIn("patron_id", result)

    def test_patron_encoder_patron_id_is_1(self):
        result = DataManager.PatronEncoder().default(DummyPatron())
        self.assertEqual(result["patron_id"], 1)

    def test_patron_encoder_loans_is_list(self):
        result = DataManager.PatronEncoder().default(DummyPatron())
        self.assertIsInstance(result["loans"], list)

    # -------- encoders: BorrowableItem --------

    def test_item_encoder_item_id_is_10(self):
        result = DataManager.BorrowableItemEncoder().default(DummyItem())
        self.assertEqual(result["item_id"], 10)

    def test_item_encoder_item_name_is_hammer(self):
        result = DataManager.BorrowableItemEncoder().default(DummyItem())
        self.assertEqual(result["item_name"], "Hammer")
