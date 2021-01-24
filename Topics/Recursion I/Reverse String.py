class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.helper(0, len(s) - 1, s)

    def helper(self, i1, i2, string):
        if i1 >= i2:
            return

        self.helper(i1 + 1, i2 - 1, string)
        string[i1], string[i2] = string[i2], string[i1]
