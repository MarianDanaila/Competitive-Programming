from collections import deque
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        dq = deque()
        dq.append(0)
        visited = set()
        visited.add(0)
        jumps = 0
        while dq:
            jumps += 1
            length = len(dq)
            for _ in range(length):
                curr = dq.popleft()
                max_jumps = nums[curr]
                for i in range(1, max_jumps + 1):
                    nxt_jump = curr + i
                    if nxt_jump == n - 1:
                        return jumps
                    if nxt_jump not in visited:
                        visited.add(nxt_jump)
                        dq.append(nxt_jump)
