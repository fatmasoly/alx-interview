#!/usr/bin/python3
"""utf8 validation"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    if not data:
        return False
    char = 0
    for byte in data:
        if char:
            if byte >> 6 != 0b10:
                return False
            char -= 1
            continue
        if byte >> 7 == 0:
            continue
        while byte:
            byte >>= 1
            char += 1
        if char == 1 or char > 4:
            return False
        char = max(char - 1, 0)
    return char == 0
