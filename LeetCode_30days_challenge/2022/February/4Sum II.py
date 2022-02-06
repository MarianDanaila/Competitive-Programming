from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        sums = {}
        counter = 0
        for num1 in nums1:
            for num2 in nums2:
                if num1 + num2 in sums:
                    sums[num1 + num2] += 1
                else:
                    sums[num1 + num2] = 1
        for num3 in nums3:
            for num4 in nums4:
                if -(num3 + num4) in sums:
                    counter += sums[-(num3 + num4)]
        return counter
