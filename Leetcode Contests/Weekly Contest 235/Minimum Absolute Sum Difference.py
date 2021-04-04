from typing import List


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        absolute_sum = 0
        n = len(nums1)
        sorted_nums = sorted(nums1)
        for i in range(n):
            absolute_sum += abs(nums1[i] - nums2[i])
        max_diff = 0
        for i in range(n):
            diff = abs(nums1[i] - nums2[i])
            if diff == 0:
                continue
            target_low = max(sorted_nums[0], nums2[i] - diff + 1)
            target_high = min(sorted_nums[-1], nums2[i] + diff - 1)
            low = 0
            high = n - 1
            possible = -1
            while low <= high:
                mid = low + (high - low) // 2
                if target_low <= sorted_nums[mid] <= target_high:
                    max_diff = max(max_diff, diff - abs(sorted_nums[mid] - nums2[i]))
                if sorted_nums[mid] - nums2[i] == 0:
                    break
                elif sorted_nums[mid] - nums2[i] < 0:
                    low = mid + 1
                else:
                    high = mid - 1
            if possible == -1:
                continue

        return (absolute_sum - max_diff) % (10 ** 9 + 7)
