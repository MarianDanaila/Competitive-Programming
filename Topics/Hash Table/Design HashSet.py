# Approach 1: Using a simple array


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keys = [False] * (10 ** 6 + 1)

    def add(self, key: int) -> None:
        if not self.keys[key]:
            self.keys[key] = True

    def remove(self, key: int) -> None:
        if self.keys[key]:
            self.keys[key] = False

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.keys[key]


# Approach 2: Using a bucket array
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_buckets = 10000
        self.buckets = [[] for _ in range(self.num_buckets)]

    def add(self, key: int) -> None:
        bucket = self.hash_function(key)
        if not self.contains(key):
            self.buckets[bucket].append(key)

    def remove(self, key: int) -> None:
        bucket = self.hash_function(key)
        if self.contains(key):
            self.buckets[bucket].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        bucket = self.hash_function(key)
        return key in self.buckets[bucket]

    def hash_function(self, key):
        return key % self.num_buckets


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
