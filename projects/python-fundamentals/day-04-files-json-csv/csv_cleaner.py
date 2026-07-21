import csv
from pathlib import Path


data_folder = Path.cwd() / "data"
input_file = data_folder / "messy_students.csv"

rows = []


try:
    with input_file.open(
        "r",
        newline="",
        encoding="utf-8"
    ) as file:
        reader = csv.DictReader(file)
        rows = list(reader)

except FileNotFoundError:
    print("Error: Input CSV file was not found.")

else:
    print("CSV file loaded successfully.")
    print(f"Total rows: {len(rows)}")
    print()

    for row in rows:
        print(row)

    cleaned_rows = []

    for row in rows:
        if (
            row["name"] != ""
            and row["age"] != ""
            and row["score"] != ""
        ):
            cleaned_rows.append(row)

    print()
    print(f"Original rows: {len(rows)}")
    print(f"Cleaned rows: {len(cleaned_rows)}")
    print(f"Removed rows: {len(rows) - len(cleaned_rows)}")
    print()

    for row in cleaned_rows:
        print(row)

    ages = []
    scores = []

    for row in cleaned_rows:
        ages.append(int(row["age"]))
        scores.append(int(row["score"]))

    average_age = sum(ages) / len(ages)
    average_score = sum(scores) / len(scores)
    highest_score = max(scores)
    lowest_score = min(scores)

    print()
    print("Dataset Statistics")
    print(f"Average age: {average_age:.2f}")
    print(f"Average score: {average_score:.2f}")
    print(f"Highest score: {highest_score}")
    print(f"Lowest score: {lowest_score}")

    output_file = data_folder / "cleaned_students.csv"

    fieldnames = ["name", "age", "score"]

    with output_file.open(
        "w",
        newline="",
        encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(cleaned_rows)

    print()
    print(f"Cleaned data saved to: {output_file}")