from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        low, high = 0, n - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] < nums[high]:
                high = mid - 1
            else:
                low = mid + 1
