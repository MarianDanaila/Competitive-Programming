from collections import Counter


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B) or len(A) < 2 or len(B) < 2:
            return False
        if A == B:
            cnt_a = Counter(A)
            for key in cnt_a:
                if cnt_a[key] > 1:
                    return True
            return False
        first = second = -1
        diff = 0
        for i in range(len(A)):
            if A[i] != B[i]:
                if first == -1:
                    first = i
                else:
                    second = i
                diff += 1
        if diff != 2:
            return False

        return A[first] == B[second] and B[first] == A[second]
