from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        low = 0
        high = n - 1
        first = last = -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                first = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        if first == -1:
            return [-1, -1]

        low = 0
        high = n - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                last = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return [first, last]
