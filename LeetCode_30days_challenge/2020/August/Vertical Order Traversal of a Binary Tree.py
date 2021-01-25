class Solution:
    def verticalTraversal(self, root):
        dct = {}
        self.min_x = float("inf")
        self.max_x = -float("inf")

        def dfs(root, x, y):
            self.min_x = min(self.min_x, x)
            self.max_x = max(self.max_x, x)
            try:
                dct[x].append([y, root.val])
            except KeyError:
                dct[x] = [[y, root.val]]
            if root.left:
                dfs(root.left, x-1, y+1)
            if root.right:
                dfs(root.right, x+1, y+1)
        dfs(root, 0, 0)
        out = []
        for i in range(self.min_x, self.max_x+1):
            temp = []
            for j in sorted(dct[i]):
                temp.append(j[1])
            out.append(temp)

        return out
