#!/usr/bin/python2
# -*- coding: UTF-8 -*-

import zlib
import binascii

#hex_str = "666c61677b68656c6c6f5f776f726c647d".decode('hex')
hex_str = "666C61677B68315F6337667D".decode('hex')
#hex_str = "495f346d2d6b3379".decode('hex')

print(hex_str)

print("Length=", len(hex_str))

#idat_hex_decompress = zlib.decompress(idat_hex)
#print(idat_hex_decompress)

#result = binascii.hexlify(zlib.decompress(idat_hex))
#result = binascii.hexlify(idat_hex)
#print(result)

#bin = result.decode('hex')
#print(bin)

#print("Length=", len(bin))
