#!/usr/bin/python2
# -*- coding: UTF-8 -*-

import zlib
import binascii

idat_hex = "789C5D91011280400802BF04FFFF5C75294B5537738A21A27D1E49CFD17DB3937A92E7E603880A6D485100901FB0410153350DE83112EA2D51C54CE2E585B15A2FC78E8872F51C6FC1881882F93D372DEF78E665B0C36C529622A0A45588138833A170A2071DDCD18219DB8C0D465D8B6989719645ED9C11C36AE3ABDAEFCFC0ACF023E77C17C7897667".decode('hex')

#print(idat_hex)

#idat_hex_decompress = zlib.decompress(idat_hex)
#print(idat_hex_decompress)

result = binascii.hexlify(zlib.decompress(idat_hex))
#result = binascii.hexlify(idat_hex)
#print(result)

bin = result.decode('hex')
print(bin)

print("Length=", len(bin))
