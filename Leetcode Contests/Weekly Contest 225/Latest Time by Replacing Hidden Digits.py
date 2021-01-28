class Solution:
    def maximumTime(self, time: str) -> str:
        ans = []
        for ch in time:
            ans.append(ch)
        if time[1] == '?' and time[0] == '?':
            ans[0] = 2
            ans[1] = 3
        elif time[0] == '?':  # ?6:
            if '0' <= time[1] <= '3':
                ans[0] = 2
            else:
                ans[0] = 1
        elif time[1] == '?':
            if '0' <= time[0] <= '1':
                ans[1] = 9
            else:
                ans[1] = 3

        if time[3] == '?':
            ans[3] = 5
        if time[4] == '?':
            ans[4] = 9

        return ''.join(map(str, ans))
