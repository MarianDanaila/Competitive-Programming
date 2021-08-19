class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        first, second = 1, 1
        n = len(s)
        for i in range(1, n):
            if s[i] == '0':
                if s[i - 1] == '1' or s[i - 1] == '2':
                    second = first
                    first = 0
                else:
                    return 0

            elif s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6'):
                first, second = second, second + first
            else:
                first = second
        return second
