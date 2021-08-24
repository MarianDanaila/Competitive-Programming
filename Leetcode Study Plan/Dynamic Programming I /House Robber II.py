from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(start, end):
            first, second = nums[start], max(nums[start], nums[start + 1])
            for i in range(start + 2, end):
                first, second = second, max(second, first + nums[i])
            return second
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])

        return max(helper(0, n - 1), helper(1, n))
