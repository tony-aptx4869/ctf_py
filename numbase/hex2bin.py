#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# !!!!! TO BE CONTINUE !!!!!

import zlib
import binascii

idat_hex = "\x78\x9C\x5D\x91\x01\x12\x80\x40\x08\x02\xBF\x04\xFF\xFF\x5C\x75\x29\x4B\x55\x37\x73\x8A\x21\xA2\x7D\x1E\x49\xCF\xD1\x7D\xB3\x93\x7A\x92\xE7\xE6\x03\x88\x0A\x6D\x48\x51\x00\x90\x1F\xB0\x41\x01\x53\x35\x0D\xE8\x31\x12\xEA\x2D\x51\xC5\x4C\xE2\xE5\x85\xB1\x5A\x2F\xC7\x8E\x88\x72\xF5\x1C\x6F\xC1\x88\x18\x82\xF9\x3D\x37\x2D\xEF\x78\xE6\x65\xB0\xC3\x6C\x52\x96\x22\xA0\xA4\x55\x88\x13\x88\x33\xA1\x70\xA2\x07\x1D\xDC\xD1\x82\x19\xDB\x8C\x0D\x46\x5D\x8B\x69\x89\x71\x96\x45\xED\x9C\x11\xC3\x6A\xE3\xAB\xDA\xEF\xCF\xC0\xAC\xF0\x23\xE7\x7C\x17\xC7\x89\x76\x67".encode('hex')

result = binascii.hexlify(zlib.decomporess(idat_hex))

print(result)

bin = result.decode('hex')

print(bin)

print('\n\n')

print("Length", len(bin))