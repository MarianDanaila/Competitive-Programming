from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        start = end = 0
        visited = set()
        max_score = curr_score = 0
        while end < n:
            if nums[end] in visited:
                max_score = max(max_score, curr_score)
                while nums[start] != nums[end]:
                    curr_score -= nums[start]
                    visited.remove(nums[start])
                    start += 1
                curr_score -= nums[start]
                visited.remove(nums[start])
                start += 1

            else:
                visited.add(nums[end])
                curr_score += nums[end]
                end += 1

        return max(max_score, curr_score)
