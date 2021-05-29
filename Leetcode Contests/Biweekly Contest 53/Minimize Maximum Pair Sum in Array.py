from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        start = 0
        end = n - 1
        max_pair = 0
        while start < end:
            max_pair = max(max_pair, nums[start] + nums[end])
            start += 1
            end -= 1
        return max_pair
