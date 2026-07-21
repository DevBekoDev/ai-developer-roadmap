def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference between two numbers."""
    return a - b


def calculate_average(numbers: list[float]) -> float:
    """Return the average of a list of numbers."""
    if not numbers:
        return 0.0

    return sum(numbers) / len(numbers)