import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (distance[start], start))
    while q:
        dist, curr = heapq.heappop(q)
        if visited[curr]:
            continue
        visited[curr] = True
        for next_ in graph[curr]:
            cost = dist + next_[1]
            if distance[next_[0]] > cost:
                distance[next_[0]] = cost
                heapq.heappush(q, (cost, next_[0]))


dijkstra(start)

for i in range(1, n + 1):
    if i == INF:
        print("INFINITY")
    else:
        print(distance[i])
