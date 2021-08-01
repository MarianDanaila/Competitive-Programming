class Solution:
    def isThree(self, n: int) -> bool:
        divisors = 0
        for divisor in range(1, int(n ** 0.5) + 1):
            if n % divisor == 0:
                if n // divisor == divisor:
                    divisors += 1
                else:
                    divisors += 2
                    if divisors > 3:
                        return False
        return divisors == 3
