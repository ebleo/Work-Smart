# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 14:55:10 2016

@author: danielle.leong
"""

cN = -1
c = 0
r = []
y = []
rTest = ''

x = input("cell name/ind")
xlen = len(x)
for i in range(xlen):
    if ord('A') <= ord(x[i]) <= ord('Z'):
        cVal = ord(x[i]) - ord('A')
        c += cVal
        cN += cN
        if cN == 1:
            cN = 0
            c = c + cN
    else:
        r.append(int(x[i]))
        rTest = (rTest + x[i])
        
rTest = int(rTest)    
    
        
