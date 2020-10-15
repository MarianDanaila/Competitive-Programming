class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)-1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])

        max1 = dp[-1]

        dp[1] = nums[1]
        dp[2] = max(nums[1], nums[2])
        for i in range(3, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])

        return max(max1, dp[-1])
