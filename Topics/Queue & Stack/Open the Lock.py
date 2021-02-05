from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set()
        for deadend in deadends:
            visited.add(deadend)

        if '0000' in visited:
            return -1
        if '0000' == target:
            return 0
        dq = deque()
        dq.append("0000")
        steps = 0
        while dq:
            steps += 1
            for _ in range(len(dq)):
                comb = dq.popleft()
                wheels = [comb[0], comb[1], comb[2], comb[3]]
                for i in range(4):
                    wheels[i] = int(comb[i]) + 1
                    if wheels[i] == 10:
                        wheels[i] = '0'
                    else:
                        wheels[i] = str(wheels[i])

                    nxt = "".join(wheels)
                    if nxt == target:
                        return steps
                    if nxt not in visited:
                        visited.add(nxt)
                        dq.append(nxt)

                    wheels[i] = int(wheels[i]) - 2
                    if wheels[i] == -2:
                        wheels[i] = '8'
                    elif wheels[i] == -1:
                        wheels[i] = '9'
                    else:
                        wheels[i] = str(wheels[i])

                    nxt = "".join(wheels)
                    if nxt == target:
                        return steps
                    if nxt not in visited:
                        visited.add(nxt)
                        dq.append(nxt)

                    wheels[i] = comb[i]
        return -1
