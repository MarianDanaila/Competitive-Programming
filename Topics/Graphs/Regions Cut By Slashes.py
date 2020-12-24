class DSU:
    def __init__(self, N):
        self.p = [i for i in range(N)]

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        x_set = self.find(x)
        y_set = self.find(y)
        self.p[x_set] = y_set


class Solution:
    def regionsBySlashes(self, grid):
        n = len(grid)
        dsu = DSU(4 * n * n)
        for i in range(n):
            for j in range(n):
                root = 4 * (i * n + j)
                if grid[i][j] in '/ ':
                    dsu.union(root + 0, root + 1)
                    dsu.union(root + 2, root + 3)
                if grid[i][j] in '\ ':
                    dsu.union(root + 0, root + 2)
                    dsu.union(root + 1, root + 3)

                # north/south
                if i + 1 < n:
                    dsu.union(root + 3, (root + 4 * n) + 0)
                if i - 1 >= 0:
                    dsu.union(root + 0, (root - 4 * n) + 3)

                # west/east
                if j + 1 < n:
                    dsu.union(root + 2, (root + 4) + 1)
                if j - 1 >= 0:
                    dsu.union(root + 1, (root - 4) + 2)
        ans = 0
        for i in range(4 * n * n):
            if dsu.find(i) == i:
                ans += 1
        return ans
