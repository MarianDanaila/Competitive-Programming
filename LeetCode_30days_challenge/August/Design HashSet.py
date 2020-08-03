class MyHashSet:
    def __init__(self):
        self.numBuckets = 15000
        self.buckets = [[] for _ in range(self.numBuckets)]

    def hash_function(self, key):
        return key % self.numBuckets

    def add(self, key):
        i = self.hash_function(key)
        if not key in self.buckets[i]:
            self.buckets[i].append(key)

    def remove(self, key):
        i = self.hash_function(key)
        if key in self.buckets[i]:
            self.buckets[i].remove(key)

    def contains(self, key):
        i = self.hash_function(key)
        if key in self.buckets[i]:
            return True
        else:
            return False
