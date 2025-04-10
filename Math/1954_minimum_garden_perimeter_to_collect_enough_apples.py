from math import ceil, sqrt


class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        n = int((neededApples / 4) ** (1/3))
        if 2 * n * (n + 1) * (2 * n + 1) < neededApples:
            n += 1
        return n * 8


def test_minimum_perimeter():
    solution = Solution()
    assert solution.minimumPerimeter(1) == 8, 'wrong result'
    assert solution.minimumPerimeter(13) == 16, 'wrong result'
    assert solution.minimumPerimeter(1000000000) == 5040, 'wrong result'


if __name__ == '__main__':
    test_minimum_perimeter()
