"""Week 6 - reading FASTA and CSV safely."""
import csv
from collections.abc import Iterator
from pathlib import Path


class FastaFormatError(ValueError):
    """Raised when a FASTA file does not follow the format."""


def _finish(record_id: str, chunks: list[str], path) -> tuple[str, str]:
    # If chunks is empty (a header with no sequence lines), raise FastaFormatError naming path
    if not chunks:
        raise FastaFormatError(f"{path}: record '{record_id}' has no sequence")
    # Return (record_id, joined upper-case sequence)
    return record_id, "".join(chunks).upper()


def read_fasta(path) -> Iterator[tuple[str, str]]:
    """Yield (record_id, sequence) for every record in a FASTA file.

    The id is the first word of the header. Wrapped lines are joined and the
    sequence is upper-cased. Records are produced one at a time, so large
    files do not have to fit in memory.

    Raises:
        FileNotFoundError: if the file does not exist.
        FastaFormatError: for data before the first header, an empty header
            or a record without sequence.
    """
    record_id: str | None = None
    chunks: list[str] = []

    # Open path with encoding="utf-8"
    with Path(path).open(encoding="utf-8") as handle:
        for raw_line in handle:
            line = raw_line.strip()
            # Skip blank lines
            if not line:
                continue
            if line.startswith(">"):
                if record_id is not None:
                    yield _finish(record_id, chunks, path)
                header_text = line[1:].strip()
                # If header_text is empty ('>' alone), raise FastaFormatError naming path
                if not header_text:
                    raise FastaFormatError(f"{path}: empty header")
                # Extract the first word of header_text (split on whitespace, index 0)
                record_id = header_text.split()[0]
                chunks = []
            else:
                # If record_id is None, sequence data appeared before the first '>' header
                if record_id is None:
                    raise FastaFormatError(f"{path}: sequence data before first header")
                chunks.append(line)

    # Yield the final record if one was started
    if record_id is not None:
        yield _finish(record_id, chunks, path)


def read_csv_records(path) -> list[dict[str, str]]:
    """Read a CSV file into a list of dictionaries (all values are strings)."""
    # Open with encoding="utf-8" and newline="" and return list(csv.DictReader(handle))
    with Path(path).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(rows: list[dict], path, fieldnames: list[str]) -> None:
    """Write rows to a CSV file, creating the parent folder if needed."""
    out_path = Path(path)
    # Create parent directories if they do not exist
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8", newline="") as handle:
        # Create a csv.DictWriter with fieldnames=fieldnames, writeheader(), and writerows(rows)
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)