import os
file_name = input("Enter file name ")
if '.txt' in file_name:
    file = open(file_name)
    y = list()
    z = list()
    #size = os.path.getsize(file)
    #print(size.st_size)
    #print("@"*40)
    s = ""
    #print(file.read())
    for x in file.readlines():
        s = s+x.rstrip('\n')
        #s= s+x
        z.append(x.split(' '))
        #print("x:",s)
    #print(y, type(y), len(y))
    #s = s.replace("\n"," ")
    y=s.split('.  ')
    print(y,len(z))
    file.close()
