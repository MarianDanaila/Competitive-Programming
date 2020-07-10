def change(amount, coins):
    dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
    dp[0][0] = 1
    for i in range(1, len(coins) + 1):
        dp[i][0] = 1  # number ways of selecting for amount zero is 1
        for j in range(1, amount + 1):
            dp[i][j] = dp[i-1][j]  # exclude current coin
            if j - coins[i-1] >= 0:  # check if amount >= to the current i` th coin
                dp[i][j] += dp[i][j-coins[i-1]]  # include current coin
    return dp[-1][-1]


print(change(5, [1, 2, 3]))