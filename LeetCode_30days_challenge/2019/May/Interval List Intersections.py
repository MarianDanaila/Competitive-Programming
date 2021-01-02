def intervalIntersection(a, b):
    i = 0
    j = 0
    output = []
    while i < len(a) and j < len(b):
        if a[i][0] <= b[j][0] <= a[i][1]:
            if a[i][1] <= b[j][1]:
                output.append([b[j][0], a[i][1]])
                i += 1
            else:
                output.append([b[j][0], b[j][1]])
                j += 1
        elif a[i][0] <= b[j][1] <= a[i][1]:
            output.append([a[i][0], b[j][1]])
            j += 1
        elif b[j][0] <= a[i][0]:
            if b[j][1] >= a[i][1]:
                output.append([a[i][0], a[i][1]])
                i += 1
            else:
                j += 1
        else:
            i += 1
    return output

print(intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))


