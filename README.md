# AI Developer Roadmap

A hands-on 90-day roadmap documenting my progress toward becoming an AI Developer.

This repository contains structured learning material, independent coding exercises, practical mini-projects, automated tests, debugging practice, technical notes, and progressively more advanced AI development work.

The main focus is learning by building:

```text
Learn
  ↓
Practice
  ↓
Build
  ↓
Test
  ↓
Document
  ↓
Commit to GitHub
```

---

## Progress

| Day | Topic | Status |
|---|---|---|
| Day 1 | Python Foundations | ✅ Completed |
| Day 2 | Functions and Clean Code | ✅ Completed |
| Day 3 | Object-Oriented Python | ✅ Completed |
| Day 4 | Files, JSON, CSV, and Data Cleaning | ✅ Completed |
| Day 5 | Modules and Project Structure | ✅ Completed |
| Day 6 | Testing and Debugging | ✅ Completed |
| Day 7 | Review and Documentation | 🚧 In Progress |

---

## Repository Structure

```text
ai-developer-roadmap/
│
├── python-fundamentals/
│   ├── day-01-python-foundations/
│   ├── day-02-functions-clean-code/
│   ├── day-03-object-oriented-python/
│   ├── day-04-files-json-csv/
│   ├── day-05-modules-project-structure/
│   ├── day-06-testing-debugging/
│   └── README.md
│
├── exercises/
│   └── python-fundamentals/
│       ├── day-01-python-foundations/
│       ├── day-02-functions-clean-code/
│       ├── day-03-object-oriented-python/
│       ├── day-04-files-json-csv/
│       ├── day-06-testing-debugging/
│       └── day-07-review-documentation/
│
├── projects/
│   ├── python-fundamentals/
│   │   ├── day-03-object-oriented-python/
│   │   ├── day-04-files-json-csv/
│   │   └── day-05-modules-project-structure/
│   │
│   └── llm/
│
├── data/
├── machine-learning/
├── notes/
├── .gitignore
└── README.md
```

---

## Repository Organization

The repository separates learning material, exercises, and projects.

### `python-fundamentals/`

Contains lessons, demonstrations, and small examples used to learn new Python concepts.

### `exercises/`

Contains coding challenges completed independently to practice syntax, problem-solving, and implementation.

### `projects/`

Contains larger practical applications that combine several concepts from the roadmap.

### `data/`

Contains datasets and generated data files used by projects.

### `machine-learning/`

Reserved for future machine-learning lessons, experiments, and projects.

### `notes/`

Contains technical explanations and study summaries.

---

## Naming Conventions

Day folders use lowercase kebab-case:

```text
day-XX-topic-name/
```

Examples:

```text
day-01-python-foundations/
day-05-modules-project-structure/
day-06-testing-debugging/
```

Python files use descriptive snake_case names:

```text
text_utilities.py
csv_cleaner.py
cleaning_stats.py
test_csv_cleaner.py
```

Generated folders and local environments are excluded through `.gitignore`, including:

```text
__pycache__/
.pytest_cache/
.venv/
.env
```

---

# Completed Work

## Day 1 — Python Foundations

Day 1 covered the core concepts required to write basic Python programs.

### Topics

- Variables
- Integers and floating-point numbers
- Strings
- Booleans
- Lists
- Tuples
- Sets
- Dictionaries
- Conditions
- `for` loops
- `while` loops
- Basic problem-solving
- Type conversion
- User input
- Formatted strings

### Outcome

Created foundational Python programs and completed independent exercises using core data types, conditions, and loops.

---

## Day 2 — Functions and Clean Code

Day 2 focused on writing reusable, readable, and maintainable Python code.

### Topics

- Defining functions
- Function parameters
- Return values
- Default parameters
- Type hints
- Docstrings
- Input validation
- String processing
- JSON utilities
- Clean-code principles
- The `main()` function
- The `if __name__ == "__main__"` guard

### Utilities Built

- Text cleaner
- Word counter
- JSON utilities
- Validation utilities
- Email validation
- Model accuracy calculator
- Training-time estimator
- Dataset storage estimator
- AI API cost estimator

### Example

```python
def clean_text(text: str) -> str:
    """Remove extra whitespace and convert text to lowercase."""
    words: list[str] = text.strip().lower().split()

    return " ".join(words)
```

The text utility can transform:

```text
"   Hello     WORLD   "
```

into:

```text
"hello world"
```

---

## Day 3 — Object-Oriented Python

Day 3 introduced object-oriented programming and how classes can be used to organize larger applications.

### Topics

- Classes and objects
- Constructors
- Instance attributes
- Instance methods
- Class attributes
- Class methods
- Static methods
- Inheritance
- `super()`
- Method overriding
- Composition

### Exercises

Created classes representing:

