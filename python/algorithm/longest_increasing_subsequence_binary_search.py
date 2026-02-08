from bisect import bisect_left

N = int(input())
nums = list(map(int, input().split()))
s = [nums[0]]
dp = [(0, s[0])]

for i in nums[1:]:
    if i > s[-1]:
        dp.append((len(s), i))
        s.append(i)
    else:
        idx = bisect_left(s, i)
        s[idx] = i
        dp.append((idx, i))

subsequence = []
cur = len(s) - 1
for i, v in dp[::-1]:
    if i == cur:
        subsequence.append(v)
        cur -= 1

print(len(s))
print(*subsequence[::-1])
