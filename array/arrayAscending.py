# array 사용하기 위해 numpy import
import numpy as np


# 값 교환해주는 함수 정의
def swap(arr, x, y):
    temp = arr[x]  # 임시 저장소(temp)에 arr[x]값 넣어줌
    arr[x] = arr[y]  # arr[x]에 arr[y]값 넣어줌
    arr[y] = temp  # arr[y]에 임시 저장소(temp)값 넣어줌


# Bubble sort 오름차순 정렬 함수 정의
def ascendingSort(arr, N):  # 배열, 배열길이값
    n = N - 1  # 배열 길이값 - 1
    j = 0  # 1회전 할 때마다 카운트 해 줄 변수 초기화
    while (n):
        print("n: ", n)  # 연산 횟수
        temp = 0  # 누적 연산 값 저장될 변수
        for i in range(1, n + 1):
            # 첫 번째 값과 그 다음 값 비교
            if (arr[i - 1] > arr[i]):
                swap(arr, i - 1, i)  # swap함수
                temp = i  # for loop 수행될 때마다 값 저장
                j = j + 1  # 1회전 할 때마다 +1
            print(i, " ", arr)  # 값 비교 연산 횟수, 데이터 출력
        n = temp  # temp에 저장된 값과 n값 같으면
    print('Turns of changes: ', j)  # 총 회전 횟수 출력


# 파일 읽어오기
with open('C:/Users/Dami/Desktop/python/3.txt', 'r') as ascending:
    #  ascending이라는 이름으로 읽어옴(r)
    data = [int(float(i)) for i in ascending.read().split(',')]
    # ','를 구분자로 파일 토큰 분류한 값(float)을 int로 변환해 data에 저장

print("Original: ", data)  # data값 출력

arr = np.array(data)  # numpy.array 함수 사용해 배열 값 arr에 저장

ascendingSort(arr, len(arr))  # 배열에 대해 오름차순 정렬 수행
