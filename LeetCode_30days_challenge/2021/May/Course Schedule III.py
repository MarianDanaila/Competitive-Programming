import heapq
from typing import List


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        max_heap = []
        time = counter = 0
        for duration, last_day in courses:
            if time + duration <= last_day:
                time += duration
                counter += 1
                heapq.heappush(max_heap, -duration)
            else:
                if max_heap and -max_heap[0] > duration:
                    time -= -max_heap[0] - duration
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap, -duration)
        return counter
