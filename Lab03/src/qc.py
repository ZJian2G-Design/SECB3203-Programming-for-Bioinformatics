"""Lab 3 - sequence quality control with conditions and loops."""


def classify_read(
    length: int,
    n_count: int,
    gc: float,
    *,
    min_len: int = 500,
    max_n: int = 10,
    gc_range: tuple[float, float] = (30.0, 70.0),
) -> str:
    """Return 'reject', 'review' or 'pass' for one sequencing record.

    Rules are checked in this order: too short -> reject; too many N or GC
    outside the inclusive range -> review; otherwise pass.
    """
    # Rule 1: Length below min_len gives 'reject'
    if length < min_len:
        return "reject"

    # Rule 2: More than max_n N bases or GC outside inclusive range gives 'review'
    low_gc, high_gc = gc_range
    if n_count > max_n or gc < low_gc or gc > high_gc:
        return "review"

    # Rule 3: Passes all quality checks
    return "pass"


def qc_summary(records: list[dict]) -> dict[str, int]:
    """Count records per decision. Values may be numbers or CSV strings."""
    counts = {"pass": 0, "review": 0, "reject": 0}
    for row in records:
        # Cast values because CSV DictReader returns strings
        length = int(row["length"])
        n_count = int(row["n_count"])
        gc = float(row["gc_percent"])
        decision = classify_read(length, n_count, gc)
        counts[decision] += 1
    return counts


def trim_low_quality(quals: list[int], threshold: int = 20) -> int:
    """Return how many bases to keep after trimming a low-quality 3' tail."""
    end = len(quals)
    # Guard loop: check end > 0 first to avoid IndexError on empty or all-low lists
    while end > 0 and quals[end - 1] < threshold:
        end -= 1
    return end