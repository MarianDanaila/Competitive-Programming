class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        stack = []
        fib1 = 0
        fib2 = 1
        while fib2 <= k:
            stack.append(fib2)
            fib1, fib2 = fib2, fib1 + fib2

        count = 0
        while k > 0:
            if stack[-1] <= k:
                k -= stack[-1]
                count += 1
            stack.pop()

        return count
