from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        order = []
        n, m = len(matrix), len(matrix[0])
        left, right, down, up = 0, m - 1, n - 1, 0
        while len(order) < n * m:
            # from left to right
            for col in range(left, right + 1):
                order.append(matrix[up][col])

            # from up to down
            for row in range(up + 1, down + 1):
                order.append(matrix[row][right])

            if up < down:  # for avoiding duplicates
                # from right to left
                for col in range(right - 1, left - 1, -1):
                    order.append(matrix[down][col])
            if left < right:  # for avoiding duplicates
                # from down to up
                for row in range(down - 1, up, -1):
                    order.append(matrix[row][left])

            # update the reference points
            left += 1
            right -= 1
            down -= 1
            up += 1
        return order
