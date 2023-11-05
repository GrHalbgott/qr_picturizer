# qr_picturizer

## Prerequisites

- [Mamba](https://mamba.readthedocs.io/en/latest/index.html) (recommended) or [Conda](https://docs.conda.io/en/latest/)

## Installation

**1. Download this repository**

```console
$ git clone https://github.com/GrHalbgott/qr_picturizer.git
$ cd qr-picturizer
```

**2. Setup new virtual environment with all necessary dependencies**

```console
$ [mamba or conda] env create -f environment.yml
$ [mamba or conda] activate qr-picturizer
$ poetry install
```
Poetry will detect and respect an existing virtual environment that has been externally activated and will install the dependencies into that environment.

To update the packages to their latest suitable versions (and the poetry.lock file), run:
```console
$ poetry update
```
