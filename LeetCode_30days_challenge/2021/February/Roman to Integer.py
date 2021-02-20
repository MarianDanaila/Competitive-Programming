class Solution:
    def romanToInt(self, s: str) -> int:
        dct = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        integer = 0
        n = len(s)
        sub = 0
        for i in range(n - 1):
            if sub > 0:
                integer += dct[s[i]] - sub
                sub = 0
                continue
            if dct[s[i]] >= dct[s[i + 1]]:
                integer += dct[s[i]]
            else:
                sub = dct[s[i]]

        if sub > 0:
            integer += dct[s[-1]] - dct[s[-2]]
        else:
            integer += dct[s[-1]]
        return integer
