def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("b must not be zero")
    return a / b


def mean(values):
    values = list(values)
    if not values:
        raise ValueError("mean of an empty sequence")
    return sum(values) / len(values)
