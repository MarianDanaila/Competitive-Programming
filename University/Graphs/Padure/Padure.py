from collections import deque
with open("padure.in", 'r') as fin:
    # pl, pc - coordinates of Algorel
    # cl, cc - coordinates of castel
    n, m, pl, pc, cl, cc = [int(s) for s in fin.readline().split(" ")]
    forest = []
    costs = [[105] * m for _ in range(n)]
    x = [1, 0, -1, 0]
    y = [0, 1, 0, -1]
    diamonds = float("inf")
    for _ in range(n):
        line = [int(s) for s in fin.readline().split(" ")]
        forest.append(line)
    q = deque()
    q.append([pl-1, pc-1])  # starting point of BFS
    costs[pl-1][pc-1] = 0

    def valid_cell(i, j):
        return 0 <= i < n and 0 <= j < m


    while q:
        curr_x, curr_y = q.popleft()
        for i in range(4):
            next_x = curr_x + x[i]
            next_y = curr_y + y[i]
            if valid_cell(next_x, next_y):
                if costs[next_x][next_y] != -1:
                    if costs[next_x][next_y] > costs[curr_x][curr_y] + 1 and forest[next_x][next_y] != forest[curr_x][curr_y]:
                        costs[next_x][next_y] = costs[curr_x][curr_y] + 1
                        q.append([next_x, next_y])
                    elif costs[next_x][next_y] > costs[curr_x][curr_y] and forest[next_x][next_y] == forest[curr_x][curr_y]:
                        costs[next_x][next_y] = costs[curr_x][curr_y]
                        q.appendleft([next_x, next_y])

with open("padure.out", 'w') as fout:
    fout.write(str(costs[cl-1][cc-1]))
