from functools import cache
from typing import List


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @cache
        def dp(left, right, k):
            if left > right:
                return 0
            while left + 1 <= right and boxes[left] == boxes[left + 1]:
                #  increase both `left` and `k` if they have consecutive colors with `boxes[i]`
                left += 1
                k += 1
            ans = (k + 1) * (k + 1) + dp(left + 1, right, 0)  # remove all boxes which are the same as `boxes[left]`
            for m in range(left + 1, right + 1):  # try to merge non-contiguous boxes of the same color together
                if boxes[left] == boxes[m]:
                    ans = max(ans, dp(m, right, k + 1) + dp(left + 1, m - 1, 0))
            return ans
        return dp(0, len(boxes) - 1, 0)
