# Python Testing with Pytest

## What Is Software Testing?

Software testing checks whether a program behaves as expected.

A test usually compares:

```text
Actual result
      ↓
Expected result
```

For example, suppose this function should add two numbers:

```python
def add(a: int, b: int) -> int:
    return a + b
```

A test can verify that:

```python
add(2, 3)
```

returns:

```text
5
```

Testing helps detect mistakes before they reach users or become part of a larger application.

---

## Manual Testing vs Automated Testing

### Manual testing

A developer runs the program and checks the result personally.

Example:

```python
result = add(2, 3)
print(result)
```

The developer looks at the output and decides whether it is correct.

Manual testing is useful while exploring code, but it becomes slow and unreliable as projects grow.

### Automated testing

A test framework runs checks automatically.

Example:

```python
def test_add() -> None:
    assert add(2, 3) == 5
```

The framework reports whether the test passed or failed.

Automated tests can be rerun whenever the code changes.

---

## What Is Pytest?

`pytest` is a popular Python testing framework.

It can:

- Discover test files automatically
- Discover test functions automatically
- Run many tests together
- Display passing and failing tests
- Show expected and actual values
- Test exceptions
- Compare floating-point values
- Organize larger test suites

Install it inside an activated virtual environment:

```powershell
python -m pip install -U pytest
```

Verify the installation:

```powershell
pytest --version
```

---

## Pytest Naming Conventions

Pytest automatically searches for files whose names follow patterns such as:

```text
test_*.py
```

Examples:

```text
test_math_utils.py
test_text_utilities.py
test_csv_cleaner.py
```

Inside those files, pytest discovers functions whose names begin with:

```text
test_
```

Example:

```python
def test_add() -> None:
    assert add(2, 3) == 5
```

A function named:

```python
def check_add() -> None:
```

would not normally be discovered automatically.

---

## Running Tests

Run all discovered tests from the repository root:

```powershell
pytest
```

Run one test file:

```powershell
pytest exercises/python-fundamentals/day-06-testing-debugging/test_csv_cleaner.py
```

Run one specific test:

```powershell
pytest exercises/python-fundamentals/day-06-testing-debugging/test_csv_cleaner.py::test_clean_rows_returns_empty_list_for_empty_input
```

Run tests with more detailed output:

```powershell
pytest -v
```

The `-v` option means:

```text
verbose
```

It displays the full name and result of each test.

---

## Understanding `assert`

`assert` checks whether a condition is true.

Example:

```python
assert 2 + 3 == 5
```

The condition is true, so execution continues.

This assertion fails:

```python
assert 2 + 3 == 6
```

Python raises:

```text
AssertionError
```

Inside pytest:

```python
def test_add() -> None:
    assert add(2, 3) == 5
```

means:

> The actual result of `add(2, 3)` must equal the expected result `5`.

---

## Actual and Expected Results

A clear test often separates the input, actual result, and expected result.

```python
def test_clean_text_removes_extra_spaces() -> None:
    text = "   Hello    WORLD   "
    expected_text = "hello world"

    result = clean_text(text)

    assert result == expected_text
```

This structure is easy to read:

```text
Arrange
    Prepare the input and expected result

Act
    Call the function

Assert
    Compare the actual result with the expectation
```

This pattern is often called:

```text
Arrange → Act → Assert
```

---

## A Passing Test

Example:

```python
def multiply(a: int, b: int) -> int:
    return a * b


def test_multiply() -> None:
    result = multiply(4, 5)

    assert result == 20
```

Running pytest should report:

```text
1 passed
```

A passing test confirms that the function behaved as expected for that test case.

---

## A Failing Test

Suppose the test incorrectly expects:

```python
def test_multiply() -> None:
    result = multiply(4, 5)

    assert result == 25
```

Pytest reports information similar to:

```text
E       assert 20 == 25
```

This shows:

```text
Actual result:   20
Expected result: 25
```

A failing test does not always mean the application code is wrong.

The mistake may be in:

- The application code
- The test expectation
- The test input
- The test setup
- The import configuration

Both the code and the test should be reviewed.

---

## Testing Text-Cleaning Functions

Example function:

```python
def clean_text(text: str) -> str:
    """Remove extra whitespace and convert text to lowercase."""
    words = text.strip().lower().split()

    return " ".join(words)
```

Test:

```python
def test_clean_text_removes_extra_spaces_and_lowercases() -> None:
    text = "   Hello     WORLD   "
    expected_text = "hello world"

    result = clean_text(text)

    assert result == expected_text
```

This test checks two behaviors:

1. Extra whitespace is removed.
2. Uppercase letters are converted to lowercase.

---

## Testing Word Counting

Example function:

```python
def count_words(text: str) -> int:
    cleaned_text = clean_text(text)

    if not cleaned_text:
        return 0

    return len(cleaned_text.split())
```

Test:

```python
def test_count_words_returns_correct_count() -> None:
    text = "Python is great for AI"

    result = count_words(text)

    assert result == 5
```

The test checks that the function returns the expected number of words.

---

## Testing Data-Cleaning Functions

