from pathlib import Path

from lookup import CODON_TABLE, count_bases, kmer_counts, safe_expression, shared_genes, translate
from panel import Variant, filter_panel, sort_variants, sorted_copy

DATA = Path(__file__).resolve().parents[1] / "data"


def test_variant_is_a_named_tuple():
    v = Variant("17", 43071077, "A", "G")
    assert v.pos == 43071077 and v[3] == "G"


def test_filter_panel_and_sorted_copy_visible():
    assert filter_panel(["BRCA1", "TP53", "CFTR"], {"CFTR", "BRCA1"}) == ["BRCA1", "CFTR"]
    original = ["TP53", "BRCA1"]
    assert sorted_copy(original) == ["BRCA1", "TP53"]
    assert original == ["TP53", "BRCA1"]


def test_sort_variants_puts_chromosome_2_before_10():
    vs = [Variant("10", 5, "A", "G"), Variant("2", 9, "C", "T"), Variant("X", 1, "G", "A")]
    assert [v.chrom for v in sort_variants(vs)] == ["2", "10", "X"]


def test_lookup_basics_visible():
    assert len(CODON_TABLE) == 64 and CODON_TABLE["ATG"] == "M"
    assert count_bases("aacgt") == {"A": 2, "C": 1, "G": 1, "T": 1}
    assert kmer_counts("ATATA", 2) == {"AT": 2, "TA": 2}
    assert safe_expression({"BRCA1": 8.2}, "MYC") is None
    assert translate("ATGGCTTAA") == "MA*"


def test_shared_genes_from_the_course_files():
    panel = set((DATA / "panel_genes.txt").read_text().split())
    detected = set((DATA / "detected_genes.txt").read_text().split())   # the file repeats BRCA1
    assert shared_genes(panel, detected) == {"BRCA1", "TP53"}
