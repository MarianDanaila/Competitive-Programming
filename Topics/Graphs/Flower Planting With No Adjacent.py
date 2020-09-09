class Solution:
    def gardenNoAdj(self, N, paths):
        ans = [0] * N
        flowers = {}
        for i in range(1, N + 1):
            flowers[i] = []
        for path in paths:
            flowers[path[0]].append(path[1])
            flowers[path[1]].append(path[0])
        for garden in range(1, N + 1):
            temp = [1, 2, 3, 4]
            for connected_garden in flowers[garden]:
                if ans[connected_garden - 1] != 0:
                    temp.remove(ans[connected_garden - 1])

            ans[garden - 1] = temp[0]
        return ans
