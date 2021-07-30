from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        dq = deque()
        visited = [[False] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    dq.append((i, j))
                    visited[i][j] = True
        while dq:
            len_dq = len(dq)
            for _ in range(len_dq):
                x, y = dq.popleft()
                if x - 1 >= 0 and not visited[x - 1][y]:
                    visited[x - 1][y] = True
                    mat[x - 1][y] = mat[x][y] + 1
                    dq.append((x - 1, y))

                if y + 1 < m and not visited[x][y + 1]:
                    visited[x][y + 1] = True
                    mat[x][y + 1] = mat[x][y] + 1
                    dq.append((x, y + 1))

                if x + 1 < n and not visited[x + 1][y]:
                    visited[x + 1][y] = True
                    mat[x + 1][y] = mat[x][y] + 1
                    dq.append((x + 1, y))

                if y - 1 >= 0 and not visited[x][y - 1]:
                    visited[x][y - 1] = True
                    mat[x][y - 1] = mat[x][y] + 1
                    dq.append((x, y - 1))

        return mat
