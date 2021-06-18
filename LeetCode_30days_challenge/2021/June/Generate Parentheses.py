from collections import deque
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dq = deque()
        dq.append(["(", 1, 0])
        ans = []
        while dq:
            combination, left, right = dq.popleft()
            if left == n and right == n:
                ans.append(combination)
                continue
            if left == right:
                dq.append([combination + "(", left + 1, right])
            elif left == n:
                dq.append([combination + ")", left, right + 1])
            else:
                dq.append([combination + "(", left + 1, right])
                dq.append([combination + ")", left, right + 1])

        return ans
