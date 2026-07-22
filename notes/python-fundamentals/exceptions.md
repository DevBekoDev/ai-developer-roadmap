# Python Exceptions and Error Handling

## What Is an Exception?

An exception is an error that happens while a Python program is running.

When Python encounters a problem that it cannot handle automatically, it raises an exception.

Example:

```python
number = 10 / 0
```

This produces:

```text
ZeroDivisionError: division by zero
```

The program stops because division by zero is not valid.

---

## Syntax Errors vs Exceptions

A syntax error means the Python code is written incorrectly.

Example:

```python
if age > 18
    print("Adult")
```

The missing colon causes:

```text
SyntaxError
```

An exception happens when the code is syntactically valid but fails during execution.

Example:

```python
numbers = []

average = sum(numbers) / len(numbers)
```

This code is valid Python, but it raises:

```text
ZeroDivisionError
```

because:

```python
len(numbers)
```

returns:

```text
0
```

---

## Common Python Exceptions

### `ValueError`

Raised when a value has the correct type but an invalid format or meaning.

```python
age = int("twenty")
```

This raises:

```text
ValueError
```

because `"twenty"` cannot be converted into an integer.

---

### `TypeError`

Raised when an operation receives an incompatible type.

```python
result = "10" + 5
```

This raises:

```text
TypeError
```

because Python cannot directly add a string and an integer.

---

### `ZeroDivisionError`

Raised when dividing by zero.

```python
result = 10 / 0
```

---

### `FileNotFoundError`

Raised when trying to open a file that does not exist.

```python
with open("missing_file.txt", "r") as file:
    content = file.read()
```

---

### `KeyError`

Raised when accessing a dictionary key that does not exist.

```python
user = {
    "name": "Sara",
}

print(user["email"])
```

---

### `IndexError`

Raised when accessing a list position that does not exist.

```python
numbers = [10, 20, 30]

print(numbers[5])
```

---

### `AttributeError`

Raised when an object does not have the requested attribute or method.

```python
name = "Python"

name.append("AI")
```

Strings do not have an `append()` method.

---

### `ModuleNotFoundError`

Raised when Python cannot find an imported module.

```python
import unknown_module
```

---

## Using `try` and `except`

The `try` block contains code that may fail.

The `except` block handles the error.

```python
try:
    age = int(input("Enter your age: "))

except ValueError:
    print("Please enter a valid number.")
```

If the conversion works, the `except` block is skipped.

If the user enters invalid text, Python raises `ValueError`, and the program handles it without crashing.

---

## Catching Specific Exceptions

It is better to catch the exact exception you expect.

Good:

```python
try:
    number = int("invalid")

except ValueError:
    print("The value could not be converted.")
```

Less clear:

```python
try:
    number = int("invalid")

except:
    print("Something went wrong.")
```

A bare `except` catches almost every error, which can hide unexpected problems.

Specific exception handling makes debugging easier.

---

## Handling Multiple Exceptions

A program may need to handle different possible errors.

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("You must enter a valid integer.")

except ZeroDivisionError:
    print("The number cannot be zero.")
```

Each exception receives its own response.

---

## Catching Multiple Exception Types Together

Several exceptions can be handled using one block.

```python
try:
    value = int(input("Enter a value: "))
    result = 100 / value

except (ValueError, ZeroDivisionError):
    print("The input must be a valid non-zero integer.")
```

This is useful when different exceptions should produce the same response.

---

## Accessing the Exception Message

The exception object can be stored in a variable.

```python
try:
    number = int("invalid")

except ValueError as error:
    print(f"Conversion failed: {error}")
```

The variable:

```text
error
```

contains information about what went wrong.

---

## The `else` Block

The `else` block runs only when no exception occurs.

```python
try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid number.")

else:
    print(f"You entered: {number}")
```

Execution flow:

```text
try succeeds
    ↓
else runs

try fails
    ↓
except runs
```

---

## The `finally` Block

The `finally` block runs whether an exception occurs or not.

```python
try:
    file = open("data.txt", "r", encoding="utf-8")
    content = file.read()

except FileNotFoundError:
    print("The file was not found.")

finally:
    print("File operation finished.")
```

The `finally` block is often used for cleanup work.

Examples include:

- Closing files
- Closing database connections
- Releasing system resources
- Ending network connections
- Logging that an operation finished

---

## Complete `try` Structure

A complete exception-handling structure can contain:

```python
try:
    # Code that may fail

except SomeException:
    # Handle the error

else:
    # Run when no exception occurs

finally:
    # Always run
```

Example:

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("Invalid integer.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print(f"Result: {result}")

finally:
    print("Calculation finished.")
```

---

## File Handling Example

```python
from pathlib import Path


file_path = Path("data/users.csv")

try:
    with file_path.open(
        "r",
        encoding="utf-8",
    ) as file:
        content = file.read()

except FileNotFoundError:
    print("The requested file does not exist.")

else:
    print("File loaded successfully.")
    print(content)
```

The program handles a missing file instead of crashing unexpectedly.

---

## Why Use `with` for Files?

This:

```python
with file_path.open("r", encoding="utf-8") as file:
    content = file.read()
```

automatically closes the file after the block finishes.

It closes the file even if an exception occurs while reading.

That makes `with` safer than manually opening and closing files.

---

## Raising Exceptions

Developers can raise exceptions intentionally using:

```python
raise
```

Example:

```python
def calculate_average(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("Numbers cannot be empty.")

    return sum(numbers) / len(numbers)
```

Usage:

```python
average = calculate_average([])
```

This raises:

```text
ValueError: Numbers cannot be empty.
```

The function rejects input that it cannot process correctly.

---

## Why Raise an Exception?

Raising an exception is useful when:

