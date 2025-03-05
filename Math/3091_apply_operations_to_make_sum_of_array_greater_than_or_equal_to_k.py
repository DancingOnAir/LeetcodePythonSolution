from math import isqrt


class Solution:
    def minOperations(self, k: int) -> int:
        i = isqrt(k)
        return i + (k - 1) // i - 1


def test_min_operations():
    solution = Solution()
    assert solution.minOperations(11) == 5, 'wrong result'
    assert solution.minOperations(1) == 0, 'wrong result'


if __name__ == '__main__':
    test_min_operations()
