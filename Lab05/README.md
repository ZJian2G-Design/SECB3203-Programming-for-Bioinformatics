# SECB3203 Lab 5 - Functions and modules: sequence_utils.py and normalize.py

Student: Seah Zhang Jian, A24CS0297

## Setup
    py -3.11 -m venv .venv
    source .venv/bin/activate        # Windows: .venv\Scripts\activate
    pip install -r requirements.txt

## Run
    python -m pytest                 # all tests
    ruff check src                   # style check

## What is in this repository
- `src/sequence_utils.py` : clean_sequence, is_valid_dna, gc_content, reverse_complement, find_motif
- `src/normalize.py` : proportions, cpm (never change the caller's data)
- `tests/` : visible tests and my own tests (test_lab05_own.py)
- `AI_USE_LOG.md` : my AI prompt log (or nil return)

## Design decisions
`proportions()` raises `ValueError` when the total is zero (or the list is empty) because dividing by zero would crash with `ZeroDivisionError`, while silently returning a list of zeros would falsely look like valid normalized expression data instead of alerting the caller to an empty or unsequenced sample. In `src/normalize.py`, the list comprehension `return [c / total for c in counts]` allocates and returns a brand-new list rather than mutating elements in place (`counts[i] = ...`), guaranteeing that the caller's original list remains completely unchanged.