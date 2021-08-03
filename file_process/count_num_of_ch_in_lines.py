#!/usr/bin/python3
# -*- coding: UTF-8 -*-

file = open('./data.dat', 'r')
print("You opened the file: ", file.name)

line_count = 0

for line in file.readlines():
    num_0 = 0
    num_1 = 0
    for ch in line:
        if ch == '0':
            num_0 += 1
        if ch == '1':
            num_1 += 1
    if num_0 % 3 == 0 or num_1 % 2 == 0:
        line_count += 1

print(line_count)

