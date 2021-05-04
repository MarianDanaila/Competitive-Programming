from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
        for i in range(n):
            op = 0
            for j in range(n):
                if boxes[j] == '1':
                    op += abs(j - i)

            answer[i] = op
        return answer
