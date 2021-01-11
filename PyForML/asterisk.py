def asterisk_test(a, *args):
    print(a, args)  # 1 (2, 3, 4, 5, 6)
    print(type(args))  # <class 'tuple'>

asterisk_test(1,2,3,4,5,6)


def asterisk_test(a, **kargs):
    print(a, kargs)  # 1 {'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
    print(type(kargs))  # <class 'dict'>

asterisk_test(1, b=2, c=3, d=4, e=5, f=6)
# In the example, 1 goes into a and the rest goes into kargs as a dict type


def asterisk_test(a, *args):
    print(a, args[0])  # 1 (2, 3, 4, 5, 6)
    print(type(args))  # <class 'tuple'>

asterisk_test(1, (2, 3, 4, 5, 6))
# Since (2, 3, 4, 5, 6) is a tuple, args[0]


def asterisk_test(a, args):
    print(a, *args)  # 1 2 3 4 5 6
    print(type(args))  # <class 'tuple'>

asterisk_test(1, (2,3,4,5,6))
# *args: unpacking


a, b, c = ([1, 2], [3, 4], [5, 6])
print(a, b, c)  # [1, 2] [3, 4] [5, 6]

data = ([1, 2], [3, 4], [5, 6])
print(*data)  # [1, 2] [3, 4] [5, 6]
# *data: unpacking


for data in zip(*([1, 2], [3, 4], [5, 6])):
    print(sum(data))  # 1+3+5=9
    
    
def asterisk_test(a, b, c, d, e=0):
    print(a, b, c, d, e)  # 10 3 2 1 56


data = {"d": 1, "c": 2, "b": 3, "e": 56}
asterisk_test(10, **data)    
# **: Keyword argument
# goes into dict type
# At the same time !
