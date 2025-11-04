from datetime import datetime

class DummyLoan:
    """A minimal Loan replacement for testing string output."""
    def __init__(self, item, due_date: datetime):
        self._item = item
        self._due_date = due_date

    def __str__(self):
        return f"Item {self._item._id} due {self._due_date.strftime('%d/%m/%Y')}"
