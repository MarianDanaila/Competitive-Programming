from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        width_sum = sum(wall[0])
        edges = {}
        for row in wall:
            sum_row = 0
            for brick in row:
                sum_row += brick
                if sum_row < width_sum:
                    if sum_row in edges:
                        edges[sum_row] += 1
                    else:
                        edges[sum_row] = 1
        max_edges = 0
        for edge in edges:
            if edges[edge] > max_edges:
                max_edges = edges[edge]
        return len(wall) - max_edges
