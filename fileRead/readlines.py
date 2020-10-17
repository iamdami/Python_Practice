f = open("C:/newFile.txt", 'r', encoding='UTF8')
lines = f.readlines()
#Reads all lines of the file and returns a list of each line element
for line in lines:
    print(line)
f.close()
