class Solution:
    def minOperations(self, s: str) -> int:
        first = second = 0
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] != '0':
                    first += 1
                else:
                    second += 1
            else:
                if s[i] != '1':
                    first += 1
                else:
                    second += 1

        return min(first, second)
