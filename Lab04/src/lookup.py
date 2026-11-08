"""Lab 4 - dictionaries and sets for biological lookup."""
import itertools
from collections import Counter

_BASES = "TCAG"
_AMINO = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"

# Generate all 64 codons with itertools.product and pair them with _AMINO
CODON_TABLE: dict[str, str] = dict(
    zip(
        ("".join(c) for c in itertools.product(_BASES, repeat=3)),
        _AMINO,
    )
)


def count_bases(seq: str) -> dict[str, int]:
    """Count each character in seq (upper-cased), sorted by key."""
    if not seq:
        return {}
    counts = Counter(seq.upper())
    return dict(sorted(counts.items()))


def kmer_counts(seq: str, k: int) -> dict[str, int]:
    """Count overlapping k-mers, sorted by key. ValueError if k < 1."""
    if k < 1:
        raise ValueError("k must be at least 1")

    s = seq.upper()
    if k > len(s):
        return {}

    kmers = [s[i : i + k] for i in range(len(s) - k + 1)]
    return dict(sorted(Counter(kmers).items()))

def shared_genes(panel: set[str], detected: set[str]) -> set[str]:
    """Genes that are both on the panel and detected."""
    return set(panel) & set(detected)


def safe_expression(expression: dict[str, float], gene: str) -> float | None:
    """Return the expression value, or None when the gene is missing."""
    return expression.get(gene)


def translate(dna: str) -> str:
    """Translate DNA to a protein string ('*' marks a stop codon).

    Raises:
        ValueError: if the length is not a multiple of 3 or a codon is invalid.
    """
    s = dna.upper()
    if not s:
        return ""

    if len(s) % 3 != 0:
        raise ValueError("Sequence length must be a multiple of 3")

    protein = []
    for i in range(0, len(s), 3):
        codon = s[i : i + 3]
        if codon not in CODON_TABLE:
            raise ValueError(f"Invalid codon: {codon}")
        protein.append(CODON_TABLE[codon])

    return "".join(protein)
