# The answer is the 2 * (number of ones) + number of zeroes - 1
class Solution:
    def numberOfSteps(self, num):
        if num == 0:
            return 0
        steps = 0
        while num > 1:
            if num % 2 == 0:
                steps += 1
            else:
                steps += 2
            num //= 2
        return steps + 1
