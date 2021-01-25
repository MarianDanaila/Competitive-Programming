class Solution:
    def removeCoveredIntervals(self, intervals):
        removed = 0
        intervals.sort(key=lambda x: (x[0], -x[1]))
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][1] <= end:
                removed += 1
            else:
                end = intervals[i][1]
        return len(intervals)-removed
