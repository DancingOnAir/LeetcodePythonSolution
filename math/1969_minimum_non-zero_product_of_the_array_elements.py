from math import pow


class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        return pow(2 ** p - 2, 2 ** (p - 1) - 1, 10 ** 9 + 7) * (2 ** p - 1) % (10 ** 9 + 7)


def test_min_non_zero_product():
    solution = Solution()
    assert solution.minNonZeroProduct(1) == 1, 'wrong result'
    assert solution.minNonZeroProduct(2) == 6, 'wrong result'
    assert solution.minNonZeroProduct(3) == 1512, 'wrong result'


if __name__ == '__main__':
    test_min_non_zero_product()
