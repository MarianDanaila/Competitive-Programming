from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        one = False
        for i in range(m):
            if one:
                obstacleGrid[i][0] = 0
            else:
                if obstacleGrid[i][0] == 1:
                    one = True
                obstacleGrid[i][0] = abs(obstacleGrid[i][0] - 1)
        if obstacleGrid[0][0] == 1:
            one = False
        else:
            one = True
        for j in range(1, n):
            if one:
                obstacleGrid[0][j] = 0
            else:
                if obstacleGrid[0][j] == 1:
                    one = True
                obstacleGrid[0][j] = abs(obstacleGrid[0][j] - 1)
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0
        return obstacleGrid[-1][-1]
