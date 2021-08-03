from collections import deque


class Solution:
    def largestIsland(self, grid):
        n = len(grid)
        dq = deque()
        component = 1
        sizes = {}
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    component += 1
                    grid[i][j] = component
                    size_component = 0
                    # run bfs
                    dq.append((i, j))
                    while dq:
                        x, y = dq.popleft()
                        size_component += 1
                        if x - 1 >= 0 and grid[x - 1][y] == 1:
                            dq.append((x - 1, y))
                            grid[x - 1][y] = component
                        if y + 1 < n and grid[x][y + 1] == 1:
                            dq.append((x, y + 1))
                            grid[x][y + 1] = component
                        if x + 1 < n and grid[x + 1][y] == 1:
                            dq.append((x + 1, y))
                            grid[x + 1][y] = component
                        if y - 1 >= 0 and grid[x][y - 1] == 1:
                            dq.append((x, y - 1))
                            grid[x][y - 1] = component
                    sizes[component] = size_component
        largest_size = 0
        zero = False
        for i in range(n):
            for j in range(n):
                components = set()
                if grid[i][j] == 0:
                    zero = True
                    if i - 1 >= 0 and grid[i - 1][j] != 0:
                        components.add(grid[i - 1][j])
                    if j + 1 < n and grid[i][j + 1] != 0:
                        components.add(grid[i][j + 1])
                    if i + 1 < n and grid[i + 1][j] != 0:
                        components.add(grid[i + 1][j])
                    if j - 1 >= 0 and grid[i][j - 1] != 0:
                        components.add(grid[i][j - 1])
                curr_size = 1
                for component in components:
                    curr_size += sizes[component]
                largest_size = max(largest_size, curr_size)
        if not zero:
            return n * n
        return largest_size
