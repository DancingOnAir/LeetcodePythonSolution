class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        return min(a + b + c - max([a, b, c]), (a + b + c) // 2)

    def maximumScore1(self, a: int, b: int, c: int) -> int:
        a, b, c = sorted([a, b, c])
        if a + b <= c:
            return a + b
        return c + (a + b - c) // 2


def test_maximum_score():
    solution = Solution()
    assert solution.maximumScore(2, 4, 6) == 6, 'wrong result'
    assert solution.maximumScore(4, 4, 6) == 7, 'wrong result'
    assert solution.maximumScore(1, 8, 8) == 8, 'wrong result'


if __name__ == '__main__':
    test_maximum_score()
