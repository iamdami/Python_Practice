import csv
import matplotlib.pyplot as plt
f = open('subwayfee.csv')
data = csv.reader(f)
next(data)
label = ['유임승차','유임하차','무임승차','무임하차']
for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    #plt.figure(dpi = 300)
    plt.pie(row[4:8])
    plt.axis('equal')
    plt.show()
