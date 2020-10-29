class Solution:
    def minDominoRotations(self, A, B):
        min_rotations = float("inf")
        tile1 = [set() for _ in range(6)]
        tile2 = [set() for _ in range(6)]
        for i in range(len(A)):
            tile1[A[i]-1].add(i)
        for i in range(len(B)):
            tile2[B[i]-1].add(i)
        for i in range(6):
            uni = tile1[i].union(tile2[i])
            if len(uni) == len(A):
                min_rotations = min(min_rotations, min(len(A)-len(tile1[i]), len(A)-len(tile2[i])))
        if min_rotations == float("inf"):
            return -1
        return min_rotations
