# todo : Recursive Approach
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from itertools import permutations


# Brute Force
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 1:
            return [TreeNode(1)]
        perm = list(permutations([i for i in range(1, n + 1)]))
        bst = []
        for permutation in perm:
            dq = deque()
            root = curr = TreeNode(permutation[0])
            dq.append([-float("inf"), curr, curr, float("inf")])
            for i in range(1, n):
                node_value = permutation[i]
                found = False
                while dq:
                    start1, end1, start2, end2 = dq[0]
                    if start1 < node_value < end1.val and not end1.left:  # left child
                        left_node = TreeNode(node_value)
                        end1.left = left_node
                        dq.append([start1, left_node, left_node, end1.val])
                        found = True
                        break
                    elif start2.val < node_value < end2 and not start2.right:  # right child
                        right_node = TreeNode(node_value)
                        start2.right = right_node
                        dq.append([start2.val, right_node, right_node, end2])
                        dq.popleft()
                        found = True
                        break
                    else:
                        dq.popleft()
                if not found:
                    break
            if found:
                bst.append(root)
        return bst


# Optimized
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.helper(1, n)

    def helper(self, start, end):
        if start > end:
            return [None]
        all_trees = []
        for curr_root_val in range(start, end + 1):
            all_left_subtrees = self.helper(start, curr_root_val - 1)
            all_right_subtrees = self.helper(curr_root_val + 1, end)

            for left_subtree in all_left_subtrees:
                for right_subtree in all_right_subtrees:
                    curr_root = TreeNode(curr_root_val)
                    curr_root.left = left_subtree
                    curr_root.right = right_subtree

                    all_trees.append(curr_root)
        return all_trees
