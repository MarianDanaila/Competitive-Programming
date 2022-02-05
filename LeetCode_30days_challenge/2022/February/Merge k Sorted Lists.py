# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        n = len(lists)
        dummy = curr = ListNode(0)

        while True:
            idx = -1
            for i in range(n):
                if lists[i] and (idx == -1 or lists[i].val < lists[idx].val):
                    idx = i
            if idx == -1:
                return dummy.next
            curr.next = lists[idx]
            curr = curr.next
            lists[idx] = lists[idx].next
