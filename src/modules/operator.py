#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Operational functions"""


import os
import numpy as np
import rasterio as rio
from PIL import Image


def read_raster(infile):
    """
    Read the input files as Numpy arrays and preprocess them
    :param in_dem: path to input file (string)
    :return: returns a Numpy array
    """
    with rio.open(infile) as src:
        data = src.read(1)

    return data


def read_image_list(path):
    """
    Read images from folder and return a list of images
    :param path: path to images
    :return: list of images
    """
    img_list = os.listdir(path)

    return img_list


def raster_enlarger(outfolder, img, data):
    """
    Expand the QR code using the shape of the input image
    :param data: QR code as Numpy array
    :return: larger Numpy array
    """
    data_ex = data.repeat(img.shape[0], axis=0).repeat(img.shape[1], axis=1)
    data_ex = np.multiply(data_ex, 255).astype(np.uint8)

    image = Image.fromarray(data_ex)
    image.save(outfolder / "qr_expanded.png")

    return data_ex
