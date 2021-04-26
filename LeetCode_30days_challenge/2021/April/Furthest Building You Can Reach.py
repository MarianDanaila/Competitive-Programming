import heapq
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        max_heap = []
        n = len(heights)
        sum_diff = 0
        for i in range(1, n):
            diff = heights[i] - heights[i-1]
            if diff > 0:
                heapq.heappush(max_heap, -diff)
                sum_diff += diff
                if sum_diff > bricks:
                    if ladders == 0:
                        return i-1
                    ladders -= 1
                    maximum = -heapq.heappop(max_heap)
                    sum_diff -= maximum
        return n - 1
