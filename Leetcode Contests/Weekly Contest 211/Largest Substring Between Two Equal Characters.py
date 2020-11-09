class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        substr = {}
        for i in range(len(s)):
            if s[i] not in substr:
                substr[s[i]] = [i, i]
            else:
                substr[s[i]][1] = i

        maximum = -1
        for key in substr:
            maximum = max(maximum, substr[key][1] - substr[key][0] - 1)
        return maximum
