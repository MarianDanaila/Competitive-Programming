from typing import List


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        n = len(nums)
        removed = False
        last = nums[0]
        for i in range(1, n):
            if nums[i] <= last:
                if removed:
                    return False
                removed = True
                if i >= 2 and nums[i] <= nums[i - 2]:
                    continue
            last = nums[i]
        return True
