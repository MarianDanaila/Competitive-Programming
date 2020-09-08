# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:
            return True
        elif not root1 and root2:
            return False
        elif not root2 and root1:
            return False
        stack = [root1]
        leaves = []
        while stack:
            root = stack.pop()
            if not root.left and not root.right:
                leaves.append(root.val)
            elif not root.left:
                stack.append(root.right)
            elif not root.right:
                stack.append(root.left)
            else:
                stack.append(root.left)
                stack.append(root.right)
        stack = [root2]
        index = 0
        while stack:
            root = stack.pop()
            if not root.left and not root.right:
                if leaves[index] != root.val:
                    return False
                else:
                    index += 1
            elif not root.left:
                stack.append(root.right)
            elif not root.right:
                stack.append(root.left)
            else:
                stack.append(root.left)
                stack.append(root.right)
        return True
