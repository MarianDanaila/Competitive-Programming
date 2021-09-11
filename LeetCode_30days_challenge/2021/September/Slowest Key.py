from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        n = len(keysPressed)
        longest = releaseTimes[0]
        ch = keysPressed[0]
        for i in range(1, n):
            if releaseTimes[i] - releaseTimes[i - 1] > longest:
                longest = releaseTimes[i] - releaseTimes[i - 1]
                ch = keysPressed[i]
            elif releaseTimes[i] - releaseTimes[i - 1] == longest:
                if keysPressed[i] > ch:
                    ch = keysPressed[i]

        return ch
