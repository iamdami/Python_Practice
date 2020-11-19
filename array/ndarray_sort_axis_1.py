import numpy as np

# 2차원 배열 열 축 기준 정렬 (from left to right)
arr = np.array([[2, 1, 6],
                [0, 7, 4],
                [5, 3, 2]])  # 2차원 배열 정의

arr_sort_axis_1 = np.sort(arr, axis=1)
# 'axis = 1' 옵션 주면 열 축을 기준으로 좌에서 우로 정렬


print("열 축 기준 정렬\n", arr_sort_axis_1)
