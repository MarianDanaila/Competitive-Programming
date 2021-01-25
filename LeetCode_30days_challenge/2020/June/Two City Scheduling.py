def twoCitySchedCost(costs):
    total = 0
    for i in costs:
        total += i[0]
    for i in costs:
        i.append(i[1]-i[0])
    i.sort(key=lambda x:x[2])
    for i in range(len(costs) // 2):
        i += costs[i][2]
    return i

