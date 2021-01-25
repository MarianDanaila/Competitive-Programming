# Kadane's algorithm
# Time-complexity: O(N)
class Solution:
    def maxProduct(self, nums) -> int:
        prefix = suffix = 0
        max_product = -float("inf")
        for i in range(len(nums)):
            prefix = (prefix or 1) * nums[i]
            suffix = (suffix or 1) * nums[-1-i]
            max_product = max(prefix, suffix, max_product)
        return max_product
