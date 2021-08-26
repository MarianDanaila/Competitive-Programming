from collections import deque
from typing import List


# Approach 1: BFS
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dq = deque()
        dq.append(0)
        visited = set()
        visited.add(0)
        n = len(nums)
        if n == 1:
            return True
        while dq:
            curr_idx = dq.popleft()
            for i in range(curr_idx + 1, curr_idx + nums[curr_idx] + 1):
                if i not in visited:
                    if i == n - 1:
                        return True
                    visited.add(i)
                    dq.append(i)
        return False


# Approach 2: From end to start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        destination = n - 1
        for i in range(n - 2, -1, -1):
            if destination - i <= nums[i]:
                destination = i
        return destination == 0


# Approach 3: From start to end
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_idx = 0
        for i in range(n):
            max_idx = max(max_idx, i + nums[i])
            if max_idx >= n - 1:
                return True
            if max_idx == i:
                return False
