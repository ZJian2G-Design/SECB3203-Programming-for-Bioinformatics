# SECB3203 Lab 4 - Biological collections: lists, tuples, dictionaries and sets

Student: Seah Zhang Jian, A24CS0297

## Setup
    python -m venv .venv
    source .venv/bin/activate        # Windows: .venv\Scripts\activate
    pip install -r requirements.txt

## Run
    python -m pytest                 # all tests
    ruff check src                   # style check

## What is in this repository
- `src/panel.py` : Variant, filter_panel, sorted_copy, sort_variants (lists and tuples)
- `src/lookup.py` : CODON_TABLE, count_bases, kmer_counts, shared_genes, safe_expression, translate (dicts and sets)
- `tests/` : visible tests and my own tests (test_lab04_own.py)
- `data/` : synthetic gene lists and variants (read-only)
- `AI_USE_LOG.md` : my AI prompt log (or nil return)
