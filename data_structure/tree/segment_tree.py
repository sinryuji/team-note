arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 실제로는 데이터의 개수 N에 4를 곱한 크기만큼 미리 세그먼트 트리의 공간을 할당한다.
tree = [0] * (len(arr) * 4)

# <세그먼트 트리를 배열의 각 구간 합으로 채워주기>
# start : 배열의 시작 인덱스, end : 배열의 마지막 인덱스
# index : 세그먼트 트리의 인덱스 (무조건 1부터 시작)
# 세그먼트 트리가 1부터 시작하는 이유는 2를 곱했을 때 왼쪽 자식노드를 가리키고
# 2를 곱하고 1을 더하면 오른쪽 자식노드를 가리키므로 효과적이기 때문에 이렇게 한다!
def init(start, end, idx):
    # 가장 끝에 도달했으면 arr 삽입
    if start == end:
        tree[idx] = arr[start]
        return tree[idx]
    mid = (start + end) // 2
    # 좌측 노드와 우측 노드를 채워주면서 부모 노드의 값도 채워준다.
    tree[idx] = init(start, mid, idx * 2) + init(mid + 1, end, idx * 2 + 1)
    return tree[idx]

# <구간 합을 구하는 함수>
# start : 시작 인덱스, end : 마지막 인덱스
# left, right : 구간 합을 구하고자 하는 범위
def find(start, end, idx, left, right):
    # 범위 밖에 있는 경우
    if left > end or right < start:
        return 0
    # 범위 안에 있는 경우
    if left <= start and right >= end:
        return tree[idx]
    # 그렇지 않다면 두 부분으로 나누어 합을 구하기
    mid = (start + end) // 2
    # start와 end가 변하면서 구간 합인 부분을 더해준다고 생각하면 된다.
    return find(start, mid, idx * 2, left, right) + find(mid + 1, end, idx * 2 + 1, left, right)

# <특정 원소의 값을 수정하는 함수(Top down)>
# 특정 원소를 수정하면 구간 합이 당연히 달라진다.
# 이때, 해당 원소를 포함하고 있는 모든 구간 합 노드들을 갱신해주면 된다.
# (즉, 전체가 아닌 부분적인 노드들만 바꿔주면 된다!)
# target : 구간 합을 수정하고자 하는 노드
# value : 수정할 값
def update_top_down(N, target, value):
    diff = value - arr[target]
    arr[target] = value
    update_tree_top_down(0, N - 1, 1, target, diff)

def update_tree_top_down(start, end, idx, target, diff):
    # 범위 밖에 있는 경우
    if target < start or target > end:
        return
    # 범위 안일 경우 차이 만큼 수정

    tree[idx] += diff
    if start == end:
        return
    mid = (start + end) // 2
    update_tree_top_down(start, mid, idx * 2, target, diff)
    update_tree_top_down(mid + 1, end, idx * 2 + 1, target, diff)

# <특정 원소의 값을 수정하는 함수(Bottom up)>
def update_bottom_up(start, end, idx, target, value):
    # 범위 밖에 있는 경우
    if target < start or target > end:
        return
    # 리프 노드를 만났을 경우
    if start == end:
        arr[target] = value
        tree[idx] = value
        return

    mid = (start + end) // 2
    update_bottom_up(start, mid, idx * 2, target, value)
    update_bottom_up(mid + 1, end, idx * 2 + 1, target, value)

    tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]


init(0, len(arr) - 1, 1)
print(tree)
print(find(0, len(arr) - 1, 1, 0, 9))  # 0부터 9까지의 구간 합 (1 + 2 + ... + 9 + 10)
print(find(0, len(arr) - 1, 1, 0, 2))  # 0부터 2까지의 구간 합 (1 + 2 + 3)
print(find(0, len(arr) - 1, 1, 6, 7))  # 0부터 2까지의 구간 합 (7 + 8)

# arr[0]을 5로 수정
update_top_down(len(arr), 0, 5)
print(find(0, len(arr) - 1, 1, 0, 2))   # 0부터 2까지의 구간 합 (5 + 2 + 3)

# arr[9]를 -1 수정
update_bottom_up(0, len(arr) - 1, 1, 9, -1)
update_top_down(len(arr), 9, -1)
print(find(0, len(arr) - 1, 1, 8, 9))   # 8부터 9까지의 구간 합 (9 + -1)
