from collections import deque
from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        dq = deque()
        n, m = len(grid), len(grid[0])
        empty = walks = 0
        visited = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] != -1:
                    if grid[i][j] == 1:
                        visited.add((i, j))
                        dq.append([i, j, visited])
                    empty += 1

        while dq:
            x, y, visited = dq.popleft()
            if grid[x][y] == 2:
                if len(visited) == empty:
                    walks += 1
            else:
                if x - 1 >= 0 and grid[x - 1][y] != -1 and (x - 1, y) not in visited:
                    next_visited = visited.copy()
                    next_visited.add((x - 1, y))
                    dq.append([x - 1, y, next_visited])
                if y + 1 < m and grid[x][y + 1] != -1 and (x, y + 1) not in visited:
                    next_visited = visited.copy()
                    next_visited.add((x, y + 1))
                    dq.append([x, y + 1, next_visited])
                if x + 1 < n and grid[x + 1][y] != -1 and (x + 1, y) not in visited:
                    next_visited = visited.copy()
                    next_visited.add((x + 1, y))
                    dq.append([x + 1, y, next_visited])
                if y - 1 >= 0 and grid[x][y - 1] != -1 and (x, y - 1) not in visited:
                    next_visited = visited.copy()
                    next_visited.add((x, y - 1))
                    dq.append([x, y - 1, next_visited])
        return walks
