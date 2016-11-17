# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 15:03:16 2016

@author: danielle.leong
"""
# https://www.sitepoint.com/using-python-parse-spreadsheet-data/
okay = True
while okay == True:
    check1 = input("Are all your files in the same directory? Enter 'Y' or 'N':\t")
    while check1 != 'Y' or check1 != 'N':
        print("Please follow directions!")
        check1 = input("Y or N")
    check2 = input("Is your folder on your desktop? Enter 'Y' or 'N':\t")
    while check1 != 'Y' or check1 != 'N':
        print("Please follow directions!")
        check1 = input("Y or N")

    if check1 == 'N' or check2 == 'N':
        okay = False

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

    def choose_file(string):
        get_menu(files)
        x = input("Enter selection: ")
        file_picked = files[x]
        return file_picked

    print("You will now select your Spotmatcher.")
    print("~~~~~")
    xl_file1 = choose_file()
    print("You will now select your Autotemplate.")
    print("~~~~~")
    xl_file2 = choose_file()

    wb1 = xl.open_workbook(xl_file1)
    wb2 = xl.open_workbook(xl_file2)
    sheet1 = wb1.sheet_by_name("Auto Template Output")
    sheet2 = wb2.sheet_by_name("Nat'l Template")

    rStart1 = 2 # [(excel row num - 1)]
    rEnd1 = sheet1.nrows # int by default
    cStart1 = 0
    cEnd1 = sheet1.ncols
