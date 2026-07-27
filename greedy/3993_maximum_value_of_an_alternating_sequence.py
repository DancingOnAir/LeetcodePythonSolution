class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        if n < 2:
            return s
        return s + m + (m - 1) * (n // 2 - 1)


def test_maximum_value():
    solution = Solution()
    assert solution.maximumValue(4, 3, 5) == 12, 'wrong result'
    assert solution.maximumValue(2, 4, 3) == 7, 'wrong result'


if __name__ == '__main__':
    test_maximum_value()
