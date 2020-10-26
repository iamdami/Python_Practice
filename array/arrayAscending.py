import numpy as np

def swap(arr, x, y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp
    
    
def ascendingSort(arr, N):
    # 원래 저장되어 있던 값 출력
    print("Original arr: ", arr)
    n = N - 1
    # 카운트 값 초기화
    count = 0
    j = 0
    while (n):
        # 연산 횟수
        print("n: ", n)
        # 누적 연산 값 저장될 변수
        temp = 0
        for i in range(1, n + 1):

            # 배열 원소 내 값 비교 수행
            if (arr[i - 1] > arr[i]):
                swap(arr, i - 1, i)
                temp = i
                j = j + 1
                # 값 비교 연산 횟수와 데이터 출력
            print(i, " ", arr)
        n = temp
    # 총 변환 횟수 출력
    print('Total numbers of changes: ', j)


with open('C:/Users/Dami/Desktop/python/3.txt', 'r') as ascending:
    arr = [int(float(i)) for i in ascending.read().split(',')]

a = np.array(arr)

print("original: ",arr)

ascendingSort(arr, len(arr))
