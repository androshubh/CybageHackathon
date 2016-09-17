import os
from stat import *

def checkSize(file_name):
    if os.stat(file_name).st_size < 250000:
        return True
    return False

def line(file_name):
    s = ""
    file = open(file_name)
    for x in file.readlines():
        s = s+x.rstrip('\n')
        z.append(x)
    file.close()
    return s,z

file_name = input("Enter file name ")
if '.txt' in file_name and   checkSize(file_name):
    y = list()
    z = list()
    s,z=line(file_name)
    y=s.split('.  ')
    print("Count of statement :- ",len(z))
    print(y,len(z))
else:
    print("file is not present or of size more than 2mb")
