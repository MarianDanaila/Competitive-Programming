class TwoStackQueue:
    def __init__(self):
        self.inbox = []
        self.outbox = []

    def push(self, number):
        self.inbox.append(number)
        return


    def pop(self):
        if len(self.outbox) == 0:
            while len(self.inbox) > 0:
                self.outbox.append(self.inbox[-1])
                self.inbox.pop()
        x = self.outbox[-1]
        self.outbox.pop()
        return x


