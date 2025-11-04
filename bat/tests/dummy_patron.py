from types import SimpleNamespace
from datetime import datetime

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

    def load_data(self, data, catalogue):  # stub
        self.loaded = True
        return self

    def set_new_patron_data(self, pid, name, age):
        self._id, self._name, self._age = pid, name, age
