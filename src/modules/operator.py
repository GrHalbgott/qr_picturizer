#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Operational functions"""


import os
import numpy as np
import rasterio as rio
from pathlib import Path
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


def raster_enlarger(img, data):
    """
    Expand the QR code using the shape of the input image
    :param data: QR code as Numpy array
    :return: larger Numpy array
    """
    data_ex = data.repeat(img.shape[0], axis=0).repeat(img.shape[1], axis=1)
    data_ex = np.multiply(data_ex, 255).astype(np.uint8)

    return data_ex


def replacer(infolder, img, data, img_list):
    """
    Iterates through array and replaces blocks with zeros with images
    :param infolder: path to images
    :param img: input image
    :param data: QR code as Numpy array
    :param img_list: list of images
    :return: updated Numpy array
    """
    shape_x = data.shape[0]
    shape_y = data.shape[1]

    for j in range(0, shape_y, img.shape[1]):
        for i in range(0, shape_x, img.shape[0]):
            img = read_raster(Path(infolder / np.random.choice(img_list)))
            if data[i, j] == 0:
                data[i:i + img.shape[0], j:j + img.shape[1]] = img
            else:
                data[i:i + img.shape[0], j:j + img.shape[1]] = 255

    return data
