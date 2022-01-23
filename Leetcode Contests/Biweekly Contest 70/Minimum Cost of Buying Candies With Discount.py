from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        total_cost = 0
        while len(cost) > 2:
            total_cost += cost.pop()
            total_cost += cost.pop()
            cost.pop()
        while len(cost) > 0:
            total_cost += cost.pop()
        return total_cost
