from heapq import heappop, heappush
from typing import List


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        max_heap = []
        minim = deviation = 10 ** 9
        for num in nums:
            if num % 2 != 0:
                num *= 2
            minim = min(minim, num)
            heappush(max_heap, -num)
        maxim = -heappop(max_heap)
        while maxim % 2 == 0:
            deviation = min(deviation, maxim - minim)
            minim = min(minim, maxim // 2)
            heappush(max_heap, -maxim // 2)
            maxim = -heappop(max_heap)
        return min(deviation, maxim - minim)
