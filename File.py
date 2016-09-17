file_name = input("Enter file name ")
if '.txt' in file_name:
    file = open(file_name)
    y = []
    s = "abc"
    #print(file.read())
    for x in file.readlines():
        s= s+x
        #y.append(x.split(' '))
        print("x:",s)
    #print(y, type(y), len(y))
    s.replace("\n","")
    y.append(s.split('.'))
    print(y,type(y))
    file.close()
