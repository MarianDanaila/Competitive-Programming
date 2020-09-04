# Approach 1 using two dictionaries
from collections import Counter


class Solution:
    def partitionLabels(self, S: str):
        counter = Counter(S)
        dct = {}
        output = []
        length = 0
        for ch in S:
            length += 1
            try:
                dct[ch] += 1
            except KeyError:
                dct[ch] = 1
            if dct[ch] == counter[ch]:
                dct.pop(ch)
            if len(dct) == 0:
                output.append(length)
                length = 0
        return output

# Approach 2 using only one dictionary


class Solution2:
    def partitionLabels(self, S: str):
        last = {}
        for i in range(len(S)):
            last[S[i]] = i  # last index of appearance of character S[i]
        output = []
        start = finish = 0
        for i in range(len(S)):
            finish = max(finish, last[S[i]])
            if i == finish:
                output.append(finish-start+1)
                start = finish + 1
        return output
