from heapq import heappush, heappop
from typing import List


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        heap = []
        x = 0
        for t in target:
            heappush(heap, -t)
            x -= t
        while heap[0] != -1:
            minim = heappop(heap)
            x -= minim
            if minim >= x or x > -1:
                return False
            minim %= x
            x += minim
            heappush(heap, minim or x)
        return True
