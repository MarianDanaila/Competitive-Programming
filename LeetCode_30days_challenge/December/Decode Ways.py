class Solution:
    def numDecodings(self, s: str) -> int:
        if s[-1] == '0':
            first = 0
        else:
            first = 1
        second = 1
        for i in range(len(s) - 2, -1, -1):
            if s[i] == '0':
                first, second = 0, first
            elif (s[i] == '1' and '0' <= s[i + 1] <= '9') or (s[i] == '2' and '0' <= s[i + 1] <= '6'):
                first, second = first + second, first
            else:
                second = first
            if first == 0 and second == 0:
                return 0
        return first
