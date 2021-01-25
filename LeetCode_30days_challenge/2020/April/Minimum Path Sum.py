def minPathSum(grid):
    dp = [[0]*len(grid[0]) for i in range(len(grid))]
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if row == 0:
                dp[row][column] = grid[row][column] + dp[row][column-1]
            elif column == 0:
                dp[row][column] = grid[row][column] + dp[row-1][column]
            else:
                dp[row][column] = grid[row][column] + min(dp[row][column-1], dp[row-1][column])
    return dp[-1][-1]


print(minPathSum([[1,3,1,],[1,5,1,],[4,2,1,]]))