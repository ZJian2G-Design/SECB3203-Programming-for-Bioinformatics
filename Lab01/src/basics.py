"""Lab 1 - Python fundamentals for biological calculations."""


def gc_percent(a: int, c: int, g: int, t: int) -> float:
    """Return the GC percentage from the four base counts.

    Raises:
        ValueError: if any count is negative or the total is zero.
    """
    if a < 0 or c < 0 or g < 0 or t < 0:
        raise ValueError("Base counts cannot be negative.")

    total = a + c + g + t
    if total == 0:
        raise ValueError("Total base count cannot be zero.")

    return (g + c) / total * 100.0


def format_report(sample: str, length: int, gc: float) -> str:
    """Return a one-line report with units, e.g. 'S1: 60 bases, GC 46.7%'."""
    return f"{sample}: {length} bases, GC {gc:.1f}%"


def parse_counts(text: str) -> tuple[int, int, int, int]:
    """Parse 'A C G T' counts separated by spaces or commas.

    Raises:
        ValueError: if there are not exactly four non-negative integers.
    """
    cleaned = text.replace(",", " ")
    parts = cleaned.split()

    if len(parts) != 4:
        raise ValueError(f"Expected exactly 4 base counts, but found {len(parts)}.")

    counts = []
    for item in parts:
        try:
            val = int(item)
        except ValueError:
            raise ValueError(f"Base count '{item}' is not a valid integer.")
        if val < 0:
            raise ValueError(f"Base count cannot be negative: {val}")
        counts.append(val)

    return (counts[0], counts[1], counts[2], counts[3])