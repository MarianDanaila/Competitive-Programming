from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        intersection_end = points[0][1]
        arrows = 1
        for start, end in points:
            if start <= intersection_end:
                intersection_end = min(intersection_end, end)
            else:
                arrows += 1
                intersection_end = end
        return arrows
