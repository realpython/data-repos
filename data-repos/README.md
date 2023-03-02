[![What's a Python Namespace Package, and What's It For?](https://raw.githubusercontent.com/realpython/data-repos/main/namespace_package.jpg)](https://realpython.com/python-namespace-package/)

# DataRepos - A Namespace Package for Data Files

This package provides a namespace intended for data files.

It lets you read data files from a common package, but with the actual data distributed over multiple packages.

For example, if you have various data files that are very large (on the order of hundreds of megabytes or larger), then you can divide the data files into different packages, but they'll be callable from the same namespace in your Python code.

To use DataRepos, you should install it into your virtual environment:

```shell
(venv) $ python -m pip install data-repos
```

You can now import DataRepos as `data_repos`.

## Read Data Files

DataRepos provides a `read()` function that you can use to read data files. The data are returned as a [pandas](https://realpython.com/pandas-python-explore-dataset/) DataFrame:

```python
>>> from data_repos import read
>>> read.data("countries")
              country   population
0             Austria      8840521
1              Canada     37057765
2                Cuba     11338138
3  Dominican Republic     10627165
4             Germany     82905782
5              Norway      5311916
...
```

## Install Data Files

You can install other data files from PyPI with pip. Other cooperating [DataRepos](https://pypi.org/search/?q=data%2Drepos) packages can be installed and will integrate smoothly:

```shell
(venv) $ python -m pip install data-repos-cars
```

You can then read the cars dataset with the exact same syntax:

```python
>>> from data_repos import read
>>> read.data("cars")
...
```

Because DataRepos is a namespace package, it can be extended on the fly.

## Available Data Files

Two datasets are included as examples:

- **`iris`**: The classical [Iris dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set), originally [published](https://doi.org/10.1111/j.1469-1809.1936.tb02137.x) by Ronald Fisher in 1936
- **`countries`**: Countries and their population, collected by [Samayo](https://github.com/samayo/country-json)

You can read these files with `read.data("iris")` and `read.data("countries")`, respectively.

## Add Your Own Data Files

You can also add your own data files by storing them in a folder named `data_repos` that's on Python's path.

See examples of how to do this and learn more about namespace packages in [What's a Python Namespace Package, and What's It For?](https://realpython.com/python-namespace-package/)
