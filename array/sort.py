# numpy import
import numpy as np

# file read
with open('putFileName.txt', 'r') as ascending:
    arr = [int(float(i)) for i in ascending.read().split(',')]

# Save in variable 'arr' in array format
arr = np.array(arr)

print("Original array: ", arr)

# sorting
s = np.sort(arr)

print("After sort: ", s)
