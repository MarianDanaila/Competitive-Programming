
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
        dq = deque()
        dq.append(root)
        while dq:
            for i in range(len(dq)):
                node = dq.popleft()
                if i == 0:
                    prev = node
                else:
                    prev.next = node
                    prev = node
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            prev.next = None
        return root
