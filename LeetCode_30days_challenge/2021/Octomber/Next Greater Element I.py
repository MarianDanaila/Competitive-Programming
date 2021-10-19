from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        n, m = len(nums1), len(nums2)
        next_greater = {}
        ans = []
        for i in range(m - 1, -1, -1):
            num = nums2[i]
            while stack and num > stack[-1]:
                stack.pop()
            if stack:
                next_greater[num] = stack[-1]
            else:
                next_greater[num] = -1
            stack.append(num)

        for num in nums1:
            ans.append(next_greater[num])

        return ans
