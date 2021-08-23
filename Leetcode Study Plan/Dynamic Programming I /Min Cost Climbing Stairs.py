from typing import List

# Approach 1: Space-complexity: O(N), where N is the length of the input array


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1] * (n + 1)
        dp[0], dp[1] = 0, 0
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[-1]


# Approach 2: Space-complexity: O(1)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        prev, curr = 0, 0
        for i in range(2, n + 1):
            prev, curr = curr, min(curr + cost[i - 1], prev + cost[i - 2])
        return curr
