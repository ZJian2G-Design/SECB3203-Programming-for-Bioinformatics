"""Reusable DNA sequence utilities for BioPyLearn."""

DNA_BASES = frozenset("ACGT")
COMPLEMENT = str.maketrans("ACGT", "TGCA")
PERCENT_SCALE = 100.0


def clean_sequence(raw: str) -> str:
    """Upper-case raw text and drop spaces, digits and newlines."""
    # Keep only characters where ch.isalpha() is True, join them, and call .upper()
    return "".join(ch for ch in raw if ch.isalpha()).upper()


def is_valid_dna(sequence: str, allow_n: bool = False) -> bool:
    """True for a non-empty string of A, C, G, T (N if allowed)."""
    # Return False immediately if sequence is empty
    if not sequence:
        return False
    # Allow "N" in addition to DNA_BASES when allow_n is True
    allowed = DNA_BASES | {"N"} if allow_n else DNA_BASES
    # Check if every uppercase character in sequence is inside allowed
    return set(sequence.upper()) <= allowed


def gc_content(sequence: str) -> float:
    """Return GC percentage (0-100); ValueError if invalid."""
    # Raise ValueError if is_valid_dna(sequence) is False
    if not is_valid_dna(sequence):
        raise ValueError("Invalid or empty DNA sequence")
    seq = sequence.upper()
    # Count "G" and "C" in seq, divide by len(seq), and multiply by PERCENT_SCALE
    gc_count = seq.count("G") + seq.count("C")
    return (gc_count / len(seq)) * PERCENT_SCALE


def reverse_complement(sequence: str) -> str:
    """Return the reverse complement; ValueError if invalid."""
    # Check if sequence is valid DNA using your function from T1 (raise ValueError if False)
    if not is_valid_dna(sequence):
        raise ValueError("Invalid or empty DNA sequence")
    # Upper-case sequence, translate with COMPLEMENT, and reverse using [::-1]
    return sequence.upper().translate(COMPLEMENT)[::-1]


def find_motif(sequence: str, motif: str) -> list[int]:
    """Return every 0-based start of motif (overlaps allowed)."""
    # Raise ValueError if motif is empty
    if not motif:
        raise ValueError("Motif must not be empty")
    # Normalize both strings to upper-case so search is case-insensitive
    seq = sequence.upper()
    pat = motif.upper()
    # Return list of all start indices i where the slice of length len(pat) equals pat
    return [i for i in range(len(seq) - len(pat) + 1) if seq[i : i + len(pat)] == pat]
