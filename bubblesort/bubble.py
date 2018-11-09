def bubble_sort(arr):
    for num in range(len(arr) - 1, 0, -1):
        for i in range(num):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp


arr = [11, 56, 23, 26, 4, 99, 55, 48, 56, 24, 36]

bubble_sort(arr)

print(arr)
