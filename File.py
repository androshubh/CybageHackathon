file_name = input("Enter file name ")
if '.txt' in file_name:
    file = open(file_name,'r')
    #print(file)
    #file.close()
    y = []
    s=''
    print(file.read())
    for x in file.read():
        #print (x.split(' '))
        s.join(x)
        y.append(x.split('.'))
#    line = file.readline()
#    print (line, type(line))
    print(y, type(y), len(y))
    print(s, type(s))
    file.close()
