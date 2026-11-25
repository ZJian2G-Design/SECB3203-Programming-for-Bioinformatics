"""Week 6 extension - batch processing, logging, FASTQ and a command-line tool."""
import argparse
import logging
import sys
from collections.abc import Iterator
from pathlib import Path

from bio_io import FastaFormatError, read_fasta, write_csv

LOG = logging.getLogger("batch")
CSV_FIELDS = ["file", "records", "status", "reason"]
FASTQ_LINES_PER_RECORD = 4


class FastqFormatError(ValueError):
    """Raised when a FASTQ file is malformed."""


def process_directory(in_dir, out_csv, log_path=None) -> dict[str, int]:
    """Read every *.fasta file in in_dir; one bad file never stops the batch.

    Writes one row per file (file, records, status, reason) to out_csv and
    returns {'processed': ..., 'rejected': ..., 'records': ...}.
    """
    handler: logging.FileHandler | None = None
    if log_path is not None:
        log_file = Path(log_path)
        log_file.parent.mkdir(parents=True, exist_ok=True)
        # Create a FileHandler with mode="w" and utf-8 encoding, set formatter with %(levelname)s
        handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
        handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
        LOG.setLevel(logging.INFO)
        LOG.addHandler(handler)

    rows: list[dict[str, str | int]] = []
    processed = 0
    rejected = 0
    total_records = 0

    try:
        # Iterate over sorted *.fasta files directly inside Path(in_dir)
        fasta_files = sorted(p for p in Path(in_dir).glob("*.fasta") if p.is_file())
        for fasta_path in fasta_files:
            try:
                # Consume read_fasta(fasta_path) into a list of records
                records = list(read_fasta(fasta_path))
                if not records:
                    raise FastaFormatError("empty file")
            except (OSError, UnicodeDecodeError, FastaFormatError) as exc:
                # Catch OSError, UnicodeDecodeError, and FastaFormatError per file
                reason = "empty file" if str(exc) == "empty file" else str(exc)
                rejected += 1
                rows.append(
                    {
                        "file": fasta_path.name,
                        "records": 0,
                        "status": "rejected",
                        "reason": reason,
                    }
                )
                if handler is not None:
                    LOG.warning("%s: %s", fasta_path.name, reason)
            else:
                count = len(records)
                processed += 1
                total_records += count
                rows.append(
                    {
                        "file": fasta_path.name,
                        "records": count,
                        "status": "processed",
                        "reason": "ok",
                    }
                )
                if handler is not None:
                    LOG.info("%s: %d records", fasta_path.name, count)
    finally:
        # Always remove and close the handler so it never leaks into later runs
        if handler is not None:
            LOG.removeHandler(handler)
            handler.close()

    # Write rows to out_csv using write_csv and CSV_FIELDS
    write_csv(rows, out_csv, CSV_FIELDS)
    return {"processed": processed, "rejected": rejected, "records": total_records}


def read_fastq(path) -> Iterator[tuple[str, str, str]]:
    """Yield (read_id, sequence, quality) for each 4-line FASTQ record."""
    with Path(path).open(encoding="utf-8") as handle:
        # Strip line endings and ignore blank lines between records
        lines = [line.strip() for line in handle if line.strip()]

    for i in range(0, len(lines), FASTQ_LINES_PER_RECORD):
        chunk = lines[i : i + FASTQ_LINES_PER_RECORD]
        # Truncated record if fewer than 4 lines remain
        if len(chunk) < FASTQ_LINES_PER_RECORD:
            raise FastqFormatError(f"{path}: truncated FASTQ record")
        header, seq, plus, qual = chunk
        # Validate header starts with '@', 3rd line starts with '+', and len(seq) == len(qual)
        if not header.startswith("@"):
            raise FastqFormatError(f"{path}: header must start with '@'")
        header_text = header[1:].strip()
        if not header_text:
            raise FastqFormatError(f"{path}: empty FASTQ read id")
        if not plus.startswith("+"):
            raise FastqFormatError(f"{path}: separator line must start with '+'")
        if len(seq) != len(qual):
            raise FastqFormatError(f"{path}: sequence and quality lengths differ")
        yield header_text.split()[0], seq.upper(), qual


def mean_phred(quality: str, offset: int = 33) -> float:
    """Mean Phred score of a quality string (Phred+33 by default)."""
    # Raise ValueError if quality string is empty
    if not quality:
        raise ValueError("Quality string must not be empty")
    return sum(ord(ch) - offset for ch in quality) / len(quality)


def main(argv: list[str] | None = None) -> int:
    """Command-line entry point. Exit code 0 = all good, 1 = some files rejected, 2 = bad input."""
    parser = argparse.ArgumentParser(description="Batch-process FASTA files.")
    parser.add_argument("in_dir", help="Input directory containing *.fasta files")
    parser.add_argument("--out", default="results", help="Output directory (default: results)")
    args = parser.parse_args(argv)

    in_path = Path(args.in_dir)
    # If in_path is not a directory, print error to sys.stderr and return exit code 2
    if not in_path.is_dir():
        print(f"Error: {in_path} is not a valid directory", file=sys.stderr)
        return 2

    out_dir = Path(args.out)
    summary = process_directory(
        in_path,
        out_dir / "processing_log.csv",
        log_path=out_dir / "batch.log",
    )
    print(
        f"processed={summary['processed']} "
        f"rejected={summary['rejected']} "
        f"records={summary['records']}"
    )
    # Return 1 if any file was rejected, otherwise 0
    return 1 if summary["rejected"] > 0 else 0


if __name__ == "__main__":
    sys.exit(main())