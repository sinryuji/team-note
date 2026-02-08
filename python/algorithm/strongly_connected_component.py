# input
# 7 9
# 1 4
# 4 5
# 5 1
# 1 6
# 6 7
# 2 7
# 7 3
# 3 7
# 7 2

# output
# 3
# 1 4 5 -1
# 2 3 7 -1
# 6 -1

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(node):
    global id_
    result = id_
    node_ids[node] = id_
    id_ += 1
    stack.append(node)

    for nxt in graph[node]:
        if node_ids[nxt] == 0:
            result = min(result, dfs(nxt))
        elif not finished[nxt]:
            result = min(result, node_ids[nxt])

    if result == node_ids[node]:
        tmp = []
        while True:
            t = stack.pop()
            tmp.append(t)
            finished[t] = True
            if t == node:
                break

        tmp.sort()
        scc.append(tmp)

    return result


V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    A, B = map(int, input().split())
    graph[A].append(B)

node_ids = [0] * (V + 1)
finished = [False] * (V + 1)
stack = []
id_ = 1
scc = []

for i in range(1, V + 1):
    if node_ids[i] == 0:
        dfs(i)

scc.sort(key=lambda x: x[0])
print(len(scc))
for s in scc:
    print(*s, -1)
