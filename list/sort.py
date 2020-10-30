# Sort Ascending of 1D array

# Define a function to exchange values
def swap(list, x, y):
    temp = list[x]
    list[x] = list[y]
    list[y] = temp


# Define ascending sort function
def ascendingSort(list, N):
    # Print the original saved value
    print("Original list: ", list)
    n = N - 1
    # Initialize count value
    count = 0
    j = 0
    while (n):
        # Number of operations
        print("n: ", n)
        # Variable to store the accumulated operation value
        temp = 0
        for i in range(1, n + 1):

            # Compare values within list elements
            if (list[i - 1] > list[i]):
                swap(list, i - 1, i)
                temp = i
                j = j + 1
                # Print the value comparison operation count and the data
            print(i, " ", list)
        n = temp
    # Pritn the total conversion count
    print('Total numbers of changes: ', j)


# read file
with open('C:/Users/Dami/Desktop/python/3.txt', 'r') as ascending:
    # Read data value based on comma and save it in list
    list = [int(float(i)) for i in ascending.read().split(',')]
    
# ascending sort function
ascendingSort(list, len(list))
