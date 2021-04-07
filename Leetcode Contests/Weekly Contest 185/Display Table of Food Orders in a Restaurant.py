from typing import List


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        restaurant = {}
        foods = []
        tables = []
        for customer, table, food in orders:
            foods.append(food)
            tables.append(int(table))
            if food not in foods:
                foods[food] = 1
            if table not in restaurant:
                restaurant[table] = {}
            if food not in restaurant[table]:
                restaurant[table][food] = 1
            else:
                restaurant[table][food] += 1
        tables.sort()
        tables_map = {}
        index = 1
        for table in tables:
            if table not in tables_map:
                tables_map[table] = index
                index += 1
        foods.sort()
        foods_map = {}
        index = 1
        for food in foods:
            if food not in foods_map:
                foods_map[food] = index
                index += 1
        ans = [['0'] * (len(foods_map) + 1) for _ in range(len(restaurant) + 1)]
        ans[0][0] = "Table"
        for food in foods_map:
            ans[0][foods_map[food]] = food

        for table in tables:
            ans[tables_map[table]][0] = str(table)

        for table in restaurant:
            for food in restaurant[table]:
                ans[tables_map[int(table)]][foods_map[food]] = str(restaurant[table][food])
        return ans
