# src/statistics.py

def sum(data):
    if data is None or len(data) == 0:
        raise ValueError("data must be non-empty")
    total = 0
    for x in data:
        total += x
    return total

def mean(data):
    return None

def minimum(data):
    return None

def maximum(data):
    return None
