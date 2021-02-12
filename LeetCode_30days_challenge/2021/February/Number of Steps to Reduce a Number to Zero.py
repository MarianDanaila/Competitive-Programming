class Solution:
    def numberOfSteps (self, num: int) -> int:
        steps = 0
        while num > 0:
            if num % 2 == 0:
                steps += 1
            else:
                steps += 2
            num //= 2
        return max(steps-1, 0)
