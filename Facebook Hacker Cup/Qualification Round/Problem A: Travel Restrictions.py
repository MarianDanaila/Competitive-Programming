t = int(input())
with open("output.txt", "w") as fout:
    for case in range(1, t+1):
        n = int(input())
        I = input()
        O = input()
        matrix = [[None] * n for _ in range(n)]
        for i in range(n):
            matrix[i][i] = 'Y'
        cop = -1
        for j in range(1, n):
            cop += 1
            k = cop
            for i in range(k, -1, -1):
                if abs(i-j) == 1:
                    if O[i] == 'Y' and I[j] == 'Y':
                        matrix[i][j] = 'Y'
                    else:
                        matrix[i][j] = 'N'

                    if O[j] == 'Y' and I[i] == 'Y':
                        matrix[j][i] = 'Y'
                    else:
                        matrix[j][i] = 'N'
                elif abs(i-j) > 1:
                    if matrix[i][j-1] == 'Y' and matrix[i+1][j] == 'Y':
                        matrix[i][j] = 'Y'
                    else:
                        matrix[i][j] = 'N'
                    if matrix[j-1][i] == 'Y' and matrix[j][i+1] == 'Y':
                        matrix[j][i] = 'Y'
                    else:
                        matrix[j][i] = 'N'

        fout.write("Case #{}:".format(case))
        fout.write('\n')
        #print("Case #{}:".format(case))
        for row in matrix:
            fout.write(''.join(row))
            fout.write('\n')
            #print(''.join(row))

