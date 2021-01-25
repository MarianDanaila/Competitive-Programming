def reconstructQueue(people):
    people.sort()
    answer = [0] * len(people)
    k = 0
    for i in range(len(people)):
        counter = 0
        if i != 0:
            if people[i][0] == people[i-1][0]:
                k += 1
            else:
                k = 0
        for j in range(len(answer)):
            if counter == people[i][1] - k and answer[j] == 0:
                answer[j] = people[i]
                break

            if answer[j] == 0:
                counter += 1
    return answer


reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])