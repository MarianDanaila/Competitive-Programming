from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        dq = deque()
        dq.append(root)
        root.next = None
        while dq:
            len_dq = len(dq)
            prev = None
            for _ in range(len_dq):
                curr = dq.popleft()
                left_child = curr.left
                if not left_child:
                    return root
                right_child = curr.right
                if prev is not None:
                    prev.next = left_child
                left_child.next = right_child
                prev = right_child
                dq.append(left_child)
                dq.append(right_child)
            prev.next = None
