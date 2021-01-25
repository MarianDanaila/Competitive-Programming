# Time-complexity: O(N)
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        if k == 1:
            return 1
        cnt = 1
        for factor in range(2, n // 2 + 1):
            if n % factor == 0:
                cnt += 1
                if cnt == k:
                    return factor
        if cnt+1 == k:
            return n
        return -1


# Time-complexity: O(logN)
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                k -= 1
                if k == 0:
                    return i

        for i in range(int(n ** 0.5), 0, -1):
            if i * i == n:
                continue
            if n % i == 0:
                k -= 1
                if k == 0:
                    return n // i
        return -1
