# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.copy_head = head
        self.length = 0
        while head:
            self.length += 1
            head = head.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        index = random.randint(1, self.length)
        i = 1
        head = self.copy_head
        while head:
            if i == index:
                return head.val
            else:
                i += 1
                head = head.next

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

# Solution 2 when we don't know the lenght of the linked list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


import random


class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        new_head = self.head
        index = 1
        while new_head:
            if random.randint(1, index) == index:
                ans = new_head.val
            new_head = new_head.next
            index += 1
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
