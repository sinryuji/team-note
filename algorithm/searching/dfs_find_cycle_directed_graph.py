def dfs(node):
    global is_cycle
    visited[node] = True
    for nxt in graph[node]:
        if not visited[nxt]:
            dfs(nxt)
        elif not finished[nxt]:
            is_cycle = True


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [False] * (n + 1)
finished = [False] * (n + 1)
cycle_cnt = 0
for i in range(1, n + 1):
    if not visited[i]:
        is_cycle = False
        dfs(i)
        if is_cycle:
            cycle_cnt += 1
