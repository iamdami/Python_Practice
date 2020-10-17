
with open('C:newFile.txt', 'r') as calc:
    data = [float(i) for i in calc.read().split('\n')]


a = data[0]
b = data[1]


# adds two numbers
def add(a, b):
    return a + b


# subtracts two numbers
def subtract(a, b):
    return a - b


# multiplies two numbers
def multiply(a, b):
    return a * b


# divides two numbers
def divide(a, b):
    return a / b


result1 = add(a, b)
result2 = subtract(a, b)
result3 = multiply(a, b)
result4 = divide(a, b)


print(a, "+", b, "=", result1)
print(a, "-", b, "=", result2)
print(a, "*", b, "=", result3)
print(a, "/", b, "=", result4)
