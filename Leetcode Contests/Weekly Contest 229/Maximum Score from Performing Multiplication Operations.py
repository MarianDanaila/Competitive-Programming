from typing import List


class Solution:
    def maximumScore(self, nums: List[int], muls: List[int]) -> int:
        n = len(nums)
        m = len(muls)
        dp = [[0] * m for _ in range(m)]

        def dfs(l, i):
            if i == m:
                return 0

            if not dp[l][i]:
                pick_left = dfs(l + 1, i + 1) + nums[l] * muls[i]
                pick_right = dfs(l, i + 1) + nums[n - (i - l) - 1] * muls[i]
                dp[l][i] = max(pick_left, pick_right)
            return dp[l][i]
        return dfs(0, 0)
