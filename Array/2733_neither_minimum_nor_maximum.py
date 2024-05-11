from typing import List


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        return sorted(nums)[1]


def test_find_non_min_or_max():
    solution = Solution()
    assert solution.findNonMinOrMax([3, 2, 1, 4]) == 2, 'wrong result'
    assert solution.findNonMinOrMax([1, 2]) == -1, 'wrong result'
    assert solution.findNonMinOrMax([2, 1, 3]) == 2, 'wrong result'


if __name__ == '__main__':
    test_find_non_min_or_max()
