from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        n = len(nums)
        left_sum, right_sum = 0, nums_sum
        for i in range(n):
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1
