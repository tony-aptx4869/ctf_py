#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from pycipher import Vigenere

print(u"Vigenere")
number = input('Input 1 for Encrypto,Input 2 for Decrypto : ')
while True:
    if number == '1':
        print(u"Vigenere Encrypto")
        plainText = input ("Please input the plainText : ")
        key = input ("Please input the key : ")
        plainTextToCipherText = Vigenere(key).encipher(plainText) 
        print(u"The CipherText is : " + plainTextToCipherText)
        break
    elif number == '2':
        print(u"Vigenere Decrypto")
        cipherText = input ("Please input the cipherText : ")
        key = input ("Please input the key : ")
        cipherTextToPlainText = Vigenere(key).decipher(cipherText)
        print(u"The PlainText is : " + cipherTextToPlainText)
        break
    else:
        print('Please input 1 or 2.')
        continue
