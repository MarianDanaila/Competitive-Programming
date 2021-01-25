class Solution:
    def detectCycle(self, head):
        if not head:
            return
        slow = fast = head
        cycle = False
        while slow.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cycle = True
                break
            if not fast.next:
                break
        if not cycle:
            return
        entry = head
        while entry != slow:
            entry = entry.next
            slow = slow.next
        return entry
