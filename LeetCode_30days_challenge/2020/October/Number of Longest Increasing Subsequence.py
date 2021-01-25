class Solution:
    def findNumberOfLIS(self, nums):
        n = len(nums)
        if n <= 1:
            return n
        lengths = [0] * n
        counts = [1] * n
        for j in range(1, n):
            for i in range(j):
                if nums[i] < nums[j]:
                    if lengths[i] >= lengths[j]:
                        lengths[j] = lengths[i] + 1
                        counts[j] = counts[i]
                    elif lengths[i] + 1 == lengths[j]:
                        counts[j] += counts[i]
        max_length = max(lengths)
        number = 0
        for i in range(n):
            if lengths[i] == max_length:
                number += counts[i]
        return number
