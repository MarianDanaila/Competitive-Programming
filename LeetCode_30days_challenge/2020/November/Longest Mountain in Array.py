class Solution:
    def longestMountain(self, A):
        if len(A) < 3:
            return 0
        peak = False
        max_length = curr_length = 1
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                if peak:
                    max_length = max(max_length, curr_length)
                    curr_length = 2
                    peak = False
                else:
                    curr_length += 1
            elif A[i] < A[i - 1]:
                if curr_length == 1:
                    continue
                if not peak:
                    peak = True
                curr_length += 1
            else:
                if curr_length == 1:
                    continue
                if not peak:
                    curr_length = 1
                else:
                    max_length = max(curr_length, max_length)
                    curr_length = 1
        if peak:
            max_length = max(max_length, curr_length)

        if max_length < 3:
            return 0
        else:
            return max_length
