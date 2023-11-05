#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Operational functions"""


import rasterio as rio


def read_raster(infile):
    """
    Read the input files as Numpy arrays and preprocess them
    param in_dem: path to input file (string)
    output: returns a Numpy array
    """
    with rio.open(infile) as src:
        data = src.read(1)

    return data
