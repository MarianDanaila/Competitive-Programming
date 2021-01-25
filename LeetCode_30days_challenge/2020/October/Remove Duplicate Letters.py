class Solution:
    def removeDuplicateLetters(self, s):
        last_index = {}
        for i in range(len(s)):
            last_index[s[i]] = i

        result = []
        for i in range(len(s)):
            if s[i] not in result:
                while result and i < last_index[result[-1]] and s[i] < result[-1]:
                    result.pop()
                result.append(s[i])
        return ''.join(result)
