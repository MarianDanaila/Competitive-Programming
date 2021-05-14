from typing import List


class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        n = len(s)
        coord = []
        for comma in range(2, n - 1):
            first = s[:comma]
            second = s[comma:]
            f = []
            sc = []
            if first == "(0":
                f.append(first)
            elif first[1] == '0' and first[-1] != '0':
                f.append(first[:2] + "." + first[2:])
            elif first[1] != '0' and first[-1] == '0':
                f.append(first)
            elif first[1] != '0' and first[-1] != '0':
                m = len(first)
                f.append(first)
                for i in range(2, m):
                    f.append(first[:i] + "." + first[i:])

            if second == "0)":
                sc.append(second)
            elif second[0] == '0' and second[-2] != '0':
                sc.append(second[0] + "." + second[1:])
            elif second[0] != '0' and second[-2] == '0':
                sc.append(second)
            elif second[0] != '0' and second[-2] != '0':
                m = len(second)
                sc.append(second)
                for i in range(1, m - 1):
                    sc.append(second[:i] + "." + second[i:])
            for coord1 in f:
                for coord2 in sc:
                    coord.append(coord1 + ", " + coord2)
        return coord
