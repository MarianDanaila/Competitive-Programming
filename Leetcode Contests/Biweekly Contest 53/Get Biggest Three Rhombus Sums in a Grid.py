import heapq
from typing import List


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        m = len(grid[0])
        length = min(n, m)
        if length % 2 == 0:
            length -= 1
        heap = []
        ans = []
        visited = set()
        while length > 0:
            for x in range(length // 2, n - length // 2):  # range for starting x
                for y in range(m - length + 1):  # range for starting y
                    curr_sum = 0
                    curr_x = x
                    curr_y = y
                    for _ in range(length // 2 + 1):
                        curr_sum += grid[curr_x][curr_y]
                        curr_x -= 1
                        curr_y += 1
                    curr_x += 2
                    for _ in range(length // 2):
                        curr_sum += grid[curr_x][curr_y]
                        curr_x += 1
                        curr_y += 1
                    curr_y -= 2
                    for _ in range(length // 2):
                        curr_sum += grid[curr_x][curr_y]
                        curr_x += 1
                        curr_y -= 1
                    curr_x -= 2
                    for _ in range(length // 2 - 1):
                        curr_sum += grid[curr_x][curr_y]
                        curr_x -= 1
                        curr_y -= 1
                    if curr_sum not in visited:
                        visited.add(curr_sum)
                        heapq.heappush(heap, -curr_sum)
            length -= 2
        for _ in range(3):
            if heap:
                ans.append(-heapq.heappop(heap))
        return ans
