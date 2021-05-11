class Solution:
    def countPrimes(self, n: int) -> int:
        cnt = 0
        sieve = [True] * n
        p = 2
        while p * p < n:
            if sieve[p]:
                for i in range(p * p, n, p):
                    sieve[i] = False
            p += 1
        for i in range(2, n):
            if sieve[i]:
                cnt += 1
        return cnt
