from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = {}
        n = len(moves)
        for i in range(n):
            x, y = moves[i]
            if i % 2 == 0:
                board[(x, y)] = 'A'
            else:
                board[(x, y)] = 'B'

        for row in range(3):
            if (row, 0) in board and (row, 1) in board and (row, 2) in board and board[(row, 0)] == board[(row, 1)] == \
                    board[(row, 2)]:
                return board[(row, 0)]

        for col in range(3):
            if (0, col) in board and (1, col) in board and (2, col) in board and board[(0, col)] == board[(1, col)] == \
                    board[(2, col)]:
                return board[(0, col)]

        if (0, 0) in board and (1, 1) in board and (2, 2) in board and board[(0, 0)] == board[(1, 1)] == board[(2, 2)]:
            return board[(0, 0)]

        if (0, 2) in board and (1, 1) in board and (2, 0) in board and board[(0, 2)] == board[(1, 1)] == board[(2, 0)]:
            return board[(0, 2)]

        if n == 9:
            return "Draw"
        return "Pending"
