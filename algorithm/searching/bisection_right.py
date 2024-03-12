def bisection_right(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return right


list = [1, 2, 2, 2, 2, 3, 4]

print(bisection_right(list, 2))
