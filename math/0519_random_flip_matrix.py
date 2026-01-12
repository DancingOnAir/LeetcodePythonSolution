from typing import List
from random import randint


class Solution:
    def __init__(self, m: int, n: int):
        self.col = m - 1
        self.row = n - 1
        self.ones = set()

    def flip(self) -> List[int]:
        i = randint(0, self.col)
        j = randint(0, self.row)
        if (i, j) not in self.ones:
            self.ones.add((i, j))
            return [i, j]
        return self.flip()

    def reset(self) -> None:
        self.ones.clear()


def test_solution():
    obj = Solution(3, 1)
    assert obj.flip() in ([1, 0], [2, 0], [0, 0]), 'wrong result'
    obj.reset()


if __name__ == '__main__':
    test_solution()
