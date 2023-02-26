# DataRepos

This package provides a namespace intended for data files.

It lets you have a common package to read data files, but with the ability to distribute the namespace over multiple packages.

For example, if you have various data files that are very large (on the order of hundreds of megabytes or larger), then you can divide the data files into different packages, but they'll be callable from the same namespace in your Python code.

That means you could install the data packages that you need from PyPI:

```shell
$ python -m pip install data-repos-cars data-repos-countries
```

Once they're installed, you can just import `read` from `data_repos`, and all your datasets will be available if there's a reader registed for the data type:

```python
>>> from data_repos import read
>>> read.data("cars")
...
>>> read.data("countries")
...
```
