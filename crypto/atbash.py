#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from pycipher import Atbash

atb = Atbash()

encoded_str = 'gsv urihg rh gsv ozhg'

print(atb.decipher(encoded_str))

plain_str = 'The quick brown fox jumps over the lazy dog.'

print(atb.encipher(plain_str))

