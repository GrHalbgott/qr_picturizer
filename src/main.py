#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Picturize QR codes"""

import yaml
import logging.config
import numpy as np
from pathlib import Path
from PIL import Image

from modules.utils import _check_input_arguments, init_logger
from modules.qr_generator import qr_generator
import modules.operator as operator


init_logger("./conf/logging_config.json")


def main():
    """Main function"""
    with open("./conf/config.yaml", "r") as yaml_file:
        config = yaml.safe_load(yaml_file)
    with open("./conf/params.yaml", "r") as yaml_file:
        params = yaml.safe_load(yaml_file)

    indir = Path(config["data_dir"])
    outdir = Path(config["out_dir"])
    outdir.mkdir(exist_ok=True)

    imgdir = indir / config["images_dir"]

    outfile = outdir / params["name_out_img"]

    checker = _check_input_arguments()

    if checker:
        path_img = indir / params["name_in_img"]
        pass
    else:
        text = input("Please enter the text you want to generate a QR-Code for: ")
        img = qr_generator(text)
        path_img = indir / params["name_gen_qr"]
        img.save(path_img)

    assert path_img.exists(), "No image found in ./data. Please put it an image in there or disable the -pic flag."

    data = operator.read_as_rgb(path_img)
    logging.info(f"Image shape: {data.shape}")

    assert imgdir.exists(), "No images found in ./data/images. Please add images to this folder and rerun the program."

    # Create image list
    logging.info("Creating image list...")
    img_list = operator.read_image_list(imgdir)

    # Read random image from list
    img = operator.read_as_rgb(Path(imgdir / np.random.choice(img_list)))
    logging.info(f"Random image shape: {img.shape}")

    # Enlarge QR code
    logging.info("Enlarging original image...")
    data, data_mean = operator.raster_enlarger(img, data)
    logging.info(f"Enlarged array shape: {data.shape}")

    # Add images
    logging.info("Adding images...")
    data = operator.replacer(imgdir, img, data, img_list, data_mean, params["replace_color"])

    # Save image
    logging.info("Saving image...")
    image = Image.fromarray(data)
    maxwidth = params["width"]
    if image.size[0] > maxwidth:
        logging.info("Compressing image...")
        image = operator.compressor(image, maxwidth)
        logging.info(f"Compressed image shape: {image.size}, 3")
    image.save(outfile, quality=95, optimize=True)


if __name__ == "__main__":
    main()
