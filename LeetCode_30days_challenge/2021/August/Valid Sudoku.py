from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        m = len(board[0])
        rows, cols, squares = {}, {}, {}
        for i in range(9):
            rows[i] = set()
            cols[i] = set()
        for i in range(3):
            for j in range(3):
                squares[(i, j)] = set()

        for i in range(n):
            for j in range(m):
                if board[i][j] != '.':
                    square_x, square_y = i // 3, j // 3
                    if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squares[(square_x, square_y)]:
                        return False
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    squares[(square_x, square_y)].add(board[i][j])

        return True
