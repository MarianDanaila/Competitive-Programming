from math import ceil
from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        minim, maxim, n = min(nums), max(nums), len(nums)
        if minim == maxim:  # all elements are the same
            return 0
        bucket_size = ceil((maxim - minim) / (n - 1))
        min_bucket = [float("inf")] * n
        max_bucket = [-float("inf")] * n
        for num in nums:
            idx = (num - minim) // bucket_size
            min_bucket[idx] = min(min_bucket[idx], num)
            max_bucket[idx] = max(max_bucket[idx], num)
        max_gap = bucket_size
        prev = max_bucket[0]
        for i in range(1, n):
            if min_bucket[i] == float("inf"):
                continue
            max_gap = max(max_gap, min_bucket[i] - prev)
            prev = max_bucket[i]

        return max_gap
