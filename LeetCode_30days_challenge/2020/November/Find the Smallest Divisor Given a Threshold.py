from math import ceil


class Solution:
    def smallestDivisor(self, nums, threshold):
        max_nums = max(nums)
        low = 1
        high = max_nums + 1
        ans = -1
        while low <= high:
            mid = low + (high-low) // 2
            curr_sum = 0
            for num in nums:
                curr_sum += ceil(num/mid)
            if curr_sum <= threshold:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans
