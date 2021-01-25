def maximalSquare(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    prev = 0
    dp = [0] * columns
    maxim = 0
    for i in range(1, rows+1):
        for j in range(1, columns+1):
            temp = dp[j]
            if matrix[i-1][j-1] == '1':
                dp[j] = min(dp[j-1], prev, dp[j])+1
                maxim = max(maxim, dp[j])
            else:
                dp[j] = 0
            prev = temp
    return maxim * maxim