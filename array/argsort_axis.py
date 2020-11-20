import numpy as np

org_array = np.array([2, 1, 0, 7])
ndarr = np.array([[2, 1, 0, 7], [5, 8, 4, 3]])
print('1차원 배열 원본 :\n', org_array)
print('다차원 배열 원본 :\n', ndarr)

print("1Darr_axis=-1\n", np.argsort(org_array, axis=-1))
print("1Darr_axis=0\n", np.argsort(org_array, axis=0))


print("NDarr_axis=-1\n", np.argsort(ndarr, axis=-1))
print("NDarr_axis=0\n", np.argsort(ndarr, axis=0))
print("NDarr_axis=1\n", np.argsort(ndarr, axis=1))
