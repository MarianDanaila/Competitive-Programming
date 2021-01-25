# Approach 1 using Binary Search and sorting
# Time-complexity: O(NlogN)
class Solution:
    def findPairs(self, nums, k):
        nums.sort()
        cnt = 0
        for i in range(len(nums)):
            if i > 0:
                if nums[i] == nums[i - 1]:
                    continue
            low = i + 1
            right = len(nums) - 1
            while low <= right:
                mid = low + (right - low) // 2
                if nums[mid] == nums[i] + k:
                    cnt += 1
                    break
                elif nums[mid] < nums[i] + k:
                    low = mid + 1
                else:
                    right = mid - 1
        return cnt


# Approach 2 using HashMap
# Time-complexity: O(N)
import collections


class Solution:
    def findPairs(self, nums, k):
        cnt = 0
        freq = collections.Counter(nums)
        if k == 0:
            for key in freq:
                if freq[key] >= 2:
                    cnt += 1
            return cnt
        else:
            for key in freq:
                if key+k in freq:
                    cnt += 1
            return cnt
