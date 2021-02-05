class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = []
        i = 0
        first = True
        while i < len(path) - 3:
            if path[i] == '/' and path[i + 1] == '.' and path[i + 2] == '.' and path[i + 3] == '/':
                while ans and ans[-1] != '/':  # move one level
                    ans.pop()
                if ans:
                    ans.pop()
                first = True
                i += 3
            elif path[i] == '/' and path[i + 1] == '.' and path[i + 2] == '/':
                first = True
                i += 2
            elif path[i] == '/' and path[i + 1] == '/':
                i += 1
                first = True
            elif path[i] == '/':
                first = True
                i += 1
            else:
                if first:
                    first = False
                    ans.append('/')
                ans.append(path[i])
                i += 1
        rem = len(path) - i
        if rem == 3:
            if path[i] == '/' and path[i + 1] == '.' and path[i + 2] == '.':
                while ans and ans[-1] != '/':
                    ans.pop()
                if ans:
                    ans.pop()
                first = True
                i += 3
            elif path[i] == '/' and path[i + 1] == '.' and path[i + 2] == '/':
                first = True
                i += 2
        for idx in range(i, len(path)):
            if path[idx] != '/':
                if first:
                    first = False
                    ans.append('/')
                ans.append(path[idx])
            else:
                first = True
        if path[-1] == '.' and path[-2] == '/':
            if ans:
                ans.pop()
                ans.pop()
        if len(ans) == 0:
            return '/'
        return "".join(ans)
