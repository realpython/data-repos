"""Tests for data_repo.read
"""

# Third party imports
import pytest

# DataRepo imports
from data_repo import read


def test_read_sample_countries_csv_data():
    """Test reading the sample country CSV file"""
    assert not read.data("countries").empty


def test_read_sample_cars_json_data():
    """Test reading the sample cars JSON file"""
    assert not read.data("cars").empty


def test_raise_exception_no_dataset():
    """Test raising exception when called data file doesn't exist"""
    with pytest.raises(FileNotFoundError):
        read.data("no_data")
