class DummyItem:
    """Minimal BorrowableItem for encoding tests."""
    def __init__(self, iid=10, name="Hammer"):
        self._id = iid
        self._name = name
        self._type = "Tool"
        self._year = 2024
        self._number_owned = 3
        self._on_loan = 1

    def load_data(self, data):  # stub
        self.loaded = True
        return self
