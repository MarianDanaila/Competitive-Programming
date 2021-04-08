class Solution:
    def isPathCrossing(self, path: str) -> bool:
        dct = {"0 0":1}
        x = 0
        y = 0
        for i in path:
            if i == 'N':
                y += 1
            elif i == 'S':
                y -= 1
            elif i == 'E':
                x += 1
            elif i == 'W':
                x -= 1
            try:
                if dct[str(x)+" "+str(y)] == 1:
                    return True
            except KeyError:
                dct[str(x)+" "+str(y)] = 1
        return False
