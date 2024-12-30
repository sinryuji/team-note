import math, time, sys
sys.setrecursionlimit(10 ** 6)

def recursion_factorial(n):
    if n < 2:
        return 1
    return n * recursion_factorial(n - 1)

def loop_factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

n = int(input())

start = time.time()
recursion_factorial(n)
print(f'custom recursion factorial: {time.time() - start:.5f} sec')

start = time.time()
loop_factorial(n)
print(f'custom loop factorial: {time.time() - start:.5f} sec')

start = time.time()
math.factorial(n)
print(f'math factorial: {time.time() - start:.5f} sec')
