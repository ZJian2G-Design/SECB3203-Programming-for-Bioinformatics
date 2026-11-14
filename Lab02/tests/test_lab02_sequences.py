import pytest
from lab02_sequences import find_motif


def test_find_motif_overlapping_matches():
    """Normal test: detects overlapping motif positions correctly."""
    assert find_motif("AAAA", "AA") == [0, 1, 2]


def test_find_motif_case_insensitive_and_no_match():
    """Boundary test: handles case insensitivity and returns empty list when absent."""
    assert find_motif("atgcgt", "CGT") == [3]
    assert find_motif("ATGC", "AAA") == []


def test_find_motif_empty_motif_raises():
    """Invalid input test: raises ValueError when motif is an empty string."""
    with pytest.raises(ValueError):
        find_motif("ATGC", "")