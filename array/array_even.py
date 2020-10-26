import numpy as np
with open('C:/even.txt', 'r') as even:
    arr = [int(float(i)) for i in even.read().split(',')]

a = np.array(arr)

print("original: ",arr)

for i in arr:
    if i % 2 == 0:
        print(i)
