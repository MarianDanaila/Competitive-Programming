class Solution:
    def flatten(self, head):
        if head is None:
            return None
        stack = []
        ans_head = head
        while True:
            if head.child:  # if we have a child then we connect the two levels
                if head.next:
                    stack.append(head.next)  # here we put in a stack to come back at that node
                # down below we connect the two level and also make the child to None
                temp = head.child
                head.child = None
                head.next = temp
                temp.prev = head
                head = temp
            else:
                if head.next is None:  # here we want to have a valid node to continue
                    break
                head = head.next

        # down below we continue where we left with the stack until the stack is empty
        while stack:
            head.next = stack[-1]
            stack[-1].prev = head
            head = stack[-1]
            while head.next:
                head = head.next
            stack.pop()

        return ans_head