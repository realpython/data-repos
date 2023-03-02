"""Tests for data_repos.read
"""

# Third party imports
import pytest

# DataRepos imports
from data_repos import read


def test_read_sample_countries_json_data():
    """Test reading the sample country JSON file"""
    assert not read.data("countries").empty


def test_read_sample_iris_csv_data():
    """Test reading the sample iris CSV file"""
    assert not read.data("iris").empty


def test_raise_exception_no_dataset():
    """Test raising exception when called data file doesn't exist"""
    with pytest.raises(FileNotFoundError):
        read.data("no_such_data_file")
