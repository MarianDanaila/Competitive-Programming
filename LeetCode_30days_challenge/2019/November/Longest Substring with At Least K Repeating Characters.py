from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        self.ans = 0

        def divide(string):
            bad_idx = [-1]
            counter = Counter(string)
            for i in range(len(string)):
                if counter[string[i]] < k:
                    bad_idx.append(i)
            bad_idx.append(len(string)+1)
            if len(bad_idx) == 2:
                self.ans = max(self.ans, len(string))
            else:
                for i in range(len(bad_idx)-1):
                    if bad_idx[i] == len(string)-1:
                        break
                    divide(string[bad_idx[i]+1:bad_idx[i+1]])
        divide(s)
        return self.ans
