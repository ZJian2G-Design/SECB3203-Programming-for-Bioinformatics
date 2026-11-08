"""Lab 4 - lists and tuples for a gene panel and variant records."""
from typing import NamedTuple


class Variant(NamedTuple):
    """One variant coordinate: an immutable record with named fields."""

    chrom: str
    pos: int
    ref: str
    alt: str


def filter_panel(genes: list[str], priority: set[str]) -> list[str]:
    """Keep the genes that are in priority, preserving the original order."""
    return [gene for gene in genes if gene in priority]


def sorted_copy(items: list) -> list:
    """Return a sorted copy; the original list is not changed."""
    return sorted(items)


def _chrom_key(chrom: str) -> tuple:
    """Return a sort key tuple so 1-22 come first in numeric order, then X, Y, M."""
    c = chrom.upper()
    c = c.removeprefix("CHR")

    # Map non-autosome chromosomes to rank values after 1-22
    special = {"X": 23, "Y": 24, "M": 25, "MT": 25}
    if c.isdigit():
        return (0, int(c))
    return (1, special.get(c, 99), c)


def sort_variants(variants: list[Variant]) -> list[Variant]:
    """Sort by chromosome (1-22, X, Y, M) and then by position."""
    return sorted(variants, key=lambda v: (_chrom_key(v.chrom), v.pos))