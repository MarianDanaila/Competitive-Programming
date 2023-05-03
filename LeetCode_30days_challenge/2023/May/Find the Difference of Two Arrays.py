from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        answer1 = []
        answer2 = []
        for num in nums1_set:
            if num not in nums2_set:
                answer1.append(num)
        for num in nums2_set:
            if num not in nums1_set:
                answer2.append(num)
        return [answer1, answer2]
