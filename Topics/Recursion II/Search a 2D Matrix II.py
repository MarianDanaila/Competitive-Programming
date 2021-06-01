from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        def search_on_row(row, left, right):
            if row == m or right == -1:
                return False
            if left > right:
                return search_on_row(row + 1, 0, right)

            mid = left + (right - left) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                return search_on_row(row, mid + 1, right)
            else:
                return search_on_row(row, left, mid - 1)

        return search_on_row(0, 0, n - 1)
