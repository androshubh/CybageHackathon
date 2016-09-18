from os import stat
#from stat import *

def checkSize(file_name):
    if stat(file_name).st_size < 250000:
        print ("Size of file ",stat(file_name).st_size)
        return True
    return False

def line(file_name):
    s = ""
    file = open(file_name)
    for x in file.readlines():
        s = s+x.rstrip('\n')
    file.close()
    y = s.split('.  ')
    print ("Type of y ",type(y))
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
        print (x," --//occure//-- ",y, "times.\n")

    #print("Words in file :- ",len(s.split(" "))-len(z)-1)

def word_count(s):
    open = dict()
    #count = 0
    s=s.replace(".", " ")
    print("count of words in file :- ",len(s.split(" ")))
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
        print ("\033[1m",x," occure ", "\033[1m",y, "times.\n")

file_name = input("Enter file name ")
if '.txt' in file_name and   checkSize(file_name):
    line(file_name)
else:
    print("file is not present or of size more than 2mb")
