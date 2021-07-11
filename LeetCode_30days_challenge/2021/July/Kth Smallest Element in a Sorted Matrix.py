from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        elements = []
        for row in matrix:
            for element in row:
                elements.append(element)
        elements.sort()
        return elements[k - 1]
