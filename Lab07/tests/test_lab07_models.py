"""Student-written tests for BiologicalSample, SampleCollection, and DNASequence (Lab 7 T5)."""
import pytest

from models import BiologicalSample, DNASequence, SampleCollection


def test_sample_composition_results_copy_and_to_dict() -> None:
    """BiologicalSample copies .results safely, isolates samples, and formats to_dict()."""
    seq = DNASequence.from_fasta_record("ISO_01", "atgcgt")
    s1 = BiologicalSample("S01", "treatment", seq)
    s2 = BiologicalSample("S02", "control", DNASequence("ISO_02", "GGCC"))

    s1.add_result("qc", "pass")
    leaked = s1.results
    leaked["qc"] = "tampered"

    assert s1.results == {"qc": "pass"}
    assert s2.results == {}
    assert s1.to_dict() == {
        "sample_id": "S01",
        "group": "treatment",
        "length": 6,
        "gc_percent": 50.0,
        "qc": "pass",
    }


def test_collection_empty_and_repeated_iteration_boundary() -> None:
    """SampleCollection handles empty state, preserves insertion order, and re-iterates cleanly."""
    col = SampleCollection()
    assert len(col) == 0
    assert col.summary() == {}
    assert col.by_group("case") == []

    s_b = BiologicalSample("S02", "z_group", DNASequence("D2", "ATGC"))
    s_a = BiologicalSample("S01", "a_group", DNASequence("D1", "GGCC"))
    col.add(s_b)
    col.add(s_a)

    assert [s.sample_id for s in col] == ["S02", "S01"]
    assert [s.sample_id for s in col] == ["S02", "S01"]
    assert list(col.summary().keys()) == ["a_group", "z_group"]


def test_invalid_inputs_and_read_only_errors() -> None:
    """Invalid dna types, duplicate sample IDs, and read-only mutations raise expected errors."""
    seq = DNASequence("D01", "atgc")
    assert seq == DNASequence("D01", "ATGC")
    assert seq != "ATGC"
    assert len({seq, DNASequence("D01", "ATGC")}) == 1

    with pytest.raises(AttributeError):
        seq.sequence = "GGGG"  # type: ignore[misc]

    with pytest.raises(TypeError):
        BiologicalSample("S01", "case", "ATGC")  # type: ignore[arg-type]

    col = SampleCollection()
    col.add(BiologicalSample("S01", "case", seq))
    with pytest.raises(ValueError):
        col.add(BiologicalSample("S01", "control", seq))