from math import sqrt
from heapq import heappushpop, heappush
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            curr_distance = -sqrt(x * x + y * y)
            if len(heap) < k:
                heappush(heap, [curr_distance, x, y])
            else:
                minim, _, _ = heap[0]
                if curr_distance > minim:
                    heappushpop(heap, [curr_distance, x, y])
        result = []
        for distance, x, y in heap:
            result.append([x, y])
        return result
