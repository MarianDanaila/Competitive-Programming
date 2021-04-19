import heapq
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        heap = []
        dp = {}
        for num in nums:
            if num <= target:
                dp[num] = 1
                heapq.heappush(heap, num)
            else:
                break

        while heap:
            curr = heapq.heappop(heap)
            for num in nums:
                if curr + num > target:
                    break
                else:
                    if curr + num not in dp:
                        dp[curr + num] = dp[curr]
                        heapq.heappush(heap, curr + num)
                    else:
                        dp[curr + num] += dp[curr]
        if target not in dp:
            return 0
        return dp[target]
