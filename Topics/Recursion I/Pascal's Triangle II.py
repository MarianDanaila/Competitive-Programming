from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]

        last_row = self.getRow(rowIndex - 1)
        length = len(last_row)
        return [1] + [last_row[idx] + last_row[idx + 1] for idx in range(length - 1)] + [1]
