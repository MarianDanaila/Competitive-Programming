from typing import List
import heapq


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heap = []
        for i in range(n - 1, -1, -1):
            while heap and heap[0][1] > i + k:  # out of needed interval
                heapq.heappop(heap)
            if heap:
                max_score = -nums[i] + heap[0][0]
            else:
                max_score = -nums[i]
            heapq.heappush(heap, [max_score, i])
        return -max_score
