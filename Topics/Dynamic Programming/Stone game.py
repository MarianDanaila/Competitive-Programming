class Solution:
    def stoneGame(self, p):
        n = len(p)
        dp = [[0] * n for i in range(n)]
        for i in range(n):
            dp[i][i] = p[i]
        print(dp)
        for d in range(1, n):
            for i in range(n - d):
                dp[i][i + d] = max(p[i] - dp[i + 1][i + d], p[i + d] - dp[i][i + d - 1])
                print(dp)
        #print(dp)
        return dp[0][-1] > 0


solution = Solution()
print(solution.stoneGame([5, 3, 4, 5]))


