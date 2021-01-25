class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        start = 0
        end = 0
        max_length = 0
        while end < len(s):
            if s[end] in freq:
                while s[start] != s[end]:
                    freq.pop(s[start])
                    start += 1
                freq.pop(s[start])
                start += 1
            else:
                freq[s[end]] = 1
                end += 1
                max_length = max(max_length, end-start)
        return max_length
