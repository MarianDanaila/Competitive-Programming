from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest_sum = -float("inf")
        curr_sum = 0
        for num in nums:
            curr_sum += num
            largest_sum = max(largest_sum, curr_sum)
            curr_sum = max(0, curr_sum)
        return largest_sum