- Required data is missing.
- A parameter contains an invalid value.
- An operation cannot continue safely.
- Configuration is incomplete.
- A file has an invalid format.
- Application rules are violated.

Example:

```python
def set_temperature(value: float) -> None:
    if value < 0:
        raise ValueError("Temperature cannot be negative.")
```

---

## Validating Function Inputs

```python
def calculate_discount(
    price: float,
    discount: float,
) -> float:
    if price < 0:
        raise ValueError("Price cannot be negative.")

    if discount < 0 or discount > 100:
        raise ValueError(
            "Discount must be between 0 and 100."
        )

    return price - (price * discount / 100)
```

This prevents invalid data from producing incorrect results.

---

## Re-Raising Exceptions

Sometimes a function performs some work when an error happens, then raises the same exception again.

```python
try:
    number = int("invalid")

except ValueError:
    print("Logging conversion failure.")
    raise
```

The `raise` statement without a new exception re-raises the current one.

This is useful when a program needs to:

- Log an error
- Add context
- Clean up resources
- Let another layer handle the final response

---

## Exception Handling Across Application Layers

In a structured application, lower-level functions often perform operations while the entry point handles user-facing errors.

Example service:

```python
def load_csv(file_path):
    with file_path.open(
        "r",
        newline="",
        encoding="utf-8",
    ) as file:
        return file.read()
```

The service does not catch `FileNotFoundError`.

The entry point handles it:

```python
def main() -> None:
    try:
        content = load_csv(input_file)

    except FileNotFoundError:
        print("Error: Input file was not found.")
        return

    print(content)
```

Responsibility:

```text
Service
    Attempts the operation

main.py
    Decides what the user sees
```

This keeps application layers focused.

---

## Avoid Silencing Errors

This is usually bad:

```python
try:
    result = important_operation()

except Exception:
    pass
```

The program silently ignores every error.

That can make bugs very difficult to find.

A better approach is:

```python
try:
    result = important_operation()

except ValueError as error:
    print(f"Invalid data: {error}")
```

Only handle errors that the program can respond to meaningfully.

---

## Catching `Exception`

Sometimes a high-level application boundary may catch:

```python
except Exception as error:
```

Example:

```python
try:
    run_application()

except Exception as error:
    print(f"Unexpected error: {error}")
```

However, this should be used carefully.

Catching `Exception` too early can hide programming mistakes.

Prefer specific exception types whenever possible.

---

## Reading a Python Traceback

A traceback shows the sequence of function calls that led to an exception.

Example:

```text
Traceback (most recent call last):
  File "traceback_practice.py", line 15, in <module>
    main()
  File "traceback_practice.py", line 9, in main
    average = calculate_average(scores)
  File "traceback_practice.py", line 4, in calculate_average
    return total / len(numbers)
ZeroDivisionError: division by zero
```

A good way to read it is:

1. Start near the bottom.
2. Identify the exception type.
3. Read the exception message.
4. Find the failing line.
5. Trace upward to understand how execution reached that line.

In this example:

```text
Exception:
ZeroDivisionError

Message:
division by zero

Failing line:
return total / len(numbers)
```

---

## Exceptions vs Assertions

An exception handles runtime problems or invalid conditions.

```python
if age < 0:
    raise ValueError("Age cannot be negative.")
```

An assertion checks an assumption, often during development or testing.

```python
assert age >= 0
```

Use exceptions for conditions that application users or external data may cause.

Use assertions mainly for tests and internal developer assumptions.

Do not depend on assertions for essential production input validation because Python can run with assertions disabled.

---

## Testing Exceptions with Pytest

Pytest can verify that a function raises the expected exception.

Example function:

```python
def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("b cannot be zero.")

    return a / b
```

Test:

```python
import pytest


def test_divide_raises_error_for_zero() -> None:
    with pytest.raises(ValueError):
        divide(10, 0)
```

This test passes only when `ValueError` is raised.

You can also check the message:

```python
def test_divide_error_message() -> None:
    with pytest.raises(
        ValueError,
        match="b cannot be zero",
    ):
        divide(10, 0)
```

---

## Exceptions in AI Applications

AI applications may need to handle:

- Missing API keys
- Failed API requests
- Network timeouts
- Invalid model responses
- Missing datasets
- Unsupported file formats
- Invalid JSON
- Empty prompts
- Token-limit errors
- Database connection failures
- Model-loading failures
- Incorrect configuration

Example:

```python
def validate_prompt(prompt: str) -> None:
    if not prompt.strip():
        raise ValueError("Prompt cannot be empty.")
```

Another example:

```python
import os


api_key = os.environ.get("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError(
        "OPENAI_API_KEY is not configured."
    )
```

Good exception handling helps AI applications fail clearly instead of behaving unpredictably.

---

## Good Exception-Handling Practices

- Catch specific exceptions.
- Use clear error messages.
- Do not hide unexpected errors.
- Validate input early.
- Raise meaningful exceptions.
- Keep the `try` block focused.
- Avoid placing too much unrelated code inside one `try`.
- Use `with` for files and other managed resources.
- Handle errors at the correct application layer.
- Use tracebacks to find the real source of a failure.
- Test important error cases.

---

## Summary

Exceptions represent errors that occur while a Python program is running.

Important concepts include:

- Syntax errors happen before execution.
- Exceptions happen during execution.
- `try` contains risky code.
- `except` handles expected failures.
- `else` runs when no error occurs.
- `finally` always runs.
- `raise` creates an exception intentionally.
- Specific exception types make programs clearer.
- Tracebacks show how execution reached an error.
- Exceptions are essential for reliable file, data, API, and AI applications.

Good exception handling does not simply prevent crashes. It makes failures understandable, controlled, and easier to debug.