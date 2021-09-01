from typing import List
from collections import deque
# Approach 1: Using a set for tracking the visited indexes and a deque


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        longest_length = 1
        visited = set()
        for i in range(n):
            if i not in visited:
                # start bfs
                dq = deque()
                dq.append(i)
                curr_length = 1
                visited.add(i)
                while dq:
                    index = dq.popleft()
                    next_index = nums[index]
                    if next_index not in visited:
                        visited.add(next_index)
                        dq.append(next_index)
                    else:
                        longest_length = max(longest_length, curr_length)
                    curr_length += 1
        return longest_length


# Approach 2: Using only a set for tracking the visited indexes
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        longest_length = 1
        visited = set()
        for i in range(n):
            if i not in visited:
                # start bfs
                curr_length = 1
                visited.add(i)
                index = nums[i]
                while index not in visited:
                    visited.add(index)
                    curr_length += 1
                    index = nums[index]
                longest_length = max(longest_length, curr_length)
        return longest_length


# Approach 3: Instead of using a set to keep track of visited nodes, we can change a value from nums array to n
# (which is the length of the array). We can also use infinity for example.
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        longest_length = 1
        for i in range(n):
            if nums[i] != n:
                curr_length = 1
                index = nums[i]
                nums[i] = n
                while nums[index] != n:
                    curr_length += 1
                    next_index = nums[index]
                    nums[index] = n
                    index = next_index
                longest_length = max(longest_length, curr_length)
        return longest_length
