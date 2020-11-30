# Approach1
# TOP-DOWN DP
class Solution:
    def canPartition(self, nums) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        subset_sum = total_sum // 2
        n = len(nums)
        dp = [[None] * (subset_sum + 1) for _ in range(n + 1)]

        def dfs(n, dp, target_sum, nums):
            if target_sum == 0:
                return True

            if n == 0 or target_sum < 0:
                return False

            if dp[n][target_sum] is not None:
                return dp[n][target_sum]

            result = dfs(n - 1, dp, target_sum - nums[n], nums) or dfs(n - 1, dp, target_sum, nums)
            dp[n][target_sum] = result
            return result

        return dfs(n - 1, dp, subset_sum, nums)


# Approach2
# BOTTOM-UP DP
class Solution:
    def canPartition(self, nums) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        subset_sum = total_sum // 2
        n = len(nums)
        dp = [[False] * (subset_sum + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            curr = nums[i - 1]
            for j in range(subset_sum + 1):
                if j < curr:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - curr]
        return dp[n][subset_sum]


# Approach3
# Optimized BOTTOM-UP DP
class Solution:
    def canPartition(self, nums) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        subset_sum = total_sum // 2
        dp = [False] * (subset_sum + 1)
        dp[0] = True
        for curr in nums:
            for j in range(subset_sum, curr - 1, -1):
                dp[j] = dp[j] or dp[j - curr]
        return dp[-1]
