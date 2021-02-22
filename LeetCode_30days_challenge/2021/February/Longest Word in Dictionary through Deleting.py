from typing import List


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        max_length = 0
        longest = ""
        n = len(s)
        for string in d:
            i = 0
            j = 0
            m = len(string)
            while i < m and j < n:
                if string[i] == s[j]:
                    i += 1
                j += 1
            if i == m:
                if m > max_length:
                    max_length = m
                    longest = string
                elif m == max_length:
                    longest = min(longest, string)
        return longest
