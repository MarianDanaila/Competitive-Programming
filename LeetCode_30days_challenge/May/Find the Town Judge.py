def findJudge(N, trust):
    possible_judge = {}
    for i in trust:
        try:
            possible_judge[i[1]] += 1
        except KeyError:
            possible_judge[i[1]] = 1
    for i in trust:
        try:
            possible_judge.pop(i[0])
        except KeyError:
            continue
    for i in possible_judge:
        if possible_judge[i] == N-1:
            return i
    return -1

print(findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]))