from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged_start, merged_end = intervals[0]
        merged_intervals = []
        for start, end in intervals:
            if start <= merged_end:
                merged_end = max(merged_end, end)
            else:
                merged_intervals.append([merged_start, merged_end])
                merged_start, merged_end = start, end
        merged_intervals.append([merged_start, merged_end])
        return merged_intervals
