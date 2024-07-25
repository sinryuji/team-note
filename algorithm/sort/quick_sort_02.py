def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
    arr[right], arr[pivot] = arr[pivot], arr[right]

    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)

arr = [5, 3, 7, 2, 6, 10, 2, 9, 2, 7, 8, 4]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
