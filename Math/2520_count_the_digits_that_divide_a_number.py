class Solution:
    def countDigits(self, num: int) -> int:
        return sum(num % int(x) == 0 for x in str(num))


def test_count_digits():
    solution = Solution()
    assert solution.countDigits(7) == 1, 'wrong result'
    assert solution.countDigits(121) == 2, 'wrong result'
    assert solution.countDigits(1248) == 4, 'wrong result'


if __name__ == '__main__':
    test_count_digits()
