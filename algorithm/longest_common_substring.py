def lcs(string_A, string_B):
    dp = [[0] * (len(string_B) + 1) for _ in range(len(string_A) + 1)]

    m, mi, mj = 0, 0, 0
    for i in range(1, len(string_A) + 1):
        for j in range(1, len(string_B) + 1):
            if string_A[i - 1] == string_B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > m:
                    m, mi, mj = dp[i][j], i, j

    res = ''
    while dp[mi][mj] != 0:
        res += string_A[mi-1]
        mi -= 1
        mj -= 1

    return res[::-1]



print(lcs('AABCDEF', 'GBCDFE'))
