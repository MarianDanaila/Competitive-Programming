import math


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        lst = []
        for i in range(lo, hi + 1):
            power = 0
            number = i
            while i != 1:
                power += 1
                if i & (i - 1) == 0:
                    power += math.log2(i)
                    break
                if i % 2 == 0:
                    i //= 2
                else:
                    i = i * 3 + 1
            lst.append([number, power])
        lst.sort(key=lambda x: (x[1], x[0]))
        return lst[k - 1][0]
