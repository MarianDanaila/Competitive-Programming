from collections import Counter
from heapq import heappop, heappush, heapify


class Solution:
    def maxSlidingWindow(self, nums, k: int):
        n = len(nums)
        window = [0] * k
        for i in range(k - 1, -1, -1):
            window[i] = -nums[i]
        occ = Counter(window)
        ans = []
        heapify(window)
        ans.append(-window[0])
        for i in range(k, n):
            last = -nums[i]
            first = -nums[i - k]
            if last not in occ:
                occ[last] = 1
            else:
                occ[last] += 1
            occ[first] -= 1
            heappush(window, last)
            while True:
                maxim = window[0]
                if occ[maxim] > 0:
                    ans.append(-maxim)
                    break
                else:
                    heappop(window)
        return ans
