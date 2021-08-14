from typing import List

# Approach 1 with O(M + N) extra memory


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()

        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for row in rows:
            for col in range(m):
                matrix[row][col] = 0

        for col in cols:
            for row in range(n):
                matrix[row][col] = 0


# Approach 2 with O(1) extra memory
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        first_row = first_col = False
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    if i == 0:
                        first_row = True
                    if j == 0:
                        first_col = True
                    matrix[0][j] = matrix[i][0] = 2 ** 31
        for row in range(1, n):
            if matrix[row][0] == 2 ** 31:
                for col in range(m):
                    matrix[row][col] = 0
        for col in range(1, m):
            if matrix[0][col] == 2 ** 31:
                for row in range(n):
                    matrix[row][col] = 0
        if matrix[0][0] == 2 ** 31:
            if first_row:
                for col in range(m):
                    matrix[0][col] = 0
            if first_col:
                for row in range(n):
                    matrix[row][0] = 0
