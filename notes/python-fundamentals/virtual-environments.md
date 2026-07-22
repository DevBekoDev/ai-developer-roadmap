# Python Virtual Environments

## What Is a Virtual Environment?

A virtual environment is an isolated Python environment created for one project.

It keeps that project’s Python interpreter and installed packages separate from other projects on the computer.

A virtual environment usually contains:

```text
.venv/
├── Scripts/
├── Lib/
├── Include/
└── pyvenv.cfg
```

On Windows, the Python interpreter is usually located at:

```text
.venv/Scripts/python.exe
```

---

## Why Virtual Environments Are Needed

Different Python projects may require different package versions.

For example:

```text
Project A:
pytest 8.x

Project B:
pytest 9.x
```

Without virtual environments, installing or upgrading a package for one project could affect another project.

Virtual environments prevent this conflict.

Each project can have its own:

- Python packages
- Package versions
- Development tools
- Testing libraries
- Dependencies

---

## Global Python vs Virtual Environment

### Global Python

The global Python installation is available to the whole computer.

Installing a package globally may make it available to many unrelated projects.

Example:

```powershell
pip install pytest
```

Depending on the terminal configuration, this may install pytest into the global Python environment.

### Virtual environment

A virtual environment belongs to one project.

After activation:

```powershell
python -m pip install pytest
```

installs pytest only inside that environment.

This keeps the project isolated.

---

## Creating a Virtual Environment

Navigate to the project folder:

```powershell
cd projects/python-fundamentals/day-05-modules-project-structure
```

Create the virtual environment:

```powershell
python -m venv .venv
```

The command structure is:

```text
python
    Run Python

-m venv
    Run Python’s built-in venv module

.venv
    Name of the environment folder
```

The name `.venv` is commonly used because it clearly identifies the folder as a local virtual environment.

---

## Activating a Virtual Environment on Windows PowerShell

Run:

```powershell
.\.venv\Scripts\Activate.ps1
```

After activation, the terminal usually shows:

```text
(.venv) PS C:\path\to\project>
```

The prefix:

```text
(.venv)
```

indicates that the virtual environment is active.

---

## PowerShell Execution-Policy Error

PowerShell may block the activation script and display an error similar to:

```text
running scripts is disabled on this system
```

A temporary fix for the current terminal session is:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate the environment again:

```powershell
.\.venv\Scripts\Activate.ps1
```

The option:

```text
-Scope Process
```

means the setting applies only to the current PowerShell process.

When that terminal closes, the temporary policy change ends.

---

## Activating in Command Prompt

In Windows Command Prompt, use:

```cmd
.venv\Scripts\activate.bat
```

The activation command differs because PowerShell and Command Prompt use different script formats.

---

## Activating on macOS or Linux

Use:

```bash
source .venv/bin/activate
```

The directory is named:

```text
bin/
```

instead of:

```text
Scripts/
```

---

## Verifying the Active Interpreter

After activation, run:

```powershell
python -c "import sys; print(sys.executable)"
```

A successful result should point to something similar to:

```text
...\project\.venv\Scripts\python.exe
```

The important part is:

```text
.venv\Scripts\python.exe
```

This confirms that the terminal is using the virtual-environment interpreter.

You can also run:

```powershell
where.exe python
```

The first result should normally be the environment’s Python executable.

---

## Checking the Python Version

Run:

```powershell
python --version
```

Example output:

```text
Python 3.14.6
```

This confirms which Python version is being used inside the environment.

---

## Installing Packages

After activating the environment, install a package using:

```powershell
python -m pip install pytest
```

Using:

```text
python -m pip
```

is safer than using only:

```text
pip
```

because it explicitly runs pip through the currently active Python interpreter.

This helps ensure the package is installed into the correct environment.

---

## Upgrading a Package

Use:

```powershell
python -m pip install -U pytest
```

The option:

```text
-U
```

means:

```text
upgrade
```

It installs a newer compatible version when one is available.

---

## Listing Installed Packages

Run:

```powershell
python -m pip list
```

Example:

```text
Package    Version
---------- -------
pip        26.0
pytest     9.1.1
```

This shows the packages installed inside the active environment.

---

## Checking One Package

Run:

```powershell
python -m pip show pytest
```

This displays information such as:

- Package name
- Version
- Installation location
- Dependencies

The installation location should point inside:

```text
.venv/
```

---

## Deactivating a Virtual Environment

Run:

```powershell
deactivate
```

The:

```text
(.venv)
```

prefix disappears from the terminal.

After deactivation, commands such as:

```powershell
python
```

use the normal system interpreter again.

---

## Re-Activating the Environment

A virtual environment does not remain active after closing the terminal.

Each time a new terminal is opened, activate it again:

```powershell
.\.venv\Scripts\Activate.ps1
```

Activation changes the current terminal session.

It does not permanently change Windows.

---

## Virtual Environments and VS Code

VS Code should use the same Python interpreter as the project.

To select the interpreter:

1. Press:

```text
Ctrl + Shift + P
```

2. Search for:

```text
Python: Select Interpreter
```

3. Select the interpreter inside:

```text
.venv\Scripts\python.exe
```

The selected interpreter affects:

- Running Python files
- Pylance analysis
- Test discovery
- Debugging
- Package resolution
- Jupyter notebooks

---

## Why Packages Sometimes Appear Missing

A package may be installed, but VS Code can still show:

```text
Import could not be resolved
```

This may happen when:

- The wrong interpreter is selected.
- The environment is not active.
- The package was installed globally instead of locally.
- VS Code has not refreshed.
- The source folder is not in Python’s import path.

The first checks should be:

```powershell
python -c "import sys; print(sys.executable)"
```

and:

```powershell
python -m pip show package_name
```

