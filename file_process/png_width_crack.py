#!/usr/bin/python2
# -*- coding: UTF-8 -*-

import os
import binascii
import struct

file = open("example.png", 'rb').read()

for i in range(1024):
    data = file[12:16] + struct.pack('>i', i) + file[20:29]
    crc32 = binascii.crc32(data) & 0xffffffff
    if crc32 == 0x84B2E9CE:
        print(hex(i), i)
