# Approach 1 (BRUTE-FORCE)
# TC: O(2^N)
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        return self.fib(n-1)+self.fib(n-2)


# Approach 2 (MEMOIZATION)
# TC: O(N)
class Solution:
    def fib(self, n: int) -> int:
        cache = {0: 0, 1: 1}

        def recur_fib(n):
            if n in cache:
                return cache[n]
            else:
                result = recur_fib(n-1)+recur_fib(n-2)

            cache[n] = result
            return result
        return recur_fib(n)
