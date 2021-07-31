from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        stack = []
        water_units = 0
        for i in range(n):
            if height[i] == 0:
                continue
            maxim = 0
            while stack and height[stack[-1]] < height[i]:
                idx = stack.pop()
                water_units += (i - idx - 1) * (height[idx] - maxim)
                maxim = max(maxim, height[idx])

            if stack:
                water_units += (i - stack[-1] - 1) * (height[i] - maxim)
            stack.append(i)

        return water_units
