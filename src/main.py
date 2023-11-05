#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Picturize QR codes"""


import logging.config
import numpy as np
from pathlib import Path

from modules.utils import _check_input_arguments, init_logger
from modules.qr_generator import qr_generator
from modules.operator import read_raster

if __name__ == "__main__":

    init_logger("./config/logging_config.json")

    outfolder = Path("results")
    outfolder.mkdir(exist_ok=True)

    name_qr = "qr_code"
    path_qr = f"./results/{name_qr}.png"
    name_qr_pic = "qr_code_picturized"
    outfile = f"./results/{name_qr_pic}.png"

    input, check = _check_input_arguments()

    if check:
        img = input
    else:
        img = qr_generator(input)
        img.save(path_qr)

data = read_raster(img)

print(data.shape)
