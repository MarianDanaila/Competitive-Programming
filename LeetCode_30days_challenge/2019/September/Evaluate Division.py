from collections import deque


class Solution(object):
    def calcEquation(self, equations, values, queries):
        graph = {}
        self.out = []

        def build_graph(equations, values):
            def add_edge(v1, v2, value):
                if v1 in graph:
                    graph[v1].append([v2, value])
                else:
                    graph[v1] = [[v2, value]]

            for i in range(len(equations)):
                add_edge(equations[i][0], equations[i][1], values[i])
                add_edge(equations[i][1], equations[i][0], 1 / values[i])

        build_graph(equations, values)

        def find_path(query):
            v1, v2 = query
            if v1 not in graph or v2 not in graph:
                self.out.append(-1.0)
            else:
                found = False
                q = deque()
                q.append([v1, 1.0])
                visited = set()
                while q:
                    print(q, self.out)
                    v, product = q.popleft()
                    if v == v2:
                        self.out.append(product)
                        found = True
                        break
                    visited.add(v)
                    for neighbor, value in graph[v]:
                        if neighbor not in visited:
                            q.append([neighbor, product * value])
                if not found:
                    self.out.append(-1.0)

        for query in queries:
            find_path(query)
        return self.out
