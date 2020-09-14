# Space-complexity: O(N)
class Solution:
    def rob(self, nums) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        dp = [nums[0]] * n
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]

# Space-complexity: O(1)
class Solution:
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        first = nums[0]
        second = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            curr = max(first + nums[i], second)
            first = second
            second = curr
        return curr
