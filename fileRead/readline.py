f = open("C:/newFile.txt", 'r', encoding='UTF8')
while True: # Print until there are no more lines to read
    line = f.readline()
    if not line: break
    print(line)
f.close()
