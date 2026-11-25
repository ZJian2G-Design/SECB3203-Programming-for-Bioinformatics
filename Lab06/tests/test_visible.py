from pathlib import Path

import pytest

from batch import main, mean_phred, process_directory, read_fastq
from bio_io import FastaFormatError, read_csv_records, read_fasta

DATA = Path(__file__).resolve().parents[1] / "data"      # not the working folder


def test_read_fasta_reads_every_record():
    records = list(read_fasta(DATA / "amplicons.fasta"))
    assert len(records) == 6 and records[0][0] == "ISO_001"


def test_read_fasta_reports_a_format_error(tmp_path):
    bad = tmp_path / "bad.fasta"
    bad.write_text("ACGT\n>a\nACGT\n")
    with pytest.raises(FastaFormatError):
        list(read_fasta(bad))


def test_read_csv_records_gives_text_values():
    rows = read_csv_records(DATA / "qc_records.csv")
    assert rows[0] == {"sample": "R01", "length": "850", "n_count": "0", "gc_percent": "51.2"}


def test_batch_survives_one_bad_file(tmp_path):
    summary = process_directory(DATA / "river", tmp_path / "log.csv", tmp_path / "batch.log")
    assert summary == {"processed": 2, "rejected": 1, "records": 30}


def test_fastq_and_exit_code(tmp_path):
    assert len(list(read_fastq(DATA / "reads.fastq"))) == 8
    assert mean_phred("IIII") == 40.0
    assert main([str(tmp_path / "missing")]) == 2
