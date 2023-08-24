#!/usr/bin/python3
"""
Determine if a given dataset is valid utf-8 encoding
"""


def validUTF8(data):
    """Determine if 'data' is valid utf-8 encoding"""
    utf8 = True
    if len(data) == 0:
        return False
    data_bin = list()
    for num in data:
        binary = bin(num)  # Convert int to binary
        if len(binary[2:]) < 8:  # Check if there is need to add leading zeros
            lead_zero = 8 - len(binary[2:])
            binary = lead_zero * '0' + binary[2:]
            data_bin.append(binary)
        else:
            data_bin.append(binary[2:])
    """Now check for utf-8 encoding in the binary numbers"""
    length = len(data_bin)
    i = 0
    print(data_bin)
    while i < length:
        binary = data_bin[i]
        if binary[0] == '0':
            i += 1
        elif binary[0:3] == '110':
            if i + 1 < length and data_bin[i + 1][0:2] == '10':
                i += 2
            else:
                utf8 = False
                break
        elif binary[0:4] == '1110':
            if i + 2 < length:
                for j in range(i + 1, i + 3):
                    if data_bin[j][0:2] != '10':
                        return False
                i += 3
            else:
                utf8 = False
                break
        elif binary[0:5] == '11110':
            if i + 3 < length:
                for j in range(i + 1, i + 4):
                    if data_bin[j][0:2] != '10':
                        return False
                i += 4
            else:
                utf8 = False
                break
        else:
            utf8 = False
            break
    return utf8
