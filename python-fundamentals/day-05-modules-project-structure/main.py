from utils import add, subtract, calculate_average


def main() -> None:
    result = add(10, 5)
    difference = subtract(10, 5)
    average = calculate_average([10, 20, 30, 40])

    print(f"Addition: {result}")
    print(f"Subtraction: {difference}")
    print(f"Average: {average}")


if __name__ == "__main__":
    main()