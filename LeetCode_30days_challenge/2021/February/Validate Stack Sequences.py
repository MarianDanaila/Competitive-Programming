from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        stack = []
        i = 0
        j = 0
        while i < n or j < n:
            if stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            else:
                if i == n:
                    return False
                stack.append(pushed[i])
                i += 1
        return True
