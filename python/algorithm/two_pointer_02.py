# 맨 앞 쪽에서 두 개의 포인터가 출발하는 투포인터.
# 부분합을 구할때 효과적.
# 입력된 수열에서 부분합이 M인 부분 수열의 개수를 구하는 코드.

import sys

input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    left, right = 0, 0
    ans, s = 0, 0

    for left in range(N):
        while s < M and right < N:
            s += nums[right]
            right += 1
        if s == M:
            ans += 1
        s -= nums[left]

    print(ans)


if __name__ == '__main__':
    solution()
