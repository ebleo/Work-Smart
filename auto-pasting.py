# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 15:03:16 2016

@author: danielle.leong
"""
# https://www.sitepoint.com/using-python-parse-spreadsheet-data/

import os
import xlrd as xl

os.chdir("C:/Users/danielle.leong/Desktop/")
folder_name = input("Give folder: ") # str by default
os.chdir(folder_name)
files = os.listdir()

def get_menu(files): # turn list of items into a menu
    print("Choose a file:")
    print("~~~~~~~~~~~~~~~~")
    for i in range(len(files)):
        print(i,". ",files[i])

xl_file1 = input("Give exact filename: ") # not case sensitive
xl_file2 = input("Give exact filename: ")

wb = xl.open_workbook(xl_file1)
sheet1 = wb.sheet_by_name("Auto Template Output")

rStart1 = 2 # [(excel row num - 1)]
rEnd1 = sheet1.nrows # int by default
