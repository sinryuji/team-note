import sys

input = sys.stdin.readline

INF = int(1e9)
n, m = int(input()), int(input())
dist = [[INF] * n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    if dist[a - 1][b - 1] > c:
        dist[a - 1][b - 1] = c

for i in range(n):
    for j in range(n):
        if i == j:
            dist[i][j] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for line in dist:
    print(*[0 if x == INF else x for x in line])
