class Solution:
    def waysToMakeFair(self, nums):
        odd = even = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                even += nums[i]
            else:
                odd += nums[i]

        prev_odd = prev_even = 0
        count = 0
        for i in range(len(nums)):
            if i % 2 == 1:
                curr_even = odd - prev_odd - nums[i] + prev_even
                curr_odd = even - prev_even + prev_odd
                prev_odd += nums[i]
            else:
                curr_even = prev_even + odd - prev_odd
                curr_odd = prev_odd + even - nums[i] - prev_even
                prev_even += nums[i]
            if curr_even == curr_odd:
                count += 1
        return count
