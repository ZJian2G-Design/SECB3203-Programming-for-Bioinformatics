# SECB3203 Lab 1 - Python fundamentals and a reproducible project

Student: Seah Zhang Jian, A24CS0297

## Setup
To set up the reproducible environment:

On Windows (Command Prompt):
python -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt

On Linux / macOS:
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt

## Run
To run the automated tests:
python -m pytest

To check style and formatting rules:
ruff check src

To generate the environment report:
python src/env_check.py > results/environment_report.txt

## What is in this repository
- src/: Contains implementation modules env_check.py and basics.py.
- tests/: Contains unit tests (test_visible.py and test_lab01_own.py).
- data/: Contains read-only synthetic laboratory QC data (qc_records.csv).
- results/: Contains generated output files (environment_report.txt).
- requirements.txt: Pinned top-level project dependencies.
- requirements-frozen.txt: Complete environment snapshot generated with pip freeze.
- pytest.ini: Pytest configuration pointing pythonpath to src/.
- .gitignore: Specifies directories and temporary files excluded from version control.
- AI_USE_LOG.md: Record of AI tutoring and explanations used during this lab.

## What is not committed, and why
The .venv/ and results/ directories are excluded from Git via .gitignore. The virtual environment is machine-specific and bulky, while results are generated outputs that would cause merge conflicts and bloat the version history if tracked.
