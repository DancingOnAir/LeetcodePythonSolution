from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        res, total = -1, sum(nums)
        for x in sorted(nums, reverse=True):
            if 2 * x < total:
                return total
            total -= x
        return -1


def test_largest_perimeter():
    solution = Solution()
    assert solution.largestPerimeter([5, 5, 5]) == 15, 'wrong result'
    assert solution.largestPerimeter([1, 12, 1, 2, 5, 50, 3]) == 12, 'wrong result'
    assert solution.largestPerimeter([5, 5, 50]) == -1, 'wrong result'


if __name__ == '__main__':
    test_largest_perimeter()
