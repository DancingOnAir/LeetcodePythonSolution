from math import pow


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        return (pow(5, n - n // 2, 10 ** 9 + 7) * pow(4, n // 2, 10 ** 9 + 7)) % (10 ** 9 + 7)


def test_count_good_numbers():
    solution = Solution()
    assert solution.countGoodNumbers(1) == 5, 'wrong result'
    assert solution.countGoodNumbers(4) == 400, 'wrong result'
    assert solution.countGoodNumbers(50) == 564908303, 'wrong result'


if __name__ == '__main__':
    test_count_good_numbers()
