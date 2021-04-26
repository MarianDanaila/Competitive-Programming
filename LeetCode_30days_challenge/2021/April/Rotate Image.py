from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for row in matrix:
            start = 0
            end = n - 1
            while start < end:
                row[start], row[end] = row[end], row[start]
                start += 1
                end -= 1
        i = n - 1
        j = 0
        while True:
            start_x = i
            start_y = j
            sum_idx = n - (start_x + start_y) - 1
            end_x = start_x + sum_idx
            end_y = start_y + sum_idx
            while start_x < end_x:
                matrix[start_x][start_y], matrix[end_x][end_y] = matrix[end_x][end_y], matrix[start_x][start_y]
                start_x += 1
                start_y += 1
                end_x -= 1
                end_y -= 1
            if i == 0:
                j += 1
            else:
                i -= 1

            if i == 0 and j == n:
                break
