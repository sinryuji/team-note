# input
# 15
# 1 2
# 1 3
# 2 4
# 3 7
# 6 2
# 3 8
# 4 9
# 2 5
# 5 11
# 7 13
# 10 4
# 11 15
# 12 5
# 14 7
# 6
# 6 11
# 10 9
# 2 6
# 7 6
# 8 13
# 8 15

# output
# 2
# 4
# 2
# 1
# 3
# 1

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
LOG = 17


def dfs(x, d):
    visited[x] = True
    depth[x] = d
    for nxt in tree[x]:
        if not visited[nxt]:
            parent[nxt][0] = x
            dfs(nxt, d + 1)


def lca(a, b):
    if depth[a] > depth[b]:
            a, b = b, a

    for i in range(LOG - 1, -1, -1):
        if depth[b] - depth[a] >= (1 << i):
            b = parent[b][i]

    if a == b:
        return a

    for i in range(LOG - 1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    return parent[a][0]


N = int(input())
tree = [[] for _ in range(N + 1)]
parent = [[0] * LOG for _ in range(N + 1)]
depth = [0] * (N + 1)
visited = [False] * (N + 1)
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(1, 0)
for i in range(1, LOG):
    for j in range(1, N + 1):
        parent[j][i] = parent[parent[j][i - 1]][i - 1]

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(lca(a, b))
