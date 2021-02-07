from collections import deque


class Solution:
    def numSquares(self, n: int) -> int:
        perf_squares = []
        i = 1
        while i * i <= n:
            perf_squares.append(i * i)
            i += 1

        dq = deque()
        dq.append(n)
        nr = 0
        visited = set()
        visited.add(n)
        while dq:
            nr += 1
            for _ in range(len(dq)):
                curr = dq.popleft()
                for i in range(len(perf_squares)):
                    if curr == perf_squares[i]:
                        return nr
                    if perf_squares[i] < curr:
                        nxt = curr - perf_squares[i]
                        if nxt not in visited:
                            visited.add(nxt)
                            dq.append(nxt)
