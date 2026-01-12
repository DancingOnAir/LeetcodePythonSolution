from typing import List
from collections import Counter


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(k for k, v in Counter(nums).items() if v == 1)


def test_sum_of_unique():
    solution = Solution()

    assert solution.sumOfUnique([1, 2, 3, 2]) == 4, 'wrong result'
    assert solution.sumOfUnique([1, 1, 1, 1, 1]) == 0, 'wrong result'
    assert solution.sumOfUnique([1, 2, 3, 4, 5]) == 15, 'wrong result'


if __name__ == '__main__':
    test_sum_of_unique()

