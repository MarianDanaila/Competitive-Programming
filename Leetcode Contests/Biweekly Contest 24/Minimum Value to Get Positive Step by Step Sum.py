from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:

        sum = 0
        min = nums[0]
        for i in nums:
            sum += i
            if sum < min:
                min = sum
        if min >= 0:
            return 1
        else:
            return abs(min) + 1
