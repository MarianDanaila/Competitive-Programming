class Solution:
    def decrypt(self, code, k):
        n = len(code)
        ans = [0] * n

        if k > 0:
            for i in range(n):
                count = 0
                curr_sum = 0
                j = i + 1
                while count < k:
                    if j == n:
                        j = 0
                    curr_sum += code[j]
                    j += 1
                    count += 1
                ans[i] = curr_sum
        if k < 0:
            k = -k
            for i in range(n):
                count = 0
                curr_sum = 0
                j = i - 1
                while count < k:
                    if j == -1:
                        j = n - 1

                    curr_sum += code[j]
                    j -= 1
                    count += 1
                ans[i] = curr_sum
        return ans