- `User`
- `Document`
- `ChatMessage`
- `AIModel`

### Day 3 Project

Built an object-oriented AI chat data program containing:

```text
User
 ↑
AdminUser

AIModel

ChatMessage

ChatSession
```

The project demonstrates inheritance:

```text
AdminUser IS A User
```

It also demonstrates composition:

```text
ChatSession HAS Users
ChatSession HAS an AIModel
ChatSession HAS ChatMessages
```

This project helped connect individual class concepts to a larger application structure.

---

## Day 4 — Files, JSON, CSV, and Data Cleaning

Day 4 focused on interacting with files and structured data.

### Topics

- `pathlib`
- Files and directory paths
- Reading text files
- Writing text files
- File modes
- UTF-8 encoding
- JSON reading and writing
- `json.load()`
- `json.dump()`
- CSV reading and writing
- `csv.DictReader`
- `csv.DictWriter`
- Exception handling
- `try`
- `except`
- `else`
- `finally`

### Day 4 Project

Built a reusable CSV data-cleaning script.

The application:

1. Finds and opens a CSV dataset.
2. Handles missing input files.
3. Reads rows with `csv.DictReader`.
4. Detects incomplete rows.
5. Removes rows containing missing values.
6. Converts numeric string values into integers.
7. Calculates dataset statistics.
8. Calculates average age and score.
9. Finds the highest and lowest scores.
10. Saves the cleaned data using `csv.DictWriter`.

### Example Dataset Result

```text
Original rows: 8
Cleaned rows: 5
Removed rows: 3

Dataset Statistics
Average age: 25.00
Average score: 88.20
Highest score: 95
Lowest score: 81
```

The cleaned dataset is saved as:

```text
cleaned_students.csv
```

---

## Day 5 — Modules and Project Structure

Day 5 focused on turning a single Python script into a professionally structured multi-file application.

### Topics

- Python imports
- Modules
- Packages
- `__init__.py`
- Models
- Services
- Utilities
- Separation of concerns
- Environment variables
- External configuration
- `.env.example`
- Virtual environments
- Clean project execution

### Day 5 Project

The Day 4 CSV cleaner was refactored into the following structure:

```text
day-05-modules-project-structure/
│
├── models/
│   ├── __init__.py
│   └── cleaning_stats.py
│
├── services/
│   ├── __init__.py
│   └── csv_cleaner.py
│
├── utils/
│   ├── __init__.py
│   └── file_utils.py
│
├── .env.example
├── config.py
└── main.py
```

### Responsibilities

```text
models/
    Represents application data

services/
    Contains the main application logic

utils/
    Contains small reusable helper functions

config.py
    Reads configuration from environment variables

main.py
    Coordinates the application
```

### CSV Service Functions

The service layer contains functions for:

```text
load_csv()
clean_rows()
calculate_statistics()
save_csv()
```

### Statistics Model

The `CleaningStats` model represents:

```text
average_age
average_score
highest_score
lowest_score
```

Instead of passing four separate values around the application, the statistics are returned as one structured object.

### Environment Variables

The input and output filenames were moved outside the source code.

Required variables:

```env
CSV_INPUT_FILENAME=messy_students.csv
CSV_OUTPUT_FILENAME=cleaned_students.csv
```

These values are documented in:

```text
.env.example
```

The application was also successfully executed inside a clean Python virtual environment.

---

## Day 6 — Testing and Debugging

Day 6 focused on automated testing, assertions, tracebacks, and debugging tools.

### Topics

- Installing `pytest`
- Running automated tests
- Pytest test discovery
- Test file naming
- Test function naming
- Python `assert`
- Passing tests
- Failing tests
- Reading pytest failure reports
- Testing text-cleaning functions
- Testing data-cleaning functions
- `pytest.approx()`
- Floating-point comparisons
- Reading Python tracebacks
- Identifying exception types
- Finding failing line numbers
- VS Code breakpoints
- Inspecting variables
- Step Into
- Step Over
- Debugging function calls

### Automated Tests

Tests were written for:

1. Addition utility
2. Cleaning and normalizing text
3. Counting words
4. Removing rows with missing values
5. Keeping complete rows
6. Calculating CSV statistics
7. Handling empty row input

### Test Result

```text
7 passed
0 failed
```

The original roadmap target was ten tests. The Day 6 learning work was completed with an intentionally adjusted target of seven passing tests.

### Example Test

```python
def test_clean_rows_returns_empty_list_for_empty_input() -> None:
    rows = []

    result = clean_rows(rows)

    assert result == []
```

### Floating-Point Testing

`pytest.approx()` was used when testing decimal calculations:

```python
assert stats.average_score == pytest.approx(83.33333333333333)
```

This avoids failures caused by tiny floating-point precision differences.

---

## Day 7 — Review and Documentation

