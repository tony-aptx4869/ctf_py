#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import re

def bin2hex(s1):
    s2 = ''
    s1 = re.findall('.{4}',s1)
    #print ('每一个hex分隔:',s1)
    for i in s1:
        s2 += str(hex(int(i,2))).replace('0x','')
    print ('HEX:', s2.upper())
    print ('hex:', s2)
    return s2


def conv(s):
    return hex(int(s, 2))[2:]

def IEEE802(bs):
    pass
    dict = {
        "0101": "11",
        "1001": "01",
        "0110": "10",
        "1010": "00"
    }
    bs=str(bs)
    print(bs)
    r = ""
    for j in range(0, len(bs), 4):
        i=bs[j:j+4]
        if i in dict.keys():
            r += dict[i]
    return r

def mqst(s):
    mdict = {
        '5': '11',
        '6': '10',
        '9': '01',
        'A': '00'
        }
    m1 = ''.join(mdict[i] for i in s)
    print('Manchester:', m1)
    bin2hex(m1)
    # m2 = ''.join(mdict[i][::-1] for i in s)
    # print('Manchester2:', m2)
    # bin2hex(m2)
    return m1

def IEEE802_reverse(bs):
    bs_reverse = ''
    s1 = re.findall('.{8}', bs)
    # print('Every 8 bits:', s1)
    for str in s1:
        bs_reverse += str[::-1]
    print('Rev_eve_8b:', bs_reverse)
    return bs_reverse


# n = 0x5555555595555A65556AA696AA6666666955
# flag = ''
# bs = '0' + bin(n)[2:]
# r = ''
# print(bs)
# r = IEEE802(bs)

# for i in range(0, len(r), 8):
#     tmp = r[i:i + 8][::-1]
#     flag += conv(tmp[:4])
#     flag += conv(tmp[4:])
# print(flag.upper())


if __name__ == '__main__':
    hex1 = "5555555595555A65556AA696AA6666666955"
    m1 = mqst(hex1)
    m2 = IEEE802_reverse(m1)
    bin2hex(m2)
