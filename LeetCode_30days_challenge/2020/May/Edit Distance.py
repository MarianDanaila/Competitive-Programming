def minDistance(word1, word2):
    dp = [[None] * (len(word2) + 1) for i in range(len(word1) + 1)]
    rem1 = -1
    rem2 = -1
    op = 0
    for i in range(len(word1) + 1):
        for j in range(len(word2) + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif word1[i-1] == word2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(dp)
    cnt = 1
    max_cnt = 0
    for i in range(1, len(dp[-1])):
        if dp[-1][i] == dp[-1][i-1]:
           cnt += 1
        else:
            if cnt != 1:
                max_cnt += cnt
            cnt = 1
    return 1 + max_cnt


print(minDistance("intention", "execution"))