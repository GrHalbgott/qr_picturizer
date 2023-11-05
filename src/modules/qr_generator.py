#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generates QR code"""


import qrcode


def qr_generator(text):
    """Generates QR code"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    return img
