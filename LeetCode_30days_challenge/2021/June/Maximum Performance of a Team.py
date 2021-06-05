import heapq
from typing import List


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        candidates = []
        for i in range(n):
            candidates.append([speed[i], efficiency[i]])
        candidates.sort(key=lambda x: x[1], reverse=True)
        speed_heap = []
        speed_sum = performance = 0
        for curr_speed, curr_efficiency in candidates:
            if len(speed_heap) > k - 1:
                speed_sum -= heapq.heappop(speed_heap)
            heapq.heappush(speed_heap, curr_speed)
            speed_sum += curr_speed
            performance = max(performance, curr_efficiency * speed_sum)
        return performance % (10 ** 9 + 7)
