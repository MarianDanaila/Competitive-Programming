with open("output.txt", "w") as fout:
    t = int(input())
    for test in range(1, t + 1):
        n = int(input())
        grid = []
        for _ in range(n):
            row = input()
            grid.append(list(row))

        configurations = set()
        min_x = n + 1

        for row in range(n):
            x = o = empty = 0
            for col in range(n):
                if grid[row][col] == 'X':
                    x += 1
                elif grid[row][col] == 'O':
                    o += 1
                else:
                    empty += 1
            if o == 0:
                if empty > min_x:
                    continue
                if empty < min_x:
                    min_x = empty
                    configurations.clear()
                configuration = []
                for col in range(n):
                    if grid[row][col] == '.':
                        configuration.append(row)
                        configuration.append(' ')
                        configuration.append(col)
                        configuration.append(' ')
                configurations.add("".join(map(str, configuration)))

        for col in range(n):
            x = o = empty = 0
            for row in range(n):
                if grid[row][col] == 'X':
                    x += 1
                elif grid[row][col] == 'O':
                    o += 1
                else:
                    empty += 1
            if o == 0:
                if empty > min_x:
                    continue
                if empty < min_x:
                    min_x = empty
                    configurations.clear()
                configuration = []
                for row in range(n):
                    if grid[row][col] == '.':
                        configuration.append(row)
                        configuration.append(' ')
                        configuration.append(col)
                        configuration.append(' ')
                configurations.add("".join(map(str, configuration)))
        if min_x == n + 1:
            fout.write("Case #{}: {}".format(test, "Impossible"))
        else:
            fout.write("Case #{}: {} {}".format(test, min_x, len(configurations)))
        fout.write("\n")
