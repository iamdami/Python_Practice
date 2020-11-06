import numpy as np

org_array = np.array([3, 7, 2, 6])
print('원본 행렬:', org_array)

# np.sort()로 정렬
sort_array1 = np.sort(org_array)
print('np.sort() 호출 후 반환된 정렬 행렬 :', sort_array1)
print('np.sort() 호출 후 원본 행렬 :', org_array)

# ndarray.sort()로 정렬
sort_array2 = org_array.sort()
print('ndarray.sort() 호출 후 반환된 정렬 행렬 :', sort_array2)
print('ndarray.sort() 호출 후 원본 행렬 :', org_array)
