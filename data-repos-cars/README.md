[![What's a Python Namespace Package, and What's It For?](https://raw.githubusercontent.com/realpython/data-repos/main/namespace_package.jpg)](https://realpython.com/python-namespace-package/)

# DataReposCars - A Cars Dataset for DataRepos

This package provides an example cars-dataset for [DataRepos](https://pypi.org/project/data-repos/).

To use DataReposCars, you should install it into your virtual environment:

```shell
(venv) $ python -m pip install data-repos-cars
```

You can then read the data as a regular DataRepos dataset:

```python
>>> from data_repos import read
>>> read.data("cars")
...
```

Learn more about DataRepos, DataReposCars, and namespace packages in [What's a Python Namespace Package, and What's It For?](https://realpython.com/python-namespace-package/)
