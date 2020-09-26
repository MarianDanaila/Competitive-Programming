class Solution:
    def uniquePathsIII(self, grid):
        n = len(grid)
        m = len(grid[0])
        self.ans = 0
        empty = 1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    x, y = [i, j]
                elif grid[i][j] == 0:
                    empty += 1

        def dfs(i, j, empty):
            if (i < 0 or i >= n) or (j < 0 or j >= m) or grid[i][j] == -1:
                return
            if grid[i][j] == 2:
                if empty == 0:
                    self.ans += 1
                return
            grid[i][j] = -1
            dfs(i, j+1, empty-1)
            dfs(i, j-1, empty-1)
            dfs(i+1, j, empty-1)
            dfs(i-1, j, empty-1)

            grid[i][j] = 0
        dfs(x, y, empty)
        return self.ans
