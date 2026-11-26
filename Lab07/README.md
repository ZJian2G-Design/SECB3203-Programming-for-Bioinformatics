# SECB3203 Lab 7 - Object-oriented programming

Student: Seah Zhang Jian, A24CS0297

## Setup
    py -3.13 -m venv .venv
    source .venv/bin/activate        # Windows: .venv\Scripts\activate
    pip install -r requirements.txt

## Run
    python -m pytest                 # all tests
    ruff check src                   # style check

## What is in this repository
- `src/models.py` : DNASequence, BiologicalSample and SampleCollection (my code)
- `src/sequence_utils.py` : given, complete (Week 5 module). Do not edit it.
- `tests/` : visible tests and my own tests (`test_lab07_models.py`)
- `AI_USE_LOG.md` : my AI prompt log (or nil return)

## Notes
All data are synthetic. `DNASequence` validates input inside `__init__` and exposes `.name` and `.sequence` as read-only `@property` attributes so an invalid or mutated sequence object can never exist. `BiologicalSample` uses composition ("has-a" `DNASequence` in `.dna`) rather than inheritance because a sample is metadata plus analysis results that owns a sequence rather than being a specialized string/sequence, and `.results` returns a defensive copy (`dict(self._results)`) so external callers cannot mutate internal sample state.