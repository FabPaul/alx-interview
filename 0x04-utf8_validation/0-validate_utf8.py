#!/usr/bin/python3
"""UTF-8"""


def validUTF8(data):
    """UTF-8 Function"""
    current_bytes_number = 0

    bitmask_1 = 1 << 7
    bitmask_2 = 1 << 6

    for byte in data:
        bitmask = 1 << 7

        if current_bytes_number == 0:
            while bitmask & byte:
                current_bytes_number += 1
                bitmask = bitmask >> 1

            if current_bytes_number == 0:
                continue

            if current_bytes_number == 1 or current_bytes_number > 4:
                return False

        else:
            if not (byte & bitmask_1 and not (byte & bitmask_2)):
                return False

        current_bytes_number -= 1

    if current_bytes_number == 0:
        return True

    return False
