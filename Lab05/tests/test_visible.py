import pytest

from normalize import cpm, proportions
from sequence_utils import (
    clean_sequence,
    find_motif,
    gc_content,
    is_valid_dna,
    reverse_complement,
)


def test_clean_and_validate_visible():
    assert clean_sequence(" atg cgt\n12") == "ATGCGT"
    assert is_valid_dna("ATGC") is True
    assert is_valid_dna("") is False


def test_gc_content_is_a_percentage_visible():
    assert gc_content("ATGC") == pytest.approx(50.0)
    with pytest.raises(ValueError):
        gc_content("")


def test_reverse_complement_visible():
    assert reverse_complement("ATGCGTACGT") == "ACGTACGCAT"


def test_find_motif_visible():
    assert find_motif("AAAA", "AA") == [0, 1, 2]


def test_proportions_leaves_the_input_alone():
    raw = [120, 80, 40]
    result = proportions(raw)
    assert sum(result) == pytest.approx(1.0)
    assert raw == [120, 80, 40]
    assert cpm([250, 750]) == pytest.approx([250_000, 750_000])
