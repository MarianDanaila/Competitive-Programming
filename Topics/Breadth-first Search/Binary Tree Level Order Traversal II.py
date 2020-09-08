from collections import deque


class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return
        bottom = []
        d = deque()
        d.append(root)
        while d:
            level = []
            for _ in range(len(d)):
                root = d.popleft()
                level.append(root.val)
                if root.left:
                    d.append(root.left)
                if root.right:
                    d.append(root.right)
            bottom.append(level)
        return bottom[::-1]
