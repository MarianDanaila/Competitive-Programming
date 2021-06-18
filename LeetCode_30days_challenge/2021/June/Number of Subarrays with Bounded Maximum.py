from typing import List


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        subarrays = 0
        n = len(nums)
        start = end = maxim = 0
        while end < n:
            maxim = max(maxim, nums[end])
            if maxim >= left:
                length = end - start
                subarrays -= length * (length + 1) // 2
                maxim = 0
                start = end + 1
            end += 1

        length = end - start
        subarrays -= length * (length + 1) // 2
        length = 0
        for num in nums:
            if num > right:
                subarrays += length * (length + 1) // 2
                length = 0
            else:
                length += 1
        subarrays += length * (length + 1) // 2
        return subarrays
