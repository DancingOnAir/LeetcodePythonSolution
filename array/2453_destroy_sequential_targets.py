from typing import List
from collections import Counter


class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        c = Counter(x % space for x in nums)
        max_c = max(c.values())
        return min(x for x in nums if c[x % space] == max_c)


def test_destroy_targets():
    solution = Solution()
    assert solution.destroyTargets([3, 7, 8, 1, 1, 5], 2) == 1, 'wrong result'
    assert solution.destroyTargets([1, 3, 5, 2, 4, 6], 2) == 1, 'wrong result'
    assert solution.destroyTargets([6, 2, 5], 100) == 2, 'wrong result'


if __name__ == '__main__':
    test_destroy_targets()
