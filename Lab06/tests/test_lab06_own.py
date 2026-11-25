"""Student-written tests for bio_io and batch using tmp_path (Lab 6 T5)."""

import pytest

from batch import FastqFormatError, main, mean_phred, process_directory, read_fastq
from bio_io import FastaFormatError, read_csv_records, read_fasta, write_csv


def test_read_fasta_empty_and_missing(tmp_path) -> None:
    """Empty FASTA yields nothing; missing file raises FileNotFoundError."""
    empty_fa = tmp_path / "empty.fasta"
    empty_fa.write_text("\n   \r\n", encoding="utf-8")
    # Empty or whitespace-only FASTA returns an empty list []
    assert list(read_fasta(empty_fa)) == []

    with pytest.raises(FileNotFoundError):
        list(read_fasta(tmp_path / "does_not_exist.fasta"))


def test_read_fasta_record_without_sequence(tmp_path) -> None:
    """A header followed by another header or EOF without sequence raises FastaFormatError."""
    bad_fa = tmp_path / "no_seq.fasta"
    bad_fa.write_text(">seq1\n>seq2\nACGT\n", encoding="utf-8")
    with pytest.raises(FastaFormatError) as exc_info:
        list(read_fasta(bad_fa))
    assert "no_seq.fasta" in str(exc_info.value)


def test_process_directory_empty_folder_and_missing_dir(tmp_path) -> None:
    """Empty folder returns zeros and exit code 0; missing folder returns exit code 2."""
    empty_dir = tmp_path / "empty_in"
    empty_dir.mkdir()
    out_csv = tmp_path / "out" / "log.csv"
    summary = process_directory(empty_dir, out_csv)
    assert summary == {"processed": 0, "rejected": 0, "records": 0}
    assert read_csv_records(out_csv) == []

    # Calling main on a non-existent directory returns exit code 2
    code = main([str(tmp_path / "missing_dir"), "--out", str(tmp_path / "cli_out")])
    assert code == 2


def test_fastq_tricky_quality_and_mean_phred(tmp_path) -> None:
    """read_fastq handles '@'/'+' inside quality strings; mean_phred computes Phred+33."""
    fq = tmp_path / "sample.fastq"
    fq.write_text("@read1 desc\r\nACGT\r\n+\r\n@+II\r\n", encoding="utf-8")
    records = list(read_fastq(fq))
    assert records == [("read1", "ACGT", "@+II")]
    assert mean_phred("IIII") == pytest.approx(40.0)
    with pytest.raises(FastqFormatError):
        bad_fq = tmp_path / "bad.fastq"
        bad_fq.write_text("@read1\nACGT\n-\nIIII\n", encoding="utf-8")
        list(read_fastq(bad_fq))
    with pytest.raises(ValueError):
        mean_phred("")