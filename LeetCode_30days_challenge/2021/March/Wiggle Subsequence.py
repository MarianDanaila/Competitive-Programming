from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        sign = 0
        deletions = 0
        for i in range(1, n):
            if sign == 0:
                if nums[i] - nums[i - 1] == 0:
                    deletions += 1
                elif nums[i] - nums[i - 1] < 0:
                    sign = -1
                else:
                    sign = 1
                continue

            if nums[i] - nums[i - 1] == 0:
                deletions += 1
            elif nums[i] - nums[i - 1] < 0:
                if sign == -1:
                    deletions += 1
                else:
                    sign = -1
            else:
                if sign == 1:
                    deletions += 1
                else:
                    sign = 1

        return n - deletions
