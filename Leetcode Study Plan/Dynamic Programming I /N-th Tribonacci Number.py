class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        first, second, third = 0, 1, 1
        for i in range(3, n + 1):
            first, second, third = second, third, third + second + first
        return third
