from typing import List
from collections import defaultdict, Counter


class DetectSquares:
    def __init__(self):
        # self.coordinates = defaultdict(int)
        self.coordinates = Counter()

    def add(self, point: List[int]) -> None:
        self.coordinates[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        x1, y1 = point
        for (x3, y3), cnt in self.coordinates.items():
            if x1 != x3 and abs(x1 - x3) == abs(y1 - y3):
                # Counter won't add new keys to the dict when you query for missing keys.
                res += self.coordinates[(x1, y3)] * self.coordinates[(x3, y1)] * cnt
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
