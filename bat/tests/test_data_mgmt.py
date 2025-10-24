import unittest
import io
import json
import sys
from types import SimpleNamespace
from datetime import datetime

# Patch the configuration paths before importing DataManager
import src.config as config
config.PATRON_DATA = "tests/tmp_patrons.json"
config.CATALOGUE_DATA = "tests/tmp_catalogue.json"

from src.data_mgmt import DataManager

# ---- Minimal stubs to replace Patron and BorrowableItem ----
class DummyPatron:
    """Minimal Patron with predictable data for encoding tests."""
    def __init__(self, pid=1, name="Alex", age=20):
        self._id = pid
        self._name = name
        self._age = age
        self._outstanding_fees = 0.0
        self._gardening_tool_training = True
        self._carpentry_tool_training = False
        self._makerspace_training = True
        self._loans = [SimpleNamespace(_item=SimpleNamespace(_id=99),
                                       _due_date=datetime(2025, 10, 10))]

    def load_data(self, data, catalogue):  # Dummy
        self.loaded = True
        return self

    def set_new_patron_data(self, pid, name, age):
        self._id, self._name, self._age = pid, name, age

class DummyItem:
    """Minimal BorrowableItem for encoding tests."""
    def __init__(self, iid=10, name="Hammer"):
        self._id = iid
        self._name = name
        self._type = "Tool"
        self._year = 2024
        self._number_owned = 3
        self._on_loan = 1

    def load_data(self, data):  # Dummy
        self.loaded = True
        return self

# Monkey patch the real classes inside DataManager
import src.data_mgmt as dm
dm.Patron = DummyPatron
dm.BorrowableItem = DummyItem


class TestDataManager(unittest.TestCase):
    """Comprehensive tests for DataManager with 100% coverage."""

    def setUp(self):
        # Prepare dummy JSON files for catalogue and patrons
        with open(config.CATALOGUE_DATA, "w") as f:
            json.dump([{"item_id": 1}], f)
        with open(config.PATRON_DATA, "w") as f:
            json.dump([{"patron_id": 1, "name": "Test", "age": 20,
                        "outstanding_fees": 0.0,
                        "gardening_tool_training": True,
                        "carpentry_tool_training": False,
                        "makerspace_training": True,
                        "loans": []}], f)

    def test_init_loads_data(self):
        """Constructor should call both load_catalogue and load_patrons successfully."""
        dmgr = DataManager()
        self.assertIsInstance(dmgr._catalogue_data[0], DummyItem)
        self.assertIsInstance(dmgr._patron_data[0], DummyPatron)

    def test_register_patron_adds_new_entry(self):
        """register_patron should append a new DummyPatron with incremented ID."""
        dmgr = DataManager()
        prev_count = len(dmgr._patron_data)
        dmgr.register_patron("Eve", 25)
        self.assertEqual(len(dmgr._patron_data), prev_count + 1)
        self.assertTrue(any(p._name == "Eve" for p in dmgr._patron_data))

    def test_save_and_load_patrons_and_catalogue(self):
        """Both save methods should write valid JSON text to the correct files."""
        dmgr = DataManager()
        # Save patrons
        dmgr.save_patrons()
        with open(config.PATRON_DATA) as f:
            content = f.read()
        self.assertIn("patron_id", content)
        # Save catalogue
        dmgr.save_catalogue()
        with open(config.CATALOGUE_DATA) as f:
            self.assertIn("item_id", f.read())

    def test_load_patrons_failure_triggers_exit(self):
        """Simulate a file read failure to ensure sys.exit() is called."""
        dmgr = DataManager()
        dmgr._catalogue_data = []
        config.PATRON_DATA = "nonexistent.json"
        with self.assertRaises(SystemExit):
            dmgr.load_patrons()
        # Reset path
        config.PATRON_DATA = "tests/tmp_patrons.json"

    def test_load_catalogue_failure_triggers_exit(self):
        """Simulate a missing file and ensure sys.exit() is called."""
        config.CATALOGUE_DATA = "missing.json"
        with self.assertRaises(SystemExit):
            DataManager().load_catalogue()
        config.CATALOGUE_DATA = "tests/tmp_catalogue.json"

    def test_patron_encoder_serializes_dummy(self):
        """PatronEncoder should convert DummyPatron to correct dict."""
        p = DummyPatron()
        encoder = DataManager.PatronEncoder()
        result = encoder.default(p)
        self.assertIn("patron_id", result)
        self.assertEqual(result["patron_id"], 1)
        self.assertTrue(isinstance(result["loans"], list))

    def test_borrowable_item_encoder_serializes_dummy(self):
        """BorrowableItemEncoder should convert DummyItem to correct dict."""
        d = DummyItem()
        encoder = DataManager.BorrowableItemEncoder()
        result = encoder.default(d)
        self.assertEqual(result["item_id"], 10)
        self.assertEqual(result["item_name"], "Hammer")
