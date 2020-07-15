class Solution:
    def countBits(self, num):
        if num == 0:
            return [0]
        elif num == 1:
            return [0, 1]
        else:
            dp = [0, 1]
            for i in range(2, num + 1):
                if i % 2 == 0:
                    dp.append(dp[i // 2])
                else:
                    dp.append(dp[i // 2] + 1)
            return dp
