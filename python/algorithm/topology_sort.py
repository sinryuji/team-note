# 위상 정렬 알고리즘
# 큐를 사용하는 위상 정렬
# 진입차수가 0인 모든 노드를 큐에 넣는다
# 큐가 빌 때까지 다음 과정을 반복한다
# 1. 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거한다
# 2. 새롭게 진입차수가 0이 된 노를 큐에 넣는다
# - 진입차수(Indegree): 특정한 노드로 들어오는 간선의 개수
# - 진출차수(Outdegree): 특정한 노드에서 나가는 간선의 개수
# 입력 예시
# 7 8
# 1 2
# 1 5
# 2 3
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4
# 출력 예시
# 1 2 5 3 6 4 7

from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for n in graph[now]:
            indegree[n] -= 1
            if indegree[n] == 0:
                q.append(n)

    print(*result)

topology_sort()