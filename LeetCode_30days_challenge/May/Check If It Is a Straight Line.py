def checkStraightLine(coordinates):
    if len(coordinates) == 2:
        return True
    for i in range(1, len(coordinates)-1):
        if coordinates[i-1][0]*(coordinates[i][1]-coordinates[i+1][1]) + coordinates[i][0]*(coordinates[i+1][1]-coordinates[i-1][1]) + coordinates[i+1][0]*(coordinates[i-1][1]-coordinates[i][1]) != 0:
            return False
    return True

print(checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))
