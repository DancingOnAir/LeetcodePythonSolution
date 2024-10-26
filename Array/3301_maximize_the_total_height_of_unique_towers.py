from typing import List


class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        for i in range(1, len(maximumHeight)):
            maximumHeight[i] = min(maximumHeight[i], maximumHeight[i - 1] - 1)
            if maximumHeight[i] == 0:
                return -1
        return sum(maximumHeight)


def test_maximum_total_sum():
    solution = Solution()
    assert solution.maximumTotalSum([2, 3, 4, 3]) == 10, 'wrong result'
    assert solution.maximumTotalSum([15, 10]) == 25, 'wrong result'
    assert solution.maximumTotalSum([2, 2, 1]) == -1, 'wrong result'


if __name__ == '__main__':
    test_maximum_total_sum()
