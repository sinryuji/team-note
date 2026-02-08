def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser, equal, greater = [], [], []
    for num in arr:
        if num < pivot:
            lesser.append(num)
        elif num > pivot:
            greater.append(num)
        else:
            equal.append(num)
    return quick_sort(lesser) + equal + quick_sort(greater)

arr = [5, 3, 7, 2, 6, 10, 2, 9, 2, 7, 8, 4]
print(quick_sort(arr))
