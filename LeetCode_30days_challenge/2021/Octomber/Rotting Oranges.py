from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dq = deque()
        n, m = len(grid), len(grid[0])
        fresh = minutes = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    dq.append([i, j])
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        while dq:
            len_dq = len(dq)
            minutes += 1
            for _ in range(len_dq):
                x, y = dq.popleft()
                if x - 1 >= 0 and grid[x - 1][y] == 1:
                    fresh -= 1
                    grid[x - 1][y] = 2
                    dq.append([x - 1, y])
                if y + 1 < m and grid[x][y + 1] == 1:
                    fresh -= 1
                    grid[x][y + 1] = 2
                    dq.append([x, y + 1])
                if x + 1 < n and grid[x + 1][y] == 1:
                    fresh -= 1
                    grid[x + 1][y] = 2
                    dq.append([x + 1, y])
                if y - 1 >= 0 and grid[x][y - 1] == 1:
                    fresh -= 1
                    grid[x][y - 1] = 2
                    dq.append([x, y - 1])

                if fresh == 0:
                    return minutes

        if fresh > 0:
            return -1
