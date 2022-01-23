from collections import deque
from typing import List


class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[
        List[int]]:
        m, n = len(grid), len(grid[0])
        dq = deque()
        visited = set()
        visited.add((start[0], start[1]))
        dq.append([start[0], start[1]])
        items = []
        steps = 0
        ans = []
        if pricing[0] <= grid[start[0]][start[1]] <= pricing[1]:
            items.append([0, grid[start[0]][start[1]], start[0], start[1]])
        while dq:
            steps += 1
            len_dq = len(dq)
            for _ in range(len_dq):
                curr_x, curr_y = dq.popleft()
                if curr_x - 1 >= 0 and (curr_x - 1, curr_y) not in visited and grid[curr_x - 1][curr_y] != 0:
                    dq.append([curr_x - 1, curr_y])
                    visited.add((curr_x - 1, curr_y))
                    if pricing[0] <= grid[curr_x - 1][curr_y] <= pricing[1]:
                        items.append([steps, grid[curr_x - 1][curr_y], curr_x - 1, curr_y])

                if curr_y + 1 < n and (curr_x, curr_y + 1) not in visited and grid[curr_x][curr_y + 1] != 0:
                    dq.append([curr_x, curr_y + 1])
                    visited.add((curr_x, curr_y + 1))
                    if pricing[0] <= grid[curr_x][curr_y + 1] <= pricing[1]:
                        items.append([steps, grid[curr_x][curr_y + 1], curr_x, curr_y + 1])

                if curr_x + 1 < m and (curr_x + 1, curr_y) not in visited and grid[curr_x + 1][curr_y] != 0:
                    dq.append([curr_x + 1, curr_y])
                    visited.add((curr_x + 1, curr_y))
                    if pricing[0] <= grid[curr_x + 1][curr_y] <= pricing[1]:
                        items.append([steps, grid[curr_x + 1][curr_y], curr_x + 1, curr_y])

                if curr_y - 1 >= 0 and (curr_x, curr_y - 1) not in visited and grid[curr_x][curr_y - 1] != 0:
                    dq.append([curr_x, curr_y - 1])
                    visited.add((curr_x, curr_y - 1))
                    if pricing[0] <= grid[curr_x][curr_y - 1] <= pricing[1]:
                        items.append([steps, grid[curr_x][curr_y - 1], curr_x, curr_y - 1])

        items.sort(key=lambda x: [x[0], x[1], x[2], x[3]])
        for item in items:
            ans.append([item[2], item[3]])
            k -= 1
            if k == 0:
                break
        return ans
