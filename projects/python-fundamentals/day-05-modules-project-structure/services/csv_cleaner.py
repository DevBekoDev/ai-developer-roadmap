import csv
from pathlib import Path

from models.cleaning_stats import CleaningStats


def load_csv(file_path: Path) -> list[dict[str, str]]:
    """Load a CSV file and return its rows as dictionaries."""

    with file_path.open(
        "r",
        newline="",
        encoding="utf-8",
    ) as file:
        reader = csv.DictReader(file)
        return list(reader)


def clean_rows(
    rows: list[dict[str, str]],
) -> list[dict[str, str]]:
    """Remove rows that contain missing required values."""

    cleaned_rows = []

    for row in rows:
        if (
            row["name"] != ""
            and row["age"] != ""
            and row["score"] != ""
        ):
            cleaned_rows.append(row)

    return cleaned_rows


def calculate_statistics(
    rows: list[dict[str, str]],
) -> CleaningStats:
    """Calculate statistics from cleaned student rows."""

    ages = []
    scores = []

    for row in rows:
        ages.append(int(row["age"]))
        scores.append(int(row["score"]))

    average_age = sum(ages) / len(ages)
    average_score = sum(scores) / len(scores)
    highest_score = max(scores)
    lowest_score = min(scores)

    return CleaningStats(
        average_age=average_age,
        average_score=average_score,
        highest_score=highest_score,
        lowest_score=lowest_score,
    )


def save_csv(
    file_path: Path,
    rows: list[dict[str, str]],
    fieldnames: list[str],
) -> None:
    """Save rows to a CSV file."""

    with file_path.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames,
        )

        writer.writeheader()
        writer.writerows(rows)