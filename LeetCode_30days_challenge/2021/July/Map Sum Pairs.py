class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pairs = {}

    def insert(self, key: str, val: int) -> None:
        self.pairs[key] = val

    def sum(self, prefix: str) -> int:
        total_sum = 0
        for key in self.pairs:
            if len(prefix) <= len(key) and prefix == key[:len(prefix)]:
                total_sum += self.pairs[key]
        return total_sum

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
