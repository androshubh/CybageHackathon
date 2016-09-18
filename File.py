from os import stat
import time
#from stat import *

def checkSize(file_name):
    if stat(file_name).st_size < 250000:
        print ("Size of file ",stat(file_name).st_size," bytes")
        return True
    return False

def line(file_name):
    s = ""
    file = open(file_name)
    for x in file.readlines():
        s = s+x.rstrip('\n')
    file.close()
    y = s.split('.  ')
    print ("statement count :- ",len(y))
    word_count(s)
    opens = dict()
    for s in y:
        s=s.replace('.','')
        if s in opens:
            count = opens[s]
            opens[s] = count+1
        else:
            opens[s] = 1
    print("%"*40)
    for x, y in opens.items():
        print (x," --//occured//-- ",y, "times.\n")

    #print("Words in file :- ",len(s.split(" "))-len(z)-1)


def word_count(s):
    open = dict()
    ss=0

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

    for x, y in open.items():
        ss=ss+y
        print ("\033[1m",x," occured ", "\033[1m",y, "times.")
    print("\n\n Word count ", ss)

file_name = input("Enter file name ")
start = time.time()
#if '.txt' in file_name and   checkSize(file_name):
if '.txt' in file_name:
    line(file_name)
else:
    print("file is not present or of size more than 2mb")
print("Exicution time",start-time.time())
