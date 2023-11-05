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
    help_msg = ""
    parser = argparse.ArgumentParser(description=help_msg, prefix_chars="-")
    parser.add_argument(
        "-t",
        metavar="Text",
        dest="text",
        help="String | Text you want to generate a QR-Code for (e.g. hyperlink)",
    )
    parser.add_argument(
        "-p",
        metavar="Picture",
        dest="picture",
        help="String | Path to your generated QR code",
    )

    if len(sys.argv) > 1:
        args = parser.parse_args()
        text = args.text
        picture = Path(args.picture)

        if picture:
            return picture, True
        elif text:
            return text, False
    else:
        text = input("Please enter the text you want to generate a QR-Code for: ")
        return text, False


def init_logger(logging_config_file=None):
    """
    Set up a logger instance with stream and file logger
    :return:
    """
    with open(logging_config_file, "r") as src:
        logging_config = json.load(src)

    logging.config.dictConfig(logging_config)
