class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        k = 0
        while target > 0:
            k += 1
            target -= k
        delta = -target
        if delta % 2 == 0:
            return k
        else:
            if (k + 1) % 2 == 0:
                return k + 2
            else:
                return k + 1
