# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode):
        self.r1 = []
        self.r2 = []
        self.ans = []
        self.dfs1(root1)
        self.dfs2(root2)
        print(self.r1, self.r2)
        i = 0
        j = 0
        while i < len(self.r1) and j < len(self.r2):
            if self.r1[i] == self.r2[j]:
                self.ans.append(self.r1[i])
                self.ans.append(self.r2[j])
                i += 1
                j += 1
            elif self.r1[i] < self.r2[j]:
                self.ans.append(self.r1[i])
                i += 1
            else:
                self.ans.append(self.r2[j])
                j += 1
        while i < len(self.r1):
            self.ans.append(self.r1[i])
            i += 1
        while j < len(self.r2):
            self.ans.append(self.r2[j])
            j += 1
        return self.ans

    def dfs1(self, root):
        if root:
            self.dfs1(root.left)
            self.r1.append(root.val)
            self.dfs1(root.right)

    def dfs2(self, root):
        if root:
            self.dfs2(root.left)
            self.r2.append(root.val)
            self.dfs2(root.right)
