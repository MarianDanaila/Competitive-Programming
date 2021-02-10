
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        bij = {None: None}
        curr = head
        first = True
        while curr:
            bij[curr] = Node(curr.val)
            if first:
                copy_head = bij[curr]
                first = False
            curr = curr.next
        curr = head
        prev = None
        while curr:
            copy = bij[curr]
            copy.random = bij[curr.random]
            if prev is not None:
                prev.next = copy
            prev = copy
            curr = curr.next
        return copy_head
