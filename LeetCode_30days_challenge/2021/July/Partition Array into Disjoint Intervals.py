from heapq import heappush, heappop
from typing import List

# Approach 1: Using Heap


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        occurrences = {}
        n = len(nums)
        heap = []
        for i in range(1, n):
            if nums[i] in occurrences:
                occurrences[nums[i]] += 1
            else:
                occurrences[nums[i]] = 1
                heappush(heap, nums[i])
        maxim = nums[0]
        for i in range(1, n):
            minim = heappop(heap)
            while minim not in occurrences:
                minim = heappop(heap)

            if maxim <= minim:
                return i
            maxim = max(maxim, nums[i])
            occurrences[nums[i]] -= 1
            if occurrences[nums[i]] == 0:
                occurrences.pop(nums[i])

            heappush(heap, minim)


# Approach 2: Linear
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        maxim = local_maxim = nums[0]
        partition_idx = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i] < local_maxim:
                local_maxim = maxim
                partition_idx = i
            else:
                maxim = max(maxim, nums[i])
        return partition_idx + 1
