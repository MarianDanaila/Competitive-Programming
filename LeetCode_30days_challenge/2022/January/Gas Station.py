from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total_gas = 0
        for i in range(n):
            gas[i] -= cost[i]
            total_gas += gas[i]
        if total_gas < 0:
            return -1
        idx = 0
        for i in range(1, n):
            gas[i] += gas[i - 1]
            if gas[i] < gas[idx]:
                idx = i
        return (idx + 1) % n
