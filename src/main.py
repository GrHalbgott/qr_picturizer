#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Picturize QR codes"""

import hydra
import logging.config
import numpy as np
from pathlib import Path
from PIL import Image
from omegaconf import DictConfig

from modules.utils import _check_input_arguments, init_logger
from modules.qr_generator import qr_generator
import modules.operator as operator


init_logger("./conf/logging_config.json")


@hydra.main(version_base=None, config_path='../conf', config_name='config')
def main(cfg: DictConfig) -> None:
    """Main function"""
    indir = Path(cfg.data_dir)
    outdir = Path(cfg.out_dir)
    outdir.mkdir(exist_ok=True)

    imgdir = indir / cfg.images_dir

    path_img = indir / cfg.name_in_img
    outfile = outdir / cfg.name_out_img

    logging.info("Checking inputs...")
    checker = _check_input_arguments()

    if checker:
        pass
    else:
        text = input("Please enter the text you want to generate a QR-Code for: ")
        img = qr_generator(text)
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
    data = operator.replacer(imgdir, img, data, img_list, data_mean, cfg.replace_color)

    # Save image
    logging.info("Saving image...")
    image = Image.fromarray(data)
    if image.size[0] > cfg.width:
        logging.info("Compressing image...")
        image = operator.compressor(image, cfg.width)
        logging.info(f"Compressed image shape: {image.size}, 3")
    image.save(outfile, quality=95, optimize=True)


if __name__ == "__main__":
    main()
