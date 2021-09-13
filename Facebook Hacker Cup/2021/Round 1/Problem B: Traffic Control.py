with open("input.txt", "r") as fin:
    with open("output.txt", "w") as fout:
        t = int(fin.readline())
        for town in range(1, t + 1):
            n, m, a, b = [int(s) for s in fin.readline().split(" ")]
            if a < n + m - 1 or b < n + m - 1:
                #print("Case #{}: {}".format(town, "Impossible"))
                fout.write("Case #{}: {}".format(town, "Impossible"))
                fout.write("\n")
            else:
                #print("Case #{}: {}".format(town, "Possible"))
                fout.write("Case #{}: {}".format(town, "Possible"))
                fout.write("\n")
                grid = [[1000] * m for _ in range(n)]
                grid[n - 1][0] = b - (m + n - 2)
                grid[n - 1][m - 1] = a - (m + n - 2)
                for i in range(m):
                    grid[0][i] = 1

                for i in range(n - 1):
                    grid[i][0] = grid[i][m - 1] = 1

                for row in grid:
                    fout.write(" ".join(map(str, row)))
                    fout.write("\n")
                    #print(" ".join(map(str, row)))
