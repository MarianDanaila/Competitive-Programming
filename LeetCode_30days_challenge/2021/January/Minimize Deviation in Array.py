import heapq


class Solution:
    def minimumDeviation(self, nums) -> int:
        res = minim = 10 ** 9
        pq = []
        for num in nums:
            if num % 2 == 1:
                num *= 2
            minim = min(minim, num)
            pq.append(-num)

        heapq.heapify(pq)
        maxim = -heapq.heappop(pq)
        while maxim % 2 == 0:
            res = min(res, maxim - minim)
            minim = min(minim, maxim // 2)
            heapq.heappush(pq, -maxim // 2)
            maxim = -heapq.heappop(pq)
        return min(res, maxim - minim)
