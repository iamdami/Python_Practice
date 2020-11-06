# numpy import
import numpy as np

# 파일 읽어오기
with open('C:/putFileName.txt', 'r') as ascending:
    # ascending이라는 이름으로 읽어옴(r)
    data = [int(float(i)) for i in ascending.read().split(',')]
    # ','를 구분자로 파일 토큰 분류한 값(float)을 int로 변환해 data에 저장

print("Original array: ", data)  # data값 출력
arr = np.array(data)  # numpy.array 함수 사용해 배열 값 arr에 저장

s = np.sort(arr)  # np.sort 함수 이용해 정렬한 값 변수 s에 넣어줌
print("After sort: ", s)  # 정렬한 값 출력
