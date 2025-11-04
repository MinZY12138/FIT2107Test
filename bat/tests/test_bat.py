import unittest
import src.bat as bat_module
import src.bat as bat_module
from .dummy_bat_ui import DummyBatUI
from .dummy_data_manager import DummyDataManager
# Patch dependencies used inside Bat.run()
bat_module.DataManager = DummyDataManager
bat_module.BatUI = DummyBatUI


class TestBat(unittest.TestCase):
    """Unit tests for Bat. One assert per test where feasible."""

    # ---- run() wiring ----
    def test_run_constructs_ui_and_calls_loop_until_quit(self):
        bat = Bat()
        bat.run()  # uses patched DummyDataManager/DummyBatUI
        ui = bat_module.BatUI(DummyDataManager())
        bat.run_loop(ui)
        self.assertEqual(ui.calls[-1], "run_QUIT")

    # ---- run_loop() behavior ----
    def test_run_loop_calls_each_screen_once(self):
        ui = DummyBatUI(DummyDataManager())
        Bat().run_loop(ui)
        self.assertEqual(ui.calls, ["run_HOME", "run_MENU", "run_QUIT"])
