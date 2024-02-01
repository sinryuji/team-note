import sys

input = sys.stdin.readline

INF = int(1e9)
n, m = int(input()), int(input())
dist = [[INF] * n for _ in range(n)]

# 간선의 길이만큼 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a - 1][b - 1] = min(c, dist[a - 1][b - 1]) # 간선이 2개 이상일 수 있으므로 최소값으로 초기화

# 자기 자신은 0으로 초기화
for i in range(n):
    for j in range(n):
        if i == j:
            dist[i][j] = 0

# 각 노드를 한 번씩 중간 다리로 지정하며 거리를 계산
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
            
for line in dist:
    print(*[0 if x == INF else x for x in line])
