from collections import Counter


class Solution:
    def countPairs(self, deliciousness):
        n = len(deliciousness)
        good = 0
        freq = Counter(deliciousness)
        deliciousness.sort()
        d = [deliciousness[0]]
        for i in range(1, n):
            if deliciousness[i] != deliciousness[i - 1]:
                d.append(deliciousness[i])
        length_d = len(d)
        if length_d == 1:
            if d[0] & (d[0] - 1) == 0 and d[0] != 0:
                return (freq[d[0]] * (freq[d[0]] - 1) // 2) % (10 ** 9 + 7)

        for i in range(length_d):
            if d[i] & (d[i] - 1) == 0 and d[i] != 0:
                good += freq[d[i]] * (freq[d[i]] - 1) // 2
            for power in range(21):
                target = 2 ** power - d[i]
                if target == d[i]:
                    continue
                if target in freq:
                    good += freq[d[i]] * freq[target]
            freq.pop(d[i])
        return good % (10 ** 9 + 7)
