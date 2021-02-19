from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        max_area = 0
        while i < j:
            if height[i] < height[j]:
                max_area = max((j-i) * height[i], max_area)
                i += 1
            else:
                max_area = max((j-i) * height[j], max_area)
                j -= 1
        return max_area