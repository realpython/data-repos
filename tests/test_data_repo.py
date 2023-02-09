# DataRepo imports
from data_repo import read


def test_read_sample_greetings_data():
    assert not read.data("greetings").empty


def test_read_sample_cars_data():
    assert not read.data("cars").empty
