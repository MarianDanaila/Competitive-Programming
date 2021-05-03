# Brute-Force: O(N ^ 3) where N - length of s
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        max_length = 0
        ans = ""
        for i in range(n - 1):
            for j in range(i + 1, n):
                good = True
                substring = s[i:j + 1]
                set_ch = set()
                for ch in substring:
                    if ch not in set_ch:
                        set_ch.add(ch)

                for ch in set_ch:
                    if 'a' <= ch <= 'z':
                        other_ch = chr(ord(ch) - 32)
                    else:
                        other_ch = chr(ord(ch) + 32)
                    if other_ch not in set_ch:
                        good = False
                        break
                if good:
                    if j - i > max_length:
                        max_length = j - i
                        ans = s[i:j + 1]

        return ans


# Optimized: O(N ^ 2)
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        start = end = 0
        for i in range(n - 1):
            set_ch = {s[i]}
            deleted = set()
            for j in range(i + 1, n):
                ch = s[j]
                if 'a' <= ch <= 'z':
                    other_ch = chr(ord(ch) - 32)
                else:
                    other_ch = chr(ord(ch) + 32)

                if other_ch in deleted or ch in deleted:
                    if not set_ch and j - i > end - start:
                        end = j
                        start = i
                    continue
                if ch not in set_ch:
                    if other_ch in set_ch:
                        set_ch.remove(other_ch)
                        if not set_ch and j - i > end - start:
                            end = j
                            start = i
                        deleted.add(ch)
                    else:
                        set_ch.add(ch)
        if start == end:
            return ""
        return s[start:end + 1]
