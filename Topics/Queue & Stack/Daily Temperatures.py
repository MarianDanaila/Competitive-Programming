# Approach 1 by storing in stack index and value
from typing import List


class Solution1:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        output = [0] * len(T)
        for i in range(len(T)):
            while stack and T[i] > stack[-1][0]:
                output[stack[-1][1]] = i - stack[-1][1]
                stack.pop()

            stack.append([T[i], i])

        return output


# Approach 2 by storing in stack only the index
class Solution2:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        output = [0] * len(T)
        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                output[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)

        return output
