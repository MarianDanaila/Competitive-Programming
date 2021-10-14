from collections import deque
from math import sqrt, ceil, floor


class Solution:
    def numSquares(self, n):
        dq = deque()
        perfect_squares = []
        visited = set()
        for i in range(1, n + 1):
            root = sqrt(i)
            if ceil(root) == floor(root):
                perfect_squares.append(i)
        dq.append(n)
        visited.add(n)
        numbers = 0
        while dq:
            len_dq = len(dq)
            numbers += 1
            for _ in range(len_dq):
                curr = dq.popleft()
                for perfect_square in perfect_squares:
                    if perfect_square > curr:
                        break
                    if perfect_square == curr:
                        return numbers
                    if curr - perfect_square not in visited:
                        visited.add(curr - perfect_square)
                        dq.append(curr - perfect_square)
