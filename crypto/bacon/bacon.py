#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

first_cipher = ["aaaaa","aaaab","aaaba","aaabb","aabaa","aabab","aabba","aabbb","abaaa","abaab","ababa","ababb","abbaa","abbab","abbba","abbbb","baaaa","baaab","baaba","baabb","babaa","babab","babba","babbb","bbaaa","bbaab"]

second_cipher = ["aaaaa","aaaab","aaaba","aaabb","aabaa","aabab","aabba","aabbb","abaaa","abaaa","abaab","ababa","ababb","abbaa","abbab","abbba","abbbb","baaaa","baaab","baaba","baabb","baabb","babaa","babab","babba","babbb"]

def encode():
    string = input("please input string to encode:\n")
    e_string1 = ""
    e_string2 = ""
    for index in string:
        for i in range(0,26):
            if index == alphabet[i]:
                e_string1 += first_cipher[i]
                e_string2 += second_cipher[i]
                break
    print("first encode method result is:\n"+e_string1)
    print("second encode method result is:\n"+e_string2)
    return


def decode():
    e_string = input("please input string to decode:\n")
    e_array = re.findall(".{5}",e_string)
    d_string1 = ""
    d_string2 = ""
    for index in e_array:
        for i in range(0,26):
            if index == first_cipher[i]:
                d_string1 += alphabet[i]
            if index == second_cipher[i]:
                d_string2 += alphabet[i]
    print("first decode method result is:\n"+d_string1)
    print("second decode method result is:\n"+d_string2)
    return


if __name__ == '__main__':
    while True:
        print("\t*******Bacon Encode_Decode System*******")
        print("input should be lowercase,cipher just include a b")
        print("1.encode\n2.decode\n3.exit")
        s_number = input("please input number to choose\n")
        if s_number == "1":
            encode()
            input()
        elif s_number == "2":
            decode()
            input()
        elif s_number == "3":
            break
        else:
            continue
