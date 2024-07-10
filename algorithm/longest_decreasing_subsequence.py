N = int(input())
nums = list(map(int, input().split()))
dp = [1] * N

for i in range(N):
    for j in range(i):
        if nums[i] < nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)

subsequence = []
cur = max(dp)
for i in range(N-1, -1, -1):
    if dp[i] == cur:
        subsequence.append(nums[i])
        cur -= 1

print(max(dp))
print(*subsequence[::-1])