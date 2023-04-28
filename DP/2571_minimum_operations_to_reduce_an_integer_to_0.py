from itertools import groupby


class Solution:
    def minOperations(self, n: int) -> int:
        res = 1
        while n & (n - 1):
            low_bit = n & -n
            # 多个连续1
            if n & (low_bit << 1):
                n += low_bit
            else:
                n -= low_bit
            res += 1
        return res


def test_min_operations():
    solution = Solution()
    assert solution.minOperations(39) == 3, 'wrong result'
    assert solution.minOperations(54) == 3, 'wrong result'


if __name__ == '__main__':
    test_min_operations()
