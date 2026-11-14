"""Lab 2 - biological sequences as strings (becomes sequence_utils.py in Week 5)."""

DNA_BASES = frozenset("ACGT")

def clean_sequence(raw: str) -> str:
    """Upper-case raw text and drop spaces, digits and newlines."""
    return "".join(ch.upper() for ch in raw if ch.isalpha())


def is_valid_dna(seq: str, allow_n: bool = False) -> bool:
    """True for a non-empty string of A, C, G, T (and N when allowed)."""
    if not seq:
        return False
    valid = set("ACGTN") if allow_n else set("ACGT")
    return set(seq) <= valid


def gc_content(seq: str) -> float:
    """Return GC percentage (0-100); ValueError if empty or not A/C/G/T."""
    seq_upper = seq.upper()
    if not is_valid_dna(seq_upper, allow_n=False):
        raise ValueError("Invalid DNA sequence or empty string.")
    gc_count = seq_upper.count("G") + seq_upper.count("C")
    return (gc_count / len(seq_upper)) * 100.0


def transcribe(dna: str) -> str:
    """Return the RNA copy of a DNA sequence (T becomes U)."""
    dna_upper = dna.upper()
    if not is_valid_dna(dna_upper, allow_n=False):
        raise ValueError("Invalid DNA sequence or empty string.")
    return dna_upper.replace("T", "U")

def find_motif(seq: str, motif: str) -> list[int]:
    """Return every 0-based start of motif in seq (overlaps allowed)."""
    if not motif:
        raise ValueError("Motif cannot be empty.")

    seq_upper = seq.upper()
    motif_upper = motif.upper()
    positions: list[int] = []
    start = 0

    while True:
        pos = seq_upper.find(motif_upper, start)
        if pos == -1:
            break
        positions.append(pos)
        start = pos + 1

    return positions