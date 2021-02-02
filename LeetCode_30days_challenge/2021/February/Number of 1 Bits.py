# Approach 1 by checking all bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        ones = 0
        while n > 0:
            if n % 2 == 1:
                ones += 1
            n //= 2
        return ones


# Approach 2 by checking just all 1 bits
class Solution:
    def hammingWeight(self, n: int) -> int:
        ones = 0
        while n != 0:
            ones += 1
            n &= (n - 1)

        return ones
