from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest_sum, curr_sum = -1, 0
        for num in nums:
            curr_sum += num
            largest_sum = max(largest_sum, curr_sum)
            curr_sum = max(curr_sum, 0)

        if largest_sum == -1:
            return max(nums)
        return largest_sum
