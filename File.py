import os
from stat import *

def checkSize(file_name):
    if os.stat(file_name).st_size < 250000:
        print ("Size of file ",os.stat(file_name).st_size)
        return True
    return False

def line(file_name):
    s = ""
    file = open(file_name)
    for x in file.readlines():
        s = s+x.rstrip('\n')
        z.append(x)
    file.close()
    y = s.split('.  ')
    print(y)
    #print("Words in file :- ",len(s.split(" "))-len(z)-1)
    word_count(s)
    return z

def word_count(s):
    print(s,type(s))
    open = dict()
    #count = 0
    s=s.replace(".", " ")
    print(len(s.split(" ")))
    for word in s.split(None, len(s)):
        #word = word.rstrip(".").rstrip(",").rstrip(" ").lower()
        word=word.lower()
        #print (word)
        if word in open:
            count = open[word]
            open[word] = count+1
        else:
            open[word] = 1
    print("%"*40)
    print(open)

file_name = input("Enter file name ")
if '.txt' in file_name and   checkSize(file_name):
    y = list()
    z = list()
    z=line(file_name)
    print("Count of statement :- ",len(z))
else:
    print("file is not present or of size more than 2mb")
