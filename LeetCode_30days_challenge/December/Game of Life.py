class Solution:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])

        def valid(i, j):
            return 0 <= i <= n-1 and 0 <= j <= m-1
        for i in range(n):
            for j in range(m):
                live = 0
                for x in [-1, 0, 1]:
                    for y in [-1, 0, 1]:
                        if x == 0 and y == 0:
                            continue
                        else:
                            if valid(i+x, j+y):
                                if board[i+x][j+y] % 10 == 1:
                                    live += 1
                if board[i][j] == 1:  # live cell
                    if live != 2 and live != 3:
                        board[i][j] = 101
                else:  # dead cell
                    if live == 3:
                        board[i][j] = 110
        for i in range(n):
            for j in range(m):
                if board[i][j] > 100:
                    board[i][j] = (board[i][j] // 10) % 10
