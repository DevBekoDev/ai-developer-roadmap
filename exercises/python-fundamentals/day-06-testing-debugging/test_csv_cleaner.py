import sys
from pathlib import Path

import pytest


REPOSITORY_ROOT = Path(__file__).resolve().parents[3]

DAY_5_PROJECT = (
    REPOSITORY_ROOT
    / "projects"
    / "python-fundamentals"
    / "day-05-modules-project-structure"
)

sys.path.insert(0, str(DAY_5_PROJECT))

from services.csv_cleaner import clean_rows, calculate_statistics


def test_clean_rows_removes_rows_with_missing_values() -> None:
    rows = [
        {"name": "Alice", "age": "20", "score": "85"},
        {"name": "", "age": "22", "score": "90"},
        {"name": "Bob", "age": "", "score": "75"},
        {"name": "Charlie", "age": "21", "score": ""},
    ]

    expected_rows = [
        {"name": "Alice", "age": "20", "score": "85"},
    ]

    result = clean_rows(rows)

    assert result == expected_rows


def test_clean_rows_keeps_rows_with_all_values() -> None:
    rows = [
        {"name": "Alice", "age": "20", "score": "85"},
        {"name": "Bob", "age": "22", "score": "90"},
    ]

    expected_rows = [
        {"name": "Alice", "age": "20", "score": "85"},
        {"name": "Bob", "age": "22", "score": "90"},
    ]

    result = clean_rows(rows)

    assert result == expected_rows


def test_calculate_statistics_returns_correct_values() -> None:
    rows = [
        {"name": "Alice", "age": "20", "score": "85"},
        {"name": "Bob", "age": "22", "score": "90"},
        {"name": "Charlie", "age": "21", "score": "75"},
    ]

    stats = calculate_statistics(rows)

    assert stats.average_age == 21.0
    assert stats.average_score == pytest.approx(83.33333333333333)
    assert stats.highest_score == 90
    assert stats.lowest_score == 75


def test_clean_rows_returns_empty_list_for_empty_input() -> None:
    rows = []

    result = clean_rows(rows)

    assert result == []