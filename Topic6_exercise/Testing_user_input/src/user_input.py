"""Utility functions for reading and validating user input."""


def is_int(val):
    """Return True if val can be parsed as an int, else False."""
    try:
        int(val)
        return True
    except ValueError:
        return False


def is_float(val):
    """Return True if val can be parsed as a float, else False."""
    try:
        float(val)
        return True
    except ValueError:
        return False


def read_string(prompt):
    """Print prompt and return raw user input."""
    return input(prompt)


def read_integer(prompt):
    """Read an integer from the user; keep asking until valid."""
    line = read_string(prompt)
    while not is_int(line):
        print("Please enter a whole number.")
        line = read_string(prompt)
    num = int(line)
    return num


def read_float(prompt):
    """Read a float from the user; keep asking until valid."""
    line = read_string(prompt)
    while not is_float(line):
        print("Please enter a decimal number.")
        line = read_string(prompt)
    num = float(line)
    return num


def read_integer_range(prompt, min_value, max_value):
    """Read an int within [min_value, max_value]; keep asking until valid."""
    num = read_integer(prompt)
    while (num < min_value) or (num > max_value):
        print(f"Please enter a value between {min_value} and {max_value}")
        num = read_integer(prompt)
    return num


def read_float_range(prompt, min_value, max_value):
    """Read a float within [min_value, max_value]; keep asking until valid."""
    num = read_float(prompt)
    while (num < min_value) or (num > max_value):
        print(f"Please enter a value between {min_value} and {max_value}")
        num = read_float(prompt)
    return num