Day 7 focuses on reviewing and improving all Week 1 work.

### Current Tasks

- Rebuild previous exercises
- Review the repository structure
- Fix inconsistent folder and file names
- Remove generated cache folders
- Improve `.gitignore`
- Improve the root repository README
- Write notes about functions
- Write notes about classes
- Write notes about exceptions
- Write notes about virtual environments
- Write notes about testing
- Commit and push all Week 1 improvements

### Completed Day 7 Work

- Rebuilt the text utilities exercise.
- Reviewed repository folder and file names.
- Removed generated `__pycache__` folders.
- Added Python and pytest cache rules to `.gitignore`.
- Renamed inconsistent exercise files.
- Improved the repository documentation.

---

# Running the Modular CSV Project

Navigate to the Day 5 project:

```powershell
cd projects/python-fundamentals/day-05-modules-project-structure
```

## Create a Virtual Environment

```powershell
python -m venv .venv
```

If PowerShell blocks activation scripts, temporarily allow them for the current terminal session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Activate the environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

After activation, the terminal should begin with:

```text
(.venv)
```

## Set the Required Environment Variables

```powershell
$env:CSV_INPUT_FILENAME="messy_students.csv"
$env:CSV_OUTPUT_FILENAME="cleaned_students.csv"
```

## Run the Project

```powershell
python main.py
```

Expected summary:

```text
CSV file loaded successfully.
Total rows: 8

Original rows: 8
Cleaned rows: 5
Removed rows: 3

Dataset Statistics
Average age: 25.00
Average score: 88.20
Highest score: 95
Lowest score: 81
```

---

# Running the Automated Tests

Activate the virtual environment, then install pytest:

```powershell
python -m pip install -U pytest
```

From the repository root, run all tests:

```powershell
pytest
```

Run only the text utility tests:

```powershell
pytest exercises/python-fundamentals/day-06-testing-debugging/test_text_utilities.py
```

Run only the CSV-cleaner tests:

```powershell
pytest exercises/python-fundamentals/day-06-testing-debugging/test_csv_cleaner.py
```

Run the original pytest learning example:

```powershell
pytest python-fundamentals/day-06-testing-debugging/test_math_utils.py
```

Expected complete result:

```text
7 passed
```

---

# Main Projects

## Object-Oriented AI Chat Data Program

Location:

```text
projects/python-fundamentals/day-03-object-oriented-python/
```

Demonstrates:

- Classes and objects
- Inheritance
- Composition
- User roles
- AI model representation
- Chat message representation
- Chat session management

---

## Reusable CSV Data Cleaner

Location:

```text
projects/python-fundamentals/day-04-files-json-csv/
```

Demonstrates:

- File handling
- CSV reading
- CSV writing
- Missing-value removal
- Numeric conversion
- Dataset statistics
- Exception handling

---

## Modular CSV Data Cleaner

Location:

```text
projects/python-fundamentals/day-05-modules-project-structure/
```

Demonstrates:

- Modules
- Packages
- Models
- Services
- Utilities
- Configuration
- Environment variables
- Virtual environments
- Separation of concerns
- Automated testing compatibility

---

# Skills Practiced

The repository currently demonstrates experience with:

- Python fundamentals
- Variables and data types
- Conditions and loops
- Functions
- Parameters and return values
- Type hints
- Docstrings
- Input validation
- String processing
- Clean-code practices
- Object-oriented programming
- Classes and objects
- Inheritance
- Composition
- File handling
- JSON processing
- CSV processing
- Data cleaning
- Exception handling
- Modules and packages
- `__init__.py`
- Project architecture
- Models and services
- Environment variables
- Virtual environments
- Automated testing with pytest
- Assertions
- Floating-point testing
- Traceback analysis
- VS Code debugging
- Git and GitHub
- Repository organization
- Technical documentation

---

# Week 1 Outcome

By the end of Week 1, the repository contains:

- Structured Python learning material
- Independent programming exercises
- Object-oriented programming exercises
- An object-oriented chat data project
- A reusable CSV-cleaning project
- A modular multi-file version of the CSV cleaner
- Environment-based configuration
- A clean virtual-environment workflow
- Seven passing automated tests
- Debugging and traceback practice
- Consistent repository naming
- Improved Git ignore rules
- Technical project documentation

---

# Long-Term Goal

The goal of this roadmap is to develop the practical skills required to build production-ready AI applications and qualify for work involving:

- AI development
- AI engineering
- LLM application development
- AI automation
- Machine learning
- API-based AI applications
- Backend development for AI systems
- Data-processing applications
- Freelance AI development
- Professional software-development roles

The roadmap focuses on practical implementation instead of passive tutorial consumption.

Every stage includes a combination of learning, coding, testing, debugging, documentation, and GitHub progress.