# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Approach 1 using Array
from collections import deque


class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        digits = [0] * 9
        digits[root.val-1] += 1
        dq = deque()
        dq.append([root, digits])
        ans = 0
        while dq:
            for _ in range(len(dq)):
                root, digits = dq.popleft()
                if not root.left and not root.right:  # if it's a leaf
                    odd = 0
                    for digit in digits:
                        if digit % 2 == 1:
                            odd += 1
                    if odd <= 1:  # it is a pseudo-palindromic
                        ans += 1
                copy_digits1 = digits[:]
                copy_digits2 = digits[:]
                if root.left:
                    copy_digits1[root.left.val-1] += 1
                    dq.append([root.left, copy_digits1])
                if root.right:
                    copy_digits2[root.right.val-1] += 1
                    dq.append([root.right, copy_digits2])
        return ans

# Approach 2 using BIT operators


class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        stack = [[root, 0]]
        ans = 0
        while stack:
            root, path = stack.pop()
            path ^= 1 << root.val
            if not root.left and not root.right:
                if path & (path-1) == 0:
                    ans += 1
            if root.left:
                stack.append([root.left, path])
            if root.right:
                stack.append([root.right, path])
        return ans
