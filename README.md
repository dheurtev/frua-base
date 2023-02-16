<!-- These are examples of badges you might want to add to your README:
     please update the URLs accordingly

[![Built Status](https://api.cirrus-ci.com/github/<USER>/base.svg?branch=main)](https://cirrus-ci.com/github/<USER>/base)
[![ReadTheDocs](https://readthedocs.org/projects/base/badge/?version=latest)](https://base.readthedocs.io/en/stable/)
[![Coveralls](https://img.shields.io/coveralls/github/<USER>/base/main.svg)](https://coveralls.io/r/<USER>/base)
[![PyPI-Server](https://img.shields.io/pypi/v/base.svg)](https://pypi.org/project/base/)
[![Conda-Forge](https://img.shields.io/conda/vn/conda-forge/base.svg)](https://anaconda.org/conda-forge/base)
[![Monthly Downloads](https://pepy.tech/badge/base/month)](https://pepy.tech/project/base)
[![Twitter](https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter)](https://twitter.com/base)
-->

[![Project generated with PyScaffold](https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold)](https://pyscaffold.org/)

# frua-base

> frua-base is a personal Python library made by the author to follow DRY practices.

My goal is to provide a development framework based on the Python standard library.

My aim is to be generic and tested.

**frua-base shall not pull dependencies other than the standard library (except for packaging and documentation) and a pre-approved list of MIT, BSD, Apache 2.0 based dependencies. It should not reimplement the standard library.**

This library is free to use and reuse (MIT Licensed).

## Structure

The base package is *frua.base*:

It contains:
- *frua.base.archive* : Tools for archiving (zip, tar)
- *frua.base.cmd*: Tools for command line execution
- *frua.base.code*: Tools for code deployment (git repository cloning)
- *frua.base.const*: Some useful constants 
- *frua.base.data* : Tools for data manipulation (read, write)
- *frua.base.db.sqlite*: SQLITE support
- *frua.base.fs* : Tools for files, directories, users and groups
- *frua.base.obj* : objects
- *frua.base.log* : Logging objects and tools
- *frua.base.time* : Time (datetime) helpers

# List of dependencies

- [requests](https://requests.readthedocs.io/en/latest/): Requests allows you to send HTTP/1.1 requests extremely easily .


## Usage

### To install locally

`pip install -e .`

### To use the library

Example: 
`import frua.base.obj as obj`


<!-- pyscaffold-notes -->

## Note

This project has been set up using [PyScaffold](https://pyscaffold.org/) 4.4.
In addition, this project has been set up using [pyscaffoldext-markdown](https://github.com/pyscaffold/pyscaffoldext-markdown)
