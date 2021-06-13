from typing import List


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        max_length = 1
        n = len(grid)
        m = len(grid[0])
        prefix_sum = [[0] * m for _ in range(n)]
        prefix_sum[0][0] = grid[0][0]
        for i in range(1, n):
            prefix_sum[i][0] = grid[i][0] + prefix_sum[i - 1][0]
        for j in range(1, m):
            prefix_sum[0][j] = grid[0][j] + prefix_sum[0][j - 1]
        for i in range(1, n):
            for j in range(1, m):
                prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] + grid[i][j] - prefix_sum[i - 1][j - 1]

        def query_sum(i1, j1, i2, j2):
            if i1 == 0 and j1 == 0:
                return prefix_sum[i2][j2]
            elif i1 == 0:
                return prefix_sum[i2][j2] - prefix_sum[i2][j1 - 1]
            elif j1 == 0:
                return prefix_sum[i2][j2] - prefix_sum[i1 - 1][j2]
            else:
                return prefix_sum[i2][j2] - prefix_sum[i2][j1 - 1] - prefix_sum[i1 - 1][j2] + prefix_sum[i1 - 1][j1 - 1]

        for i1 in range(n):
            for j1 in range(m):
                i2 = i1 + 1
                j2 = j1 + 1
                while i2 < n and j2 < m:
                    sum_magic = query_sum(i1, j1, i2, j2)
                    side_length = i2 - i1 + 1
                    if sum_magic % side_length == 0:
                        expected = sum_magic // side_length
                        good = True
                        for idx in range(side_length):
                            side_sum1 = query_sum(i1 + idx, j1, i2 - side_length + idx + 1, j2)
                            side_sum2 = query_sum(i1, j1 + idx, i2, j2 - side_length + idx + 1)
                            if side_sum1 != expected or side_sum2 != expected:
                                good = False
                                break
                        if good:
                            diagonal1 = diagonal2 = 0
                            for idx in range(side_length):
                                diagonal1 += grid[i1 + idx][j1 + idx]
                                diagonal2 += grid[i2 - idx][j1 + idx]
                            if diagonal1 != expected or diagonal2 != expected:
                                good = False
                            if good:
                                max_length = max(max_length, side_length)
                    i2 += 1
                    j2 += 1
        return max_length
