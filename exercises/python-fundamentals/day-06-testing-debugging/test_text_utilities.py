import importlib.util
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[3]

MODULE_PATH = (
    REPOSITORY_ROOT
    / "python-fundamentals"
    / "day-02-functions-clean-code"
    / "text_utilities.py"
)

spec = importlib.util.spec_from_file_location(
    "text_utilities",
    MODULE_PATH,
)

text_utilities = importlib.util.module_from_spec(spec)
spec.loader.exec_module(text_utilities)

clean_text = text_utilities.clean_text

def test_clean_text_removes_extra_spaces_and_lowercase() -> None:
    input_text = "  Hello   World  "
    expected_output = "hello world"
    assert clean_text(input_text) == expected_output

def test_count_words_counts_correctly() -> None:
    input_text = "  This is a test.  "
    expected_count = 4
    assert text_utilities.count_words(input_text) == expected_count