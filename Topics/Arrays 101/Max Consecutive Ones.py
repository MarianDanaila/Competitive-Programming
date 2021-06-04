from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        max_consecutive = consecutive = nums[0]
        for i in range(1, n):
            if nums[i] == 1:
                consecutive += 1
            else:
                max_consecutive = max(max_consecutive, consecutive)
                consecutive = 0
        return max(max_consecutive, consecutive)
