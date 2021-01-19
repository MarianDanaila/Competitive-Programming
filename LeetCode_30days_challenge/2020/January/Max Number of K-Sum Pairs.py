# Approach 1 using Sorting and Two Pointers
# TC: O(N log N) where N is length of the nums array
class Solution:
    def maxOperations(self, nums, k):
        nums.sort()
        i = 0
        j = len(nums)-1
        operations = 0
        while i < j:
            if nums[i] + nums[j] == k:
                operations += 1
                i += 1
                j -= 1
            elif nums[i] + nums[j] < k:
                i += 1
            else:
                j -= 1
        return operations


# Approach 2 using HashMap
# TC: O(N) where N is length of the nums array
from collections import Counter


class Solution:
    def maxOperations(self, nums, k):
        counter = Counter(nums)
        operations = 0
        for key in counter:
            if k - key in counter:
                if k == 2 * key:
                    operations += counter[key] // 2
                else:
                    operations += min(counter[key], counter[k - key])
                    counter[key] = 0
        return operations
