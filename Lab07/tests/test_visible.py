import pytest

from models import BiologicalSample, DNASequence, SampleCollection


def test_dnasequence_visible():
    d = DNASequence("D01", "atgc")
    assert d.sequence == "ATGC" and d.name == "D01" and len(d) == 4


def test_invalid_sequence_visible():
    with pytest.raises(ValueError):
        DNASequence("bad", "ATGN")


def test_reverse_complement_visible():
    assert DNASequence("D01", "ATGC").reverse_complement().sequence == "GCAT"


def test_sample_visible():
    s = BiologicalSample("S01", "case", DNASequence("S01", "ATGCGT"))
    s.add_result("qc", "pass")
    assert s.to_dict()["qc"] == "pass"


def test_collection_visible():
    c = SampleCollection()
    c.add(BiologicalSample("S01", "case", DNASequence("S01", "ATGC")))
    assert len(c) == 1 and c.summary() == {"case": 1}
