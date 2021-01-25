class Solution:
    def isBalanced(self, root):
        if not root:
            return True
        stack = [[root, False]]
        while stack:
            root = stack.pop()
            if root[1]:
                if abs(root[2]-root[3]) > 1:
                    return False
                if not stack:
                    return True
                elif len(stack) == 1:
                    stack[-1].append(max(root[2], root[3])+1)
                else:
                    if len(stack[-1]) == 3:
                        stack[-1].append(max(root[2], root[3])+1)
                    else:
                        stack[-2].append(max(root[2], root[3])+1)
            else:
                if not root[0].left and not root[0].right:
                    stack.append([root[0], True, 0, 0])
                elif not root[0].left or not root[0].right:
                    stack.append([root[0], True, 0])
                    if not root[0].left:
                        stack.append([root[0].right, False])
                    else:
                        stack.append([root[0].left, False])
                else:
                    stack.append([root[0], True])
                    stack.append([root[0].right, False])
                    stack.append([root[0].left, False])
