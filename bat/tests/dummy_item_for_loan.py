class ItemStub:
    """Minimal item stub with attributes used by Loan.__str__."""
    def __init__(self, item_id, name, type_):
        self._id = item_id
        self._name = name
        self._type = type_