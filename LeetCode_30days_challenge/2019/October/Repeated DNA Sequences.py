class Solution:
    def findRepeatedDnaSequences(self, s: str):
        ans = []
        substrings = {}
        for i in range(len(s) - 9):
            if s[i:i + 10] not in substrings:
                substrings[s[i:i + 10]] = 1
            else:
                substrings[s[i:i + 10]] += 1

        for substring in substrings:
            if substrings[substring] > 1:
                ans.append(substring)

        return ans
