# Time-complexity:O(n^2)
class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder.pop())
        indexInorder = inorder.index(root.val)

        root.right = self.buildTree(inorder[indexInorder+1:], postorder)
        root.left = self.buildTree(inorder[:indexInorder], postorder)

        return root

# Time-complexity:O(n)
class Solution2:
    def buildTree(self, inorder, postorder):
        map_inorder = {}
        for i in range(len(inorder)):
            map_inorder[inorder[i]] = i
        print(map_inorder)
        def recur(low, high):
            if low > high:
                return None
            x = TreeNode(postorder.pop())
            mid = map_inorder[x.val]
            x.right = recur(mid+1, high)
            x.left = recur(low, mid-1)
            return x
        return recur(0, len(inorder)-1)

sol = Solution2()
print(sol.buildTree([9,3,15,20,7], [9,15,7,20,3]))