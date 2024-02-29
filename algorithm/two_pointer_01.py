# 앞과 끝에서 시작하는 투포인터.
# 두 포인터의 합을 구할 때 효과적.
# 중복된 수가 없어야 하고 수열이 정렬되어 있어야 함.
# 수열에서 목표 합계가 되는 두 수를 구하는 코드.

import sys
input = sys.stdin.readline

def solution():
    arr = [3, 9, 25, 22, 1, 6, 5, 11, 19, 28, 17, 12, 16] # 중복수가 없고 정렬되지 않은 배열
    S = 27 # 목표 합계
    arr.sort()
    start, end = 0, len(arr) - 1

    while start != end:
        s = arr[start] + arr[end]
        if s > S:
            end -= 1
        elif s < S:
            start += 1
        else:
            print(start + 1, '번째 수 (', arr[start], ') + ', end, '번째 수 (', arr[end], ')')
            start += 1
            end -= 1


if __name__ == '__main__':
    solution()