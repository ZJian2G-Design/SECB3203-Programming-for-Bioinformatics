# AI USE LOG

<!-- SECB3203 prompt log. Policy: PROPOSED - for approval by the SECB3203 course team before circulation to students. Fill in, then run: python tools/check_ai_log.py AI_USE_LOG.md --assessment <key> -->

- Course: SECB3203
- Assessment: Lab 6
- Student name: Seah Zhang Jian
- Matric no: A24CS0297
- Group ID: n/a
- AI level: 1
- Tools cited: Google (2026). Gemini. Retrieved 18 November 2026 from https://gemini.google.com

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [/] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: 2026-11-18 23:25
- Tool: Google (2026). Gemini. Retrieved 18 November 2026 from https://gemini.google.com
- Purpose: hint
- Prompt: here you are [attached starter src/bio_io.py and src/batch.py]
- Output: Provided structural fill-in-the-blank templates and explanations for `read_fasta` (streaming generator yielding `(record_id, sequence)` and raising `FastaFormatError` naming the file), `read_csv_records`, and `write_csv` with `newline=""` and parent directory creation.
- Verified by: Ran `python -m pytest` and `ruff check src` after completing `src/bio_io.py`.
- My change: Filled in all blanks and completed the FASTA and CSV I/O logic in `src/bio_io.py`.
- Used in: `src/bio_io.py` (`_finish`, `read_fasta`, `read_csv_records`, `write_csv`)

## Entry 2

- Date: 2026-11-18 23:32
- Tool: Google (2026). Gemini. Retrieved 18 November 2026 from https://gemini.google.com
- Purpose: hint
- Prompt: [continued from src/bio_io.py completion to implement src/batch.py]
- Output: Guided the per-file `try/except` structure inside `process_directory` with `logging.FileHandler(..., mode="w")` removed in a `finally` block, 4-line FASTQ validation in `read_fastq`, `mean_phred`, and exit code handling (`0`, `1`, `2`) in `main`.
- Verified by: Ran `python -m pytest` (5 passed), `ruff check src` (0 issues), and executed `python src/batch.py data/river --out results/cli` (`processed=2 rejected=1 records=30`).
- My change: Completed `src/batch.py` and verified both the test suite and CLI output files (`results/cli/processing_log.csv` and `results/cli/batch.log`).
- Used in: `src/batch.py` (`process_directory`, `read_fastq`, `mean_phred`, `main`)

## Entry 3

- Date: 2026-11-18 23:38
- Tool: Google (2026). Gemini. Retrieved 18 November 2026 from https://gemini.google.com
- Purpose: tests-plan
- Prompt: pass [screenshot showing 5 passed, ruff check src passed, and CLI run output]
- Output: Provided a fill-in-the-blank test plan for `tests/test_lab06_own.py` using pytest's `tmp_path` fixture to cover empty/missing FASTA files, missing sequence errors, empty/missing batch directories, and tricky FASTQ quality lines.
- Verified by: Ran `python -m pytest` (all 9 tests passed) and `ruff check src`.
- My change: Completed all assertions in `tests/test_lab06_own.py`.
- Used in: `tests/test_lab06_own.py`