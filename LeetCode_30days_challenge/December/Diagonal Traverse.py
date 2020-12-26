class Solution:
    def findDiagonalOrder(self, matrix):
        if not matrix:
            return []
        n = len(matrix)
        m = len(matrix[0])
        ans = []
        k = 0
        while len(ans) < m*n:
            if k % 2 == 0:
                i = min(k, n-1)
                j = max(0, k-(n-1))
                while j <= min(k, m-1):
                    ans.append(matrix[i][j])
                    i -= 1
                    j += 1
            else:
                i = max(0, k-(m-1))
                j = min(k, m-1)
                while i <= min(k, n-1):
                    ans.append(matrix[i][j])
                    i += 1
                    j -= 1
            k += 1
        return ans
