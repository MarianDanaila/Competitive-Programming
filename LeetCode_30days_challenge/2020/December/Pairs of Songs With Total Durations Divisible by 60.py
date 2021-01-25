class Solution:
    def numPairsDivisibleBy60(self, time):
        dct = {}
        n = len(time)
        for i in range(n):
            el = time[i] % 60
            if el not in dct:
                dct[el] = 1
            else:
                dct[el] += 1
        pairs = 0
        for key in dct:
            if key == 0 or key == 30:
                pairs += (dct[key]*(dct[key]-1)) // 2
            else:
                if 60-key in dct and dct[60-key] > 0:
                    pairs += dct[key] * dct[60-key]
                    dct[key] = 0
        return pairs
