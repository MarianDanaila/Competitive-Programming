# Approach 1: Space Complexity: O(M*N)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        return grid[m - 1][n - 1]


# Approach 2: Space Complexity: O(2 * N)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        curr_row = [1] * n
        prev_row = [1] * n
        for _ in range(1, m):
            for i in range(1, n):
                curr_row[i] = curr_row[i - 1] + prev_row[i]
            for i in range(1, n):
                prev_row[i] = curr_row[i]
                curr_row[i] = 1
        return prev_row[n - 1]


# Approach 3: Space Complexity: O(N)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for _ in range(1, m):
            for i in range(1, n):
                row[i] += row[i - 1]

        return row[n - 1]


