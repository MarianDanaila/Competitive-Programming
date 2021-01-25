
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


from collections import deque


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        root.next = None
        dq = deque()
        dq.append(root)
        while dq:
            for i in range(len(dq)):
                node = dq.popleft()
                if node.left and node.right:
                    dq.append(node.left)
                    dq.append(node.right)
                    if i > 0:
                        prev.next = node.left
                    node.left.next = node.right
                    prev = node.right
                else:
                    return root
            node.right.next = None
