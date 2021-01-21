class Solution:
    def longestPalindrome(self, s):
        def expand(s, l, r):
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]

        n = len(s)
        max_length = 1
        ans = s[0]
        for i in range(n - 1):
            string = expand(s, i, i)
            if len(string) > max_length:
                max_length = len(string)
                ans = string

            string = expand(s, i, i + 1)
            if len(string) > max_length:
                max_length = len(string)
                ans = string
        return ans
