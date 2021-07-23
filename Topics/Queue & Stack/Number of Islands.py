from collections import deque
from typing import List

# BFS Approach


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dq = deque()
        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islands += 1
                    dq.append([i, j])
                    grid[i][j] = '-1'
                    while dq:
                        x, y = dq.popleft()
                        if x - 1 >= 0:
                            if grid[x - 1][y] == '1':
                                grid[x - 1][y] = '-1'
                                dq.append([x - 1, y])

                        if y - 1 >= 0:
                            if grid[x][y - 1] == '1':
                                grid[x][y - 1] = '-1'
                                dq.append([x, y - 1])

                        if x + 1 < m:
                            if grid[x + 1][y] == '1':
                                grid[x + 1][y] = '-1'
                                dq.append([x + 1, y])

                        if y + 1 < n:
                            if grid[x][y + 1] == '1':
                                grid[x][y + 1] = '-1'
                                dq.append([x, y + 1])
        return islands

# DFS Approach


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()

        def dfs(x, y):
            if x - 1 >= 0 and (x - 1, y) not in visited and grid[x - 1][y] == '1':
                visited.add((x - 1, y))
                dfs(x - 1, y)
            if y + 1 < m and (x, y + 1) not in visited and grid[x][y + 1] == '1':
                visited.add((x, y + 1))
                dfs(x, y + 1)
            if x + 1 < n and (x + 1, y) not in visited and grid[x + 1][y] == '1':
                visited.add((x + 1, y))
                dfs(x + 1, y)
            if y - 1 >= 0 and (x, y - 1) not in visited and grid[x][y - 1] == '1':
                visited.add((x, y - 1))
                dfs(x, y - 1)

        n = len(grid)
        m = len(grid[0])
        islands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and (i, j) not in visited:
                    visited.add((i, j))
                    islands += 1
                    dfs(i, j)

        return islands
