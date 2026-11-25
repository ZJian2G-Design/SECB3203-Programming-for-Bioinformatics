"""Student-written tests for sequence_utils and normalize (Lab 5 T5)."""

import pytest

from normalize import cpm, proportions
from sequence_utils import (
    clean_sequence,
    find_motif,
    gc_content,
    is_valid_dna,
    reverse_complement,
)


def test_proportions_input_unchanged() -> None:
    """proportions returns a new list and never mutates the caller's list."""
    raw = [120, 80, 40]
    result = proportions(raw)
    assert result == pytest.approx([0.5, 1 / 3, 1 / 6])
    # 1. Verify raw is still [120, 80, 40] and result is not the same object
    assert raw == [120, 80, 40]
    assert result is not raw


def test_normalize_zero_and_negative_errors() -> None:
    """proportions and cpm raise ValueError on zero/empty total or negative library_size."""
    with pytest.raises(ValueError):
        proportions([0, 0, 0])
    with pytest.raises(ValueError):
        proportions([])
    with pytest.raises(ValueError):
        cpm([10, 20], library_size=-50)


def test_clean_and_validate_edge_cases() -> None:
    """clean_sequence strips noise; is_valid_dna rejects empty string and controls N."""
    assert clean_sequence("  acg12\t\r\nT ") == "ACGT"
    assert is_valid_dna("") is False
    assert is_valid_dna("ACNGT", allow_n=False) is False
    assert is_valid_dna("ACNGT", allow_n=True) is True


def test_gc_revcomp_and_overlapping_motif() -> None:
    """gc_content, reverse_complement, and find_motif handle case, overlaps, and errors."""
    assert gc_content("ggcc") == pytest.approx(100.0)
    assert reverse_complement("aAaC") == "GTTT"
    assert find_motif("aaaaa", "AA") == [0, 1, 2, 3]
    assert find_motif("ACGT", "ACGTACGT") == []
    with pytest.raises(ValueError):
        find_motif("ACGT", "")