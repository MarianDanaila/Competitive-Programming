class Solution:
    def findSmallestSetOfVertices(self, n: int, edges):
        visited = [False] * n
        for edge in edges:
            visited[edge[1]] = True
        output = []
        for i in range(n):
            if not visited[i]:
                output.append(i)
        return output
