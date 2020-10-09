from typing import List
import numpy as np


class SubrectangleQueries1:
    def __init__(self, rectangle: List[List[int]]):
        self._rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1, row2 + 1):
            self._rectangle[i][col1: col2 + 1] = [newValue] * (col2 - col1 + 1)

    def getValue(self, row: int, col: int) -> int:
        return self._rectangle[row][col]


class SubrectangleQueries:
    def __init__(self, rectangle: List[List[int]]):
        self._rectangle = np.array(rectangle, dtype='int64')

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self._rectangle[row1:row2+1, col1:col2+1] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self._rectangle[row, col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
def test_subrectangle_queries():
    rectangle1 = [[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]]
    obj1 = SubrectangleQueries(rectangle1)
    print(obj1.getValue(0, 2))
    obj1.updateSubrectangle(0, 0, 3, 2, 5)
    print(obj1.getValue(0, 2))
    print(obj1.getValue(3, 1))
    obj1.updateSubrectangle(3, 0, 3, 2, 10)
    print(obj1.getValue(3, 1))
    print(obj1.getValue(0, 2))

    print('-' * 10)

    rectangle2 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
    obj2 = SubrectangleQueries(rectangle2)
    print(obj2.getValue(0, 0))
    obj2.updateSubrectangle(0, 0, 2, 2, 100)
    print(obj2.getValue(0, 0))
    print(obj2.getValue(2, 2))
    obj2.updateSubrectangle(1, 1, 2, 2, 20)
    print(obj2.getValue(2, 2))


if __name__ == '__main__':
    test_subrectangle_queries()
