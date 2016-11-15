"""
                             .__  __  ._.
  _____   _______  __ ____   |__|/  |_| |
 /     \ /  _ \  \/ // __ \  |  \   __\ |
|  Y Y  (  <_> )   /\  ___/  |  ||  |  \|
|__|_|  /\____/ \_/  \___  > |__||__|  __
      \/                 \/            \/
a simple code for moving the Kantar Pulls
by Danielle Leong, Data Superstar
no autographs, please~

Created on Wed Nov  9 15:47:05 2016
"""
# referencing the following site:
# https://www.tutorialspoint.com/python/python_files_io.htm
# https://docs.python.org/3/library/os.html

# generate file names
# for all to rename
names = []
for i in range(12):
    if i < 4:
        t = "C3"
        names.append(t + " DEMO " + str(i + 1))
    elif i < 8:
        t = "C7"
        names.append(t + " DEMO " + str(i - 3))
    else:
        t = "LIVE"
        names.append(t + " DEMO " + str(i - 7))

fileNames = ["C3", "LIVE", "PANEL C3", "PANEL LIVE"]
fileNames.extend(names) # used for renaming

counter = 0
for name in fileNames:
    fileNames[counter] = name + ".csv"
    counter = counter + 1

import os
os.chdir("C:/Users/danielle.leong/Desktop/Kantar Pull--testing")

# splitting and renaming
# http://stackoverflow.com/questions/5749195/how-can-i-split-and-parse-a-string-in-python

# obtain file names
ori = os.listdir("C:/Users/danielle.leong/Desktop/Kantar Pull--testing")

counter = 0
for f in ori:
    os.rename(f, fileNames[counter])
    counter = counter + 1
