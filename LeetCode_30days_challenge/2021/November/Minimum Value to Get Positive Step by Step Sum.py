from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        total_sum = 0
        minimum_sum = 0
        for num in nums:
            total_sum += num
            minimum_sum = min(minimum_sum, total_sum)
        return -minimum_sum + 1
