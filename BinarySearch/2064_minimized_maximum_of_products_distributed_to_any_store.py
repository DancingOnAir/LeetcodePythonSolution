from typing import List


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left, right = 1, max(quantities)
        while left <= right:
            mid = left + (right - left) // 2
            if sum((x - 1) // mid + 1 for x in quantities) > n:
                left = mid + 1
            else:
                right = mid - 1

        return left


def test_minimized_maximum():
    solution = Solution()
    assert solution.minimizedMaximum(1, [1]) == 1, 'wrong result'
    assert solution.minimizedMaximum(6, [11, 6]) == 3, 'wrong result'
    assert solution.minimizedMaximum(7, [15, 10, 10]) == 5, 'wrong result'


if __name__ == '__main__':
    test_minimized_maximum()
