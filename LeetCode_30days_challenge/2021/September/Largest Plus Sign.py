from typing import List


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        zeros = set()
        for r, c in mines:
            zeros.add((r, c))

        grid = [[0] * n for _ in range(n)]
        order = 0
        for i in range(n):
            count = 0
            for j in range(n):
                if (i, j) in zeros:
                    count = 0
                else:
                    count += 1
                grid[i][j] = count
            count = 0
            for j in range(n - 1, -1, -1):
                if (i, j) in zeros:
                    count = 0
                else:
                    count += 1
                grid[i][j] = min(grid[i][j], count)

        for j in range(n):
            count = 0
            for i in range(n):
                if (i, j) in zeros:
                    count = 0
                else:
                    count += 1

                grid[i][j] = min(grid[i][j], count)
            count = 0
            for i in range(n - 1, -1, -1):
                if (i, j) in zeros:
                    count = 0
                else:
                    count += 1
                grid[i][j] = min(grid[i][j], count)
                order = max(order, grid[i][j])

        return order
