from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1
        added = i = 0
        len_nums = len(nums)
        while miss <= n:
            if i < len_nums and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                added += 1
        return added
