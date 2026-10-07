from itertools import pairwise
from collections import defaultdict


class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        cnt = defaultdict(int)
        base = 0
        for x, y in pairwise(nums):
            if x == y:
                base += 1
            else:
                if x > y:
                    x, y = y, x
                cnt[(x, y)] += 1
        return base + max(cnt.values(), default=0)


def test_max_equal_adjacent_pairs():
    solution = Solution()
    assert solution.maxEqualAdjacentPairs([1, 2, 3, 2]) == 2, 'wrong result'
    assert solution.maxEqualAdjacentPairs([1, 2, 1, 2, 1]) == 4, 'wrong result'
    assert solution.maxEqualAdjacentPairs([1, 1, 1]) == 2, 'wrong result'


if __name__ == '__main__':
    test_max_equal_adjacent_pairs()
