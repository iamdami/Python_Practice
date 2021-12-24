import csv
f = open('subwayfee.csv')
data = csv.reader(f)
next(data)

for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    print(row)
