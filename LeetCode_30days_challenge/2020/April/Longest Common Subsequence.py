def longestCommonSubsequence(text1, text2):
    len1 = len(text1)
    len2 = len(text2)
    dp = [[None]*(len2+1) for i in range(len1+1)]
    for i in range(len1+1):
        for j in range(len2+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif text1[i-1] == text2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[len1][len2]

print(longestCommonSubsequence("ABD", "AD"))

