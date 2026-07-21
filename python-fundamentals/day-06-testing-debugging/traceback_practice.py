def calculate_average(numbers: list[int]) -> float:
    """Return the average of a list of numbers."""
    total = sum(numbers)
    return total / len(numbers)


def main() -> None:
    scores = []
    average = calculate_average(scores)

    print(f"Average: {average}")


if __name__ == "__main__":
    main()