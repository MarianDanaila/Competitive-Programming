from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        rows = [[1], [1, 1]]
        for i in range(2, numRows):
            row = [1]
            for j in range(1, i):
                row.append(rows[-1][j] + rows[-1][j - 1])
            row.append(1)
            rows.append(row)
        return rows
