def lcs(string_A, string_B):
    dp = [[0] * (len(string_B) + 1) for _ in range(len(string_A) + 1)]

    for i in range(1, len(string_A) + 1):
        for j in range(1, len(string_B) + 1):
            if string_A[i - 1] == string_B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    res = ''
    i, j = len(string_A), len(string_B)
    while dp[i][j] > 0:
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j - 1]:
            j -= 1
        else:
            i -= 1
            j -= 1
            res += string_A[i]

    return res[::-1]


print(lcs('GBCDFE', 'ABCDEF'))
