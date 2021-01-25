class Solution:
    def generateMatrix(self, n: int):
        mat = [[0] * n for _ in range(n)]
        if n % 2 != 0:
            mat[n // 2][n // 2] = n * n
        low = 0
        high = n
        number = 1
        for _ in range(n // 2):
            for j in range(low, high):
                mat[low][j] = number
                number += 1
            for i in range(low + 1, high):
                mat[i][high - 1] = number
                number += 1
            for j in range(high - 2, low - 1, -1):
                mat[high - 1][j] = number
                number += 1
            for i in range(high - 2, low, -1):
                mat[i][low] = number
                number += 1
            low += 1
            high -= 1
        return mat
