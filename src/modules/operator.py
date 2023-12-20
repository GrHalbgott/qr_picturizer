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
    :return: larger Numpy array and mean value of array
    """
    data_ex = data.repeat(img.shape[0], axis=0).repeat(img.shape[1], axis=1)
    data_ex = np.multiply(data_ex, 255).astype(np.uint8)

    data_mean = data_ex.mean()

    return data_ex, data_mean


def replacer(infolder, img, data, img_list, data_mean, brightness):
    """
    Iterates through array and replaces value blocks with images
    :param infolder: path to images
    :param img: image used for shape
    :param data: original image as Numpy array
    :param img_list: list of images
    :param data_mean: mean of array values
    :param brightness: color brightness to replace (over or below mean)
    :return: updated Numpy array
    """
    shape_x = data.shape[0]
    shape_y = data.shape[1]

    # iterate through array and replace values
    for j in range(0, shape_y, img.shape[1]):
        for i in range(0, shape_x, img.shape[0]):
            img = read_as_rgb(Path(infolder / np.random.choice(img_list)))
            # replace values in square on all bands according to brightness
            if brightness == "bright":
                if data[i, j, 0] > data_mean:
                    data[i:i + img.shape[0], j:j + img.shape[1], 0] = img[:, :, 0]
                    data[i:i + img.shape[0], j:j + img.shape[1], 1] = img[:, :, 1]
                    data[i:i + img.shape[0], j:j + img.shape[1], 2] = img[:, :, 2]
                else:
                    data[i:i + img.shape[0], j:j + img.shape[1], 0] = 0
                    data[i:i + img.shape[0], j:j + img.shape[1], 1] = 0
                    data[i:i + img.shape[0], j:j + img.shape[1], 2] = 0
            elif brightness == "dark":
                if data[i, j, 0] < data_mean:
                    data[i:i + img.shape[0], j:j + img.shape[1], 0] = img[:, :, 0]
                    data[i:i + img.shape[0], j:j + img.shape[1], 1] = img[:, :, 1]
                    data[i:i + img.shape[0], j:j + img.shape[1], 2] = img[:, :, 2]
                else:
                    data[i:i + img.shape[0], j:j + img.shape[1], 0] = 255
                    data[i:i + img.shape[0], j:j + img.shape[1], 1] = 255
                    data[i:i + img.shape[0], j:j + img.shape[1], 2] = 255

    return data


def compressor(image, width):
    """
    Compresses image
    :param data: pillow object
    :return: updated pillow object
    """
    maxwidth = width
    width, height = image.size
    aspectratio = width / height
    new_height = maxwidth / aspectratio

    # resize image with maxwidth and calculated maxheight
    image = image.resize((maxwidth, round(new_height)))

    return image
