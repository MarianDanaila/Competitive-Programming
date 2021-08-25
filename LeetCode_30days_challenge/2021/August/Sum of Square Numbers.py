import math


# Approach 1 using sqrt function
# Time complexity: O(sqrt(c) * log(c))
# Space complexity: O(1)
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        limit = int(math.sqrt(c) + 1)
        for i in range(limit):
            target = c - i * i
            if int(math.sqrt(target)) == math.sqrt(target):
                return True
        return False


# Approach 2 using Set
# Time complexity: O(sqrt(c))
# Space complexity: O(sqrt(c))
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squares = set()
        i = 0
        while i * i <= c:
            squares.add(i * i)
            i += 1

        for square in squares:
            if c - square in squares:
                return True
        return False
