class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        odd = False
        length = 0
        counter = Counter(s)
        for count in counter:
            if counter[count] % 2 != 0:
                odd = True
            if counter[count] > 1:
                length += counter[count] - counter[count] % 2
        if odd:
            return length + 1
        return length
