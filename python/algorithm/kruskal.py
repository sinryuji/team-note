import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

V, E = map(int, input().split())
edges = []
for _ in range(E):
    edges.append(tuple(map(int, input().split())))

parent = [i for i in range(V + 1)]
edges.sort(key=lambda x : x[2])
ans = 0
cnt = 0

for a, b, dist in edges:
    if find(a) != find(b):
        union(a, b)
        ans += dist

    if cnt == V:
        break

print(ans)