class Solution:
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        if sum(gas) < sum(cost):
            return -1
        curr_sum = 0
        minim = float("inf")
        for i in range(n):
            curr_sum += gas[i]-cost[i]
            if curr_sum < minim:
                minim = curr_sum
                index = i
        if index + 1 == n:
            return 0
        else:
            return index + 1
