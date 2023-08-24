#!/usr/bin/python3
"""
Determines if given dataset is utf8 encoded
"""


def validUTF8(data):
    """ Check if 'data' is utf-8 encoded """
    try:
        maskeddata = [n & 255 for n in data]
        bytes(maskeddata).decode("UTF-8")
        return True
    except Exception:
        return False
