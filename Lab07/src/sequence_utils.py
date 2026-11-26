"""Reusable DNA sequence utilities for BioPyLearn."""

DNA_BASES = frozenset("ACGT")
COMPLEMENT = str.maketrans("ACGT", "TGCA")


def clean_sequence(raw: str) -> str:
    """Upper-case raw text and drop spaces, digits and newlines."""
    return "".join(ch for ch in raw.upper() if ch.isalpha())


def is_valid_dna(sequence: str, allow_n: bool = False) -> bool:
    """True for a non-empty string of A, C, G, T (N if allowed)."""
    allowed = DNA_BASES | {"N"} if allow_n else DNA_BASES
    return bool(sequence) and set(sequence.upper()) <= allowed


def gc_content(sequence: str) -> float:
    """Return GC percentage (0-100); ValueError if invalid."""
    if not is_valid_dna(sequence):
        raise ValueError(f"invalid DNA sequence: {sequence!r}")
    seq = sequence.upper()
    return (seq.count("G") + seq.count("C")) / len(seq) * 100


def reverse_complement(sequence: str) -> str:
    """Return the reverse complement; ValueError if invalid."""
    if not is_valid_dna(sequence):
        raise ValueError(f"invalid DNA sequence: {sequence!r}")
    return sequence.upper().translate(COMPLEMENT)[::-1]


def find_motif(sequence: str, motif: str) -> list[int]:
    """Return every 0-based start of motif (overlaps allowed)."""
    if not motif:
        raise ValueError("motif must not be empty")
    seq, mot = sequence.upper(), motif.upper()
    return [i for i in range(len(seq) - len(mot) + 1)
            if seq.startswith(mot, i)]
