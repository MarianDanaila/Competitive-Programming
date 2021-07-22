from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        if nums[0] < nums[1]:
            idx1, idx2 = 1, 0
        else:
            idx1, idx2 = 0, 1

        for i in range(2, n):
            if nums[i] > nums[idx1]:
                idx2, idx1 = idx1, i
            elif nums[i] > nums[idx2]:
                idx2 = i
        if nums[idx1] >= 2 * nums[idx2]:
            return idx1
        return -1
