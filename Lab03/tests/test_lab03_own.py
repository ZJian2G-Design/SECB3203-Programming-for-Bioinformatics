from qc import classify_read, trim_low_quality


def test_classify_read_boundary_gc_exact_limits():
    """Boundary test: GC content at exactly 30.0% and 70.0% must pass."""
    assert classify_read(600, 5, 30.0) == "pass"
    assert classify_read(600, 5, 70.0) == "pass"
    assert classify_read(600, 5, 29.9) == "review"
    assert classify_read(600, 5, 70.1) == "review"


def test_classify_read_boundary_n_count():
    """Boundary test: 10 N bases passes, but 11 N bases triggers review."""
    assert classify_read(550, 10, 50.0) == "pass"
    assert classify_read(550, 11, 50.0) == "review"


def test_trim_low_quality_empty_and_all_low():
    """Trim test: empty list and list with all low scores both return 0."""
    assert trim_low_quality([]) == 0
    assert trim_low_quality([10, 15, 18, 5]) == 0
    assert trim_low_quality([30, 20]) == 2  # threshold 20 is kept