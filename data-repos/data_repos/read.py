"""Collect and register reader functions to read any resources in data_repos
namespace
"""

# Standard library imports
import importlib
import pathlib
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
    file_type = data_path.suffix.lstrip(".")
    return readers[file_type](data_path)


def path(name, package=__package__):
    """Find the path to a data file."""
    for resource in _files_iterdir(package):
        if resource.stem == name:
            return resource

    raise FileNotFoundError(f"{name} not found in {package}")


def _files_iterdir(package):
    """Use resources.files on Python 3.10 and above to yield resources.
    On previous versions, iterate over the __path__ attribute of the namespace"""
    try:
        yield from resources.files(package).iterdir()
    except (AttributeError, TypeError):  # pragma: no cover
        for path in importlib.import_module(package).__path__:
            yield from pathlib.Path(path).iterdir()


@register
def csv(data_path):
    """Read a CSV file from a path."""
    return pd.read_csv(data_path)


@register
def json(data_path):
    """Read a JSON file from a path."""
    return pd.read_json(data_path)
