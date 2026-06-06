class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        return sum(map(int, str(n)))


def test_digit_frequency_score():
    solution = Solution()
    assert solution.digitFrequencyScore(122) == 5, 'wrong result'
    assert solution.digitFrequencyScore(101) == 2, 'wrong result'


if __name__ == '__main_':
    test_digit_frequency_score()
