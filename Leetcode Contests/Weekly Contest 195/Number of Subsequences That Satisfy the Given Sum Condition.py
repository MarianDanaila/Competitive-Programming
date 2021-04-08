from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        counter = 0
        i = 0
        j = len(nums) - 1
        while i <= j:
            if nums[i] + nums[j] > target:
                j -= 1
            else:
                counter += 2 ** (j - i)
                i += 1
        return counter % ((10 ** 9) + 7)
