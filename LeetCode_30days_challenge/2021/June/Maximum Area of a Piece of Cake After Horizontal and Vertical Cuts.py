from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        verticalCuts.append(0)
        verticalCuts.append(w)
        horizontalCuts.sort()
        verticalCuts.sort()
        n = len(horizontalCuts)
        m = len(verticalCuts)
        max_height = max_width = 0
        for i in range(1, n):
            max_height = max(max_height, horizontalCuts[i] - horizontalCuts[i - 1])
        for i in range(1, m):
            max_width = max(max_width, verticalCuts[i] - verticalCuts[i - 1])

        return (max_height * max_width) % (10 ** 9 + 7)
