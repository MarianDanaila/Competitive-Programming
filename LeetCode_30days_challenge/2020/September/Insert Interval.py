class Solution:
    def insert(self, intervals, newInterval):
        # case when intervals is empty
        if len(intervals) == 0:
            return [newInterval]
        mergeIntervals = []
        start = newInterval[0]
        end = newInterval[1]
        overlap = False
        i = 0
        # case when end of newInterval is less than start of the first interval
        if end < intervals[0][0]:
            mergeIntervals.append(newInterval)
            overlap = True
        while i < len(intervals):
            # case when newInterval doesn't overlap with one interval from intervals
            if intervals[i][0] > end and not overlap:
                mergeIntervals.append(newInterval)
                overlap = True
            if intervals[i][0] <= start <= intervals[i][1] or intervals[i][0] <= end <= intervals[i][1] or (
                    start < intervals[i][0] and end > intervals[i][1]):
                overlap = True
                startMerge = min(start, intervals[i][0])
                endMerge = max(end, intervals[i][1])

                i += 1
                while i < len(intervals):
                    if end < intervals[i][0]:
                        break
                    endMerge = max(end, intervals[i][1])
                    i += 1
                mergeIntervals.append([startMerge, endMerge])
                if i < len(intervals):
                    mergeIntervals.append(intervals[i])
            else:
                mergeIntervals.append(intervals[i])
            i += 1
        # case when start of newInterval is greater than end of the last interval
        if start > intervals[-1][1]:
            mergeIntervals.append(newInterval)

        return mergeIntervals
