def bubble_sort(arr):
    for i in range(1, len(arr)):
        for j in range(len(arr) - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [5, 3, 7, 6, 10, 9, 7, 8, 4]
bubble_sort(arr)
print(arr)