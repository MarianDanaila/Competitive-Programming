from collections import deque
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        graph = {}
        in_degree = {}
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                neighbours = []
                if i - 1 >= 0 and matrix[i][j] < matrix[i - 1][j]:
                    neighbours.append([i - 1, j])
                    if (i - 1, j) in in_degree:
                        in_degree[(i - 1, j)] += 1
                    else:
                        in_degree[(i - 1, j)] = 1
                if j - 1 >= 0 and matrix[i][j] < matrix[i][j - 1]:
                    neighbours.append([i, j - 1])
                    if (i, j - 1) in in_degree:
                        in_degree[(i, j - 1)] += 1
                    else:
                        in_degree[(i, j - 1)] = 1
                if i + 1 < n and matrix[i][j] < matrix[i + 1][j]:
                    neighbours.append([i + 1, j])
                    if (i + 1, j) in in_degree:
                        in_degree[(i + 1, j)] += 1
                    else:
                        in_degree[(i + 1, j)] = 1
                if j + 1 < m and matrix[i][j] < matrix[i][j + 1]:
                    neighbours.append([i, j + 1])
                    if (i, j + 1) in in_degree:
                        in_degree[(i, j + 1)] += 1
                    else:
                        in_degree[(i, j + 1)] = 1

                if (i, j) not in in_degree:
                    in_degree[(i, j)] = 0
                if neighbours:
                    graph[(i, j)] = neighbours

        dq = deque()
        length = 0
        for x, y in in_degree:
            if in_degree[(x, y)] == 0:
                dq.append((x, y))

        while dq:
            length += 1
            for _ in range(len(dq)):
                x, y = dq.popleft()
                if (x, y) in graph:
                    for nxt_x, nxt_y in graph[(x, y)]:
                        in_degree[(nxt_x, nxt_y)] -= 1
                        if in_degree[(nxt_x, nxt_y)] == 0:
                            dq.append((nxt_x, nxt_y))

        return length
