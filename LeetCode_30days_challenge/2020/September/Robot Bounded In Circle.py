class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = 0
        y = 0
        direction = 0

        for instruction in instructions:
            if instruction == 'L':
                direction -= 1
            elif instruction == 'R':
                direction += 1
            else:
                if direction < 0:
                    cardinality = (4 - (direction % 4)) % 4
                else:
                    cardinality = direction % 4
                if cardinality == 0:
                    y += 1
                elif cardinality == 1:
                    x += 1
                elif cardinality == 2:
                    y -= 1
                else:
                    x -= 1
        if direction < 0:
            cardinality = (4 - (direction % 4)) % 4
        else:
            cardinality = direction % 4
        if (x == 0 and y == 0) or cardinality != 0:
            return True
        return False
