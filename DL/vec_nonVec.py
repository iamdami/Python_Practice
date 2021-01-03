import numpy as np
import time  # Time how long the operation takes

# Create million-dimensional array of random numbers
a = np.random.rand(1000000)
b = np.random.rand(1000000)

tic = time.time()  # Set current time
c = np.dot(a, b)
toc = time.time()

print(c)
# Expressed in milliseconds
print("Vectorized version: " + str(1000 * (toc - tic)) + "ms")

c = 0
tic = time.time()
for i in range(1000000):
    c += a[i]*b[i]
toc = time.time()

print(c)
# Non-Vectorized version
print("for loop: " + str(1000*(toc-tic)) + "ms")