Example input:

```python
rows = [
    {"name": "Alice", "age": "20", "score": "85"},
    {"name": "", "age": "22", "score": "90"},
]
```

Expected output:

```python
expected_rows = [
    {"name": "Alice", "age": "20", "score": "85"},
]
```

Test:

```python
def test_clean_rows_removes_rows_with_missing_values() -> None:
    rows = [
        {"name": "Alice", "age": "20", "score": "85"},
        {"name": "", "age": "22", "score": "90"},
    ]

    expected_rows = [
        {"name": "Alice", "age": "20", "score": "85"},
    ]

    result = clean_rows(rows)

    assert result == expected_rows
```

This verifies that incomplete rows are removed.

---

## Testing Valid Input

Tests should not only check what gets removed.

They should also verify that valid data remains unchanged.

```python
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
```

A good test suite checks both:

```text
Invalid data is rejected
Valid data is preserved
```

---

## Testing Empty Input

Empty input is a common edge case.

Example:

```python
def test_clean_rows_returns_empty_list_for_empty_input() -> None:
    rows = []

    result = clean_rows(rows)

    assert result == []
```

This checks that the function handles an empty list without crashing or returning an unexpected value.

---

## What Is an Edge Case?

An edge case is an unusual or extreme input that may expose problems.

Examples include:

- Empty strings
- Empty lists
- Zero
- Negative numbers
- Missing dictionary keys
- Duplicate records
- Very long input
- Invalid file paths
- Whitespace-only text
- No valid rows after cleaning

Normal case:

```text
"Python is useful"
```

Edge case:

```text
"     "
```

Both should be considered when designing tests.

---

## Testing Objects

The statistics function returns a `CleaningStats` object.

```python
stats = calculate_statistics(rows)
```

A test can inspect its attributes:

```python
def test_calculate_statistics_returns_correct_values() -> None:
    rows = [
        {"name": "Alice", "age": "20", "score": "85"},
        {"name": "Bob", "age": "22", "score": "90"},
        {"name": "Charlie", "age": "21", "score": "75"},
    ]

    stats = calculate_statistics(rows)

    assert stats.average_age == 21.0
    assert stats.highest_score == 90
    assert stats.lowest_score == 75
```

Each assertion checks one part of the returned object.

---

## Floating-Point Comparisons

Floating-point calculations can contain tiny precision differences.

For example:

```python
(85 + 90 + 75) / 3
```

may produce a long decimal:

```text
83.33333333333333
```

Instead of relying on exact equality, pytest provides:

```python
pytest.approx()
```

Example:

```python
import pytest


def test_average_score() -> None:
    stats = calculate_statistics(rows)

    assert stats.average_score == pytest.approx(
        83.33333333333333
    )
```

`pytest.approx()` allows tiny floating-point differences while still checking that the value is correct.

Use exact equality for values such as:

```python
assert stats.highest_score == 90
```

Use approximate comparison for calculated decimals when necessary.

---

## Testing Exceptions

Some functions should raise an exception for invalid input.

Example:

```python
def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("b cannot be zero.")

    return a / b
```

Pytest can verify this behavior:

```python
import pytest


def test_divide_raises_error_for_zero() -> None:
    with pytest.raises(ValueError):
        divide(10, 0)
```

The test passes only if `ValueError` is raised.

The error message can also be tested:

```python
def test_divide_has_clear_error_message() -> None:
    with pytest.raises(
        ValueError,
        match="b cannot be zero",
    ):
        divide(10, 0)
```

---

## Test Independence

Each test should be able to run independently.

A test should not require another test to run first.

Bad dependency:

```text
Test 1 creates important data
Test 2 assumes Test 1 already ran
```

Better:

```text
Each test creates its own required input
```

Independent tests are easier to:

- Run individually
- Debug
- Reorder
- Maintain
- Execute in parallel

---

## One Behavior per Test

A test should usually focus on one clear behavior.

Clear:

```python
def test_clean_rows_removes_missing_names() -> None:
    ...
```

Less clear:

```python
def test_everything() -> None:
    # Tests cleaning
    # Tests statistics
    # Tests saving
    # Tests error handling
    ...
```

Focused tests make failures easier to understand.

When a focused test fails, its name immediately explains which behavior is broken.

---

## Descriptive Test Names

A test name should describe:

```text
What is being tested
+
What behavior is expected
```

Good examples:

```python
test_clean_rows_removes_rows_with_missing_values
test_clean_rows_keeps_rows_with_all_values
test_calculate_statistics_returns_correct_values
test_clean_rows_returns_empty_list_for_empty_input
```

Less useful:

```python
test_one
test_function
test_data
```

Descriptive names improve reports and documentation.

---

## Importing Code from Other Folders

Tests may need to import code from a project stored elsewhere in the repository.

Example project location:

```text
projects/python-fundamentals/day-05-modules-project-structure/
```

A test can temporarily add that folder to Python’s search path:

