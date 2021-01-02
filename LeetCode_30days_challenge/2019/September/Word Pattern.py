class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        bijection = {}
        strings = string.split(" ")
        if len(strings) != len(pattern):
            return False
        for i in range(len(strings)):
            try:
                if bijection[pattern[i]] != strings[i]:
                    return False
            except KeyError:
                for el in bijection:
                    if bijection[el] == strings[i]:
                        return False
                bijection[pattern[i]] = strings[i]
        return True
