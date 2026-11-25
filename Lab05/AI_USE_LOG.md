# AI USE LOG

<!-- SECB3203 prompt log. Policy: PROPOSED - for approval by the SECB3203 course team before circulation to students. Fill in, then run: python tools/check_ai_log.py AI_USE_LOG.md --assessment <key> -->

- Course: SECB3203
- Assessment: Lab 5
- Student name: Seah Zhang Jian
- Matric no: A24CS0297
- Group ID: n/a
- AI level: 1
- Tools cited: Google (2026). Gemini. Retrieved 18 November 2026 from https://gemini.google.com

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [/] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: 2026-11-18 22:30
- Tool: Google (2026). Gemini. Retrieved 18 November 2026 from https://gemini.google.com
- Purpose: debug
- Prompt: what happen? [screenshot of pip install -r requirements.txt failing on numpy==2.4.4 in Python 3.10]
- Output: Explained that numpy==2.4.4 requires Python >=3.11 and guided recreating the virtual environment using `py -3.11 -m venv .venv` before running `pip install -r requirements.txt`.
- Verified by: Recreated `.venv` with Python 3.11, installed `requirements.txt`, and confirmed `pytest` and `ruff` ran cleanly.
- My change: Recreated my local `.venv` using Python 3.11 without modifying `requirements.txt`.
- Used in: Local development environment setup (`.venv`)

## Entry 2

- Date: 2026-11-18 22:45
- Tool: Google (2026). Gemini. Retrieved 18 November 2026 from https://gemini.google.com
- Purpose: hint
- Prompt: Please guide me through completing SECB3203 Lab 5 as well here are the documents i attached
- Output: Provided step-by-step hints and structural fill-in-the-blank guidance for `clean_sequence`, `is_valid_dna`, `gc_content`, `reverse_complement`, and `find_motif`, reminding me to check empty strings before set subset comparisons and reuse `is_valid_dna` and `COMPLEMENT`.
- Verified by: Ran `python -m pytest` (all visible tests passed) and `ruff check src` (0 issues).
- My change: Wrote and completed the logic myself in `src/sequence_utils.py`, adding named constant `PERCENT_SCALE = 100.0` to avoid magic numbers.
- Used in: `src/sequence_utils.py` (`clean_sequence`, `is_valid_dna`, `gc_content`, `reverse_complement`, `find_motif`)

## Entry 3

- Date: 2026-11-18 22:55
- Tool: Google (2026). Gemini. Retrieved 18 November 2026 from https://gemini.google.com
- Purpose: tests-plan
- Prompt: NEXT [after submitting src/normalize.py implementation]
- Output: Reviewed `src/normalize.py` (`proportions` and `cpm`) and provided a fill-in-the-blank test plan structure for `tests/test_lab05_own.py` covering list immutability, zero/negative `ValueError` cases, and sequence edge cases.
- Verified by: Ran `python -m pytest` (all 9 tests passed) and `ruff check src tests` (0 issues).
- My change: Completed the test assertions in `tests/test_lab05_own.py` and verified both modules pass all checks.
- Used in: `src/normalize.py` and `tests/test_lab05_own.py`