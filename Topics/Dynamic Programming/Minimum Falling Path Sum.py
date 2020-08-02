# Approach 1 using an auxiliary array
# Time-complexity: O(N^2) where N is length of a
# Space-complexity: O(N^2)
class Solution:
    def minFallingPathSum(self, a):
        dp = [[0] * (len(a)) for _ in range(len(a))]
        for i in range(len(a)):
            for j in range(len(a)):
                if i == 0:
                    dp[i][j] = a[i][j]
                else:
                    if j == 0:
                        dp[i][j] = a[i][j] + min(dp[i-1][j], dp[i-1][j+1])
                    elif j == len(a) - 1:
                        dp[i][j] = a[i][j] + min(dp[i-1][j-1], dp[i-1][j])
                    else:
                        dp[i][j] = a[i][j] + min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])
        return min(dp[-1])

# Approach 2 without using an auxiliary array
# Time-complexity: O(N^2) where N is lenght of a
# Space-complexity: O(1)
class Solution:
    def minFallingPathSum(self, a):
        for i in range(1, len(a)):
            for j in range(len(a)):
                if j == 0:
                    a[i][j] += min(a[i-1][j], a[i-1][j+1])
                elif j == len(a)-1:
                    a[i][j] += min(a[i-1][j-1], a[i-1][j])
                else:
                    a[i][j] += min(a[i-1][j-1], a[i-1][j], a[i-1][j+1])
        return min(a[-1])

sol = Solution()
print(sol.minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))