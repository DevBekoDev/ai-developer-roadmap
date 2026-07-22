# Python Functions

## What Is a Function?

A function is a reusable block of code that performs a specific task.

Functions help us avoid repeating the same code and make programs easier to read, test, and maintain.

Example:

```python
def greet() -> None:
    print("Hello!")
```

Calling the function:

```python
greet()
```

Output:

```text
Hello!
```

---

## Defining a Function

A function is created using the `def` keyword.

```python
def function_name() -> None:
    # Function body
    pass
```

The basic structure includes:

1. The `def` keyword.
2. The function name.
3. Parentheses.
4. An optional return type.
5. A colon.
6. An indented function body.

---

## Function Parameters

Parameters allow a function to receive values.

```python
def greet_user(name: str) -> None:
    print(f"Hello, {name}!")
```

Calling it:

```python
greet_user("Abubakr")
```

Output:

```text
Hello, Abubakr!
```

Here:

```text
name
```

is the parameter.

And:

```text
"Abubakr"
```

is the argument passed to the function.

---

## Multiple Parameters

A function can receive multiple values.

```python
def add(a: float, b: float) -> float:
    return a + b
```

Usage:

```python
result = add(10, 5)
print(result)
```

Output:

```text
15
```

---

## Return Values

The `return` statement sends a value back to the code that called the function.

```python
def multiply(a: int, b: int) -> int:
    result = a * b

    return result
```

Usage:

```python
answer = multiply(4, 5)
print(answer)
```

Output:

```text
20
```

A function stops executing when it reaches `return`.

---

## Functions That Return Nothing

Some functions perform an action without returning a value.

```python
def display_message(message: str) -> None:
    print(message)
```

The return type:

```python
-> None
```

means the function does not return a useful value.

---

## Default Parameters

Default parameters provide a value when an argument is not supplied.

```python
def greet(name: str = "Guest") -> str:
    return f"Hello, {name}!"
```

Usage:

```python
print(greet())
print(greet("Sara"))
```

Output:

```text
Hello, Guest!
Hello, Sara!
```

---

## Keyword Arguments

Arguments can be passed using parameter names.

```python
def create_user(name: str, age: int) -> str:
    return f"{name} is {age} years old."
```

Usage:

```python
result = create_user(
    name="Abubakr",
    age=23,
)
```

Keyword arguments make function calls easier to understand.

---

## Type Hints

Type hints describe the expected parameter and return types.

```python
def calculate_average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)
```

Here:

```text
numbers: list[float]
```

means the function expects a list of floating-point numbers.

And:

```text
-> float
```

means it should return a floating-point number.

Type hints improve readability and help editors detect possible mistakes.

They do not normally prevent Python from receiving a different type at runtime.

---

## Docstrings

A docstring explains what a function does.

```python
def clean_text(text: str) -> str:
    """Remove extra whitespace and convert text to lowercase."""
    words = text.strip().lower().split()

    return " ".join(words)
```

A docstring appears immediately under the function definition.

It helps developers understand how the function should be used.

---

## Local Variables

Variables created inside a function are local to that function.

```python
def calculate_total(price: float, quantity: int) -> float:
    total = price * quantity

    return total
```

The variable:

```text
total
```

only exists while the function is running.

Code outside the function cannot normally access it directly.

---

## Separation of Concerns

A function should ideally have one clear responsibility.

Less clear:

```python
def process_user_data() -> None:
    # Read input
    # Validate data
    # Save data
    # Send email
    # Print a report
    pass
```

Better:

```python
def read_user_data() -> dict:
    pass


def validate_user_data(data: dict) -> bool:
    pass


def save_user_data(data: dict) -> None:
    pass
```

Smaller focused functions are easier to:

- Understand
- Reuse
- Test
- Debug
- Maintain

---

## The `main()` Function

A `main()` function is commonly used as the entry point of a Python program.

```python
def main() -> None:
    text = input("Enter text: ")
    print(text)


if __name__ == "__main__":
    main()
```

The main guard:

```python
if __name__ == "__main__":
```

ensures that `main()` runs only when the file is executed directly.

It does not run when the file is imported into another module.

This makes functions easier to reuse and test.

---

## Pure Functions

A pure function:

1. Receives input.
2. Returns output.
3. Does not unexpectedly change outside data.

Example:

```python
def add(a: int, b: int) -> int:
    return a + b
```

Given the same inputs, it always returns the same output.

Pure functions are usually easier to test.

---

## Example: Text Utility Functions

```python
def clean_text(text: str) -> str:
    """Remove extra whitespace and convert text to lowercase."""
    words = text.strip().lower().split()

    return " ".join(words)


def count_words(text: str) -> int:
    """Return the number of words in the text."""
    cleaned_text = clean_text(text)

    if not cleaned_text:
        return 0

    return len(cleaned_text.split())
```

Example usage:

```python
text = "   Python    Is   Great   "

cleaned_text = clean_text(text)
word_count = count_words(text)

print(cleaned_text)
print(word_count)
```

Output:

```text
python is great
3
```

---

## Example: Data-Cleaning Function

```python
def clean_rows(
    rows: list[dict[str, str]],
) -> list[dict[str, str]]:
    """Remove rows containing missing required values."""
    cleaned_rows = []

    for row in rows:
        if (
            row["name"] != ""
            and row["age"] != ""
            and row["score"] != ""
        ):
            cleaned_rows.append(row)

    return cleaned_rows
```

This function has one responsibility:

```text
Receive rows
    ↓
Remove incomplete rows
    ↓
Return valid rows
```

---

## Why Functions Matter in AI Development

AI applications commonly use functions for:

- Loading datasets
- Cleaning text
- Validating user input
- Preparing model prompts
- Calling APIs
- Processing model responses
- Calculating evaluation metrics
- Saving results
- Generating embeddings
- Running model inference

Example structure:

```python
def load_data() -> list:
    pass


def preprocess_data(data: list) -> list:
    pass


def run_model(data: list) -> list:
    pass


def evaluate_results(results: list) -> dict:
    pass
```

Breaking an AI application into functions makes the application easier to build, test, and improve.

---

## Summary

Functions allow developers to:

- Reuse code
- Avoid duplication
- Organize program logic
- Separate responsibilities
- Accept input through parameters
- Return processed results
- Add type hints and documentation
- Test individual parts of an application
- Build larger programs from smaller components

A well-designed function should have a clear name, one primary responsibility, understandable parameters, and a predictable return value.