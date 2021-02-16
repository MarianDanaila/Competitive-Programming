import heapq
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans = [0] * k
        soldiers = {}
        n = len(mat)
        m = len(mat[0])
        max_heap = []
        length_heap = 0
        for i in range(n):  # O(N)
            low = 0
            high = m - 1
            cnt = -1
            while low <= high:  # O(log M)
                mid = low + (high - low) // 2
                if mat[i][mid] == 1:
                    cnt = mid
                    low = mid + 1
                else:
                    high = mid - 1
            cnt += 1
            if length_heap < k:
                if -cnt not in max_heap:
                    heapq.heappush(max_heap, -cnt)
                length_heap += 1
                if cnt in soldiers:
                    soldiers[cnt].append(i)
                else:
                    soldiers[cnt] = [i]
            else:
                maxim = -max_heap[0]
                if cnt < maxim:
                    if len(soldiers[maxim]) == 1:
                        heapq.heappop(max_heap)
                    else:
                        soldiers[maxim].pop()

                    if -cnt not in max_heap:
                        heapq.heappush(max_heap, -cnt)

                    if cnt in soldiers:
                        soldiers[cnt].append(i)
                    else:
                        soldiers[cnt] = [i]

        for i in range(len(max_heap)):
            maxim = -heapq.heappop(max_heap)
            for j in range(len(soldiers[maxim]) - 1, -1, -1):
                ans[k - 1] = soldiers[maxim][j]
                k -= 1
        return ans
