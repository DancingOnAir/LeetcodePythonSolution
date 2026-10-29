class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        x, y = a.bit_count(), b.bit_count()
        if x >= y:
            return x * y
        return y // x


def test_calculate_score():
    solution = Solution()
    assert solution.calculateScore(14, 6) == 6, 'wrong result'
    assert solution.calculateScore(5, 15) == 2, 'wrong result'
    assert solution.calculateScore(10, 12) == 4, 'wrong result'


if __name__ == '__main__':
    test_calculate_score()
