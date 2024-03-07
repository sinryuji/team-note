# 경로 압축 find
def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

# 일반 find
# def find(x):
#     if parent[x] == x:
#         return x
#     else:
#         return find(parent[x])

# 일반 union
# def union(a, b):
#     a = find(a)
#     b = find(b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# union by rank(트리를 합칠 때 높이가 작은 트리를 큰 트리의 루트에 붙이는 방법)
def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    # 만약 랭크 a가 랭크 b보다 높거나 같으면
    if rank[a] > rank[b]:
        parent[b] = a # 트리 b를 트리 a의 루트에 붙인다
    elif rank[a] < rank[b]: # 만약 랭크 b가 랭크 a보다 높다면
        parent[a] = b # 트리 a를 트리 b의 루트에 붙인다
    else: # 만약 둘의 랭크가 같다면
        rank[b] += 1 # 랭크 b를 1 높인 뒤
        parent[a] = b # 트리 a를 트리 b의 루트에 붙인다

v, e = map(int, input().split())

# 부모 테이블 초기화
parent = [i for i in range(v + 1)]

# union by rank
rank = [0] * (v + 1)

# Union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union(a, b)

# 각 원소가 속한 집합 출력하기
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find(i), end=' ')

print()

# 부모 테이블 내용 출력하기
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')