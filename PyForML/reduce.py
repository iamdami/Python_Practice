from functools import reduce
print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))  # (((1+2)+3)+4)+5
# 15


# factorial
from functools import reduce
def factorial(n):
    return reduce(
            lambda x, y: x*y, range(1, n+1))


factorial(5)
# 120
