import pytest
from basics import gc_percent, parse_counts


def test_gc_percent_boundary_all_gc():
    """Boundary test: 100% GC when only G and C bases exist."""
    assert gc_percent(0, 25, 25, 0) == 100.0


def test_gc_percent_zero_total_raises():
    """Zero total test: raises ValueError when all counts are 0."""
    with pytest.raises(ValueError):
        gc_percent(0, 0, 0, 0)


def test_parse_counts_negative_value_raises():
    """Invalid input test: raises ValueError on negative base counts."""
    with pytest.raises(ValueError):
        parse_counts("10 -5 20 15")