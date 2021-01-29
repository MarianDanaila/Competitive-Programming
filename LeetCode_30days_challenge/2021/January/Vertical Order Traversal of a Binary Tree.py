# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def verticalTraversal(self, root: TreeNode):
        if not root:
            return
        dq = deque()
        reports = {}
        dq.append([root, 0])
        visited = set()
        ans = []
        while dq:
            for _ in range(len(dq)):
                curr, x = dq.popleft()
                if x not in reports:
                    reports[x] = [[curr.val]]
                    visited.add(x)
                else:
                    if x not in visited:
                        visited.add(x)
                        reports[x].append([curr.val])
                    else:
                        reports[x][-1].append(curr.val)
                if curr.left:
                    dq.append([curr.left, x - 1])
                if curr.right:
                    dq.append([curr.right, x + 1])

            visited.clear()
        sorted_keys = sorted(reports.keys())
        for key in sorted_keys:
            for arr in reports[key]:
                arr.sort()

        for key in sorted_keys:
            lst = []
            for arr in reports[key]:
                for el in arr:
                    lst.append(el)
            ans.append(lst)
        return ans
