class MinStack:
    def __init__(self):
        self._stack = []
        self._minstack = []

    def push(self, val):
        self._stack.append(val)
        if len(self._minstack) == 0 or val <= self._minstack[len(self._minstack)-1]:
            self._minstack.append(val)
        return

    def pop(self):
        popped = self._stack.pop()
        if popped == self._minstack[len(self._minstack)-1]:
            self._minstack.pop()
        return popped

    def peek(self):
        return self._stack[len(self._stack)-1]

    def min(self):
        return self._minstack[len(self._minstack)-1]

stack = MinStack()
stack.push(4)
stack.push(7)
stack.push(3)
stack.push(2)
stack.push(6)

print(stack.min())
stack.pop()
print(stack.min())
stack.pop()
print(stack.min())




