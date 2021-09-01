from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(profit)
        jobs = []
        for i in range(n):
            jobs.append([startTime[i], endTime[i], profit[i]])

        jobs.sort(key=lambda x: x[1])
        dp = [0] * n
        dp[0] = jobs[0][2]
        for i in range(1, n):
            include_job = jobs[i][2]
            # check previous job not overlapped
            low, high, job_idx = 0, i - 1, -1
            while low <= high:
                mid = low + (high - low) // 2
                if jobs[mid][1] <= jobs[i][0]:
                    job_idx = mid
                    low = mid + 1
                else:
                    high = mid - 1
            if job_idx != -1:
                include_job += dp[job_idx]
            dp[i] = max(include_job, dp[i - 1])
        return dp[-1]
