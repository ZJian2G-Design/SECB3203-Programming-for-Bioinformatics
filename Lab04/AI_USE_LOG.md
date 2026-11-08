# AI USE LOG

<!-- SECB3203 prompt log. Policy: PROPOSED - for approval by the SECB3203 course team before circulation to students. Fill in, then run: python tools/check_ai_log.py AI_USE_LOG.md --assessment <key> -->

- Course: SECB3203
- Assessment: Lab 4
- Student name: Seah Zhang Jian
- Matric no: A24CS0297
- Group ID: <group work only, else n/a>
- AI level: 1
- Tools cited: Google (2026). Gemini. Retrieved 8 November 2026 from https://gemini.google.com

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [x] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: 8 November 2026
- Tool: Google (2026). Gemini. Retrieved 8 November 2026 from https://gemini.google.com 

- Purpose: explain, hint, tests-plan

- Prompt: Please guide me through completing SECB3203 Lab 4, including the function implementations in panel.py and lookup.py, unit tests, and style checks.

- Output: Explained list mutability vs sorted(), tuple sort keys for chromosome natural order, itertools.product codon table generation, safe dict lookups, and test boundaries.

- Verified by: Ran python -m pytest and ruff check src. All 9 test fixtures and boundary assertions passed with zero linting issues.

- My change: Wrote the implementation of filter_panel, sort_variants, and translate, applied removeprefix for FURB188, and authored test_lab04_own.py.

- Used in: src/panel.py, src/lookup.py, and tests/test_lab04_own.py

<!-- Copy the whole 'Entry' block for each extra interaction: ## Entry 2, ## Entry 3 ... -->
