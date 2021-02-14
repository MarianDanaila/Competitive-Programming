from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        low = 1
        high = max(nums)
        while low <= high:
            target = low + (high - low) // 2
            cost = 0
            for num in nums:
                cost += (num - 1) // target

            if cost > maxOperations:
                low = target + 1
            else:
                high = target - 1
        return low
