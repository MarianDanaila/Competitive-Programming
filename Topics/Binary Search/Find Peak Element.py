from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        low, high = 0, n - 1
        while low <= high:
            mid = low + (high - low) // 2
            if mid == 0:
                if nums[mid] > nums[mid + 1]:
                    return mid
                else:
                    low = mid + 1
            elif mid == n - 1:
                return mid
            else:
                if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                    return mid
                elif abs(nums[mid] - nums[low]) < mid - low:
                    high = mid - 1
                    continue
                elif abs(nums[high] - nums[mid]) < high - mid:
                    low = mid + 1
                    continue
                else:
                    if nums[mid] > nums[mid - 1]:
                        low = mid + 1
                    else:
                        high = mid - 1
