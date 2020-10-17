f = open("C:/newFile.txt", 'r', encoding='UTF8')
data = f.read() # Returns all text in file
print(data)
f.close()
