class Solution:
    def minJumps(self, arr: List[int]) -> int:
        visited = set()
        dq = deque()
        dq.append(0)
        visited.add(0)
        occ = {}
        n = len(arr)
        jumps = 0
        for i in range(n):
            if arr[i] not in occ:
                occ[arr[i]] = set()
            occ[arr[i]].add(i)
        while dq:
            len_dq = len(dq)
            for _ in range(len_dq):
                idx = dq.popleft()
                if idx == n - 1:
                    return jumps
                if arr[idx] in occ:
                    for same in occ[arr[idx]]:
                        if same not in visited:
                            visited.add(same)
                            dq.append(same)
                    occ.pop(arr[idx])
                if idx - 1 > 0 and idx - 1 not in visited:
                    visited.add(idx - 1)
                    dq.append(idx - 1)
                if idx + 1 < n and idx + 1 not in visited:
                    visited.add(idx + 1)
                    dq.append(idx + 1)
            jumps += 1
