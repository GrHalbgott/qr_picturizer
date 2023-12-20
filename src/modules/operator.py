#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Operational functions"""


import os
import numpy as np
from pathlib import Path
from PIL import Image


def read_as_rgb(infile):
    """
    Convert image to RGB
    :param infile: input image
    :return: RGB image
    """
    file = Image.open(infile)
    rgb = file.convert("RGB")
    arr = np.asarray(rgb)

    return arr


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

    data_mean = data_ex.mean()

    return data_ex, data_mean


def replacer(infolder, img, data, img_list, data_mean):
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
            img = read_as_rgb(Path(infolder / np.random.choice(img_list)))
            # check values in axis 0, replace all values below mean with img, else 255
            if data[i, j, 0] > data_mean:
                data[i:i + img.shape[0], j:j + img.shape[1], 0] = img[:, :, 0]
                data[i:i + img.shape[0], j:j + img.shape[1], 1] = img[:, :, 1]
                data[i:i + img.shape[0], j:j + img.shape[1], 2] = img[:, :, 2]
            else:
                data[i:i + img.shape[0], j:j + img.shape[1], 0] = 0
                data[i:i + img.shape[0], j:j + img.shape[1], 1] = 0
                data[i:i + img.shape[0], j:j + img.shape[1], 2] = 0

    return data
