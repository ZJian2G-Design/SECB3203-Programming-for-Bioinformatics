import csv
from pathlib import Path

import pytest

from qc import classify_read, qc_summary, trim_low_quality


@pytest.mark.parametrize("length, n, gc, expected", [(850, 0, 51.2, "pass"), (790, 12, 49.8, "review"), (420, 0, 68.5, "reject")])
def test_classify_read_visible(length, n, gc, expected):
    assert classify_read(length, n, gc) == expected


def test_boundary_500_bases_and_10_n_are_allowed():
    assert classify_read(500, 10, 45.0) == "pass"
    assert classify_read(499, 0, 50.0) == "reject"


def test_qc_summary_visible():
    rows = [
        {"sample": "A", "length": "850", "n_count": "0", "gc_percent": "51.2"},
        {"sample": "B", "length": "420", "n_count": "0", "gc_percent": "68.5"},
    ]
    assert qc_summary(rows) == {"pass": 1, "review": 0, "reject": 1}


def test_trim_low_quality_visible():
    assert trim_low_quality([30, 32, 35, 12, 10]) == 3


def test_qc_summary_on_the_course_file():
    data_file = Path(__file__).resolve().parents[1] / "data" / "qc_records.csv"   # not the working folder
    with open(data_file, newline="") as handle:
        rows = list(csv.DictReader(handle))
    assert sum(qc_summary(rows).values()) == len(rows) == 10
