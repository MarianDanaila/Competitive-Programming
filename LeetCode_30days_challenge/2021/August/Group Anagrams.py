from typing import List

# Approach 1
# Time-complexity: O(N * M(logM)) where N is the length of strings array and M length of a string


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string not in groups:
                groups[sorted_string] = [string]
            else:
                groups[sorted_string].append(string)

        answer = []
        for key in groups:
            answer.append(groups[key])
        return answer


# Approach 2
# Time-complexity: O(N * M) where N is the length of strings array and M length of a string
class Solution:
    def groupAnagrams(self, strs: List[str]):
        groups = {}
        for string in strs:
            alphabet = [0] * 26
            for ch in string:
                alphabet[ord(ch) - 97] += 1
            key = " ".join(map(str, alphabet))
            if key in groups:
                groups[key].append(string)
            else:
                groups[key] = [string]
        return groups.values()
