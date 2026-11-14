# SECB3203 Lab 3 - Loops and algorithms for sequence quality control

Student: Seah Zhang Jian, A24CS0297

## Setup
    python -m venv .venv
    source .venv/bin/activate        # Windows: .venv\Scripts\activate
    pip install -r requirements.txt

## Run
    python -m pytest                 # all tests
    ruff check src                   # style check

## What is in this repository
- `design/qc_design.md` : my pseudocode, flowchart and hand-trace table (written BEFORE the code)
- `src/qc.py` : classify_read, qc_summary, trim_low_quality
- `tests/` : visible tests and my own tests (test_lab03_own.py)
- `data/qc_records.csv` : synthetic QC records (read-only)
- `AI_USE_LOG.md` : my AI prompt log (or nil return)
