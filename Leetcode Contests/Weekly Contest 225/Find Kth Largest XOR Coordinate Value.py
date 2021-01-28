class Solution:
    def kthLargestValue(self, matrix, k: int) -> int:
        large = [matrix[0][0]]
        n = len(matrix)
        m = len(matrix[0])
        for i in range(1, n):
            matrix[i][0] ^= matrix[i - 1][0]
            large.append(matrix[i][0])

        for j in range(1, m):
            matrix[0][j] ^= matrix[0][j - 1]
            large.append(matrix[0][j])

        for i in range(1, n):
            for j in range(1, m):
                matrix[i][j] ^= matrix[i][j - 1] ^ matrix[i - 1][j] ^ matrix[i - 1][j - 1]
                large.append(matrix[i][j])

        large.sort()
        return large[-k]
