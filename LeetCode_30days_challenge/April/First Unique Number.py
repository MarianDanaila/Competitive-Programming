from collections import OrderedDict


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.od = OrderedDict()
        self.deleted = {}
        for i in nums:
            try:
                if self.deleted[i] == 1:
                    continue
            except KeyError:
                try:
                    if self.od[i] > 0:
                        self.deleted[i] = 1
                        self.od.pop(i)
                except KeyError:
                    self.od[i] = 1

        return

    def showFirstUnique(self) -> int:
        if len(self.od) > 0:
            for i in self.od:
                return i
        else:
            return -1

    def add(self, value: int) -> None:
        try:
            if self.deleted[value] == 1:
                return
        except KeyError:
            try:
                if self.od[value] > 0:
                    self.deleted[value] = 1
                    self.od.pop(value)
            except KeyError:
                self.od[value] = 1
        return

    # Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)