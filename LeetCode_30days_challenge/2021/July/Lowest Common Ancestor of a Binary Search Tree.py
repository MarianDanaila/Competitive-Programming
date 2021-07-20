from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents = {root.val: None}
        dq = deque()
        dq.append(root)
        while dq:
            len_dq = len(dq)
            for _ in range(len_dq):
                curr = dq.popleft()
                if curr.left:
                    dq.append(curr.left)
                    parents[curr.left.val] = curr.val
                if curr.right:
                    dq.append(curr.right)
                    parents[curr.right.val] = curr.val

        ancestors_p = set()
        ancestor = p.val
        while ancestor is not None:
            ancestors_p.add(ancestor)
            ancestor = parents[ancestor]
        ancestor = q.val
        while ancestor is not None:
            if ancestor in ancestors_p:
                return TreeNode(ancestor)
            ancestor = parents[ancestor]


# Optimized solution
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root
