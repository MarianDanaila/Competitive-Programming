class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return "".join(map(str, sorted(s)))
        else:
            n = len(s)
            smallest = s
            for i in range(1, n):
                string = s[i:] + s[:i]
                if smallest > string:
                    smallest = string
            return smallest
