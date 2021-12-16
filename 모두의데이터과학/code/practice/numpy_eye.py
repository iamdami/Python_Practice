import numpy as np

noise1 = np.eye(4) + 0.01
print("noise1:")
print(noise1)

print("\n")

noise2 = np.eye(4) + 0.1 * np.ones((4, ))
print("noise2:")
print(noise2)

print("\n")

noise3 = np.eye(4) + 0.01 * np.random.random([4, 4])
noise3_rnd = np.round(noise3, 2)
print("noise3:")
print(noise3_rnd)
