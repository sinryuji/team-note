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
        # 두 깊이의 차이가 2^i보다 크거나 같은 경우 b를 parent[b][i]로 업데이트를 하면 b가 2^i번째 조상으로 올라감 이 과정이 2^0, 그러니까 1까지 반복하므로 결국 둘의 깊이는 같아질수 밖에 없음.
        if depth[b] - depth[a] >= (1 << i):
            b = parent[b][i]

    if a == b:
        return a

    for i in range(LOG - 1, -1, -1):
        # 둘의 2^i 번째 부모가 같다는 것은 너무 큰 범위라 parent 배열에서 둘 다 0인 상태이거나 최소 공통 조상보다 위에 있어서 조상이 같은 경우임
        # 반대로 다르다는 것은 최소 공통 조상보다 아래 레벨의 조상이라는 것
        # 그 아래 레벨의 조상으로 업데이트를 해주는 과정을 2^0번째 조상. 그러니까 내 바로 위 조상까지 반복을 해주면 무조건 최소 공통 조상의 바로 아래 조상에 도달하게 됨.
        # 왜냐? 애초에 2^LOG가 노드의 총 개수보다 크도록 LOG를 설정해주기 때문. 그렇기 때문에 2^i로 조상을 건너뛰어 올라가다보면 최소 공통 조상까지 도달하지 못하는 케이스는 없음.
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
