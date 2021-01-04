from heapq import heappop, heappush
t = int(input())
for test in range(1, t+1):
    n = int(input())
    e = []
    r = []
    sum_e = 0
    for _ in range(n):
        curr_e, curr_r = [int(s) for s in input().split(" ")]
        e.append(curr_e)
        r.append(curr_r)
        sum_e += curr_e
    toys = []
    curr_time = max_time = sum_e
    removed = count = 0
    for i in range(n):
        heappush(toys, [-e[i]-r[i], i])
        curr_time += e[i]
        while toys:
            #  check if any toy in priority queue violates the condition
            toy = toys[0]
            if -toy[0] <= sum_e:
                break
            else:
                index = toy[1]
                curr_time -= e[index] * 2  # we multiply by 2 because toy was added once in round1 and once in round2
                sum_e -= e[index]
                count += 1
                heappop(toys)
        if curr_time > max_time:
            removed = count
            max_time = curr_time
        elif curr_time == max_time:
            removed = min(removed, count)
    if toys:
        print("Case #{}: {} {}".format(test, count, "INDEFINITELY"))
    else:
        print("Case #{}: {} {}".format(test, removed, max_time))
