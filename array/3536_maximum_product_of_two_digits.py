class Solution:
    def maxProduct(self, n: int) -> int:
        d1, d2 = sorted(str(n))[-2:]
        return int(d1) * int(d2)

    def maxProduct1(self, n: int) -> int:
        sorted_digits = sorted(list(map(int, str(n))))
        return sorted_digits[-1] * sorted_digits[-2]


def test_max_product():
    solution = Solution()
    assert solution.maxProduct(31) == 3, 'wrong result'
    assert solution.maxProduct(22) == 4, 'wrong result'
    assert solution.maxProduct(124) == 8, 'wrong result'


if __name__ == '__main__':
    test_max_product()

