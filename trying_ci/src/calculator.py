"""Basic calculator used in CI static analysis demo."""

class Calculator:
    """Provide simple arithmetic operations."""

    def __init__(self):
        """Initialize the calculator with an answer value of zero."""
        self._answer = 0

    def get_answer(self):
        """Return the current stored answer."""
        return self._answer

    def reset(self):
        """Reset the stored answer to zero and return self."""
        self._answer = 0
        return self

    def add(self, num):
        """Add a number to the stored answer and return self."""
        self._answer += num
        return self

    def subtract(self, num):
        """Subtract a number from the stored answer and return self."""
        self._answer -= num
        return self

    def multiply(self, num):
        """Multiply the stored answer by a number and return self."""
        self._answer *= num
        return self

    def power(self, num):
        """Raise the stored answer to the given power and return self."""
        self._answer **= num
        return self
