from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dq = deque()
        n, m = len(board), len(board[0])
        for i in range(n):
            if board[i][0] == 'O':
                dq.append([i, 0])
            if board[i][m - 1] == 'O':
                dq.append([i, m - 1])
        for j in range(m):
            if board[0][j] == 'O':
                dq.append([0, j])
            if board[n - 1][j] == 'O':
                dq.append([n - 1, j])
        while dq:
            x, y = dq.popleft()
            board[x][y] = 'V'
            if x - 1 >= 0 and board[x - 1][y] == 'O':
                dq.append([x - 1, y])
            if y + 1 < m and board[x][y + 1] == 'O':
                dq.append([x, y + 1])
            if x + 1 < n and board[x + 1][y] == 'O':
                dq.append([x + 1, y])
            if y - 1 >= 0 and board[x][y - 1] == 'O':
                dq.append([x, y - 1])
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'V':
                    board[i][j] = 'O'
