# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists) -> ListNode:
        dummy = ListNode(0)
        head = dummy

        while True:
            minim = 10 ** 4 + 1
            index = -1
            for i in range(len(lists)):
                if not lists[i]:
                    continue
                if lists[i].val < minim:
                    minim = lists[i].val
                    index = i

            if index == -1:
                break

            head.next = lists[index]
            head = head.next
            lists[index] = lists[index].next

        head.next = None
        return dummy.next
