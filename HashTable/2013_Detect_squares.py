from typing import List
from collections import defaultdict


class DetectSquares:
    def __init__(self):
        self.coordinates = defaultdict(int)
        self.xs = defaultdict(set)
        self.ys = defaultdict(set)

    def add(self, point: List[int]) -> None:
        p = tuple(point)
        self.coordinates[p] += 1
        self.xs[point[0]].add(p)
        self.ys[point[1]].add(p)

    def count(self, point: List[int]) -> int:
        res = 0
        for p in self.xs[point[0]]:
            for q in self.ys[point[1]]:
                r = (q[0], p[1])
                if r in self.coordinates and abs(p[1] - point[1]) == abs(q[0] - point[0]):
                    res += self.coordinates[p] * self.coordinates[q] * self.coordinates[r]
        return res


def test_detect_squares():
    obj = DetectSquares()
    obj.add([3, 10])
    obj.add([11, 2])
    obj.add([3, 2])
    assert obj.count([11, 10]) == 1, 'wrong result'
    assert obj.count([14, 8]) == 0, 'wrong result'

    obj.add([11, 2])
    assert obj.count([11, 10]) == 2, 'wrong result'


if __name__ == '__main__':
    test_detect_squares()
