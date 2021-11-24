from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j = 0
        n, m = len(firstList), len(secondList)
        output = []
        while i < n and j < m:
            first = None
            if secondList[j][0] <= firstList[i][0] <= secondList[j][1]:
                first = firstList[i][0]
            elif firstList[i][0] <= secondList[j][0] <= firstList[i][1]:
                first = secondList[j][0]
            if firstList[i][1] < secondList[j][1]:
                second = firstList[i][1]
                i += 1
            elif firstList[i][1] > secondList[j][1]:
                second = secondList[j][1]
                j += 1
            else:
                second = firstList[i][1]
                i += 1
                j += 1
            if first is not None:
                output.append([first, second])
        return output
