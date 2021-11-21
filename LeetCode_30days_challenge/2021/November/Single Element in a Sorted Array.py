from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        low, high = 0, n - 1
        while low <= high:
            mid = low + (high - low) // 2
            if (mid == 0 and nums[mid + 1] != nums[mid]) or (mid == n - 1 and nums[mid - 1] != nums[mid]) or (
                    nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]):
                return nums[mid]
            elif nums[mid] == nums[mid - 1]:
                if (mid - 1 - low) % 2 == 1:
                    high = mid - 2
                else:
                    low = mid + 1
            else:
                if (mid - low) % 2 == 1:
                    high = mid - 1
                else:
                    low = mid + 2
