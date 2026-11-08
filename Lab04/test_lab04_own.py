from lookup import kmer_counts, safe_expression
from panel import Variant, sort_variants, sorted_copy


def test_sorted_copy_leaves_original_list_unchanged():
    """Verify that sorted_copy creates a new list and does not mutate the original."""
    original = ["TP53", "EGFR", "BRCA1", "BRAF"]
    original_copy = list(original)

    result = sorted_copy(original)

    assert result == ["BRAF", "BRCA1", "EGFR", "TP53"]
    assert original == original_copy
    assert result is not original


def test_sort_variants_full_chromosome_order_including_x_and_m():
    """Verify natural sorting across autosomes 1-22, chr prefix, X, Y, and M."""
    variants = [
        Variant("M", 100, "A", "G"),
        Variant("chr2", 50, "C", "T"),
        Variant("10", 20, "G", "C"),
        Variant("X", 300, "T", "A"),
        Variant("1", 500, "A", "T"),
        Variant("Y", 10, "C", "G"),
    ]

    sorted_vs = sort_variants(variants)
    chrom_order = [v.chrom for v in sorted_vs]

    assert chrom_order == ["1", "chr2", "10", "X", "Y", "M"]


def test_kmer_counts_k_larger_than_sequence_and_empty_string():
    """Verify kmer_counts handles k greater than sequence length and empty string."""
    assert kmer_counts("ACGT", 10) == {}
    assert kmer_counts("", 2) == {}


def test_safe_expression_missing_gene_and_zero_value():
    """Verify safe_expression returns None for missing keys and preserves 0.0."""
    expr_data = {"BRCA1": 12.5, "TP53": 0.0}

    assert safe_expression(expr_data, "TP53") == 0.0
    assert safe_expression(expr_data, "UNKNOWN_GENE") is None
    assert "UNKNOWN_GENE" not in expr_data  # verify dictionary was not modified