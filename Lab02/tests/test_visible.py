import pytest

from lab02_sequences import clean_sequence, find_motif, gc_content, is_valid_dna, transcribe


def test_clean_sequence_visible():
    assert clean_sequence(" atg cgt\n") == "ATGCGT"


def test_is_valid_dna_visible():
    assert is_valid_dna("ATGC") is True
    assert is_valid_dna("") is False


def test_gc_content_visible():
    assert gc_content("ATGC") == pytest.approx(50.0)


def test_transcribe_visible():
    assert transcribe("ATG") == "AUG"


def test_find_motif_visible():
    assert find_motif("ATGCGTACGT", "CGT") == [3, 7]
