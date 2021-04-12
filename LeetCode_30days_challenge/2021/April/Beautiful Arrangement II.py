from typing import List


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        out = [1]
        plus = True
        for i in range(k, 0, -1):
            last = out[-1]
            if plus:
                out.append(last + i)
                plus = False
            else:
                out.append(last - i)
                plus = True
        maxim = out[1]
        for i in range(maxim + 1, n+1):
            out.append(i)
        return out
