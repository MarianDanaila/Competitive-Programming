class Solution:
    def calculateMinimumHP(self, dungeon):
        n = len(dungeon)
        m = len(dungeon[0])
        dp = [[float("inf")] * m for _ in range(n)]

        def recursive(i, j):
            if i == n or j == m:
                return float('inf')

            if i == n - 1 and j == m - 1:
                if dungeon[i][j] <= 0:
                    return -dungeon[i][j] + 1
                else:
                    return 1

            if dp[i][j] != float("inf"):
                return dp[i][j]

            right = recursive(i, j + 1)
            down = recursive(i + 1, j)
            min_health_required = min(right, down) - dungeon[i][j]
            if min_health_required <= 0:
                dp[i][j] = 1
            else:
                dp[i][j] = min_health_required
            return dp[i][j]

        return recursive(dungeon, dp)
