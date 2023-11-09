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
from modules.operator import read_as_rgb, read_image_list, raster_enlarger, replacer


init_logger("./conf/logging_config.json")


@hydra.main(version_base=None, config_path='../conf', config_name='config')
def main(cfg: DictConfig) -> None:
    """Main function"""
    indir = Path(cfg.data_dir)
    outdir = Path(cfg.out_dir)
    outdir.mkdir(exist_ok=True)

    imgdir = indir / cfg.images_dir

    path_qr = indir / cfg.name_in_qr
    outfile = outdir / cfg.name_out_qr

    logging.info("Checking inputs...")
    checker = _check_input_arguments()

    if checker:
        pass
    else:
        text = input("Please enter the text you want to generate a QR-Code for: ")
        img = qr_generator(text)
        img.save(path_qr)

    assert path_qr.exists(), "No QR code found in data. Please put it a QR code or disable the -pic flag."

    data = read_as_rgb(path_qr)
    logging.info(f"QR code shape: {data.shape}")

    assert imgdir.exists(), "No images found in data/images. Please add images to this folder and rerun the program."

    # Create image list
    logging.info("Creating image list...")
    img_list = read_image_list(imgdir)

    # Read random image from list
    img = read_as_rgb(Path(imgdir / np.random.choice(img_list)))
    logging.info(f"Random image shape: {img.shape}")

    # Enlarge QR code
    logging.info("Enlarging QR code...")
    data = raster_enlarger(img, data)
    logging.info(f"Enlarged array shape: {data.shape}")

    logging.info("Replacing QR code with images...")
    data = replacer(imgdir, img, data, img_list)

    logging.info("Saving image...")
    image = Image.fromarray(data)
    image.save(outfile)


if __name__ == "__main__":
    main()
