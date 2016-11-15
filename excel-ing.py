# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 14:35:53 2016

@author: danielle.leong
"""

import os
import xlrd as xl

print(os.getcwd())
os.chdir("C:/Users/danielle.leong/Desktop/TEST")

wb = xl.open_workbook("File1.xlsx")
sheet = wb.sheet_by_index(0)

emp1 = 0 # 2 rows
emp2 = 0 # two cols

rMax = int(sheet.nrows) # nothing needs to be passed to method
cMax = int(sheet.ncols)

xl_list = [[]]


# make a counter count how many lists in lists and if equal to c/rMax stop making new lists in list
for i in range(rMax):
    for j in range(cMax):
        xl_list
