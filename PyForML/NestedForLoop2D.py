case_1 = ["A", "B", "C"]
case_2 = ["D", "E", "F"]

result = [a+b for a in case_1 for b in case_2]
print(result)
# ['AD', 'AE', 'AF', 'BD', 'BE', 'BF', 'CD', 'CE', 'CF']


result = [[a+b for a in case_1] for b in case_2]
print(result)
# [['AD', 'BD', 'CD'], ['AE', 'BE', 'CE'], ['AF', 'BF', 'CF']]
