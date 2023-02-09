"""Collect and register reader functions to read any resources in data_repo
namespace
"""

# Standard library imports
from importlib import resources

# Third party imports
import pandas as pd

readers = {}


def register(func):
    """Register reader for a given data type."""
    readers[func.__name__] = func
    return func


def data(name, package=__package__):
    """Get a data file."""
    data_path = path(name, package)
    if data_path is None:
        raise FileNotFoundError(f"{name} not found in {package}")

    file_type = data_path.suffix.lstrip(".")
    return readers[file_type](data_path)


def path(name, package=__package__):
    """Find the path to a data file."""
    for resource in resources.files(package).iterdir():
        if resource.stem == name:
            return resource

    raise FileNotFoundError(f"{name} not found in {package}")


@register
def csv(data_path):
    """Read a CSV file from a path."""
    return pd.read_csv(data_path)


@register
def json(data_path):
    """Read a JSON file from a path."""
    return pd.read_json(data_path)
