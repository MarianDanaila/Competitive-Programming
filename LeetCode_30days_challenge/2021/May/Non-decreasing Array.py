from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2:
            return True
        changes = 0
        for i in range(1, n - 1):
            if nums[i - 1] > nums[i] > nums[i + 1]:
                return False
            if nums[i] >= nums[i - 1] and nums[i] > nums[i + 1]:
                if nums[i + 1] >= nums[i - 1]:
                    nums[i] = nums[i - 1]
                else:
                    nums[i + 1] = nums[i]
                changes += 1
            elif nums[i - 1] > nums[i]:
                nums[i - 1] = nums[i]
                changes += 1
            if changes == 2:
                return False
        return True
