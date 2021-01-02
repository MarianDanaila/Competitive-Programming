class Solution:
    def cherryPickup(self, grid):
        n = len(grid)
        m = len(grid[0])
        dp = [[[0] * m for _ in range(m)] for _ in range(n)]
        for row in range(n - 1, -1, -1):
            for col1 in range(m):
                for col2 in range(m):
                    if col1 == col2:
                        cherries = grid[row][col1]
                    else:
                        cherries = grid[row][col1] + grid[row][col2]

                    if row == n - 1:
                        dp[row][col1][col2] = cherries
                    else:
                        best = 0
                        for i in [-1, 0, 1]:
                            for j in [-1, 0, 1]:
                                if 0 <= col1 + i <= m - 1 and 0 <= col2 + j <= m - 1:
                                    best = max(best, dp[row + 1][col1 + i][col2 + j])
                        dp[row][col1][col2] = best + cherries
        return dp[0][0][m - 1]
