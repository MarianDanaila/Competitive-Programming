class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        if k > n:
            return False
        numbers = set()
        limit = 2 ** k
        for i in range(limit):
            numbers.add(i)

        curr = 0
        for i in range(k):
            curr *= 2
            if s[i] == '1':
                curr += 1

        if curr in numbers:
            numbers.remove(curr)

        end = k
        while end < n:
            if s[end - k] == '1':
                curr -= 2 ** (k - 1)
            curr *= 2
            if s[end] == '1':
                curr += 1
            if curr in numbers:
                numbers.remove(curr)
            end += 1

        return len(numbers) == 0
