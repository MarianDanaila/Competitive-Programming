class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        side = max_tree = max_apples = inside = outside = 0
        while max_apples < neededApples:
            side += (max_tree + 1)
            max_tree += 2
            side += 2 * max_tree
            inside += outside
            outside = 4 * (side - max_tree)
            max_apples = inside + outside
        return max_tree * 4
