# qr_picturizer

Picturize QR codes with your own pictures!
Create QR codes from links or text and picturize them with your pictures.

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

## Run program

**Example**:
```console
$ python src/main.py -t https://github.com/GrHalbgott/qr_picturizer.git
```
**Usage**:
```console
$ python .\src\main.py -h

usage: main.py [-h] [-t Text] [-p Picture]

-h, --help  show this help message and exit

optional arguments:
  -t Text     String | Text you want to generate a QR-Code for (e.g. hyperlink)
  -p Picture  String | Path to your generated QR code
```
