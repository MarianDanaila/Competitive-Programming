class Solution:
    def mostCompetitive(self, nums, k: int):
        stack = []
        n = len(nums)
        for i in range(n):
            while stack and stack[-1] > nums[i] and len(stack)-1+n-i >= k:
                stack.pop()
            if len(stack) < k:
                stack.append(nums[i])
        return stack
