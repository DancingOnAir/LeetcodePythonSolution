class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left, right = 1, maxSum
        while left <= right:
            mid = left + (right - left) // 2
            cur = 0
            # 计算1 ... 1 ... mid
            if mid <= index + 1:
                cur = (1 + mid) * mid // 2
                cur += index + 1 - mid
            else:
                cur += (mid - index + mid) * (1 + index) // 2
            # 计算mid - 1 ... 1 ... 1
            if mid - 1 <= n - index - 1:
                cur += (mid - 1) * mid // 2
                cur += n - index - mid
            else:
                cur += (mid - 1 - n + index + 1 + 1 + mid - 1) * (n - index - 1) // 2

            if cur > maxSum:
                right = mid - 1
            else:
                left = mid + 1
        return left - 1


def test_max_value():
    solution = Solution()
    assert solution.maxValue(9, 3, 16) == 3, 'wrong result'
    assert solution.maxValue(4, 2, 6) == 2, 'wrong result'
    assert solution.maxValue(6, 1, 10) == 3, 'wrong result'


if __name__ == '__main__':
    test_max_value()
