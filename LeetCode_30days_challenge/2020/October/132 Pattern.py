# Approach 1: Brute Force
# Time-complexity: O(N^2)
# Space-complexity: O(1)
class Solution:
    def find132pattern(self, nums):
        min_i = float("inf")
        n = len(nums)
        for j in range(n-1):
            min_i = min(min_i, nums[j])
            for k in range(j+1, n):
                if min_i < nums[k] < nums[j]:
                    return True
        return False


# Approach 2: Searching Intervals
# Time-complexity: O(N^2)
# Space-complexity: O(N)

class Solution:
    def find132pattern(self, nums):
        intervals = []
        i = 1
        s = 0
        while i < len(nums):
            if nums[i] < nums[i-1]:
                if s < i-1:
                    intervals.append([nums[s], nums[i-1]])
                s = i

            for interval in intervals:
                if interval[0] < nums[i] < interval[1]:
                    return True

            i += 1
        return False

# Approach 3: Using Stack


class Solution:
    def find132pattern(self, nums):
        n = len(nums)
        stack = []
        min_arr = [nums[0]] * n
        for i in range(1, n):
            min_arr[i] = min(min_arr[i - 1], nums[i])
        for i in range(n - 1, -1, -1):
            if nums[i] > min_arr[i]:
                while stack and stack[-1] <= min_arr[i]:
                    stack.pop()

                if stack and stack[-1] < nums[i]:
                    return True

                stack.append(nums[i])
        return False
