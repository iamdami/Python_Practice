import numpy as np
with open('C:/even.txt', 'r') as ascending:
    arr = [int(float(i)) for i in ascending.read().split(',')]

a = np.array(arr)

print("original: ",arr)

for i in arr:
    if i % 2 == 0:
        print(i)
