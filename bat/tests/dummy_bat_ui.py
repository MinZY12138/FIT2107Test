class DummyBatUI:
    """UI double matching BatUI signature and simple screen flow."""
    def __init__(self, data_manager):
        self.data_manager = data_manager
        self.calls = []
        self.screens = ["HOME", "MENU", "QUIT"]
        self.index = 0

    def get_current_screen(self):
        return self.screens[self.index]

    def run_current_screen(self):
        self.calls.append(f"run_{self.screens[self.index]}")
        if self.screens[self.index] != "QUIT":
            self.index += 1
