import pytest

from basics import format_report, gc_percent, parse_counts
from env_check import check_environment


def test_report_has_python_platform_and_packages():
    report = check_environment()
    assert set(report) == {"python", "platform", "packages"}


def test_gc_percent_visible():
    assert gc_percent(18, 12, 10, 20) == pytest.approx(36.6667, abs=1e-3)


def test_format_report_visible():
    assert format_report("Amplicon_01", 60, 36.6667) == "Amplicon_01: 60 bases, GC 36.7%"


def test_parse_counts_visible():
    assert parse_counts("18 12 10 20") == (18, 12, 10, 20)
    with pytest.raises(ValueError):
        parse_counts("18 12 10")
