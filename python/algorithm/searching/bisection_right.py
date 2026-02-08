def bisection_right(array, target):
    left, right = 0, len(array)
    while left < right:
        mid = (left + right) // 2
        if array[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left


list = [1, 2, 2, 2, 2, 3, 4]

print(bisection_right(list, 2))
print(bisection_right(list, 5))
