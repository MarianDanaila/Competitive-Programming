from collections import deque


class CombinationIterator:

    def __init__(self, characters, combinationLength):
        self.output = []
        self.cur = -1

        q = deque()
        q.append(("", 0))
        N = len(characters)
        while q:
            temp, cur = q.popleft()
            if len(temp) == combinationLength:
                self.output.append(temp)
                continue
            for i in range(cur, N):
                q.append((temp+characters[i], i+1))

    def next(self):
        if self.hasNext():
            self.cur += 1
            return self.output[self.cur]

    def hasNext(self):
        return self.cur + 1 < len(self.output)

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()