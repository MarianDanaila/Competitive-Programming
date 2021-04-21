from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)
        for i in range(1, rows):
            length_row = len(triangle[i])
            for j in range(length_row):
                if j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                elif j == length_row - 1:
                    triangle[i][j] += triangle[i - 1][j - 1]
                else:
                    triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
        return min(triangle[rows - 1])
