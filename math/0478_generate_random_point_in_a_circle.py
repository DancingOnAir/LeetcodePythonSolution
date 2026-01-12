from typing import List
from random import uniform
from math import pi, sin, cos, sqrt


class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        theta = uniform(0, 2 * pi)
        R = self.r * sqrt(uniform(0, 1))
        return [self.x + R * cos(theta), self.y + R * sin(theta)]


def test_random_point():
    solution = Solution(1.0, 0.0, 0.0)
    x, y = solution.randPoint()
    assert -1.0 <= x <= 1.0, 'wrong result'
    assert -1.0 <= y <= 1.0, 'wrong result'
    assert x * x + y * y <= 1.0, 'wrong result'


if __name__ == '__main__':
    test_random_point()
