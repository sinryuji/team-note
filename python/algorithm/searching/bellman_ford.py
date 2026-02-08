import sys

input = sys.stdin.readline
INF = int(1e9)

def bellman_ford(start):
    distance[start] = 0
    for i in range(V):
        for j in range(E):
            cur = edges[j][0]
            nxt = edges[j][1]
            cost = edges[j][2]
            if distance[cur] != INF and distance[cur] + cost < distance[nxt]:
                distance[nxt] = distance[cur] + cost
                if i == V - 1:
                    return True
    return False


V, E = map(int, input().split())
edges = []
distance = [INF] * (V + 1)

for _ in range(E):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))


negative_cycle = bellman_ford(1)
if negative_cycle:
    print('-1')
else:
    for i in range(2, V + 1):
        if distance[i] == INF:
            print("-1")
        else:
            print(distance[i])
