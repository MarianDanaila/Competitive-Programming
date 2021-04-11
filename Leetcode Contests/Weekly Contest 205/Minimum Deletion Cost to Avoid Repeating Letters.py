from typing import List


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        start = -1
        first = True
        min_cost = 0
        for i in range(len(s) - 1):
            if s[i + 1] == s[i]:
                if first:
                    start = i
                first = False
            else:
                if not first:
                    min_cost += sum(cost[start:i + 1]) - max(cost[start:i + 1])
                first = True
        if not first:
            min_cost += sum(cost[start:i + 2]) - max(cost[start:i + 2])
        return min_cost
