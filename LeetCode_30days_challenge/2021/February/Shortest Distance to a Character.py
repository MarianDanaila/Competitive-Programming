from collections import deque
from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        dq = deque()
        n = len(s)
        out = [0] * n
        for i in range(n):
            if s[i] == c:
                dq.append(i)

        for i in range(n):
            if len(dq) == 1:
                out[i] = abs(dq[0] - i)
            else:
                if abs(dq[0] - i) >= abs(dq[1] - i):
                    out[i] = abs(dq[1] - i)
                    dq.popleft()
                else:
                    out[i] = abs(dq[0] - i)
        return out