```python
import sys
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[3]

DAY_5_PROJECT = (
    REPOSITORY_ROOT
    / "projects"
    / "python-fundamentals"
    / "day-05-modules-project-structure"
)

sys.path.insert(0, str(DAY_5_PROJECT))

from services.csv_cleaner import clean_rows
```

This allows Python to locate:

```text
services/
models/
utils/
```

at runtime.

For larger projects, packaging the application properly is preferable to repeatedly modifying `sys.path`.

---

## Import Side Effects

When Python imports a file, it executes top-level code inside that file.

Problematic module:

```python
def clean_text(text: str) -> str:
    return text.strip().lower()


original_text = input("Enter text: ")
```

Importing this file immediately calls:

```python
input()
```

This causes problems during automated testing.

The solution is to place interactive code inside `main()`:

```python
def clean_text(text: str) -> str:
    return text.strip().lower()


def main() -> None:
    original_text = input("Enter text: ")
    print(clean_text(original_text))


if __name__ == "__main__":
    main()
```

Now:

```text
Running the file directly
    main() runs

Importing the file
    main() does not run
```

This makes the functions safe to test and reuse.

---

## Understanding Pytest Progress Percentages

Pytest may show:

```text
test_text_utilities.py ..                            [66%]
test_csv_cleaner.py .                                [100%]
```

The percentage is not a test score.

It shows how much of the complete test run has finished.

For example:

```text
2 of 3 tests completed
    ↓
66%
```

The final summary determines the actual result:

```text
3 passed
```

---

## Pytest Cache

Pytest may create:

```text
.pytest_cache/
```

This is generated data used to improve test execution.

It should normally be excluded from Git:

```gitignore
.pytest_cache/
```

Python may also generate:

```text
__pycache__/
```

Ignore it using:

```gitignore
__pycache__/
*.py[cod]
```

---

## Tests and Virtual Environments

Pytest should be installed inside the project’s virtual environment.

Create and activate an environment:

```powershell
python -m venv .venv
```

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

```powershell
.\.venv\Scripts\Activate.ps1
```

Install pytest:

```powershell
python -m pip install -U pytest
```

Confirm the active Python interpreter:

```powershell
python -c "import sys; print(sys.executable)"
```

Then run:

```powershell
pytest
```

Using an isolated environment makes test results more reproducible.

---

## Tests as Documentation

Tests explain how functions are expected to behave.

For example:

```python
def test_clean_text_removes_extra_spaces_and_lowercases() -> None:
```

documents that `clean_text()` should:

- Remove extra spaces
- Convert text to lowercase

A developer reading the tests can understand the intended behavior without examining every implementation detail.

---

## Regression Testing

A regression happens when a previously working feature breaks after a code change.

Example:

1. `clean_rows()` works correctly.
2. A developer modifies it.
3. The change accidentally stops removing missing scores.
4. Existing tests detect the problem.

Automated tests protect completed functionality from future changes.

Running:

```powershell
pytest
```

after each important change helps detect regressions quickly.

---

## Testing in AI Applications

AI applications can test deterministic parts such as:

- Input validation
- Text cleaning
- Prompt formatting
- Dataset loading
- JSON parsing
- API request construction
- Response extraction
- Token calculations
- Cost estimation
- File handling
- Data transformations
- Evaluation metric calculations

Example:

```python
def build_prompt(question: str) -> str:
    return f"Answer clearly: {question.strip()}"
```

Test:

```python
def test_build_prompt_formats_question() -> None:
    result = build_prompt("  What is AI?  ")

    assert result == "Answer clearly: What is AI?"
```

AI model outputs may be probabilistic, but the surrounding application logic can still be tested carefully.

---

## Good Testing Practices

- Give tests descriptive names.
- Use Arrange, Act, Assert.
- Keep tests independent.
- Test one clear behavior at a time.
- Test normal inputs.
- Test invalid inputs.
- Test edge cases.
- Test expected exceptions.
- Use `pytest.approx()` for floating-point values.
- Avoid interactive code during imports.
- Run all tests after changing application code.
- Keep generated test caches out of Git.
- Treat failing tests as useful information.
- Review both the code and the expectation when a test fails.

---

## Week 1 Test Suite

The Week 1 repository contains tests for:

1. Addition
2. Text cleaning
3. Word counting
4. Removing incomplete CSV rows
5. Keeping complete CSV rows
6. Calculating statistics
7. Handling empty row input

Final result:

```text
7 passed
0 failed
```

The original roadmap listed a target of ten tests. The target was intentionally adjusted to seven passing tests while completing the main testing, assertion, traceback, and debugger lessons.

---

## Summary

Testing checks that software behaves as expected.

Important concepts include:

- Pytest automatically discovers properly named tests.
- `assert` compares actual and expected behavior.
- Tests should be focused and independent.
- Descriptive names explain the behavior being checked.
- Edge cases reveal problems that normal inputs may not expose.
- `pytest.approx()` handles floating-point comparisons.
- `pytest.raises()` verifies expected exceptions.
- The main guard prevents import side effects.
- Automated tests detect regressions.
- Tests also serve as technical documentation.

A reliable Python or AI application is not only built—it is repeatedly tested as it changes.