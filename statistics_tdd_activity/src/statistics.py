# src/statistics.py

def sum(data):
    if data is None or len(data) == 0:
        raise ValueError("data must be non-empty")
    total = 0
    for x in data:          # 不用内置 sum
        total += x
    return total

def mean(data):
    if data is None or len(data) == 0:
        raise ValueError("data must be non-empty")
    total = 0
    count = 0
    for x in data:
        total += x
        count += 1
    return total / count

def minimum(data):
    if data is None or len(data) == 0:
        raise ValueError("data must be non-empty")
    first = True
    m = None
    for x in data:
        if first:
            m = x
            first = False
        elif x < m:
            m = x
    return m

def maximum(data):
    if data is None or len(data) == 0:
        raise ValueError("data must be non-empty")
    first = True
    m = None
    for x in data:
        if first:
            m = x
            first = False
        elif x > m:
            m = x
    return m


