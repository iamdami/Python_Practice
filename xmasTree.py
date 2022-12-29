import colorama
import random

colors = list(vars(colorama.Fore).values())
# print(colors)
c = 10
for i in range(0, c):
    if i == 0:  # top deco
        txt = ' ' * int(c - i) + colorama.Fore.WHITE + '*' * (2 * i + 1)
        print(''.join(txt))
    else:  # the others
        txt = ' ' * int(c - i) + '*' * (2 * i + 1)
        colored_chars = [random.choice(colors) + char for char in txt]
        print(''.join(colored_chars))

# tree btm
for j in range(0, round(c / 3)):
    txt2 = ' ' * int((2 * c - 1) / 2 - 1) + colorama.Fore.BLACK + '|' * (5)
    print(''.join(txt2))