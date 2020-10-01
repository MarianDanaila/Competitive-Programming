# Approach 1 using Binary Search
class RecentCounter:

    def __init__(self):
        self.requests = 0
        self.times = []
        self.l = 0

    def ping(self, t: int) -> int:
        self.times.append(t)
        l = self.l
        r = len(self.times) - 2
        keep = 0
        while l <= r:
            mid = l + (r - l) // 2
            if self.times[mid] == t - 3000:
                return len(self.times) - mid
            elif self.times[mid] > t - 3000:
                r = mid - 1
            else:
                l = mid + 1
                keep = l
        return len(self.times) - keep


# Approach 2 using Deque
from collections import deque


class RecentCounter:

    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q:
            if self.q[0] < t - 3000:
                self.q.popleft()
            else:
                return len(self.q)
