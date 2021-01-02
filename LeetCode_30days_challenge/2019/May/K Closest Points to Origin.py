def kClosest(points, K):
    output = []
    for i in points:
        i.append(i[0] * i[0] + i[1] * i[1])
    points.sort(key=lambda x: x[2])
    for i in range(K):
        output.append(points[i][:2])
    return output


print(kClosest([[3, 3], [5, -1], [-2, 4]], 2))
