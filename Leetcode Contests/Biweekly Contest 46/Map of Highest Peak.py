from collections import deque
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        dq = deque()
        n = len(isWater)
        m = len(isWater[0])
        visited = [[False] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    dq.append([i, j])
                    visited[i][j] = True
                    isWater[i][j] = 0
        while dq:
            for _ in range(len(dq)):
                x, y = dq.popleft()
                height = isWater[x][y]
                if 0 <= x - 1 < n and not visited[x - 1][y]:
                    visited[x - 1][y] = True
                    isWater[x - 1][y] = height + 1
                    dq.append([x - 1, y])
                if 0 <= y - 1 < m and not visited[x][y - 1]:
                    visited[x][y - 1] = True
                    isWater[x][y - 1] = height + 1
                    dq.append([x, y - 1])

                if 0 <= x + 1 < n and not visited[x + 1][y]:
                    visited[x + 1][y] = True
                    isWater[x + 1][y] = height + 1
                    dq.append([x + 1, y])

                if 0 <= y + 1 < m and not visited[x][y + 1]:
                    visited[x][y + 1] = True
                    isWater[x][y + 1] = height + 1
                    dq.append([x, y + 1])
        return isWater
