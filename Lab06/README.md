# SECB3203 Lab 6 - Files and exceptions: bio_io.py and batch.py

Student: Seah Zhang Jian, A24CS0297

## Setup
    py -3.11 -m venv .venv
    source .venv/bin/activate        # Windows: .venv\Scripts\activate
    pip install -r requirements.txt

## Run
    python -m pytest                 # all tests
    ruff check src                   # style check
    python src/batch.py data/river --out results/cli      # the command-line tool

## What is in this repository
- `src/bio_io.py` : FastaFormatError, read_fasta, read_csv_records, write_csv
- `src/batch.py` : process_directory, read_fastq, mean_phred, main (command-line tool)
- `tests/` : visible tests and my own tests (test_lab06_own.py)
- `data/` : raw synthetic data, read-only (amplicons.fasta, river/, qc_records.csv, reads.fastq)
- `results/` : files the tool writes (not committed)
- `AI_USE_LOG.md` : my AI prompt log (or nil return)

## Exit codes of batch.py
- **0**: All `*.fasta` files in the input directory were processed cleanly with zero rejected files (including when the directory contains no FASTA files).
- **1**: The batch completed and wrote the summary CSV and log file, but at least one `*.fasta` file was rejected (for example, an empty file, invalid FASTA format, or non-UTF-8 encoding).
- **2**: Invalid input directory — the given `IN_DIR` path does not exist or is not a folder, so an error message was printed to `stderr` and no batch run was executed.