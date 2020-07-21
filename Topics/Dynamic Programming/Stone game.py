class Solution:
    def stoneGame(self, p):
        n = len(p)
        dp = [[0] * n for i in range(n)]
        for i in range(n):
            dp[i][i] = p[i]
        #print(dp)
        for i in range(1, n):
            for j in range(n - i):
                dp[j][j + i] = max(p[j] - dp[j + 1][j + i], p[j + i] - dp[j][j + i - 1])
                print(dp)
        #print(dp)
        return dp[0][-1] > 0


#solution = Solution()
#print(solution.stoneGame([5, 3, 4, 5]))

# Another type of solution (EASIER TO UNDERSTAND)

class Solution2:
    def stoneGame(self, piles):
        n = len(piles)
        dp = [[0] * n for i in range(n)]
        for i in range(n):
            dp[i][i] = [piles[i], 0]

        k = 1
        while k < n:
            i = 0
            while i+k < n:
                j = i + k
                # piles[i.....j]

                # score if Alex picks piles[i]
                pickLeftScore = piles[i] + dp[i+1][j][1]
                
                # score if Alex picks piles[j]
                pickRightScore = piles[j] + dp[i][j-1][1]
                
                if pickLeftScore > pickRightScore:
                    leeScore = dp[i+1][j][0]
                    dp[i][j] = [pickLeftScore, leeScore]
                else:
                    leeScore = dp[i][j-1][0]
                    dp[i][j] = [pickRightScore, leeScore]
                i += 1
            k += 1

        return dp[0][n-1][0] > dp[0][n-1][1]
   

sol = Solution2()
print(sol.stoneGame([3, 9, 1, 2]))


