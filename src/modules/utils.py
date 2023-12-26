#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Utility functions"""


import sys
import argparse
import logging
import json

from pathlib import Path


def _check_input_arguments():
    """Check input arguments"""
    # Initialize argparse and specify the optional arguments
    help_msg = "Picturize QR codes with your own pictures! Just specify if you want to use your own QR code or create one."
    parser = argparse.ArgumentParser(description=help_msg, prefix_chars="-")
    parser.add_argument(
        "-pic",
        action="store_true",
        dest="checker",
        help="Flag | Use if you provide a QR code, otherwise create one. Default: False")

    args = parser.parse_args()
    checker = args.checker

    return checker


def init_logger(logging_config_file=None):
    """
    Set up a logger instance with stream and file logger
    :return:
    """
    with open(logging_config_file, "r") as src:
        logging_config = json.load(src)

    logging.config.dictConfig(logging_config)
