from typing import List


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        users = {}
        answer = [0] * k
        for idd, time in logs:
            if idd not in users:
                users[idd] = set()
                users[idd].add(time)
            else:
                users[idd].add(time)

        for user in users:
            answer[len(users[user]) - 1] += 1
        return answer
