from typing import List
# Approach 1 using sorting


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        minim = nums[0]
        l1 = 1
        l2 = 0
        max_length = 0
        for i in range(1, len(nums)):
            if nums[i] == minim:
                l1 += 1
            elif nums[i] - minim == 1:
                l2 += 1
                max_length = max(l1 + l2, max_length)
            else:
                if nums[i] - nums[i - 1] == 1:
                    l1 = l2
                    l2 = 1
                    minim = nums[i - 1]
                else:
                    minim = nums[i]
                    l1 = 1
                    l2 = 0

        return max_length

# Approach 2 using HashMap


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        occ = {}
        max_length = 0
        for num in nums:
            if num in occ:
                occ[num] += 1
            else:
                occ[num] = 1

            if num + 1 in occ:
                max_length = max(max_length, occ[num] + occ[num + 1])
            if num - 1 in occ:
                max_length = max(max_length, occ[num] + occ[num - 1])

        return max_length
