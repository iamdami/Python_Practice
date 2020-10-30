import numpy as np

def swap(arr, x, y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp
    
    
def ascendingSort(arr, N):
    # Print the original saved value
    print("Original arr: ", arr)
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

            # Perform comparison of values within array elements
            if (arr[i - 1] > arr[i]):
                swap(arr, i - 1, i)
                temp = i
                j = j + 1
                # Print the Value comparison operation count and the data
            print(i, " ", arr)
        n = temp
    # Print the Total conversion count
    print('Total numbers of changes: ', j)


with open('PutFileName.txt', 'r') as ascending:
    arr = [int(float(i)) for i in ascending.read().split(',')]

a = np.array(arr)

print("original: ",arr)

ascendingSort(arr, len(arr))
