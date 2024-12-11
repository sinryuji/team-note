# input
# 10 4
# 75
# 30
# 100
# 38
# 50
# 51
# 52
# 20
# 81
# 5
# 1 10
# 3 5
# 6 9
# 8 10

# output
# 5
# 38
# 20
# 5

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

h = [0] * (N + 1)
h[1] = 0
for i in range(2, N + 1):
    h[i] = h[i >> 1] + 1

table = [[-1] * N for _ in range(h[-1] + 1)]
for i in range(N):
    table[0][i] = arr[i]

step = 1
for i in range(1, h[-1] + 1):
    for j in range(N - step):
        table[i][j] = min(table[i-1][j], table[i-1][j+step])
    step <<= 1

def query(left, right):
    row = h[right - left + 1]
    return min(table[row][left], table[row][right + 1 - (1 << row)])

for _ in range(M):
    a, b = map(int, input().split())
    print(query(a - 1, b - 1))
