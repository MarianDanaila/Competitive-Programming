# Approach 1 using sort
class Solution:
    def findKthLargest(self, nums, k):
        nums.sort()
        return nums[-k]


# Approach 2 using min-heap
import heapq


class Solution:
    def findKthLargest(self, nums, k):
        h = []
        for i in range(len(nums)):
            heapq.heappush(h, nums[i])
            if len(h) > k:
                heapq.heappop(h)
        return heapq.heappop(h)
