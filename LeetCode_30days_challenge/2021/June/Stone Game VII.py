from typing import List


class Solution:
    def stoneGameVII(self, s: List[int]) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        prefix_sum = [0]
        for i in range(n):
            prefix_sum.append(s[i] + prefix_sum[i])

        def helper(left, right):
            if left == right:  # only one stone left
                return 0
            if dp[left][right] == 0:
                interval_sum = prefix_sum[right + 1] - prefix_sum[left]
                dp[left][right] = max(interval_sum - s[left] - helper(left + 1, right), interval_sum - s[right] - helper(left, right - 1))
            return dp[left][right]

        return helper(0, n - 1)
