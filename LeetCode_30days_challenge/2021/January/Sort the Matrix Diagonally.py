from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        i = n - 1
        j = 0
        bound = min(n, m)
        while i >= 0:
            for k in range(min(bound, n - i) - 1):
                for l in range(k + 1, min(bound, n - i)):
                    if mat[i + k][j + k] > mat[i + l][j + l]:
                        mat[i + k][j + k], mat[i + l][j + l] = mat[i + l][j + l], mat[i + k][j + k]
            i -= 1

        i = 0
        j = 1
        while j < m:
            for k in range(min(bound, m - j) - 1):
                for l in range(k + 1, min(bound, m - j)):
                    if mat[i + k][j + k] > mat[i + l][j + l]:
                        mat[i + k][j + k], mat[i + l][j + l] = mat[i + l][j + l], mat[i + k][j + k]
            j += 1

        return mat
