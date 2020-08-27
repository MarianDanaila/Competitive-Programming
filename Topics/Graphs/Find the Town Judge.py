# Approach 1 using hashing
# Time-complexity: O(N)
class Solution:
    def findJudge(self, N, trust):
        people = [0] * N
        for pair in trust:
            people[pair[1]-1] += 1
        trust_judge = max(people)
        if trust_judge == N - 1:
            judge = people.index(trust_judge)
            for pair in trust:
                if pair[0] == judge+1:
                    return -1
            return judge+1
        return -1

# Approach 2 using matrix
# Time-complexity: O(N ^ 2)
class Solution:
    def findJudge(self, N, trust) -> int:
        possible_town_judge = -1
        matrix = [[0] * N for _ in range(N)]
        for pair in trust:
            matrix[pair[0] - 1][pair[1] - 1] = 1
        # Check possible town judge by searching a line with all zeroes
        for i in range(N):
            zero = True
            for j in range(N):
                if matrix[i][j] == 1:
                    zero = False
                    break
            if zero:
                possible_town_judge = i

        if possible_town_judge == -1:
            return -1

        # Check if possible town judge is the actual town judge by searching for a column with only one zero
        cnt = 0
        for i in range(N):
            if matrix[i][possible_town_judge] == 1:
                cnt += 1
        if cnt == N - 1:
            return possible_town_judge + 1
        else:
            return -1

