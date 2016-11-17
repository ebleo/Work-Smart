# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 14:55:10 2016

@author: danielle.leong
"""
def xl_ind(x):
    index = []
    c = 0
    r = ''
    add_cols = 0

    xlen = len(x)
    for i in range(xlen):
        if ord('A') <= ord(x[i]) <= ord('Z'):
            cVal = ord(x[i]) - ord('A')
            cNext = ord('A') <= ord(x[i + 1]) <= ord('Z')
            print(cNext)
            if cNext:
                print('entered')
                print(x[i])
                add_cols = (cVal + 1) * 26
                print(add_cols)
                c = c + add_cols
                print("l1\t",c)
            else:
                c = c + cVal + 1
                print("l2\t",c)
        else:
            r = (r + x[i])

    r = int(r)
    print(r)
    index.append(r)
    index.append(c)
    return index
