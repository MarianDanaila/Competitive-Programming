from collections import deque


class Solution:
    def countStudents(self, students, sandwiches):
        dq = deque()
        i = 0
        j = len(sandwiches) - 1
        while i < j:
            sandwiches[i], sandwiches[j] = sandwiches[j], sandwiches[i]
            i += 1
            j -= 1
        for student in students:
            dq.append(student)
        bad = 0
        while sandwiches:
            if dq[0] == sandwiches[-1]:
                sandwiches.pop()
                dq.popleft()
                bad = 0
            else:
                bad += 1
                if bad == len(dq):
                    return bad
                dq.append(dq[0])
                dq.popleft()
        return 0
