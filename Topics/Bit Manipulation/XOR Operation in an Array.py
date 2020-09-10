class Solution:
    def xorOperation(self, n, start):
        nums = []
        for i in range(n):
            nums[i] = start + 2*i
        ans = nums[0]
        for i in range(1, n):
            ans ^= nums[i]
        return ans
