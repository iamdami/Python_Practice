# Unpacking index and value in list
for i, v in enumerate(['tic', 'tac', 'tok']):
    print(i, v)
# 0 tic
# 1 tac
# 2 tok


# Unpacking the index and value in the list and saving it as a list
mylist = ['a', 'b', 'c', 'd']
print(list(enumerate(mylist)))    
# [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]


# Make a sentence into a list, unpack the list index and value, and save it as a dict
print({i:j for i, j in enumerate("Cat is the cutiest animal in the world.".split())})
# {0: 'Cat', 1: 'is', 2: 'the', 3: 'cutiest', 4: 'animal', 5: 'in', 6: 'the', 7: 'world.'}
