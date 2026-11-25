class Solution:
    def minRange(self, a: int, b: int, c: int) -> int:
        a, b, c = sorted((a, b, c))
        return min(c - a, b)


def test_min_range():
    solution = Solution()
    assert solution.minRange(9, 2, 5) == 5, 'wrong result'
    assert solution.minRange(5, 7, 6) == 2, 'wrong result'
    assert solution.minRange(3, 3, 3) == 0, 'wrong result'


if __name__ == '__main__':
    test_min_range()
