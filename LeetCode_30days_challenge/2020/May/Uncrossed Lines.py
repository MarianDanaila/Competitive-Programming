def maxUncrossedLines(a, b) -> int:
    dp = [[None] * (len(b) + 1) for i in range(len(a) + 1)]
    print(dp)
    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif a[i - 1] == b[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    print(dp)
    return dp[-1][-1]

print(maxUncrossedLines([1,3], [1,2]))