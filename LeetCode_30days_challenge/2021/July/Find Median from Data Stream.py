from heapq import *


class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num):
        heappush(self.small, -heappushpop(self.large, num))
        if len(self.small) > len(self.large):
            heappush(self.large, -heappop(self.small))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0]) / 2
        else:
            return self.large[0]
