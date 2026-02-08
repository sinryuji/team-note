# input
# 1000000 30000
#
# output
# basic operator power: 0.03494 sec
# loop power: 0.53234 sec
# recursion power: 0.52792 sec
# divide power: 0.01465 sec
#
# result
# divide > basic operator >>> loop = recursion

import time, sys
sys.setrecursionlimit(10 ** 6)

a, b = map(int, input().split())

def loop_power(a, b):
    result = 1
    for _ in range(b):
        result *= a
    return result

def recursion_power(a, b):
    if b == 1:
        return a
    return recursion_power(a, b - 1) * a

def divide_power(a, b):
    if b == 0:
        return 1
    x = divide_power(a, b // 2)
    if b % 2 == 0:
        return x * x
    else:
        return x * x * a

start = time.time()
tmp = a ** b
print(f'basic operator power: {time.time() - start:.5f} sec')

start = time.time()
tmp = loop_power(a, b)
print(f'loop power: {time.time() - start:.5f} sec')

start = time.time()
tmp = recursion_power(a, b)
print(f'recursion power: {time.time() - start:.5f} sec')

start = time.time()
tmp = divide_power(a, b)
print(f'divide power: {time.time() - start:.5f} sec')
