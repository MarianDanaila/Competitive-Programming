from collections import deque


class Solution:
    def reverseWords(self, s: str) -> str:
        dq = deque()
        start = -1
        n = len(s)
        for i in range(n):
            if s[i] == ' ':
                if start != -1:
                    dq.appendleft(s[start:i])
                    start = -1
            else:
                if start == -1:
                    start = i

        if start != -1:
            dq.appendleft(s[start:])

        return " ".join(dq)
