a = [1, 2, 3, 4, 5]
fun = lambda x: x ** 2
print(list(map(fun, a)))
# [1, 4, 9, 16, 25]


a = [1, 2, 3, 4, 5]
fun = lambda x, y: x + y
print(list(map(fun, a, a)))
# [2, 4, 6, 8, 10]


a = [1, 2, 3, 4, 5]
print(list(map(
    lambda x: x ** 2 if x % 2 == 0 else x,
    a)))
# [1, 4, 3, 16, 5]


# From Python 3, you must add 'list' before the map function
a = [1,2,3,4,5]
print(list(map(lambda x: x+x, a)))  # [2, 4, 6, 8, 10]
print((map(lambda x: x+x, a)))  # <map object at 0x00000239631301C0>


a = [1, 2, 3, 4, 5]
fun = lambda x: x ** 2
print(map(fun, a))  # <map object at 0x0000018B19E30340>
for i in map(fun, a):
    print(i)
# 1
# 4
# 9
# 16
# 25   

result = map(fun, a)
print(result)  # <map object at 0x0000018271C00340>
print(next(result))  # 1
