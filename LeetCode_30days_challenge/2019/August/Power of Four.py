# Approach 1 Iterative
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        while num % 4 == 0 and num > 1:
            num /= 4
        return num == 1

# Approach 2 Bit Manipulation
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and (num & (num - 1)) == 0 and (num - 1) % 3 == 0

sol = Solution()
print(sol.isPowerOfFour(4))