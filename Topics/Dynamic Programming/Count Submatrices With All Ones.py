# Time-complexity: O(N^2)*O(M)

class Solution:
    def numSubmat(self, matrix):
        result = 0
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if j == 0:
                    dp[i][j] = matrix[i][j]
                else:
                    if matrix[i][j] == 0:
                        dp[i][j] = 0  # no consecutive left zeroes starting from mat[i][j]
                    else:
                        dp[i][j] = dp[i][j-1]+1  # count consecutive left zeroes

        for j in range(m):  # from left to right
            for i in range(n):  # from top to bottom
                minimum = dp[i][j]
                for k in range(i, -1, -1):  # from i to top(count the number of rectangles that can be made)
                    minimum = min(minimum, dp[k][j])  # the number of rectangles that can be made with the right edge extended from mat[i][j] to mat[k][j]
                    if minimum == 0:
                        break
                    result += minimum
        return result
