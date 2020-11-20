import numpy as np

arr = np.array([[3, 2, 4], [5, 0, 1]])
print("호출 전 원래 값\n", arr)
arr_reverse = arr[::-1].sort()  # ndarray 내림차순 정렬
print("호출 후 내림차순 정렬한 값\n", arr_reverse)
print("호출 전 원래 값\n", arr)
