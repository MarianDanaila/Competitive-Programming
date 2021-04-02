from typing import List


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = []
        for i in range(m):
            P.append(i + 1)
        print(P)
        output = []
        for i in range(len(queries)):
            position = P.index(queries[i])
            output.append(position)
            P.pop(position)
            P.insert(0, queries[i])
        return output
