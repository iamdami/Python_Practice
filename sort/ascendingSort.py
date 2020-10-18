def swap(arr, x, y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp


def ascendingSort(arr, N):
    print("Original array: ", arr)
    n = N - 1
    count = 0
    j = 0
    while (n):
        print("n: ", n)
        temp = 0
        for i in range(1, n + 1):

            if (arr[i - 1] > arr[i]):
                swap(arr, i - 1, i)
                temp = i
                j = j + 1
            print(i, " ", arr)
        n = temp
    print('Total numbers of changes: ', j)


with open('C:/newFile.txt', 'r') as ascending:
    arr = [int(float(i)) for i in ascending.read().split('\n')]
ascendingSort(arr, len(arr))
