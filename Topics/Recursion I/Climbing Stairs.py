class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {0: 1, 1: 1}

        def recur(n):
            if n in cache:
                return cache[n]
            else:
                result = recur(n - 1) + recur(n - 2)

            cache[n] = result
            return result

        return recur(n)
