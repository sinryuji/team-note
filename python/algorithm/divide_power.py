def divide_power(a, b):
    if b == 0:
        return 1
    x = divide_power(a, b // 2)
    if b % 2 == 0:
        return x * x
    else:
        return x * x * a

a, b = map(int, input().split())
print(divide_power(a, b))