Both should refer to the same virtual environment.

---

## Standard-Library Modules

Some modules do not need to be installed with pip because they are included with Python.

Examples:

```python
import csv
import json
import os
import sys
from pathlib import Path
```

These belong to the Python standard library.

A project using only standard-library modules can run in a fresh virtual environment without additional package installation.

Our modular CSV-cleaning project used:

```text
csv
os
pathlib
```

Therefore, it required no third-party runtime packages.

---

## Third-Party Packages

Third-party packages are installed separately.

Examples:

```text
pytest
pandas
numpy
requests
transformers
torch
```

They are usually installed with:

```powershell
python -m pip install package_name
```

Each project should install only the packages it needs.

---

## Dependency Files

A project can document its required packages in a dependency file.

A common format is:

```text
requirements.txt
```

Example:

```text
pytest==9.1.1
requests==2.32.5
```

Install all listed packages using:

```powershell
python -m pip install -r requirements.txt
```

---

## Creating `requirements.txt`

One approach is:

```powershell
python -m pip freeze > requirements.txt
```

This records installed packages and versions.

Example:

```text
iniconfig==2.3.0
packaging==26.0
pluggy==1.6.0
pytest==9.1.1
```

However, `pip freeze` may include indirect dependencies.

For small projects, developers may also write the direct dependencies manually.

---

## Rebuilding an Environment

Virtual-environment folders should not usually be shared or committed to Git.

Instead, another developer can rebuild the environment.

Example process:

```powershell
python -m venv .venv
```

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

```powershell
.\.venv\Scripts\Activate.ps1
```

```powershell
python -m pip install -r requirements.txt
```

The environment can therefore be recreated from project documentation and dependency files.

---

## Why `.venv/` Should Not Be Committed

The `.venv/` folder may contain:

- Many files
- Platform-specific executables
- Installed package code
- Large binary files
- Machine-specific paths

Committing it would make the repository unnecessarily large and less portable.

Add this to `.gitignore`:

```gitignore
.venv/
venv/
```

This keeps the local environment out of Git.

---

## Checking Whether `.venv/` Is Ignored

Run:

```powershell
git status
```

The `.venv/` folder should not appear as an untracked or staged directory.

You can also run:

```powershell
git check-ignore -v projects/python-fundamentals/day-05-modules-project-structure/.venv
```

Git should show which `.gitignore` rule is excluding the environment.

---

## Environment Variables vs Virtual Environments

These concepts are related but different.

### Virtual environment

Isolates:

- Python interpreter
- Installed packages
- Dependency versions

### Environment variables

Store external configuration such as:

```text
API keys
database URLs
input filenames
output filenames
debug settings
```

Example:

```powershell
$env:CSV_INPUT_FILENAME="messy_students.csv"
```

A project may use both:

```text
Virtual environment
    Controls Python and packages

Environment variables
    Control application configuration
```

---

## Example Project Workflow

Navigate to the project:

```powershell
cd projects/python-fundamentals/day-05-modules-project-structure
```

Create the environment:

```powershell
python -m venv .venv
```

Allow activation for the current PowerShell session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Activate:

```powershell
.\.venv\Scripts\Activate.ps1
```

Verify:

```powershell
python -c "import sys; print(sys.executable)"
```

Set configuration:

```powershell
$env:CSV_INPUT_FILENAME="messy_students.csv"
$env:CSV_OUTPUT_FILENAME="cleaned_students.csv"
```

Run:

```powershell
python main.py
```

Deactivate when finished:

```powershell
deactivate
```

---

## Virtual Environments in AI Development

AI projects often depend on many third-party packages.

Examples include:

- PyTorch
- TensorFlow
- Transformers
- NumPy
- Pandas
- Scikit-learn
- FastAPI
- LangChain
- OpenAI SDKs
- Vector-database clients

Different projects may require different versions.

For example:

```text
Project A:
torch 2.x
transformers 5.x

Project B:
torch 1.x
transformers 4.x
```

Virtual environments allow these projects to coexist without package conflicts.

---

## Virtual Environments and Reproducibility

Reproducibility means another developer can rebuild the same working setup.

A reproducible project should document:

- Supported Python version
- Required packages
- Package versions
- Environment variables
- Setup commands
- Run commands
- Test commands

Useful files include:

```text
README.md
requirements.txt
.env.example
.gitignore
```

Together, they help another developer clone and run the project.

---

## Common Problems

### Activation is blocked

Use:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate again.

### `pytest` is not found

Check that the environment is active, then install:

```powershell
python -m pip install pytest
```

### The wrong Python interpreter is used

Run:

```powershell
python -c "import sys; print(sys.executable)"
```

Select the matching interpreter in VS Code.

### A package imports in one terminal but not another

The other terminal may not have the environment activated.

### The environment works locally but not after cloning

The `.venv/` folder is intentionally not shared.

Create a new environment and reinstall dependencies.

---

## Good Practices

- Create one virtual environment per project.
- Use `.venv` as a clear local folder name.
- Activate the environment before installing packages.
- Prefer `python -m pip` over plain `pip`.
- Verify `sys.executable` when unsure.
- Select the same interpreter in VS Code.
- Never commit `.venv/`.
- Document dependencies.
- Keep `.env` private.
- Commit `.env.example`.
- Test the project inside a clean environment.
- Delete and recreate environments when they become corrupted.

---

## Summary

A virtual environment isolates a project’s Python interpreter and packages.

The basic workflow is:

```text
Create
    ↓
Activate
    ↓
Verify interpreter
    ↓
Install dependencies
    ↓
Run and test project
    ↓
Deactivate
```

Virtual environments prevent dependency conflicts, make projects easier to reproduce, and are essential for professional Python and AI development.