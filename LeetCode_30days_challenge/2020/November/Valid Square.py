class Solution:
    def validSquare(self, p1, p2, p3, p4):
        edge1 = (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2
        edge2 = (p3[0] - p2[0]) ** 2 + (p3[1] - p2[1]) ** 2
        edge3 = (p4[0] - p3[0]) ** 2 + (p4[1] - p3[1]) ** 2
        edge4 = (p1[0] - p4[0]) ** 2 + (p1[1] - p4[1]) ** 2
        edge5 = (p3[0] - p1[0]) ** 2 + (p3[1] - p1[1]) ** 2
        edge6 = (p2[0] - p4[0]) ** 2 + (p2[1] - p4[1]) ** 2

        edges = [edge1, edge2, edge3, edge4, edge5, edge6]
        dct = {}
        for edge in edges:
            if edge not in dct:
                dct[edge] = 1
            else:
                dct[edge] += 1
        diagonals = edges = -1
        if len(dct) == 2:
            for key in dct:
                if dct[key] == 2:
                    diagonals = key
                if dct[key] == 4:
                    edges = key
        return 2 * edges == diagonals
