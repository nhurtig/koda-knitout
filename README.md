# koda-knitout

[![PyPI - Version](https://img.shields.io/pypi/v/koda-knitout.svg)](https://pypi.org/project/koda-knitout)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/koda-knitout.svg)](https://pypi.org/project/koda-knitout)

-----
## Description
KODA (Knitting Optimization by Dependency Analysis). 

A system for analyzing the dependencies between knitout operations executed on a knitting machine and supports the optimization of knitout programs using this dependency structure. 
## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install koda-knitout
```

## Use as a submodule

```console
git submodule add git@github.com:nhurtig/koda-knitout.git koda-knitout
pip install -r koda-knitout/requirements.txt
python3 koda-knitout/koda_cli.py infile.k outfile.k
```

With the versions pinned in `requirements.txt`, the input must not use negative
needle indices, `x-` extension lines, or drops.

## License

`koda-knitout` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
