class Solution:
    def pivotInteger(self, n: int) -> int:
        right_sum = (1 + n) * n // 2
        left_sum = 0
        for i in range(1, n + 1):
            right_sum -= i
            if left_sum == right_sum:
                return i
            left_sum += i
        return -1

    def pivotInteger1(self, n: int) -> int:
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
