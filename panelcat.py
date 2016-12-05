# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 13:47:29 216

@author: danielle.leong
"""

# this doesn't work and I dont rmember whyu, my brain is shot. do not use. cannot be used. logic appears fine.
#doesn't work because freezes after running line 27 (?) also doesn't save anything. that would hlep.

import xlutils
from xlutils.copy import copy
import xlrd
import xlwt
import os

os.chdir('c:/users/danielle.leong/desktop/test')
files = os.listdir()

count = 0
for f in files:
    print(count, ') ',f)
    count = count + 1

text = 'Pick your PANEL'
p1 = int(input(text +' LIVE\t'))
p2 = int(input(text + ' C3\t'))

f1 = files[p1]
f2 = files[p2]

rb1 = xlrd.open_workbook(f1)
rb2 = xlrd.open_workbook(f2)
srb2 = rb2.sheet_by_index(0)

wb1 = copy(rb1)
sheet1 = wb1.get_sheet(0) # writable sheet

begin = [8, 17]
end = [srb2.nrows, 18]
vals2copy = []

# stores C3 values
for i in range(end[0] - begin[0]): # rows
    vals2copy.append([])
    for j in range(end[1] - begin[1]):
        x = i + begin[0]
        y = j + begin[1]
        val = srb2.cell(x, y).value
        vals2copy[i][j].append(val)

# write C3 above cols
writeCs = [[7, 19], [7, 20]]
for cell in writeCs:
    sheet1.write(cell[0], cell[1], 'C3')

# writing data
xoff = 0
yoff = 0
start_cell = [8, 19]
for i in len(vals2copy): # returns rows
    x = xoff + start_cell[0]
    y = yoff + start_cell[1]
    for j in vals2copy[i]: #list of col items
        sheet1.write(x, y, j)
        xoff = xoff + 1
        yoff = yoff + 1
