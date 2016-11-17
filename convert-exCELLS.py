# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 14:55:10 2016

@author: danielle.leong
"""

cN = 0
c = 0
r = []
y = []
rTest = ''
prev = 0

x = input("cell name/ind \t")
xlen = len(x)
for i in range(xlen):
    if ord('A') <= ord(x[i]) <= ord('Z'):
        cVal = ord(x[i]) - ord('A')
        if cN == 1:
            cN = 0
            c = c + 26 + (cVal - prev) + 1
        else:
            c += cVal
            cN += 1
            prev = cVal

    else:
        r.append(int(x[i]))
        rTest = (rTest + x[i])

rTest = int(rTest)
