from math import sqrt, ceil


class Solution:
    def twoEggDrop(self, n: int) -> int:
        return ceil(sqrt(2 * n - 0.25) - 0.5)


def test_two_egg_drop():
    solution = Solution()
    assert solution.twoEggDrop(2) == 2, 'wrong result'
    assert solution.twoEggDrop(100) == 14, 'wrong result'


if __name__ == '__main__':
    test_two_egg_drop()
