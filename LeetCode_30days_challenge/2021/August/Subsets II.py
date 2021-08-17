from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subsets = []
        nums.sort()

        def backtrack(first, comb):
            if k == len(comb):
                subsets.append(comb[:])
                return

            for i in range(first, n):
                if i == first or nums[i] != nums[i - 1]:
                    comb.append(nums[i])
                    backtrack(i + 1, comb)
                    comb.pop()

        for k in range(n + 1):
            backtrack(0, [])

        return subsets
