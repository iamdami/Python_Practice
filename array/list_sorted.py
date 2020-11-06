# file read
with open('C:/Users/Dami/Desktop/python/3.txt', 'r') as ascending:
    #  ascending이라는 이름으로 읽어옴(r)
    list = [int(float(i)) for i in ascending.read().split(',')]
    # ','를 구분자로 파일 토큰 분류한 값(float)을 int로 변환해 list에 저장

print("Original list: ", list)  #list값 출력

# 정렬
s = sorted(list)  # sorted() 함수 이용해 정렬한 값 변수 s에 넣어줌

print("After sort: ", s)  # 정렬 값 출력
# 원본 값은 그대로, 정렬 값 반환
