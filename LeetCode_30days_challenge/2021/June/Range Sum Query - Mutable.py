from math import sqrt, ceil
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        n = len(self.nums)
        bucket_length = sqrt(n)
        self.nr_buckets = ceil(n / bucket_length)
        self.buckets = [0] * int(self.nr_buckets)
        for i in range(n):
            self.buckets[i // self.nr_buckets] += self.nums[i]

    def update(self, index: int, val: int) -> None:
        self.buckets[index // self.nr_buckets] += val - self.nums[index]
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        start_bucket = left // self.nr_buckets
        end_bucket = right // self.nr_buckets
        if start_bucket == end_bucket:
            total_sum = sum(self.nums[left: right + 1])
        else:
            total_sum = sum(self.nums[left: (start_bucket + 1) * self.nr_buckets])  # sum from first bucket
            total_sum += sum(self.buckets[start_bucket + 1: end_bucket])  # sum from middle buckets
            total_sum += sum(self.nums[end_bucket * self.nr_buckets: right + 1])  # sum from last bucket
        return total_sum

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
