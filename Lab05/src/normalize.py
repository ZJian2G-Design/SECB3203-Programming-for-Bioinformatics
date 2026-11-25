"""Week 5 extension - side-effect-free normalisation functions."""

CPM_SCALE = 1_000_000.0


def proportions(counts: list[float]) -> list[float]:
    """Return each count divided by the total; the input is not changed.

    Raises:
        ValueError: if the total is zero (a list of zeros would look like data).
    """
    # Calculate the sum of counts (sum([]) is 0, so this catches empty lists too)
    total = sum(counts)
    # Raise ValueError if total is 0 (or <= 0)
    if total <= 0:
        raise ValueError("Total count must be greater than zero")
    # Return a NEW list where each c in counts is divided by total
    return [c / total for c in counts]


def cpm(counts: list[float], library_size: float | None = None) -> list[float]:
    """Counts per million; library_size defaults to the sum of counts."""
    # If library_size is None, set total = sum(counts); otherwise use library_size
    total = sum(counts) if library_size is None else library_size
    # aise ValueError if total is zero or negative
    if total <= 0:
        raise ValueError("Library size must be greater than zero")
    # Return a NEW list of (c / total) * CPM_SCALE for each c in counts
    return [(c / total) * CPM_SCALE for c in counts]
