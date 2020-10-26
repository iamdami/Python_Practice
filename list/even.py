with open('C:/even.txt', 'r') as even:
    list = [int(float(i)) for i in even.read().split(',')]

print("Original list: ", list)

for i in list:
    if i % 2 == 0:
        print(i)
