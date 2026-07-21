from services.csv_cleaner import (
    calculate_statistics,
    clean_rows,
    load_csv,
    save_csv,
)
from utils.file_utils import get_data_file
from config import INPUT_FILENAME, OUTPUT_FILENAME


def main() -> None:
    input_file = get_data_file(INPUT_FILENAME)
    output_file = get_data_file(OUTPUT_FILENAME)

    fieldnames = ["name", "age", "score"]

    try:
        rows = load_csv(input_file)

    except FileNotFoundError:
        print("Error: Input CSV file was not found.")
        return

    print("CSV file loaded successfully.")
    print(f"Total rows: {len(rows)}")
    print()

    for row in rows:
        print(row)

    cleaned_rows = clean_rows(rows)

    print()
    print(f"Original rows: {len(rows)}")
    print(f"Cleaned rows: {len(cleaned_rows)}")
    print(f"Removed rows: {len(rows) - len(cleaned_rows)}")

    if not cleaned_rows:
        print("No valid rows remain after cleaning.")
        return

    print()

    for row in cleaned_rows:
        print(row)

    stats = calculate_statistics(cleaned_rows)

    print()
    print("Dataset Statistics")
    print(f"Average age: {stats.average_age:.2f}")
    print(f"Average score: {stats.average_score:.2f}")
    print(f"Highest score: {stats.highest_score}")
    print(f"Lowest score: {stats.lowest_score}")

    save_csv(
        output_file,
        cleaned_rows,
        fieldnames,
    )

    print()
    print(f"Cleaned data saved to: {output_file}")


if __name__ == "__main__":
    main()