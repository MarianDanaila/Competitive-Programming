from collections import Counter


class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        bucket = [[] for _ in range(9)]
        counter = Counter(str(N))
        for i in range(30):
            nr = 2 ** i
            length = len(str(nr))
            bucket[length - 1].append(nr)

        length = len(str(N))
        for nr in bucket[length - 1]:
            if Counter(str(nr)) == counter:
                return True
        return False
