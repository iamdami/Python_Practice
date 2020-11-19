import numpy as np

# 2차원 배열 행 축 기준 정렬 (from top to bottom)
arr = np.array([[2, 1, 6],
                [0, 7, 4],
                [5, 3, 2]])  # 2차원 배열 정의

arr_sort_axis_0 = np.sort(arr, axis=0)
# 'axis = 0' 옵션 주면 행 축을 기준으로 위에서 아래로 정렬


print("행 축 기준 정렬\n", arr_sort_axis_0)
