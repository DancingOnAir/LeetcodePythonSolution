class Solution:
    # binary search
    def pivotInteger(self, n: int) -> int:
        total = (1 + n) * n // 2
        lo, hi = 1, n
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            left_sum = (mid - 1) * mid // 2
            right_sum = total - left_sum - mid
            if left_sum == right_sum:
                return mid
            elif left_sum < right_sum:
                lo = mid + 1
            elif left_sum > right_sum:
                hi = mid - 1
        return -1

    # linear search
    def pivotInteger2(self, n: int) -> int:
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
    assert solution.pivotInteger(49) == 35, 'wrong result'
    assert solution.pivotInteger(8) == 6, 'wrong result'
    assert solution.pivotInteger(1) == 1, 'wrong result'
    assert solution.pivotInteger(4) == -1, 'wrong result'


if __name__ == '__main__':
    test_pivot_integer()
