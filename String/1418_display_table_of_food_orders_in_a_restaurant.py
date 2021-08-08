from typing import List
from collections import defaultdict, Counter


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        tables = defaultdict(Counter)
        meal = set()

        for _, tbl_num, food in orders:
            meal.add(food)
            tables[tbl_num][food] += 1
        foods = sorted(meal)
        res = [["Table"] + foods]

        for tbl_num in sorted(tables, key=int):
            res.append([tbl_num] + [str(tables[tbl_num][food]) for food in foods])
        return res

    # defaultdict of defaultdict + set
    def displayTable1(self, orders: List[List[str]]) -> List[List[str]]:
        title = set()
        items = defaultdict(lambda: defaultdict(int))

        for i in range(len(orders)):
            title.add(orders[i][2])
            items[orders[i][1]][orders[i][2]] += 1

        res = list()
        title = sorted(title)
        res.append(["Table"] + title)

        for tbl_num, v in sorted(items.items(), key=lambda x: int(x[0])):
            cur_table = [tbl_num]
            for item_name in title:
                if item_name in v:
                    cur_table.append(str(v[item_name]))
                else:
                    cur_table.append("0")
            res.append(cur_table)

        return res


def test_display_table():
    solution = Solution()

    assert solution.displayTable(
        [["David", "3", "Ceviche"], ["Corina", "10", "Beef Burrito"], ["David", "3", "Fried Chicken"],
         ["Carla", "5", "Water"], ["Carla", "5", "Ceviche"], ["Rous", "3", "Ceviche"]]) == [
               ["Table", "Beef Burrito", "Ceviche", "Fried Chicken", "Water"], ["3", "0", "2", "1", "0"],
               ["5", "0", "1", "0", "1"], ["10", "1", "0", "0", "0"]], 'wrong result'
    assert solution.displayTable(
        [["James", "12", "Fried Chicken"], ["Ratesh", "12", "Fried Chicken"], ["Amadeus", "12", "Fried Chicken"],
         ["Adam", "1", "Canadian Waffles"], ["Brianna", "1", "Canadian Waffles"]]) == [
               ["Table", "Canadian Waffles", "Fried Chicken"], ["1", "2", "0"], ["12", "0", "3"]], 'wrong result'
    assert solution.displayTable(
        [["Laura", "2", "Bean Burrito"], ["Jhon", "2", "Beef Burrito"], ["Melissa", "2", "Soda"]]) == [
               ["Table", "Bean Burrito", "Beef Burrito", "Soda"], ["2", "1", "1", "1"]], 'wrong result'


if __name__ == '__main__':
    test_display_table()
