class Solution(object):
    def advantageCount(self, A, B):
        A.sort()
        sortedB = sorted(B)
        ans = []
        assigned = {}
        remaining = []
        ans = []

        # assigned[b] = list of a that are assigned to beat b
        # remaining = list of a that are not assigned to any b

        for b in B:
            assigned[b] = []

        # populate (assigned, remaining) appropriately
        # sortedB[j] is always the smallest unassigned element in B

        j = 0
        for a in A:
            if a > sortedB[j]:
                assigned[sortedB[j]].append(a)
                j += 1
            else:
                remaining.append(a)

        # Reconstruct the answer from annotations (assigned, remaining)
        # print(assigned, remaining)
        for i in range(len(B)):
            if assigned[B[i]]:
                B[i] = assigned[B[i]].pop()
            else:
                B[i] = remaining.pop()

        return B
