class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = y = 0
        orientation = 'N'
        for _ in range(4):
            for instruction in instructions:
                if instruction == 'G':
                    if orientation == 'N':
                        y += 1
                    elif orientation == 'S':
                        y -= 1
                    elif orientation == 'W':
                        x -= 1
                    else:
                        x += 1
                elif instruction == 'L':
                    if orientation == 'N':
                        orientation = 'W'
                    elif orientation == 'W':
                        orientation = 'S'
                    elif orientation == 'S':
                        orientation = 'E'
                    else:
                        orientation = 'N'
                elif instruction == 'R':
                    if orientation == 'N':
                        orientation = 'E'
                    elif orientation == 'E':
                        orientation = 'S'
                    elif orientation == 'S':
                        orientation = 'W'
                    else:
                        orientation = 'N'
            if x == 0 and y == 0:
                return True
        return False
