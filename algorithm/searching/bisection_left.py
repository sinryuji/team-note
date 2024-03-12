def bisection_left(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


list = [1, 2, 2, 2, 2, 3, 4]

print(bisection_left(list, 2))
