class Solution:
    def pivotInteger(self, n: int) -> int:
        total = (1 + n) * n // 2
        for x in range(max(1, n // 2), n + 1):
            pre = (1 + x) * x // 2
            if 2 * pre == total + x:
                return x
        return -1


def test_pivot_integer():
    solution = Solution()
    assert solution.pivotInteger(8) == 6, 'wrong result'
    assert solution.pivotInteger(1) == 1, 'wrong result'
    assert solution.pivotInteger(4) == -1, 'wrong result'


if __name__ == '__main__':
    test_pivot_integer()
