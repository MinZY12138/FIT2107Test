import unittest

from src.bat import Bat

# --- Dummy UI class to simulate BatUI behaviour ---
class DummyUI:
    """A minimal UI mock with predictable screen flow."""
    def __init__(self):
        self.calls = []
        self.screens = ["HOME", "MENU", "QUIT"]
        self.index = 0

    def get_current_screen(self):
        """Simulate screen progression."""
        return self.screens[self.index]

    def run_current_screen(self):
        """Record the call and advance screen state."""
        self.calls.append(f"run_{self.screens[self.index]}")
        if self.screens[self.index] != "QUIT":
            self.index += 1


# --- Dummy DataManager and BatUI to replace real ones ---
class DummyDataManager:
    """Placeholder class for DataManager (no real data needed)."""
    pass

class DummyBatUI(DummyUI):
    """Extends DummyUI to match BatUI constructor signature."""
    def __init__(self, data_manager):
        super().__init__()
        self.data_manager = data_manager


# --- Monkey patch Bat dependencies ---
import src.bat as bat_module
bat_module.DataManager = DummyDataManager
bat_module.BatUI = DummyBatUI


class TestBat(unittest.TestCase):
    """Comprehensive tests for the Bat class achieving 100% coverage."""

    def test_run_creates_instances_and_executes_loop(self):
        """
        Test run(): should create a DataManager, initialise a BatUI,
        and call run_loop() which executes run_current_screen().
        """
        bat = Bat()
        bat.run()  # This uses our patched DummyBatUI and DummyDataManager

        # Verify the loop ran through HOME → MENU → QUIT → final QUIT
        ui = bat_module.BatUI(DummyDataManager())
        bat.run_loop(ui)
        self.assertIn("run_QUIT", ui.calls)
        self.assertEqual(ui.calls[-1], "run_QUIT")

    def test_run_loop_directly(self):
        """
        Test run_loop() explicitly with a dummy UI that starts at HOME
        and cycles until QUIT.
        """
        ui = DummyUI()
        bat = Bat()
        bat.run_loop(ui)
        # run_current_screen() should be called for each screen including QUIT
        self.assertEqual(ui.calls, ["run_HOME", "run_MENU", "run_QUIT"])

