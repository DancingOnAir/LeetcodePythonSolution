from math import pow


class Solution:
    def stringCount(self, n: int) -> int:
        mod = 10 ** 9 + 7
        return (pow(26, n, mod) - pow(25, n - 1, mod) * (75 + n) + pow(24, n - 1) * (72 + n * 2) - pow(23, n - 1, mod) * (23 + n)) % mod


def test_string_count():
    solution = Solution()
    assert solution.stringCount(4) == 12, 'wrong result'
    assert solution.stringCount(10) == 83943898, 'wrong result'


if __name__ == '__main__':
    test_string_count()
