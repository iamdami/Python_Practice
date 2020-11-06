# 파일 읽기
with open('C:/Users/Dami/Desktop/python/3.txt', 'r') as even:
    #  even이라는 이름으로 읽어옴(r)
    list = [int(float(i)) for i in even.read().split(',')]
    # ','를 구분자로 파일 토큰 분류한 값(float)을 int로 변환해 list에 저장

# 원래 저장되어 있던 리스트 출력
print("Original list: ", list)

# 리스트 원소 중 짝수인 원소만 출력
for i in list:
    if i % 2 == 0:
        print(i)


