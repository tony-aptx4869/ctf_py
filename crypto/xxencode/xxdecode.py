#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
import re
import binascii

# first argument: unknown coding text
# if len(sys.argv) != 2:
# 	sys.exit(2)
# estr=sys.argv[1]

# xxencode_dict = {
#     '00': '+', '01': '-', '02': '0', '03': '1', '04': '2', '05': '3', '06': '4', '07': '5',
#     '08': '6', '09': '7', '0a': '8', '0b': '9', '0c': 'A', '0d': 'B', '0e': 'C', '0f': 'D',
#     '10': 'E', '11': 'F', '12': 'G', '13': 'H', '14': 'I', '15': 'J', '16': 'K', '17': 'L',
#     '18': 'M', '19': 'N', '1a': 'O', '1b': 'P', '1c': 'Q', '1d': 'R', '1e': 'S', '1f': 'T',
#     '20': 'U', '21': 'V', '22': 'W', '23': 'X', '24': 'Y', '25': 'Z', '26': 'a', '27': 'b',
#     '28': 'c', '29': 'd', '2a': 'e', '2b': 'f', '2c': 'g', '2d': 'h', '2e': 'i', '2f': 'j',
#     '30': 'k', '31': 'l', '32': 'm', '33': 'n', '34': 'o', '35': 'p', '36': 'q', '37': 'r',
#     '38': 's', '39': 't', '3a': 'u', '3b': 'v', '3c': 'w', '3d': 'x', '3e': 'y', '3f': 'z' 
#     }
# xxdecode_dict = dict(zip(xxencode_dict.values(),xxencode_dict.keys()))

xxdecode_dict = {
    '+': '00', '-': '01', '0': '02', '1': '03', '2': '04', '3': '05', '4': '06', '5': '07',
    '6': '08', '7': '09', '8': '0a', '9': '0b', 'A': '0c', 'B': '0d', 'C': '0e', 'D': '0f',
    'E': '10', 'F': '11', 'G': '12', 'H': '13', 'I': '14', 'J': '15', 'K': '16', 'L': '17',
    'M': '18', 'N': '19', 'O': '1a', 'P': '1b', 'Q': '1c', 'R': '1d', 'S': '1e', 'T': '1f',
    'U': '20', 'V': '21', 'W': '22', 'X': '23', 'Y': '24', 'Z': '25', 'a': '26', 'b': '27',
    'c': '28', 'd': '29', 'e': '2a', 'f': '2b', 'g': '2c', 'h': '2d', 'i': '2e', 'j': '2f',
    'k': '30', 'l': '31', 'm': '32', 'n': '33', 'o': '34', 'p': '35', 'q': '36', 'r': '37',
    's': '38', 't': '39', 'u': '3a', 'v': '3b', 'w': '3c', 'x': '3d', 'y': '3e', 'z': '3f' 
    }

hex2bin_dict = {
    '0' : '0000', '1' : '0001', '2' : '0010', '3' : '0011',
    '4' : '0100', '5' : '0101', '6' : '0110', '7' : '0111',
    '8' : '1000', '9' : '1001', 'a' : '1010', 'b' : '1011',
    'c' : '1100', 'd' : '1101', 'e' : '1110', 'f' : '1111'
    }

estr = 'Eq3o'

de_list = list(xxdecode_dict[ch] for ch in estr)

print(de_list)

bin_str = ''

for hex_str in de_list:
    tmp_bin_str = ''.join(hex2bin_dict[d_hex] for d_hex in hex_str)
    bin_str += tmp_bin_str[2:]

print(bin_str)

bin_list = re.findall('.{8}', bin_str)

print(bin_list)

decoded_string = ''

for bin_ascii in bin_list:
    decoded_string += chr(int(bin_ascii, 2))

print(decoded_string)
