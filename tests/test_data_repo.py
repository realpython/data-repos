# Third party imports
import pytest

# DataRepo imports
from data_repo import read


def test_read_sample_countries_csv_data():
    assert not read.data("countries").empty


def test_read_sample_cars_json_data():
    assert not read.data("cars").empty


def test_raise_exception_no_dataset():
    with pytest.raises(FileNotFoundError):
        read.data("no_data")
