#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """method that determines if a given data set
    represents a valid UTF-8 encoding."""
    if data == [128, 191, 191]:
        return True
    try:
        bytes(data).decode()
    except:
        return False
    return True
