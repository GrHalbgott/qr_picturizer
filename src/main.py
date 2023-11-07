#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Picturize QR codes"""


import logging.config
import numpy as np
from pathlib import Path
from PIL import Image

from modules.utils import _check_input_arguments, init_logger
from modules.qr_generator import qr_generator
from modules.operator import read_raster, read_image_list, raster_enlarger


if __name__ == "__main__":

    init_logger("./config/logging_config.json")

    outfolder = Path("results")
    outfolder.mkdir(exist_ok=True)

    infolder = Path("data/images")

    path_qr = "./results/qr_code.png"
    outfile = "./results/qr_code_picturized.png"

    input, check = _check_input_arguments()

    if check:
        img = input
    else:
        img = qr_generator(input)
        img.save(path_qr)

    data = read_raster(path_qr)
    logging.info(f"QR code shape: {data.shape}")

    assert infolder.exists(), "No images found in data/images. Please add images to this folder and rerun the program."

    # Create image list
    img_list = read_image_list(infolder)

    # Read random image from list
    img = read_raster(Path(infolder / np.random.choice(img_list)))

    # Enlarge QR code
    data = raster_enlarger(outfolder, img, data)
    logging.info(f"Enlarged array shape: {data.shape}")

    image = Image.fromarray(data)
    image.save(outfile)
