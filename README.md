# AI Developer Roadmap

A hands-on 90-day roadmap documenting my journey toward becoming an AI Developer.

This repository contains my learning notes, coding exercises, mini-projects, and progressively more advanced AI development work.

## Progress

| Day | Topic | Status |
|---|---|---|
| Day 1 | Python Foundations | ✅ Completed |
| Day 2 | Functions and Clean Code | ✅ Completed |
| Day 3 | Object-Oriented Python | ✅ Completed |
| Day 4 | Files, JSON, CSV, and Data Cleaning | ✅ Completed |
| Day 5 | Modules and Project Structure | ⏳ Next |

---

## Repository Structure

```text
ai-developer-roadmap/
│
├── python-fundamentals/
│   ├── day-01-python-foundations/
│   ├── day-02-functions-clean-code/
│   ├── day-03-object-oriented-python/
│   └── day-04-files-json-csv/
│
├── exercises/
│   └── python-fundamentals/
│       ├── day-01-python-foundations/
│       ├── day-02-functions-clean-code/
│       └── day-03-object-oriented-python/
│
├── projects/
│   ├── python-fundamentals/
│   │   ├── day-03-object-oriented-python/
│   │   └── day-04-files-json-csv/
│   │
│   └── llm/
│
├── data/
├── machine-learning/
├── notes/
├── .gitignore
└── README.md
```

The repository is organized by **topic**, while individual learning days keep their original day numbering.

- `python-fundamentals/` — learning material and examples
- `exercises/` — coding challenges completed independently
- `projects/` — larger practical programs and mini-projects
- `data/` — datasets and generated data files
- `machine-learning/` — machine-learning work
- `notes/` — additional study notes

---

# Completed Days

## Day 1 — Python Foundations ✅

Covered core Python concepts and strengthened fundamental programming skills.

Topics included:

- Variables
- Data types
- Strings
- Lists
- Dictionaries
- Sets
- Tuples
- Conditions
- Loops
- Basic Python problem solving

Exercises were completed independently and pushed to GitHub.

---

## Day 2 — Functions and Clean Code ✅

Focused on writing reusable and maintainable Python code.

Topics included:

- Creating functions
- Function parameters
- Return values
- Default parameters
- Type hints
- Docstrings
- Input validation
- String processing
- Clean-code practices

Exercises included practical AI-related utilities such as:

- Model accuracy calculations
- Training-time estimation
- Dataset storage estimation
- AI API cost estimation
- Input and email validation

---

## Day 3 — Object-Oriented Python ✅

Learned how to structure larger Python applications using object-oriented programming.

Topics included:

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

Exercises included:

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

The project demonstrates both:

```text
Inheritance → AdminUser IS A User

Composition → ChatSession HAS Users, AIModel, and ChatMessages
```

---

## Day 4 — Files, JSON, CSV, and Data Cleaning ✅

Learned how Python applications interact with files and structured data.

Topics included:

- `pathlib`
- File and folder paths
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

The script:

1. Reads a CSV dataset.
2. Handles missing input files.
3. Detects incomplete rows.
4. Removes rows containing missing values.
5. Converts numeric CSV values.
6. Calculates dataset statistics.
7. Calculates average age and score.
8. Finds minimum and maximum scores.
9. Saves the cleaned dataset to a new CSV file.

Example:

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

Output:

```text
data/cleaned_students.csv
```

---

# Next — Day 5

## Modules and Project Structure

Day 5 will focus on turning Python scripts into professionally structured Python projects.

Topics will include:

- Python imports
- Modules
- Packages
- `__init__.py`
- Separating application responsibilities
- Models
- Services
- Utilities
- Configuration
- Environment variables
- `.env`
- `.env.example`
- Virtual environments

The Day 4 CSV cleaner will also be reorganized into a more professional multi-file Python application.

---

# Goal

The long-term goal of this roadmap is to develop the skills required to build production-ready AI applications and qualify for:

- AI Developer roles
- AI Engineer roles
- LLM application development
- AI automation projects
- Machine-learning projects
- API-based AI applications
- Freelance AI development work

The roadmap focuses heavily on **building**, not just watching tutorials.

Every section includes practical coding and project work that is committed to GitHub as progress is made.
