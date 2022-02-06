from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        ans = []
        for num in nums:
            if num < pivot:
                ans.append(num)
        for num in nums:
            if num == pivot:
                ans.append(num)
        for num in nums:
            if num > pivot:
                ans.append(num)
        return ans
