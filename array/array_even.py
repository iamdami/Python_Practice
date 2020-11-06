# array 사용 위해 numpy import
import numpy as np

# 파일 읽어오기
with open('C:/Users/Dami/Desktop/python/3.txt', 'r') as even:
    #  even이라는 이름으로 읽어옴(r)
    data = [int(float(i)) for i in even.read().split(',')]
    # ','를 구분자로 파일 토큰 분류한 값(float)을 int로 변환해 data에 저장

# 읽어온 배열 값 출력
print("original: ", data)

arr = np.array(data)

# 배열 원소 중 짝수인 원소만 출력
for i in arr:
    if i % 2 == 0:
        print(i)
