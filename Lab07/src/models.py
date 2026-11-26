"""Week 7 - classes for biological sequences and samples."""
from sequence_utils import find_motif, gc_content, is_valid_dna, reverse_complement


class DNASequence:
    """A validated, read-only DNA sequence with a name."""

    def __init__(self, name: str, sequence: str):
        if not isinstance(sequence, str) or not is_valid_dna(sequence):
            raise ValueError(f"invalid DNA sequence for {name!r}")
        self._name = name
        self._sequence = sequence.upper()

    @classmethod
    def from_fasta_record(cls, record_id: str, sequence: str) -> "DNASequence":
        """Build an object from a (record_id, sequence) pair such as read_fasta yields."""
        return cls(record_id, sequence)

    @property
    def name(self) -> str:
        return self._name

    @property
    def sequence(self) -> str:
        return self._sequence

    def gc_content(self) -> float:
        return gc_content(self._sequence)

    def reverse_complement(self) -> "DNASequence":
        return type(self)(f"{self._name}_rc", reverse_complement(self._sequence))

    def find_motif(self, motif: str) -> list[int]:
        return find_motif(self._sequence, motif)

    def __len__(self) -> int:
        return len(self._sequence)

    def __repr__(self) -> str:
        return f"DNASequence(name={self._name!r}, sequence={self._sequence!r})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, DNASequence):
            return NotImplemented
        return (self._name, self._sequence) == (other._name, other._sequence)

    def __hash__(self) -> int:
        return hash((self._name, self._sequence))


class BiologicalSample:
    """Sample metadata plus a validated sequence and analysis results (composition)."""

    def __init__(self, sample_id: str, group: str, dna: DNASequence):
        if not isinstance(dna, DNASequence):
            raise TypeError("dna must be a DNASequence instance")
        self.sample_id = sample_id
        self.group = group
        self.dna = dna
        self._results: dict = {}

    def add_result(self, name: str, value) -> None:
        self._results[name] = value

    @property
    def results(self) -> dict:
        """A copy, so callers cannot change the stored results by accident."""
        return dict(self._results)

    def to_dict(self) -> dict:
        data = {
            "sample_id": self.sample_id,
            "group": self.group,
            "length": len(self.dna),
            "gc_percent": round(self.dna.gc_content(), 2),
        }
        data.update(self._results)
        return data


class SampleCollection:
    """An ordered collection of samples with unique ids."""

    def __init__(self):
        self._samples: list[BiologicalSample] = []
        self._ids: set[str] = set()

    def add(self, sample: BiologicalSample) -> None:
        if sample.sample_id in self._ids:
            raise ValueError(f"duplicate sample_id: {sample.sample_id!r}")
        self._samples.append(sample)
        self._ids.add(sample.sample_id)

    def __len__(self) -> int:
        return len(self._samples)

    def __iter__(self):
        return iter(self._samples)

    def by_group(self, group: str) -> list[BiologicalSample]:
        return [sample for sample in self._samples if sample.group == group]

    def summary(self) -> dict[str, int]:
        """Number of samples per group, sorted by group name."""
        counts: dict[str, int] = {}
        for sample in self._samples:
            counts[sample.group] = counts.get(sample.group, 0) + 1
        return {group: counts[group] for group in sorted(counts)}